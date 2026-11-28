# Blueberry — Premium Web Design System

> Quiet precision. Confident simplicity. Every detail earns its place.

Version: 1.0.0  
Scope: responsive product websites, storefronts, documentation, and lightweight web applications.  
Status: independent design specification with a locally tested reference implementation.

## 01. The Blueberry doctrine

- Put the user's task and the product ahead of interface decoration.
- Express premium quality through alignment, typography, material consistency, and predictable behavior.
- Give each section one dominant purpose, each control one clear responsibility, and each state one recognizable appearance.
- Treat negative space as a structural resource. Use it to separate unrelated information and group related elements.
- Use familiar interaction semantics with an intentionally styled visual layer.
- Preserve the host product's identity, content, functionality, accessibility, and explicit user preferences during adoption.
- Apply the smallest relevant subset of this system. A landing page, an editor, and a checkout have different densities.
- Treat the following numerical specifications as Blueberry defaults, adjustable when measured user needs justify a change.

## 02. Product modes

| Mode | Surface | Density | Dominant object |
|---|---|---|---|
| Bloom | Neutral light, spacious sections | Low | Product imagery and editorial text |
| Midnight | Obsidian and blue-black | Low to medium | Product silhouette and contrast |
| Ledger | Flat matte, restrained decoration | Medium | Tasks, records and actionable data |
| Grove | Reading-oriented, neutral | Medium | Text and navigation |

Select a mode according to the job. Keep shared interaction patterns stable across modes. A marketing hero belongs to Bloom or Midnight; a working dashboard benefits from Ledger. Explicit product color preferences take precedence over the default accent.

## 03. Color architecture — Berry pigments

All values are sRGB HEX. The scale is a collection of solid tones; gradients remain optional image or editorial treatments.

| Token | Light | Dark | Role |
|---|---|---|---|
| `--bb-canvas` | #FFFFFF | #101114 | Page background |
| `--bb-surface` | #F4F5F7 | #1B1E24 | Section and quiet panel |
| `--bb-raised` | #FFFFFF | #252A33 | Dialog and distinct surface |
| `--bb-ink` | #17191D | #F5F6F8 | Primary text |
| `--bb-muted` | #505661 | #BAC2CF | Supporting text |
| `--bb-line` | #D5D9E0 | #3C4655 | Decorative separators |
| `--bb-control` | #737D8C | #8795A8 | Meaningful control boundaries |
| `--bb-accent` | #2159C5 | #8CB4FF | Accent, links and primary fill |
| `--bb-on-accent` | #FFFFFF | #101C33 | Primary fill text |
| `--bb-hover` | #1849AA | #ABC8FF | Primary hover |
| `--bb-pressed` | #123984 | #729DEB | Primary press |
| `--bb-focus` | #2159C5 | #A6C7FF | Focus indicator |
| `--bb-danger` | #B3263B | #FF9EA9 | Destructive and error text |
| `--bb-success` | #176746 | #83DBB0 | Success text |
| `--bb-warning` | #795000 | #F3C675 | Warning text |
| `--bb-disabled` | #565E6B | #A7B0BE | Disabled text |
| `--bb-disabled-bg` | #E6E9EE | #333B48 | Disabled fill |

### Blueberry tonal scales

| Scale | 900 | 700 | 500 | 300 | 100 |
|---|---|---|---|---|---|
| Berry | #10234A | #1849AA | #3976E2 | #8CB4FF | #E9F0FF |
| Slate | #17191D | #39414F | #737D8C | #BAC2CF | #F4F5F7 |
| Fir | #102D22 | #176746 | #398B65 | #83DBB0 | #E6F7EE |
| Cherry | #39151F | #8E253C | #C64C61 | #FF9EA9 | #FCE9ED |
| Mineral | #13262C | #28555D | #528B92 | #A4C8CD | #E8F3F4 |

### Color rules

