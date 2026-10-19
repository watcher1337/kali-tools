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

# Per-category operational guidance. Every value is deliberately generic,
# help-first, and flag-free: it teaches how to approach the category safely,
# never tool-specific syntax. classify() falls back to systems-utilities.
CATEGORY_GUIDE: dict[str, dict[str, str]] = {
    "network-reconnaissance": {
        "role": "host, port, and service inventory for explicitly allowed targets",
        "questions": (
            "which approved hosts respond, which ports or services they expose,\n"
            "and how traffic between you and them is filtered"
        ),
        "workflow": (
            "1. Confirm the exact target list; expand nothing from DNS or routing results.\n"
            "2. Read the local help and pick the smallest probe set that answers the\n"
            "   approved inventory question.\n"
            "3. Establish a baseline (a known-down address or a single known host) so\n"
            "   timeouts can be distinguished from silence.\n"
            "4. Run the smallest scan, record probe types and timing, then stop at the\n"
            "   approved port/host coverage."
        ),
        "pitfalls": (
            "- A silent host is not an absent host: filtered probes look identical to\n"
            "  dead hosts. Never infer absence from one probe type.\n"
            "- Skipping host discovery multiplies traffic across every listed address;\n"
            "  it needs explicit approval for that reason.\n"
            "- Service/version probes and UDP coverage are slow and heavier than\n"
            "  plain port probes; add them only when the objective requires it.\n"
            "- Banners and version strings can be masked, generic, or stale."
        ),
        "interpretation": (
            "Port states are observations under the probes you sent, not facts about\n"
            "the host. A response timeout may be filtering, rate limiting, or loss. A\n"
            "version string is a candidate identity, never a confirmed patch level."
        ),
        "evidence": "target list, probe types, port coverage, timing/rate, raw output files, and the baseline",
        "scope": (
            "- Target addresses or ranges are written and allowlisted.\n"
            "- Port coverage and probe types are named in the approval.\n"
            "- Packet rate or timing ceiling and test window are agreed.\n"
            "- A stop contact exists before the first packet."
        ),
    },
    "dns-infrastructure": {
        "role": "authoritative DNS record, delegation, and resolution-path questions for approved domains",
        "questions": (
            "which records exist for approved names, which servers are authoritative,\n"
            "and how resolution routes through delegations and resolvers"
        ),
        "workflow": (
            "1. Confirm the approved domain list and record types.\n"
            "2. Query known-good names first to validate your resolver path.\n"
            "3. Query one record type at a time; keep query volume low.\n"
            "4. Compare answers across the authoritative server and one neutral resolver."
        ),
        "pitfalls": (
            "- Wildcard records make every invented name resolve; test a random name\n"
            "  to detect this before trusting any discovery result.\n"
            "- Cached answers differ from authoritative answers; note TTLs and which\n"
            "  server answered.\n"
            "- Zone transfers are intrusive and rarely in scope; request approval or\n"
            "  do not attempt them.\n"
            "- High query rates to authoritative servers look like abuse and may\n"
            "  trigger rate limiting or blocks."
        ),
        "interpretation": (
            "A record is an observation published by an authority, not proof of\n"
            "ownership or liveness. Absence in one resolver proves nothing global;\n"
            "propagation and caching delay changes."
        ),
        "evidence": "queried names, record types, resolver used, full answers with TTLs, and timestamps",
        "scope": (
            "- Approved domains and record types are enumerated in advance.\n"
            "- Query rate and total query count stay small.\n"
            "- No zone transfer, dynamic update, or registry change without separate approval."
        ),
    },
    "web-discovery": {
        "role": "wordlist-driven content, route, or virtual-host discovery against an approved base URL",
        "questions": (
            "which approved paths, virtual hosts, or routes exist on the target and\n"
            "which of those responses deserve manual inspection"
        ),
        "workflow": (
            "1. Request one known-missing path and record its status, size, and\n"
            "   behavior; this baseline exposes soft-404 pages.\n"
            "2. Start with the smallest approved wordlist at the approved rate.\n"
            "3. Filter results against the documented baseline; review automatic\n"
            "   filter suggestions instead of accepting them blindly.\n"
            "4. Manually re-request a minimal sample of candidates with a read-only\n"
            "   request before recording anything as a candidate."
        ),
        "pitfalls": (
            "- Soft-404 and wildcard hosts answer 200 for everything; without a\n"
            "  baseline every path looks like a finding.\n"
            "- Redirect chains can leave the approved scope; follow nothing\n"
            "  off-host without approval.\n"
            "- TLS/SNI mismatches and certificate errors change responses per host\n"
            "  header; record which host header was used.\n"
            "- Each word multiplies request volume; rate limits and WAFs engage\n"
            "  quickly and are a stop signal, not a challenge."
        ),
        "interpretation": (
            "Status, length, and redirect differences are triage signals only. A\n"
            "401 or 403 shows a route exists, not that access is possible or\n"
            "permitted. Discovery output is a candidate list, never a finding list."
        ),
        "evidence": "baseline response, wordlist identity and size, filters applied, rate/concurrency, raw output, and the manually verified sample",
        "scope": (
            "- Base URL, allowed methods, and excluded paths are written.\n"
            "- Wordlist size and request ceiling are approved.\n"
            "- Virtual-host names, if tested, come from an approved list.\n"
            "- No credentialed or state-changing requests inside discovery."
        ),
    },
    "vulnerability-assessment": {
        "role": "bounded validation of specific weaknesses with reviewed, non-destructive checks",
        "questions": (
            "whether a specific, approved weakness shows its minimal safe indicator\n"
            "on an approved target"
        ),
        "workflow": (
            "1. Select the exact checks or templates; read what each one sends before\n"
            "   running it.\n"
            "2. Exclude state-changing, brute-force, code-execution, and out-of-band\n"
            "   behavior unless separately approved.\n"
            "3. Run at the lowest rate against one target at a time.\n"
            "4. Re-validate any match manually with the smallest harmless request\n"
            "   before recording it."
        ),
        "pitfalls": (
            "- Full default profiles are broad and frequently intrusive; run selected\n"
            "  checks, not everything.\n"
            "- Scanner updates change template behavior between runs; record the\n"
            "  exact version or revision used.\n"
            "- Out-of-band and callback checks send data to third parties; they need\n"
            "  explicit approval.\n"
            "- Matches go stale: server changes, feature flags, and middleware all\n"
            "  produce false positives."
        ),
        "interpretation": (
            "A match is a scanner alert, not a confirmed vulnerability; a non-match\n"
            "is not proof of absence. Impact, exploitability, and business relevance\n"
            "require separate manual validation."
        ),
        "evidence": "target, tool and check/template versions, filters, rate, raw output, and the manual validation note",
        "scope": (
            "- Target list and approved check set are written down.\n"
            "- Callback/out-of-band policy is decided before the run.\n"
            "- Request rate ceiling and stop conditions are agreed.\n"
            "- Sensitive-response handling rules are known."
        ),
    },
    "smb-active-directory": {
        "role": "controlled validation of one supplied credential against one approved host and protocol",
        "questions": (
            "whether one designated test credential is accepted by one approved\n"
            "service, under a known lockout policy"
        ),
        "workflow": (
            "1. Confirm the lockout threshold, allowed protocol, and test window.\n"
            "2. Use one host, one account, one attempt at minimum concurrency.\n"
            "3. Record the single result; do not retry on failure.\n"
            "4. Any follow-up (enumeration, command execution) requires a new, "
            "specific approval."
        ),
        "pitfalls": (
            "- Repeated failures lock accounts and trigger security alerts; there is\n"
            "  no harmless retry.\n"
            "- Authentication relays and hash forwarding are separate intrusive\n"
            "  techniques, never part of a validation test.\n"
            "- Accepted credentials say nothing about authorization level or data\n"
            "  access.\n"
            "- Passwords and hashes leak into shell history, logs, and process\n"
            "  listings; keep them out of all of those."
        ),
        "interpretation": (
            "One success means the service accepted the material under that\n"
            "protocol. It does not establish privilege, and a failure may be\n"
            "network, DNS, policy, or clock skew rather than a wrong credential."
        ),
        "evidence": "host and protocol, tool version, sanitized command, the single result, and the lockout constraints",
        "scope": (
            "- Host, account, and protocol are individually named in the approval.\n"
            "- Attempt count and concurrency are fixed in advance.\n"
            "- Credential handling and storage rules are agreed.\n"
            "- A stop contact is available during the test window."
        ),
    },
    "web-application": {
        "role": "least-invasive validation of one suspected application-layer weakness on an approved parameter or request",
        "questions": (
            "whether one approved parameter or request exhibits a specific\n"
            "suspected weakness under safe test settings"
        ),
        "workflow": (
            "1. Capture or sanitize the exact request; work from a file, not from\n"
            "   live browsing.\n"
            "2. Name the single parameter or request under test.\n"
            "3. Use the lowest risk/level/intensity the tool supports; one thread.\n"
            "4. Validate the smallest harmless indicator manually, then stop."
        ),
        "pitfalls": (
            "- Automated payloads can change server state or create records; safe\n"
            "  settings still send attack traffic.\n"
            "- Session tokens and CSRF values invalidate or rotate mid-test;\n"
            "  replays can log you out or corrupt the session.\n"
            "- WAF blocks and error spikes are stop signals, not obstacles to\n"
            "  bypass.\n"
            "- Responses may contain other users' data; treat every response as\n"
            "  sensitive."
        ),
        "interpretation": (
            "A tool detection is a lead. Neither a response difference nor tool\n"
            "output alone proves data access, and impact claims need a separate,\n"
            "explicitly approved demonstration."
        ),
        "evidence": "sanitized request file, parameter, tool version, risk/level settings, output, and the validation note",
        "scope": (
            "- Exact request, parameter, and methods are written down.\n"
            "- Request volume and state-changing restrictions are agreed.\n"
            "- Data-handling rules for captured responses are known.\n"
            "- No extraction, dumping, or shell options without new approval."
        ),
    },
    "password-auditing": {
        "role": "offline auditing of lawfully obtained hashes or one approved online credential test",
        "questions": (
            "whether supplied credential material matches expectation or policy,\n"
            "without endangering accounts or leaking secrets"
        ),
        "workflow": (
            "1. Confirm the material was lawfully obtained and its storage rules.\n"
            "2. Prefer offline auditing; it endangers nothing.\n"
            "3. For online tests: one target, one account, minimum rate, known\n"
            "   lockout threshold.\n"
            "4. Record coverage (ruleset, masks), not just results."
        ),
        "pitfalls": (
            "- Online attempts lock accounts; there is no safe retry loop.\n"
            "- Cracked results are live credentials; store them as secrets, never\n"
            "  in reports, logs, or chat.\n"
            "- GPU load and heat need monitoring; hardware limits are real.\n"
            "- Uncracked does not mean strong; it means your coverage did not\n"
            "  reach the secret."
        ),
        "interpretation": (
            "A crack proves the secret was within your coverage. A non-crack says\n"
            "nothing about policy compliance without a documented ruleset and\n"
            "duration."
        ),
        "evidence": "material source, hash/credential type, tool version, ruleset or mask, duration, and result location (protected)",
        "scope": (
            "- Lawful source of material is documented.\n"
            "- Online tests name host, account, rate, and attempt ceiling.\n"
            "- Lockout policy is known before any online attempt.\n"
            "- Result storage is protected and access-controlled."
        ),
    },
    "privilege-escalation": {
        "role": "local misconfiguration and permission enumeration on an approved host session",
        "questions": (
            "which local misconfigurations, writable paths, or capability gaps\n"
            "exist for one supplied session on an approved host"
        ),
        "workflow": (
            "1. Confirm host and session are in scope; note the host is production\n"
            "   or test.\n"
            "2. Enumerate read-only; avoid kernel probes or state-changing checks.\n"
            "3. Manually verify each candidate (effective permission, ownership).\n"
            "4. Escalate only through the explicitly approved path."
        ),
        "pitfalls": (
            "- Some checks are noisy or can destabilize kernels; skip intrusive\n"
            "  probes unless approved.\n"
            "- Enumerated output leaks credentials, tokens, and other users' data;\n"
            "  protect it.\n"
            "- A writable service path or cron is dangerous to touch even for\n"
            "  testing; modification needs explicit approval.\n"
            "- Containers and sandboxes limit what local findings mean."
        ),
        "interpretation": (
            "Findings are candidates until the effective permission is verified in\n"
            "place. Being able to read a file is not being able to exploit the\n"
            "path; exploitability needs its own approval to establish."
        ),
        "evidence": "host, session identity, exact commands, raw output, and the verification note per candidate",
        "scope": (
            "- Host and local session are named in the approval.\n"
            "- Check set is restricted to read-only enumeration.\n"
            "- No exploitation, credential use, or persistence without new approval.\n"
            "- Output handling rules for captured secrets are agreed."
        ),
    },
    "wireless": {
        "role": "authorized 802.11 observation and assessment with compatible hardware",
        "questions": (
            "which authorized access points, channels, and security settings are\n"
            "present in the approved radio scope"
        ),
        "workflow": (
            "1. Confirm regulatory domain, channels, and duration in writing.\n"
            "2. Monitor on the approved channel(s) only; monitor mode, no\n"
            "   transmission.\n"
            "3. Capture a bounded window, then analyze offline.\n"
            "4. Correlate findings with the approved AP list by BSSID."
        ),
        "pitfalls": (
            "- Transmission rules are legal, not technical: injection, deauth, and\n"
            "  jamming are disruptive and need explicit written approval.\n"
            "- Channel hopping drops frames; fix the channel per capture window.\n"
            "- Captures contain third-party device identifiers and traffic; handle\n"
            "  as personal data.\n"
            "- Signal strength varies with position and environment; single-sample\n"
            "  geolocation is unreliable."
        ),
        "interpretation": (
            "Beacon security fields are the AP's claims, not verified configuration.\n"
            "A captured handshake is an artifact, not a cracked credential. Absence\n"
            "of frames is not absence of an AP."
        ),
        "evidence": "authorized AP/BSSID list, channel, capture file, duration, and tool versions",
        "scope": (
            "- Regulatory domain and channels are confirmed.\n"
            "- Duration and physical location of the test are approved.\n"
            "- No transmission, injection, or deauthentication without separate approval.\n"
            "- Capture files are stored and disposed per data rules."
        ),
    },
    "forensics": {
        "role": "evidence-preserving analysis of supplied data or images on an approved workstation",
        "questions": (
            "what artifacts, timelines, or recoverable content exist in the\n"
            "supplied evidence"
        ),
        "workflow": (
            "1. Verify and record the evidence hash; work on a verified copy.\n"
            "2. Record every command and tool version as you go.\n"
            "3. Interpret in context: timestamps, timezones, and file system quirks.\n"
            "4. Maintain chain of custody for any derived artifact."
        ),
        "pitfalls": (
            "- Mounting or scanning the original mutates metadata; always work on a\n"
            "  copy.\n"
            "- Tool versions change output formats; record versions with results.\n"
            "- Evidence contains personal and sensitive data; exposure is a\n"
            "  reportable incident.\n"
            "- Malicious files may be booby-trapped; open untrusted documents in\n"
            "  isolated tooling only."
        ),
        "interpretation": (
            "Timestamps depend on timezone, filesystem, and clock accuracy. Deleted\n"
            "content lingers until overwritten, but its presence is not proof of\n"
            "user intent or action."
        ),
        "evidence": "original hash, working-copy hash, tool versions, full command log, and derived artifact custody",
        "scope": (
            "- Supplied evidence set and working directory are defined.\n"
            "- Approved tool set and analysis methods are agreed.\n"
            "- Output and derivative handling rules are known.\n"
            "- No modification of original evidence, ever."
        ),
    },
    "exploitation": {
        "role": "approved exploitation of one specific validated weakness, for a defined proof",
        "questions": (
            "whether the one approved weakness yields the agreed proof of impact\n"
            "on the approved target"
        ),
        "workflow": (
            "1. Written approval names target, weakness, payload class, and proof.\n"
            "2. Reproduce the weakness non-destructively first.\n"
            "3. Use the minimal payload that achieves the agreed proof.\n"
            "4. Clean up and record before/after state immediately."
        ),
        "pitfalls": (
            "- Exploitation changes target state; assume damage until cleanup is\n"
            "  verified.\n"
            "- Public exploits can crash services; test behavior conservatively.\n"
            "- Out-of-band payloads phone home to third parties; use approved\n"
            "  infrastructure only.\n"
            "- Backdoors and persistence created during testing must be removed and\n"
            "  documented."
        ),
        "interpretation": (
            "Success proves the agreed impact on that target at that time, nothing\n"
            "more. Failure may mean mitigation or version drift, not absence of the\n"
            "weakness."
        ),
        "evidence": "approval record, exact payload and version, target, timestamp, before/after state, and cleanup confirmation",
        "scope": (
            "- Target, weakness, and allowed payload class are written in the approval.\n"
            "- The agreed proof of impact is defined before execution.\n"
            "- Cleanup obligations and verification are agreed.\n"
            "- A stop contact is live during execution."
        ),
    },
    "systems-utilities": {
        "role": "general system and network utility tasks (transfer, capture, archive, service helper) on approved endpoints",
        "questions": (
            "which utility behavior safely answers the approved operational need\n"
            "without widening exposure"
        ),
        "workflow": (
            "1. Read the local help for the installed version first.\n"
            "2. Choose the least intrusive invocation that answers the need.\n"
            "3. Bind services to the narrowest interface; verify output paths.\n"
            "4. Stop once the operational need is met; remove started services."
        ),
        "pitfalls": (
            "- Listeners and daemons bound to all interfaces expose data to the\n"
            "  network; bind explicitly.\n"
            "- Transfers can leak data off-path; confirm destinations and TLS.\n"
            "- Archives may contain unexpected content; list before extracting.\n"
            "- Root widens blast radius; run at the least privilege that works."
        ),
        "interpretation": (
            "Utility output is raw observation. Exit codes and warnings are part of\n"
            "the result; a quiet failure is still a failure."
        ),
        "evidence": "tool version, exact command, endpoints or paths involved, and full output including errors",
        "scope": (
            "- Endpoints, paths, and interfaces are named in the approval.\n"
            "- Privileges required are the minimum needed.\n"
            "- Data classes handled are known and permitted.\n"
            "- Any service started is removed at the end."
        ),
    },
}

