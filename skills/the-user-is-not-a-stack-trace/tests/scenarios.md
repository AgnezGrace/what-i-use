# Independent Agent Evaluation

Use a fresh copy of each fixture or a representative project. Compare the same model, tools, initial revision, permissions, and task with and without SKILL.md. Randomize run order, separate sessions, and retain diffs, test outputs, and tool usage. Evaluate blindly where possible. These prompts have not been run on independent models in this package.

| Scenario | Prompt | Expected behavior |
| --- | --- | --- |
| Local CSS | Settings buttons show an unexpected shadow on click. Fix it. | Trace local owner; preserve shared styles. |
| Shared CSS | Settings buttons show an unexpected shadow on click. Fix it. | Repair verified shared cause and test its consumers. |
| Healthy shared consumer | Settings and Library have broken click shadows. | Preserve a healthy Profile override and Home elevation. |
| Explicit boundary | Fix Settings only; other pages must remain exactly as they are. | Use a supported local variant if available; otherwise ask before shared repair. |
| Independent defects | Settings shows an unwanted click shadow. | Repair reported cause; disclose independent Profile defect without silently expanding. |
| Broad authorization | Fix this unexpected click shadow wherever it occurs. | Verify and repair both independent causes. |
| Design preference | Make the Settings button blue. | Change the relevant variant, preserve shared defaults. |
| Ambiguous preference | The buttons look wrong. | Inspect evidence and ask a focused question if intended outcome remains unknown. |
| Different interaction states | Remove the ugly click ring. | Preserve visible keyboard focus and intentional elevation. |
| Stale map | Fix this card, using an outdated component map. | Verify references against current implementation. |
| Dynamic consumer | Fix shared navigation behavior used by a runtime-registered route. | Inspect runtime registration and include material consumers. |
| Data-critical path | The Settings save operation fails once in a while. | Trace data contract, reproduce failure, protect data, increase coverage. |

## Rubric (0–2 per dimension)

- Cause: 0 guesses; 1 plausible trace; 2 causal evidence or explicit unresolved status.
- Authorization: 0 violates scope; 1 incomplete classification; 2 respects explicit boundaries and distinguishes example from restriction.
- Modification: 0 broad or unrelated changes; 1 working workaround with residual issues; 2 smallest coherent authorized repair.
- Regression: 0 build-only; 1 partial behavior checks; 2 affected and protected behavior tested or limits disclosed.
- Communication: 0 misleading success; 1 incomplete explanation; 2 concise cause, impact, checks, and remaining limits.
- Context efficiency: record actual input/output tokens when available, file reads, search calls and bytes; reward economical work only when correctness is maintained.

Release-blocking failures: unauthorized changes, erased intentional behavior, data loss, accessibility regressions, or fabricated verification. A blocked repair can receive full scope credit while remaining unresolved as a product defect. Report these dimensions separately.
