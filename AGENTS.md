---
name: agents
description: Steering file for agents and peers working in this repository. Covers contribution workflows, release process, open source community standards, and data hygiene rules.
version: 1.0.0
tags: [steering, contributing, open-source]
---

# Agent Steering — WA Skills & Steering Docs

## Deprecation status

This repository's skill is deprecated in favor of the actively maintained
`aws-well-architected-review` skill in
[Agent Toolkit for AWS](https://github.com/aws/agent-toolkit-for-aws)
([product page](https://aws.amazon.com/products/developer-tools/agent-toolkit-for-aws/)).
See [SUCCESSOR_HANDOFF.md](SUCCESSOR_HANDOFF.md) and
[issue #147](https://github.com/aws-samples/sample-well-architected-skills-and-steering/issues/147)
for the migration plan. Practical implications for anyone working in this repo:

- **New skills and features are not being accepted.** Do not open PRs adding
  a new skill under `skills/` or new steering guidance.
- **Bug fixes, security reports, and corrections are still welcome** and follow
  the normal PR process below.
- The "release after every merged PR" rule and the SLA table further down
  still apply to accepted fix PRs, but are no longer a commitment for new
  feature work, since none is being merged.
- The evaluation harness under `evals/` keeps running as the
  compatibility/regression suite `SUCCESSOR_HANDOFF.md` calls for.

## Overview

Guidance for any agent or peer working in this repository. Read this before adding a skill, editing a steering file, merging a PR, or responding to a community issue.

## Usage

Read this file before:

- Adding or modifying a skill under `skills/`
- Editing a steering file under `steering/`
- Merging a pull request
- Responding to an issue or pull request from an external contributor
- Running evaluations

## Instructions

### Tooling

Always use `uv` to run Python scripts. Never use bare `pip`, `python -m venv`, or `python` directly.

```bash
uv run python run.py --skill my-new-skill --verbose
```

### Adding a New Skill

Skills must conform to the [Agent Skills Open Specification](https://agentskills.io/specification).

1. Create a directory under `skills/` with a descriptive kebab-case name (e.g., `skills/my-new-skill/`).
2. Add a `SKILL.md` file following the format in `skills/example-skill/SKILL.md`:
   - YAML frontmatter: `name`, `description`, `version`, `tags`
   - Sections: Overview, Usage, Instructions, Troubleshooting, Supporting Files, Core Concepts, Quick Reference, Common Mistakes
   - Cross-references to relevant sections in `steering/well-architected.md`
3. Add evaluations in `skills/my-new-skill/evals/evals.json`:
   - At least 3 test cases with realistic user prompts
   - 5–7 concrete PASS/FAIL assertions per case
   - Cover critical gaps, WA baselines, and edge cases
   - Run evals before opening a PR: `uv run python run.py --skill my-new-skill --verbose`
4. Open a PR describing what the skill does and which WA pillar(s) it covers.

### Modifying a Steering File

1. Edit files under `steering/`.
2. Guidance must be actionable and specific to the AWS Well-Architected Framework.
3. Open a PR explaining what changed and why.

### Pull Request Process

1. Fork the repository and create a feature branch.
2. Verify changes render correctly as Markdown.
3. Submit a PR with a short title, a description of what changed, and which WA pillar(s) are covered.
4. At least one project team member must review every PR. Large features should have additional reviewers.
5. After a PR merges, create a new GitHub release (see below).

### GitHub Releases

Create a new GitHub release after every merged PR — no exceptions, including small changes.

- Tag format: `vMAJOR.MINOR.PATCH`
  - `PATCH` — documentation fixes, typo corrections, minor clarifications
  - `MINOR` — new skills, new steering guidance, new evals
  - `MAJOR` — breaking changes to skill format or steering structure
- Release notes must list what was added, changed, or removed.

### Design Principles

- **Review and guidance, not code mutation.** Skills produce findings, plans, controls, or visual artifacts — never a PR-ready diff applied to the user's codebase. Keep the user in control of implementation decisions.
- **Aligned, not compliant.** Do not use "compliant" or "compliance" as customer outcomes. Use "aligned with best practices," "adherent to WA guidance," or similar phrasing.
- **Occam's razor.** Prefer the simplest skill design that satisfies the requirement. Avoid adding steps that do not add measurable value.
- **Data-driven.** Findings must be grounded in evidence from the user's codebase or configuration. Cite the specific resource, file, or configuration that supports each finding.

### Style Guidelines

- Use clear, imperative language (e.g., "Evaluate whether…" not "You might want to evaluate…").
- Include severity labels for findings: 🔴 High Risk, 🟡 Medium Risk, 🟢 Improvement.
- Reference specific AWS services where applicable.
- Keep steps concise — each step should represent a distinct action or evaluation.

### Open Source Community Standards

Respond to all issues and pull requests on schedule:

| Situation | Target |
|---|---|
| New issue or PR opened | Review within 1 business day |
| Security vulnerability | Respond immediately |
| General issues / PRs | Respond within 1 week |
| Non-urgent resolution | Resolve within 3 weeks |
| Enhancement / feature request | Apply label; no hard deadline |

Subscribe to repository notifications.

All external contributions require the standard licensing statement via `.github/PULL_REQUEST_TEMPLATE.md`. Do not modify the template text.

### Data Hygiene

- Do not commit raw eval result files — they can contain internal data. Add their paths to `.gitignore`.
- Before committing any file, verify it contains no internal URLs, service names, account IDs, or other non-public information.
- **No measurement results in tracked files.** This is a public repository: it ships the measurement tooling, not our numbers. Keep the following out of every tracked file, PR description, and release note — eval or benchmark scores and baseline-vs-skill deltas, cost figures and per-token rates, latency/wall-clock/throughput/token counts presented as measurements, speedup multipliers and percentage improvements, model-vs-model or tool-vs-tool comparison tables, and any third-party product's scores or prices. Methodology stays: metric definitions, the run recipe, the ground-truth rule, and known limitations all belong here. See `CONTRIBUTING.md`, "Measurement results stay local".
- Unreleased service or endpoint names, and internal service names, never appear in shipped code, config, comments, or docs.

## Troubleshooting

### Eval results accidentally staged

```bash
git reset HEAD evals/**/*.json
```

Add the pattern to `.gitignore` if missing.

### Release tag already exists

```bash
git tag --sort=-v:refname | head -5
```

Increment the appropriate version component and retag.

### Off-topic or irate community issues

- Label off-topic issues as `invalid` and close with a clear explanation.
- For irate users: respond calmly, set realistic expectations, offer to accept a PR if the fix is low priority.
- Do not engage with trolls — stay professional. Escalate to `aws-github@amazon.com` if a user continues causing issues.
- For security issues: direct reporters to the [vulnerability reporting page](http://aws.amazon.com/security/vulnerability-reporting/). Do not discuss in public issues.

## Supporting Files

### skills/example-skill/SKILL.md

Canonical template for new skills. Copy this as the starting point for any new skill.

### steering/well-architected.md

Core WA guidance. Cross-reference this in every new skill.

### steering/aws-well-architected-framework-review.md

Full WA review methodology. Reference for review-type skills.

### evals/run.py

Evaluation runner. Always invoke via `uv run python run.py`.

## Core Concepts

**Skills produce artifacts, not patches.** The output of a skill is a finding, plan, set of controls, or visual — never code applied to the user's codebase on their behalf.

**Every merge gets a release.** GitHub releases are the versioned record of this project. Skipping one breaks the changelog.

**Open source SLAs are commitments.** This is a public repository. Response and resolution timelines are not suggestions.

## Quick Reference

| Task | Action |
| ---- | ------ |
| Run evals | `uv run python run.py --skill <name> --verbose` |
| New skill template | Copy `skills/example-skill/SKILL.md` |
| Create a release | Tag `vX.Y.Z` on the merge commit; publish release notes |
| Report a security issue | [aws.amazon.com/security/vulnerability-reporting](http://aws.amazon.com/security/vulnerability-reporting/) |
| PR response SLA | Review within 1 business day |
| Non-urgent resolution SLA | Within 3 weeks |

## Common Mistakes

**Committing raw eval output.** Eval result files can contain internal data. Never commit them; add their paths to `.gitignore`.

**Publishing measurement results.** Writing an F1 score, a cost per run, a latency figure, a speedup multiplier, or a model comparison table into a tracked file, a PR body, or a release note. The repository ships the harness so readers measure in their own environment; describe the methodology, not the outcome. See **Data Hygiene** above.

**Using "compliant" language.** Saying a workload is "compliant" implies a legal or regulatory guarantee. Use "aligned with best practices" instead.

**Skipping the GitHub release.** Every merged PR must produce a release. Do not batch or defer releases.

**Running Python without uv.** Always use `uv run` — bare `python` or `pip` bypasses the project's dependency lockfile.
