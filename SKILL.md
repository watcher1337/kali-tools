---
name: kali-tools
description: Use when planning or performing an authorized security assessment with a Kali Linux default-tool package, or when selecting the least intrusive Kali tool for a scoped security-testing task.
---

# Kali Tools

A portable catalog of starter skills for the **Kali Linux default desktop image**. The pinned package manifest is in [references/default-tools.txt](references/default-tools.txt); it is release-specific and intentionally does not claim to cover Kali's `kali-linux-everything` metapackage.

## Mandatory safety gate

Before any tool use, obtain explicit authorization and confirm the in-scope assets, allowed techniques, rate limits, test window, credentials, exclusions, and stop contact. Do not conduct testing against public or third-party systems without permission. Do not evade defenses, steal data, maintain access, or make destructive changes.

## Workflow

1. Select a package from the pinned manifest; use [tool-selection](references/tool-selection.md) to choose a category.
2. Load that package's `SKILL.md`. Check the installed package and its command help rather than guessing executable names or flags.
3. Start with the least intrusive, read-only operation. Keep output in an engagement-specific directory outside version control.
4. Manually validate findings and report sanitized evidence, affected scope, impact, and remediation.
5. Stop on instability, scope ambiguity, or any behavior that could change data or availability.

## Catalog maintenance

The included skills are generated from `references/default-tools.txt`. To update a pinned release after reviewing Kali's `kali-meta` source, update that manifest and run:

```bash
python3 scripts/generate-tool-skills.py
```

Use `--overwrite` only to intentionally replace existing starter skills. See [release-sync](references/release-sync.md) for the source and update process.
