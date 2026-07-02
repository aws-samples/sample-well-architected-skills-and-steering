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
