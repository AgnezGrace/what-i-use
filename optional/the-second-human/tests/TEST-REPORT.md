# Test report

## Executed checks

Run `python3 tests/validate.py` from the package root. Python standard library only.

| Group | Passed | Total |
| --- | ---: | ---: |
| Structural and reference checks | 23 | 23 |
| Authored-fixture lexical assertions | 40 | 40 |
| Injected forbidden-phrase mutations | 20 | 20 |
| Total | 83 | 83 |

The fixture checks verify explicitly chosen text anchors, rejection of deliberately weak authored baselines, and detection of one injected forbidden phrase per candidate. Results appear in `results.json`.

## Limitations

Both response variants were authored by the package creator. They are illustrative, not outputs collected from separate baseline and skill-enabled model sessions. Lexical assertions cannot establish semantic accuracy, naturalness, fairness, or behavior in unseen conversations. No human reviewer or independent model was used. Platform-specific automatic loading has not been exercised. Use the independent evaluation protocol in `evaluation-rubric.md` before drawing conclusions about model effectiveness.
