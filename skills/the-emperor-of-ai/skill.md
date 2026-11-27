---
name: the-emperor-of-ai
description: Govern familiar AI-generated UI patterns through deliberate hierarchy, coherent composition, restrained effects, and verified usability. Use when designing, implementing, reviewing, or refining interfaces that employ conventional cards, bento layouts, dashboards, gradients, badges, rounded shapes, glass, shadows, or motion.
---

# The Emperor of AI

*If you insist on making slop, give it a spine, a constitution, and a reason to exist.*

## 1. The imperial doctrine

Familiarity is useful. A card can organize information. A gradient can establish atmosphere. A dashboard can make a complex system legible. The quality of these devices depends on their relationship to the product, the task, and each other.

Treat AI slop as raw material. Transform it through judgment, discipline, and execution. The goal is recognizable patterns arranged with dignity, rather than novelty pursued for its own sake.

The user is the sovereign. The interface serves their objectives. The agent acts as steward of the system, while visual effects occupy subordinate roles.

Judge success through task completion, comprehension, consistency, accessibility, performance, and the credibility of the finished product. Visual spectacle is a secondary reward.

## 2. Jurisdiction

Activate this skill for interface design, component styling, dashboard composition, design-system development, visual review, and redesign requests involving generic-looking UI.

Apply the principles to web, mobile, and desktop software through the conventions of the actual target platform. Respect existing design systems, native interaction behavior, accessibility requirements, product identity, user constraints, and security boundaries.

Use the skill at the smallest scope that solves the task. A single dialog deserves a local correction; a product-wide redesign warrants a system-level audit.

For an existing product, preserve meaningful workflows, data, routes, and integration contracts. Request clarification when a missing product decision materially changes the outcome. Proceed with reversible assumptions when the remaining uncertainty concerns minor presentation details.

Treat these instructions as a design method. Actual content, user research, platform requirements, and measured behavior determine the final decision.

## 3. Establish the empire before decorating the palace

Create a compact internal design brief:

- Product purpose and target audience.
- Primary task, secondary tasks, and high-risk operations.
- Existing visual identity, theme, and component inventory.
- Main screen hierarchy and navigation model.
- Content density, responsive constraints, and accessibility needs.
- Available typography, icons, assets, and rendering capabilities.
- Success criteria and a representative test scenario.

Use actual interface content or clearly marked representative data. Build around realistic title lengths, localized text, empty states, large collections, validation errors, and permission boundaries.

Identify the user's next meaningful action before choosing a layout. A writing editor, account settings page, media browser, and analytics dashboard each deserve a different spatial structure.

## 4. Give the interface a spine

Define the reading order using alignment, scale, spacing, contrast, and position. Establish a dominant region, supporting regions, and contextual details.

Select one primary action per decision context. Multiple independent workflows may each have their own primary action within a clearly bounded region.

Keep the main task near the information required to perform it. Place supporting controls adjacent to their effects. Maintain stable anchor points across related screens.

Use a deliberate container width and consistent alignment lines. On wide screens, dedicate space to useful content rather than stretching every component across the viewport. On narrow screens, preserve logical reading order and reachable controls.

Test the hierarchy in grayscale, at reduced size, and with long content. The dominant task should remain recognizable through structure alone.

## 5. The nobility of components

Assign each component a role before assigning its appearance.

| Rank | Role | Typical treatment |
| --- | --- | --- |
| Crown | Primary task or meaningful focal content | Highest appropriate emphasis |
| Council | Key supporting content and actions | Clear, stable visual weight |
| Citizens | Routine information and controls | Quiet, readable presentation |
| Infrastructure | Separators, containers, hints, and decoration | Minimal visual demand |

Apply visual weight according to role. A warning can temporarily outrank the primary action when the situation requires attention. A selected tab communicates location; a destructive action communicates consequences.

Reuse component anatomy, interaction states, and tokens across equivalent roles. Customize the presentation to the product while retaining proven accessible primitives and platform behavior.

Treat native controls as legitimate infrastructure. Their visual integration, reliability, and suitability determine whether to style, wrap, or retain them.

## 6. Cards: a republic of boxes is still a mess

Use cards for independently meaningful units, repeated entities, actionable summaries, or content that benefits from a recognizable boundary.

Select the quietest useful boundary: spacing, divider, tonal surface, border, or elevation. Give related elements one shared container where that improves grouping.

Reserve stronger treatments for meaningful distinctions such as a selected item, featured content, or active task. Maintain consistent padding and alignment among peer cards.

Use direct page sections, lists, tables, or inline controls for content whose relationships are clearer through those structures.

For nested surfaces, establish a visible parent-child relationship through scale and contrast. Every additional layer earns its visual cost through a concrete interaction or grouping need.

## 7. Bento: architecture, not a box collection

A bento layout earns its place when content units possess different priorities or useful dimensions.

Choose a dominant tile and size supporting tiles according to their content and importance. Align edges using a shared grid, controlled gaps, and deliberate spans. Keep the reading order coherent with DOM and keyboard order.

Use equal-sized cards for truly comparable items. Allow asymmetry for genuinely different tasks, charts, media, or summaries. At narrow widths, reflow into a meaningful sequence with natural heights.

