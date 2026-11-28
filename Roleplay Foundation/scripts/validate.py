"""Offline structural validator. No semantic or model-behavior claims."""
import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ID = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")
KINDS = {"trait", "emotion", "motive", "behavior", "temperament", "mixed"}


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def safe_file(root, value):
    if not isinstance(value, str) or not value or "\\" in value:
        raise ValueError("invalid relative path")
    p = Path(value)
    if p.is_absolute() or ".." in p.parts:
        raise ValueError("path escapes root")
    resolved = (root / p).resolve()
    if not resolved.is_relative_to(root.resolve()) or not resolved.is_file():
        raise ValueError(f"missing or unsafe file: {value}")
    return resolved


def ident(value):
    return isinstance(value, str) and bool(ID.fullmatch(value))


def labels(value):
    return isinstance(value, list) and all(isinstance(x, str) and x.strip() for x in value)


def check_entry(path, expected):
    source = path.read_text(encoding="utf-8")
    match = re.match(r"---\n(.*?)\n---\n", source, re.S)
    if not match or not re.search(rf"^name: {re.escape(expected)}$", match[1], re.M):
        raise ValueError(f"invalid skill name: {path.name}")
    if not re.search(r"^description: \S.+$", match[1], re.M):
        raise ValueError("missing description")


def validate_catalog(root, index):
    if type(index.get("schema_version")) is not int or index["schema_version"] != 1 or not isinstance(index.get("modules"), list):
        raise ValueError("invalid catalog envelope")
    seen = set()
    for m in index["modules"]:
        key = m["id"]
        if not ident(key) or key in seen or key in {"core", "catalog", "adapters", "assets", "scripts", "tests"}:
            raise ValueError(f"invalid/duplicate category: {key}")
        seen.add(key)
        if m["kind"] not in KINDS or not labels(m["aliases"]) or not isinstance(m["title"], str) or not m["title"].strip():
            raise ValueError("invalid module metadata")
        if m["entry"] != f"{key}/SKILL.md":
            raise ValueError("entry must be category SKILL.md")
        check_entry(safe_file(root, m["entry"]), key)
        paths, ids = set(), set()
        if not isinstance(m["manifestations"], list):
            raise ValueError("manifestations must be an array")
        for sub in m["manifestations"]:
            sid, path = sub["id"], sub["path"]
            if not ident(sid) or sid in ids or path in paths or not labels(sub["aliases"]):
                raise ValueError("invalid/duplicate manifestation")
            if path != f"{key}/manifestations/{sid}/GUIDE.md":
                raise ValueError("invalid manifestation path")
            safe_file(root, path)
            ids.add(sid)
            paths.add(path)


def lookup(index, query):
    """Exact casefold label lookup; retain ambiguity, no fuzzy guesses."""
    q = query.strip().casefold()
    matches = []
    for m in index["modules"]:
        if q in {s.strip().casefold() for s in [m["id"], *m["aliases"]]}:
            matches.append({"category": m["id"], "path": m["entry"]})
        for sub in m["manifestations"]:
            if q in {s.strip().casefold() for s in [sub["id"], *sub["aliases"]]}:
                matches.append({"category": m["id"], "manifestation": sub["id"], "path": sub["path"]})
    return matches


def validate_adapters(root, index):
    if type(index.get("schema_version")) is not int or index["schema_version"] != 1 or not isinstance(index.get("platforms"), list):
        raise ValueError("invalid adapter envelope")
    ids, paths = set(), set()
    for p in index["platforms"]:
        if not ident(p["id"]) or p["id"] in ids or p["path"] in paths:
            raise ValueError("invalid/duplicate adapter")
        if p["path"] != f'adapters/{p["id"]}.md':
            raise ValueError("invalid adapter path")
        if not p["title"].strip() or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", p["evidence_date"]):
            raise ValueError("missing adapter evidence metadata")
        from datetime import date
        date.fromisoformat(p["evidence_date"])
        safe_file(root, p["path"])
        ids.add(p["id"])
        paths.add(p["path"])


def check_profile(value, schema, root_schema=None, where="profile"):
    """Validate the schema's limited vocabulary; fail on unknown keywords."""
    root_schema = schema if root_schema is None else root_schema
    allowed = {"$schema", "$defs", "$ref", "title", "type", "required", "additionalProperties", "properties", "items", "const", "minLength"}
    if set(schema) - allowed:
        raise ValueError(f"unsupported schema keyword at {where}")
    if "$ref" in schema:
        ref = schema["$ref"]
        if not ref.startswith("#/$defs/"):
            raise ValueError("unsupported reference")
        return check_profile(value, root_schema["$defs"][ref.split("/")[-1]], root_schema, where)
    if "const" in schema and (type(value) is not type(schema["const"]) or value != schema["const"]):
        raise ValueError(f"wrong constant at {where}")
    types = {"object": dict, "array": list, "string": str}
    typ = schema.get("type")
    if typ is not None and (typ not in types or not isinstance(value, types[typ])):
        raise ValueError(f"wrong type at {where}")
    if typ == "object":
        if set(schema.get("required", [])) - set(value):
            raise ValueError(f"missing fields at {where}")
        props = schema.get("properties", {})
        if schema.get("additionalProperties") is False and set(value) - set(props):
            raise ValueError(f"unexpected fields at {where}")
        for key in set(value) & set(props):
            check_profile(value[key], props[key], root_schema, f"{where}.{key}")
    if typ == "array":
        for i, item in enumerate(value):
            check_profile(item, schema["items"], root_schema, f"{where}[{i}]")
    if typ == "string" and len(value) < schema.get("minLength", 0):
        raise ValueError(f"string too short at {where}")


def validate_root(root):
    for name in ["README.md", "ROLEPLAY_ROUTER.md", "core/identity.md", "core/manifestation.md", "core/relationships.md", "core/composition.md", "core/continuity.md", "core/boundaries.md", "core/dialogue.md", "core/module-contract.md", "core/evaluation.md", "adapters/README.md", "adapters/universal-prompt.md", "assets/module-template.md", "assets/adapter-template.md", "assets/profile-template.md", "assets/character-schema.json"]:
        safe_file(root, name)
    check_entry(safe_file(root, "SKILL.md"), "roleplay")
    validate_catalog(root, read_json(root / "catalog/index.json"))
    validate_adapters(root, read_json(root / "adapters/index.json"))
    for path in root.rglob("*.md"):
        for target in re.findall(r"\]\(([^)]+)\)", path.read_text(encoding="utf-8")):
            if "://" in target or target.startswith("#"):
                continue
            resolved = (path.parent / target.split("#")[0]).resolve()
            if not resolved.is_relative_to(root.resolve()) or not resolved.is_file():
                raise ValueError(f"broken local link: {path.name} -> {target}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lookup", help="exact trait or manifestation label")
    parser.add_argument("--profile", type=Path, help="portable profile JSON")
    args = parser.parse_args()
    try:
        validate_root(ROOT)
        if args.profile:
            check_profile(read_json(args.profile), read_json(ROOT / "assets/character-schema.json"))
        if args.lookup is not None:
            matches = lookup(read_json(ROOT / "catalog/index.json"), args.lookup)
            print(json.dumps({"status": "unlisted" if not matches else "unique" if len(matches) == 1 else "ambiguous", "matches": matches}, ensure_ascii=False))
        else:
            print("PASS: foundation structure, registry paths, local links" + (", profile" if args.profile else ""))
    except (ValueError, KeyError, TypeError, OSError) as exc:
        parser.exit(1, f"FAIL: {exc}\n")


if __name__ == "__main__":
    main()
