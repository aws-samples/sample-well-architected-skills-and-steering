# Security

**Pages**: 3

---

# Assess

It's important to conduct a security review of the discovery tool
used to assess on-premises inventory and understand how they work
to ensure they don't introduce any vulnerabilities. During this
phase, it's also key to review your current security tools and map
them to their equivalents on AWS and to identify your compliance
framework.

MIG-SEC-01: Have you performed a security review of the discovery tool you plan to use to assess your on-premises inventory?

Organizations have to meet different security and compliance
standards. Ensure you fully understand the impact of any
discovery tool against your security posture by assessing the
risk profile of the discovery tool, how the data about
on-premises environment is collected, where the data is stored,
and how the stored data is secured.

## MIG-SEC-BP-1.1 Understand the security credentials needed by the discovery tool

This BP applies to the following best practice area: Identity and access management

### Implementation guidance

**Suggestion 1.1.1**: Determine the required discovery tools and techniques.

Discovery tools, whether AWS native or partner solutions,
typically leverage two types of discovery methodologies:
agent-based discovery or agentless discovery. Agent-based
tools require access to the workloads to install the
discovery agent for data collection. Agentless discovery
requires permission to scan the network and identify
workloads. Identify the least privilege model and apply
accordingly.

For more detail, see the following:

- [AWS Application Discovery Service FAQs](https://aws.amazon.com/application-discovery/faqs/)
- [Discovery, Planning, and Recommendation migration tool details](https://aws.amazon.com/prescriptive-guidance/migration-tools/migration-discovery-tools-details/#awsapplicationdiscovery)

**Suggestion 1.1.2:** Identify and safeguard credentials needed by discovery tools.

Follow the principle of least privilege, granting only the
necessary permissions to discovery tools and their
associated AWS Identity and Access Management (IAM) roles or
users. Use a credential management system, such as AWS Secrets Manager, to limit sharing and proliferations of
credentials. Additionally, limit the use of long-term
credentials when possible.

For more detail, see the following:

- [Least
privilege](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege)
- [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/)

## MIG-SEC-BP-1.2 Understand how the discovery tool works

This BP applies to the following best practice areas: Infrastructure protection

### Implementation guidance

**Suggestion 1.2.1**: Understand the network requirements for discovery tools.

Discovery tools, whether AWS native or partner solutions,
typically leverage 2 types of discovery methodologies: Agent
based discovery or agentless discovery. These 2 methods use
different ports and protocols to collect information. Once
you choose a discovery tool, study the documentation to
understand the networking and potential security and
availability considerations. For example, if the tool uses a
non-standard port, is that port reachable on the assets you
want to assess.

For more detail, refer to the following information:

- [Agent and Agentless discovery tools](https://aws.amazon.com/application-discovery/faqs/)
- [Discovery, Planning, and Recommendation migration tool details](https://aws.amazon.com/prescriptive-guidance/migration-tools/migration-discovery-tools-details/#awsapplicationdiscovery)

## MIG-SEC-BP-1.3 Understand the discovery tool's data security and apply appropriate controls

This BP applies to the following best practice areas: Data
protection

### Implementation guidance

**Suggestion 1.3.1:** Understand what data the discovery tool collects.

Discovery tools collect various pieces of data, such as
server names, IP addresses, allocated and utilized
resources, network ports, and applications installed on the
machine. Organizations should try to limit the collection of
data to only the minimum data types necessary and relevant
to support migration planning.

**Suggestion 1.3.2**: Understand where the discovery data is stored.

Collected data from discovery tools is typically stored
locally within a customer's data center or sent over the
network directly to the tool vendor as a SaaS model.
Understand the tool's data storage capabilities and vendor's
security controls to verify that they align to your data
management, handling, and storage policies. You can also
collect the data and store it locally within your data
center and only share redacted data with AWS or partners for
analysis.

**Suggestion 1.3.3**: Understand how the data is encrypted in transit and at rest.

Different discovery tools come with different security
controls when it comes to how data is encrypted in transit
and at rest. Ensure this meets your organization's security
policy requirements.

**Suggestion 1.3.4**: Get the necessary approval from your security team in your organization to install and use the discovery tool.

After deciding the right discovery tool to use, work with
the security team in your organization to get the necessary
approval to start using the tool. This process make take
time, so plan accordingly.

For more detail, refer to the following information:

- [Selecting the discovery tool for your cloud migration](https://aws.amazon.com/blogs/architecture/selecting-the-appropriate-discovery-tool-for-your-cloud-migration/)

MIG-SEC-02: Have you reviewed and mapped your existing security tools and controls to equivalent AWS services?

Customers moving into AWS can leverage a comprehensive selection
of AWS cloud-native security services. Before migrating to AWS,
it is important to map your on-premise security tools and
controls to those available in your AWS environment. This
includes controls like identity and access management, perimeter
security, encryption tools, network security, data security,
vulnerability management tools, code scanning tools, and threat
detection.

## MIG-SEC-BP-2.1  Perform a tools mapping exercise

This BP applies to the following best practice areas: Infrastructure security

### Implementation guidance

**Suggestion 2.1.1:** Understand the AWS Shared Responsibility Model.

Identify the security controls of resources hosted in AWS, keeping in mind the [AWS Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/) and how this model shifts based on the AWS service being used. While AWS is responsible for the security *of* the cloud, and the customer is responsible for security *in* the cloud, the customer needs to understand how both sides of the shared responsibility model align to any compliance and regulatory requirements. Review the security functionality and configuration options of individual AWS services within the security chapters of [AWS service documentation](https://docs.aws.amazon.com/security/). Customers can view a variety of security and compliance reports created by third-party auditors by using [AWS Artifact](https://docs.aws.amazon.com/artifact/latest/ug/what-is-aws-artifact.html).

**Suggestion 2.1.2**: Map network security tools.

Map network security tools such as firewalls, IDS/IPS, deep
packet inspection, and web application firewalls, and
understand AWS native capabilities. Understand the
difference between networking in AWS and on-premise data
centers, as it is important to apply this to your design and
tools selection. AWS native services can be complemented
with AWS Partner services of choice through the
[AWS Marketplace](https://aws.amazon.com/marketplace/search/?category=3141913d-a073-4452-8473-843f58081505) to reach a desired security posture.

For more detail, see the following:

- [Network and Application Protection](https://aws.amazon.com/free/security/#Network_and_Application_Protection)
- [Detection](https://aws.amazon.com/free/security/#Detection_)

**Suggestion 2.1.3**: Map operating system (OS) level security tools, including third-party tools.

Customers should understand if they can continue to use the
existing OS level security tools in their self-managed EC2
instances or containers. Understand the technical and
licensing limitations of porting those tools to AWS. For
more detail, see
[AWS Systems Manager FAQs](https://aws.amazon.com/systems-manager/faq/).

**Suggestion 2.1.4**: Map on-premises vulnerability management controls.

Map your on-premises vulnerability management security
control policies and requirements to AWS workload
architectures, service capabilities, and controls.

For more detail, see the following:

- [Amazon Inspector](https://aws.amazon.com/inspector/)
- [SEC06-BP01 Perform vulnerability management](https://docs.aws.amazon.com/wellarchitected/latest/framework/sec_protect_compute_vulnerability_management.html)
- [Application Security partner tools](https://aws.amazon.com/marketplace/search/?searchTerms=application+security)

**Suggestion 2.1.5**: Map your on-premises data security control policies and requirements to AWS data and storage architectures, service capabilities, and controls.

Map data security tools and services, such as certificate
management tools, key management, TLS certificates,
encryption tools, and AWS Secret Manager to AWS service
capabilities and controls. For more detail, see
[Data
Protection services](https://aws.amazon.com/free/security/#Detection_).

MIG-SEC-03: Do you have an established compliance framework?

Customers have distinct risk and compliance requirements, based
on factors such as industry, geographical location, customer
base, and governmental and regulatory authorities. The

[AWS Compliance Program](https://aws.amazon.com/compliance/programs/) helps customers understand the robust
controls in place at AWS to maintain security and compliance of
the cloud. By tying together governance-focused, audit-friendly
service features with applicable compliance or audit standards, [AWS Compliance Enablers](https://aws.amazon.com/compliance/resources/) build on traditional programs,
helping customers to establish and operate in an AWS security
control environment.

## MIG-SEC-BP-3.1 Understand, establish, and implement compliance framework

This BP applies to the following best practice areas: Security
foundations

### Implementation guidance

**Suggestion 3.1.1**:
Identify your compliance requirements.

IT standards that AWS complies with are broken out by [Certifications and Attestations](https://aws.amazon.com/compliance/programs/#Certifications_.2F_Attestations.3A), [Laws, Regulations](https://aws.amazon.com/compliance/programs/#Laws_.2F_Regulations.3A) and [Privacy](https://aws.amazon.com/compliance/programs/#Privacy),
and [Alignments and Frameworks](https://aws.amazon.com/compliance/programs/#Alignments_.2F_Frameworks.3A). Compliance certifications
and attestations are assessed by third-party, independent
auditors and result in a certification, audit report, or
attestation of compliance. AWS customers remain responsible
for complying with applicable compliance laws, regulations,
and privacy programs. Compliance alignments and frameworks
include published security or compliance requirements for a
specific purpose, such as a specific industry or function.

For more detail, see the following:

- [AWS Compliance Programs](https://aws.amazon.com/compliance/programs/)
- [AWS Customer Compliance Guides](https://aws.amazon.com/blogs/security/customer-compliance-guides-now-available-on-aws-artifact/)

**Suggestion 3.1.2**:
Determine if you operate and store data in multiple
countries and identify any geography-based compliance
requirements.

An organization's compliance needs can vary depending on the
city, state, country, or even Region. Work closely with your
organization's compliance and legal teams to understand any
regulatory or other compliance requirements, including data
residency and
[digital sovereignty](https://aws.amazon.com/compliance/digital-sovereignty/) requirements.

For more detail, see the following:

- [Compliance FAQs](https://aws.amazon.com/compliance/faq/)
- [Compliance Resources](https://aws.amazon.com/compliance/resources/)
- [Digital Sovereignty at AWS](https://aws.amazon.com/compliance/digital-sovereignty/)

**Suggestion 3.1.3**:
Familiarize yourself with the compliance postures of the AWS
services that make up your solution's architecture.

Security and compliance are a shared responsibility between
AWS and the customer. Depending on the services deployed,
this shared model can help relieve the customer's
operational burden.  AWS is responsible for compliance of
underlying service capabilities, while the customer is
responsible for compliance of the specific implementations.
Use AWS Artifact to look at compliance reports for various
AWS services and assess what you as a customer are
responsible for meeting in terms of compliance and what AWS
as a service provider is responsible for.

For more detail, see the following:

- [AWS Services in Scope by Compliance Program](https://aws.amazon.com/compliance/services-in-scope/)
- [AWS Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/)
- [AWS Artifact](https://aws.amazon.com/artifact/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/migration-lens/assess-sec.html*

---

# Mobilize

During the mobilize phase of the migration, you plan for your
authentication and authorization systems to ensure secure access
to your migrated workloads. This phase also involves building your
AWS environment in alignment with AWS security foundations.
Establishing a secure connection between on-premises and AWS is
essential for safely migrating workloads to AWS. This includes
establishing policies and tools for data encryption at rest and in
transit. Furthermore, it's important to consider any third-party
integrations and align them with the overall security strategy.
These steps collectively enhance the security resilience of the
migration process and prepare the infrastructure for a successful
transition to AWS.

MIG-SEC-04: Do you have an established standard for authentication and authorization?

AWS Identity and Access Management (IAM) provides fine-grained
access control across the entire AWS platform. You can use IAM
to specify who or what can access which services and resources,
and under which conditions. IAM policies let you manage
permissions to your workforce and systems to ensure least
privilege permissions.

[Least privilege](https://docs.aws.amazon.com/wellarchitected/latest/framework/sec-design.html) is an AWS Well-Architected Framework best
practice for building securely in the cloud.

## MIG-SEC-BP-4.1 Implement strong identity and least privilege principles

This BP applies to the following best practice areas: Identity
and access management

### Implementation guidance

**Suggestion
4.1.1:** Protect
and limit the use of the AWS account root user.

It's vital to ensure strong security measures for your AWS account's root user, treating its credentials with the
utmost confidentiality and limitation.  You should regard
your root user credentials with the same seriousness as
vital personal information, deploying them only when
required.

For a comprehensive guide on the best practices surrounding
the AWS root account, see
[Root user best practices for your AWS account](https://docs.aws.amazon.com/accounts/latest/reference/best-practices-root-user.html).

**Suggestion 4.1.2:**
Assess how user identities are managed and authenticated in
AWS.

In the migration process, the selection of a suitable
identity provider (IDP) is essential. This choice determines
how smoothly and securely you can connect to the cloud. When
migrating to AWS, it's crucial to evaluate and optimize how
user identities are managed and authenticated to pick the
most appropriate option based on your long-term
authentication and authorization requirements:

- **AWS Identity and Access Management (IAM):** Define distinct user roles
and permissions tailored to AWS resources. Consider the
enhanced security of AWS multi-factor authentication for
high-priority accounts. IAM's federated capabilities
integrate effortlessly with established identity
systems, like Microsoft Active Directory. Federation
should be leveraged in place of IAM users whenever
feasible. This allows users to authenticate using their
existing credentials, streamlining the authentication
process and simplifying the account management
provisioning and de-provisioning processes.
- **Directory Service:**Facilitate your migration by
integrating with corporate directories, enhancing user
experience and reducing operational burdens.
- **AWS IAM Identity Center:**Centrally coordinate workforce
access, a pivotal asset during the migration phase. AWS
IAM Identity Center is the preferred method for
organizations to federate existing workforce identity
stores.
- **Amazon Cognito:**
Provides customer identity and access management to
applications and workloads.
- **External identity
providers**: While adopting AWS, integrate with
existing IDPs to establish connections. External
identity providers can easily integrate directly with
AWS IAM, AWS IAM Identity Center, and Amazon Cognito.
Manual configuration may be required to provide optimal
connectivity. Regularly synchronize identities to
maintain accurate access controls.

For more detail, see the following:

- [Identity and Access Control](https://docs.aws.amazon.com/whitepapers/latest/introduction-aws-security/identity-and-access-control.html)
- [Require human users to use federation with an identity provider to access AWS using temporary credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-users-federation-idp)
- [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)

**Suggestion
4.1.3:** Implement
a strong privileged access management program and controls.

A key security consideration for the enterprise is
monitoring and administrating elevated access, often known
as privileged access, for business-critical applications
that are running in the AWS Cloud. You need to have a
process to request, fulfill, certify, and govern privileged
assets in the cloud to maintain privileged access management
(PAM). Based on your compliance requirements, you may need
to limit the privileged access to a certain group of
resources or for a specific period of time.

For more detail, see the following:

- [AWS Marketplace for PAM solutions](https://aws.amazon.com/marketplace/search/results?searchTerms=PAM)
- [Temporary elevated access management with IAM Identity Center](https://aws.amazon.com/blogs/security/temporary-elevated-access-management-with-iam-identity-center/)

MIG-SEC-05: Have you built your AWS environment following the AWS recommended security foundations?

As you move into the mobilize phase of the migration journey,
you build the foundational components, such as AWS accounts and
networking and security, before the workloads move to AWS. We
refer to this as building a
[landing zone](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-aws-environment/understanding-landing-zones.html) (not to be confused with AWS Landing Zone Service,
which is part of

[AWS Control Tower](https://aws.amazon.com/controltower/)).

## MIG-SEC-BP-5.1 Implement AWS multi-account structure

This BP applies to the following best practice areas: Security
foundations

### Implementation guidance

**Suggestion
5.1.1:** Understand
and design AWS multi-account structure for isolation
boundaries at the AWS account, VPC, business unit, and
environment levels.

As you adopt AWS, we recommend that you determine how your
business, governance, security, and operational requirements
can be met in AWS. Use of multiple AWS accounts plays an
important role in how you meet those requirements. The use
of multiple accounts allows for benefits like group
workloads based on business purpose and ownership.

Apply distinct security controls by environment, constrain
access to sensitive data, and limit scope of impact from
adverse events.

For more detail, see the following:

- [Building
a landing zone](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-aws-environment/building-landing-zones.html)
- [The
AWS Security Reference Architecture](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/architecture.html)
- [Best
practices for AWS Control Tower administrators](https://docs.aws.amazon.com/controltower/latest/userguide/best-practices.html)
- [Security
in AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/security.html)

**Suggestion 5.1.2:** Take
note of AWS service quotas per AWS account.

Your AWS account has

[default
quotas](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html), formerly referred to as limits, for each AWS
service. Unless otherwise noted, each quota is
Region-specific. You can request increases for some quotas,
and other quotas cannot be increased. As you scale, AWS
multi-account strategy quotas play an important role in
designing multi-account strategy and workload grouping
strategy.

MIG-SEC-06: Have you established secure connectivity in preparation for migrating workloads to AWS?

There are many different mechanisms available for connectivity
between a customer's data center and AWS. Which solution you
choose is dependent on your use case and requirements. For all
solutions, secure connectivity between your on-premises
infrastructure and AWS is paramount during the migration
process. This involves the use of robust strategies for
maintaining data confidentiality and integrity in transit.

## MIG-SEC-BP-6.1 Establish secure connectivity to AWS

This BP applies to the following best practice areas: Data
protection

### Implementation guidance

**Suggestion 6.1.1:** Establish secure data transmission capabilities between on-premise networks and AWS

Create secure data transmission utilizing virtual private networks (VPNs) or dedicated private connections to establish secure network connections for your migration. These connections keep the data confidential and maintain its integrity as it moves between your on-premises environment and AWS. If your organization has compliance requirements for encryption in transit, implement VPN or encryption for connectivity between your data center and AWS. This provides secure transmission of data during the migration process. You might consider using AWS Transit Gateway in conjunction with a VPN to securely connect your on-premise datacenters to your VPCs.

For more detail, see the following:

- [Site-to-Site VPN](https://aws.amazon.com/vpn/)
- [AWS Transit Gateway](https://aws.amazon.com/transit-gateway/)

**Suggestion 6.1.2:** Use
AWS Direct Connect for large bandwidth and dedicated
connectivity

Use
[AWS Direct Connect](https://aws.amazon.com/directconnect/) for stable connectivity for large data
movement with stable bandwidth and low latency network
connectivity. It provides a dedicated, private network
connection from your premises to AWS, which is crucial for
large workload migrations.

**Suggestion 6.1.3:** Use AWS PrivateLink to limit exposure between VPCs and AWS services.

Establish connectivity between VPCs and AWS services without exposing data to the internet using [AWS PrivateLink](https://aws.amazon.com/privatelink/).  [AWS Application Migration Service](https://docs.aws.amazon.com/mgn/latest/ug/AWS-Related-FAQ.html#mgn-and-vpc) interacts with interface [VPC endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html) to establish a private connection between your VPC and AWS Application Migration Service.

## MIG-SEC-BP-6.2: Establish network security controls

This BP applies to the following best practice areas:
Infrastructure protection and Data protection

During the migration process to AWS, it's important to ensure
robust network protection, including the implementation of
intrusion detection and prevention systems (IDS/IPS), as well
as OSI layer 4 to layer 7 security. AWS and the Amazon Partner
Network offer a variety of services that can support these
requirements.

### Implementation guidance

**Suggestion
6.2.1**: Enable
layer 7 Security with AWS Web Application Firewall (WAF) to
protect your web applications from common web exploits.

[AWS WAF](https://aws.amazon.com/waf/) allows you to control how traffic reaches your
applications by creating security rules that block common
attack patterns, such as SQL injection or cross-site
scripting (XSS).  Use

[AWS Shield](https://aws.amazon.com/shield/) for managed Distributed Denial of Service
(DDoS) protection. AWS Shield Advanced provides additional
DDoS protections and capabilities.

**Suggestion 6.2.2:** Use
VPCs and network segmentation.

Use the appropriate network controls to isolate your
applications appropriately. [Virtual Private Clouds (VPCs)](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) allow you to create logically
isolated virtual networks. Within a VPC, you can use [security groups (SGs)](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html) and [network access control lists (NACLS)](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html) that implement inbound
and outbound traffic rules and ensure appropriate
segmentation. For more detail, see [Zero Trust](https://aws.amazon.com/security/zero-trust/).

**Suggestion
6.2.3**: Explore
IDS/IPS solutions in the AWS Marketplace.

Explore third-party IDS/IPS solutions offered in the [AWS Marketplace](https://aws.amazon.com/marketplace/search/results?searchTerms=ids+and+ips). Many of these solutions offer additional
security features and capabilities that can complement those
provided by AWS services. For more detail, see [AWS Network Firewall](https://docs.aws.amazon.com/network-firewall/latest/developerguide/what-is-aws-network-firewall.html).

**Suggestion
6.2.4**:
Identify anomalous network behavior from migrated workloads
using Amazon GuardDuty.

[Amazon GuardDuty](https://aws.amazon.com/guardduty/) monitors your accounts and various
workloads to identify malicious and anomalous behaviors,
including monitoring network and DNS traffic. When migrating
workloads such as virtual machines and containers, Amazon GuardDuty can detect and alert you if those workloads are
attempting to use your network for potentially malicious or
unauthorized activities.

MIG-SEC-07: Do you have policies and tools defined for data encryption at rest during and after migration?

Data at rest represents any data that you persist in
non-volatile storage for any duration in your workload. This
includes block storage, object storage, databases, archives, IoT
devices, and any other storage medium on which data is
persisted. Protecting your data at rest reduces the risk of
unauthorized access, when encryption and appropriate access
controls are implemented. AWS provides robust and scalable
encryption solutions for both data at rest and in transit to
help you meet your data security requirements and compliance
needs.

## MIG-SEC-BP-7.1 Establish security controls for protecting data at rest

This BP applies to the following best practice areas: Data
protection

### Implementation guidance

**Suggestion
7.1.1**:
Classify your data based on its sensitivity

Understand what data is sensitive, confidential, or public.
This helps in applying appropriate security controls. To
effectively manage risk, organizations should consider
[classifying data](https://docs.aws.amazon.com/whitepapers/latest/data-classification/data-classification-overview.html) by working backward from the contextual use of
the data, and creating a [categorization scheme](https://docs.aws.amazon.com/whitepapers/latest/data-classification/using-aws-cloud-to-support-data-classification.html) that takes into account whether a given use
case results in significant impact to an organization's
operations (for example, if data is confidential, it needs
to have integrity, and it needs to be available). Customers
also need to take into account their regulatory and
compliance requirements for protection of data like GDPR.

**Suggestion 7.1.2:** Use
AWS Key Management Service (KMS) for protecting data at
rest.

Protect data at rest by using [AWS Key Management Service (KMS)](https://aws.amazon.com/kms/) to create and control the
cryptographic keys used to encrypt your data. Additionally,
use the built-in encryption capabilities of services like [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingEncryption.html), [Amazon EBS](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html), [Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.html), and [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/security-dataprotection.html#security-privacy-atrest) for protecting data at rest.

**Suggestion 7.1.3:** Use
AWS CloudHSM when compliance dictates.

If compliance requirements dictate the need for
hardware-based cryptographic key storage, commonly referred
to as hardware security models (HSMs), consider

[AWS CloudHSM](https://aws.amazon.com/cloudhsm/). HSMs provided by CloudHSM are FIPS 140-2
level 3 certified.

**Suggestion 7.1.4**: Use
strong IAM policies for key management.

Establish granular IAM policies that explicitly delineate
permissions for activities related to data encryption at
rest. Verify that only trusted roles or users can decrypt
the data or manage encryption keys, further bolstering the
security of your data during and after migration.

For more detail, see the following:

- [AWS IAM Policy Best Practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)
- [AWS Key Management Service (KMS) Best Practices](https://docs.aws.amazon.com/kms/latest/developerguide/best-practices.html)

MIG-SEC-08: Have you identified and applied application security controls?

Protecting applications, hosting environments, and detecting
irregular behavior is critical to a secure cloud environment.
Customers transitioning to AWS have the advantage of tapping
into a comprehensive array of AWS cloud-native application
security services and work on existing applications to match the
overall security posture.

## MIG-SEC-BP-8.1: Establish application layer security controls

This BP applies to the following best practice areas:
Application security

### Implementation guidance

**Suggestion
8.1.1**:
Implement application layer vulnerability scanning.

AWS emphasizes the importance of application security
through comprehensive practices such as regular updates,
vulnerability scanning, penetration testing, and secure
coding principles. Conduct regular scanning and testing to
identify weaknesses within AWS applications and
infrastructure. Use AWS tools like [Amazon Inspector](https://aws.amazon.com/inspector/) for streamlined security assessments.

**Suggestion 8.1.2:**
Implement full-lifecycle secure coding practices and
supporting tools.

Implement secure coding practices for applications within
AWS, leveraging code review and proper methodologies. Use
AWS services such as [AWS CodeGuru](https://aws.amazon.com/codeguru/) for enhanced code quality insights and
security. Use [Amazon CodeWhisperer](https://docs.aws.amazon.com/codewhisperer/latest/userguide/security-scans.html) to provide additional security context
and recommendations within your IDE as you write your
application code. For more detail, see [Building a secure CICD pipeline](https://aws.amazon.com/blogs/devops/building-end-to-end-aws-devsecops-ci-cd-pipeline-with-open-source-sca-sast-and-dast-tools/).

**Suggestion 8.1.3**:
Perform threat modeling.

Identify and prioritize risks using a [threat model](https://aws.amazon.com/blogs/security/how-to-approach-threat-modeling/). Use a threat model to identify and maintain an
up-to-date register of potential threats. Prioritize your
threats and adapt your security controls to prevent, detect,
and respond. Revisit on a recurring basis and maintain this
in the context of the evolving security landscape.

**Suggestion
8.1.4**:
Implement customer identity and access management for your
applications that target non-workforce users.

Implement a customer identity and access management (CIAM)
solution that allows your customers and end-users (like
non-employee accounts) to access your application securely.
Use
[Amazon Cognito](https://aws.amazon.com/cognito/), which is designed to handle the scale and
full lifecyle of CIAM account management, or consider
various partner CIAM solutions in the [AWS Marketplace](https://aws.amazon.com/marketplace). Additionally, use [Amazon Verified Permissions (AVP)](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/what-is-avp.html) for scalable, fine-grained
permissions management and authorization service for custom
applications built by you.

## MIG-SEC-BP-8.2: Optimize application security with AWS Application Migration Service

This BP applies to the following best practice areas:
Application security

### Implementation guidance

**Suggestion
8.2.1**:
Automate the migration and conversion processes using
AWS-provided services.

Use the
[AWS Application Migration Service](https://aws.amazon.com/application-migration-service/) (MGN) to convert source
servers to run natively on AWS, streamlining the conversion
and migration processes and minimizing manual errors. This
provides a seamless transition through a tested
non-interactive and secure conversion, introduces automation
for post-migration configurations, and optimizes
applications to benefit from robust AWS infrastructure.

**Suggestion
8.2.2**:
Modernize and enhance your application.

During migration, take advantage of the service's in-built
options such as disaster recovery, OS or license conversion,
and cloud-native capabilities. This ensures applications are
not just migrated but also modernized to meet contemporary
security and operational standards.

MIG-SEC-9: Do you have a data backup and disaster recovery strategy during migration?

Data backups are an essential element of data security. In the
context of migration to AWS, planning for data backup and
disaster recovery is critical to assure business continuity and
protect against data loss. These concepts are covered in more
details in the Reliability pillar of this document. AWS provides
several services that can help with data backup and restoration,
as well as managing and testing disaster recovery plans.

## MIG-SEC-BP-9.1: Establish a data backup and restore strategy

This BP applies to the following best practice areas: Data
protection

### Implementation guidance

**Suggestion
9.1.1:** Implement
and test backup and recovery capabilities.

Use [AWS Backup](https://aws.amazon.com/backup/) to create backup plans, which define when and
how often backups are created and how long they're stored.
Regularly test backup restoration to test that your backup
strategy is effective and backups are usable in case of data
loss or system failure.

**Suggestion
9.1.2:** Audit
and validate your backup requirements.

Use [AWS Backup Audit Manager](https://docs.aws.amazon.com/aws-backup/latest/devguide/aws-backup-audit-manager.html) to audit the compliance of your
AWS Backup policies against controls you define. Audit and
identify issues regarding backup schedules, which resources
are being backed up, and any non-compliance against the
controls you set up can be reported and leveraged for
remediation.

## MIG-SEC-BP-9.2: Establish a Disaster recovery plan

This BP applies to the following best practice areas: Data
protection and Infrastructure protection

### Implementation guidance

**Suggestion
9.2.1:** Develop
and test a disaster recovery plan and capabilities.

Leverage [AWS Elastic Disaster Recovery](https://aws.amazon.com/disaster-recovery/?nc2=type_a) to minimize downtime and
data loss with fast, reliable recovery of physical, virtual,
and cloud-based servers into AWS. Use the [AWS Well-Architected Framework Reliability Pillar](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html) to
design, deploy, and manage workloads and align them with
disaster recovery strategies and requirements.

MIG-SEC-10: Have you established monitoring controls with the right set of tools?

Establishing robust monitoring controls for security is
essential to detect and respond to potential security threats in
your AWS environment. By implementing comprehensive monitoring
controls, you can gain visibility into activities, monitor for
unusual behavior, and proactively identify security incidents.

## MIG-SEC-BP-10.1: Validate and use AWS native monitoring tools.

This BP applies to the following best practice areas: Incident
response

### Implementation guidance

**Suggestion
10.1.1:** Develop
and deploy a comprehensive logging strategy

An effective logging strategy is a cornerstone of any
successful migration to AWS. By leveraging the right
combination of AWS and third-party tools, you can maintain
full visibility into your infrastructure and ensure your
operations are running smoothly.

For more detail, see the following:

- [Getting started with AWS CloudTrail tutorials](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-tutorial.html)
- [Setting Up AWS Config with the Console](https://docs.aws.amazon.com/config/latest/developerguide/gs-console.html)
- [Getting set up (Amazon CloudWatch)](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/GettingSetup.html)
- [Analyze Network Traffic of Amazon Virtual Private Cloud (VPC) by CIDR blocks](https://aws.amazon.com/blogs/networking-and-content-delivery/analyze-network-traffic-of-amazon-virtual-private-cloud-vpc-by-cidr-blocks/)
- [Considerations for the security operations center in the cloud: deployment using AWS security services](https://aws.amazon.com/blogs/security/considerations-for-the-security-operations-center-in-the-cloud-deployment-using-aws-security-services/)
- [Logging strategies for security incident response](https://aws.amazon.com/blogs/security/logging-strategies-for-security-incident-response/)

## MIG-SEC-BP-10.2: Explore cloud native AWS partner monitoring tools

This BP applies to the following best practice areas: Incident
response

### Implementation guidance

**Suggestion
10.2.1:** Deploy
application monitoring capabilities.

Alongside AWS tools such as
[AWS X-Ray](https://aws.amazon.com/xray/), consider [third-party
partner tools](https://aws.amazon.com/marketplace/) which provide application-level
insights and monitoring on AWS. They can supplement AWS
services and help create a more holistic monitoring strategy
tailored to your business needs.

MIG-SEC-11: Do you have any third-party integrations?

When integrating third-party services into your AWS migration,
it's crucial to review the security features, permissions, and
data handling practices of these services to maintain a secure
and compliant migration process. Review their security practices
and verify that they align with your organization's security
requirements.

## MIG-SEC-BP-11.1: Perform third-party integration due diligence

This BP applies to the following best practice areas: Security
foundations

### Implementation guidance

**Suggestion 11.1.1:**
Review third-party integration patterns and security
practices.

When reviewing third-party integration patterns, conduct
thorough due diligence and consider engaging with the vendor
directly to discuss their security practices and address any
specific security concerns you may have. Additionally,
consult the AWS Shared Responsibility Model to understand
the division of security responsibilities between AWS and
third-party service providers.

Review the following checklist in regard to third-party
integrations:

- **Authentication and
authorization:** The third-party should
supports secure mechanisms like multi-factor
authentication (MFA) and role-based access control
(RBAC).
- **Data encryption**:
Confirm encryption both in transit (using TLS) and at
rest with robust algorithms.
- **Compliance and
certifications**: Assess adherence to standards
like SOC 2, ISO 27001, and other relevant industry
certifications.
- **Data privacy and
residency**: Verify that data handling aligns
with organizational privacy policies and legal
regulations.
- **Logging and
monitoring:** Review capabilities for security
analysis and incident response visibility.
- **Security incident
response:** Understand incident management,
customer communication, and resolution speed.
- **Third-party audits and
assessments:** Request information on security
tests and independent reviews undergone.
- **Data backup and
recovery**: Check mechanisms against data loss.
- **Service-level agreements
(SLAs):** Check that they fulfill
organizational needs in terms of availability,
performance, and security.
- **Integration with AWS
services:** Verify that AWS integration adheres
to security best practices.
- **Vendor reputation and
support:** Research vendor credibility,
reviews, and their support effectiveness.
- **Continual security
updates:** Confirm timely vulnerability
addressing and update provision.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/migration-lens/mobilize-sec.html*

---

# Migrate

As the migration progresses, security remains top priority. It's
essential to understand the data security and compliance,
establish a secure credential mechanism, and have robust
mechanisms in place for monitoring, identifying, and responding to
any security incidents or anomalies. This involves not only
employing the right tools, but also training teams and preparing
them to respond effectively. In this phase, you also implement
mechanisms to protect the migrated resources of compute, network,
databases and applications.

MIG-SEC-12: Have you performed a security review of your migration tools?

When using AWS migration tools to move data and applications
from on-premises or other cloud environments to AWS, it's
essential to consider security throughout the migration process.
This section contains key security considerations when using AWS
migration tools.

## MIG-SEC-BP-12.1: Understand the data security and compliance

This BP applies to the following best practice areas: Data
protection

### Implementation guidance

**Suggestion 12.1.1:**
Verify data encryption and integrity.

Data transferred during the migration process should be
[encrypted
in transit](https://docs.aws.amazon.com/prescriptive-guidance/latest/encryption-best-practices/welcome.html). [AWS migration tools](https://docs.aws.amazon.com/whitepapers/latest/overview-aws-cloud-data-migration-services/overview-aws-cloud-data-migration-services.html), such as AWS DataSync, [AWS Database Migration Service](https://repost.aws/knowledge-center/validation-feature-dms), and [AWS Application Migration Service](https://aws.amazon.com/application-migration-service/) support TLS encryption
to secure data as it moves between your on-premise and AWS
environments. Verify the integrity of data during migration
by using cryptographic hashes or checksums. This helps
detect any unauthorized changes or tampering during transit.

**Suggestion 12.1.2:
Implement** secure
credential management.

Safeguard access credentials used by migration tools. Follow
the principle of [least
privilege](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege), granting only the necessary permissions to
migration tools and their associated IAM roles or users. Use
a credential management system, such as [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/), to limit sharing and proliferations
of credentials. Also, limit the use of long-term credentials
when possible, and use [IAM
Roles Anywhere](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/introduction.html) to prevent the need for storage
secrets.

MIG-SEC-13: How do you detect and investigate security events?

Migrating your workloads from on-premises to AWS also requires
you to update your security detection and investigation
processes. Detective controls, crucial for governance and
compliance, help identify potential threats and support threat
identification and response. These controls include asset
inventory for informed decision-making (you must know what
resources you have so you know how to protect them) and internal
auditing of information systems to align practices with policies
and correctly set automated alerting notifications. Such
controls are pivotal in pinpointing and understanding anomalous
activity.

## MIG-SEC-BP-13.1: Understand AWS service capabilities for event detection and investigation

This BP applies to the following best practice areas: Incident
response

### Implementation guidance

**Suggestion
13.1.1:** Configure
service and application logging.

Retain [security
event logs](https://docs.aws.amazon.com/prescriptive-guidance/latest/logging-monitoring-for-application-owners/logging-applications-aws-cloud.html) from services and applications, a
fundamental principle for audit, investigations, and
operational use cases. This retention must be in line with
governance, risk, and compliance (GRC) requirements and
industry-specific standards. Ahead of security
investigations, capture logs to reconstruct AWS account
activity. Select [log
sources](https://docs.aws.amazon.com/prescriptive-guidance/latest/logging-monitoring-for-application-owners/aws-services-logging-monitoring.html) pertinent to your workloads based on your
business use cases and any regulatory or compliance
requirements you may have. Establish a logging trail for
each AWS account, and in each region using [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/best-practices-security.html) or an AWS Organizations trail, store logs
in a dedicated and centralized Amazon S3 bucket.

**Suggestion 13.1.2:**
Analyze logs, findings, and metrics centrally.

As you migrate to AWS, security operations teams should use
advanced data search and analytics tools, especially given
the volume of data from complex architectures and
applications. Reliance on manual data analysis is not suited
for the majority of most customer security requirements and
could impact your ability to investigate potential security
issues in a timely manner. Use services such as [AWS Security Hub CSPM](https://aws.amazon.com/security-hub/) to aggregate security events and alerts
from other security services, evaluate your security
posture, and automate remediations. [Amazon
Detective](https://aws.amazon.com/detective/) can help you investigate security events by
contextualizing events in relationship across several
service and log sources.

For more detail, see the following:

- [Collect, analyze, and display Amazon CloudWatch Logs in a single dashboard with the Centralized Logging on AWS solution](https://docs.aws.amazon.com/solutions/latest/centralized-logging-on-aws/solution-overview.html)
- [Amazon Security Lake](https://aws.amazon.com/security-lake/)
- [AWS Security Competency Partners](https://aws.amazon.com/security/partner-solutions/#Logging_and_Monitoring)
- [Searching
and analyzing logs in CloudWatch](https://docs.aws.amazon.com/prescriptive-guidance/latest/implementing-logging-monitoring-cloudwatch/cloudwatch-search-analysis.html)

**Suggestion
13.1.3:** Automate
and implement the response to security events.

Using [automation](https://aws.amazon.com/solutions/implementations/automated-security-response-on-aws/)
to investigate and remediate events reduces human effort and
error, [quickens
responses](https://docs.aws.amazon.com/whitepapers/latest/aws-security-incident-response-guide/detection.html), and allows you to scale investigation
capabilities. Regular reviews help you tune automation tools
and continually iterate. AWS provides guidance on how this
can be achieved using a combination of AWS security services
and patterns. Consider the impact to the availability of
your workloads carefully when implementing security
automations, as you may not be able to fully automate all [remediation
activities](https://youtu.be/nyh4imv8zuk).

For more detail, see [Threat management in the cloud: Amazon GuardDuty and AWS Security Hub CSPM](https://youtu.be/vhYsm5gq9jE).

MIG-SEC-14: Do you have security incident response capabilities in place?

To migrate your security incident response capabilities from
on-premises to AWS, careful planning and adopting cloud-native
practices are essential. It's crucial to understand AWS security
incident response concepts, prepare and educate your teams, and
identify automation-based remediation methods for faster and
more consistent responses. Additionally, it is key to understand
your compliance and regulatory requirements for your security
incident response program, and how they relate to building a
security incident response program to fulfill those
requirements.

## MIG-SEC-BP-14.1: Understand AWS best practices for incident response

This BP applies to the following best practice areas: Incident
response

### Implementation guidance

**Suggestion
14.1:** Develop and test an incident response plan.

The first document to develop for incident response is the
[incident
response plan](https://docs.aws.amazon.com/whitepapers/latest/aws-security-incident-response-guide/detection.html), which is designed to serve
as the foundation for your incident response program. It
typically includes:

- **An incident response team
overview**: Outlines the goals and functions of
the incident response team.
- **Roles and
responsibilities**: Lists stakeholders and
their incident roles.
- **A communication plan**:
Details contact information and how to communicate
during incidents. Emphasizes the best practice of having
out-of-band communication as a
backup.

[AWS Wickr](https://aws.amazon.com/wickr/) can be used as a secure out-of-band
communications channel.
- **Phases of incident response and
actions to take**: Enumerates response phases
(like detect, analyze, eradicate, contain, and recover)
and associated high-level actions.
- **Incident severity and
prioritization definitions**: Explains incident
severity classification, prioritization, and their
impact on escalation procedures.

While these sections are common, each organization's plan is
unique and should be tailored accordingly.

MIG-SEC-15: How do you protect your compute and network resources in AWS?

Compute resources that support your workloads require multiple
layers of defense to help protect from external and internal
threats. Compute resources include EC2 instances, containers,
AWS Lambda functions, database services, and IoT devices.

## MIG-SEC-BP-15.1: Protect your network resources

This BP applies to the following best practice areas:
Infrastructure protection

### Implementation guidance

**Suggestion 15.1.1:** Create
a layered networking architecture with isolation boundaries.

Components such as Amazon Elastic Compute Cloud (Amazon EC2)
instances, Amazon Relational Database Service (Amazon RDS)
database clusters, and AWS Lambda functions that share
reachability requirements can be segmented into layers
formed by subnets. Consider deploying serverless workloads,
such as [Lambda](https://docs.aws.amazon.com/lambda/index.html)
functions, within a VPC or behind an [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html). [AWS Fargate](https://aws.amazon.com/fargate/getting-started/) tasks (and all other compute workloads) that
have no need for internet access should be placed in subnets
with no route to or from the internet. This layered approach
mitigates the impact of a single layer misconfiguration,
which could allow unintended access. For AWS Lambda, you can
run your functions in your VPC to take advantage of
VPC-based controls. Regardless of your workload type, it is
imperative to understand the data flow between layers of
your application, and implement the controls necessary to
restrict ingress and egress traffic to only authorized users
and services.

For more detail, see the following:

- [Well-Architected
Lab - Automated Deployment of VPC](https://catalog.workshops.aws/well-architected-security/en-US/4-infrastructure-protection/automated-deployment-of-vpc)
- [Amazon VPC | AWS Security Blog](https://aws.amazon.com/blogs/security/tag/amazon-vpc/)

**Suggestion 15.1.2:** Create centralized policies for network security.

Use [AWS Firewall Manager](https://aws.amazon.com/firewall-manager/) to centrally configure and manage your network security policies across all accounts and applications in your organization, simplifying the administration of AWS WAF, AWS Shield Advanced, AWS Network Firewall, and [Amazon VPC](https://www.wellarchitectedlabs.com/security/200_labs/200_automated_deployment_of_vpc/) security groups.

With [AWS Network Firewall](https://aws.amazon.com/network-firewall/), you can define firewall rules that
provide fine-grained control over network traffic. Network Firewall works together with AWS Firewall Manager, so you
can build policies based on Network Firewall rules and then
centrally apply those policies across your virtual private
clouds (VPCs) and accounts.

MIG-SEC-16: What are your authentication and authorization processes for applications and databases?

When migrating databases and applications to AWS, it's essential
to have robust authentication and authorization controls to
secure access to sensitive data. AWS offers several services and
best practices to achieve this.

## MIG-SEC-BP-16.1: Manage authentication for applications and databases

This BP applies to the following best practice
areas:

[Identity
and access management](https://docs.aws.amazon.com/wellarchitected/latest/container-build-lens/identity-and-access-management.html)

### Implementation guidance

**Suggestion 16.1.1**:
Consider more secure database authentication
and authorization methods.

When moving databases to AWS managed services, such as RDS
(Relational Database Service) and Aurora databases, you can
enable

[IAM
database authentication](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.IAMDBAuth.html). This allows you to use IAM
roles instead of static or [hard
coded credentials](https://docs.aws.amazon.com/secretsmanager/latest/userguide/hardcoded-db-creds.html) to authenticate and access the
databases, improving security by removing the need to manage
database passwords. Define database-level roles and
permissions to control access to specific tables, views, and
stored procedures within your databases.

**Suggestion 16.1.2**:
Consider stronger application authentication and
authorization mechanisms for applications.

Implement strong authentication mechanisms for your
applications. Use protocols like OAuth 2.0 or OpenID Connect
for web applications, and consider token-based
authentication for APIs. Implement [role-based
access control (RBAC)](https://aws.amazon.com/identity/) within your applications. Map
AWS IAM roles to application roles, and control access to
application features and data based upon business need. [Verified Permissions](https://aws.amazon.com/verified-permissions/) can also be leveraged to help
manage permissions and fine-grained authorizations in
applications.

**Suggestion 16.1.3**:
Use AWS Secrets Manager
for storing credentials.

Use [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/) to manage, retrieve, and rotate
database credentials, application credentials, OAuth tokens,
API keys, and other secrets throughout their lifecycles.
Secrets Manager helps you improve your security posture,
because you no longer need [hard-coded
credentials](https://docs.aws.amazon.com/secretsmanager/latest/userguide/hardcoded-db-creds.html) in application source code. Storing the
credentials in Secrets Manager helps avoid possible
compromise by anyone who can inspect your application or the
components.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/migration-lens/migrate-sec.html*

---

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
