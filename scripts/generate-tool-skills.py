#!/usr/bin/env python3
"""Generate or upgrade portable starter skills for the pinned Kali manifest.

Starter skills carry the full canonical section set (see
references/skill-format.md) but help-first content: they never invent flags.
They are written directly under skills/<id>/ and are independently portable.
Hand-curated skills (no generated marker) are never touched unless
--overwrite is given.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from catalog_common import (  # noqa: E402
    GENERATED_MARKER,
    LICENSE_ID,
    REPO_ROOT,
    classify,
)

MANIFEST = REPO_ROOT / "references" / "default-tools.txt"
# Debian package names may map to a canonical skill id. The package remains in
# metadata; this prevents duplicate installable skills for aliases.
PACKAGE_SKILL_IDS = {"burpsuite": "burp-suite"}


def skill_contents(package: str, skill_id: str | None = None) -> str:
    skill_id = skill_id or package
    title = package.replace("-", " ").title()
    category = classify(package)
    return f"""---
name: {skill_id}
description: Use when an authorized assessment requires the Kali Linux `{package}` package. Confirm the installed commands and read their own help before executing anything.
license: {LICENSE_ID}
metadata:
  category: {category}
  type: tool
  status: starter
  source: generated
  package: [{package}]
  capabilities: [shell]
  activation:
    - An authorized engagement is active and its scope is confirmed
    - The approved objective specifically requires the {package} package
  prerequisites:
    - Explicit authorization covering targets, techniques, and rate limits
    - Package installed in an approved environment
  related: []
  verification: none
---

# {title}

`{package}` {GENERATED_MARKER} for this release of the catalog. Package names and executable names can differ, so this starter deliberately contains no flags.

## Identity

- Package: `{package}` (Debian/Kali). Discover executables with `dpkg -L {package}`.
- Purpose: consult the installed command's own documentation; this starter carries no tool-specific behavior.
- Limitations: no verified examples, output formats, or flag guidance.

## Activation

- An authorized engagement is active and its scope is confirmed.
- The approved objective specifically requires `{package}`, and no curated skill in this catalog covers the task better.

## Do not use when

- Authorization, ownership, or scope for the target is unconfirmed.
- A skill with `status: curated` in `manifest.yaml` already covers the task.
- The operation would change data, credentials, availability, or access without explicit approval.

## Prerequisites

- Explicit authorization: targets, allowed techniques, rate limits, test window, stop contact.
- Package installed in an approved environment: `dpkg -s {package}`.
- An engagement evidence directory outside version control.

## Execution patterns

No verified examples in this starter. Before running anything:

1. Identify the executables: `dpkg -L {package}`.
2. Read the installed help for the exact version: `<command> --help`, `<command> -h`, or `man <command>`.
3. Record the version where the command supports it.
4. Start with the least intrusive, read-only invocation that answers the approved question.

## Interpretation

- This starter establishes nothing about output formats or result meaning.
- Treat raw output as observations, not findings; validate significant results independently before reporting them.

## Decision rules

- Executable not found: report the limitation and the smallest next step (approved install or execution backend). Do not improvise flags.
- Command exits with an error: capture the exact error, correct arguments only from real help output, stop after one retry.
- Result answers the approved question: record evidence and stop.
- Result inconclusive or ambiguous: switch to a curated skill or ask the operator.

## Evidence

- Save the exact command, tool version, timestamp, target, and full output in the engagement evidence directory.
- Redact credentials, cookies, tokens, and personal data from any copy that leaves that directory.

## Related tools

- Category routing is provided by the `kali-tools` master skill when it is installed.
- This skill remains usable on its own: inspect local help before selecting an alternative.

## Safety

- Read-only operations only unless the engagement explicitly approves state changes.
- Respect rate and concurrency limits; stop on instability or scope drift.
- Having the tool installed is not authorization to use it.
"""


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--overwrite", action="store_true", help="replace every existing SKILL.md, curated included"
    )
    parser.add_argument(
        "--upgrade-generated",
        action="store_true",
        help="replace only skills that still carry the original generated marker",
    )
    args = parser.parse_args()

    packages = [
        line.strip()
        for line in MANIFEST.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.startswith("#")
    ]

    created, upgraded, skipped = [], [], []
    for package in packages:
        skill_id = PACKAGE_SKILL_IDS.get(package, package)
        skill_path = REPO_ROOT / "skills" / skill_id / "SKILL.md"
        if skill_path.exists():
            text = skill_path.read_text(encoding="utf-8")
            if args.overwrite or (args.upgrade_generated and GENERATED_MARKER in text):
                skill_path.write_text(skill_contents(package, skill_id), encoding="utf-8")
                upgraded.append(package)
            else:
                skipped.append(package)
            continue
        skill_path.parent.mkdir(parents=True, exist_ok=True)
        skill_path.write_text(skill_contents(package, skill_id), encoding="utf-8")
        created.append(package)

    print(f"created={len(created)} upgraded={len(upgraded)} skipped={len(skipped)}")
    if created:
        print("created:", " ".join(created))
    if upgraded:
        print("upgraded:", " ".join(upgraded[:20]) + (" ..." if len(upgraded) > 20 else ""))


if __name__ == "__main__":
    main()
