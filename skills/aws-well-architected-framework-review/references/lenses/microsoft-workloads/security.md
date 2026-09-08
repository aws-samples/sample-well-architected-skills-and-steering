# Security

**Pillar**: Security  
**Questions**: 3

---

# MSFTSEC01 — Workload security

**Pillar**: Security  
**Best Practices**: 3

---

# MSFTSEC01-BP01 Protect the operating system

Securing the operating system that hosts your Microsoft application
is crucial in blocking unauthorized access, securing software
availability, and maintaining the stability of your critical
systems. By following Microsoft and AWS recommendations for Windows
Server environments, you can reduce the risk of malicious attacks.

This is particularly important when using unmanaged or
non-serverless services. Implementing these best practices creates a
robust foundation for your Microsoft workload, enhancing overall
security and resilience. Remember that a well-protected operating
system forms a critical layer in your defense strategy, safeguarding
your application and data from potential threats.

**Desired outcome:** Establish a
hardened Windows Server environment that follows security best
practices, implements proper access controls, and maintains
up-to-date security configurations to protect your Microsoft
workload from operating system-level threats and vulnerabilities.

**Common anti-patterns:**

- Using default Windows Server configurations without implementing
security hardening measures, leaving systems vulnerable to
common attack vectors and exploitation techniques.
- Failing to implement proper user account management and access
controls, allowing excessive privileges or shared accounts that
increase security risks and make it difficult to track user
activities.
- Neglecting to configure Windows Firewall and network security
settings appropriately, potentially exposing unnecessary
services or ports to network-based attacks.

**Benefits of establishing this best
practice:**

- Reduced attack surface through proper system hardening,
disabling unnecessary services, and implementing security
configurations that minimize potential entry points for
malicious actors.
- Enhanced access control and accountability through proper user
account management, role-based access controls, and audit
logging that tracks system access and changes.
- Improved regulatory posture by implementing security baselines
and configurations that align with industry standards and
regulatory requirements for Windows Server environments.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Protecting the Windows Server operating system requires a
systematic approach to security hardening that addresses user
accounts, services, network configuration, and system monitoring.
Start by implementing Microsoft security baselines and
AWS-recommended configurations, then customize these settings
based on your specific workload requirements. This comprehensive
approach verifies that your Windows Server instances provide a
secure foundation for your Microsoft applications while
maintaining operational functionality.

### Implementation steps

- Apply Microsoft Security Baselines for Windows Server using
Group Policy or local security policies to establish
fundamental security configurations.
- Configure Windows Firewall with appropriate rules that allow
only necessary network traffic and block potentially
malicious connections.
- Implement proper user account management with strong
password policies, account lockout settings, and regular
review of user privileges.
- Disable unnecessary Windows services and features that are
not required for your Microsoft workload to reduce the
attack surface.
- Configure Windows Event Logging to capture security events,
system changes, and access attempts for monitoring and audit
purposes.
- Enable Microsoft Windows Defender on your EC2 instances
running Windows Server for local anti-malware protection.
- Implement regular security assessments using AWS Systems Manager Compliance or third-party security scanning tools.
- Establish automated patch management processes using AWS Systems Manager Patch Manager to keep the operating system
current with security updates.

## Resources

**Related documents:**

- [Security
best practices for Windows instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-windows-security-best-practices.html)
- [Add
optional Windows Server components to Amazon EC2 Windows
instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/windows-optional-components.html)
- [Security
baselines](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-security-baselines)

**Related tools:**

