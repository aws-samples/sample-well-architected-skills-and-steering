# LSREL10 — Change nanagement

**Pillar**: Reliability  
**Best Practices**: 3

---

# LSREL10-BP01 Implement comprehensive reliability testing

Develop structured protocols that test reliability aspects including
load performance, failover, recovery, and long-term stability. For
regulated systems, include reliability tests in the validation
package with traceability to user and regulatory requirements. Use
controlled chaos engineering experiments to validate resilience by
safely injecting faults and failures into your applications while
preserving data integrity and adherence.

**Desired outcome:**

- Reliability tests are systematic, repeatable, and documented.
- Systems demonstrate resilience to failure injection and load
stress.
- Test evidence supports regulatory validation requirements.

**Common anti-patterns:**

- Treating reliability tests as optional instead of mandatory.
- Running only idealized tests without simulating failures.
- Lack of traceability between reliability test cases and
regulatory or user requirements.

**Benefits of establishing this best
practice:**

- Improves predictability of experiments and workloads under
stress.
- Builds regulator and auditor confidence in system resilience.
- Reduces costly delays by uncovering reliability gaps early.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Define reliability acceptance criteria in line with user and
regulatory requirements.

Incorporate resilience tests into validation and qualification
protocols.

Perform controlled chaos experiments to uncover weaknesses safely.

Automate reliability testing where possible for repeatability.

### Implementation steps

- Run fault-injection experiments with AWS Fault Injection Service (FIS).
- Use AWS CodePipeline to integrate reliability tests into
CI/CD.
- Capture test logs in Amazon CloudWatch Logs and archive
evidence in Amazon S3 Object Lock for regulatory adherence.
- Document test execution and results in AWS Audit Manager.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsrel10-bp01.html*

---

# LSREL10-BP02 Validate end-to-end reliability of regulated workloads

Conduct end-to-end reliability validation exercises that test not
just recovery but the overall system's ability to maintain adherence
and functionality during adverse events. These tests should validate
high availability, monitoring alerts, automated failover, and
controls in production-like scenarios.

**Desired outcome:**

- Holistic system reliability validated under real-world
conditions.
- Compliance-aligned functions (audit trails, access controls,
data integrity) remain intact during adverse events.
- Test outcomes provide documented evidence for regulatory audits.

**Common anti-patterns:**

- Focusing only on technical recovery while ignoring controls.
- Testing components in isolation but never validating the
end-to-end system.
- No evidence of reliability testing available for auditors.

**Benefits of establishing this best
practice:**

- Demonstrates system resilience across full workflows, not just
components.
- Strengthens audit readiness with comprehensive reliability
evidence.
- Reduces operational risk by validating reliability before real
incidents occur.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Plan integrated reliability tests across application and data
layers.

Simulate production-like workloads during validation.

Validate not only failover and monitoring but also regulatory
controls.

Store test artifacts centrally with immutable retention.

### Implementation steps

- Use AWS Elastic Load Balancing with Auto Scaling to validate
failover.
- Run simulated production workloads using AWS Batch or Amazon ECS.
- Trigger alerts through Amazon CloudWatch Alarms and verify
monitoring in AWS Config.
- Archive reliability validation evidence in Amazon Glacier
for long-term retention.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsrel10-bp02.html*

---

# LSREL10-BP03 Test data integrity under failure conditions

Design and execute specific tests to validate that data integrity is
preserved during system failures, network outages, or recovery
processes. For workloads involving trial data, manufacturing
records, or patient datasets, enforce transactional boundaries, roll
back partial updates safely, and block corrupted data from entering
downstream systems.

**Desired outcome:**

- Data integrity maintained during failures and recovery.
- Tests confirm correct handling of partial transactions and error
scenarios.
- Evidence demonstrates adherence to data integrity requirements.

**Common anti-patterns:**

- Relying on functional tests without failure/integrity
validation.
- No rollback or compensation testing for partial failures.
- Assuming backups restore consistent datasets without testing.

**Benefits of establishing this best
practice:**

- Protects against corrupted datasets invalidating scientific
outcomes.
- Builds trust in data reproducibility and traceability for
regulators.
- Avoids costly reruns of experiments or trials due to data loss.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Incorporate integrity validation into test plans for recovery and
failover.

Test for both transient disruptions and long-term outages.

Use domain-specific integrity checks for genomic, clinical, or
manufacturing datasets.

### Implementation steps

- Enable Amazon RDS point-in-time recovery and validate
consistency after restore.
- Run AWS Glue Data Quality jobs to verify schema and record
consistency.
- Store validation reports in Amazon S3 with Object Lock for
immutability.
- Integrate validation results into reports with AWS Audit
Manager.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsrel10-bp03.html*

---