- Begin with canvas, ink and one accent. Introduce additional colors when a semantic or product need exists.
- Use a neutral cool baseline; warm whites, gold, sepia and vivid gradients require an explicit creative rationale or request.
- Use surface transitions and spacing before adding borders, shadows or tint.
- Reserve danger for consequential actions and actual errors. Pair state color with text or a recognizable symbol.
- Use semantic tokens in component CSS. Change themes through token values rather than individual component overrides.
- Use `color-scheme` to coordinate native form controls and scrollbars with the theme.
- Establish text contrast of at least 4.5:1 for normal text and 3:1 for qualifying large text; aim higher for long reading.
- Establish at least 3:1 contrast for required control boundaries, meaningful icons and focus indicators against adjacent colors.
- Decorative lines may have lower contrast when the interface remains understandable without them.
- Verify text over media at every crop, theme and state. Add a controlled scrim or move text onto a solid surface when necessary.
- Confirm hover, pressed, disabled, selected and validation states separately. Contrast belongs to a pair of colors, rather than a single swatch.

## 04. Typography — Blueberry Type

Use a legally available typeface with a neutral, humanist or contemporary grotesk character. Establish a single family for most interfaces, with an optional editorial face when the content requires it.

| Family alias | Implementation choice | Role |
|---|---|---|
| Berry Sans | `system-ui, "Segoe UI", Arial, sans-serif` | Fast native system experience |
| Berry Studio | Inter, self-hosted under its applicable license, then Berry Sans | Consistent cross-platform presentation |
| Berry Editorial | A licensed Source Serif 4 or similar | Optional long-form or editorial accent |
| Berry Code | `ui-monospace, monospace` | Code and technical identifiers |

Use the user's preferred family when provided. The aliases are conceptual names, rather than distributed font binaries. Obtain webfont rights before packaging any font. Keep system font fallback available. Use WOFF2, appropriate subset and `font-display: swap` for licensed assets. Measure layout shift and verify glyph coverage. Avoid loading weights that the interface never uses.

| Role | Size range (rem; 16px base) | Line height | Weight | Tracking |
|---|---|---|---|---|
| Display XL | 2.75–5.5 | 1.02–1.10 | 650–700 | -0.045em |
| Display L | 2.25–4 | 1.08–1.14 | 600–700 | -0.035em |
| Section title | 1.75–2.75 | 1.12–1.2 | 600–700 | -0.025em |
| Card title | 1.25–1.75 | 1.2–1.3 | 600 | -0.015em |
| Lead | 1.125–1.5 | 1.4–1.55 | 400–500 | -0.01em |
| Body | 1–1.125 | 1.5–1.65 | 400 | 0 |
| Control | 0.875–1.0625 | 1.25–1.4 | 500–600 | 0 |
| Supporting | 0.875–1 | 1.45–1.6 | 400 | 0 |
| Caption | 0.75–0.875 | 1.4–1.5 | 400–500 | 0.005em |

Suggested fluid rule: `font-size: clamp(2.75rem, 1.4rem + 5vw, 5.5rem)`.
Use available real font weights; variable ranges apply only to families that support them. Keep body copy comfortably around 45–75 characters per line. Give long text natural wrapping and preserve the language's script and diacritics. Allow zoom and text resizing; avoid fixed-height text containers. Preserve semantic heading order independently of visual size. Use concise sentence-case copy; reserve uppercase for short functional identifiers where meaningful. Keep labels that communicate required fields, unfamiliar actions, or safety information. Eliminate copy that repeats an already clear heading or control.

## 05. Spacing, grid and responsive composition

Spacing scale in px: 4, 8, 12, 16, 20, 24, 32, 40, 48, 64, 80, 96, 128.
Use rem equivalents for scalable content spacing. Use a small set of shared tokens instead of arbitrary offsets.

| Viewport | Grid | Outer gutter | Grid gap | Section vertical spacing |
|---|---|---|---|---|
| 320–599px | 4 columns | 16–20px | 12–16px | 48–64px |
| 600–959px | 8 columns | 24–32px | 16–24px | 64–80px |
| 960–1439px | 12 columns | 40–48px | 24–32px | 80–112px |
| 1440px+ | 12 columns | 48–64px | 24–32px | 96–128px |

Use a 1200px content maximum for product pages, 1440px for wider comparisons, and 720px for long-form prose. Full-bleed backgrounds can surround a constrained inner grid. Use logical properties, `minmax(0, 1fr)`, `min-inline-size: 0`, fluid images, and `overflow-wrap` for unusually long content. Set breakpoints where the actual content becomes crowded rather than detecting brands of devices.

### Hierarchy of layout

