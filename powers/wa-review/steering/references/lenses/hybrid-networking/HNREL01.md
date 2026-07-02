# HNREL01 — Foundations

**Pillar**: Reliability  
**Best Practices**: 2

---

# HNREL01-BP01 Implement redundant power infrastructure

Deploy dual power feeds, redundant uninterruptible power supply
(UPS) systems, and backup generators for all critical network
equipment. Regularly test and maintain power systems to ensure
continuous operation during outages.

**Desired outcome:** Sustain
on-premises operations and prevent downtime during power failures.

**Level of risk exposed if this best practice
is not established:** High

**Benefits of establishing this best
practice:**

- Avoid unexpected outages due to power disruptions
- Supports continuous network connectivity to cloud
- Satisfies disaster recovery and business continuity requirements
- Prevents a single-point power failure

## Implementation guidance

- Use dual utility or grid power where available
- Maintain redundant UPS and generator systems
- Schedule and document periodic power failover drills

*Source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnrel01-bp01.html*

---

# HNREL01-BP02 Maintain effective life cycle management for on-premises network equipment

Implement a structured life cycle management process for all
on-premises networking equipment, including routers, switches, and
cabling. Track equipment age, support contracts, firmware, and plan
for timely refreshes and replacement to avoid end-of-life risks.

**Desired outcome:** All network
hardware supporting hybrid connectivity remains supported, secure,
and reliable throughout its operational life.

**Level of risk exposed if this best practice
is not established:** High

**Benefits of establishing this best
practice:**

- Reduces risk of unplanned outages due to equipment failure
- Ensure continued vendor support and security patching
- Simplifies compliance and audit for critical infrastructure
- Prevents operational surprises from obsolete hardware

## Implementation guidance

- Maintain an asset inventory with warranty or support
expiration dates
- Monitor firmware and software for patches and end-of-support
notices
- Budget for regular equipment refresh and upgrade cycles
- Retire or replace equipment before it reaches end-of-life
- Document and regularly review network equipment management
procedures

*Source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnrel01-bp02.html*

---
