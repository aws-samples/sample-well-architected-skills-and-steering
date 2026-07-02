# LSREL13 — Failure management

**Pillar**: Reliability  
**Best Practices**: 3

---

# LSREL13-BP01 Implement comprehensive monitoring for regulated systems

Establish monitoring that spans infrastructure, applications, data
integrity, and audit controls. For GxP systems, verify that your
monitoring covers validation-critical parameters identified in risk
assessments, so that regulated workloads can demonstrate continuous
oversight.

**Desired outcome:**

- Holistic visibility into workload health and reliability.
- Early detection of anomalies across infrastructure and
applications.
- Assurance that monitoring captures validation-critical
parameters in GxP systems.

**Common anti-patterns:**

- Monitoring only infrastructure without application or data-level
coverage.
- Relying on reactive alerts instead of proactive anomaly
detection.
- Lack of defined monitoring scope for regulated workloads.

**Benefits of establishing this best
practice:**

- Enables quick response before failures impact experiments or
studies.
- Provides audit-ready evidence of system oversight for
regulators.
- Improves researcher trust in system stability and availability.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Design monitoring across layers, including infrastructure
(compute, storage, network), application (latency, errors,
throughput), and data integrity. Incorporate health checks aligned
with business priorities. Define thresholds for alerting and
automate incident response workflows. Retain monitoring records in
adherence to retention and audit requirements.

### Implementation steps

- Instrument workloads with Amazon CloudWatch metrics, alarms,
and dashboards.
- Capture logs centrally in Amazon CloudWatch Logs.
- Use AWS X-Ray for distributed tracing of microservices.
- Monitor configuration drift with AWS Config and events with
AWS Security Hub CSPM.
- Store monitoring evidence in Amazon S3 for regulatory
audits.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsrel13-bp01.html*

---

# LSREL13-BP02 Monitor data integrity across scientific processing pipelines

Implement monitoring specifically for data integrity across research
pipelines. Track errors such as checksum mismatches, validation
failures, or audit trail gaps. For scientific domains like genomics
or clinical processing, add plausibility checks to detect
biologically impossible or outlier results that may signal workflow
errors.

**Desired outcome:**

- Early detection of data corruption or processing errors.
- Continuous assurance of data accuracy, completeness, and
traceability.
- Adherence to data integrity expectations for regulated research.

**Common anti-patterns:**

- Only validating data at ingestion or final outputs, not during
processing.
- Ignoring intermediate pipeline results when monitoring for
errors.
- Not capturing or preserving logs for data validation failures.

**Benefits of establishing this best
practice:**

- Protects reproducibility by keeping datasets accurate across
processing steps.
- Reduces wasted compute from propagating corrupted or invalid
data.
- Strengthens audit confidence through consistent integrity
checks.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Incorporate integrity checks throughout pipelines. Validate the
following during this process:

- File checksums
- Schema conformance
- Expected data patterns

Retain metadata and logs for traceability. Define biologically
relevant plausibility thresholds (for example, variant frequencies
or image metrics) to detect anomalies early. Integrate alerts with
workflow orchestration so that failed steps are isolated.

### Implementation steps

- Validate file integrity with Amazon S3 ETag checks or
checksum verification jobs in AWS Lambda.
- Store audit trails in Amazon DynamoDB or Amazon S3.
- Use AWS Glue DataBrew or AWS Data Quality rules for schema
and value checks.
- Implement plausibility validations in genomics workflows
through AWS HealthOmics Workflows.
- Route alerts through Amazon EventBridge into incident
response pipelines.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsrel13-bp02.html*

---

# LSREL13-BP03 Track reliability metrics aligned to regulatory needs

Define and monitor reliability metrics that align with both
operational resilience and regulatory requirements. For
GxP-regulated systems, include system availability, backup/restore
success, recovery test completion, and data integrity checks. Retain
metric history for audit evidence.

**Desired outcome:**

- Clear visibility into workload reliability health.
- Metrics aligned with both business SLAs and regulatory
expectations.
- Historical reporting available for audits and inspections.

**Common anti-patterns:**

- Collecting technical metrics without mapping to regulatory
requirements.
- Not retaining monitoring data for required regulatory periods.
- No baselines to measure whether reliability is improving or
degrading.

**Benefits of establishing this best
practice:**

- Provides measurable evidence of system reliability for
regulators and auditors.
- Builds trust with researchers and clinical teams in system
performance.
- Supports proactive investment in reliability improvements based
on trends.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Define metrics in collaboration with QA, governance, and IT teams.
Track technical indicators (uptime, error rates, and RTO and RPO
adherence) alongside compliance-related ones (backup success,
recovery validation, and audit trail completeness). Retain
reliability data in tamper-evident storage for required retention
periods. Review metrics periodically to drive improvement.

### Implementation steps

- Collect uptime and error metrics using Amazon CloudWatch and
log retention policies.
- Monitor backup success using AWS Backup Audit Manager.
- Track recovery validation evidence in AWS Audit Manager.
- Store metric histories in Amazon S3 with Object Lock for
immutability.
- Build dashboards using Quick for regulators and
QA stakeholders.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsrel13-bp03.html*

---
