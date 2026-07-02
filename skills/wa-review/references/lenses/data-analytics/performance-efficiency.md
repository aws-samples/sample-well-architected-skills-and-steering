# Performance efficiency

**Pages**: 10

---

## 8 – Choose the best-performing compute solution

# Best practice 8.1 – Identify analytics solutions that best suit your technical challenges

AWS has multiple analytics processing services that are
built for specific purposes. These include Amazon Redshift
for data warehousing, Amazon Kinesis for streaming data, and
Quick for data visualization. Your organization
should consider each step of the data analytics process as
an opportunity to identify the right tool for the job.

## Suggestion 8.1.1 – Identify the requirements based on the collected business metrics

Applications and services are designed to overcome
specific challenges. It’s essential that your organization
identifies the right tool for the right job to meet your
business and technical requirements. Choosing inappropriate technology can introduce performance issues,
especially when processing data at scale.

For more details, refer to the following information:

- AWS Right Tool for the Job:
[Databases
on AWS: The Right Tool for the Right Job](https://www.youtube.com/watch?v=WE8N5BU5MeI)
- AWS Right Tool for the Job:
[How
to Choose the Right Database](https://aws.amazon.com/startups/start-building/how-to-choose-a-database/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/best-practice-8.1-identify-analytics-solutions-that-best-suit-your-technical-challenges..html*

---

# Best practice 8.2 – Provision the compute resources to the location of the data storage

Data analytics workloads require moving data through a
pipeline, either for ingesting data, processing intermediate
results, or producing curated datasets. It is often
more efficient to select the location of data processing
services near where the data is stored. This approach is
preferred instead of copying or streaming large amounts
of data to the processing location. For example, if an
Amazon Redshift cluster frequently ingests data from a data
lake, ensure that the Amazon Redshift cluster is in the same
Region as your data lake S3 buckets.

This extends to considering where your compute and storage are located at the Availability Zone level. Co-locating in the same Availability Zone allows fast, lower latency access. It is still important, however, to replicate data across zones when required.

## Suggestion 8.2.1 – Migrate or copy primary data stores from on-premises environments to AWS so that cloud compute and storage are closely located

Minimize duplication of data when transferring datasets from on-premises storage to the cloud. Instead, create copies of your data near the analytics platform to avoid data transfer latency and improve overall performance of the analytics solution. For optimal performance, keep your data and analytics systems in the same AWS Region. If they are in separate Regions, relocate one of them.

## Suggestion 8.2.2 – Consider where your analytics resources are placed

For optimal performance, your organization should align the location of the data with the location of the resources that process it. Where possible, your organization should
consider using a permanent Region for all data analytics
processing as this will help with data transferring
overhead.

## Suggestion 8.2.3 – Consider the use of provisioned compared to serverless offerings to match your workload pattern

When considering services for ingesting, transforming, and analyzing your data, there is often the choice between provisioned or serverless solutions. There are many trade-offs and potential advantages of each, but from a performance perspective, it can be beneficial to use serverless offerings when your workloads are consistently and unpredictably spikey. Whereas provisioned deployments may offer advantages when you have more stable, predictable workloads.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/best-practice-8.2---provision-the-compute-resources-to-the-location-of-the-data-storage..html*

---

# Best practice 8.3 – Define and measure the computing performance metrics

Define how you will measure performance of the analytics
solutions for each step in the process. For example, if the
computing solution is a transient Amazon EMR cluster, you
can take the following approach. Define the performance as
the Amazon EMR job runtime from the launch of the EMR
cluster, process the job, then shut down the cluster. As
another example, if the computing solution is an Amazon Redshift cluster that is shared by a business unit, you can
define the performance as the runtime duration for each SQL
query.

## Suggestion 8.3.1 – Define performance efficiency metrics

Collect and use metrics to scale the resources to meet
business requirements. By doing so, your team can track
unexpected spikes to make future improvements.

## Suggestion 8.3.2 – Continually identify under-performing components and ﬁne-tune the infrastructure or application logic

After you have deﬁned the performance measurement, you should identify which infrastructure components or jobs are running below the performance criteria. Performance ﬁne-tuning varies for each AWS service, but generally, optimizing queries or workloads can enhance performance without necessitating infrastructure modifications. For example, if it is an Amazon EMR cluster running a Spark application, you could explore tuning your Spark configuration. If after fine-tuning you still need more performance, you can change to a larger cluster instance type, or increase the number of cluster nodes.

For an Amazon Redshift cluster, you can ﬁne-tune the SQL queries that are running below the performance criteria and if required, increase the number of cluster nodes to increase parallel computing capacity.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/best-practice-8.3---define-and-measure-the-computing-performance-metrics..html*

---

## 9 – Choose the best-performing storage solution

# Best practice 9.1 – Identify critical performance criteria for your storage workload

In data analytics, throughput is often a constraining
factor to enable your workloads to run effectively.
Throughput is measured by the amount of information that has
successfully moved through the network, compute, or storage
layers. Improving throughput in each of these layers
generally results in better query performance.

## Suggestion 9.1.1 – Use performance monitoring tools to determine if the analytics system performance is limited by compute, storage, or networking

Use a metric collection and reporting system, such as
Amazon CloudWatch, to analyze the performance
characteristics of the analytics system. Evaluate the
measured performance metrics relative to system reference
documentation to characterize the system constraints for
the workload as a percentage of maximum performance.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/best-practice-9.1---identify-critical-performance-criteria-for-your-storage-workload..html*

---

# Best practice 9.2 – Identify and evaluate the available storage options for your compute solution

Many AWS data analytics services allow you to use more than
one type of storage. For example, Amazon Redshift allows
access to data stored in the compute nodes in addition to
data stored in Amazon S3. When performing research on each
data analytics service, evaluate relevant storage options
to determine the most performance efficient solution that
meets business requirements.

## Suggestion 9.2.1 – Review the available storage options for the analytics services being considered

There are often multiple storage options available for each service, each offering different characteristics and potentially performance benefits. It is important to review these available options and determine which may best fit your requirements.

For example, Amazon EMR provides local storage via HDFS
file system and Amazon S3 as an external storage via EMRFS.
For more information, refer to the AWS documentation for
your compute solution:

- Amazon EMR Management Guide:
[Work
with storage and file systems](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-file-systems.html)
- Amazon Redshift Cluster Management Guide:
[Overview
of Amazon Redshift clusters](https://docs.aws.amazon.com/redshift/latest/mgmt/working-with-clusters.html#working-with-clusters-overview)
- Amazon OpenSearch Service Developer Guide:
[Managing](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managing-indices.html)
[indices
in Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managing-indices.html)
- Amazon Aurora User Guide:
[Overview
of Aurora storage](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Overview.StorageReliability.html#Aurora.Overview.Storage)

## Suggestion 9.2.2 – Evaluate the performance of the selected storage option

To ensure that the overall analytics system design meets
your non-functional requirements, evaluate the performance
by running simulated real-world tests in a test
environment.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/best-practice-9.2-identify-evaluate-available-storage-options.html*

---

# Best practice 9.3 – Choose the optimal storage based on access patterns, data growth, and the performance requirements

Storage options for data analytics can have performance
tradeoffs based on access patterns and data size. For
example, in Amazon S3, can be much more efficient to retrieve a smaller number of larger objects, as opposed to a larger number of smaller objects.

Evaluate your workload needs and usage patterns
to determine if the method or location of storing your data
can improve the overall efficiency of your solution.

## Suggestion 9.3.1 – Identify available solution options for the performance improvement

When data I/O is limiting performance and business
requirements are not being met, improve I/O through the
options available within that service. For example, with
EBS volumes of GP3 type, increase Provisioned IOPS or
throughput, or for Amazon Redshift, increase the number of
nodes.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/best-practice-9.3---choose-the-optimal-storage-based-on-access-patterns-data-growth-and-the-performance-metrics..html*

---

## 10 – Choose the best-performing file format and partitioning

# Best practice 10.1 – Select format based on data write frequency and patterns for append-only compared to in-place update

Review your data storage write patterns and performance requirements for streaming and batch workloads. Streaming workloads may require you to write smaller files at a higher frequency compared to batch workloads. This enables your streaming applications to reduce latency but can impact read and write performance of the data.

## Suggestion 10.1.1 – Understand your analytics workload data’s write characteristics

If storing data in Amazon S3, evaluate if an append-only
method, such as Apache Hudi, is right for your needs.

There are also table formats available, such as Apache Hudi, Apache Iceberg and Delta Lake that can, amongst other capabilities, provide transactional semantics over data tables in Amazon S3. These formats can also provide improved query times through the use of additional metadata. For more detail on getting started with these formats, see [Introducing native support for Apache Hudi, Delta Lake, and Apache Iceberg on AWS Glue for Apache Spark, Part 1: Getting Started](https://aws.amazon.com/blogs/big-data/part-1-getting-started-introducing-native-support-for-apache-hudi-delta-lake-and-apache-iceberg-on-aws-glue-for-apache-spark/).

## Suggestion 10.1.2 – Avoid querying data stored in many small files

Rather than running queries over many small data ﬁles, periodically combine the small ﬁles into a single larger compressed ﬁle for analytics. This approach provides better data retrieval performance when using analytics services. Keep in mind that in streaming use cases there is a tradeoff between latency and throughput, as time is required to batch records. The production of larger files can be done as a post process job rather than necessarily at the point of ingestion.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/best-practice-10.1-select-format-based-on-data-write-frequency-and-patterns-for-append-only-vs.-in-place-update..html*

---

# Best practice 10.2 – Choose data formatting based on your data access pattern

Choosing the right data type for your workload is important. There are many different data types available to support your workload. Choosing the right format is a key step in the performance optimization of your analytics workloads.

## Suggestion 10.2.1 – Decide the correct data format for your analytics workload

You can work on unstructured, semi-structured, and structured data formats (CSV,
JSON, or columnar formats such as Apache Parquet and Apache ORC) with your data stored in Amazon S3 by using Amazon Athena, which lends itself to querying data as-is without the need for data preparation or ETL processes.

You should also consider compression when choosing data formats. Efficient compression can help queries run faster and reduce cost. It can also lead to reductions in the amount of data stored in a storage layer, alongside improved network and I/O throughput. For more information on when to use compression, see 10.3.2.

Using splittable formats is also an option. These formats allow individual files to be broken up so that they can be processed in parallel by multiple workers. Similarly to compression, this can also lead to reductions in query time. Often, you need to choose between compression or splittable formats because applying both is currently not well supported for analytics workloads.

## Suggestion 10.2.2 – API-driven data access pattern constraints, such as the amount of data retrieved per API call, can impact overall performance

If you are calling APIs to ingest, transform or access data, many implement a maximum amount of data or records that can be returned in a call. So, your solution may need to page through and make subsequent API calls to retrieve all results. If a large amount of data is returned this can lead to a long amount of time being spent retrieving the data in this manner. Most APIs have limits and constraints, such as number of calls in a particular time limit, so it is important to consider this, and relevant strategies for dealing with these conditions.

Result caching on API sources can help speed up reads if the same or similar data is frequently queried. Using asynchronous methods can help avoid blocking calls in your processing that would otherwise have to wait for synchronous operations to complete.

## Suggestion 10.2.3 – Use data, results, and query cache to improve performance and reduce reads from the storage tier

Caching services can speed up the responses to common
queries and reduce the load on the storage tier. Use
Amazon ElastiCache, DynamoDB Accelerator (DAX), API
gateway caching, Athena query result reuse, Amazon Redshift Advanced Query Accelerator (AQUA), or other relevant caching services.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/best-practice-10.2-choose-data-formatting-based-on-your-data-access-pattern..html*

---

# Best practice 10.3 – Utilize compression techniques to both decrease storage requirements and enhance I/O efficiency

Store data in a compressed format to reduce the burden on
the underlying storage host and network. For example, for
columnar data stored in Amazon S3, use a compatible
compression algorithm that supports parallel reads.

We recommend that your organization test the performance and
storage overhead of both uncompressed and compressed
datasets to determine best fit prior to implementing this
approach.

## Suggestion 10.3.1 – Compress data to reduce the transfer time

When storage read/write performance becomes a bottleneck,
use compression to reduce data transfer time. Consider the
tradeoffs between compute time needed to perform compression
and decompression versus the storage I/O bottleneck in your
estimates of overall improvements in performance efficiency.

## Suggestion 10.3.2 – Evaluate the available compression options for each resource of the workload

Compressing data can improve the performance as there are
fewer bytes transferred between the disk and compute
layers. The trade-off using this approach is that it
requires more compute for data compression and
decompression. You can, however, obtain a net efficiency
improvement if compression performs as well as or better
than uncompressed data transfer time. Compression also
requires much less storage, depending on the data type in
use, thus saving on data storage latency and costs.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/best-practice-10.3---use-file-compression-to-reduce-number-of-files-and-to-improve-file-io-efficiency..html*

---

# Best practice 10.4 – Partition your data to enable efficient data pruning and reduce unnecessary file reads

Storing your data in structured partitions will allow compute to identify the location of only that portion of the data relevant to the query. Determine the most frequent query parameters and store this data in the appropriate location suited to your data retrieval needs. For example, if an analytics workload regularly generates daily, weekly, and monthly reports, then store your data using partitions with a year/month/day format.

## Suggestion 10.4.1 – Partition data to support the most common query predicates

When your query uses a particular predicate in a WHERE clause, if your data is partitioned according to the field then the query engine can prune the data that it needs to look at and go directly to the relevant data partition. This means a full table scan is avoided, meaning faster performance and lower query cost.

## Suggestion 10.4.2 – Store data partitioned based on time attributes with earlier data stored in tiers that are accessed infrequently

Use the tiering capabilities of the storage service to put
infrequently-accessed data into the tier that is most
appropriate for the workload. For example, in an Amazon Redshift data warehouse, data that is accessed
infrequently can be stored in Amazon S3. Then you can
query it with Amazon Redshift Spectrum, while more
frequently-accessed data can be stored in local Amazon Redshift storage.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/best-practice-10.4---partition-your-data-to-avoid-unnecessary-file-reads..html*

---
