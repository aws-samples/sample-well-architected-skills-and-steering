# HNCOST03 — Cost-effective resources

**Pillar**: Cost Optimization  
**Best Practices**: 1

---

# HNCOST03-BP01 Implement tiered connectivity based on workload requirements

Hybrid networking connectivity must balance performance,
reliability, and cost. Workloads with varying requirements for
throughput, latency, and uptime should leverage different
connectivity solutions. For example, non-critical workloads (for
example, development or testing) can use cost-effective
internet-based VPNs, while mission-critical production workloads may
require dedicated connections like AWS Direct Connect. A tiered
approach ensures you only pay for the level of connectivity your
workloads actually need.

**Desired outcome:** Cost savings
through workload-aligned connectivity, with no overpayment for
unnecessary bandwidth or redundancy.

**Level of risk exposed if this best practice
is not established:** Medium

**Benefits of establishing this best
practice:**

- Reduces costs for non-critical workloads
- Ensures high performance for production workloads
- Simplifies scaling as requirements evolve

## Implementation guidance

- Use IPSec VPN connections for non-mission critical workloads
- Use dedicated connections for production workloads
- Scale from IPSec VPN connections in testing phase to dedicated
connections after bandwidth requirements are defined
- Use direct connectivity to single cloud network connectivity
to avoid additional cloud transit costs, For example, you can
use Direct Connect private VIF to connect directly to VPC.
- Use cloud transit connectivity to connect to multiple cloud
networks. For example, you can use Direct Connect transit VIF
to connect to Transit Gateway for VPCs in the same region, or
Cloud WAN core network for VPCs in multiple regions

## Resources

- [Site-to-Site VPN
pricing](https://aws.amazon.com/vpn/pricing/)
- [AWS Direct Connect Pricing](https://aws.amazon.com/directconnect/pricing/)
- [AWS Transit Gateway Pricing](https://aws.amazon.com/transit-gateway/pricing/)
- [AWS Cloud WAN Pricing](https://aws.amazon.com/cloud-wan/pricing/)
- [Hybrid
Connectivity](https://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/hybrid-connectivity.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hncost03-bp01.html*

---
