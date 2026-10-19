---
name: kali-burp-suite
description: Use when an authorized assessment requires Burp Suite for controlled HTTP inspection or manual validation in a non-production or explicitly approved environment.
---

# Burp Suite

Confirm the target, proxy configuration, test account, and whether passive scanning, active scanning, or request replay is allowed. Prefer staging and dedicated test data.

## Safe workflow

1. Configure the browser proxy and scope the target in Burp before browsing.
2. Use Proxy and HTTP history to inspect normal application behavior.
3. Use Repeater only for idempotent, low-impact requests unless state changes are approved.
4. Run passive checks first. Select individual active checks only after approval and at a controlled rate.
5. Remove session tokens, cookies, personal data, and secrets from exports.

Do not use Intruder for credential attacks, bypass session controls, modify production records, or activate automated scanning outside the approved scope.
