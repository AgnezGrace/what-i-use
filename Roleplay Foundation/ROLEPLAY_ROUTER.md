# Roleplay router

Entry point: `SKILL.md`. This is a routing contract, not a second personality prompt.

## Determine mode

| Mode | Read next | Output |
|---|---|---|
| Create | identity, manifestation, relationships, composition | Portable profile or character definition |
| Refine | manifestation; only other affected references | Minimal patch or revised definition |
| Compose | composition, manifestation, relevant relationship/state references | Integrated profile |
| Transfer | platform adapter guide; source profile | Copy-ready fields and loss report |
| Author module | module-contract, manifestation, evaluation | Module and index entry |
| Evaluate | evaluation; only relevant character references | Evidence-based findings |

Core references are under `core/` with the exact filenames in this table: `identity.md`, `manifestation.md`, `relationships.md`, `composition.md`, `continuity.md`, `boundaries.md`, `dialogue.md`, `module-contract.md`, `evaluation.md`. Load boundaries when intimacy, power, coercion, user agency, or real-user dependence is relevant; its baseline invariants are also in SKILL.md. Load dialogue for voice or repetition problems; continuity for memory, scene progression or contradictions.

## Select catalog knowledge

Read `catalog/index.json` only when a task requires catalog traits. Match requested concepts to module ID or aliases; aliases may be multilingual. The index lists relative paths from the roleplay root. Load a matching category's SKILL.md and then only the requested manifestation references. If a trait is ambiguous, use context or ask one clarifying question. If no match exists, use generic core principles and mark catalog coverage absent. Do not guess paths or create an entry unless asked to author a module.

A future attention request might mean caring, attentiveness, or seeking attention. These are not automatically equivalent. A future module may specify its own disambiguation logic. Do not assume an emotion, motive, temperament and relationship are the same kind of attribute.

## Composition order

1. User task and explicit constraints.
2. Established identity, canon, and narrative mode.
3. Relationship and current scene; knowledge available to the character.
4. Selected trait tendencies and modifiers.
5. Voice and output format.

Resolve conflict rather than mechanically following every example. If an explicit revision changes canon, label the change. Do not let a trait module overwrite unrelated identity or boundaries.

## Deployment route

If a target is requested, read `adapters/README.md`, then the adapter index. Use an existing mapping only if it covers the actual target and version; otherwise follow the universal procedure. If no platform is requested, produce portable output. Do not interrupt creative work merely to select a platform.

## Stop conditions

Stop loading when sufficient evidence is available to fulfill the request. Tests and fixtures are read only when authoring or evaluating. The catalog may grow indefinitely; its size is not a reason to ingest it all. Do not claim this routing contract saves a measured number of tokens without measurement.
