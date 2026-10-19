# kali-tools

A portable catalog of Kali Linux tool skills for **authorized** security assessments, CTFs, training labs, and systems you own. It provides a master router plus independently installable tool workflows; it does not ship Kali software or grant authorization.

## Layout

```text
skills/
  kali-tools/SKILL.md       # scope, selection, evidence, and stop router
  nmap/SKILL.md             # independently installable tool skill
  ffuf/SKILL.md
  ...
references/                 # catalog/release material, not a runtime dependency
workflows/                  # pack-level workflow guides
manifest.yaml               # generated catalog index
```

Every canonical skill is at `skills/<id>/SKILL.md`. Generated starter skills are deliberately help-first; curated skills have verified, bounded workflows. See [`references/migration-ledger.md`](references/migration-ledger.md) for the catalog mapping and alias decisions.

## Install

The open [skills CLI](https://github.com/vercel-labs/skills) supports collection discovery and per-skill installation. Replace `OWNER` after publication:

```bash
npx skills add watcher1337/kali-tools --list
npx skills add watcher1337/kali-tools
npx skills add watcher1337/kali-tools --skill nmap
npx skills add watcher1337/kali-tools --skill ffuf
```

A one-skill install copies only `skills/<id>/`; therefore individual skills contain no required repository-root runtime reference. The `kali-tools` router bundles its own references. Validate a clone or installed copy with:

```bash
python3 scripts/validate-skills.py
python3 scripts/build-manifest.py --check
python3 scripts/check-links.py
python3 scripts/validate-evals.py
```

Use the selected host's documented update command (or re-run `npx skills add …`) after reviewing changes. See [`adapters/`](adapters/) for host-specific discovery guidance and verification status.

## Safe use

Before execution, record explicit targets, permitted techniques, rate/concurrency limits, test window, credentials/lockout rules, data handling, exclusions, and stop contact. A tool being installed, a service being discovered, an authentication success, or a scanner alert is not authorization or a confirmed vulnerability.

Start with `skills/kali-tools/SKILL.md`; it selects the smallest relevant individual skill. Do not assume a router automatically loads sibling skills—use the host's actual skill-loading mechanism.

## Contributing

Read [`CONTRIBUTING.md`](CONTRIBUTING.md), [`references/skill-format.md`](references/skill-format.md), and [`evals/README.md`](evals/README.md). Do not invent flags: validate against `tests/fixtures/help/` or authoritative documentation. Regenerate only generated starters:

```bash
python3 scripts/generate-tool-skills.py --upgrade-generated
python3 scripts/build-manifest.py
```

See [`references/release-sync.md`](references/release-sync.md) before changing `default-tools.txt`. Do not publish, push, or release without maintainer approval.

## Runtime status

Generic Markdown packaging is structurally tested. OpenCode, Claude Code, Codex, and Cursor have documentation-linked adapters but have **not** been runtime-tested in this checkout; do not treat them as release-verified. See [`manifest.yaml`](manifest.yaml) and [`adapters/README.md`](adapters/README.md).

## License

GPL-3.0-only. See [`LICENSE`](LICENSE).
