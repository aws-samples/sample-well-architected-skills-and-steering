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