1. Orchard: page shell, global navigation and footer.
2. Branch: independent section with one purpose.
3. Cluster: layout group, such as comparison grid or action group.
4. Berry: reusable functional component.
5. Seed: a primitive element or token.

Each level owns its own spacing. Parent layouts manage inter-component gaps; a component manages internal padding. Avoid child margins that accidentally double section spacing. Keep semantic DOM order equivalent to the reading order. Avoid absolute positioning for core text, navigation, and critical controls. Reserve it for isolated decoration that has an explicit containing block.

### Responsive and overlap contract

- Use natural document flow for main content; fixed and sticky elements require reserved space or an explicit overlay role.
- Prefer flex wrapping for action groups and CSS Grid for structured content. At narrow widths, collapse to a single column when text or hit targets would crowd.
- Keep page reflow at 320 CSS px; intentional horizontal tables and galleries have local scroll containers, with cues and keyboard access.
- Use intrinsic image dimensions or `aspect-ratio` to reserve media space; use `object-fit` appropriate to preserving product details.
- Add `scroll-margin-block-start` to anchor targets under sticky headers; allow scroll padding for focused elements.
- Verify long translations, 200% text resizing, 400% browser zoom, landscape, safe areas and narrow mobile widths on target devices.
- Keep visible controls from overlapping their neighbors, clipping labels, or extending beyond their designated region.
- Treat overflow at the page level as a defect to diagnose. Global `overflow-x: hidden` is not a substitute for fixing the offending element.

## 06. Button family — Berry Controls

Button dimensions are minimums. Content can grow naturally. Sizes are based on action context, rather than on arbitrary visual variety. Related sibling actions share the same size and baseline.

| Variant | Min height | Inline padding | Font | Radius | Use |
|---|---:|---:|---:|---:|---|
| Seed | 28px visual / 44px hit | 10px | 13px | 999px | Compact utility, inside a 44px nonoverlapping target |
| Bud | 36px visual / 44px hit | 14px | 14px | 999px | Local toolbar, inside a 44px target |
| Berry | 44px | 20px | 15–16px | 999px | Default action |
| Bloom | 52px | 24px | 17px | 999px | Hero CTA, major next step |
| Harvest | 56px | 28px | 17px | 14px | Checkout or full-width mobile completion |
| Utility icon | 44 × 44px | 0 | 20px icon | 50% or 12px | Close, menu, next, previous |
| Form action | 44–48px | 20px | 15–16px | 10–12px | Submit, save, cancel |
| Text link | 44px target | 0–8px | Inherited | 4px | In-flow navigation; inline prose links use text geometry |

Prefer 44px targets as a Blueberry product policy, with larger targets for high-frequency actions. WCAG 2.2 AA has a 24 CSS px minimum target criterion with defined exceptions; the Blueberry 44px target is an intentional stronger default. The compact visual treatment uses an actual larger outer button, not overlapping invisible pseudo-element hit regions. Keep at least 8px between adjacent targets where practical.

| Priority | Treatment | Meaning |
|---|---|---|
| Primary | Solid accent with on-accent text | Main action of the current section or task |
| Secondary | Transparent surface with visible border | Complementary action |
| Tertiary | Text or quiet tonal fill | Low priority navigation or utility |
| Destructive | Danger treatment, explicit action wording | Irreversible or harmful operation |
| Toggle | Persistent selected state plus semantic state | Binary or selectable preference |

Use native buttons for actions and real links for destinations. Icon-only actions require accessible names and a visible label or tooltip when meaning is unfamiliar. Buttons with text should name the resulting action, such as Save changes or View details. Group actions by purpose. Prefer one primary action per decision context; multiple sections may each have a primary CTA. Make disabled states understandable; explain an important blocking condition nearby when needed.

### Button interaction state machine

| State | Visual response | Behavior |
|---|---|---|
| Rest | Stable geometry, flat surface | Ready |
| Hover | Color shift on fine hover pointers | Preview interactivity |
| Press | Solid color shift | Immediate acknowledgement |
| Focus visible | 2px outline with 3px clearance | Keyboard and assistive navigation |
| Selected | Persistent fill, border or check | `aria-pressed` or correct native selected state |
| Pending | Stable width, spinner or text | Guard duplicate actions, announce progress |
| Disabled | Disabled token | Native disabled or correctly guarded aria-disabled |
| Error | Inline reason, persistent until corrected | Preserve input and expose recovery |

