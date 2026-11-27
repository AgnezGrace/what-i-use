# What I Use

A small collection of skills I use. Each skill lives in its own folder under `skills/`. Copy what you need.

## Skills

| Skill | What it does |
| --- | --- |
| [simplicity](skills/simplicity/skill.md) | Design, audit, implement, and refine interfaces around genuine user needs, coherent interaction paths, useful language, and durable simplicity. |
| [lazy-ui-is-a-crime](skills/lazy-ui-is-a-crime/skill.md) | Build and refine product-native interfaces with intentional components, coherent visual identity, SVG-based iconography, economical copy, accessible interactions, and smooth motion. |
| [color-palettes-are-bullshit](skills/color-palettes-are-bullshit/skill.md) | Select and implement distinctive, context-driven UI color systems using curated tonal ramps, accessible semantic tokens, and explicit safeguards against generic AI aesthetics. |
| [the-emperor-of-ai](skills/the-emperor-of-ai/skill.md) | Govern familiar AI-generated UI patterns through deliberate hierarchy, coherent composition, restrained effects, and verified usability. |
| [you-are-a-king](skills/you-are-a-king/skill.md) | Apply disciplined, evidence-led assistant conduct when asked to adopt the You Are a King persona, change its register, resist sycophancy or emotional pressure, or review conversational judgment. Supports Noble, King, and Emperor styles. |

## Install

### Automatic: ask your AI assistant

Paste this prompt into your AI coding assistant:

```
Install the skills from https://github.com/AgnezGrace/what-i-use

1. Clone the repository.
2. Ask me which skills to install, or install all of them.
3. For each skill, copy skills/<name>/skill.md into my agent's skills directory.
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

Save it as `skill.md` (or `SKILL.md`, depending on your agent) inside a folder named after the skill.

## License

MIT. See [LICENSE](LICENSE).
