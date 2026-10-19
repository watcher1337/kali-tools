<!-- generated: scripts/generate-tool-skills.py; package=bully -->
# bully: package reference

## What it is

`bully` is the Debian/Kali package mapped to the `bully` skill. A
package can provide several executables, services, libraries, or data files;
the package name is **not** assumed to be an executable. In this catalog the
package sits in the **wireless** category, where tools typically answer
which authorized access points, channels, and security settings are
present in the approved radio scope. This reference makes no unverified claim about this
package's flags, output, or security impact; it teaches how to approach the
category safely while you discover the installed commands.

## Install and verify

In an approved Kali environment, inspect availability before installing:

```bash
dpkg -s bully
apt-cache policy bully
```

If the operator approves installing it, use the local package-manager policy,
for example `sudo apt install bully`, then record the installed version.
Installation changes the environment; it is not an assessment action and may
need a separate change approval.

## How to use

Follow the category workflow with the installed command's own help as the
syntax authority:

1. Confirm regulatory domain, channels, and duration in writing.
2. Monitor on the approved channel(s) only; monitor mode, no
   transmission.
3. Capture a bounded window, then analyze offline.
4. Correlate findings with the approved AP list by BSSID.

Always substitute only operator-supplied approved values, and confirm local
help matches the installed version before running anything.

## When to use

Use when the approved objective needs authorized 802.11 observation and assessment with compatible hardware and no more focused curated
skill in this catalog already answers the question.

## When not to use

Do not use when scope, authorization, rate limits, credentials, or the effect
of the selected executable is unknown. Do not treat an installed package as
permission to scan, authenticate, alter data, or access evidence. Do not use
it to substitute a curated skill whose bounded workflow already fits the
approved task.

## Common pitfalls

- Transmission rules are legal, not technical: injection, deauth, and
  jamming are disruptive and need explicit written approval.
- Channel hopping drops frames; fix the channel per capture window.
- Captures contain third-party device identifiers and traffic; handle
  as personal data.
- Signal strength varies with position and environment; single-sample
  geolocation is unreliable.

## Interpretation guidance

Beacon security fields are the AP's claims, not verified configuration.
A captured handshake is an artifact, not a cracked credential. Absence
of frames is not absence of an AP.

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
authorized AP/BSSID list, channel, capture file, duration, and tool versions. Redact credentials, tokens, cookies, personal data, and
sensitive artifacts. A command error is evidence of a limitation, not a reason
to guess flags or retry aggressively.

## Scope and approval checklist

- Regulatory domain and channels are confirmed.
- Duration and physical location of the test are approved.
- No transmission, injection, or deauthentication without separate approval.
- Capture files are stored and disposed per data rules.

## Local sources

- [Skill workflow](../SKILL.md)
- Installed package metadata and manual pages are the authority for this
  starter's version-specific behavior.
