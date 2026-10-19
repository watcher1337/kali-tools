<!-- generated: scripts/generate-tool-skills.py; package=gss-ntlmssp -->
# gss-ntlmssp: package reference

## What it is

`gss-ntlmssp` is the Debian/Kali package mapped to the `gss-ntlmssp` skill. A
package can provide several executables, services, libraries, or data files;
the package name is **not** assumed to be an executable. In this catalog the
package sits in the **smb-active-directory** category, where tools typically answer
whether one designated test credential is accepted by one approved
service, under a known lockout policy. This reference makes no unverified claim about this
package's flags, output, or security impact; it teaches how to approach the
category safely while you discover the installed commands.

## Install and verify

In an approved Kali environment, inspect availability before installing:

```bash
dpkg -s gss-ntlmssp
apt-cache policy gss-ntlmssp
```

If the operator approves installing it, use the local package-manager policy,
for example `sudo apt install gss-ntlmssp`, then record the installed version.
Installation changes the environment; it is not an assessment action and may
need a separate change approval.

## How to use

Follow the category workflow with the installed command's own help as the
syntax authority:

1. Confirm the lockout threshold, allowed protocol, and test window.
2. Use one host, one account, one attempt at minimum concurrency.
3. Record the single result; do not retry on failure.
4. Any follow-up (enumeration, command execution) requires a new, specific approval.

Always substitute only operator-supplied approved values, and confirm local
help matches the installed version before running anything.

## When to use

Use when the approved objective needs controlled validation of one supplied credential against one approved host and protocol and no more focused curated
skill in this catalog already answers the question.

## When not to use

Do not use when scope, authorization, rate limits, credentials, or the effect
of the selected executable is unknown. Do not treat an installed package as
permission to scan, authenticate, alter data, or access evidence. Do not use
it to substitute a curated skill whose bounded workflow already fits the
approved task.

## Common pitfalls

- Repeated failures lock accounts and trigger security alerts; there is
  no harmless retry.
- Authentication relays and hash forwarding are separate intrusive
  techniques, never part of a validation test.
- Accepted credentials say nothing about authorization level or data
  access.
- Passwords and hashes leak into shell history, logs, and process
  listings; keep them out of all of those.

## Interpretation guidance

One success means the service accepted the material under that
protocol. It does not establish privilege, and a failure may be
network, DNS, policy, or clock skew rather than a wrong credential.

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
host and protocol, tool version, sanitized command, the single result, and the lockout constraints. Redact credentials, tokens, cookies, personal data, and
sensitive artifacts. A command error is evidence of a limitation, not a reason
to guess flags or retry aggressively.

## Scope and approval checklist

- Host, account, and protocol are individually named in the approval.
- Attempt count and concurrency are fixed in advance.
- Credential handling and storage rules are agreed.
- A stop contact is available during the test window.

## Local sources

- [Skill workflow](../SKILL.md)
- Installed package metadata and manual pages are the authority for this
  starter's version-specific behavior.
