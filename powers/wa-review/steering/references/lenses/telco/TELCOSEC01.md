# TELCOSEC01 — Security foundations

**Pillar**: Security  
**Best Practices**: 2

---

# TELCOSEC01-BP01 Follow the industry standards and local regulations to host telecom networks in the cloud, demonstrating a security commitment

When operating a telecommunications network in a cloud environment, it is crucial to comply
with relevant industry specifications and local regulatory requirements. This includes adhering
to standards set forth by leading telecom standardization bodies such as the 3rd Generation
Partnership Project (3GPP), which develops technical specifications for mobile networks, and the
European Telecommunications Standards Institute (ETSI), which produces globally applicable
standards for information and communications technologies.

Additionally, the network operations must meet the regulations enforced by authorities like
the Federal Communications Commission (FCC) in the United States and the European Union's
Electronic Communications Code. By aligning with these industry specifications and local laws,
the organization demonstrates a strong commitment to security and building trust with customers.

Adhering to established standards and regulations verifies the cloud-based
telecommunications network functions reliably and safeguards sensitive customer data. This
approach fosters lasting relationships with the customer base through transparent, secure, and
well-regulated operations.

## Implementation guidance

Establish a comprehensive security hardening strategy that protects your AWS
infrastructure through multi-layered defense mechanisms and continuous monitoring. Design a
robust security architecture that encompasses identity management, network segmentation,
encryption protocols, and vulnerability management while maintaining operational efficiency.
Implement centralized logging and monitoring capabilities that provide visibility across the
layers of your infrastructure, enabling rapid detection and response to security incidents.
Create detailed security policies and operational procedures that enforce least privilege
access, automate checks, and maintain audit trails for configuration changes to verify the
integrity and resilience of your cloud environment.

### Implementation steps

- Use Amazon Security Lake for centralized logging.
- Deploy AWS Config for configuration tracking.
- Implement Amazon CloudWatch for monitoring and alerting.
- Enable AWS CloudTrail for API activity logging.
- Configure AWS IAM Identity Center for authentication.
- Set up AWS IAM for role-based access control.
- Deploy AWS Secrets Manager for credential management.
- Enable MFA for privileged accounts.
- Design Amazon VPC architecture for network isolation.
- Configure AWS Transit Gateway for traffic management.
- Implement AWS Network Firewall for traffic filtering.
- Set up security groups and NACLs for micro-segmentation.
- Deploy AWS KMS for key management.
- Configure AWS Certificate Manager for TLS certificates.
- Implement AWS CloudHSM for hardware security modules.
- Enable encryption at rest for data stores.
- Implement AWS Systems Manager for patch management.
- Deploy Amazon Inspector for vulnerability scanning.
- Configure AWS Security Hub CSPM for security posture monitoring.
- Establish automated remediation workflows.

