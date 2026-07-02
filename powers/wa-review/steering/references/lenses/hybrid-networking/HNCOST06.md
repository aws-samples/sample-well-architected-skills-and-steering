# HNCOST06 — Manage demand and supply resources

**Pillar**: Cost Optimization  
**Best Practices**: 2

---

# HNCOST06-BP01 Implement QoS policies for traffic prioritization

Configure QoS rules on on-premises routers to prioritize
latency-sensitive traffic such as voice and video over bulk
transfers such as data syncs.

**Desired outcome:** Guaranteed
performance for critical workloads while optimizing bandwidth costs.

**Level of risk exposed if this best practice
is not established:** Medium

**Benefits of establishing this best
practice:**

- Prevents costly performance degradation for high-priority
traffic
- Enables oversubscription of links without impacting critical
workloads
- Aligns network costs with business value

## Implementation guidance

- Tag traffic with DSCP markers for on-premises traffic
classification
- Apply shapers or queues on on-premises routers

*Source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hncost06-bp01.html*

---

# HNCOST06-BP02 Separate traffic classes for dedicated connections

Create multiple dedicated connections for distinct traffic classes
such as production versus backups. Assign guaranteed bandwidth to
critical dedicated connections and use best-effort routing for
dedicated connections.

**Desired outcome:** Cost-effective
traffic segregation with guaranteed SLAs for priority workloads.

**Level of risk exposed if this best
practice is not established:** Low

**Benefits of establishing this best
practice:**

- Simplifies cost allocation by traffic type
- Enables independent scaling of traffic classes
- Complies with network isolation requirements

## Implementation guidance

- Configure separate BGP communities for dedicated connection.
For example, you can achieve this using AWS Direct Connection
VIFs on dedicated connections.

### Resources

- [Direct
Connect virtual interfaces](https://docs.aws.amazon.com/directconnect/latest/UserGuide/create-vif.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hncost06-bp02.html*

---
