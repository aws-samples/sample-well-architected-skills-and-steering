# MIDAPERF05 — Pre-process data at edge

**Pillar**: Performance Efficiency  
**Best Practices**: 2

---

# MIDAPERF05-BP01 Implement edge data pre-processing

In manufacturing settings, industrial devices and sensors often generate massive volumes
of raw data that may not all be valuable for cloud-based analytics. Implementing edge
pre-processing capabilities enables local summarization, filtering, and aggregation of data
before transmission, significantly reducing bandwidth requirements, cloud processing needs,
and storage costs while still preserving analytical value.

**Desired outcome:** A manufacturing data architecture that optimally distributes processing between edge and
cloud, performing appropriate data reduction, summarization, and filtering at the edge while
preserving essential information for cloud-based analytics and long-term storage.

**Common anti-patterns:**

- Sending all sensor data unfiltered to the cloud without edge processing, creating massive bandwidth waste and storage costs
- Using fixed sampling rates regardless of operational context or equipment state, missing critical events during high-activity periods while wasting resources during stable operations
- Designing systems that cannot function locally during connectivity disruptions, losing valuable operational data and halting local decision-making
- Deploying edge devices with insufficient CPU, memory, or storage capacity to handle required pre-processing, creating bottlenecks and system failures
- Sending data without contextual filtering or prioritization, treating routine operational data the same as critical alerts or anomalies
- Failing to implement temporary storage at the edge, resulting in permanent data loss during network outages or connectivity issues
- Performing all data analysis in the cloud instead of leveraging edge capabilities for real-time local decisions and immediate responses
- Excessive data summarization that loses critical analytical value or masks important operational insights needed for maintenance and optimization
- Applying identical pre-processing logic across all equipment types and operational contexts without considering specific requirements or characteristics
- Not implementing immediate local processing for time-sensitive data that requires instant action or real-time operational adjustments
- Ignoring the compound effect of raw data storage costs over time, failing to implement appropriate data lifecycle and retention policies
- Designing systems assuming unlimited or cheap network bandwidth without considering actual connectivity constraints in industrial environments

**Benefits of establishing this best practice:**

