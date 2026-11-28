---
name: fuck-it-use-math
description: Generate original, dependency-free visual icons and simple geometric assets using mathematics, native SVG and CSS. Activate when designing icons, adding UI controls, replacing icon dependencies, creating vector assets, or establishing a product-specific icon system. Preserve accessibility, familiar semantics, and justified existing dependencies.
---

# Fuck It, Use Math

*Import expertise. Generate geometry. Own your identity.*

## 1. The Circle Does Not Need a Package Manager

Use native browser geometry for simple interface assets. Treat a third-party visual dependency as an engineering decision with a maintenance cost, a trust boundary, and a measurable benefit. Prefer a small, locally owned icon registry for new products that require ordinary interface symbols.

Preserve useful established icon systems in existing products until an authorized migration has a clear benefit. Evaluate the actual dependency graph before claiming a dependency has been removed. A bundled library reduces runtime network dependency; its installation and build process still has supply-chain exposure. Local geometry reduces one class of risk, while source control, build integrity, and secure delivery remain essential.

Keep mature libraries for complex behavior, accessibility infrastructure, authentication, cryptography, and other specialized domains where their value justifies their use. Apply this skill to visual geometry, rather than reimplementing security primitives or browser behavior.

## 2. The Trigger

Activate when a task involves:
- Creating, replacing, or styling navigation, toolbar, action, status, or product icons.
- Adding an icon package, CDN stylesheet, external icon font, or simple decorative graphic.
- Establishing a consistent icon family, custom SVG assets, or procedural brand geometry.
- Supporting offline operation or reducing visual-asset dependencies.
- Reviewing inconsistent icon weights, clipping, poor alignment, or unclear symbols.

Scope work to the requested surface. Explain meaningful migration cost and compatibility risks before broad replacement. Retain the established product vocabulary wherever users already recognize it.

## 3. The Decision Contract

| Need | Preferred tool | Reason |
|---|---|---|
| Divider, dot, simple rectangle, chevron | CSS or SVG | Small native geometry |
| Functional symbol | Static local SVG | Scalable, testable, reusable |
| Repeated radial or symmetric shape | Build-time generator | Shared parameters and reproducibility |
| Dynamic chart or data-driven geometry | SVG or canvas with accessible equivalent | Geometry follows data |
| Complex artwork | Reviewed local asset | Preserves intended artistic quality |
| Existing mature icon set | Retain or migrate deliberately | Avoid needless churn |

Compare implementation size, runtime requests, maintenance, semantic clarity, and accessibility. Treat the smallest sufficient solution as the default. Use measured bundle results for performance claims.

## 4. First Meaning, Then Mathematics

1. Identify the action, object, status, or destination represented by the icon.
2. Check the local registry for an existing equivalent.
3. Select a recognizable visual metaphor appropriate to the domain and locale.
4. Choose an icon family and optical size.
5. Derive geometry from shared dimensions and a small number of primitives.
6. Render at actual intended sizes, in every supported theme and state.
7. Verify the accessible name and native control semantics.
8. Register the asset under a stable semantic identifier.

Treat originality as a family-level visual property: corner shape, stroke, proportions, and terminal treatment. Preserve established meanings for search, close, download, back, and destructive actions. Pair unfamiliar icons with visible text; use labels wherever ambiguity has a meaningful cost. Distinguish upload from download, expand from external navigation, and delete from archive.

## 5. A Geometry Constitution

Establish explicit tokens. These are starting values for a new outline family, rather than universal platform requirements.

| Token | Default | Purpose |
|---|---:|---|
| Coordinate system | 24 × 24 | Shared viewBox |
| Center | (12, 12) | Symmetry reference |
| Stroke | 1.75 | Default line weight |
| Safe painted inset | 1 | Minimum viewport clearance |
| Common centerline extent | 3–21 | Main drawing area |
| Rect corner radius | 2 | Family corner character |
| Stroke caps / joins | round / round | Consistent terminals |
| Small / standard / large | 16 / 24 / 32 CSS px | Render targets |
| Touch target | 44 × 44 CSS px | Product comfort target |

