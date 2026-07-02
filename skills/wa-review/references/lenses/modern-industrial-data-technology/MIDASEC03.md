# MIDASEC03 — Detection

**Pillar**: Security  
**Best Practices**: 5

---

# MIDASEC03-BP01 Integrate and enforce privacy by design principles

Apply privacy-by-design principles in the architecture of manufacturing data environments
to help you comply with privacy regulations from the outset. This includes minimizing data
collection, embedding access controls, and anonymizing personal data.

**Desired outcome:** Data privacy is protected from the start
of the system design, reducing regulatory risks and improving trust with stakeholders.

**Benefits of establishing this best practice:** Aligns with
data protection regulations like GDPR or CCPA, reduces risk of breaches, and supports ethical
data use.

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

Design architectures with data minimization, separation, encryption, and auditability
as core principles.

### Implementation steps

- Identify personal and sensitive data processed within the manufacturing system.
- Limit collection and retention to only required fields and durations.
- Implement anonymization or pseudonymization where applicable.
- Embed access controls and audit logs from the start.

## Resources

- [General Data Protection Regulation (GDPR) Center](https://aws.amazon.com/compliance/gdpr-center/)
- [Privacy by Design on AWS](https://docs.aws.amazon.com/whitepapers/latest/privacy-by-design-on-aws/privacy-by-design-on-aws.pdf)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasec03-bp01.html*

---

# MIDASEC03-BP02 Implement industrial data classifications and protection policies

Define classification tiers for industrial data (for example, public, internal,
confidential, and restricted), and apply policies to control access, visibility, and
protection levels accordingly.

**Desired outcome:** Manufacturing data is systematically
classified and protected based on its criticality and sensitivity.

**Benefits of establishing this best practice:** Reduces risk
of data leakage, safeguards sensitive data, and supports scalable governance models.

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

Use AWS tools like Amazon Macie and AWS IAM policies to tag, monitor, and restrict
access to classified data.

### Implementation steps

- Define classification categories based on business needs and risk.
- Tag data assets using AWS resource tags or AWS AWS Glue Data Catalog.
- Use Amazon Macie to identify and monitor sensitive data types.
- Enforce access controls and monitoring based on classification tags.

## Resources

- [What is Amazon Macie?](https://docs.aws.amazon.com/macie/latest/user/what-is-macie.html)
- [Populating the AWS Glue Data Catalog](https://docs.aws.amazon.com/glue/latest/dg/populate-data-catalog.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasec03-bp02.html*

---

# MIDASEC03-BP03 Identify source data and set data classifications

Discover and classify data at the source (for example, sensors, PLCs, MES, and ERP
systems) to apply appropriate controls from ingestion onward.

**Desired outcome:** Data is classified and governed from the
moment it enters the system, helping prevent downstream risk exposure.

**Benefits of establishing this best practice:** Improves
control over high-risk data, simplifies pipeline security, and enhances lineage tracking and
compliance auditing.

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

Build data ingestion pipelines with tagging and classification integrated into the
ingestion and cataloging layers.

### Implementation steps

- Identify all upstream data sources contributing to the system.
- Use edge and gateway services to apply initial metadata or tags.
- Ingest data into AWS using services like Amazon Kinesis, AWS IoT Core, or AWS IoT SiteWise with classification.
- Catalog and tag datasets in AWS Glue or AWS Lake Formation.

## Resources

- [AWS Lake Formation](https://aws.amazon.com/lake-formation/)
- [AWS Glue](https://aws.amazon.com/glue/)
- [What is AWS IoT SiteWise?](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/what-is-sitewise.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasec03-bp03.html*

---

# MIDASEC03-BP04 Implement industrial encryption policies

Apply encryption policies across all layers of the manufacturing data system, including
at rest, in transit, and optionally during processing, to help protect sensitive operational
and proprietary information.

**Desired outcome:** Data remains encrypted end-to-end,
providing confidentiality and integrity and helping with regulatory alignment.

**Benefits of establishing this best practice:** Reduces impact
of data breaches, supports regulatory compliance, and builds trust with partners and
customers.

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

Use AWS KMS for key management and enforce encryption using S3 bucket policies, VPC
security, and service-level configurations.

### Implementation steps

- Enable default encryption on all data stores (for example, Amazon S3, Amazon RDS,
Amazon Redshift, and Amazon DynamoDB).
- Use TLS 1.2+ for all data in transit.
- Create customer-managed keys (CMKs) using AWS KMS for sensitive workloads.
- Regularly rotate keys and audit access with AWS CloudTrail.

## Resources

- [AWS Key Management Service](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html)
- [Setting default server-side encryption behavior for Amazon S3 buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/default-bucket-encryption.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasec03-bp04.html*

---

# MIDASEC03-BP05 Implement data retention policies for each data class

Define and enforce data retention rules based on classification and regulatory
requirements to reduce storage costs and minimize compliance risks.

**Desired outcome:** Only required data is retained, improving
cost efficiency and reducing exposure of legacy data.

**Benefits of establishing this best practice:** Helps prevent
unnecessary storage costs, reduce audit complexity, and support lifecycle compliance.

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

Use Amazon S3 lifecycle policies, AWS Glue table TTLs, and tagging strategies to
automate enforcement of retention policies.

### Implementation steps

- Define data retention durations based on classification and compliance needs.
- Apply tags and metadata to datasets to identify lifecycle requirements.
- Use S3 lifecycle rules or Glue jobs to delete or archive data.
- Regularly review and update retention policies based on changing regulations.

## Resources

- [Managing your storage lifecycle](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html)
- [AWS Glue Documentation](https://docs.aws.amazon.com/glue/index.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasec03-bp05.html*

---
