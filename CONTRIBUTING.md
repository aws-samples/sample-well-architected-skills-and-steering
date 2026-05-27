# Contributing

Thank you for your interest in contributing to the Well-Architected Skills & Steering collection!

## How to Contribute

### Reporting Issues

Open an issue on GitHub describing the problem, including which steering file or skill is affected.

### Adding a New Skill

1. Create a directory under `skills/` with a descriptive kebab-case name (e.g., `skills/my-new-skill/`).
2. Add a `SKILL.md` file following the existing format:
   - YAML frontmatter with `name`, `description`, and `version`
   - Step-by-step instructions that Kiro can follow
   - A structured output template
   - Cross-references to relevant sections in `steering/well-architected.md`
3. Add evaluations in `skills/my-new-skill/evals/evals.json`:
   - Include at least 3 test cases with realistic user prompts
   - Each case should have 5–7 concrete assertions (gradable as PASS/FAIL)
   - Cover a range of scenarios: critical gaps, well-architected baselines, and edge cases
   - Run `uv run python run.py --skill my-new-skill --verbose` from the `evals/` directory to verify skill impact
4. Open a pull request with a description of what the skill does and which WA pillar(s) it covers.

### Modifying a Steering File

1. Edit files under `steering/`.
2. Ensure guidance is actionable and specific to the AWS Well-Architected Framework.
3. Open a pull request explaining what changed and why.

### Style Guidelines

- Use clear, imperative language in skills (e.g., "Evaluate whether..." not "You might want to evaluate...").
- Include severity labels for findings: 🔴 High Risk, 🟡 Medium Risk, 🟢 Improvement.
- Reference specific AWS services where applicable.
- Keep steps concise — each step should represent a distinct action or evaluation.

### Pull Request Process

1. Fork the repository and create a feature branch.
2. Make your changes and verify they render correctly as Markdown.
3. Submit a pull request with:
   - A short title summarizing the change
   - A description of what guidance you added or modified
   - Which WA pillar(s) are covered
4. A maintainer will review your PR and may request changes.

## Security Issue Notifications

If you discover a potential security issue in this project, we ask that you notify AWS/Amazon Security via our [vulnerability reporting page](http://aws.amazon.com/security/vulnerability-reporting/). Please do **not** create a public GitHub issue.

## Code of Conduct

This project has adopted the [Amazon Open Source Code of Conduct](https://aws.github.io/code-of-conduct). For more information, see the [Code of Conduct FAQ](https://aws.github.io/code-of-conduct-faq) or contact [opensource-codeofconduct@amazon.com](mailto:opensource-codeofconduct@amazon.com) with any additional questions or comments.

## Licensing

See the [LICENSE](LICENSE) file for our project's licensing. We will ask you to confirm the licensing of your contribution.

We may ask you to sign a [Contributor License Agreement (CLA)](http://en.wikipedia.org/wiki/Contributor_License_Agreement) for larger changes.