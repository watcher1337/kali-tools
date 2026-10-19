<!-- curated: manual reference for the http-enum skill; extendable, do not regenerate -->
# http-enum: operational reference

## What it is

The `http-enum` skill is the catalog selector for read-only HTTP(S)
inspection; the underlying executable is `curl`, which is normally present
on Kali. It covers response headers, redirect behavior, TLS details, and
documented endpoints such as `robots.txt` and `security.txt`. Headers,
banners, and redirects are observations, not vulnerabilities. The canonical
bounded workflow is [SKILL.md](../SKILL.md).

Command patterns below come from the captured help of the assessed version
and are proposed invocations, never evidence they ran.

## Install and verify

- No dedicated package: the skill maps to the `curl` executable.
- Verify presence and version: `curl --version`; package check:
  `dpkg -s curl`.
- If absent, install only with change approval: `sudo apt install curl`.
- Confirm flags: `curl --help` (the installed version is the authority).

## Quick start

```bash
# Response headers and redirect chain for one approved URL
curl --silent --show-error --head --location 'https://<authorized-host>/'

# Method advertisement on an approved endpoint
curl --silent --show-error --request OPTIONS --include 'https://<authorized-host>/'
```

Use `OPTIONS` only where the method is approved. Keep redirects and request
count bounded; `--location` follows redirects and each hop is a new request
(and possibly a new host).

## How to use

1. Confirm the canonical URL, allowed virtual hosts/methods, redirect
   policy, and rate limit from the approval.
2. Request headers (`--head`) for the approved URL; record status and full
   header set.
3. Follow redirects only while every hop stays inside approved scope.
4. Request documented files (`/robots.txt`, `/.well-known/security.txt`)
   only when the approval covers them.
5. Compare only representative approved pages; stop when the question is
   answered.

## Key options (from captured help)

| Option | Role |
| --- | --- |
| `--silent --show-error` | Quiet output with errors still reported. |
| `--head` | Headers only (`-I`), the least intrusive fetch. |
| `--location` | Follow redirects; each hop is extra traffic. |
| `--request OPTIONS` | Method query; approved methods only. |
| `--include` | Include response headers in the body output. |

## When to use

- Approved URL needs bounded read-only response, header, or TLS
  inspection.
- Redirect chains and method advertisements need documenting.
- Documented endpoint files (`robots.txt`, `security.txt`) are in scope.

## When not to use

- Form submission, undocumented administration paths, user impersonation,
  or added authentication headers without approval.
- Crawling or recursive fetching; this skill inspects, it does not
  discover.
- When `whatweb` or `nikto` objectives are separately approved; do not
  stack scanners without a distinct question.

## Common issues and troubleshooting

| Symptom | Likely cause | Bounded response |
| --- | --- | --- |
| Redirect leaves approved scope | Cross-host redirect | Stop following; record the target as an observation. |
| TLS handshake error | Certificate/SNI mismatch | Record the error; verify the approved hostname before retrying once. |
| Empty body with 200 | `--head` on servers that mishandle HEAD | Switch to a bounded GET of the same approved URL. |
| Credentials appear in response | Misconfigured target | Stop; treat as sensitive evidence, redact everywhere. |

## Suggestions and decisions

- Headers and version-like values can be altered, generic, or incomplete;
  record them as observed, not as fact.
- An allowed method or banner does not prove exploitable behavior.
- Route a specific approved follow-up to the relevant tool skill rather
  than broadening requests.
- One observation that answers the question ends the task.

## Failure handling and evidence

Record URL, timestamp, `curl --version`, sanitized command, response
status/headers, redirect chain, and interpretation. Redact cookies,
authorization headers, and tokens from every copy. Cross-scope redirects
and sensitive response content are stop signals; preserve them as evidence
of the boundary.

## Local sources

- Installed `curl --help` and `man curl` are the version authority.
- The canonical workflow lives in [SKILL.md](../SKILL.md).
