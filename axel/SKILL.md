---
name: kali-axel
description: Use when an authorized security assessment requires the Kali Linux `axel` package. Confirm the package's installed commands and use its own documentation before executing it.
---

# Axel

`axel` is in the pinned Kali Linux default-package manifest for this release of the catalog. Package names and executable names can differ, so do not invent commands or flags.

## Safe workflow

1. Confirm explicit authorization, the exact in-scope target or artifact, and operational limits.
2. Confirm the package is installed and identify its supplied files:

```bash
dpkg -L axel
```

3. Read the installed command's `--help` and manual page before choosing options.
4. Start with the least intrusive, read-only operation that answers the approved question; save sanitized evidence outside version control.
5. Stop for errors, rate limiting, unexpected state changes, out-of-scope results, or any operation that could change data, credentials, availability, or access.

Do not use this starter skill as proof that a command is safe for a production target. Replace it with a tool-specific workflow when repeated use needs validated flags, prerequisites, and failure handling.
