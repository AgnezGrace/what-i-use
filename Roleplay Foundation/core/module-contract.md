# Catalog module contract

The catalog is intentionally empty in the foundation release. Future categories belong directly under `roleplay/<category-id>/`, not inside `catalog/`; the latter is an index only.

A category is a knowledge package, not a complete character. Category IDs are stable lowercase kebab-case identifiers. Use a clear ID and optionally a satirical display title. A category SKILL.md has Agent Skills frontmatter (`name` equals folder ID, `description` explains activation) and refers to the root core using explicit relative paths. If installed separately, include or make the required core accessible; do not assume it is present.

Recommended layout (create only files with actual content):

```text
<category-id>/
  SKILL.md
  README.md
  manifestations/<manifestation-id>/GUIDE.md
  relationships/<relationship-id>.md
  modifiers/<dimension>.md
  interactions/<trait-id>.md
  anti-patterns/<pattern>.md
  tests/scenarios.md
```

A manifestation guide describes intent, observable evidence, triggers, channels, context, variation, limits, anti-patterns, examples, neutral examples and evaluation criteria. Use `assets/module-template.md` as an authoring template. Relationship and modifier files contain only category-specific differences from the shared core. Do not precompute Cartesian products of all manifestations, relationships and intensities.

Index entry fields: `id`, `title`, `aliases`, `kind`, `entry`, `manifestations` (each with `id`, `aliases`, `path`). Kinds: `trait`, `emotion`, `motive`, `behavior`, `temperament`, `mixed`. Register only files that exist and are reviewed. Aliases are case-insensitive exact labels, not semantic equivalence assertions; a polysemous label may match multiple entries and requires disambiguation. No duplicate IDs or paths within a category. Generate the root `catalog/index.json` from reviewed metadata using `python scripts/sync_catalog.py --write`; see [catalog maintenance](catalog-maintenance.md). Do not register placeholders as supported content.

Before publishing: validate catalog paths; check module invariants, behavior examples and nonexamples; test ambiguity, unrelated scenes, relationship variation and trait composition; report whether evaluation was structural, reviewed examples, or an actual model run. Research factual psychology claims when making them; label creative heuristics as such. Avoid clinical diagnosis or universal claims about real groups.
