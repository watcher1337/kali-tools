# Changelog

## Unreleased

## 0.1.0-beta.2 (2026-10-19)

- Added self-contained `references/package-reference.md` to every tool skill: what it is, install/verify, how to use, when to use and avoid, suggestions, and failure/evidence handling.
- Curated references for nmap, ffuf, gobuster, http-enum, netexec, nuclei, sqlmap, and burp-suite now carry tool-specific workflows, option tables, and troubleshooting sourced from captured help and official documentation.
- Generated starter skills gained category-aware scope checklists, pitfalls, and interpretation guidance across all 12 catalog categories, still without inventing flags.
- Validator now enforces reference presence and required reference sections; generator, contributing guide, and skill-format docs updated.

## 0.1.0-beta.1 (2026-10-19)

- Migrated the catalog to independently discoverable `skills/<id>/SKILL.md` directories.
- Added a portable master router, manifest metadata, migration ledger, evaluations, workflows, and adapter guidance.
- Consolidated the `burpsuite` package selector into the canonical `burp-suite` skill alias.
