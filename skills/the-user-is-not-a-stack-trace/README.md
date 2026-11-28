# The User Is Not a Stack Trace

A standalone agent skill for resolving local versus cross-surface change scope. Copy this directory into a skill location supported by the host agent. The host determines when the skill is loaded; for persistent use, add a short instruction in the project's agent configuration to invoke it when a bug report or revision has ambiguous scope.

Read `SKILL.md` first. Load the tests only when validating or evaluating the skill. The skill complements change-minimization practices rather than replacing project requirements or safety constraints.

## Reproduce the reference experiment

Requirements: Python 3, Playwright, and Chromium installed locally. Run from the package root:

```sh
python tests/test_scope.py
```

The script constructs temporary, synthetic multi-page sites, applies three predetermined repair strategies, and checks actual Chromium computed styles after pointer and keyboard interaction. It also verifies edit scope and checks a small decision table. No network access or production project is needed. Set `CHROMIUM_PATH` if Chromium is installed at a different path.

Results are written to `tests/results.json`. The experiment tests implementation examples and a deterministic policy oracle, not independent language-model compliance. See `tests/scenarios.md` for a repeatable agent evaluation protocol.
