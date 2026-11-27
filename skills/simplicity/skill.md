---
name: simplicity-is-everything
description: Design, audit, implement, and refine interfaces around genuine user needs, coherent interaction paths, useful language, and durable simplicity. Use for UI design, UX review, feature planning, interface implementation, and product refinement.
---

# Simplicity Is Everything

## 1. Purpose

Create products whose features earn their place through practical value. Make the interface easy to understand, the interaction easy to complete, and the resulting experience worth returning to.

Simplicity is the alignment of purpose, capability, presentation, and behavior. A simple product can contain sophisticated engineering, advanced workflows, and extensive functionality. The user encounters the right degree of complexity at the right moment.

Design for the people using the product. Treat designer taste, implementation convenience, and visual novelty as inputs whose value depends on their contribution to the user's experience.

Apply this skill to new interfaces, existing screens, feature proposals, navigation systems, component libraries, and interaction flows.

## 2. Core principles

| Principle | Operational meaning |
| --- | --- |
| Necessity | Every feature serves an identifiable user outcome. |
| Proportion | The interface gives each task the space and attention its importance warrants. |
| Cohesion | Related actions, information, and states form a continuous experience. |
| Clarity | Users understand what matters, what they can do, and what happens next. |
| Economy | Each visible element contributes distinct value at its current location. |
| Durability | Common workflows remain efficient through repeated use and product growth. |
| Agency | Users retain meaningful control over consequential actions. |
| Inclusion | People with varied abilities, devices, and experience can accomplish essential tasks. |

## 3. Priority order

Resolve design conflicts in this sequence:

1. User safety, privacy, accessibility, and data integrity.
2. Explicit requirements and established product behavior.
3. Successful completion of the user's task.
4. Discoverability, comprehension, and recovery.
5. Efficiency across repeated use.
6. Visual coherence, expressive identity, and aesthetic refinement.
7. Implementation economy and maintainability.

Treat legal, domain, and platform requirements as binding constraints. Preserve essential capabilities while simplifying their presentation and access paths.

When priorities compete, select the option with the clearest user benefit and document the tradeoff.

## 4. Activation and scope

Activate this skill when a request involves any of these activities:

- Creating or restructuring an interface.
- Adding a feature or changing its placement.
- Reviewing navigation, settings, onboarding, or workflows.
- Improving usability, accessibility, or visual hierarchy.
- Reducing interface clutter or consolidating functionality.
- Implementing responsive layouts and reusable components.

Scale the process to the task. A focused label change calls for local inspection and targeted verification. A product redesign calls for a wider inventory, workflow analysis, and regression coverage.

Use the current implementation and explicit user requirements as the primary sources of product context. Treat unverified assumptions as hypotheses.

## 5. Establish the user's actual task

Identify the following before proposing interface changes:

| Input | Question |
| --- | --- |
| Actor | Who performs the task? |
| Goal | What outcome are they trying to achieve? |
| Context | Where, when, and under which conditions does the task occur? |
| Frequency | How often does the actor perform it? |
| Knowledge | Which concepts and controls are familiar to this actor? |
| Consequence | What happens when the task succeeds, fails, or gets interrupted? |
| Constraints | Which platform, accessibility, business, and data requirements apply? |

Distinguish observed user behavior, explicit requirements, and design hypotheses. Validate material uncertainties through product evidence, task testing, or focused clarification.

Proceed with a clearly stated, reversible assumption when available evidence supports a reasonable decision. Seek clarification when the choice materially changes scope, irreversible behavior, or core product direction.

Express the primary task in one sentence:

> The user wants to [action] so they can [outcome] within [context].

Use this statement as the reference for feature selection and interface decisions.

## 6. Feature admission

Evaluate each proposed capability using this decision record:

```yaml
feature:
  user_outcome: ""
  evidence: ""
  frequency: occasional | recurring | frequent
  criticality: routine | important | essential
  existing_path: ""
  expected_benefit: ""
  interaction_cost: ""
  maintenance_cost: ""
  dependencies: []
  placement: primary | secondary | contextual | advanced
  decision: admit | merge | defer | retire | investigate
  rationale: ""
```

