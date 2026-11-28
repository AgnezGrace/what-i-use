---
name: fuck-the-navigation-bar
description: Design, implement, or audit contextual radial navigation, Ghost Orbit, adaptive arc menus, hidden navigation, and gesture-invoked action menus. Activate for requests involving touch-centered menus, collision-free icon placement, responsive spatial navigation, or replacing permanent bars with on-demand controls.
---
# Fuck the Navigation Bar

*The user came for the content. The controls can wait their turn.*

## 1. The doctrine

Build Ghost Orbit: an adaptive spatial navigation system whose controls appear near an intentional invocation point. The system supports a maximum of seven primary actions per invocation, preserves access to ordinary navigation, and gives content the available space when closed.

Treat this as a product-specific navigation pattern, rather than a universal replacement for visible navigation. Readers, canvases, galleries, and workspaces are good candidates. Public onboarding, high-stakes transactions, and frequent primary actions warrant visible alternatives.

The name is satire. User autonomy, discoverability, accessibility, and evidence are serious.

## 2. Read the room before drawing a circle

- Identify the product, primary tasks, target devices, input modes, and protected content.
- Inventory commands and destinations. Assign each a stable ID, accessible name, action handler, availability state, and risk classification.
- Keep critical actions, system navigation, and frequently used controls discoverable through a visible or reliably accessible route.
- Offer an ordinary button/list path with identical commands. A first-use hint may explain the gesture once; allow replay and dismissal.
- Preserve text selection, editing, links, native scrolling, pinch zoom, system edge gestures, and assistive technology.
- Ask about product intent when it changes behavior; choose reversible technical defaults yourself.

## 3. Architecture: one brain, several bodies

Separate these responsibilities:

```text
navigation/
  registry          # stable IDs, names, handlers, permissions
  geometry          # pure solver, no DOM or state changes
  input-controller  # pointer ownership, timers, cancellation
  state-machine     # open, select, dismiss, restore focus
  presentation      # native buttons, SVG, focus, layout
  fallback          # accessible list of the same registry entries
  tests             # geometry, gesture, rendering, regressions
```

Use a single command dispatcher for radial and list modes. Recheck command availability and authorization on activation. Preserve the application router, back stack, focus, and unsaved state. A hidden command is never an authorization boundary.

## 4. The finger is a coordinate, not a fortune teller

Use CSS pixels in a consistent coordinate system. Convert `clientX/clientY` into the menu's overlay coordinate space. Derive usable bounds from the actual viewport, safe-area insets, browser chrome as exposed by the platform, keyboard, and reserved application regions. Avoid mixing device pixels, screen pixels, CSS pixels, and document coordinates.

Prefer the direction from the invocation point toward the usable center. Treat the nine-region model as a conceptual illustration only; compute continuously.

- Left edge: prefer rightward expansion.
- Right edge: prefer leftward expansion.
- Top edge: prefer downward expansion.
- Bottom edge: prefer upward expansion.
- Corners: prefer the interior diagonal.
- Center: use an input-specific default and declared hand preference.

Detect input via pointer type, not merely viewport width. Touch and pen can exist on desktop. Mouse input can exist on mobile. Touch coordinates alone cannot reveal handedness or palm location. Support automatic, left, and right preferences. Treat hand exclusion geometry as an approximation, validate against actual grips, and offer overrides.

## 5. A circle is not a collision strategy

Define these independent quantities in CSS pixels:

| Quantity | Starting value |
|---|---|
| Icon glyph | 20–24 |
| Touch hit region | 48 × 48 |
| Mouse/keyboard hit region | 44 × 44 |
| Minimum hit-region gap | 8 |
| Viewport inset | 8, plus safe-area and focus requirements |
| Neutral radius | 30 touch; 18 mouse |
| Primary actions | 1–7 |
| Hold threshold | 320 ms |
| Pre-hold movement tolerance | 10 |
| Entry motion | 120–180 ms; immediate in reduced motion |

