---
name: publish-is-not-a-prayer
description: Verify first-release readiness and safe distribution; use before publishing, deploying, packaging, or recommending a production release.
---

# Publish Is Not a Prayer

*The publish button is a responsibility, not a ritual.*

## Mandate
Make the first public release a deliberate, evidence-backed decision. Distinguish preparing an artifact, recommending release, obtaining authorization, distributing it, and confirming availability.

## Release contract
Identify target users, platforms, channels, version, source revision, distribution requirements, data and privacy impact, and accountable release owner. Record known limitations in language the audience can understand.

## Preflight
- Confirm the intended scope and applicable critical acceptance criteria.
- Inspect the working tree and select the intended source revision. Preserve user changes.
- Use the declared toolchain and resolved dependencies to build in a clean workspace or equivalent reproducible environment.
- Check production configuration, debug settings, credentials, endpoints, permissions, and logging behavior.
- Run applicable security and dependency checks, review distribution rights and licenses, and identify relevant privacy disclosures. Escalate uncertain legal or platform requirements to the owner.
- Verify migration, backup, recovery, and compatibility for any user data at risk.
- Document version, installation instructions, supported environments, and release notes.

## Test the artifact that will leave the building
- Capture artifact identity with a digest or immutable identifier.
- Inspect package contents, required assets, metadata, and accidental secrets or development-only material.
- Install, start, or deploy that exact artifact to a disposable representative environment.
- Run critical journeys through the installed or deployed entry point, including persisted data and external boundaries where relevant.
- Verify signing and trust metadata when the distribution channel requires them.
- Preserve the tested artifact for distribution; rebuilds require renewed identity and appropriate verification.
- Record target-device or platform coverage gaps explicitly. A browser preview establishes browser behavior rather than native installation behavior.

## Recovery and operational readiness
Choose a rollback, forward-repair, or recovery procedure suited to the platform. Verify it against a disposable environment when meaningful. Consider database compatibility, offline installations, already-distributed artifacts, and users who cannot immediately upgrade. Establish a minimal way to receive and diagnose reports. Keep infrastructure proportionate to the product.

## Release ledger
For each applicable requirement record: criterion, criticality, status, evidence reference, environment, and unresolved risk. Use VERIFIED, FAILED, UNVERIFIED, BLOCKED, or NOT APPLICABLE with rationale. Link evidence to the exact candidate. A changed candidate invalidates affected checks.

| Decision | Rule |
|---|---|
| READY FOR AUTHORIZATION | Critical checks VERIFIED; residual risks disclosed; artifact identified |
| HOLD | Critical check FAILED, BLOCKED, or UNVERIFIED; unresolved material risk |
| PUBLISHED | Authorized distribution executed and confirmed by destination evidence |

Treat applicable critical security, data integrity, functionality, installation, and distribution requirements as release gates. Noncritical exceptions need explicit owner acceptance and documented impact. Keep HOLD distinct from a claim that release is impossible.

## Authorization and confirmation
Present a concise release recommendation, exact candidate, destination, and remaining risks. Obtain explicit authorization for public distribution, production deployment, spending, or sensitive data transfers unless the user has already granted specific authority. Follow platform permissions and applicable system rules. Confirm external actions from actual results and report partial or uncertain outcomes accurately.

## Hand-off to a nontechnical owner
Explain whether the application is ready, what was actually tested, what remains untested, how to install or recover it, and which decision belongs to the owner. Offer the safest next concrete action. Retain technical evidence for future maintenance.

*Publishing is the moment your assumptions become someone else's problems. Verify them first.*