### Admission rules

- Admit capabilities that satisfy a demonstrated need, an explicit requirement, or a credible essential use case.
- Merge capabilities when they share the same outcome, scope, permissions, and interaction contract.
- Place specialized capabilities within the context where users need them.
- Defer speculative enhancements until their value and fit become clear.
- Investigate uncertain cases through a lightweight prototype or existing usage evidence.
- Retire obsolete capabilities through an approved migration that preserves user data and essential workflows.

Treat frequency and criticality separately. A rare account recovery action can be essential. A frequent decorative interaction can have marginal value.

Evaluate feature value over the full lifecycle: discovery, initial use, repeated use, recovery, maintenance, and eventual migration.

## 7. Interface element admission

Inspect every visible element according to its contribution at its specific location.

An element earns placement through at least one of these roles:

- Performing an action.
- Communicating necessary state or information.
- Establishing meaningful orientation or hierarchy.
- Supporting comprehension, accessibility, or recovery.
- Satisfying a legitimate product, identity, or regulatory requirement.

Use this audit record for questionable elements:

```yaml
element:
  location: ""
  role: ""
  user_question_answered: ""
  unique_contribution: ""
  related_elements: []
  consequence_of_removal: ""
  decision: retain | combine | relocate | replace | remove | verify
```

Compare the proposed interface with the version that omits the element. Retain it when the comparison demonstrates a material contribution to usability, meaning, safety, or identity.

Consolidate overlapping visual and functional roles while preserving accessible names and semantic structure.

## 8. Screen hierarchy

Give every screen a recognizable purpose. Identify its primary task, supporting information, secondary actions, and contextual tools.

Arrange elements according to task relevance and natural reading order. Establish hierarchy through spacing, alignment, typography, grouping, and meaningful contrast.

Give the dominant action prominence when the screen has a clear next step. Give equal visual weight to actions with equivalent importance, such as choices in a comparison interface.

Keep related controls near the content they affect. Place persistent navigation where users can predictably return to it.

Use whitespace as functional separation. Use cards, borders, dividers, and surfaces when they clarify relationships or interaction boundaries.

Adjust density to the user's work. A professional data table may benefit from compact rows; a first-run form may benefit from generous spacing and explicit guidance.

## 9. Feature placement and progressive disclosure

| Feature category | Preferred access |
| --- | --- |
| Primary, frequent task | Directly visible within the main workflow. |
| Essential, occasional task | Predictable, clearly discoverable location. |
| Item-specific action | Adjacent to the item or in its contextual menu. |
| Advanced configuration | Relevant settings or an expandable section. |
| Global utility | Stable navigation or a consistent application-level control. |
| Sensitive or destructive action | Deliberate entry point with suitable safeguards. |

Reveal supporting controls as the task creates a need for them. Keep task-critical actions available at the point of use.

Consider the cumulative effort of opening menus, scrolling, changing screens, and restoring context. Prefer direct access when repeated retrieval creates meaningful friction.

Give collapsed groups descriptive names and clear expanded states. Maintain keyboard access and predictable focus behavior.

Preserve context when opening a detail view, menu, modal, or configuration panel. Restore the user's position and focus when they return.

## 10. Navigation and interaction paths

Map the actual path from intention to outcome:

```text
Intent -> Entry point -> Action -> Feedback -> Outcome
                              -> Recovery when needed
```

Count meaningful decisions, context switches, and repeated inputs alongside clicks or taps. A necessary confirmation can protect an important outcome; an extra menu can reduce crowding for occasional actions.

Use stable terminology across navigation, page titles, actions, and feedback. Maintain a consistent destination and scope for equivalent controls.

Support platform conventions for back navigation, keyboard interaction, search, and dismissal. Preserve edits, selection, scroll position, and filters according to the workflow's expectations.

Combine equivalent entry points when they serve the same actor and context. Retain multiple entry points when they serve distinct contexts, accessibility needs, or established navigation habits.

