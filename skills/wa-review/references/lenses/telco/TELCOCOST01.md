# TELCOCOST01 — Expenditure and usage awareness

**Pillar**: Cost Optimization  
**Best Practices**: 1

---

# TELCOCOST01-BP01 Implement attribution of cost to each telco domain hosted on the AWS (access, core, edge, OSS, and BSS)

Telcos with workloads running on AWS can take advantage of AWS' detailed cost and usage
reporting to attribute costs to each of their domains (like access, core, edge, OSS, and BSS). By
tagging resources appropriately, costs can be allocated to each domain.

**Desired outcome:**

- Gain visibility into the cost breakdown of your telco workload across different
domains.
- Identify high-cost areas and make informed decisions to optimize spending.
- Improve cost transparency and accountability across your telco organization.

**Common anti-patterns:**

- Lack of cost tagging and tracking for resources, leading to unclear cost attribution.
- Siloed cost management, with different teams responsible for distinct domains.
- Reliance on high-level consolidated billing reports without granular cost breakdowns.

**Benefits of establishing this best practice:**

- Enables data-driven cost optimization decisions.
- Improves cross-team collaboration and accountability for cost management.
- Facilitates chargeback or show back models for internal cost allocation.
- Supports regulatory adherence and auditing requirements.

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

Accurately attributing costs to different telco domains is essential for effective cost
optimization. By using AWS's detailed cost and usage reporting capabilities, you can
gain visibility into the specific costs associated with each of your telco domains. This information can assist you to identify areas of high
spending and make informed decisions to optimize costs.

### Implementation steps

- Verify you have enabled detailed billing and cost allocation reports in your AWS account.
- Create AWS Cost and Usage tags for your resources to categorize costs by domain.
- Apply the appropriate tags to your AWS resources, such as EC2 instances, S3
buckets, and Lambda functions.
- Configure AWS Cost Explorer to analyze and visualize your costs by the tagged
domains.
- Set up AWS Budgets and alerts to monitor and receive notifications on cost trends
for each domain.
- Regularly review the cost allocation reports and optimize costs in high-spend
domains.

## Resources

**Key AWS services:**

- [AWS Cost and Usage Reports](https://aws.amazon.com/aws-cost-management/aws-cost-and-usage-reporting/)
- [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/)
- [AWS Budgets](https://aws.amazon.com/aws-cost-management/aws-budgets/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/telco-lens/telcocost01-bp01.html*

---
