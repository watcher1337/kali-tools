---
name: kali-http-enum
description: Use when an authorized assessment needs read-only HTTP(S) response, header, TLS, or documented-endpoint inspection.
---

# HTTP enumeration

Keep requests read-only and rate-limited. Confirm the canonical URL, allowed virtual hosts, and whether authenticated testing is permitted.

## Safe workflow

1. Fetch response headers and redirects.
2. Inspect supported methods with `OPTIONS` only when approved.
3. Review `robots.txt`, `security.txt`, TLS certificate details, and published API documentation.
4. Compare security headers across representative public pages.

```bash
curl --silent --show-error --head --location 'https://<authorized-host>/'
curl --silent --show-error --request OPTIONS --include 'https://<authorized-host>/'
```

Do not probe undocumented administrative paths, submit forms, alter headers to impersonate users, or treat banner versions as proof of a vulnerability.
