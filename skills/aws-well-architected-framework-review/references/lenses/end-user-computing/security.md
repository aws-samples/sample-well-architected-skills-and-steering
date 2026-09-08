# Security

**Pillar**: Security  
**Questions**: 15

---

# EUCSEC01 — Security foundations

**Pillar**: Security  
**Best Practices**: 1

---

# EUCSEC01-BP01 Identify discrete groups of users that require access and implement security controls appropriate for their risk profiles

When modelling user access to computing systems, it is important
to consider different risk profiles associated with discrete
groups of users. For example, internal employees and external
contractors will have different risk profiles associated with
them. Because of their risk profile, different security controls
should be applied to the groups of users.

**Level of risk exposed if this best
practice is not established:** High

## Implementation guidance

Create a group to manage users associated with each risk
profile. If different discrete sets of users will be
interacting with the AWS EUC services, take a risk-based
approach to determine the risk profile associated with each
group. The groups being considered here are broader than other
AWS services, as you need to consider users across multiple
lines of business each with their own discrete risk profiles
in addition to the standard administrators, developers, and
operators.

Based on the risk profile, implement different security
controls to mitigate residual risks within the groups of
users. A matrix can be used to assess the risks associated
with users. For example, in a scenario where four groups of
internal and external users will be accessing the EUC
services, a 2x2 matrix can be created that captures the type
of users on one axis (for example, internal or external) and
the risk profile of the group of users on the other (for
example, high or low risk). By populating the matrix with the
different groups, you can determine the appropriate risk
posture and apply the appropriate level of security controls
for the user group, such as enforcing multi-factor
authentication. An example matrix is shown in the following
figure for groups of internal and external users that will
access a computing service.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucsec01-bp01.html*

---

# EUCSEC02 — Security foundations

**Pillar**: Security  
**Best Practices**: 1

---

# EUCSEC02-BP01 Identify external stakeholders and their security or regulatory compliance requirements

When creating and configuring an end user computing environment,
verify that the regulatory requirements for the users of your
environment are met. Consider the broader regulatory frameworks
and their associated requirements in relation to accessibility
that may be in scope for users with specific accessibility
requirements.

**Level of risk exposed if this best
practice is not established:** High

## Implementation guidance

Determine internal and external policies that are applicable
to your environment. To help identify stakeholders external to
the organization, consider the following groups of potential
sources of policy:

- Government
- Legal (for example, employment law, health and safety
regulation, financial regulation, or accessibility)
- Industry (for example, financial services regulators)

By considering each of these groups, you can assess the
different potential sources of regulatory compliance for
relevance against the applications being delivered, as well as
the data they process and visualize.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucsec02-bp01.html*

---

# EUCSEC03 — Security foundations

**Pillar**: Security  
**Best Practices**: 1

---

# EUCSEC03-BP01 Restrict user permissions to the minimum required to perform their role

To implement the principle of least privilege when configuring
AWS EUC services, define appropriate access controls for role
categories like users, service desk users, first-level
administrators, second-level administrators, and accounts used
for automation.

**Level of risk exposed if this best
practice is not established:** High

## Implementation guidance