- [Reduces network bandwidth requirements by 60-90% in typical manufacturing deployments](https://journalwjarr.com/sites/default/files/fulltext_pdf/WJARR-2025-2015.pdf)
- Decreases cloud storage costs proportionally to reduction in data volume
- Lowers data ingestion and processing costs in cloud environments
- Minimizes latency for local decision-making through edge processing
- Improves overall system resilience by enabling continued local operation during
connectivity disruptions

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

- Evaluate existing data pipelines to identify compression and aggregation opportunities that preserve analytical insights. Use Amazon Managed Service for Apache Flink to perform real-time stream processing for averaging high-frequency sensor data, use AWS IoT Device SDK to implement delta-based transmission protocols that only send data when values exceed defined thresholds, and deploy AWS Lambda functions to calculate KPIs and derived metrics at the edge before transmission to reduce payload sizes.
- Architect distributed computing capabilities at plant locations using ruggedized hardware optimized for industrial environments. Deploy AWS IoT Greengrass on industrial-grade edge devices to enable local compute, messaging, and ML inference capabilities, utilize Amazon EC2 instances or AWS Outposts for locations requiring substantial remote processing power, and implement AWS Systems Manager for remote device management and software deployment across manufacturing sites.
- Configure intelligent data collection systems that adapt based on operational states and process conditions. Use AWS IoT Device Defender and AWS IoT Events to create rules-based filtering that correlates equipment status with data collection requirements, implement Amazon DynamoDB at the edge using AWS IoT Greengrass to store operational context and filtering rules, and leverage AWS IoT Core message routing to direct different data streams based on production state classifications.
- Develop dynamic data acquisition systems that automatically adjust collection frequencies based on real-time equipment health and process stability indicators. Implement AWS IoT Greengrass ML Inference to run anomaly detection models locally that trigger increased sampling rates, use Amazon CloudWatch metrics and alarms to define operational state thresholds, and deploy AWS Lambda functions that dynamically reconfigure sampling parameters based on equipment condition scores and process variables.
- Implement resilient data buffering and intelligent transmission systems that maintain data integrity during network disruptions. Configure AWS IoT Greengrass local storage capabilities with Amazon DynamoDB local tables for temporary data persistence, implement Amazon Data Firehose for reliable data delivery with automatic retry mechanisms, and use AWS IoT Core device shadows to maintain synchronization state and prioritize critical alarm data transmission over historical trend data during bandwidth-constrained conditions.

## Key AWS services

- AWS IoT Greengrass for edge processing and analytics
- AWS IoT SiteWise for equipment modeling and edge processing
- AWS IoT Core for secure device connectivity
- Amazon Kinesis for data streaming from edge to cloud
- AWS Lambda for custom edge processing functions
- Amazon S3 for storing pre-processed data

## Resources

- [Processing Data at the Edge with AWS IoT Greengrass](https://docs.aws.amazon.com/greengrass/latest/developerguide/stream-manager.html)
- [Edge Processing with AWS IoT SiteWise Edge](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/edge.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midaperf05-bp01.html*

---

# MIDAPERF05-BP02 Optimize storage and access for current manufacturing data

In manufacturing environments, rapid access to recent operational data is critical for
real-time monitoring, anomaly detection, and immediate decision-making. Implementing
specialized time series database solutions for current data while leveraging cost-effective
storage for historical information creates an optimal balance between performance and cost,
verifying that dashboards and analytics remain responsive for operational needs.

**Desired outcome:** A tiered data storage architecture that provides millisecond-level query performance for
recent manufacturing data while cost-effectively storing historical information, resulting in
responsive operational dashboards, efficient anomaly detection, and appropriate
performance-to-cost ratios across different data lifecycle stages.

**Common anti-patterns:**

- Storing all historical data in expensive, high-performance databases without implementing data lifecycle management or tiered storage strategies
- Using relational databases or general-purpose storage solutions instead of purpose-built time series databases for manufacturing sensor data and operational metrics
- Implementing overly complex data models with excessive normalization that require multiple joins for simple time series queries in operational dashboards
- Querying raw, unaggregated historical data spanning years directly from operational dashboards instead of using pre-computed aggregations or summaries
- Setting excessively long retention periods (6+ months) in high-performance time series databases without analyzing actual operational access patterns
- Creating inefficient tagging and indexing strategies that don't align with common manufacturing query patterns, causing slow dashboard performance
- Failing to implement query federation, forcing applications to maintain separate connection logic for different storage tiers and complicating data access
- Loading operational dashboards with unnecessary historical context that extends query windows beyond immediate operational needs (24-48 hours)
- Using synchronous data migration processes that block real-time ingestion during data lifecycle transitions between storage tiers
- Implementing generic caching strategies instead of manufacturing-specific data access patterns, missing opportunities for significant performance gains
- Storing all data at full resolution permanently instead of implementing intelligent down sampling for aging data based on operational value
- Creating monolithic storage architectures that force all queries through a single database tier regardless of data age or access frequency

**Benefits of establishing this best practice:**

- 1. Substantially reduces dashboard refresh latency for current operational data
- Provides sub-second query response for real-time operational decision support
- Optimizes storage costs by matching data access patterns with appropriate
technologies
- Improves overall system scalability by distributing query load across appropriate
storage tiers
- Enables more sophisticated real-time analytics without performance penalties

**Level of risk exposed if this best practice is not
established:**

Medium

## Implementation guidance

- Conduct comprehensive analysis of your manufacturing systems' data consumption using Amazon CloudWatch to monitor current query patterns and AWS X-Ray to trace application performance. Use Quick usage analytics to understand dashboard access frequency and identify critical real-time metrics that drive production decisions. Use AWS Cost and Usage Reports to correlate data access costs with business value.
- Deploy Amazon Timestream as your primary industrial IoT data store, configured for high-throughput sensor data ingestion with magnetic storage tier for 30-90 day retention windows. Complement with Amazon MemoryDB for sub-millisecond query requirements on critical process variables. Use AWS IoT Core and AWS IoT SiteWise for seamless OT-to-cloud data pipeline integration.
- Structure your Timestream tables with equipment-based partitioning and implement hierarchical tagging using AWS Resource Groups naming conventions. Use AWS Glue Data Catalog to maintain metadata schemas and leverage Amazon OpenSearch Service for fast dimensional queries across manufacturing assets and process parameters.
- Establish automated data archival using AWS Lambda functions initiated by Amazon EventBridge schedules to move aged data from Timestream to Amazon S3 with S3 Intelligent-Tiering. Implement data aggregation pipelines using AWS Glue ETL jobs to create summarized views during the transition process, reducing storage costs while preserving analytical value.
- Deploy Amazon Athena with federated queries to create unified access across Timestream (hot data) and Amazon S3 (warm and cold data) using a single SQL interface. Use AWS AppSync GraphQL APIs to provide consistent data access patterns for manufacturing applications and implement Amazon API Gateway caching to optimize performance across storage tiers.

## Key AWS services

- Amazon Timestream for time series data storage
- Amazon OpenSearch Service for operational data visualization
- Amazon S3 for cost-effective historical data storage
- AWS Glue for data lifecycle management
- Amazon Athena for queries across multiple storage tiers
- Quick for operational dashboards

## Resources

- [Getting Started with Amazon Timestream](https://docs.aws.amazon.com/timestream/latest/developerguide/getting-started.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midaperf05-bp02.html*

---
