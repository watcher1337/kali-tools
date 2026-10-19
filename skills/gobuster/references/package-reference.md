<!-- curated: manual reference for the gobuster skill; extendable, do not regenerate -->
# gobuster: operational reference

## What it is

Gobuster performs wordlist-driven directory (`dir`), DNS (`dns`), and
virtual-host (`vhost`) discovery against approved targets. In this catalog
it is the bounded discovery instrument for web and DNS enumeration. A
result is a candidate for inspection, not authorization or a finding. The
canonical bounded workflow is [SKILL.md](../SKILL.md).

Command patterns below come from the captured help of the assessed version
and are proposed invocations, never evidence they ran.

## Install and verify

- Kali/Debian package: `gobuster`. Executable: `gobuster`.
- Inspect: `apt-cache policy gobuster`; verify installed: `dpkg -s gobuster`.
- Install only with change approval: `sudo apt install gobuster`.
- Verify options: `gobuster --help` and the mode help (`gobuster dir --help`).

## Quick start

```bash
# Directory discovery with documented status filter and bounded threads
gobuster dir -u 'https://<authorized-host>/' -w <approved-wordlist> \
  -t 5 -s 200,204,301,302,307,401,403 -o results/gobuster-dir.txt

# DNS subdomain discovery for one approved domain
gobuster dns -d <approved-domain> -w <approved-wordlist> -t 5 \
  -o results/gobuster-dns.txt
```

Use `-t` at or below the approved concurrency. For DNS, query only the
approved domain and never follow discovered names outside scope.

## How to use

1. Confirm target/mode (`dir`, `dns`, `vhost`), wordlist, request ceiling,
   and stop contact from the approval.
2. Establish the response baseline: request one known-missing path (dir) or
   one random name (dns) and document its behavior.
3. Run at the approved thread count; keep output files in the evidence
   directory.
4. Inspect a minimal sample of candidates manually before recording them.

## Key options (from captured help)

| Option | Role |
| --- | --- |
| `dir`/`dns`/`vhost` | Mode; each has its own subcommand help. |
| `-u <url>` | Base URL (dir/vhost modes). |
| `-d <domain>` | Domain (dns mode). |
| `-w <file>` | Approved wordlist. |
| `-t <n>` | Threads; keep at or below the approved concurrency. |
| `-s <codes>` | Status codes to include. |
| `-o <file>` | Output file. |

## When to use

- Approved directory or virtual-host discovery on a single web target.
- Approved DNS enumeration where discovered names do not expand scope.
- When the engagement favors status-filtered, file-output discovery over
  flexible fuzzing.

## When not to use

- Large wordlists, extension spraying, broad DNS expansion, or aggressive
  threads when a smaller approved test answers the question.
- Credentialed or state-changing requests inside discovery.
- When `ffuf` already covers the approved objective; do not run overlapping
  discovery tools without a distinct question.

## Common issues and troubleshooting

| Symptom | Likely cause | Bounded response |
| --- | --- | --- |
| Wildcard DNS answers everything | Subdomain wildcard record | Test a random name; treat all matches as noise until proven otherwise. |
| Every path 200 | Soft-404 catch-all | Baseline a missing path; compare sizes/redirects manually. |
| 429/5xx responses | Rate limiting engaged | Stop; concurrency reduction needs approval. |
| Empty output, no errors | Status filter excludes real hits | Re-check the documented baseline codes before widening `-s`. |

## Suggestions and decisions

- A smaller wordlist at approved concurrency beats a big one that trips
  defenses; scope decides wordlist growth.
- Candidate validation uses the smallest read-only request; escalate only
  with approval.
- DNS results are observations; the allowlist, not the result, controls
  scope.
- Stop when the approved question is answered.

## Failure handling and evidence

Record mode, wordlist, rate/concurrency, version, sanitized command,
baseline, output, and manually checked candidates. Redact cookies,
authorization headers, and sensitive response content. Wildcard or
rate-limit behavior is evidence of the target's defenses; capture it rather
than engineering around it.

## Local sources

- Installed `gobuster --help` and per-mode help are the version authority.
- The canonical workflow lives in [SKILL.md](../SKILL.md).