## 11. Language economy

Write interface copy for the user's next decision or action. Use familiar terms, concise phrasing, and direct verbs.

### Text roles

| Role | Content |
| --- | --- |
| Title | Current task, object, or destination. |
| Label | Meaning of a field, control, or unfamiliar icon. |
| Helper text | A constraint, consequence, or useful instruction. |
| Status | Current state, progress, or result. |
| Error | Problem, affected field or operation, and recovery action. |
| Confirmation | Meaningful consequence and deliberate choices. |
| Empty state | Current condition and an appropriate next action. |
| Onboarding | Essential knowledge at the moment it becomes useful. |

Give each piece of copy a distinct responsibility. A heading and a subtitle earn separate placement when each communicates different information.

Choose concise action labels such as `Save`, `Export PDF`, `Rename`, and `Create project`. Use outcome-specific wording for high-consequence actions, such as `Delete project`.

Use placeholders for examples and formatting cues. Give inputs persistent accessible labels and visible labels where recognition, recall, and task complexity warrant them.

Use concise instructional text for unfamiliar workflows, validation constraints, and consequential decisions. Place extended guidance in a relevant help surface.

### Copy refinement procedure

1. Identify the user's question at the current step.
2. Identify the information already conveyed by the interface and context.
3. Assign a distinct purpose to each remaining text element.
4. Combine overlapping messages into one precise statement.
5. Preserve instructions, constraints, state changes, and recovery guidance that affect task success.
6. Read the resulting screen in task order and check its meaning in isolation and in context.

## 12. Icons and labels

Select icons through recognition, meaning, platform convention, and the consequence of misunderstanding.

Use familiar icon-only controls when the symbol, context, and expected behavior provide reliable recognition. Supply an accessible name, a sufficiently sized target, and appropriate tooltip or contextual guidance for such controls.

Pair icons with visible labels when actions are unfamiliar, ambiguous, consequential, or central to navigation for the intended audience.

Prefer text controls when words communicate the action more clearly than a symbol. Use decorative icons to support visual identity or orientation when their role is clear.

Treat an accessible name as a semantic requirement. Align it with the visible label when one is present. Mark decorative artwork with appropriate presentation semantics.

Evaluate icon recognition through representative task testing. Consider touch users, keyboard users, screen reader users, first-time users, and localization.

## 13. Components and visual treatment

Use a coherent component vocabulary grounded in platform and product conventions.

- Buttons perform actions; links navigate to destinations.
- Form fields communicate their purpose and applicable constraints.
- Selection controls represent choices and current values.
- Menus group related commands or destinations.
- Dialogs handle focused decisions and context-sensitive interactions.
- Status surfaces communicate changes and outcomes.

Select the component whose semantics and interaction model match the task. Give interactive elements perceivable states for focus, hover where applicable, press, selection, loading, and availability.

Use design tokens for recurring spacing, color, typography, radii, and elevation. Apply visual variation when it communicates a meaningful difference.

Use motion to clarify transitions, spatial relationships, and feedback. Respect reduced-motion preferences and preserve timely access to controls.

## 14. Essential states and recovery

Design the workflow as a state system rather than a collection of ideal screens.

| State | Expected treatment |
| --- | --- |
| Ready | Available actions and current information. |
| Empty | Meaningful context and an available next step. |
| Loading | Appropriate feedback while preserving useful context. |
| Success | Clear outcome, with continuation where useful. |
| Validation | Specific field guidance and correction path. |
| Failure | Accurate explanation and available recovery action. |
| Offline | Available capabilities, pending work, and synchronization status where relevant. |
| Restricted | Relevant access status and legitimate resolution path. |
| Interrupted | Preserved progress and a predictable return path. |

Choose feedback intensity according to consequence. Local state changes may benefit from an inline update; significant failures may warrant a prominent message.

Use undo for reversible operations when recovery remains reliable. Use explicit confirmation for irreversible or high-impact operations when it materially protects the user.