These are project defaults, not universal accessibility requirements. WCAG 2.2 AA has a 24 CSS pixel minimum target criterion with exceptions; this system intentionally chooses larger targets. Honor stronger platform or user requirements.

Let `a=(ax,ay)` be the invocation point, `r` the orbital radius, `theta` the initial angle, and `delta` the angular step.

```text
x[i] = ax + r*cos(theta + i*delta)
y[i] = ay + r*sin(theta + i*delta)
open arc: delta = spread/(n-1), when n > 1
full ring: delta = 2*pi/n, when n > 1
single item: delta = 0
```

For equal circular hit regions with diameter `D` and edge gap `g`, chord length must satisfy `2*r*sin(delta/2) >= D+g`. Thus a circular lower bound is `r >= (D+g)/(2*sin(delta/2))`. This is insufficient for square buttons. Use an exact footprint check or a conservative circumscribed-circle bound. Full rings must also validate first against last. Use radians internally.

For axis-aligned hit rectangles A and B, overlap with gap `g` exists when both are true:

```text
abs(A.x-B.x) < (A.w+B.w)/2 + g
abs(A.y-B.y) < (A.h+B.h)/2 + g
```

Test complete footprints, including focus clearance. Verify every pair, every viewport edge, each reserved rectangle, and the neutral zone. Treat the hand exclusion estimate separately from hard viewport constraints. The reference solver conservatively excludes a rectangular approximate palm region when a hand is declared. A target center outside a neutral radius alone is insufficient; account for its half-diagonal.

## 6. Geometry before paint

1. Measure usable bounds and the actual action count.
2. Resolve target dimensions, spacing, neutral radius, reserved regions, and input modality.
3. Compute preferred direction using the vector to the usable center; blend with a configurable touch bias.
4. Enumerate candidate arc spreads, rotations, and bounded radii. Handle one item and full-circle endpoints explicitly.
5. Reject candidates violating any hard constraint. A candidate must contain every requested action exactly once.
6. Score feasible candidates by proximity, direction deviation, occlusion estimate, reach, and stable ordering. Document the weights as tunable heuristics.
7. Choose deterministically. Keep action IDs in a stable semantic sequence; adapt the rotation rather than randomly shuffling functions.
8. Freeze positions and command mapping for the duration of the interaction.
9. Render only after validation. When viewport, keyboard, orientation, or permissions change mid-selection, cancel and allow reinvocation.

The reference solver uses bounded angular/radius sampling and exact rectangular collision checks. It is a heuristic, not a global optimizer. Failure to find a candidate means use fallback, rather than a proof that all possible layouts are infeasible.

## 7. Stop shrinking the damn buttons

Use a degradation ladder:

- Try a compact arc with the preferred rotation.
- Try alternate rotations, spreads, and larger radii within a reach budget.
- Optionally evaluate a translated visual center, two rings, or a compact grid; revalidate every footprint and gesture mapping. Keep the original invocation point separate from the visual center.
- Present a scrollable accessible command list when safe orbital placement is unavailable. Preserve every command, order, and permission.
- For more than seven actions, group by task or use a second-level list. Avoid silently dropping actions.

Glyph size may adapt independently for legibility and optical balance. Keep hit regions and spacing intact. Never solve a collision by overlapping invisible targets, disabling focus, or reducing controls below the established minimum.

## 8. Gestures are invitations, not traps

Default state machine:

```text
IDLE -> ARMING -> OPEN_HELD -> OPEN_TAP -> COMMIT -> IDLE
           |          |           |
           +----------+-----------+-> CANCEL -> IDLE
```

- Arm only on explicitly eligible surfaces, primary pointer, and intentional hold. Track pointer ID and initial position.
- During arming, movement beyond tolerance, early release, secondary touch, pointer cancellation, or loss of eligibility clears the timer without committing.
- Open once at the hold threshold. Use pointer capture where appropriate; cancellation and capture loss must have a defined cleanup path.
- During held selection, highlight only a valid hit region. Release over that region commits once; release away from all targets cancels, or release inside the neutral zone enters tap-select mode.
- Tap-select mode supports ordinary buttons, keyboard, and outside dismissal. Avoid dispatch on pointerdown.
- Suppress duplicate synthetic activation from the same gesture. Keep confirmation for destructive operations independent of the menu.
- Escape, outside press, focus loss where appropriate, page hide, resize, orientation change, and pointercancel cancel without action.

