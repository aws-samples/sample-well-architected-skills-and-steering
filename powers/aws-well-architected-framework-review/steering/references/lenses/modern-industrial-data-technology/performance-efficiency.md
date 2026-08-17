# Performance Efficiency

**Pillar**: Performance Efficiency  
**Questions**: 6

---

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

# MIDAPERF02 — Event-driven architecture

**Pillar**: Performance Efficiency  
**Best Practices**: 2

---

# MIDAPERF02-BP01 Implement event-driven architectures for manufacturing systems

In manufacturing environments, operational data is generated based on specific events
such as equipment state changes, threshold violations, or production milestones. Implementing
event-driven architectures allows systems to respond efficiently to these events rather than
constantly polling for changes, significantly improving resource utilization and system
responsiveness. This approach aligns perfectly with IoT communication patterns while enabling
scalable, loosely-coupled manufacturing systems.

**Desired outcome:** A responsive, efficient manufacturing data architecture that processes information only
when meaningful events occur, reducing unnecessary computation, minimizing latency for
critical operations, and enabling dynamic scaling based on actual processing demand rather
than peak capacity requirements.

**Common anti-patterns:**

- Transforming all incoming manufacturing data immediately instead of lazy evaluation when needed
- Making multiple small database calls per event instead of batching operations or using bulk APIs
- Processing all events and filtering in application code rather than using message-level filtering capabilities
- Routing all events from similar equipment to the same partition, creating processing bottlenecks
- Creating point-to-point integrations between manufacturing systems instead of using event mediators
- Making blocking calls between manufacturing subsystems instead of asynchronous event-driven communication
- Processing events without validating structure, leading to runtime failures and data corruption
- Building event consumers that depend on specific event producer implementations rather than standardized interfaces
- Allowing event processing failures to occur without proper logging, alerting, or dead letter handling
- Not implementing flow control when downstream systems cannot keep up with event volume
- Failing to implement end-to-end tracing for manufacturing processes spanning multiple event handlers
- Only monitoring for failures instead of proactively tracking performance metrics and trends

**Benefits of establishing this best practice:**

