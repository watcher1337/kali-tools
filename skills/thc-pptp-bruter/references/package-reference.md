<!-- generated: scripts/generate-tool-skills.py; package=thc-pptp-bruter -->
# thc-pptp-bruter: package reference

## What it is

`thc-pptp-bruter` is the Debian/Kali package mapped to the `thc-pptp-bruter` skill. A
package can provide several executables, services, libraries, or data files;
the package name is **not** assumed to be an executable. In this catalog the
package sits in the **systems-utilities** category, where tools typically answer
which utility behavior safely answers the approved operational need
without widening exposure. This reference makes no unverified claim about this
package's flags, output, or security impact; it teaches how to approach the
category safely while you discover the installed commands.

## Install and verify

In an approved Kali environment, inspect availability before installing:

```bash
dpkg -s thc-pptp-bruter
apt-cache policy thc-pptp-bruter
```

If the operator approves installing it, use the local package-manager policy,
for example `sudo apt install thc-pptp-bruter`, then record the installed version.
Installation changes the environment; it is not an assessment action and may
need a separate change approval.

## How to use

Follow the category workflow with the installed command's own help as the
syntax authority:

1. Read the local help for the installed version first.
2. Choose the least intrusive invocation that answers the need.
3. Bind services to the narrowest interface; verify output paths.
4. Stop once the operational need is met; remove started services.

Always substitute only operator-supplied approved values, and confirm local
help matches the installed version before running anything.

## When to use

Use when the approved objective needs general system and network utility tasks (transfer, capture, archive, service helper) on approved endpoints and no more focused curated
skill in this catalog already answers the question.

## When not to use

Do not use when scope, authorization, rate limits, credentials, or the effect
of the selected executable is unknown. Do not treat an installed package as
permission to scan, authenticate, alter data, or access evidence. Do not use
it to substitute a curated skill whose bounded workflow already fits the
approved task.

## Common pitfalls

- Listeners and daemons bound to all interfaces expose data to the
  network; bind explicitly.
- Transfers can leak data off-path; confirm destinations and TLS.
- Archives may contain unexpected content; list before extracting.
- Root widens blast radius; run at the least privilege that works.

## Interpretation guidance

Utility output is raw observation. Exit codes and warnings are part of
the result; a quiet failure is still a failure.

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
tool version, exact command, endpoints or paths involved, and full output including errors. Redact credentials, tokens, cookies, personal data, and
sensitive artifacts. A command error is evidence of a limitation, not a reason
to guess flags or retry aggressively.

## Scope and approval checklist

- Endpoints, paths, and interfaces are named in the approval.
- Privileges required are the minimum needed.
- Data classes handled are known and permitted.
- Any service started is removed at the end.

## Local sources

- [Skill workflow](../SKILL.md)
- Installed package metadata and manual pages are the authority for this
  starter's version-specific behavior.
