# LSREL12 — Failure management

**Pillar**: Reliability  
**Best Practices**: 4

---

# LSREL12-BP01 Implement recovery processes with data integrity verification

Design recovery procedures with explicit steps to verify data
integrity once recovery operations complete. For regulated life
sciences workloads, include checksums, reconciliation processes, or
dual-control verification. Verification evidence should be
documented as part of disaster recovery and audit processes.

**Desired outcome:**

- Recovered datasets are validated for completeness and accuracy.
- Data integrity verification is automated where possible.
- Audit evidence of verification steps is retained for
compliance-related purposes.

**Common anti-patterns:**

- Recovery plans restore services without validating data
correctness.
- Assuming backups are correct without performing validation
checks.
- No retention of verification evidence for audit purposes.

**Benefits of establishing this best
practice:**

- Avoids propagation of corrupted or incomplete data into research
workflows.
- Provides regulators confidence that scientific data is accurate
after recovery.
- Reduces risk of invalid conclusions or repeated experiments.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Define recovery procedures that integrate integrity checks,
including checksum validation, record counts, and cross-system
reconciliation. Automate as much as possible to reduce manual
errors, and document the results. For GxP workloads, require dual
sign-offs for verification evidence. Retain logs and reports as
part of change and recovery records.

### Implementation steps

- After recovery, run checksum verification jobs with AWS Lambda across restored datasets in Amazon S3.
- Use AWS Glue or AWS DataBrew to validate schema and record
counts.
- Store verification logs in Amazon S3 with Object Lock for
immutability.
- Integrate verification results into audit tracking using AWS
Audit Manager.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsrel12-bp01.html*

---

# LSREL12-BP02 Define recovery time objectives based on scientific and business impact

Recovery time objectives (RTOs) should be established through
analysis of the scientific and business impact of downtime. For
clinical trial systems, delays may affect patient safety or data
collection. For manufacturing or analytical systems, downtime may
disrupt schedules, supply chains, or data reproducibility. RTOs must
be documented and justified in continuity planning.

**Desired outcome:**

- Recovery time targets reflect business and scientific
criticality.
- Downtime risks are balanced against cost of recovery
capabilities.
- RTOs are documented and approved as part of continuity planning.

**Common anti-patterns:**

- Arbitrary RTOs set without input from science or operations
stakeholders.
- Uniform recovery targets across systems.
- Failure to periodically review RTOs as workloads evolve.

**Benefits of establishing this best
practice:**

- Verifies that critical research and clinical activities resume
within acceptable windows.
- Avoids over-investment in low-priority systems while
safeguarding high-value workloads.
- Builds alignment between IT, R&D, QA, and business
stakeholders.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Conduct impact analyses for each workload, identifying scientific,
regulatory, and operational consequences of downtime. Define
system-specific RTOs based on these findings and align them with
acceptable risk tolerances. Document RTOs in continuity and
disaster recovery plans, and review them regularly to keep them
appropriate as workloads scale.

### Implementation steps

- Use AWS Well-Architected Resilience Hub to document RTO
targets for workloads.
- Configure Amazon RDS Multi-AZ for critical databases to meet
short RTOs, while less critical workloads can use Amazon Glacier for slower recovery.
- Run recovery drills using AWS Elastic Disaster Recovery
(DRS) to validate RTO adherence.
- Record results in AWS Audit Manager for tracking.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsrel12-bp02.html*

---

# LSREL12-BP03 Maintain data consistency in distributed research systems

Distributed life sciences workloads (for example, spanning multiple
sites, cloud Regions, or CRO integrations) require mechanisms to
maintain data consistency during partial failures and recovery. This
includes distributed transactions, compensating actions, and
reconciliation processes to improve accuracy and completeness across
system components.

**Desired outcome:**

- Data remains accurate and consistent across distributed
components after recovery.
- Conflicts or anomalies are detected and resolved automatically
where possible.
- Reconciliation evidence is preserved for audit and
reproducibility.

