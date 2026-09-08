# Cost Optimization

**Pillar**: Cost Optimization  
**Questions**: 8

---

# HNCOST01 — Practice Cloud Financial Management

**Pillar**: Cost Optimization  
**Best Practices**: 1

---

# HNCOST01-BP01 Implement a comprehensive tagging strategy for hybrid networking resources

Apply consistent tags to all hybrid networking components to enable
cost allocation and usage analysis. Teams gain visibility into
resource usage patterns, improve cost attribution, and enhance
operational governance.

**Desired outcome:** Accurate
attribution of hybrid networking expenses to specific workloads,
teams, or business units.

**Level of risk exposed if this best practice
is not established:** Medium

**Benefits of establishing this best
practice:**

- Transparent cost accountability for cross-functional teams
- Identification of underutilized resources for optimization
- Improved forecasting through historical cost trends
- Simplified chargeback and showback processes

## Implementation guidance

- Define standardized tags (for example, Environment, Workload,
and CostCenter) for hybrid networking resources.
- Enforce tagging compliance. For example, you can achieve this
using AWS Service Control Policies (SCPs) or AWS Config rules.
- Organize resources by tags. For example, you can achieve this
using AWS Resource Groups.

## Resources

- [Best
Practices for Tagging AWS Resources](https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/)
- [AWS Data Exports](https://docs.aws.amazon.com/cur/latest/userguide/cost-alloc-tags.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hncost01-bp01.html*

---

# HNCOST02 — Expenditure and usage awareness

**Pillar**: Cost Optimization  
**Best Practices**: 3

---

# HNCOST02-BP01 Track and analyze hybrid networking expenses

By implementing comprehensive cost monitoring tools and establishing
standardized expense categorization, businesses can gain visibility
into spending across different networking components. This holistic
approach enables finance and technical teams to identify
optimization opportunities, allocate costs accurately to business
units, forecast future expenditures based on growth patterns, and
ultimately make informed decisions that balance performance
requirements with financial considerations while avoiding unexpected
budget overruns.

**Desired outcome:** A clear
understanding of network-related expenses, with the ability to
attribute costs accurately and identify opportunities for savings.

**Level of risk exposed if this best practice
is not established:** Medium

**Benefits of establishing this best
practice:**

- Enhanced visibility into hybrid networking costs
- Early detection of unexpected cost increases
- Improved cost allocation and accountability
- Data-driven insights for ongoing optimization

## Implementation guidance

- Regularly review cost dashboards for networking services. For
example, you can achieve this using Cost Explorer, AWS Quick
Suite dashboards of Cost and Usage data.
- Implement cost allocation tags for all hybrid networking
resources

## Resources

- [AWS Cost Management](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html)
- [AWS Cost and Usage Report Documentation](https://docs.aws.amazon.com/cur/latest/userguide/what-is-cur.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hncost02-bp01.html*

---

# HNCOST02-BP02 Set up alerts to proactively notify hybrid networking cost thresholds

Implement a comprehensive cost monitoring system for your hybrid
networking infrastructure that automatically alerts stakeholders
when spending approaches or exceeds predefined thresholds. Integrate
these alerts with notification systems that provide timely updates
to both technical teams and business stakeholders, enabling rapid
response to cost spikes before they significantly impact your
budget. This proactive approach allows organizations to recognize
network flow costs, optimize data transfer paths, and make informed
decisions about hybrid connectivity options

**Desired outcome:** Proactive
management of hybrid networking costs

**Level of risk exposed if this best practice
is not established:** Medium

**Benefits of establishing this best
practice:**

- Prevents unexpected cost overruns
- Enables timely response to cost anomalies
- Promotes a culture of cost awareness and accountability

## Implementation guidance

- Create separate budgets for networking components
- Configure alerting mechanisms
- Establish monitoring processes
- Enable budget forecasting

## Resources

- [Managing
your costs with AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html)
- [AWS Budget Actions](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/budgets-controls.html)
- [Organizing
and tracking costs using AWS cost allocation tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hncost02-bp02.html*

---

# HNCOST02-BP03 Analyze network traffic patterns for optimization opportunities

Analyzing network traffic patterns in hybrid environments is crucial
for optimizing performance across cloud components. By examining
data flow, organizations can identify latency issues caused by
network distance, data volume, and traffic spikes that impact
application responsiveness. Traffic pattern monitoring enables
businesses to make informed decisions about workload placement and
data prioritization, ultimately creating a more efficient hybrid
infrastructure that balances performance needs with cost
considerations.

**Desired outcome:** Optimized
network traffic flows and reduced data transfer costs through
actionable insights.

**Level of risk exposed if this best practice
is not established:** Medium

**Benefits of establishing this best
practice:**

- Improved network efficiency
- Reduced data transfer costs
- Enhanced troubleshooting and capacity planning

## Implementation guidance

- Enable flow logs to collect network flow data. For example,
you can achieve this using VPC Flow Logs and Transit Gateway
Flow Logs
- Regularly review and analyze flow logs to identify
optimization opportunities. For example, you can achieve this
using Amazon Managed Grafana or Amazon OpenSearch Service

## Resources

- [VPC
Flow Logs Documentation](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html)
- [AWS Transit Gateway Flow Logs](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-flow-logs.html)
- [Stream
VPC flow logs to Amazon OpenSearch Service via Amazon Data Firehose](https://aws.amazon.com/blogs/big-data/stream-vpc-flow-logs-to-amazon-opensearch-service-via-amazon-kinesis-data-firehose/)
- [Monitor
AWS Transit Gateway Flow Logs centrally using Amazon Managed Grafana](https://aws.amazon.com/blogs/mt/monitor-aws-transit-gateway-flow-logs-centrally-using-amazon-managed-grafana/)
- [Visualize
and gain insights into your VPC Flow logs with Amazon Managed Grafana](https://aws.amazon.com/blogs/mt/visualize-and-gain-insights-into-your-vpc-flow-logs-with-amazon-managed-grafana/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hncost02-bp03.html*

---

# HNCOST03 — Cost-effective resources

**Pillar**: Cost Optimization  
**Best Practices**: 1

---

# HNCOST03-BP01 Implement tiered connectivity based on workload requirements

Hybrid networking connectivity must balance performance,
reliability, and cost. Workloads with varying requirements for
throughput, latency, and uptime should leverage different
connectivity solutions. For example, non-critical workloads (for
example, development or testing) can use cost-effective
internet-based VPNs, while mission-critical production workloads may
require dedicated connections like AWS Direct Connect. A tiered
approach ensures you only pay for the level of connectivity your
workloads actually need.

**Desired outcome:** Cost savings
through workload-aligned connectivity, with no overpayment for
unnecessary bandwidth or redundancy.

**Level of risk exposed if this best practice
is not established:** Medium

**Benefits of establishing this best
practice:**

- Reduces costs for non-critical workloads
- Ensures high performance for production workloads
- Simplifies scaling as requirements evolve

## Implementation guidance

- Use IPSec VPN connections for non-mission critical workloads
- Use dedicated connections for production workloads
- Scale from IPSec VPN connections in testing phase to dedicated
connections after bandwidth requirements are defined
- Use direct connectivity to single cloud network connectivity
to avoid additional cloud transit costs, For example, you can
use Direct Connect private VIF to connect directly to VPC.
- Use cloud transit connectivity to connect to multiple cloud
networks. For example, you can use Direct Connect transit VIF
to connect to Transit Gateway for VPCs in the same region, or
Cloud WAN core network for VPCs in multiple regions

## Resources

- [Site-to-Site VPN
pricing](https://aws.amazon.com/vpn/pricing/)
- [AWS Direct Connect Pricing](https://aws.amazon.com/directconnect/pricing/)
- [AWS Transit Gateway Pricing](https://aws.amazon.com/transit-gateway/pricing/)
- [AWS Cloud WAN Pricing](https://aws.amazon.com/cloud-wan/pricing/)
- [Hybrid
Connectivity](https://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/hybrid-connectivity.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hncost03-bp01.html*

---

# HNCOST04 — Cost-effective resources

**Pillar**: Cost Optimization  
**Best Practices**: 3

---

# HNCOST04-BP01 Implement data transfer optimization techniques

Optimizing data transfer between AWS and on-premises environments
through compression and efficient transfer protocols is crucial for
reducing hybrid networking costs. Implementing appropriate
optimization techniques can significantly reduce bandwidth
consumption while maintaining required performance levels across
hybrid connections.

**Desired outcome:** Reduced data
transfer costs across hybrid network connections while maintaining
application performance and reliability through optimized traffic
patterns and compression techniques.

**Level of risk exposed if this best practice
is not established:** Low

**Benefits of establishing this best
practice:**

- Lower bandwidth utilization across dedicated connections or
IPSec VPN connections
- Reduced data transfer costs for hybrid network traffic
- Improved application performance across hybrid environments
- More efficient use of hybrid network capacity
- Better cost predictability for network usage
- Optimized throughput for critical applications

## Implementation guidance

- Optimize application-level transfer:

Enable compression for application protocols (HTTP/HTTPS)
- Configure TCP optimization for hybrid connections
- Implement efficient data replication strategies
- Use bulk transfer windows for large datasets

- Configure network optimization:

Enable protocol compression on IPSec VPN connections
- Implement QoS policies for traffic prioritization
- Configure WAN optimization for dedicated connections
- Optimize routing policies for efficient paths

- Monitor and analyze:

Track bandwidth utilization across hybrid links
- Monitor compression effectiveness
- Analyze traffic patterns and peak usage
- Review cost impact of optimization measures

- Regular review and adjustment:

Assess optimization effectiveness
- Update compression policies as needed
- Fine-tune network configurations
- Validate cost savings

## Resources

- [Overview
of Data Transfer Costs for Common Architectures](https://aws.amazon.com/blogs/architecture/overview-of-data-transfer-costs-for-common-architectures/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hncost04-bp01.html*

---

# HNCOST04-BP02 Select cost-effective regions and availability zones

Selecting the appropriate AWS Region and Availability Zone (AZ) is
crucial for optimizing hybrid networking and reducing data transfer
costs. AWS pricing for services such as compute, storage, and data
transfer can vary significantly across regions due to differences in
operational costs, local demand, and infrastructure. However, it is
important to balance cost savings with performance, compliance, and
data residency requirements. Some regions may have lower prices but
might also have limited services availability or higher latency for
end users. Regularly reviewing AWS pricing updates and reassessing
region and AZ choices ensures ongoing cost efficiency as your needs
evolve.

**Desired outcome:** Minimize
infrastructure and data transfer costs by strategically placing
resources in regions and AZs that offer the best balance of price,
performance, and compliance.

**Level of risk exposed if this best practice
is not established:** Medium

**Benefits of establishing this best
practice:**

- Significant reduction in compute, storage, and data transfer
costs
- Improved cost predictability for DR and test environments
- Enhanced ability to scale and optimize hybrid workloads
- Opportunity to leverage AWS pricing differences for competitive
advantage

## Implementation guidance

- Compare regional pricing for compute, storage, and data
transfer before deploying workloads
- Use lower-cost regions for DR, backups, and test platforms
where performance and compliance permit
- Minimize inter-region and inter-AZ data transfers to avoid
additional charges
- Consider service availability and latency when selecting
regions and AZs
- Monitor AWS pricing changes and adjust resource placement
strategies accordingly

## Resources

- [AWS Services by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/)
- [Amazon EC2 On-Demand Pricing](https://aws.amazon.com/ec2/pricing/on-demand/)
- [Cost
Optimization with AWS](https://aws.amazon.com/aws-cost-management/aws-cost-optimization/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hncost04-bp02.html*

---

# HNCOST04-BP03 Implement compression and caching for repetitive data transfers

Reduce data transfer volumes by compressing in-transit data and
caching frequently accessed content at the edge.

**Desired outcome:** Reduction in
data transfer volumes and associated costs.

**Level of risk exposed if this best practice
is not established:** Low

**Benefits of establishing this best
practice:**

- Lower bandwidth consumption
- Faster transfer times
- Reduced storage costs for compressed data

## Implementation guidance

- Enable compression for payloads
- Configure TTL for static assets in content delivery network
such as Amazon CloudFront
- Use compression for file/volume syncs using services such as
AWS Storage Gateway

## Resources

- [Manage
how long content stays in the cache](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Expiration.html)
- [Payload
compression for REST APIs in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-gzip-compression-decompression.html)
- [AWS Storage Gateway FAQ](https://aws.amazon.com/storagegateway/faqs/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hncost04-bp03.html*

---

# HNCOST05 — Manage demand and supply resources

**Pillar**: Cost Optimization  
**Best Practices**: 1

---

# HNCOST05-BP01 Forecast demand and baseline requirements before scaling dedicated connections

Begin with IPSec VPN or small-scale dedicated connection links
during testing or migration phases. Monitor traffic patterns to
establish baseline bandwidth needs. Scale to larger dedicated
connections or LAGs only after validating requirements.

**Desired outcome:** Cost-efficient
scaling that matches actual workload demands, avoiding premature
investment in underutilized dedicated connections.

**Level of risk exposed if this best practice
is not established:** Medium

**Benefits of establishing this best
practice:**

- Reduces upfront capital expenditure
- Prevents over-provisioning of high-cost dedicated links
- Enables data-driven scaling decisions

## Implementation guidance

- Analyze historical data transfer costs using services such as
Cost Explorer or Cost and Usage
- Analyze traffic patterns using services such as VPC Flow Logs
or Transit Gateway Flog Logs

## Resources

- [Logging
IP traffic using VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html)
- [Transit
Gateway Flow Logs](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-flow-logs.html)
- [Using
AWS Cost Explorer to analyze data transfer costs](https://aws.amazon.com/blogs/mt/using-aws-cost-explorer-to-analyze-data-transfer-costs/)
- [AWS Well-Architected Cost & Usage Report Library](https://catalog.workshops.aws/cur-query-library/en-US/queries/networking-and-content-delivery)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hncost05-bp01.html*

---

# HNCOST06 — Manage demand and supply resources

**Pillar**: Cost Optimization  
**Best Practices**: 2

---

# HNCOST06-BP01 Implement QoS policies for traffic prioritization

Configure QoS rules on on-premises routers to prioritize
latency-sensitive traffic such as voice and video over bulk
transfers such as data syncs.

**Desired outcome:** Guaranteed
performance for critical workloads while optimizing bandwidth costs.

**Level of risk exposed if this best practice
is not established:** Medium

**Benefits of establishing this best
practice:**

- Prevents costly performance degradation for high-priority
traffic
- Enables oversubscription of links without impacting critical
workloads
- Aligns network costs with business value

## Implementation guidance

- Tag traffic with DSCP markers for on-premises traffic
classification
- Apply shapers or queues on on-premises routers

*Source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hncost06-bp01.html*

---

# HNCOST06-BP02 Separate traffic classes for dedicated connections

Create multiple dedicated connections for distinct traffic classes
such as production versus backups. Assign guaranteed bandwidth to
critical dedicated connections and use best-effort routing for
dedicated connections.

**Desired outcome:** Cost-effective
traffic segregation with guaranteed SLAs for priority workloads.

**Level of risk exposed if this best
practice is not established:** Low

**Benefits of establishing this best
practice:**

- Simplifies cost allocation by traffic type
- Enables independent scaling of traffic classes
- Complies with network isolation requirements

## Implementation guidance

- Configure separate BGP communities for dedicated connection.
For example, you can achieve this using AWS Direct Connection
VIFs on dedicated connections.

### Resources

- [Direct
Connect virtual interfaces](https://docs.aws.amazon.com/directconnect/latest/UserGuide/create-vif.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hncost06-bp02.html*

---

# HNCOST07 — Optimize over time

**Pillar**: Cost Optimization  
**Best Practices**: 1

---

# HNCOST07-BP01 Use dedicated connection for high-volume predictable traffic

Deploy dedicated connection for production workloads requiring
consistent, high-bandwidth connectivity between on-premises and
cloud environments. Dedicated connection offers lower per-GB costs
compared to IPSec VPN and avoids internet variability.

**Desired outcome:** Predictable,
reduced data transfer costs for mission-critical workloads.

**Level of risk exposed if this best practice
is not established:** Medium

**Benefits of establishing this best
practice:**

- cost savings versus VPN for high-volume traffic
- Improved performance and reliability

## Implementation guidance

- Start with low bandwidth dedicated connections and scale up
with high bandwidth connections or multiple connections with
LAG

## Resources

- [AWS Direct Connect Pricing](https://aws.amazon.com/directconnect/pricing/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hncost07-bp01.html*

---

# HNCOST08 — Optimize over time

**Pillar**: Cost Optimization  
**Best Practices**: 1

---

# HNCOST08-BP01 Regular cost analysis

Review cost dashboards to identify underutilized resources,
anomalous spikes, and opportunities to switch connectivity types.

**Desired outcome:** Data-driven cost
reduction through continuous refinement.

**Level of risk exposed if this best practice
is not established:** Low

**Benefits of establishing this best
practice:**

- Visibility into cost drivers
- Identification of legacy resources for decommissioning
- Support for budget forecasting

## Implementation guidance

- Identified data transfer changes in cost data, such as by
filtering Cost and Usage data by line_item_usage_type for
DataTransfer-Out-Bytes.
- Use cost dashboards to review usage patterns. For example, you
can achieve this by using Amazon Athena and Amazon Quick
Suite.
- Share findings in regular, weekly or monthly and FinOps
reviews.

**Resources:**

- [AWS Data Exports](https://docs.aws.amazon.com/cur/latest/userguide/data-transfer-cost-analysis.html)
- [AWS Well-Architected Cost & Usage Report Library](https://catalog.workshops.aws/cur-query-library/en-US/queries/networking-and-content-delivery)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hncost08-bp01.html*

---

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
