# HNREL04 — Failure management

**Pillar**: Reliability  
**Best Practices**: 4

---

# HNREL04-BP01 Use physical location redundancy to host dedicated connections

Design dedicated connections hosted at multiple geographically
separated data centers or colocation facilities to provide physical
location redundancy. This design ensures that your connectivity to
cloud remains available even if one location is affected by an
outage or disaster.

**Desired outcome:** Maintain high
availability and business continuity for hybrid connectivity, even
in the event of a site-level failure.

**Level of risk exposed if this best practice
is not established:** High

**Benefits of establishing this best
practice:**

- Minimizes the risk of a single point of failure
- Enhance disaster recovery capabilities
- Supports compliance and uptime requirements
- Increases overall hybrid network resilience

## Implementation guidance

- Deploy Direct Connect connections in at least two
geographically distinct locations.
- Route traffic dynamically between locations for failover.
- Test failover scenarios regularly to validate resilience.

**Resources:**

- [AWS Direct Connect Resiliency Recommendations](https://aws.amazon.com/directconnect/resiliency-recommendation/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnrel04-bp01.html*

---

# HNREL04-BP02 Use redundant hardware and telecommunication providers

When designing remote connections to your cloud provider, use
redundant on-premises hardware and diverse telecommunications
providers. Ensure your last-mile connectivity has diverse physical
paths and that providers offer SLAs that meet your uptime
requirements.

**Desired outcome:** Reduce the risk
of connectivity loss due to hardware failure or carrier issues,
supporting continuous access to cloud resources.

**Level of risk exposed if this best practice
is not established:** High

**Benefits of establishing this best
practice:**

- Mitigates risks from hardware or provider outages
- Increases fault tolerance and connection reliability
- Supports compliance with high-availability SLAs
- Provides business continuity during provider-specific
disruptions

## Implementation guidance

- Use at least two separate routers, switches, and cabling for
each Direct Connect location.
- Contract with multiple telecommunications providers for
circuit diversity.
- Periodically review provider SLAs and test failover.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnrel04-bp02.html*

---

# HNREL04-BP03 Use dynamic routing for automatic failover

Implement dynamically routing for dedicated connections and IPSec
VPN connections using BGP to enable automatic load balancing and
failover across redundant links.

**Desired outcome:** Ensure seamless
failover and traffic distribution across all available network
paths, minimizing downtime and manual intervention.

**Level of risk exposed if this best practice
is not established:** High

**Benefits of establishing this best
practice:**

- Enables automatic failover in the event of a connection failure
- Balances network traffic for optimal performance
- Reduces manual intervention and operational overhead
- Increases resilience of hybrid connectivity

## Implementation guidance

- Use BGP for dynamic routing between on-premises and cloud
networks.
- Regularly validate routing and failover with controlled tests.

## Resources

- [BGP
Negotiation over AWS Site-to-Site VPN and Direct Connect:
Troubleshooting Strategies for Efficient Networking](https://repost.aws/articles/ARIKYhXEYyQQqtO2ulKERrbw/bgp-negotiation-over-aws-site-to-site-vpn-and-direct-connect-troubleshooting-strategies-for-efficient-networking)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnrel04-bp03.html*

---

# HNREL04-BP04 Provision sufficient network capacity

Provision enough network capacity so that the failure of a single
network connection does not overwhelm or degrade the remaining
redundant connections.

**Desired outcome:** Maintain
performance and service levels during network outages or planned
maintenance by ensuring available bandwidth meets business needs.

**Level of risk exposed if this best practice
is not established:** High

**Benefits of establishing this best
practice:**

- Avoids performance bottlenecks during failover
- Ensure sufficient capacity for critical workloads at all times
- Supports scalability and growth in hybrid environments
- Enhances customer and user experience

## Implementation guidance

- Analyze peak and average bandwidth requirements for hybrid
workloads.
- Size redundant connections so any one connection can handle
the full load if others fail.
- Monitor bandwidth usage and adjust capacity proactively.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnrel04-bp04.html*

---
