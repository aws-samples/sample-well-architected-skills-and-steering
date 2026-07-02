# TELCOOPS04 — IP verification

**Pillar**: Operational Excellence  
**Best Practices**: 1

---

# TELCOOPS04-BP01 Implement the Bring Your Own IP (BYOIP) address processes and associate the prefixes with the IPAM solution

The IPAM is a shared resource that can be provisioned in a single Region in a shared
services account. Pools of IP addresses can be shared using Resource Access Manager to
sub-accounts and specific Regions where telco assets reside. The BYOIP process allows the
telco to present their mobile subscribers to the Internet as members of their own network
instead of AWS. The size of the address pools should be forecasted with sufficient room
for growth. It is important to minimize the fragmentation of the address blocks and allow
for contiguous blocks for a given Region. This will simplify access controls such as
firewall rules, NACLs, and security groups. Finally, the bring your own ASN process should
be invoked to enable AWS to use BGP to represent the BYOIP pool to the Internet as owned
by the CSPs.

**Desired outcome:**

- Controlled IP address representation.
- Maintained IP reputation.
- Efficient address pool management.
- Proper ASN association.
- Optimized address utilization.
- Clear ownership documentation.

**Common anti-patterns:**

- Uncontrolled address advertising.
- Poor address pool planning.
- Missing ASN documentation.
- Fragmented address spaces.
- Inefficient address allocation.
- No address forecasting.
- Inconsistent routing policies.

**Level of risk if the best practice is not established:** High

## Implementation guidance

Design a comprehensive BYOIP implementation strategy that maintains control over IP
address representation while maintaining proper routing and advertisement. Establish a
detailed IP address management plan that includes address pool allocation, subnet design, and
forecasting mechanisms to support future growth without fragmentation. Implement robust BGP
routing policies and ASN configurations that maintain proper route advertisement while
maintaining optimal path selection and failover capabilities. Create detailed documentation
and operational procedures for managing IP address assignments, including regular audits of
address utilization and routing effectiveness to maintain the integrity of your network
addressing scheme.

### Implementation steps

- Use Amazon VPC IPAM for address pool management and AWS Resource Groups for IP address organization.
- Configure AWS Global Accelerator for IP address advertising and Amazon Route 53 for DNS management.
- Set up AWS Direct Connect for BGP routing and AWS Transit Gateway for route propagation.
- Deploy Amazon VPC IPAM for BYOIP address management and AWS Network Manager for network
visibility.
- Implement AWS Systems Manager for operational tasks and Amazon CloudWatch for IP address monitoring.

## Resources

**Key AWS services:**

- [Use VPC IP Address Manager to manage subnet CIDRs](https://aws.amazon.com/blogs/networking-and-content-delivery/use-vpc-ip-address-manager-to-manage-subnet-cidrs/)
- [AWS Direct Connect](https://aws.amazon.com/directconnect/)
- [Amazon Route 53](https://aws.amazon.com/route53/)
- [AWS Transit Gateway](https://aws.amazon.com/transit-gateway/)
- [AWS Network Manager](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-network-manager.html)
- [AWS Global Accelerator](https://aws.amazon.com/global-accelerator/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/telco-lens/telcoops04-bp01.html*

---
