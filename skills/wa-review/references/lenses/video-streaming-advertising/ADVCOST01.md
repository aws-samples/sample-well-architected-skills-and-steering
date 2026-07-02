# ADVCOST01 — Practice Cloud Financial Management

**Pillar**: Cost Optimization  
**Best Practices**: 2

---

# ADVCOST01-BP01 Continually measure costs of different real-time bidding workloads, and adjust resource allocation accordingly

With fluctuations in usage over time, the costs associated with real-time bidding
workloads can vary significantly. Continually monitoring costs is the best way to keep them
under control.

## Implementation guidance

- Set KPIs for each campaign to evaluate cost-to-revenue ratios, as this is key to
measuring value generation.
- Set KPIs for billing metrics (for example, resource costs) as well as campaign
metrics (for example, click-through rate or new subscribers).
- Implement cost allocation tags for resources relevant to campaign tracking.
- Use the Cost and Usage Dashboards Operations Solution (CUDOS) Dashboard as a way
to quickly visualize information about RTB costs and performance.
- Use [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) for one-off visualizations of cost data.
- Generate [Quick](https://aws.amazon.com/quicksight/) dashboards that
are specific to each campaign or that comprise the business as a whole.
- Configure Quick with user-configurable filters to allow users to focus on the data
that matters most to them.
- Configure Quick to email dashboard reports to users on a schedule to automate and
simplify the process.
- Regularly evaluate the data and report findings back to the business.
- As campaigns progress, continually re-evaluate them, and adjust resource
allocation to meet value generation goals.

## Key AWS services

- [Amazon Athena](https://aws.amazon.com/athena/)
- [AWS Data Exports](https://docs.aws.amazon.com/cur/latest/userguide/what-is-data-exports.html)

## Resources

- [Guidance for Deploying a Data Transfer Dashboard for AdTech on AWS](https://aws.amazon.com/solutions/guidance/deploying-a-data-transfer-dashboard-for-adtech-on-aws/)
- [Guidance for Capturing Advertising OpenRTB (Real-Time Bidding) Events for Analytics
on AWS](https://aws.amazon.com/solutions/guidance/capturing-advertising-openrtb-real-time-bidding-events-for-analytics-on-aws/)
- [Using CUDOS Dashboard visualizations for AWS Marketplace spend visibility and
optimization](https://aws.amazon.com/blogs/awsmarketplace/using-cudos-dashboard-visualizations-aws-marketplace-spend-visibility-optimization/)
- [Additional dashboards](https://catalog.workshops.aws/awscid/en-US/dashboards/additional)
- [Organizing costs
using AWS Cost Categories](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/manage-cost-categories.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advcost01-bp01.html*

---

# ADVCOST01-BP02 Evaluate resiliency needs against the cost of downtime for ad delivery and bidding

While resiliency can increase the cost of workloads, downtime can also be very
expensive. It's important to understand the costs of having a resilient infrastructure
against the costs of not having a resilient infrastructure.

## Implementation guidance

- Quantify the cost of downtime for each campaign based on its expected revenue.

Analyze historical data and projections to estimate the potential revenue
loss due to downtime.
- Consider the impact on customer satisfaction and brand reputation.

- Estimate the cost of applying resiliency measures.

Evaluate the cost of additional resources required for multi-Regional
deployments, backup, and recovery solutions
- Use AWS tools like [AWS Pricing Calculator](https://calculator.aws/#/)
for estimating costs of future resiliency efforts and [Quick](https://aws.amazon.com/quicksight/), [Amazon Athena](https://aws.amazon.com/athena/), AWS Cost and Usage Report, and [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) for cost analysis
and reporting.

- Compare the cost of downtime with the cost of resiliency measures.

If the potential lost revenue and reputation costs of downtime exceed the
cost of resiliency, favor implementing resiliency measures.
- Consider multi-regional deployments, backup and recovery solutions, and other
resiliency best practices.

By following these steps, you can make informed decisions about implementing
resiliency measures based on a cost-benefit analysis, using AWS tools and services to
optimize your approach and ensure business continuity.

## Key AWS services

- [AWS Data Exports](https://aws.amazon.com/aws-cost-management/aws-data-exports/)
- [AWS Resilience Hub](https://aws.amazon.com/resilience-hub/)

## Resources

- [Stage
1: Set objectives](https://docs.aws.amazon.com/prescriptive-guidance/latest/resilience-lifecycle-framework/stage-1.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advcost01-bp02.html*

---
