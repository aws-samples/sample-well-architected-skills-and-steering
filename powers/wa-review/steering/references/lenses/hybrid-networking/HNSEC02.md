# HNSEC02 — Identity and access management

**Pillar**: Security  
**Best Practices**: 5

---

# HNSEC02-BP01 Implement a landing zone

Implementing a landing zone establishes a standardized, secure
foundation for hybrid networking infrastructure. A landing zone
provides centralized identity and access management, standardized
security controls, governance mechanisms, network architecture, and
account structures that enable scalable growth while maintaining
compliance. By automating resource provisioning and implementing
guardrails from the start, organizations can avoid costly rework
later while accelerating their cloud adoption journey with
confidence, knowing they have established proper security boundaries
and operational efficiency from day one.

**Desired outcome:** Establish a
secure foundation for your hybrid networking environment with
consistent architecture and configuration controls.

**Level of risk exposed if this best practice
is not established:** High

**Benefits of establishing this best
practice:**

- Ensures consistent security and compliance across all accounts
- Automates account provisioning and governance
- Reduces operational overhead and human error
- Enables scalable and secure hybrid networking environment

## Implementation guidance

- Deploy a landing zone using services such as AWS Control Tower.
- Apply preventive and detective guardrails for governance and
compliance.
- Standardize account creation and management through Account
Factory.
- Monitor the landing zone using services such as AWS Control Tower dashboard and Security Hub CSPM.

## Resources

