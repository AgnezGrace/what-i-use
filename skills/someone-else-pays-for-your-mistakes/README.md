# Someone Else Pays for Your Mistakes

A portable agent skill for third-party harm and operational readiness. Install the directory containing SKILL.md using the agent harness's skill mechanism. If activation is unreliable, add a short persistent instruction to the existing agent rules: load this skill when a project involves real funds, sensitive data, consequential decisions, physical safety, or a public launch with material third-party reliance. Merge with existing rules instead of replacing them.

This skill complements security, engineering, and release checks. It provides a risk-based readiness protocol, not a license, legal opinion, clinical approval, or autonomous deployment enforcement. The rules are intentionally jurisdiction-neutral; verify actual laws and requirements on each project.

## Reproduce the reference tests

From the package directory, run `python tests/test_readiness.py`. Python 3.9+; standard library only. The script writes `tests/results.json` and reports each check. The gate is an illustrative deterministic implementation, not a universal legal decision engine. SQLite tests use synthetic money only.

The included scenario prompts are for independent agent evaluation. Run fresh sessions with identical prompts, first without the skill and then with it, randomize evaluation order, and score against the stated expectations. Do not treat authored expected answers as observed model outputs.
