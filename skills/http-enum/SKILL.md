---
name: http-enum
description: Use when an authorized assessment needs read-only HTTP(S) response, header, TLS, or documented-endpoint inspection.
license: GPL-3.0-only
metadata:
  category: network-reconnaissance
  type: tool
  status: curated
  source: manual
  executable: [curl]
  capabilities: [shell, network, evidence-handling]
  activation: [An approved URL needs bounded read-only HTTP response or header inspection]
  prerequisites: [Explicit URL, allowed methods, redirect policy, and rate limit]
  related: [curl, whatweb, nikto]
  verification: kali-help
---
# HTTP enumeration

## Reference

Read the self-contained [operational reference](references/package-reference.md) for installation, selection, suggestions, and failure handling.

## Identity
This workflow uses `curl` for read-only inspection; `http-enum` is the catalog/package selector. Headers, banners, and redirects are observations, not vulnerabilities.

## Activation
Use for a specified approved URL when response headers, redirect behavior, public `robots.txt`/`security.txt`, TLS details, or documented endpoints need inspection.

## Do not use when
Do not submit forms, probe undocumented administration paths, impersonate users, or add authentication headers without approval.

## Prerequisites
Confirm canonical URL, allowed virtual hosts/methods, authenticated-testing policy, rate limit, and stop contact. Check the installed `curl --help`.

## Execution patterns
```bash
curl --silent --show-error --head --location 'https://<authorized-host>/'
curl --silent --show-error --request OPTIONS --include 'https://<authorized-host>/'
```
Use `OPTIONS` only where the method is approved. Keep redirects and request count bounded.

## Interpretation
Headers and version-like values can be altered, generic, or incomplete. An allowed method or banner does not prove exploitable behavior. Compare only representative approved pages.

## Decision rules
Stop for redirects outside scope, unexpected sensitive content, errors, or rate limits. Route a specific approved follow-up to a relevant tool skill rather than broadening requests.

## Evidence
Record URL, timestamp, curl version, sanitized command, response status/headers, redirect chain, and interpretation. Redact cookies and sensitive headers.

## Related tools
Use `whatweb` for approved technology hints and `nikto` for separately approved vulnerability checks. Do not stack scanners without a distinct objective.

## Safety
Read-only intent is not a guarantee: redirects, OPTIONS, and headers still create traffic. Honor scope and data-handling controls.

## Common rationalizations and rebuttals
| Rationalization | Rebuttal |
| --- | --- |
| “It is just a header request.” | It is still traffic to a target and can reveal sensitive response data. |

## Red flags
Cross-scope redirects, credentials in responses, or requests to alter methods/headers require a stop.

## Verification and exit criteria
Finish when the approved response evidence is retained and claims are limited to observed behavior.
