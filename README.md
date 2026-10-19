# kali-tools

`kali-tools` is a portable Agent Skills catalog for Kali Linux's default desktop toolset. It helps an AI coding agent choose an appropriate tool, check scope and safety first, and then load a tool-specific `SKILL.md`.

> **Use only with explicit permission.** These skills are for authorized security assessments, training labs, CTFs, and systems you own. They do not authorize scanning, credential attacks, data access, persistence, or disruptive testing.

## What you get

- **1 main skill** — `kali-tools/SKILL.md` handles scope, safety, and tool selection.
- **241 default-package skills** — one folder per package in Kali's `kali-linux-default` toolset.
- **Curated guides** — practical, conservative workflows for Nmap, ffuf, NetExec, Gobuster, SQLMap, Burp Suite, HTTP enumeration, and Nuclei.
- **No bundled Kali software** — install tools separately on a Kali system or another approved environment.

```text
kali-tools/
├── SKILL.md                 # Start here
├── nmap/SKILL.md
├── ffuf/SKILL.md
├── sqlmap/SKILL.md
├── references/
└── scripts/
```

## Before you install

1. Install the relevant Kali package in an approved environment. For example: `sudo apt install nmap`.
2. Confirm your written or explicit authorization: targets, test window, allowed techniques, rate limit, and stop contact.
3. Read the target agent's security/trust prompt before enabling a skill from any repository.

## Install from GitHub

Replace `<owner>` with the GitHub organization or account that publishes this repository:

```bash
git clone https://github.com/<owner>/kali-tools.git
cd kali-tools
```

For a personal install, clone directly to your agent's skills directory using the command for that agent below. Restart the agent, or reload its skills when its documentation says to do so.

## Install for a specific agent

All examples below install the same folder. The shared `SKILL.md` files use the portable Agent Skills format, but discovery and commands vary by agent.

| Agent | Personal install | Project install | Use it |
| --- | --- | --- | --- |
| **Codex** | `git clone https://github.com/<owner>/kali-tools.git ~/.codex/skills/kali-tools` | Clone to `.agents/skills/kali-tools` | Ask for an authorized assessment; load `kali-tools` when tool selection is needed. |
| **Claude Code** | `git clone https://github.com/<owner>/kali-tools.git ~/.claude/skills/kali-tools` | Clone to `.claude/skills/kali-tools` | Start a new session and ask for the scoped task. |
| **Cursor** | Use the version-specific global skills location, or clone to `.cursor/skills/kali-tools` | `git clone https://github.com/<owner>/kali-tools.git .cursor/skills/kali-tools` | Ask for the scoped task after Cursor has indexed the project. |
| **OpenCode** | `git clone https://github.com/<owner>/kali-tools.git ~/.config/opencode/skills/kali-tools` | Clone to `.opencode/skills/kali-tools` or `.agents/skills/kali-tools` | Allow the skill when OpenCode asks for permission. |
| **Gemini CLI** | Use Gemini's supported skill installer or configured skills location | `git clone https://github.com/<owner>/kali-tools.git .agents/skills/kali-tools` | Start a new Gemini CLI session and describe the authorized task. |
| **Pi** | `git clone https://github.com/<owner>/kali-tools.git ~/.pi/agent/skills/kali-tools` | Clone to `.pi/skills/kali-tools` or `.agents/skills/kali-tools` | Run `/reload`, then use `/skill:kali-tools` or `/skill:kali-nmap`. |

### One repository, many agents

For a team repository, the most portable location is `.agents/skills/kali-tools`:

```bash
mkdir -p .agents/skills
git clone https://github.com/<owner>/kali-tools.git .agents/skills/kali-tools
```

Commit it only if your team intends to distribute the full skill catalog with the repository. Otherwise, add `.agents/skills/kali-tools` to `.gitignore` or install it personally.

## How to use it

Give the agent a complete, authorized scope. Good prompts include a target, permission, goal, constraints, and desired output.

```text
I have written authorization to assess https://staging.example.test today.
Only test this host, use read-only checks, keep requests below 5 per second,
and save a short findings summary without secrets. Use Kali tools if needed.
```

For Pi, you can explicitly load a skill:

```text
/skill:kali-tools select a safe tool for authorized web header inspection
/skill:kali-nmap enumerate ports 80 and 443 on the approved staging host
```

The agent should ask for missing authorization or scope details. It should stop when the operation risks changing data, availability, access, or scope.

## Publish this catalog

Before publishing, replace `<owner>` in this README with your GitHub account or organization and choose an open-source license.

```bash
cd kali-tools
git init
git add .
git commit -m "feat: publish Kali tools skill catalog"
gh repo create kali-tools --public --source=. --push
```

Then:

1. Add a `LICENSE` file and state the chosen license in the repository settings and release notes.
2. Create a GitHub release and tag it, for example `v0.1.0`.
3. Tell users to clone a tag for repeatable installs: `git clone --branch v0.1.0 --depth 1 <repository-url> <skill-directory>`.
4. Test at least one personal and one project install before announcing support for an agent.
5. Never publish real targets, VPN hosts, credentials, cookies, request captures, customer data, or assessment reports.

## Scope and updates

The catalog is pinned to the `kali-linux-default` dependency definition in Kali's `kali-meta` source. It does **not** claim to cover every package in `kali-linux-everything`. Kali changes its package set over time.

To regenerate starter skills after reviewing a new Kali package manifest:

```bash
python3 scripts/generate-tool-skills.py
```

Read [release-sync](references/release-sync.md) before updating the manifest. The generator does not overwrite a hand-curated skill unless `--overwrite` is supplied.

## Sources

- [Kali Linux metapackages](https://www.kali.org/docs/general-use/metapackages/)
- [Kali `kali-meta` source](https://gitlab.com/kalilinux/packages/kali-meta/-/blob/kali/master/debian/control)
- [Kali all tools](https://www.kali.org/tools/all-tools/)
