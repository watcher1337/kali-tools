<!-- generated: scripts/generate-tool-skills.py; package=nikto -->
# nikto: package reference

## What it is

`nikto` is the Debian/Kali package mapped to the `nikto` skill. A
package can provide several executables, services, libraries, or data files;
the package name is **not** assumed to be an executable. In this catalog the
package sits in the **vulnerability-assessment** category, where tools typically answer
whether a specific, approved weakness shows its minimal safe indicator
on an approved target. This reference makes no unverified claim about this
package's flags, output, or security impact; it teaches how to approach the
category safely while you discover the installed commands.

## Install and verify

In an approved Kali environment, inspect availability before installing:

```bash
dpkg -s nikto
apt-cache policy nikto
```

If the operator approves installing it, use the local package-manager policy,
for example `sudo apt install nikto`, then record the installed version.
Installation changes the environment; it is not an assessment action and may
need a separate change approval.

## How to use

Follow the category workflow with the installed command's own help as the
syntax authority:

1. Select the exact checks or templates; read what each one sends before
   running it.
2. Exclude state-changing, brute-force, code-execution, and out-of-band
   behavior unless separately approved.
3. Run at the lowest rate against one target at a time.
4. Re-validate any match manually with the smallest harmless request
   before recording it.

Always substitute only operator-supplied approved values, and confirm local
help matches the installed version before running anything.

## When to use

Use when the approved objective needs bounded validation of specific weaknesses with reviewed, non-destructive checks and no more focused curated
skill in this catalog already answers the question.

## When not to use

Do not use when scope, authorization, rate limits, credentials, or the effect
of the selected executable is unknown. Do not treat an installed package as
permission to scan, authenticate, alter data, or access evidence. Do not use
it to substitute a curated skill whose bounded workflow already fits the
approved task.

## Common pitfalls

- Full default profiles are broad and frequently intrusive; run selected
  checks, not everything.
- Scanner updates change template behavior between runs; record the
  exact version or revision used.
- Out-of-band and callback checks send data to third parties; they need
  explicit approval.
- Matches go stale: server changes, feature flags, and middleware all
  produce false positives.

## Interpretation guidance

A match is a scanner alert, not a confirmed vulnerability; a non-match
is not proof of absence. Impact, exploitability, and business relevance
require separate manual validation.

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
target, tool and check/template versions, filters, rate, raw output, and the manual validation note. Redact credentials, tokens, cookies, personal data, and
sensitive artifacts. A command error is evidence of a limitation, not a reason
to guess flags or retry aggressively.

## Scope and approval checklist

- Target list and approved check set are written down.
- Callback/out-of-band policy is decided before the run.
- Request rate ceiling and stop conditions are agreed.
- Sensitive-response handling rules are known.

## Local sources

- [Skill workflow](../SKILL.md)
- Installed package metadata and manual pages are the authority for this
  starter's version-specific behavior.
