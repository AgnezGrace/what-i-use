# What I Use

A small collection of skills I use, in three separate catalogs: `skills/` for the main set, `optional/` for additional skills, and `DESIGN/` for design systems. Copy what you need.

## Skills

| Skill | What it does |
| --- | --- |
| [simplicity](skills/simplicity/skill.md) | Design, audit, implement, and refine interfaces around genuine user needs, coherent interaction paths, useful language, and durable simplicity. |
| [lazy-ui-is-a-crime](skills/lazy-ui-is-a-crime/skill.md) | Build and refine product-native interfaces with intentional components, coherent visual identity, SVG-based iconography, economical copy, accessible interactions, and smooth motion. |
| [color-palettes-are-bullshit](skills/color-palettes-are-bullshit/skill.md) | Select and implement distinctive, context-driven UI color systems using curated tonal ramps, accessible semantic tokens, and explicit safeguards against generic AI aesthetics. |
| [the-emperor-of-ai](skills/the-emperor-of-ai/skill.md) | Govern familiar AI-generated UI patterns through deliberate hierarchy, coherent composition, restrained effects, and verified usability. |
| [you-are-a-king](skills/you-are-a-king/skill.md) | Apply disciplined, evidence-led assistant conduct when asked to adopt the You Are a King persona, change its register, resist sycophancy or emotional pressure, or review conversational judgment. Supports Noble, King, and Emperor styles. |
| [fuck-it-use-math](skills/fuck-it-use-math/SKILL.md) | Generate original, dependency-free icons and simple geometric assets with mathematics, native SVG and CSS. Includes the generator, icon registry, catalog, and tests. |
| [fuck-the-navigation-bar](skills/fuck-the-navigation-bar/SKILL.md) | Replace permanent navigation bars with on-demand radial menus (Ghost Orbit): collision-free geometry, hold gestures, and an accessible fallback list. |
| [the-user-is-not-a-stack-trace](skills/the-user-is-not-a-stack-trace/SKILL.md) | Resolve ambiguous bug and revision scope with evidence: treat the user as a witness, classify the cause, read wide, write narrow, and verify what was left alone. |

## Optional

| Skill | What it does |
| --- | --- |
| [architecture-before-prayer](optional/architecture-before-prayer/architecture-before-prayer.md) | Establish a proportional, testable project foundation before implementation; use for new products, inherited projects with unclear boundaries, and architectural decisions. |
| [your-database-is-not-a-trash-can](optional/your-database-is-not-a-trash-can/your-database-is-not-a-trash-can.md) | Protect user data, trust boundaries, and operational integrity; use when implementing persistence, authentication, imports, external services, migrations, or recovery. |
| [put-the-chainsaw-down](optional/put-the-chainsaw-down/put-the-chainsaw-down.md) | Make focused changes while protecting existing behavior; use for features, bug fixes, refactors, dependency updates, and maintenance. |
| [it-compiles-so-what](optional/it-compiles-so-what/it-compiles-so-what.md) | Verify actual behavior through risk-based tests; use for implementation, debugging, regression checks, integration, and release validation. |
| [publish-is-not-a-prayer](optional/publish-is-not-a-prayer/publish-is-not-a-prayer.md) | Verify first-release readiness and safe distribution; use before publishing, deploying, packaging, or recommending a production release. |
| [congratulations-youve-been-hacked](optional/congratulations-youve-been-hacked/congratulations-youve-been-hacked.md) | Secure software built with AI, especially when a user delegates technical decisions or shows limited security knowledge; activate for authentication, user data, secrets, uploads, public exposure, deployment, and pre-release security verification. |
| [the-second-human](optional/the-second-human/SKILL.md) | Communicate naturally and context-awarely: turn protocol, register, conversational repair, editing restraint, and honest AI identity. |

## Design

| Design | What it is |
| --- | --- |
| [Blueberry](DESIGN/Blueberry/DESIGN.md) | Premium web design system: quiet precision, four product modes, Berry pigment tokens, 44px targets, and a clean press and focus edge contract. |

## Install

### Automatic: ask your AI assistant

Paste this prompt into your AI coding assistant:

```
Install the skills from https://github.com/AgnezGrace/what-i-use

1. Clone the repository.
2. Ask me which skills to install, or install all of them.
3. For each skill, copy its file from the skills/ or optional/ directory into my agent's skills directory.
4. Rename the file to SKILL.md if my agent requires that filename.
5. Tell me which skills were installed and where.
```

### Manual: clone and copy

```bash
git clone https://github.com/AgnezGrace/what-i-use.git
```

Then copy the skill you want into your agent's skills directory, for example:

```bash
cp what-i-use/skills/simplicity/skill.md <your-skills-dir>/simplicity/SKILL.md
```

Adjust the destination path to match your agent. Rename the file to `SKILL.md` if your agent requires that name.

### Single skill: direct download

Download one file, no clone needed:

- Simplicity: https://raw.githubusercontent.com/AgnezGrace/what-i-use/main/skills/simplicity/skill.md
- Lazy UI Is a Crime: https://raw.githubusercontent.com/AgnezGrace/what-i-use/main/skills/lazy-ui-is-a-crime/skill.md
- Color Palettes Are Bullshit: https://raw.githubusercontent.com/AgnezGrace/what-i-use/main/skills/color-palettes-are-bullshit/skill.md
- The Emperor of AI: https://raw.githubusercontent.com/AgnezGrace/what-i-use/main/skills/the-emperor-of-ai/skill.md
- You Are a King: https://raw.githubusercontent.com/AgnezGrace/what-i-use/main/skills/you-are-a-king/skill.md
- Fuck It, Use Math: https://raw.githubusercontent.com/AgnezGrace/what-i-use/main/skills/fuck-it-use-math/SKILL.md
- Fuck the Navigation Bar: https://raw.githubusercontent.com/AgnezGrace/what-i-use/main/skills/fuck-the-navigation-bar/SKILL.md
- The User Is Not a Stack Trace: https://raw.githubusercontent.com/AgnezGrace/what-i-use/main/skills/the-user-is-not-a-stack-trace/SKILL.md

Optional skills:

- Architecture Before Prayer: https://raw.githubusercontent.com/AgnezGrace/what-i-use/main/optional/architecture-before-prayer/architecture-before-prayer.md
- Your Database Is Not a Trash Can: https://raw.githubusercontent.com/AgnezGrace/what-i-use/main/optional/your-database-is-not-a-trash-can/your-database-is-not-a-trash-can.md
- Put the Chainsaw Down: https://raw.githubusercontent.com/AgnezGrace/what-i-use/main/optional/put-the-chainsaw-down/put-the-chainsaw-down.md
- It Compiles. So What?: https://raw.githubusercontent.com/AgnezGrace/what-i-use/main/optional/it-compiles-so-what/it-compiles-so-what.md
- Publish Is Not a Prayer: https://raw.githubusercontent.com/AgnezGrace/what-i-use/main/optional/publish-is-not-a-prayer/publish-is-not-a-prayer.md
- Congratulations, You've Been Hacked: https://raw.githubusercontent.com/AgnezGrace/what-i-use/main/optional/congratulations-youve-been-hacked/congratulations-youve-been-hacked.md
- The Second Human: https://raw.githubusercontent.com/AgnezGrace/what-i-use/main/optional/the-second-human/SKILL.md

Design:

- Blueberry: https://raw.githubusercontent.com/AgnezGrace/what-i-use/main/DESIGN/Blueberry/DESIGN.md

Save it as `skill.md` (or `SKILL.md`, depending on your agent) inside a folder named after the skill.

## License

MIT. See [LICENSE](LICENSE).
