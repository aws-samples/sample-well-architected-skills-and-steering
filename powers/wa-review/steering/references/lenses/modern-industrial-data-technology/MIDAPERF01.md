# MIDAPERF01 — Real-time data access

**Pillar**: Performance Efficiency  
**Best Practices**: 2

---

# MIDAPERF01-BP01 Use time series database for real-time analytics and data lake for long-term storage

In manufacturing environments, access patterns for operational data vary significantly
based on data age. Current data requires high-performance, low-latency access for real-time
decision making, while historical data typically serves longer-term analysis with less
stringent performance requirements. Implementing a tiered storage architecture with time
series databases for recent data and data lakes for historical information helps optimize both
performance and cost.

**Desired outcome:** A multi-tiered data storage architecture that provides millisecond-level query
performance for recent manufacturing data while cost-effectively storing and enabling
analytics on historical data spanning months or years, with appropriate retention policies and
data lifecycle management.

**Common anti-patterns:**

- Using only one type of database (relational
or noSQL) for both real-time operational data and years of historical data
- Keeping years of
manufacturing data in high-performance databases designed for real-time access
- Attempting to store
millisecond-level sensor data in traditional RDBMs without proper optimization
- Storing data without logical separation by time,
production line, or equipment type, leading to full table scans
- Relying on manual intervention to move aging data
between storage tiers
- Allowing unlimited data accumulation in high-performance
storage without lifecycle rules
- Moving data to archival storage too quickly before
operational teams have adequate access for troubleshooting
- Moving data between tiers without
optimizing format, compression, or structure for the target storage
- Running long-term trend analysis
queries against time series databases optimized for recent data
- Forcing applications to know and manage which storage system
contains the data they need
- Using generic database indexes instead of
time-series optimized indexing for temporal queries
- Attempting to join data across time series databases and data
lakes in real-time queries
- Requiring each application to integrate separately
with time series databases and data lakes
- No unified query interface, forcing users to learn different query languages and
APIs for current versus Historical data
- Synchronous data migration, blocking real-time operations while moving data between
storage tiers
- Direct storage access from applications, allowing applications to directly query
storage systems without abstraction layers
- Inadequate tagging and dimensions, storing time series data without proper metadata
tags for equipment, location, or process context
- Row-based storage for analytics, using row-oriented formats in data lakes when
columnar formats would provide better compression and query performance
- Normalized schemas for time series, applying traditional database normalization to
high-frequency sensor data
- Using one-size-fits-all schemas instead of optimizing for
specific manufacturing data patterns

**Benefits of establishing this best practice:**

- Delivers sub-second dashboard response times for real-time operational monitoring
- Reduces query costs for frequent access to current production metrics
- Enables cost-effective long-term storage of complete manufacturing history
- Optimizes storage costs by matching data access patterns to appropriate technologies
- Supports both real-time alerting and historical trend analysis from the same dataset

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

Implement time series database layer**:** Deploy
Amazon Timestream, a purpose-built time series database optimized for industrial IoT
data from manufacturing equipment like CNC machines, conveyor systems, and temperature
sensors. Configure retention policies (typically 30-90 days in memory store, longer
periods in magnetic store) based on operational requirements such as real-time quality
control monitoring. Design efficient data models with appropriate tags (equipment_id,
production_line, and shift) and dimensions (temperature, pressure, and vibration) to
support common manufacturing queries like equipment performance analysis and predictive
maintenance alerts.

Establish data lake architecture: Create an Amazon S3-based data lake with
appropriate partitioning strategies (by date=2024/01/15, production_line=assembly_1,
product_type=automotive_parts) to optimize query performance on historical manufacturing
data. Implement Apache Parquet columnar storage format to improve compression and query
efficiency for manufacturing analytics such as Overall Equipment Effectiveness (OEE)
calculations, quality trend analysis, and production optimization studies across
multiple factories.

Configure data lifecycle management: Develop AWS Lambda functions triggered by
Amazon EventBridge to automatically migrate data from Amazon Timestream to S3 as it ages
beyond immediate operational relevance (for example, after 90 days). Use AWS Glue ETL
jobs to implement data transformation during migration, converting real-time sensor data
into optimized Parquet format and aggregating metrics for long-term analytics like
annual production trends and equipment lifecycle analysis.

