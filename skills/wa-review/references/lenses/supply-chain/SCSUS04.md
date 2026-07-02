# SCSUS04 — Software and architecture

**Pillar**: Sustainability  
**Best Practices**: 2

---

# SCSUS04-BP01 Optimize your compute workloads for your supply chain sustainability

Consider configuring AWS Compute Optimizer to analyze and
investigate supply chain sustainability related workloads, to
support your analysis on how to optimize the usage of compute
resources to sustain your supply chain workloads.

**Desired outcome:** Optimize the
performance of compute workloads to reduce energy consumption and
emissions while maintaining the reliability of supply chain
operations.

**Benefits of establishing this best
practice:** Enhances the efficiency of compute resource
utilization, reduces operational costs, and aligns sustainability
efforts with performance objectives.

**Level of risk exposed if this best
practice is not established:** Medium

## Implementation guidance

Before proceeding with scenarios simulation over your supply
chains operations, to help you understand why and which set of
operations are requiring more compute and memory resources,
consider to setup and run AWS Compute Optimizer combined with
Amazon CloudWatch metrics to analyze resource utilization
patterns and identify optimization opportunities, leading as a
direct consequence to sustainability's KPIs improvements.

### Implementation steps

- Configure AWS Compute Optimizer to analyze supply chains
workload performance and resource utilization patterns.
- Provision Amazon CloudWatch and configure metrics
collection to gather detailed performance data across all
supply chains compute resources.
- Analyze compute utilization patterns to identify
over-provisioned or under-utilized resources that can be
optimized.
- Right-size compute instances based on actual usage
patterns and performance requirements.
- Implement automated scaling policies to match compute
resources with actual demand patterns.
- Monitor and measure the impact of optimization efforts on
both performance and sustainability metrics.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/supply-chain-lens/scsus04-bp01.html*

---

# SCSUS04-BP02 Build and run optimization models for resources involved in supply chains sustainability

Consider building and run specific optimization models targeting
supply chains sustainability, through scenarios simulation able to
simulate resources usage and collect metrics for supply chains
planning, execution and enablement.

**Desired outcome**: Develop and
use optimization models to identify opportunities for operations
efficiency, resource efficiency, reduce emissions, and align
resource usage with both sustainability and business objectives.

**Benefits of establishing this best
practice:** Facilitates data-driven resource allocation,
helps with optimal performance with minimal environmental impact,
and supports comprehensive scenario planning for supply chain
operations.

**Level of risk exposed if this best
practice is not established:** High

## Implementation guidance

Optimization models specifically envisioned for supply chain
sustainability can be designed, built, and configured through
optimization capabilities running on AWS as managed services.

This allows you to optimize your operations and the use of
resources to achieve lower CO2 emissions and energy
optimization, while generating more efficient purpose-built
analysis for sustainability. The integration of these
sustainability measures with existing optimization analysis
enables greater focus on cost efficiency, service-level
performance, and the ability to respond to disruptions or
failures.

### Implementation steps

- Design and develop optimization models specifically
focused on supply chain sustainability using AWS managed
services.
- Integrate sustainability
[Software
and architecture](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/software-and-architecture.html)metrics with existing cost
efficiency and performance optimization models.
- Implement scenario simulation capabilities to test
different resource allocation strategies and their
sustainability impact.
- Configure automated optimization workflows that balance
sustainability goals with operational efficiency and
requirements.
- Establish feedback loops to continuously improve
optimization models based on actual performance and
sustainability outcomes.
- Create reporting and visualization tools to communicate
optimization results and sustainability improvements to
stakeholders.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/supply-chain-lens/scsus04-bp02.html*

---
