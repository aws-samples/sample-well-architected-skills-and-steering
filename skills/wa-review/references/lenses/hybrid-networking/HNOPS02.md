# HNOPS02 — Prepare

**Pillar**: Operational Excellence  
**Best Practices**: 1

---

# HNOPS02-BP01 Use IP address management tool

Use IP Address Manager tool to automate workflows to efficiently
manage IP addresses. It helps to organize and monitor the IP address
space and automatically allocate CIDRs using specific business
rules.

**Desired outcome:**

- Organized and efficiently managed IP addressing scheme across
hybrid environments
- Get clear visibility, prevents overlapping addresses, and
supports scalable network growth.

**Level of risk exposed if this best practice
is not established:** High

**Benefits of establishing this best
practice:**

- Efficient route summarization, allowing organizations to
advertise larger CIDR blocks instead of individual prefixes.
- Clean network boundaries and facilitate easier security
management.
- Achieve better resource utilization through automated IP address
assignment, eliminating manual tracking processes and reducing
human errors.

## Implementation guidance

- Create a hierarchical structure of IP pools that align with
your organizational needs and geographical presence. For
example, you can use services such as
[Amazon VPC IPAM](https://docs.aws.amazon.com/vpc/latest/ipam/what-it-is-ipam.html).
- Establish clear policies for CIDR allocation, including
reserved ranges for specific purposes such as Amazon VPCs,
subnets, and on-premises networks.
- Implement workflows for IP address assignment, such as using
Amazon VPC IPAM allocation rules.

## Resources

- [Amazon VPC IP Address Manager Best Practices](https://aws.amazon.com/blogs/networking-and-content-delivery/amazon-vpc-ip-address-manager-best-practices/)
- [Managing
IP pools across VPCs and Regions using Amazon VPC IP Address
Manager](https://aws.amazon.com/blogs/networking-and-content-delivery/managing-ip-pools-across-vpcs-and-regions-using-amazon-vpc-ip-address-manager/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnops02-bp01.html*

---
