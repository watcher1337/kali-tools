<!-- generated: scripts/generate-tool-skills.py; package=ike-scan -->
# ike-scan: package reference

## What it is

`ike-scan` is the Debian/Kali package mapped to the `ike-scan` skill. A
package can provide several executables, services, libraries, or data files;
the package name is **not** assumed to be an executable. In this catalog the
package sits in the **network-reconnaissance** category, where tools typically answer
which approved hosts respond, which ports or services they expose,
and how traffic between you and them is filtered. This reference makes no unverified claim about this
package's flags, output, or security impact; it teaches how to approach the
category safely while you discover the installed commands.

## Install and verify

In an approved Kali environment, inspect availability before installing:

```bash
dpkg -s ike-scan
apt-cache policy ike-scan
```

If the operator approves installing it, use the local package-manager policy,
for example `sudo apt install ike-scan`, then record the installed version.
Installation changes the environment; it is not an assessment action and may
need a separate change approval.

## How to use

Follow the category workflow with the installed command's own help as the
syntax authority:

1. Confirm the exact target list; expand nothing from DNS or routing results.
2. Read the local help and pick the smallest probe set that answers the
   approved inventory question.
3. Establish a baseline (a known-down address or a single known host) so
   timeouts can be distinguished from silence.
4. Run the smallest scan, record probe types and timing, then stop at the
   approved port/host coverage.

Always substitute only operator-supplied approved values, and confirm local
help matches the installed version before running anything.

## When to use

Use when the approved objective needs host, port, and service inventory for explicitly allowed targets and no more focused curated
skill in this catalog already answers the question.

## When not to use

Do not use when scope, authorization, rate limits, credentials, or the effect
of the selected executable is unknown. Do not treat an installed package as
permission to scan, authenticate, alter data, or access evidence. Do not use
it to substitute a curated skill whose bounded workflow already fits the
approved task.

## Common pitfalls

- A silent host is not an absent host: filtered probes look identical to
  dead hosts. Never infer absence from one probe type.
- Skipping host discovery multiplies traffic across every listed address;
  it needs explicit approval for that reason.
- Service/version probes and UDP coverage are slow and heavier than
  plain port probes; add them only when the objective requires it.
- Banners and version strings can be masked, generic, or stale.

## Interpretation guidance

Port states are observations under the probes you sent, not facts about
the host. A response timeout may be filtering, rate limiting, or loss. A
version string is a candidate identity, never a confirmed patch level.

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
target list, probe types, port coverage, timing/rate, raw output files, and the baseline. Redact credentials, tokens, cookies, personal data, and
sensitive artifacts. A command error is evidence of a limitation, not a reason
to guess flags or retry aggressively.

## Scope and approval checklist

- Target addresses or ranges are written and allowlisted.
- Port coverage and probe types are named in the approval.
- Packet rate or timing ceiling and test window are agreed.
- A stop contact exists before the first packet.

## Local sources

- [Skill workflow](../SKILL.md)
- Installed package metadata and manual pages are the authority for this
  starter's version-specific behavior.
