# Operational Excellence

**Pillar**: Operational Excellence  
**Questions**: 5

---

# HNOPS01 — Organization

**Pillar**: Operational Excellence  
**Best Practices**: 1

---

# HNOPS01-BP01 Have a team responsible for operating the hybrid networking environment

**Desired outcome:** Create a
specialized group that handles the complexities of hybrid network
architectures. This team effectively designs, implements, and
manages network infrastructure that spans both on-premises and cloud
environments, while maintaining consistent operations and
standardized practices.

**Benefits of establishing this best
practice**:

- Enhances network reliability and performance through team
expertise
- Focused approach leads to:

Faster incident response times
- Reduced downtime
- Efficient resource utilization

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

- The core networking team should include specialists for both
cloud and on-premises networking, with well-defined escalation
paths and on-call rotations.
- Skills and training are crucial components, requiring
investment in networking related certifications and
maintaining expertise in on-premises networking technologies.
- The team should develop strong capabilities in automation and
infrastructure as code, while staying current with the latest
hybrid networking best practices.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnops01-bp01.html*

---

# HNOPS02 — Prepare

**Pillar**: Operational Excellence  
**Best Practices**: 1

---

# HNOPS02-BP01 Use IP address management tool

Use IP Address Manager tool to automate workflows to efficiently
manage IP addresses. It helps to organize and monitor the IP address
space and automatically allocate CIDRs using specific business
rules.

**Desired outcome:**

- Organized and efficiently managed IP addressing scheme across
hybrid environments
- Get clear visibility, prevents overlapping addresses, and
supports scalable network growth.

**Level of risk exposed if this best practice
is not established:** High

**Benefits of establishing this best
practice:**

- Efficient route summarization, allowing organizations to
advertise larger CIDR blocks instead of individual prefixes.
- Clean network boundaries and facilitate easier security
management.
- Achieve better resource utilization through automated IP address
assignment, eliminating manual tracking processes and reducing
human errors.

## Implementation guidance

