# Reliability

**Pillar**: Reliability  
**Questions**: 13

---

# LSREL01 — Foundations

**Pillar**: Reliability  
**Best Practices**: 2

---

# LSREL01-BP01 Identify and protect sensitive data elements with auditable classification.

Conduct a systematic analysis to identify sensitive data elements
(like PHI, identifiers, and lab results), establish classification
standards, and map business processes that generate or consume them.
Define which data should be anonymized, irreversibly de-identified,
or remain re-identifiable to support authorized patient re-linking
after research.

**Desired outcome:** The complete
dataset will be accessible to a broader group of individuals and
organizations. However, access to individual data elements will be
restricted to only those with the necessary permissions.

**Common anti-patterns:**

- Encrypting each data element.
- No or incorrect data classification.
- Incorrect classification of de-identify data element.

**Benefits of establishing this best
practice:**

- Enables broader data sharing and secondary analysis while
preserving trust, meeting regulatory requirements.
- Fosters a culture of trust and appropriate data handling.
- Verifies that anonymization procedures correspond effectively
with legal requirements and organizational goals through
collaborative effort among technical, legal, and governance
teams.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Consider Amazon SageMaker AI Unified Studio and AWS Lake Formation
for a unified view of data sources and consumers. This combination
of services assists you to centrally govern, secure, and globally
share data for analytics and machine learning. With AWS Lake Formation, you can enforce fine-grained access control for your
data at row, column, and cell level. This centralized access
control mechanism reduces the risk of configuration errors and
consistently enforces policies across your data access patterns,
improving the reliability of your data governance.

Use AWS Key Management Service (KMS) to securely manage and audit
encryption keys during the lifecycle of life science data like
genomics or bioscience research data. Implement automatic key
rotation and use AWS CloudTrail integration for full traceability
and recovery assurance. Forward CloudTrail logs to a dedicated
account for log integrity and to avoid tampering, supporting
reliable audit trails for regulatory verification. This provides a
resilient and highly available key management system that
consistently encrypts and decrypts data even during Regional
failover or transient service issues.

Store classification manifests (including dataset UUID, sensitive
field mappings, classification levels, and SHA-256 digests) in
Amazon S3 with S3 Object Lock enabled. This makes your
classification records immutable, stopping accidental or malicious
deletion and providing a reliable audit trail for
compliance-related and recovery scenarios. Configure appropriate
retention periods based on regulatory requirements.

### Implementation steps

- Identify and inventory the data sources that generate or
capture sensitive data elements, and use AWS AWS Glue Data Catalog as a centralized metadata repository. Use Amazon Macie to automatically discover and classify sensitive data
elements, reducing manual classification errors and
improving consistency across datasets. Add custom attributes
in the Data Catalog to indicate if a data element requires
de-identification, irreversible anonymization, or
encryption. Automate this discovery and classification
process to maintain accuracy as data elements are added,
updated, or removed across systems.
- Make decision which data elements to secure and protect in
system of record. Consider using AWS KMS for creating and
controlling encryption keys to protect data across systems.
Consider using AWS CloudTrail for audit trail what keys are
used by who, when, and on which data elements.
- Consider providing a scalable decryption function or API to
reverse data based on role and permissions at data-domain,
row, column, or cell level.

## Resources

**Related best practices:**

- Encrypting data at rest and in transit.
- Copies of data with or without sensitive data based on need.
- Removing sensitive data for downstream systems and relying on
source systems to make sure data is reverse traceable with
primary keys.
- Adding features to source systems to avoid data egress even
within the organization.

**Related documents:**

