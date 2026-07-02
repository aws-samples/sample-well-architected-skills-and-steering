# MLPERF03 — Data processing

**Pillar**: Performance Efficiency  
**Best Practices**: 1

---

# MLPERF03-BP01 Use a modern data architecture

Get the best insights from exponentially growing data using a modern
data architecture. This architecture enables movement of data
between a data lake and purpose-built stores including a data
warehouse, relational databases, non-relational databases, ML and
big data processing, and log analytics. A data lake provides a
single place to run analytics across mixed data structures collected
from disparate sources. Purpose-built analytics services provide the
speed required for specific use cases like real-time dashboards and
log analytics.

**Desired outcome:** You implement a
modern data architecture that enables seamless data movement between
storage systems, provides unified governance, and supports diverse
ML workloads. This architecture accelerates data preparation,
improves data quality, and enables efficient feature engineering for
machine learning models.

**Common anti-patterns:**

- Creating isolated data silos where different teams manage
separate data stores without coordination.
- Building data architecture without establishing proper
governance, access controls, or compliance-aligned frameworks.
- Using one-size-fits-all storage solutions without considering
specific workload requirements.
- Relying on manual processes for data movement, transformation,
and quality checks.
- Neglecting to implement proper data cataloging and discovery
mechanisms.

**Benefits of establishing this best
practice:**

- Unified data governance and access control across data stores.
- Reduced data preparation time through integrated data services.
- Improved data quality and consistency for ML model training.
- Enhanced scalability for growing data volumes and ML workloads.
- Better cost optimization through purpose-built storage
solutions.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

When building machine learning solutions, you need a modern data
architecture that can handle diverse data types, support various
ML workloads, and provide unified governance across data stores.
This architecture enables efficient data movement between storage
systems while maintaining security, quality, and cost
optimization.

Avoid creating isolated data silos where different teams manage
separate data stores without coordination. Many organizations
struggle with inconsistent data governance policies across
different storage systems, lack unified access controls for ML
teams, fail to implement proper data cataloging and discovery
mechanisms, and neglect to optimize storage costs based on access
patterns. These issues create bottlenecks in ML workflows and
increase operational complexity.

For example, in a retail ML use case, you might need to combine
customer transaction data from a data warehouse, real-time
clickstream data from streaming services, and product catalog
information from operational databases. A modern data architecture
enables seamless access to these data sources while maintaining
consistent security policies and enabling efficient feature
engineering for recommendation models.

Different ML workloads require different data access patterns.
Batch training jobs benefit from optimized data lake storage with
efficient querying capabilities, while real-time inference
requires low-latency access to feature stores and streaming data
pipelines. Custom data processing workflows can be developed when
standard ETL processes don't adequately support your specific ML
requirements.

Continuous monitoring of data quality and pipeline performance is
crucial for maintaining reliable ML systems. Setting up automated
data quality checks and pipeline monitoring allows for early
detection of data issues that could impact model performance.

### Implementation steps