- [AWS Systems Manager Patch Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager.html)
- [AWS Systems Manager Compliance](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-compliance.html)
- [Windows
Security Baseline](https://www.microsoft.com/en-us/download/details.aspx?id=55319)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftsec01-bp01.html*

---

# MSFTSEC01-BP02 Secure the Microsoft application and database

Maintaining strong security at both the database and application
layers is crucial, as even read-only access by malicious actors
could compromise critical business data. To protect your Microsoft
environment, implement security best practices including the least
access principle, least privilege model, encryption at rest, and
encryption in transit. These measures help safeguard your Microsoft
application and database against unauthorized access and potential
data breaches, maintaining the confidentiality and integrity of your
business-critical information.

**Desired outcome:** Establish
comprehensive security controls for Microsoft applications and
databases that implement defense in depth strategies, proper access
controls, and encryption mechanisms to protect sensitive data and
block unauthorized access at the application and database layers.

**Common anti-patterns:**

- Using default database and application configurations without
implementing security hardening, leaving systems vulnerable to
common attack vectors such as SQL injection, privilege
escalation, and unauthorized data access.
- Implementing overly permissive database and application access
controls that grant excessive privileges to users or
applications, violating the principle of least privilege and
increasing the risk of data breaches.
- Storing sensitive data in plaintext or using weak encryption
methods, making it vulnerable to exposure if the database or
application is compromised or if data is intercepted during
transmission.

**Benefits of establishing this best
practice:**

- Enhanced data protection through comprehensive encryption
strategies that secure sensitive information both at rest and in
transit, reducing the risk of data exposure even if systems are
compromised.
- Improved access control and audit capabilities through
implementation of least privilege principles and detailed
logging, enabling better monitoring of data access patterns and
potential security incidents.
- Reduced attack surface through application and database
hardening measures that eliminate common vulnerabilities and
implement security best practices specific to Microsoft
technologies.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Securing Microsoft applications and databases requires a
multi-layered approach that addresses authentication,
authorization, encryption, and monitoring. Focus on implementing
Microsoft SQL Server security features alongside AWS security
services to create a comprehensive protection strategy. This
includes configuring proper access controls, enabling encryption
mechanisms, and establishing monitoring capabilities that provide
visibility into application and database activities.

### Implementation steps

- Configure SQL Server authentication using Windows
Authentication mode or mixed mode with strong password
policies and account management practices.
- Implement database-level security through proper user roles,
schema permissions, and row-level security where appropriate
for your Microsoft SQL Server environment.
- Enable SQL Server audit logging to track database access,
data modifications, and administrative activities for
compliance and security monitoring.
- Configure application-level security controls including
input validation, output encoding, and secure session
management for .NET applications.
- Implement database connection security using encrypted
connections (SSL/TLS) and connection string protection
mechanisms.
- Enable SQL Server security features such as dynamic data
masking for sensitive data protection and Always Encrypted
for client-side encryption.
- Configure network security controls including database
firewall rules and network segmentation to limit database
access to authorized sources.
- Establish regular security assessments and vulnerability
scanning for both applications and databases using AWS and
Microsoft security tools.

## Resources

**Related documents:**

- [Security
best practices for Microsoft SQL Server on AWS](https://docs.aws.amazon.com/sql-server-ec2/latest/userguide/security-sql-server-on-ec2.html)
- [Security
Best Practices for Modernizing .NET Framework Applications on
AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-net-applications-security/)

**Related tools:**

- [SQL
Server Management Studio](https://docs.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms)
- [AWS Database Migration Service](https://aws.amazon.com/dms/)
- [Amazon RDS for SQL Server](https://aws.amazon.com/rds/sqlserver/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftsec01-bp02.html*

---

# MSFTSEC01-BP03 Develop a comprehensive software update strategy

Microsoft regularly releases scheduled security updates and
emergency patches to address vulnerabilities. Stay informed about
the latest security advisories from relevant vendors. It's crucial
to keep your Microsoft application and its underlying components
up-to-date with the latest security fixes on a regular schedule to
avoid security gaps. Develop a plan for applying critical emergency
patches when released. Consider implementing automated processes to
streamline this update process, which keeps your Microsoft
environment secure and current with minimal manual intervention.

**Desired outcome:** Establish an
automated and systematic approach to patch management that verifies
Microsoft workloads receive timely security updates while
maintaining system stability and minimizing downtime through proper
testing and deployment procedures.

**Common anti-patterns:**

- Applying patches without proper testing or staging procedures,
potentially introducing system instability or breaking critical
applications during production deployments.
- Delaying security updates for extended periods due to fear of
system disruption, leaving systems vulnerable to known exploits
and security threats that could have been avoided.
- Managing patches manually across multiple systems without
automation, leading to inconsistent patch levels, missed
updates, and increased administrative overhead that doesn't
scale effectively.

**Benefits of establishing this best
practice:**

- Reduced security vulnerabilities through timely application of
security patches and updates, minimizing the window of exposure
to known threats and exploits targeting Microsoft technologies.
- Improved operational efficiency through automated patch
management processes that reduce manual effort, maintain
consistency across environments, and provide better visibility
into patch compliance status.
- Enhanced system stability and reliability through structured
testing and deployment procedures that validate patches before
production deployment, reducing the risk of patch-related
outages or application failures.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Developing a comprehensive software update strategy requires
balancing security needs with operational stability. Implement a
structured approach that includes automated patch management,
testing procedures, and emergency response capabilities.

Use AWS Systems Manager Patch Manager to automate routine updates
while maintaining control over critical systems through approval
processes and maintenance windows. For Windows instances in
private subnets without internet connectivity, consider
implementing Windows Server Update Services (WSUS) in public
subnets to provide local patch distribution while still using
Systems Manager for orchestration and compliance monitoring.

### Implementation steps

- Establish patch management policies that define update
schedules, testing requirements, and approval processes for
different types of systems and environments.
- Configure AWS Systems Manager Patch Manager to automate
patch deployment with appropriate maintenance windows and
approval workflows.
- Create staging environments that mirror production systems
for testing patches before deployment to critical workloads.
- Set up patch groups and baselines in Systems Manager to
manage different update requirements for various system
types and criticality levels.
- Implement monitoring and alerting for patch compliance
status using AWS Systems Manager Compliance and Amazon CloudWatch dashboards.
- Establish emergency patch procedures for critical security
vulnerabilities that require immediate attention outside of
normal maintenance windows.
- Configure automated rollback procedures and system snapshots
before patch deployment to enable quick recovery if issues
occur.
- Create regular reporting mechanisms to track patch
adherence, update success rates, and identify systems that
require attention.

## Resources

**Related documents:**

- [AWS Systems Manager Patch Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager.html)
- [Microsoft
Security Update Guide](https://msrc.microsoft.com/update-guide/)

**Related tools:**

- [AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html)
- [Windows
Server Update Services (WSUS)](https://docs.microsoft.com/en-us/windows-server/administration/windows-server-update-services/get-started/windows-server-update-services-wsus)
- [Microsoft
Update Catalog](https://www.catalog.update.microsoft.com/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftsec01-bp03.html*

---

# MSFTSEC02 — Access management

**Pillar**: Security  
**Best Practices**: 2

---

# MSFTSEC02-BP01 Align your Microsoft workload access with organizational identity strategy

Microsoft workloads, including .NET applications and SQL Server
environments, typically integrate with Active Directory (AD) or
similar identity management systems. A centralized approach to user
management, regardless of the specific solution, can significantly
reduce security risks and operational complexity. This comprehensive
approach enhances security, streamlines user access, and provides a
consistent identity management experience across your Microsoft
workloads in the cloud.

**Desired outcome:** Establish a
unified identity management strategy that integrates Microsoft
workloads with organizational identity systems, providing
centralized authentication, authorization, and user lifecycle
management while maintaining security and operational efficiency
across cloud and on-premises environments.

**Common anti-patterns:**

- Creating isolated identity silos for different Microsoft
workloads without integration with centralized identity systems,
leading to inconsistent access controls and increased
administrative overhead.
- Implementing local user accounts on individual systems instead
of using centralized identity management, making it difficult to
maintain consistent security policies and user lifecycle
management.
- Failing to implement multi-factor authentication (MFA) and
single sign-on (SSO) capabilities, resulting in weaker security
posture and poor user experience across Microsoft applications.

**Benefits of establishing this best
practice:**

- Enhanced security through centralized identity management that
enables consistent policy enforcement, better access control,
and improved visibility into user activities across your
Microsoft workloads.
- Reduced operational complexity through unified user lifecycle
management, automated provisioning and deprovisioning, and
streamlined access request and approval processes.
- Improved user experience through single sign-on capabilities
that reduce password fatigue while maintaining strong
authentication requirements including multi-factor
authentication.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

When designing your identity strategy for Microsoft environments
in AWS, consider using AWS services and compatible third-party
tools to implement centralized user management, single sign-on
(SSO) capabilities, and multi-factor authentication (MFA).
Aligning Microsoft workload access with organizational identity
strategy requires careful planning and integration between AWS
services, Microsoft identity technologies, and existing
organizational systems. Focus on establishing trust relationships,
implementing proper authentication mechanisms, and providing a
simple-to-use user experience while maintaining security controls.

**Note:** While local service
accounts or isolated identity management may be necessary in
specific technical scenarios, these approaches should be
considered a last resort when centralized identity integration is
not feasible. Local accounts increase security risks,
administrative overhead, and compliance challenges. Always
prioritize integration with organizational identity providers and
use temporary credentials whenever possible, as recommended by AWS
security best practices.

### Implementation steps

- Assess current organizational identity infrastructure and
determine integration requirements for Microsoft workloads
on AWS:

Document existing Active Directory schema, domains, and
trust relationships.
- Map out current authentication flows and identify
Microsoft applications requiring integration.

- Choose appropriate Directory Service option (AWS Managed Microsoft AD, AD Connector, or Active Directory on EC2)
based on your organizational needs and existing
infrastructure:

Compare directory service options against requirements
(scale, features, management overhead).
- Evaluate cost implications and licensing requirements
for each option.
- Conduct proof-of-concept testing with selected directory
service option.

- Establish trust relationships between AWS-hosted Active
Directory and on-premises Active Directory domains if hybrid
connectivity is required:

Configure VPN or Direct Connect for secure hybrid
connectivity.
- Set up forest and domain trusts and verify DNS
resolution between environments.
- Test authentication flows across trusted domains.

- Configure single sign-on (SSO) using AWS IAM Identity Center
or compatible third-party solutions to provide unified
access across Microsoft applications:

Set up AWS IAM Identity Center integration with chosen
directory service.
- Configure application-specific SSO connectors for
Microsoft workloads.
- Test SSO flows for required applications.

- Implement multi-factor authentication (MFA) for user
accounts accessing Microsoft workloads using AWS IAM Identity Center MFA capabilities, which support various
authentication methods including TOTP, SMS, email, and
passwordless options like Windows Hello for Business and
FIDO2 security keys, or integrate with AWS Managed Microsoft AD using RADIUS-based MFA solutions:

Define MFA policies and enforcement rules.
- Configure selected MFA methods in AWS IAM Identity Center or RADIUS.
- Test MFA enrollment and authentication processes.

- Set up automated user provisioning and deprovisioning
processes that integrate with HR systems and organizational
identity management workflows:

Design user lifecycle workflows and approval processes.
- Implement SCIM or PowerShell-based provisioning scripts.
- Configure integration between HR systems and AWS
directory service.

- Configure role-based access control (RBAC) that aligns with
organizational roles and responsibilities while following
least privilege principles:

Define role hierarchy and permission sets.
- Create security groups and implement group-based
assignments.
- Document and implement approval workflows for role
changes.

- Establish monitoring and auditing capabilities to track
identity-related activities and adhere to organizational
security policies:

Configure CloudWatch logging for directory service
events.
- Set up alerts for suspicious authentication activities.
- Implement regular compliance reporting and access
reviews.

## Resources

**Related documents:**

- [Directory
services options in AWS](https://docs.aws.amazon.com/whitepapers/latest/active-directory-domain-services/directory-services-options-in-aws.html)
- [Security
considerations for Active Directory Domain Services on
AWS](https://docs.aws.amazon.com/whitepapers/latest/active-directory-domain-services/security-considerations.html)
- [Directory Service](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/what_is.html)

**Related tools:**

- [AWS IAM Identity Center](https://aws.amazon.com/iam/identity-center/)
- [AWS Managed Microsoft AD](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/directory_microsoft_ad.html)
- [Active
Directory Federation Services (ADFS)](https://docs.microsoft.com/en-us/windows-server/identity/active-directory-federation-services)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftsec02-bp01.html*

---

# MSFTSEC02-BP02 Implement logging to track access and authorization changes

Regularly log, analyze, and audit user access and authorization
events in your Microsoft systems. Consolidate security events from
Microsoft applications and databases with other architectural
components to enable comprehensive tracing during security
incidents. Implement a centralized security information and event
management (SIEM) system to automate event analysis, allowing your
operations team to identify unusual or suspicious activities.

This integrated approach to security monitoring enhances your
ability to detect and respond to potential threats across your
entire Microsoft environment, strengthening your overall security
posture and enabling more effective incident management.

**Desired outcome:** Establish
comprehensive logging and monitoring capabilities that capture,
analyze, and correlate access and authorization events across
Microsoft workloads, enabling rapid detection of security incidents
and providing detailed audit trails for compliance and forensic
analysis.

**Common anti-patterns:**

- Collecting logs from individual systems without centralized
aggregation and correlation, making it difficult to identify
patterns or conduct comprehensive security analysis across the
Microsoft environment.
- Focusing only on successful authentication events while ignoring
failed attempts, authorization changes, and privilege
escalations that could indicate security threats or policy
violations.
- Storing logs locally on individual systems without proper
retention, backup, or protection mechanisms, risking log loss
during security incidents when they are most needed for
investigation.

**Benefits of establishing this best
practice:**

- Enhanced threat detection through comprehensive logging that
captures authentication attempts, authorization changes, and
access patterns, enabling early identification of suspicious
activities and potential security breaches.
- Improved incident response capabilities through centralized log
aggregation and correlation that provides security teams with
complete visibility into user activities and system events
during security investigations.
- Strengthened regulatory posture through detailed audit trails
that document user access, privilege changes, and administrative
activities, supporting regulatory requirements and internal
security policies.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Implementing comprehensive access and authorization logging
requires a systematic approach to log collection, centralization,
and analysis. Focus on capturing relevant security events from
each Microsoft workload component while protecting, retaining, and
documenting for analysis and compliance purposes.

### Implementation steps

- Configure Windows Event Logging on your Microsoft workload
systems to capture security events, including authentication
attempts, privilege changes, and administrative activities.
- Enable SQL Server audit logging to track database access,
permission changes, and data access patterns for
comprehensive database security monitoring.
- Set up Amazon CloudWatch Logs or AWS CloudTrail to collect
and centralize logs from Microsoft workloads running on AWS
infrastructure.
- Configure log forwarding from Microsoft applications and
databases to a centralized SIEM solution such as Amazon
Security Lake or third-party security platforms.
- Implement log parsing and normalization for consistent event
formats, enabling effective correlation across different
Microsoft technologies and AWS services.
- Set up automated alerting and monitoring rules to detect
suspicious access patterns, failed authentication attempts,
and unauthorized privilege escalations.
- Establish log retention policies that meet regulatory
requirements while balancing storage costs and operational
needs for security analysis.
- Create regular reporting and analysis procedures to review
access patterns, identify security trends, and validate the
effectiveness of access controls.

## Resources

**Related documents:**

- [Security
Best Practices for Modernizing .NET Framework Applications on
AWS - Application Logging](https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-net-applications-security/logging.html)
- [AWS Security Best Practices](https://docs.aws.amazon.com/wellarchitected/latest/framework/sec-detection.html)

**Related tools:**

- [Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html)
- [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html)
- [Amazon
Security Lake](https://aws.amazon.com/security-lake/)
- [SQL
Server Audit](https://docs.microsoft.com/en-us/sql/relational-databases/security/auditing/sql-server-audit-database-engine)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftsec02-bp02.html*

---

# MSFTSEC03 — Data protection

**Pillar**: Security  
**Best Practices**: 3

---

# MSFTSEC03-BP01 Encrypt data stored in Microsoft workloads

Data at rest encompasses the entirety of your digitally stored
information. Encryption is crucial to verify that this data remains
visible only to authorized users and stays protected, even if
storage or database access is compromised independently of the
application. For Microsoft SQL Server environments, consider
implementing Transparent Data Encryption (TDE). This technology
provides robust encryption at rest solution specifically designed
for Microsoft databases, offering strong protection for sensitive
data without significant changes to your application architecture.

By employing these encryption methods, you enhance the security of
your stored data, mitigating risks associated with unauthorized
access and potential data breaches in your Microsoft SQL Server
deployments.

**Desired outcome:** Implement
comprehensive encryption at rest for sensitive data stored in
Microsoft workloads, protecting data even if underlying storage
systems are compromised while maintaining application performance
and operational efficiency.

**Common anti-patterns:**

- Storing sensitive data in plaintext without any encryption
protection, leaving it vulnerable to unauthorized access if
storage systems or database files are compromised.
- Implementing encryption inconsistently across different data
stores or only encrypting some sensitive data while leaving
other critical information unprotected.
- Using weak encryption algorithms or poor key management
practices that could be compromised, effectively negating the
security benefits of encryption.

**Benefits of establishing this best
practice:**

- Enhanced data protection through strong encryption that renders
data unreadable to unauthorized users even if they gain access
to storage systems or database files.
- Improved regulatory posture by meeting regulatory requirements
for data protection that mandate encryption of sensitive
information at rest.
- Reduced impact of security incidents through encryption that
limits the value of stolen data and reduces the scope of
potential data breaches.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

When encrypting Microsoft workloads at rest, start with
Windows-based solutions like SQL Server TDE to protect databases
and files. Establish a secure key management process and monitor
performance metrics to maintain application responsiveness.

### Implementation steps

- Identify each data store containing sensitive information in
your Microsoft workload, including SQL Server databases,
file systems, and application data repositories.
- Enable Transparent Data Encryption (TDE) on SQL Server
databases to encrypt data files, log files, and backup files
at the database level.
- Configure AWS Key Management Service (KMS) or SQL Server key
management to securely store and manage encryption keys with
proper access controls.
- Implement file system encryption using Amazon EBS encryption
for EC2 instance storage volumes.
- Enable encryption for backup files and verify that database
backups maintain encryption protection during storage and
transfer operations.
- Configure application-level encryption for sensitive data
fields that require additional protection beyond
database-level encryption.
- Establish key rotation policies and procedures to regularly
update encryption keys while maintaining data accessibility
and system availability.
- Monitor encryption status and key usage through logging and
alerting mechanisms to maintain continuous protection and
detect any encryption failures.

## Resources

**Related documents:**

- [Best
Practices for Deploying Microsoft SQL Server on Amazon EC2 -
Encryption at Rest](https://docs.aws.amazon.com/whitepapers/latest/best-practices-for-deploying-microsoft-sql-server/security-optimization.html#encryption-at-rest)
- [SQL
Server Transparent Data Encryption](https://docs.microsoft.com/en-us/sql/relational-databases/security/encryption/transparent-data-encryption)

**Related tools:**

- [AWS Key Management Service (KMS)](https://aws.amazon.com/kms/)
- [Amazon EBS Encryption](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-encryption.html)
- [BitLocker
Drive Encryption](https://docs.microsoft.com/en-us/windows/security/information-protection/bitlocker/bitlocker-overview)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftsec03-bp01.html*

---

# MSFTSEC03-BP02 Enable Always Encrypted feature for SQL Server

Microsoft SQL Server's *Always Encrypted* feature
provides robust data protection using client-side encryption with
certificates. This technology creates a clear separation between
data owners who can view the information and data managers who
shouldn't have access. It effectively safeguards sensitive data by
encrypting it in the database, during transit, and even while being
processed. Always Encrypted is available not only in on-premises SQL
Server deployments but also in cloud environments, including Amazon RDS for SQL Server and SQL Server instances running on Amazon EC2.
By implementing Always Encrypted, organizations can enhance their
data security posture, particularly when handling sensitive
information in Microsoft SQL Server environments on AWS.

**Desired outcome:** Implement
client-side encryption capabilities that protect sensitive data
throughout its entire lifecycle, keeping data encrypted even during
processing and is only accessible to authorized applications and
users with proper decryption keys.

**Common anti-patterns:**

- Processing sensitive data in plaintext within applications or
databases, exposing it to potential compromise during
computation or memory access by unauthorized processes.
- Implementing encryption in use inconsistently across different
data types or applications, leaving some sensitive information
vulnerable during processing operations.
- Using client-side encryption without proper key management or
secure key distribution mechanisms, potentially compromising the
security benefits of the encryption implementation.

**Benefits of establishing this best
practice:**

- Maximum data protection through encryption that maintains data
confidentiality even during processing operations, verifying
that sensitive information is never exposed in plaintext to
unauthorized systems or users.
- Enhanced separation of duties between data owners and data
managers, allowing database administrators to manage systems
without accessing sensitive business data.
- Improved regulatory capabilities for highly regulated industries
that require the highest levels of data protection, including
protection during data processing operations.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

When implementing Always Encrypted, first identify which sensitive
data elements truly need this protection layer. Then map out where
to apply based on your data flows and access patterns. Evaluate
feature limitations and potential performance impacts before
proceeding, as encryption/decryption operations can affect
response times and resource usage.

### Implementation steps

- Identify highly sensitive data elements that require
protection during processing, such as personally
identifiable information (PII), financial data, or
healthcare records.
- Configure SQL Server Always Encrypted for identified
sensitive columns, choosing appropriate encryption types
(deterministic or randomized) based on query requirements.
- Set up certificate-based key management for Always
Encrypted, and properly store and distribute keys to
authorized client applications.
- Modify client applications to handle encrypted data
operations, including proper connection string configuration
and query modifications.
- Implement secure key provisioning mechanisms that allow
authorized applications to access encryption keys while
blocking unauthorized access.
- Configure column master keys and column encryption keys with
appropriate permissions and access controls to maintain
separation of duties.
- Test application functionality with encrypted data for
proper operation and performance while maintaining data
protection.
- Establish monitoring and auditing procedures to track key
usage, encryption operations, and access to sensitive
encrypted data.

## Resources

**Related documents:**

- [Best
Practices for Deploying Microsoft SQL Server on Amazon EC2 -
Encryption in Use](https://docs.aws.amazon.com/whitepapers/latest/best-practices-for-deploying-microsoft-sql-server/security-optimization.html#encryption-in-use)
- [SQL
Server Always Encrypted](https://docs.microsoft.com/en-us/sql/relational-databases/security/encryption/always-encrypted-database-engine)

**Related tools:**

- [SQL
Server Management Studio](https://docs.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms)
- [Always
Encrypted Wizard](https://docs.microsoft.com/en-us/sql/relational-databases/security/encryption/always-encrypted-wizard)
- [Azure
Key Vault](https://azure.microsoft.com/en-us/services/key-vault/) (for hybrid scenarios)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftsec03-bp02.html*

---

# MSFTSEC03-BP03 Use Trusted Platform Module (TPM) technology for hardware-based security on your instances

The AWS Nitro Trusted Platform Module (NitroTPM) is a virtual TPM
2.0 device that's fully integrated with the AWS Nitro System,
providing hardware-based security features for EC2 instances running
Windows Server 2016 and later, as well as supported Linux
distributions. It enables secure boot functionality, disk
encryption, and enhanced protection of sensitive data and keys
directly through the operating system.

When enabled on instance launch, NitroTPM allows Windows to use
BitLocker disk encryption, measured boot capabilities, and Windows
Hello for Business authentication. The TPM functionality is
implemented through the Nitro security chip, which processes
cryptographic operations and sensitive key material in an isolated,
hardware-protected environment separate from the instance's CPU and
hypervisor. This hardware-based root of trust helps meet
requirements for regulated workloads and supports Windows security
features that require TPM 2.0, including Windows Defender System
Guard, Credential Guard, and Device Guard.

NitroTPM integrates with Windows' built-in security tools and
third-party applications that rely on TPM capabilities, making it
particularly valuable for enterprises requiring enhanced security
posture for their Windows workloads on AWS. Additionally, NitroTPM
supports attestation capabilities, allowing applications to verify
the integrity and authenticity of the platform, which is essential
for zero-trust architectures and confidential computing scenarios.

**Desired outcome:** Implement
hardware-based security capabilities through TPM technology that
provides a secure foundation for cryptographic operations, secure
boot processes, and enhanced protection of sensitive keys and
credentials in Microsoft workloads on AWS.

**Common anti-patterns:**

- Deploying Windows workloads without enabling TPM capabilities,
missing opportunities to use hardware-based security features
that provide stronger protection than software-only solutions.
- Using software-based encryption and key storage without the
additional security layer provided by hardware security modules,
potentially exposing keys to compromise through software
vulnerabilities.
- Failing to integrate TPM capabilities with Windows security
features, limiting the effectiveness of built-in security
technologies that depend on hardware-based trust anchors.

**Benefits of establishing this best
practice:**

- Enhanced security through hardware-based cryptographic
operations that provide stronger protection for encryption keys
and sensitive data compared to software-only solutions.
- Improved compliance capabilities through hardware-based
attestation and secure boot features that help meet regulatory
requirements for high-security environments.
- Strengthened Windows security features through TPM integration
that enables advanced capabilities like Credential Guard, Device
Guard, and Windows Hello for Business authentication.

**Level of risk exposed if this best practice
is not established:** Low

## Implementation guidance

Implementing TPM technology for Microsoft workloads requires
enabling NitroTPM during EC2 instance launch and configuring
Windows security features to use the hardware-based capabilities.
Focus on integrating TPM with existing security controls and
Windows features to maximize security benefits.

### Implementation steps

- Enable NitroTPM when launching new EC2 instances running
Windows Server 2016 or later, verifying that the instance
type supports TPM functionality and is built on the AWS
Nitro System.
- Deploy EC2 Instances with NitroTPM Using AWS CloudFormation.
- Integrate AWS KMS with NitroTPM for Enhanced Key Management
for runtime attestation and system integrity protection
against firmware and kernel-level attacks.
- Configure AWS Systems Manager for TPM-enabled Microsoft
workloads to secure credential storage and certificate-based
authentication capabilities.
- Implement Credential Guard to protect domain credentials and
other sensitive authentication information using TPM-based
virtualization security.
- Set up secure boot functionality that uses TPM to verify the
integrity of the boot process and block unauthorized code
execution during startup.
- Configure monitoring and logging using AWS CloudTrail,
Amazon CloudWatch, and Windows event logs to track TPM
usage, key operations, and security events related to
hardware-based security features.
- Establish procedures for TPM endorsement key management and
disaster recovery, understanding that NitroTPM keys are
instance-specific and require proper backup strategies for
encrypted data.
- Implement AWS IAM Roles Anywhere for certificate-based
authentication.

## Resources

**Related documents:**

- [Amazon EC2 now supports NitroTPM and UEFI Secure Boot](https://aws.amazon.com/blogs/aws/amazon-ec2-now-supports-nitrotpm-and-uefi-secure-boot/)
- [Credential
Guard for Windows instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/credential-guard.html)
- [Windows
TPM 2.0 Overview](https://docs.microsoft.com/en-us/windows/security/information-protection/tpm/trusted-platform-module-overview)

**Related tools:**

- [IAM
Roles Anywhere Credential Helper - GitHub Repository](https://github.com/aws/rolesanywhere-credential-helper)
- [IAM
Roles Anywhere Credential Helper - Configuration
Examples](https://github.com/aws/rolesanywhere-credential-helper/tree/main/examples)
- [BitLocker
Drive Encryption](https://docs.microsoft.com/en-us/windows/security/information-protection/bitlocker/bitlocker-overview)
- [Windows
Defender System Guard](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-system-guard/system-guard-how-hardware-based-root-of-trust-helps-protect-windows)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftsec03-bp03.html*

---

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
