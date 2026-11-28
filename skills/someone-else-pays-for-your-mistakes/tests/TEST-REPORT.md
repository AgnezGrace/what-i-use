# Reference test report

## Scope and result

The Python standard-library reference tests ran successfully: 66/66 checks passed (49 stage-gate checks and 17 SQLite transaction checks). All data, identities, financial effects, evidence strings and provider reconciliation records are synthetic. No external services or live accounts were used.

The gate checks cover three exposure stages, missing or failed critical gates, absent evidence, justified versus unjustified N/A, mismatched evidence stage, explicit authorization and a malformed stage. The SQLite fixture checks atomic rollback, duplicate request behavior, conflicting request IDs, authorization, positive integer amounts, insufficient funds, balancing entries, reconciliation mismatches and persistence after reopen.

## Limits

The gate tests validate a deterministic reference policy with predefined inputs; the program cannot assess the truth of evidence strings, legal applicability, actual authorization, staffing, human qualifications or residual risk. The ledger is a tiny educational fixture with global request IDs and simulated identities, not a production accounting or payment service. It does not implement real authentication, provider callbacks, concurrency stress, currency handling, dispute operations or external settlement. The reconciliation input is synthetic. The 18 written agent scenarios are not independent model experiments. No legal or clinical certification is implied. Real operational readiness requires evidence from the actual organization, systems, qualified reviewers and authorities as applicable.

Run `python tests/test_readiness.py` from the package directory. See `results.json` for individual assertions.
