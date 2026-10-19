<!-- generated: scripts/generate-tool-skills.py; package=hashdeep -->
# hashdeep: package reference

## What it is

`hashdeep` is the Debian/Kali package mapped to the `hashdeep` skill. A
package can provide several executables, services, libraries, or data files;
the package name is **not** assumed to be an executable. In this catalog the
package sits in the **forensics** category, where tools typically answer
what artifacts, timelines, or recoverable content exist in the
supplied evidence. This reference makes no unverified claim about this
package's flags, output, or security impact; it teaches how to approach the
category safely while you discover the installed commands.

## Install and verify

In an approved Kali environment, inspect availability before installing:

```bash
dpkg -s hashdeep
apt-cache policy hashdeep
```

If the operator approves installing it, use the local package-manager policy,
for example `sudo apt install hashdeep`, then record the installed version.
Installation changes the environment; it is not an assessment action and may
need a separate change approval.

## How to use

Follow the category workflow with the installed command's own help as the
syntax authority:

1. Verify and record the evidence hash; work on a verified copy.
2. Record every command and tool version as you go.
3. Interpret in context: timestamps, timezones, and file system quirks.
4. Maintain chain of custody for any derived artifact.

Always substitute only operator-supplied approved values, and confirm local
help matches the installed version before running anything.

## When to use

Use when the approved objective needs evidence-preserving analysis of supplied data or images on an approved workstation and no more focused curated
skill in this catalog already answers the question.

## When not to use

Do not use when scope, authorization, rate limits, credentials, or the effect
of the selected executable is unknown. Do not treat an installed package as
permission to scan, authenticate, alter data, or access evidence. Do not use
it to substitute a curated skill whose bounded workflow already fits the
approved task.

## Common pitfalls

- Mounting or scanning the original mutates metadata; always work on a
  copy.
- Tool versions change output formats; record versions with results.
- Evidence contains personal and sensitive data; exposure is a
  reportable incident.
- Malicious files may be booby-trapped; open untrusted documents in
  isolated tooling only.

## Interpretation guidance

Timestamps depend on timezone, filesystem, and clock accuracy. Deleted
content lingers until overwritten, but its presence is not proof of
user intent or action.

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
original hash, working-copy hash, tool versions, full command log, and derived artifact custody. Redact credentials, tokens, cookies, personal data, and
sensitive artifacts. A command error is evidence of a limitation, not a reason
to guess flags or retry aggressively.

## Scope and approval checklist

- Supplied evidence set and working directory are defined.
- Approved tool set and analysis methods are agreed.
- Output and derivative handling rules are known.
- No modification of original evidence, ever.

## Local sources

- [Skill workflow](../SKILL.md)
- Installed package metadata and manual pages are the authority for this
  starter's version-specific behavior.
