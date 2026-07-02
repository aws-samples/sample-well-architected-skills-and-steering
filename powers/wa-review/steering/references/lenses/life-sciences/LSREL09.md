# LSREL09 — Change nanagement

**Pillar**: Reliability  
**Best Practices**: 6

---

# LSREL09-BP01 Create and verify rollback plans

For every release or approved change, maintain a documented rollback
plan that is versioned with the release artifacts. Validate rollback
procedures in non-production environments and include rollback steps
in the change control package and test evidence. Define roles,
approvals, and communications for execution and escalation.

**Desired outcome:** Rollback
processes are predictable, validated, and repeatable so that failed
changes do not compromise operations, regulatory adherence, or data
integrity.

**Common anti-patterns:**

- Relying on undocumented or manual rollback steps.
- Skipping rollback testing due to time constraints.
- Treating rollback as optional rather than mandatory in GxP
environments.

**Benefits of establishing this best
practice:**

- Reduces risk of prolonged downtime that can invalidate
experiments or delay clinical timelines.
- Preserves integrity of regulated datasets and audit trails.
- Demonstrates predictable change control to auditors and
stakeholders.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Rollback plans should be created alongside release plans and
treated as first-class artifacts in change control. Plans must
include the exact steps to revert application code, configuration,
database schema, and dependent infrastructure changes. Validation
of rollback plans in staging or pre-production environments should
exercise the entire procedure (including approvals and
notifications) so that time-to-rollback and behavioral impacts are
well understood.

Where human steps are required, provide clear runbooks and defined
approvers. Where feasible, automate rollback actions to reduce
human error. Record rollback test evidence, and attach the
evidence to the validation package for auditability.

### Implementation steps

- Create pipelines and rollback actions in AWS CodePipeline
and codify deployment artifacts with AWS CloudFormation
templates so infrastructure changes are reversible.
- Use AWS CodeDeploy or CloudFormation change-sets with
pre-defined rollback behavior.
- Implement standardized rollback runbooks using AWS Systems Manager Automation so operators can run approved, automated
steps.
- Store validated rollback artifacts and test evidence in AWS CodeCommit or Amazon S3, and include change-control metadata
for traceability.

## Resources

**Related best practices:**

- Continuity of workflows and data availability during downtime
- Fault isolation and graceful degradation in workflows
- Automated validation in deployments

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsrel09-bp01.html*

---

# LSREL09-BP02 Implement safe deployment strategies (like blue/green or canary)

Adopt deployment patterns that minimize blast radius and allow rapid
diversion to the last known good state. Phased rollouts provide
early detection of issues and enable quick rollback without
impacting users or downstream regulatory workflows.

**Desired outcome:** Failed releases
can be quickly rolled back or diverted with minimal disruption to
end users and regulatory processes.

**Common anti-patterns:**

- Performing deployments at once without a rollback path.
- No traffic segmentation or user impact analysis during rollouts.
- Failing to gather metrics and health signals during phased
deployments.

**Benefits of establishing this best
practice:**

- Limits impact to a subset of experiments or studies rather than
the entire user base and workflows.
- Enables rapid return to a validated state, protecting study
timelines.
- Improves stakeholder confidence in release safety and stability.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Choose a rollout strategy based on risk and verification needs:
blue/green for fast switchovers to fully validated environments,
canary for incremental exposure and metric observation, or
feature-flag driven rollouts for business-level segmentation.
Instrument deployments with health metrics, business KPIs, and
signals so an automated or manual rollback decision can be made
quickly. Validate the traffic-shift and rollback procedures during
staging exercises and include them in release approvals.

### Implementation steps

- Use blue/green deployment patterns available in AWS Elastic Beanstalk or by provisioning parallel stacks using AWS CloudFormation and switching traffic with Amazon Route 53 or
load balancer reconfiguration.
- Use Amazon ECS or Amazon EKS with traffic shifting
configured (for example, using AWS App Mesh or AWS CodeDeploy integration) to implement canary releases.
- Implement automated traffic shifting and rollback policies
in AWS CodeDeploy so that failing canaries automatically
trigger rollbacks or traffic diversion.

## Resources

**Related best practices:**

- Continuity of workflows and data availability during downtime
- Resilient environment provisioning and lifecycle management
- Automated validation in deployments

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsrel09-bp02.html*

---

# LSREL09-BP03 Verify data integrity and point-in-time recovery

Protect application and data state so that you can restore to a
precise point-in-time prior to a failed change. Backups must be
consistent, validated, and aligned with organizational RTO and RPO
targets. Include configuration and metadata in backups so restored
environments are audit-complete.

**Desired outcome:** Data and
application state can be restored to the exact state prior to the
failed change, preserving adherence and operational continuity.

**Common anti-patterns:**

- Infrequent or unplanned backups without restore validation.
- Omitting metadata or configuration in backup sets.
- Not aligning backup frequency to defined RTO and RPO needs of
regulated systems.

**Benefits of establishing this best
practice:**

- Avoids loss of experiment data, patient records, or audit
evidence during failed changes.
- Shortens recovery time, preserving study timelines and sample
integrity.
- Demonstrates recoverability to auditors and stakeholders.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Define RTO and RPO aligned to the criticality of datasets and
regulated processes. Implement automated, policy-driven backups
that include application-level snapshots, database backups
(including transaction logs for point-in-time recovery), and
configuration exports. Regularly perform restore drills and
document restoration time and fidelity as part of validation
evidence. Store backups in tamper-evident, redundant storage and
that retention policies meet regulatory retention requirements.

### Implementation steps

