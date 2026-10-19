# Release synchronization

## Pinned source

`references/default-tools.txt` is derived from the `kali-linux-default` package in Kali's `kali-meta` source. Its dependency graph includes `kali-linux-headless`, `kali-linux-core`, `kali-system-*`, and `kali-tools-top10` packages. The manifest records the leaf package names from that graph, selecting the first alternative where Kali declares a dependency alternative.

## Update procedure

1. Fetch and review the current `debian/control` from the Kali `kali-meta` repository.
2. Resolve only the dependency graph rooted at `kali-linux-default`; do not silently substitute `kali-linux-everything`.
3. Record the source URL, revision or release date, and extraction rules in the pull request or release notes.
4. Update `default-tools.txt`, run `python3 scripts/generate-tool-skills.py`, and inspect the diff.
5. Preserve hand-curated `SKILL.md` files unless their documented commands were verified against the new package version.

## Limits

A Debian package is not always a single executable, and some packages are system dependencies rather than security tools. The generated starter skill therefore directs the agent to `dpkg -L`, `--help`, and `man` before use. Do not publish made-up command names or unsafe default flags.
