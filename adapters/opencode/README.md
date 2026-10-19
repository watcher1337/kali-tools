# OpenCode adapter

OpenCode documents discovery from `.opencode/skills/<name>/SKILL.md`, `.claude/skills/<name>/SKILL.md`, and `.agents/skills/<name>/SKILL.md` (plus matching global locations). Copy selected directories from this repository's `skills/` into one of those roots; do not copy the root compatibility pointer.

OpenCode exposes available skills to its native `skill` tool and loads content on demand. The catalog adds no OpenCode-specific frontmatter or automatic-execution permissions.

Source: <https://opencode.ai/docs/skills/>. **Status:** documentation-linked; runtime installation is not tested in this checkout.