- Implement policy-driven backups using AWS Backup for
supported services.
- Enable automated backups and snapshots for databases (for
example, automated backups for Amazon RDS and snapshot
schedules for Amazon EC2 or Amazon EBS).
- Configure point-in-time recovery for services that support
it, such as enabling PITR for Amazon DynamoDB.
- Store and catalog backup artifacts in Amazon S3 with
appropriate lifecycle and retention rules, and use AWS Backup's recovery testing features to validate restores.

## Resources

**Related best practices:**

- Long-term storage and reliable recovery of trial data
- Observability and monitoring of pipelines
- Automated validation in deployments

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsrel09-bp03.html*

---

# LSREL09-BP04 Maintain auditable rollback and recovery records

Capture and retain immutable, timestamped records of every rollback
and recovery action, including approvals, deviations, timing, and
outcomes. Audit and governance artifacts are required evidence for
GxP adherence and should be integrated into change control and
incident reporting.

**Desired outcome:** Every rollback
or recovery is traceable and auditable with internal SOPs and
external GxP requirements.

**Common anti-patterns:**

- Treating rollback as a purely technical process without
traceability.
- Failing to log deviations or decisions during recovery.
- Storing audit records in a non-durable or unsearchable formats.

**Benefits of establishing this best
practice:**

- Demonstrates regulatory adherence and governance over change
activities.
- Enables post-event analysis and corrective actions to avoid
recurrence.
- Supports transparent reporting to sponsors, regulators, and QA
teams.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Integrate audit capture into every phase of change and rollback:
record the release checksum, approvals, automated actions taken,
timestamps for each step, deviations, and post-rollback
verification results. Use immutable storage and tamper-evident
logs and include audit evidence as part of the change record.
Verify that your log retention policy meets regulatory retention
policies and that search and indexing capabilities support timely
retrieval for inspections.

### Implementation steps

- Enable AWS CloudTrail to capture API activity and
operational actions related to deployment and rollback.
- Use AWS Config to record configuration state and change
history for infrastructure resources.
- Store immutable audit records in Amazon S3 with S3 Object
Lock enabled to enforce retention and immutability.
- Index and make records discoverable with Amazon OpenSearch Service or a governance catalog for rapid response to audit
requests.

## Resources

**Related best practices:**

- Security and logging for research environments
- Resilient environment provisioning and lifecycle management
- Automated validation in deployments

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsrel09-bp04.html*

---

# LSREL09-BP05 Implement risk-based change control for validated systems

Establish a structured, risk-based change control process that
categorizes changes according to their potential impact on product
quality, patient safety, and data integrity. Apply proportional
testing and validation depending on the change classification.
High-risk changes to GxP systems should undergo rigorous
verification and dual review, while low-risk changes may be handled
with streamlined procedures. Track, approve, and document changes,
and update validation evidence to confirm the system remains in a
validated state after the change.

**Desired outcome:** Changes are
assessed, approved, tested, and documented based on risk so that
systems remain reliable and validated.

**Common anti-patterns:**

- Treating each change identically.
- Making undocumented infrastructure changes.
- Failing to demonstrate that the validated state was preserved.

**Benefits of establishing this best
practice:** Maintains continuity of validated research
systems, reduces audit findings, and minimizes the chance of
change-related downtime or data issues.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Risk-based change control should be embedded in governance
processes. Each proposed change should be assessed for potential
impact on regulated workloads. Testing scope and depth must scale
with risk, and approval workflows should reflect that
classification. Documentation should be continuously updated so
there is a clear link between requirements, specifications,
executed tests, and evidence that the validated state was
maintained.

### Implementation steps

- Use AWS Config to track infrastructure changes and maintain
a configuration history.
- Codify infrastructure in AWS CloudFormation with change sets
for controlled, reversible changes.
- Store approvals, validation results, and associated
artifacts in Amazon S3 with Object Lock for immutability.
- Use AWS Audit Manager to map evidence against regulatory
controls and demonstrate ongoing validation.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsrel09-bp05.html*

---

# LSREL09-BP06 Automate validation testing for changes

Develop automated functional and regulatory validation test suites
that run after system changes to verify critical functionality, data
integrity, and regulatory controls. Include tests for audit trails,
access control, and business functionality. These tests should also
reassess resiliency factors like recovery time objectives (RTO) and
recovery point objectives (RPO) to verify that changes do not
degrade reliability targets. Test results should be retained as
evidence in the validation package.

**Desired outcome:** Automated
validation verifies that changes do not compromise functionality,
data integrity, or resiliency, and provides evidence of continued
adherence.

**Common anti-patterns:**

- Relying only on manual testing.
- Skipping regression validation for minor changes.
- Not verifying resiliency requirements after updates.

**Benefits of establishing this best
practice:** Reduces downtime risk, improves
reproducibility, and increases regulator confidence by demonstrating
that every change is validated and reliable.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Validation test suites should be version-controlled and updated as
systems evolve. Automating them improves consistency and reduces
the burden on QA teams. These tests must be integrated into the
deployment pipeline so that every change produces verifiable
evidence of continued system validation. Results should be
reviewed, approved, and archived as part of the change control
record.

### Implementation steps

- Integrate automated validation tests into AWS CodePipeline
so they run after deployments.
- Execute functional tests with containerized workloads on
Amazon ECS/EKS or serverless tests with AWS Lambda.
- Capture logs and results in Amazon CloudWatch Logs and
archive them to Amazon S3 for long-term retention.
- Use AWS Audit Manager to generate audit evidence linking
test execution to change approvals.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsrel09-bp06.html*

---
