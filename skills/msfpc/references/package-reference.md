<!-- generated: scripts/generate-tool-skills.py; package=msfpc -->
# msfpc: package reference

## What it is

`msfpc` is the Debian/Kali package mapped to the `msfpc` skill. A
package can provide several executables, services, libraries, or data files;
the package name is **not** assumed to be an executable. In this catalog the
package sits in the **exploitation** category, where tools typically answer
whether the one approved weakness yields the agreed proof of impact
on the approved target. This reference makes no unverified claim about this
package's flags, output, or security impact; it teaches how to approach the
category safely while you discover the installed commands.

## Install and verify

In an approved Kali environment, inspect availability before installing:

```bash
dpkg -s msfpc
apt-cache policy msfpc
```

If the operator approves installing it, use the local package-manager policy,
for example `sudo apt install msfpc`, then record the installed version.
Installation changes the environment; it is not an assessment action and may
need a separate change approval.

## How to use

Follow the category workflow with the installed command's own help as the
syntax authority:

1. Written approval names target, weakness, payload class, and proof.
2. Reproduce the weakness non-destructively first.
3. Use the minimal payload that achieves the agreed proof.
4. Clean up and record before/after state immediately.

Always substitute only operator-supplied approved values, and confirm local
help matches the installed version before running anything.

## When to use

Use when the approved objective needs approved exploitation of one specific validated weakness, for a defined proof and no more focused curated
skill in this catalog already answers the question.

## When not to use

Do not use when scope, authorization, rate limits, credentials, or the effect
of the selected executable is unknown. Do not treat an installed package as
permission to scan, authenticate, alter data, or access evidence. Do not use
it to substitute a curated skill whose bounded workflow already fits the
approved task.

## Common pitfalls

- Exploitation changes target state; assume damage until cleanup is
  verified.
- Public exploits can crash services; test behavior conservatively.
- Out-of-band payloads phone home to third parties; use approved
  infrastructure only.
- Backdoors and persistence created during testing must be removed and
  documented.

## Interpretation guidance

Success proves the agreed impact on that target at that time, nothing
more. Failure may mean mitigation or version drift, not absence of the
weakness.

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
approval record, exact payload and version, target, timestamp, before/after state, and cleanup confirmation. Redact credentials, tokens, cookies, personal data, and
sensitive artifacts. A command error is evidence of a limitation, not a reason
to guess flags or retry aggressively.

## Scope and approval checklist

- Target, weakness, and allowed payload class are written in the approval.
- The agreed proof of impact is defined before execution.
- Cleanup obligations and verification are agreed.
- A stop contact is live during execution.

## Local sources

- [Skill workflow](../SKILL.md)
- Installed package metadata and manual pages are the authority for this
  starter's version-specific behavior.
