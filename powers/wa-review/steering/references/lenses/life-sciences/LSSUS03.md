# LSSUS03 — Data management efficiency in data analytics and data lifecycle

**Pillar**: Sustainability  
**Best Practices**: 2

---

# LSSUS03-BP01 Optimize data management for sustainability in life sciences

Implement data management practices that reduce redundant storage,
optimize processing efficiency, and minimize data movement while
maintaining regulatory requirements. Establish centralized data
catalogs and automated lifecycle policies to optimize your storage
tier utilization based on access patterns. Design data architectures
that balance accessibility requirements with energy efficiency
goals.

**Desired outcome:** Achieve
significant reduction in storage footprint and energy consumption
through optimized data lifecycle management, deduplication
strategies, and intelligent storage tiering while maintaining
adherence to life sciences regulatory requirements.

**Common anti-patterns:**

- You store data in the same storage tier regardless of access
patterns or lifecycle requirements.
- You don't implement deduplication strategies for redundant
research datasets.
- You move large datasets frequently between regions or storage
systems without considering energy impact.
- You don't establish data retention policies aligned with
regulatory requirements and business needs.
- You maintain multiple copies of reference datasets across
different research projects.
- You don't use compression techniques for archival and
infrequently accessed data.
- You don't monitor storage utilization and costs to identify
optimization opportunities.

**Benefits of establishing this best
practice:**

- Reduce storage costs through intelligent lifecycle management
and tiering.
- Lower energy consumption of storage systems by using optimal
storage classes.
- Improve data accessibility through centralized cataloging and
metadata management.
- Improve regulatory adherence through automated retention and
archival policies.
- Reduce data transfer costs and energy consumption through
strategic data placement.
- Enable better research collaboration through shared,
deduplicated reference datasets.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Life sciences organizations generate and consume vast amounts of
data across research, clinical, and manufacturing operations.
Effective data management for sustainability requires
understanding data access patterns, regulatory retention
requirements, and the energy implications of different storage
approaches. The key is implementing automated policies that
transition data through appropriate storage tiers while
maintaining accessibility for research and regulatory needs.

Centralized data catalogs play a crucial role in reducing
redundancy and improving data discoverability. By implementing
services like AWS Lake Formation for research data or AWS HealthLake for healthcare data, organizations can remove duplicate
datasets, improve data governance, and reduce overall storage
requirements. This approach is particularly important for
reference datasets, genomic databases, and clinical trial data
that may be accessed across multiple research projects.

### Implementation steps

- Establish centralized data catalogs and governance:

Centralize the management of data by implementing
services such as AWS Lake Formation for research data
cataloging and governance.
- Use data lakes such as AWS HealthLake for healthcare and
clinical data management.
- Create standardized metadata schemas for different data
types.
- Establish data ownership and access control policies.

- Implement intelligent storage lifecycle management:

Configure lifecycle policies to automatically transition
data between storage classes.
- Use Amazon S3 Standard for active research data
requiring frequent access.
- Implement dynamic tiering for data with changing or
unknown access patterns.
- Archive audit and reference data to durable, infrequent
access storage such as Amazon Glacier or S3 Glacier Deep Archive.

- Deploy deduplication and compression strategies:

Implement data deduplication for reference datasets and
genomic databases.
- Use compression algorithms appropriate for different
data types (genomic, imaging, clinical).
- Use service compression features for automated
optimization.
- Create shared reference datasets to remove redundant
storage across projects.

- Optimize data placement and movement:

Analyze data access patterns.
- Implement regional data placement strategies to minimize
transfer costs.
- Use transfer services such as AWS DataSync for efficient
data transfer and synchronization.
- Consider AWS Storage Gateway for hybrid storage
optimization.

- Monitor and continuously optimize storage efficiency:

Use AWS Cost Explorer to track storage costs and
utilization patterns.
- Implement Amazon CloudWatch metrics for storage
efficiency monitoring.
- Set up automated alerts for storage anomalies and
optimization opportunities.
- Conduct regular reviews of data lifecycle policies and
storage class effectiveness.

## Resources

**Related best practices:**

