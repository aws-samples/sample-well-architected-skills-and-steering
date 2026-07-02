# IOTPERF06 — Performance efficiency

**Pillar**: Performance Efficiency  
**Best Practices**: 1

---

## IOTPERF06-BP01 Store data in different tiers following formats, access patterns and methods

AWS has several database offerings that support IoT solutions.
For structured data, you should use Amazon Aurora, a highly
scalable relational interface to organizational data. For
semi-structured data that requires low latency for queries and
will be used by multiple consumers, use Amazon DynamoDB, a fully
managed, multi-Region database that provides consistent
single-digit millisecond latency and offers built-in security,
backup and restore, and in-memory caching.

AWS also provides specific data storage solutions for industrial
use cases with AWS IoT SiteWise. For equipment data, three tiers
are available:

- A hot storage tier optimized for real-time applications
- A warm storage tier optimized for analytical workloads
- A cold storage tier using Amazon Simple Storage Service
(Amazon S3) for operational data applications with high
latency tolerance

SiteWise helps you to reduce storage cost by keeping recent data
in the hot storage tier for at least 30 days and moving
historical data to a cost-optimized warm storage tier based upon
user-defined data retention policies.

Use Amazon SageMaker AI AI to build, train, and deploy machine
learning models based on your IoT data, in the cloud, and on the
edge using AWS IoT services, such as machine learning inference
in AWS IoT Greengrass.

Consider storing your raw formatted time series data in a data
warehouse solution such as Amazon Redshift. Unformatted data can
be imported to Amazon Redshift using Amazon S3 and Amazon Data
Firehose. By archiving unformatted data in a scalable, managed
data storage solution, you can begin to gain business insights,
explore your data, and identify trends and patterns over time.

In addition to storing and leveraging the historical trends of
your IoT data, you should have a system that stores the current
state of the device and provides the ability to query against
the current state of all of your devices. This supports internal
analytics and customer facing views into your IoT data.

The AWS IoT Device Shadow service is an effective mechanism to
store a virtual representation of your device in the cloud. AWS IoT Device Shadow service is best suited for managing the
current state of each device.

In addition, for internal teams that need to query against the
shadow for operational needs, use the managed capabilities of
fleet indexing, which provides a searchable index incorporating
your IoT registry and shadow metadata. If there is a need to
provide index-based searching or filtering capability to a large
number of external users, such as for a consumer application,
dynamically archive the shadow state using a combination of the
IoT rules engine, Amazon Data Firehose, and Amazon OpenSearch Service to store your data in a format that allows fine grained
query access for external users.

**Level of risk exposed if this best
practice is not established:** Medium

**Prescriptive guidance
IOTPERF06-BP01-01**
*Create automated
mechanisms to transition data from tiers to implement
lifecycles.*

In an IoT solution, data often follows a lifecycle, transitioning from real-time ingestion to historical storage and archiving. To efficiently verify that stored data is utilizable throughout its lifecycle, it's crucial to implement automated mechanisms that transition data across different storage tiers based on predefined rules and policies.

For example, you can use AWS IoT rules and AWS Lambda functions to automatically route incoming real-time data to Amazon DynamoDB or Amazon Timestream for low-latency access and processing. As the data ages, you can initiate automated processes to transition it to Amazon S3 or Amazon Glacier for cost-effective, long-term archival storage.

Additionally, you can implement data retention policies and lifecycle management rules within your data storage solutions. For instance, in Amazon DynamoDB, you can configure Time to Live (TTL) settings to automatically expire and remove data after a specified period, improving the efficiency of storage utilization and reducing costs.

By creating automated mechanisms to transition data across different storage tiers, you can optimize storage costs, make data accessible based on its lifecycle stage, and maintain data integrity and availability for various analytical and operational use cases throughout the data lifespan.

### Resources

- [Managing
the lifecycle of objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html)
- [Backing
up and restoring Timestream tables: How it works](https://docs.aws.amazon.com/timestream/latest/developerguide/backups-how-it-works.html)
- [RetentionProperties](https://docs.aws.amazon.com/timestream/latest/developerguide/API_RetentionProperties.html)
- [Manage
data storage in AWS IoT SiteWise](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/manage-data-storage.html)
- [Configure
storage settings in AWS IoT SiteWise](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/configure-storage.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/data-management.html*

---
