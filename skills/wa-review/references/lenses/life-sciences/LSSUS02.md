# LSSUS02 — Sustainability metric tracking and reporting

**Pillar**: Sustainability  
**Best Practices**: 1

---

# LSSUS02-BP01 Implement sustainability proxy metrics pipeline for research workloads

Establish comprehensive tagging strategies and normalized metrics to
track and measure sustainability performance across research
workloads. Implement proxy metrics that correlate resource
consumption with research outputs to enable meaningful comparisons
and optimization opportunities. Create sustainability KPIs that
combine resource utilization data with research milestones to drive
continuous improvement in energy efficiency and environmental
impact.

**Desired outcome:** Establish
measurable sustainability metrics that enable data-driven
optimization of research workloads and provide clear visibility into
environmental impact across different research activities and
architectural patterns.

**Common anti-patterns:**

- You don't implement consistent tagging strategies across
research workloads and resources.
- You measure absolute resource consumption without normalizing
for research outputs.
- You don't establish baseline metrics to track sustainability
improvements over time.
- You collect metrics but don't integrate them into research
workflow planning and optimization.
- You don't correlate resource consumption with actual research
deliverables and milestones.
- You rely solely on cost metrics without considering
environmental impact measurements.
- You don't establish regular review cycles to assess and act on
sustainability metrics.

**Benefits of establishing this best
practice:**

- Enable data-driven decisions for optimizing research workload
sustainability.
- Provide clear visibility into environmental impact across
different research activities.
- Support regulatory adherence and sustainability reporting
requirements.
- Align research operations with organizational sustainability
goals and commitments.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Sustainability metrics for research workloads require a strategic
approach that balances measurement granularity with practical
implementation. Life sciences organizations must track resource
consumption in ways that correlate with research outputs, enabling
meaningful comparisons across different types of analyses and
computational approaches. This is particularly important given the
diverse nature of life sciences computing, from high-throughput
genomics processing to complex molecular modeling simulations.

Proxy metrics serve as practical indicators of sustainability
performance when direct energy measurements are not feasible. By
normalizing resource consumption against research outputs (such as
vCPU hours per genome processed or GPU hours per molecular
structure analyzed), organizations can identify optimization
opportunities and track improvements over time. Integration with
the AWS Customer Carbon Footprint Tool provides additional context
by correlating proxy metrics with actual carbon footprint data.

### Implementation steps

- Establish comprehensive tagging strategy for research
workloads:

Implement consistent tags for research type (genomics,
proteomics, drug discovery).
- Tag resources by project phase (discovery, validation,
production).
- Include architectural pattern tags (batch processing,
interactive analysis, real-time).
- Use AWS Resource Groups and Tag Editor for centralized
tag management.

- Define and implement normalized sustainability metrics:

Calculate vCPU hours per genome processed for genomics
workloads.
- Track GPU hours per molecular structure analyzed for
computational chemistry.
- Measure storage efficiency through data processed per TB
stored.
- Use Amazon CloudWatch custom metrics to track normalized
performance indicators.

- Create sustainability KPIs aligned with research outputs:

Combine resource utilization metrics with research
milestone achievements.
- Track energy efficiency improvements over time using
baseline comparisons.
- Implement cost-per-research-output metrics for
comprehensive sustainability assessment.
- Use AWS Cost and Usage Reports for detailed resource
consumption analysis.

- Integrate metrics with AWS Customer Carbon Footprint Tool:

Correlate proxy metrics with account and Region-level
carbon footprint data.
- Establish regular reporting cycles for sustainability
performance.
- Create dashboards that combine resource efficiency with
environmental impact.
- Use Quick for sustainability reporting and
visualization.

- Establish continuous monitoring and optimization processes:

Integrate sustainability metrics into research workflow
planning.
- Conduct regular sustainability reviews with research
teams.
- Create feedback loops to incorporate sustainability
learnings into future research planning.

## Resources

**Related best practices:**

- [LSSUS01-BP01
Design high-performance computing workloads to minimize energy
usage](lssus01-bp01.html)
- [LSSUS01-BP02
Leverage energy efficient hardware and services](lssus01-bp02.html)
- [LSSUS03-BP01
Optimize Data Management for Sustainability in Life
Sciences](lssus03-bp01.html)

**Related documents:**

- [AWS Customer Carbon Footprint Tool](https://aws.amazon.com/aws-cost-management/aws-customer-carbon-footprint-tool/)

**Related examples:**

- [AWS Solutions for Sustainability](https://aws.amazon.com/solutions/sustainability/)

**Related tools:**

- [AWS Customer Carbon Footprint Tool](https://aws.amazon.com/aws-cost-management/aws-customer-carbon-footprint-tool/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lssus02-bp01.html*

---
