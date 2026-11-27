---
name: architecture-before-prayer
description: Establish a proportional, testable project foundation before implementation; use for new products, inherited projects with unclear boundaries, and architectural decisions.
---

# Architecture Before Prayer

*The user asked for an application. You are the one holding the engineering tools.*

## Mandate
Convert a human goal into an implementable, maintainable product foundation. Treat technical competence as the agent's responsibility. Preserve the user's authority over product outcomes, budget, privacy, and distribution.

## Talk to the human, engineer the system
- Ask about outcomes, audience, target devices, connectivity, data sensitivity, and distribution when these materially affect the result.
- Read available project files and previous decisions before requesting information again.
- Infer reversible technical details from existing conventions and disclose consequential assumptions.
- Explain important options in terms of cost, behavior, risk, and maintenance. Supply a recommended default and its reason.
- Seek explicit authorization for material spending, external data disclosure, destructive changes, and public release.
- Translate technical uncertainty into a concrete decision or a bounded investigation.

## The foundation contract
Create or update a concise project-owned foundation record. Reuse an existing README, architecture record, or specification when suitable.

| Field | Required content |
|---|---|
| Product intent | Audience, primary job, target environment, initial release scope |
| Acceptance | Observable outcomes for each critical user journey |
| Constraints | Offline requirements, platform limits, privacy, budget, licensing |
| Architecture | Runtime, module responsibilities, interfaces, data ownership |
| Invariants | Conditions that must survive every supported change |
| Dependencies | Runtime and build requirements, versions, rationale |
| Delivery | Source control, clean build/run/test commands, release destination |
| Risks | Failure consequences, verification strategy, unresolved decisions |

## Build the smallest adequate architecture
- Inspect the repository, build scripts, dependency declarations, and existing contracts.
- For a new product, select a mature stack supported by its target environment and maintenance needs.
- Prefer a modular single deployable when its boundaries satisfy the product. Split processes when isolation, scaling, security, or deployment evidence justifies the cost.
- Give each module one coherent responsibility and each persisted concept one authoritative owner.
- Define input, output, error, ownership, and lifecycle semantics at boundaries.
- Place platform and external-service integration behind boundaries where substitution or testing has practical value.
- Use existing abstractions when they fit; add new layers when they remove demonstrated complexity.
- Establish version control or use the existing repository. Preserve user changes and establish a baseline revision.
- Pin resolved dependencies using the ecosystem's supported lock mechanism where applicable; document toolchain requirements.
- Record significant architecture decisions with context, alternatives, rationale, consequences, and revisit triggers.

## Define invariants before features
Write invariants as assertions about observable state. For example:
- Successful saves survive process restart and preserve the intended content.
- Every operation on a protected record follows the applicable authorization policy.
- A completed import preserves required identifiers and ordering.
- A failed multi-step write leaves a valid pre-operation state or a documented recoverable state.
- Existing supported clients continue to interpret public contracts according to their version policy.
Select only applicable invariants and assign each an evidence method.

## Foundation gate
1. Trace every critical outcome to its owner and acceptance criterion.
2. Trace persistent data and external trust boundaries.
3. Inspect dependency direction and interface definitions; execute available architecture checks.
4. Run the documented minimal build or startup path in the available environment.
5. Identify unresolved assumptions and determine whether implementation can proceed safely.

Mark each claim VERIFIED, FAILED, UNVERIFIED, BLOCKED, or NOT APPLICABLE. VERIFIED requires observed evidence specific to the claim; a proposed architecture remains a proposal until checked. Record commands, revision, environment, and outcomes.

## Hand-off
Deliver the foundation record, a short implementation sequence, critical risks, and the next verification step. Keep advanced infrastructure conditional on product needs. For high-impact decisions, use a concise ADR. Carry the record into later changes and release checks.

*Architecture is a tool for keeping tomorrow's changes survivable. Prayer is a poor substitute for a contract.*
