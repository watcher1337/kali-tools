---
name: kali-gobuster
description: Use when an authorized assessment requires rate-limited directory or DNS discovery with Gobuster.
---

# Gobuster

Confirm whether web content or DNS discovery is allowed, the exact host or domain, and a request limit. Start with a small approved wordlist.

For web content discovery, filter the normal missing-page response and keep threads low:

```bash
gobuster dir -u 'https://<authorized-host>/' -w <approved-wordlist> \
  -t 5 -s 200,204,301,302,307,401,403 -o results/gobuster-dir.txt
```

For DNS, query only the approved domain and do not pursue discovered names outside it. Do not use large wordlists, aggressive threading, extension spraying, or access found paths containing sensitive data without approval.
