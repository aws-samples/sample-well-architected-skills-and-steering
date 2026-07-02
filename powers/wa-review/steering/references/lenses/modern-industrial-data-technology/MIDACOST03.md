# MIDACOST03 — Migration optimization

**Pillar**: Cost Optimization  
**Best Practices**: 1

---

# MIDACOST03-BP01 Analyze all components of your industry workloads for migration and modernization

Develop an optimized migration strategy that reduces costs while maintaining or improving
operational capabilities for manufacturing-specific workloads. This includes analyzing OT and IT
dependencies, assessing modernization opportunities, and planning migrations that minimize
production impact.

**Desired outcome:** Optimized migration strategy that reduces
costs while maintaining or improving operational capabilities.

**Common anti-patterns:**

- Migrating manufacturing systems without analyzing OT and IT dependencies
- Implementing direct migration strategies for all workloads while disregarding
potential optimization opportunities
- Migrating critical production systems first without proper testing
- Overlooking data transfer costs between cloud and on-premises manufacturing equipment
- Planning migration without input from shop floor operations teams
- Ignoring regulatory compliance requirements specific to manufacturing processes
- Making migration decisions based solely on IT costs without considering production
impact
- Not accounting for legacy manufacturing systems' integration requirements

**Benefits of establishing this best practice:**

- Reduced infrastructure costs
- Improved operational efficiency
- Optimized resource utilization
- Clear migration roadmap

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

Before starting, verify that you have:

- Complete inventory of IT/OT systems and their dependencies
- Manufacturing process maps and criticality levels
- Compliance and regulatory requirements documented

Key decisions needed:

- Which systems are candidates for migration based on criticality
- Migration strategy selection (rehost, replatform, or refactor) per system
- Migration sequence aligned with production impact
- Cost-saving validation thresholds

Then, analyze industrial workloads by documenting current infrastructure costs, mapping
OT and IT system dependencies (like SCADA to MES connections), and analyzing data transfer
patterns. Evaluate options including rehost, replatform, or modernize based on each
component's needs. Create cost-benefit analyses comparing current versus projected cloud
costs, with particular attention to manufacturing-specific requirements and production
continuity.

### Implementation steps

- Conduct comprehensive workload assessment:

Current infrastructure costs
- Application dependencies
- Performance requirements
- Data transfer patterns

- Evaluate migration options:

Rehost (lift and shift)
- Replatform
- Refactor or modernize

- Create a cost-benefit analysis.
- Develop a migration timeline.
- Plan for optimization post-migration.

## Key AWS services

- AWS Migration Hub
- AWS Application Discovery Service
- AWS Migration Evaluator
- AWS Transform MGN

## Resources

**Related documents:**

- [AWS Migration Hub](https://docs.aws.amazon.com/migrationhub/)
- [AWS Application
Discovery Service](https://docs.aws.amazon.com/application-discovery/)
- [AWS Migration
Evaluator](https://aws.amazon.com/migration-evaluator/)
- [AWS Application Migration
Service](https://docs.aws.amazon.com/mgn/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midacost03-bp01.html*

---
