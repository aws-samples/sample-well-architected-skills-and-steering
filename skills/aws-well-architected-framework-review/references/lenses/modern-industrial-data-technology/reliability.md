# Reliability

**Pillar**: Reliability  
**Questions**: 5

---

# MIDAREL01 — Foundations

**Pillar**: Reliability  
**Best Practices**: 2

---

# MIDAREL01-BP01 Monitor manufacturing-specific service quotas

Implement proactive monitoring and management of service quotas that are critical to
manufacturing operations. Manufacturing workloads often have unique patterns of resource
consumption based on production cycles, which require specialized monitoring approaches.

**Desired outcome:** Your manufacturing workloads remain fully
operational without disruption from quota limits, especially during peak production periods or
when processing high volumes of sensor data. Early identification of approaching quota limits
allows for timely adjustments.

**Benefits of establishing this best practice:** Helps prevent
production downtime caused by service disruptions, maintains consistent performance of
real-time monitoring systems, and supports continuous operation of automated manufacturing
processes. This approach also helps optimize costs by right-sizing resources according to
actual production needs.

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

Before implementing service quota management in manufacturing environments, it's
crucial to understand how quotas impact different aspects of your industrial operations.
Manufacturing workloads often have unique patterns of resource consumption based on
production cycles, maintenance windows, and seasonal demands. A comprehensive quota
management strategy should consider both steady-state operations and peak production periods
to help prevent disruptions to critical manufacturing processes.

Start by establishing baseline quota requirements for different manufacturing
scenarios:

- Normal production operations
- Peak production periods
- Maintenance and quality inspection windows
- End-of-month/quarter reporting cycles
- Emergency response situations

Consider implementing a multi-layered approach that includes proactive monitoring,
automated alerting, and buffer capacity for unexpected spikes in demand. This strategy helps
prevent quota-related disruptions while maintaining operational efficiency.

### Implementation steps

- **Use AWS Service Quotas and AWS Trusted Advisor:**
Configure Service Quotas to track usage across critical manufacturing systems and set up
Amazon CloudWatch alarms to notify when approaching thresholds. Use Trusted Advisor to
receive recommendations about service limits and usage optimization.
- **Implement request queuing:** Deploy Amazon SQS queues
to buffer incoming requests during peak production periods, helping prevent quota
exceedance while processing all data eventually.
- **Configure dynamic resource allocation:** Use AWS Auto Scaling to automatically adjust resource capacity based on manufacturing production
schedules and real-time demand from factory floor systems.
- **Set up cross-Region redundancy:** Implement AWS Global Accelerator to distribute workloads across multiple Regions, reducing the risk of
regional quota limitations affecting manufacturing operations.

## Key AWS services

- AWS Service Quotas
- AWS Trusted Advisor
- Amazon CloudWatch
- Amazon SQS
- AWS Auto Scaling
- AWS Global Accelerator

## Resources