State precedence: disabled or pending guard activation; selected remains distinct; hover and press change appearance; focus remains an independent accessible layer. Keep border thickness, padding and box dimensions consistent across pointer states. For a stateful action, use logical state rather than CSS focus as the selected indicator.

## 07. The edge contract — clean press and focus rendering

A dark rim or square shadow on click can originate from separate mechanisms. Reproduce the artifact before changing CSS. Inspect the actual component and ancestor chain in developer tools, including pseudo-elements and computed styles.

| Symptom | Likely cause | Repair |
|---|---|---|
| Rim persists after mouse release | `:focus` or framework focus ring | Separate `:focus-visible` from pointer-only focus; preserve a fallback |
| Square flash during touch | Browser tap highlight or native appearance | Keep intentional native feedback or replace locally with accessible pressed feedback |
| Outer ring stops at card edge | Ancestor overflow, paint containment or clipping | Move the control outside the clipped media layer; reserve focus clearance |
| Shadow follows a rectangular pseudo-element | Inconsistent radii or filter geometry | Inherit radius and inspect the layer that actually paints the shadow |
| Border jumps on click | Border width/padding changes | Keep geometry stable and change paint only |
| Shadow appears twice | Competing component and utility rules | Define a single owner of focus and elevation |
| Flicker during transform | Compositing, scaling or fractional pixels | Remove unnecessary transforms and filters; test actual target engine and DPR |
| Ring hidden behind sticky UI | Overlay or scrolling geometry | Reserve scroll clearance and correct stacking order |

### Separate paint responsibilities

- Outer shell owns radius, background, optional elevation and focus clearance.
- Inner media crop owns `overflow: hidden` and image clipping only.
- Control owns press, selected and focus styling. Keep the interactive control and its outline outside the media crop.
- A scroll region owns scroll overflow; reserve at least the outline width plus offset on all relevant edges (8px default).
- Inspect `overflow-x` and `overflow-y` computed values: mixed axes can produce a scrolling or clipping container unexpectedly.
- Inspect `clip-path`, `mask`, `contain: paint`, `filter`, `transform` and stacking contexts along the ancestor path. Raising `z-index` alone cannot escape an ancestor clip.
- Use `outline` for focus and `box-shadow` for elevation. Avoid using a press shadow as the sole feedback or focus indicator.
- Keep hover and active border radius stable. Use background changes for press by default; avoid `transition: all` and unnecessary forced GPU layers.
- Apply `-webkit-tap-highlight-color: transparent` only to specifically styled controls with reliable replacement feedback and visible keyboard focus. Leave ordinary links and input controls with appropriate feedback. This is a nonstandard browser-specific property.
- Preserve keyboard focus, text-input focus, forced-colors behavior, and visible programmatic focus when it is appropriate. Avoid blanket removal of outlines or blur-on-click scripts.

### Reference CSS for clean controls

```css
.bb-button {
  box-sizing: border-box;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-block-size: 44px;
  padding: 10px 20px;
  border: 1px solid transparent;
  border-radius: 999px;
  background: var(--bb-accent);
  color: var(--bb-on-accent);
  font: inherit;
  font-weight: 600;
  box-shadow: none;
  cursor: pointer;
  -webkit-tap-highlight-color: transparent;
  transition: background-color 160ms ease, color 160ms ease;
}
@media (hover: hover) and (pointer: fine) {
  .bb-button:hover:not(:disabled) { background: var(--bb-hover); }
}
.bb-button:active:not(:disabled) { background: var(--bb-pressed); }
.bb-button:focus { outline: 2px solid var(--bb-focus); outline-offset: 3px; }
@supports selector(:focus-visible) {
  .bb-button:focus:not(:focus-visible) { outline: none; }
  .bb-button:focus-visible { outline: 2px solid var(--bb-focus); outline-offset: 3px; }
}
.bb-button:disabled { background: var(--bb-disabled-bg); color: var(--bb-disabled); cursor: default; }
.bb-shell { border-radius: 24px; overflow: visible; }
.bb-media { border-radius: 20px; overflow: hidden; }
.bb-actions { display: flex; flex-wrap: wrap; gap: 12px; padding: 8px; }
@media (prefers-reduced-motion: reduce) { .bb-button { transition: none; } }
@media (forced-colors: active) {
  .bb-button { border-color: ButtonText; }
  .bb-button:focus-visible { outline-color: Highlight; }
}
```

