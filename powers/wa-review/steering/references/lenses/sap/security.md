# Security

**Pages**: 18

---

# Best Practice 5.1 – Define security roles and responsibilities

By defining the requirements to secure your SAP workloads, you can identify risks that
must be addressed and ensure that security-related roles and responsibilities are
appropriately assigned. In the suggestions, we discuss standards for AWS, SAP, and any
service providers to form a baseline on which you can build your security strategy.

**Suggestion 5.1.1 - Understand the AWS shared responsibility
model**

AWS is responsible for security of the cloud and you, as the customer, are
responsible for security in the cloud. Be aware of and understand the following resources:

- AWS Documentation: [AWS Shared
Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/)
- AWS Documentation:[AWS Response to Abuse and Compromise](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/abuse-and-compromise.html)
- AWS Documentation: [AWS Acceptable Use
Policy](https://aws.amazon.com/aup/)

Understand the division of responsibilities between you and your partners in the
context of the AWS shared responsibility model

**Suggestion 5.1.2 - Understand the security foundations across SAP
and AWS including compliance certificates, reports, and attestations**

Understand the security standards and compliance certifications that SAP and AWS
support. Determine which are relevant to your industry and country (for example, PCI-DSS,
GDPR, HIPAA). These controls can help strengthen your own compliance and certification
programs, and reduce the effort required to meet your security standards.

Refer to the SAP and AWS documentation for more details:

- AWS Documentation: [AWS
Compliance](https://aws.amazon.com/compliance)
- AWS Documentation: [AWS Compliance Center](https://aws.amazon.com/financial-services/security-compliance/compliance-center/)
- AWS Documentation: [Compliance Programs](https://aws.amazon.com/compliance/programs/)
- AWS Documentation: [Compliance Services in
Scope](https://aws.amazon.com/compliance/services-in-scope/)
- SAP Documentation: [Trust
Center](https://www.sap.com/about/trust-center.html)

**Suggestion 5.1.3 - Assess the security foundation of the service
providers that support your SAP workload**

If you are dependent on third-party organizations to manage all or part of your SAP
workload, assess the ability of the third party to meet the required security controls.
This includes the legal and regulatory requirements mandated by your enterprise.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-5-1.html*

---

# Best Practice 5.2 – Classify the data within your SAP workloads

Data sensitivity can impact the controls required to mitigate risk. AWS suggests
referring to standard frameworks within your industry or organization and adopting these
to classify your SAP workloads and the data contained within them.

**Suggestion 5.2.1 - Determine data classification and handling
requirements**

Identify any data classification frameworks already in place in your organization.
These frameworks can help you to categorize data based on the sensitivity of information,
such as data that must be safeguarded for confidentiality, integrity, and availability.
[Standard classification models](https://docs.aws.amazon.com/whitepapers/latest/data-classification/data-classification-models-and-schemes.html) exist,
for example, the US Information Categorization Scheme, that may be customizable based on your
industry, business, or IT requirements.

Understand how data should be handled according to the guidelines appropriate for the
classification. This includes specific security controls related to standards or
regulatory requirements, such as PCI-DSS or GDPR, and common privacy considerations,
such as handling personal identifiable information (PII). The following documents
provide additional information:

- AWS Documentation: [Data Classification: Secure Cloud Adoption Whitepaper](https://docs.aws.amazon.com/whitepapers/latest/data-classification/data-classification-overview.html)
- AWS Documentation: [General Data Protection Regulation (GDPR) Center](https://aws.amazon.com/compliance/gdpr-center/)
- [NIST
Security and Privacy Controls for Information Systems and Organizations](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final)
- [ISO/IEC 27001:2013 FAQs](https://aws.amazon.com/compliance/iso-27001-faqs/)
- Well-Architected Framework [Security]: [Data Protection](https://docs.aws.amazon.com/wellarchitected/latest/framework/a-data-protection.html)

**Suggestion 5.2.2 - Identify SAP data types with specific handling
rules**

Based on the business processes supported by your SAP system, there may be
requirements for the handling and storage of data. Familiarize yourself with the guidance
for your location and industry. SAP examples may include:

- Assess whether a digital payments add-on is necessary to protect stored
cardholder data and ensure PCI compliance.
- Assess HR data for data residency requirements, for example, some countries and
jurisdictions might require data to be stored within a specific geographical
location.
- Consider which data may need to be scrambled in non-production systems to obscure
sensitive data but maintain data integrity.

**Suggestion 5.2.3 - Classify all your workloads according to the
defined framework**

Classify your SAP systems according to their business usage and the existence of
critical data types. Transactional systems such as SAP ERP are more likely to contain
sensitive data than analytical systems such as SAP BW or management systems such as
Solution Manager, although this should be validated by functional and security
experts.

Additionally, assess whether the same controls apply to non-production workloads. For
example, do non-production workloads include production data and therefore must they
adhere to the same security controls?

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-5-2.html*

---

# Best Practice 5.3 – Assess the need for specific security controls for your SAP workloads

Based on the data classification, evaluate any controls that can help you to meet the
standards and requirements established in the previous best practices. These include
location, AWS account strategy and scrambling requirements for non-production SAP
workloads.

**Suggestion 5.3.1 - Assess any geographical location
requirements**

Your SAP workloads might be deployed in one or many AWS Regions and Availability
Zones (AZs). Each AWS Region consists of multiple, isolated, and physically separate AZs
within a geographic area. In addition to evaluating the Region for latency, resilience,
and sustainability specifications,
you should consider whether security and compliance requirements can be met. Examples of
isolated Regions with specific operating jurisdictions include:

- AWS GovCloud (US) - designed to host sensitive data, regulated workloads, and
address the most stringent US government security and compliance requirements
- Amazon Web Services in China - AWS has collaborated with local partners to
ensure China’s legal and regulatory requirements are met

Some industries and countries will have data residency requirements that all customer
content processed and stored in an IT system must remain within a specific country’s
borders.

- AWS Documentation: [AWS Security blogs for data residency](https://aws.amazon.com/blogs/security/tag/data-residency/)

Before deciding on a location, review the availability of services for that AWS
Region to ensure that the services that you require are available.

- AWS Documentation: [AWS Regional Services](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/)

**Suggestion 5.3.2 - Determine how your SAP workloads align with your
AWS account strategy and landing zone**

An important consideration when running SAP workloads in AWS is the AWS account
strategy and landing zone approach that you adopt to meet your organization’s security
controls. You should consider separating SAP from non-SAP workloads and having production workloads in
a separate account from non-production workloads.

Understand your organization’s existing AWS account management strategy, including
the use of the AWS Organizations and AWS Control Tower. Consider isolating security and log capabilities
into an isolated account. Refer to the following for additional details:

- Well-Architected Framework [Security]: [AWS Account Management and Separation](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/aws-account-management-and-separation.html)
- AWS Documentation: [Establishing your best practice AWS environment](https://aws.amazon.com/organizations/getting-started/best-practices/)
- AWS Documentation: [Organizing Your AWS Environment Using Multiple Accounts](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.html)
- AWS Documentation:[AWS multi-account strategy for your AWS Control Tower landing zone](https://docs.aws.amazon.com/controltower/latest/userguide/aws-multi-account-landing-zone.html)

The account strategy you adopt will also affect the network configuration within
AWS. As part of determining the appropriate AWS account strategy for your SAP
workloads you should consider the following:

- Requirements for cross-account access, such as the need for setting up [VPC
Peering](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-peering.html) or [Transit
Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-transit-gateways.html) to allow communication between non-production and production
systems. For example, the movement of SAP transports through your landscape.
- Dependencies on shared services (such as directory management resources) and
network management components that are deployed in different AWS accounts from your
SAP workloads.
- In addition to the core security services, such as IAM and network controls,
consider how AWS managed security services can help achieve security goals or uplift
your security posture. AWS provides security services to assist with web application
firewalls, traffic auditing, DDOS protection, CVE management, configuration auditing,
and virus and threat detection.
- AWS Documentation: [AWS Foundational Security Best Practices Controls](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-standards-fsbp-controls.html)

**Suggestion 5.3.3 - Review the controls for data scrambling (if
applicable)**

Many SAP customers rely on copies of production data for testing purposes, including
regression and performance testing. If creating a copy of production data, decide which
controls you must add to ensure that your production data is protected from unintended
access and modifications.

Consider the following options:

- Traditional data scrambling mechanisms provided by SAP or third-party
providers
- The use of additional accounts or network controls to limit access during a copy
of production data
- Use of a non-production account with the same controls as production

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-5-3.html*

---

# Best Practice 5.4 – Create a strategy for managing security controls

Having evaluated business requirements based on data classification, create a strategy
that balances the security controls of your broader organization with the application
guides and open standards available. Take into consideration the implementation effort and
acknowledge risk.

**Suggestion 5.4.1 - Identify a matrix to assess risk**

A range of risk management frameworks are available for specific industries and
geographies. Understand the risk framework adopted by your organization and how this
applies to managing risks related to your SAP workloads.

- AWS Documentation: [Example Risk Matrix](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/governance.html)
- AWS Blog: [Scaling
a governance, risk, and compliance program for the cloud](https://aws.amazon.com/blogs/security/scaling-a-governance-risk-and-compliance-program-for-the-cloud/)
- [NIST Risk
Management Framework](https://www.nist.gov/cyberframework/risk-management-framework)

**Suggestion 5.4.2 - Evaluate security and compliance requirements
mandated by your organization**

Consult with your cloud center of excellence, legal team, compliance teams, and
managed service provider to understand their security baseline and how controls are
enforced. Evaluate whether all of these controls can easily be applied to your SAP
workload and identify areas that might require an exception, for example allow and deny
lists for AWS services, inbound and outbound traffic flow and access
restrictions.

**Suggestion 5.4.3 - Identify and agree on a process for
exceptions**

In some situations, software, business, or support requirements for SAP might require
you to deviate from the standard security patterns. Identify a process to agree and
document any exceptions with a change advisory board or security design authority and
reassess the process on a regular basis.

AWS Documentation: [Change Management in the Cloud](https://docs.aws.amazon.com/whitepapers/latest/change-management-in-the-cloud/change-management-in-the-cloud.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-5-4.html*

---

# Best Practice 6.1 – Ensure that security and auditing are built into the SAP network design

Protecting access to the network that hosts your SAP workloads is the first line of
defense against malicious activity. Evaluate your business requirements and the specific
SAP solution to determine the ports, protocols, and traffic patterns that need to be
enabled. Consider the security standards of your organization and the tools and patterns
available to simplify network design. Audit on a regular basis or as changes occur.

**Suggestion 6.1.1 – Understand network traffic flows for
SAP**

Start by understanding your traffic flows. Network traffic patterns for SAP workloads
can be categorized as inbound traffic, outbound traffic, and internal traffic. You should
identify whether the source and destination fall within your trusted network boundary to
assist with defining your rule sets.

In addition to known inbound traffic and outbound traffic flows such as user access
and interface connections, consider SAP-specific requirements, including connections to
SAP Support (via SAProuter) and SAP SaaS offerings that restrict access based on source IP
addresses.

For internal traffic, consider traffic between components and systems, as well as
AWS and shared services. Tools such as [VPC Flow
Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html) and [VPC Reachability Analyzer](https://docs.aws.amazon.com/vpc/latest/reachability/what-is-reachability-analyzer.html) can help you understand traffic flows into and out of
your Amazon VPC.

For more details, refer to the following information:

- AWS Documentation: [Attack surface reduction](https://docs.aws.amazon.com/whitepapers/latest/aws-best-practices-ddos-resiliency/attack-surface-reduction.html)
- SAP Documentation: [TCP/IP Ports for
All SAP Products](https://help.sap.com/viewer/ports)

**Suggestion 6.1.2 – Evaluate options to permit and restrict traffic
flows**

First, understand how you connect users and systems in your on-premises network to the
AWS account in which your SAP systems are running. This is covered in [Network-to-Amazon VPC connectivity options](https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/network-to-amazon-vpc-connectivity-options.html).

Two primary methods for controlling the flow of network traffic into and out of your
VPC include the use of [security
groups](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html) and [network
access control lists](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html) (network ACL). A security group acts as a virtual firewall
at the EC2 instance level to control inbound and outbound traffic and is stateful. A
network ACL is an optional layer of security for your VPC that acts as a firewall for
controlling traffic in and out of one or more subnets, and — unlike security groups — a
network ACL is stateless.

Also consider the dependencies of network components outside of your VPC. This can
include external network components provided by AWS such as CloudWatch endpoints.
This also can include internet hosted services such as software repositories for operating
system patches.

In addition to the standard options in AWS, SAP itself provides additional network
security options, including the use of the [SAProuter](https://support.sap.com/content/dam/support/en_us/library/ssp/tools/connectivity-tools/saprouter/SAProuter.pdf), the [SAP Web Dispatcher](https://help.sap.com/doc/7b5ec370728810148a4b1a83b0e91070/1610%20002/en-US/frameset.htm?488fe37933114e6fe10000000a421937.html), and SAP Gateway [network-based access control lists](https://help.sap.com/viewer/62b4de4187cb43668d15dac48fc00732/LATEST/en-US/d0a4956abd904c8d855ee9d368bc510b.html). These work in tandem with AWS services and
configurations to permit or restrict network access to SAP systems.

For more details, refer to the following information:

- SAP on AWS Blog: [VPC Subnet Zoning Patterns for SAP on AWS](https://aws.amazon.com/blogs/awsforsap/vpc-subnet-zoning-patterns-for-sap-on-aws/)
- Well-Architected Framework [Security]: [Infrastructure Protection – Protecting Networks](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/protecting-networks.html)
- Well-Architected Framework [Management and Governance Cloud Environment Guide]: [Network Connectivity](https://docs.aws.amazon.com/wellarchitected/latest/management-and-governance-guide/networkconnectivity.html)
- SAP Documentation: [Network and Communication Security](https://help.sap.com/viewer/621bb4e3951b4a8ca633ca7ed1c0aba2/LATEST/en-US/492f0050d5ac612fe10000000a44176d.html)

**Suggestion 6.1.3 – Use design guidelines and AWS tooling to
simplify network security**

SAP systems often have complex integration requirements, and the cloud offers
additional ways to simplify network security management. Consider the following
approaches:

- Avoid referring to individual IP addresses or IP ranges where possible to simplify
management.
- Use a standard set of SAP system numbers across all your SAP workloads to reduce
the range of network ports required.
- [AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/userguide/endpoint-services-overview.html) removes the requirement for outbound internet access from your
VPC to access AWS services such as Amazon S3 and CloudWatch. Where possible
and not mandated by business requirements, you can prevent SAP traffic to and from
these services from traversing the internet, routing all traffic through AWS
managed network components.
- Simplify security groups by the use of [VPC
Prefix Lists](https://docs.aws.amazon.com/vpc/latest/userguide/managed-prefix-lists.html) and/or [security group rules](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/security-group-rules.html) that reference other security groups rather than IP
address ranges.
- Use automation to create, update, and manage security groups to avoid
configuration drift.
- Consider the use of [AWS Firewall Manager](https://docs.aws.amazon.com/waf/latest/developerguide/what-is-aws-waf.html#fms-intro) to provide centralized management of security groups across VPCs
and AWS accounts.
- Consider the use of [SAProuter](https://support.sap.com/en/tools/connectivity-tools/saprouter.html), [SAP Web Dispatcher](https://help.sap.com/doc/7b5ec370728810148a4b1a83b0e91070/1610 002/en-US/frameset.htm?488fe37933114e6fe10000000a421937.html), and Elastic Load Balancing to obfuscate the entry
points to backend systems.
- Consider the use of multiple [SAP Internet Communication Manager (ICM)](https://help.sap.com/doc/d2ecfdfcaedc4e2ba46a99a6be7d5797/1610 002/en-US/frameset.htm#:~:text=The%20ICM%20is%20a%20component%20of%20the%20SAP%20NetWeaver%20Application%20Server.&text=The%20Internet%20Communication%20Manager%20ensures,processes%20requests%20from%20the%20Internet.) entry points to provide finer
grain access control.
- Consider [AWS Shield](https://aws.amazon.com/shield/), a managed
Distributed Denial of Service (DDoS) protection service, to safeguard applications
running on AWS. Use to protect public-facing SAP Fiori or API endpoints.
- Consider [AWS WAF](https://aws.amazon.com/waf/), a web
application firewall that helps protect your web applications or APIs against common web
exploits and bots that may affect availability, compromise security, or consume
excessive resources. Use to protect public-facing user interfaces and APIs, for example,
SAP Fiori applications.

For more details, refer to the following information:

- SAP Documentation: [Network-based Access Control Lists](https://help.sap.com/viewer/62b4de4187cb43668d15dac48fc00732/LATEST/en-US/d0a4956abd904c8d855ee9d368bc510b.html)
- SAP Documentation: [TCP/IP Ports
for All SAP Products](https://help.sap.com/viewer/ports)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-6-1.html*

---

# Best Practice 6.2 – Build and protect the operating system

Protecting the operating system underlying your SAP software reduces the possibility
that a malicious actor could gain unauthorized access to data within the SAP application,
impact software availability, or otherwise destabilize your mission-critical
implementation. Follow recommendations from SAP, the operating system vendor, the database
vendor, and AWS to help secure the operating system. Depending on your chosen SAP
solution and operating system, you may need to enable/disable services, set specific
kernel parameters, and apply different combinations of security patches. Consider how SAP
requirements align with those of your organization, and identify any conflicts.

**Suggestion 6.2.1 – Determine an approach for provisioning a secure
operating system**

An Amazon Machine Image (AMI) provides the information required to launch an EC2
instance. You should be confident that your AMIs are secure at the operating system level;
otherwise, security holes could be propagated to any number of instances as AMIs are
reused and updated over time.

AMIs can be either standard images from the operating system vendor or custom images
that you build yourself. In both cases, you need to have a consistent approach for ensuring
the operating system is secure at launch and maintained in an on-going basis. Using
infrastructure as code (IaC) tools such as [CloudFormation](https://aws.amazon.com/cloudformation/) can assist with achieving image
security consistency. For HANA-based SAP solutions, the [AWS Launch Wizard](https://aws.amazon.com/launchwizard/) for SAP simplifies
the installation process, including pre- and post-installation scripts that can be
customized to automate the installation of security components.

Refer to the AWS Well-Architected Framework [Security Pillar] guidance on
protecting compute resources, specifically the information on performing vulnerability
management and reducing the attack surface, for additional details.

- Well-Architected Framework [Security]: [Protecting Compute](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/protecting-compute.html)

**Suggestion 6.2.2 – Determine an approach for building and patching a
secure operating system**

As mentioned in the Well-Architected Framework [Security Pillar] discussion on
protecting compute, if your chosen operating system is supported by the EC2 Image Builder,
it can simplify the building, testing, and deployment of your SAP-specific AMIs and their
ongoing patch management. AWS Systems Manager Patch Manager should also be investigated
for maintaining the security posture of your operating system by automating security patch
application.

- Well-Architected Framework [Security]: [Protecting Compute](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/protecting-compute.html)
- AWS Documentation: [EC2 Image
Builder](https://aws.amazon.com/image-builder/)
- AWS Documentation: [AWS Systems Manager Patch Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-patch.html)

**Suggestion 6.2.3 – Review additional security recommendations
applicable to your operating system**

Determine the complete list of items that are required to harden the operating system
underlying the SAP software. For example, file system permissions on Linux-based systems
should be set according to SAP guidelines, while limiting Administrator group access is a
best practice on Windows-based systems.

The following SAP-specific recommendations might be relevant to your environment:

- SAP Documentation: [SAP NetWeaver Security Guide - Operating System Security](https://help.sap.com/viewer/621bb4e3951b4a8ca633ca7ed1c0aba2/LATEST/en-US/4a6e3d96f90472dde10000000a42189b.html)
- SAP Note: 2808515 - [Installing security software on SAP servers running on Linux](https://launchpad.support.sap.com/#/notes/2808515)

Operating System
Guidance

All Supported UNIX/Linux Operating Systems

- SAP Documentation: [SAP System Security Under UNIX/LINUX](https://help.sap.com/viewer/621bb4e3951b4a8ca633ca7ed1c0aba2/LATEST/en-US/4d3da980d936391ee10000000a15822b.html)

SUSE Linux Enterprise Server

- SAP Note: [2684254 - SAP HANA
DB: Recommended OS settings for SLES 15 / SLES for SAP Applications
15](https://launchpad.support.sap.com/#/notes/2684254) [Requires SAP Portal Access]
- SAP Note: [2578899 - SUSE
Linux Enterprise Server 15: Installation Note](https://launchpad.support.sap.com/#/notes/2578899) [Requires SAP Portal
Access]
- Operating system-specific Documentation: [SUSE Hardening Guide](https://documentation.suse.com/sbp/all/html/OS_Security_Hardening_Guide_for_SAP_HANA_SLES15/)

Red Hat Enterprise Linux

- SAP Note: [2777782 - SAP HANA DB: Recommended OS Settings for RHEL 8](https://launchpad.support.sap.com/#/notes/2777782) [Requires
SAP Portal Access]
- SAP Note: [2772999 - Red Hat Enterprise Linux 8.x: Installation and
Configuration](https://launchpad.support.sap.com/#/notes/2772999) (with particular mention of SELinux support) [Requires
SAP Portal Access]
- Red Hat Documentation: [Red Hat Enterprise Linux
Security Hardening Guide for SAP HANA 2.0](https://access.redhat.com/articles/6892601)
- Red Hat Blog: [Security recommendations for SAP HANA on RHEL](https://www.redhat.com/en/blog/security-recommendations-sap-hana-rhel)

Microsoft Windows

- SAP Documentation: [SAP System Security on Windows](https://help.sap.com/viewer/621bb4e3951b4a8ca633ca7ed1c0aba2/LATEST/en-US/4d6b747d7f961fbbe10000000a15822b.html)
- SAP Note: [1837765 - Security
policies for adm and SAPService on Windows](https://launchpad.support.sap.com/#/notes/1837765)
[Requires SAP Portal Access]

Oracle Enterprise Linux

- (Consult SAP or Vendor documentation for guidance)

**Suggestion 6.2.4 – Validate the security posture of the operating
system**

After the operating system has been securely deployed and patched, validating the
operating system security posture ensures that the operating system maintains an ongoing
high level of security without violation. Consider automating this validation using
third-party host intrusion protection, intrusion detection, antivirus, and operating system
firewall software.

Consider the following services:

- [Amazon Inspector](https://aws.amazon.com/inspector/) is an automated
vulnerability management service that continually scans AWS workloads for software
vulnerabilities and unintended network exposure.
- [Amazon GuardDuty Malware Protection](https://docs.aws.amazon.com/guardduty/latest/ug/malware-protection.html) is a continuous security monitoring service to
analyze and process threats from multiple data sources. Use it to highlight activity
that may indicate an instance compromise, such as cryptocurrency mining, denial of
service activity, EC2 credential compromise, or data exfiltration using DNS.
- [AWS Security Hub CSPM](https://aws.amazon.com/security-hub/) and [AWS Config](https://aws.amazon.com/config/) can be used for aggregation and
assessment of operating system based alerts and configuration, along with other AWS
services.

For more details, refer to the following information:

- Well-Architected Framework [Security]: [Secure Operation](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/operating-your-workload-securely.html)
- Well-Architected Framework [Security]: [Detection](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/detection.html)
- Well-Architected Framework [Security]: [Protecting Compute](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/protecting-compute.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-6-2.html*

---

# Best Practice 6.3 – Protect the database and the application

Security vigilance is imperative at the database and application layers, as a
malicious actor gaining access at even a read-only level could compromise the security of
critical business data. In all cases, follow the standard SAP best practices for database
access protection and application security. These apply to both on-premises and
cloud-based installations, and there are guidelines for each supported underlying database
for SAP systems.

**Suggestion 6.3.1 Follow SAP guidance on database security for your
chosen database**

Refer to the following for appropriate guidelines:

Database
Documentation

SAP HANA

- AWS Documentation: [AWS SAP HANA Security](https://docs.aws.amazon.com/sap/latest/sap-hana/hana-ops-security.html)
- SAP Documentation: [SAP HANA Security Guide](https://help.sap.com/viewer/b3ee5778bc2e4a089d3299b82ec762a7/latest)
- SAP Documentation: [SAP
HANA Administration Guide](http://help.sap.com/hana/SAP_HANA_Administration_Guide_en.pdf)
- SAP Note: [2159014 - FAQ: SAP
HANA Security](https://launchpad.support.sap.com/#/notes/2159014) [Requires SAP Portal Access]

SAP ASE
SAP Documentation: [Security Administration in SAP ASE](https://help.sap.com/viewer/2705a3b1e3df4514ab089cfedf87750d/LATEST/en-US/a90b1f6cbc2b10148e32ab3706191414.html)

IBM Db2
(Consult SAP or Vendor documentation for guidance)

Oracle
SAP Documentation: [SAP Database Guide - Oracle](https://help.sap.com/viewer/3ef1b95cacbf4f77a066797285371bb9/LATEST/en-US/4717849f6e8a21c3e10000000a114a6b.html)

Microsoft SQL Server
SAP Note: [3019299 - Security Audit
Questions or Security Customization in NetWeaver and SQL Server systems](https://launchpad.support.sap.com/#/notes/3019299)
[Requires SAP Portal Access]

SAP MaxDB
SAP Documentation: [SAP
MaxDB Security Guide](https://help.sap.com/viewer/b255f72263a84a48b22eb41f4d381dda/latest)

**Suggestion 6.3.2 – Follow SAP guidance on application
security**

For SAP NetWeaver-based solutions, prescriptive guidance can be found in the SAP
NetWeaver Security Guide.

- SAP Documentation: [ABAP Platform Security Guide](https://help.sap.com/viewer/621bb4e3951b4a8ca633ca7ed1c0aba2/LATEST/en-US/4aaf6fd65e233893e10000000a42189c.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-6-3.html*

---

# Best Practice 6.4 – Establish a plan for upgrading and patching all applicable software

SAP and the vendors of the underlying operating systems and databases release standard
security updates on a fixed schedule as well as provide emergency updates to fix
vulnerabilities. Be aware of the latest security information from each vendor. We
recommend that you keep your SAP application and all underlying components updated with
the latest security fixes on a scheduled basis to avoid introducing security holes. We
also recommend that you put a plan in place for applying emergency fixes when critical
security patches are released.

**Suggestion 6.4.1 - Subscribe to alerts from the vendors of operating
system, database, and software solutions**

Subscribing to your various vendor portals for security updates can help you become
aware of new security issues and remediations as they are released. This can help you plan
for required changes.

- AWS Documentation: [AWS Security Bulletins](https://aws.amazon.com/security/security-bulletins/?card-body.sort-by=item.additionalFields.bulletinDateSort&card-body.sort-order=desc)
- SAP Documentation: [SAP EarlyWatch Alert](https://support.sap.com/en/offerings-programs/support-services/earlywatch-alert.html)
- SAP Documentation: [SAP Security News](https://support.sap.com/en/my-support/knowledge-base/security-notes-news.html)

Operating System
Guidance

SUSE Linux Enterprise Server

[SUSE Update Advisories](https://www.suse.com/support/update/)

Red Hat Enterprise Linux

[Red Hat
Security Advisories](https://access.redhat.com/security/security-updates/#/)

Microsoft Windows

[Microsoft Security Alerts](https://www.microsoft.com/en-us/msrc/technical-security-notifications)

Oracle Enterprise Linux

[Oracle Security
Alerts](https://www.oracle.com/security-alerts/)

**Suggestion 6.4.2 – Review the recommended changes and risk to your
business and implementation effort**

SAP teams must learn to balance the need for system uptime with the criticality of
system changes that have been recommended to improve SAP security. Failure to do so can
introduce unnecessary risks such as service interruptions, financial impact, or lost
productivity. Review the recommended changes and implementation steps to fix
vulnerabilities from your vendors and plan to implement them promptly. This directly
relates to the Operational Excellence best practices discussed in this Lens, particularly
the creation of runbooks for security.

- SAP Lens [Operational Excellence]: [Suggestion
3.4.1 - Create specific runbooks for SAP security operations](./best-practice-3-4.html)

**Suggestion 6.4.3 – Establish a plan to address vulnerabilities in a
timely manner**

Applying new SAP security recommendations and security-related patches as quickly as
possible is paramount both for AWS based SAP solutions and those installed elsewhere.
Regularly review the [SAP
Security Notes and News](https://support.sap.com/en/my-support/knowledge-base/security-notes-news.html), and create a process to remediate security issues quickly
with the patches, notes, and recommendations found there. In some cases, SAP administrators
may also have to put in temporary mitigation or control measures until the underlying
vulnerability can be addressed. Also follow the Security Pillar recommendations around
incident response.

- Well-Architected Framework [Security]: [Incident Response](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/incident-response.html)
- SAP Documentation: [SAP Security Notes and News](https://support.sap.com/en/my-support/knowledge-base/security-notes-news.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-6-4.html*

---

## 7 – Control access to your SAP workload through identity and permissions

# Best Practice 7.1 – Understand your SAP user categories and access mechanisms

The types of users accessing your SAP system will determine the security controls you
need to apply. By examining each use case, you can develop a strategy. This should include
how you manage identities, authentication, tooling and mechanisms to support those
requirements.

**Suggestion 7.1.1 Understand data access permissions and permitted
actions**

SAP systems often contain highly sensitive business data. As you define your user
types, understand the data access permissions. (For example, an administrative database user
does not have the fine-grained controls of an application user, and therefore may be more
critical.) Also refer to [Security]: [Best Practice 5.2 -
Classify the data within your SAP workloads](./best-practice-5-2.html).

Consider the following questions in relation to your SAP system access:

- Do the actions taken by an administrative or service user need to be traceable to
a uniquely identifiable individual?
- At which layer of the application will the access be granted?
- Can you restrict access to a subset of functionality via permissions?
- Can you restrict access to a subset of functionality via other controls, for
example exposing only certain services?
- Is there a requirement to audit the actions taken?

**Suggestion 7.1.2 – Understand the network and/or location from which
users will access the SAP systems**

Network and/or location often contributes to the security risk profile and may
determine whether the user is considered trusted or untrusted. Typically, this is coupled
with the controls to prevent unauthorized access (refer to [Best Practice 6.1 - Ensure that security and auditing are built into the SAP network
design](./best-practice-6-1.html)).

This can influence your design. For example, an untrusted internet user or device may
require additional factors of authentication to access your SAP workload, when compared
with a trusted user from your corporate network.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-7-1.html*

---

# Best Practice 7.2 – Manage privileged access to your SAP workload

Adopt an approach of least privilege where possible. Only grant the minimum access
required to perform a particular role to a minimum set of users, while managing usability
and efficiency. There are administrative accounts (for example,
`adm`), which by default, have access to significantly impact the
reliability or data security of your SAP workload. Consider how you can limit this
risk.

**Suggestion 7.2.1 – Manage AWS credentials and
authentication**

AWS Identity and Access Management (IAM) enables you to manage access to AWS services and resources securely.
Using IAM, you can create and manage AWS users and groups for different SAP and cloud
administration tasks. Use IAM permissions to allow and deny users access to AWS resources.
Standard guidance should be followed, in particular restricting and securing root access.

- AWS Documentation: [Security
best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)

For access that is not assigned to a user but is required for the operation of the SAP
application, pay particular attention to ensuring least privilege.

- AWS Documentation: [Using an IAM role to grant permissions to applications running on Amazon EC2
instances](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2.html)

[IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html) helps identify security risks associated with resources that are
shared with an external entity, validates policies against IAM policy grammar and best
practice, and can generate an IAM policy from the analysis of AWS CloudTrail logs. Consider its
use as a mechanism for continuously reducing permissions based on user and role access
patterns.

**Suggestion 7.2.2 – Manage SAP Administrative credentials and
authentication**

Implement a process for approving and granting elevated permissions only when
required, for a limited time-period. Use auditing functionality that addresses who and why
the access was granted.

Restrict the use of username/password for privileged accounts. Disable direct access
where possible. Store credentials securely, for example, in a privileged access management
solution or password vault.

Evaluate how Systems Manager could be used to restrict direct operating system access for
specific tasks using runbooks, RunCommand, and AWS Secrets Manager.

- AWS Documentation: [Restricting access to root-level commands through SSM Agent](https://docs.aws.amazon.com/systems-manager/latest/userguide/ssm-agent-restrict-root-level-commands.html)
- AWS Documentation: [Referencing AWS Secrets Manager secrets from Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/integration-ps-secretsmanager.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-7-2.html*

---

# Best Practice 7.3 – Understand your organization’s identity management approach, and its application to SAP

Typical SAP workloads will consist of multiple systems and therefore multiple
identities. A centralized approach for managing these users can reduce the security risk and
operational complexity. Your focus should be on how to use AWS services and third-party
tools in your approach to SAP security, considering such options as centralized user
management, single sign-on, and multi-factor authentication.

**Suggestion 7.3.1 – Determine an Identity Provider for named
users**

Users will be associated with an identity store, for example Active Directory. This
acts as a central repository for managing identity information, such as roles,
permissions, and identifiers. For each set of identities, determine if this can be
associated with an Identity Provider. An identity provider enables you to off-load the
authentication of users. It facilitates single sign-on (SSO) and also manages the user
identity lifecycle (for example joiners, movers, leavers).

Consider exceptions for named users that are not associated with a human. This may
include batch, job scheduling, integration, and monitoring users.

- AWS Documentation: [AWS
Directory Service | Amazon Web Services (AWS)](https://aws.amazon.com/directoryservice/)
- AWS Documentation: [AWS Identity
Services](https://aws.amazon.com/identity/)

**Suggestion 7.3.2 – Determine the authentication
mechanisms**

Understand the supported authentication mechanisms (for example, SAML, Kerberos,
X.509, SAP Single Sign-On tickets) at each of the layers for your SAP workload. Evaluate
the requirements to integrate with your application. Where possible use single sign-on to
avoid the administrative and security impact of managing multiple user credentials.

- SAP Documentation: [User Authentication and single sign-on](https://help.sap.com/viewer/621bb4e3951b4a8ca633ca7ed1c0aba2/LATEST/en-US/4a112f1a2228101ee10000000a42189b.html)
- AWS Documentation: [Cloud
applications - AWS IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/saasapps.html)
- SAP on AWS Blog: [Enable SAP Single Sign On with AWS IAM Identity Center Part 1: Integrate SAP NetWeaver ABAP with
IAM Identity Center](https://aws.amazon.com/blogs/awsforsap/enable-sap-single-sign-on-with-aws-sso-part1-integrate-sap-netweaver-abap-based-applications-sso-with-aws-sso/)
- SAP on AWS Blog: [Enable SAP Single Sign On with AWS IAM Identity Center Part 2: Integrate SAP NetWeaver Java](https://aws.amazon.com/blogs/awsforsap/enable-sap-single-sign-on-with-aws-sso-part-2-integrate-sap-netweaver-java/)
- SAP on AWS Blog: [Enable Single Sign On for SAP Cloud Platform Foundry and SAP Cloud Platform Neo
with IAM Identity Center](https://aws.amazon.com/blogs/awsforsap/enable-single-sign-on-for-sap-cloud-platform-foundry-and-sap-cloud-platform-neo-with-aws-sso/)

**Suggestion 7.3.3 – Consider multi-factor authentication**

Multi-Factor Authentication (MFA) is a best practice that adds an extra layer of
protection on top of your logon credentials. These multiple factors provide increased
security for your SAP application. Use cases include: access to SAP from an untrusted
device; access to the AWS Management Console; and privileged activities such as deletion of backups or
termination of EC2 instances.

- SAP on AWS Blog: [Securing SAP Fiori with MFA](https://aws.amazon.com/blogs/awsforsap/securing-sap-fiori-with-multi-factor-authentication/)
- AWS Documentation: [Using MFA devices with your IAM sign-in page - AWS Identity and Access](https://docs.aws.amazon.com/IAM/latest/UserGuide/console_sign-in-mfa.html)
- AWS Documentation: [Configuring MFA delete -Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/MultiFactorAuthenticationDelete.html)
- AWS Documentation: [Amazon EC2: Requires MFA (GetSessionToken) for specific EC2 operations](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_examples_ec2_require-mfa.html)

**Suggestion 7.3.4 – Determine the approach to certificate
management**

Client-based certificates can be used for authentication without the need for
credentials. Determine an approach which includes time-based expiration for session
management and certificate rotation for system to system communication. AWS provides a
Certificate Authority (CA) that is trusted by SAP. Certificates can be issued and managed
using [AWS Certificate Manager
(ACM)](https://aws.amazon.com/certificate-manager/).

- SAP Note: [2801396
- SAP Global Trust List](https://launchpad.support.sap.com/#/notes/2801396) [Requires SAP Portal Access]
- SAP Note: [3040959
- How to get a CA signed server certificate in ABAP](https://launchpad.support.sap.com/#/notes/3040959) [Requires SAP Portal
Access]
- SAP Lens [Operational Excellence]: [Suggestion
3.4.1 - Create specific runbooks for SAP security operations](./best-practice-3-4.html)
- SAP Lens [Operational Excellence]: [Suggestion
4.1.2 - Maintain a calendar for expiring of credentials, certificates and
licenses](./best-practice-4-1.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-7-3.html*

---

# Best Practice 7.4 – Implement logging and reporting for user access and authorization changes and events

User access and authorization events in your SAP systems should be logged, analyzed,
and audited regularly. Consolidate and correlate security events from your SAP applications
and database with other components of your architecture. This can allow for end-to-end
tracing in the event of a critical security problem or breach. Automate analysis of events
in a central Security Information and Event Management (SIEM) system. This can allow your
operations team to understand if any unexpected or suspicious activity occurs outside of the
bounds of normal system controls. They can then remediate as needed.

**Suggestion 7.4.1 – Log AWS Identity and Access Management (IAM)
events**

Consider keeping a historical log of AWS IAM events. This can be used in detection
or audit of user and authorization changes within AWS accounts. Determine your log
retention period and types of events to log based on your organizations required security
policies.

Enable your operations team to answer audit questions at the infrastructure level for
your SAP system:

- When and by whom was the new AWS console/CLI user created?
- When and by whom was the AWS IAM role modified?
- When did the AWS user last successfully sign in?
- Is there a suspicious number of failed sign-in attempts to the AWS
account?

For further information, consider the following:

- AWS Documentation: [IAM Best Practices: Monitor activity in your AWS account](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#keep-a-log)
- AWS Documentation: [Logging IAM and AWS STS API
calls with AWS CloudTrail](https://docs.aws.amazon.com/IAM/latest/UserGuide/cloudtrail-integration.html)
- AWS Well-Architected Framework [Security]: [Detection](https://docs.aws.amazon.com/wellarchitected/latest/framework/sec-detection.html)
- AWS Security Blog: [Visualizing Amazon GuardDuty
findings](https://aws.amazon.com/blogs/security/visualizing-amazon-guardduty-findings/)
- AWS Security Blog:[Amazon GuardDuty Enhances Detection of EC2 Instance Credential Exfiltration](https://aws.amazon.com/blogs/aws/amazon-guardduty-enhances-detection-of-ec2-instance-credential-exfiltration/)

**Suggestion 7.4.2 – Log user and authorization changes in your
operating system**

Consider keeping a historical log of operating system (OS) user and authorization
events such that they can be used in detection or audit. Determine your log retention
period and types of events to log based on your organizations required security
policies.

Enable your operations team to answer audit questions at the operating system level
for your SAP system such as:

- When and by whom was the new superuser OS account created?
- When and by whom was the OS account permissions modified?
- When did the OS user last successfully sign in?
- Is there a suspicious number of failed sign-in attempts for the OS account?
- When did your OS user last use elevated permissions?

For further information on auditing at the operating system consider:

Operating System
Guidance

SUSE Linux Enterprise Server

[Setting Up the Linux Audit Framework | Security Guide](https://documentation.suse.com/sles/12-SP4/html/SLES-all/cha-audit-setup.html)

Red Hat Enterprise Linux

[Chapter 14. Auditing the system Red Hat Enterprise Linux 8 | Security
Guide](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/security_hardening/auditing-the-system_security-hardening)

Microsoft Windows

[Windows Audit Policy Recommendations](https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/plan/security-best-practices/audit-policy-recommendations)

Oracle Enterprise Linux

[Oracle Linux 8 Enhancing System Security - Using System Auditing and Monitoring](https://docs.oracle.com/en/operating-systems/oracle-linux/8/security/security-ImplementingAdditionalSecurityFeaturesandBestPractices.html#ol-s4-syssec)

**Suggestion 7.4.3 – Log SAP application and database user and
authorization events**

Consider keeping a historical log of SAP user and authorization events such that they
can be used in detection or audit. Consider both the application stack (for example, ABAP
authorizations) and your database (for example, SAP HANA). Determine your log retention
period and types of events to log based on your organizations required security
policies.

Enable your operations team to answer audit questions at the SAP application and
database level for events such as:

- When and by whom was the new SAP or database account created?
- When and by whom was the SAP or database account permissions modified?
- When did the SAP or database user last successfully sign in?
- Is there a suspicious number of failed sign-in attempts for the account?
- What sensitive transaction codes or tools did the account last use?

For further information consider the following:

- SAP Documentation: [SAP Access Control
and Governance | User Access](https://www.sap.com/australia/products/access-control.html)
- SAP Documentation: [SAP NetWeaver ABAP: The Security Audit Log](https://help.sap.com/viewer/280f016edb8049e998237fcbd80558e7/LATEST/en-US/4d41bec4aa601c86e10000000a42189b.html)
- SAP Documentation: [SAP NetWeaver JAVA: The Security Audit Log](https://help.sap.com/viewer/56bf1265a92e4b4d9a72448c579887af/LATEST/en-US/c769bcb7f36611d3a6510000e835363f.html)
- SAP Documentation: [SAP HANA: Auditing Activity in SAP HANA](https://help.sap.com/viewer/b3ee5778bc2e4a089d3299b82ec762a7/LATEST/en-US/ddcb6ed2bb5710148183db80e4aca49b.html)

**Suggestion 7.4.4 – Consolidate user and authorization events in a
Security Information and Event Management (SIEM) system for analysis**

Consider sending all your user and authorization events from across your SAP workload
components into a central SIEM tool to allow correlation and analysis. Use tools like SAP
Enterprise Threat Detection, third-party add-ons or directly ship your SAP audit logs from
your application and database servers to an ingestion and analysis tool.

Establish baseline behaviors for your workload and monitor for abnormalities to
improve detection of security incidents.

Consider [AWS Marketplace
SIEM solutions](https://aws.amazon.com/marketplace/solutions/control-tower/siem/) to monitor your workload in real-time, identify security issues,
and expedite root-cause analysis and remediation.

For further information, consider the following resources:

- AWS Marketplace: [SIEM
Solutions](https://aws.amazon.com/marketplace/solutions/control-tower/siem/)
- AWS Documentation: [AWS Security Hub CSPM](https://aws.amazon.com/security-hub/?aws-security-hub-blogs.sort-by=item.additionalFields.createdDate&aws-security-hub-blogs.sort-order=desc)
- SAP Documentation: [SAP Enterprise Threat Detection](https://help.sap.com/viewer/eb42e48f5e9c4c9ab58a7ad73ff3bc66/LATEST/en-US/e12aa17b106c4c6193b7d593328aad48.html)
- Well-Architected Framework [Security]: [Security Incident Response](https://docs.aws.amazon.com/wellarchitected/latest/framework/sec-incresp.html)
- AWS Documentation: [AWS Security Incident Response - Technical Whitepaper](https://docs.aws.amazon.com/whitepapers/latest/aws-security-incident-response-guide/welcome.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-7-4.html*

---

## 8 – Protect your SAP data at rest and in transit

# Best Practice 8.1 – Encrypt data at rest

Data at rest refers to any data stored digitally. We use encryption to ensure that
this data is only visible to authorized users and remains protected when access to the
storage or database is compromised independently of the application.

**Suggestion 8.1.1 – Define at which levels encryption will be
applied**

In general, the further up the stack you deploy encryption, the more secure your data
is. This increased security is accompanied by additional complexity for deployment and
management. AWS recommends using the encryption at rest options available within its
services. Consider additional operating system or database encryption when required, as
defined in [Security]: [Best Practice 5.3 - Assess the
need for specific security controls for your SAP workloads](./best-practice-5-3.html).

**Suggestion 8.1.2 – Understand AWS encryption options for SAP
services and solutions**

Many AWS services used by SAP support the encryption of data at rest. Refer to
the following documentation for further details.

- AWS Documentation: [Use encryption with EBS-backed
AMIs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIEncryption.html)
- AWS Documentation: [Amazon EBS Encryption](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html)
- AWS Documentation: [Amazon EFS encryption](https://docs.aws.amazon.com/efs/latest/ug/encryption.html)
- AWS Documentation: [Amazon FSx encryption](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/encryption.html)
- AWS Documentation: [FSx for ONTAP encryption](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/encryption-at-rest.html)
- AWS Documentation: [Amazon S3 Encryption](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingEncryption.html)

Data stored in these services can be encrypted at rest using either AWS or customer
managed keys from AWS KMS.

Operating system encryption options include BitLocker, DM-crypt and SuSE Remote
Disk.

The following links may assist with finding information about encryption options for
your database:

Database
Guidance

SAP HANA

- SAP Documentation: [Server-Side Data Encryption Services](https://help.sap.com/viewer/b3ee5778bc2e4a089d3299b82ec762a7/LATEST/en-US/b30fda1483b34628802a8d62bd5d39df.html)
- SAP Documentation:[HANA Local Secure Store (LSS)](https://help.sap.com/docs/SAP_HANA_PLATFORM/b3ee5778bc2e4a089d3299b82ec762a7/5a43dc48190f4543b0d840952d3dec55.html?&locale=en-US)

SAP ASE
SAP Documentation: [SAP ASE Overview of Encryption](https://help.sap.com/viewer/833788dd3e9c413799014a0fd002d0b2/LATEST/en-US/a7b86bb3bc2b1014b9b08178723a5ee2.html)

IBM Db2
IBM Documentation: [Db2
Encryption Overview](https://www.ibm.com/docs/en/db2/11.5?topic=encryption-overview)

Oracle
SAP Note: [2591575 - Using Oracle
Transparent Data Encryption (TDE) with SAP NetWeaver](https://launchpad.support.sap.com/#/notes/2591575) [Requires SAP Portal
Access]

Microsoft SQL Server
SAP Note: [1380493 - SQL Server
Transparent Data Encryption (TDE)](https://launchpad.support.sap.com/#/notes/1380493) [Requires SAP Portal Access]

SAP MaxDB
SAP Documentation: [SAP MaxDB Database Administration - Encryption](https://help.sap.com/viewer/2c2effc99b6746019aeb1af52ad59f5d/LATEST/en-US/741a232db1754d1899d23f9837e6052c.html)

**Suggestion 8.1.3 – Define encryption methods and key management
stores**

Typically, key management is defined at the enterprise level and this will determine
which key management options are permitted for use with your SAP workloads. AWS KMS is a
secure and resilient service to simplify the management of encryption keys for AWS
services. If you have a requirement to manage your own hardware security modules (HSMs),
you can use AWS CloudHSM.

- AWS Documentation: [AWS encryption tool and service options](https://docs.aws.amazon.com/crypto/latest/userguide/awscryp-choose-toplevel.html)
- AWS Documentation: [AWS Key
Management Service (AWS KMS)](https://aws.amazon.com/kms/)
- AWS Documentation: [AWS CloudHSM](https://aws.amazon.com/cloudhsm/)

Also consider mechanisms to protect master keys. How do you restrict access, manage
rotation, and ensure recoverability of the keys?

Be aware that HANA data at rest encryption root keys can only be stored securely in
the instance secure store in the file system (Instance SSFS) or within the SAP Data
Custodian SaaS Solution. If using instance store the master key could be stored in [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/) with a rotation policy.

- SAP Note: [2154997
- Migration of hdbuserstore entries to ABAP SSFS](https://launchpad.support.sap.com/#/notes/2154997) [Requires SAP Portal
Access]
- SAP Note: [2755815
- How to Ensure Recoverability of Hana's Data-At-Rest Encryption](https://launchpad.support.sap.com/#/notes/2755815) [Requires
SAP Portal Access]

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-8-1.html*

---

# Best Practice 8.2 – Encrypt data in transit

Using encryption of data in transit makes it harder for your data to be intercepted,
accessed, or tampered with while it’s moving from one point to another. Ensure that there
are secure protocols and network-level encryption in place to minimize potential threats
and provide the level of protection aligned with your requirements.

Well-Architected Framework [Security]: [Protecting Data in Transit](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/protecting-data-in-transit.html)

**Suggestion 8.2.1 – Encrypt application traffic based on SAP and
database protocols**

For application traffic using SAP Protocols (SAPGUI Dialog, RFC, and CPIC) use SAP
SNC to enforce Transport Layer Security.

- SAP Documentation: [SNC-Protected Communication Paths in SAP Systems](https://help.sap.com/viewer/621bb4e3951b4a8ca633ca7ed1c0aba2/LATEST/en-US/ad38ff4fa187622fe10000000a44176d.html)

For database traffic, use a secure connection between the client and database, where
available.

Database
Guidance

SAP HANA
SAP Documentation: [SAP HANA: Securing Data Communication](https://help.sap.com/viewer/b3ee5778bc2e4a089d3299b82ec762a7/LATEST/en-US/dda2ae94bb571014a48fc3b22f8e919e.html)

SAP ASE
SAP Documentation: [SSL in SAP ASE](https://help.sap.com/viewer/2705a3b1e3df4514ab089cfedf87750d/LATEST/en-US/a947184cbc2b10149416e3140b2f61aa.html)

IBM Db2
SAP Note: [2385640 - DB6: database
connection using SSL encryption](https://launchpad.support.sap.com/#/notes/2385640) [Requires SAP Portal Access]

Oracle
SAP Note: [973450 - Oracle Database
network encryption and data integrity](https://launchpad.support.sap.com/#/notes/973450) [Requires SAP Portal Access]

Microsoft SQL Server
SAP Note: [1570930 - SQL Server
network encryption with SAP](https://launchpad.support.sap.com/#/notes/1570930) [Requires SAP Portal Access]

SAP MaxDB
SAP Documentation: [MaxDB Network and Communication](https://help.sap.com/viewer/b255f72263a84a48b22eb41f4d381dda/LATEST/en-US/44bb54e8e00215b2e10000000a155369.html)

**Suggestion 8.2.2 – Encrypt SAP application traffic based on internet
protocols**

For application traffic based on internet protocols (HTTP, P4 (RMI), LDAP) use
SSL/TLS to enforce Transport Layer Security.

- SAP Documentation: [Transport Layer Security](https://help.sap.com/viewer/621bb4e3951b4a8ca633ca7ed1c0aba2/LATEST/en-US/5f0f558b8a7841049139f0fb558ac62c.html)

**Suggestion 8.2.3 – Encrypt data exchange based on file transfer or
message transfer protocols**

For file-based transfers, AWS provides AWS Transfer Family for secure file
exchange over SFTP or FTPS. AWS Transfer Family supports the transfer of data to and
from Amazon S3 and Amazon EFS.

- AWS Documentation: [AWS Transfer Family](https://aws.amazon.com/aws-transfer-family)

Using message-level data integrity checks helps ensure that data is not being
tampered with while being transferred. Consider the use of one or more of the message
level security standards supported by SAP to sign and verify the integrity of the data in
messages.

- SAP Documentation: [SAP ABAP Web Services Message-Level Security](https://help.sap.com/viewer/684cffda9cbc4187ad7dad790b03b983/1709 000/en-US/47ac469337a24845e10000000a421138.html?q=netweaver%20security%20guide%20message%20level%20security)
- SAP Documentation: [SAP NetWeaver Process Integration Security Guide](https://help.sap.com/doc/saphelp_nwpi711/7.1.1/en-US/f7/c2953fc405330ee10000000a114084/frameset.htm)
- SAP Documentation: [SAP Cloud Integration Message-Level Security](https://help.sap.com/viewer/368c481cd6954bdfa5d0435479fd4eaf/Cloud/en-US/463a9085156d4672bc4ee9095277e453.html)

For IDOC based messages use SNC to secure the RFC connection used by ALE.

- SAP Documentation: [Handling Sensitive Data in IDocs](https://help.sap.com/viewer/621bb4e3951b4a8ca633ca7ed1c0aba2/LATEST/en-US/7f2e71922f4a4d7081e1d2032b0934f7.html)

**Suggestion 8.2.4 – Encrypt administrative access**

It is common to use both Windows and SSH-based tools for the administration of SAP. In
addition to security controls such as Bastian Hosts consider if it is possible to Encrypt
this traffic.

Alternatively, [AWS Systems Manager Session Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager.html) provides a secure mechanism to access the
operating system via the AWS Management Console using TLS for encryption.

- AWS Documentation: [Amazon EC2 Windows Guide - Encryption in Transit](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/data-protection.html)
- AWS Documentation: [Amazon EC2 Linux Guide - Encryption in Transit](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/data-protection.html)
- AWS Documentation: [Data protection in AWS Systems Manager – Data Encryption](https://docs.aws.amazon.com/systems-manager/latest/userguide/data-protection.html#data-encryption)

**Suggestion 8.2.5 – Evaluate the features of AWS services that
enable encryption in transit**

In addition to application-based encryption, many AWS services provide encryption
in transit capabilities. Evaluate your corporate standards, the implementation effort and
associated benefits for each service. The following are some examples that are relevant
for SAP workloads.

- AWS Documentation: [Amazon S3 - Encryption in Transit](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingEncryption.html) - On by default and recommended for
backups to Amazon S3.
- AWS Documentation: [Amazon
EFS - Encryption in Transit](https://docs.aws.amazon.com/efs/latest/ug/encryption-in-transit.html) / [Amazon FSx](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/encryption-in-transit.html) - May be required for shared filesystems.
- AWS Documentation: [Elastic Load Balancing](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/data-protection.html) - Review your encryption requirements and whether
end-to-end TLS with pass-through is required as this feature may not be available for
all Load Balancer types.
- AWS Documentation: [Amazon EC2 - Encryption in Transit](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/data-protection.html) - Only later generation instance types
have this feature.

**Suggestion 8.2.6 – Implement network level encryption**

SAP customers will typically use either Direct Connect or a combination of Direct
Connect and VPN, to provide reliable connectivity to their resources on AWS.

AWS Direct Connect does not encrypt your traffic in transit. If encryption is
required, transport level encryption should be implemented, for example, using a VPN over
Direct Connect.

AWS provides Site-to-Site VPN that can be used for network channel encryption. You
can also choose to deploy third-party VPN solutions like OpenVPN from AWS Marketplace or
with a bring your own license.

Alternatively, consider AWS PrivateLink for supported AWS services and solutions,
including AWS Partners offering SaaS services. AWS PrivateLink provides private connectivity
without exposing your traffic to the internet.

- AWS Documentation: [AWS Managed VPN](https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/aws-managed-vpn.html)
- AWS Documentation: [AWS Client VPN](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/what-is.html)
- AWS Documentation: [AWS Direct Connect + VPN](https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/aws-direct-connect-vpn.html)
- AWS Documentation: [Software Site-to-Site VPN](https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/software-site-to-site-vpn.html)
- AWS Documentation: [AWS PrivateLink](https://aws.amazon.com/privatelink/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-8-2.html*

---

# Best Practice 8.3 – Secure your data recovery mechanisms to protect against threats

To help protect against malicious activities, follow the guidelines set out within
your organization’s security framework. [Protecting against ransomware](https://aws.amazon.com/security/protecting-against-ransomware/)
provides an overview of the key items to
address before an incident and as part of an incident response including network controls,
patching, and least privilege permissions. For SAP systems, the threat is similar to other
applications, but the impact is potentially greater. If SAP is a system of record, or
required for mission critical transactions, consider the following suggestions to secure a
backup against a malicious attack.

- SAP Note: [2663467
- Tips to avoid a Ransomware situation](https://launchpad.support.sap.com/#/notes/2663467) [Requires SAP Portal Access]
- SAP Note: [2496239
- Ransomware / malware on Windows](https://launchpad.support.sap.com/#/notes/2496239) [Requires SAP Portal Access]

**Suggestion 8.3.1 – Secure backups in a separate account with
additional controls**

By securing backups in an account that is isolated from the primary copy of your data,
either directly or using replication, it’s possible to minimize the risk of a compromised
system also impacting your data recovery mechanisms.

The secondary account can be viewed as a “data bunker” with access requirements
aligned to the use case.

For backups using Amazon S3, additional controls might include S3 Object Lock to
store objects using a write-once-read-many (WORM) model or [multi-factor authentication delete](https://docs.aws.amazon.com/AmazonS3/latest/userguide/MultiFactorAuthenticationDelete.html).

If using replication, understand the different options available, including [delete marker replication](https://docs.aws.amazon.com/AmazonS3/latest/userguide/delete-marker-replication.html) (by default deletion markers are not replicated) and
[S3 Replication Time Control](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication-time-control.html). To optimize costs, ensure that housekeeping is
performed on both the primary and secondary buckets.

Consider [AWS Backup Audit Manager](https://aws.amazon.com/about-aws/whats-new/2022/03/aws-backup-audit-manager-controls-compliance-backups-accounts/) to monitor and prove compliance for immutable backups
across Regions and accounts.

**Suggestion 8.3.2 – Validate your ability to recover**

Backups are the last line of defense when protecting your data from malicious
activities, but might prove worthless if recovery is not possible due to incomplete
backups or backups that are not valid. Recovery might not be possible if you are unable to
access or decrypt backups. Consider how you protect encryption keys and
credentials.

Perform recovery tests aligned with a malicious scenario, including a rebuild in an
alternate account.

- SAP Lens [Operational Excellence]: [Best
Practice 4.3 - Regularly test business continuity plans and fault recovery](./best-practice-4-3.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-8-3.html*

---

# Best Practice 9.1 – Understand your strategy for SAP application and database security event analysis

Without keeping security logs at the appropriate levels of granularity, vital data
required for incident response, forensic security analysis, and threat modeling can be
lost. SAP security staff must be able to evaluate potential security incidents affecting
SAP systems in alignment with your business security requirements. For SAP workloads
running on AWS, the AWS services described in the Well-Architected Framework Security
Pillar are a helpful starting point in conjunction with the following suggestions.

- Well-Architected Framework [Security]: [Detection – Configure](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/configure.html)

**Suggestion 9.1.1 – Determine which logs are required to detect
security events**

For individual SAP software and supported databases refer to the SAP NetWeaver Guide
Finder as well as the SAP NetWeaver Security Guide for what logs might be applicable (for
example, [read access logging](https://help.sap.com/viewer/621bb4e3951b4a8ca633ca7ed1c0aba2/LATEST/en-US/631dfbf00a604784b69fc30570bfb69d.html)). In addition, review the SAP advisory on [security logging](https://help.sap.com/viewer/1a93b7a44ac146b5ad9b6fd95c1223cc/LATEST/en-US/182e167819f6405792686e94c177b9eb.html) and related topics surrounding best practices for your
development activities.

- SAP Documentation: [SAP
NetWeaver Guide Finder](https://help.sap.com/viewer/nwguidefinder)
- SAP Documentation: [ABAP Platform Security Guide](https://help.sap.com/viewer/621bb4e3951b4a8ca633ca7ed1c0aba2/LATEST/en-US/4aaf6fd65e233893e10000000a42189c.html)
- SAP Documentation: [Security Logging](https://help.sap.com/viewer/1a93b7a44ac146b5ad9b6fd95c1223cc/LATEST/en-US/182e167819f6405792686e94c177b9eb.html)

**Suggestion 9.1.2 – Develop mechanisms for storing and analyzing
logs**

Having relevant data regarding potential security events is necessary for any secure
SAP installation, but it is equally important to store that data securely and have the
necessary tools for searching and analyzing the data in an efficient and timely manner. One
option within AWS includes using the [CloudWatch Agent](https://docs.aws.amazon.com/systems-manager/latest/userguide/monitoring-cloudwatch-agent.html) to store instance logs and SAP application logs relevant to
security in an [Amazon CloudWatch log group](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html). Such logs could also be [exported to
Amazon S3](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/S3Export.html) for holistic log analysis and for integration with [third-party log
analytics solutions](https://aws.amazon.com/marketplace/solutions/control-tower/siem).

Refer to the following for help with assembling, combining, and analyzing your SAP on
AWS security logs:

- SAP Lens [Security]: [Suggestion 7.4.4 -
Consolidate user and authorization events in a Security Information and Event
Management (SIEM) system for analysis](./best-practice-7-4.html)
- SAP on AWS Blog: [Set up observability for SAP HANA databases with Amazon CloudWatch Application Insights](https://aws.amazon.com/blogs/awsforsap/sap-hana-observability-with-amazon-cloudwatch-application-insights/)
- SAP on AWS Blog: [SAP HANA monitoring: A serverless approach using Amazon CloudWatch](https://aws.amazon.com/blogs/awsforsap/sap-hana-monitoring-a-serverless-approach-using-amazon-cloudwatch/)
- SAP on AWS Blog: [SAP Monitoring: A serverless approach using Amazon CloudWatch](https://aws.amazon.com/blogs/awsforsap/sap-monitoring-a-serverless-approach-using-amazon-cloudwatch/)

**Suggestion 9.1.3 – Use machine learning to analyse and determine
events of importance**

Consider applying pattern recognition, anomaly detection, or both to security logs to
assist in determining potential threats and events of importance to your SAP workload. AWS
managed services, such as [AWS Security Hub CSPM](https://aws.amazon.com/security-hub/) and [Amazon
GuardDuty](https://aws.amazon.com/guardduty/), can help, combined with third-party security solutions from the AWS
Marketplace.

- AWS Video: [An Overview
of AWS Security Hub CSPM](https://www.youtube.com/watch?v=oBac-GAoZJ8)
- AWS Documentation: [Getting started with GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_settingup.html?ref=wellarchitected)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-9-1.html*

---

# Best Practice 9.2 – Perform periodic tests for security bugs

As described in the Well-Architected Framework Security Pillar incident response
sections on simulations, assembling a runbook and conducting game days are recommended for all
workloads, including those for SAP on AWS. This type of periodic testing can identify
new attack vectors and vulnerabilities as well as prepare your SAP security resources for
a rapid and effective response in the event of a security incident.

Well-Architected Framework [Security]: [Incident Response – Simulation](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/simulate.html)

**Suggestion 9.2.1 – Include SAP applications as targets in addition
to standard security and penetration testing**

Probative security testing is an important part of maintaining a secure environment.
In addition to conducting standard penetration testing in AWS, make sure to include your
SAP solution as an additional potential target for malicious activities. Keep in mind
SAP-specific software solutions that often are publicly exposed in your architecture such
as SAProuter, Web Dispatcher, Cloud Connector, and SAP Fiori.

- AWS Documentation: [Penetration
Testing](https://aws.amazon.com/security/penetration-testing/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-9-2.html*

---

# Best Practice 9.3 – Have a documented plan for responding to security events

Without a documented plan for addressing a security event involving your SAP
applications, the security team’s response may be delayed, less comprehensive, and less
effective both in mitigating the event and understanding its cause. Document security
response patterns thoroughly for your SAP applications.

**Suggestion 9.3.1 - Prepare for security events by having a
documented incident management plan**

This directly aligns with the AWS Well-Architected Framework Security Pillar
guidance on incident response preparation. Refer to this documentation and be sure to
include your SAP applications accordingly:

- Well-Architected Framework [Security]: [Incident Response – Prepare](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/prepare.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/best-practice-9-3.html*

---
