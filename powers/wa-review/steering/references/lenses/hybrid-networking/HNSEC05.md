# HNSEC05 — Data protection

**Pillar**: Security  
**Best Practices**: 3

---

# HNSEC05-BP01 Use IPSec VPN over Internet

For hybrid network connectivity over the internet, IPSec VPN
services can be used to create encrypted tunnels between cloud and
on-premises environments.

**Desired outcome:** Ensure that all
data transmitted between AWS and on-premises networks over the
internet is encrypted and protected from unauthorized access.

**Level of risk exposed if this best practice
is not established:** High

**Benefits of establishing this best
practice:**

- Provides encryption for data in transit
- Reduces risk of data interception or tampering over public
networks
- Supports compliance with security and privacy requirements
- Enables secure, flexible hybrid networking without dedicated
links

## Implementation guidance

- Establish IPSec VPN tunnels between your cloud and on-premises
network, such as using AWS Site-to-Site VPN.
- Configure VPN endpoints to enforce strong encryption and
authentication.
- Monitor tunnel health and activity.
- Ensure only approved subnets and IP ranges are routable over
the VPN.

## Resources

- [AWS Site-to-Site VPN](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html)
- [Get
started with AWS Site-to-Site VPN](https://docs.aws.amazon.com/vpn/latest/s2svpn/SetUpVPNConnections.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnsec05-bp01.html*

---

# HNSEC05-BP02 Use MACsec encryption for dedicated connections

Dedicated connections allow hybrid network connectivity over a
private network link. MACsec encrypts traffic at Layer 2 to securely
pass high bandwidth workloads between cloud and on-premises
infrastructure. It provides native, point-to-point encryption to
protect data communications. To use MACsec, both the dedicated
connection and your on-premises equipment must support it.

**Desired outcome:** Encrypt
high-speed data traffic between cloud and your data center to
protect sensitive workloads from interception or tampering.

**Level of risk exposed if this best practice
is not established:** High

**Benefits of establishing this best
practice:**

- Delivers encryption for high bandwidth connections
- Secures data in transit without sacrificing performance
- Enables compliance with industry and regulatory standards

## Implementation guidance

- Use dedicated connection links that support MACsec.
- Enable MACsec on both the dedicated connection port and your
on-premises network device.
- Regularly validate and monitor MACsec status and connection
health.

## Resources

- [MAC
Security in Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/MACsec.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnsec05-bp02.html*

---

# HNSEC05-BP03 Use application layer encryption

Applying TLS encryption at the application layer ensures data
confidentiality even when transmitted over untrusted networks. For
optimal security, use certificates for authentication where
available and ensure encryption requirements follow the latest
standards and best practices, allowing only secure protocols with
strong cipher suites that are regularly monitored and updated.

**Desired outcome:** Ensure that data
remains protected on lower-speed or hosted Direct Connect
connections.

**Level of risk exposed if this best practice
is not established:** High

**Benefits of establishing this best
practice:**

- Protects sensitive data regardless of Direct Connect speed or
type
- Enables flexibility with software or application-based
encryption
- Maintains compliance with security policies and data protection
requirements
- Ensures end-to-end encryptions for all workloads

## Implementation guidance

- For application-layer encryption, use TLS/SSL for all
sensitive communications.
- Use certificate-based authentication where possible.
- Periodically test and review encryption configurations and key
management.

## Resources

- [Encryption
in transit over external networks: AWS guidance for NYDFS and
beyond](https://aws.amazon.com/blogs/security/encryption-in-transit-over-external-networks-aws-guidance-for-nydfs-and-beyond/)
- [Hybrid
Connectivity AWS Whitepaper](https://docs.aws.amazon.com/whitepapers/latest/hybrid-connectivity/hybrid-connectivity.pdf).

*Source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnsec05-bp03.html*

---
