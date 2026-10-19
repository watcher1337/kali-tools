---
name: kali-netexec
description: Use when an authorized assessment needs a single, explicitly supplied credential validated against an in-scope enterprise service with NetExec.
---

# NetExec

Use only organization-owned targets and assessment credentials. Confirm permitted protocols, lockout thresholds, and concurrency. Do not spray passwords, relay credentials, execute commands, dump secrets, or modify remote systems.

1. Start with one host and a designated test account.
2. Confirm installed syntax with `nxc <protocol> --help`.
3. Make one authentication validation request and capture only its result.

```bash
nxc smb <authorized-host> -u '<approved-user>' -p '<approved-password>'
```

Stop after success unless a specific follow-up is authorized. Redact usernames, passwords, hashes, and host identifiers from evidence.
