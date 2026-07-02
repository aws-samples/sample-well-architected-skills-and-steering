# EUCREL02 — Workload architecture

**Pillar**: Reliability  
**Best Practices**: 1

---

# EUCREL02-BP01 Use multiple regions for your EUC environment to minimize downtime

[Amazon WorkSpaces Multi-Region Resilience](https://docs.aws.amazon.com/workspaces/latest/adminguide/multi-region-resilience.html) offers cost-effective,
easy-to-manage operational continuity solutions that keep your
users online and productive . Organizations should proactively
design their environment to anticipate failure and plan for a
fast recovery.

**Level of risk exposed if this best
practice is not established:** Medium

## Implementation guidance

Implement Amazon WorkSpaces Multi-Region Resilience to enable
cost-effective and smoothly managed operational continuity.
This approach verifies that users remain online and productive
with minimal recovery time through standby WorkSpaces in
alternative AWS Regions during disruptive events.
Additionally, regularly test your multi-Region setup to verify
its effectiveness in supporting operational continuity.
Conduct failover drills and simulations to validate the RTO
and identify any potential areas of improvement in your
resilience strategy. By using Multi-Region Resilience, you can
minimize service interruptions and provide uninterrupted
access to Amazon WorkSpaces for your users, even during
disruptive events.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucrel02-bp01.html*

---
