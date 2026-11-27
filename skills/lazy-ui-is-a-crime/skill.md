---
name: lazy-ui-is-a-crime
description: Build and refine product-native interfaces with intentional components, coherent visual identity, SVG-based iconography, economical copy, accessible interactions, and smooth motion. Apply when creating, reviewing, or modifying user-facing software and when generic interface styling causes repeated design corrections.
---

# Lazy UI Is a Crime

> No emoji as interface icons. No untouched default components. Build an interface that belongs to the product.

A crime against the user’s time, figuratively speaking. The real cost of lazy interface design is paid by the person who repeatedly explains what a finished interface should look and feel like. Spend design effort once, preserve the decisions, and carry them through the product.

## 1. Operating mandate

- Treat visual design as part of implementation quality.
- Deliver product-native components as the standard outcome.
- Translate the product's purpose into a recognizable visual language.
- Make every visible element earn its space through function, orientation, feedback, or identity.
- Preserve user intent throughout implementation, revision, and extension.
- Resolve routine design decisions autonomously using the product context.
- Match the degree of craftsmanship to the scope, platform, and available implementation resources.
- Preserve accessibility, correctness, security, and performance as foundational requirements.

The product is the interface's source of identity. The component library is an implementation resource.

**Reject the default.** A functional scaffold is the beginning of design work. Ship a deliberately designed product instead of a framework demonstration.

## 2. Activation and scope

Activate for interface design, frontend implementation, application screens, dashboards, websites, responsive layouts, component refactors, visual polish, and UI reviews.

For an existing product, inspect its established visual system before changing it. For a new product, derive a compact visual system from its purpose and audience.

For a narrowly scoped fix, apply the skill to the affected area and preserve unrelated behavior. For an explicit redesign, establish a coherent system across the requested surfaces.

Honor explicit user requirements, platform constraints, and established project conventions. When these conflict, surface the concrete tradeoff and choose the smallest coherent resolution.

## 3. Start with the product

Before writing interface code, establish:

| Dimension | Question |
|---|---|
| Purpose | What outcome brings a person here? |
| Audience | What knowledge, devices, and interaction patterns are typical? |
| Context | Is the product a business tool, casual application, creative workspace, editorial experience, or specialized utility? |
| Frequency | Which actions happen repeatedly? |
| Identity | Which visual characteristics make this product recognizable? |
| Constraints | What does the platform, existing code, or accessibility requirement demand? |

Use the actual content and workflows to guide the design. A banking application, a comic reader, and a creative editor deserve different expressions of the same engineering quality.

Record the relevant answers in the working plan or existing design system. Keep internal reasoning separate from user-facing copy.

## 4. Component ownership

### 4.1 The default is raw material

A component exported by a framework represents a starting point. Its final appearance belongs to the product.

Inspect buttons, inputs, selects, tabs, navigation, dialogs, drawers, popovers, dropdowns, tooltips, cards, notifications, toggles, tables, and empty states.

For each component, define the following where relevant:

- Shape, density, typography, surface, border, and elevation.
- Icon family and icon placement.
- Default, hover, focus-visible, pressed, selected, disabled, loading, success, and error states.
- Keyboard behavior, touch behavior, responsive placement, and accessible name.
- State transitions and motion behavior.

Use a shared component implementation and tokens to express these decisions consistently. Originality comes from the visual language and interaction design, rather than a fresh implementation of every primitive.

### 4.2 Choose the appropriate implementation layer

| Situation | Preferred implementation |
|---|---|
| Simple visual control | Semantic native element with product-specific styling |
| Complex interaction | Accessible headless primitive with a custom visual layer |
| Established project library | Theme tokens, variants, slots, and component overrides |
| Platform-owned interaction | Native platform control with supported theme integration |
| Specialized product behavior | Purpose-built component with explicit state and interaction tests |

Suitable resources include native HTML and CSS, CSS utility libraries, headless UI libraries, component kits, design tokens, and framework-native primitives. Evaluate their suitability and licensing in the project context.

Rebuilding the behavior of a mature select, dialog, or combobox carries keyboard and accessibility obligations. Reuse reliable behavior; own the visible presentation.

Retain a platform-owned file picker, permission prompt, or operating-system interaction when its security, accessibility, or reliability depends on that platform. Style the surrounding entry point.

### 4.3 The component admission gate

Before shipping a control, confirm that it:

1. Serves a defined user action or information need.
2. Fits the established visual tokens and nearby controls.
3. Uses familiar interaction semantics.
4. Exposes complete relevant states.
5. Works with the required input methods.
6. Remains maintainable through shared primitives.

A screenshot that resembles an untouched component-library demo signals unfinished theming when the project calls for an original visual identity.

## 5. Iconography: use actual interface assets

