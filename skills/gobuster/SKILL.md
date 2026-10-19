---
name: gobuster
description: Use when an authorized assessment needs bounded directory or DNS discovery with Gobuster and an approved wordlist.
license: GPL-3.0-only
metadata:
  category: web-discovery
  type: tool
  status: curated
  source: manual
  package: [gobuster]
  executable: [gobuster]
  capabilities: [shell, network, wordlists, evidence-handling]
  activation: [An approved web URL or DNS domain, wordlist, and request limit require bounded discovery]
  prerequisites: [Explicit target, mode, wordlist, rate/concurrency, and stop-contact approval]
  related: [ffuf, dirb, dnsrecon]
  verification: kali-help
---
# Gobuster

## Identity
Gobuster performs wordlist-driven directory, DNS, and virtual-host discovery. A result is a candidate, not authorization or a finding.

## Activation
Use the `dir` or `dns` mode only for the approved URL or domain and objective.

## Do not use when
Do not use large wordlists, extension spraying, broad DNS expansion, or aggressive threads when a smaller approved test answers the question.

## Prerequisites
Confirm target/mode, wordlist, response baseline, request ceiling, and stop contact. Check `gobuster --help` and mode-specific help.

## Execution patterns
Captured help supports directory status filtering, threads, and output:
```bash
gobuster dir -u 'https://<authorized-host>/' -w <approved-wordlist> \
  -t 5 -s 200,204,301,302,307,401,403 -o results/gobuster-dir.txt
```
Use `-t` at or below the approved concurrency. For DNS, query only the approved domain and do not follow discovered names outside scope.

## Interpretation
A status code or DNS response can be a soft-404, wildcard, redirect, or stale record. Inspect a minimal sample manually; do not access sensitive paths merely because they appear.

## Decision rules
Stop for 429/5xx/WAF behavior or scope drift. If a candidate needs validation, use the smallest read-only request and escalate only with approval.

## Evidence
Record mode, wordlist, rate/concurrency, version, sanitized command, baseline, output, and manually checked candidates.

## Related tools
Use `ffuf` for flexible HTTP fuzzing and `dnsrecon` for approved DNS investigation. Do not run overlapping discovery tools without a distinct question.

## Safety
Directory and DNS discovery create traffic. Keep wordlists and concurrency small; never treat discovery as permission to access data.

## Common rationalizations and rebuttals
| Rationalization | Rebuttal |
| --- | --- |
| “DNS results expand scope.” | They are observations; the allowlist controls scope. |

## Red flags
Wildcard DNS, rate limiting, unexpected content, or a request to increase threads requires a stop.

## Verification and exit criteria
Finish with bounded output, manual interpretation, and a documented stop or approved follow-up.
