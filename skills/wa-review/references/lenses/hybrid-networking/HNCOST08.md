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