Emoji belong to human expression, authored content, and explicitly emoji-oriented features. Interface commands belong to a coherent icon system.

For navigation, actions, status indicators, settings, toolbars, and system feedback, choose:

- SVG icons from a consistent, appropriately licensed icon library.
- Original SVG assets when the product requires distinctive symbols.
- CSS shapes for simple geometric indicators.
- Platform-native icon assets when appropriate to the target environment.

Lucide, Phosphor, Material Symbols, Heroicons, and similar resources are implementation options. Select a family based on the product rather than mixing them casually.

Align view boxes, optical size, stroke weight, corner treatment, and filled or outlined conventions. Use `currentColor` or theme-aware assets where supported.

Prefer familiar symbols for universal actions. Use accessible names for icon-only controls and visible text when the meaning requires it. Decorative SVGs should be hidden from assistive technology; interactive semantics belong to the containing control.

Use semantic text and multiple cues for important statuses. Color, an icon, and animation each have their place; clarity determines the combination.

Reserve bespoke illustration and symbolic branding for meaningful identity. Build an icon system, rather than a collection of unrelated drawings.

## 6. Visual direction

Choose a direction deliberately. The following profiles are starting points, with the product brief taking precedence.

### 6.1 Business: flat and matte

Use stable, quiet surfaces and controlled contrast. Let typography, alignment, spacing, and semantic color establish hierarchy.

- Flat or subtly layered solid backgrounds.
- Restrained neutral palette with a purposeful accent.
- Moderate corner radii and precise geometry.
- Predictable alignment and consistent data density.
- Fine borders or restrained elevation for meaningful boundaries.
- Clear tables, forms, and work states.
- Motion that communicates state while keeping work efficient.

Prefer contrast through surface and typography over decorative effects. Reserve saturated colors for brand expression or meaningful statuses. Keep persistent chrome visually subordinate to the work.

### 6.2 Casual: elegant and bold

Use confident composition, personality, and memorable typography. Casual design can have strong visual character while remaining composed.

- Deliberate display typography alongside legible functional type.
- Confident solid color fields and intentional accent placement.
- Distinctive silhouettes, custom imagery, or art direction where useful.
- Strong focal points supported by breathing room.
- Expressive components anchored in familiar interaction patterns.
- Refined motion that contributes to the product's rhythm.

Use color harmony and composition as the primary expression tools. Reserve neon, glow, gradients, and glass effects for a brief that specifically benefits from those materials. Elegance and boldness come from confident decisions, rather than effect intensity.

### 6.3 Other contexts

Editorial products prioritize reading rhythm and typography. Creative tools prioritize the canvas and efficient controls. Utilities prioritize immediate outcomes and reliable feedback. Match materials, density, motion, and hierarchy to the actual context.

### 6.4 Establish the token contract

Define or reuse a small set of semantic tokens for:

- Background, surface, raised surface, border, text, muted text, accent, focus, and status colors.
- Font families, type scale, weights, and line heights.
- Spacing, control sizes, radii, and elevation.
- Icon size and stroke convention.
- Motion duration, easing, and reduced-motion behavior.

Support all required themes and screen sizes. Place component-specific exceptions in the component system with a clear functional reason.

### 6.5 Stop serving sepia by default

Use cool or genuinely neutral surfaces as the starting palette when the brief leaves temperature open. Treat cream, amber, beige, warm gray, sepia, and yellow-tinted whites as explicit art-direction choices. Respect an existing warm brand identity or a requested warm palette. Preserve semantic warning colors and authentic content imagery.

Derive palette choices from the actual product and explicit preferences rather than assumptions about age. Evaluate the combined effect of backgrounds, text, imagery, overlays, and lighting. A cool accent over a yellow canvas still reads warm.

### 6.6 Typography is a design decision

**No default typography.** Choose type deliberately, even when the final choice is a system font.

- Inspect the user's stated font preferences and the product's established type system within the available context.
- Select families for the reading task, language coverage, character shapes, and intended visual identity.
- Pair expressive display type with legible functional type when the product benefits from contrast.
- Define fallbacks with compatible metrics, practical font weights, and supported writing systems.
- Check licensing, offline availability, loading cost, and layout stability before introducing a dependency.
- Verify long titles, numbers, localized strings, and small controls in the rendered interface.

For a new product, choose an intentional stack. For an existing product, retain its type identity or apply the requested change coherently. A purposeful platform font remains a valid choice for a native interface.

## 7. Labels: earn the pixels

**Cut the filler.** Keep the meaning, reclaim the filler. Every piece of visible text competes with the user's work. Make it useful.

### 7.1 Visible copy admission

Retain text that provides a control's meaning, a necessary instruction, a value, a constraint, a consequential warning, orientation, or actionable feedback.

