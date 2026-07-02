# LSPERF15 — Network and content delivery

**Pillar**: Performance Efficiency  
**Best Practices**: 2

---

# LSPERF15-BP01 Implement application-aware network path optimization and traffic prioritization methods

Analyze network paths to find optimal routes for clinical data and
implement dynamic routing for time-sensitive medical information.
Use deep packet inspection to identify and prioritize clinical
traffic, which verifies that critical systems like patient monitors
get priority bandwidth through quality of service (QoS) controls.
Set up network segmentation using VLANs to separate clinical from
administrative traffic, maintaining guaranteed bandwidth and latency
limits for clinical applications.

**Desired outcome:** You have an
intelligent network infrastructure that automatically optimizes
paths for clinical data while prioritizing the handling of critical
medical traffic through effective segmentation and QoS controls.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Establish comprehensive monitoring of network paths for clinical
data flows. Implement automated systems to identify optimal routes
and provides priority handling to time-sensitive medical
information through intelligent path selection.

Deploy deep packet inspection mechanisms to identify clinical
traffic patterns. Create QoS policies that guarantee bandwidth for
critical medical systems and patient monitoring applications while
maintaining required performance levels.

Design and implement VLAN architecture that separates clinical and
administrative traffic. Establish clear bandwidth allocation
policies that provide guaranteed resources to clinical
applications without interference from other network traffic.

### Implementation steps

- Optimize network paths by deploying AWS Transit Gateway for
centralized routing, AWS Global Accelerator for performance
enhancement, and Amazon Route 53 for intelligent
health-aware DNS routing.
- Implement comprehensive traffic management using AWS Network Firewall for classification, AWS Transit Gateway for QoS
enforcement, and VPC endpoints to prioritize access to
critical services.
- Establish strong network segmentation with separate VPCs for
clinical and administrative traffic, AWS PrivateLink for
secure service connectivity, and VPC Flow Logs for detailed
traffic monitoring.
- Deploy end-to-end performance monitoring with Amazon CloudWatch dashboards for network metrics visualization,
configured alarms for threshold violations, and AWS X-Ray
for distributed application tracing.
- Document network architecture with traffic flow patterns,
segmentation boundaries, and performance baselines for
different application categories.
- Conduct regular network assessments to identify optimization
opportunities and validate segmentation controls.
- Implement automated remediation for common network
performance issues and security policy violations.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsperf15-bp01.html*

---

# LSPERF15-BP02 Deploy synthetic transaction monitoring and real user monitoring with automated performance optimization

Implement synthetic monitoring methods that continuously simulate
critical clinical workflows such as record retrieval, patient
monitoring data transmission, and medication order processing to
measure end-to-end latency and automatically trigger optimization
actions when thresholds are exceeded. Use real user monitoring (RUM)
techniques to capture actual network performance experienced by
clinicians and implement adaptive optimization that adjusts network
configurations based on real-time performance data, such as
switching to alternate network paths or increasing bandwidth
allocation for degraded connections.

**Desired outcome:** You have an
integrated monitoring system combining synthetic testing and real
user monitoring that automatically detects and responds to
performance issues in clinical workflows. This enables proactive
optimization of network performance and provides reliable operation
of critical healthcare applications.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Establish comprehensive synthetic monitoring for critical clinical
workflows, including automated tests for record retrieval and
patient data transmission. Configure monitoring scenarios that
simulate real clinical activities with defined performance
thresholds. Implement automated response mechanisms that trigger
optimization actions when performance degrades below acceptable
levels.

Deploy RUM solutions to capture actual performance metrics
experienced by clinical users across different locations and
devices. Set up data collection for key performance indicators
including page load times, API response times, and network
latency. Create performance baselines that reflect real-world
usage patterns in clinical environments.

Design automated optimization systems that respond to both
synthetic and RUM data. Implement intelligent routing algorithms
that can automatically adjust network paths based on performance
metrics. Establish bandwidth allocation rules that dynamically
adapt to changing network conditions and clinical priorities.

Create comprehensive alerting mechanisms that identify performance
issues before they impact clinical operations. Implement automated
remediation procedures for common performance issues. Establish
escalation paths for situations requiring manual intervention.

### Implementation steps

- Establish comprehensive synthetic monitoring by deploying
Amazon CloudWatch Synthetics with canaries simulating
clinical workflows, AWS X-Ray traces for performance
tracking, and custom metrics to measure healthcare-specific
application performance.
- Implement real user monitoring (RUM) with CloudWatch RUM for
real-time clinical application data collection, performance
monitoring agents on user devices, and client-side
monitoring to track user experience metrics.
- Deploy performance optimization tools including AWS Global Accelerator for automatic path optimization, Application
Auto Scaling to adjust resources based on demand, and AWS Transit Gateway for intelligent network traffic routing.
- Create integrated monitoring and alerting with CloudWatch
dashboards visualizing synthetic and RUM metrics, Amazon EventBridge rules automating responses to performance
issues, and Amazon SNS notifications providing rapid
response to critical alerts.
- Document performance baselines specific to clinical
workflows and establish escalation procedures for different
severity levels of performance degradation.
- Implement regular performance reviews to identify
optimization opportunities and validate monitoring coverage
across critical healthcare applications.
- Configure automated remediation for common performance
issues to minimize impact on clinical operations.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsperf15-bp02.html*

---