Use the focus-only override for button-like controls; inputs retain a visible focus affordance regardless of pointer. In constrained layouts where exterior clearance is impossible, design a measured inset indicator with sufficient area and contrast instead of clipping the exterior ring. Verify against the actual adjacent backgrounds. The sample provides a practical focus treatment, rather than a blanket claim of WCAG conformance.

### Edge regression procedure

1. Reproduce at the original viewport, device pixel ratio, browser, theme and input type.
2. Capture rest, hover, mouse-down, mouse-up, focus-visible, blur and touch states. Use real input events rather than adding a fake CSS class alone.
3. Inspect outline style, radius, border widths, shadow, transforms and computed ancestor overflow.
4. Compare control bounds across states. Confirm that neighboring controls and page geometry remain stable.
5. Place a control near a rounded media crop and near a scroll-region edge; tab to it and verify a complete focus indicator.
6. Test modal and sticky header contexts, keyboard traversal, rapid repetition, text input and reduced motion.
7. Check rendered pixels at representative edges and inspect screenshots at DPR 1 and 2 (plus actual target hardware).
8. Repeat in Chromium, Firefox and WebKit or the actual embedded WebView. Record engines and versions that were available; mark missing environments unverified.
9. Preserve a regression fixture and report the specific root cause and evidence. Treat a CSS change as a candidate fix until the original symptom is reproduced and resolved.

## 08. Surface geometry and depth

| Token | Value | Role |
|---|---|---|
| Radius S | 8px | Small fields and supporting controls |
| Radius M | 12px | Forms, utility control, compact panels |
| Radius L | 20px | Product tile and image crop |
| Radius XL | 24–32px | Large feature panel, modal |
| Radius pill | 999px | Short standalone actions |
| Elevation 0 | none | Default sections, cards and buttons |
| Elevation 1 | `0 8px 28px rgb(16 24 40 / 10%)` | Popover or floating surface |
| Elevation 2 | `0 20px 64px rgb(16 24 40 / 18%)` | Modal |

Use dark theme shadows only when meaningful; a contrasting surface or border may communicate depth better. Outer and inner radii should be visually concentric when padding permits. Prefer a flat layout over a card collection. Cards are appropriate for independent content objects, not every line of text. Glass effects belong to a small number of purposeful floating surfaces, with an opaque readable fallback and verified contrast. Avoid material effects on dense working surfaces.

## 09. Navigation — Orchard and Branch

- Global header: 56px minimum desktop/mobile; center or align items to the content grid. Keep only primary destinations visible.
- Product local bar: 52–64px minimum; use a sticky bar only when navigation or purchase actions benefit from persistence.
- Keep global and local navigation semantically distinct and avoid two overlapping sticky headers. If both must remain sticky, calculate combined offsets.
- Mobile: use a real menu button with `aria-expanded` and controlled navigation; prioritize one or two frequent actions outside the menu.
- Preserve a route's active indication using `aria-current` and a persistent visual cue. Use links for navigation.
- Use breadcrumbs for real depth, not decoration. Use search when the information structure warrants it.
- Provide a skip link, logical tab order and visible focus. Close expanded menus on selection or Escape and restore focus appropriately.
- Let translated navigation wrap or switch to a menu before it collides with other controls.

## 10. Page patterns

### Bloom — product landing

Header → editorial hero → product media → benefit sections → comparison or proof → final relevant action → footer.
- Hero: one clear heading, short lead, one or two actions, and a large product visual. Give the visual real space rather than placing it behind unreadable text.
- Large sections may alternate neutral surfaces. Keep their inner content aligned to the same grid.
- Feature rows use image/text splits or editorial blocks. Equal cards fit comparable content; varied spans express genuine priority.
- Product imagery must be owned or licensed and appropriate to the actual product. Use original illustrations for placeholders, identify demonstrations honestly, and reserve image dimensions.
- Keep the price and terms clear when commerce is involved. Use factual proof rather than invented numbers or badges.

### Ledger — working application

