<!-- curated: manual reference for the nuclei skill; extendable, do not regenerate -->
# nuclei: operational reference

## What it is

Nuclei executes reviewed templates against approved targets; a template
match means its matcher condition succeeded. In this catalog it is the
bounded, template-driven validation instrument for the
vulnerability-assessment category. A match is a scanner alert, not a
confirmed vulnerability, and template behavior plus request volume
determine risk. The canonical bounded workflow is [SKILL.md](../SKILL.md).

Command patterns below come from the captured help of the assessed version
and are proposed invocations, never evidence they ran.

## Install and verify

- Kali/Debian package: `nuclei`. Executable: `nuclei`.
- Inspect: `apt-cache policy nuclei`; verify installed: `dpkg -s nuclei`.
- Install only with change approval: `sudo apt install nuclei`.
- Verify: `nuclei -version` and `nuclei --help`; inspect the templates you
  selected (`head <template.yaml>`) before running anything.

## Quick start

```bash
# Reviewed low-impact tags, callbacks disabled, JSONL output
nuclei -u 'https://<authorized-host>' -tags exposure,misconfig \
  -rl 5 -c 1 -ni -j -o results/nuclei.jsonl
```

Replace tags only with reviewed selections. The command is a bounded
pattern, not an executed scan or a safe-template guarantee.

## How to use

1. Confirm the target allowlist, template revision/source, rate/concurrency
   ceiling, callbacks policy, and stop contact.
2. Select templates or tags; read each selected template's requests before
   execution.
3. Exclude state-changing, authentication, fuzzing, code, and out-of-band
   behavior unless separately approved.
4. Run one target at a time with `-ni` unless callbacks are explicitly
   approved.
5. Validate any match manually with the minimum non-destructive indicator.

## Key options (from captured help)

| Option | Role |
| --- | --- |
| `-u <url>` | Single approved target. |
| `-tags <a,b>` | Template selection by reviewed tags. |
| `-rl <n>` / `-c <n>` | Rate limit and concurrency ceilings. |
| `-ni` | Disable Interactsh callbacks; the conservative default here. |
| `-j` | JSONL output for evidence handling. |
| `-o <file>` | Output file. |

## When to use

- Selected, reviewed templates need to run against an approved target.
- A bounded validation pass with conservative rate and disabled callbacks.
- Producing JSONL evidence for later manual triage.

## When not to use

- Full template sets by default, auto-updating templates without review, or
  `-dast`/`-code`/callback templates without approval.
- Targets discovered outside scope.
- When treating a match as reportable without manual validation.

## Common issues and troubleshooting

| Symptom | Likely cause | Bounded response |
| --- | --- | --- |
| Thousands of matches | Too-broad tag selection | Stop; narrow the reviewed set, do not triage at volume. |
| Unexpected outbound callbacks | OAST template selected | Stop; `-ni` and re-review templates. |
| 429s or throttling | Rate ceiling hit | Stop; lower rate only with approval. |
| Matches not reproducible manually | Stale/context-dependent matcher | Record as unvalidated; never report as confirmed. |

## Suggestions and decisions

- Pin and record the template revision: scans are only comparable when the
  template set is identical.
- A non-match does not establish absence of the weakness.
- If validated impact would require exploitation, credentials, data
  access, or state changes, obtain approval before continuing.
- Stop when the approved validation question is answered.

## Failure handling and evidence

Preserve target, template IDs and revision, `nuclei -version`, filters,
rate/concurrency, timestamp, JSONL output, and sanitized validation
evidence. Redact headers, tokens, and sensitive response content. Callback
traffic and rate-limit responses are evidence of scope boundaries; capture
them instead of widening the run.

## Local sources

- Installed `nuclei --help` and the selected template files are the
  authority for behavior.
- The canonical workflow lives in [SKILL.md](../SKILL.md).
