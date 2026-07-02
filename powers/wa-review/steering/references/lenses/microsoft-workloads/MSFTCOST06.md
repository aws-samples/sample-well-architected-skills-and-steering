# MSFTCOST06 — Active directory

**Pillar**: Cost Optimization  
**Best Practices**: 3

---

# MSFTCOST06-BP01 Use AWS Managed Microsoft Active Directory

AWS Managed Microsoft AD provides redundant Windows Server domain
controllers across two Availability Zones in your VPC. It handles
all maintenance tasks automatically, including monitoring,
replication, backups, and updates. The service supports
directory-aware workloads like SharePoint and .NET applications, and
can integrate with on-premises Active Directory through trust
relationships. Based on size requirements, you can either choose the
Standard or the Enterprise edition.

**Desired outcome:** By implementing
AWS Managed Microsoft Active Directory, you aim to reduce
operational overhead and costs associated with managing Active
Directory in the AWS Cloud. This solution provides a highly
available, fully managed directory service that automatically
handles maintenance tasks, supports directory-aware workloads, and
enables integration with on-premises Active Directory. The result is
a more efficient, scalable, and cost-effective approach to directory
services in your cloud environment.

**Common anti-patterns:**

- Managing your own domain controllers on EC2 instances, resulting
in unnecessary operational overhead from manual patching,
backups, monitoring, and high availability configuration.
- Creating multiple standalone Active Directory environments
across different workloads instead of using a centralized
managed service, leading to increased costs and management
complexity.

**Benefits of establishing this best
practice:**

- Reduced operational overhead: AWS handles maintenance tasks such
as patching, backups, and monitoring, freeing up IT staff to
focus on core business activities.
- Improved reliability and availability: The service automatically
deploys domain controllers across multiple Availability Zones,
ensuring high availability and disaster recovery capabilities.
- Seamless integration: Enables easy connection with on-premises
Active Directory through trust relationships, facilitating
hybrid cloud scenarios and simplifying user access management
across environments.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

To implement AWS Managed Microsoft AD effectively, start by
assessing your directory service needs and selecting the
appropriate edition (Standard or Enterprise) based on your
organization's size and requirements. Plan your VPC and network
configuration to ensure proper connectivity for your domain
controllers. If you have an existing on-premises Active Directory,
establish a trust relationship to enable seamless integration.
Migrate your directory-aware workloads gradually, beginning with
less critical applications to gain experience and confidence.
Leverage AWS IAM Identity Center for unified access management
across your AWS environment. Finally, regularly review and
optimize your setup to ensure it continues to meet your evolving
needs while maximizing cost efficiency.

### Implementation steps

- Prepare your environment by configuring VPC with appropriate
subnets across multiple AZs and setting up required network
connectivity for hybrid scenarios
- Deploy AWS Managed Microsoft AD by selecting the appropriate
edition, choosing target VPC and subnets, and configuring
directory administrator credentials and DNS settings
- Establish connectivity and access through security group
configuration, trust relationship setup with on-premises AD
if needed, and AWS IAM Identity Center integration
- Migrate workloads gradually, starting with test
applications, followed by directory-aware workloads, while
updating DNS settings and application configurations
- Monitor and maintain the environment using CloudWatch
metrics, managing directory users and groups, and performing
regular access permission audits

## Resources

**Related documents:**

