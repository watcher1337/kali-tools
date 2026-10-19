---
name: burp-suite
description: Use when an authorized assessment needs controlled HTTP inspection or manual validation with Burp Suite in an explicitly approved environment.
license: GPL-3.0-only
metadata:
  category: web-application
  type: tool
  status: curated
  source: manual
  aliases: [burpsuite]
  package: [burpsuite]
  capabilities: [interactive-gui, network, evidence-handling]
  activation:
    - An approved web-assessment objective requires manual request and response inspection
  prerequisites:
    - Explicit HTTP scope, proxy configuration approval, and sensitive-data handling rules
  related: [ffuf, sqlmap, mitmproxy]
  verification: official-docs
---

# Burp Suite

## Identity

Burp Suite is an interactive web-security testing platform. It can inspect, replay, and modify HTTP traffic; that capability is stateful and can expose credentials and sensitive data.

## Activation

Use for approved manual HTTP inspection or minimal validation after passive evidence identifies a specific request or behavior to examine.

## Do not use when

Do not proxy third-party traffic, intercept credentials without approval, replay state-changing requests, or use active scanning without a separate authorization.

## Prerequisites

Confirm approved hosts, proxy/browser configuration, allowed methods, authentication/data handling, rate limits, and stop contact. Verify the installed edition/version and create a protected evidence location.

## Execution patterns

Start with proxy history or a single approved read-only request. Inspect and annotate the request/response before using repeater. Verify edition-specific controls in the installed UI; this skill intentionally gives no unverified UI sequence.

## Interpretation

An observed request shows what the approved client exchanged; it does not prove a vulnerability. A replayed response can differ because of session, CSRF, cache, or server state.

## Decision rules

Stop before sending a modified or repeated state-changing request. Escalate active scanning, login testing, or data retrieval only with explicit approval. If one observation answers the question, export sanitized evidence and stop.

## Evidence

Save sanitized request/response excerpts, target, timestamp, tool version, and the manual conclusion. Do not export passwords, cookies, tokens, or unnecessary response bodies.

## Related tools

Use `ffuf` for bounded content discovery and `sqlmap` only for separately approved suspected injection validation. `burpsuite` is a package alias, not a second installable skill.

## Safety

Keep interception scoped to approved traffic. Disable interception when not actively reviewing, and treat repeater/intruder/active scanner actions as potentially state-changing.

## Common rationalizations and rebuttals

| Rationalization | Rebuttal |
| --- | --- |
| “Repeater is just viewing.” | Replaying can change server state. Check method and authorization first. |
| “The proxy captured a token, so include it in the report.” | Retain secrets only in protected evidence and redact distributed material. |

## Red flags

Unapproved domains, live-session secrets, non-idempotent methods, or requests to enable active scanning require a stop.

## Verification and exit criteria

Finish when the exact approved request, sanitized evidence, interpretation, and any approval-gated next step are recorded.
