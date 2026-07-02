# MLSUS03 — Data processing

**Pillar**: Sustainability  
**Best Practices**: 3

---

# MLSUS03-BP01 Minimize idle resources

Minimize your environmental impact by efficiently managing compute
resources in your ML data pipeline. Use serverless architectures
that provision resources only when needed, reducing energy
consumption and carbon footprint.

**Desired outcome:** You implement a
serverless, event-driven architecture for your ML data pipelines
that only provisions resources when work needs to be done. This
approach reduces idle resources, optimizes utilization of computing
infrastructure, and reduces your organization's environmental impact
while maintaining performance and scalability.

**Common anti-patterns:**

- Provisioning compute instances that run 24/7 regardless of
workload requirements.
- Overprovisioning resources rather than scaling dynamically.
- Using traditional batch processing with fixed schedules instead
of event-driven approaches.
- Failing to monitor and optimize resource utilization metrics.

**Benefits of establishing this best
practice:**

- Lower carbon footprint and energy consumption.
- Improved resource efficiency across your ML pipeline.
- Automatic scaling to match workload demands.
- Simplified maintenance with managed services.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Adopting a serverless architecture for your ML data pipelines
significantly reduces idle resources by allocating compute power
only when needed. This approach uses AWS managed services that
automatically scale based on workload, avoiding the need to
maintain an always-on infrastructure. When you design your data
pipeline using serverless technologies like AWS Glue and AWS Step Functions, you not only optimize resource utilization but also
distribute the sustainability impact across the tenants of those
services, reducing your individual environmental contribution.

The key principle is to transition from a static infrastructure
model to an event-driven approach where resources are provisioned
in response to triggers. This verifies that compute resources are
only active during actual processing tasks rather than sitting
idle waiting for work. AWS managed services handle the underlying
infrastructure optimization, allowing you to focus on your ML
workloads while maintaining efficiency.

### Implementation steps

