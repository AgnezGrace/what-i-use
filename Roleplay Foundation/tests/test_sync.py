import shutil
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from sync_catalog import plan, apply, json_text, block, START, END
from validate import read_json, validate_root, lookup


class SyncTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name) / 'roleplay'
        def ignore(folder, names):
            if Path(folder) == ROOT:
                return set(names) - {'README.md', 'SKILL.md', 'ROLEPLAY_ROUTER.md', 'core', 'catalog', 'adapters', 'assets', 'scripts', 'tests'}
            if Path(folder) == ROOT / 'adapters':
                return set(names) - {'README.md', 'index.json', 'universal-prompt.md'}
            return {'__pycache__'} & set(names)
        shutil.copytree(ROOT, self.root, ignore=ignore)
        self.put('catalog/index.json', {'schema_version': 1, 'modules': []})
        self.put('adapters/index.json', {'schema_version': 1, 'platforms': []})
        apply(plan(self.root))

    def put(self, path, content):
        dest = self.root / path
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(content if isinstance(content, str) else json_text(content), encoding='utf-8')

    def category(self, name='attention', status='reviewed'):
        self.put(f'{name}/SKILL.md', f'---\nname: {name}\ndescription: Fixture only.\n---\n')
        self.put(f'{name}/README.md', 'Manual description.\n')
        self.put(f'{name}/module.json', {'title': 'Fixture', 'kind': 'trait', 'aliases': ['perhatian'], 'status': status})
        self.put(f'{name}/manifestations/practical/GUIDE.md', 'Fixture behavior.')
        self.put(f'{name}/manifestations/practical/manifestation.json', {'aliases': ['tindakan'], 'status': 'reviewed'})

    def adapter(self, date='2026-01-01'):
        self.put('adapters/sample.md', 'Fixture mapping.')
        self.put('adapters/sample.adapter.json', {'title': 'Fixture platform', 'evidence_date': date, 'status': 'reviewed'})

    def test_add_and_idempotence(self):
        self.category(); self.adapter()
        router = (self.root/'ROLEPLAY_ROUTER.md').read_bytes()
        changes = plan(self.root)
        self.assertEqual(len(changes), 5)
        self.assertEqual(read_json(self.root/'catalog/index.json')['modules'], [])
        apply(changes)
        self.assertEqual(plan(self.root), {})
        validate_root(self.root)
        index = read_json(self.root/'catalog/index.json')
        self.assertEqual(lookup(index, 'TINDAKAN')[0]['manifestation'], 'practical')
        self.assertIn('Manual description.', (self.root/'attention/README.md').read_text())
        self.assertEqual(router, (self.root/'ROLEPLAY_ROUTER.md').read_bytes())

    def test_draft_excluded(self):
        self.category(status='draft')
        apply(plan(self.root))
        self.assertEqual(read_json(self.root/'catalog/index.json')['modules'], [])
        self.assertEqual(plan(self.root), {})

    def test_draft_manifestation_excluded(self):
        self.category()
        self.put('attention/manifestations/practical/manifestation.json', {'aliases': [], 'status': 'draft'})
        apply(plan(self.root))
        self.assertEqual(read_json(self.root/'catalog/index.json')['modules'][0]['manifestations'], [])

    def test_removal_guard(self):
        self.category(); apply(plan(self.root))
        (self.root/'attention/module.json').unlink()
        with self.assertRaises(ValueError): plan(self.root)
        apply(plan(self.root, allow_remove=True))
        self.assertEqual(read_json(self.root/'catalog/index.json')['modules'], [])
        self.assertIn('not registered', (self.root/'attention/README.md').read_text())

    def test_missing_guide_preflight(self):
        self.category(); (self.root/'attention/manifestations/practical/GUIDE.md').unlink()
        before = (self.root/'README.md').read_bytes()
        with self.assertRaises(ValueError): plan(self.root)
        self.assertEqual(before, (self.root/'README.md').read_bytes())

    def test_bad_adapter(self):
        self.adapter('2026-02-31')
        with self.assertRaises(ValueError): plan(self.root)

    def test_ambiguous_alias(self):
        self.category('one'); self.category('two'); apply(plan(self.root))
        self.assertEqual(len(lookup(read_json(self.root/'catalog/index.json'), 'perhatian')), 2)

    def test_managed_block(self):
        source = f'Before\n{START}\nold\n{END}\nAfter\n'
        self.assertEqual(block(source, 'new'), f'Before\n{START}\nnew\n{END}\nAfter\n')
        with self.assertRaises(ValueError): block(START, 'new')

    def test_symlink_rejected(self):
        self.category()
        path = self.root/'attention/manifestations/practical/GUIDE.md'
        path.unlink(); path.symlink_to(self.root/'SKILL.md')
        with self.assertRaises(ValueError): plan(self.root)

    def test_drift_repaired(self):
        self.category(); apply(plan(self.root))
        path = self.root/'README.md'
        path.write_text(path.read_text().replace('1 manifestations','99 manifestations'))
        self.assertEqual(set(plan(self.root)), {path})
        apply(plan(self.root)); self.assertFalse(plan(self.root))

    def test_sorting(self):
        self.category('zeta'); self.category('alpha'); apply(plan(self.root))
        self.assertEqual([x['id'] for x in read_json(self.root/'catalog/index.json')['modules']], ['alpha','zeta'])


if __name__ == '__main__':
    unittest.main()
