# Claude Code adapter

Claude Code documents skills at `.claude/skills/<skill-name>/SKILL.md` for a project and `~/.claude/skills/<skill-name>/SKILL.md` for a user. Copy selected directories from `skills/` under either root; each directory remains intact so bundled references travel with the selected skill.

Claude Code may select a relevant skill or it may be invoked by its skill name. The router does not itself load sibling skills.

Source: <https://code.claude.com/docs/en/skills>. **Status:** documentation-linked; runtime installation is not tested in this checkout.
