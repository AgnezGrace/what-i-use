# Fuck the Navigation Bar

Ghost Orbit is a dependency-free reference for contextually invoked navigation, not a claim of invention or universal usability.

- `SKILL.md`: agent instructions. Install this folder as a skill, or load the Markdown explicitly in your agent harness.
- `geometry.js`: pure deterministic solver usable in Node and browser.
- `preview.html`: self-contained offline demonstration; open in a modern browser. Hold on the dedicated canvas (320 ms), move to a target and release, or release at the origin and tap. Mouse right-click is supported on the canvas. The visible Actions button opens the accessible list. Choose 1, 4, or 7 items and a hand preference. Commands update a status counter; they are not a real application router.
- `preview-template.html`: source template. To regenerate: `python build.py`.
- `tests/`: reproducible test scripts, results, screenshots, and limitations.

Run from the package directory:

```sh
node tests/geometry.test.js
python tests/browser_test.py
```

The browser test requires Python Playwright and Chromium. Set `CHROMIUM_PATH` if the system browser is in a different location. The runtime preview has no external dependencies; test tooling is separate. No network access is needed after test tooling is installed.

Integrate the solver with the application's actual safe viewport, keyboard, reserved rectangles, command registry, navigation, and authorization. The demo's canvas is deliberately non-scrolling; do not apply its touch-action policy to a normal document, editor, or whole page. A visible fallback remains intentional.
