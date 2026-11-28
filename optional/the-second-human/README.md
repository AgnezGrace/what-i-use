# The Second Human

A portable communication framework inspired by human history, linguistics, and conversational practice. All instructions are original, generic, and written in English; sample conversations also include Indonesian to demonstrate register transfer.

## Install

- Agent Skills: copy the `the-second-human` folder into a skills location supported by your host. Activate by skill name or let the host match its description.
- Persistent behavior: merge the core block in `AGENTS.md` into the instruction file recognized by your agent (for example project `AGENTS.md`, `CLAUDE.md`, or `GEMINI.md`). Preserve existing rules. Confirm the host's scope and loading behavior.
- Persona workspace: merge `adapters/SOUL.md` into an existing persona file where the host supports it. The short profile works independently of the history modules.
- Custom agent: load `agent.md` together with its referenced files, or paste `AGENTS.md` into the supported instructions field. The singular filename is a portable convention, not a universal standard.

Install one persistent entry point per scope. Keep the skill available for deeper tasks. The core rules require no tool, network, or personal profile. The history files are optional context. Inspect which instructions were actually loaded before evaluating behavior.

## Contents

`the-second-human.md` is the philosophical manifesto. `SKILL.md` is the executable instruction in natural language. `references/` is the knowledge library. `tests/` contains illustrative response pairs and a reproducible structural and fixture check.

## Evaluation

From this directory, run `python3 tests/validate.py`. Use `tests/evaluation-rubric.md` for independent model comparisons. The included pairs are authored examples, not captured outputs from a controlled model experiment.

## Research foundation

The knowledge library synthesizes human-origins research, oral traditions, linguistic pragmatics, conversation analysis, and register studies. Historical stages are an organizing device, not a claim that cultures develop in a single sequence. The origin of language is uncertain. Stylistic tendencies are not reliable proof of authorship.