DEFAULT_CATEGORY = "systems-utilities"


def guide_for(category: str) -> dict[str, str]:
    return CATEGORY_GUIDE.get(category, CATEGORY_GUIDE[DEFAULT_CATEGORY])


def reference_contents(package: str, skill_id: str, category: str) -> str:
    """Return a self-contained, help-first runtime reference for a starter skill."""
    g = guide_for(category)
    return f"""<!-- generated: scripts/generate-tool-skills.py; package={package} -->
# {package}: package reference

## What it is

`{package}` is the Debian/Kali package mapped to the `{skill_id}` skill. A
package can provide several executables, services, libraries, or data files;
the package name is **not** assumed to be an executable. In this catalog the
package sits in the **{category}** category, where tools typically answer
{g['questions']}. This reference makes no unverified claim about this
package's flags, output, or security impact; it teaches how to approach the
category safely while you discover the installed commands.

## Install and verify

In an approved Kali environment, inspect availability before installing:

```bash
dpkg -s {package}
apt-cache policy {package}
```

If the operator approves installing it, use the local package-manager policy,
for example `sudo apt install {package}`, then record the installed version.
Installation changes the environment; it is not an assessment action and may
need a separate change approval.

## How to use

Follow the category workflow with the installed command's own help as the
syntax authority:

{g['workflow']}

Always substitute only operator-supplied approved values, and confirm local
help matches the installed version before running anything.

## When to use

Use when the approved objective needs {g['role']} and no more focused curated
skill in this catalog already answers the question.

## When not to use

Do not use when scope, authorization, rate limits, credentials, or the effect
of the selected executable is unknown. Do not treat an installed package as
permission to scan, authenticate, alter data, or access evidence. Do not use
it to substitute a curated skill whose bounded workflow already fits the
approved task.

## Common pitfalls

{g['pitfalls']}

## Interpretation guidance

{g['interpretation']}

## Suggestions and next decisions

- Prefer an executable's local help over online snippets or guessed syntax.
- If multiple commands are installed, choose the least intrusive one that
  answers the approved question.
- If the package exposes a service or state-changing command, obtain explicit
  approval before starting it.
- If no suitable executable is present, report that limitation rather than
  substituting another tool silently.
- If the result is ambiguous, validate the smallest harmless indicator by hand
  instead of widening the run.

## Failure handling and evidence

Capture the package version, chosen executable, exact help consulted,
sanitized command, target, timestamp, output, and errors in the engagement
evidence directory. Expected artifacts for this category include
{g['evidence']}. Redact credentials, tokens, cookies, personal data, and
sensitive artifacts. A command error is evidence of a limitation, not a reason
to guess flags or retry aggressively.

## Scope and approval checklist

{g['scope']}

## Local sources

- [Skill workflow](../SKILL.md)
- Installed package metadata and manual pages are the authority for this
  starter's version-specific behavior.
"""