Use a 24-unit viewBox independent of CSS display size. Set width and height together to preserve aspect ratio. For outline artwork, declare fill="none", stroke="currentColor", stroke-width, stroke-linecap and stroke-linejoin. Use fill="currentColor" for filled variants. Use explicit fill-rule when holes or compound paths require it.

Keep the total painted bounds within the viewBox, including half the stroke, cap extension, joins, and transforms. With round joins and caps, a centerline margin at least stroke/2 plus desired clearance is a useful conservative starting point. Miter joins may exceed that margin; account for the miter limit. Verify actual rasterized pixels as well as geometric bounds.

Use a consistent baseline and optical center. A circle, square, and triangle with identical bounds may have different apparent size. Compare visual weight at actual size, then apply small documented corrections. Preserve recognizable negative space at 16 px. Use dedicated optical variants for dense shapes where scaling alone fails.

## 6. Pythagoras Pays Rent

### Coordinate normalization

For a source rectangle (x0, y0, w, h), target usable width W and height H, compute s = min(W/w, H/h). With target center (cx, cy):

```
x' = cx + s * (x - x0 - w/2)
y' = cy + s * (y - y0 - h/2)
```

Require positive finite dimensions. Include stroke and transformed extrema in the source bounds when fitting painted artwork. Preserve the original aspect ratio. Round generated coordinates only at serialization; verify the resulting shape.

### Distance and unit vectors

For A=(ax,ay), B=(bx,by), let d = hypot(bx-ax,by-ay). When d > 0, define u = ((bx-ax)/d,(by-ay)/d), and perpendicular n = (-uy,ux).

An arrowhead at B uses endpoints B - L*u ± W*n, with positive head length L and half-width W. Draw the shaft and arrowhead as a path. Handle coincident endpoints explicitly before dividing.

### Polar coordinates and radial symmetry

```
x = cx + r * cos(theta)
y = cy + r * sin(theta)
theta_i = theta0 + 2*pi*i/n
```

Angles are radians; screen y increases downward. Use this to derive regular polygons, suns, radial marks, orbit points and gear silhouettes. Require integer n >= 3 for polygons and positive finite radius. Start at -pi/2 for an upward first vertex.

A stylized gear uses four vertices per tooth with alternating root and tip radii. For tooth i and substep j in 0..3, theta = -pi/2 + (i+(j-1.5)/4)*2*pi/n. Use the tip radius at j=1,2 and root radius at j=0,3. The result is a visual settings symbol, rather than a mechanical involute gear. Maintain clearance between the hub and the tooth roots.

### Rotation and reflection

Rotate around (cx,cy):

```
x' = cx + (x-cx)*cos(a) - (y-cy)*sin(a)
y' = cy + (x-cx)*sin(a) + (y-cy)*cos(a)
```

Reflect around vertical center: x' = 2*cx - x. Reflect around horizontal center: y' = 2*cy - y. Mirror directional navigation for RTL where the meaning follows reading direction. Preserve physical directions, media symbols, and culturally fixed marks where appropriate.

### Curves and arcs

Quadratic Bezier: B(t) = (1-t)^2 P0 + 2(1-t)t P1 + t^2 P2.

Cubic Bezier: B(t) = (1-t)^3 P0 + 3(1-t)^2 t P1 + 3(1-t)t^2 P2 + t^3 P3, for 0 <= t <= 1.

Use SVG Q and C commands for smooth edges. Align incoming and outgoing control vectors for tangent continuity at a smooth join. Evaluate extrema through derivative roots in [0,1] or inspect browser geometry; control points alone provide only a conservative bound.

Use A rx ry rotation largeArcFlag sweepFlag x y for elliptic arcs. Set the flags according to direction and intended sweep. Split full circles into two arcs or use circle; a single arc with identical endpoints cannot represent a complete circle. Validate positive radii and handle degenerate endpoints.