- Create a hierarchical structure of IP pools that align with
your organizational needs and geographical presence. For
example, you can use services such as
[Amazon VPC IPAM](https://docs.aws.amazon.com/vpc/latest/ipam/what-it-is-ipam.html).
- Establish clear policies for CIDR allocation, including
reserved ranges for specific purposes such as Amazon VPCs,
subnets, and on-premises networks.
- Implement workflows for IP address assignment, such as using
Amazon VPC IPAM allocation rules.

## Resources

- [Amazon VPC IP Address Manager Best Practices](https://aws.amazon.com/blogs/networking-and-content-delivery/amazon-vpc-ip-address-manager-best-practices/)
- [Managing
IP pools across VPCs and Regions using Amazon VPC IP Address
Manager](https://aws.amazon.com/blogs/networking-and-content-delivery/managing-ip-pools-across-vpcs-and-regions-using-amazon-vpc-ip-address-manager/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnops02-bp01.html*

---

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

# HNOPS04 — Operate

**Pillar**: Operational Excellence  
**Best Practices**: 2

---

# HNOPS04-BP01 Monitor network service provider maintenance events

Implementing a proactive monitoring and response system for
scheduled network maintenance activities is crucial for minimizing
service disruptions. By establishing a methodical framework to track
maintenance notifications and planned network events, teams can
prepare effectively, strategically schedule necessary changes during
designated maintenance windows, and ensure continuous network
connectivity throughout the process. This systematic approach
enhances operational resilience while reducing the impact of
essential maintenance on critical services

**Desired outcome:**

- Get timely notifications about links connecting the on-premises
data center to the cloud.
- Enables proper planning for scheduled activities, minimizes
service disruptions, and ensures optimal management of hybrid
network connectivity.

**Level of risk exposed if this best practice
is not established:** High

**Benefits of establishing this best
practice:**

- Proactive maintenance planning and reduces the risk of
unexpected service disruptions.
- Better coordination during maintenance windows with business
operations, minimizing impact on critical workloads.
- Enhanced visibility into service health and upcoming changes

## Implementation guidance

- Integrate service provider notifications into monitoring and
observability platforms. For example, you can achieve this
using Amazon EventBridge to send AWS Direct Connect
maintenance messages.

## Resources

- [AWS Direct Connect maintenance](https://docs.aws.amazon.com/directconnect/latest/UserGuide/dx-maintenance.html)
- [Monitoring
events in AWS Health with Amazon EventBridge](https://docs.aws.amazon.com/health/latest/ug/cloudwatch-events-health.html)
- [How
can I get notifications for AWS Direct Connect scheduled
maintenance or events](https://aws.amazon.com/premiumsupport/knowledge-center/get-direct-connect-notifications/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnops04-bp01.html*

---

# HNOPS04-BP02 Develop automated runbooks and maintain clear documentations

Developing automated runbooks and maintaining clear, comprehensive
documentation ensures that your team can respond effectively to
network events, perform routine maintenance, and troubleshoot issues
across your cloud and on-premises infrastructure.

**Desired outcome:**

- Create a robust, efficient, and consistent operational framework
for managing hybrid network environments.
- Consider comprehensive set of procedures that can be easily
followed and automated where possible, ensuring quick and
accurate responses to network events, routine maintenance tasks,
and troubleshooting scenarios.

**Level of risk exposed if this best practice
is not established:** High

**Benefits of establishing this best
practice:**

- Ensures consistency in operations across diverse environments,
reducing the likelihood of errors and improving overall service
quality.
- Enable faster onboarding of new team members and reduce
dependency on specific individuals.

## Implementation guidance

- Identify critical network operational processes and common
incident scenarios in your hybrid network environment.
- Develop clear, step-by-step procedures for each identified
process, ensuring they cover both AWS and on-premises
components.
- Ensure that documentation is easily accessible, regularly
updated, and includes both technical details and business
context.

## Resources

- [OPS07-BP03
Use runbooks to perform procedures](https://docs.aws.amazon.com/wellarchitected/latest/framework/ops_ready_to_support_use_runbooks.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnops04-bp02.html*

---

# HNOPS05 — Evolve

**Pillar**: Operational Excellence  
**Best Practices**: 1

---

# HNOPS05-BP01 Measure and track the KPIs

Measuring and tracking KPI in hybrid networking environments
involves identifying, monitoring, and analyzing critical metrics
that reflect the health, performance, and efficiency of your network
infrastructure across both on-premises and cloud environments.

**Desired Outcome:**

- Comprehensive and real-time view of hybrid network performance
through well-defined KPIs
- Track metrics such as network latency, throughput, availability,
error rates, and cost efficiency across both cloud and
on-premises infrastructure

**Level of risk exposed if this best practice
is not established:** Medium

**Benefits of establishing this best
practice:**

- Gain improved visibility into hybrid network's health and
performance, enabling faster identification and resolution of
issues.
- Better capacity planning and resource optimization, leading to
more efficient use of network resources and potential cost
savings.
- Alignment of network performance metrics with business
objectives helps in demonstrating the value of networking
investments to stakeholders.

## Implementation guidance

- Identify critical KPIs that are specifically relevant to their
hybrid networking environment
- Ensure metrics align with business objectives and operational
requirements.
- Effective monitoring solution to collect and aggregate data
from both cloud and on-premises systems
- Real-time visualization dashboards to provide stakeholders
with immediate insights into network performance and health.

## Resources

- [Monitor
with Amazon CloudWatch](https://docs.aws.amazon.com/directconnect/latest/UserGuide/monitoring-cloudwatch.html)
- [Monitor
AWS Site-to-Site VPN tunnels using Amazon CloudWatch](https://docs.aws.amazon.com/vpn/latest/s2svpn/monitoring-cloudwatch-vpn.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnops05-bp01.html*

---

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