For more detail, see [Enhancing telecom security with
AWS](https://aws.amazon.com/blogs/security/enhancing-telecom-security-with-aws/).

## Resources

**Related documents:**

- [Enhancing telecom security with AWS](https://aws.amazon.com/blogs/security/enhancing-telecom-security-with-aws/)

**Key AWS services:**

- [AWS Key Management Service (KMS)](https://aws.amazon.com/kms/)
- [Amazon VPC](https://aws.amazon.com/vpc/)
- [AWS IAM](https://aws.amazon.com/iam/)
- [AWS CloudHSM](https://aws.amazon.com/cloudhsm/)
- [AWS CloudTrail](https://aws.amazon.com/cloudtrail/)
- [AWS Config](https://aws.amazon.com/config/)
- [AWS Systems Manager](https://aws.amazon.com/systems-manager/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/telco-lens/telcosec01-bp01.html*

---

# TELCOSEC01-BP02 Encrypt data at-rest and sensitive traffic (control plane, data plane) using secure VPNs and custom encryption keys

Due to regulatory requirements, the CSPs often need to apply
additional encryption to traffic that is not already secured by the underlying transport or
application protocols. Both control plane traffic, such as Diameter signaling, and data plane
traffic, like voice or RTP, require the use of encrypted virtual private networks (VPNs), most
commonly IPsec. It is crucial for CSPs to evaluate their regulatory landscape and establish a
framework to identify and label the traffic and data that needs to be encrypted in transit as
well as at rest, using customer-owned encryption keys.

The data in-use is protected by the
underlying CPU architecture and features like AMD SEV-SNP, Intel TME, and Graviton Memory
Encryption. However, these security measures come with additional costs and limitations, such as
restrictions on packets per second (PPS) per flow (number of IPsec tunnels), PPS per instance
(lack of equal-cost multi-path routing after reaching the largest single-slot capacity),
complexity, and vendor dependencies.

**Desired outcome:**

- Verify sensitive telco network traffic, including control plane and data plane, is
encrypted using secure VPN protocols like IPsec.
- Implement a comprehensive data encryption strategy to protect data in transit and
at rest using customer-managed encryption keys.
- Fulfill regulatory requirements for data protection and secure communications in the
telco industry.
- Maintain the confidentiality and integrity of critical telco network data and signaling
traffic, even when traversing the public cloud infrastructure.
- Provide visibility and control over the encryption keys and algorithms used to secure
the telco workloads.

**Level of risk exposed if this best practice is not established:** High

## Implementation guidance

Implement a secure, encrypted communication framework for control and data plane traffic
comply with industry standards and regulations. Leverage built-in features for key management,
high availability, and automatic failover. Utilize a centralized key management service to
generate, manage, and rotate encryption keys for securing data in-transit and at-rest across
various systems and services. Verify comprehensive auditing and monitoring of encryption and
key management activities to maintain adherence and provide detailed reporting.

### Implementation steps

- Implement VPN-based encryption for control and data plane traffic:

Configure AWS managed VPN solutions, such as Site-to-Site VPN, to establish secure IPsec
tunnels for control and data plane communications.
- Use the built-in features of these services for automatic key management,
tunnel failover, and high availability.
- Verify the VPN configurations comply with industry standards and regulations
for secure network communications.

- Encrypt data in-transit using custom keys:

Use AWS Key Management Service to generate and manage the encryption keys used to
secure data in-transit.
- Integrate KMS with other AWS services, such as Amazon S3, Amazon EBS, and Amazon RDS, to
transparently encrypt data flowing through these services.
- Implement a key rotation strategy to maintain the cryptographic strength of the
encryption keys over time.

- Encrypt data at rest using custom keys:

Configure AWS services handling telco data, such as Amazon S3, Amazon EBS, and Amazon RDS,
to use customer-managed encryption keys from KMS.
- Verify that sensitive telco data, including logs, metrics, and configuration
files, is encrypted at rest using the custom encryption keys.
- Use KMS key policies to control access and usage of the encryption keys,
aligned with the principle of least privilege.

- Implement key management and rotation:

Establish key management processes and procedures for the creation,
distribution, and rotation of the customer-managed encryption keys.
- Automate key rotation using AWS Lambda functions or AWS Systems Manager, verifying that
keys are updated on a regular basis.
- Integrate the key management processes with the overall security operations and
incident response procedures.

- Maintain audit trails:

Use AWS CloudTrail to create comprehensive audit trails of key management and
data encryption activities.
- Configure AWS Config to continuously monitor the configuration of the encryption
services and report on deviations from the desired state.
- Integrate the encryption and key management data with the organization's
security information and event management (SIEM) system for advanced analytics and
reporting.

## Resources

**Key AWS services:**

- [Site-to-Site VPN](https://aws.amazon.com/vpn/)
- [AWS Direct Connect](https://aws.amazon.com/directconnect/)
- [AWS Key Management Service (KMS)](https://aws.amazon.com/kms/)
- [Amazon S3](https://aws.amazon.com/s3/)
- [Amazon EBS](https://aws.amazon.com/ebs/)
- [Amazon RDS](https://aws.amazon.com/rds/)
- [AWS CloudTrail](https://aws.amazon.com/cloudtrail/)
- [AWS Config](https://aws.amazon.com/config/)
- [AWS Lambda](https://aws.amazon.com/lambda/)
- [AWS Systems Manager](https://aws.amazon.com/systems-manager/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/telco-lens/telcosec01-bp02.html*

---