Header or sidebar → page heading and primary action → work area → contextual details.
- Prefer aligned lists, tables and forms to nested decorative cards. Optimize frequent tasks for efficient scanning.
- Use a compact toolbar with grouped actions. Preserve persistent primary controls; move low-frequency actions to an overflow menu when necessary.
- Keep status, validation and recovery near the affected object. Use empty states only when the relevant content is absent.
- Preserve state ownership in the domain or feature layer; presentation components display it and emit events.

### Grove — documentation

Navigation tree → article heading → readable body → related navigation.
- Constrain long-form content. Provide a table of contents for genuinely long articles.
- Collapse the sidebar at narrow widths without changing article reading order. Keep code and tables in local scroll regions.

## 11. Forms, selection and feedback

- Use visible labels for inputs, explicit required and optional states where needed, suitable input types and autocomplete attributes.
- Minimum input height: 44px; form body text: 16px where practical; padding: 12–16px; radius: 10–12px.
- Associate help and error text with its input. Announce changes appropriately and preserve user input after validation errors.
- Use native checkbox, radio and select behavior where possible; style their visual shells with semantic states intact.
- Use toggles for immediate binary settings, radios for exclusive choices, checkboxes for independent choices, and buttons for actions.
- Reserve toasts for short feedback that remains understandable; persistent errors and consequential decisions need a persistent surface.
- Show meaningful pending states with stable geometry; completion means the underlying operation completed.

## 12. Overlays — Canopy

Use a native modal dialog or a proven accessible dialog foundation. Keep implementation behavior separate from visual styling.
- Dialog width: 440–560px for simple decisions, up to 720px for structured editing; cap to viewport minus 32px and allow content scrolling.
- Dialog radius: 24px; padding: 24–32px; use elevation 2 or a contrasting border.
- Modal overlay: neutral black at roughly 40–55% opacity, calibrated to the underlying theme.
- Use the browser top layer where appropriate. Focus moves to the appropriate initial element, stays within modal interaction, and returns to the trigger when closed.
- Provide accessible title, suitable description, close control and Escape behavior appropriate to the task.
- Keep the background inert while modal. Avoid overlapping simultaneous modals; use an internal step or close the first safely.
- Separate dialog content scroll from outer paint. Reserve focus clearance; sticky action rows require scroll clearance and must not conceal controls.
- Place popovers near their trigger with viewport collision handling; use a modal or inline disclosure when available space is insufficient.
- Preserve native scrolling and user zoom; account for virtual keyboards and safe-area insets on target devices.

## 13. Motion — Berry Flow

| Event | Duration | Preferred property |
|---|---:|---|
| Press or hover | 100–180ms | Background, color, opacity |
| Small disclosure | 160–240ms | Opacity, limited transform |
| Menu or dialog | 200–300ms | Opacity, translate |
| Section entrance | 300–450ms | Opacity, restrained movement |

Use `cubic-bezier(.2,.8,.2,1)` as a general entrance curve and `ease-out` for short feedback. Keep content available without animation. Honor reduced motion and replace large motion with immediate or subtle state changes. Keep hit geometry stable. Animate a dedicated visual layer instead of transforming the entire interactive region. Prefer explicit transition property lists. Avoid scroll hijacking, forced wait times, and autoplay that obstructs the task. Measure smoothness on target hardware; a configured duration alone is not a performance guarantee.

## 14. Icons and imagery — Berry Glyphs

Use original SVG or a licensed coherent icon family. Typical icon size: 16px supporting, 20px controls, 24px navigation, 32px feature accents. Use a consistent viewBox and stroke system (1.5–2px at 24px), rounded joins where appropriate, `currentColor`, and optical alignment. Decorative glyphs are hidden from assistive technology; standalone meaningful icons have accessible names. Choose recognizable symbols instead of emoji for core interaction. Keep labels when symbols alone are ambiguous. Use imagery to express product character rather than generic stock decoration. Provide meaningful alt text for informative images and empty alt text for purely decorative imagery.

## 15. Implementation architecture — The Orchard

Suggested framework-neutral organization; adapt it to the host project's conventions rather than forcing a rewrite.

