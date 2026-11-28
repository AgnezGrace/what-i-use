# You Are a Character, Not an Adjective

**Roleplay foundation — v0.1.0**

Design fictional AI characters through observable behavior, relationships, motives, limitations and continuity rather than lists of adjectives. This is a foundation for a future modular behavioral catalog. No trait categories or verified platform-specific adapters are included yet.

## Quick start

- With an Agent Skills-compatible agent: make this complete `roleplay/` directory available as a skill, keeping relative paths intact. Ask it to use the roleplay skill. Discovery/install conventions vary by host.
- With a file-capable chatbot: attach `SKILL.md`, `ROLEPLAY_ROUTER.md`, and the relevant core files (or the archive if the chatbot can actually unpack it). Ask it to create or revise a character. Do not assume ZIP support.
- With a text-only chatbot: copy [the universal prompt](adapters/universal-prompt.md). This is a standalone condensed workflow, not the entire knowledge base.
- To edit a character manually: use [the portable profile template](assets/profile-template.md).

## Platform not listed?

No specific platforms are registered in this foundation. Use the [Universal Adaptation Prompt](adapters/universal-prompt.md). Tell your chatbot the platform name; give it the actual creation fields, screenshot, or reliable documentation if it cannot verify them. It should return separately labeled copy-ready content and explain exactly where to paste it. If the platform is unknown, request a portable definition. Do not trust invented fields or claimed import compatibility without verification.

## Structure

- `SKILL.md`: agent entry point.
- `ROLEPLAY_ROUTER.md`: selective knowledge loading and task routing.
- `core/`: shared character, dialogue, relationship, composition, continuity, boundary and evaluation principles.
- `catalog/index.json`: registry for future trait categories (currently empty).
- `adapters/`: shared platform workflow, universal prompt and future mapping registry.
- `assets/`: authoring templates and portable profile schema.
- `scripts/`: optional offline structural checks and exact-label lookup.
- `tests/`: executable structural tests and a behavioral evaluation plan.

## Add a category later

Read `core/module-contract.md` and copy the authoring template. For example, a future `attention/` category can contain `manifestations/practical/GUIDE.md` and other meaningful expression modules. Relationships and modifiers can combine with manifestations without creating a folder for every possible combination. Keep shared adapters in `adapters/`. Register only completed categories and manifests in `catalog/index.json`; there is no need to modify the router for each addition.

## Verify

From the roleplay root, run `python scripts/validate.py` and `python -m unittest discover -s tests -v`. Python 3.10+ standard library; no model, API key, network or dependency installation is needed. The portable schema is JSON Schema, with optional external validation; the bundled validator checks its documented structural subset. See `tests/TEST-REPORT.md` for executed checks and limitations. Behavioral tests require a model or reviewer and are not automatically run by these commands.

## Scope

This package is a fictional writing framework, not a clinical taxonomy, a guarantee of model behavior, or an inventory of all human personalities. Platform compatibility and long-conversation quality depend on actual model and platform capabilities. No links to external research are embedded; the base uses creative design heuristics rather than empirical psychological claims.
