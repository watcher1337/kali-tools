---
name: kali-ffuf
description: Use when an authorized assessment requires rate-limited web content or parameter discovery with ffuf.
---

# ffuf

Confirm the approved base URL, wordlist, HTTP method, and request rate. Never fuzz third-party services, login endpoints, or state-changing routes without explicit authorization.

1. Request a known missing path to establish the normal not-found response.
2. Use a small wordlist and low request rate.
3. Filter baseline status, size, or word count; manually inspect results.

```bash
ffuf -w <approved-wordlist> -u 'https://<authorized-host>/FUZZ' \
  -rate 10 -mc 200,204,301,302,307,401,403 -of json \
  -o results/ffuf-content.json
```

Use `-ac` only after checking its suggested filters. Do not send credentials, sensitive payloads, large wordlists, or mutation-heavy requests unless approved.