- **Limit the use of administrator
permissions:** Users should not be granted local
administrator access to Amazon WorkSpaces or WorkSpaces Applications
instances unless it is required for them to undertake
their role. Use tools and products that provide the
ability to temporarily provide elevated rights in
preference to granting users long term administrative
access.
- **Do not provide all support staff
with administrator permissions:** Grant service
desk users should the minimal set of access permissions to
allow them to perform their function. This can vary among
organizations, but service desk users should not be
granted full access to the Amazon WorkSpaces and AppStream
2.0 services.
- **Use administrative toolsets and
automation to avoid the need to provide administrator
permissions:** Administrators providing
first-level support for the users consuming the AWS EUC
service can use the enhanced administrative toolset that
AWS offers in the form of the EUC toolkit. For more detail
on the EUC Toolkit, see
[Use EUC Toolkit to manage Amazon WorkSpaces Applications and Amazon WorkSpaces](https://aws.amazon.com/blogs/desktop-and-application-streaming/euc-toolkit/).
- **Audit and monitor privileged or
sensitive operations:** Log any privileged or
sensitive operations associated with the management of AWS
EUC services. These logs can then be used to generate
alerts as required.
- **Use temporary elevated access for
privileged or sensitive operations:** When users
occasionally require elevated or privileged access to
support or operate the environment, provide a way for them
to gain temporary elevated access. For an example of
temporary elevated access to AWS IAM Identity Center, see
[Temporary
elevated access for AWS accounts](https://docs.aws.amazon.com/singlesignon/latest/userguide/temporary-elevated-access.html).
- **Restrict the allocation and use of
IAM permissions providing service access:**
Administrators providing second or third-level support
that use the AWS Management console require IAM
permissions. Grant the minimal set of permissions to
administrative users providing an enhanced level of
support to users using
[Amazon WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-access-control.html) and

[AppStream
2.0](https://docs.aws.amazon.com/appstream2/latest/developerguide/controlling-administrator-access-with-policies-roles.html) for them to fulfill their role.
- **Restrict the scope of access for
service accounts:** Restrict permissions for
service accounts for Amazon WorkSpaces (with Active
Directory Connector) and Amazon WorkSpaces Applications (with
domain-joined fleets) to only allow them to create
computer objects within their designated Organizational
Unit (OU). For implementing service accounts, see
[Amazon
WorkSpaces Applications Active Directory Administration](https://docs.aws.amazon.com/appstream2/latest/developerguide/active-directory-admin.html#active-directory-permissions) and

[AD
Connector prerequisites](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/prereq_connector.html#connect_delegate_privileges).

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucsec03-bp01.html*

---

# EUCSEC04 — Identity and access management

**Pillar**: Security  
**Best Practices**: 1

---

# EUCSEC04-BP01 Separate end user systems between different groups of users when required to satisfy policy or regulatory requirements

Many organizations have security requirements that mandate the
segregation of systems accessed and interacted with by end users
from servers that perform an infrastructure or application
hosting function. Regardless of whether there is a specific
security requirement, end user systems should be segregated from
each other. This is for multiple reasons including reducing the
risk of unintended access and exposure to unsafe software.

**Level of risk exposed if this best
practice is not established:** High

## Implementation guidance

- **Use distinct AWS accounts to
separate EUC services from other AWS workloads:**
Separate AWS EUC workloads deployed to an AWS account from
application and infrastructure servers and services that
are consumed by the EUC workloads using different AWS accounts. You can use
[AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html) and

[AWS Organizations](https://docs.aws.amazon.com/organizations/) are two services to implement and
manage a multi-account structure in your AWS environment.
Create an AWS account for EUC workloads and use other
accounts for infrastructure and application services. For
more detail, see
[SEC01-BP01
Separate workloads using accounts](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_securely_operate_multi_accounts.html).
- **Use
[IAM
roles with WorkSpaces Applications](https://docs.aws.amazon.com/appstream2/latest/developerguide/using-iam-roles-to-grant-permissions-to-applications-scripts-streaming-instances.html#how-to-use-iam-role-with-streaming-instances) to enable access to AWS
services**: To access AWS services from an
WorkSpaces Applications instance, use an IAM role and verify that
the IAM policy attached to it is scoped to the specific
services required. This approach avoids the need for users
in WorkSpaces Applications sessions to have access with additional
credentials. If groups of users require differing levels
of access to other AWS services, consider creating an
additional role for each set of permissions. To help
determine the least privilege policies based on the needed
access, analyze user access with AWS IAM Access Analyzer.
For further detail, see
[Use IAM Access Analyzer policy generation to grant fine-grained permissions for your AWS CloudFormation service roles](https://aws.amazon.com/blogs/security/use-iam-access-analyzer-policy-generation-to-grant-fine-grained-permissions-for-your-aws-cloudformation-service-roles/).
- **Restrict access to only authorized
applications**: By default, WorkSpaces Applications allows
users or applications to start programs on the instance,
beyond what is specified in the image application catalog.
This is useful when your application relies on another
application as part of a workflow, but it may be
undesirable for the user to be able to start that
dependent application directly. For example, an
application starts the browser to provide help
instructions from an application vendor's website, but the
ability for the user to start the browser directly must be
blocked.

In some situations, it can be desirable to
control which applications can be launched on streaming
instances. Microsoft AppLocker is application control
software that uses explicit control policies to enable, or
disable, the applications a user can run. An alternative
to Microsoft AppLocker is FSLogix Application Masking
which is available with Windows desktop and server
operating systems. The
[use
of application entitlements with WorkSpaces Applications](https://docs.aws.amazon.com/appstream2/latest/developerguide/manage-application-entitlements.html) can
restrict the ability of users to launch only authorized
applications, but this control by itself does not prevent
the launch of other applications on WorkSpaces Applications
instances. To achieve this, we recommend the two preceding
approaches AppLocker or FSLogix.
- **Secure access to the S3 buckets
used by Amazon WorkSpaces Applications:** Review, maintain,
and update S3 bucket policies as appropriate. These
reviews should verify that restricted access is in place
to protect S3 buckets that are created and used to persist
user data for both home folders and application settings
persistence when enabled. This blocks non-WorkSpaces Applications
administrators from accessing the data. Use S3 bucket
policies and IAM policies together. For more information,
see
[IAM Policies and Bucket Policies and ACLs! Oh, My! (Controlling Access to S3 Resources)](https://aws.amazon.com/blogs/security/iam-policies-and-bucket-policies-and-acls-oh-my-controlling-access-to-s3-resources/).

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucsec04-bp01.html*

---

# EUCSEC05 — Identity and access management

**Pillar**: Security  
**Best Practices**: 1

---

# EUCSEC05-BP01 Evaluate applications and data access requirements and implement entitlements accordingly

Assess the types of users, their associated risk profile, and
the access that each group of users requires to understand the
access permissions each group of users require. Map the
requirements to security groups, such as Active
Directory security groups and the required permissions granted
to these groups. Continually maintain the users associated with
the group to verify ongoing appropriate access to applications
and data.

**Level of risk exposed if this best
practice is not established:** High

## Implementation guidance

- **Automate user
entitlements**: Use a provisioning and
entitlement system that automates the addition and removal
of users from groups that provide role-based permissions
access. Automation creates consistency in the approach for
handling permissions.
- **Use templates for user
creation:** Use templates when creating user
accounts to avoid manual configuration of user groups and
settings that may lead to overly permissive access.
- **Review user entitlements
regularly**: Review user entitlements regularly
to verify that they are aligned with each user's current
role and access requirements to fulfill the role. Consider
a regular cadence, such as a quarterly or monthly review.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucsec05-bp01.html*

---

# EUCSEC06 — Identity and access management

**Pillar**: Security  
**Best Practices**: 1

---

# EUCSEC06-BP01 Rely on a centralized authentication system that satisfies security requirements for your EUC environment

Evaluate your organization's security policies to determine the
requirements that authentication systems need to provide for end
users accessing EUC services.

**Level of risk exposed if this best
practice is not established:** High

## Implementation guidance

- **Use authentication providers
configured for best practices**: Consider the
following regarding authentication of users accessing AWS
EUC services using Microsoft Active Directory or an
authentication provider:

Use a strong password policy.
- Use multi-factor authentication (MFA) to provide
additional protection to end users in your
environment. For Amazon WorkSpaces and WorkSpaces Applications
environments integrated with a SAML IdP, enable MFA in
the IdP. For Amazon WorkSpaces Personal where a SAML
IdP is not in use, implement a RADIUS server to
provide the MFA capability.
- Consider adding password expiration policy to require
users to change their passwords regularly.
- When using a SAML identity provider (IdP), consider
enabling advanced features like geo-restrictions and
conditional access.
- Using a corporate managed (and HR linked) identity
provider improves security by automatically
propagating role and permission changes to the EUC
environment. It also promotes the best practice of
managing access based on user lifecycle.

- **Users should be authenticated and
authorized to access EUC services**: Use an
authentication system, such as a SAML 2.0 IdP or Microsoft
Active Directory, to authenticate users prior to them
accessing an AWS EUC service. Verifying authenticating or
authorization checks that only entitled users can access
the applications and data accessible from Amazon WorkSpaces and WorkSpaces Applications instances.
- **Manage user entitlements using
groups where possible**: Use groups within Active
Directory or your authentication provider instead of
granting access to individual users. This approach
simplifies the administration process and helps you
perform access reviews and updates more efficiently.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucsec06-bp01.html*

---

# EUCSEC07 — Detection

**Pillar**: Security  
**Best Practices**: 1

---

# EUCSEC07-BP01 Monitor user access to EUC instances and aggregate logs in central location

Record events generated when users access systems to a central
system to log attempted and successful user authentication, as
well as access to applications. Prior to implementation,
consider that the use of a central system for security events
may be subject to local regulation and legal framework.

Events logged in the central system should include the following
data attributes:

- Timestamps
- User ID
- IP address
- Outcome of access attempt (success or failure)

Additional attributes or metadata may be required for compliance
reasons. Evaluate any applicable regulatory and organizational
security policy requirements to determine the complete set of
attributes to record.

For completeness, consider all possible sources of events,
including:

- Service-emitted events and logs (for example, Amazon WorkSpaces EventBridge events and WorkSpaces Applications usage
reports)
- Data plane logs collected through agents installed onto
Amazon WorkSpaces or WorkSpaces Applications instances

For Windows instances, use events recorded in the Windows
security log alongside a log management system to collect and
aggregate data from various sources, such as other text-based
logs, network devices, and security applications. This
integration provides a deeper insight into potential security
issues so that your organization can address them.

**Level of risk exposed if this best
practice is not established:** High

## Implementation guidance

Use agents on Amazon WorkSpaces Applications and Amazon WorkSpaces
instances to aggregate security logs. If instance security
logs need to be captured from WorkSpaces Applications instances, then
event forwarding agents such as Amazon CloudWatch, Amazon Kinesis Agent for Windows, or Telegraf can be used to forward
relevant events into the central security logging system.

For WorkSpaces, these agents can be pre-installed into a
WorkSpaces custom bundle to make sure a logging capability is
available before users attempt to access WorkSpaces. For
WorkSpaces Applications, these agents need to be installed into the
Image Builder for On-Demand and Always-On fleets.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucsec07-bp01.html*

---

# EUCSEC08 — Detection

**Pillar**: Security  
**Best Practices**: 1

---

# EUCSEC08-BP01 Install endpoint protection software on instances to detect unexpected behavior

Endpoint protection software can provide the capability to
detect anomalous behavior on end user computing services.

**Level of risk exposed if this best
practice is not established:** High

## Implementation guidance

- **Configure security software for
Amazon WorkSpaces Applications:** If you choose to install
security software (for example, anti-virus or behavioral
anomaly detection) on your image, we recommend that you do
not enable automatic updates for the software. Otherwise,
the software may attempt to update itself with the latest
definition or configuration files or other updates during
user sessions, which can affect performance. In addition,
updates made to the software will not persist beyond the
current user session. To verify that your fleet instances
have the latest updates, we recommend that you do either
of the following:

Update your image builder and create a new image on a
regular basis (for example, by using the Image
Assistant CLI operations).
- Use security software that delegates scanning,
detection, or other operations to an continuously
updated external server.
- For more detail, see
[Administer
Your Amazon WorkSpaces Applications Images](https://docs.aws.amazon.com/appstream2/latest/developerguide/administer-images.html#windows-update-antivirus-software-av) and

[Best
Practices for Deploying Amazon WorkSpaces Applications](https://docs.aws.amazon.com/whitepapers/latest/best-practices-for-deploying-amazon-appstream-2/security-1.html).

- **Configure security software for Amazon WorkSpaces:** Security software can adversely affect the operation of Amazon WorkSpaces if it is not configured to consider the requirements of the service. For details on the configuration elements that are required to be considered as exclusions for anti-malware scanning, see [Required configuration and service components for WorkSpaces Personal](https://docs.aws.amazon.com/workspaces/latest/adminguide/required-service-components.html).

The configuration of endpoint security software should verify that the status of the agents deployed on Amazon WorkSpaces is centralized to provide a consolidated view of the status of the deployed Amazon WorkSpaces.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucsec08-bp01.html*

---

# EUCSEC09 — Detection

**Pillar**: Security  
**Best Practices**: 1

---

# EUCSEC09-BP01 Verify that your instances are configured as expected

Unexpected configuration changes to end user systems can help
you identify possible threat actors. Users should not need to
reconfigure applications or operating systems for the daily use
of their application portfolio.

**Level of risk exposed if this best
practice is not established:** High

## Implementation guidance

Automate configuration management tools to verify compliance.
Use centralized control and enforcement of configuration
settings applied to Amazon WorkSpaces and WorkSpaces Applications
instances to verify that configuration settings align with the
desired configuration of instances.

- For Active Directory domain-joined Windows instances, use
Group Policy Objects (GPOs) to apply a known configuration
to instances.
- For Amazon WorkSpaces Linux instances, consider
configuration management tools such as Ansible, Chef, and
Puppet to apply a known configuration.
- For Amazon WorkSpaces Applications On-Demand and Always-On fleets,
apply desired configuration settings to the instance used
to create the Image for the associated fleet.

After deployment, you can audit Amazon WorkSpaces Personal
instances to determine if the expected and desired
configuration of instances is in effect or whether this has
been overridden or tampered with. Configuration management
tools such as Ansible, Chef, and Puppet can help with this, as
can PowerShell Desired State Configuration.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucsec09-bp01.html*

---

# EUCSEC10 — Infrastructure protection

**Pillar**: Security  
**Best Practices**: 2

---

# EUCSEC10-BP01 Implement network separation for AWS EUC instances

Separating end user systems from infrastructure, application
servers, and data at the network level verifies that you can
enforce minimal access between systems to help prevent
unauthorized access to data and applications.

**Level of risk exposed if this best
practice is not established:** High

## Implementation guidance

Enforce network separation between user instances and other
services. EUC instances provided by Amazon WorkSpaces or
WorkSpaces Applications usually have network connectivity to other
workloads in the same network subnet. The use of security
groups within VPCs can restrict lateral movement and are
recommended for implementation. For defense-in-depth, non-end
user instances such as application servers, authentication
providers, and other infrastructure services should reside on
subnets different to those where user instances reside.

You can apply security controls to the non-end user instances
at various points using AWS capabilities, such as separate AWS accounts and VPCs, VPC endpoints, proxy servers, and network
firewalls. Review network security best practices for
[WorkSpaces](https://d1.awsstatic.com/whitepapers/best-practices-vpcs-networking-amazon-workspaces-deployments.pdf)
and

[AppStream
2.0](https://docs.aws.amazon.com/appstream2/latest/developerguide/what-is-appstream.html) to improve security posture in your EUC
environment.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucsec10-bp01.html*

---

# EUCSEC10-BP02 Restrict access to open ports on instances to reduce risks

Restrict use of network ports on end user systems to reduce the
potential exposure surface of these systems. Block network ports
that aren't required for the operation and support of end user
systems using host-based or network firewalls.

**Level of risk exposed if this best
practice is not established:** High

## Implementation guidance

Implement networking security controls on Amazon EUC
instances. AWS provides several services and capabilities that
can help you secure AWS EUC instances for Amazon WorkSpaces
and WorkSpaces Applications. In addition to these services, consider OS
capabilities and additional software to provide the required
level of security.

For AWS networking, the following services and features should
be evaluated:

- Network ACLs
- Security groups
- AWS Network Firewall
- NAT Gateway

Consider these services to create a baseline of network
security. Additionally, review and explore
[best
practices for VPC and networking in WorkSpaces](https://d1.awsstatic.com/whitepapers/best-practices-vpcs-networking-amazon-workspaces-deployments.pdf), as well
as
[best practices for deploying WorkSpaces Applications](https://docs.aws.amazon.com/whitepapers/latest/best-practices-for-deploying-amazon-appstream-2/best-practices-for-deploying-amazon-appstream-2.html), as you evaluate
your network security.

In addition to AWS security capabilities and services, when
users require access to the Internet from browsers installed
in Amazon WorkSpaces or WorkSpaces Applications instances, consider
using a web proxy to log web site access and implement
restrictions on where users can browse.

In Amazon WorkSpaces and WorkSpaces Applications instances, consider
existing OS software to harden the instances. For example, you
can use host-based firewalls available within the operating
system to restrict accessible ports in your instances. In
addition, consider endpoint protection software to identify
and mitigate security risks that may be introduced into the
environment using software local to the instances. For detail
on the ports required by Amazon WorkSpaces and WorkSpaces Applications,
see the following:

- [List of ports required by Amazon WorkSpaces Applications](https://docs.aws.amazon.com/appstream2/latest/developerguide/creating-streaming-from-interface-vpc-endpoints.html)
- [List
of ports required for Amazon WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucsec10-bp02.html*

---

# EUCSEC11 — Infrastructure protection

**Pillar**: Security  
**Best Practices**: 1

---

# EUCSEC11-BP01 Perform vulnerability scanning on EUC instances

The frequent release of patches for vulnerabilities in operating
systems and applications means that you should patch them on a
frequent basis to address potential risks.

**Level of risk exposed if this best
practice is not established:** High

## Implementation guidance

- **Perform frequent vulnerability
scanning and patch instances accordingly:**
Software patching is critical for the security and
performance of compute resources. Frequent patching is a
best practice in the security pillar of the
Well-Architected Framework.
- **Regularly patch Amazon AppStream
2.0 images:** As part of the AWS Shared
Responsibility Model, customers are responsible for
patching and securing their WorkSpaces Applications images. When an
image is built and deployed, there are five categories of
software that require patching in your WorkSpaces Applications
image:

- **Applications and
dependencies:** Customers are responsible for
patching the applications and dependencies in images.
- **Operating system:**
Customers are responsible for installing and maintaining
updates for Linux and Windows.
- **Software components:**
These are drivers, agents, and other software required for
WorkSpaces Applications operation (for example, the Amazon CloudWatch agent). WorkSpaces Applications periodically releases new
base images that contain new agents and drivers. Customers
can recreate their images using the latest base image to
bring the software components to the latest baseline.
- **WorkSpaces Applications agent**:
Customers can choose to consistently use the latest agent
version in the Image Assistant. With this option,
streaming instances that are launched from the image
automatically use the latest version of the agent.
- **Clients**: Where the
Amazon WorkSpaces Applications client is in use, this should also be
updated upon the release of each new version.

- **Regularly patch Amazon WorkSpaces
Personal instances:** Amazon WorkSpaces Personal
instances need to be scanned for vulnerabilities and
patched regularly post-deployment. Use configuration
management tools or patch management tools to satisfy the
requirement for ongoing assessment and deployment of
patches. The Amazon WorkSpaces client should also be
updated upon the release of a new version.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucsec11-bp01.html*

---

# EUCSEC12 — Infrastructure protection

**Pillar**: Security  
**Best Practices**: 1

---

# EUCSEC12-BP01 Allow user access to only the software binaries needed to perform their job

Users should only have access to the software binaries required
for them to perform their role. Access to additional software
that could introduce risks should be blocked.

**Level of risk exposed if this best
practice is not established:** Medium

## Implementation guidance

Implement security controls to restrict access to software
binaries. Permissions applied to software binaries present on
Amazon WorkSpaces or WorkSpaces Applications instances should restrict
the ability for users to run the programs and applications
that they require to fulfill their role. Evaluate other
software binaries present in the image to verify that the
default permissions applied in the file system do not permit
users to run them.

System hardening should also be considered to further secure
the operating system image. For reference, consider the Center
for Internet Security (CIS) AWS End User Compute Services
Benchmark. You can apply your chosen security settings by
incorporating them into the image pre-deployment,
post-deployment using scripts, or for Windows instances by
using Group Policy Objects (GPOs). In addition, for Windows
instances, consider FSLogix or AppLocker to restrict access to
specific software binaries.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucsec12-bp01.html*

---

# EUCSEC13 — Data protection

**Pillar**: Security  
**Best Practices**: 1

---

# EUCSEC13-BP01 Align your compliance of data storage with policies and regulatory requirements

The storage of data accessible by users and applications on end
user systems should align with and comply with the data
residency requirements for the data and the organization.

**Level of risk exposed if this best
practice is not established:** High

## Implementation guidance

Data should be stored and accessed in compliance with the
in-scope policies and regulatory requirements. The location of
data and the applications accessing data should align with the
compliance framework and requirements for the respective
organization. To achieve this, consider your AWS Region for
compliance against the data sovereignty requirements for the
application and data. Additionally, consider data permissions
to verify compliance and enforce least privilege access. Keep
latency between end user devices and the data they need to
access in consideration when choosing the location of the EUC
environment but also adhere to data residency requirements.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucsec13-bp01.html*

---

# EUCSEC14 — Data protection

**Pillar**: Security  
**Best Practices**: 3

---

# EUCSEC14-BP01 Encrypt disk volumes to protect data at rest

Protect security, integrity, and availability of data at rest to
make sure it is reliably accessible when needed.

**Level of risk exposed if this best
practice is not established:** High

## Implementation guidance

Encrypt Amazon WorkSpaces Personal disk volumes. Each Amazon
WorkSpace Personal instance is provisioned with a root volume
(C: drive for Windows WorkSpaces Personal, root file system
for Amazon Linux WorkSpaces Personal) and a user volume (D:
drive for Windows WorkSpaces Personal, /home for Amazon Linux
WorkSpaces Personal). The encrypted WorkSpaces feature
encrypts one or both volumes. For WorkSpaces Personal
instances used by users (rather than for creating custom
images), it is a best practice for these to be encrypted. For
more details, see
[Encrypted
WorkSpaces in WorkSpaces Personal](https://docs.aws.amazon.com/workspaces/latest/adminguide/encrypt-workspaces.html).

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucsec14-bp01.html*

---

# EUCSEC14-BP02 Encrypt data in transit in your EUC environment

Use encryption to protect data confidentiality while in transit
inside your EUC environment.

**Level of risk exposed if this best
practice is not established:** High

## Implementation guidance

Use AWS EUC streaming protocols to encrypt streaming data in
transit. Amazon WorkSpaces and Amazon WorkSpaces Applications provide
data encryption of pixel streaming traffic between instances
and end user devices by default. Evaluate the default levels
of encryption to verify that they provide sufficient
protection in terms of key length and cipher suites and
satisfy the requirements of the organization. For further
details regarding the encryption used for Amazon AppStream,
see
[Data
Protection in Amazon WorkSpaces Applications](https://docs.aws.amazon.com/appstream2/latest/developerguide/data-protection.html) , and for Amazon WorkSpaces, see

[Data
Protection in Amazon WorkSpaces.](https://docs.aws.amazon.com/workspaces/latest/adminguide/data-protection.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucsec14-bp02.html*

---

# EUCSEC14-BP03 Limit egress channels available to users to only the required set of channels to perform their role

End user systems can provide multiple channels for users to
export and access data. Evaluate these channels to determine
their suitability in the specific use case being delivered.
Block channels not required for specific use cases.

**Level of risk exposed if this best
practice is not established:** High

## Implementation guidance

- **Encrypt streaming and control data
traffic using strong ciphers**: To protect data
confidentiality, WorkSpaces using PCoIP are encrypted
using an AES 128-bit cipher by default. For encryption up
to AES 256-bit see
[Data
protection in Amazon WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/data-protection.html). Evaluate your
security requirements and use stronger ciphers where
necessary. For Windows, you can implement this using the
Group Policy template, and for Linux WorkSpaces, the
appropriate configuration file needs to be edited to
increase the default level of encryption. For example, for
PCoIP Amazon Linux 2 WorkSpaces, edit the
/etc/pcoip-agent/pcoip-agent.conf file.
- WorkSpaces using the Amazon DCV protocol have streaming
and control data in-transit encrypted using DTLS 1.3
encryption for UDP traffic and TLS 1.3 encryption for TCP
traffic with AES-256 ciphers. For details of the
implementation, see
[Data
protection in Amazon WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/data-protection.html).
- **Restrict data access to required
functionality within Amazon WorkSpaces**: To
protect data on the endpoint used to connect to an Amazon WorkSpaces session and the WorkSpace itself, enable data
exportation features only when needed and allowed to
users. For example, Amazon WorkSpaces can block copying
in-session clipboard contents to the endpoint, copying of
files between client and WorkSpace, and block printers
attached to the endpoint from being mapped into the
session. The blocking of these capabilities can remove
these potential data exportation vectors from the Amazon WorkSpaces service.
- The implementation of these controls is through Group
Policy on Windows WorkSpaces, editing the
/etc/pcoip-agent/pcoip-agent.conf file on Amazon Linux 2
WorkSpaces using PCoIP, or editing the /etc/wsp/wsp.conf
file on Ubuntu Amazon WorkSpaces using Amazon DCV. For
details on how to configure clipboard and other settings
on Windows WorkSpaces, see
[Manage
your Windows WorkSpaces in WorkSpaces Personal](https://docs.aws.amazon.com/workspaces/latest/adminguide/group_policy.html).
- **Restrict data access to required
functionality within Amazon WorkSpaces Applications**: To
protect data on the endpoint used to connect to an Amazon
WorkSpaces Applications session and the WorkSpaces Applications instance
itself, implement controls to close potential inbound or
outbound channels that are not required by the users
connecting to the service. The service has controls to
configure the clipboard, file transfer, printing to a
local device, and file system redirection. You can
configure each of these options on an WorkSpaces Applications stack
and disable them when not required. For details on
configuring data access restrictions with Amazon AppStream
2.0, see
[Create
an Amazon WorkSpaces Applications Fleet and Stack](https://docs.aws.amazon.com/appstream2/latest/developerguide/set-up-stacks-fleets.html#set-up-stacks-fleets-install).

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucsec14-bp03.html*

---

# EUCSEC15 — Data protection

**Pillar**: Security  
**Best Practices**: 1

---

# EUCSEC15-BP01 Encourage users to store data on long-term storage services

Educate users to avoid storing critical data directly on EUC
systems without also saving that data to an approved, long-term
storage solution that is regularly backed up. This practice
verifies that data remains visible, accessible, and protected
against loss in the event of an EUC instance failure or
lifecycle event such as termination or rebuild.

**Level of risk exposed if this best
practice is not established:** Medium

## Implementation guidance

Verify that EUC services are not used for long-term data
storage. EUC services such as Amazon WorkSpaces and Amazon
WorkSpaces Applications are optimized for application delivery and user
productivity, rather than as primary long-term data storage
solutions. Amazon WorkSpaces Applications streaming instances are
non-persistent, meaning data stored locally during a session
is lost when the instance is recycled or terminated. Amazon WorkSpaces provides persistent root and user volumes, which
are well-suited for user profiles, application settings, and
day-to-day productivity tasks. However, for storing critical
or long-term data, organizations should use dedicated storage
services that offer centralized management, data durability,
and backup capabilities.

To reduce the risk of data loss, encourage users to save
important data to approved, persistent storage services that
align with the organization's data protection and recovery
requirements. Recommended options include Amazon FSx for Windows File Server, which integrates with WorkSpaces to
provide durable, backed-up home directories, as well as Amazon S3 or other enterprise-grade cloud storage services. Implement
clear governance policies and user education to verify that
data is consistently stored in systems designed for long-term
retention and resilience.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucsec15-bp01.html*

---

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
