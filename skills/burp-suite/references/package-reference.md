<!-- curated: manual reference for the burp-suite skill; extendable, do not regenerate -->
# burp-suite: operational reference

## What it is

Burp Suite is an interactive web-security testing platform: it proxies,
inspects, replays, and modifies HTTP traffic between an approved browser
and an approved target. That capability is stateful and can expose
credentials and sensitive data, which is why this catalog treats it as an
approval-gated manual instrument for the web-application category. The
canonical bounded workflow is [SKILL.md](../SKILL.md); this reference adds
installation and environment guidance and deliberately gives no unverified
UI click-sequence.

## Install and verify

- Kali/Debian package: `burpsuite` (skill id `burp-suite`; `burpsuite` is a
  package alias, not a second installable skill).
- Inspect: `apt-cache policy burpsuite`; verify installed:
  `dpkg -s burpsuite`.
- Install only with change approval: `sudo apt install burpsuite`.
- On first launch, record the edition (Community or Pro) and version from
  the UI: features and licensing differ, and the edition bounds what the
  engagement can do (e.g., professional-only scanning).
- Configure the approved browser to proxy through Burp's listener only for
  approved hosts; keep interception off outside active review.

## How to use

1. Confirm approved hosts, proxy/browser configuration, allowed methods,
   authentication/data handling, rate limits, and stop contact.
2. Launch Burp, set the proxy listener, and point only the approved
   browser profile at it.
3. Load the single approved URL; inspect the captured request/response in
   proxy history.
4. Annotate findings in context; move one request to repeater for read-only
   re-examination only when needed.
5. Export sanitized evidence and shut down the proxy when finished.

## Operating guidance

- Treat proxy history as a sensitive store: it accumulates cookies,
  tokens, and personal data passively. Restrict access to the evidence
  workstation.
- Repeater replay is potentially state-changing; check the method and
  authorization before every send.
- Intruder, active scanning, and login testing are separate approval
  gates, never part of passive inspection.
- Edition-specific controls live in the installed UI; verify them there
  rather than from memory or screenshots.

## When to use

- Approved manual HTTP inspection when passive evidence identified a
  specific request or behavior to examine.
- Minimal validation of observed request/response behavior.
- Sanitized capture of evidence for a web-assessment finding.

## When not to use

- Proxying third-party traffic, intercepting credentials without
  approval, or replaying state-changing requests.
- Active scanning, brute force, or login testing without separate
  authorization.
- When `ffuf` or `sqlmap` objectives are separately approved; do not stack
  web tools without a distinct question.

## Common issues and troubleshooting

| Symptom | Likely cause | Bounded response |
| --- | --- | --- |
| Browser refuses connection | Proxy listener/cert not trusted | Import the CA into the approved browser profile only. |
| Traffic from unrelated sites | Browser profile leaks | Restrict the proxy scope to approved hosts; close other tabs. |
| Replay returns 403/redirect | Session, CSRF, or cache drift | Compare with the original capture; do not re-authenticate without approval. |
| History full of secrets | Passive capture working as designed | Treat history as protected evidence; redact every export. |

## Suggestions and decisions

- If one observation answers the question, export sanitized evidence and
  stop; the proxy does not need to stay up.
- A replayed response differing from the original is usually session,
  CSRF, cache, or server state — not a new finding by itself.
- Never export passwords, cookies, tokens, or unnecessary response bodies
  into reports or chat.

## Failure handling and evidence

Save sanitized request/response excerpts, target, timestamp, edition and
version, and the manual conclusion in the evidence directory. Redact
cookies, authorization headers, tokens, and personal data from every copy
that leaves it. Unapproved domains appearing in history, live-session
secrets, or non-idempotent methods are stop signals requiring an operator
decision.

## Local sources

- The installed Burp UI and its built-in documentation are the authority
  for edition-specific behavior.
- The canonical workflow lives in [SKILL.md](../SKILL.md).
