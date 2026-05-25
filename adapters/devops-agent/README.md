# AWS DevOps Agent Adapter

Deploy Well-Architected skills to [AWS DevOps Agent](https://docs.aws.amazon.com/devopsagent/latest/userguide/) as reusable investigation workflows.

## How it works

AWS DevOps Agent consumes the same `SKILL.md` format used in this repository. Each skill directory under `skills/` can be uploaded directly to your Agent Space as a zip file, or created via the Operator Web App UI.

## Deployment options

### Option 1: Upload as zip files

Each skill directory is already structured for DevOps Agent zip upload:

```bash
# Package a single skill
cd skills/wa-review
zip -r wa-review.zip SKILL.md

# Package a skill with references/assets (if present)
cd skills/security-assessment
zip -r security-assessment.zip .
```

Then upload via the Operator Web App:
1. Navigate to **Skills** in your Agent Space
2. Click **Add skill** → **Upload skill**
3. Select the zip file
4. Choose agent type(s): **Generic** (recommended for WA skills) or target specific types

### Option 2: Create via UI

1. Navigate to **Skills** in your Agent Space
2. Click **Add skill** → **Create skill**
3. Copy the `name` and `description` from the SKILL.md frontmatter
4. Paste the instructions (everything after the frontmatter)
5. Select agent type(s)

### Option 3: Use the install script

```bash
# Package all skills for DevOps Agent upload
./install.sh ~/output-dir --tool devops-agent
```

This creates zip files ready for upload in the target directory.

## Agent type recommendations

| Skill | Recommended Agent Type |
|-------|----------------------|
| `wa-review` | On-demand, Evaluation |
| `security-assessment` | On-demand, Evaluation |
| `reliability-improvement-plan` | On-demand, Incident RCA |
| `cost-optimization-audit` | On-demand, Evaluation |
| `performance-efficiency` | On-demand, Incident RCA |
| `sustainability-optimization` | On-demand, Evaluation |
| `migration-readiness` | On-demand |
| `architecture-decision-record` | On-demand |

## Shared assets

The top-level `assets/` directory contains best-practice reference material (WA Framework best practices, CloudWatch metrics reference, investigation patterns, skill authoring guide). When packaging for DevOps Agent via the install script, these are automatically bundled into each skill's `assets/` folder. Other adapters can also reference these assets in the future.

## Skill compatibility

The skills in this repository follow the [Agent Skills specification](https://agentskills.io/) subset supported by DevOps Agent:

- SKILL.md with frontmatter (`name`, `description`) — required
- `references/` directory with Markdown docs — optional
- `assets/` directory with images, diagrams, data — optional
- No executable scripts (not supported by DevOps Agent)
