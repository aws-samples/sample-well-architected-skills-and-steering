**Pillar**: Performance Efficiency

# FSIPERF03: How do you select your storage architecture?

AWS offers a wide range of storage options and as with compute, the best performance
is obtained when targeting the specific storage needs of an application.

## FSIPERF03-BP01 Select your storage architecture based on workload requirements

When you select a storage solution, verify that it aligns with your access patterns to
achieve the desired performance. It is simple to experiment with different storage types
and configurations without having to make commitments.

Financial services grid compute workloads can take advantage of Amazon FSx for Lustre, which
provides a fully managed file system that’s optimized for the performance and costs of
workloads requiring file system access across thousands of Amazon EC2 instances, optionally
backed by an S3 bucket, which makes it simple for clients to persist input and results of
the calculations.

Consider whether your solutions can make use of caching services to improve
performance, by storing frequently used data in memory, or bringing data closer to
consumers. Many AWS services offer features for caching or dedicated services including
Amazon ElastiCache, and Amazon File Cache.

Financial services solutions have historically made use of databases as a key
component, often to verify transactional integrity, and here AWS also offers a wide
range of database options. Select database options that align with your performance
requirements, using different database technologies for different purposes, such as
Amazon Timestream time-series database for storing ticking market data, rather than a
one-size-fits-all use of traditional relational databases.

## FSIPERF03-BP02 Consider changing needs over the entire lifecycle of your data

Financial services workloads often have requirements to keep data available for many
years to help meet regulatory requirements, leading to significant amounts of data being
retained. Amazon S3 and Amazon Glacier storage classes provide the optimal solution for many data
retention requirements with their almost unlimited capacity and predictable performance.
Consider the use of the services’ own lifecycle policies (supported by Amazon Elastic File System and Amazon S3
among others) to help meet your requirements. These services offer integrated
lifecycle-based policies for moving data between tiers of storage based on access patterns
and user-defined requirements. If the features of a single service do not meet your
requirements, combine multiple storage services to satisfy requirements, rather than
selecting a single storage service to help meet your requirements, for example persisting
Amazon FSx for Lustre file systems to Amazon S3 for long-term, low-cost retention. Note that costs
for the service remain low, provided that the services are restricted to a single
AWS Region.

## FSIPERF03-BP03 Optimize storage for AI model and data requirements

AI workloads in financial services generate unique storage
requirements due to large model files, extensive training
datasets, and real-time inference data needs. Optimize storage
architecture to support AI model lifecycle management and data
processing pipelines.

**Storage optimization
strategies:**

- Use Amazon S3 with S3 Transfer Acceleration for fast model
artifact uploads and downloads.
- Use Amazon FSx for Lustre for high-throughput access to
large financial datasets during model training.
- Use Amazon ElastiCache to cache frequently accessed model
predictions and reference data.
- Implement S3 versioning and lifecycle policies for model
artifact management.

**Performance considerations for
financial AI storage:**

- Use Amazon EBS gp3 volumes with provisioned IOPS for
consistent I/O performance during model training.
- Implement data partitioning strategies to optimize access
patterns for time-series financial data.
- Configure cross-region replication for disaster recovery of
critical AI models and training data.
- Use Amazon S3 Intelligent Tiering to automatically optimize
costs for infrequently accessed training datasets.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsiperf03.html*
