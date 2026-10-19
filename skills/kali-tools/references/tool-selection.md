# Tool selection

Choose the smallest tool skill that answers the approved objective.

| Objective | Prefer | Guardrail |
| --- | --- | --- |
| Host/service inventory | `nmap` | Explicit hosts and ports; conservative timing. |
| Web content discovery | `ffuf` or `gobuster` | Approved base URL, wordlist, and low request rate. |
| Enterprise-service credential validation | `netexec` | A supplied test credential, one host first, lockout limits. |
| Template-based checks | `nuclei` | Reviewed non-destructive templates and manual validation. |

Use the individual skill's activation/exclusion rules. Do not use a tool merely because it is installed.
