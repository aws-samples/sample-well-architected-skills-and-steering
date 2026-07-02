**Pillar**: Sustainability

# FSISUS10: Have you selected the storage class with the lowest carbon footprint?

Data is at the heart of strategic innovations for the financial services industry. This
can have many use cases ranging from providing hyperpersonalised experiences for customers,
training machine learning models to better understand risk and fraud detection. Each use
case requires different levels of data availability, processing, and storage and therefore
varies in storage technologies from transactional databases, to data lakes and data
warehouses. These come with various considerations from a sustainability perspective.

## FSISUS10-BP01 Balance your data performance requirements against its carbon footprint

### Prescriptive guidance

To balance data performance requirements against its carbon footprint:

- Define proxy metrics to monitor the business outcome of the data-involved
service in relation to their environmental impact. An example proxy metric could be
efficiency of the AI/ML service to help detect fraud faster (with the associated
cost saving) and the carbon footprint of training and storing the data. These proxy
metrics then become the vehicle to balance your performance requirements against its
carbon footprint. Proxy metrics can be collected by importing AWS Cost and Usage
Report as well as Amazon CloudWatch metrics into Amazon S3 and monitored using Amazon Athena and Quick.
- Use the right storage class for Amazon S3 Storage Classes based on the data
performance requirements. The storage class impacts the environmental impact of the
dataset through its access patterns and its architecture. For example, in [Amazon S3
One Zone-IA](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html), energy and server capacity are reduced because data is stored
only within one Availability Zone. Amazon

S3 Storage Classes can be configured at the object level and a single bucket can
contain objects stored across all of the storage classes.

- Learn more about [Amazon S3 Storage
Classes](https://aws.amazon.com/s3/storage-classes/) and their use cases.
- You can also use Amazon S3 lifecycle policies to transition objects automatically
between storage classes without application changes. In general, you must make a
trade-off between resource efficiency, access latency, and reliability when
considering these storage mechanisms.
- For storage systems that are a fixed size, such as Amazon EBS or Amazon FSx, monitor
the available storage space and automate storage allocation on reaching a threshold.
You can use Amazon CloudWatch to collect and analyze different metrics for [Amazon EBS](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using_cloudwatch_ebs.html) and [Amazon FSx](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/monitoring-cloudwatch.html).
- Avoiding the backup of unnecessary data can help lower cost and reduce the
storage resources used by the workload. Only back up data that has business value or
is needed to satisfy compliance requirements. Use [AWS Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html) for Amazon EFS or
Amazon Glacier Storage options for backup of infrequently accessed data.

Data types may include the following:

- Real-time analytics for financial services, including banking, payments,
insurance, and markets.
- Unstructured data such as biometrics, facial images, and documents.
- Structured data like fund movements or, transaction attempts.

## FSISUS10-BP02 Separate data into hot, warm, and cold storage

### Prescriptive guidance

- Implement a data classification policy to understand its criticality to
business outcomes and choose the right energy-efficient storage tier. Determine
criticality, confidentiality, integrity, and availability of data based on risk to
the organization.

Evaluate your data characteristics and access pattern to collect the key
characteristics of your storage needs. Key characteristics to consider include:

**Data type:** Structured, semistructured,
unstructured
- **Data growth:** Bounded, unbounded
- **Data durability:** Persistent, ephemeral,
transient
- **Access patterns:** Reads or writes,
frequency, spiky, or consistent

- Use these requirements to group data into one of the data classification tiers
that you adopt. For more detail on data classification categories, see the [Data
Classification whitepaper](https://docs.aws.amazon.com/whitepapers/latest/data-classification/data-classification.html).
- [AWSAWS Glue Data Catalog](https://docs.aws.amazon.com/glue/latest/dg/components-overview.html#data-catalog-intro) lets you store, annotate, and share metadata in the AWS
cloud while providing comprehensive audit and governance capabilities, to
periodically audit your environment for untagged and unclassified data and tag the
data appropriately.
- Optimize storage for generative AI training data and model artifacts using
appropriate storage classes.
- Implement data purification filters to reduce unnecessary generative AI
training data storage.
- Use columnar formats and compression for generative AI datasets.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsisus10.html*
