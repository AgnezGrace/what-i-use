---
name: it-compiles-so-what
description: Verify actual behavior through risk-based tests; use for implementation, debugging, regression checks, integration, and release validation.
---

# It Compiles. So What?

*The compiler is a witness to a narrow claim. It is not the customer.*

## Mandate
Prove user-visible behavior and critical invariants with reproducible evidence. Distinguish code presence, build success, test success, and actual target-environment behavior.

## Start with outcomes
Translate critical journeys into preconditions, actions, expected results, and observable postconditions. Include persistence, side effects, permissions, and failure behavior when applicable. Identify the exact revision, configuration, data, and environment under test.

## Select tests by risk
| Layer | Evidence |
|---|---|
| Static/build | Syntax, types, lint, packaging and configuration checks |
| Unit | Boundary logic, pure functions, validation, edge conditions |
| Integration | Real module contracts, persistence, services, permissions |
| End-to-end | Primary journeys through the actual entry point |
| Failure/recovery | Interruption, malformed data, resource errors, restart |
| Target | Supported browser, OS, device, install or deployment behavior |

Use the lowest layer that reliably proves each claim and add higher-layer checks for integration risks. Choose realistic fixtures and representative production-like configurations with test credentials. Use mocks for controlled fault injection or unavailable systems; explicitly identify what remains untested by a mock.

## Test the product, not the story
- For each critical journey, verify the resulting observable state and relevant side effects.
- For a save, reopen data; for an export, parse or inspect the exported artifact; for a download, verify bytes, integrity, completion, and recovery where applicable.
- Exercise empty, invalid, boundary, and repeated actions. Test concurrent use where the system supports it.
- Exercise appropriate authorization boundaries, cancellation, timeout, and failure states.
- Test UI interactions through their real controls where feasible, including keyboard access, readable feedback, supported viewports, and navigation.
- Measure performance against explicit workload and device assumptions; disclose proxy environments and limits.
- Add regression checks for reproduced defects; verify that the test detects the original failure when safe and practical.
- Keep tests isolated, deterministic where feasible, and independent of real user data.

## Evidence integrity
Run the commands you cite. Record exit codes, relevant output, exact scope, environment, and artifact or revision identity. Separate actual executions from planned, simulated, or inspected checks. Record flaky behavior and repeated attempts; investigate rather than hide instability. Preserve failing assertions and distinguish harness errors from product errors.

Test counts describe executed assertions or cases, rather than universal quality. A passing mock, screenshot, build, or static inspection supports only its own claim. Use a negative control or targeted mutation when practical to establish that a critical test detects the intended defect.

## Status protocol
- VERIFIED: observed evidence meets the stated criterion in the declared environment.
- FAILED: observed behavior contradicts the criterion.
- UNVERIFIED: evidence is missing or insufficient.
- BLOCKED: a named capability, credential, device, or dependency prevents verification.
- NOT APPLICABLE: a recorded product-specific reason establishes irrelevance.

## Verification gate
All applicable critical journeys and invariants require VERIFIED status before a release-ready recommendation. An unresolved critical failure or missing evidence blocks that recommendation. Document acceptable residual noncritical risks for the authorized release owner. Provide safe partial results when the environment prevents further testing.

## Hand-off
Report what works, what failed, what remains unknown, and the shortest route to further evidence. Use plain language first, with reproducible technical details available alongside it.

*Green build lights are lovely. Working software is better.*