Validate the layout with real content, including unusually long values. Let content determine minimum space; let priority determine emphasis.

## 8. The radius constitution

Choose a small radius scale appropriate to the product. For example, a restrained software system might use 4, 8, and 12 CSS pixels, with pills reserved for naturally pill-shaped roles such as status chips.

Map the scale to component anatomy: controls, containers, and large feature regions. Align nested corners with inset geometry when surfaces visually follow each other.

Treat extreme rounding as a stylistic choice with a purpose, such as a playful media product or a compact segmented control. Preserve useful interior space and clear focus boundaries.

Keep shape language consistent across buttons, fields, menus, dialogs, charts, and navigation.

## 9. Gradients: the court painter has a budget

A gradient can convey atmosphere, depth, a data scale, or a purposeful brand transition. Choose its location, endpoints, direction, and contrast with intent.

Start with one expressive gradient region per view as a review heuristic. Expand the budget when a creative brief, visualization, or coherent surface system supports it. Related regions may share a coordinated treatment.

Use restrained tonal transitions for professional contexts and expressive color transitions when the product calls for them. Evaluate the entire text area over the gradient, including intermediate colors and hover states.

Use solid treatments for routine controls when they provide clearer hierarchy. Keep decorative gradients separate from semantic data encoding and interaction states.

## 10. Glass, shadows, and the laws of gravity

Use transparency and blur for overlays, contextual floating controls, and surfaces whose relationship to the background conveys useful information.

Provide an opaque fallback and a readable foreground across expected underlying content. Account for rendering cost on constrained devices and reduced-transparency preferences where supported.

Use elevation to communicate actual layering: base surface, raised control, overlay, and modal. Give peer surfaces equivalent depth. Keep shadows consistent in direction, softness, and strength.

Flat borders and tonal surfaces can carry most everyday grouping. Reserve stronger shadows for separation that matters, such as a menu floating above a scrollable region.

## 11. Color is a chain of command

Choose a coherent palette according to product identity, audience, user preferences, and context. Separate neutral surfaces, foregrounds, brand accents, interaction states, and semantic status colors.

Establish a restrained accent hierarchy. Give primary actions, selection, and focus an identifiable relationship while keeping error, warning, and success states distinguishable.

Use semantic tokens for background, surface, foreground, muted text, border, accent, on-accent, focus, and status roles. Supply explicit light and dark values when both modes are in scope.

Validate actual foreground-background pairs. For web interfaces targeting WCAG AA, use 4.5:1 for normal text, 3:1 for qualifying large text, and 3:1 for applicable non-text visual information. Evaluate each state and relevant gradient position. Convey meaning through text or shape alongside color when needed.

For formal business software, begin with neutral or cool matte surfaces and a measured accent. For expressive consumer products, consider stronger chroma, typography, or imagery within a disciplined structure. Warm hues, neon, and multicolor treatments earn their place through the brief.

## 12. Typography: let the content speak

Select a type family suitable for the audience, script coverage, visual identity, and reading duration. Use a stable fallback stack and account for font availability, loading, licensing, and metrics.

Assign a compact scale to page titles, section titles, body copy, and metadata. Create hierarchy through size, weight, line height, and contrast. Use tabular numerals when comparing changing numeric values.

Favor readable line lengths and natural wrapping. Verify zoom, localization, and dense data views. Reserve display type for moments that benefit from expressive personality.

Use headings, labels, and supporting copy according to their informational role. Accessible names and essential field labels belong to the interaction contract. Visible repetition earns its place through clarity, discoverability, or safety.

## 13. Badges, icons, and the ministry of unnecessary noise

Use badges to identify meaningful status, category, or exceptional information. Maintain a consistent vocabulary and visual treatment for the same state.

Use an intentional SVG or platform icon family with coherent stroke, optical size, and alignment. Give interactive icons an accessible name; provide visible text when the meaning needs explanation.

Reserve emoji for content, expressive communication, or a brief that deliberately treats it as part of the product identity. Functional iconography benefits from consistent geometry and predictable meaning.

Select ornament according to its contribution to atmosphere, identity, or orientation. Let the product's own content supply the strongest personality wherever possible.

## 14. Data deserves a reason to be on the throne

Choose metrics that support a concrete decision or action. Supply units, time ranges, and appropriate comparisons. Present uncertainty, empty data, and errors truthfully.

Select charts by analytical purpose: trends through lines, comparisons through bars, relationships through scatter plots, and exact values through tables. Provide accessible descriptions or equivalent data where appropriate.

Use a focal metric when it matters more than its peers. Give comparable metrics equal treatment. Coordinate axes, labels, legends, and semantic colors.

For ordinary workflows, favor useful work queues, recent items, search, and task shortcuts over ceremonial dashboards. Representative fixture data belongs to a clearly identified demo context.

## 15. Motion is a royal escort

Use motion to explain entry, exit, expansion, reordering, selection, or navigation continuity. Keep feedback immediate and transitions proportional to the interaction.