- [Viewing service quotas and setting CloudWatch
alarms](https://docs.aws.amazon.com/servicequotas/latest/userguide/configure-cloudwatch.html)
- [Using Amazon SQS to manage request
rates](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/quotas-messages.html)
- [Target tracking scaling policies for Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-target-tracking.html)
- [Optimizing global network performance with AWS Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/introduction-how-it-works.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midarel01-bp01.html*

---

# MIDAREL01-BP02 Scale network architecture for manufacturing operations

In manufacturing environments, network reliability is crucial as disruptions can directly
impact production, quality, and safety. A reliable network architecture must provide
continuous operations even during component failures, maintenance windows, or unexpected
spikes in industrial data traffic. Implementing redundant connections, proper network
segmentation, and automated failover mechanisms helps maintain operational continuity across
the manufacturing floor.

**Desired outcome:** A resilient network infrastructure that
supports manufacturing operations without disruption, creating a continuous data flow between
manufacturing equipment and edge devices, with appropriate redundancy and failover
capabilities.

**Benefits of establishing this best practice:**

- Minimizes production downtime due to network failures
- Provides consistent data collection from production equipment
- Maintains operational integrity during maintenance or failures
- Supports scaling production capacity without compromising reliability
- Enables real-time decision making through dependable data transmission

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

Establish redundant connectivity with automatic failover capabilities to improve the
continuity of your network operations. Implement multiple network paths to help prevent
single points of failure, with automated routing to alternative connections during
disruptions.

Consider implementing redundant connections using services like AWS Direct Connect and
AWS Site-to-Site VPN with AWS Transit Gateway to enable automatic failover and routing
capabilities across multiple network paths.

Design network segmentation that isolates critical manufacturing zones (production,
quality control, and maintenance) while maintaining appropriate communication paths.
Implement security boundaries that help protect sensitive manufacturing operations without
impeding necessary data flows.

Consider using Amazon VPC with multiple subnets and AWS Transit Gateway to create
isolated network zones while maintaining controlled communication paths. Network ACLs and
security groups can provide additional security boundaries for manufacturing-specific
requirements.

Deploy comprehensive network monitoring that tracks performance metrics, sets up alerts
for latency or throughput issues, and creates dashboards specific to manufacturing network
requirements. Include proactive monitoring of network health and automated notification
systems for potential issues.

Consider implementing monitoring using services like Amazon CloudWatch and AWS Network
Manager to track network health metrics and create automated alerts. Amazon EventBridge can
help orchestrate automated responses to network events.

Configure automated recovery procedures when network anomalies are detected in
manufacturing environments. Implement self-healing capabilities that can automatically
reroute traffic or fail over to backup systems without manual intervention.

Consider using AWS Systems Manager Automation with Amazon Route 53 health checks to
automatically detect and respond to network issues. Use AWS Lambda to implement custom
recovery logic based on your manufacturing requirements.

## Key AWS services

- AWS Direct Connect
- AWS Site-to-Site VPN
- AWS Transit Gateway
- Amazon VPC
- AWS Network Manager
- Amazon CloudWatch
- AWS Lambda
- AWS Auto Scaling

## Resources

[Building a Scalable and Secure Multi-VPC AWS Network
Infrastructure](https://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/welcome.html)

[AWS Direct Connect Resiliency
Recommendations](https://docs.aws.amazon.com/directconnect/latest/UserGuide/resiliency_recommendation.html)

[Monitoring Network Health with Network
Manager](https://aws.amazon.com/about-aws/whats-new/2022/11/network-manager-real-time-performance-monitoring-aws-global-network/)

[AWS Transit Gateway Network Manager for Industrial
IoT](https://pages.awscloud.com/Introduction-to-AWS-Transit-Gateway-Network-Manager_2019_1214-NET_OD.html?cr=%7Bcreative%7D&kw=%7Bkeyword%7D)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midarel01-bp02.html*

---

# MIDAREL02 — Workload architecture

**Pillar**: Reliability  
**Best Practices**: 3

---

# MIDAREL02-BP01 Design resilient industrial integration patterns

Implement redundant and fault-tolerant architectural patterns that maintain operational
continuity during system failures. Your manufacturing data architecture should include local
processing capabilities, data buffering, and automatic recovery mechanisms to verify that
critical production processes continue even when cloud connectivity or key systems fail.

**Desired outcome:** Manufacturing operations continue with
minimal disruption when systems fail, with production data preserved and synchronized once
systems are restored. Critical operational parameters remain accessible to machine operators,
and production workflows continue functioning through degraded modes.

**Benefits of establishing the Best Practice:** By implementing
resilient integration patterns, manufacturers can minimize production downtime, maintain
product quality during system failures, preserve critical operational data, and properly
synchronize systems once they are restored, ultimately helping protect revenue and customer
satisfaction.

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

**Implement edge computing solutions**

First, assess your manufacturing systems' criticality, required processing latency, and
local autonomy requirements.

Document which operations must continue during cloud connectivity disruptions.

Design local processing capabilities that can operate independently when disconnected,
with clear rules for autonomous decision-making and data buffering.

Consider implementing AWS IoT Greengrass on factory floor gateways to enable local
processing and autonomous operations during connectivity issues, with rules that determine
which operations can continue locally and which require cloud connectivity.

**Create data buffering mechanisms**

Begin by analyzing your data generation patterns, storage requirements, and acceptable
data latency windows. Document recovery time objectives (RTOs) and recovery point objectives
(RPOs) for different data types.

Implement local storage mechanisms that can retain manufacturing data during outages
and automatically synchronize when connectivity is restored.

Consider using AWS IoT SiteWise Edge to store time-series production data locally
during connectivity interruptions, with automatic synchronization to AWS IoT SiteWise in the
cloud when connectivity returns.

**Design circuit breaker patterns**

Start by mapping dependencies between manufacturing systems and identifying potential
failure points. Define graceful degradation modes for each critical service and establish
fallback mechanisms.

Implement patterns that can detect failures and automatically switch to alternative
processing paths.

Consider implementing circuit breakers using AWS Step Functions to handle failures in
downstream dependencies and automatically switch to predefined fallback mechanisms that
maintain critical manufacturing operations.

**Configure automatic failover systems**

First document your manufacturing system's availability requirements and acceptable
downtime windows. Establish clear failover activations and recovery procedures.

Design redundant connectivity paths with automated switching capabilities to maintain
continuous operations.

Consider deploying redundant AWS IoT Core endpoints with automatic failover
capabilities to provide reliable connectivity between manufacturing systems and cloud
services, with monitoring to verify successful failover operations.

## Key AWS services

- AWS IoT Greengrass
- AWS IoT SiteWise
- AWS Step Functions
- AWS IoT Core
- Amazon Kinesis Data Streams

## Resources

- [Implementing Edge Computing with AWS IoT Greengrass](https://docs.aws.amazon.com/greengrass/v2/developerguide/edge-runtime.html)
- [Configuring Data Buffering with AWS IoT SiteWise
Edge](https://aws.amazon.com/about-aws/whats-new/2023/11/aws-iot-sitewise-buffered-batched-measurement-data/)
- [Designing Resilient Industrial Applications with AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-error-handling.html)
- [Building High Availability Industrial IoT Solutions with
AWS](https://docs.aws.amazon.com/whitepapers/latest/industrial-iot-architecture-patterns/variant-7-edge-gateway-high-availability.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midarel02-bp01.html*

---

# MIDAREL02-BP02 Verify data consistency and availability across OT/IT systems through redundancy and failover mechanisms

Manufacturing environments operate with complex interactions between OT and IT systems.
When these systems fail, the impact can cascade through production lines, quality control
processes, and enterprise planning systems. Successfully maintaining data consistency and
system availability requires careful orchestration of data synchronization, communication
paths, and recovery procedures across the manufacturing technology stack.

**Desired outcome:** Production operations continue with
minimal disruption during system failures. Critical operational data remains available and
consistent during disruptions, allowing for automated or manual fallback procedures to
maintain production output while primary systems are restored.

**Benefits of establishing the Best Practice:**

- Minimize production downtime and associated revenue losses.
- Preserve data integrity across manufacturing systems.
- Enable smooth recovery without data reconciliation challenges.
- Maintain quality control and regulatory compliance during system failures.

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

**Real-time manufacturing data management**

First, map your critical manufacturing data flows and establish requirements for data
synchronization across OT/IT systems. Document recovery time objectives (RTOs), recovery
point objectives (RPOs), and regulatory compliance needs.

Define data models that support consistent representation of equipment states and
process parameters across systems.

For implementation, establish standardized data models and real-time state management
systems for production equipment and processes. Verify data consistency through distributed
databases with conflict resolution capabilities.

Consider using AWS IoT SiteWise for consistent equipment and process data models, AWS IoT Core's Device Shadow service for reliable state management, and Amazon DynamoDB global
tables for distributed manufacturing data management.

**Data validation and quality controls**

Document data quality requirements for different manufacturing processes and establish
validation rules. Define acceptable tolerance ranges for process parameters and identify
critical quality metrics that must be maintained during system transitions.

Implement automated validation mechanisms that verify data integrity across systems,
with standardized data quality rules and monitoring.

Set up continuous validation of data synchronization between OT/IT systems and
establish regular backup points for critical manufacturing datasets.

Consider implementing AWS Glue Data Quality rules for automated validation, AWS IoT SiteWise Asset Models for standardized validation, and AWS Backup for consistent recovery
points.

**Recovery mechanisms and failover systems**

Document system dependencies and define acceptable failover scenarios. Establish clear
procedures for both automated and manual recovery processes.

Determine sequence of operations for graceful system transitions that preserve data
integrity. Design idempotent processing mechanisms to help prevent data duplication during
recovery.

Implement point-in-time recovery capabilities for critical production systems and
configure automated failover with health monitoring.

Consider using Amazon DynamoDB Point-in-Time Recovery for maintaining accurate
operational states, Amazon Route 53 health checks for automated failover, and AWS Systems Manager for coordinated recovery automation.

## Key AWS services

- AWS IoT SiteWise
- AWS IoT Core
- Amazon Timestream
- Amazon DynamoDB
- AWS Glue Data Quality
- Amazon CloudWatch
- AWS Backup
- Amazon Route 53
- AWS Systems Manager

## Resources

- [AWS IoT SiteWise for industrial data collection and monitoring](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/what-is-sitewise.html)
- [Using Device Shadows for manufacturing equipment state management](https://docs.aws.amazon.com/iot/latest/developerguide/iot-device-shadows.html)
- [Implementing DynamoDB Global Tables for distributed manufacturing data](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GlobalTables.html)
- [AWS Glue
Data Quality for manufacturing data validation](https://docs.aws.amazon.com/glue/latest/dg/data-quality.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midarel02-bp02.html*

---

# MIDAREL02-BP03 Enable automated recovery mechanisms

Design your manufacturing workloads with automated recovery processes that allow
production to continue despite OT and IT system failures. Implement edge processing
capabilities that can operate independently when disconnected from central IT systems.

**Desired outcome:** Production operations continue without
interruption even when data collection systems, network connectivity, or cloud services
experience failures. Critical manufacturing data is preserved and synchronized once systems
are restored.

**Benefits of establishing the best practice:** Minimizing
production downtime, preserving data integrity during system failures, reducing manual
intervention during recovery processes, and maintaining product quality metrics during system
disruptions.

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

**Implement edge computing capabilities**

Assess your manufacturing system's autonomy requirements and identify critical
processes that must continue during connectivity loss. Document acceptable operational modes
during disconnected states and establish clear thresholds for autonomous decision-making.

Design local processing systems that support offline operations, with clearly defined
rules for degraded mode operations and boundaries for autonomous decisions based on safety
requirements and operational parameters.

For implementation, deploy edge computing capabilities that can maintain essential
operations during network disruptions. This requires integration with industrial control
systems and PLCs for real-time operations with appropriate redundancy and failover
mechanisms for critical manufacturing processes.

Consider using AWS IoT Greengrass to maintain local processing and decision-making when
connectivity is lost. Configure AWS IoT Greengrass components to cache production data locally and
execute critical workflows without cloud dependency.

**Deploy local data buffering mechanisms**

Analyzing your data generation patterns and retention requirements. Define priorities
for different data types and establish minimum retention periods based on operational and
compliance needs. Document synchronization requirements for when connectivity is restored.

Implement robust local storage systems with appropriate capacity planning for expected
outage durations. Configure data retention policies that preserve critical production
metrics during disconnection periods.

Consider using AWS IoT SiteWise Edge to continually collect data during network
outages, with configured data retention policies for high-value production metrics.

**Create automated data synchronization protocols**

Map data dependencies and establishing synchronization priorities. Define conflict
resolution rules for handling data updates during disconnected operations.

Document recovery procedures for different types of outages.

Design synchronization mechanisms that can handle data reconciliation when connectivity
is restored. Implement prioritization rules for critical production data during reconnection
events.

Consider using AWS IoT Core rules to prioritize critical production data during
reconnection events, with clear handling of potential data conflicts.

**Establish monitoring and alerting systems**

Define normal operational parameters and alert thresholds. Document escalation
procedures and response requirements for different types of failures.

Establish KPIs for measuring recovery effectiveness. Implement comprehensive monitoring
of both edge and cloud components.

Configure automated alerts based on predefined thresholds and create recovery procedure
activations.

Consider using Amazon CloudWatch to detect failures and automatically initiate recovery
procedures based on predefined thresholds specific to manufacturing processes.

## Key AWS services

- AWS IoT Greengrass
- AWS IoT SiteWise
- AWS IoT Core
- Amazon CloudWatch
- AWS Lambda
- Amazon S3

## Resources

- [Implementing local processing with AWS IoT Greengrass](https://docs.aws.amazon.com/greengrass/v2/developerguide/local-processing.html)
- [Data buffering with AWS IoT SiteWise
Edge](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/edge-data-processing.html)
- [Designing resilient manufacturing applications with AWS IoT Core](https://docs.aws.amazon.com/whitepapers/latest/designing-mqtt-topics-aws-iot-core/designing-mqtt-topics-aws-iot-core.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midarel02-bp03.html*

---

# MIDAREL03 — Change management

**Pillar**: Reliability  
**Best Practices**: 1

---

# MIDAREL03-BP01 Implement dynamic scaling for shop floor data ingestion pipelines

Manufacturing operations generate varying volumes of data from machines, sensors, and
production lines. Dynamic scaling verifies that your data ingestion pipelines can handle peak
production times without overprovisioning during slower periods.

**Desired outcome:**

A resilient data ingestion system that automatically scales to accommodate fluctuating
data volumes from the shop floor, providing consistent performance during peak production
while optimizing costs during lower activity periods.

**Benefits of establishing this best practice:**

- Cost optimization by avoiding overprovisioning of resources.
- Improved system reliability during production surges.
- Consistent data processing regardless of production volumes.
- Enhanced ability to capture critical manufacturing data during unexpected events.

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

**Design scalable data ingestion architecture**

Assess your manufacturing data sources, volumes, and velocity requirements. Document
peak production periods, shift patterns, and seasonal variations that affect data generation
rates.

Identify critical data streams that require guaranteed delivery and establish
performance baselines for normal operations.

Define acceptable latency thresholds for different types of manufacturing data.

For implementation, create a flexible ingestion architecture that can automatically
adapt to changing production volumes. Design ingestion paths with appropriate buffering and
throttling mechanisms to handle sudden surges in manufacturing data.

Consider using AWS IoT Core and AWS Lambda for serverless ingestion points that
automatically scale with the volume of incoming sensor data from manufacturing equipment.

**Configure stream processing capabilities**

Map your data processing requirements and identifying real-time analytics needs.

Document throughput requirements for different production scenarios and establish
monitoring thresholds.

Define scaling triggers based on production metrics rather than just system metrics.

For implementation, establish stream processing mechanisms that can handle variable
throughput from production lines while maintaining data consistency. Include automatic
scaling capabilities based on actual production demands and data volumes.

Consider setting up Amazon Kinesis Data Streams with appropriate shard management to
handle varying throughput from production lines.

**Implement data flow controls**

Analyze your data priority levels and establish handling rules for different data
types.

Define quality of service requirements for critical manufacturing data and document
acceptable processing delays for non-critical data.

Establish clear overflow handling procedures for peak production periods.

For implementation, deploy mechanisms to manage data flow rates and help prevent system
overload during production peaks. Create prioritization schemes that process critical
manufacturing data first during high-load periods.

Consider implementing Amazon SQS queues between data collection points and processing
systems to handle sudden surges in manufacturing data.

**Establish comprehensive monitoring**

Define key performance indicators for your data ingestion system. Document alerting
thresholds based on production requirements and establish escalation procedures.

Create baseline metrics for normal operations across different production scenarios.

For implementation, deploy monitoring systems that track both technical metrics and
production-related indicators. Configure automated alerts for potential bottlenecks or
capacity issues before they impact production.

Consider using Amazon CloudWatch to track performance metrics and adjust scaling
parameters based on historical production patterns and seasonal manufacturing demands.

## Key AWS services

- Amazon Kinesis Data Streams
- AWS Lambda
- Amazon SQS
- AWS IoT Core
- Amazon CloudWatch
- AWS Auto Scaling

## Resources

- [Auto Scaling for Amazon Kinesis Data Streams](https://docs.aws.amazon.com/streams/latest/dev/service-sizes-and-limits.html)
- [Serverless event-driven architecture for industrial data
ingestion](https://docs.aws.amazon.com/serverless/latest/devguide/serverless-transition.html)
- [Implementing the IoT analytics pipeline for
manufacturing](https://docs.aws.amazon.com/iotanalytics/latest/userguide/create-pipeline.html)
- [Designing scalable IoT applications with
AWS](https://aws.amazon.com/blogs/iot/how-to-build-a-scalable-multi-tenant-iot-saas-platform-on-aws-using-a-multi-account-strategy/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midarel03-bp01.html*

---

# MIDAREL04 — Failure management

**Pillar**: Reliability  
**Best Practices**: 3

---

# MIDAREL04-BP01 Implement a multi-layered backup strategy

Manufacturing environments require comprehensive backup solutions that account for both
on-premises equipment data and cloud-based systems. A multi-layered approach helps protect
critical production data against various failure scenarios, from local hardware failures to
Regional disruptions.

**Desired outcome:** Manufacturing data is consistently backed
up, recoverable, and protected against various failure modes. Recovery Point Objectives (RPOs)
and Recovery Time Objectives (RTOs) are met to minimize production impact during recovery
operations.

**Benefits of establishing this best practice:** Implementing a
multi-layered backup strategy helps reduce manufacturing downtime, protect intellectual
property, improve compliance with industry regulations, and provide business continuity during
disruptions. It also improves recovery from data loss incidents and provides confidence in
data integrity.

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

**Design comprehensive backup policies**

Analyze your manufacturing data criticality levels and establish retention requirements
for different data types. Document regulatory compliance needs, audit requirements, and data
sovereignty rules.

Define Recovery Time Objectives (RTOs) and Recovery Point Objectives (RPOs) for
different manufacturing systems.

Map dependencies between production systems to understand the impact of data loss
scenarios.

For implementation, create tiered backup policies aligned with data criticality and
compliance requirements. Design automated backup schedules that don't impact production
operations and provide consistent backup states across interconnected systems.

Consider using AWS Backup to help protect manufacturing data across multiple services
with schedules aligned to production cycles and maintenance windows.

**Implement cross-Region redundancy**

Identify geographic distribution requirements for your manufacturing operations.
Document Regional compliance requirements and data residency restrictions. Establish
performance requirements for cross-region data access and recovery procedures.

For implementation, create backup copies in geographically separate regions to help
protect against regional disasters. Verify that your backup strategies take into account
data sovereignty requirements while providing necessary redundancy.

Consider implementing AWS Backup cross-Region copy capabilities to provide
manufacturing data resilience against Regional disruptions.

**Establish hybrid backup solutions**

Map your on-premises manufacturing systems and their backup requirements. Document
integration points between cloud and on-premises systems. Define data transfer windows that
align with production schedules and network capacity.

For implementation, create backup mechanisms that help protect both cloud and
on-premises manufacturing data. Design efficient data transfer methods that minimize impact
on production networks.

Consider deploying AWS Storage Gateway to create hybrid backup solutions that help
protect on-premises manufacturing equipment data while enabling seamless recovery.

**Configure version control and lifecycle management**

Establish version retention requirements for critical manufacturing data. Document
change control procedures and audit requirements. Define archival policies based on data
access patterns and compliance needs.

For implementation, create versioning policies that maintain appropriate historical
records while managing storage costs. Design lifecycle rules that automatically transition
aging backups to cost-effective storage tiers.

Consider implementing S3 Versioning with lifecycle policies to enable point-in-time
recovery of critical files like CAD designs and production recipes.

## Key AWS services

- AWS Backup
- Amazon S3
- AWS Storage Gateway
- Amazon EBS
- AWS Backup cross-region copy

## Resources

- [Creating a backup plan with AWS Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/creating-a-backup-plan.html)
- [AWS Storage Gateway for manufacturing data
protection](https://aws.amazon.com/storagegateway/features/)
- [Using cross-Region backup copies](https://docs.aws.amazon.com/aws-backup/latest/devguide/cross-region-backup.html)
- [Retaining multiple versions of objects with S3 Versioning](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midarel04-bp01.html*

---

# MIDAREL04-BP02 Use cloud replication for manufacturing data resilience

Implement automated, multi-Region cloud replication to maintain manufacturing operational
data integrity across production systems, quality control databases, and equipment monitoring
systems. Establish consistent backup patterns that align with recovery time objectives (RTOs)
critical to manufacturing operations.

**Desired outcome:** Manufacturing data is replicated according
to defined recovery point objectives, helping you avoid data loss in failure scenarios.
Critical systems can be restored rapidly, minimizing production downtime and maintaining
continuity of operations.

**Benefits of establishing this best practice:**

- Minimizes production downtime during recovery operations.
- Preserves historical manufacturing data needed for quality control and compliance.
- Enables rapid recovery of operational systems supporting the production line.
- Provides resilience against Regional failures that could impact manufacturing
operations.

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

**Design automated replication strategies**

Assess your manufacturing data types and their replication requirements. Document
recovery point objectives (RPOs) for different systems and establish data consistency
requirements across replicated environments. Map dependencies between manufacturing systems
to understand the impact of replication delays. Define acceptable latency thresholds for
data synchronization.

For implementation, create automated replication mechanisms that maintain data
consistency without impacting production performance. Design replication schedules that
align with manufacturing cycles and maintenance windows.

Consider using AWS Backup for automated and centralized replication management that
aligns with your production schedules and operational requirements.

**Implement multi-Region data distribution**

Analyze your geographic manufacturing footprint and Regional compliance requirements.
Document data sovereignty rules and cross-border data transfer restrictions. Define
performance requirements for data access across Regions. Establish recovery procedures for
Regional failures.

For implementation, create Region-specific replication policies that help you maintain
compliance while providing higher data availability. Design efficient data transfer
mechanisms that optimize costs and performance.

Consider implementing Amazon S3 Cross-Region Replication for critical production data,
making manufacturing specifications and quality records available across required geographic
locations.

**Configure database replication**

Map your manufacturing databases and their criticality levels. Document consistency
requirements for replicated databases and establish acceptable lag times. Define failover
procedures and recovery priorities.

For implementation, create database replication mechanisms that maintain data integrity
during normal operations and system failures. Design automated failover procedures that
minimize production disruption.

Consider using AWS Database Migration Service (DMS) continuous replication for
manufacturing databases containing production recipes and equipment configurations.

**Establish deployment automation**

Document your infrastructure requirements and configuration standards. Define change
management procedures and testing requirements for replicated environments. Establish
validation protocols for replicated resources.

For implementation, create automated deployment procedures that provide consistent
configuration across replicated environments. Design validation checks that verify
replication health and data consistency.

Consider implementing AWS CloudFormation templates to automate the deployment of
consistent backup infrastructure across manufacturing facilities.

## Key AWS services

- AWS Backup
- Amazon S3
- AWS Database Migration Service (DMS)
- AWS CloudFormation

## Resources

- [AWS Backup](https://aws.amazon.com/backup/)
- [S3 Cross-Region Replication for Business
Continuity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html)
- [Continuous
Database Replication with AWS DMS](https://aws.amazon.com/dms/)
- [Automating Backup Deployment with
CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backup-backupplan.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midarel04-bp02.html*

---

# MIDAREL04-BP03 Use versioning and automated backup procedures

Implement comprehensive data backup strategies with automated procedures and versioning
to help protect manufacturing data assets from corruption, accidental deletion, or system
failures, helping improve business continuity and speeding up recovery.

**Desired outcome:** Manufacturing data is consistently backed
up with comprehensive versioning that captures different types of changes and modifications
over time. This encompasses full versions of production recipes and process parameters,
iterative versions of equipment configurations and control logic, sequential versions of
quality control specifications, and temporal versions showing historical changes to
manufacturing master data. The versioning system maintains delta versions for incremental
changes to production workflows and baseline versions that establish known good states for
critical systems. The versions are properly tagged, cataloged, and retrievable to support
various recovery scenarios, from point-in-time restoration to full system rollbacks. This
comprehensive versioning strategy helps you consistently meet RTOs and RPOs, maintaining
operational continuity while providing a clear audit trail of changes for compliance and
troubleshooting purposes.

**Benefits of establishing this best practice:** Implementing
automated backups with versioning reduces the risk of data loss, helps you improve compliance
with industry regulations, minimizes downtime during recovery events, and provides audit
trails for manufacturing processes and quality control.

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

**Establish versioning policies**

Identify version control requirements for different types of manufacturing data -
production recipes, equipment configurations, quality specifications, and operational
parameters. Document retention requirements for each data type based on regulatory
compliance, quality audits, and operational needs. Define clear versioning rules including
baseline versions, major and minor changes, and delta tracking requirements. Map
dependencies between versioned items to maintain system-wide consistency.

For implementation, create versioning mechanisms that maintain complete historical
records while optimizing storage utilization. Design automated version management that
integrates with existing manufacturing workflows.

Consider implementing S3 versioning and lifecycle policies that support manufacturing
data versioning requirements while automatically managing version retention and archival.

**Configure automated backup procedures**

Analyze your backup requirements across different manufacturing systems. Document
backup windows that align with production schedules and maintenance periods. Establish
verification procedures to verify backup integrity and completeness. Define backup frequency
based on data change rates and business risk tolerance.

For implementation, create automated backup procedures that maintain data consistency
across interconnected manufacturing systems. Design backup validation checks that verify
both content and version integrity.

Consider using AWS Backup to create automated, scheduled backups of manufacturing
systems with appropriate retention policies and integrity checks.

**Implement data transfer optimization**

Map data transfer patterns and volumes across your manufacturing environment. Document
network capacity constraints and identify potential bottlenecks. Define acceptable transfer
windows that don't impact production operations.

For implementation, create efficient data movement mechanisms that minimize impact on
production systems. Design transfer optimization strategies including compression and
deduplication.

Consider using AWS DataSync to automate and optimize data transfer between on-premises
manufacturing systems and AWS storage services.

**Establish monitoring and validation**

Define success criteria for backup and versioning operations. Document monitoring
requirements including version completeness, backup status, and system health indicators.
Establish alert thresholds and escalation procedures.

For implementation, create comprehensive monitoring systems that track both technical
success and business relevance of versioning operations. Design automated validation checks
that verify version consistency and backup integrity.

Consider implementing AWS Backup test restore capabilities to regularly verify backup
integrity and recovery procedures.

## Key AWS services

- Amazon S3
- AWS Backup
- Amazon RDS
- AWS DataSync
- Amazon EBS

## Resources

- [Using versioning in S3 buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html)
- [Creating manufacturing backup plans with AWS Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/creating-a-backup-plan.html)
- [Backup and recovery approaches on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/backup-recovery/welcome.html)
- [Testing recovery capabilities with AWS Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/test-restore.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midarel04-bp03.html*

---

# MIDAREL05 — Failure management

**Pillar**: Reliability  
**Best Practices**: 2

---

# MIDAREL05-BP01 Design a multi-Region disaster recovery strategy

Manufacturing operations require high availability of systems that control production
lines, inventory management, and supply chain logistics. A multi-Region disaster recovery
strategy means that if one Region experiences an outage, manufacturing systems can continue
operating from another region with minimal disruption.

**Desired outcome:** A resilient manufacturing environment that
can quickly recover from regional failures, which improves continuous production capabilities,
maintains access to critical manufacturing data, and minimizes operational downtime.

**Benefits of establishing this best practice:**

- Reduced production downtime during Regional outages.
- Protection of critical manufacturing data and systems.
- Maintained supply chain continuity.
- Improved compliance posture with industry regulations and customer SLAs.
- Enhanced business resilience against natural disasters or large-scale infrastructure
failures.

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

- **Implement data replication across Regions:** Set up
continuous replication of manufacturing data, including ERP and MES systems and
production databases using Amazon RDS Multi-AZ with cross-Region read replicas or Amazon S3 Cross-Region Replication.
- **Create automated recovery procedures:** Develop AWS CloudFormation templates or use AWS Elastic Disaster Recovery to automate the recovery
of manufacturing applications and infrastructure components with predefined RTOs and
RPOs.
- **Establish production monitoring and failover
mechanisms:** Implement Route 53 health checks and failover routing policies
to automatically redirect traffic to backup manufacturing systems in case of primary
system failure.
- **Test DR procedures regularly:** Schedule periodic
disaster recovery tests using AWS Fault Injection Service to validate that manufacturing
operations can be recovered within defined time frames and that all production-critical
systems function properly after recovery.

## Key AWS services

- AWS Elastic Disaster Recovery
- Amazon S3 Cross-Region Replication
- Amazon RDS Multi-AZ and Cross-Region Read Replicas
- AWS CloudFormation
- Amazon Route 53
- AWS Fault Injection Service

## Resources

- [Getting Started with AWS Elastic Disaster
Recovery](https://docs.aws.amazon.com/drs/latest/userguide/getting-started.html)
- [Cross-Region Replication for Manufacturing
Workloads](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html)
- [Disaster Recovery Options in the
Cloud](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html)
- [AWS Manufacturing and Industrial Reference
Architectures](https://d1.awsstatic.com/architecture-diagrams/ArchitectureDiagrams/manufacturing-on-aws-ra.pdf)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midarel05-bp01.html*

---

# MIDAREL05-BP02 Implement and regularly test DR procedures

Regularly test and review your disaster recovery procedures to verify they work as
expected when needed. Manufacturing environments have unique requirements including machine
connectivity, production data integrity, and maintaining operational technology systems, which
makes systematic testing critical to validate recovery capabilities.

**Desired outcome:** Successfully validated and regularly
updated disaster recovery procedures that can be executed with confidence during actual
incidents, minimizing downtime and resuming manufacturing operations within defined RTOs and
RPOs.

**Benefits of establishing this best practice:**

- Regular testing builds confidence in recovery procedures
- Identifies gaps before real incidents occur
- Reduces recovery time during actual disasters
- Helps meet compliance requirements for business continuity in manufacturing
environments
- Maintains currency of procedures as manufacturing systems evolve
- Aligns with changing production requirements
- Validates recovery capabilities across seasonal manufacturing patterns

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

**Establish regular review cycles:** First document all
components of your manufacturing disaster recovery plan including systems, data, and
processes. Map changes in production environments that could impact recovery procedures.
Define review participants from operations, IT, and business teams. Identify regulatory
requirements that necessitate periodic review and testing. For implementation, create a
structured review process that evaluates recovery plans against current manufacturing
operations. Design evaluation criteria that validate recovery procedures remain aligned with
business needs. Consider implementing AWS Backup for manufacturing data and systems with
review cycles that align with your quarterly assessment schedule.

**Conduct systematic testing:** Begin by defining test
scenarios that reflect realistic disaster situations in your manufacturing environment.
Document test scope and success criteria for different recovery scenarios. Establish test
schedules that align with production maintenance windows. Map dependencies between systems
to test them comprehensively. For implementation, create testing protocols that validate all
aspects of recovery procedures. Design testing environments that accurately reflect
production configurations. Consider deploying AWS Elastic Disaster Recovery to test
replication of critical manufacturing systems with minimal RPO and enable rapid recovery
validation.

**Configure automated health checks:** Start by identifying
critical components requiring continuous monitoring. Document acceptable performance
thresholds and recovery triggers. Define escalation procedures for different types of
failures. Establish monitoring metrics that indicate recovery readiness. For implementation,
create automated monitoring systems that continuously validate recovery capability. Design
health checks that verify system and data availability. Consider using Route 53 health
checks and Application Recovery Controller to automate failover testing of manufacturing
applications.

**Create automated recovery scripts**: Document all critical manufacturing systems and their recovery requirements. Map
dependencies between systems to establish proper recovery sequence. Define acceptance
criteria for successful recovery and establish test scenarios that reflect realistic failure
modes. Identify required permissions and access controls for recovery operations.

For implementation, create automated recovery procedures that can consistently restore
manufacturing systems. Design recovery orchestration that maintains data integrity and
system dependencies.

Consider developing AWS CloudFormation templates or AWS CDK scripts that can
automatically recreate your manufacturing infrastructure, including device connections and
monitoring systems.

**Schedule regular recovery testing**: Identify testing windows that minimize impact on production operations. Document test
scope and success criteria for different scenarios. Establish clear roles and
responsibilities during recovery tests. Define test frequency based on system criticality
and compliance requirements.

For implementation, create a systematic testing program that validates recovery
procedures across different failure scenarios. Design testing protocols that simulate
various disruption types while maintaining safety and operational controls.

Consider using AWS Fault Injection Service to simulate failures in your manufacturing
workloads and practice recovery procedures at least quarterly.

**Implement cross-Region backup testing**: Map your geographic redundancy requirements and identify critical systems requiring
cross-Region recovery. Document regional compliance requirements and data sovereignty
constraints. Define acceptable recovery time frames for cross-Region restoration.

For implementation, create backup verification procedures that provide data
availability across regions. Design testing mechanisms that validate cross-Region recovery
capabilities.

Consider configuring AWS Backup to regularly test restore operations of critical
manufacturing data across multiple AWS Regions.

**Establish recovery monitoring**: Define key metrics for measuring recovery effectiveness. Document monitoring
requirements during recovery operations. Establish thresholds for recovery success and
failure conditions.

For implementation, create monitoring systems that track recovery progress and success
rates. Design dashboards that provide clear visibility into recovery operations.

Consider using Amazon CloudWatch to track recovery time and success rates during
recovery tests, creating dashboards that highlight areas needing improvement.

**Implement improvement processes:** Begin by establishing
methods to capture lessons learned from each test cycle. Document required updates to
recovery procedures based on test results. Define change management processes for updating
recovery plans. Create training requirements for updated procedures. For implementation,
create systematic processes to incorporate test findings into recovery plans. Design
validation procedures for updated recovery methods. Consider conducting quarterly tabletop
exercises using AWS Fault Injection Service to validate recovery procedures and team
readiness

## Key AWS services

- AWS Backup
- AWS CloudFormation
- Amazon CloudWatch
- AWS Fault Injection Service
- AWS Systems Manager
- AWS Elastic Diater Recovery

## Resources

- [Disaster Recovery of Workloads on AWS](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-workloads-on-aws.html)
- [Managing AWS Fault Injection Service experiments](https://docs.aws.amazon.com/resilience-hub/latest/userguide/testing.html)
- [AWS Backup Documentation](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midarel05-bp02.html*

---

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