**Common anti-patterns:**

- No reconciliation of data between distributed systems after
recovery.
- Assuming eventual consistency will resolve discrepancies without
validation.
- Ignoring data mismatches introduced during failover or partial
recovery.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

For distributed systems, design recovery processes that reconcile
states across components. This may involve compensating
transactions, replaying messages, or performing checksum-based
reconciliation. Where eventual consistency is used, implement
monitoring and exception handling to identify unreconciled
discrepancies. Document reconciliation processes in DR runbooks.

### Implementation steps

- Use Amazon DynamoDB global tables or Amazon Aurora Global
Database to maintain multi-region consistency.
- For asynchronous pipelines, implement reconciliation jobs
using AWS Step Functions and AWS Lambda to compare datasets
across Regions.
- Capture anomalies in Amazon CloudWatch Logs and route issues
into incident workflows through Amazon EventBridge.
- Retain reconciliation evidence in Amazon S3 for
compliance-related purposes.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsrel12-bp03.html*

---

# LSREL12-BP04 Implement cyber resilience for GxP-regulated backup data

Implement cyber resilience strategies for your backup data to
protect against ransomware and other cyber threats, with specific
considerations for GxP-regulated systems. Cyber resilience goes
beyond traditional backup approaches by keeping backups immutable,
isolated, and recoverable even during sophisticated cyber attacks
while maintaining data integrity in accordance with ALCOA+
principles.

**Desired outcome:** A robust backup
strategy that protects GxP-regulated data from cyber threats, which
recovers clean, unaltered data following an attack while maintaining
regulatory adherence and data integrity.

**Common anti-patterns:**

- Relying solely on encryption without implementing immutability,
leaving GxP data backups vulnerable to deletion.
- Using the same security domain for production and backup
systems, allowing credential compromise to affect both
environments.
- Assuming backups are valid without regular validation testing,
potentially discovering issues only during actual recovery.
- Allowing single-person authorization for critical recovery
operations, reducing segregation of duties required for
regulated systems.
- Failing to document backup immutability controls as part of the
quality management system.

**Benefits of establishing this best
practice:**

- Enhanced protection against ransomware and other cyber threats
that specifically target backup infrastructure.
- Maintained data integrity for GxP-regulated information during
recovery.
- Improved confidence in recovery capabilities during security
incidents.
- Enhanced adherence to regulatory requirements for data
protection and recovery.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Traditional backup approaches for GxP systems focus on data
availability and integrity but may not adequately address
sophisticated cyber threats that specifically target backup
infrastructure. Life sciences organizations must implement
cyber-resilient backup strategies that maintain regulatory
adherence while protecting against evolving threats.

Implement a comprehensive cyber resilience strategy for your
GxP-regulated backups that includes four fundamental pillars:

- **Immutability:** Stop backup
data from being altered or deleted during its retention
period, maintaining the ALCOA+ principle of originality
- **Logical isolation:** Separate
backup storage from production environments with distinct
security controls to avoid compromise of both systems
- **Integrity validation:**
Regularly verify backup data remains uncorrupted and can be
successfully restored, improving ongoing adherence to data
integrity requirements
- **Access controls:** Implement
multi-party approval for critical recovery operations to
maintain appropriate segregation of duties for regulated
systems

For GxP-regulated systems, document your cyber-resilient backup
strategy within your quality management system, including
validation of backup immutability controls and recovery processes.
This documentation should address how your backup strategy adheres
data integrity requirements and should be sufficient to
demonstrate regulatory adherence during inspections or audits.

### Implementation steps

- Assess your GxP backup strategy for cyber resilience gaps:

- Evaluate current backup solutions for immutability
capabilities and potential vulnerabilities.
- Identify potential attack vectors that could compromise both
production and backup systems.
- Determine appropriate retention periods based on data
criticality, regulatory requirements, and threat models.
- Document recovery time objectives (RTOs) and recovery point
objectives (RPOs) for cyber recovery scenarios.
- Classify backup data based on GxP relevance and criticality.

