# Verification report — Ghost Orbit

## Executed tests

- Node: 2181 deterministic layout cases, including 80 reserved-area cases and one deliberately impossible case; three malformed-input rejection checks.
- 1561 orbital placements satisfied independent rectangle separation, bounds, neutral clearance, action identity, and deterministic repeat checks. 620 cases returned a list fallback, including the deliberately impossible case. A fallback is a valid safety outcome, not a proof of mathematical impossibility.
- Chromium / Python Playwright: 152 named checks passed across 360×740 touch, 320×568 touch with reduced motion, and 1280×800 mouse. Touch gestures were dispatched through Chromium CDP, not a physical touchscreen.
- Browser checks included short tap, hold, pre-hold movement, drag release, tap selection, Escape, pointer cancellation, keyboard list activation, focus restoration, outside dismissal, native text input, actual DOM bounds, fallback reachability, resize, offline operation, reduced motion and fallback touch scrolling. Release outside is tested in configurations where the four-action orbit opens.
- Screenshots are real Chromium output. The screenshots show a deliberately simple laboratory canvas rather than a full product.

## Corrections during development

The initial sampled solver returned 939 list fallbacks. Narrower candidate spreads (60 and 75 degrees) and a larger bounded radius (260 CSS px) reduced this to 620 on the identical grid. The target dimensions and minimum gap remained unchanged. The dedicated gesture surface was separated from the list overlay to avoid blocking native list scrolling; a touch-scroll check was added and passed.

## Limits

The solver is a bounded heuristic; its 620 fallback outcomes are intentional and may include feasible arrangements not found by sampling. The 260px radius is a configurable engineering limit, not evidence of comfortable thumb reach. Hand occlusion is a crude declared-hand rectangle, not actual sensing. The 1, 4, and 7 action counts, selected insets, and sampled anchors do not exhaust every layout. The demo does not implement translated centers, multi-ring placement, a production router, or real authorization. The neutral marker is illustrative, and the sample canvas has no application-reserved rectangles; those are tested in the pure solver. Screen-reader behavior, Safari, Firefox, WebView, real devices, multi-touch variations, magnification, and human discoverability/ergonomics remain unverified. Normal scrolling document integration must be tested separately. This is a reference implementation and controlled self-test, not an independent evaluation of how an AI model follows the skill. The skill sets additional production requirements beyond the reference implementation.

## Reproduction

Run `node tests/geometry.test.js` and `python tests/browser_test.py`. JSON files contain exact recorded counts and browser check names.
