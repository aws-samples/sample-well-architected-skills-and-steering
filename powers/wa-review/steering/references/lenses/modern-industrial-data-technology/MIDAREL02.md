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