Consolidate duplicated headings, ornamental category labels, repeated explanations, obvious hints, redundant icon captions, and filler descriptions. A heading should introduce content that benefits from the heading. A subtitle should add information the title leaves unresolved.

Use direct action verbs where visible button text is useful. Prefer the user's vocabulary to internal technical language. Place relevant help near the point of need.

### 7.2 Choose the correct representation

| Context | Preferred representation |
|---|---|
| Familiar compact toolbar action | Recognizable icon, accessible name, contextual tooltip if helpful |
| Ambiguous or unfamiliar action | Concise visible text or icon plus text |
| Navigation where destinations need identification | Visible destination names where necessary for recognition |
| Form field | Persistent associated label and relevant constraints |
| Destructive or consequential action | Explicit wording and appropriate confirmation |
| Status or error | Clear meaning and recovery guidance where applicable |
| Decorative section eyebrow or duplicate hint | Reclaim the space for the content |

Accessible names and visible labels serve different purposes. Keep programmatic names for icon-only controls. Preserve persistent labels for form fields; placeholders serve as examples. Retain visible words where discoverability or comprehension depends on them.

Tooltips supplement accessible controls and should support the relevant input methods. Essential guidance deserves a persistent or readily discoverable presentation.

### 7.3 Read the interface aloud

Inspect the rendered screen as though each visible word occupies a cost budget. Identify repeated concepts and assign each one an authoritative location. Review the resulting screen with a first-time user perspective and a frequent-user perspective.

## 8. Motion: polish with purpose

Smooth transitions help a person understand where an element came from, what changed, and where attention belongs.

Use motion for:

- Press and hover feedback.
- Menu, popover, drawer, and dialog entry and exit.
- Selection and state changes.
- Expand and collapse behavior.
- Context-preserving navigation when appropriate.
- Progress and completion feedback for real operations.

Starting ranges, tuned to the actual component:

| Interaction | Duration |
|---|---|
| Press, hover, focus-adjacent feedback | 100–160 ms |
| Toggle or small state change | 120–200 ms |
| Menu or popover | 150–220 ms |
| Drawer or dialog | 200–320 ms |
| Large contextual transition | 220–400 ms |

Use easing suited to direction and distance. Fast feedback and a controlled deceleration are good defaults for entering surfaces. Prefer explicit transitioned properties, particularly transform and opacity for visual motion. Animate layout dimensions only when necessary, with performance validation.

Keep interactions interruptible. Update functional state promptly, then let motion communicate the result. Maintain focus behavior and correct state during rapid interactions. Match exit animations with actual removal or hidden-state timing.

Honor reduced-motion preferences. Provide equivalent state changes through immediate updates or brief, appropriate fades. Keep focus visibility and meaningful feedback available in every motion mode.

Reserve continuous motion for genuine activity, progress, or an explicitly requested ambient experience. Use static composition for ordinary resting states.

## 9. Layout and interaction quality

- Establish a dominant task or content area on each screen.
- Group related controls by purpose and proximity.
- Match density to task frequency, device size, and reading requirements.
- Give touch controls adequate target size and spacing; meet the applicable platform and accessibility requirements.
- Preserve meaningful keyboard order and visible focus.
- Maintain text legibility under resizing, localization, and theme changes.
- Handle real data, empty states, loading, errors, long text, and overflow.
- Use progressive disclosure for secondary operations and infrequent settings.
- Keep navigation and high-frequency actions predictable across screens.
- Make feedback proportional to the action and preserve recovery paths.

### 9.1 When the toolbar becomes a junk drawer

Keep the primary task visible. Group secondary actions into a compact overflow control or contextual menu. Use a hamburger button for a collapsed navigation hierarchy when screen width or task priority justifies it. Use an ellipsis menu for secondary commands associated with a specific object or screen.

- Keep frequent destinations readily discoverable; use visible navigation when space and frequency justify it.
- Give the menu a clear accessible name, expanded state, visible focus, and an appropriate dismissal path.
- Preserve logical grouping and predictable item order inside the disclosure.
- Keep critical actions and active status visible where the task requires them.
- Compare the extra interaction cost against the space recovered and the frequency of the hidden task.

A menu organizes secondary work. A bloated menu simply relocates the clutter.

A polished screen is a working screen under realistic conditions.

## 10. Dialogs and overlays: style them properly

Choose the surface according to the task. Inline controls suit local edits; popovers suit lightweight contextual choices; drawers suit related secondary tasks; dialogs suit focused decisions or interactions requiring modality.

Design the surface, backdrop, spacing, content hierarchy, and actions using the same visual system as the host screen. Use an accessible dialog primitive or native dialog semantics for modality. Provide an accessible title, initial focus appropriate to the content, focus containment where modal, Escape behavior where appropriate, and focus restoration on dismissal.

