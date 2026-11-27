---
name: put-the-chainsaw-down
description: Make focused changes while protecting existing behavior; use for features, bug fixes, refactors, dependency updates, and maintenance.
---

# Put the Chainsaw Down

*The user asked you to fix a door, not demolish the house.*

## Mandate
Deliver the requested outcome through the smallest coherent change that protects existing contracts, user work, and future maintenance. Larger changes earn their scope through demonstrated necessity.

## Establish the starting point
- Read applicable repository instructions, architecture records, tests, and build configuration.
- Inspect version control status and diffs. Preserve unrelated or uncommitted user work.
- Locate existing implementations, shared utilities, callers, tests, and data ownership before adding code.
- Reproduce reported defects where feasible and record the observed behavior. When reproduction fails, describe the evidence gap and investigate plausible causes.
- Establish the baseline tests relevant to the affected contracts; distinguish pre-existing failures from regressions.

## Change contract
State the requested outcome, affected boundaries, preserved behavior, and verification plan. For a trivial correction, keep this implicit in the working context. For consequential changes, record it concisely.

Map impacts across callers, state, storage, compatibility, public interfaces, user-facing flows, permissions, deployment, and external dependencies. Include the actual platform when behavior differs by environment.

## Scope discipline
- Reuse existing paths where they satisfy the new requirement.
- Repair the authoritative implementation rather than adding parallel logic or symptom-specific exceptions.
- Keep behavior, formatting, and naming consistent with nearby code unless changing them is part of the goal.
- Separate unrelated cleanup from the requested patch. Record worthwhile follow-ups independently.
- Introduce dependencies only for a concrete benefit; compare built-in facilities, existing dependencies, and lifecycle costs.
- Preserve public contracts and stored formats according to the version policy; add migration or compatibility handling when a breaking change is authorized.
- Prefer explicit state transitions and clear ownership over speculative abstraction.
- Treat generated code, lockfiles, schema migrations, and configuration as part of the change surface.

## When a larger change is justified
Examples include a compromised trust boundary, corrupt data model, unsupported dependency, or architecture that prevents the acceptance criterion. Document the constraint, options, cost, migration path, and rollback implications. Obtain authorization when the change materially expands scope or risk. Proceed with bounded safe work while awaiting any consequential decision.

## Verification loop
1. Add or identify a check that distinguishes the intended outcome from the defect or previous behavior.
2. Apply the focused patch.
3. Run relevant focused checks, followed by adjacent integration and regression checks.
4. Inspect the diff for unrelated edits, duplicate logic, accidental generated changes, and secret exposure.
5. Verify affected invariants and compatibility boundaries.
6. Record baseline failures, new failures, and remaining unverified paths.

## Rollback and preservation
Use reversible commits or patches within the authorized scope. Preserve the user's working tree; destructive version-control commands and production changes require explicit authority. Ensure data rollback is compatible with schema changes, or document a tested forward-recovery path.

## Change gate
A change passes when the requested outcome is evidenced, relevant previous behavior remains intact, and scope is justified. Use VERIFIED, FAILED, UNVERIFIED, BLOCKED, or NOT APPLICABLE per claim. Record revision, commands, target environment, and outcomes. A small diff is a useful signal rather than proof of correctness.

## Hand-off
Explain the observed outcome, essential changes, tests actually executed, and residual limitations in ordinary language. Technical detail belongs in the repository evidence or a concise appendix. Keep the next action concrete.

*Use a scalpel when the problem calls for a scalpel.*
