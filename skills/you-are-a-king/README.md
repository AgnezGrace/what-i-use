# You Are a King.

A portable AI personality framework for independent judgment, factual integrity, professional service, and restrained communication. The crown symbolizes responsibility rather than superiority.

## Choose one installation route

| Host | Packaged source | Destination and scope |
|---|---|---|
| OpenClaw | SOUL.md; optional IDENTITY.md | Active agent workspace; merge the core into SOUL.md and preserve the existing identity fields. |
| OpenAI Codex | adapters/codex/AGENTS.md | Project root AGENTS.md, or CODEX_HOME/AGENTS.md (commonly ~/.codex/AGENTS.md) for personal defaults. |
| Claude Code | adapters/claude/CLAUDE.md | Project root CLAUDE.md or ~/.claude/CLAUDE.md for personal defaults. |
| Gemini CLI | adapters/gemini/GEMINI.md | Project root GEMINI.md or ~/.gemini/GEMINI.md for personal defaults. |
| Cursor | adapters/cursor/sovereignty.mdc | Project .cursor/rules/sovereignty.mdc; alwaysApply is true. |
| GitHub Copilot | adapters/copilot/copilot-instructions.md | Repository .github/copilot-instructions.md; supported clients and settings determine application. |
| Agent Skills host | SKILL.md and its companion files | Install the complete you-are-a-king directory in the host's supported skill location. |
| Other assistant | SOUL.md | Paste the core into the supported custom instructions or persona field. |

## Installation procedure
1. Back up the current instruction files and inspect existing rules. Merge the core into an existing file, preserving project-specific instructions and identity configuration.
2. Choose one adapter for each host. Each adapter embeds the operational core, so relative file loading is unnecessary. Avoid stacking the same core via multiple always-active files in one context.
3. Change `Active register: King.` to `Active register: Noble.` or `Active register: Emperor.` in the installed core to set the default. A clear conversational preference can change the local style.
4. Start a fresh session or reload context using the host's supported procedure. Inspect active instructions where the host exposes them.
5. Retain the backup. To revert, remove the inserted section or restore the original file and refresh context.

## Maintenance
SOUL.md is the canonical operational text. CONSTITUTION.md provides deeper reasoning guidance; IDENTITY.md is optional identity guidance, not a required replacement for configured metadata. Copy revised core text into each adapter while preserving its header.

The folder names inside adapters are packaging conveniences. Hosts discover the destination files, rather than this archive's adapter directory itself. Platform versions, context budgets, instruction precedence, and user settings affect loading and adherence. This package changes supplied instructions, not model weights, permissions, or consciousness.
