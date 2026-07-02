# LSREL08 — Workload architecture

**Pillar**: Reliability  
**Best Practices**: 3

---

# LSREL08-BP01 Incorporate validated redundancy into architecture design

During the design phase, plan for redundancy across fault-isolated
zones and validate that each component meets regulatory
requirements. Qualification of secondary systems should not be an
afterthought but part of the original architecture plan. Document
design decisions to show how redundancy supports both technical
reliability and regulatory obligations.

**Desired outcome:** Workloads remain
available during component failures, and redundant systems are
equally validated for adherence.

**Common anti-patterns:**

- Treating secondary systems as non-validated backups rather than
qualified components.
- Adding redundancy late in design, creating gaps.
- Documenting only the primary system in validation records.

**Benefits of establishing this best
practice:** Improves confidence in availability without
compromising regulatory expectations. Provides reproducible
architectural evidence for audits.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

When planning workload architecture, design for multi-zone
redundancy from the start. Your validation protocols should
explicitly include redundant components, not just primaries. For
each architecture diagram and system description, demonstrate that
redundant paths preserve the same adherence controls, including
data capture and security safeguards. Qualification evidence
should reflect the entire redundant system architecture as
validated.

### Implementation steps

- Define multi-AZ or multi-Region designs in your architecture
blueprints and validate them in qualification testing.
- Document redundancy plans in your system design
specifications and standard operating procedures.
- Use AWS services such as Amazon RDS Multi-AZ, Amazon S3
cross-region replication, or Elastic Load Balancing across
multiple Availability Zones, verifying that validation
records include both primary and redundant configurations.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsrel08-bp01.html*

---

# LSREL08-BP02 Design compliance-aware failover workflows

Architect failover mechanisms that explicitly maintain critical
functions such as authentication, audit logging, and data
validation. During the planning phase, map how these functions
transition across components and zones, and include them in system
qualification protocols.

**Desired outcome:** Failover
processes preserve your regulatory state and do not bypass required
controls.

**Common anti-patterns:**

- Assuming failover preserves compliance-aligned workflows without
testing.
- Not qualifying the secondary environment.
- Logging or audit trails that break during transition.

**Benefits of establishing this best
practice:** Maintains trust with regulators and reduces
deviations during outages.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Plan failover mechanisms alongside your core architecture,
treating them as integral rather than auxiliary processes. Map how
functions such as authentication, authorization, encryption, and
audit logging persist across failover scenarios. Include these
workflows in risk assessments and validation test plans to verify
that they behave consistently under failover conditions.

### Implementation steps

- Document failover workflows in architecture specifications
and validate them with test evidence.
- Use AWS managed services to design automated failover with
Amazon Route 53 health checks, Amazon RDS Multi-AZ failover,
or Auto Scaling group replacements.
- Keep AWS CloudTrail, AWS Config, and Amazon CloudWatch
monitoring active during failover, and include these checks
in validation evidence to demonstrate persistence.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsrel08-bp02.html*

---

# LSREL08-BP03 Align architecture priorities with scientific and regulatory context

Early in the design cycle, evaluate the scientific and regulatory
priorities of each workload. In patient-facing clinical workloads,
design for continuous availability with reconciliation workflows. In
regulated manufacturing, prioritize data integrity in the
architecture, even if this limits availability. Planning with these
priorities in mind avoids trade-off surprises later.

**Desired outcome:** Availability
trade-offs are consciously designed to meet workload-specific
requirements.

**Common anti-patterns:**

- Treating each workload with a uniform HA design.
- Prioritizing availability at the cost of data integrity in
regulated processes.
- Failing to document the rationale for architectural trade-offs.

**Benefits of establishing this best
practice:** Aligns architectures with the unique regulatory
and scientific priorities of each workload, and improves
transparency in audits.

## Implementation guidance

Architectural planning should explicitly evaluate the workload's
scientific and regulatory context before finalizing availability
and failover mechanisms. For example, clinical trial systems may
tolerate some reconciliation steps post-recovery if availability
is critical, while batch manufacturing systems may require
uncompromising data integrity even if it reduces availability.
Document these trade-offs, rationale, and validation approach as
part of the design package.

### Implementation steps

- Capture availability and data integrity requirements in
system requirements specifications and risk assessments.
- Map RTO and RPO targets to these requirements.
- On AWS, implement availability features with services like
Amazon Aurora Multi-AZ or Amazon S3 Versioning, paired with
validation steps for data integrity.
- Store architecture trade-off documentation and validation
outcomes in a controlled repository for audit readiness.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsrel08-bp03.html*

---
