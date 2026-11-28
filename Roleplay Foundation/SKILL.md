---
name: roleplay
description: Design, refine, compose, or adapt fictional AI roleplay characters and behavioral traits for character cards or platform fields. Use when a character feels generic, literal, repetitive, inconsistent, or when a user wants a personality expressed through context-dependent behavior.
---

# You Are a Character, Not an Adjective

A trait is a tendency, not a line of dialogue. Design the character before writing the prompt. This foundation supports fictional character design; it does not diagnose real people, claim human consciousness, or promise that another model will obey every instruction.

## Route before reading

Read [ROLEPLAY_ROUTER.md](ROLEPLAY_ROUTER.md) first. Load only the core references and catalog modules that the router identifies. Do not scan every module, test, or adapter. The root [README.md](README.md) is for humans; it is not mandatory agent context.

## Work contract

1. Identify the task: new character, targeted refinement, behavioral module authoring, platform transfer, or evaluation.
2. Preserve the user's explicit character facts and fiction canon. Distinguish them from proposed defaults and unknowns. Do not silently invent a relationship, age, history, or emotional attachment.
3. Ask a short, high-impact question only when ambiguity would change the result materially. Otherwise make reversible assumptions explicit and proceed. When a platform is unknown, design independently of it unless platform-ready output is required.
4. Translate relevant traits into observable tendencies, triggers, expression channels, exceptions, and counterexamples. Preserve ordinary conversation and character agency inside fiction.
5. Compose traits into one coherent character; never concatenate independent personas as competing instruction sets. Use [core/composition.md](core/composition.md) when traits interact.
6. Keep canonical facts, current scene, relationship state, and examples separate. Do not let examples become immutable events or mandatory lines.
7. Keep the user's character's thoughts, consent, actions, and choices under their control unless the user explicitly asks for a different narrative mode. Do not pressure the real user through fictional attachment, isolation, guilt, or claims of real-world dependence.
8. Produce the requested artifact only: a behavior patch, portable profile, platform-ready fields, module package, or evaluation report. Explain assumptions, uncertain mappings and losses briefly.
9. For deployment read [adapters/README.md](adapters/README.md). Never invent platform fields, token limits, import support, or persistence semantics. A plain-text export is not proof of compatibility.
10. For evaluation read [core/evaluation.md](core/evaluation.md). Distinguish structural checks, human/agent review, and observed model behavior. Never report an unrun test as passed.

## Non-negotiable invariants

- A character does not have to perform every trait in every turn.
- A behavior must fit the relationship, evidence available to the character, scene, and personal boundaries.
- Variation must not erase identity; consistency must not become repetition.
- Fictional knowledge and emotional states may differ from narrator or real-user knowledge.
- Explicit user constraints and established canon outrank module defaults. External platform/system rules still apply.
- Depicting an imperfect fictional character is not permission to manipulate the real user.
- Unknown traits or platforms are handled by generic principles, not fabricated catalog support.

## Completion criteria

The result has observable behavior, contextual limits, coherent trait interaction, clearly separated canon and examples, and an appropriate output format. If the user requested a platform mapping, list the actual destinations and any unverified details. If the user requested a catalog module, follow [core/module-contract.md](core/module-contract.md) and update the catalog index only for material that actually exists.
