# Fuck It, Use Math

An independent agent skill for building locally owned vector icon systems with native SVG and deterministic geometry. The 26 reference symbols use familiar visual metaphors and independently authored coordinates. They are examples, rather than a claim of unique trademarkable shapes.

## Use

Load `SKILL.md` when the task involves iconography, simple visual assets, or visual dependency decisions. For an existing product, evaluate migration scope and preserve established meanings. Copy the reviewed assets or adapt the generator to the product's own visual tokens.

Open `catalog.html` in a browser that permits local HTML and JavaScript. The catalog is self-contained. Each row of icons shows 16, 20, 24, 32 and 48 CSS px, in that order. Search, theme switch, SVG source copying (with manual fallback) and the procedural gear demonstration are included. Fixed icons need neither the generator nor the catalog script in production.

Run `python generate.py` to regenerate all assets, the registry and the catalog using Python's standard library. Run `python tests/test_icons.py` with Playwright, Pillow and Chromium installed; set `CHROMIUM` to the executable path if it differs from `/usr/bin/chromium`. These are development-only verification dependencies. Record actual versions in a project lockfile when integrating the harness.

## Package

- `SKILL.md`: agent instructions and acceptance gate.
- `generate.py`: deterministic geometry and serialization.
- `registry.json`: semantic IDs, geometry and paths.
- `icons/`: 26 standalone SVG files.
- `catalog-template.html`: offline catalog source template.
- `catalog.html`: generated self-contained atlas.
- `tests/`: executable checks, evidence and screenshots.

The security profile is deliberately restricted to trusted, generated geometry. It is not an upload sanitizer. Existing libraries with justified functionality remain legitimate. Read the test report before making portability or security claims.
