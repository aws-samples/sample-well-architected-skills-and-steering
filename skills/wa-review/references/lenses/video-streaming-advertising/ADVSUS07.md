# ADVSUS07 — Process and culture

**Pillar**: Sustainability  
**Best Practices**: 1

---

# ADVSUS07-BP01 Incorporate an improvement process to reduce low utilization and idle resources or maximize the output from resources

Advertising workloads are changing at a rapid rate. As changes are
introduced consider which resources are the most efficient and
where resources can be removed. Use automation to create and
remove infrastructure as needed.

## Implementation guidance

- Establish a cadence to revisit SLAs with advertising partners.
- Prioritize how to reduce use when over-provisioning is identified (for example,
start with compute, then storage, then network usage).
- Continue to iterate with advertising partners on reducing the infrastructure needed
for a minimum viable representation of production for testing.
- Use [infrastructure as code (IaC)](https://docs.aws.amazon.com/whitepapers/latest/introduction-devops-aws/infrastructure-as-code.html) to set up a test environment, so they can be
removed when a testing or staging environment is no longer needed but easily recreated
when beneficial.

## Resources

- [Well-Architected Lab - Optimize Hardware Patterns and Observe Sustainability
KPIs](https://wellarchitectedlabs.com/sustainability/200_labs/200_optimize_hardware_patterns_observe_sustainability_kpis/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advsus07-bp01.html*

---
