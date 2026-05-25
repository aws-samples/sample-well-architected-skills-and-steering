# Well-Architected Skills & Steering for AI Coding Agents

Reusable skills and steering that teach AI coding agents how to apply the AWS Well-Architected Framework. Works with Kiro, Claude Code, Cursor, Codex, Windsurf, GitHub Copilot, and Cline.

> ⚠️ **Important:** This sample is provided for educational and demonstrative purposes. It is not intended for production use without additional review and testing appropriate to your environment.

## What's inside

```text
steering/                           Steering (Kiro) — always-on context
  well-architected.md                 WA Framework pillars, design principles, review process

skills/                             Skills — standalone step-by-step playbooks (tool-agnostic)
  wa-review/                          Full Well-Architected review across all 6 pillars
  reliability-improvement-plan/       Identify SPOFs and produce a reliability remediation plan
  security-assessment/                Deep-dive security posture assessment
  cost-optimization-audit/            Find waste, right-sizing, pricing model improvements
  performance-efficiency/             Resource selection, scaling, caching, optimization
  sustainability-optimization/        Carbon footprint reduction via utilization and architecture
  migration-readiness/                7 Rs assessment with migration plan
  operational-excellence/              CI/CD, observability, incident mgmt, operational maturity
  architecture-decision-record/       WA-aligned ADRs with pillar impact analysis

assets/                             Shared reference material (WA best practices, metrics, patterns)
  v13/                                Well-Architected Framework v13 best practices by ID
  well-architected-best-practices.md  Per-pillar best practices with investigation checklists
  cloudwatch-metrics-reference.md     Metric thresholds by service + composite alarm patterns
  incident-investigation-patterns.md  Triage, RCA, mitigation playbooks, post-mortem template
  skill-authoring-guide.md            Guide for writing effective DevOps Agent skills

adapters/                           Tool-specific config files
  claude-code/                        CLAUDE.md + .claude/commands/*.md
  cursor/                             .cursor/rules/*.md
  codex/                              AGENTS.md
  windsurf/                           .windsurfrules
  github-copilot/                     .github/copilot-instructions.md
  cline/                              .clinerules
  gemini-cli/                         GEMINI.md
  antigravity/                        .agents/rules/*.md
  devops-agent/                       Assets + packaging for AWS DevOps Agent

install.sh                          Setup script for any tool
```

## Quick start

### Install script (recommended)

```bash
# Install for a specific tool
./install.sh ~/my-project --tool claude-code
./install.sh ~/my-project --tool cursor
./install.sh ~/my-project --tool kiro

# Install for multiple tools
./install.sh ~/my-project --tool kiro --tool claude-code --tool cursor

# Install for all supported tools
./install.sh ~/my-project --tool all

# Use symlinks for automatic updates
./install.sh ~/my-project --tool claude-code --symlink

# Install globally (applies to all projects)
./install.sh --global --tool claude-code
```

Run `./install.sh --help` for full usage.

> **Note on `--global`**: Global installation places configuration files directly in your home directory (e.g., `~/CLAUDE.md`, `~/AGENTS.md`, `~/.clinerules`, `~/.windsurfrules`) or in global tool-specific directories (e.g., `~/.kiro/`, `~/.claude/`, `~/.cursor/`). These files apply to all projects that don't have their own project-level configuration. Use project-level installation (the default) if you only want Well-Architected guidance for specific projects.
>
> **Note on existing files**: The installer will prompt before overwriting any existing files. Use `--force` to skip the prompt and overwrite without confirmation.

### Manual installation

#### Kiro

```bash
mkdir -p .kiro/steering .kiro/skills
cp path/to/this-repo/steering/well-architected.md .kiro/steering/
cp -r path/to/this-repo/skills/* .kiro/skills/
```

#### Claude Code

```bash
cp path/to/this-repo/adapters/claude-code/CLAUDE.md ./CLAUDE.md
cp -r path/to/this-repo/adapters/claude-code/commands .claude/commands
```

#### Cursor

```bash
cp -r path/to/this-repo/adapters/cursor/rules .cursor/rules
```

#### Codex (OpenAI)

```bash
cp path/to/this-repo/adapters/codex/AGENTS.md ./AGENTS.md
cp -r path/to/this-repo/skills ./skills
```

