# Verification report

## Scope and environment

The reference implementation generates 26 static SVG icons using Python's standard library. Chromium 144.0.7559.96 rendered the exact generated HTML via Playwright. The harness used `set_content` in an offline browser context because direct file navigation was blocked by the environment's browser policy. The test therefore verifies self-contained rendering and tested interactions without HTTP(S) requests, rather than actual file-navigation permissions. Pillow inspected screenshots.

Configurations: 360 and 1280 CSS px viewport widths, DPR 1 and 2, light and dark themes. Each configuration renders 26 icons at 16, 20, 24, 32 and 48 CSS px (1,040 total icon instances). Four DPR-1 full-page screenshots are retained.

## Results

| Group | Passed / total |
|---|---:|
| Static registry and profile | 54/54 |
| Deterministic regeneration | 2/2 |
| Mathematics and generator parity | 48/48 |
| Negative profile / parameter checks | 17/17 |
| Browser configuration / offline requests / errors | 32/32 |
| Native control interaction | 64/64 |
| Raster, inherited color, contrast, silhouette | 3128/3128 |
| Total | 3345/3345 |

The raster checks compare each screenshot crop with its card background using a grayscale difference threshold of 18. They check visibility and a clear outermost pixel border at the sampled threshold. This is a practical clipping-risk check, rather than proof of exact vector bounds. Contrast is calculated from computed foreground and background colors, rather than from every antialiased edge pixel. The 24 px silhouette check catches identical binary masks within each configuration; it does not prove originality or comprehensibility.

The gear generator was checked for 5–12 teeth, vertex counts, radii, mean center and invalid parameters. Browser/Python geometry parity was checked at the two endpoints. Native button naming, keyboard focus and activation, target size, filtering, theme state and the gear slider were exercised. Static checks reject the listed unsupported markup and malformed parameter examples. Regeneration twice matched the prior bytes of all 26 assets, registry and catalog.

## Revision during verification

The first completed run passed 3339/3345 checks. The Library symbol failed six raster edge-clearance checks at selected DPR-1 sizes. Its third book outline extended to x=22; the revised outline extends to x=21 and uses a slightly narrower spine. The entire suite was rerun and all checks passed. A desktop light screenshot was visually inspected; the small samples reveal the expected limitations of proportional scaling for dense artwork.

## Limitations

- The same agent authored the skill, reference assets and tests. This is implementation verification, rather than an independent evaluation of an agent before and after skill activation.
- Only Chromium was exercised. Firefox, Safari, WebView, real mobile touch, zoom, forced colors, reduced motion, clipboard permissions and screen-reader announcements remain unverified. The catalog has a manual clipboard fallback but the harness did not exercise it.
- The restricted XML checker is a regression check for owned geometry, not a full SVG grammar validator, upload sanitizer, or security audit. It cannot establish security against every SVG input.
- Recognizability, aesthetic quality, optical balance and brand differentiation require human review; numeric checks alone cannot establish them. No production dependency graph or bundle was measured. No universal supply-chain protection is claimed.

Reproduce using `python tests/test_icons.py`. See `results.json` for individual checks.
