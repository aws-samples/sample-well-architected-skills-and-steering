# HNSEC01 — Security foundations

**Pillar**: Security  
**Best Practices**: 3

---

# HNSEC01-BP01 Implement network segmentation and least-privilege access control

Segment your hybrid network using accounts, cloud networks, and
on-premises controls to isolate regulated workloads. Enforce
least-privilege connectivity by restricting traffic with network
access controls.

**Desired outcome:** Sensitive
workloads and data are isolated, with only authorized access
allowed, reducing compliance scope and limiting potential exposure.

**Level of risk exposed if this best practice
is not established:** High

**Benefits of establishing this best
practice:**

- Reduces compliance audit complexity and risk
- Minimizes lateral movement and impact of security incidents
- Aligns with regulatory requirements for network isolation
- Enables focused monitoring and incident response

## Implementation guidance

- Create separate accounts for different workloads (for example,
production, development, and regulated environments). For example,
you can achieve this using service such as AWS Organizations.
- Design isolated networks for sensitive workloads and segment
further using services such as Amazon VPC.
- Control network traffic access using services such as AWS
security groups to tightly control allowed traffic at the
instance level or use network access control lists for
subnet-level control.
- Configure route tables to enforce segmentation, such as using
AWS Transit Gateway route tables or AWS Cloud WAN segments.
- Regularly review and update access control for least-privilege
access.

## Resources

- [Best
practices for a multi-account environment](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_best-practices.html)
- [Ensure
internetwork traffic privacy in Amazon VPC](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Security.html)
- [Transit
Gateway Segmentation](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-vpc-attachments.html)
- [AWS Cloud WAN Segment](https://docs.aws.amazon.com/network-manager/latest/cloudwan/cloudwan-policy-segments.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnsec01-bp01.html*

---

# HNSEC01-BP02 Implement encryption in transit

Encryption in transit is essential for protecting data
confidentiality as traffic moves between on-premises networks and
cloud environments. All sensitive data traversing untrusted networks
should be encrypted using strong protocols like TLS or IPsec.

**Desired outcome:** All sensitive
data is protected during transmission, meeting regulatory mandates
for confidentiality and data integrity.

**Level of risk exposed if this best practice
is not established:** High

**Benefits of establishing this best
practice:**

- Ensures confidentiality and integrity of sensitive data
- Meets requirements in regulations such as HIPAA, GDPR, and PCI
DSS
- Reduces risk of breaches and compliance penalties
- Build customer and auditor trust

## Implementation guidance

- Establish encrypted connections between cloud and on-premises
environments.

For example, you can use services such as AWS Site-to-Site VPN
and AWS Direct Connect with MACsec.
- Enforce HTTPS/TLS for all application traffic between cloud
and on-premises environments.
- Manage and rotate encryption keys according to compliance
requirements.

## Resources

- [Encryption
in AWS Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/encryption-in-transit.html)
- [AWS Site-to-Site VPN](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html)
- [Choosing
an AWS cryptography service](https://docs.aws.amazon.com/decision-guides/latest/cryptography-on-aws-how-to-choose/guide.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnsec01-bp02.html*

---

# HNSEC01-BP03 Implement continuous logging

Continuous logging provides real-time visibility across on-premises
and cloud infrastructures. Implementing comprehensive logging
mechanisms enables teams to quickly detect anomalies, troubleshoot
connectivity issues, and maintain a consistent audit trail for
security compliance.

**Desired outcome:** Achieve
continuous visibility, reduce mean time to resolution during
incidents, and automated enforcement of compliance configurations.

**Benefits of establishing this best
practice:**

- Enables prompt incident detection and response
- Provides clear audit trails for compliance
- Ensures ongoing alignment with regulatory standards
- Reduces manual compliance effort

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

- Capture cloud environment API activities using services such
as AWS CloudTrail.
- Enable flow logs for network visibility using services such as
VPC Flow Logs and Transit Gateway Flow Logs.

## Resources

- [AWS services for logging and monitoring](https://docs.aws.amazon.com/prescriptive-guidance/latest/logging-monitoring-for-application-owners/aws-services-logging-monitoring.html)
- [AWS Transit Gateway Flow Logs](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-flow-logs.html)
- [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html)
- [Logging
IP traffic using VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnsec01-bp03.html*

---
