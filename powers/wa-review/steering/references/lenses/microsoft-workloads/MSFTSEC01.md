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
