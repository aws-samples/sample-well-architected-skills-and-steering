# HNSEC04 — Infrastructure protection

**Pillar**: Security  
**Best Practices**: 5

---

# HNSEC04-BP01 Control access to network resources

Comprehensive network access control applied across both on-premises
and cloud environments to create a unified security posture that
addresses the unique challenges of hybrid infrastructures while
maintaining compliance with regulatory requirements.

**Desired outcome:** Protect hybrid
network resources by controlling traffic from on-premises and cloud
environments.

**Level of risk exposed if this best practice
is not established:** High

**Benefits of establishing this best
practice:**

- Restrict network access to only approved sources
- Minimizes risk of unauthorized or malicious traffic
- Enables granular, instance-level security controls

## Implementation guidance

- Define least-privilege inbound and outbound rules matching
only approved network prefixes.
- Regularly review and update rules for accuracy and compliance.

## Resources

- [Control
traffic to your AWS resources using security groups](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html)
- [Control
subnet traffic with network access control lists](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnsec04-bp01.html*

---

# HNSEC04-BP02 Implement routing controls for network segments

Implementing routing controls for network segments involves
strategically managing traffic flow between different parts of your
network infrastructure. This includes setting up route tables to
direct traffic based on security policies. These controls should
enforce the principle of least privilege, ensuring network
components can only communicate with authorized segments.

**Desired outcome:** Enable
centralized, flexible, and secure traffic routing between cloud and
on-premises networks.

**Level of risk exposed if this best practice
is not established:** High

**Benefits of establishing this best
practice:**

- Provides centralized control of network paths
- Allows for segmentation and isolation using null routes
- Prevents unauthorized or misrouted hybrid traffic

## Implementation guidance

- Design route tables to segment environments and block
unnecessary paths.
- Use null routes to block specific destinations when needed.
- Periodically review and simulate route changes before
deployment.

## Resources

- [Transit
gateway route tables in AWS Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-route-tables.html)
- [Core
network policy versions in AWS Cloud WAN](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-create-policy-version.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnsec04-bp02.html*

---

# HNSEC04-BP03 Implement network traffic security inspection

Network traffic security inspection provides a layered security
approach to ensure traffic between your cloud and on-premises
resources is properly monitored and protected against threats.

**Desired outcome:** Deploy
inspection and security enforcement on ingress and egress network
paths as needed.

**Level of risk exposed if this best practice
is not established:** High

**Benefits of establishing this best
practice:**

- Enables deep packet inspection
- Provides scalable firewall for hybrid network traffic
- Enables advanced rule sets for protocol, domain, and threat
filtering
- Simplifies compliance with perimeter defense requirements

## Implementation guidance

- Route traffic through the firewall appliances
- Define and maintain firewall rule groups for hybrid traffic.
- Monitor firewall activity and adapt rules as threats evolve.

## Resources

- [Gateway
Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/gateway/introduction.html)
- [Centralized Traffic Inspection with Gateway Load Balancer on AWS](https://aws.amazon.com/blogs/apn/centralized-traffic-inspection-with-gateway-load-balancer-on-aws/)
- [AWS Network Firewall Documentation](https://docs.aws.amazon.com/network-firewall/latest/developerguide/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnsec04-bp03.html*

---

# HNSEC04-BP04 Implement DNS security controls

DNS security control protects against DNS threats such as data
exfiltration. You can create blocklists and allowlists to manage
which domains your resources can query through DNS.

**Desired outcome:** Prevent data
exfiltration and block malicious domains at the DNS layer in hybrid
networks.

**Level of risk exposed if this best practice
is not established:** Medium

**Benefits of establishing this best
practice:**

- Blocks DNS-based attacks and data exfiltration
- Provides centralized control over DNS traffic
- Enables logging and reporting for compliance

## Implementation guidance

- Define DNS firewall rule groups for blocklists and allowlists.
- Associate DNS firewall rules with relevant networks.
- Monitor DNS queries and refine rules based on findings.

## Resources

- [How
Resolver DNS Firewall works](https://docs.aws.amazon.com/Route%C2%A053/latest/DeveloperGuide/resolver-dns-firewall-overview.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnsec04-bp04.html*

---

# HNSEC04-BP05 Allow only authorized personnel access to on-premises infrastructure

Ensure that only authorized personnel have physical access to your
on-premises networking infrastructure, such as data centers, server
rooms, and network equipment. Implement strict access controls,
logging, and monitoring to protect against unauthorized entry and
physical tampering.

**Desired outcome:** Prevent
unauthorized physical access and tampering with critical hybrid
network resources, supporting a robust security posture across both
cloud and on-premises environments.

**Level of risk exposed if this best practice
is not established:** High

**Benefits of establishing this best
practice:**

- Reduces risk of physical compromise or sabotage of network
infrastructure
- Supports regulatory compliance and audit requirements
- Deters insider threats and unauthorized activity
- Complement logical cloud security controls with physical
safeguards

## Implementation guidance

- Implement access control systems (for example, keycards and
biometrics) for data center and server room entry.
- Maintain visitor logs and conduct background checks for
authorized personnel.
- Use surveillance cameras and alarms to monitor critical
physical locations.
- Conduct regular audits and reviews of physical access records.
- Establish clear procedures for visitor access and equipment
removal or servicing.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnsec04-bp05.html*

---
