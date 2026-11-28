---
name: the-user-is-not-a-stack-trace
description: Resolve ambiguous bug and revision scope using evidence. Use when a user reports a symptom on one page, requests a cross-page correction, describes visual inconsistency, or risks unintended changes to shared components. Inspect narrowly outward, locate the cause, preserve intentional variation, and verify affected and unaffected consumers with minimal context.
---
# The User Is Not a Stack Trace

*The user reports what they observe. The agent investigates what causes it.*

## 1. Your User Is a Witness, Not a Debugger
Treat a reported page, screenshot, or example as an observation unless wording establishes a boundary. A user can identify a broken experience without knowing its component, dependency, or root cause. Convert the report into an observable behavior and an acceptance condition. Explain technical uncertainty in terms of user impact.

Recognize scope signals:
- “On Settings, the button has a strange shadow” identifies an observed location.
- “Only change Settings” establishes a modification boundary, including indirect effects.
- “Fix this wherever it occurs” authorizes investigation and correction of confirmed equivalent defects.
- “Make Settings blue” expresses a local design preference by default.
- “Make every primary button blue” expresses a shared design requirement.
- “This looks wrong” without a clear intended outcome may require a focused question after examining available context.

A defect is a demonstrable mismatch with an established requirement, expected behavior, or invariant. An aesthetic preference is a requested change in appearance. Similarity alone establishes neither equivalence nor authority.

## 2. Read Wide, Write Narrow
Maintain separate scope sets throughout the task:
- `reported`: the surfaces named by the user.
- `inspected`: the relevant implementation and consumers examined.
- `affected`: surfaces where the same cause produces an established defect.
- `protected`: working behavior, intentional variants, explicit exclusions, and unrelated user changes.
- `authorized`: the permitted behavioral impact, interpreted from the request and applicable project rules.
- `modified`: files and symbols necessary to implement the authorized correction.
- `verified`: surfaces and states actually checked after the change.

A file path is an implementation location, not the full impact boundary. A one-line shared change can affect every route. Read permission and change permission remain distinct. Consider generated output and downstream packages when tracing consequences.

## 3. Three Questions Before Touching Anything
1. What is the expected behavior, and what is the observed behavior?
2. Which implementation or configuration produces the difference?
3. Which other consumers would actually change if this implementation were corrected?

Use project requirements, existing tests, established design tokens, healthy comparison surfaces, and user instructions as evidence. When those sources disagree, record the conflict and resolve the consequential uncertainty before broadening the change.

## 4. The Same Shadow Can Have Different Parents
Classify the cause with evidence:
- LOCAL: a route, wrapper, local state, selector, or configuration creates the defect.
- SHARED: a reused component, inherited token, global rule, or common service creates the defect in multiple consumers.
- MULTIPLE: matching symptoms have separate confirmed causes.
- INTENTIONAL: the appearance or behavior is a supported variation.
- UNKNOWN: available observations do not establish causality.

Trace from the rendered element to its computed style, source declaration, event handler, state owner, or relevant service. For CSS examine cascade order, specificity, inheritance, pseudo-states, layers, media queries, and component variants. For stateful behavior examine event flow, data ownership, subscriptions, and asynchronous transitions.

A shared import alone proves reuse, not a shared defect. A matching screenshot alone proves similarity, not a common cause. A common dependency may have healthy consumers because of overrides, variants, or different runtime conditions.

## 5. Your Repository Is Not a Buffet
Start with the reported route and the smallest useful source excerpt. Trace its direct dependencies. Search exact component names, selectors, tokens, handler names, or error signatures. Prefer file paths, symbol references, and line ranges over full-file dumps.

Escalate progressively:
1. Read the reported implementation, relevant requirement, and focused tests.
2. Trace the suspected owner and relevant dependency edges.
3. Enumerate consumers of that owner; group equivalent consumers by variant and runtime context.
4. Inspect representative healthy and affected consumers, plus explicit exceptions.
5. Expand to transitive consumers, runtime registrations, or global style rules when evidence warrants it.
6. Stop expanding once the cause, intended behavior, impact boundary, and verification plan are sufficiently supported.

Suggested initial investigation budget: one reported surface, its nearest owner, and one healthy comparison. Escalate when the evidence is incomplete; the budget is a starting heuristic, not a cap on safety. For security, data loss, authentication, payments, and release-critical paths, use risk-appropriate coverage even when context cost rises.

Prefer existing symbol indexes, import graphs, targeted search, git diff, and test discovery. Exclude generated bundles, vendored code, and dependency directories from initial searches unless they are directly implicated. Use actual source for changes; generated output is evidence, not the preferred repair location.

A component map may help if it is derived from current source, keyed to a revision, and verified when used. Treat stale or incomplete maps as hints. Dynamic imports, aliases, CSS selectors, plugins, runtime themes, and indirect consumers can escape static indexing.

## 6. The Scope Resolution Protocol
| Evidence and intent | Decision |
| --- | --- |
| Confirmed local cause | Correct the local owner; verify a relevant neighbor or shared consumer remains unchanged. |
| Confirmed shared defect; no explicit local restriction | Correct the narrowest shared owner when the correction restores an established invariant; verify affected consumers and protected variants. |
| Shared owner; user explicitly restricts effects to one page | Use a supported local configuration or isolated variant only if it preserves the architecture and intended behavior. Otherwise report the conflict and ask before editing the shared owner. |
| Separate causes; same observable defect; explicit cross-page request | Correct each confirmed owner independently; preserve healthy surfaces. |
| Separate causes outside an example-only report | Correct the reported cause, disclose independently discovered defects, and seek authorization if fixing them constitutes additional scope. |
| Similar appearance; intended behavior differs | Preserve the intentional variation. |
| Subjective local preference | Apply locally or through a supported variant; establish global intent before changing a shared default. |
| Unknown cause or uncertain intended outcome | Continue bounded investigation; if a consequential ambiguity remains, ask one focused question or report a blocker. |

