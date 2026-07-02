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
