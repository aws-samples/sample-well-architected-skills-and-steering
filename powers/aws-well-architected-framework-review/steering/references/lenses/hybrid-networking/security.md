# Security

**Pillar**: Security  
**Questions**: 7

---

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

# HNSEC03 — Detection

**Pillar**: Security  
**Best Practices**: 2

---

# HNSEC03-BP01 Implement network traffic monitoring and threat detection

Monitor and implement an immediate response process that detects and
reacts to any suspicious or malicious activity. Continuously
monitoring workloads helps to identify security incidents faster. At
a minimum, the metadata of logs should be captured for hybrid
network connections with private connections.

**Desired outcome:** Detect
suspicious or unauthorized activity and improve security posture by
capturing and analyzing network traffic logs.

**Level of risk exposed if this best practice
is not established:** High

**Benefits of establishing this best
practice:**

- Enables early detection and response to security incidents
- Provides visibility into hybrid network activity
- Helps with forensic analysis and compliance reporting
- Reduces risk of undetected malicious activity

## Implementation guidance

- Enable flow logs on all relevant networks using services such
as VPC Flow Logs and Transit Gateway Flow Logs
- Enable continuous threat detection across network traffic and
accounts. For example, you can achieve this with Amazon GuardDuty.
- Review findings regularly and establish automated or manual
incident response processes.
- Store and analyze logs in a central location for correlation
and investigation.

## Resources

- [Logging
IP traffic using VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html)
- [AWS Transit Gateway Flow Logs](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-flow-logs.html)
- [Amazon GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html)
- [Centralized
Logging with OpenSearch](https://aws.amazon.com/solutions/implementations/centralized-logging-with-opensearch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnsec03-bp01.html*

---

# HNSEC03-BP02 Set up central logging and analytics

Establishing a centralized logging and analytics system is crucial
for comprehensive visibility, security monitoring, and operational
efficiency across both on-premises and cloud infrastructures. A
central logging solution enables organizations to collect, store,
analyze, and respond to events occurring throughout their
distributed network environments.

**Desired outcome:** Achieve
comprehensive visibility and efficient analysis across all
networking environments for rapid detection and troubleshooting.

**Level of risk exposed if this best practice
is not established:** High

**Benefits of establishing this best
practice:**

- Centralizes monitoring and log management
- Streamlines threat detection and operational insights
- Supports compliance and audit requirements
- Simplifies troubleshooting across hybrid environments

## Implementation guidance

- Aggregate logs from on-premises and cloud environments to a
centralized analytics platform.
- Implement dashboards and alerting for key performance and
security events.

## Resources

- [Centralized
Logging with
OpenSearch](https://aws.amazon.com/solutions/implementations/centralized-logging-with-opensearch/)
- [Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html)
- [Central
Logging and Analytics in Hybrid Environments](https://d1.awsstatic.com/architecture-diagrams/ArchitectureDiagrams/central-logging-and-analytics-in-hybrid-environments.pdf)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnsec03-bp02.html*

---

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

# HNSEC06 — Incident response

**Pillar**: Security  
**Best Practices**: 2

---

# HNSEC06-BP01 Monitor your environment for malicious behavior

Responding to any cyber incident requires the ability to detect
threats and establish a baseline for normal operations in a hybrid
environment. Continuously monitors your environment for malicious
behavior to protect your accounts and workloads.

**Desired outcome:** Quick detection
of malicious activity enables fast containment and limits the impact
of ransomware and other security incidents.

**Level of risk exposed if this best practice
is not established:** High

**Benefits of establishing this best
practice:**

- Early identification of threats and abnormal behaviors
- Reduces containment and remediation time
- Enhances overall security posture with automated, continuous
monitoring

## Implementation guidance

- Monitor flow logs, API activity, and DNS logs for threats,
such as using Amazon GuardDuty that monitors and reports
findings from these sources.
- Regularly review and baseline findings to distinguish normal
from abnormal activity.

## Resources

- [Amazon GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnsec06-bp01.html*

---

# HNSEC06-BP02 Automate incident response

Implement automated response capabilities to enhance incident
containment speed and reliability while reducing manual intervention
requirements. This approach ensures consistent execution of response
procedures while minimizing human error during critical security
events.

**Desired outcome:** Faster, more
reliable containment and recovery from incidents with reduced
operational burden.

**Level of risk exposed if this best practice
is not established:** High

**Benefits of establishing this best
practice:**

- Shortens response times and limits damage
- Reduces alert fatigue and manual workload
- Ensures consistent, repeatable incident handling

## Implementation guidance

- Automate incident response by configuring security findings
with response actions. For example, you can achieve this by
integrating AWS Security Hub CSPM findings with AWS Lambda for
automated actions.
- Test and tune automation playbooks in non-production
environments.

## Resources

- [Using
EventBridge for automated response and remediation PDF
RSS](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-cloudwatch-events.html)
- [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/automating-security-responses.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnsec06-bp02.html*

---

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

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