- **Evaluate your current
infrastructure**. Assess your existing data
pipeline architecture to identify components that run
continuously but have low utilization. Look for workloads
with predictable patterns or batch processes that could
benefit from an event-driven approach using
[AWS CloudWatch metrics](https://aws.amazon.com/cloudwatch/) to identify utilization patterns.
- **Adopt managed services**.
Replace self-managed infrastructure with AWS managed
services to distribute sustainability impact across service
tenants. Services like
[AWS Glue](https://aws.amazon.com/glue/),
[AWS Lambda](https://aws.amazon.com/lambda/), and
[Amazon EMR Serverless](https://aws.amazon.com/emr/serverless/) provision resources on-demand and
automatically scale with your workloads.
- **Create serverless, event-driven data
pipelines**. Use
[AWS Glue](https://aws.amazon.com/glue/) for data processing and
[AWS Step Functions](https://aws.amazon.com/step-functions/) for orchestration to build ETL and ELT
pipelines that only consume resources when triggered. Step
Functions can coordinate AWS Glue jobs efficiently,
provisioning compute resources only when needed and
releasing them immediately after completion.
- **Implement efficient data
storage**. Choose appropriate storage solutions
like [Amazon S3](https://aws.amazon.com/s3/) for your data lake and
[Amazon S3 Intelligent-Tiering](https://aws.amazon.com/s3/storage-classes/intelligent-tiering/) to automatically move data
between access tiers based on usage patterns, reducing
storage costs and resource waste.
- **Configure event-based
triggers**. Set up event notifications through
[Amazon EventBridge](https://aws.amazon.com/eventbridge/) to automatically launch processing jobs
when new data arrives. This avoids the need for scheduled
jobs that might run when no new data is available, reducing
unnecessary compute usage.
- **Optimize compute
resources**. For AWS Glue jobs, configure
appropriate worker types and dynamically allocate resources
based on workload requirements. Use features like
[AWS Glue Auto Scaling](https://docs.aws.amazon.com/glue/latest/dg/auto-scaling.html) to automatically adjust capacity as
needed during jobs.
- **Implement monitoring and
metrics**. Set up comprehensive monitoring of your
serverless infrastructure using
[Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) to track resource utilization, job
execution time, and idle periods. Use these metrics to
identify further optimization opportunities.
- **Establish automatic cleanup
processes**. Implement automated processes to
remove temporary resources, intermediate data, and other
artifacts after job completion to avoid unnecessary storage
costs and reduce digital waste.
- **Optimize data transfer**.
Minimize data movement between services by processing data
close to where it's stored when possible. Use
[AWS Glue DataBrew](https://aws.amazon.com/glue/features/databrew/) for data preparation tasks within the
same environment as your data storage.
- **Use AI-powered
optimization**. Use Amazon Q data integration in
AWS Glue to automatically generate optimized ETL jobs for
common data sources. This reduces development time while
implementing efficient resource utilization patterns from
the start.

## Resources

**Related documents:**

- [What
is AWS Lambda?](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)
- [What
is Amazon EMR Serverless?](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/emr-serverless.html)
- [Using
auto scaling for AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/auto-scaling.html)
- [What
is Amazon EventBridge?](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html)
- [Start
an AWS Glue job with Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/connect-glue.html)
- [Serverless
Applications Lens - AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/serverless-applications-lens/welcome.html)
- [Optimize
AI/ML workloads for sustainability: Part 3, deployment and
monitoring](https://aws.amazon.com/blogs/architecture/optimize-ai-ml-workloads-for-sustainability-part-3-deployment-and-monitoring/)
- [Fuel
your data with Generative AI](https://aws.amazon.com/blogs/enterprise-strategy/fuel-your-data-with-generative-ai/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlsus03-bp01.html*

---

# MLSUS03-BP02 Implement data lifecycle policies aligned with your sustainability goals

Classify your data to identify its business relevance and implement
efficient storage strategies that support your sustainability goals.
By understanding your data's importance, you can appropriately tier
storage, implement retention policies, and manage the entire
lifecycle to reduce your environmental footprint while meeting
business requirements.

**Desired outcome:** You have a
comprehensive data management strategy that classifies data based on
business importance and implements automatic storage optimization.
Your workloads store data in the most energy-efficient storage tiers
possible, and data that no longer serves a business purpose is
automatically purged, resulting in minimal storage footprint and
reduced environmental impact.

**Common anti-patterns:**

- Storing data indefinitely without classification or lifecycle
policies.
- Using a single storage tier for data regardless of access
patterns.
- Manually managing data retention and deletion.
- Keeping redundant or obsolete data that no longer serves
business purposes.

**Benefits of establishing this best
practice:**

- Reduced storage infrastructure and energy consumption.
- Improved data governance and adherence.
- Enhanced system performance with streamlined data management.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Implementing data lifecycle policies begins with understanding the
relationship between your data and business outcomes. Each
category of data has different requirements for retention, access
patterns, and eventual disposal. By aligning these requirements
with sustainability goals, you can optimize storage utilization
while improving business continuity.

Start by creating a data classification framework that categorizes
data based on its criticality, frequency of access, and business
value over time. This classification will guide your decisions
about which storage tiers to use and when data should be moved or
deleted. For instance, frequently accessed operational data might
remain in high-performance storage, while rarely accessed archival
data can be moved to more energy-efficient cold storage options.

Once you've classified your data, use AWS storage features like S3
Lifecycle policies to automate data transitions between storage
tiers and eventual deletion. For example, you can configure
policies that automatically transition data from S3 Standard to S3
Intelligent-Tiering, S3 Standard-IA, S3 One Zone-IA, and
eventually to Amazon Glacier or S3 Glacier Deep Archive based on
access patterns and age.

### Implementation steps

- **Define your data classification
framework.** Develop a comprehensive data
classification system that categorizes data based on
business importance, access frequency, and regulatory
requirements. Include clear definitions for each data
category and establish ownership for classification
decisions.
- **Map retention requirements to data
classes.** For each data classification, determine
appropriate retention periods that satisfy business needs,
regulatory requirements, and sustainability goals. Document
these requirements to guide policy implementation.
- **Analyze current storage usage
patterns.** Use
[Amazon S3 Storage Lens](https://aws.amazon.com/s3/storage-analytics-insights/) to gain visibility into your current
storage usage patterns, identifying opportunities for
optimization and tracking progress on storage efficiency
metrics.
- **Implement S3 Lifecycle
policies.** Configure
[Amazon S3 Lifecycle policies](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html) to automatically transition
data between storage classes and enforce deletion timelines
based on your defined retention requirements.
- **Deploy intelligent storage
tiering.** Implement
[Amazon S3 Intelligent-Tiering storage class](https://aws.amazon.com/s3/storage-classes/intelligent-tiering/) to automatically
move data between access tiers based on changing access
patterns, optimizing for both cost and sustainability.
- **Establish monitoring and
reporting.** Create dashboards to track storage
optimization metrics, including total storage used, storage
class distribution, and lifecycle transition metrics.
Regularly review these metrics to identify further
optimization opportunities.
- **Continuously refine data
classification.** Review and update your data
classification framework regularly to align it with evolving
business needs and sustainability goals.

## Resources

**Related documents:**

- [Managing
the lifecycle of objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html)
- [Managing
storage costs with Amazon S3 Intelligent-Tiering](https://docs.aws.amazon.com/AmazonS3/latest/userguide/intelligent-tiering.html)
- [Comparing
the Amazon S3 storage classes](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html#sc-compare)
- [Assessing
your storage activity and usage with Amazon S3 Storage
Lens](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage_lens.html)
- [Setting
an S3 Lifecycle configuration on a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/how-to-set-lifecycle-configuration-intro.html)
- [Data
discovery and cataloging in AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/catalog-and-crawler.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlsus03-bp02.html*

---

# MLSUS03-BP03 Adopt sustainable storage options

Reduce the volume of data to be stored and adopt sustainable storage
options to limit the carbon impact of your workload. For artifacts
like models and log files that must be kept for long-term regulatory
and audit requirements, use efficient compression algorithms and use
energy efficient cold storage.

**Desired outcome:** You optimize
your ML workload storage to minimize environmental impact while
improving adherence to regulatory requirements. By implementing
efficient storage practices, you reduce data redundancy, properly
size resources, use energy-efficient storage options, and implement
effective compression techniques. This results in reduced carbon
footprint, lower storage costs, and improved overall sustainability
of your ML systems.

**Common anti-patterns:**

- Storing redundant copies of datasets across multiple locations.
- Over-provisioning storage resources for notebooks and instances.
- Using inefficient file formats like CSV instead of columnar
formats such as parquet.
- Keeping data in high-performance storage regardless of access
frequency.

**Benefits of establishing this best
practice:**

- Lower operational costs through efficient resource utilization.
- Improved data access performance through appropriate format
selection.
- Improved ability to adhere to regulatory requirements through
proper long-term storage planning.
- Reduced waste through optimization of storage resources.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Storage is a critical component of ML workloads, with large
datasets and model artifacts requiring significant resources. By
optimizing how you store, compress, and manage this data, you can
substantially reduce the environmental impact of your ML systems.
Consider the entire lifecycle of your data, from initial
collection through processing to long-term retention. For
frequently accessed data, choose efficient formats and compression
algorithms. For infrequently accessed data, use Amazon S3 storage
tiers that minimize energy consumption while improving your
adherence to regulatory requirements. By right-sizing your storage
resources and removing redundant data, you can achieve both
sustainability goals and cost optimization.

### Implementation steps

- **Reduce redundancy of processed
data**. If you can re-create an infrequently
accessed dataset, use the
[Amazon S3 One Zone-IA](https://aws.amazon.com/s3/storage-classes/#__) class to minimize the total data
stored. Implement S3 Lifecycle policies to automatically
transition objects to more energy-efficient storage tiers
based on access patterns.
- **Right size block storage for
notebooks**. Don't over-provision block storage of
your notebooks and use centralized object storage services
like [Amazon S3](https://aws.amazon.com/s3/) for common datasets to avoid data duplication.
Monitor usage patterns and adjust storage allocations
accordingly.
- **Use efficient file
formats**. Use
[Parquet](https://parquet.apache.org/)
to train your models. Compared to CSV, they can reduce
[your
storage by up to 87%](https://docs.aws.amazon.com/whitepapers/latest/building-data-lakes/monitoring-optimizing-data-lake-environment.html#data-lake-optimization2). These columnar formats not only
reduce storage requirements but also improve query
performance.
- **Migrate to more efficient
compression algorithms**. Evaluate different
compression algorithms and select the most efficient for
your data. For example,
[Zstandard](https://github.com/facebook/zstd)
produces 10–15% smaller files than
[Gzip](https://www.gzip.org/) at the
same compression speed.
- **Implement storage lifecycle
management**. Configure
[S3
Intelligent-Tiering](https://aws.amazon.com/s3/storage-classes/intelligent-tiering/) to automatically move data
between access tiers based on changing usage patterns. For
long-term archival needs, use
[S3 Glacier Deep Archive](https://aws.amazon.com/s3/storage-classes/glacier/) to minimize energy consumption
for rarely accessed data.
- **Monitor and optimize storage
utilization**. Regularly review and clean up
unnecessary data and snapshots. Use
[Amazon S3 Storage Lens](https://aws.amazon.com/s3/storage-analytics-insights/) to gain visibility into usage
patterns and identify optimization opportunities across your
organization.
- **Centralize and share
datasets**. Implement a centralized data catalog
using
[AWSAWS Glue Data Catalog](https://docs.aws.amazon.com/glue/latest/dg/catalog-and-crawler.html) to make datasets discoverable and
reusable, reducing the need for multiple copies of the same
data.
- **For generative AI workloads, use AI
for intelligent data management**. Implement
embeddings storage with efficient vector databases like
[Amazon OpenSearch Service](https://aws.amazon.com/opensearch-service/) to optimize storage of large language
model context.

## Resources

**Related documents:**

- [Understanding
and managing Amazon S3 storage classes](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html)
- [Managing
storage costs with Amazon S3 Intelligent-Tiering](https://docs.aws.amazon.com/AmazonS3/latest/userguide/intelligent-tiering.html)
- [Amazon S3 Storage Analytics and Insights](https://aws.amazon.com/s3/storage-analytics-insights/)
- [AWS Well-Architected Framework: Performance Efficiency Pillar -
Data Management](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/data-management.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlsus03-bp03.html*

---
