---
name: your-database-is-not-a-trash-can
description: Protect user data, trust boundaries, and operational integrity; use when implementing persistence, authentication, imports, external services, migrations, or recovery.
---

# Your Database Is Not a Trash Can

*The source code can be regenerated. A person's lost work may be irreplaceable.*

## Mandate
Protect confidentiality, integrity, availability, and recoverability in proportion to the product's actual risks. Treat a successful operation as a promise about its resulting state.

## Inspect before writing
Identify data classes, owners, storage locations, retention, trust boundaries, external transfers, and consequences of loss. Inspect current schemas, migration history, access controls, and backup mechanisms. Use synthetic data for destructive experiments.

## Data integrity
- Establish an authoritative record and stable identity for each persistent concept.
- Validate at trust boundaries and enforce essential invariants in the persistence layer where supported.
- Select appropriate constraints, encoding, size limits, schema versions, and serialization formats.
- Use parameterized queries and safe platform APIs for untrusted inputs.
- Group related writes into a transaction or equivalent atomic operation. Define crash behavior for multi-step workflows.
- Use concurrency control suited to the store: transactions, unique constraints, revisions, locks, or compare-and-swap as applicable.
- Design repeated requests around idempotency when duplication has consequences. Scope keys to the correct owner and operation; define conflict and expiration behavior.
- Report success after the durable commit or clearly distinguish queued work from completed work.
- Keep import validation separate from commit; handle malformed and oversized inputs and preserve existing records on failure.

## Schema evolution and recovery
- Version persistent formats and define supported upgrade paths.
- Test migration against representative previous-version data, including interruptions and invalid records.
- Use a recovery strategy consistent with the store: transactional migration, verified backup, or forward repair.
- Choose backups according to the loss tolerance and storage model. Document retention, access restrictions, and restoration steps.
- Restore a backup into an isolated target and verify representative records. A backup file alone proves creation, while a restore test establishes recoverability.
- Require authorization for destructive production operations, and confirm the target and recovery path.

## Security baseline
- Identify assets, actors, entry points, abuse cases, and privilege boundaries.
- Enforce authorization at the authoritative server or local trust boundary for every protected operation. Treat UI visibility as presentation.
- Use mature authentication, credential storage, encryption, and transport facilities when applicable.
- Keep credentials out of committed source, client bundles, and diagnostic output. Use platform credential stores or deployment secrets and least privilege.
- Validate paths and uploads, constrain resource consumption, and encode output according to its destination.
- Review dependency advisories, licenses, and supported versions with available ecosystem tooling. Record any blocked or unavailable checks.
- Keep real private information out of test fixtures and diagnostics.

## Failure is part of the interface
| Failure | Expected engineering response |
|---|---|
| Interrupted write | Atomic outcome or documented recoverable state |
| Duplicate request | One intended effect or explicit conflict |
| Storage full | Explicit failure, prior data preserved where feasible |
| Network loss | Bounded timeout, safe retry or cancellation, honest status |
| Invalid or corrupt input | Rejection or recovery with actionable feedback |
| Unauthorized request | Denial at the trust boundary, protected data preserved |
| Process termination | Valid persisted state and documented restart behavior |

Retry transient failures with bounded attempts and appropriate backoff. Retry mutating operations only with safe semantics. Record useful diagnostic context while protecting sensitive content. Distinguish user-actionable messages from developer diagnostics.

## Integrity gate
Execute applicable tests in a disposable environment: invalid input, unauthorized access, interrupted writes, duplicates, restart, upgrade and restore. Verify the resulting persisted state, not merely an exception or status code. Exercise actual storage and boundary logic where possible. Report unsupported failure modes as UNVERIFIED or BLOCKED.

## Hand-off
Record data ownership, recovery instructions, checked trust boundaries, and residual risks. Translate impact into plain language for the user. Use VERIFIED, FAILED, UNVERIFIED, BLOCKED, and NOT APPLICABLE with claim-specific evidence and scope.

*Treat every successful save as a promise you can prove.*
