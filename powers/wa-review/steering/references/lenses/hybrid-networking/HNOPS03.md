# HNOPS03 — Operate

**Pillar**: Operational Excellence  
**Best Practices**: 2

---

# HNOPS03-BP01 Monitor hybrid networking components

Monitoring solutions serve as an essential tool to provide
visibility across your hybrid network infrastructure. It enables
collection, visualization, and analysis of metrics from network
connectivity components like virtual private networks, dedicated
connections, and network transit hubs, allowing teams to set alarms
for performance thresholds and detect anomalies before they impact
connectivity.

**Desired outcome:**

- Quickly identified and address performance issues, security
anomalies, and connectivity problems
- Improved network reliability, optimized resource utilization,
and enhanced operational efficiency.

**Level of risk exposed if this best practice
is not established:** High

**Benefits of establishing this best
practice:**

- Get real-time visibility into network performance, enabling
quick detection and resolution of issues.
- Customizable alerts and automated responses to predefined
conditions.
- Support capacity planning and resource optimization by providing
historical data and trends.

## Implementation guidance:

- Identify critical hybrid networking components that require
monitoring. Determine key metrics and thresholds relevant to
each component.
- Configure dashboards, alarms, and automated actions using
services such as Amazon CloudWatch
- Integrate automated notification and remediation to alarms
using services such as Amazon SNS and AWS Lambda

## Resources

- [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html)
- [Metrics
and events in Amazon VPC Transit Gateways](https://docs.aws.amazon.com/vpc/latest/tgw/transit-gateway-monitoring.html)
- [AWS Direct Connect Monitoring](https://docs.aws.amazon.com/directconnect/latest/UserGuide/monitoring-cloudwatch.html)
- [Monitor
hybrid connectivity with Amazon CloudWatch Network Synthetic
Monitor](https://aws.amazon.com/blogs/networking-and-content-delivery/monitor-hybrid-connectivity-with-amazon-cloudwatch-network-monitor/)
- [AWS Cloud WAN events and metrics](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-events-metrics.html)
- [Amazon SNS](https://docs.aws.amazon.com/sns/latest/dg/welcome.html)
- [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnops03-bp01.html*

---

# HNOPS03-BP02 Consider flow logs for enhanced network visibility when needed

Flow logs capture detailed information about network traffic
traversing your cloud infrastructure network components. While not
essential for all deployments, implementing flow logs is recommended
for environments requiring in-depth network analysis and security
auditing. The logs provide valuable insights into network behavior,
enabling teams to troubleshoot connectivity issues, monitor traffic
patterns, detect security anomalies, ensure compliance with network
policies, and optimize network performance. By leveraging this
feature, organizations can enhance their network visibility, improve
security posture, and gain actionable insights for network
optimization.

**Desired outcome:**

- Comprehensive visibility into network traffic patterns, source
and destination IP addresses, ports, protocols, and packet
counts.
- Greater insights during network troubleshooting, and security
analysis

**Level of risk exposed if this best practice
is not established:** Medium

**Benefits of establishing this best
practice:**

- Reduce mean time to resolution (MTTR) for network issues through
rapid troubleshooting and root cause analysis.
- Detailed traffic visibility enables teams to analyze traffic
patterns to enhance capacity planning, optimize network
spending, and prevent over-provisioning of resources.
- Comprehensive audit trails of network activity help
organizations to meet compliance requirements and security
standards.

## Implementation guidance

- Evaluate the volume of network traffic and associated logging
costs of flow logs.
- Identify the network resources that require monitoring and
determine the appropriate destination for your logs based on
your analysis needs and retention requirements.

For example, VPC and Transit Gateway flow logs can be sent to
Amazon CloudWatch Logs, S3, or Amazon Data Firehose.
- Consider implementing log filters to focus on specific types
of traffic or to alert suspicious activities.

## Resources

- [Logging
IP traffic using VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html)
- [AWS Transit Gateway Flow Logs](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-flow-logs.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnops03-bp02.html*

---