- **Design your data lake
foundation**. Begin by establishing a centralized
data lake using
[Amazon S3](https://aws.amazon.com/s3/) as the primary storage layer. Organize data using
a logical structure that supports both current and future ML
use cases, such as organizing by business domain, data
source, and processing stage. Implement data partitioning
strategies based on common query patterns to optimize
performance and reduce costs. For example, partition
time-series data by date and customer data by region to
enable efficient querying for ML feature extraction.
- **Implement unified data
governance**. Use
[AWS Lake Formation](https://docs.aws.amazon.com/lake-formation/latest/dg/what-is-lake-formation.html) to build a scalable and secure data
lake with centralized governance. Establish consistent
security policies, access controls, and audit trails across
data stores. Apply fine-grained permissions that enable
self-service access for ML practitioners while maintaining
security and and addressing requirements. Create data
stewardship roles and processes to improve ongoing data
quality and governance.
- **Integrate purpose-built analytics
services**. Build a high-speed analytic layer with
purpose-built services selected based on your specific ML
workload requirements:

Use
[Amazon Redshift](https://aws.amazon.com/redshift/) for data warehousing and complex
analytical queries
- Implement
[Amazon Kinesis](https://aws.amazon.com/kinesis/) for real-time streaming data processing
- Deploy
[Amazon Athena](https://aws.amazon.com/athena/) for interactive queries and ad-hoc
analysis
- Consider
[Amazon DynamoDB](https://aws.amazon.com/dynamodb/) for high-performance operational
workloads
- Use
[Amazon Timestream](https://aws.amazon.com/timestream/) for time-series data applications

- **Enable seamless data
integration**. Use
[AWS Glue](https://aws.amazon.com/glue/) to integrate data across services and data
stores. Implement automated data cataloging to maintain
metadata and enable data discovery across your organization.
Create ETL pipelines that prepare data for ML workloads
while maintaining data lineage and enabling reproducibility.
Design workflows that can handle both batch and streaming
data processing requirements.
- **Optimize for ML
workloads**. Design data pipelines that support
both batch and real-time ML training scenarios. Implement
feature stores using services like
[Amazon SageMaker AI Feature Store](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store.html) to manage and share ML
features across teams and models. Create standardized
feature engineering processes that can be reused across
different ML projects and provide consistent data
transformations.
- **Establish data quality
monitoring**. Implement automated data quality
checks and monitoring for data reliability for ML models.
Use
[AWS Glue DataBrew](https://aws.amazon.com/glue/features/databrew/) for data profiling and quality
assessment. Set up automated alerts for data quality issues
such as missing values, schema changes, or statistical
anomalies that could impact ML model performance.
- **Implement cost optimization
strategies**. Use appropriate storage classes in
Amazon S3 based on data access patterns. Implement lifecycle
policies to automatically transition data to lower-cost
storage tiers such as S3 Infrequent Access or Amazon Glacier for
archival data. Monitor and optimize query performance to
control compute costs, and use reserved capacity where
appropriate for predictable workloads.
- **Enable real-time data
processing**. For ML use cases requiring real-time
inference, implement streaming data pipelines using Amazon Kinesis and
[AWS Lambda](https://aws.amazon.com/lambda/) to process data as it arrives and update
feature stores in near real-time. Design architectures that
can handle varying data volumes and provide consistent
low-latency access to features for real-time ML predictions.
- **Implement data lineage and
versioning**. Establish comprehensive data lineage
tracking to understand data flow from source to ML models.
Use versioning for both datasets and feature definitions to
enable reproducible ML experiments and model rollbacks when
necessary. This is crucial for improving regulatory
adherence and debugging ML model issues.
- **Create self-service data
access**. Build data catalogs and discovery tools
that enable ML practitioners to find and access relevant
data without requiring deep technical knowledge of the
underlying storage systems. Implement standardized APIs and
interfaces that abstract the complexity of the data
architecture while providing the flexibility needed for
diverse ML workloads.

## Resources

**Related documents:**

- [The
lakehouse architecture of Amazon SageMaker AI](https://aws.amazon.com/sagemaker/lakehouse/)
- [Amazon SageMaker AI Unified Studio](https://aws.amazon.com/sagemaker/unified-studio/)
- [What
is AWS Lake Formation?](https://docs.aws.amazon.com/lake-formation/latest/dg/what-is-lake-formation.html)
- [AWS Lake Formation: How it works](https://docs.aws.amazon.com/lake-formation/latest/dg/how-it-works.html)
- [Create,
store, and share features with Feature Store](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store.html)
- [What
is AWS Glue?](https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html)
- [Modern
Data Architecture on AWS](https://aws.amazon.com/big-data/datalakes-and-analytics/data-lake-house/)
- [Amazon SageMaker AI Lakehouse | AWS Big Data
Blog](https://aws.amazon.com/blogs/big-data/category/analytics/amazon-sagemaker-lakehouse/)moving-from-notebooks-to-automated-ml-pipelines-using-amazon-sagemaker-and-aws-glue/)
- [Amazon SageMaker AI | AWS Big Data Blog](https://aws.amazon.com/blogs/big-data/category/artificial-intelligence/sagemaker/)

**Related videos:**

- [Understanding
Amazon S3 Tables: Architecture, performance, and
integration](https://www.youtube.com/watch?v=e1ypMWSHgsM)
- [Accelerate
your Analytics and AI with Amazon SageMaker AI LakeHouse](https://www.youtube.com/watch?v=qZTbS0xPN-U)
- [Unifying
data governance with Immuta and AWS Lake Formation](https://www.youtube.com/watch?v=X09-n2jJZKw)
- [The
lake house approach to data warehousing with Amazon Redshift](https://www.youtube.com/watch?v=35wXL0Q1Dcc)

**Related services:**

- [AWS Glue DataBrew](https://aws.amazon.com/glue/features/databrew/)
- [Amazon Kinesis Data Streams](https://aws.amazon.com/kinesis/data-streams/)
- [Amazon Athena](https://aws.amazon.com/athena/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlperf03-bp01.html*

---
