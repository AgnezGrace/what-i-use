import copy
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from validate import validate_root, validate_catalog, validate_adapters, lookup, safe_file, check_profile, read_json


def fixture_profile():
    return {"schema_version": 1, "identity": {"name": "Fictional example", "canon": ["A cartographer"], "goals": ["Finish a map"], "knowledge_limits": []}, "tendencies": [{"trait": "curious", "motive": "Learn", "triggers": ["Unfamiliar map"], "channels": ["Ask specific questions"], "exceptions": ["Urgent task"], "anti_patterns": ["Invent answers"]}], "relationships": [], "voice": "Plain", "boundaries": [], "scene": {"current": "At work", "established_events": []}, "examples": [], "assumptions": []}


class FoundationTests(unittest.TestCase):
    def test_root(self):
        validate_root(ROOT)

    def test_empty_catalog(self):
        validate_catalog(ROOT, {"schema_version": 1, "modules": []})

    def test_empty_adapters(self):
        validate_adapters(ROOT, {"schema_version": 1, "platforms": []})

    def test_unknown_lookup(self):
        self.assertEqual(lookup({"modules": []}, "attention"), [])

    def test_safe_path(self):
        self.assertEqual(safe_file(ROOT, "SKILL.md"), ROOT / "SKILL.md")

    def test_traversal(self):
        for path in ["../SKILL.md", "/etc/passwd", "core\\identity.md", "missing.md"]:
            with self.subTest(path=path), self.assertRaises(ValueError):
                safe_file(ROOT, path)

    def test_profile_valid(self):
        check_profile(fixture_profile(), read_json(ROOT / "assets/character-schema.json"))

    def test_profile_invalid(self):
        schema = read_json(ROOT / "assets/character-schema.json")
        for mutation in [lambda p:p.pop("identity"), lambda p:p.update(schema_version=True), lambda p:p.update(unknown="x"), lambda p:p["identity"].update(name=""), lambda p:p["scene"].update(established_events="bad"), lambda p:p["tendencies"][0].pop("exceptions"), lambda p:p.update(examples=[42])]:
            p = fixture_profile(); mutation(p)
            with self.subTest(profile=p), self.assertRaises(ValueError):
                check_profile(p, schema)

    def test_profile_unknown_schema_keyword(self):
        with self.assertRaises(ValueError):
            check_profile("x", {"type":"string", "pattern":"x"})

    def test_future_extension(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for cat in ["fixture-one", "fixture-two"]:
                d = root / cat / "manifestations" / "sample"
                d.mkdir(parents=True)
                (d / "GUIDE.md").write_text("Fixture only")
                (root / cat / "SKILL.md").write_text(f"---\nname: {cat}\ndescription: Test fixture only.\n---\n")
            modules = [{"id": c, "title": c, "aliases": ["shared", "Perhatian"] if c == "fixture-one" else ["shared"], "kind": "trait", "entry": f"{c}/SKILL.md", "manifestations": [{"id":"sample", "aliases":["unique" if c == "fixture-one" else "other"], "path":f"{c}/manifestations/sample/GUIDE.md"}]} for c in ["fixture-one", "fixture-two"]]
            idx = {"schema_version":1,"modules":modules}
            validate_catalog(root, idx)
            self.assertEqual(len(lookup(idx,"shared")), 2)
            self.assertEqual(lookup(idx," PERHATIAN ")[0]["category"], "fixture-one")
            self.assertEqual(lookup(idx,"unique")[0]["manifestation"], "sample")
            self.assertEqual(lookup(idx,"unrelated"), [])
            for mutation in [lambda i:i["modules"].append(copy.deepcopy(i["modules"][0])), lambda i:i["modules"][0].update(entry="../SKILL.md"), lambda i:i["modules"][0]["manifestations"].append(copy.deepcopy(i["modules"][0]["manifestations"][0])), lambda i:i["modules"][0]["manifestations"][0].update(path="fixture-two/manifestations/sample/GUIDE.md"), lambda i:i["modules"][0].update(kind="unknown")]:
                bad = copy.deepcopy(idx); mutation(bad)
                with self.subTest(index=bad), self.assertRaises(ValueError):
                    validate_catalog(root,bad)
            (root / modules[0]["manifestations"][0]["path"]).unlink()
            with self.assertRaises(ValueError):
                validate_catalog(root,idx)

    def test_adapter_extension(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp); (root/"adapters").mkdir(); (root/"adapters/sample.md").write_text("Fixture only")
            item = {"id":"sample","title":"Sample", "path":"adapters/sample.md", "evidence_date":"2026-01-01"}
            idx = {"schema_version":1,"platforms":[item]}
            validate_adapters(root,idx)
            for mutation in [lambda i:i["platforms"].append(copy.deepcopy(item)), lambda i:i["platforms"][0].update(evidence_date="2026-02-31"), lambda i:i["platforms"][0].update(path="../sample.md")]:
                bad = copy.deepcopy(idx); mutation(bad)
                with self.subTest(index=bad), self.assertRaises(ValueError):
                    validate_adapters(root,bad)


if __name__ == "__main__":
    unittest.main()
