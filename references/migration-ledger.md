# Migration ledger

| Source | Canonical destination | Status | Notes |
| --- | --- | --- | --- |
| Root `SKILL.md` | `skills/kali-tools/SKILL.md` | migrated/manual | Root is now a compatibility pointer. |
| `references/tools/<package>/SKILL.md` | `skills/<package>/SKILL.md` | migrated | 237 generated starters moved without required root-runtime links. |
| `references/tools/nmap`, `ffuf`, `netexec`, `nuclei` | same canonical IDs | migrated/improved | Pilot workflows rewritten against captured help fixtures. |
| `references/tools/burp-suite` | `skills/burp-suite/SKILL.md` | migrated/improved | Canonical curated web-inspection workflow. |
| `references/tools/burpsuite` | `burp-suite` alias | merged | Package alias; pre-migration source retained at `references/migration-archive/burpsuite-SKILL.md`. |
| `binwalk`, `binwalk3` | same canonical IDs | retained distinct | Different Kali packages/versions; no merge. |

All 244 source tool directories were reconciled: 243 canonical tool skills plus one documented `burpsuite` alias. No active skill remains under `references/tools/`.
