# TELCOOPS07 — Geographical redundancy

**Pillar**: Operational Excellence  
**Best Practices**: 1

---

# TELCOOPS07-BP01 Design architecture patterns that maximize redundancy within available geographical constraints

For telco CSPs requiring 200 or more kilometers of geo-redundancy while maintaining in-country data residency,
it is essential to design cloud-based architectural solutions within available geographical
constraints. This may include leveraging available Availability Zones, Local Zones, or Wavelength
Zones where available, implementing hybrid architectures, or working with cloud providers to
understand future infrastructure expansion plans. The solution should balance regulatory
requirements with disaster recovery needs while maintaining required service levels.

**Desired outcome:**

- Optimal geographical redundancy.
- Adherence with data residency.
- Resilient architecture design.
- Efficient disaster recovery.
- Maintained service levels.
- Balanced resource distribution.

**Common anti-patterns:**

- Single region deployments.
- Insufficient separation distance.
- Non-compatible data placement.
- Poor failover planning.
- Missing redundancy testing.
- Inadequate backup strategies.
- Unclear recovery procedures.

**Level of risk exposed if this best practice is not established:**
High

## Implementation guidance

Develop architectural solutions that optimize geographical redundancy while adhering to
data residency requirements and regulatory constraints. Create detailed mapping of available
infrastructure options, including primary locations, disaster recovery sites, and edge
locations, to design optimal redundancy patterns that meet separation requirements. Implement
robust data replication and synchronization mechanisms that maintain consistency across
geographical locations while minimizing latency and bandwidth usage. Establish comprehensive
failover procedures and regular testing protocols to validate the effectiveness of
geographical redundancy implementations, verifying that service levels are maintained during
both planned and unplanned events.

### Implementation steps

- Use AWS Local Zones and Wavelength for edge presence and AWS Global Infrastructure for
Region or zone selection based on regulatory requirements.
- Implement AWS Transit Gateway for inter-region connectivity and AWS Global Accelerator for intelligent
traffic routing.
- Deploy AWS CloudFormation StackSets for multi-Region deployment and Amazon Route 53 for DNS-based
failover.
- Use AWS Fault Injection Service for disaster recovery testing and AWS Systems Manager Automation for failover
procedures.
- Configure AWS Network Manager for global network visibility and Amazon CloudWatch for
cross-Region monitoring.

## Resources

**Key AWS services:**

- [AWS Local
Zones](https://aws.amazon.com/about-aws/global-infrastructure/localzones/)
- [AWS Wavelength](https://aws.amazon.com/wavelength/)
- [Amazon Route 53](https://aws.amazon.com/route53/)
- [AWS Global Accelerator](https://aws.amazon.com/global-accelerator/)
- [AWS Transit Gateway](https://aws.amazon.com/transit-gateway/)
- [AWS Site-to-Site VPN](https://aws.amazon.com/vpn/site-to-site-vpn/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/telco-lens/telcoops07-bp01.html*

---
