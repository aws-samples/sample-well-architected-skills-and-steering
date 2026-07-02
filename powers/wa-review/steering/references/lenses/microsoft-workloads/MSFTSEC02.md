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
