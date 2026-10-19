# Repository instructions

- Canonical installable skills are only `skills/<id>/SKILL.md`; root `SKILL.md` is a pointer.
- Do not regenerate or overwrite curated skills. Generated starters carry `metadata.source: generated` and the generator marker.
- Run `python3 scripts/validate-skills.py`, `python3 scripts/build-manifest.py --check`, `python3 scripts/check-links.py`, and `python3 scripts/validate-evals.py` after catalog changes.
- Do not claim runtime installation or command execution without recorded evidence.