### Boolean shapes and interpolation

Use compound paths with evenodd fill for holes, or correctly oriented nonzero winding. Construct simple unions from shared boundaries; use a vetted offline geometry tool for complex boolean operations when justified. Avoid unintended overlapping stroke seams.

Interpolate numeric parameters with lerp(a,b,t)=a+(b-a)*t, t clamped to [0,1]. Morph paths only when command topology is compatible; otherwise crossfade or transform. Use reduced-motion alternatives for animated icons.

## 7. The Pixel Is the Judge

At display size S, one viewBox unit maps to S/24 CSS px. A 1.75-unit stroke becomes 1.17 CSS px at 16 px and 2.33 CSS px at 32 px. Device pixels additionally depend on DPR and zoom.

For a horizontal or vertical stroke of integer device-pixel width, align its painted edges to integer device-pixel boundaries where practical: centerline on an integer for even widths and on a half integer for odd widths. Account for transform, DPR, and zoom. Treat this as an optical aid, rather than a universal snapping rule. Curves and diagonals naturally use antialiasing.

Use proportional strokes by default. Consider vector-effect="non-scaling-stroke" for diagrams whose line width must stay constant under transformation; inspect actual behavior before adopting it for icons. Use optical-size variants to address dense small icons. Compare icons at 16, 20, 24, 32 and 48 CSS px, at representative device pixel ratios.

## 8. Build a Family, Spare the User

Organize by semantic role:
- Navigation: home, back, forward, menu, external destination.
- Actions: search, add, close, edit, save, delete, copy, download, upload.
- Objects: document, folder, image, library.
- State: check, warning, information, lock, visibility.
- Product: settings, layers, custom brand marks.

Use one shared outline family; introduce filled or selected variants only when the state benefits from them. Preserve state information in accessible properties. Reserve decorative geometry for branding and illustration. Emoji can remain legitimate user content, while functional interface iconography follows the product family.

## 9. The Registry Is the Source of Truth

Suggested architecture:

```
design-system/icons/
  geometry/           # pure functions and shared constants
  generate.py         # deterministic build-time generation
  registry.json       # semantic IDs, geometry, metadata
  assets/             # reviewed standalone SVGs
  component/          # optional local typed wrapper
  tests/              # static, render, accessibility, integration
```

Use one stable ID per meaning and explicit aliases when migrating. Keep geometry separate from button behavior and themes. Generate deterministic output with bounded numeric precision, stable ordering, and finite values. Commit source and generated assets; check regeneration in CI. Select only used icons for production when bundling is beneficial. Keep the generator out of the runtime for fixed artwork.

Use local inline SVG when theme inheritance is needed, or a local image when a separate cached asset is appropriate. An SVG inside an img element has its own document context; parent currentColor does not automatically propagate. A same-document symbol sprite may reduce repeated markup; use stable unique IDs, local fragment references, and test accessible naming on the instance. Avoid introducing a new runtime just to render geometry.

## 10. SVG Is Code Wearing a Nice Suit

Treat SVG markup as executable-capable content in document contexts. For owned static icons, enforce a deliberately narrow allowlist of geometry tags and attributes. The reference generator uses svg, path, circle, rect, line, polyline, polygon and ellipse, with literal geometry and paint tokens.

Use a structured serializer and trusted constants. Bound numeric parameters, node counts, file size and path length. Reject non-finite values, unexpected namespaces, DTDs, entities, processing instructions, event-handler attributes, scripts, foreignObject, external references, arbitrary styles, embedded images, and URL-based paint in this restricted profile. The SVG namespace URI is a namespace identifier rather than a network dependency.

Apply a maintained sanitizer or reject untrusted uploaded SVG when the feature requires accepting user assets. A static allowlist for generated icons is not a general-purpose SVG sanitizer. Avoid inserting arbitrary user strings into innerHTML. Preserve the application's content-security policy and other trust boundaries.