As a starting point, use roughly 100–180 ms for small state changes, 180–280 ms for local overlays, and 220–350 ms for larger transitions. Adjust according to distance, platform, task urgency, and measured performance.

Favor compositor-friendly transforms and opacity when appropriate. Preserve focus, pointer behavior, and stable layout while transitions run. Honor reduced-motion preferences with a direct state change or substantially reduced motion.

Use decorative animation sparingly and pause persistent effects when the interface is inactive or the user requests reduced motion. Confirm usability on representative hardware before making performance claims.

## 16. Spacing and density: govern the territory

Adopt a compact spacing scale, such as 4, 8, 12, 16, 24, and 32 CSS pixels. Apply it to equivalent relationships while allowing purposeful exceptions for optical alignment and platform conventions.

Use smaller spacing within a group and larger spacing between groups. Match density to task frequency and reading requirements. Keep important content visible without sacrificing touch targets, focus indicators, or readable text.

Use overflow menus or collapsible navigation for secondary destinations when screen width or task priority warrants it. Maintain access to the primary workflow, current location, and common actions.

Test scrolling, sticky elements, dialogs, browser zoom, and safe areas. Preserve useful content order as regions reflow.

## 17. The five questions of imperial judgment

For each conspicuous pattern or effect, answer:

1. What user objective or product identity does this serve?
2. Why is this treatment appropriate for its role and location?
3. Which other element competes with it for attention?
4. How does it behave across states, screen sizes, and preferences?
5. What evidence supports retaining this design?

Choose retention, refinement, substitution, or removal based on the answers. Preserve expressive patterns that have a legitimate purpose. Record consequential tradeoffs in the implementation summary.

## 18. An actual workflow, because a manifesto ships nothing

1. Inspect the product and establish the task and baseline.
2. Inventory conventional patterns, their roles, and their current states.
3. Rank content and actions by importance to the user.
4. Establish a shared token system and responsive layout.
5. Refine existing components or introduce suitable reusable primitives.
6. Allocate effects through the judgment questions; resolve competing focal points.
7. Implement real interactions and required states.
8. Render representative screen sizes and inspect actual output.
9. Verify behavior, accessibility, and visual consistency; revise discovered defects.
10. Deliver the result with concrete evidence, known limitations, and meaningful changes.

During review-only work, identify issues by screen, component, user consequence, and suggested correction. Prioritize blocking functional or accessibility problems before decorative refinements.

## 19. The imperial audit

For significant changes, capture a baseline and candidate using equivalent data, content, task flows, and viewport conditions. Record intentional changes to content or functionality separately.

Inspect these dimensions:

| Dimension | Evidence |
| --- | --- |
| Hierarchy | Reading order, primary-action treatment, focal regions |
| Composition | Grid alignment, reflow, spacing and overflow |
| Coherence | Token use, icon family, peer component treatment |
| Effects | Gradient regions, elevations, transparency and motion roles |
| Accessibility | Keyboard, focus, accessible names, contrast and target sizing |
| Function | Real task completion, state transitions, errors and data integrity |
| Adaptation | Narrow and wide screens, zoom, long content, user preferences |
| Performance | Measurements on relevant rendering conditions where available |

Use screenshots and executable browser checks when available. Inspect rendered geometry and computed styles rather than relying only on source-code declarations. Compare representative task paths, including failure recovery.

Use effect counts as diagnostic evidence, rather than universal scores. A creative product may legitimately need more expressive treatments. A reduction in decoration demonstrates a change in styling, while usability requires separate evidence.

For visual review, evaluate the actual screenshot at ordinary reading size. Human testing provides stronger evidence of comprehension, trust, and aesthetic preference. Automated checks establish only the properties they measure.

## 20. Release gates

A candidate earns release when the relevant gates pass:

- Primary workflows remain available and function correctly.
- Reading and interaction order remain meaningful across supported viewports.
- Each visually dominant region has an identifiable product purpose.
- Component states are coherent and accessible under the intended standard.
- Essential text remains readable; semantic states communicate their meaning.
- Effects follow an intentional hierarchy and respect user preferences.
- Required loading, empty, error, success, and destructive states are covered according to scope.
- Measured findings and unresolved limitations are accurately reported.

Treat critical functional, security, and accessibility defects as release blockers. Treat visual preferences as decisions supported by the brief and evidence. Mark unavailable checks as pending and state their impact.

## 21. The relationship with other design skills

A feature-admission skill decides what belongs in the product. A component-craft skill defines how the admitted elements are built. A palette skill provides or constrains color choices. This skill governs the relationships among those elements, with conventional AI patterns available as legitimate material.

When another active instruction limits an effect or component, respect that boundary. When the brief explicitly authorizes a rich or conventional aesthetic, use the imperial audit to give it structure.

For the accompanying demonstration, see `tests/ui-fixture.html` and `tests/TEST-REPORT.md`. The fixture is illustrative, and its visual tokens are specific to its fictional product. Transfer the method rather than its exact appearance.

## 22. The emperor's last decree

Familiar patterns can be useful. Discipline gives them dignity. The interface earns its authority through the confidence, clarity, and control it gives the person using it.

*Rule the slop. Let the user rule the product.*
