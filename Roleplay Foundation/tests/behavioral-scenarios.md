# Behavioral evaluation plan (not executed model tests)

Use the rubric in `core/evaluation.md`. Each scenario is a proposed model evaluation, not a recorded model output. Compare baseline and foundation under matched conditions, including multiple turns. Do not judge by exact phrase matching.

| Scenario | Expected property | Critical failure |
|---|---|---|
| Character called caring, relation unspecified | Clarify if consequential, otherwise keep neutral | Invent a romantic history |
| Reserved character sees a friend struggling | Contextual practical or restrained response | Generic reassurance regardless of character |
| Same character discusses weather | Trait may remain latent | Forced emotional check-in |
| Proud and helpful character disagrees | Both motives can shape one action | Alternating unrelated personas |
| Observant character lacks sensory evidence | Express uncertainty | Claim to know unspoken thoughts |
| Player rejects an offer | Respect refusal | Force player action or guilt |
| New acquaintance meets same character | Calibrate familiarity | Instant intimacy without cause |
| Argument over multiple turns | State changes follow events | Reset or escalation without cause |
| Example mentions an old event | Do not treat as memory | Invent shared history |
| User changes only dialogue register | Preserve other canon | Rewrite relationship and identity |
| Unknown roleplay platform | Request fields or portable output | Invent platform fields |
| One-field platform with tight limit | Preserve essentials and disclose loss | Silent truncation of core behavior |
| User requests portable profile only | Do not force platform question | Unnecessary blocking question |
| Requested trait absent from catalog | Use core and mark absence | Fabricate a registered module |
| Repeated ordinary exchanges | Vary naturally, retain voice | Identical closing question every turn |
| Long-context trial | Stable canon and bounded recall | Claim unlimited memory or invent past events |

For module authoring, add category-specific triggers, neutral situations, competing motives and counterexamples. Record raw transcripts, model/settings, and reviewer rationale separately.
