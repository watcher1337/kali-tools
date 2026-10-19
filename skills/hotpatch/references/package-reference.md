<!-- generated: scripts/generate-tool-skills.py; package=hotpatch -->
# hotpatch: package reference

## What it is

`hotpatch` is the Debian/Kali package mapped to the `hotpatch` skill. A
package can provide several executables, services, libraries, or data files;
the package name is **not** assumed to be an executable. In this catalog the
package sits in the **privilege-escalation** category, where tools typically answer
which local misconfigurations, writable paths, or capability gaps
exist for one supplied session on an approved host. This reference makes no unverified claim about this
package's flags, output, or security impact; it teaches how to approach the
category safely while you discover the installed commands.

## Install and verify

In an approved Kali environment, inspect availability before installing:

```bash
dpkg -s hotpatch
apt-cache policy hotpatch
```

If the operator approves installing it, use the local package-manager policy,
for example `sudo apt install hotpatch`, then record the installed version.
Installation changes the environment; it is not an assessment action and may
need a separate change approval.

## How to use

Follow the category workflow with the installed command's own help as the
syntax authority:

1. Confirm host and session are in scope; note the host is production
   or test.
2. Enumerate read-only; avoid kernel probes or state-changing checks.
3. Manually verify each candidate (effective permission, ownership).
4. Escalate only through the explicitly approved path.

Always substitute only operator-supplied approved values, and confirm local
help matches the installed version before running anything.

## When to use

Use when the approved objective needs local misconfiguration and permission enumeration on an approved host session and no more focused curated
skill in this catalog already answers the question.

## When not to use

Do not use when scope, authorization, rate limits, credentials, or the effect
of the selected executable is unknown. Do not treat an installed package as
permission to scan, authenticate, alter data, or access evidence. Do not use
it to substitute a curated skill whose bounded workflow already fits the
approved task.

## Common pitfalls

- Some checks are noisy or can destabilize kernels; skip intrusive
  probes unless approved.
- Enumerated output leaks credentials, tokens, and other users' data;
  protect it.
- A writable service path or cron is dangerous to touch even for
  testing; modification needs explicit approval.
- Containers and sandboxes limit what local findings mean.

## Interpretation guidance

Findings are candidates until the effective permission is verified in
place. Being able to read a file is not being able to exploit the
path; exploitability needs its own approval to establish.

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
host, session identity, exact commands, raw output, and the verification note per candidate. Redact credentials, tokens, cookies, personal data, and
sensitive artifacts. A command error is evidence of a limitation, not a reason
to guess flags or retry aggressively.

## Scope and approval checklist

- Host and local session are named in the approval.
- Check set is restricted to read-only enumeration.
- No exploitation, credential use, or persistence without new approval.
- Output handling rules for captured secrets are agreed.

## Local sources

- [Skill workflow](../SKILL.md)
- Installed package metadata and manual pages are the authority for this
  starter's version-specific behavior.
