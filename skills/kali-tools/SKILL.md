---
name: kali-tools
description: Route authorized Kali Linux security-assessment tasks to the smallest suitable tool skill, with scope, safety, evidence, and stop gates.
license: GPL-3.0-only
metadata:
  category: master
  type: master
  status: curated
  source: manual
  capabilities: [shell, network, evidence-handling]
  activation:
    - An authorized security-testing task needs tool selection or an engagement safety gate
  prerequisites:
    - Explicit authorization and defined target scope
  related: [nmap, ffuf, netexec, nuclei]
  verification: official-docs
---

# Kali Tools router

Use this routing skill for legitimate assessments, CTFs, training labs, and systems the operator owns. It selects a focused tool skill; it is not permission to execute a tool and does not automatically load sibling skills in every host.

## Mandatory safety gate

Before any network, authentication, wireless, exploitation, or evidence-handling action, obtain and record: target allowlist, test window, allowed techniques, rate/concurrency limit, credentials/lockout constraints, exclusions, data-handling rules, and stop contact. Tool availability, a discovered service, successful authentication, a scanner match, and a command example are **not** authorization, proof of access, a confirmed vulnerability, or evidence that a command ran.

## Workflow

1. Restate the objective and existing evidence. If authorization or a material limit is missing, ask; do not probe to fill the gap.
2. Select the least intrusive category using [tool selection](references/tool-selection.md), then load only the named `skills/<id>/SKILL.md` through the host's documented skill mechanism. Do not assume loading this router loads sibling skills.
3. Check the executable/package and exact version (`command -v`, package manager, then `--help`) before relying on a command. Check any MCP server separately; none is required by this catalog.
4. Begin with the smallest approved target set and read-only operation. Apply the approved rate/concurrency ceiling, capture sanitized command/version/output in the engagement evidence directory, and interpret output with the selected skill.
5. Validate only the minimum harmless indicator necessary. Escalate to authentication, state change, exploitation, callbacks, remote execution, or broad enumeration only with explicit approval.
6. Stop when the objective is answered, a prerequisite is absent, scope drifts, instability occurs, or further testing would not materially improve the conclusion. Report observations, uncertainty, and justified next steps.

Load these bundled references only when needed: [scope and safety](references/scope-and-safety.md), [evidence management](references/evidence-management.md), and [tool selection](references/tool-selection.md). Pack-level workflow guides are under `workflows/` in a full collection install; they are not required by this independently installed router.

## Common rationalizations and rebuttals

| Rationalization | Rebuttal |
| --- | --- |
| “The host answered, so it is in scope.” | Scope comes from the engagement allowlist, not DNS or scan results. |
| “This is only a harmless scan.” | Traffic volume, authentication, callbacks, and scripts can still affect systems. Confirm the allowed technique and limits. |
| “The scanner found it.” | A match is an indicator. Preserve it and validate the smallest non-destructive indicator before reporting a finding. |

## Red flags

Stop and ask the operator if a command would use credentials broadly, change remote state, increase target coverage, trigger out-of-band callbacks, collect sensitive content, or exceed an agreed rate.

## Verification and exit criteria

A routed action is complete only when evidence identifies the approved target, tool/version, sanitized invocation, timestamp, output or error, interpretation, and the reason to stop or escalate.
