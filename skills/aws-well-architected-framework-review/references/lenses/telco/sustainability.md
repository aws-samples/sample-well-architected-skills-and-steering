# Sustainability

**Pillar**: Sustainability  
**Questions**: 5

---

# TELCOSUS01 — Energy optimization

**Pillar**: Sustainability  
**Best Practices**: 1

---

# TELCOSUS01-BP01 Implement energy-efficient infrastructure for telco networks

When designing telco network infrastructure for sustainability, focus on optimizing
compute resources, implementing intelligent scaling, and leveraging edge computing to reduce
energy consumption. Start by analyzing your current network functions deployment patterns -
including virtual network functions (VNFs), cloud-based network functions (CNFs), and support
systems like business support systems (BSS) and operations support systems (OSS).

**Desired outcome:** Achieve reduction in energy consumption across
telco network operations through optimized infrastructure deployment, intelligent auto scaling,
and efficient resource utilization while maintaining service availability and meeting service
requirements.

**Benefits of establishing this practice:**

- Reduced energy costs through efficient
resource utilization.
- Progress toward net-zero emissions
commitments and Science Based Targets.
- Meeting government mandates for
carbon reduction in telecommunications.
- Improved performance through right-sized
infrastructure.
- Automated scaling reduces manual
intervention and human error.

**Level of risk exposed if this best practice is not established:**
Low

## Implementation guidance

For compute optimization, use AWS Compute Optimizer to analyze your EC2 instances running telco
workloads and receive recommendations for rightsizing. Deploy your network functions on AWS
Graviton-based instances which provide up to 60% better energy efficiency compared to
comparable x86-based instances. For containerized network functions, use Amazon ECS with
AWS Fargate Spot or Amazon EKS with Karpenter to automatically optimize container placement and
reduce idle capacity.

Implement edge computing strategies using AWS Outposts, AWS Local Zones, or AWS Wavelength to
process data closer to Radio Access Network (RAN) sites and end users. This reduces backhaul
traffic and core network energy consumption. For 5G deployments, use AWS Wavelength to embed
compute and storage at the network edge within telecommunications providers' datacenters.

Configure AWS Auto Scaling with predictive scaling policies based on historical traffic patterns
typical in telco networks (peak hours, special events, seasonal variations). Use Amazon CloudWatch to
monitor metrics like CPU utilization, network throughput, and custom metrics from your network
functions to trigger scaling actions.

### Implementation steps

- Deploy AWS Compute Optimizer and analyze recommendations for EC2 instances running telco workloads.
Generate reports to identify over-provisioned instances and potential savings.
- Implement tagging strategy for telco resources using tags like Environment,
NetworkFunction, TrafficPattern to enable granular monitoring and optimization.
- Configure AWS Systems Manager to automatically stop non-production telco workloads during
off-hours and weekends using Maintenance Windows and Automation documents.
- Deploy Amazon CloudWatch Container Insights for ECS/EKS clusters running containerized
network functions to identify idle containers and optimization opportunities.
- Set up AWS Auto Scaling with target tracking policies for core network functions, using
metrics like requests per second or concurrent sessions typical in telco workloads.
- Implement AWS Lambda for event-driven telco functions like billing notifications,
network alerts, and configuration updates to reduce idle compute.
- Use AWS Cost and Usage Reports with hourly granularity to correlate resource
usage with network traffic patterns and identify optimization windows.

## Resources

**Key AWS services:**

