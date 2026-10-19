<!-- generated: scripts/generate-tool-skills.py; package=dirbuster -->
# dirbuster: package reference

## What it is

`dirbuster` is the Debian/Kali package mapped to the `dirbuster` skill. A
package can provide several executables, services, libraries, or data files;
the package name is **not** assumed to be an executable. In this catalog the
package sits in the **web-discovery** category, where tools typically answer
which approved paths, virtual hosts, or routes exist on the target and
which of those responses deserve manual inspection. This reference makes no unverified claim about this
package's flags, output, or security impact; it teaches how to approach the
category safely while you discover the installed commands.

## Install and verify

In an approved Kali environment, inspect availability before installing:

```bash
dpkg -s dirbuster
apt-cache policy dirbuster
```

If the operator approves installing it, use the local package-manager policy,
for example `sudo apt install dirbuster`, then record the installed version.
Installation changes the environment; it is not an assessment action and may
need a separate change approval.

## How to use

Follow the category workflow with the installed command's own help as the
syntax authority:

1. Request one known-missing path and record its status, size, and
   behavior; this baseline exposes soft-404 pages.
2. Start with the smallest approved wordlist at the approved rate.
3. Filter results against the documented baseline; review automatic
   filter suggestions instead of accepting them blindly.
4. Manually re-request a minimal sample of candidates with a read-only
   request before recording anything as a candidate.

Always substitute only operator-supplied approved values, and confirm local
help matches the installed version before running anything.

## When to use

Use when the approved objective needs wordlist-driven content, route, or virtual-host discovery against an approved base URL and no more focused curated
skill in this catalog already answers the question.

## When not to use

Do not use when scope, authorization, rate limits, credentials, or the effect
of the selected executable is unknown. Do not treat an installed package as
permission to scan, authenticate, alter data, or access evidence. Do not use
it to substitute a curated skill whose bounded workflow already fits the
approved task.

## Common pitfalls

- Soft-404 and wildcard hosts answer 200 for everything; without a
  baseline every path looks like a finding.
- Redirect chains can leave the approved scope; follow nothing
  off-host without approval.
- TLS/SNI mismatches and certificate errors change responses per host
  header; record which host header was used.
- Each word multiplies request volume; rate limits and WAFs engage
  quickly and are a stop signal, not a challenge.

## Interpretation guidance

Status, length, and redirect differences are triage signals only. A
401 or 403 shows a route exists, not that access is possible or
permitted. Discovery output is a candidate list, never a finding list.

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
baseline response, wordlist identity and size, filters applied, rate/concurrency, raw output, and the manually verified sample. Redact credentials, tokens, cookies, personal data, and
sensitive artifacts. A command error is evidence of a limitation, not a reason
to guess flags or retry aggressively.

## Scope and approval checklist

- Base URL, allowed methods, and excluded paths are written.
- Wordlist size and request ceiling are approved.
- Virtual-host names, if tested, come from an approved list.
- No credentialed or state-changing requests inside discovery.

## Local sources

- [Skill workflow](../SKILL.md)
- Installed package metadata and manual pages are the authority for this
  starter's version-specific behavior.
