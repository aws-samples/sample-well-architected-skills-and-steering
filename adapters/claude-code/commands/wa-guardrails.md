Generate preventive Well-Architected guardrails — AWS Config rules, Service Control Policies, permission boundaries, CloudWatch alarms, and IaC policy checks (CDK Aspects, cfn-guard, OPA/Sentinel) — so a workload stays compliant over time instead of being assessed once.

Unlike the assessment commands (which find gaps) or `/wa-remediation` (which fixes one finding), guardrails codify best practices so non-compliant changes are blocked or flagged automatically — in CI, at deploy time, and continuously in the account.

## Step 1: Gather context

Ask the user (skip anything already provided or inferable from the codebase):

> I can generate guardrails to keep your workload Well-Architected. Let me know:
> - **Workload name** and code packages/directories (IaC, CI/CD configs)
> - **IaC dialect**: CDK (which language), CloudFormation, Terraform, SAM, or mixed
> - **Source of controls**: a prior `/wa-review` or assessment output, specific concerns, or "scan and propose"
> - **Enforcement points available**: CI pipeline (which one), AWS Organizations/SCPs, AWS Config, account-level admin
> - **Pillars to prioritize** (optional; default: Security and Reliability)

If you are in a codebase, proceed directly and infer the IaC dialect and CI system from the files present.

## Step 2: Discovery — what to enforce

**Path A — From an assessment (preferred):** parse the prior review for findings, their pillar, severity, evidence (file:line), and the Best Practice IDs cited. Each High/Critical finding becomes a candidate guardrail so the same gap cannot recur.

**Path B — Standalone scan:** analyze the IaC and identify the control-worthy configurations in use — encryption, public access, IAM scope, multi-AZ, backups, logging, TLS, tagging — and map each to the WA Best Practice it relates to.

Produce a **control candidate list**: pillar, WA Question/BP ID, resource type, current state (compliant / non-compliant / absent), and the enforcement point that fits.

## Step 3: Select preventive vs. detective

For each candidate pick the strongest control the user's enforcement points allow. Prefer **preventive** over detective:

- Catchable in IaC before deploy → **CI policy check** (CDK Aspect, `cfn-guard`/`cfn-lint`, Terraform OPA/Sentinel). Strongest and cheapest.
- Must be blocked org-wide → **SCP / permission boundary**.
- Only observable on the live resource (drift, runtime) → **AWS Config rule** (detective; auto-remediation only if confirmed).
- Continuous reliability/cost/performance signal → **CloudWatch metric + alarm**.

If a control can't be enforced with the available points, say so rather than emitting something that won't run.

## Step 4: Generate the controls

Emit each selected control as ready-to-commit code in the workload's existing dialect. Each MUST cite the WA Question/BP ID it enforces, be labeled 🛡️ Preventive or 🔍 Detective, and state in one line what it blocks/flags and why. Cover as applicable:

- **Security (SEC)** — Config: `s3-bucket-server-side-encryption-enabled`, `s3-bucket-public-read-prohibited`, `iam-policy-no-statements-with-admin-access`; SCP denying unencrypted-resource creation or CloudTrail disablement; CDK Aspect failing synth on a `0.0.0.0/0` security group.
- **Reliability (REL)** — `rds-multi-az-support`, `dynamodb-pitr-enabled`, `db-instance-backup-enabled`; `cfn-guard` rule requiring `DeletionProtection`; alarm on DLQ depth.
- **Operational Excellence (OPS)** — CI check for required tags; Config rule for log retention; SCP preventing out-of-band changes.
- **Cost (COST)** — CI check for approved instance types/capacity modes; budget/anomaly alarm.
- **Performance / Sustainability (PERF/SUS)** — CI check preferring Graviton/managed services.

Provide each snippet in a fenced code block with its target filename, matching the workload's dialect. Examples of the three common forms:

```yaml
# guardrails/config-rules.yaml  — 🔍 Detective, SEC 8 (encryption at rest)
Resources:
  S3EncryptionEnabled:
    Type: AWS::Config::ConfigRule
    Properties:
      ConfigRuleName: s3-bucket-server-side-encryption-enabled
      Source: { Owner: AWS, SourceIdentifier: S3_BUCKET_SERVER_SIDE_ENCRYPTION_ENABLED }
```

```typescript
// guardrails/no-open-sg.aspect.ts — 🛡️ Preventive, SEC 5 (fails cdk synth on 0.0.0.0/0)
export class NoOpenIngress implements IAspect {
  visit(node: IConstruct): void {
    if (node instanceof CfnSecurityGroupIngress &&
        node.cidrIp === "0.0.0.0/0" && ![80, 443].includes(Number(node.fromPort))) {
      Annotations.of(node).addError(`SEC 5: open to 0.0.0.0/0 on port ${node.fromPort}`);
    }
  }
}
```

```
# guardrails/reliability.guard — 🛡️ Preventive, REL 9 (cfn-guard)
AWS::RDS::DBInstance { Properties { MultiAZ == true  DeletionProtection == true } }
```

## Step 5: Produce the guardrails plan

Output: a summary (dialect, enforcement points, source, control counts split preventive/detective); controls grouped by pillar (each with name, preventive/detective label, enforcement point, what it blocks, the file + snippet, and any coverage gap); a **rollout plan** table (start preventive checks/SCPs in warn/log mode, promote to block once clean); a **verification** section (attempt a known-bad change, confirm CI fails / check Config compliance); and a **not covered** section for controls the available enforcement points can't implement.

## Step 6: Offer a governance steering doc

Beyond machine-enforced controls, offer to capture the same standards as a **human- and agent-readable governance doc** — the prose counterpart to the guardrails, for standards a control can't fully express (design conventions, review expectations) and for teams that want an always-on policy their AI agent follows. Generate it on request as a steering file the agent loads automatically (`.kiro/steering/`, `CLAUDE.md`, `.cursor/rules/`), with: an "Enforced automatically" section (one line per machine control + its BP ID), a "Conventions to follow (not auto-enforced)" section, and standing "When proposing or reviewing changes" instructions. Keep each statement tied to a WA Question/BP ID and short enough for always-on context.

## Step 7: Offer follow-up

> Would you like me to:
> - Generate the CI workflow wiring (GitHub Actions / CodePipeline step) to run the policy checks?
> - Produce a governance steering doc (`CLAUDE.md` / `.cursor/rules/` / `.kiro/steering/`) capturing these standards for your AI agent?
> - Add auto-remediation to a detective Config rule (with safety review)?
> - Run a `/wa-remediation` pass to fix the existing violations these guardrails would block?
> - Tighten a control from warn mode to block mode?

## Calibration

- Prefer **preventive** (CI/IaC) over **detective**; fall back to detective only when the issue is only visible on the live resource.
- Never emit a control for an enforcement point the user doesn't have — say it's not enforceable and what's needed.
- Roll out preventive controls and `Deny` SCPs in **warn/log mode first** — a hard block on day one can break existing pipelines.
- Auto-remediation is destructive: only when explicitly asked, with a safety/rollback note.
- Tie every control to a WA Question/BP ID — a guardrail without a "why" gets disabled the first time it's inconvenient.
- Don't over-generate: a focused set the team keeps beats 50 noisy rules they'll mute.
- Match the workload's dialect — CDK Aspects for CDK, `cfn-guard` for CloudFormation, OPA/Sentinel for Terraform; don't mix paradigms.
