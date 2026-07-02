# SCPERF03 — Database and storage selection

**Pillar**: Performance Efficiency  
**Best Practices**: 3

---

# SCPERF03-BP01 Select your database architecture based on workload

Purpose-built data storage for your workloads can help increase
the performance efficiency of the overall system, as well to be
more resilient in case of failures.

**Desired outcome:** Purpose-built
data storage. Increased performance efficiency of the overall
system.

**Benefits of establishing this best
practice:** Scalability, resilience, and end user
performance improvement.

**Level of risk exposed if this best
practice is not established:** High.

## Implementation guidance

Select database options that align with your performance
requirements, using different database technologies for
different purposes, such as Amazon Timestream time-series
database for storing ticking market data, rather than a
one-size-fits-all use of traditional relational databases. Also,
Amazon RDS is a straightforward relational database service
optimized for total cost of ownership. It is simple to set up,
operate, and scale with demand. Amazon RDS automates the
undifferentiated database management tasks, such as
provisioning, configuring, backups, and patching.

### Implementation steps

- Analyze supply chain data access patterns and performance
requirements to determine optimal database architectures.
- Implement purpose-built databases for specific use cases,
such as time-series databases for IoT sensor data and
document databases for product catalogs.
- Configure Amazon RDS for transactional supply chain data
that requires ACID compliance and complex queries.
- Deploy NoSQL databases like Amazon DynamoDB for
high-throughput, low-latency applications such as
inventory tracking.
- Establish database performance monitoring and optimization
processes to maintain continued efficiency as data volumes
grow.
- Implement automated backup and disaster recovery
strategies to maintain data availability and business
continuity.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/supply-chain-lens/scperf03-bp01.html*

---

# SCPERF03-BP02 Select your storage architecture based on workload

Data lineage is important in the world of producers and consumers
of the data. This lineage can be verified and validated when it is
tracked from the source system to the destination systems. As a
result, well-organized data leads to better understanding.

**Desired outcome:** Well-organized
data with improved understanding.

**Benefits of establishing this best
practice:** Data lineage, scalability, resilience, and
re-usability.

**Level of risk exposed if this best
practice is not established:** Medium

## Implementation guidance

AWS Supply Chian needs a data lake with AI/ML models for supply
chains to understand, extract, and transform disparate,
incompatible data into a unified data model. The data lake can
ingest your data from various data sources, including your
existing ERP systems, such as SAP S/4HANA, and supply chain
management systems. To add data from variable sources such as
EDI 856, some applications use AI/ML and natural language
processing (NLP) to associate data from source systems to the
unified data model. EDI 850 and 860 messages are transformed
directly with predefined but customizable transformation
recipes.

### Implementation steps

- Design a data lake architecture using Amazon S3 to store
diverse supply chain data from multiple sources and
formats.
- Implement data ingestion pipelines using AWS Glue to
extract, transform, and load data from ERP systems and
supply chain applications.
- Configure AI/ML models to process and standardize
disparate data formats, including EDI messages and
unstructured documents.
- Establish data lineage tracking mechanisms to maintain
visibility into data flow from source systems to
destination applications.
- Implement data governance policies and access controls to
maintain data quality and security across the storage
architecture.
- Create automated data validation and quality monitoring
processes to maintain data integrity throughout the supply
chain environment.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/supply-chain-lens/scperf03-bp02.html*

---

# SCPERF03-BP03 Use cache memory to help improve the performance

Cache memory provides improved latency of the application when
accessed outside of the solution-hosted Regions.

**Desired outcome:** Low latency of
the application when accessed outside of designated Regions.

**Benefits of establishing this best
practice:** Better throughput, low latency, reduced power
consumption, improved reliability, and increased scalability.

**Level of risk exposed if this best
practice is not established:** High

## Implementation guidance

While considering using the cache memory for your supply chain
solutions, you can architect the solution to use caching
services to improve performance. Store frequently used data in
memory or bring the data closer to consumers. Many AWS services
offer features for caching or dedicated services including
Amazon ElastiCache, and Amazon File Cache. For example,
frequently accessed inventory data should be stored in cache
memory, with time-to-live (TTL) settings configured to align
with the data's update frequency and usage patterns. In this
case, data caching solutions (Redis Cache or MemoryDB) are
important to quickly access last available data with low latency
(200 milliseconds or less) interval.

### Implementation steps

- Identify frequently accessed supply chain data that would
benefit from caching, such as inventory levels, product
information, and pricing data.
- Implement Amazon ElastiCache with Redis or Memcached to
cache frequently accessed data and reduce database load.
- Configure appropriate TTL settings for cached data based
on update frequency and business requirements for data
freshness.
- Deploy Amazon CloudFront for caching static content and
API responses to improve global access performance.
- Implement cache invalidation strategies to maintain data
consistency when underlying data changes.
- Monitor cache performance metrics and optimize cache
configurations to maximize hit rates and minimize latency.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/supply-chain-lens/scperf03-bp03.html*

---
