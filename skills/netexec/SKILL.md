---
name: netexec
description: Use when an authorized assessment needs a single supplied credential validated against an in-scope enterprise service with NetExec.
license: GPL-3.0-only
metadata:
  category: smb-active-directory
  type: tool
  status: curated
  source: manual
  package: [netexec]
  executable: [nxc]
  capabilities: [shell, network, credentials, evidence-handling]
  activation:
    - A supplied test credential and explicit service/host scope require one controlled authentication validation
  prerequisites:
    - Lockout policy, allowed protocol, concurrency, and credential-handling approval
  related: [smbmap, enum4linux, evil-winrm]
  verification: kali-help
---

# NetExec

## Identity

NetExec is invoked as `nxc` by the Kali package `netexec`. It supports multiple protocols. An authentication success is not administrative access and does not authorize enumeration, command execution, credential dumping, or lateral movement.

## Activation

Use only to validate one designated account against one approved host/protocol after the operator supplies a safe test credential and lockout constraints.

## Do not use when

Do not spray passwords, relay credentials, use hashes, enumerate broadly, execute commands, dump secrets, modify remote systems, or test accounts/hosts outside the written scope.

## Prerequisites

Confirm the protocol, exact host, account, lockout threshold, thread limit, test window, and stop contact. Verify with `nxc --version` and `nxc <protocol> --help`. Store secrets outside shell history, logs, and source control.

## Execution patterns

The captured help lists `smb` and global `-t`/`--timeout` options. For one approved SMB host and a supplied credential:

```bash
nxc smb <authorized-host> -u '<approved-user>' -p '<approved-password>' -t 1 --timeout <approved-seconds>
```

Do not add modules or post-authentication options without a separate approval. This example is a proposed command, not evidence it ran.

## Interpretation

A success indicates the service accepted the supplied authentication material under that protocol. It does not establish authorization level, data access, or that the account should be used further. Failures can result from network, DNS, protocol, clock, policy, or credential issues; do not retry repeatedly.

## Decision rules

Stop after one result. If lockout indicators, timeouts, unexpected service behavior, or ambiguity occurs, preserve the error and contact the operator. If success requires a follow-up, obtain a specific approval for the smallest next read-only action.

## Evidence

Record host/protocol, version, timestamp, sanitized command, one result, and lockout constraints. Never retain or print passwords, hashes, tickets, tokens, or raw credential-bearing logs in shared evidence.

## Related tools

Use `enum4linux` or `smbmap` only for separately approved enumeration. Use `evil-winrm` only with explicit authorization for an approved remote-management objective.

## Safety

Authentication attempts can trigger lockouts and alerts. Use one host, one account, one attempt, and `-t 1` unless the engagement explicitly says otherwise.

## Common rationalizations and rebuttals

| Rationalization | Rebuttal |
| --- | --- |
| “One more password is harmless.” | Repeated failures can lock accounts; the approved test is one supplied credential. |
| “Login worked, so enumerate everything.” | Authentication is not an authorization grant or an access-level conclusion. |

## Red flags

Multiple failures, account lockout messages, requests to use hashes/relays/modules, or a broader target list require an immediate stop.

## Verification and exit criteria

Finish when one approved authentication result is recorded with secrets redacted and no post-authentication action has occurred without approval.
