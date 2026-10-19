#!/usr/bin/env python3
"""Generate portable starter skills for the pinned Kali default-package manifest."""

from __future__ import annotations

import argparse
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "references" / "default-tools.txt"


def skill_name(package: str) -> str:
    return f"kali-{package}"


def skill_contents(package: str) -> str:
    title = package.replace("-", " ").title()

    return f"""---
name: {skill_name(package)}
description: Use when an authorized security assessment requires the Kali Linux `{package}` package. Confirm the package's installed commands and use its own documentation before executing it.
---

# {title}

`{package}` is in the pinned Kali Linux default-package manifest for this release of the catalog. Package names and executable names can differ, so do not invent commands or flags.

## Safe workflow

1. Confirm explicit authorization, the exact in-scope target or artifact, and operational limits.
2. Confirm the package is installed and identify its supplied files:

```bash
dpkg -L {package}
```

3. Read the installed command's `--help` and manual page before choosing options.
4. Start with the least intrusive, read-only operation that answers the approved question; save sanitized evidence outside version control.
5. Stop for errors, rate limiting, unexpected state changes, out-of-scope results, or any operation that could change data, credentials, availability, or access.

Do not use this starter skill as proof that a command is safe for a production target. Replace it with a tool-specific workflow when repeated use needs validated flags, prerequisites, and failure handling.
"""


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--overwrite", action="store_true", help="replace existing SKILL.md files")
    args = parser.parse_args()

    packages = [
        line.strip()
        for line in MANIFEST.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.startswith("#")
    ]

    for package in packages:
        if not re.fullmatch(r"[a-z0-9][a-z0-9+.-]*", package):
            raise ValueError(f"Invalid Debian package name: {package}")

        skill_path = ROOT / package / "SKILL.md"
        if skill_path.exists() and not args.overwrite:
            continue

        skill_path.parent.mkdir(parents=True, exist_ok=True)
        skill_path.write_text(skill_contents(package), encoding="utf-8")


if __name__ == "__main__":
    main()
