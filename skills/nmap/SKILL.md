---
name: nmap
description: Use when an authorized assessment needs scoped, low-impact host, port, or service enumeration with Nmap.
license: GPL-3.0-only
metadata:
  category: network-reconnaissance
  type: tool
  status: curated
  source: manual
  package: [nmap]
  executable: [nmap]
  capabilities: [shell, network, evidence-handling]
  activation:
    - The approved objective requires host, port, or service inventory for explicitly allowed targets
  prerequisites:
    - Written host and port scope, timing limit, and stop contact
  related: [masscan, zenmap]
  verification: kali-help
---

# Nmap

## Reference

Read the self-contained [operational reference](references/package-reference.md) for installation, selection, suggestions, and failure handling.

## Identity

Nmap (`nmap`, package `nmap`) discovers hosts, ports, and service/version responses. Open or filtered ports are observations; they do not establish a vulnerability, ownership, or authorization.

## Activation

Use after scope identifies exact hosts or ranges and the objective needs an inventory. Prefer a specified small port set before broader coverage.

## Do not use when

Do not use for unapproved Internet-wide ranges, to expand scope from DNS results, or when passive evidence already answers the question. Do not use intrusive scripts, OS detection, UDP scans, evasion, or spoofing unless specifically approved.

## Prerequisites

Confirm allowlisted targets, ports, scan type, timing/rate limits, test window, and stop contact. Verify the installed version and options with `nmap -V` and `nmap --help`; create an evidence directory outside the repository.

## Execution patterns

For one approved host and explicit ports, the captured help supports:

```bash
nmap -sV -T3 -p 22,80,443 -oA results/nmap-services <authorized-host>
```

`-sV` probes open ports for service/version information; `-p` constrains ports; `-oA` writes normal, XML, and grepable output. `-T3` is a timing template, not a substitute for an agreed rate limit. Use `-Pn` only when testing hosts that block discovery is explicitly allowed.

## Interpretation

`open` indicates Nmap received a response consistent with an accepting service; `closed` and `filtered` do not prove host absence. A banner or version is not a vulnerability. Record host-discovery assumptions and distinguish timeout/error output from negative evidence.

## Decision rules

If a target is absent from the allowlist or results imply scope expansion, stop. If a responsive approved host exposes a relevant service, use the smallest matching tool skill for a read-only follow-up. If the inventory answers the objective, stop rather than broadening ports or scripts.

## Evidence

Keep the `.nmap`, `.xml`, and `.gnmap` outputs plus target scope, timestamp, version, sanitized command, and errors. Redact confidential hostnames or banners from distributed reports.

## Related tools

Use `masscan` only where its higher-speed behavior is explicitly approved. Use `zenmap` for approved interactive visualization. This skill is the conservative service-inventory baseline.

## Safety

Nmap sends network traffic. Keep targets/ports narrow and concurrency conservative; stop on instability. Do not use evasion, spoofing, brute force, exploit scripts, or disruptive UDP scanning without written approval.

## Common rationalizations and rebuttals

| Rationalization | Rebuttal |
| --- | --- |
| “It is only discovery.” | Discovery can load systems and cross scope. Honor the target and timing limits. |
| “A banner proves the CVE.” | Validate a minimal non-destructive condition; versions can be patched or misleading. |

## Red flags

Unexpected hosts, high packet loss, IDS notifications, or requests to add `-Pn`, broad ranges, or NSE scripts require an operator decision.

## Verification and exit criteria

Finish only when the approved target/ports, Nmap version, output files, interpretation, and a stop or approved next-step decision are recorded.