When a shared fix has uncertain effects on protected consumers, prefer reversible experiments and further inspection. A page-local workaround that hides a shared defect is appropriate only when its limitation is explicit and the requested boundary requires it. Avoid duplicating components merely to bypass a proper shared correction.

## 7. Your Evidence Ledger Beats Your Confidence
Before writing, construct a compact internal ledger:

```text
Observed: route / state / input / actual behavior
Expected: requirement or comparison / desired behavior
Cause: owner + evidence + confidence
Consumers: affected / protected / unknown
Authorization: explicit boundary or inferred defect scope
Proposed edit: owner + minimal correction
Verification: failing reproduction + protected control + affected checks
```

For ambiguous cases, reproduce the defect first. Where reproduction is unavailable, distinguish a hypothesis from a demonstrated cause. Use an isolated experiment or a targeted test to discriminate between local and shared causes. Preserve artifacts or evidence as appropriate, without collecting unnecessary personal data or secrets.

Confidence labels are qualitative: confirmed, supported hypothesis, unknown. A confirmed cause needs an observation tied to implementation, ideally a controlled change or equivalent test. A shared owner discovered by search remains a hypothesis until its effect is established.

## 8. Put the Chainsaw Down, Then Pick Up a Scalpel
Inspect the current diff and respect pre-existing user changes. Select the smallest coherent change that repairs the cause and preserves established contracts. Reuse existing component APIs, variants, and design tokens. Add a new abstraction only when it resolves a demonstrated architectural need.

Keep unrelated cleanup, cosmetic redesign, broad formatting, package changes, and speculative refactors outside the repair. Preserve accessibility semantics, keyboard focus, intentional elevation, responsive behavior, state transitions, and user data.

When the evidence contradicts the proposed edit, revise the plan. Avoid stacking unverified overrides. Restore only your own experimental changes; respect work belonging to others.

## 9. Prove the Fix, Including What You Left Alone
Capture a failing reproduction before the change when feasible. After the change, rerun the reproduction under comparable conditions and check the expected behavior.

For a local edit, test the reported surface and a relevant unaffected control. For a shared edit, enumerate direct consumers, classify equivalent contexts, and test each material variant and applicable input/state combination. Use full coverage where practical and risk-based grouping where exhaustive coverage is costly; report which consumers were directly tested and which were only inspected or inferred.

For visual changes, inspect actual rendered behavior in relevant viewports, themes, and interaction states. Preserve visible keyboard focus when repairing pointer-focus artifacts. Compare computed styles or geometry and screenshots where useful. For backend changes, test the real contract and its callers, including failure cases.

A passing build is evidence of compilation, not of correct behavior. A source inspection is evidence of implementation, not of runtime success. An unchanged file can still exhibit changed behavior through a dependency.

Use status labels: VERIFIED, FAILED, UNVERIFIED, BLOCKED, NOT APPLICABLE (with reason). Record exact scope and evidence. When runtime access is unavailable, provide the most useful verified partial result and identify the remaining check.

## 10. Stop Asking the User to Be the Engineer
Resolve implementation ambiguity through evidence where possible. Ask a focused question when user intent, authorization, or a meaningful design choice remains unresolved. State the practical consequence rather than asking the user to select unfamiliar implementation details.

Example: “This button is shared by four pages. A global change would alter the intended shadow on the checkout button. Should that style remain?”

When a confirmed shared fix safely restores established behavior, communicate the broader affected scope without requiring an unnecessary page-by-page instruction. For a material new effect, external action, or explicit scope conflict, obtain the necessary authorization first.

## 11. Context Is Expensive, Confusion Is More Expensive
Keep one compact ledger instead of repeatedly restating the entire task. Reuse confirmed evidence within the current revision. Read changed regions and relevant definitions after edits. Cache search results only while their revision and assumptions remain valid.

Avoid repeated repo-wide scans, redundant full-file reads, duplicated patches, and tests unrelated to the change. Expand coverage when new evidence or risk warrants it. Record file reads, search calls, changed lines, and test scope if measuring efficiency; treat those as proxies, not measured token savings. Actual token comparisons require comparable runs and instrumentation.

## 12. The Final Report Is Not a Novel
Report the cause, modification scope, affected surfaces, protected behavior, actual checks, and remaining uncertainty. Give the user the practical result first. Keep the internal ledger internal unless useful for the task.

Example: “The click artifact came from the shared Button focus rule. I corrected that rule, verified Settings and Library, and preserved keyboard focus and the checkout button’s intended elevation. Profile was inspected but not changed.”

If additional unrelated defects were found, distinguish them from the completed repair. Avoid claims about every page unless the evidence covers every page.

## 13. Acceptance Gate
A change qualifies for completion when the requested behavior is verified or its verification limits are explicitly reported, the cause and impact are supported by evidence, the edit remains within the authorized behavioral boundary, and protected behavior has received risk-appropriate regression checks. A critical failed or blocked check prevents a claim of release readiness.

See `tests/TEST-REPORT.md` for the controlled reference experiment and `tests/scenarios.md` for agent-level evaluation prompts. The fixture is an example of the protocol, rather than a replacement for inspecting the actual project.

**The user gives you a symptom, not a license to remodel the planet. Read wide. Write narrow. Prove the difference.**
