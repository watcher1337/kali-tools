---
name: nuclei
description: Use when an authorized assessment needs selected, reviewed, non-destructive Nuclei template checks with manual validation.
license: GPL-3.0-only
metadata:
  category: vulnerability-assessment
  type: tool
  status: curated
  source: manual
  package: [nuclei]
  executable: [nuclei]
  capabilities: [shell, network, evidence-handling]
  activation:
    - Reviewed templates and an approved target/rate limit are available for a bounded validation task
  prerequisites:
    - Template review, explicit target scope, and approval for request volume and callbacks
  related: [nikto, sslscan, ffuf]
  verification: kali-help
---

# Nuclei

## Identity

Nuclei (`nuclei`, package `nuclei`) executes templates against targets. A template match is a scanner alert, not a confirmed vulnerability; template behavior and request volume determine risk.

## Activation

Use only after selecting reviewed templates or tags that are appropriate for the approved target and explicitly excluding state-changing, authentication, fuzzing, code, headless, and out-of-band behavior unless approved.

## Do not use when

Do not run all templates by default, auto-update templates without review, use `-dast`, `-code`, or callback/OAST templates, or scan targets discovered outside scope. Do not treat an alert as a reportable finding without validation.

## Prerequisites

Confirm target allowlist, template revision/source, rate/concurrency ceiling, callbacks policy, sensitive-output handling, and stop contact. Verify exact options with `nuclei -version` and `nuclei --help`; inspect selected templates before execution.

## Execution patterns

The captured help supports target `-u`, template/tag filtering, rate limit `-rl`, concurrency `-c`, JSONL `-j`, output `-o`, and `-ni` to disable Interactsh. For reviewed low-impact tags:

```bash
nuclei -u 'https://<authorized-host>' -tags exposure,misconfig \
  -rl 5 -c 1 -ni -j -o results/nuclei.jsonl
```

Replace tags only with reviewed selections. The command is a bounded pattern, not an executed scan or a safe-template guarantee.

## Interpretation

A match means its matcher condition succeeded. Check the template ID and request/response context, then reproduce the minimum non-destructive indicator manually. A match can be stale, context-dependent, or false positive; a non-match does not establish absence.

## Decision rules

Stop for unexpected requests, callbacks, errors, rate limiting, sensitive response data, or any template whose behavior is unclear. Validate only the minimum indicator. If validated impact would require exploitation, credentials, data access, or state changes, obtain approval before continuing.

## Evidence

Preserve target, template IDs/revision, version, filters, rate/concurrency, timestamp, JSONL output, and sanitized validation evidence. Redact headers, tokens, and sensitive response content.

## Related tools

Use `ffuf` for bounded content discovery and `nikto`/`sslscan` for their specific approved checks. Do not stack scanners without a distinct objective.

## Safety

Templates are executable testing content. Enforce template review, target scope, `-ni`, conservative rate/concurrency, and approval gates for all callbacks or stateful behavior.

## Common rationalizations and rebuttals

| Rationalization | Rebuttal |
| --- | --- |
| “It is only an info template.” | Template side effects and request volume still need review. |
| “Nuclei matched, so it is confirmed.” | A matcher is an indicator; validate a minimal harmless condition. |

## Red flags

Unreviewed template updates, OAST/callback behavior, DAST/code/headless templates, target expansion, or sensitive results require stopping.

## Verification and exit criteria

Finish when template selection/revision, limits, output, and manual validation status are recorded, with unmatched claims clearly distinguished from confirmed findings.
