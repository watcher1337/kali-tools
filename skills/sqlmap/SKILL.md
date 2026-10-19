---
name: sqlmap
description: Use when an explicitly authorized assessment needs least-invasive SQL injection validation for one suspected parameter.
license: GPL-3.0-only
metadata:
  category: web-application
  type: tool
  status: curated
  source: manual
  package: [sqlmap]
  executable: [sqlmap]
  capabilities: [shell, network, evidence-handling]
  activation: [A specific approved parameter has credible injection evidence and safe validation approval]
  prerequisites: [Written target/parameter scope and explicit approval for any request volume or state risk]
  related: [burp-suite, nuclei]
  verification: kali-help
---
# SQLMap

## Reference

Read the self-contained [operational reference](references/package-reference.md) for installation, selection, suggestions, and failure handling.

## Identity
SQLMap automates SQL injection testing. It can generate stateful and high-impact requests; a detection is a lead, not permission to extract data or execute commands.

## Activation
Use only for one approved suspected parameter in a safe test environment or with written production approval.

## Do not use when
Do not use for broad crawling, blind parameter hunting, data dumping, OS commands, file access, shells, tamper scripts, or evasion.

## Prerequisites
Confirm exact request/parameter, allowed methods, rate/latency limits, data-integrity rules, test window, and stop contact. Use a sanitized request file and check `sqlmap --help` for the installed version.

## Execution patterns
The captured help supports request files, parameter selection, risk/level, threads, batch mode, and output directories:
```bash
sqlmap -r sanitized-request.txt -p '<approved-parameter>' \
  --batch --level=1 --risk=1 --threads=1 --output-dir=results/sqlmap
```
This is a proposed, bounded pattern—not evidence it ran or a guarantee of non-impact. Do not add extraction or post-exploitation options without a new approval.

## Interpretation
A reported technique can be a false positive or context-dependent. Manually validate the smallest harmless indicator; neither a response difference nor tool output alone proves data access or vulnerability impact.

## Decision rules
Stop for errors, latency, unexpected state changes, WAF responses, or sensitive output. Escalate only after a documented minimal validation and explicit authorization.

## Evidence
Preserve sanitized request, tool/version, exact parameter, limits, output, timestamps, and validation notes. Protect and redact cookies, tokens, and response data.

## Related tools
Use Burp Suite for approved manual request inspection and Nuclei for selected template checks. Neither removes SQLMap’s approval gate.

## Safety
Keep risk, level, threads, and target scope at the approved minimum. Never dump data or seek a shell by default.

## Common rationalizations and rebuttals
| Rationalization | Rebuttal |
| --- | --- |
| “It is only a scanner.” | Its payloads can affect availability and state; safe settings still need approval. |

## Red flags
Unexpected writes, delays, sensitive data, or requests to enable dumping/shell options require an immediate stop.

## Verification and exit criteria
Finish with a minimal validation or an inconclusive result, evidence, and a clear statement that no extraction or stateful action occurred.
