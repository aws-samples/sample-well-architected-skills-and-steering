# ADVPERF03 — Data storage selection

**Pillar**: Performance Efficiency  
**Best Practices**: 3

---

# ADVPERF03-BP01 Choose appropriate block storage options to power your advertising workload

Block storage is crucial for data storage in the cloud. Customers
need to choose the appropriate block storage service based on
different types of workloads, as well as their requirements for
storage performance and stability.

## Implementation guidance

[Amazon EBS](https://aws.amazon.com/ebs/) provides persistent block-level storage
volumes for use with Amazon Elastic Compute Cloud (Amazon EC2) instances. In the advertising industry, Amazon EBS can be
used to store databases, such as MySQL or PostgreSQL, that power ad servers, bid management
systems, and other critical components. Amazon EBS volumes can be easily scaled and optimized for
different workload patterns, which provides high performance and reliability.

- **Volume types:** Choose the
appropriate EBS volume type based on your workload. For
general-purpose workloads, use GP3 volumes. For
high-performance needs, consider IO2 volumes. If you need
high performance, you'll need to use
[EC2
Instance Store](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html?utm_source=simpleaws&utm_medium=referral&utm_campaign=amazon-ebs-basics-and-best-practices). It's ephemeral block storage with a
much higher performance than EBS.
- **EBS-optimized instances:** Use Amazon EBS-optimized Amazon EC2
instances to provide dedicated throughput between your instances and Amazon EBS volumes. For
example, use Amazon EBS-optimized Amazon EC2 instances and provisioned IOPS volumes for real-time
bidding or ad serving. workloads.
- **Encryption:** Enable encryption by default for all Amazon EBS
volumes to meet security and compliance requirements.
- **Snapshot management:** Regularly create and manage Amazon EBS
snapshots for backup and disaster recovery. Use AWS Data Lifecycle Manager to automate
snapshot management.
- **Performance monitoring:**
Use Amazon CloudWatch metrics to monitor and optimize EBS
health and performance.
- **Scaling:** Leverage Amazon EBS Elastic Volumes to increase the
size of Amazon EBS volumes dynamically without disrupting your applications.

## Resources

- [Amazon EBS volume types](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volume-types.html)
- [Amazon EBS volume performance](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-performance.html)
- [Monitoring
tools for Amazon EBS](https://docs.aws.amazon.com/ebs/latest/userguide/monitoring-overview.html)
- [Automate
backups with Amazon Data Lifecycle Manager](https://docs.aws.amazon.com/ebs/latest/userguide/snapshot-lifecycle.html)
- [What
is Amazon Elastic Block Store?](https://docs.aws.amazon.com/ebs/latest/userguide/work-with-ebs-encr.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advperf03-bp01.html*

---

# ADVPERF03-BP02 Use object storage to store and analyze raw data from ad servers, DSPs, and DMP

Object storage can be used to store massive amounts of data while
balancing cost and performance. Customers can use object storage
services to build data lakes and analyze this data to uncover
valuable insights and achieve business goals.

## Implementation guidance

[Amazon S3](https://aws.amazon.com/s3/) is a highly scalable and durable object
storage service that can store and protect any amount of data for a range of use cases. It
is ideal for storing and serving static content, such as images, videos, and other media
assets used in advertising campaigns. Amazon S3 also supports data lakes, which you can use to
store and analyze vast amounts of raw data from various sources, including ad servers,
demand-side platforms (DSPs), and data management platforms (DMPs).

- **[Amazon S3 Express One Zone](https://aws.amazon.com/s3/storage-classes/express-one-zone/):** A powerful storage class for
performance-critical applications, including advertising model training. Its low
latency, high throughput, and cost efficiency makes it an ideal choice for real-time ad
placement, machine learning for ad personalization, and interactive analytics.
- **Data partitioning:** Use
multiple prefixes to partition your data, which distributes
the load and improves performance. For example, instead of
storing all objects under a single prefix, use multiple
prefixes like `s3://bucket-name/prefix1/` and
`s3://bucket-name/prefix2/`.
- **Data transfer:** Use Amazon S3 Transfer Acceleration to speed up data transfers over
long distances, improving the performance of data ingestion
and distribution processes.
- **Monitoring and auditing:**
Use AWS CloudTrail and Amazon CloudWatch to monitor S3
access and performance metrics.
- **Storage tiering and
class:** Each object in Amazon S3 has a
[storage
class](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html) associated with it. Choosing a storage class
designed for your use case lets you optimize storage costs,
performance, and availability for your objects. Use the S3
Intelligent-Tiering storage class, which is designed to
optimize storage costs by automatically moving data to the
most cost-effective access tier when access patterns change,
without operational overhead or impact on performance. S3
Intelligent-Tiering monitors access patterns and
automatically moves objects that have not been accessed to
lower-cost access tier.

## Resources

- [Getting
started with S3 Express One Zone](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-getting-started.html)
- [Setting
an S3 Lifecycle configuration on a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/how-to-set-lifecycle-configuration-intro.html)
- [Protecting
data with server-side encryption](Users/jblatch/Downloads/%E2%80%A2%20https:/docs.aws.amazon.com/AmazonS3/latest/userguide/serv-side-encryption.html)
- [Monitoring
metrics with Amazon CloudWatch](https://docs.aws.amazon.com/AmazonS3/latest/userguide/cloudwatch-monitoring.html)
- [Manage
Amazon S3 storage costs granularly and at scale using S3 Intelligent-Tiering](https://aws.amazon.com/blogs/storage/manage-amazon-s3-storage-costs-granularly-and-at-scale-using-s3-intelligent-tiering/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advperf03-bp02.html*

---

# ADVPERF03-BP03 Use a cloud file system to store shared data between applications

File storage services (such as Amazon EFS) provide a simple way to
set up and scale file systems and are widely used for big data and
analytics workloads, media processing workflows, and content
management scenarios. They are well-suited for distributed
workloads and applications that need to share files across
multiple EC2 instances.

## Implementation guidance

[Amazon EFS](https://aws.amazon.com/efs/)
is a scalable and fully managed cloud file system that provides
a simple, serverless way to share file data across AWS Cloud
services and on-premises resources. In the advertising industry,
Amazon EFS can be used to store and share log files,
configuration files, and other data that needs to be accessed
concurrently by multiple applications or instances. This is
particularly useful for log processing and analysis pipelines,
where data needs to be shared across multiple stages.

- **[Performance
modes](https://docs.aws.amazon.com/efs/latest/ug/performance.html#performancemodes):** Amazon EFS offers both General
Purpose and Max I/O performance modes.
- **[Throughput
modes](https://docs.aws.amazon.com/efs/latest/ug/performance.html#throughput-modes):** Choosing the correct throughput mode for your file system
depends on your workload's performance requirements.
- **Cost optimization:** Use Amazon EFS lifecycle policies to
automatically move infrequently accessed files to the [EFS Infrequent Access](https://aws.amazon.com/efs/features/infrequent-access/) storage class,
reducing stor
- **High availability:** Create Amazon EFS mount targets in all
availability zones to provide high availability and low latency access to your file
system.
- age costs.

## Resources

- [Encrypting
data in Amazon EFS](https://docs.aws.amazon.com/efs/latest/ug/encryption.html)
- [Create an Amazon EFS
file system and mount it on an Amazon EC2 instance using the AWS CLI](https://docs.aws.amazon.com/efs/latest/ug/wt1-getting-started.html)
- [Mounting
considerations for Linux](https://docs.aws.amazon.com/efs/latest/ug/mounting-fs-mount-cmd-general.html)
- [Managing
automatic backups of Amazon EFS file systems](https://docs.aws.amazon.com/efs/latest/ug/automatic-backups.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advperf03-bp03.html*

---
