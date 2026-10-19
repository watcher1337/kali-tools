---
name: kali-nuclei
description: Use when an authorized assessment requires selected, non-destructive Nuclei checks and manual validation.
---

# Nuclei

Use only reviewed templates appropriate to the agreed scope. Template execution can issue many requests; confirm rate limits and exclude templates that cause callbacks, authentication attempts, data changes, or denial-of-service behavior.

## Safe workflow

1. Check the installed options with `nuclei --help`.
2. Select tags or template paths that have been reviewed for passive or low-impact behavior.
3. Set a conservative request rate and save JSONL evidence.
4. Manually reproduce a minimal, non-destructive indicator before reporting it.

```bash
nuclei -u 'https://<authorized-host>' -tags exposure,misconfig \
  -rate-limit 5 -jsonl -o results/nuclei.jsonl
```

Do not run all templates by default, auto-update templates without approval, use out-of-band interaction templates, or assume a match is a confirmed vulnerability.