#### Windsurf

```bash
cp path/to/this-repo/adapters/windsurf/.windsurfrules ./.windsurfrules
```

#### GitHub Copilot

```bash
mkdir -p .github
cp path/to/this-repo/adapters/github-copilot/.github/copilot-instructions.md .github/
```

#### Cline

```bash
cp path/to/this-repo/adapters/cline/.clinerules ./.clinerules
```

#### Gemini CLI

```bash
cp path/to/this-repo/adapters/gemini-cli/GEMINI.md ./GEMINI.md
cp -r path/to/this-repo/skills ./skills
```

#### Antigravity

```bash
mkdir -p .agents/rules .agents/skills
cp -r path/to/this-repo/adapters/antigravity/rules/* .agents/rules/
for skill_dir in path/to/this-repo/skills/*/; do
  skill_name=$(basename "$skill_dir")
  mkdir -p ".agents/skills/$skill_name"
  cp "$skill_dir/SKILL.md" ".agents/skills/$skill_name/SKILL.md"
done
```

#### AWS DevOps Agent

```bash
# Package all skills as zip files for upload to your Agent Space
./install.sh ~/output-dir --tool devops-agent
# Then upload each .zip from ~/output-dir/devops-agent-skills/ via the Operator Web App
```

## How it works

**Skills** (`skills/*/SKILL.md`) are self-contained, tool-agnostic playbooks. Any AI coding agent can follow them step-by-step. They don't depend on steering or on each other.

**Steering** (`steering/*.md`) is Kiro-specific always-on context loaded into every conversation. Other tools use equivalent mechanisms (see adapters).

**Adapters** (`adapters/`) translate the steering into each tool's native config format and wire up skills as commands or rules.

| Tool | Steering mechanism | Skills mechanism |
| ---- | ----------------- | --------------- |
| Kiro | `.kiro/steering/*.md` | `.kiro/skills/*/SKILL.md` |
| Claude Code | `CLAUDE.md` | `.claude/commands/*.md` (slash commands) |
| Cursor | `.cursor/rules/*.md` | Rules with conditional activation |
| Codex | `AGENTS.md` | References `skills/` directory |
| Windsurf | `.windsurfrules` | References `skills/` directory |
| GitHub Copilot | `.github/copilot-instructions.md` | Inline (no separate skill mechanism) |
| Cline | `.clinerules` | References `skills/` directory |
| Gemini CLI | `GEMINI.md` | References `skills/` directory |
| Antigravity | `.agents/rules/well-architected.md` | `.agents/skills/*/SKILL.md` |
| AWS DevOps Agent | N/A (skills are self-contained) | `SKILL.md` zip upload to Agent Space |

## Skills overview

| Skill | Pillar(s) | Use when you need to... |
| ----- | --------- | ----------------------- |
| `wa-review` | All 6 | Run a full Well-Architected review |
| `reliability-improvement-plan` | Reliability | Find and eliminate single points of failure |
| `security-assessment` | Security | Assess IAM, detection, data protection, incident response |
| `cost-optimization-audit` | Cost Optimization | Identify waste and right-sizing opportunities |
| `performance-efficiency` | Performance Efficiency | Evaluate resource selection, scaling, and caching |
| `sustainability-optimization` | Sustainability | Reduce carbon footprint and resource waste |
| `migration-readiness` | All 6 | Assess readiness to migrate a workload to AWS |
| `operational-excellence` | Operational Excellence | Assess CI/CD, observability, incident management, operational maturity |
| `architecture-decision-record` | All 6 | Document a design decision with WA pillar impact |

## Verifying it works

Ask your AI coding agent:

```text
What Well-Architected pillars should I consider for this architecture?
```

If configured correctly, it will reference all six pillars with specific guidance rather than giving a generic answer. For Claude Code, try `/wa-review` to invoke the full review skill.

## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on adding skills or modifying steering files.

## License

This project is licensed under the [MIT-0 License](LICENSE).

## Related Resources

- [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html)
- [AWS Well-Architected Tool](https://aws.amazon.com/well-architected-tool/)
- [Kiro — AI-powered IDE](https://kiro.dev)
- [AWS DevOps Agent](https://docs.aws.amazon.com/devopsagent/latest/userguide/)