- [Reduces processing overhead by 40-60% compared to polling-based systems](https://arxiv.org/html/2510.04404v1)
- Improves response time to critical manufacturing events by removing processing queues
- Enhances system scalability by allocating resources only when needed for event
processing
- Simplifies integration between manufacturing subsystems through standardized event
interfaces
- Enables more granular cost allocation by associating resource usage with specific
event types

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

- Implement a publish or subscribe
messaging architecture where manufacturing devices and systems publish events to
centralized topics. Configure consumers to process only relevant event types using message
filtering capabilities to reduce unnecessary processing.
- Deploy durable message queues between producers and
consumers to handle throughput spikes and provide reliable event delivery even during
processing backlogs or temporary downstream system outages common in manufacturing
environments. AWS SQS and Amazon EventBridge services are tools that can accomplish these
goals.
- Design event handlers with idempotency in mind to help
prevent duplicate processing when events are retried. Implement deduplication mechanisms
using event IDs or processing timestamps to maintain data integrity during retries. A
- Establish dead-letter queues to capture events that
cannot be processed successfully after multiple attempts. Implement automated monitoring
and alerting for these queues to quickly identify and resolve processing issues that could
impact manufacturing operations. AWS Step functions, Amazon EventBridge, and AWS IoT core
are example services to help accomplish these tasks.
- For multi-step manufacturing processes, implement
state machines to coordinate event sequences and manage process state. Design workflows
that can handle long-running operations while maintaining visibility into process status.
AWS Step functions, Amazon EventBridge, and AWS IoT core are example services to help
accomplish these tasks.

## Key AWS services

- Amazon EventBridge for event routing and filtering
- Amazon SQS for reliable message queueing
- AWS Lambda for serverless event processing
- Amazon SNS for event notifications
- AWS Step Functions for manufacturing process orchestration
- AWS IoT Core for device-generated events

## Resources

**Related documents:**

- [Building Event-Driven Architectures on AWS](https://aws.amazon.com/event-driven-architecture/)
- [Serverless Patterns for Event-Driven Architectures](https://serverlessland.com/patterns)
- [Implementing Idempotency Patterns with AWS Lambda](https://aws.amazon.com/blogs/compute/implementing-idempotent-aws-lambda-functions-with-powertools-for-aws-lambda-typescript/)
- [Handling Failure Scenarios with Amazon SQS Dead-Letter
Queues](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.html)
- [Build a serverless Amazon Bedrock batch job orchestration workflow using AWS Step Functions](https://aws.amazon.com/blogs/machine-learning/build-a-serverless-amazon-bedrock-batch-job-orchestration-workflow-using-aws-step-functions/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midaperf02-bp01.html*

---

# MIDAPERF02-BP02 Use historical cloud usage data aligned with production schedules and business forecasts

Aligning cloud resource allocation with production schedules and business forecasts
enables organizations to optimize system performance during critical periods while helping
prevent resource constraints that could impact throughput and quality. By analyzing patterns
in historical cloud usage alongside manufacturing cycles, plant managers can anticipate
processing requirements for data-intensive operations like quality inspection systems,
predictive maintenance algorithms, and real-time production monitoring, providing optimal
performance when manufacturing demands are highest.

**Desired outcome:** A predictive resource management approach that provides manufacturing systems with
precisely calibrated computing capacity, removing performance bottlenecks during peak
production periods while maintaining processing responsiveness for time-sensitive
manufacturing analytics and control systems.

Common anti-patterns:

- Using static capacity planning without considering manufacturing cycles, seasonal demands, or planned maintenance windows
- Analyzing cloud usage data in isolation without correlating with production schedules, quality metrics, or business forecasts
- Applying uniform auto-scaling rules across all manufacturing workloads regardless of their specific performance characteristics
- Triggering resource scaling exactly when demand increases without accounting for provisioning and initialization delays
- Using only basic CPU/memory metrics for scaling decisions without considering manufacturing-specific performance indicators
- Running large ETL jobs or analytics workloads during active production periods, competing for resources with real-time systems
- Processing all manufacturing data synchronously, even for non-time-sensitive analytics
- Retaining all historical data at the same performance tier regardless of access patterns
- Setting static performance thresholds that don't account for normal variations in manufacturing operations
- Monitoring individual components without understanding overall system performance impact on manufacturing processes
- Failing to establish and maintain performance baselines for different production scenarios
- Running development, testing, and production workloads on shared infrastructure during critical manufacturing periods
- Not considering latency between cloud resources and manufacturing equipment locations when designing system architecture
- Failing to properly tag resources to correlate performance investments with specific manufacturing outcomes and ROI

**Benefits of establishing this best practice:**

- [Improves production system responsiveness by up to 40% during peak manufacturing
periods](https://www.researchgate.net/publication/393472445_A_Cloud-Native_Framework_for_Cross-Industry_Demand_Forecasting_Transferring_Retail_Intelligence_to_Manufacturing_with_Empirical_Validation)
- Removes data processing bottlenecks that can cause manufacturing quality or
throughput issues
- Enables higher-fidelity monitoring and analytics during critical production runs
- Accelerates time-to-insight for manufacturing intelligence during complex production
sequences
- Facilitates seamless integration between production scheduling and infrastructure
provisioning teams

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

- Analyze cloud resource utilization patterns during different manufacturing operations to identify performance-critical periods requiring enhanced computing capacity, especially for vision systems, complex analytics, or high-frequency data collection. Analysis and alerting can be implanted through using Amazon CloudWatch, AWS X-Ray, and Amazon CloudWatch insights.
- Establish relationships between specific manufacturing activities (high-precision runs, quality inspections, material changeovers) and corresponding infrastructure performance requirements to develop predictive capacity models.
- Develop automated scaling mechanisms that proactively adjust computing resources based on upcoming production schedules, which verifies that critical systems have sufficient processing power before high-demand manufacturing phases begin. Using services such as Amazon SageMaker AI for predictive modeling, auto scaling with AWS Auto Scaling, and Amazon CloudWatch for monitoring metrics can help with implementation.
- Refine ETL processes and analytics workflows based on historical performance data to maximize throughput during peak production periods when real-time insights are most valuable. AWS services such as Amazon Kinesis Data Streams, Amazon MSK, and AWS IoT Core can help with implementing optimized data processing pipelines. Real time processing can be implemented through Lambda, and Amazon Kinesis Data Analytics. AWS X-Ray can help with end to end pipeline tracking and anomaly detection.
- Implement continuous performance monitoring that compares actual versus expected response times and processing capabilities, refining resource allocation models to improve manufacturing system responsiveness over time. AWS services that can help with implementation are Amazon CloudWatch, AWS X-Ray, and Application Load Balancer.

## Key AWS services

- Amazon CloudWatch for performance monitoring and metrics collection
- AWS Auto Scaling for automatically adjusting capacity based on production needs
- AWS Forecast for predicting resource requirements based on historical patterns
- Amazon Kinesis for managing high-throughput data streams from manufacturing
equipment
- AWS Lambda for dynamic processing of production event data
- Amazon RDS Performance Insights for database performance optimization

## Resources

- [Performance Efficiency Pillar - AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/welcome.html)
- [Implementing Predictive Scaling with AWS Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-predictive-scaling.html)
- [Real-time Analytics with Amazon Kinesis](https://docs.aws.amazon.com/streams/latest/dev/introduction.html)
- [Optimizing AWS Lambda Performance for Manufacturing Workloads](https://aws.amazon.com/blogs/compute/operating-lambda-performance-optimization-part-1/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midaperf02-bp0.html*

---

# MIDAPERF03 — Data processing infrastructure

**Pillar**: Performance Efficiency  
**Best Practices**: 2

---

# MIDAPERF03-BP01 Use cloud observability tools for manufacturing systems

In manufacturing environments, comprehensive visibility into system performance, data
processing pipelines, and infrastructure health is critical for maintaining operational
excellence. Implementing cloud-native observability tools provides unified monitoring,
actionable alerting, and diagnostic capabilities across the entire manufacturing technology
stack. This integrated approach enables rapid identification and resolution of performance
issues before they impact production operations.

**Desired outcome:** A comprehensive observability framework that provides real-time visibility into
manufacturing data systems, enabling proactive performance optimization, rapid
troubleshooting, and data-driven capacity planning while providing maximum uptime for critical
manufacturing operations.

**Common anti-patterns:**

- Waiting for system failures before implementing monitoring instead of proactive performance tracking
- Collecting massive amounts of data without establishing manufacturing-specific KPIs or business relevance
- Only monitoring at infrastructure level while ignoring application and business process performance
- Setting too many low-priority alerts or poorly tuned thresholds that create noise instead of actionable insights
- Using disconnected monitoring solutions that prevent correlation across system components
- Operating manufacturing systems without comprehensive API activity logging and analysis
- Ignoring API call patterns and frequency that could indicate over-utilization or inefficient integrations
- Storing critical operational logs in systems where they can be modified, compromising audit trails
- Mixing production logs with development/testing data instead of maintaining dedicated audit accounts
- Manually configuring edge devices instead of using standardized fleet management approaches
- Pushing configuration changes directly to all devices without canary or blue/green deployment strategies
- Operating edge devices without hardware performance monitoring and health tracking
- Relying on human intervention for common device communication issues instead of automated remediation
- Collecting metrics without establishing appropriate performance thresholds for manufacturing-critical systems
- Using only critical alerts instead of progressive severity levels based on threshold proximity
- Creating alerts that don't run automated remediation or clear escalation procedures
- Learning about performance issues only after they affect manufacturing operations
- Operating manufacturing data flows without end-to-end visibility into processing steps and dependencies
- Either over-sampling (performance impact) or under-sampling (missing critical issues) distributed traces
- Running manufacturing systems without understanding request flow timing and bottleneck identification

**Benefits of establishing this best practice:**

- [Reduces MTTD for performance anomalies by 65-85%](https://newrelic.com/resources/white-papers/observability-as-a-priority)
- Enables correlation of issues across different system components for faster root
cause analysis
- Provides quantifiable metrics to justify optimization investments and measure their
impact
- Enhances capacity planning through historical performance trend analysis
- Minimizes production impact through early detection of emerging performance
bottlenecks

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

Deploy AWS CloudTrail
across all manufacturing data services to capture API calls from SCADA systems, MES
integrations, and data pipelines. Store logs in a dedicated Amazon S3 bucket with S3
Object Lock for immutability. Use AWS CloudWatch Insights to analyze patterns in equipment
data ingestion rates and identify potential security issues in your OT/IT bridge
connections. Configure AWS Organizations to centralize trail management across production,
staging, and development environments.

Implement Amazon CloudWatch as your unified metrics system, capturing infrastructure metrics from EC2
instances running historian services, custom manufacturing metrics using CloudWatch Custom
Metrics for OEE, throughput, and quality indicators, application performance from
containerized services using Amazon ECS/EKS with Container Insights, and business process
metrics through CloudWatch Embedded Metric Format in your Lambda functions processing
production data. Use Amazon Managed Service for Prometheus for time-series data from edge
devices and Amazon Managed Grafana for manufacturing dashboards.

Configure CloudWatch Alarms
with manufacturing-specific thresholds (for example, data ingestion gaps indicating
equipment downtime). Implement progressive alerting using Amazon SNS topics with different
severity levels: Critical for production line stoppage detection, Warning for trending
toward SLA violations, and Info for planned maintenance windows. Use AWS Lambda functions
triggered by CloudWatch Events for automated remediation, such as restarting stuck data
collection services or switching to backup data sources.

Deploy AWS X-Ray across your manufacturing
data pipeline to trace requests from edge devices through AWS IoT Core, Kinesis Data
Streams, Lambda processing functions, and final storage in Amazon Timestream or S3.
Configure sampling rules to capture 100% of critical production data flows while sampling
routine maintenance data at lower rates. Use X-Ray service maps to visualize dependencies
between your MES, ERP, and analytics systems.

Use AWS IoT Device Management to manage your industrial edge devices and gateways. Deploy AWS IoT Greengrass
for edge computing capabilities. Implement fleet-wide updates using IoT Jobs with
controlled rollout strategies by using IoT Device Management Fleet Indexing to group
devices by production line or equipment type, configuring progressive deployment patterns
with canary releases to test configuration changes on non-critical equipment first, and
monitoring deployment success rates with automatic rollback of failed updates.

Configure AWS IoT Events to detect offline devices, abnormal sensor readings, or communication pattern
anomalies. Set up AWS IoT Device Defender for security monitoring of your industrial
devices. Create automated recovery procedures using AWS Step Functions to orchestrate
device troubleshooting workflows, AWS Systems Manager to remotely diagnose and restart
edge gateway services, and Amazon SNS notifications to operations teams when manual
intervention is required.

Implement intelligent data retention
using Amazon S3 Intelligent Tiering for historical manufacturing data, S3 Lifecycle
policies to transition detailed sensor data from Standard to IA to Glacier based on access
patterns, Amazon Timestream with automatic data tiering for time-series data (memory for
recent data, magnetic storage for historical), and CloudWatch Logs retention policies
configured by criticality (30 days for debug logs, one year for production events). Use AWS Cost Explorer and AWS Budgets to monitor storage costs and set alerts for unexpected data
growth. Consider Amazon Redshift with automatic table optimization for long-term analytics
on production trends while maintaining cost efficiency through Reserved Instance planning
for predictable workloads.

## Key AWS services

- AWS CloudTrail for API activity monitoring
- Amazon CloudWatch for metrics, logs, and alerting
- AWS X-Ray for distributed tracing
- AWS IoT Greengrass for edge device management
- AWS Systems Manager for configuration management
- AWS IoT Events for device state monitoring

## Resources

- [Monitoring AWS IoT Applications](https://docs.aws.amazon.com/iot/latest/developerguide/monitoring_overview.html)
- [Analyzing API Calls with CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html)
- [AWS X-Ray features](https://aws.amazon.com/xray/features/)
- [AWS IoT Device Management features](https://aws.amazon.com/iot-device-management/features/)
- [AWS Solutions Library](https://aws.amazon.com/solutions/implementations/centralized-logging/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midaperf03-bp01.html*

---

# MIDAPERF03-BP02 Implement comprehensive performance measurement for manufacturing data infrastructure

Understanding the performance characteristics of data processing infrastructure is
essential for maintaining performance efficiency and planning for growth. Implementing robust
measurement frameworks with appropriate metrics, dashboards, and alerting enables
organizations to proactively manage performance, optimize resource utilization, and justify
infrastructure investments with quantifiable data.

**Desired outcome:** A comprehensive performance measurement framework that provides real-time visibility into
all aspects of manufacturing data infrastructure, enabling data-driven optimization decisions,
capacity planning, and early detection of performance degradation before it impacts production
operations.

**Common anti-patterns:**

- Waiting for system failures or user complaints before investigating performance issues instead of implementing proactive monitoring and alerting
- Using separate, disconnected monitoring tools for different infrastructure components without centralized observability and correlation
- Creating technical dashboards with standard IT metrics that don't relate to manufacturing operations or business context
- Setting fixed performance thresholds that don't account for normal manufacturing workload variations and production cycle patterns
- Deploying monitoring without first conducting controlled testing to understand normal performance characteristics
- Failing to track API usage patterns, leading to undetected redundant calls, inefficient integrations, and quota exhaustion
- Monitoring only basic system metrics while ignoring manufacturing-specific measurements like message throughput by device type or processing latency for time-sensitive data
- Configuring too many low-priority alerts or alerts without clear escalation paths, leading to ignored notifications
- Not retaining sufficient performance history for trend analysis and capacity planning decisions
- Implementing only critical threshold alerts without predictive or warning-level notifications for emerging performance trends
- Requiring human intervention for common, predictable performance issues that could be automatically resolved
- Operating without granular resource utilization tracking, making it impossible to allocate costs by workload or justify optimization investments
- Not implementing distributed tracing to understand end-to-end data processing delays across manufacturing workflows
- Skipping controlled performance validation during infrastructure changes or capacity planning exercises

**Benefits of establishing this best practice:**

- Enables proactive identification of performance bottlenecks before they impact
production
- Provides quantifiable metrics to justify optimization investments and infrastructure
scaling
- Facilitates accurate capacity planning based on historical performance trends
- Improves cost allocation through precise measurement of resource utilization by
workload
- Reduces troubleshooting time by pinpointing specific performance constraints

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

- Deploy Amazon CloudWatch agents on
EC2 instances and integrate with AWS IoT Core device metrics to collect comprehensive
performance data across the manufacturing infrastructure components. Configure
CloudWatch Custom Metrics specific to industrial data processing needs alongside
standard system metrics through AWS Systems Manager and Amazon Kinesis Data Streams.
- Key metrics to consider:

Message throughput rates (messages per second) by device type and production area
using AWS IoT Device Management groupings
- Data storage utilization trends with forecasted growth patterns via Amazon S3
Storage Lens and Amazon EBS monitoring
- Bandwidth consumption during different production phases through VPC Flow Logs
and AWS Direct Connect monitoring
- Processing latency for time-sensitive manufacturing data flows using Amazon Kinesis Analytics and AWS Lambda duration metrics
- API call volumes and patterns with service quota utilization percentages
through AWS CloudTrail and Service Quotas integration

- Establish a unified monitoring environment
using Amazon CloudWatch Dashboards and AWS Grafana that aggregates metrics from the
infrastructure components. Create manufacturing-specific dashboards using Quick that visualize performance metrics in the context of production operations
rather than just technical indicators, integrated with AWS IoT SiteWise for operational
technology data correlation.
- Enable comprehensive API activity logging
through AWS CloudTrail and Amazon API Gateway access logging to track service usage
patterns. Configure Amazon CloudWatch Insights and AWS X-Ray to identify redundant or
inefficient API calls that could impact performance or exceed service quotas, with cost
optimization insights from AWS Cost Explorer API usage analysis.
- Conduct controlled performance testing using AWS
Load Testing Solution and Amazon CloudWatch Synthetics to establish baseline metrics for
normal operations. Configure dynamic thresholds using CloudWatch Anomaly Detection based
on these baselines to account for expected variations in manufacturing workloads,
leveraging Amazon Forecast for predictive baseline modeling.
- Design a multi-tiered alerting strategy using Amazon CloudWatch Alarms with Amazon SNS notifications and predictive alerts through CloudWatch
Anomaly Detection that identify concerning trends before they reach critical thresholds.
Implement automated remediation using AWS Systems Manager Automation, AWS Lambda
functions, and Amazon EventBridge rules for common performance issues to minimize human
intervention in manufacturing operations.

## Key AWS services

- Amazon CloudWatch for metrics collection and visualization
- AWS X-Ray for distributed tracing and latency analysis
- AWS CloudTrail for API activity monitoring
- AWS Compute Optimizer for resource optimization recommendations
- Amazon Managed Service for Prometheus and Amazon Managed Grafana for advanced
monitoring scenarios

## Resources

- [Monitoring AWS IoT Applications with
CloudWatch](https://docs.aws.amazon.com/iot/latest/developerguide/monitoring_overview.html)
- [Analyzing API Calls with CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html)
- [AWS X-Ray: Use a console](https://docs.aws.amazon.com/xray/latest/devguide/xray-console.html#xray-console-servicemap)
- [Service Quotas and Amazon CloudWatch
alarms](https://docs.aws.amazon.com/servicequotas/latest/userguide/configure-cloudwatch.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midaperf03-bp02.html*

---

# MIDAPERF04 — Troubleshoot and optimize pipelines

**Pillar**: Performance Efficiency  
**Best Practices**: 2

---

# MIDAPERF04-BP01 Implement end-to-end observability for manufacturing data pipelines

In manufacturing environments, comprehensive visibility into data processing and
ingestion infrastructures is critical for maintaining operational excellence and providing
timely delivery of production insights. Implementing robust observability solutions enables
rapid identification and resolution of issues that could impact data quality, processing
efficiency, or analytical outcomes.

**Desired outcome:** A fully observable data processing and ingestion infrastructure that provides immediate
visibility into performance metrics, error conditions, and processing bottlenecks, enabling
teams to quickly troubleshoot issues, minimize downtime, and maintain reliable data flows that
support critical manufacturing operations.

**Common anti-patterns:**

- Waiting for production teams to report data issues instead of proactive monitoring and alerting
- Using separate, disconnected monitoring tools that prevent correlation of issues across the entire data pipeline
- Implementing basic logging without contextual information like correlation IDs, production batch identifiers, or equipment-specific metadata
- Failing to trace data flows end-to-end through multi-stage processing pipelines, making bottleneck identification difficult
- Not monitoring edge gateways, industrial PCs, and on-premises servers that are critical points of failure
- Failing to track API interactions, retries, throttling, and authentication failures that can silently degrade pipeline performance
- Either over-sampling (causing performance overhead) or under-sampling (missing critical performance insights) in trace collection
- Inability to correlate symptoms across distributed manufacturing systems during troubleshooting
- Relying on manual detection of data quality issues, latency increases, or data gaps instead of automated monitoring
- Not configuring appropriate logging verbosity or failing to enhance detail levels during active troubleshooting scenarios
- Tracking only technical metrics without correlating to manufacturing KPIs like production batch status or equipment performance
- Lacking systematic protocols that isolate bottlenecks from sensor collection through visualization systems

**Benefits of establishing this best practice:**

- Reduces mean time to identification and resolution for data pipeline issues
- Enables correlation of symptoms across distributed manufacturing systems
- Provides transparency into third-party component interactions
- Facilitates root cause analysis through comprehensive tracing capabilities
- Supports continuous improvement of pipeline reliability and performance

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

- Implement structured logging across the data pipeline components using Amazon CloudWatch Logs for centralized log aggregation, AWS IoT Device Management for edge device logging, and Amazon Data Firehose for high-volume log streaming. Use AWS X-Ray trace IDs as correlation identifiers and leverage CloudWatch Log Insights for querying logs with manufacturing context like batch numbers and equipment tags.
- Deploy AWS X-Ray across your data services including Lambda functions, ECS containers, and API Gateway endpoints to trace data flow end-to-end. Configure X-Ray sampling rules to reduce overhead while maintaining visibility for critical manufacturing processes and use AWS App Mesh for service mesh tracing in containerized environments.
- Install Amazon CloudWatch agent on edge gateways and industrial PCs to collect system metrics, logs, and custom manufacturing metrics. Use AWS Systems Manager for agent deployment and configuration management and leverage AWS IoT Greengrass for edge computing monitoring with local data processing capabilities.
- Enable AWS CloudTrail for API call logging, configure Amazon API Gateway access logging and throttling monitoring, and use Amazon CloudWatch alarms to detect retry patterns and authentication failures. Implement AWS WAF logging for additional API security monitoring and use Amazon EventBridge for real-time API event processing.
- Create unified dashboards using Amazon CloudWatch Dashboards combined with AWS X-Ray service maps for end-to-end pipeline visualization. Use Amazon OpenSearch Service for advanced log analytics, Amazon Managed Grafana for custom manufacturing dashboards, and AWS Systems Manager OpsCenter for centralized operational issue management and correlation.

## Key AWS services

- Amazon CloudWatch for metrics, logs, and dashboards
- CloudWatch Agent for on-premises monitoring
- AWS X-Ray for distributed tracing and service maps
- AWS CloudTrail for API activity monitoring
- Amazon OpenSearch Service for advanced log analytics
- Amazon Managed Grafana for visualization (where applicable)

## Resources

- [Monitoring AWS IoT Applications with CloudWatch](https://docs.aws.amazon.com/iot/latest/developerguide/monitoring_overview.html)
- [Installing and Configuring the CloudWatch Agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.html)
- [Getting Started with AWS X-Ray](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html)
- [Analyzing API Calls with CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midaperf04-bp01.html*

---

# MIDAPERF04-BP02 Decouple data ingestion from processing in manufacturing systems

In manufacturing environments, tightly coupled data pipelines create single points of
failure that can lead to data loss and operational disruptions. Implementing a decoupled
architecture that separates ingestion from processing enhances system resilience, enables
independent scaling of components, and provides the foundation for reliable data processing
even during partial system failures common in industrial settings.

**Desired outcome:** A resilient manufacturing data architecture where ingestion and processing components
operate independently, enabling continuous data capture during processing failures, supporting
reprocessing capabilities when ingestion recovers from outages, and maintaining overall system
performance through appropriate component scaling.

**Common anti-patterns:**

- Tightly coupling data ingestion directly to processing components - Creates single
points of failure that can cause complete system shutdowns and data loss during processing
failures
- Implementing synchronous processing without buffering - Forces ingestion to wait for
processing completion, creating bottlenecks and reducing overall system throughput
- Using shared scaling policies for ingestion and processing - Leads to
over-provisioning or under-provisioning of resources since components have different load
patterns and scaling requirements
- Designing non-idempotent processing operations - Causes data corruption and
inconsistencies during replay scenarios, requiring expensive cleanup operations that
impact performance
- Failing to implement dead-letter queues or error handling - Results in infinite retry
loops that consume resources and degrade system performance during data quality issues
- Configuring insufficient buffer retention periods - Forces data loss during extended
outages, requiring expensive data recovery operations and potential reprocessing from
external sources
- Omitting queue depth monitoring for scaling decisions - Causes reactive rather than
proactive scaling, leading to buffer overflows and performance degradation during traffic
spikes
- Creating processing components without replay capabilities - Requires rebuilding
entire datasets during recovery, consuming significant computational resources and
extending downtime
- Using inadequate buffer storage capacity planning - Results in data loss during peak
ingestion periods or extended processing outages, requiring expensive data reconstruction
- Implementing blocking operations in ingestion pipelines - Creates cascading failures
where upstream data collection stops when downstream processing experiences issues
- Designing stateful processing without proper checkpointing - Forces complete
reprocessing from the beginning during failures, wasting computational resources and
extending recovery times
- Configuring overly aggressive retry policies without backoff - Overwhelms failing
components and prevents recovery while consuming network and computational resources
unnecessarily

**Benefits of establishing this best practice:**

- Helps prevent critical production data loss during equipment shutdowns or unplanned
downtime – Continually captures sensor readings, alarm states, and process variables even
when historians, SCADA systems, or edge devices require maintenance or experience hardware
failures.
- Allows dynamic resource allocation to match plant operational cycles and data volumes
- Enables scaling data ingestion during high-production periods or maintenance windows
while independently adjusting processing power for complex analytics like predictive
maintenance algorithms or real-time quality control calculations.
- Provides data replay capabilities for root cause analysis and process optimization -
Supports reprocessing historical operational data after system outages, calibration
changes, or when new analytics models are deployed to backfill insights for compliance
reporting or process improvement initiatives.
- Maintains data pipeline integrity despite industrial network instabilities and
equipment faults – Continually operates through common industrial challenges like network
congestion, PLC communication errors, fieldbus disruptions, or temporary sensor
malfunctions that frequently impact manufacturing environments.
- Minimizes production impact during system upgrades and reduces maintenance windows -
Enables rolling updates of data processing systems without disrupting critical real-time
monitoring, trending, or automated control loops, allowing maintenance activities during
normal production hours rather than costly scheduled downtime.

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

- Implement Durable Ingestion Buffers - Deploy Amazon Kinesis Data Streams or Amazon MSK (Kafka) for high-throughput streaming data with configurable retention periods up to
365 days. For batch workloads, use Amazon SQS with extended message retention and DLQ
configuration, combined with Amazon S3 for long-term storage overflow when queue limits
are approached.
- Design Idempotent Processing - Leverage Amazon DynamoDB conditional writes or
Amazon RDS with upsert operations for processing idempotency. Implement AWS Lambda with
event source mapping deduplication features or use Amazon Managed Service for Apache Flink for
exactly-once processing semantics. Store processing state in DynamoDB with composite
keys to track message processing status.
- Configure Dead-Letter Handling - Set up Amazon SQS Dead Letter Queues with Amazon CloudWatch alarms for message count thresholds. Use Amazon SNS to trigger notifications
when DLQ thresholds are exceeded. Store failed messages in Amazon S3 with lifecycle
policies for cost optimization and use AWS Step Functions for orchestrating retry logic
and failure investigation workflows.
- Implement Replay Capabilities - Utilize Kinesis Data Streams' time-based replay
functionality or Amazon MSK's offset management for streaming data replay. For batch
data, implement S3-based data lake architecture with AWS Glue ETL jobs that can
reprocess partitioned data based on timestamps. Use AWS Batch for large-scale
reprocessing jobs with automatic retry and scaling capabilities.
- Establish Independent Scaling - Configure Amazon EC2 Auto Scaling Groups with
custom CloudWatch metrics for queue depth monitoring. Use AWS Application Auto Scaling
for Kinesis shard scaling based on incoming records and iterator age metrics. Implement
AWS Lambda concurrent execution limits and reserved concurrency to help prevent
downstream system overload while allowing independent scaling of processing components.

## Key Services

- Amazon Kinesis Data Streams for scalable data ingestion
- Amazon SQS for durable message queuing
- Amazon MSK (Managed Streaming for Apache Kafka) for high-throughput streaming
- Amazon S3 for durable data landing and replay capabilities
- AWS Lambda for serverless processing of ingested data
- Amazon EventBridge for event-based processing orchestration

## Resources

- [Resilience in AWS Data Pipelines](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/disaster-recovery-resiliency.html)
- [AWS Prescriptive Guidance Patterns](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/decouple-microservices-using-amazon-sqs-and-aws-lambda.html)
- [Amazon EventBridge features](https://aws.amazon.com/eventbridge/features/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midaperf04-bp02.html*

---

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

# MIDAPERF06 — Data storage organization

**Pillar**: Performance Efficiency  
**Best Practices**: 1

---

# MIDAPERF06-BP01 Implement efficient storage and access for historical manufacturing data

In manufacturing environments, historical data serves critical functions beyond immediate
operational needs, supporting long-term trend analysis, root cause investigations, and
business performance validation. Implementing properly structured data lakes or warehouses for
historical manufacturing data improves cost-effective storage at scale while maintaining
analytical capabilities for deriving strategic insights from extended operational timelines.

**Desired outcome:** A scalable, cost-effective historical data architecture that efficiently stores years of
manufacturing data while enabling performant analytics, supporting business intelligence
requirements, and providing evidence-based validation of continuous improvement initiatives
across extended time periods.

**Common anti-patterns:**

- Storing all historical data in a single, unpartitioned repository without considering access patterns or query performance requirements
- Using row-based storage formats without compression, leading to unnecessarily high storage costs and slower query performance
- Keeping all historical data in expensive, high-performance storage tiers regardless of access frequency or business value
- Failing to maintain data catalogs, schemas, or business context, making historical data difficult to discover and interpret over time
- Not implementing materialized views, aggregation tables, or indexing strategies for common analytical patterns
- Storing manufacturing data without logical partitioning by time, production line, or product, forcing full dataset scans for targeted queries
- Using expensive, high-performance databases for historical data that doesn't require sub-second access times
- Not implementing automated tiering policies to move older data to cost-effective storage classes while maintaining accessibility
- Storing historical data in multiple incompatible formats without standardization, complicating cross-temporal analysis
- Relying on manual processes for data organization, optimization, and lifecycle management instead of automated policies and procedures

**Benefits of establishing this best practice:**

- Enables cost-effective storage of multi-year manufacturing data at petabyte scale
- Supports sophisticated trend analysis and pattern detection across extended
production history
- Provides factual basis for validating return on technology and process investments
- Facilitates root cause analysis of intermittent or slowly developing quality issues
- Serves as a foundation for advanced analytics and machine learning initiatives

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

- Build a multi-tier data lake using Amazon S3 with intelligent partitioning by date, hour, line, and product hierarchies, use AWS Lake Formation for centralized data lake management, and implement Amazon S3 Transfer Acceleration for high-speed manufacturing data uploads from plant edge systems.
- Deploy Apache Parquet and ORC columnar formats through AWS Glue ETL jobs with automatic compression algorithms, use Amazon S3 Intelligent-Tiering for cost optimization, and schedule AWS Glue crawlers to continuously optimize data layout based on manufacturing query access patterns.
- Implement AWS AWS Glue Data Catalog as your central metadata repository for the manufacturing datasets, use Amazon DataZone for business glossary management and data governance, and integrate AWS Lake Formation permissions to maintain data lineage and regulatory compliance across industrial data assets.
- Deploy Amazon Redshift materialized views for common manufacturing KPI aggregations, use Amazon Athena with AWS Glue for historical analysis when needed, and implement Amazon ElastiCache for frequently accessed production metrics and real-time dashboard acceleration.
- Configure S3 Lifecycle Management policies to automatically transition manufacturing data through storage classes (Standard to IA to Glacier to Deep Archive), implement AWS DataSync for automated archival processes, and use Amazon Macie to classify sensitive manufacturing data for appropriate retention and compliance management.

## Key AWS services

- Amazon S3 for scalable, durable object storage
- AWS Lake Formation for data lake management
- Amazon Athena for serverless SQL queries
- AWS Glue for data cataloging and ETL
- Amazon Redshift for data warehousing
- Quick for business intelligence

## Resources

- [Building a Data Lake on AWS](https://aws.amazon.com/blogs/big-data/build-a-data-lake-foundation-with-aws-glue-and-amazon-s3/)
- [Best Practices for Organizing S3 Objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/organizing-objects.html)
- [Implementing Data Lifecycle Management in S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html)

[Manufacturing analytic in regulated industries with MachineMetrics on AWS](https://aws.amazon.com/blogs/industries/manufacturing-analytics-in-regulated-industries-with-machinemetrics-on-aws/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midaperf06-bp01.html*

---

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
