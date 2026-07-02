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
