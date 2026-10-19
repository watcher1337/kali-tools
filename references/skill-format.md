# Canonical skill format

Canonical installable skills live directly at `skills/<id>/SKILL.md`; `<id>` and frontmatter `name` are lowercase kebab-case and identical. The root `SKILL.md` is only a compatibility pointer.

Required frontmatter fields are `name`, `description`, `license`, and `metadata`. Metadata records category, type, status, source (`manual` or `generated`), capabilities, activation, prerequisites, verification, package/executable mappings, related skills, aliases, and dependencies. The exact schema is [`../schemas/skill.schema.json`](../schemas/skill.schema.json).

Tool skills use this ordered core: Identity, Activation, Do not use when, Prerequisites, Execution patterns, Interpretation, Decision rules, Evidence, Related tools, Safety. They also include common rationalizations, red flags, and verification/exit criteria. The master router has a safety gate and routing workflow instead.

A single-skill installer copies only its own directory. Required runtime references must therefore be inside that directory; repository-root references are pack-level material only.
