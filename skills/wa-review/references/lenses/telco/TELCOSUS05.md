# TELCOSUS05 — Carbon tracking

**Pillar**: Sustainability  
**Best Practices**: 1

---

# TELCOSUS05-BP01 Establish comprehensive carbon footprint monitoring for telco networks

Measuring carbon footprint across telco operations requires tracking emissions from
multiple sources including data centers, network equipment, edge sites, and even supply chain
activities.

**Desired outcome:** Achieve complete visibility of carbon
emissions across network operations with automated tracking, reporting accuracy, and actionable
insights that enable emission reductions aligned with Science Based Targets initiative (SBTi)
commitments.

**Benefits of establishing this practice:**

- Automated reporting for
telecommunications environmental regulations.
- Identify and prioritize
highest-impact reduction opportunities.
- Accurate sustainability reporting
for investors and customers.
- Demonstrated environmental
leadership in telecommunications sector.
- Link carbon reduction initiatives to
operational cost savings.

**Level of risk exposed if this best practice is not established**:
Low

## Implementation guidance

Implement a comprehensive monitoring system that captures the following while
providing actionable insights for reduction strategies:

- Scope 1: direct emissions
- Scope 2: purchased electricity
- Scope 3: value chain emissions

Design your monitoring architecture to automatically collect energy consumption data from
infrastructure components. Tag AWS resources with sustainability metadata (equipment type,
location, and business function) to enable granular carbon accounting. Integrate with AWS
Customer Carbon Footprint Tool for baseline cloud emissions data, then augment with custom
metrics for on-premises equipment and network operations.

Establish automated reporting pipelines that aggregate carbon data, calculate emissions
using regional grid factors, and generate reports for regulatory requirements and
sustainability frameworks like SBTi or Global System for Mobile
Communications Association (GSMA) climate targets.

### Implementation steps

- Enable AWS Customer Carbon Footprint Tool and configure monthly exports to S3 for
historical analysis and trend tracking.
- Implement comprehensive tagging strategy with tags: `CarbonCategory`, `LocationGrid`,
`NetworkFunction`, and `EquipmentType` for AWS resources.
- Deploy Amazon CloudWatch custom metrics to track energy consumption from on-premises network
equipment using AWS IoT Greengrass at edge sites.
- Create AWS Glue ETL pipelines to combine AWS carbon data with on-premises
metrics, calculating total emissions using Regional emission factors.
- Set up Amazon Managed Grafana dashboards displaying real-time carbon intensity metrics, with
drill-down capabilities by service, region, and network function.
- Configure Quick to generate automated monthly sustainability reports aligned with
GSMA or SBTi reporting requirements.
- Implement Amazon EventBridge rules to trigger alerts when carbon emissions exceed defined
thresholds or deviate from reduction targets.
- Deploy AWS Lambda functions to calculate power usage effectiveness (PUE) for data
centers and network efficiency metrics for RAN sites.
- Use Amazon Forecast to predict future carbon emissions based on network growth
projections and planned efficiency improvements.

## Resources

**Key AWS services:**

- [Amazon S3](https://aws.amazon.com/s3/)
- [AWS Glue](https://aws.amazon.com/glue/)
- [Quick](https://aws.amazon.com/quicksuite/quicksight/)
- [Amazon EventBridge](https://aws.amazon.com/eventbridge/)
- [AWS Lambda](https://aws.amazon.com/lambda/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/telco-lens/telcosus05-bp01.html*

---
