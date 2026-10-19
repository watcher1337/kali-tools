#!/usr/bin/env python3
"""Create portable per-skill reference files without overwriting curated notes.

Generated starters are refreshed by generate-tool-skills.py. This script fills
missing references for manually maintained skills, using their metadata and
workflow as the authoritative catalog content. It deliberately does not invent
commands or tool capabilities.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from catalog_common import REPO_ROOT, load_catalog  # noqa: E402


def manual_reference(skill_id: str, fm: dict) -> str:
    meta = fm["metadata"]
    packages = ", ".join(f"`{item}`" for item in meta.get("package", [])) or "not recorded"
    executables = ", ".join(f"`{item}`" for item in meta.get("executable", [])) or "discover with package metadata"
    return f"""<!-- generated bootstrap: scripts/build-tool-references.py; preserve manual enhancements -->
# {skill_id}: operational reference

## What it is

{fm['description']} The canonical workflow is [SKILL.md](../SKILL.md). It is
the source for bounded command patterns and interpretation; this reference
provides installation, selection, and operating guidance that remains present
when `{skill_id}` is installed alone.

## Install and verify

- Kali/Debian package mapping: {packages}.
- Known executable mapping: {executables}.
- Inspect before installation with `apt-cache policy <package>` and verify an
  installed package with `dpkg -s <package>`.
- Install only with environment/change approval: `sudo apt install <package>`.
  Then check the exact local `--help` and version output. Package names and
  executable names can differ.

## How to use

Follow the command patterns in [SKILL.md](../SKILL.md), substitute only
operator-supplied approved values, and confirm local help matches the installed
version. Examples are proposed commands, never evidence of execution.

## When to use

{fm['description']}

## When not to use

Do not use it without explicit scope, authorization, rate/concurrency limits,
and any required credential or data-handling approval. Do not substitute it for
a more focused skill when that skill already answers the approved question.

## Suggestions and decisions

Start with the smallest read-only action, preserve a baseline where applicable,
and validate the minimum harmless indicator. A discovery, login, banner, or
scanner alert is not by itself proof of a vulnerability or administrative
access. Escalate only through an explicit approval gate.

## Failure handling and evidence

If the executable is absent, report the missing dependency; if local help and
the workflow differ, prefer local help and label the workflow example
unverified. Save tool/package version, sanitized command, target, timestamp,
output/error, interpretation, and stop/escalation decision. Redact secrets and
sensitive data.
"""


def main() -> int:
    created: list[str] = []
    existing: list[str] = []
    for record in load_catalog():
        if record["id"] == "kali-tools":
            continue
        target = record["dir"] / "references" / "package-reference.md"
        if target.exists():
            existing.append(record["id"])
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(manual_reference(record["id"], record["fm"]), encoding="utf-8")
        created.append(record["id"])
    print(f"created={len(created)} existing={len(existing)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