- [AWS Managed Microsoft AD](https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/active-directory-aws-managed.html)
- [How
to migrate your on-premises domain to AWS Managed Microsoft AD
using ADMT](https://aws.amazon.com/blogs/security/how-to-migrate-your-on-premises-domain-to-aws-managed-microsoft-ad-using-admt/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftcost06-bp01.html*

---

# MSFTCOST06-BP02 Use AD Connector

AD Connector is a directory gateway with which you can redirect
directory requests to your on-premises Microsoft Active Directory
without caching any information in the cloud. AD Connector comes in
two sizes, small and large. A small AD Connector is designed for
smaller organizations and is intended to handle a low number of
operations per second. A large AD Connector is designed for larger
organizations and is intended to handle a moderate to high number of
operations per second. You can spread application loads across
multiple AD Connectors to scale to your performance needs. There are
no enforced user or connection limits.

**Desired outcome:** By implementing
AD Connector, the organization may achieve seamless integration
between on-premises Microsoft Active Directory and AWS Cloud
services without data replication or cloud caching. The solution
will be appropriately sized (small or large) based on operational
requirements, with the flexibility to add multiple AD Connectors for
increased performance as needed, ensuring cost-effective directory
services management while maintaining security and scalability.

**Common anti-patterns:**

- Replicating the entire on-premises Active Directory to AWS using
AWS Managed Microsoft AD or EC2 instances running AD Domain
Controllers, when only authentication and authorization services
are required, leading to increased attack surface, higher costs,
and unnecessary data duplication.
- Implementing AWS Managed Microsoft AD when only directory
authentication is needed, resulting in higher operational costs
and unnecessary complexity when AD Connector could provide the
same functionality through simple proxying of authentication
requests to the existing on-premises Active Directory.

**Benefits of establishing this best
practice:**

- AD Connector eliminates the need for complex directory
synchronization solutions or maintaining separate directory
infrastructures in the cloud, reducing both capital and
operational expenses associated with directory services
management.
- By not storing or caching any directory information in the
cloud, AD Connector minimizes the risk of data breaches and
maintains a smaller attack surface, while still allowing AWS
resources to leverage existing on-premises Active Directory for
authentication and authorization.

**Level of risk exposed if this best practice
is not established:** Low

## Implementation guidance

To implement AD Connector effectively, start by assessing your
organization's directory service needs and sizing requirements.
Choose between small and large AD Connector options based on your
expected operation volume. Ensure your on-premises Active
Directory is properly configured and accessible from your AWS VPC
through a secure connection, such as AWS Direct Connect or a VPN.
Set up the AD Connector in your VPC, configure the necessary
security groups, and test the connection thoroughly. For high
availability, consider deploying AD Connectors in multiple
Availability Zones. Finally, integrate your AWS resources and
applications with AD Connector for seamless authentication and
authorization using your existing Active Directory credentials.

### Implementation steps

- Establish network connectivity between AWS and on-premises
environment through either AWS Direct Connect or AWS Site-to-Site VPN, ensuring proper routing and security group
configurations are in place.
- Deploy AD Connector in your VPC, selecting the appropriate
size (small or large) based on your organization's
authentication operation volume and configuring it with your
on-premises Active Directory service account credentials.
- Test AD Connector functionality by verifying authentication
flows and ensuring proper communication between AWS
resources and your on-premises Active Directory.
- Enable and configure AWS services and applications to use AD
Connector for authentication, including AWS Management Console access and AWS Enterprise Applications that support
SAML 2.0.

## Resources

**Related documents:**

- [AD
Connector](https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/active-directory-connector.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftcost06-bp02.html*

---

# MSFTCOST06-BP03 Use self-managed Active Directory on Amazon EC2

Depending on the requirements, your Microsoft workload may require
the use of a self-managed Active Directory deployment (either a new
forest or extending an existing one). Deploying Active Directory
domains controllers to Amazon EC2 is fairly simple. Domain
controllers are usually good candidates to run on Amazon EC2
burstable instance family, saving on compute costs. Make sure to
evaluate the capacity planning recommendations provided by Microsoft
to address your workload requirements.

**Desired outcome:** Deploy
self-managed Active Directory domain controllers on Amazon EC2,
leveraging burstable instance families where appropriate to optimize
costs. The implementation will follow Microsoft's capacity planning
guidelines and support either new or extended Active Directory
forests based on organizational requirements, ensuring a robust and
cost-effective directory service solution.

**Common anti-patterns:**

- Deploying Active Directory domain controllers on oversized EC2
instances, such as using high-performance compute-optimized
instances when not required. This leads to unnecessary costs and
underutilized resources, contradicting the goal of cost
optimization.
- Implementing Active Directory on EC2 without properly evaluating
Microsoft's capacity planning recommendations. This can result
in performance issues, scalability problems, and potential
service disruptions, ultimately affecting the reliability of the
Microsoft workload and potentially increasing long-term costs
due to necessary remediation efforts.

**Benefits of establishing this best
practice:**

- Cost-effective directory services through optimized EC2 instance
selection and burstable computing, reducing operational expenses
while maintaining performance requirements.
- Enhanced control and flexibility in deploying and managing
Active Directory infrastructure, supporting both new
implementations and extensions of existing directory services.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

To implement self-managed Active Directory on Amazon EC2, begin by
assessing your workload requirements and consulting Microsoft's
capacity planning recommendations. Choose appropriate EC2 instance
types, favoring burstable instances where suitable. Deploy at
least two domain controllers across different Availability Zones
for high availability. Use Amazon EBS volumes for storage,
ensuring proper backups and snapshots. Implement security best
practices, including network segmentation with VPCs and security
groups. Finally, establish monitoring and alerting using Amazon CloudWatch to maintain optimal performance and availability of
your Active Directory infrastructure.

### Implementation steps

- Size and deploy EC2 instances based on Microsoft's capacity
planning guidelines, utilizing burstable instance families
where appropriate, and ensure distribution across multiple
Availability Zones for high availability.
- Configure networking components including VPC design,
security groups, and DHCP options to support Active
Directory requirements and establish secure communication
paths.
- Install and configure Active Directory Domain Services,
establishing either a new forest or extending an existing
one, following Microsoft's recommended configurations and
security baselines.
- Implement monitoring and backup solutions using Amazon CloudWatch and automated EBS snapshots to maintain service
health and enable disaster recovery capabilities.

## Resources

**Related documents:**

- [Self-managed
Active Directory on Amazon EC2](https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/active-directory-self-managed.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftcost06-bp03.html*

---
