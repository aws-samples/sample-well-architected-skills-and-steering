# MSFTCOST05 — Storage

**Pillar**: Cost Optimization  
**Best Practices**: 4

---

# MSFTCOST05-BP01 Migrate Amazon EBS volumes from gp2 to gp3

General Purpose SSD (gp3) volumes are the latest generation of
General Purpose SSD volumes, and the lowest cost SSD volume offered
by Amazon EBS. This volume type helps to provide the right balance
of price and performance for most applications. It also helps you to
scale volume performance independently of volume size. This means
that you can provision the required performance with no need to
provision additional block storage capacity. Additionally, gp3
volumes offer a 20 percent lower price per GiB than General Purpose
SSD (gp2) volumes.

**Desired outcome:** By migrating
Amazon EBS volumes from gp2 to gp3, we aim to achieve a 20%
reduction in storage costs while gaining the ability to
independently scale volume performance without increasing capacity.
This transition will optimize our storage expenses and provide
better performance control for our workloads, ultimately resulting
in improved cost efficiency without compromising performance
requirements.

**Common anti-patterns:**

- Some organizations maintain large gp2 volumes to achieve higher
IOPS, unnecessarily increasing costs. They fail to recognize
that gp3 volumes allow separate scaling of IOPS and throughput,
potentially leading to significant overspending on storage.
- Some teams might hastily migrate all gp2 volumes to gp3 without
analyzing workload-specific performance needs. This can result
in performance degradation for applications that require higher
baseline performance than what's provided by the default gp3
configuration, leading to potential application issues and the
need for retroactive adjustments.

**Benefits of establishing this best
practice:**

- Immediate 20% reduction in per-GiB storage costs compared to gp2
volumes, leading to significant cost savings across the storage
infrastructure, especially for large-scale deployments with
multiple volumes.
- Independent scaling of IOPS and throughput without increasing
volume size, allowing precise performance tuning based on
application needs while avoiding unnecessary storage capacity
expenses.
- The ability to maintain smaller volume sizes while still
achieving desired performance levels eliminates the need to
overprovision storage for performance reasons, resulting in more
efficient resource utilization and easier capacity management.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Begin by identifying all existing gp2 volumes using AWS Cost Explorer or AWS Systems Manager. Create a phased migration plan,
prioritizing non-production environments first to validate the
performance impact. Use AWS CloudFormation templates or AWS CLI
scripts to automate the modification process, ensuring each
volume's baseline performance requirements are properly configured
during the transition to gp3. Monitor performance metrics through
Amazon CloudWatch before and after migration to verify that
application performance remains optimal. Include snapshot backups
in your migration strategy as a rollback mechanism, and schedule
migrations during low-traffic periods to minimize potential impact
on business operations.

### Implementation steps

- Conduct an inventory analysis using AWS Cost Explorer and
Systems Manager to identify all gp2 volumes, documenting
their current size, IOPS requirements, and associated
workloads.
- Create automated scripts using AWS CLI or Infrastructure as
Code (IaC) to modify volumes from gp2 to gp3, including
proper configuration of baseline IOPS and throughput based
on historical performance data.
- Implement the migration in phases, starting with development
and test environments, followed by non-critical production
workloads, and finally business-critical applications, with
performance validation at each stage.
- Monitor post-migration performance using Amazon CloudWatch
metrics and establish a feedback loop to adjust gp3 volume
configurations as needed, ensuring optimal performance while
maintaining cost savings.

## Resources

**Related documents:**

