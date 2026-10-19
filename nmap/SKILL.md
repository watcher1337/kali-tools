---
name: kali-nmap
description: Use when an authorized security assessment requires scoped, low-impact Nmap host, port, or service enumeration.
---

# Nmap

Confirm the permitted hosts, ports, timing, and rate before scanning. Do not expand scope through discovered DNS records.

1. Check options with `nmap --help` and create an engagement-specific output directory.
2. Begin with a small specified port set and conservative timing.
3. Identify services only on responsive in-scope hosts.
4. Save normal and XML output. Report open ports and banners as observations, not vulnerabilities.

```bash
nmap -sV -T3 -p 22,80,443 -oA results/nmap-services <authorized-host>
```

Use `-Pn` only when the engagement permits testing hosts that block discovery. Avoid high-rate scans, broad Internet ranges, exploit scripts, and disruptive UDP scanning unless explicitly approved.