- [AWS Control Tower Landing Zone](https://docs.aws.amazon.com/controltower/latest/userguide/what-is-aws-control-tower.html)
- [AWS Control Tower Guardrails](https://docs.aws.amazon.com/audit-manager/latest/userguide/controltower.html)
- [Provision
and manage accounts with Account Factory](https://docs.aws.amazon.com/controltower/latest/userguide/account-factory.html)
- [AWS Control Tower Dashboard](https://docs.aws.amazon.com/controltower/latest/userguide/control-tower-dashboard.html)
- [AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnsec02-bp01.html*

---

# HNSEC02-BP02 Use a central networking account to host all hybrid networking resources

A central networking account makes it easier to manage network
infrastructure and control access to it. By consolidating networking
components in a centralized account, organizations gain improved
visibility across their entire network topology, reduce redundant
connections, streamline troubleshooting, and enable more efficient
scaling as business needs evolve. This centralized model also
supports separation of duties, allowing networking specialists to
maintain connectivity services while application teams focus on
their core responsibilities.

**Desired outcome:** Simplified and
consistent management, governance, and security for all hybrid
networking resources across your cloud environment.

**Level of risk exposed if this best practice
is not established:** High

**Benefits of establishing this best
practice:**

- Centralizes management of networking infrastructure
- Simplifies access controls and governance
- Reduces configuration errors and operational overhead
- Enables secure resource sharing across multiple accounts
- Facilitates compliance and auditability

## Implementation guidance

- Designate a dedicated account as your central networking
account within your landing zone or multi-account environment.
- Deploy shared networking resources in this central networking
account.
- Share networking resources with other accounts as needed. For
example, you can use
[AWS Resource Access Manager](https://docs.aws.amazon.com/ram/latest/userguide/what-is.html) to share resources.
- Control access to networking resources using service such as
AWS IAM and resource-based policies.

## Resources

- [Infrastructure
OU - Network account](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/network.html)
- [AWS Resource Access Manager](https://docs.aws.amazon.com/ram/latest/userguide/what-is.html)
- [Share
your VPC subnets with other accounts](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-sharing.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnsec02-bp02.html*

---

# HNSEC02-BP03 Implement least privilege access for hybrid network management

To implement least privilege, hybrid connectivity resources
management should be granted only to teams responsible for hybrid
connectivity. The teams should own circuits, dedicated connections,
and VPNs even though other teams depend on these shared networking
resources.

**Desired outcome:** Ensure that
hybrid connectivity resources are securely managed, access is
restricted to authorized personnel, and operational risk is
minimized by centralizing ownership and management.

**Level of risk exposed if this best practice
is not established:** High

**Benefits of establishing this best
practice:**

- Enforces least privilege and separation of duties
- Reduces risk of misconfiguration or unauthorized changes
- Improve governance and compliance
- Enables consistent operational practices and incident response
- Ensures accountability for networking and security controls

## Implementation guidance

- Assign responsibility for managing hybrid connectivity
resources, such as Direct Connect, VPN, Transit Gateway, to a
dedicated networking and security team.
- Restrict permissions so only approved networking and security
personnel can create, modify, or delete connectivity
resources.
- Separate development and operational responsibilities to
prevent developers from modifying shared networking
infrastructure.
- Establish standard operating procedures and change management
workflows for connectivity changes.
- Audit access and configuration change regularly. For example,
you can achieve this using AWS CloudTrail.

## Resources

- [Security
best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)
- [AWS Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html)
- [AWS Site-to-Site VPN](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html)
- [AWS Transit Gateway for Amazon VPC](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html)
- [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnsec02-bp03.html*

---

# HNSEC02-BP04 Limit access to networking APIs

Implement strict controls over network management interfaces and
APIs to prevent unauthorized access and changes to critical network
infrastructure. This includes limiting access based on identity,
role, and network location while maintaining comprehensive audit
trails of all management actions.

**Desired outcome:** Prevent
unauthorized access and modification of sensitive networking
resources by restricting API access to approved personnel and secure
locations.

**Level of risk exposed if this best practice
is not established:** High

**Benefits of establishing this best
practice:**

- Minimizes risk of accidental or malicious changes to critical
network resources
- Supports enforcement of least privilege and security boundaries
- Reduces attack surface and potential for misconfiguration
- Enables better auditability and compliance

## Implementation guidance

- Grant access to networking APIs only to authorized networking
teams or accounts. For example, you can achieve this using AWS
IAM policies and resource-based policies.
- Monitor and audit API call to sensitive networking services,
using services such as AWS CloudTrail.
- Regularly review permissions and restrict access on a
least-privilege basis.

## Resources

- [Controlling
Access to AWS Resources Using Policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html)
- [IAM
Policy Conditions for Source IP](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html#AvailableKeys)
- [AWS CloudTrail Documentation](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html)
- [Best
Practices for IAM Permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnsec02-bp04.html*

---

# HNSEC02-BP05 Tag networking resources for accountability and access control

Implementing consistent tagging for networking resources is
essential in hybrid environments to establish clear ownership,
enforce access controls, and ensure proper governance across cloud
and on-premises infrastructure. By applying standardized tags to
networking components, organizations can effectively track resource
ownership, control who can modify critical network configurations,
and enforce the principle of least privilege. These tags enable
granular access policies where permissions can be dynamically
granted based on tag values, creating a strong foundation for
identity and access management while providing the accountability
needed for security audits and compliance requirements.

**Desired outcome:** Enable resource
ownership, cost allocation, and fine-grained access control by
ensuring all networking resources are consistently and accurately
tagged.

**Level of risk exposed if this best practice
is not established:** Medium

**Benefits of establishing this best
practice:**

- Increases accountability and traceability of network resources
- Enables cost allocation and chargeback by business unit or
environment
- Facilitates automation, compliance, and operational reporting
- Supports fine-grained access control using tag-based policies

## Implementation guidance

- Establish a tagging strategy for all networking resources
- Enforce tagging standards and restrict actions on untagged
resources. For example, you can achieve this using AWS Organizations Service Control Policies (SCPs) or IAM policies.
- Apply tag-based access control to limit who can modify,
delete, or create specific networking resources.
- Monitor resource tagging compliance and automate remediation
where possible using service such as AWS Config rules.

## Resources

- [Tagging
AWS Resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html)
- [Guidance
for Tagging on AWS](https://aws.amazon.com/solutions/guidance/tagging-on-aws/)
- [Controlling
access to AWS resources using tags](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html)
- [Implement
AWS resource tagging strategy using AWS Tag Policies and
Service Control Policies (SCPs)](https://aws.amazon.com/blogs/mt/implement-aws-resource-tagging-strategy-using-aws-tag-policies-and-service-control-policies-scps/)
- [Implementing
and enforcing Tagging](https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/implementing-and-enforcing-tagging.html)
- [Best
Practices for Tagging AWS Resources](https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/tagging-best-practices.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnsec02-bp05.html*

---