- [Guidance
for Data Anonymization on AWS](https://aws.amazon.com/solutions/guidance/data-anonymization-on-aws/)

**Related tools:**

- [Amazon Macie](https://aws.amazon.com/macie/)
- [Amazon SageMaker AI Unified Studio](https://aws.amazon.com/sagemaker/unified-studio/)
- [AWS Lake Formation](https://aws.amazon.com/lake-formation/)
- [AWS Key Management Service](https://aws.amazon.com/kms/)
- [AWS CloudTrail](https://aws.amazon.com/cloudtrail/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsrel01-bp01..html*

---

# LSREL01-BP02 Decouple anonymization logic from core workflows using orchestration and versioning.

Implement data anonymization as a modular, orchestrated workflow
with support for AI-based or rule-based anonymization. Store
intermediate data in secure, versioned storage to enable rollback,
reproducibility, and auditability, verifying that sensitive data
handling aligns with life sciences regulatory and research
requirements.

**Desired outcome:** A modular system
architecture where anonymization processes operate independently of
core application logic, allowing for better scalability, simple
maintenance, and improved reliability. The system maintains data
lineage and provides rollback capabilities for reproducibility for
scientific and regulatory purposes.

**Benefits of establishing this best
practice:**

- Improves system resilience by isolating failures in the
anonymization process.
- Enables independent scaling of anonymization resources based on
workload.
- Provides audit trail and reproducibility for regulatory
adherence.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Decouple anonymization logic from core application workflows by
implementing it as an independent, orchestrated process. Use AWS Step Functions to define anonymization workflows as state machines
with distinct stages for data ingestion, validation,
transformation (rule-based or AI-based), quality verification, and
output generation. This separation allows the anonymization
process to scale independently, fail gracefully without impacting
core systems, and be updated or rolled back without touching
production application code.

For rule-based anonymization (like deterministic masking,
tokenization, and generalization), implement transformation logic
in AWS Lambda functions that can be versioned and tested
independently. For AI-based anonymization (like context-aware
redaction and synthetic data generation), deploy models as Amazon SageMaker AI endpoints that can be updated independently of the
orchestration layer. Use Amazon EventBridge to trigger workflows
based on data arrival events or scheduled intervals, maintaining
loose coupling between data producers and anonymization consumers.

Store intermediate transformation manifests in Amazon S3 with
versioning enabled to create an immutable audit trail of
anonymization operations. Each manifest should capture the
complete context of a transformation: input data digest (SHA-256),
transformation version identifier, operator ID, timestamp,
anonymization parameters, and output data location. Enable S3
Object Lock in compliance mode with retention periods aligned to
regulatory requirements. This manifest-based approach enables
reproducibility allowing you to re-run historical anonymization
with the exact same logic and parameters—and supports rollback by
maintaining references to both original and transformed data
states.

### Implementation steps

- Create Step Functions state machines for anonymization
workflows with Lambda functions for rule-based logic or
SageMaker AI endpoints for AI-based models. Configure
EventBridge rules to trigger workflows on data arrival or
schedule.
- Store transformation manifests in S3 with versioning and
Object Lock enabled. Include input digest, transform
version, operator ID, timestamp, and parameters in each
manifest.
- Version anonymization logic in Git repositories and store
model artifacts in S3 with versioning enabled. Tag Lambda
function versions and SageMaker AI model artifacts with
semantic versioning and link to transformation manifests for
reproducibility.
- Configure CloudWatch Logs, CloudTrail, and X-Ray for
workflow monitoring. Set up alarms for failures, duration
anomalies, and data quality metrics.

## Resources

**Related best practices:**

- Monitoring and observability for data transformation workflows
- Data lineage and provenance tracking for regulatory adherence
- Automated testing and validation of anonymization quality

**Related guides, videos, and
documentation:**

- [Guidance
for Data Anonymization on AWS](https://aws.amazon.com/solutions/guidance/data-anonymization-on-aws/)
- [AWS Step Functions Developer Guide](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html)

**Related tools:**

- [AWS Step Functions](https://aws.amazon.com/step-functions/)
- [AWS Lambda](https://aws.amazon.com/lambda/)
- [Amazon SageMaker AI](https://aws.amazon.com/sagemaker/)
- [Amazon S3](https://aws.amazon.com/s3/)
- [Amazon EventBridge](https://aws.amazon.com/eventbridge/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
- [AWS CloudTrail](https://aws.amazon.com/cloudtrail/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsrel01-bp02..html*

---

# LSREL02 — Foundations

**Pillar**: Reliability  
**Best Practices**: 2

---

# LSREL02-BP01 Build resilient and highly available research solutions

Design research systems using fault-isolated, redundant deployment
patterns that allow continuous access during maintenance or
localized outages. Use highly available configurations where
near-zero downtime is required (for example, ELNs) and
active-passive designs with automated failover for systems with less
stringent latency or availability needs (for example, LIMS).

**Desired outcome:**

- Research systems remain available during maintenance or outages.
- Ongoing experiments and data collection continue without
interruption.
- Researchers have a consistent experience across sites and
geographies.

**Common anti-patterns:**

- Relying on single-instance deployments for critical systems.
- Maintenance performed without phased rollouts or rollback plans.
- Highly available architectures implemented without routine
failover testing.

**Benefits of establishing this best
practice:**

- Protects ongoing experiments from interruption, reducing risk of
wasted samples or time.
- Preserves continuity in multi-day or multi-week lab workflows.
- Provides global research teams access to shared tools without
productivity loss.
- Enhances regulatory readiness by reducing gaps in system
availability records.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

When designing research workloads for resiliency, use deployment
topologies that minimize the scope of impact of maintenance and
outage events. Multi-site or multi–AZ deployments allow for
uninterrupted operation when a system component is taken offline.
Automated health checks and intelligent traffic routing directs
users to healthy endpoints, maintaining continuity during upgrades
or failover scenarios. Maintenance windows should be orchestrated
to minimize user disruption, and resilience should be validated
regularly through simulated failovers or planned game days.

### Implementation steps

- Deploy AWS IoT Greengrass for local buffering of instrument
data.
- Deploy LIMS, EHR and ELN solutions across multiple
Availability Zones using Amazon EC2 Auto Scaling for
workload redundancy.
- Place applications behind an Elastic Load Balancer (ALB or
NLB) to support highly available deployment configurations,
or configure Amazon Route 53 DNS failover with health checks
for active-passive failover strategies.
- Use AWS Systems Manager to coordinate upgrades with minimal
disruption. Monitor resilience, health status, and failover
events in Amazon CloudWatch, and validate readiness with
regular failover exercises.

## Resources

**Related best practices:**

- Change management and controlled rollout strategies
- Incident response playbooks for scientific research systems
- Risk-based classification of R&D applications

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsrel02-bp01.html*

---

# LSREL02-BP02 Maintain continuous data availability and integrity

Implement real-time or near-real-time data replication strategies
across Availability Zones or AWS Regions to protect against system
failures or maintenance interruptions. Use warm standby environments
with synchronized datasets to enable quick failover and avoid data
loss or research disruption.

**Desired outcome:**

- Continuous data access during maintenance and outages.
- Minimal risk of data loss or corruption across failure events.
- Trust in the accuracy, completeness, and reproducibility of
research datasets.

**Common anti-patterns:**

- Relying on manual backups without automated validation or
recovery testing.
- Replicating data without maintaining consistency or integrity
verification.
- Treating replication as optional for intermediate or temporary
data sources unless cost/time-effective to reproduce.

**Benefits of establishing this best
practice:**

- Enables uninterrupted access to experimental results and
research datasets.
- Reduces risk of losing critical data from unique or costly
experiments.
- Supports reproducibility and regulatory adherence (like audit
trails and traceability).
- Strengthens collaboration by making shared datasets available
globally.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Data availability must be preserved even when system components
undergo maintenance or fail unexpectedly. Structured research
data, such as LIMS transactions, should use multi-zone replication
to maintain availability, while unstructured research datasets
should be replicated across independent storage domains.
Monitoring replication lag and validating dataset consistency are
critical to avoid silent data corruption. Automated recovery
validation and regular restore drills build trust that data can be
recovered accurately and within defined RPO and RTO objectives.

### Implementation steps

- Configure Amazon RDS Multi-AZ deployments for LIMS databases
to achieve transactional durability.
- Use Amazon S3 Cross-Region Replication (CRR) for
uninterrupted access to critical datasets, and protect
large-scale file-based research workloads with Amazon FSx for Lustre combined with snapshot policies managed by AWS Backup.
- Define automated recovery validation policies in AWS Backup
for audit tracking.
- Continuously monitor replication lag and recovery objectives
through Amazon CloudWatch, aligning recovery metrics with
the needs of research workflows.

## Resources

**Related best practices:**

- Data lifecycle management for research datasets
- Data integrity and reproducibility controls
- Governance documentation for GxP-relevant systems

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsrel02-bp02.html*

---

# LSREL03 — Foundations

**Pillar**: Reliability  
**Best Practices**: 2

---

# LSREL03-BP01 Digitize and modernize archival of research data

Replace legacy storage formats such as tapes, optical disks, or
local hard drives with digital storage strategies that provide
redundancy, immutability, and verifiable integrity. Centralized
digital archives keep data accessible, protected from degradation,
and adhere to long-term retention requirements.

**Desired outcome:**

- Research and clinical data remains intact and accessible for
extended periods.
- Immutable archives block tampering or accidental deletion.
- Metadata supports efficient search and retrieval for audits or
scientific review.

**Common anti-patterns:**

- Relying on physical tapes or local servers with no periodic
validation.
- Storing critical data without metadata, making retrieval
inefficient.
- Keeping data in non-standard formats that hinder long-term
usability.

**Benefits of establishing this best
practice:**

- Improved durability and accessibility compared to physical
archives.
- Reduced operational costs and manual overhead of physical
storage.
- Simplified adherence to regulatory audits through traceable,
verifiable archives.
- Supports reproducibility by keeping datasets intact and usable
over decades.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Long-term storage strategies should prioritize immutability and
regulatory alignment. Establish centralized digital archives with
policies that enforce retention and stop premature deletion.
Periodically validate archived datasets with integrity checks and
maintain metadata to verify that datasets are searchable and
contextualized. Migrating legacy media into durable repositories
reduces the risk of data degradation and provides consistent
access across global research teams.

### Implementation steps

- Digitize and migrate legacy media into Amazon S3 with Object
Lock to enforce immutability.
- Use Amazon Glacier Vault Lock to apply retention rules.
- Migrate large historical datasets efficiently with AWS
DataSync.
- Schedule automated integrity checks with Amazon S3 Inventory
and log validation results into AWS Audit Manager for audit
tracking.
- Maintain searchable metadata indexes using Amazon DynamoDB
or Amazon OpenSearch Service to enable rapid dataset
retrieval during audits or scientific reviews.

## Resources

**Related best practices:**

- Data integrity validation for regulatory adherence
- Metadata management and data cataloging
- Lifecycle management policies for long-term research data

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsrel03-bp01.html*

---

# LSREL03-BP02 Implement tiered storage and recovery strategies

Adopt a tiered approach to storage and retrieval, balancing cost,
durability, and recovery speed. Critical research datasets should be
stored in durable, retrievable formats, while less frequently
accessed archives can be stored in lower-cost, long-term archival
tiers.

**Desired outcome:**

- Cost-effective storage of large volumes of research data.
- Ability to retrieve datasets reliably within regulatory or
operational timelines.
- Long-term durability and reproducibility for clinical trial and
research data.

**Common anti-patterns:**

- Treating each dataset equally, leading to unnecessary costs or
slow recovery.
- Archiving data without defining retrieval timelines or
compliance-related needs.
- Failing to test retrieval procedures, risking failed restores
during audits.

**Benefits of establishing this best
practice:**

- Reduces storage costs without sacrificing durability.
- Provides scalable recovery aligned with business and
compliance-related needs.
- Improved preparation for regulatory audits or re-analysis of
research and clinical data.
- Supports sustainable scaling of data management as volumes grow
exponentially.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Classify datasets by criticality, regulatory requirements, and
access frequency. Assign storage tiers accordingly, with active
datasets kept on performant storage and archival datasets
transitioned to lower-cost tiers. Lifecycle automation reduces
human error and improves adherence to retention schedules.
Recovery workflows must be tested periodically to confirm that
timelines can be met during regulatory audits or scientific
reviews.

### Implementation steps

- Store frequently accessed datasets in Amazon S3 Standard,
then transition infrequently accessed data to Amazon Glacier Flexible Retrieval or enable Amazon S3
Intelligent-Tiering.
- Archive rarely accessed datasets with Amazon Glacier Deep
Archive for the lowest-cost, long-term retention.
- Use S3 Lifecycle Policies to automate transitions across
tiers.
- Implement recovery workflows using AWS Step Functions to
orchestrate retrieval steps, and align with regulatory
timelines and audit needs.

## Resources

**Related best practices:**

- Business continuity planning for research data
- Backup validation and recovery testing
- Risk-based classification of clinical and research datasets

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsrel03-bp02.html*

---

# LSREL04 — Foundations

**Pillar**: Reliability  
**Best Practices**: 3

---

# LSREL04-BP01 Map regulatory requirements to reliability controls

Create a comprehensive mapping between applicable regulatory
requirements (like GxP, 21 CFR Part 11, and GDPR) and your
reliability controls. Document how each control satisfies specific
regulatory requirements and maintain this mapping as regulations
evolve. For example, if regulations require system availability of
99.9% for critical applications, implement and document the
architecture decisions, monitoring systems, and recovery procedures
that support this requirement.

**Desired outcome:** A clear,
documented traceability matrix between regulatory requirements and
implemented reliability controls that demonstrates adherence and
guides architecture decisions. This mapping serves as evidence
during audits and inspections while verifying that reliability
measures directly address regulatory obligations.

**Common anti-patterns:**

- Implementing reliability controls without considering regulatory
requirements.
- Failing to document how reliability controls satisfy specific
regulations.
- Not updating the mapping when regulations or system architecture
changes.
- Focusing only on technical controls without considering
procedural and documentation requirements.

**Benefits of establishing this best
practice:**

- Provides clear evidence of regulatory adherence for audits and
inspections.
- Aligns reliability investments with regulatory priorities.
- Facilitates impact assessment when regulations change.
- Supports risk-based decision making for reliability investments.

## Implementation guidance

Use AWS Config to track configuration changes that might affect
adherence to regulatory requirements.

Consider implementing AWS Audit Manager to continuously audit your
AWS usage to simplify risk assessment and adherence with
regulations.

Implement tagging strategies to identify resources subject to
specific regulatory requirements.

Use AWS Systems Manager documents to standardize and automate
checks.

### Implementation steps

- Identify the applicable regulatory requirements related to
system reliability (like FDA, EMA, and ICH).
- Create a traceability matrix documenting each requirement
and corresponding control.
- Use AWS Config to establish configuration rules that enforce
regulatory requirements.
- Implement AWS CloudWatch alarms to monitor adherence to
availability requirements.
- Document architecture decisions that support regulatory
requirements using AWS Well-Architected Tool.
- Establish a review process to update the mapping when
regulations or systems change.

## Resources

**Related best practices:**

- Implement comprehensive monitoring for regulated systems
- Establish reliability qualification procedures
- Design for fault isolation and  graceful degradation

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsrel04-bp01.html*

---

# LSREL04-BP02 Implement risk-based reliability testing for regulated systems

Develop a risk-based approach to reliability testing that
prioritizes critical system components based on patient safety, data
integrity, and regulatory impact. For high-risk components in GxP
systems, implement more rigorous testing including fault injection,
recovery testing, and performance under stress. Document test
results as part of your evidence package.

**Desired outcome:** A comprehensive
testing program that verifies reliability requirements are met, with
testing depth proportional to risk. The testing approach provides
documented evidence that systems can maintain reliability under
various conditions, supporting both regulatory adherence and
operational confidence.

**Common anti-patterns:**

- Applying the same level of testing to each component regardless
of risk.
- Focusing only on functional testing while neglecting reliability
aspects.
- Not documenting test procedures and results for regulatory
evidence.
- Testing only in development environments without validating
production configurations.

**Benefits of establishing this best
practice:**

- Focuses testing resources on components with the highest risk
assessment.
- Provides documented evidence of reliability for regulatory
submissions.
- Identifies potential failures before they impact operations.
- Builds confidence in system resilience under adverse conditions.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Use AWS Fault Injection Service to safely test system resilience
through controlled experiments.

Consider implementing AWS Resilience Hub to assess and improve
application resilience.

Implement chaos engineering principles using AWS Fault Injection Service for GxP-critical systems.

Use AWS CloudWatch Synthetics to create canaries that continuously
verify critical paths.

### Implementation steps

- Perform a risk assessment to categorize system components by
regulatory impact.
- Define testing protocols with depth and frequency based on
risk categories.
- Implement automated testing using Amazon CloudWatch
Synthetics for continuous verification.
- Use AWS Fault Injection Service to test recovery mechanisms
for high-risk components.
- Document test procedures, results, and remediation actions
in a format suitable for regulatory review.
- Establish a regular cadence for reviewing and updating
testing protocols.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsrel04-bp02.html*

---

# LSREL04-BP03 Establish reliability qualification procedures

Create formal verification procedures for reliability aspects of
your system that align with regulatory expectations. Include
installation qualification (IQ), operational qualification (OQ), and
performance qualification (PQ) elements that verify reliability
features like high availability, disaster recovery, and data backup
and restore capabilities. Maintain these qualification records as
part of your regulatory documentation.

**Desired outcome:** A formal,
documented qualification process that verifies reliability features
work as intended and meet regulatory requirements. The qualification
procedures provide evidence that the system can reliably perform its
intended functions under expected conditions and recover from
failures, satisfying both technical reliability needs and regulatory
requirements.

**Common anti-patterns:**

- Focusing qualification only on functional aspects while
neglecting reliability features.
- Not including disaster recovery and failover testing in
qualification procedures.
- Qualifying systems only at initial deployment without
re-qualification after significant changes.
- Documenting only successful test results without capturing and
addressing failures.
- Separating reliability qualification from the overall validation
process.
- Using manual, non-repeatable qualification procedures that can't
be consistently executed.

**Benefits of establishing this best
practice:**

- Provides documented evidence of reliability capabilities for
regulatory adherence.
- Thoroughly verifies reliability features before production use.
- Establishes baseline performance for monitoring and continuous
improvement.
- Reduces risk of reliability-related findings during inspections.
- Builds confidence in the system's ability to maintain data
integrity during failures.
- Creates a foundation for continuous adherence as systems evolve.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Use AWS Systems Manager documents to create standardized
qualification procedures.

Consider AWS Backup for testing and validating backup and recovery
procedures.

Implement infrastructure as code using AWS CloudFormation for
consistent, repeatable infrastructure deployment.

Use AWS Config to verify that production environments match
qualified configurations.

Consider implementing AWS Resilience Hub to assess application
resilience against defined resilience policies.

Use AWS Fault Injection Service to validate recovery procedures in
a controlled manner.

### Implementation steps

- Define qualification protocols for reliability features
(like HA, DR, or backup and restore) based on risk
assessment.
- Create IQ procedures to verify infrastructure components are
properly installed and configured:

- Validate AWS service configurations match design
specifications.
- Verify networking components, security controls, and
monitoring systems.

- Develop OQ procedures to test reliability features under
normal conditions:

- Test automatic failover between availability zones.
- Verify data replication mechanisms function correctly.
- Validate backup processes complete successfully.

- Establish PQ procedures to verify performance under expected
load and stress conditions:

- Test system recovery after simulated failures.
- Verify data integrity is maintained during recovery
operations.
- Validate system meets defined recovery time and point
objectives.

- Document qualification results with evidence of successful
testing.
- Implement change control procedures to maintain qualified
state and determine when re-qualification is required.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsrel04-bp03.html*

---

# LSREL05 — Workload architecture

**Pillar**: Reliability  
**Best Practices**: 1

---

# LSREL05-BP01 Design edge buffering and queuing for laboratory instruments during network disruptions

Implement local data buffering, intelligent queuing, and automatic
retry mechanisms at the edge to verify that data from laboratory
instruments and clinical devices is never lost during network
connectivity issues. Edge infrastructure should provide sufficient
storage capacity, prioritize critical data streams, and
automatically resume transmission with integrity verification when
connectivity is restored.

**Desired outcome:**

- Avoid gaps in data collection from laboratory instruments or
clinical devices in the event of network disruption.
- Data integrity is verified before and after transmission to
detect corruption.
- Experiments and clinical workflows remain valid despite
temporary connectivity issues.

**Common anti-patterns:**

- Relying solely on instrument internal storage without additional
edge buffering capacity.
- Missing integrity verification, allowing corrupted data to
propagate to cloud storage.
- Lack of monitoring for buffer utilization, leading to unexpected
data loss when capacity is exceeded.
- Manual intervention required to resume data transmission after
network recovery.

**Benefits of establishing this best
practice:**

- Avoids invalidation of long-running experiments due to transient
network issues.
- Reduces risk of losing irreplaceable clinical or research data
from one-time procedures.
- Maintains scientific integrity by capturing complete and
accurate data.
- Provides operators with visibility and control during network
disruptions.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Design edge buffering based on instrument data generation rates,
expected network outage durations, and data criticality. Select
edge compute infrastructure that provides sufficient local storage
capacity and supports automatic retry mechanisms with exponential
backoff. Implement continuous monitoring of buffer utilization
with alerts before capacity thresholds are reached, giving
operators time to take corrective action. Validate buffered data
for integrity before and after transmission to detect corruption
during network disruptions.

### Implementation steps

- Deploy edge compute infrastructure (such as AWS IoT Greengrass, AWS Outposts, or local servers) to provide local
compute, storage, and data management capabilities.
Configure local buffering with retention policies based on
data priority and available storage capacity.
- Configure data transfer mechanisms with built-in retry and
exponential backoff strategies. Use services like AWS
DataSync for large file transfers with automatic integrity
verification, or implement custom retry logic for smaller
payloads.
- Monitor edge storage utilization using Amazon CloudWatch
metrics and create alarms for capacity thresholds to alert
operators before buffers reach maximum capacity.
- For disconnected environments, consider AWS Snowball Edge Edge
devices with local S3-compatible storage and automatic sync
when connectivity is restored.

## Resources

**Related best practices:**

- [LSREL07-BP01 Implement
system-wide data checksums and transfer validation](lsrel07-bp01.html)
- [LSREL11-BP01
Implement monitoring of equipment telemetry to detect
anomalies](lsrel11-bp01.html)

**Related tools:**

- [AWS IoT Greengrass](https://aws.amazon.com/greengrass/)
- [AWS IoT Core](https://aws.amazon.com/iot-core/)
- [AWS DataSync](https://aws.amazon.com/datasync/)
- [AWS Snowball Edge Edge](https://aws.amazon.com/snowball/)
- [AWS Outposts](https://aws.amazon.com/outposts/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsrel05-bp01.html*

---

# LSREL06 — Workload architecture

**Pillar**: Reliability  
**Best Practices**: 1

---

# LSREL06-BP01 Orchestrate workflows with checkpointing and failure isolation

Implement workflow orchestration with built-in checkpoints, retries,
and error isolation. By persisting intermediate results and enabling
targeted retries, failed tasks can be reprocessed independently
without requiring full pipeline reruns. Event-driven reprocessing
further improves efficiency, allowing workflows to resume from the
last successful step.

**Desired outcome:**

- Multi-step workflows can continue execution despite partial
failures.
- Failed tasks are retried automatically or isolated for
reprocessing.
- Long-running pipelines are resilient and cost-efficient with
research reproducibility requirements.

**Common anti-patterns:**

- Monolithic pipelines without checkpointing, forcing a complete
rerun if one step fails.
- Lack of retry or backoff strategies for transient errors,
leading to wasted compute cycles.
- Hardcoding dependencies between tasks so that downstream steps
fail on minor upstream issues.
- No visibility into workflow state, making recovery manual and
error-prone.

**Benefits of establishing this best
practice:**

- Reduces wasted compute and accelerates scientific turnaround
time.
- Improves reproducibility and auditability by maintaining
step-level logs and artifacts.
- Lowers cost by reprocessing only failed tasks instead of entire
workflows.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Break workflows into modular, independently testable steps with
well-defined inputs and outputs. Introduce checkpoints by
persisting intermediate artifacts in durable storage, allowing
workflows to restart from the last good state. Implement retry and
backoff strategies for transient errors to avoid unnecessary
failures.

Event-driven or rule-based triggers can restart only failed steps,
enabling faster recovery. Build in bservability from the start,
with centralized logs, metrics, and traces for each step to
support debugging and auditing.

### Implementation steps

- Use AWS Step Functions to orchestrate pipelines with retry
and error handling policies.
- Execute step workloads on AWS Batch or Amazon ECS or Amazon EKS for scalable and isolated compute.
- For genomics workloads, use AWS HealthOmics Workflows to run
CWL and WDL pipelines with built-in support for
checkpointing.
- Persist intermediate results in Amazon S3 for recovery and
reproducibility.
- Capture centralized logs and metrics in Amazon CloudWatch
for workflow observability.
- Use Amazon EventBridge to automatically trigger recovery
workflows for failed steps without restarting the full
pipeline.

## Resources

**Related best practices:**

- Long-term storage and reliable recovery of trial data
- Improve observability and operational insights in pipelines

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsrel06-bp01.html*

---

# LSREL07 — Workload architecture

**Pillar**: Reliability  
**Best Practices**: 4

---

# LSREL07-BP01 Implement system-wide data checksums and transfer validation

Incorporate integrity verification at every transfer and
transformation stage. Use cryptographic checksums (like SHA-256 or
MD5) or ETags to validate files when moved into or across the cloud.
Use managed services like AWS DataSync or Amazon S3 replication that
perform integrity checks automatically. For domain-specific use
cases (like genomics and imaging), add plausibility checks to detect
biologically inconsistent results that may indicate processing
corruption.

**Desired outcome:** Data fidelity is
preserved during ingestion, transfer, and transformation, with
verifiable proof that data has not been altered.

**Common anti-patterns:**

- Moving data without checksum or hash verification.
- Relying solely on application logs to detect corruption.
- Using manual copy processes without automated validation.

**Benefits of establishing this best
practice:**

- Reduces risk of silent corruption during high-volume genomic or
imaging transfers.
- Increases trust in research outputs by deriving results
validated input data.
- Provides auditors and regulators with evidence of data integrity
safeguards.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Integrate checksums and validation at every stage where data is
moved or transformed. Cryptographic checksums (such as SHA-256) or
S3 ETags provide automated validation during transfers into cloud
storage. Managed services like AWS DataSync, S3 Replication, and
S3 Transfer Acceleration perform integrity checks by default,
reducing operational burden. For scientific pipelines, augment
checksum validation with domain-specific checks, such as detecting
biologically implausible variants in genomic data or corrupt
slices in imaging data.

### Implementation steps

- Data should be ingested into Amazon S3 where ETag-based
validation confirms file integrity.
- Use AWS DataSync for on-premises to cloud transfers,
verifying that validation occurs automatically.
- Configure S3 Replication with replication metrics enabled to
verify data consistency across buckets.
- For sensitive research workloads, embed integrity checks
directly into processing pipelines (for example, validating
SHA-256 digests before and after transformation).

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsrel07-bp01.html*

---

# LSREL07-BP02 Build idempotent and reproducible processing pipelines

Design processing systems that produce consistent results regardless
of retries or partial failures. Incorporate unique identifiers,
transaction logs, and state tracking to verify that retries don't
duplicate or corrupt data. In research and clinical analysis,
reproducibility of results under repeated execution is a cornerstone
of scientific and regulatory assurance.

**Desired outcome:** Processing
pipelines can be retried without causing duplication or corruption,
maintaining reproducibility of results under repeated execution.

**Common anti-patterns:**

- Designing pipelines that overwrite intermediate results without
safeguards.
- Using non-unique identifiers for jobs, leading to duplication of
processed data.
- Failing to persist state, making retries non-deterministic.

**Benefits of establishing this best
practice:**

- Maintains scientific reproducibility by producing consistent
outputs from the same inputs.
- Reduces wasted compute cycles by allowing safe retries after
transient errors.
- Increases confidence in regulatory submissions where
reproducibility is scrutinized.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Idempotency should be a foundational principle in workflow design.
Each job execution must generate unique identifiers tied to input
datasets and persist transaction logs or checkpoints. State
tracking should record which inputs have been successfully
processed, enabling retries without duplication. For long-running
genomic analysis, idempotency verifies that a failed job can be
retried without corrupting downstream results.

### Implementation steps

- Processing pipelines should use AWS Step Functions or AWS Batch to track execution state and verify that retries are
idempotent.
- Use Amazon DynamoDB or Amazon RDS to persist transaction
logs and job state.
- Store intermediate artifacts in Amazon S3 with unique
identifiers as S3 prefixes (for example, prefixing with
dataset UUIDs) to maintain reproducibility.
- Implement retry policies with exponential backoff in AWS Step Functions, so transient failures don't result in
duplicate or corrupted processing.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsrel07-bp02.html*

---

# LSREL07-BP03 Use staged validation and data quarantine mechanisms

Introduce controlled validation stages where data is quarantined
before being processed further. Apply automated rules for schema
conformity, metadata completeness, and domain-specific plausibility
(for example, genomic variants outside biological ranges). Only data
that passes validation and adherence data standards (such as CDISC
or FHIR) proceeds. Isolate data that fails for human review, with
full audit trails to support regulatory adherence.

**Desired outcome:** Only data that
meets predefined quality and plausibility criteria enters production
pipelines, while problematic data is isolated for review.

**Common anti-patterns:**

- Directly processing incoming data without validation.
- Overlooking schema, metadata, or biological plausibility checks.
- Mixing invalid data with production datasets, causing downstream
corruption.

**Benefits of establishing this best
practice:**

- Stops invalid datasets from contaminating results.
- Accelerates regulatory reviews by providing traceable validation
evidence.
- Improves scientific trust by verifying that only high-quality
data enters analysis.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Data pipelines should incorporate a quarantine stage where
incoming data is validated before processing. Automated rules must
check for schema adherence, metadata completeness, and
instrument-specific error patterns. Apply domain-specific rules,
such as filtering out biologically implausible values in clinical
data. Flag and isolate quarantined data, with human review
workflows for resolution.

### Implementation steps

- Ingest new datasets into a quarantine Amazon S3 bucket with
tagging enabled to indicate that data is pending validation.
- Use AWS Glue or AWS Lambda to validate schema, metadata, and
plausibility.
- Store failed validation results in Amazon DynamoDB or
OpenSearch for investigation, and configure notifications
through Amazon SNS to alert data stewards.
- Only validated data should be transitioned into production
pipelines using S3 lifecycle policies or Step Functions
orchestration.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsrel07-bp03.html*

---

# LSREL07-BP04 Track data lineage with lifecycle metadata

Assign metadata tags (for example, raw,
filtered, processed, and
analyzed) at each lifecycle stage, so data state
is visible. This enables reproducibility, auditing, and debugging
when results need to be traced back to raw inputs. Use catalogs and
governance tools to track lineage across storage and processing
layers.

**Desired outcome:** Data state is
transparent across ingestion, processing, and analysis, with lineage
records supporting reproducibility and audits.

**Common anti-patterns:**

- Failing to label datasets by processing stage.
- Storing derived data without linkage to raw inputs.
- Using inconsistent or unstructured metadata practices.

**Benefits of establishing this best
practice:**

- Enables reproducibility by tracing results back to raw data.
- Simplifies compliance-related audits by showing how data was
transformed.
- Reduces troubleshooting time by quickly identifying the source
of anomalies.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Every dataset should be tagged with lifecycle metadata reflecting
its stage: raw, filtered,
processed, or analyzed.
Lineage metadata should include transformation steps, software
versions, and parameter settings. These lineage records must be
centralized in a catalog or metadata repository to provide
transparency across the workload.

### Implementation steps

- Store datasets in Amazon S3 with metadata tags to reflect
their lifecycle stage.
- Use AWS AWS Glue Data Catalog to maintain a centralized record
of lineage and transformations.
- Capture transformation metadata during pipeline execution
using AWS Step Functions or AWS Lambda and store results in
Amazon DynamoDB or Amazon OpenSearch Service.
- Include metadata in evidence packages for GxP-regulated
workloads.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsrel07-bp04.html*

---

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

# LSREL11 — Failure management

**Pillar**: Reliability  
**Best Practices**: 3

---

# LSREL11-BP01 Implement monitoring of equipment telemetry to detect anomalies

Capture equipment telemetry such as temperature, vibration, cycle
counts, and error codes in real time to identify anomalies early. A
consistent telemetry pipeline enables proactive monitoring, alerts,
and traceability of equipment performance across research
facilities.

**Desired outcome:**

- Continuous monitoring of lab equipment to detect anomalies
early.
- Reduced risk of unplanned downtime through proactive alerts.
- Complete telemetry records available for troubleshooting and
audits.

**Common anti-patterns:**

- Not collecting or collecting telemetry data inconsistently.
- Storing telemetry without time-stamping or contextual metadata.
- Failing to establish thresholds or alerts on critical
parameters.

**Benefits of establishing this best
practice:**

- Improves reliability of experiments through early detection of
issues.
- Enables root cause analysis and reproducibility through
equipment performance records.
- Supports regulatory adherence by providing traceable operational
logs.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

A resilient telemetry strategy requires secure, standardized
pipelines for collection and long-term storage. Verify that your
data includes time stamps and contextual metadata to support
traceability. Integrate alerts with incident response processes
for timely remediation. Preserve telemetry records for audits and
long-term performance analysis.

### Implementation steps

- Deploy AWS IoT Greengrass to capture telemetry locally and
preprocess sensitive data at the lab site.
- Stream telemetry securely into AWS IoT Core for ingestion.
- Store data in Amazon Timestream for time-series analysis or
Amazon S3 for long-term archival.
- Configure anomaly detection with Amazon CloudWatch Alarms
and notify research operations teams through Amazon SNS.
- Provide researchers with performance dashboards using Quick for visualization.

## Resources

**Related best practices:**

- Incident detection and alerting
- Data integrity and traceability for regulated environments
- Root cause analysis frameworks

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsrel11-bp01.html*

---

# LSREL11-BP02 Apply predictive maintenance using AI models

Use AI/ML models to analyze telemetry, usage logs, and maintenance
records for predicting potential equipment failures. Integrating
predictive insights with laboratory management systems reduces
downtime, optimize calibration schedules, and extend equipment life.

**Desired outcome:**

- Anticipation of failures before they occur, reducing experiment
disruption.
- Optimized maintenance schedules that balance reliability with
operational efficiency.
- Integration of predictive insights into research workflows and
logs.

**Common anti-patterns:**

- Relying solely on reactive maintenance after equipment fails.
- Collecting data but not training or updating predictive models.
- Not integrating predictive insights with LIMS or quality
systems, leading to disconnected records.

**Benefits of establishing this best
practice:**

- Reduces equipment failure rates and downtime.
- Extends equipment life cycles and optimized resource
utilization.
- Enhances regulatory adherence through integrated maintenance and
calibration logs.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Predictive maintenance requires high-quality, centralized datasets
including logs, calibration records, and telemetry. Periodically
validate AI models to maintain trustworthiness in regulated
environments. Integrating outputs into research systems verifies
that predictions drive actionable workflows, rather than remaining
siloed in technical teams.

### Implementation steps

- Ingest telemetry into Amazon CloudWatch and usage logs into
Amazon S3.
- Train ML models in Amazon SageMaker AI using historical
performance datasets.
- For turnkey options, deploy Amazon Lookout for Equipment to
analyze telemetry streams.
- Integrate predictive alerts into Amazon EventBridge to
trigger workflows or incident responses.
- Store maintenance logs in Amazon RDS or integrate directly
with LIMS databases for traceability.

## Resources

**Related best practices:**

- AI/ML lifecycle management in regulated environments
- Integration of IT and OT (Operational Technology) systems
- GxP-aligned system validation for ML-driven processes

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsrel11-bp02.html*

---

# LSREL11-BP03 Plan redundancy for critical laboratory equipment

Design redundancy strategies for critical laboratory equipment by
maintaining hot spares, parallelized runs, or vendor service
agreements. Effective redundancy maintains continuity of operations
even during failures of high-value or high-throughput instruments.

**Desired outcome:**

- Continuous operation of critical research workflows during
equipment failures.
- Reduced delays in experiments and studies by having spare
capacity.
- Documented continuity plans for audits and inspections.

**Common anti-patterns:**

- Treating equipment equally without prioritizing critical
instruments.
- Failing to budget or plan for spare capacity in core systems.
- Assuming vendor maintenance SLAs are sufficient for continuity
of research operations.

**Benefits of establishing this best
practice:**

- Reduces operational risk by maintaining continuity during
unexpected failures.
- Increases confidence in meeting research timelines and
commitments.
- Demonstrates resilience and preparedness to regulators and
auditors.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Start by classifying lab equipment by criticality and throughput
to identify which instruments require redundancy. Define
strategies such as hot spares, workload sharing, or vendor backup
agreements. Maintain documented runbooks for failover to redundant
equipment, and periodically simulate outages to test readiness.

### Implementation steps

- Track redundancy configurations using AWS Config for
reporting.
- Store redundancy plans, SLAs, and vendor contracts in Amazon S3, and enable fast search with Amazon OpenSearch Service.
- Orchestrate escalation procedures using Amazon SNS and AWS Lambda when failures are detected.
- Record continuity outcomes in Amazon DynamoDB for audit
traceability.
- Periodically simulate infrastructure and application-level
failures with AWS Fault Injection Service (FIS) to
validate the continuity of data capture, workflow
orchestration, and failover processes supporting laboratory
equipment.
- For physical instruments, conduct tabletop or vendor-led
failure simulations to keep redundancy plans practical.

## Resources

**Related best practices:**

- Business continuity and disaster recovery planning
- Risk-based classification of lab assets
- Vendor management and SLA governance

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsrel11-bp03.html*

---

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

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
