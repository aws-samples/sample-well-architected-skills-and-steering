---
name: wa-guardrails
description: Generate preventive Well-Architected guardrails — AWS Config rules, Service Control Policies, permission boundaries, CloudWatch alarms, and IaC policy checks (CDK Aspects, cfn-guard, OPA/Sentinel) — plus an optional governance steering doc, so a workload stays compliant over time instead of being assessed once. Use when the user wants to enforce best practices in CI, prevent insecure or non-compliant configurations from shipping, detect configuration drift, codify the fixes from a Well-Architected review as ongoing controls, or capture standards as an always-on steering file for their AI coding agent.
version: 1.0.0
---

# Well-Architected Guardrails

This skill generates **preventive and detective controls** that keep a workload Well-Architected over time. Unlike the assessment skills (which find gaps) or remediation (which fixes a specific finding once), guardrails codify best practices so non-compliant changes are blocked or flagged automatically — in CI, at deploy time, and continuously in the account.

**What you'll produce:** ready-to-commit control files (Config rules, SCPs, CI policy checks, alarms), each tied to the WA Question/Best Practice ID it enforces, with a note on whether the control is **preventive** (blocks the bad change) or **detective** (flags it after the fact).

## Step 1: Gather context

Ask the user (skip any already provided or inferable from the codebase):

> I can generate guardrails to keep your workload Well-Architected. Let me know:
> - **Workload name** and code packages/directories (IaC, CI/CD configs)
> - **IaC dialect**: CDK (which language), CloudFormation, Terraform, SAM, or mixed
> - **Source of controls**: a prior `/wa-review` or assessment output, specific concerns, or "scan and propose"
> - **Enforcement points available**: CI pipeline (which one), AWS Organizations/SCPs, AWS Config, account-level admin — so controls target what you can actually deploy
> - **Pillars to prioritize** (optional; default: Security and Reliability)

If you are in a codebase, proceed directly and infer the IaC dialect and CI system from the files present.

## Step 2: Discovery — what to enforce

Determine the controls to generate from one of two inputs:

**Path A — From an assessment (preferred):** parse the prior review for findings, their pillar, severity, evidence (file:line), and the Best Practice IDs cited. Each High/Critical finding becomes a candidate guardrail so the same gap cannot recur.

**Path B — Standalone scan:** analyze the IaC and identify the control-worthy configurations actually in use — storage encryption, public access, IAM scope, multi-AZ, backups, logging, TLS, tagging. Map each to the WA Best Practice it relates to.

Produce a **control candidate list**: for each, record the pillar, the WA Question/BP ID, the resource type it applies to, the current state (compliant / non-compliant / absent), and the **enforcement point** that fits (CI check, Config rule, SCP, alarm).

## Step 3: Select preventive vs. detective for each control

For every candidate, choose the strongest control the user's enforcement points allow. Prefer **preventive** (stops the bad change before it ships) over **detective** (catches it afterward). Use this decision guidance:

- Can the misconfiguration be caught in IaC before deploy? → **CI policy check** (CDK Aspect, `cfn-guard`/`cfn-lint`, Terraform OPA/Sentinel). Strongest and cheapest.
- Must it be blocked org-wide regardless of who deploys? → **SCP or permission boundary**.
- Is it only observable on the live resource (e.g. drift, runtime state)? → **AWS Config rule** (detective; add auto-remediation only if the user confirms).
- Is it a continuous reliability/cost/performance signal? → **CloudWatch metric + alarm**.

If a control cannot be enforced with the available points, say so explicitly rather than emitting a control that won't run.

## Step 4: Generate the controls

Generate every selected control as ready-to-commit code in the workload's existing dialect and conventions. Each control MUST:

- Cite the WA Question/BP ID it enforces (e.g. `SEC 8`, `REL 9`)
- Be labeled 🛡️ Preventive or 🔍 Detective
- Include a one-line statement of what it blocks/flags and why it matters

Cover, as applicable to the workload:

**Security (SEC)** — examples: `s3-bucket-server-side-encryption-enabled`, `s3-bucket-public-read-prohibited`, `iam-policy-no-statements-with-admin-access` (Config); SCP denying creation of unencrypted resources or disabling CloudTrail; a CDK Aspect failing synth on a security group open to `0.0.0.0/0` on non-web ports.

**Reliability (REL)** — `rds-multi-az-support`, `dynamodb-pitr-enabled`, `db-instance-backup-enabled` (Config); a `cfn-guard` rule requiring `DeletionProtection` on stateful resources; an alarm on DLQ depth.

**Operational Excellence (OPS)** — a CI check requiring tags (owner, cost-center, environment); a Config rule for required CloudWatch log retention; an SCP preventing manual changes outside IaC.

**Cost (COST)** — a CI check flagging instance types or capacity modes outside an approved list; a budget/anomaly alarm.

**Performance / Sustainability (PERF/SUS)** — a CI check preferring Graviton/managed services where applicable.

Provide each control's snippet in a fenced code block with the target filename, so the user can commit it directly. Match the workload's dialect — examples of the three most common forms:

**Detective — AWS Config managed rule (SEC 8, encryption at rest), CloudFormation:**

```yaml
# guardrails/config-rules.yaml
Resources:
  S3EncryptionEnabled:                      # 🔍 Detective — flags any S3 bucket without SSE
    Type: AWS::Config::ConfigRule
    Properties:
      ConfigRuleName: s3-bucket-server-side-encryption-enabled
      Source: { Owner: AWS, SourceIdentifier: S3_BUCKET_SERVER_SIDE_ENCRYPTION_ENABLED }
```