Preserve entered data through recoverable errors. Communicate saving and synchronization accurately. Keep retry behavior safe for transactions and repeated submissions.

## 15. Accessibility and adaptability

Treat accessibility as part of simplicity. An interface becomes easier to use when its meaning survives different input methods, screen sizes, and sensory conditions.

Apply relevant accessibility standards and platform guidance to the implementation. Include these checks as a practical baseline:

- Semantic controls, headings, landmarks, and form associations.
- Accessible names for interactive elements and meaningful descriptions for relevant images.
- Logical keyboard order, visible focus, and appropriate dialog focus management.
- Adequate contrast, including meaningful control boundaries and focus indicators.
- Touch targets sized and spaced for the intended platform; use 44 CSS pixels as a practical touch-friendly default and verify applicable requirements.
- Text resizing and reflow, including narrow viewports and long translated strings.
- State information conveyed through text, semantics, shape, or other perceivable cues alongside color.
- Announced dynamic feedback when it affects assistive technology users.
- Reduced-motion support and appropriate alternatives for gesture-based interactions.

Use automated checks for machine-detectable defects and manual or representative user testing for meaning, operability, and real-world comprehension.

## 16. Long-term usability and product growth

Evaluate the design after its novelty has faded. Favor predictable layouts, stable terminology, reliable state, and efficient repeated actions.

Use sensible defaults that reflect the task and respect user preferences. Remember appropriate settings and recent context when persistence is useful and authorized.

Provide optional shortcuts for experienced users while preserving a discoverable baseline interaction path.

Organize new capabilities around established user goals. Extend existing patterns when their semantics remain suitable. Introduce a new pattern when a distinct interaction requirement justifies it.

Evaluate recurring maintenance burden across components, state handling, documentation, localization, and support. Keep the interface and underlying implementation aligned through shared contracts.

## 17. Agent workflow

### Phase A — Inspect

Read the requested scope, current screens, component definitions, interaction handlers, and relevant product constraints. Identify user outcomes and existing capabilities.

Produce an internal inventory of primary tasks, supporting actions, text roles, state handling, and accessibility dependencies.

### Phase B — Diagnose

Trace representative task paths. Identify overlapping controls, repeated information, uncertain icons, misplaced actions, unnecessary context switches, and missing recovery paths.

Classify findings by effect: task failure, safety or data risk, accessibility barrier, comprehension friction, repeated effort, or visual inconsistency.

### Phase C — Decide

Select the smallest coherent change set that delivers the intended improvement. Map each change to a user outcome and a verification method.

Protect existing capabilities, state semantics, permissions, and data contracts. Treat feature retirement and substantial scope expansion as decisions requiring appropriate authorization.

### Phase D — Implement

Use existing components and design tokens where they satisfy the task. Align visual presentation, semantic roles, event handling, and state transitions.

Connect every interactive control to its intended behavior. Integrate the necessary loading, error, empty, and recovery states within the affected flow.

### Phase E — Verify

Run relevant automated checks, execute representative task paths, inspect responsive layouts, and exercise accessibility interactions. Compare equivalent baseline and candidate workflows when available.

Review any changed metrics alongside task success and observed regressions. Record limitations and evidence gaps.

### Phase F — Deliver

Summarize the user benefit, affected scope, verification results, remaining limitations, and any material tradeoffs. Use the requested output format and repository conventions.

## 18. Verification protocol

### Establish task equivalence

Define the same starting data, goal, completion condition, and essential safeguards for each compared interface. Reset state between trials. Keep environment differences explicit.

### Collect evidence

| Measure | Meaning |
| --- | --- |
| Task completion | The intended outcome is reached and verified in state or output. |
| Action count | The number of intentional user inputs required for the defined path. |
| Context switches | Movement between surfaces that interrupts the current task. |
| Visible controls | Interactive elements presented at a defined screen state. |
| Visible copy | Words presented to the user within a defined region and state. |
| Recovery | Ability to correct errors, cancel, retry, or undo as applicable. |
| Accessibility | Verified semantics, keyboard paths, focus behavior, and relevant visual checks. |
| Responsive behavior | Usability within representative viewport sizes and content conditions. |

