# MSFTOPS02 — Operational automation

**Pillar**: Operational Excellence  
**Best Practices**: 4

---

# MSFTOPS02-BP01 Implement Management and Governance solutions

Set up Management and Governance solutions to ensure your Microsoft
workload is patched and compliant with your security requirements.
AWS Systems Manager functions as an operations hub for your
workload, addressing fleet management, compliance, inventory, admin
session management, state management, patch management, and running
remote commands or scripts. Additionally, leverage AWS Systems Manager OpsCenter to provide a central location for viewing,
investigating, and resolving operational issues related to your
Microsoft workloads. OpsCenter aggregates and standardizes
operations items across services while providing contextual
investigation data about each operations item, related items, and
related resources.

**Desired outcome:** Establish
comprehensive management and governance capabilities for your
Microsoft workloads through AWS Systems Manager, ensuring consistent
patch management, compliance monitoring, and centralized operational
issue resolution while maintaining security standards and
operational efficiency across your Windows-based infrastructure.

**Common anti-patterns:**

- Managing Microsoft workloads manually without centralized
management tools, leading to inconsistent patch levels, security
vulnerabilities, and increased operational overhead across the
Windows infrastructure.
- Implementing patch management without proper testing and
rollback procedures, risking system stability and application
availability when updates are applied to production Microsoft
workloads.
- Operating without centralized visibility into operational issues
and compliance status, making it difficult to identify and
resolve problems quickly across distributed Microsoft workload
environments.

**Benefits of establishing this best
practice:**

- Enhanced security posture and compliance through automated patch
management, configuration compliance monitoring, and centralized
governance of Microsoft workloads, reducing security
vulnerabilities and ensuring adherence to organizational
policies.
- Improved operational efficiency through centralized management
capabilities, automated administrative tasks, and streamlined
incident resolution processes that reduce manual effort and
human error.
- Better visibility and control over Microsoft workload operations
through centralized dashboards, automated reporting, and
integrated operational issue management that enables faster
problem resolution and improved system reliability.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Implementing comprehensive management and governance for Microsoft
workloads requires a systematic approach using AWS Systems Manager
capabilities. Begin by setting up the Systems Manager Agent on all
Windows instances, configure patch management policies, and
establish compliance monitoring. This approach ensures consistent
management across your Microsoft workload infrastructure while
maintaining security and operational standards.

### Implementation steps

- Install and configure the AWS Systems Manager Agent (SSM
Agent) on all Windows instances in your Microsoft workload
environment.
- Set up AWS Systems Manager Patch Manager with maintenance
windows and patch baselines appropriate for your Microsoft
workload requirements.
- Configure AWS Systems Manager Compliance to monitor
configuration compliance and security standards across your
Windows infrastructure.
- Implement AWS Systems Manager Inventory to maintain an
up-to-date inventory of software, configurations, and system
information.
- Set up AWS Systems Manager Session Manager for secure
administrative access to Windows instances without requiring
RDP or VPN connections.
- Configure AWS Systems Manager State Manager to maintain
consistent configuration states across your Microsoft
workload components.
- Implement AWS Systems Manager OpsCenter to centralize
operational issue management and incident response for your
Microsoft workloads.
- Establish automated workflows using AWS Systems Manager
Automation for common administrative tasks and incident
response procedures.

## Resources

**Related documents:**