- [EC2](https://aws.amazon.com/ec2/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
- [EKS](https://aws.amazon.com/pm/eks/)
- [ECS](https://aws.amazon.com/ecs/)
- [AWS Lambda](https://aws.amazon.com/lambda/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/telco-lens/telcosus01-bp01.html*

---

# TELCOSUS02 — Data processing and storage

**Pillar**: Sustainability  
**Best Practices**: 1

---

# TELCOSUS02-BP01 Implement efficient data lifecycle management for telco networks

telco networks generate diverse data types with varying retention requirements. Call
detail records (CDRs) requiring long-term retention for regulatory adherence, network
performance metrics needed for real-time analysis, and IoT sensor data with high velocity but
short relevance periods. Design your data architecture to automatically optimize storage based
on access patterns while maintaining adherence with telecommunications regulations.

**Desired outcome:** Reduce storage costs and energy consumption
through intelligent data tiering, compression, and lifecycle management while maintaining
adherence with telecommunications regulatory requirements for data retention and accessibility.

**Benefits of establishing this practice:**

- Achieve reduction in storage costs
through intelligent tiering and compression.
- Automated retention policies meeting
telecommunications data regulations.
- Faster data processing through
optimized storage patterns.
- Lower energy consumption from
reduced storage infrastructure.
- Automated data management reducing
manual intervention.

**Level of risk exposed if this best practice is not established:**
Low

## Implementation guidance

Start by categorizing your telco data based on regulatory requirements, access frequency,
and business value. For CDRs and lawful intercept data, implement immutable storage with
defined retention periods. For network telemetry and performance data, use time-series
optimized storage with aggressive compression. For customer analytics and billing data,
implement tiered storage based on access patterns.

Use Amazon S3 Intelligent-Tiering to automatically move data between frequent, infrequent, and
archive access tiers without performance impact or operational overhead. Configure lifecycle
policies specific to telco data types (for example, moving CDRs to Glacier Deep Archive after
90 days (about three months) while keeping metadata in Amazon S3 Standard for quick retrieval).

For real-time data processing, implement stream processing architectures using Amazon Kinesis Data Streams
for ingesting network telemetry, with Managed Service for Apache Flink for real-time anomaly detection and Firehose for
delivering processed data to Amazon S3 in compressed Parquet format.

### Implementation steps

- Create S3 buckets with specific naming conventions for different telco data types,
for example: `cdr-data`, `network-telemetry`, `customer-analytics`, or `iot-sensors`.
- Enable S3 Intelligent-Tiering on S3 buckets and configure archive policies: CDRs to
Deep Archive after 90 days (about three months) and network logs to Glacier Instant after 30
days (about a month).
- Implement AWS Glue ETL jobs to compress and convert raw telco data to columnar
formats (like Parquet or ORC).
- Deploy Amazon Kinesis Data Streams with shard auto scaling for ingesting real-time network data,
sized based on peak traffic.
- Configure Managed Service for Apache Flink applications with SQL queries to detect network anomalies and
aggregate metrics in real-time, reducing downstream processing needs.
- Set up AWS Lambda functions triggered by S3 events to validate data adherence, apply
compression, and update metadata in Amazon DynamoDB.
- Implement Amazon Athena with partition projection for querying historical telco data
directly from S3 without maintaining separate data warehouses.
- Create CloudWatch dashboards to monitor storage metrics, data transfer costs, and
lifecycle transition effectiveness.

## Resources

**Key AWS services:**

- [Amazon S3](https://aws.amazon.com/s3)
- [AWS Glue](https://aws.amazon.com/glue/)
- [Amazon Kinesis Data Streams/Analytics](https://aws.amazon.com/pm/kinesis/)
- [AWS Lambda](https://aws.amazon.com/lambda/)
- [Amazon DynamoDB](https://aws.amazon.com/dynamodb/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/telco-lens/telcosus02-bp01.html*

---

# TELCOSUS03 — Investment protection

**Pillar**: Sustainability  
**Best Practices**: 1

---

# TELCOSUS03-BP01 Adopt circular economy principles for telco network assets

Implementing circular economy principles in telco networks requires comprehensive
visibility into physical and virtual assets throughout their lifecycle. This includes tracking
network equipment from procurement through decommissioning, optimizing hardware utilization to
extend lifespan, and establishing processes for equipment refurbishment and responsible
recycling.

**Desired outcome**: Extend network equipment lifespan through
predictive maintenance, optimize asset utilization, and establish sustainable end-of-life
processes for hardware recycling and repurposing, reducing electronic waste and capital
expenditure.

**Benefits of establishing this practice:**

- Achieve reduction in equipment
replacement costs through lifecycle extension.
- Minimized electronic waste through reuse
and responsible recycling.
- Improved utilization rates through
better visibility.
- Meeting circular economy
regulations and corporate ESG commitments.
- Data-driven decisions on asset
replacement and maintenance.

**Level of risk exposed if this best practice is not established:**
Low

## Implementation guidance

Design an asset tracking system that monitors both physical infrastructure (base
stations, routers, switches) and virtual resources (VNF licenses, cloud resources). Use IoT
sensors to track equipment health metrics like temperature, power consumption, and performance
degradation to predict optimal replacement timing and identify reuse opportunities.

Implement predictive maintenance using machine learning to extend equipment lifespan. By
analyzing historical failure patterns and real-time telemetry, you can perform maintenance
before failures occur, reducing premature equipment replacement and minimizing electronic
waste.

### Implementation steps

- Deploy AWS IoT Core to connect and manage telco network equipment sensors, creating
digital twins for major assets like base stations and core network equipment.
- Configure AWS IoT SiteWise to model your telco asset hierarchy (regions, sites, equipment
types) and collect metrics on utilization, energy consumption, and health status.
- Implement Amazon Timestream to store time-series data from network equipment, enabling
long-term trend analysis for predictive maintenance.
- Create AWS IoT Events detectors to identify equipment approaching end-of-life based on
performance degradation patterns specific to telco equipment.
- Deploy Amazon SageMaker AI to build predictive maintenance models using historical failure
data.
- Set up Quick dashboards displaying asset utilization rates, predicted replacement
schedules, and opportunities for equipment redeployment.
- Implement AWS Systems Manager Inventory to track software licenses and virtual resource
allocation, identifying underutilized assets for reallocation.
- Configure Amazon SNS notifications for equipment lifecycle events (like warranty expiration,
maintenance due, and end-of-life) to enable proactive asset management.

## Resources

**Key AWS services:**

- [AWS IoT Core](https://aws.amazon.com/iot-core/)
- [Quick](https://aws.amazon.com/quicksuite/quicksight/)
- [Amazon SNS](https://aws.amazon.com/sns/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/telco-lens/telcosus03-bp01.html*

---

# TELCOSUS04 — Climate change risk

**Pillar**: Sustainability  
**Best Practices**: 1

---

# TELCOSUS04-BP01 Enhance telco network resilience to climate change risks

Climate resilience for telco networks requires architecting for extreme weather events,
implementing geographic redundancy, and establishing automated failover mechanisms. Design
your infrastructure to withstand increasing frequency of floods, heatwaves, storms, and other
climate-related disruptions while maintaining service continuity for critical communications.

**Desired outcome:** Achieve network availability despite
climate-related disruptions through geographic redundancy, automated failover mechanisms, and
predictive risk management, maintaining continuous service for critical communications during
extreme weather events.

**Benefits of establishing this practice:**

- Maintained network availability during
extreme weather events.
- Achieve reduction in climate-related
service disruptions.
- Enhanced capacity to support
disaster response communications.
- Meeting government requirements for
critical infrastructure resilience.
- Improved reputation as reliable service
provider during emergencies.

**Level of risk exposed if this best practice is not established**:
Low

## Implementation guidance

Start by mapping your network infrastructure against climate risk data to identify
vulnerable locations. For high-risk areas, implement additional redundancy and strengthened
physical protection. Deploy critical network functions across multiple AWS Regions and
Availability Zones to verify geographic diversity. For edge locations, use AWS Outposts with
ruggedized options for harsh environments.

Implement real-time environmental monitoring at cell sites and data centers to detect
climate-related threats early. Use predictive analytics to anticipate weather-related traffic
surges (emergency calls during disasters) and pre-scale resources accordingly. Design
automated response systems that can reroute traffic, activate backup sites, and notify
operations teams without manual intervention.

### Implementation steps

Deploy AWS Outposts or Local Zones in geographically diverse locations, maintaining
critical network functions are distant apart to avoid single weather event impact.

- Implement AWS Backup with cross-Region replication for critical telco workloads,
with the appropriate Recovery Time Objectives (RTO) for essential services.
- Configure Amazon Route 53 health checks with automatic DNS failover for critical
endpoints, verifying traffic reroutes upon failure detection.
- Set up AWS IoT Core to collect environmental data (like temperature, humidity, and water
levels) from cell sites, with IoT Analytics to predict climate-related risks.
- Create AWS Lambda functions triggered by weather API data to automatically scale
resources in anticipation of emergency traffic surges.
- Implement AWS Step Functions to orchestrate complex disaster recovery workflows, including
service failover, data synchronization, and stakeholder notifications.
- Deploy Amazon CloudWatch Synthetics to continuously monitor service availability from
multiple geographic locations, simulating user traffic patterns.
- Configure AWS Systems Manager Automation documents for common climate-related scenarios
(like power outage response, flooding protocols, and heatwave procedures).

## Resources

**Key AWS services:**

- [AWS Outposts](https://aws.amazon.com/outposts/)
- [Amazon Route 53](https://aws.amazon.com/route53/)
- [AWSIoT Core](https://aws.amazon.com/iot-core/)
- [AWS Lambda](https://aws.amazon.com/lambda/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/telco-lens/telcosus04-bp01.html*

---

# TELCOSUS05 — Carbon tracking

**Pillar**: Sustainability  
**Best Practices**: 1

---

# TELCOSUS05-BP01 Establish comprehensive carbon footprint monitoring for telco networks

Measuring carbon footprint across telco operations requires tracking emissions from
multiple sources including data centers, network equipment, edge sites, and even supply chain
activities.

**Desired outcome:** Achieve complete visibility of carbon
emissions across network operations with automated tracking, reporting accuracy, and actionable
insights that enable emission reductions aligned with Science Based Targets initiative (SBTi)
commitments.

**Benefits of establishing this practice:**

- Automated reporting for
telecommunications environmental regulations.
- Identify and prioritize
highest-impact reduction opportunities.
- Accurate sustainability reporting
for investors and customers.
- Demonstrated environmental
leadership in telecommunications sector.
- Link carbon reduction initiatives to
operational cost savings.

**Level of risk exposed if this best practice is not established**:
Low

## Implementation guidance

Implement a comprehensive monitoring system that captures the following while
providing actionable insights for reduction strategies:

- Scope 1: direct emissions
- Scope 2: purchased electricity
- Scope 3: value chain emissions

Design your monitoring architecture to automatically collect energy consumption data from
infrastructure components. Tag AWS resources with sustainability metadata (equipment type,
location, and business function) to enable granular carbon accounting. Integrate with AWS
Customer Carbon Footprint Tool for baseline cloud emissions data, then augment with custom
metrics for on-premises equipment and network operations.

Establish automated reporting pipelines that aggregate carbon data, calculate emissions
using regional grid factors, and generate reports for regulatory requirements and
sustainability frameworks like SBTi or Global System for Mobile
Communications Association (GSMA) climate targets.

### Implementation steps

- Enable AWS Customer Carbon Footprint Tool and configure monthly exports to S3 for
historical analysis and trend tracking.
- Implement comprehensive tagging strategy with tags: `CarbonCategory`, `LocationGrid`,
`NetworkFunction`, and `EquipmentType` for AWS resources.
- Deploy Amazon CloudWatch custom metrics to track energy consumption from on-premises network
equipment using AWS IoT Greengrass at edge sites.
- Create AWS Glue ETL pipelines to combine AWS carbon data with on-premises
metrics, calculating total emissions using Regional emission factors.
- Set up Amazon Managed Grafana dashboards displaying real-time carbon intensity metrics, with
drill-down capabilities by service, region, and network function.
- Configure Quick to generate automated monthly sustainability reports aligned with
GSMA or SBTi reporting requirements.
- Implement Amazon EventBridge rules to trigger alerts when carbon emissions exceed defined
thresholds or deviate from reduction targets.
- Deploy AWS Lambda functions to calculate power usage effectiveness (PUE) for data
centers and network efficiency metrics for RAN sites.
- Use Amazon Forecast to predict future carbon emissions based on network growth
projections and planned efficiency improvements.

## Resources

**Key AWS services:**

- [Amazon S3](https://aws.amazon.com/s3/)
- [AWS Glue](https://aws.amazon.com/glue/)
- [Quick](https://aws.amazon.com/quicksuite/quicksight/)
- [Amazon EventBridge](https://aws.amazon.com/eventbridge/)
- [AWS Lambda](https://aws.amazon.com/lambda/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/telco-lens/telcosus05-bp01.html*

---

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
