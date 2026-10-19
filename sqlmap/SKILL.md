---
name: kali-sqlmap
description: Use when an explicitly authorized assessment needs least-invasive SQL injection verification for a specific suspected parameter.
---

# SQLMap

Use only after a specific authorized parameter is suspected and a safe test environment or written production approval exists. Confirm testing will not affect data integrity or availability.

1. Save a sanitized request that targets one approved parameter.
2. Begin with low risk and level, one thread, and no data extraction.
3. Treat output as a lead; manually confirm a minimal harmless indicator.

```bash
sqlmap -r sanitized-request.txt -p '<approved-parameter>' \
  --batch --level=1 --risk=1 --threads=1 --output-dir=results/sqlmap
```

Do not dump data, execute OS commands, read or write files, obtain shell access, escalate privileges, use tamper scripts, or evade defenses. Stop for errors, latency, or unexpected state changes.
