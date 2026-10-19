<!-- curated: manual reference for the ffuf skill; extendable, do not regenerate -->
# ffuf: operational reference

## What it is

ffuf ("Fuzz Faster U Fool") drives wordlist-based HTTP requests against an
approved base URL and prints responses that differ from the documented
baseline. In this catalog it is the flexible web-discovery instrument for
explicitly approved targets. A response match is a candidate to inspect; it
does not prove content exposure, authorization, or a vulnerability. The
canonical bounded workflow is [SKILL.md](../SKILL.md).

Command patterns below come from the captured help of the assessed version
and are proposed invocations, never evidence they ran.

## Install and verify

- Kali/Debian package: `ffuf`. Executable: `ffuf`.
- Inspect: `apt-cache policy ffuf`; verify installed: `dpkg -s ffuf`.
- Install only with change approval: `sudo apt install ffuf`.
- Verify options match this reference: `ffuf -V` and `ffuf --help`.

## Quick start

```bash
# Baseline first: run against a known-missing path with the planned filters,
# and record its status/size/words/lines before the real run.

# Bounded content discovery at the approved ceiling
ffuf -w <approved-wordlist> -u 'https://<authorized-host>/FUZZ' \
  -rate 10 -t 1 -mc 200,204,301,302,307,401,403 \
  -of json -o results/ffuf-content.json
```

## How to use

1. Confirm the base URL, allowed paths/methods, wordlist, and request
   ceiling from the approval.
2. Request a known-missing path; record status, size, word count, and
   redirect behavior as the baseline.
3. Run at `-rate` at or below the approved ceiling and `-t 1` unless the
   engagement permits more.
4. Filter the observed baseline with `-fs` (size), `-fw` (word count), or
   `-fl` (line count) only after documenting it. `-ac` proposes filters;
   review rather than blindly accept them.
5. Manually re-request a minimal sample of candidates with a read-only
   request before recording anything.

## Key options (from captured help)

| Option | Role |
| --- | --- |
| `-w <file>` | Approved wordlist; its size multiplies request volume. |
| `-u <url>` | Target URL with the `FUZZ` placeholder. |
| `-rate <n>` | Requests per second; keep at or below the approved ceiling. |
| `-t <n>` | Concurrent threads; `1` is the conservative default here. |
| `-mc <codes>` | Match codes to report. |
| `-fs`/`-fw`/`-fl` | Filter by size/words/lines against the documented baseline. |
| `-ac` | Auto-calibrate from responses; review its proposals. |
| `-o`/`-of` | Output file and format (e.g. `json`). |

## When to use

- Approved content discovery where the base URL, wordlist, and rate are
  named in writing.
- Baseline-then-filter discovery on a single host before any manual
  inspection.
- Custom request fuzzing only when the approved objective specifically
  needs it.

## When not to use

- Login, payment, state-changing, or third-party endpoints without explicit
  approval.
- Broad wordlists, recursion, mutation, credentialed requests, or default
  high concurrency when limits are unknown.
- When `gobuster` or `dirb` already answers the approved question; do not
  run several directory fuzzers redundantly.

## Common issues and troubleshooting

| Symptom | Likely cause | Bounded response |
| --- | --- | --- |
| Every path matches | Soft-404 or wildcard host | Rebuild baseline with a random path; re-filter and re-run. |
| Sudden 429/5xx flood | Rate limit or WAF engaged | Stop; lower rate only with approval. |
| Candidates all same size | Redirecting catch-all | Compare redirect targets manually, do not follow off-host. |
| TLS errors | SNI/certificate mismatch | Verify the host header and certificate scope before continuing. |

## Suggestions and decisions

- Start with the smallest approved wordlist; growth is a scope decision.
- Manually inspect a minimal sample of candidates with a read-only request.
- A 401/403 shows a route exists; it does not authorize access and must not
  be bypassed.
- Stop when the approved discovery objective is satisfied; escalate only to
  a relevant skill with approval.

## Failure handling and evidence

Preserve the baseline request/result, wordlist identity, version, sanitized
command, rate/concurrency, JSON output, timestamp, and manually verified
candidates. Redact cookies, authorization headers, and response bodies
containing sensitive data. Error floods and rate-limit responses are
evidence of a boundary; record them rather than retrying wider.

## Local sources

- Installed `ffuf --help` is the authority for the installed version.
- The canonical workflow lives in [SKILL.md](../SKILL.md).
