# Kiro CLI Adapter — Well-Architected Agent

A dedicated Kiro CLI custom agent that scopes a session to Well-Architected work. It complements the Kiro steering and skills (which the installer also copies) by packaging them into a switchable agent with a review-first tool policy.

## What it provides

- `agents/well-architected.json` — a custom agent config installed to `.kiro/agents/` (project) or `~/.kiro/agents/` (global).

## Design

The agent follows the repository design principles (see `AGENTS.md`):

- Review and guidance, not code mutation. Only `fs_read` is pre-approved; every write or command execution requires explicit user approval.
- Data-driven. The prompt requires each finding to cite the specific resource, file, or configuration that supports it.
- Aligned, not compliant. The prompt forbids "compliant" as a customer outcome.
- Local-only. No MCP servers and no API calls are configured; the agent works entirely from the local steering, skills, and workspace files.

Resources are declared for both project-level (`.kiro/...`) and global (`~/.kiro/...`) install locations; whichever exists is loaded.

## Install

Handled by the root installers:

```bash
./install.sh ~/my-project --tool kiro
```

```powershell
.\install.ps1 -TargetDir C:\Projects\my-app -Tool kiro
```

Or manually:

```bash
mkdir -p .kiro/agents
cp adapters/kiro-cli/agents/well-architected.json .kiro/agents/
```

## Use

```bash
kiro-cli chat --agent well-architected
```

Or switch inside a session with `/agent swap`. Validate after edits with:

```bash
kiro-cli agent validate --path .kiro/agents/well-architected.json
```