def skill_contents(package: str, skill_id: str | None = None) -> str:
    skill_id = skill_id or package
    title = package.replace("-", " ").title()
    category = classify(package)
    g = guide_for(category)
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
- Catalog role: {g['role']}.
- Purpose: consult the installed command's own documentation; this starter carries no tool-specific behavior.
- Limitations: no verified examples, output formats, or flag guidance.
- Read the self-contained [package reference](references/package-reference.md)
  before choosing an executable or installation action.

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
5. Follow the category workflow in the [package reference](references/package-reference.md).

## Interpretation

- This starter establishes nothing about output formats or result meaning.
- Treat raw output as observations, not findings; validate significant results independently before reporting them.
- Read the category interpretation guidance in the [package reference](references/package-reference.md) before drawing conclusions.

## Decision rules

- Executable not found: report the limitation and the smallest next step (approved install or execution backend). Do not improvise flags.
- Command exits with an error: capture the exact error, correct arguments only from real help output, stop after one retry.
- Result answers the approved question: record evidence and stop.
- Result inconclusive or ambiguous: switch to a curated skill or ask the operator.

## Evidence

- Save the exact command, tool version, timestamp, target, and full output in the engagement evidence directory.
- Expected artifacts for this category: {g['evidence']}.
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
        reference_path = skill_path.parent / "references" / "package-reference.md"
        if skill_path.exists():
            text = skill_path.read_text(encoding="utf-8")
            if args.overwrite or (args.upgrade_generated and GENERATED_MARKER in text):
                skill_path.write_text(skill_contents(package, skill_id), encoding="utf-8")
                reference_path.parent.mkdir(parents=True, exist_ok=True)
                reference_path.write_text(
                    reference_contents(package, skill_id, classify(package)), encoding="utf-8"
                )
                upgraded.append(package)
            else:
                skipped.append(package)
            continue
        skill_path.parent.mkdir(parents=True, exist_ok=True)
        skill_path.write_text(skill_contents(package, skill_id), encoding="utf-8")
        reference_path.parent.mkdir(parents=True, exist_ok=True)
        reference_path.write_text(
            reference_contents(package, skill_id, classify(package)), encoding="utf-8"
        )
        created.append(package)

    print(f"created={len(created)} upgraded={len(upgraded)} skipped={len(skipped)}")
    if created:
        print("created:", " ".join(created))
    if upgraded:
        print("upgraded:", " ".join(upgraded[:20]) + (" ..." if len(upgraded) > 20 else ""))


if __name__ == "__main__":
    main()
