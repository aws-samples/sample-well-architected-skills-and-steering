# MIDASEC04 — Infrastructure protection

**Pillar**: Security  
**Best Practices**: 2

---

# MIDASEC04-BP01 Segment OT networks from IT systems

Establish clear segmentation between OT networks and IT systems to limit the scope of
impact and reduce risk of lateral movement between environments.

**Desired outcome:** OT systems are logically and physically
isolated from IT networks while enabling secure data flows.

**Benefits of establishing this best practice:** Reduces
propagation of malware, minimizes risk of compromise of safety-critical systems, and supports
compliance with industrial cybersecurity frameworks.

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

Implement logical segmentation using VPCs, subnets, routing controls, and edge
gateways. Verify that minimal and controlled data flows between domains.

### Implementation steps

- Design separate network segments for IT and OT environments using VPCs and
subnets.
- Deploy gateway services like AWS IoT Greengrass or AWS Transit Gateway to manage
traffic between zones.
- Apply network ACLs and security groups to limit access paths.
- Log and monitor all cross-boundary traffic using VPC Flow Logs and AWS Network Firewall.

## Resources

- [Secure data ingestion from OT to IT using AWS IoT SiteWise and AWS IoT Greengrass](https://aws.amazon.com/blogs/iot/secure-data-ingestion-from-ot-to-it-using-aws-iot-sitewise-and-iot-greengrass/)
- [Security in your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Security.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasec04-bp01.html*

---

# MIDASEC04-BP02 Use firewalls, perimeter networks, and dedicated network zones

Implement perimeter defenses such as firewalls, perimeter networks and dedicated network
zones to manage and secure traffic flows between cloud, IT, and OT systems.

**Desired outcome:** Traffic is filtered and restricted at each
trust boundary to enforce zero trust and layered defense.

**Benefits of establishing this best practice:** Helps improve
network security posture, prevent direct exposure of OT systems, and support layered
defense-in-depth architecture.

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

Deploy AWS Network Firewall, private subnets, and multi-tier perimeter network
architectures to filter and control inbound and outbound traffic.

### Implementation steps

- Deploy AWS Network Firewall or third-party appliances in VPCs.
- Create perimeter networks between public internet and sensitive workloads using
public and private subnet models.
- Enforce rule groups that restrict IPs, ports, and protocols.
- Continuously monitor and update firewall rules and network configurations.

## Resources

- [What is AWS Network Firewall?](https://docs.aws.amazon.com/network-firewall/latest/developerguide/what-is-aws-network-firewall.html)
- [Building a Scalable and Secure Multi-VPC AWS Network Infrastructure](https://aws.amazon.com/whitepapers/building-a-scalable-and-secure-multi-vpc-aws-network-infrastructure/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasec04-bp02.html*

---
