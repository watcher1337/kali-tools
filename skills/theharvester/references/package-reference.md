<!-- generated: scripts/generate-tool-skills.py; package=theharvester -->
# theharvester: package reference

## What it is

`theharvester` is the Debian/Kali package mapped to the `theharvester` skill. A
package can provide several executables, services, libraries, or data files;
the package name is **not** assumed to be an executable. In this catalog the
package sits in the **dns-infrastructure** category, where tools typically answer
which records exist for approved names, which servers are authoritative,
and how resolution routes through delegations and resolvers. This reference makes no unverified claim about this
package's flags, output, or security impact; it teaches how to approach the
category safely while you discover the installed commands.

## Install and verify

In an approved Kali environment, inspect availability before installing:

```bash
dpkg -s theharvester
apt-cache policy theharvester
```

If the operator approves installing it, use the local package-manager policy,
for example `sudo apt install theharvester`, then record the installed version.
Installation changes the environment; it is not an assessment action and may
need a separate change approval.

## How to use

Follow the category workflow with the installed command's own help as the
syntax authority:

1. Confirm the approved domain list and record types.
2. Query known-good names first to validate your resolver path.
3. Query one record type at a time; keep query volume low.
4. Compare answers across the authoritative server and one neutral resolver.

Always substitute only operator-supplied approved values, and confirm local
help matches the installed version before running anything.

## When to use

Use when the approved objective needs authoritative DNS record, delegation, and resolution-path questions for approved domains and no more focused curated
skill in this catalog already answers the question.

## When not to use

Do not use when scope, authorization, rate limits, credentials, or the effect
of the selected executable is unknown. Do not treat an installed package as
permission to scan, authenticate, alter data, or access evidence. Do not use
it to substitute a curated skill whose bounded workflow already fits the
approved task.

## Common pitfalls

- Wildcard records make every invented name resolve; test a random name
  to detect this before trusting any discovery result.
- Cached answers differ from authoritative answers; note TTLs and which
  server answered.
- Zone transfers are intrusive and rarely in scope; request approval or
  do not attempt them.
- High query rates to authoritative servers look like abuse and may
  trigger rate limiting or blocks.

## Interpretation guidance

A record is an observation published by an authority, not proof of
ownership or liveness. Absence in one resolver proves nothing global;
propagation and caching delay changes.

## Suggestions and next decisions

- Prefer an executable's local help over online snippets or guessed syntax.
- If multiple commands are installed, choose the least intrusive one that
  answers the approved question.
- If the package exposes a service or state-changing command, obtain explicit
  approval before starting it.
- If no suitable executable is present, report that limitation rather than
  substituting another tool silently.
- If the result is ambiguous, validate the smallest harmless indicator by hand
  instead of widening the run.

## Failure handling and evidence

Capture the package version, chosen executable, exact help consulted,
sanitized command, target, timestamp, output, and errors in the engagement
evidence directory. Expected artifacts for this category include
queried names, record types, resolver used, full answers with TTLs, and timestamps. Redact credentials, tokens, cookies, personal data, and
sensitive artifacts. A command error is evidence of a limitation, not a reason
to guess flags or retry aggressively.

## Scope and approval checklist

- Approved domains and record types are enumerated in advance.
- Query rate and total query count stay small.
- No zone transfer, dynamic update, or registry change without separate approval.

## Local sources

- [Skill workflow](../SKILL.md)
- Installed package metadata and manual pages are the authority for this
  starter's version-specific behavior.
