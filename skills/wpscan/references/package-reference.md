<!-- generated: scripts/generate-tool-skills.py; package=wpscan -->
# wpscan: package reference

## What it is

`wpscan` is the Debian/Kali package mapped to the `wpscan` skill. A
package can provide several executables, services, libraries, or data files;
the package name is **not** assumed to be an executable. In this catalog the
package sits in the **web-application** category, where tools typically answer
whether one approved parameter or request exhibits a specific
suspected weakness under safe test settings. This reference makes no unverified claim about this
package's flags, output, or security impact; it teaches how to approach the
category safely while you discover the installed commands.

## Install and verify

In an approved Kali environment, inspect availability before installing:

```bash
dpkg -s wpscan
apt-cache policy wpscan
```

If the operator approves installing it, use the local package-manager policy,
for example `sudo apt install wpscan`, then record the installed version.
Installation changes the environment; it is not an assessment action and may
need a separate change approval.

## How to use

Follow the category workflow with the installed command's own help as the
syntax authority:

1. Capture or sanitize the exact request; work from a file, not from
   live browsing.
2. Name the single parameter or request under test.
3. Use the lowest risk/level/intensity the tool supports; one thread.
4. Validate the smallest harmless indicator manually, then stop.

Always substitute only operator-supplied approved values, and confirm local
help matches the installed version before running anything.

## When to use

Use when the approved objective needs least-invasive validation of one suspected application-layer weakness on an approved parameter or request and no more focused curated
skill in this catalog already answers the question.

## When not to use

Do not use when scope, authorization, rate limits, credentials, or the effect
of the selected executable is unknown. Do not treat an installed package as
permission to scan, authenticate, alter data, or access evidence. Do not use
it to substitute a curated skill whose bounded workflow already fits the
approved task.

## Common pitfalls

- Automated payloads can change server state or create records; safe
  settings still send attack traffic.
- Session tokens and CSRF values invalidate or rotate mid-test;
  replays can log you out or corrupt the session.
- WAF blocks and error spikes are stop signals, not obstacles to
  bypass.
- Responses may contain other users' data; treat every response as
  sensitive.

## Interpretation guidance

A tool detection is a lead. Neither a response difference nor tool
output alone proves data access, and impact claims need a separate,
explicitly approved demonstration.

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
sanitized request file, parameter, tool version, risk/level settings, output, and the validation note. Redact credentials, tokens, cookies, personal data, and
sensitive artifacts. A command error is evidence of a limitation, not a reason
to guess flags or retry aggressively.

## Scope and approval checklist

- Exact request, parameter, and methods are written down.
- Request volume and state-changing restrictions are agreed.
- Data-handling rules for captured responses are known.
- No extraction, dumping, or shell options without new approval.

## Local sources

- [Skill workflow](../SKILL.md)
- Installed package metadata and manual pages are the authority for this
  starter's version-specific behavior.
