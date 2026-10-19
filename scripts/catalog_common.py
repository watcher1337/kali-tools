#!/usr/bin/env python3
"""Shared catalog logic: frontmatter parsing, categories, validation constants.

Stdlib only. Imported by the scripts in this directory and by the tests
(tests add this directory to sys.path).
"""

from __future__ import annotations

import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]

# --- Canonical enums (see references/skill-format.md) ---------------------

CATEGORIES = frozenset(
    {
        "master",
        "network-reconnaissance",
        "dns-infrastructure",
        "web-discovery",
        "vulnerability-assessment",
        "smb-active-directory",
        "web-application",
        "password-auditing",
        "privilege-escalation",
        "wireless",
        "forensics",
        "exploitation",
        "systems-utilities",
    }
)

CAPABILITIES = frozenset(
    {
        "shell",
        "network",
        "root",
        "credentials",
        "wordlists",
        "gpu",
        "interactive-gui",
        "wireless-hardware",
        "evidence-handling",
    }
)

VERIFICATION = frozenset({"kali-help", "official-docs", "none"})
STATUSES = frozenset({"curated", "starter"})
TYPES = frozenset({"tool", "master"})
SKILL_ID_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")

TOOL_SECTIONS = (
    "## Identity",
    "## Activation",
    "## Do not use when",
    "## Prerequisites",
    "## Execution patterns",
    "## Interpretation",
    "## Decision rules",
    "## Evidence",
    "## Related tools",
    "## Safety",
)

MASTER_HEADINGS = ("## Mandatory safety gate", "## Workflow")

# Marker written by the original starter generator. Files containing it are
# treated as regenerable starter content by scripts/generate-tool-skills.py.
GENERATED_MARKER = "is in the pinned Kali Linux default-package manifest"

LICENSE_ID = "GPL-3.0-only"

# Installable skills live directly under skills/<skill-id>/SKILL.md. The root
# SKILL.md is only a compatibility pointer and is deliberately not discovered.
SKILLS_DIR = "skills"
NON_SKILL_DIRS = frozenset(
    {
        SKILLS_DIR,
        "scripts",
        "tests",
        "schemas",
        "adapters",
        "integrations",
        "workflows",
        "references",
        "dist",
        "node_modules",
        ".git",
    }
)

# --- Category classification ---------------------------------------------
# Explicit lists for security-relevant packages; everything else falls back to
# systems-utilities. Order matters: first match wins.

_CATEGORY_LISTS: tuple[tuple[str, tuple[str, ...]], ...] = (
    (
        "network-reconnaissance",
        (
            "nmap",
            "masscan",
            "rustscan",
            "arp-scan",
            "arping",
            "hping3",
            "fping",
            "netdiscover",
            "nbtscan",
            "dmitry",
            "onesixtyone",
            "ike-scan",
            "lbd",
            "netmask",
            "traceroute",
            "sbd",
            "http-enum",
            "zenmap",
            "netcat-traditional",
            "cryptcat",
        ),
    ),
    (
        "dns-infrastructure",
        (
            "bind9-dnsutils",
            "dig",
            "dnsenum",
            "dnsrecon",
            "dnsx",
            "dns2tcp",
            "dnschef",
            "fierce",
            "iodine",
            "rebind",
            "theharvester",
            "amass",
            "subfinder",
            "whois",
            "recon-ng",
        ),
    ),
    (
        "web-discovery",
        (
            "ffuf",
            "gobuster",
            "feroxbuster",
            "dirsearch",
            "dirb",
            "dirbuster",
            "wfuzz",
            "whatweb",
            "curl",
            "wget",
            "httpx",
            "wafw00f",
            "cutycapt",
            "skipfish",
        ),
    ),
    (
        "vulnerability-assessment",
        (
            "nuclei",
            "nikto",
            "testssl.sh",
            "sslscan",
            "sslyze",
            "qsslcaudit",
            "faraday",
            "legion",
        ),
    ),
    (
        "smb-active-directory",
        (
            "netexec",
            "smbclient",
            "enum4linux",
            "enum4linux-ng",
            "samba",
            "samba-common-bin",
            "smbmap",
            "gss-ntlmssp",
            "certipy-ad",
            "impacket-scripts",
            "python3-impacket",
            "gpp-decrypt",
            "passing-the-hash",
            "ldapsearch",
            "ldap-utils",
            "bloodhound",
            "bloodhound-python",
            "cifs-utils",
            "evil-winrm",
        ),
    ),
    (
        "web-application",
        (
            "burp-suite",
            "burpsuite",
            "sqlmap",
            "wpscan",
            "commix",
            "davtest",
            "webshells",
            "weevely",
            "mitmproxy",
            "spiderfoot",
        ),
    ),
    (
        "password-auditing",
        (
            "john",
            "hashcat",
            "hashcat-utils",
            "hash-identifier",
            "hashid",
            "maskprocessor",
            "statsprocessor",
            "crunch",
            "patator",
            "hydra",
            "hydra-gtk",
            "ncrack",
            "ophcrack",
            "ophcrack-cli",
            "cewl",
            "rsmangler",
            "chntpw",
            "samdump2",
            "creddump7",
            "pipal",
            "ophcrack",
        ),
    ),
    (
        "privilege-escalation",
        ("peass", "unix-privesc-check", "windows-binaries", "wce", "hotpatch"),
    ),
    (
        "wireless",
        (
            "aircrack-ng",
            "kismet",
            "wifite",
            "fern-wifi-cracker",
            "bully",
            "reaver",
            "pixiewps",
            "spooftooph",
            "bluez",
            "fern-wifi-cracker",
        ),
    ),
    (
        "forensics",
        (
            "autopsy",
            "binwalk",
            "binwalk3",
            "bulk-extractor",
            "hashdeep",
            "sleuthkit",
            "scalpel",
            "testdisk",
            "guymager",
            "magicrescue",
            "pdf-parser",
            "pdfid",
            "exiv2",
            "libimage-exiftool-perl",
            "scrounge-ntfs",
            "foremost",
        ),
    ),
    (
        "exploitation",
        (
            "metasploit-framework",
            "exploitdb",
            "set",
            "msfpc",
            "powershell-empire",
            "starkiller",
            "mimikatz",
            "powersploit",
            "responder",
            "gophish",
            "weevely",
            "laudanum",
            "sqlmap",
        ),
    ),
)


