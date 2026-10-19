---
name: sakis3g
description: Use when an authorized assessment requires the Kali Linux `sakis3g` package. Confirm the installed commands and read their own help before executing anything.
license: GPL-3.0-only
metadata:
  category: systems-utilities
  type: tool
  status: starter
  source: generated
  package: [sakis3g]
  capabilities: [shell]
  activation:
    - An authorized engagement is active and its scope is confirmed
    - The approved objective specifically requires the sakis3g package
  prerequisites:
    - Explicit authorization covering targets, techniques, and rate limits
    - Package installed in an approved environment
  related: []
  verification: none
---

# Sakis3G

`sakis3g` is in the pinned Kali Linux default-package manifest for this release of the catalog. Package names and executable names can differ, so this starter deliberately contains no flags.

## Identity

- Package: `sakis3g` (Debian/Kali). Discover executables with `dpkg -L sakis3g`.
- Catalog role: general system and network utility tasks (transfer, capture, archive, service helper) on approved endpoints.
- Purpose: consult the installed command's own documentation; this starter carries no tool-specific behavior.
- Limitations: no verified examples, output formats, or flag guidance.
- Read the self-contained [package reference](references/package-reference.md)
  before choosing an executable or installation action.

## Activation

- An authorized engagement is active and its scope is confirmed.
- The approved objective specifically requires `sakis3g`, and no curated skill in this catalog covers the task better.

## Do not use when

- Authorization, ownership, or scope for the target is unconfirmed.
- A skill with `status: curated` in `manifest.yaml` already covers the task.
- The operation would change data, credentials, availability, or access without explicit approval.

## Prerequisites

- Explicit authorization: targets, allowed techniques, rate limits, test window, stop contact.
- Package installed in an approved environment: `dpkg -s sakis3g`.
- An engagement evidence directory outside version control.

## Execution patterns

No verified examples in this starter. Before running anything:

1. Identify the executables: `dpkg -L sakis3g`.
2. Read the installed help for the exact version: `<command> --help`, `<command> -h`, or `man <command>`.
3. Record the version where the command supports it.
4. Start with the least intrusive, read-only invocation that answers the approved question.
5. Follow the category workflow in the [package reference](references/package-reference.md).

## Interpretation

- This starter establishes nothing about output formats or result meaning.
- Treat raw output as observations, not findings; validate significant results independently before reporting them.
- Read the category interpretation guidance in the [package reference](references/package-reference.md) before drawing conclusions.

## Decision rules

- Executable not found: report the limitation and the smallest next step (approved install or execution backend). Do not improvise flags.
- Command exits with an error: capture the exact error, correct arguments only from real help output, stop after one retry.
- Result answers the approved question: record evidence and stop.
- Result inconclusive or ambiguous: switch to a curated skill or ask the operator.

## Evidence

- Save the exact command, tool version, timestamp, target, and full output in the engagement evidence directory.
- Expected artifacts for this category: tool version, exact command, endpoints or paths involved, and full output including errors.
- Redact credentials, cookies, tokens, and personal data from any copy that leaves that directory.

## Related tools

- Category routing is provided by the `kali-tools` master skill when it is installed.
- This skill remains usable on its own: inspect local help before selecting an alternative.

## Safety

- Read-only operations only unless the engagement explicitly approves state changes.
- Respect rate and concurrency limits; stop on instability or scope drift.
- Having the tool installed is not authorization to use it.