Use a native context menu or shortcut on desktop when appropriate. Override the browser context menu only on designated surfaces, and preserve the native menu elsewhere. Provide a visible accessible trigger and keyboard equivalent. For ordinary reading/scrolling surfaces, preserve browser touch handling; use tap-select when the browser takes ownership of a gesture. `touch-action: none` belongs only on deliberate non-scrolling gesture surfaces with an alternative for zoom and navigation. Changing it after pointerdown does not retroactively change the gesture negotiation.

## 9. An invisible menu must still be findable

Use native buttons with accessible names. Decorative SVG is hidden from assistive technologies. Use actual links for destinations when appropriate. A toggle announces expanded state; closed controls leave the tab order and accessibility tree. On open, move focus into the list or menu for keyboard users; on close, restore the prior meaningful focus. Provide a keyboard route to every command, Escape dismissal, and visible focus with sufficient clearance.

Choose a semantic dialog, disclosure, or menu pattern according to the actual interaction. A menu role requires its complete keyboard contract. A simple labelled group of native buttons can use ordinary Tab navigation. Never simulate a modal without managing background interaction and focus.

Use explicit confirmation or undo for irreversible actions. Keep visible cues where icon meaning is ambiguous, including labels in fallback and accessible names everywhere. Ensure contrast, reduced motion, high contrast modes, text scaling, and screen magnification. An invisible-only gesture is not an accessible interaction strategy.

## 10. Motion should follow geometry, not fight it

Use local SVG geometry and CSS tokens. Avoid adding a navigation library solely to draw circles. Keep the overlay independent from scroll layout, clipping ancestors, transformed containing blocks, and unintended stacking contexts. Reserve focus-ring padding. Use opacity-only entry or a validated animation path; moving hit regions during selection risks collisions. Reduce motion to immediate display when requested.

Use a single overlay at a time. Treat pointer positions as transient interaction data; avoid logging precise coordinates unless needed and explicitly justified. Dispose timers, capture, and event listeners on unmount.

## 11. The verification contract

Verify geometry using deterministic tests across anchors, sizes, input types, handedness, safe insets, and counts. Add randomized reproducible tests and impossible layouts. Assert full containment, gap, neutral clearance, reserved-region avoidance, no duplicates, stable order, finite values, and deterministic output. Include fallback reachability, rather than treating every fallback as failure.

Verify DOM bounds using real browser rendering; mathematical geometry alone cannot expose CSS overflow or focus clipping. Test touch and mouse, short tap, hold, scroll/move cancellation, drag selection, neutral release, outside dismissal, Escape, keyboard activation, rapid repeated use, resize, reduced motion, and native controls. Record actual results separately from proposed coverage. Test real devices, browser engines, assistive technology, and both hands before claiming ergonomic success.

Compare with conventional navigation using task completion, accidental activation, time, errors, discovery, reach, and repeat-use learning. A screenshot is not an ergonomic study.

Report each requirement as VERIFIED, FAILED, UNVERIFIED, BLOCKED, or NOT APPLICABLE with evidence. Hold a release recommendation when critical navigation, cancellation, accessibility, or action integrity is unverified. Provide an ordinary navigation alternative when the pattern fails usability evaluation.

## 12. Deliverables

Produce a command registry, pure solver, input controller, accessible overlay, fallback, tests, and a concise integration guide. Preserve existing working navigation until the replacement is verified. Use the supplied reference as a small laboratory, rather than copying its assumptions into every product. Disclose tradeoffs and remaining device-specific verification in plain language.

*The interface may disappear. The user's ability to use it must remain.*