Design unified query interface: Create a query abstraction layer using Amazon Athena for historical data analysis and Amazon Timestream Query for real-time
operational data, with Amazon API Gateway providing a unified REST interface. Implement
intelligent routing logic using AWS Lambda that directs queries to Timestream for recent
data (last 30 days for live production monitoring) and to Athena for historical analysis
(older data for quarterly performance reviews and compliance reporting), verifying that
manufacturing engineers and analysts can access data consistently regardless of storage
location.

## Key AWS services

- Amazon Timestream for time series data storage
- Amazon S3 for data lake foundation
- AWS Glue for data transformation and cataloging
- Amazon Athena for querying historical data
- AWS Lambda for lifecycle management automation

## Resources

- [Amazon Timestream: Purpose-built
time series database](https://aws.amazon.com/timestream/)
- [Guidance for Data Lakes on AWS](https://aws.amazon.com/solutions/implementations/data-lake-solution/)
- [Time Series Forecasting Principles with Amazon Forecast](https://d1.awsstatic.com/asset-repository/Amazon%20Forecast%20Technical%20Guide%20to%20Time-Series%20Forecasting%20Principles.pdf)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midaperf01-bp01.html*

---

# MIDAPERF01-BP02 Compress, sample and summarize data at edge, before sending to the cloud environment

In manufacturing environments, IoT devices and sensors often generate massive volumes of
high-frequency data that can overwhelm networking, processing, and storage resources.

**Desired outcome:** Reduce amount of data flowing from
on-premises to cloud by summarizing time series machine data, for example average temperature
over a time period instead of raw temperature values every second. This allows for quicker
data processing long term for trending insights.

**Common anti-patterns:**

- Sending raw, unprocessed data streams directly to the cloud
- Ignoring data compression opportunities
- Not implementing edge-level data processing
- Overwhelming network bandwidth with high-frequency data

- Creating unnecessary network congestion
- Ignoring data transmission timing optimization
- Bypassing gateway-level processing capabilities
- Not using MQTT topic filtering
- Skipping data summarization strategies

**Benefits of establishing this best practice:**

- Less processing time processing and querying long term data
- Less time transmitting data to cloud
- Reduced storage costs
- Reduced network congestion to cloud

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

To reduce network traffic and overhead to allow faster processing:

- Configure small data processing applications to summarize data on your gateway
devices using AWS IoT Greengrass components

**Manufacturing example:** Deploy AWS IoT Greengrass on factory floor gateways to
run edge analytics components that process real-time data from CNC machines,
conveyor belt sensors, and quality control cameras, summarizing production metrics
like throughput rates, defect counts, and equipment utilization before sending to
the cloud.

- Subscribe to direct topics through MQTT of machine data, then use components to
summarize and re-publish data on a new topic that is routed to AWS IoT Core or SiteWise.

**Industrial example:** Use AWS IoT Greengrass components to subscribe to MQTT
topics from industrial equipment like turbines, pumps, and generators, then
aggregate temperature, vibration, and pressure readings into health score summaries
that are republished to AWS IoT SiteWise for asset monitoring dashboards and AWS IoT Core for further processing and alerting.

- Alternatively, locally compress summarized data into Apache Parquet format and
transfer directly to Amazon S3.

**Manufacturing example:** Configure edge devices in automotive plants to compress
daily production data (part counts, cycle times, energy consumption) from assembly
line robots and quality inspection systems into Parquet files, then batch upload to
Amazon S3 for long-term storage and analysis with AWS analytics services like Amazon Athena and Quick for operational intelligence reporting.

### Implementation Steps

- Create data processing component in your language of choice, using the AWS IoT Greengrass Development Kit (GDK).
- Have component subscribe to raw data topics on-premises.
- Build components to do tasks such as summarize data and rolling averages for set
time periods, and re-publish to new topic.
- Relay only new topic from on premises to AWS IoT Core or SiteWise for storage and
processing.

## Key AWS services

- AWS IoT Core
- AWS IoT Greengrass
- AWS IoT SiteWise
- AWS IoT SiteWise Edge

## Resources

- [Cost-effectively ingest IoT data directly into Amazon S3 using AWS IoT Greengrass](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/cost-effectively-ingest-iot-data-directly-into-amazon-s3-using-aws-iot-greengrass.html)
- [Ingest and analyze equipment data in the cloud](https://aws.amazon.com/blogs/industries/ingest-and-analyze-equipment-data-in-the-cloud/)
- [Getting Started with AWS IoT Greengrass Solution Accelerators for Edge
Computing](https://pages.awscloud.com/rs/112-TZM-766/images/2020_0320-IOT_Slide-Deck.pdf)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midaperf01-bp02..html*

---
