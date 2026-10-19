#!/usr/bin/env python3
"""Validate structural activation/evaluation coverage for every canonical skill.

This is not an LLM runner. Behavioral cases are reviewer-gated until an approved
runtime harness executes them and stores results under evals/fixtures/.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from catalog_common import REPO_ROOT, load_catalog  # noqa: E402


def main() -> int:
    errors: list[str] = []
    ids = {record["id"] for record in load_catalog()}
    cases = {path.stem: path for path in (REPO_ROOT / "evals" / "cases").glob("*.json")}
    for skill_id in sorted(ids):
        path = cases.get(skill_id)
        if path is None:
            errors.append(f"missing case for {skill_id}")
            continue
        try:
            case = json.loads(path.read_text())
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"{path.relative_to(REPO_ROOT)}: {exc}")
            continue
        if case.get("skill") != skill_id:
            errors.append(f"{path.relative_to(REPO_ROOT)}: skill mismatch")
        if len(case.get("positive_activation", [])) < 3:
            errors.append(f"{path.relative_to(REPO_ROOT)}: need 3 positive activations")
        if len(case.get("negative_activation", [])) < 2:
            errors.append(f"{path.relative_to(REPO_ROOT)}: need 2 negative activations")
        behavioral = case.get("behavioral", {})
        if not behavioral.get("prompt") or not behavioral.get("assertions"):
            errors.append(f"{path.relative_to(REPO_ROOT)}: behavioral prompt/assertions required")
    for case_id in sorted(set(cases) - ids):
        errors.append(f"orphan case: {cases[case_id].relative_to(REPO_ROOT)}")
    if errors:
        print("\n".join(f"error: {e}" for e in errors), file=sys.stderr)
        return 1
    print(f"OK: {len(ids)} skills have activation and reviewer-gated behavioral cases")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
