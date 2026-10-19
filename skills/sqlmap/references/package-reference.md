<!-- curated: manual reference for the sqlmap skill; extendable, do not regenerate -->
# sqlmap: operational reference

## What it is

SQLMap automates SQL-injection testing for one explicitly approved
parameter. It can generate stateful and high-impact requests; a detection
is a lead, not permission to extract data or execute commands. In this
catalog it is the least-invasive validation instrument for the
web-application category. The canonical bounded workflow is
[SKILL.md](../SKILL.md).

Command patterns below come from the captured help of the assessed version
and are proposed invocations, never evidence they ran.

## Install and verify

- Kali/Debian package: `sqlmap`. Executable: `sqlmap`.
- Inspect: `apt-cache policy sqlmap`; verify installed: `dpkg -s sqlmap`.
- Install only with change approval: `sudo apt install sqlmap`.
- Verify: `sqlmap --version` and `sqlmap --help` for the installed version.

## Quick start

```bash
# One approved parameter from a sanitized request file, minimum settings
sqlmap -r sanitized-request.txt -p '<approved-parameter>' \
  --batch --level=1 --risk=1 --threads=1 --output-dir=results/sqlmap
```

This is a proposed, bounded pattern — not evidence it ran and not a
guarantee of non-impact. Do not add extraction or post-exploitation options
without a new approval.

## How to use

1. Confirm the exact request/parameter, allowed methods, rate/latency
   limits, data-integrity rules, test window, and stop contact.
2. Sanitize the captured request into a file: strip live cookies and
   tokens or replace them with approved test values.
3. Run at `--level=1 --risk=1 --threads=1` against the single parameter.
4. Validate the smallest harmless indicator manually; record whether the
   result reproduces.
5. Stop. Extraction, dumping, tamper scripts, and shells are separate,
   explicitly approved activities.

## Key options (from captured help)

| Option | Role |
| --- | --- |
| `-r <file>` | Sanitized request file; the safe substitute for live URLs. |
| `-p <param>` | The single approved parameter. |
| `--batch` | No interactive prompts; keeps runs scriptable and bounded. |
| `--level` / `--risk` | Test depth and payload risk; keep both at `1`. |
| `--threads=1` | Minimal concurrency. |
| `--output-dir <dir>` | Keeps per-run artifacts in the evidence directory. |

## When to use

- One approved suspected parameter with credible prior injection evidence.
- Safe test environments, or production with written approval.
- Minimal validation of a specific technique before any manual proof.

## When not to use

- Broad crawling, blind parameter hunting, data dumping, OS commands, file
  access, shells, tamper scripts, or evasion.
- Any target whose data-integrity rules are unknown.
- When the engagement has not approved request volume and state risk.

## Common issues and troubleshooting

| Symptom | Likely cause | Bounded response |
| --- | --- | --- |
| Immediate WAF block page | Protective layer engaged | Stop; bypass/evasion needs separate approval. |
| Growing latency/errors | Payloads affecting availability | Stop; record as impact signal. |
| Session invalidated mid-run | CSRF/token rotation | Stop; re-sanitize only with approval. |
| "Not injectable" at level 1 | Shallow test depth | Record as inconclusive; deeper levels are a scope decision. |

## Suggestions and decisions

- Neither a response difference nor tool output alone proves data access;
  reproduce the minimum indicator by hand.
- Keep risk, level, threads, and target scope at the approved minimum for
  every run, not just the first.
- Stop for errors, latency, unexpected state changes, WAF responses, or
  sensitive output.
- Escalate only after a documented minimal validation and explicit
  authorization.

## Failure handling and evidence

Preserve the sanitized request, `sqlmap --version`, exact parameter,
limits, output directory, timestamps, and validation notes. Protect and
redact cookies, tokens, and response data. The final record must state
whether any extraction or stateful action occurred (normally: none).

## Local sources

- Installed `sqlmap --help` is the authority for the installed version.
- The canonical workflow lives in [SKILL.md](../SKILL.md).
