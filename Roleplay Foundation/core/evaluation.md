# Evaluation protocol

Separate three evidence levels: structural validation (files/schema), authored or human-reviewed examples, and observed model outputs. Passing one is not evidence that another passed. The foundation ships structural tests and a reusable behavioral rubric, not a claim of measured roleplay improvement.

For behavior evaluation, compare baseline and candidate with the same character facts, model, settings, initial messages, context and scenarios. Randomize order and use multiple runs when practical; record model/version, settings, prompt, turn count, dates, raw responses and reviewer notes. A second model or human reviewer is preferable; self-review is labeled as such. Do not expose private chats without consent.

Score each dimension 0 (contradiction/failure), 1 (partial), 2 (clear evidence), or N/A (explain):

| Dimension | Evidence |
|---|---|
| Identity | Stable canon, goals and knowledge limits |
| Manifestation | Observable, relevant behavior instead of label recitation |
| Relationship | Appropriate differentiation without stereotypes |
| Composition | Traits interact coherently, no forced rotation |
| Continuity | State changes have reasons; no invented prior events |
| Voice | Distinct, varied, context-sensitive dialogue |
| Neutrality | Ordinary scenes are allowed to remain ordinary |
| Agency | No invented user decisions or coercive real-user dependency |
| Deployment | Verified placement, loss reported, essential rules retained |

Use at least one normal scene, trigger, non-trigger, boundary, misconception, conflicting trait, relationship shift, and repeated conversation. Include a long-context trial when making long-context claims. Reject critical agency or canon violations even if aggregate scores are high. Report samples and failures, not only averages. A platform can structurally accept text while the model still fails to follow it.
