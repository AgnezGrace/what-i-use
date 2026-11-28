# Catalog maintenance

The local metadata is the source of truth; both indexes and README managed blocks are derived. The Python 3.10+ synchronizer has no external dependencies. It never writes character behavior or changes the router. Human review is required; `reviewed` is an explicit author declaration, not an automated quality certification.

## Add a category

Create `<id>/SKILL.md`, `<id>/README.md`, and `<id>/module.json`. Example metadata (illustrative only):

```json
{"title":"Stop Asking If I'm Okay","kind":"trait","aliases":["attention","perhatian"],"status":"draft"}
```

Create `<id>/manifestations/<manifestation-id>/GUIDE.md` and a sibling `manifestation.json`:

```json
{"aliases":["practical care","perhatian praktis"],"status":"draft"}
```

Change `status` to `reviewed` only after content review. A reviewed manifestation under a draft category is not published. IDs and paths are derived from directory names. Missing metadata means unregistered content; it is not guessed. Relationships, modifiers and other references remain local knowledge linked from the category skill, not individual global catalog entries.

## Add an adapter

Create `adapters/<id>.md` plus `adapters/<id>.adapter.json`:

```json
{"title":"Example platform","evidence_date":"2026-01-01","status":"draft"}
```

Use the actual evidence date and record the observed interface in the guide. Mark reviewed only after checking the mapping.

## Synchronize

From the roleplay directory:

```sh
python scripts/sync_catalog.py          # dry run
python scripts/sync_catalog.py --write  # apply
python scripts/sync_catalog.py --check  # CI: nonzero on drift
python scripts/validate.py
python -m unittest discover -s tests -v
```

Generated destinations: `catalog/index.json`, `adapters/index.json`, the managed block in root README, adapter README and each metadata-bearing category README. All text outside the markers is preserved (first-run append may normalize trailing newlines). The router is stable and uses the indexes. Aliases can remain ambiguous. Drafts stay unlisted. No module or adapter is created by the synchronizer.

For intentional deletion or renaming, preview with `--allow-remove`, then use `--write --allow-remove`. Existing registrations without metadata also require migration or explicit removal. Keep metadata and guides in the same commit. Run in a clean working tree and avoid simultaneous writers. The script validates candidate indexes and stages all files before replacement; each file replacement is atomic, not the entire batch. If interrupted, inspect the diff and rerun. Structural validation does not prove behavioral quality or adapter compatibility.
