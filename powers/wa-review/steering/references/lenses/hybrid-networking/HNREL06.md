# HNREL06 — Failure management

**Pillar**: Reliability  
**Best Practices**: 2

---

# HNREL06-BP01 Use multiple data centers for physical location redundancy

Connect from multiple geographically separate data centers or
colocation sites to cloud for true physical location redundancy. Use
dynamically routed, Active/Active connections across these sites to
enable automatic load balancing and failover.

**Desired outcome:** Ensure network
connectivity to cloud remains available even if one location
experiences an outage or disaster.

**Level of risk exposed if this best practice
is not established:** High

**Benefits of establishing this best
practice:**

- Eliminates single points of failure at the physical site level
- Enables business continuity and disaster recovery
- Supports high availability and compliance requirements
- Improves resilience to disasters or unplanned events

## Implementation guidance

- Deploy dedicated connections from at least two geographically
distinct facilities.
- Use dynamic routing BGP for automatic failover.
- Test failover regularly to validate resiliency.

## Resources

- [AWS Direct Connect Resiliency Recommendations](https://aws.amazon.com/directconnect/resiliency-recommendation/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnrel06-bp01.html*

---

# HNREL06-BP02 Ensure service continuity with redundant hardware and diverse telecommunications providers

Implementing redundant hardware components across geographic
locations, organizations can mitigate single points of failure that
threaten critical workloads. This resilience strategy should extend
beyond computing resources to include diverse telecommunications
providers, creating independent network paths that remain
operational even when regional carriers experience outages. The
combination of hardware redundancy and carrier diversity creates a
robust foundation that enables businesses to maintain operations
through localized disruptions, ensuring that customers experience
minimal service interruptions and that service level agreements
remain intact despite infrastructure challenges.

**Desired outcome:** Reduce risk of
connectivity loss due to hardware or carrier failures, maintaining
consistent hybrid network availability.

**Level of risk exposed if this best practice
is not established:** High

**Benefits of establishing this best
practice:**

- Increases fault tolerance and uptime
- Minimizes downtime from single hardware or carrier outages
- Supports disaster recovery planning
- Helps meet or exceed AWS and provider SLA commitments

## Implementation guidance

- Use separate network devices and cables for each connection.
- Engage more than one telecom provider with diverse paths for
"last mile" connections.
- Periodically review and test infrastructure and SLAs.

## Resources

- [AWS Direct Connect Service Level Agreement](https://aws.amazon.com/directconnect/sla/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnrel06-bp02.html*

---