Define dismissal behavior according to data loss and consequence. Use explicit actions when a decision requires commitment. Provide a coherent transition and retain usable interaction at small viewport sizes.

Use ordinary navigation or a full screen for workflows that benefit from space and persistent context.

## 11. Agent workflow

### Inspect

Read the relevant existing screens, components, dependencies, style tokens, and implementation constraints. Identify generic defaults, duplicated copy, inconsistent icons, and interaction friction in the affected scope.

### Decide

Select the visual profile and the existing or new token contract. Identify component reuse, accessible primitives, icon assets, meaningful labels, and motion needs. Resolve routine choices using the product context; ask for input when a consequential product decision remains ambiguous.

### Implement

Build a representative component or screen using the selected direction. Connect real actions and states. Extend through shared components, then verify the affected neighboring surfaces. Preserve business logic and data contracts.

### Inspect the result

Render the interface in a browser, emulator, simulator, or target platform when available. Review actual screenshots and exercise interactions. Distinguish measured observations from code-based predictions.

### Persist decisions

Use the project's existing design system, theme files, component conventions, or local agent guidance to preserve durable decisions within the authorized scope. Reuse them on subsequent screens. Keep changes focused and respect the user's requested file boundaries.

### Report

Summarize the implementation, verification results, and any meaningful tradeoff or untested behavior. Keep the report proportional to the task. Give the user a finished result rather than another assignment of routine design decisions.

### Carry the lesson forward

When the user corrects a reusable design choice, translate it into a durable rule inside the authorized project scope: a theme token, shared component, design-system entry, or agent instruction. Apply it to the relevant family of components. Recheck the affected screens. Treat the user's corrections as engineering inputs rather than disposable chat messages.

## 12. Verification protocol

Check the affected interface against its baseline or established design language. Use the same task and representative content when comparing alternatives.

| Gate | Evidence |
|---|---|
| Visual ownership | Rendered components follow the product token contract |
| Icon coherence | Functional icons use the selected asset system and accessible names |
| Copy economy | Each visible label has an identified purpose |
| Contextual style | Materials, typography, density, and accents suit the product; palette temperature follows the brief |
| Disclosure | Secondary controls are grouped and primary actions remain accessible |
| State completeness | Relevant interaction states are implemented and exercised |
| Accessibility | Keyboard flow, focus, naming, contrast, and target sizes are checked |
| Responsive behavior | Representative narrow and wide layouts handle realistic content |
| Motion | State transitions are smooth, interruptible, and respect reduced motion |
| Functional integrity | Primary tasks, errors, and relevant recovery paths still work |
| Maintainability | Shared styling and behavior have a clear implementation home |

Review screenshots for visual issues and use automated interaction checks for functional behavior. Test keyboard access and touch-oriented layout. Include accessibility tooling and human review when available. For performance-sensitive motion, inspect frame behavior on representative hardware or report the measurement gap.

Prioritize failed correctness, accessibility, and primary-task gates ahead of cosmetic polish. Treat visual coherence as a completion gate for requested design work. Record exceptions with their technical or product rationale.

## 13. Regression scenarios

Use relevant cases from this set when testing a new or revised interface:

| Case | Expected agent decision |
|---|---|
| Generic component kit in a business dashboard | Theme the kit and retain its reliable behavior; use matte surfaces and readable data hierarchy |
| Casual reader with generic emoji navigation | Use coherent SVG navigation, strong typography, and intentional solid colors |
| Familiar icon action with a duplicate caption | Choose the compact icon control if its meaning is clear; retain its accessible name |
| Unfamiliar icon action | Add concise visible meaning and preserve the accessible name |
| Form with placeholder-only identification | Add persistent associated labels and useful examples |
| Custom dialog request | Apply the product surface styling to accessible modal behavior |
| Operating-system file picker | Preserve the platform interaction and style its entry point |
| User requests a vivid neon-themed experience | Implement the explicit art direction with coherent tokens and legible controls |
| Unrequested yellow-tinted neutral palette | Choose cool or neutral surfaces; preserve semantic warning colors |
| Crowded mobile navigation | Collapse secondary destinations into an accessible navigation menu |
| Untouched framework typography | Select a purposeful family and verify rendering, coverage, and fallback |
| Reduced-motion preference | Preserve feedback and behavior using reduced or immediate transitions |
| Existing product with a small bug fix | Preserve the established system and limit changes to the affected scope |

## 14. Completion contract

A completed interface expresses its product identity through deliberate component styling, economical language, coherent iconography, functional states, and refined motion. Its structure supports accessibility, reliable operation, and future maintenance.

Make these choices part of the implementation from the first screen. The user's next message should be about the product's next meaningful improvement, rather than the same visual corrections again.
