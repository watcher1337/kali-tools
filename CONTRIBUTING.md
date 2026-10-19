# Contributing

## Before editing

1. Search `skills/` and [`references/migration-ledger.md`](references/migration-ledger.md) for overlap and aliases.
2. Keep canonical content at `skills/<id>/SKILL.md`; do not add active skills under `references/`.
3. Preserve package names separately from executables. Use `metadata.aliases` for selectors that should resolve to a canonical ID.
4. Mark a skill `manual` or `generated`. Never overwrite curated/manual content with the starter generator.

## Quality bar

A skill is an actionable, bounded workflow. It needs valid frontmatter, activation and exclusion conditions, prerequisites, interpretation, failure/decision handling, evidence, safety gates, anti-rationalization, red flags, and checkable exit criteria. Examples must be verified by a local fixture or authoritative source; otherwise label them unverified.

Add `evals/cases/<id>.json` with at least three positive prompts, two negative prompts, and one behavioral case. Do not claim behavioral LLM evaluation passed unless it was run and reviewed.

## Checks

```bash
python3 scripts/validate-skills.py
python3 scripts/build-manifest.py --check
python3 scripts/check-links.py
python3 scripts/validate-evals.py
```

Run the generator only for pinned packages and inspect its diff:

```bash
python3 scripts/generate-tool-skills.py --upgrade-generated
python3 scripts/build-manifest.py
```

Never include real targets, credentials, cookies, customer data, or engagement artifacts. See [`SECURITY.md`](SECURITY.md).
