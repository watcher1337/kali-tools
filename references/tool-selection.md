# Tool selection

Choose tools from the approved objective, not from a desire to enumerate broadly.

| Objective | Start with | Guardrail |
| --- | --- | --- |
| Asset and service inventory | `nmap`, `arp-scan`, `dnsrecon` | Restrict hosts and ports; use conservative rates. |
| Web response review | `curl`, `whatweb`, `nikto` | Prefer read-only requests and one approved base URL. |
| Web content discovery | `ffuf`, `gobuster`, `dirb` | Use a small approved wordlist and a low request rate. |
| Wireless assessment | `aircrack-ng`, `kismet` | Require explicit radio/network authorization. |
| Password-audit evidence | `john`, `hashcat` | Use only organization-provided test hashes; never obtain credentials. |
| Network capture analysis | `tcpdump`, `wireshark` | Capture only approved traffic; protect personal or confidential data. |
| Database injection validation | `sqlmap` | Require a suspected parameter and approved safe environment. |
| Evidence and file analysis | `binwalk`, `bulk-extractor`, `sleuthkit` | Preserve evidence integrity and follow retention requirements. |

A scanner result is not a confirmed finding. Validate the minimal harmless indicator and record tool version, sanitized command, target, time, and result.
