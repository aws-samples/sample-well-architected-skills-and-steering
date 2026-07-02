# LSPERF02 — Architecture selection

**Pillar**: Performance Efficiency  
**Best Practices**: 3

---

# LSPERF02-BP01 Data-aware storage tiering

Implement intelligent storage tiering strategies that align storage
performance characteristics with data access patterns. Place
frequently accessed reference data on high-performance tiers, move
aging research data to cost-optimized tiers, and archive completed
study data to deep storage, while maintaining appropriate encryption
and access controls based on data sensitivity classification.

**Desired outcome:** Implement a
comprehensive, data-driven storage management system that
automatically places data on the most appropriate storage tier based
on access patterns, age, and sensitivity classification.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Working backward from your research data needs, design an
intelligent storage architecture that aligns with actual access
patterns to optimize both performance and cost.

Start by classifying data based on access frequency and
sensitivity. Deploy high-performance options like Amazon EFS with
provisioned throughput or Amazon FSx for Lustre for frequently
accessed data requiring low-latency retrieval.

As access patterns decrease, implement automated lifecycle
policies that transition data to cost-optimized tiers such as S3
Standard-Infrequent Access or S3 Intelligent-Tiering.

For rarely accessed audit data, use S3 Glacier Deep Archive to
minimize costs while maintaining accessibility.

Maintain consistent encryption and access controls across each
tier, with appropriate keys and permissions based on sensitivity
classification. Use S3 Analytics to continuously monitor access
patterns and refine tiering policies, while implementing object
tagging to preserve context across tiers.

For domain-specific optimization, consider purpose-built solutions
like AWS HealthOmics, AWS HealthImaging, and AWS HealthLake.

### Implementation steps

- Configure S3 Intelligent-Tiering for scientific dataset
storage.
- Store sensitive data in encrypted Amazon RDS instances.
- Implement Amazon S3 Lifecycle policies for data archival.
- Implement AWS Lambda for auto scaling data processing.
- Consider purpose-built storage such as HealthLake,
HealthOmics, and HealthImaging.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsperf02-bp01.html*

---

# LSPERF02-BP02 Secure data separation by classification

Establish clear boundaries between different data types based on
sensitivity and regulatory requirements. Maintain sensitive patient
records in encrypted, highly-available database instances with
comprehensive audit capabilities, while allowing broader access to
de-identified research datasets through separate storage mechanisms
with appropriate controls for scientific collaboration.

**Desired outcome:** Establish a
comprehensive data separation framework that clearly separates
different data types based on sensitivity levels and regulatory
requirements, providing appropriate storage, access controls, and
availability for each category.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Design your data architecture with clearly defined boundaries that
separate information based on sensitivity levels and regulatory
requirements. Implement a comprehensive data classification system
that identifies and tags data according to sensitivity, regulatory
scope, and access requirements. For sensitive patient records and
protected health information (PHI), use encrypted,
highly-available database services like Amazon RDS with multi-AZ
deployments and encryption at rest using AWS KMS customer-managed
keys.

Enable comprehensive audit logging through services like AWS CloudTrail and Amazon RDS Enhanced Monitoring to track access and
modifications to sensitive data, improving adherence to
regulations like HIPAA or GDPR.

For de-identified research datasets intended for broader
scientific collaboration, establish separate storage mechanisms
using services like Amazon S3 with appropriate bucket policies and
access controls that facilitate controlled sharing while blocking
unauthorized access. Implement robust de-identification processes
that follow established standards like HIPAA Safe Harbor or Expert
Determination methods before moving data to these collaborative
environments.

Use AWS Identity and Access Management (IAM) with attribute-based
access control (ABAC) to create fine-grained permissions based on
data classification tags, verifying that users can only access
data appropriate to their role and research needs. Consider
implementing additional safeguards like VPC endpoints and network
isolation to provide network-level separation between sensitive
and de-identified data environments.

### Implementation steps

- Implement AWS Organizations for multi-account data
separation.
- Configure S3 bucket policies for sensitivity-based
isolation.
- Use AWS IAM for fine-grained data access controls.
- Deploy AWS Lake Formation for centralized data governance.
- Implement AWS KMS with Customer Managed keys for each data
category.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsperf02-bp02.html*

---

# LSPERF02-BP03 Elastic data processing pipelines

Design data processing architectures that automatically scale to
accommodate both predictable and unexpected processing demands.
Implement event-driven pipelines that efficiently handle
high-velocity instrument data streams while maintaining strict
controls over clinical data flows, providing consistent performance
during peak research periods without compromising security or
regulatory requirements.

**Desired outcome:** Implement an
adaptive data processing architecture that automatically scales to
meet varying workload demands while maintaining strict security and
audit controls for each data type, particularly clinical
information.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

To effectively manage high-velocity data processing, implement
event-driven architectures that respond to data events in
real-time, enabling efficient handling of instrument data streams.
Maintain separate processing flows for different data types,
applying appropriate controls to clinical data while optimizing
research workloads.

Use managed AWS services like AWS Lambda, Amazon SQS, and Amazon Kinesis that automatically scale to match processing needs without
manual intervention. Implement throttling mechanisms to protect
downstream systems from being overwhelmed during peak research
periods. Set up comprehensive monitoring to track performance and
automatically adjust resources based on observed patterns, while
maintaining regulatory guardrails to verify that automatic scaling
doesn't compromise security requirements.

Regularly conduct load testing to verify that your architecture
can scale as expected under stress, validating the system's
ability to handle varying data volumes while maintaining
performance and regulatory standards.

### Implementation steps

- Deploy Amazon Kinesis for high-velocity data streaming.
- Implement AWS Lambda for event-driven data processing
and auto scaling data processing.
- Use AWS Step Functions to orchestrate workflows.
- Configure Amazon MSK for reliable clinical data pipelines.
- Implement AWS Auto Scaling for predictable research peaks.

## Resources

**Related tools:**

- [Amazon Kinesis](https://aws.amazon.com/kinesis/)
- [AWS Lambda](https://aws.amazon.com/lambda/)
- [AWS Step Functions](https://aws.amazon.com/step-functions/)
- [Amazon MSK
(Managed Streaming for Apache Kafka)](https://aws.amazon.com/msk/)
- [AWS Auto Scaling](https://aws.amazon.com/autoscaling/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsperf02-bp03.html*

---