- [Amazon EBS General Purpose SSD volumes](https://docs.aws.amazon.com/ebs/latest/userguide/general-purpose.html)
- [Migrate
Amazon EBS volumes from gp2 to gp3](https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/ebs-migrate-gp2-gp3.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftcost05-bp01.html*

---

# MSFTCOST05-BP02 Control Amazon EBS volumes or snapshots lifecycle

EBS snapshots are incremental backups stored in S3, saving only
changed blocks since the last snapshot. They can backup unattached
volumes before deletion. Two storage tiers available: Standard
(higher storage cost and free retrieval) and Archive (lower storage
cost and paid retrieval). Managing snapshot lifecycles and removing
unused volumes helps optimize costs.

**Desired outcome:** Implement an
effective EBS volume and snapshot management strategy that
automatically identifies and removes unused volumes while
maintaining cost-efficient snapshot lifecycles across appropriate
storage tiers, resulting in optimized storage costs for Microsoft
workloads on AWS.

**Common anti-patterns:**

- Neglecting to delete unattached EBS volumes: Keeping unused
volumes active, leading to unnecessary ongoing storage costs for
resources that are no longer needed.
- Inconsistent or manual snapshot management: Relying on manual
processes or ad-hoc scripts for creating and managing snapshots,
leading to inconsistent backup coverage, potential data loss,
and inefficient use of storage resources.

**Benefits of establishing this best
practice:**

- By systematically managing EBS volumes and snapshots, you can
significantly reduce storage costs by removing unused resources
and efficiently tiering snapshots based on access needs.
- Regular lifecycle management ensures that your backup strategy
is consistent and up-to-date, reducing the risk of data loss and
maintaining appropriate retention periods for compliance and
disaster recovery purposes.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

To effectively control EBS volume and snapshot lifecycles, start
by implementing automated tools such as AWS Data Lifecycle
Manager. Configure policies to regularly identify and delete
unattached volumes, create consistent snapshot schedules, and
manage snapshot retention across appropriate storage tiers. Use
tags to categorize resources and enable granular control.
Regularly review and adjust your policies to ensure they align
with changing business needs and cost optimization goals.
Implement monitoring and alerting to track resource usage and
potential cost savings opportunities.

### Implementation steps

- Set up AWS Data Lifecycle Manager policies to automate
snapshot creation and deletion based on defined schedules
and retention rules.
- Implement a tagging strategy to categorize EBS volumes and
snapshots, enabling easier management and cost allocation.
- Create an automated process to identify and alert on
unattached EBS volumes, with an option to delete them after
a specified period.
- Establish a tiering policy to move infrequently accessed
snapshots from Standard to Archive tier after a set duration
to optimize storage costs.

## Resources

**Related documents:**

- [Modify
Amazon EBS snapshots](https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/ebs-migrate-ebs-snapshots.html)
- [Delete
unattached Amazon EBS volumes](https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/ebs-delete-ebs-volumes.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftcost05-bp02.html*

---

# MSFTCOST05-BP03 Use Amazon FSx for NetApp ONTAP

Amazon FSx for NetApp ONTAP offers a file system that supports SMB
and iSCSI protocols. Useful for critical Microsoft SQL Server
environments, as ONTAP volumes can be mapped to Windows Server
instances as block storage devices using the iSCSI model, also
providing shared storage for cluster-aware applications. FSx for ONTAP has two capacity settings (HDD and SSD), data
deduplication, and cache layers. Smaller EC2 instances can leverage
the FSx solution to achieve high performance storage levels.

**Desired outcome:** By implementing
Amazon FSx for NetApp ONTAP, an organization can achieve a highly
available and performant storage solution for Microsoft workloads.
The implementation will leverage both SMB and iSCSI protocols,
enabling efficient block storage access while benefiting from
advanced features like data deduplication and multi-tiered caching.
This will result in optimized storage costs, improved performance
even with smaller EC2 instances, and reduced operational overhead
for managing Microsoft workloads.

**Common anti-patterns:**

- Running Microsoft SQL Server or other Microsoft workloads with
directly attached EBS volumes may limit high availability and
scalability, making failover scenarios complex and
time-consuming. This approach also lacks the advanced storage
management features and efficiency benefits provided by FSx for ONTAP, potentially leading to higher costs and
operational overhead.
- Compensating for storage performance requirements by using
oversized EC2 instances with local storage or multiple EBS
volumes, rather than leveraging FSx for ONTAP's efficient
storage architecture. This results in unnecessary compute costs
and doesn't address the underlying need for enterprise-grade
storage features like deduplication and efficient snapshots.

**Benefits of establishing this best
practice:**

- FSx for ONTAP provides high-performance storage, allowing
even small EC2 instances to achieve excellent I/O capabilities.
- Easily scale storage capacity and performance independently of
compute resources, adapting to changing workload demands.
- Reduce management overhead with built-in features like data
deduplication, snapshots, and multi-protocol support.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

To implement FSx for ONTAP for Microsoft workloads, create
an FSx file system in your VPC. Configure SVMs and volumes for
your applications, setting up SMB shares and iSCSI LUNs as needed.
Connect Windows instances to these resources using native tools.
For high availability, use Windows Server Failover Clustering with
FSx as shared storage. Migrate your data, then update backup and
recovery processes to leverage FSx features like snapshots and
replication.

### Implementation steps

- Create FSx for ONTAP file system within your VPC,
configuring the appropriate storage capacity and throughput
based on workload requirements
- Set up Storage Virtual Machines (SVMs) and configure storage
volumes with proper protocols (SMB/iSCSI) based on your
Microsoft application needs
- Connect Windows Server instances to FSx storage using native
tools (File Explorer for SMB, iSCSI Initiator for block
storage)
- Configure Windows Server Failover Clustering if high
availability is required, using FSx for ONTAP as the shared
storage
- Migrate existing data to FSx storage and implement
backup/recovery procedures using ONTAP's snapshot and
replication capabilities

## Resources

**Related documents:**

- [What
is Amazon FSx for NetApp ONTAP?](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/what-is-fsx-ontap.html)
- [Provisioning
iSCSI for Windows](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/mount-iscsi-windows.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftcost05-bp03.html*

---

# MSFTCOST05-BP04 Use Amazon FSx for Windows File Server

Amazon FSx for Windows File Server is a fully managed file storage service that's optimized for Microsoft
workloads. It provides an SMB file system that can be accessed by applications, including
Windows web servers and Microsoft SQL Server. FSx for Windows File Server is a scalable solution that offers
Single AZ or Multi AZ availability, automatic data deduplication, different pricing options, and
two capacity settings (HDD and SSD), being flexible to fit your Microsoft workloads. Fairly
small EC2 instances can leverage the FSx solution to achieve high performance storage levels.

**Desired outcome:** Implement Amazon FSx for Windows File Server to optimize storage
for Microsoft workloads, reducing operational overhead while enhancing scalability and
performance. This change aims to improve efficiency, simplify management, and potentially reduce
costs associated with file storage for Windows-based applications in AWS.

**Common anti-patterns:**

- Running Windows file servers on EC2 instances with attached EBS volumes, requiring
manual management of storage capacity, backups, and Windows Server maintenance while
incurring higher operational costs and complexity.
- Using non-Windows-optimized storage solutions for Windows workloads, resulting in
compatibility issues, degraded performance, and the need for additional software or
configurations to handle SMB protocol requirements.

**Benefits of establishing this best practice:**

- Eliminates the need for manual file server management, Windows patching, and backup
administration through AWS's fully managed service.
- Provides high-performance storage with automatic capacity management and the ability to
scale up or down based on workload demands, while supporting both Single-AZ and Multi-AZ
deployments.
- Offers flexible storage options (HDD/SSD) and pricing models, allowing organizations to
align costs with actual needs while eliminating the overhead of maintaining dedicated
Windows file servers and associated licenses.

**Level of risk exposed if this best practice is not established:**
Medium

## Implementation guidance

Begin by assessing your current Windows workload requirements, including storage
capacity, performance needs, and availability requirements. Choose between Single-AZ or
Multi-AZ deployment based on your reliability needs, and select the appropriate storage type
(HDD for general purpose or SSD for performance-intensive workloads). Start with a pilot
migration of a non-critical workload to validate the setup and performance. Configure your
existing Windows applications and services to connect to the FSx file system using standard
SMB protocol, and implement appropriate security groups and Active Directory integration. Once
validated, proceed with a phased migration approach for remaining workloads while monitoring
performance metrics through CloudWatch.

### Implementation steps

- Assess workload requirements and select appropriate FSx configuration
(Single/Multi-AZ, HDD/SSD, and storage capacity) based on performance needs and budget
constraints.
- Configure network security by setting up VPC security groups, ensuring proper
routing, and establishing Active Directory integration for authentication.
- Migrate existing file data to FSx using AWS DataSync or standard file copy tools,
validating data integrity and permissions post-migration.
- Update application configurations to point to the new FSx file share endpoints and
verify connectivity, performance, and functionality across all dependent services.

## Resources

**Related documents:**

- [Amazon FSx for Windows File Server](https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/storage-fsx.html)

**Related tools:**

- [AWS DataSync](https://aws.amazon.com/datasync/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftcost05-bp04.html*

---
