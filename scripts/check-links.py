#!/usr/bin/env python3
"""Check that every relative Markdown link in the repository resolves.

External links (http/https/mailto) are not fetched; a separate network check
is intentionally out of scope so validation stays deterministic. Links inside
fenced code blocks and inline code spans are ignored.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SKIP_DIRS = {".git", "dist", "node_modules", ".venv", "__pycache__"}

LINK_RE = re.compile(r"\[([^\]]*)\]\(\s*<?([^)\s>]+)>?(?:\s+\"[^\"]*\")?\s*\)")
CODE_SPAN_RE = re.compile(r"`[^`\n]*`")


def _strip_code(text: str) -> str:
    """Remove fenced code blocks and inline code spans before link scanning."""
    text = re.sub(r"```.*?```", lambda m: "\n" * m.group(0).count("\n"), text, flags=re.S)
    return CODE_SPAN_RE.sub("", text)


def iter_markdown(root: Path | None = None) -> list[Path]:
    root = root or REPO_ROOT
    files = []
    for path in sorted(root.rglob("*.md")):
        if any(part in SKIP_DIRS for part in path.relative_to(root).parts):
            continue
        files.append(path)
    return files


def find_broken(root: Path | None = None) -> list[str]:
    """Return one error string per unresolved relative link."""
    root = root or REPO_ROOT
    errors: list[str] = []
    for path in iter_markdown(root):
        rel = path.relative_to(root)
        text = _strip_code(path.read_text(encoding="utf-8", errors="replace"))
        for match in LINK_RE.finditer(text):
            target = match.group(2)
            if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target):
                continue  # external or mailto
            anchor_stripped = target.split("#", 1)[0]
            if not anchor_stripped:
                continue  # pure-anchor link
            resolved = (path.parent / anchor_stripped).resolve()
            if not resolved.exists():
                errors.append(f"{rel}: broken link -> {target}")
    return errors


def main() -> int:
    files = iter_markdown()
    errors = find_broken()
    total_links = 0
    for path in files:
        text = _strip_code(path.read_text(encoding="utf-8", errors="replace"))
        total_links += len(LINK_RE.findall(text))
    if errors:
        for e in errors:
            print(f"error: {e}", file=sys.stderr)
        print(f"\n{len(errors)} broken link(s) out of {total_links} checked", file=sys.stderr)
        return 1
    print(f"OK: {total_links} links in {len(files)} files resolve")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