Measure completion time through representative user sessions when available. Treat automation timings as execution measurements rather than evidence of human comprehension.

Use element counts and word counts as diagnostic signals. Interpret a reduction as beneficial when task success, meaningful information, discoverability, and safeguards remain intact.

### Test cases

| Scenario | Verification |
| --- | --- |
| Primary task | Complete the main workflow and verify the resulting state. |
| Secondary task | Locate and complete an occasional action through its intended path. |
| Duplicate control | Verify equivalent functionality after consolidation. |
| Empty and error states | Trigger the condition, understand the available action, and recover. |
| Sensitive action | Verify deliberate confirmation, cancellation, and final state as applicable. |
| Keyboard use | Reach and operate essential controls with a predictable focus sequence. |
| Narrow viewport | Inspect reflow, interaction targets, and access to essential actions. |
| Extended content | Exercise long names, translated copy, and dense or sparse data. |
| Repeated use | Repeat the task and verify stable behavior and expected state preservation. |
| Regression | Verify preserved capabilities and relevant data integrity. |

Select cases that match the changed scope and existing capabilities. Add domain-specific cases for transactions, permissions, synchronization, or other material risks.

### Evidence grades

- **Inspection:** reasoned evaluation of structure or code.
- **Automated execution:** reproducible assertions against actual application behavior.
- **Expert walkthrough:** structured manual task and interaction review.
- **Representative user test:** observed task performance by intended users.
- **Production evidence:** measured behavior under real usage conditions with appropriate privacy safeguards.

Name the evidence grade actually achieved. Treat claims of long-term adoption, discoverability, and satisfaction as hypotheses until appropriate human or production evidence supports them.

## 19. Acceptance gates

A candidate is ready for the proposed scope when the applicable gates are satisfied:

- Every required capability remains available and functional.
- The main task has a coherent, discoverable completion path.
- Each retained visible element has a defensible role.
- Consolidated controls preserve distinct scopes and behavior where applicable.
- Copy communicates essential meaning, constraints, and feedback.
- Critical actions preserve appropriate safeguards and recovery.
- Accessibility and responsive checks meet applicable requirements.
- Changed behavior passes relevant regression tests.
- Material assumptions, unresolved findings, and evidence limitations are recorded.

Resolve blocking failures before claiming readiness. Report partial verification when the environment or evidence supports a narrower conclusion.

## 20. Examples of design decisions

| Situation | Preferred decision | Reason |
| --- | --- | --- |
| A page title and subtitle express the same task. | Retain the clearer title. | One orientation cue serves the purpose. |
| A toolbar and footer offer the same save action. | Keep the most useful entry point, or retain both when context warrants. | Access matches actual workflow needs. |
| A familiar close symbol appears in a dialog. | Use the icon with an accessible name and appropriate target. | Context supports recognition. |
| A specialized export icon appears in a writing tool. | Use a visible `Export PDF` label. | The output format matters to the user's decision. |
| A destructive action appears alongside ordinary actions. | Give it deliberate placement and appropriate confirmation or undo. | Consequence determines interaction safeguards. |
| A settings page contains several expert parameters. | Group them by task and disclose advanced settings contextually. | The default path stays understandable. |
| A form includes an important input constraint. | Retain concise field-level guidance. | Useful information prevents avoidable errors. |
| A dense professional workspace supports repeated comparison. | Preserve meaningful density and efficient navigation. | User efficiency determines suitable complexity. |

## 21. Delivery record

Use this compact record for substantial changes:

```yaml
outcome: ""
scope: ""
changes:
  - decision: ""
    user_benefit: ""
verification:
  evidence_grade: ""
  passed: []
  outstanding: []
tradeoffs: []
assumptions: []
limitations: []
```

The final measure of simplicity is the user's ability to achieve a meaningful outcome with clarity, confidence, and appropriate effort. Design decisions earn their place through that experience.
