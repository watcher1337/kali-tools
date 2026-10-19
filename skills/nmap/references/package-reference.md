<!-- curated: manual reference for the nmap skill; extendable, do not regenerate -->
# nmap: operational reference

## What it is

Nmap ("Network Mapper") sends crafted IP packets to answer three questions
about explicitly allowed targets: which hosts are available, what services
they offer, and how traffic to them is filtered. In this catalog it is the
conservative service-inventory baseline for the network-reconnaissance
category. The canonical bounded workflow is [SKILL.md](../SKILL.md); this
reference adds installation detail, technique selection, and interpretation
depth that stays present when `nmap` is installed alone.

Everything below is sourced from the official Nmap Reference Guide
(nmap.org/book/man.html) and the captured help of the assessed version.
Command patterns are proposed invocations, never evidence they ran.

## Install and verify

- Kali/Debian package: `nmap`. Executable: `nmap`.
- Inspect before installing: `apt-cache policy nmap`; verify installed:
  `dpkg -s nmap`.
- Install only with environment/change approval: `sudo apt install nmap`.
- Verify the version and that options match this reference:
  `nmap -V` and `nmap --help`.
- Nmap distinguishes privileged and unprivileged modes: raw-socket scans
  (SYN, OS detection, UDP) need root or `CAP_NET_RAW`; unprivileged runs
  fall back to connect() scans and lose some techniques. Record which mode
  the engagement used.

## Quick start

Bounded patterns for one approved host and explicit ports (proposed, not
executed):

```bash
# Baseline sanity list: what would be scanned, no packets to targets
nmap -sL <authorized-host>

# Service inventory on approved ports, all three output formats
nmap -sV -T3 -p 22,80,443 -oA results/nmap-services <authorized-host>
```

`-sV` probes open ports for service/version information; `-p` constrains
ports; `-oA` writes normal, XML, and grepable output. `-T3` is a timing
template, not a substitute for an agreed rate limit.

## How to use

1. Confirm the allowlisted targets and ports; expand nothing from DNS
   results.
2. List-scan (`-sL`) the target set: it sends no packets and catches wrong
   or surprising addresses before any traffic exists.
3. Establish the discovery baseline with the smallest approved probe set.
4. Run the port scan at the approved timing; add `-sV` only when the
   objective needs service identity.
5. Interpret states, record evidence, and stop at the approved coverage.

## Host discovery techniques

From the official Host Discovery reference. The `-P*` options combine;
specifying any of them replaces the default probe set.

| Option | Probe | Notes |
| --- | --- | --- |
| `-sL` | none (list scan) | No packets to targets; reverse-DNS names only. Sanity check. |
| `-sn` | default probes, no port scan | Host discovery only ("ping scan"); on local LAN uses ARP by default. |
| `-Pn` | none (skip discovery) | Port-scans every listed address as if alive; multiplies traffic. Needs explicit approval. |
| `-PS<ports>` | TCP SYN | Default port 80; RST or SYN/ACK both prove liveness. Needs raw sockets (root). |
| `-PA<ports>` | TCP ACK | Cuts through stateless SYN-filtering rules; stateful firewalls may drop it. |
| `-PU<ports>` | UDP | Bypasses TCP-only filters; open UDP ports usually stay silent, hence the uncommon default probe port. |
| `-PY<ports>` | SCTP INIT | SCTP-aware hosts answer; not available to unprivileged users. |
| `-PE` | ICMP echo request | The classic ping; widely blocked, unreliable over the Internet. |
| `-PP` / `-PM` | ICMP timestamp / address mask | Work when echo is blocked but other ICMP queries are not. |
| `-PO<protos>` | IP protocol ping | Looks for same-protocol replies or ICMP protocol-unreachable. |

Default discovery when no `-P*` option is given: ICMP echo, TCP SYN to 443,
TCP ACK to 80, ICMP timestamp (`-PE -PS443 -PA80 -PP`). On local Ethernet,
ARP/Neighbor Discovery replaces these unless `--disable-arp-ping` is set.
`--discovery-ignore-rst` exists for networks whose firewalls spoof RSTs at
unoccupied addresses.

## Port states

| State | Meaning |
| --- | --- |
| `open` | An application on the target is listening on that port. |
| `closed` | No application is listening; the port is reachable and responsive. |
| `filtered` | A firewall or obstacle blocks the port; Nmap cannot tell open from closed. |
| `unfiltered` | The port responds, but Nmap cannot determine open vs. closed (ACK scan). |
| `open\|filtered` / `closed\|filtered` | Nmap cannot distinguish the two states (common in UDP and IP-protocol scans). |

`open` is a strong observation. `closed` proves reachability, not safety.
`filtered` is the common external view and proves nothing about the host.

## Output handling

- `-oA <basename>` writes `<basename>.nmap` (normal), `.xml`, and `.gnmap`
  (grepable) in one run; keep all three.
- XML output feeds report tooling; grepable output feeds quick filtering.
- Always archive the exact command line with the outputs: the files are
  meaningless without probe context.

## When to use

- Host, port, or service inventory for explicitly allowed targets.
- Establishing whether an approved host exposes an expected service.
- Producing a documented baseline for later, narrower follow-up checks.

## When not to use

- Unapproved Internet-wide or partner ranges; scope never expands from DNS
  or routing results.
- When passive evidence (pcap, logs, CMDB) already answers the question.
- Intrusive NSE script sets, OS detection, UDP sweeps, evasion, or spoofing
  without separate written approval (see SKILL.md "Do not use when").
- When a faster scanner's behavior has not been explicitly approved; prefer
  this baseline first.

## Common issues and troubleshooting

| Symptom | Likely cause | Bounded response |
| --- | --- | --- |
| Every port `filtered` | Egress filtering or wrong network path | Verify scope and routing; one `-PS` probe tells you if anything passes. |
| `Host seems down` on a known-live host | Discovery probes blocked | Re-run discovery with a different approved `-P*` probe, not `-Pn`, first. |
| Service versions look wrong/generic | Masked banners or version guessing limits | Record as candidate identity; verify with a manual read-only request. |
| Scan far slower than expected | Timing template, retransmits, UDP cost | Stay at approved timing; shrink port set instead of raising speed. |
| Unprivileged run fails on scan types | Missing raw-socket rights | Record the limitation; request the smallest privilege change, do not improvise. |

## Suggestions and decisions

- Prefer `-sL`, then the smallest probe set, then ports, then `-sV`: each
  layer adds traffic and each must earn its place in the objective.
- A responsive approved host exposing a relevant service routes to the
  smallest matching tool skill for read-only follow-up.
- If the inventory answers the objective, stop rather than broadening ports
  or scripts.
- `-Pn` on a /16 means a /16 port scan; it is a scope decision, not a flag.

## Failure handling and evidence

Preserve the `.nmap`, `.xml`, and `.gnmap` outputs, the target
scope, timestamp, `nmap -V` output, sanitized command, and errors. Record
host-discovery assumptions (probe types, `-Pn` if approved) so `filtered`
and timeout rows can be interpreted later. Redact confidential hostnames
and banners from distributed reports. A run that ends early is evidence of
a limit; capture why rather than re-running wider.

## Local sources

- [Nmap Reference Guide](https://nmap.org/book/man.html) (official)
- [Nmap Book: Network Discovery](https://nmap.org/book/man-host-discovery.html)
- Local `man nmap` and `nmap --help` are the authority for the installed
  version.
