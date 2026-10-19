#!/usr/bin/env python3
"""Exercise installer-equivalent copy layouts without requiring a published repo."""
from __future__ import annotations

import re
import shutil
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LINK = re.compile(r"\[[^]]*\]\(([^)\s]+)")


def broken_links(root: Path) -> list[str]:
    errors: list[str] = []
    for path in root.rglob("*.md"):
        text = re.sub(r"```.*?```", "", path.read_text(errors="replace"), flags=re.S)
        for target in LINK.findall(text):
            if ":" in target or target.startswith("#"):
                continue
            target = target.split("#", 1)[0]
            if target and not (path.parent / target).resolve().exists():
                errors.append(f"{path.relative_to(root)} -> {target}")
    return errors


def main() -> int:
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        # Whole-collection installer copies the skills root.
        full = tmp / "full" / "skills"
        shutil.copytree(ROOT / "skills", full)
        # Per-skill installer copies only the selected skill directory.
        singles = []
        for skill_id in ("nmap", "ffuf"):
            single = tmp / "single" / skill_id
            shutil.copytree(ROOT / "skills" / skill_id, single)
            singles.append(single)
        master = tmp / "single-master" / "kali-tools"
        shutil.copytree(ROOT / "skills" / "kali-tools", master)
        errors = [error for single in singles for error in broken_links(single)] + broken_links(master)
        if errors:
            print("broken single-skill links:\n" + "\n".join(errors), file=sys.stderr)
            return 1
        if not (full / "nmap" / "SKILL.md").is_file() or not (full / "kali-tools" / "SKILL.md").is_file():
            print("full collection copy incomplete", file=sys.stderr)
            return 1
    print("OK: full collection and single-skill copy layouts are portable")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
