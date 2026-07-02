# LSCOST03 — Manage demand and supply resources

**Pillar**: Cost Optimization  
**Best Practices**: 1

---

# LSCOST03-BP01 Align infrastructure capacity with R&D development stages

Design infrastructure that can adapt to changing requirements across
different R&D phases while maintaining regulatory adherence and
research integrity.

**Desired outcome:** An adaptive
infrastructure framework that efficiently matches computational
resources to R&D stage requirements, minimizing costs through
automated scaling while improving regulatory adherence and
maintaining research velocity across the development phases.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

To effectively optimize research and development (R&D)
infrastructure costs across development stages, establish a clear
framework for identifying and categorizing different R&D
phases and their specific infrastructure requirements.

Create a resource mapping matrix that defines computational,
storage, and processing needs for each phase. Implement automated
scaling solutions that adjust infrastructure based on research
phase triggers and actual usage patterns.

Establish monitoring and metrics to track resource utilization and
costs across different stages. Verify that regulatory requirements
are built into the infrastructure design from the start, with
appropriate validation and documentation processes.

### Implementation steps

- Document current infrastructure usage patterns across
R&D phases and map regulatory requirements to each
stage. Define key performance indicators and cost metrics,
and establish baseline costs for each R&D phase. This
comprehensive assessment provides a foundation for
optimization efforts and maintains regulatory standards
throughout the process.
- Create flexible templates for different R&D phase
configurations, and design automated scaling triggers based
on phase transitions. Implement robust monitoring and
alerting systems, and develop cost allocation mechanisms.
This design phase focuses on building a responsive and
efficient infrastructure that can adapt to changing research
needs while maintaining cost visibility.
- Deploy the phase-specific infrastructure templates and
configure automated scaling policies. Implement resource
tagging for detailed cost tracking and set up governance
controls. This phase puts the design into action, verifying
that the infrastructure can efficiently support various
R&D stages while maintaining regulatory adherence.
- Continuously monitor resource utilization and costs,
regularly reviewing and adjusting scaling thresholds. Use
AWS right-sizing technologies such as AWS Compute Optimizer,
AWS Cost Optimization Hub, and AWS Trusted Advisor to
validate scaling policy implementations across each phase.
Conduct periodic regulatory validations and pursue ongoing
optimization based on usage patterns. These tools provide
data-driven recommendations to optimize resource
utilization, validate scaling configurations, and identify
cost-saving opportunities. This ongoing process keeps the
infrastructure efficient, cost-effective, and compatible as
research needs evolve over time.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lscost03-bp01.html*

---
