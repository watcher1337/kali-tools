<!-- generated: scripts/generate-tool-skills.py; package=hash-identifier -->
# hash-identifier: package reference

## What it is

`hash-identifier` is the Debian/Kali package mapped to the `hash-identifier` skill. A
package can provide several executables, services, libraries, or data files;
the package name is **not** assumed to be an executable. In this catalog the
package sits in the **password-auditing** category, where tools typically answer
whether supplied credential material matches expectation or policy,
without endangering accounts or leaking secrets. This reference makes no unverified claim about this
package's flags, output, or security impact; it teaches how to approach the
category safely while you discover the installed commands.

## Install and verify

In an approved Kali environment, inspect availability before installing:

```bash
dpkg -s hash-identifier
apt-cache policy hash-identifier
```

If the operator approves installing it, use the local package-manager policy,
for example `sudo apt install hash-identifier`, then record the installed version.
Installation changes the environment; it is not an assessment action and may
need a separate change approval.

## How to use

Follow the category workflow with the installed command's own help as the
syntax authority:

1. Confirm the material was lawfully obtained and its storage rules.
2. Prefer offline auditing; it endangers nothing.
3. For online tests: one target, one account, minimum rate, known
   lockout threshold.
4. Record coverage (ruleset, masks), not just results.

Always substitute only operator-supplied approved values, and confirm local
help matches the installed version before running anything.

## When to use

Use when the approved objective needs offline auditing of lawfully obtained hashes or one approved online credential test and no more focused curated
skill in this catalog already answers the question.

## When not to use

Do not use when scope, authorization, rate limits, credentials, or the effect
of the selected executable is unknown. Do not treat an installed package as
permission to scan, authenticate, alter data, or access evidence. Do not use
it to substitute a curated skill whose bounded workflow already fits the
approved task.

## Common pitfalls

- Online attempts lock accounts; there is no safe retry loop.
- Cracked results are live credentials; store them as secrets, never
  in reports, logs, or chat.
- GPU load and heat need monitoring; hardware limits are real.
- Uncracked does not mean strong; it means your coverage did not
  reach the secret.

## Interpretation guidance

A crack proves the secret was within your coverage. A non-crack says
nothing about policy compliance without a documented ruleset and
duration.

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
material source, hash/credential type, tool version, ruleset or mask, duration, and result location (protected). Redact credentials, tokens, cookies, personal data, and
sensitive artifacts. A command error is evidence of a limitation, not a reason
to guess flags or retry aggressively.

## Scope and approval checklist

- Lawful source of material is documented.
- Online tests name host, account, rate, and attempt ceiling.
- Lockout policy is known before any online attempt.
- Result storage is protected and access-controlled.

## Local sources

- [Skill workflow](../SKILL.md)
- Installed package metadata and manual pages are the authority for this
  starter's version-specific behavior.