- [What
is AWS Systems Manager?](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html)
- [Patch
Manager requirements and WSUS](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-prerequisites.html#source-connectivity)

**Related tools:**

- [AWS Systems Manager Patch Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager.html)
- [AWS Systems Manager OpsCenter](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftops02-bp01.html*

---

# MSFTOPS02-BP02 Implement infrastructure deployment and update automation for your Microsoft workload

Set up Infrastructure as Code (IaC) to apply patterns to the
infrastructure of your Microsoft workload. You can use AWS CloudFormation to help model and deploy the required AWS resources
based on templates. Third-party solutions, such as Terraform, are
also useful for the case.

**Desired outcome:** Establish
automated, repeatable, and version-controlled infrastructure
deployment processes for your Microsoft workloads using
Infrastructure as Code (IaC) practices, ensuring consistent
environments, reducing deployment errors, and enabling rapid scaling
and recovery of your Windows-based infrastructure.

**Common anti-patterns:**

- Deploying Microsoft workload infrastructure manually through the
AWS console or CLI without using Infrastructure as Code, leading
to configuration drift, inconsistent environments, and
difficulty in reproducing deployments across different stages.
- Creating IaC templates without proper version control, testing,
or documentation, making it difficult to track changes, rollback
deployments, or collaborate effectively on infrastructure
modifications.
- Implementing IaC without considering Microsoft workload-specific
requirements such as Windows licensing, Active Directory
integration, or SQL Server configuration, resulting in
incomplete or non-functional deployments.

**Benefits of establishing this best
practice:**

- Consistent and reliable deployments through standardized
Infrastructure as Code templates that ensure all Microsoft
workload components are deployed with the same configuration
across development, testing, and production environments.
- Improved operational efficiency and reduced deployment time
through automated infrastructure provisioning, enabling rapid
scaling, disaster recovery, and environment replication for
Microsoft workloads.
- Enhanced change management and auditability through
version-controlled infrastructure templates that provide clear
documentation of infrastructure changes and enable easy rollback
when issues occur.
- IaC can help enforce security best practices by defining secure
configurations within templates.
- By automating resource provisioning and de-provisioning, IaC can
help optimize resource utilization and reduce costs.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Implementing Infrastructure as Code for Microsoft workloads
requires careful consideration of Windows-specific requirements
and AWS services. Start by identifying your Microsoft workload
components and their dependencies, then create modular IaC
templates that can be reused across environments. This approach
ensures consistent deployments while accommodating the specific
needs of Windows-based applications and services.

### Implementation steps

- Analyze your Microsoft workload architecture and identify
all AWS resources, dependencies, and configuration
requirements.
- Choose an appropriate IaC tool (AWS CloudFormation, AWS CDK,
or Terraform) based on your team's expertise and
organizational requirements.
- Create modular IaC templates for common Microsoft workload
components such as Windows EC2 instances, SQL Server
databases, and Active Directory services.
- Implement version control for your IaC templates using Git
repositories with proper branching strategies and code
review processes.
- Set up automated testing and validation for your IaC
templates using tools like AWS CloudFormation Guard or
Terraform validation.
- Establish CI/CD pipelines for infrastructure deployment
using AWS CodePipeline, GitHub Actions, or similar tools to
automate template deployment.
- Create environment-specific parameter files and
configuration management to support deployment across
development, testing, and production environments.
- Implement infrastructure monitoring and drift detection to
ensure deployed resources remain consistent with your IaC
templates.

## Resources

**Related documents:**

- [AWS CloudFormation and Windows](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-windows-stacks.html)

**Related videos:**

- [AWS re:Invent 2024 - Use generative AI to optimize cloud
operations for Microsoft workloads (XNT312)](https://www.youtube.com/watch?v=FXul8gfj1Qk&t=3s)

**Related examples:**

- [Use
Terraform to Build Microsoft Infrastructure on AWS](https://catalog.us-east-1.prod.workshops.aws/workshops/e5122482-ded0-4259-94f0-c373f23c5257/en-US)

**Related tools:**

- [AWS CloudFormation](https://docs.aws.amazon.com/cloudformation/)
- [Terraform
AWS Windows Workloads](https://github.com/aws-samples/terraform-aws-windows-workloads-on-aws)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftops02-bp02.html*

---

# MSFTOPS02-BP03 Implement operating system image control

AWS has developed a set of Amazon Machine Images (AMIs) for popular
Microsoft solutions with License Included software, enabling
standardized and automated deployments of Windows Server instances
in Amazon EC2. You can either use the latest images that are built
by AWS or create your own. You can subscribe to AWS Windows AMI
notifications or create custom AMIs of your own to apply the
standards required by your environment, such as regional settings,
agents, base patches, and general tools. EC2 Image Builder is a
fully managed AWS service that helps you to automate the creation,
management, and deployment of customized, secure, and up-to-date
server images.

**Desired outcome:** Establish
standardized, secure, and consistently configured Windows Server
images for your Microsoft workloads through automated AMI
management, ensuring rapid deployment capabilities, security
compliance, and operational consistency across all Windows instances
in your environment.

**Common anti-patterns:**

- Using outdated or unpatched base AMIs without regular updates,
leading to security vulnerabilities and inconsistent
configurations across Windows instances in your Microsoft
workload environment.
- Creating custom AMIs manually without automation or version
control, resulting in configuration drift, difficulty in
reproducing images, and challenges in maintaining security and
compliance standards.
- Deploying Windows instances without standardized configurations,
leading to operational inconsistencies, increased
troubleshooting time, and potential security gaps across your
Microsoft workload infrastructure.

**Benefits of establishing this best
practice:**

- Faster deployment and improved consistency through standardized
Windows Server images that include all necessary configurations,
patches, and tools, reducing instance launch time and ensuring
uniform environments.
- Enhanced security posture through automated image updates and
patch management, ensuring all Windows instances are deployed
with the latest security updates and compliance configurations.
- Reduced operational overhead through automated AMI creation and
management processes that eliminate manual image preparation
tasks and ensure consistent, repeatable deployments across
environments.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Implementing operating system image control for Microsoft
workloads requires a systematic approach to AMI management and
automation. Begin by establishing your image requirements and
standards, then implement EC2 Image Builder to automate the
creation and maintenance of custom Windows AMIs. This approach
ensures consistent, secure, and up-to-date images for your
Microsoft workload deployments.

### Implementation steps

- Define your Windows Server image requirements including base
configurations, security settings, required software, and
organizational standards.
- Set up EC2 Image Builder with appropriate IAM roles and
permissions to automate AMI creation and management
processes.
- Create Image Builder recipes that include your required
Windows configurations, software installations, and security
hardening steps.
- Configure automated testing pipelines to validate AMI
functionality and security compliance before distribution.
- Implement automated AMI distribution to multiple AWS regions
and accounts as needed for your Microsoft workload
deployment strategy.
- Set up AMI lifecycle management policies to automatically
deprecate and delete outdated images while maintaining
required retention periods.
- Subscribe to AWS Windows AMI notifications to stay informed
about security updates and new releases for base Windows
Server images.
- Establish regular AMI update schedules to incorporate
security patches, software updates, and configuration
changes into your custom images.

## Resources

**Related documents:**

- [What
is EC2 Image Builder?](https://docs.aws.amazon.com/imagebuilder/latest/userguide/how-image-builder-works.html)
- [How
Amazon creates AWS Windows AMIs](https://docs.aws.amazon.com/ec2/latest/windows-ami-reference/windows-ami-versions.html)

**Related tools:**

- [Amazon EC2 AMIs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html)
- [EC2 Image Builder](https://docs.aws.amazon.com/imagebuilder/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftops02-bp03.html*

---

# MSFTOPS02-BP04 Leverage managed services for your Microsoft workload

To reduce operational overhead, implement the use of AWS managed
services to address your Microsoft workload requirements. Consider
AWS Managed Microsoft Active Directory, Amazon Relational Database Service for SQL Server, Amazon FSx for Windows File Server, Amazon FSx for NetApp ONTAP, AWS Elastic Beanstalk, and others.

**Desired outcome:** Reduce
operational complexity and overhead for your Microsoft workloads by
strategically adopting AWS managed services that handle
infrastructure management, patching, backups, and scaling
automatically, allowing your team to focus on application
development and business value rather than infrastructure
maintenance.

**Common anti-patterns:**

- Managing Microsoft infrastructure components manually when
equivalent AWS managed services are available, leading to
increased operational overhead, higher maintenance costs, and
potential security vulnerabilities from delayed patching.
- Choosing self-managed solutions without evaluating the total
cost of ownership, including operational effort, expertise
requirements, and ongoing maintenance compared to AWS managed
service alternatives.
- Implementing managed services without proper integration
planning, resulting in architectural complexity, security gaps,
or performance issues that could have been avoided with better
design considerations.

**Benefits of establishing this best
practice:**

- Significantly reduced operational overhead through AWS-managed
infrastructure components that handle patching, backups,
monitoring, and scaling automatically, freeing up resources for
higher-value activities.
- Improved reliability and availability through AWS-managed
services that provide built-in high availability, disaster
recovery, and automated failover capabilities designed and
tested by AWS experts.
- Enhanced security posture through managed services that include
automatic security updates, encryption capabilities, and
compliance features that are maintained and updated by AWS
according to industry best practices.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Implementing AWS managed services for Microsoft workloads requires
careful evaluation of your current architecture and identification
of components that can be replaced or enhanced with managed
alternatives. Begin by assessing your Microsoft workload
components and their operational requirements, then systematically
migrate to appropriate AWS managed services while ensuring proper
integration and security.

### Implementation steps

- Conduct a comprehensive assessment of your current Microsoft
workload architecture to identify components suitable for
managed service replacement.
- Evaluate AWS managed service options including AWS Managed Microsoft AD, Amazon RDS for SQL Server, Amazon FSx for Windows File Server, and AWS Elastic Beanstalk.
- Develop a migration strategy that prioritizes
high-maintenance components and considers dependencies
between services and applications.
- Implement pilot migrations with non-critical workloads to
validate managed service configurations and integration
patterns.
- Configure managed services with appropriate security
settings, backup policies, and monitoring to meet your
operational requirements.
- Establish connectivity and integration between managed
services and existing Microsoft workload components using
VPC networking and security groups.
- Migrate production workloads systematically, ensuring proper
testing and rollback procedures are in place for each
migration phase.
- Update operational procedures and documentation to reflect
the new managed service architecture and reduced maintenance
requirements.

## Resources

**Related documents:**

- [AWS Managed Services for Microsoft Workloads](https://aws.amazon.com/windows/)

**Related tools:**

- [AWS Managed Microsoft AD](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/directory_microsoft_ad.html)
- [Amazon RDS for SQL Server](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_SQLServer.html)
- [Amazon FSx for Windows File Server](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/what-is.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftops02-bp04.html*

---