**Preventive — CDK Aspect (SEC 5, no open security groups), TypeScript:**

```typescript
// guardrails/no-open-sg.aspect.ts
import { IAspect, Annotations } from "aws-cdk-lib";
import { CfnSecurityGroupIngress } from "aws-cdk-lib/aws-ec2";
import { IConstruct } from "constructs";

// 🛡️ Preventive — fails `cdk synth` on 0.0.0.0/0 ingress to non-web ports
export class NoOpenIngress implements IAspect {
  visit(node: IConstruct): void {
    if (node instanceof CfnSecurityGroupIngress &&
        node.cidrIp === "0.0.0.0/0" && ![80, 443].includes(Number(node.fromPort))) {
      Annotations.of(node).addError(`SEC 5: security group open to 0.0.0.0/0 on port ${node.fromPort}`);
    }
  }
}
```

**Preventive — cfn-guard rule (REL 9, stateful resources need deletion protection):**

```
# guardrails/reliability.guard
# 🛡️ Preventive — blocks RDS instances without Multi-AZ + deletion protection
AWS::RDS::DBInstance {
  Properties { MultiAZ == true  DeletionProtection == true }
}
```

## Step 5: Produce the guardrails plan

Output a structured deliverable:

```markdown
# Well-Architected Guardrails: {Workload Name}

## Summary
- **IaC dialect**: {CDK/CloudFormation/Terraform/SAM}
- **Enforcement points used**: {CI / Config / SCP / alarms}
- **Source**: {prior review / standalone scan}
- **Controls generated**: {N} ({P} preventive, {D} detective) across {pillars}

## Controls by pillar

### {Pillar} — {WA Question/BP ID}
- **Control**: {name}  |  🛡️ Preventive / 🔍 Detective  |  Enforcement: {CI / Config / SCP / alarm}
- **Blocks/flags**: {what, and why it matters}
- **File**: `{path}`
  ```{lang}
  {ready-to-commit snippet}
  ```
- **Coverage gap** (if any): {what this control does NOT catch}

## Rollout plan
| Order | Control | Enforcement | Risk of false-positive | Notes |
|-------|---------|-------------|------------------------|-------|
{Start in warn/log mode for preventive CI checks and SCPs, then promote to block once clean.}

## Verification
{How to confirm each control works — e.g. attempt a known-bad change in a branch and confirm CI fails; check Config rule compliance status.}

## Not covered
{Controls the available enforcement points cannot implement, and what would be needed.}
```

## Step 6: Offer a governance steering doc

Beyond machine-enforced controls, offer to capture the same standards as a **human- and agent-readable governance doc** — the prose counterpart to the guardrails. This is useful for the standards a control can't fully express (design conventions, review expectations) and for teams that want an always-on policy their AI coding agent will follow.

Generate it on request as a steering file the agent loads automatically (e.g. `.kiro/steering/`, `CLAUDE.md`, `.cursor/rules/`), structured as:

```markdown
# {Workload} — Well-Architected Guardrails (Governance)

## Enforced automatically
{One line per machine control, linking the rule file and its WA BP ID — so readers know what is already gated in CI/Config.}

## Conventions to follow (not auto-enforced)
- {Pillar} — {convention}, because {WA BP ID rationale}. {How a reviewer/agent checks it.}

## When proposing or reviewing changes to this workload
- {Standing instruction, e.g. "new data stores MUST set encryption + backups before merge (SEC 8 / REL 9)"}
```

Keep each statement tied to a WA Question/BP ID, and keep the doc short enough to live in always-on context without bloat.

## Step 7: Offer follow-up

> Would you like me to:
> - Generate the CI workflow wiring (GitHub Actions / CodePipeline step) to run the policy checks?
> - Produce a governance steering doc (`CLAUDE.md` / `.cursor/rules/` / `.kiro/steering/`) capturing these standards for your AI agent?
> - Add auto-remediation to a detective Config rule (with safety review)?
> - Fix the existing violations these guardrails would block (remediate the current code)?
> - Tighten a control from warn mode to block mode?

## Calibration Guidance

- Prefer **preventive** controls (catch in CI/IaC) over **detective** — they're cheaper and stop the problem before it ships; only fall back to detective when the issue is only visible on the live resource.
- Never emit a control for an enforcement point the user doesn't have — say it's not enforceable and what's needed instead.
- **Roll out preventive controls in warn/log mode first.** Recommending a hard `block` or `Deny` SCP on day one risks breaking existing pipelines — flag this and stage it.
- Auto-remediation is **destructive**: only generate it when the user explicitly asks, and include a safety/rollback note.
- Tie every control to a WA Question/BP ID so the builder can trace the rationale — a guardrail without a "why" gets disabled the first time it's inconvenient.
- Don't over-generate: a focused set of high-value controls that the team will keep beats 50 noisy rules they'll mute.
- Respect the workload's existing dialect and conventions — emit CDK Aspects for a CDK app, `cfn-guard` for CloudFormation, OPA/Sentinel for Terraform; don't mix paradigms.
- The governance steering doc complements controls, it doesn't replace them — prefer a machine-enforced control whenever one exists, and use the doc for what code can't express. Keep it concise enough for always-on context.
