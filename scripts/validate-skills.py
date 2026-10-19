#!/usr/bin/env python3
"""Validate the canonical skill tree, frontmatter, sections, and manifest.

Exit code 0 = valid. Errors go to stderr. Functions are imported by the tests
in tests/validation/.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from catalog_common import (  # noqa: E402
    CAPABILITIES,
    CATEGORIES,
    FrontmatterError,
    LICENSE_ID,
    MASTER_HEADINGS,
    REPO_ROOT,
    SKILL_ID_RE,
    STATUSES,
    TOOL_SECTIONS,
    TYPES,
    VERIFICATION,
    load_catalog,
    parse_simple_yaml,
)

MAX_DESCRIPTION = 1024
MASTER_ID = "kali-tools"
MASTER_LINKS = (
    "references/tool-selection.md",
    "references/scope-and-safety.md",
    "references/evidence-management.md",
)


def _check_description(desc: object, where: str, errors: list[str]) -> None:
    if not isinstance(desc, str) or not desc.strip():
        errors.append(f"{where}: description missing or empty")
        return
    if "\n" in desc:
        errors.append(f"{where}: description must be a single line")
    if len(desc) > MAX_DESCRIPTION:
        errors.append(f"{where}: description longer than {MAX_DESCRIPTION} chars")


def _check_metadata(fm: dict, where: str, is_master: bool, errors: list[str]) -> None:
    meta = fm.get("metadata")
    if not isinstance(meta, dict):
        errors.append(f"{where}: metadata block missing")
        return
    required = ("category", "type", "status", "source", "capabilities", "activation", "prerequisites", "verification")
    for key in required:
        if key not in meta:
            errors.append(f"{where}: metadata.{key} missing")
    if meta.get("category") not in CATEGORIES:
        errors.append(f"{where}: metadata.category {meta.get('category')!r} not in enum")
    if meta.get("type") not in TYPES:
        errors.append(f"{where}: metadata.type {meta.get('type')!r} not in enum")
    else:
        if is_master and meta["type"] != "master":
            errors.append(f"{where}: master skill must have type: master")
        if not is_master and meta["type"] != "tool":
            errors.append(f"{where}: tool skill must have type: tool")
    if meta.get("status") not in STATUSES:
        errors.append(f"{where}: metadata.status {meta.get('status')!r} not in enum")
    if meta.get("source") not in {"manual", "generated"}:
        errors.append(f"{where}: metadata.source must be 'manual' or 'generated'")
    if meta.get("verification") not in VERIFICATION:
        errors.append(f"{where}: metadata.verification {meta.get('verification')!r} not in enum")
    caps = meta.get("capabilities")
    if not isinstance(caps, list) or not all(c in CAPABILITIES for c in caps):
        errors.append(f"{where}: metadata.capabilities must be a list from {sorted(CAPABILITIES)}")
    elif not caps and not is_master:
        errors.append(f"{where}: tool skill needs at least one capability")
    for key in ("activation", "prerequisites"):
        val = meta.get(key)
        if not isinstance(val, list) or not val or not all(isinstance(v, str) and v.strip() for v in val):
            errors.append(f"{where}: metadata.{key} must be a non-empty list of strings")
    for key in ("package", "executable", "related", "aliases", "dependencies"):
        val = meta.get(key, [])
        if not isinstance(val, list) or not all(isinstance(v, str) for v in val):
            errors.append(f"{where}: metadata.{key} must be a list of strings")


def _check_sections(body: str, where: str, is_master: bool, errors: list[str]) -> None:
    headings = MASTER_HEADINGS if is_master else TOOL_SECTIONS
    positions = []
    for h in headings:
        pos = body.find(h)
        if pos < 0:
            errors.append(f"{where}: missing section {h!r}")
        else:
            positions.append(pos)
    if positions != sorted(positions):
        errors.append(f"{where}: sections out of documented order")


def validate(root: Path | None = None) -> tuple[list[str], list[str]]:
    """Return (errors, warnings) for the canonical tree at *root*."""
    root = root or REPO_ROOT
    errors: list[str] = []
    warnings: list[str] = []

    try:
        records = load_catalog(root)
    except FrontmatterError as exc:
        return [f"frontmatter: {exc}"], warnings

    ids: set[str] = set()
    for rec in records:
        rid, fm, body, path = rec["id"], rec["fm"], rec["body"], rec["path"]
        rel = str(path.relative_to(root))
        is_master = rid == MASTER_ID
        where = rel

        if is_master:
            if fm.get("name") != MASTER_ID:
                errors.append(f"{where}: master skill name must be '{MASTER_ID}' (got {fm.get('name')!r})")
        else:
            if not SKILL_ID_RE.match(rid):
                errors.append(f"{where}: directory name is not a valid skill id")
            if rid == MASTER_ID:
                errors.append(f"{where}: '{MASTER_ID}' id is reserved for the master skill")
            if fm.get("name") != rid:
                errors.append(f"{where}: metadata name {fm.get('name')!r} must equal directory name {rid!r}")
        if fm.get("license") != LICENSE_ID:
            errors.append(f"{where}: license must be {LICENSE_ID!r} (got {fm.get('license')!r})")
        _check_description(fm.get("description"), where, errors)
        _check_metadata(fm, where, is_master, errors)
        _check_sections(body, where, is_master, errors)

        if is_master:
            for link in MASTER_LINKS:
                if link not in body:
                    errors.append(f"{where}: master must link bundled {link}")
            if "workflows/" not in body:
                errors.append(f"{where}: master must link pack-level workflows/")
        else:
            if "## Safety" not in body:
                errors.append(f"{where}: missing Safety section")
            desc = fm.get("description")
            if isinstance(desc, str) and not desc.startswith("Use when"):
                warnings.append(f"{where}: description does not start with 'Use when'")
            status = fm.get("metadata", {}).get("status")
            verification = fm.get("metadata", {}).get("verification")
            if status == "curated" and verification == "none":
                errors.append(f"{where}: curated skill must declare verification kali-help or official-docs")

        if rid in ids:
            errors.append(f"{where}: duplicate skill id {rid!r}")
        ids.add(rid)

    # related references, aliases, and package mappings must resolve uniquely.
    aliases: dict[str, str] = {}
    packages: dict[str, set[str]] = {}
    for rec in records:
        rel = str(rec["path"].relative_to(root))
        meta = rec["fm"].get("metadata", {})
        for ref in meta.get("related", []) or []:
            if ref not in ids:
                errors.append(f"{rel}: related skill {ref!r} does not exist")
        for alias in meta.get("aliases", []) or []:
            if alias in ids and alias != rec["id"]:
                errors.append(f"{rel}: alias {alias!r} conflicts with a canonical skill id")
            if alias in aliases and aliases[alias] != rec["id"]:
                errors.append(f"{rel}: alias {alias!r} is already owned by {aliases[alias]!r}")
            aliases[alias] = rec["id"]
        for package in meta.get("package", []) or []:
            packages.setdefault(package, set()).add(rec["id"])

    # Every pinned package must map to one canonical skill, allowing package aliases.
    pinned = root / "references" / "default-tools.txt"
    if pinned.is_file():
        for line in pinned.read_text(encoding="utf-8").splitlines():
            pkg = line.strip()
            if pkg and not pkg.startswith("#") and pkg not in packages:
                errors.append(f"references/default-tools.txt: no canonical skill maps package {pkg!r}")

    # manifest must exist and mirror the tree
    manifest_path = root / "manifest.yaml"
    if not manifest_path.is_file():
        errors.append("manifest.yaml missing (run scripts/build-manifest.py)")
    else:
        try:
            manifest = parse_simple_yaml(manifest_path.read_text(encoding="utf-8"))
        except FrontmatterError as exc:
            errors.append(f"manifest.yaml: {exc}")
            manifest = None
        if manifest is not None:
            mskills = {s.get("id") for s in manifest.get("skills", [])}
            if mskills != ids:
                missing = sorted(ids - mskills)
                extra = sorted(mskills - ids)
                errors.append(f"manifest.yaml out of sync (missing={missing}, extra={extra}); rerun scripts/build-manifest.py")
            if manifest.get("license") != LICENSE_ID:
                errors.append("manifest.yaml: license mismatch")
    return errors, warnings


def main() -> int:
    errors, warnings = validate()
    for w in warnings:
        print(f"warning: {w}")
    if errors:
        for e in errors:
            print(f"error: {e}", file=sys.stderr)
        print(f"\n{len(errors)} error(s), {len(warnings)} warning(s)", file=sys.stderr)
        return 1
    print(f"OK: valid ({len(warnings)} warning(s))")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