def classify(package: str) -> str:
    """Return the catalog category for a skill id / package name."""
    if package == "kali-tools":
        return "master"
    for category, names in _CATEGORY_LISTS:
        if package in names:
            return category
    return "systems-utilities"


# --- Frontmatter (minimal YAML subset) ------------------------------------
# Supported shapes (documented in references/skill-format.md):
#   key: scalar
#   key: [a, b]
#   metadata:
#     key: scalar
#     key: [a, b]
#     key:
#       - item


class FrontmatterError(ValueError):
    pass


def _scalar(value: str) -> object:
    value = value.strip()
    if value.startswith("[") and value.endswith("]"):
        inner = value[1:-1].strip()
        return [v.strip() for v in inner.split(",") if v.strip()]
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


def parse_frontmatter(text: str) -> tuple[dict, str]:
    """Split a SKILL.md into (frontmatter dict, markdown body)."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise FrontmatterError("missing opening '---'")
    end = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end = i
            break
    if end is None:
        raise FrontmatterError("missing closing '---'")

    fm: dict = {}
    i = 1
    while i < end:
        line = lines[i]
        if not line.strip() or line.lstrip().startswith("#"):
            i += 1
            continue
        if line.startswith(" "):
            raise FrontmatterError(f"unexpected indent outside metadata: {line!r}")
        m = re.match(r"^([A-Za-z0-9_/-]+):\s*(.*)$", line)
        if not m:
            raise FrontmatterError(f"cannot parse line: {line!r}")
        key, rest = m.group(1), m.group(2)
        if key == "metadata" and rest.strip() == "":
            meta, i = _parse_metadata(lines, i + 1, end)
            fm["metadata"] = meta
            continue
        fm[key] = _scalar(rest)
        i += 1
    return fm, "\n".join(lines[end + 1 :])


def _parse_metadata(lines: list[str], i: int, end: int) -> tuple[dict, int]:
    meta: dict = {}
    while i < end:
        line = lines[i]
        if not line.strip():
            i += 1
            continue
        if not line.startswith("  "):
            break
        m = re.match(r"^  ([A-Za-z0-9_/-]+):\s*(.*)$", line)
        if not m:
            raise FrontmatterError(f"cannot parse metadata line: {line!r}")
        key, rest = m.group(1), m.group(2)
        if rest.strip() == "":
            items: list = []
            j = i + 1
            while j < end and lines[j].strip().startswith("- ") and lines[j].startswith("    "):
                items.append(_scalar(lines[j].strip()[2:]))
                j += 1
            meta[key] = items
            i = j
            continue
        meta[key] = _scalar(rest)
        i += 1
    return meta, i


def dump_frontmatter(fm: dict) -> str:
    """Serialize a frontmatter dict back to canonical text (including fences)."""
    out = ["---"]
    meta = fm.get("metadata", {})
    for key, value in fm.items():
        if key == "metadata":
            continue
        out.append(f"{key}: {_dump_scalar(value)}")
    if meta:
        out.append("metadata:")
        for key, value in meta.items():
            if isinstance(value, list):
                if value:
                    out.append(f"  {key}: [{', '.join(str(v) for v in value)}]")
                else:
                    out.append(f"  {key}: []")
            else:
                out.append(f"  {key}: {_dump_scalar(value)}")
    out.append("---")
    return "\n".join(out)


def _dump_scalar(value: object) -> str:
    if isinstance(value, list):
        return "[" + ", ".join(str(v) for v in value) + "]"
    return str(value)


# --- Catalog discovery -----------------------------------------------------


def skill_dirs(root: Path | None = None) -> list[Path]:
    """All canonical skill directories (skills/<id>/SKILL.md)."""
    root = root or REPO_ROOT
    skills = root / SKILLS_DIR
    if not skills.is_dir():
        return []
    return sorted(d for d in skills.iterdir() if d.is_dir() and (d / "SKILL.md").is_file())


def read_skill(path: Path) -> tuple[dict, str]:
    return parse_frontmatter(path.read_text(encoding="utf-8"))


def skill_id_of(path: Path) -> str:
    return path.name if path.name != "SKILL.md" else "kali-tools"


def load_catalog(root: Path | None = None) -> list[dict]:
    """Return one record per skill: id, path, frontmatter, body."""
    root = root or REPO_ROOT
    records = []
    for d in skill_dirs(root):
        p = d / "SKILL.md"
        fm, body = read_skill(p)
        records.append({"id": d.name, "dir": d, "path": p, "fm": fm, "body": body})
    return records


# --- manifest.yaml reader (YAML subset used by build-manifest.py) ---------
# Supported: top-level scalars/flow lists, one nested mapping level, and a
# block sequence of single-level mappings under a top-level key. Generated
# output is also valid YAML for strict parsers; when PyYAML is available,
# tests cross-check both interpretations.


def _split_flow(inner: str) -> list[str]:
    """Split a flow-list body on commas, ignoring commas inside double quotes."""
    parts: list[str] = []
    buf: list[str] = []
    in_quote = False
    for ch in inner:
        if ch == '"':
            in_quote = not in_quote
            buf.append(ch)
        elif ch == "," and not in_quote:
            parts.append("".join(buf))
            buf = []
        else:
            buf.append(ch)
    parts.append("".join(buf))
    return [p.strip() for p in parts if p.strip()]


def _scalar_q(value: str) -> object:
    value = value.strip()
    if value.startswith("[") and value.endswith("]"):
        return [_scalar(v) for v in _split_flow(value[1:-1])]
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


def parse_simple_yaml(text: str) -> dict:
    """Parse the YAML subset emitted by build-manifest.py.

    Supported shapes: top-level ``key: value`` scalars and flow lists; a nested
    mapping one level deep; a block sequence of flat mappings (``- key: value``
    items whose continuation keys are indented two spaces deeper). Sequence
    values inside those items must be flow lists.
    """
    lines = [
        (len(raw) - len(raw.lstrip(" ")), raw.strip())
        for raw in text.splitlines()
        if raw.strip() and not raw.lstrip().startswith("#")
    ]
    value, i = _parse_block(lines, 0, lines[0][0] if lines else 0)
    if i != len(lines):
        raise FrontmatterError(f"trailing content at line: {lines[i][1]!r}")
    if not isinstance(value, dict):
        raise FrontmatterError("document root must be a mapping")
    return value


def _parse_block(lines: list[tuple[int, str]], i: int, indent: int):
    if i >= len(lines):
        return {}, i
    if lines[i][1].startswith("- "):
        return _parse_seq(lines, i, indent)
    return _parse_map(lines, i, indent)


def _parse_map(lines: list[tuple[int, str]], i: int, indent: int):
    out: dict = {}
    while i < len(lines):
        cur_indent, line = lines[i]
        if cur_indent < indent or line.startswith("- "):
            break
        if cur_indent > indent:
            raise FrontmatterError(f"unexpected indent: {line!r}")
        key, sep, rest = line.partition(":")
        if not sep:
            raise FrontmatterError(f"cannot parse line: {line!r}")
        key, rest = key.strip(), rest.strip()
        if rest:
            out[key] = _scalar_q(rest)
            i += 1
        else:
            if i + 1 >= len(lines) or lines[i + 1][0] <= indent:
                out[key] = {}
                i += 1
            else:
                child, i = _parse_block(lines, i + 1, lines[i + 1][0])
                out[key] = child
    return out, i


def _parse_seq(lines: list[tuple[int, str]], i: int, indent: int):
    out: list = []
    while i < len(lines):
        cur_indent, line = lines[i]
        if cur_indent != indent or not line.startswith("- "):
            break
        item = line[2:].strip()
        if ":" in item and not item.startswith(("[", '"', "'")):
            key, _, rest = item.partition(":")
            entry: dict = {key.strip(): _scalar_q(rest)} if rest.strip() else {key.strip(): {}}
            i += 1
            cont_indent = indent + 2
            while i < len(lines) and lines[i][0] == cont_indent and not lines[i][1].startswith("- "):
                ckey, sep, crest = lines[i][1].partition(":")
                if not sep:
                    raise FrontmatterError(f"cannot parse line: {lines[i][1]!r}")
                entry[ckey.strip()] = _scalar_q(crest) if crest.strip() else {}
                i += 1
            out.append(entry)
        else:
            out.append(_scalar_q(item))
            i += 1
    return out, i