- Implement immutable backup storage for GxP data:

- Configure AWS Backup Vault Lock or S3 Object Lock for GxP
data with appropriate retention periods.
- Define immutability settings based on data classification
and regulatory requirements.
- Implement technical controls to avoid override of
immutability settings.
- Document immutability configurations in your data protection
policies and Quality Management System.
- Test immutability by attempting to delete or modify
protected backups.

- Establish logical isolation for GxP backup storage:

- Create dedicated AWS accounts for GxP backup storage with
separate administrative controls.
- Implement AWS Backup logically air-gapped vault for critical
GxP systems requiring enhanced protection.
- Configure strict cross-account access controls using IAM and
service control policies (SCPs).
- Establish network isolation between production and backup
environments.
- Implement separate authentication mechanisms for backup
administration.
- Document isolation controls in your Quality Management
System.

- Implement multi-party approval for GxP system recovery:

- Configure AWS Backup multi-party approval workflows for GxP
systems.
- Define approver roles and responsibilities with appropriate
separation of duties.
- Document escalation procedures for emergency scenarios
requiring expedited recovery.
- Implement comprehensive audit trails for approval actions.
- Align your approval workflows with your quality management
system requirements.
- Regularly test approval workflows to verify effectiveness
during actual incidents.

- Validate GxP backup integrity and recovery processes:

- Implement AWS Backup restore testing with automated
validation of restored resources.
- Schedule regular recovery exercises in isolated environments
for critical GxP systems.
- Document validation procedures and success criteria for
different resource types.
- Test recovery from various cyber attack scenarios including
ransomware and data corruption.
- Validate data integrity after restoration to improve
consistency and completeness.
- Maintain validation documentation as part of your quality
management system.

- Monitor and audit GxP backup protection:

- Configure AWS CloudTrail logging for backup and recovery
operations.
- Implement Amazon CloudWatch alarms for unauthorized access
attempts or policy violations.
- Regularly review backup protection controls through
automated checks.
- Conduct periodic security assessments of backup
infrastructure.
- Maintain comprehensive documentation of cyber resilience
controls for audits and regulatory inspections.

## Resources

**Related best practices:**

- LSREL13-BP01
- LSOPS03-BP01

**Related documents:**

- [GxP
Systems on AWS](https://docs.aws.amazon.com/whitepapers/latest/gxp-systems-on-aws/gxp-systems-on-aws.html)
- [Building
cyber resiliency with AWS Backup logically air-gapped
vault](https://aws.amazon.com/blogs/storage/building-cyber-resiliency-with-aws-backup-logically-air-gapped-vault/)
- [Validate
recovery readiness with AWS Backup restore testing](https://aws.amazon.com/blogs/storage/validate-recovery-readiness-with-aws-backup-restore-testing/)
- [Ransomware
Risk Management on AWS Using the NIST Cyber Security
Framework](https://docs.aws.amazon.com/whitepapers/latest/ransomware-risk-management-on-aws-using-nist-csf/ransomware-risk-management-on-aws-using-nist-csf.html)

**Related examples:**

- [Building
cyber resiliency with AWS Backup logically air-gapped
vault](https://aws.amazon.com/blogs/storage/building-cyber-resiliency-with-aws-backup-logically-air-gapped-vault/)
- [Validate
recovery readiness with AWS Backup restore testing](https://aws.amazon.com/blogs/storage/validate-recovery-readiness-with-aws-backup-restore-testing/)
- [Improve
recovery resilience with AWS Backup support for Multi-party
approval](https://aws.amazon.com/blogs/storage/improve-recovery-resilience-with-aws-backup-support-for-multi-party-approval/)

**Related tools:**

- AWS Backup
- AWS Backup Vault Lock
- Amazon S3 Object Lock
- AWS CloudTrail
- Amazon CloudWatch
- AWS IAM

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsrel12-bp04.html*

---