```text
src/
  app/                  # route composition, app shell, providers
  features/             # product-specific behavior and state
  ui/
    primitives/         # Button, Icon, Text, Input
    patterns/           # Dialog, Navigation, ProductTile, FormGroup
    layouts/            # Container, Stack, Grid, Section
  styles/
    tokens.css          # semantic values and themes
    base.css            # box model, typography, focus baseline
    utilities.css       # limited compositional helpers
  assets/               # owned/licensed images and glyphs
  tests/                # visual, functional, accessibility regression
```

Dependency direction: routes compose features and layouts; features compose patterns; patterns compose primitives; primitives consume tokens. Domain logic stays out of style primitives. Shared state has one authoritative owner; local disclosure state stays local. Use explicit component APIs for size, variant, disabled, loading and selected. Centralize token values and state styling. Avoid parallel versions of a button for each page. Use semantic HTML as the base, with behavior enhanced where necessary.

### CSS ownership and stacking

Order: tokens → base → layout → components → intentional utilities → documented local exceptions. Use CSS cascade layers only with an integration strategy for external styles; ordinary unlayered rules outrank normal layered rules. Keep specificity low and inspect generated utility conflicts. Avoid pervasive `!important` and broad wildcard reset rules. Use scoped component classes or the host's established encapsulation. Define a stacking scale: content 0, sticky 10, local popover 20, global navigation 30; native top-layer dialogs sit outside this ordinary scale. Treat transformed ancestors as possible stacking and containing-block boundaries. Avoid arbitrary z-index escalation. Use a single overlay manager when the product requires multiple overlay types.

## 16. Accessibility and performance contract

- Target WCAG 2.2 AA for applicable web content; document product-specific exceptions, and verify manually plus automated tooling.
- Verify keyboard navigation, focus visibility and non-obscured focus, meaningful names, semantics, input errors, contrast, reflow, text zoom and reduced motion.
- Use visible focus indicators that contrast with adjacent colors and retain adequate clearance; test forced colors.
- Support pointer, touch, keyboard and assistive technology. Avoid relying on hover alone for access to information.
- Respect user zoom, system preferences and text settings. Keep essential content in the semantic DOM.
- Reserve image space, use responsive media and defer noncritical offscreen assets. Prioritize the meaningful hero image rather than preloading every resource.
- Load only required font subsets and weights. Avoid unnecessary large animation libraries and global event handlers.
- Measure LCP, INP and CLS in representative conditions; common good field targets are 2.5s, 200ms and 0.1 respectively at the 75th percentile. Treat these as field goals, not results inferred from a local screenshot.
- Establish product-specific resource budgets before adding costly effects. Test real mobile hardware, slow networks and offline behavior where applicable.

## 17. Agent adoption sequence

1. Inspect existing UI, user preferences, routes, components, tokens, dependencies and known bugs.
2. Choose relevant Blueberry mode and density. Document a compact palette, type scale, grid, control size and focus plan.
3. Map each section and action to a purpose; remove redundant visual wrappers while retaining necessary meaning and behavior.
4. Implement tokens and primitives first; compose one complete representative flow before broad rollout.
5. Inspect rendered states across responsive sizes. Compare existing behavior and preserve unrelated functionality.
6. Diagnose edge artifacts using the procedure in section 07; avoid speculative browser hacks.
7. Verify semantics, contrast, overflow, interaction, focus, reduced motion, and target browser behavior.
8. Report verified results, unresolved defects, and unavailable environments. Obtain authorization before publishing where required.

## 18. Acceptance gates

| Gate | Required evidence |
|---|---|
| Identity | Consistent tokens, type and component variants |
| Hierarchy | Clear section purpose and task priority |
| Geometry | No unintended page overflow or control collision at tested sizes |
| Press | Stable bounds and intentional feedback during and after activation |
| Focus | Complete, contrasting indicator during keyboard navigation |
| Interaction | Actual links/actions, valid state changes, modal and menu behavior |
| Accessibility | Relevant automated checks plus manual keyboard and assistive checks |
| Motion | Reduced-motion alternative and no task obstruction |
| Compatibility | Tested engines and devices recorded; missing targets explicit |
| Maintainability | Single component and token ownership, documented exceptions |

Use VERIFIED, FAILED, UNVERIFIED, BLOCKED and NOT APPLICABLE with evidence and scope. A browser fixture proves only its tested behavior. A production implementation requires project-specific testing and visual review.

> Premium is the absence of unnecessary friction, expressed through disciplined form and reliable behavior.
