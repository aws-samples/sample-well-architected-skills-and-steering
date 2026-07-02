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