- [LSSUS01-BP01
Design high-performance computing workloads to minimize energy
usage](lssus01-bp01.html)
- [LSSUS02-BP01
Implement sustainability proxy metrics pipeline for research
workloads](lssus02-bp01.html)

**Related documents:**

- [Sustainability
Pillar - AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/)

**Related videos:**

- [AWS re:Invent 2024 - Build and optimize a data lake on Amazon S3
(STG323)](https://www.youtube.com/watch?v=SIGpBvmlick)
- [AWS re:Invent 2024 - Data-driven sustainability with AWS
(SUS201)](https://www.youtube.com/watch?v=nA5WqgM7Jt0)
- [Securely
Store, Transform, Query and Analyze Health Data with AWS HealthLake](https://www.youtube.com/watch?v=a5WInyTti74)

**Related examples:**

- [Guidance
for Data Lakes on AWS](https://aws.amazon.com/solutions/guidance/data-lakes-on-aws/)

**Related tools:**

- [AWS Lake Formation](https://aws.amazon.com/lake-formation/)
- [AWS HealthLake](https://aws.amazon.com/healthlake/)
- [Amazon S3 Intelligent-Tiering](https://aws.amazon.com/s3/storage-classes/intelligent-tiering/)
- [Amazon Glacier](https://aws.amazon.com/s3/storage-classes/glacier/)
- [AWS DataSync](https://aws.amazon.com/datasync/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lssus03-bp01.html*

---

# LSSUS03-BP02 Process data closer to source

Optimize data processing locations to minimize network usage and
reduce energy consumption associated with data movement. Implement
edge computing and hybrid architectures that process large datasets
near their generation points, particularly for bandwidth-intensive
applications like genomic sequencing and imaging workflows. Use
managed services that provide optimized resource utilization and
automatic scaling to reduce infrastructure overhead.

**Desired outcome:** Significantly
reduce network bandwidth usage and associated energy consumption by
processing data at optimal locations relative to data sources, while
maintaining processing performance and regulatory requirements.

**Common anti-patterns:**

- You transfer large datasets to centralized processing locations
without considering network and energy costs.
- You don't evaluate edge computing options for
bandwidth-intensive research applications.
- You process data in regions distant from data generation points
without justification.
- You don't consider data sovereignty and regulatory requirements
when choosing processing locations.
- You transfer raw data for processing instead of implementing
preprocessing at the edge.

**Benefits of establishing this best
practice:**

- Reduce network bandwidth costs and energy consumption for large
dataset processing.
- Improve processing performance by reducing network latency for
data-intensive operations.
- Lower infrastructure costs through optimized resource
utilization and managed service adoption.
- Enhance data security and regulatory adherence by minimizing
data movement across network boundaries.
- Enable real-time processing capabilities for time-sensitive
research applications.
- Support hybrid and multi-cloud architectures that optimize for
both performance and sustainability.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Life sciences research generates massive datasets that
traditionally require significant network resources to transfer to
centralized processing locations. This approach is particularly
inefficient for applications like genomic sequencing,
cryo-electron microscopy, and high-resolution imaging where raw
data volumes can reach terabytes per experiment. Processing data
closer to its source reduces both network energy consumption and
processing latency while often improving overall system
performance.

Edge computing and hybrid architectures become essential when
dealing with specialized equipment that generates large amounts of
data continuously. For example, cryo-EM facilities, genomic
sequencers, and imaging systems can benefit significantly from
local preprocessing that reduces data volumes before cloud
transfer. AWS services like AWS Outposts enable on-premises
processing with cloud tools, while managed services provide
automatic optimization without requiring dedicated infrastructure
management.

### Implementation steps

- Analyze data generation patterns and processing
requirements:

Map data sources and their typical output volumes and
processing needs.
- Identify bandwidth-intensive workflows that would
benefit from edge processing.
- Assess regulatory requirements for data processing
locations.
- Use and application discovery service to understand
current data flow patterns.

- Implement edge computing solutions for high-volume data
sources:

Deploy edge compute solution such as AWS Outposts for
on-premises processing of large genomic datasets.
- Use AWS Snow Family devices for data processing in
remote or bandwidth-constrained locations.
- Implement IoT edge processing of sensor and instrument
data.
- Consider AWS Wavelength for ultra-low latency processing
requirements.

- Use managed services for optimized data processing:

Use services such as Amazon Kinesis Data Streams for
real-time data processing and analytics.
- Implement AWS Transfer Family for optimized file
transfer and processing workflows.
- Deploy AWS Batch at edge locations for containerized
processing workloads.
- Use Amazon SageMaker AI Edge for machine learning inference
at data sources.

- Optimize data preprocessing and filtering at source
locations:

Implement data compression and filtering before cloud
transfer.
- Use AWS Lambda@Edge for lightweight data processing and
transformation.
- Deploy containerized preprocessing pipelines using
Amazon ECS on AWS Outposts.
- Implement quality control and data validation at source
locations.

- Monitor and optimize data movement and processing
efficiency:

Track data transfer volumes and costs using FinOps tools
such as Cloud Intelligence Dashboards.
- Monitor processing performance and resource utilization
with Amazon CloudWatch.
- Use AWS X-Ray to trace data processing workflows and
identify optimization opportunities.
- Implement automated alerts for unusual data transfer
patterns or processing inefficiencies.

## Resources

**Related best practices:**

- [LSSUS03-BP01
Optimize Data Management for Sustainability in Life
Sciences](lssus03-bp01.html)
- [LSSUS01-BP01
Design high-performance computing workloads to minimize energy
usage](lssus01-bp01.html)
- [LSSUS02-BP01
Implement sustainability proxy metrics pipeline for research
workloads](lssus02-bp01.html)

**Related documents:**

- [Sustainability
Pillar - AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/)
- [AWS Outposts Documentation](https://docs.aws.amazon.com/outposts/)
- [AWS Snow Family Documentation](https://docs.aws.amazon.com/snowball/)
- [Amazon Kinesis Data Streams Documentation](https://docs.aws.amazon.com/kinesis/)
- [AWS Transfer Family Documentation](https://docs.aws.amazon.com/transfer/)
- [Optimizing
data transfers for high throughput life science instruments
using AWS DataSync](https://aws.amazon.com/blogs/storage/optimizing-data-transfers-for-high-throughput-life-science-instruments-using-aws-datasync/)
- [Cloud
at the Edge for Healthcare and Life Sciences](https://d1.awsstatic.com/product-marketing/Outposts/AWS%20HCLS%20eBook.pdf)
- [Genomics
data and transfer storage use cases](https://aws.amazon.com/health/genomics/solutions/data-transfer-and-storage/)

**Related videos:**

- [AWS re:Invent 2024 - AWS wherever you need it: From the cloud to
the edge (HYB201)](https://www.youtube.com/watch?v=_1quMnn2TI0&list=PL2yQDdvlhXf-xkVwHXosPxQh6BdY5LMIc&index=8)

**Related examples:**

- [Guidance
for Optimizing Data Architecture for Sustainability on
AWS](https://aws.amazon.com/solutions/guidance/optimizing-data-architecture-for-sustainability-on-aws/)
- [Building
a GPU-enabled CryoEM workflow on AWS](https://aws.amazon.com/blogs/industries/building-a-gpu-enabled-cryoem-workflow-on-aws/)

**Related tools:**

- [AWS Outposts](https://aws.amazon.com/outposts/)
- [AWS Snow Family](https://aws.amazon.com/snow/)
- [AWS IoT Greengrass](https://aws.amazon.com/greengrass/)
- [AWS Wavelength](https://aws.amazon.com/wavelength/)
- [Amazon Kinesis Data Streams](https://aws.amazon.com/kinesis/data-streams/)
- [AWS Transfer Family](https://aws.amazon.com/aws-transfer-family/)
- [AWS Lambda@Edge](https://aws.amazon.com/lambda/edge/)
- [Amazon SageMaker AI Edge](https://aws.amazon.com/sagemaker/edge/)
- [AWS Application Discovery Service](https://aws.amazon.com/application-discovery/)
- [AWS X-Ray](https://aws.amazon.com/xray/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lssus03-bp02.html*

---
