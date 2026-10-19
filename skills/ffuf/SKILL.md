---
name: ffuf
description: Use when an authorized assessment needs rate-limited web content discovery against an explicitly approved base URL with ffuf.
license: GPL-3.0-only
metadata:
  category: web-discovery
  type: tool
  status: curated
  source: manual
  package: [ffuf]
  executable: [ffuf]
  capabilities: [shell, network, wordlists, evidence-handling]
  activation:
    - An approved web URL, wordlist, request rate, and discovery objective are available
  prerequisites:
    - Explicit HTTP scope including routes, methods, rate limit, and exclusions
  related: [gobuster, dirb, wfuzz]
  verification: kali-help
---

# ffuf

## Reference

Read the self-contained [operational reference](references/package-reference.md) for installation, selection, suggestions, and failure handling.

## Identity

ffuf (`ffuf`, package `ffuf`) makes wordlist-driven HTTP requests. A response match identifies a candidate to inspect; it does not prove content exposure, authorization, or a vulnerability.

## Activation

Use for approved content discovery after confirming the base URL, allowed paths/methods, wordlist, and request ceiling.

## Do not use when

Do not use against login, payment, state-changing, or third-party endpoints without explicit approval. Do not use broad wordlists, recursion, mutation, credentialed requests, or a default 40-thread run when limits are unknown.

## Prerequisites

Verify `ffuf -V` and `ffuf --help`. Request a known missing path to establish a baseline response. Create an evidence directory and use an approved small wordlist.

## Execution patterns

The captured help supports URL fuzzing, `-w`, `-u`, `-rate`, `-mc`, `-o`, `-of`, and `-t`:

```bash
ffuf -w <approved-wordlist> -u 'https://<authorized-host>/FUZZ' \
  -rate 10 -t 1 -mc 200,204,301,302,307,401,403 \
  -of json -o results/ffuf-content.json
```

Set `-rate` at or below the approved ceiling and retain low concurrency (`-t 1`) unless the engagement permits more. Filter the observed baseline with `-fs`, `-fw`, or `-fl` only after documenting it. `-ac` proposes filters; review rather than blindly accept them.

## Interpretation

Status, size, word count, and redirect differences are triage signals. Soft-404 behavior and WAF responses cause false positives. A 401/403 can show a route exists but does not authorize access; do not bypass controls.

## Decision rules

If responses become unstable, error-heavy, or rate-limited, stop and lower load only with approval. Manually inspect a minimal sample of candidates with a read-only request. Stop when the approved discovery objective is satisfied; escalate only to a relevant skill with approval.

## Evidence

Preserve baseline request/result, wordlist identity, version, sanitized command, rate/concurrency, JSON output, timestamp, and manually verified candidates. Never publish cookies, authorization headers, or response bodies containing sensitive data.

## Related tools

Use `gobuster` or `dirb` only when their workflow better fits the approved task; do not run several directory fuzzers redundantly. Use `wfuzz` for approved custom request fuzzing.

## Safety

Each word expands traffic. Respect URL/path/method scope, rate limits, and data-handling rules. Do not send credentials or state-changing payloads without separate approval.

## Common rationalizations and rebuttals

| Rationalization | Rebuttal |
| --- | --- |
| “It is GET-only.” | GET can still be expensive and expose sensitive material. |
| “403 means it is safe to continue.” | It proves neither safety nor permission to bypass access controls. |

## Red flags

Login redirects, 429/5xx spikes, WAF blocks, unexpected sensitive content, or a request to raise threads/rate require a stop and operator decision.

## Verification and exit criteria

Finish with the approved URL, baseline, rate/concurrency, output, manually checked candidates, and a statement that candidates are not confirmed findings.