Review generated files, track provenance and licensing, pin any justified build/test tools, and verify the final asset graph. Local files still need trustworthy source control, build and delivery.

## 11. A Button Is More Than a Drawing

Use native button and link elements for interaction. Keep decorative SVG hidden from assistive technology using aria-hidden="true" and focusable="false"; provide the accessible name on the parent control. For a meaningful standalone image use appropriate alternative text or an explicit image role and name. Avoid duplicate announcements.

```html
<button type="button" aria-label="Search" class="icon-button">
  <svg aria-hidden="true" focusable="false" viewBox="0 0 24 24"
       fill="none" stroke="currentColor" stroke-width="1.75"
       stroke-linecap="round" stroke-linejoin="round">
    <circle cx="10" cy="10" r="6"/>
    <path d="M14.24 14.24 L20 20"/>
  </svg>
</button>
```

```css
.icon-button {
  display: inline-grid;
  place-items: center;
  inline-size: 44px;
  block-size: 44px;
  color: var(--ink);
  background: transparent;
  border: 1px solid transparent;
  border-radius: 10px;
}
.icon-button svg { inline-size: 24px; block-size: 24px; flex: none; }
.icon-button:focus-visible { outline: 2px solid currentColor; outline-offset: 2px; }
```

Keep the 44 px product target distinct from the visual drawing. WCAG 2.2 AA target-size minimum is 24 CSS px with specified exceptions; the larger comfort target is a design choice. For essential visual information, verify at least 3:1 contrast with adjacent colors where WCAG non-text contrast applies. Preserve focus indicators, disabled semantics, keyboard activation, and accessible state such as aria-pressed or aria-expanded. Use visible labels for ambiguous or consequential controls. Avoid relying solely on color to communicate state.

Keep focus rings outside clipped artwork and provide space between targets. Test forced colors, dark/light themes, hover, pressed, disabled, and reduced motion. A tooltip may supplement a meaningful name; touch and keyboard users need equivalent access.

## 12. Prove the Math, Then Prove the Pixels

Run checks proportionate to the icon system:
1. Parse each SVG and validate the restricted static profile.
2. Verify finite geometry, unique IDs, declared viewBox, and allowed paint values.
3. Regenerate twice and compare bytes or hashes.
4. Exercise parametric bounds, invalid inputs, symmetry, and degenerate geometry.
5. Render every asset at intended sizes and device pixel ratios in supported themes.
6. Inspect raster bounds, clipping, empty artwork, and unintended identical outputs.
7. Inspect optical balance, recognizable meaning, stroke weight, small-size gaps, and family consistency by viewing actual screenshots.
8. Verify names, keyboard activation, focus, target dimensions, state, and contrast on actual controls.
9. Run with external requests blocked; verify rendering and interaction. Inspect source and final bundles for external icon references and imports.
10. Record browser version, test dimensions, results, exceptions, and untested targets.

A numeric pass supports a defined claim. Visual interpretation and usability require separate review. Pixel differences alone establish neither quality nor originality. Use real user evaluation for unfamiliar symbols and independent review for high-impact controls.

## 13. Acceptance Gate

| Status | Meaning |
|---|---|
| VERIFIED | Relevant check executed and evidence retained |
| FAILED | Observed mismatch |
| UNVERIFIED | Evidence still absent |
| BLOCKED | Environment or access prevents verification |
| NOT APPLICABLE | Excluded with a reason |

Deliver the icon registry, source geometry, generated assets, usage example, and verification report. For a small feature, provide only the relevant subset. Keep critical failures visible and unresolved checks explicit. Describe removed dependencies only after inspecting the actual project graph and build artifact.

Reference implementation: `generate.py`, `registry.json`, `icons/`, `catalog.html`, and `tests/`. The reference uses Python standard-library generation and native browser rendering; its test harness uses external development tools solely for verification.

**Fuck it, use math. Then check the result at sixteen pixels.**
