"""Rebuild derived catalog files from reviewed local metadata; no network."""
import argparse
import json
import os
import tempfile
from pathlib import Path
from validate import ROOT, ident, labels, read_json, safe_file, validate_catalog, validate_adapters

START = '<!-- catalog:begin -->'
END = '<!-- catalog:end -->'
RESERVED = {'core', 'catalog', 'adapters', 'assets', 'scripts', 'tests'}


def safe_path(root, path):
    relative = path.relative_to(root)
    current = root
    for part in relative.parts:
        current = current / part
        if current.is_symlink():
            raise ValueError(f'symlink not allowed: {relative}')
    return path


def metadata(root, path, keys):
    data = read_json(safe_path(root, path))
    if not isinstance(data, dict) or set(data) != set(keys) | {'status'}:
        raise ValueError(f'invalid metadata fields: {path}')
    if data['status'] not in ('draft', 'reviewed'):
        raise ValueError(f'invalid review status: {path}')
    return data


def block(source, body):
    generated = START + '\n' + body.rstrip() + '\n' + END
    if START not in source and END not in source:
        return source.rstrip('\n') + '\n\n' + generated + '\n'
    if source.count(START) != 1 or source.count(END) != 1 or source.index(START) > source.index(END):
        raise ValueError('malformed managed block')
    a = source.index(START)
    b = source.index(END) + len(END)
    return source[:a] + generated + source[b:]


def json_text(obj):
    return json.dumps(obj, ensure_ascii=False, indent=2) + '\n'


def plan(root, allow_remove=False):
    root = root.resolve()
    modules, platforms, changes = [], [], {}

    def managed(path, body):
        safe_path(root, path)
        source = path.read_text(encoding='utf-8')
        changes[path] = block(source, body)

    for folder in sorted(root.iterdir()):
        if folder.name in RESERVED or not (folder / 'module.json').exists():
            continue
        safe_path(root, folder)
        key = folder.name
        if not ident(key):
            raise ValueError(f'invalid category: {key}')
        m = metadata(root, folder / 'module.json', ['title', 'kind', 'aliases'])
        if m['status'] == 'draft':
            if (folder / 'README.md').exists():
                managed(folder / 'README.md', 'No reviewed manifestations in this draft category.')
            continue
        subs = []
        base = folder / 'manifestations'
        safe_path(root, base)
        for sub in sorted(base.iterdir()) if base.is_dir() else []:
            if not (sub / 'manifestation.json').exists():
                continue
            item = metadata(root, sub / 'manifestation.json', ['aliases'])
            if item['status'] == 'draft':
                continue
            path = sub / 'GUIDE.md'
            safe_path(root, path)
            subs.append({'id': sub.name, 'aliases': item['aliases'], 'path': path.relative_to(root).as_posix()})
        safe_path(root, folder / 'SKILL.md')
        modules.append({'id': key, 'title': m['title'], 'aliases': m['aliases'], 'kind': m['kind'], 'entry': f'{key}/SKILL.md', 'manifestations': subs})
        managed(folder / 'README.md', '### Reviewed manifestations\n\n' + ('\n'.join(f'- [{s["id"]}](manifestations/{s["id"]}/GUIDE.md)' for s in subs) or 'None yet.'))
    for path in sorted((root / 'adapters').glob('*.adapter.json')):
        item = metadata(root, path, ['title', 'evidence_date'])
        if item['status'] == 'draft':
            continue
        key = path.name.removesuffix('.adapter.json')
        safe_path(root, root / 'adapters' / f'{key}.md')
        platforms.append({'id': key, 'title': item['title'], 'path': f'adapters/{key}.md', 'evidence_date': item['evidence_date']})
    catalog = {'schema_version': 1, 'modules': modules}
    adapters = {'schema_version': 1, 'platforms': platforms}
    validate_catalog(root, catalog)
    validate_adapters(root, adapters)
    for relative, value, group in [('catalog/index.json', catalog, 'modules'), ('adapters/index.json', adapters, 'platforms')]:
        path = safe_path(root, root / relative)
        if path.exists():
            old = read_json(path)
            def keys(entries):
                result = {e['id'] for e in entries}
                result.update(f'{e["id"]}/{s["id"]}' for e in entries for s in e.get('manifestations', []))
                return result
            removed = keys(old[group]) - keys(value[group])
            if removed and not allow_remove:
                raise ValueError(f'removal requires --allow-remove: {sorted(removed)}')
            if group == 'modules' and allow_remove:
                for key in removed:
                    if '/' in key or not ident(key) or key in RESERVED:
                        continue
                    readme = root / key / 'README.md'
                    if readme.exists() and readme not in changes:
                        managed(readme, 'This category is not registered.')
        changes[path] = json_text(value)
    managed(root / 'README.md', '### Reviewed character modules\n\n' + ('\n'.join(f'- [{m["id"]}]({m["id"]}/README.md) — {len(m["manifestations"])} manifestations' for m in modules) or 'No registered categories yet.'))
    managed(root / 'adapters/README.md', '### Reviewed platform mappings\n\n' + ('\n'.join(f'- [{p["id"]}]({p["id"]}.md) — evidence {p["evidence_date"]}' for p in platforms) or 'No registered platform adapters yet.'))
    return {p: v for p, v in changes.items() if not p.exists() or p.read_text(encoding='utf-8') != v}


def apply(changes):
    # Stage all output before replacing any destination. Each replacement is atomic;
    # the batch is not a filesystem transaction. Re-run after an interrupted write.
    staged = []
    try:
        for path, value in changes.items():
            with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', dir=path.parent, delete=False) as f:
                staged.append((Path(f.name), path))
                f.write(value)
            if path.exists():
                os.chmod(f.name, path.stat().st_mode & 0o777)
        for tmp, path in staged:
            os.replace(tmp, path)
    finally:
        for tmp, _ in staged:
            tmp.unlink(missing_ok=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument('--write', action='store_true')
    mode.add_argument('--check', action='store_true', help='exit 1 when derived files drift')
    parser.add_argument('--allow-remove', action='store_true', help='authorize removal of registered entries')
    args = parser.parse_args()
    try:
        changes = plan(ROOT, args.allow_remove)
        for path in changes:
            print('UPDATE', path.relative_to(ROOT))
        if args.write:
            apply(changes)
        print(f'{len(changes)} file(s) {"updated" if args.write else "would change"}')
        return int(args.check and bool(changes))
    except (ValueError, KeyError, TypeError, OSError) as exc:
        parser.exit(2, f'FAIL: {exc}\n')


if __name__ == '__main__':
    raise SystemExit(main())
