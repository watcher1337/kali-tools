<!-- curated: manual reference for the netexec skill; extendable, do not regenerate -->
# netexec: operational reference

## What it is

NetExec (invoked as `nxc`, Kali package `netexec`) validates one supplied
credential against one approved host under a specific protocol (SMB among
others). In this catalog it is the single-attempt credential-validation
instrument for the smb-active-directory category. A success is one
accepted authentication, not administrative access and not authorization
for enumeration, execution, or lateral movement. The canonical bounded
workflow is [SKILL.md](../SKILL.md).

Command patterns below come from the captured help of the assessed version
and are proposed invocations, never evidence they ran.

## Install and verify

- Kali/Debian package: `netexec`. Executable: `nxc` (package and executable
  names differ here — a common Debian pattern).
- Inspect: `apt-cache policy netexec`; verify installed: `dpkg -s netexec`.
- Install only with change approval: `sudo apt install netexec`.
- Verify: `nxc --version` and `nxc <protocol> --help` for the exact
  protocol in scope.

## Quick start

```bash
# One approved host, one supplied credential, minimal concurrency
nxc smb <authorized-host> -u '<approved-user>' -p '<approved-password>' \
  -t 1 --timeout <approved-seconds>
```

Do not add modules or post-authentication options without a separate
approval. This is a proposed command, not evidence it ran.

## How to use

1. Confirm protocol, exact host, account, lockout threshold, thread limit,
   test window, and stop contact.
2. Keep the password out of shell history: environment variable or prompt
   where the tool supports it; never in scripts or logs.
3. Run exactly one attempt at `-t 1`; record the single result.
4. Stop. Any follow-up (enumeration, command execution, a second account)
   needs a new, specific approval.

## Key options (from captured help)

| Option | Role |
| --- | --- |
| `smb <host>` | Protocol subcommand with the single approved target. |
| `-u` / `-p` | Supplied credential; keep both out of history and logs. |
| `-t 1` | Minimal concurrency; lockout safety depends on it. |
| `--timeout <s>` | Bound per-connection waiting. |

## When to use

- One designated test account against one approved host/protocol.
- Confirming a supplied credential works under a known lockout policy.
- Establishing authentication status before a separately approved
  follow-up.

## When not to use

- Password spraying, hash use, relays, or any multi-account attempt.
- Broad host enumeration, module execution, dumping, or lateral movement.
- Accounts or hosts outside the written scope, no matter how tempting the
  DNS results are.

## Common issues and troubleshooting

| Symptom | Likely cause | Bounded response |
| --- | --- | --- |
| Timeout/no answer | Filtering, DNS, or host down | Capture the error; verify scope. Do not retry repeatedly. |
| `STATUS_LOGON_FAILURE` | Wrong credential or locked account | One result; stop. Retries risk lockout. |
| `STATUS_ACCOUNT_LOCKED_OUT` | Threshold reached | Immediate stop; contact the operator. |
| Access denied after success | Account lacks rights | Success stands as authentication only; rights need new approval to test. |

## Suggestions and decisions

- Failure can be network, DNS, protocol, clock, policy, or credential
  issue; ambiguity is a reason to stop, not retry.
- If success requires follow-up, request the smallest next read-only action
  as its own approval.
- Keep passwords out of evidence; record that a supplied credential was
  used, not what it was.

## Failure handling and evidence

Record host/protocol, `nxc --version`, timestamp, sanitized command, the
single result, and the lockout constraints in effect. Never retain or print
passwords, hashes, tickets, tokens, or raw credential-bearing logs in
shared evidence. A lockout or unexpected service behavior is an incident
signal: preserve evidence and contact the operator.

## Local sources

- Installed `nxc --help` and `nxc <protocol> --help` are the version
  authority.
- The canonical workflow lives in [SKILL.md](../SKILL.md).
