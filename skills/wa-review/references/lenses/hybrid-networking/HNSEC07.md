# HNSEC07 — Application security

**Pillar**: Security  
**Best Practices**: 1

---

# HNSEC07-BP01 Enforce End-to-End TLS Encryption

Protect data integrity and confidentiality by enforcing TLS
encryption for all application-layer communication, both within your
cloud environment and across hybrid connections to on-premises
systems. End-to-end TLS ensures that sensitive data is always
encrypted in transit, even if it traverses untrusted networks.

**Desired outcome:** Sensitive
application data remains protected from interception and tampering
at all times between end users, on-premises infrastructure, and
cloud workloads.

**Benefits of establishing this best
practice:**

- Ensures confidentiality and integrity of data in transit
- Meets regulatory and customer expectations for data protection
- Reduces risk of data breaches from network sniffing or
man-in-the-middle attacks
- Simplifies compliance reporting by demonstrating encryption
controls

## Implementation guidance

- Configure firewall rules to only allow HTTPS traffic and block
HTTP, ensuring all connections are encrypted.
- Select the strongest cipher suites that terminate TLS
connections.
- Managed and deployed public certificates. For example, you can
achieve this by using AWS Certificate Manager.
- Managed private PKI (Public Key Infrastructure) as needed. For
example, you can achieve this by using AWS Private Certificate Authority.

## Resources

- [AWS Certificate Manager (ACM)](https://docs.aws.amazon.com/acm/latest/userguide/acm-overview.html)
- [Encrypting
Data-at-Rest and Data-in-Transit](https://docs.aws.amazon.com/whitepapers/latest/logical-separation/encrypting-data-at-rest-and--in-transit.html)
- [Create
an HTTPS listener for your Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-https-listener.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnsec07-bp01.html*

---
