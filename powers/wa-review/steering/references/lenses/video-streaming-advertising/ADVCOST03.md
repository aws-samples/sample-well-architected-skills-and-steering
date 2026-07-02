# ADVCOST03 — Optimizing communication costs

**Pillar**: Cost Optimization  
**Best Practices**: 3

---

# ADVCOST03-BP01 Consider private communication channels between SSP and DSP

Private communication channels can help keep traffic secure while also reducing
internet egress charges.

## Implementation guidance

With [AWS PrivateLink](https://aws.amazon.com/privatelink/), you can
establish secure, private communication channels between your SSPs, DSPs, and other AWS
services or on-premises resources. This approach enhances security, reduces data exposure
risks, and can improve performance for your programmatic advertising workloads, while
simplifying your network architecture and reducing operational overhead. In cases where
PrivateLink cannot be used, then Amazon VPC Peering, AWS Direct Connect, and AWS Global Accelerator can be
considered.

## Resources

- [AWS lowers data processing charges for AWS PrivateLink](https://aws.amazon.com/about-aws/whats-new/2021/07/aws-lowers-data-processing-charges-aws-privatelink/)
- [Get
started with AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/getting-started.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advcost03-bp01.html*

---

# ADVCOST03-BP02 When integrating SSPs and DSPs for programmatic advertising, co-locate the platforms

Keeping SSP and DSP components together can keep transactions fast while minimizing
inter-AZ and inter-Region traffic charges.

## Implementation guidance

When integrating SSPs and DSPs for programmatic advertising, use Network Load
Balancer (NLB) to direct traffic from the SSP to the DSP within the same Availability
Zone. This approach can help optimize costs while providing high performance and
availability.

- **Deploy in the same Availability Zone:** Deploy your SSP
and DSP components (such as bidding nodes) within the same Availability Zone based on
expected traffic patterns to minimize cross-AZ data transfer costs and reduce network
latency.
- **Use Network Load Balancer (NLB):** Use Network Load
Balancer (NLB) to distribute traffic from the SSP to the DSP instances within the same
Availability Zone. NLB is cost-effective for TCP traffic and can handle millions of
requests per second.
- **Configure your NLB:** Set the cross-zone-load-balancing
attribute to false, or use the appropriate routing policy to prioritize routing within
the same Availability Zone. This approach routes traffic preferentially to bidder
nodes within the same Availability Zone, reducing cross-AZ data transfer costs.
- **Monitor and optimize:** Regularly monitor your data
transfer costs and traffic patterns across Availability Zones. Adjust your resource
placement and NLB configurations as needed to optimize cost-effectiveness.
- **Use cost optimization tools:** Use AWS Cost Explorer,
AWS Budgets, and AWS Cost Anomaly Detection to monitor and analyze your costs, set budgets, and
receive alerts for potential cost anomalies.
- **Automate and scale:** Use AWS CloudFormation or AWS CDK to
automate the provisioning and management of your SSP and DSP infrastructure, which
helps you scale efficiently and consistently while maintaining cost optimization.

## Resources

- [Guidance for AdTech Private Network on AWS](https://aws.amazon.com/solutions/guidance/adtech-private-network-on-aws/)
- [Announcing new AWS Network Load Balancer (NLB) availability and performance
capabilities](https://aws.amazon.com/about-aws/whats-new/2023/10/aws-nlb-availability-performance-capabilities/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advcost03-bp02.html*

---

# ADVCOST03-BP03 Co-locate bidder and database nodes

Keeping bidder and database nodes together can help transactions occur quickly and can
also reduce inter-AZ and inter-Region traffic charges.

## Implementation guidance

To optimize costs when configuring advertising bidder nodes to communicate with
database nodes within the same Availability Zone, consider the following guidance:

- **Resource placement:** Carefully plan the placement of
your bidder nodes and database nodes across Availability Zones. Co-locate bidder nodes
and their corresponding database nodes within the same Availability Zone to minimize
cross-AZ data transfer costs.
- **Database configuration:** If using a managed database
service like Amazon RDS, configure your database instances to use multi-AZ deployment
within the same AWS Region. This separates the primary and standby database
instances into separate Availability Zones, providing high availability while
minimizing cross-AZ data transfer costs for your bidder nodes.
- **Network configuration:** Configure your VPC and subnets
to verify that bidder nodes and database nodes within the same AZ can communicate
efficiently. Use private IP addresses, and avoid public IP addresses or internet
gateways, which can incur additional data transfer costs.
- **Caching and replication:** Implement caching strategies
and read replicas for your database nodes to reduce the amount of data transfer
required between bidder nodes and database nodes. This can further minimize cross-AZ
data transfer costs.
- **Monitoring and optimization:** Regularly monitor your
data transfer costs and traffic patterns across AZs. Adjust your resource placement
and network configurations as needed to optimize cost-effectiveness.
- **Use cost optimization tools:** Use [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/),
[AWS Budgets](https://aws.amazon.com/aws-cost-management/aws-budgets/), and [AWS Cost Anomaly Detection](https://aws.amazon.com/aws-cost-management/aws-cost-anomaly-detection/) to monitor
and analyze your costs, set budgets, and receive alerts for potential cost anomalies.

## Key AWS services

[Network Load Balancer (NLB)](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html)

## Resources

- [Exploring Data Transfer Costs for AWS Managed Databases](https://aws.amazon.com/blogs/architecture/exploring-data-transfer-costs-for-aws-managed-databases/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advcost03-bp03.html*

---
