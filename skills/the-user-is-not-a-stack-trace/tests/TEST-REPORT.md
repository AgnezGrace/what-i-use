# Controlled Scope Resolution Experiment

## Method
Five synthetic four-page sites (Home, Settings, Library, Profile) were generated with actual separate shared and local CSS source files. Three predetermined repair strategies were applied to fresh copies of each site. Chromium via Playwright measured computed CSS after click and keyboard interaction at 360×780 and 1280×800 CSS pixels. Local file navigation was blocked by the environment, so the harness read the CSS sources and inserted them into HTML in their original cascade order using set_content. It did not validate network loading or physical touch interaction.

- Local override appends a Settings-specific override regardless of cause.
- Global reset suppresses all button box shadows regardless of cause.
- Evidence-based reference removes the known causal rule from the expected source owner(s), or holds when the fixture stipulates no approved local variant and an explicit local boundary conflicts with shared repair.

Each run checks 16 rendered properties across four pages (idle shadow, click shadow, pointer outline, and keyboard focus) and one reference edit-set comparison. The last assertion compares exact expected source files for this fixture, rather than proving every alternative implementation would be invalid. Baseline observations also confirm the seeded defects and intended Home shadow.

## Results
| Strategy | Checks passed | Entire runs passed |
| --- | ---: | ---: |
| Local override | 158/170 | 4/10 |
| Global reset | 136/170 | 0/10 |
| Evidence-based reference | 170/170 | 10/10 |

The deterministic decision-table oracle passed 10/10 cases. It checks policy branches with already classified inputs; it does not establish that an LLM can classify a real bug. The full results, including per-page observations and changed files, are in results.json.

The local override leaves a shared defect in Library and misses independently authorized defects outside Settings. Even in cases where it passes this test suite, it can leave the original defective declaration in source. The global reset destroys Home's intentional elevation. The reference repair preserves the intentional Home shadow and the Profile override, and maintains visible keyboard focus. When independent defects exist outside the authorized example scope, the reference leaves them unresolved and calls for disclosure. When the explicit-boundary fixture is on hold, the reference makes no edit; passing that run means it respected the stipulated boundary, not that the reported defect was repaired.

## Limitations
The same author designed the fixture, policies, comparison strategies, and expected results. The reference edit is chosen from known fixture metadata rather than automatically inferred by an agent. The experiment demonstrates the consequences of predetermined scope choices; it does not measure model compliance, automatic causal discovery, production complexity, token savings, human usability, physical devices, other browsers, or screen reader accessibility. No actual token usage comparison was performed. See scenarios.md for the independent evaluation procedure.
