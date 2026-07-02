# MSFTPERF03 — Storage solutions

**Pillar**: Performance Efficiency  
**Best Practices**: 5

---

# MSFTPERF03-BP01 Consider Amazon EBS gp3 volumes for general workloads

Amazon EBS's newest and most cost-effective SSD option, General
Purpose SSD (gp3) volumes, strikes an optimal balance between price
and performance for a wide range of applications. A key advantage of
gp3 volumes is the ability to adjust performance independently of
storage capacity, allowing users to meet specific performance
requirements without unnecessarily increasing block storage.
Moreover, gp3 volumes offer significant cost savings, with prices
20% lower per GiB compared to their predecessor, General Purpose SSD
(gp2) volumes.

**Desired outcome:** Optimize storage
performance and cost efficiency for Microsoft workloads by
leveraging gp3 volumes that provide independent scaling of IOPS and
throughput from storage capacity, enabling right-sized storage
configurations that meet performance requirements while minimizing
costs.

**Common anti-patterns:**

- Continuing to use gp2 volumes without evaluating gp3 benefits,
missing opportunities for cost savings and performance
optimization through independent IOPS and throughput scaling.
- Over-provisioning storage capacity to meet IOPS requirements
when using gp2 volumes, leading to unnecessary storage costs
that could be avoided with gp3's independent performance
scaling.
- Choosing high-performance storage options like io1/io2 for
workloads that could be adequately served by gp3 with
appropriate IOPS configuration, resulting in unnecessary costs.

**Benefits of establishing this best
practice:**

- Significant cost savings through 20% lower per-GiB pricing
compared to gp2 volumes while maintaining or improving
performance characteristics for Microsoft workloads.
- Enhanced flexibility through independent scaling of IOPS and
throughput from storage capacity, enabling optimal resource
allocation without over-provisioning storage.
- Improved performance predictability through consistent baseline
performance and the ability to provision additional IOPS and
throughput as needed for specific workload requirements.

**Level of risk exposed if this best practice
is not established:** Low

## Implementation guidance

Implementing gp3 volumes for Microsoft workloads requires
understanding your storage performance requirements and migrating
from existing volume types where appropriate. Focus on workloads
that can benefit from independent IOPS and throughput scaling
while achieving cost savings.

### Implementation steps

- Analyze current storage performance requirements for
Microsoft workloads including IOPS, throughput, and capacity
needs.
- Identify existing gp2 volumes and other storage types that
could benefit from migration to gp3 for cost and performance
optimization.
- Plan gp3 volume configurations with appropriate baseline
performance and additional provisioned IOPS or throughput
based on workload requirements.
- Test gp3 performance in non-production environments to
validate performance characteristics for your specific
Microsoft applications.
- Implement migration procedures for existing volumes using
EBS volume modification or snapshot-based migration
approaches.
- Monitor storage performance and costs after migration to
validate expected benefits and optimize configurations as
needed.
- Establish policies for new volume provisioning that default
to gp3 unless specific requirements dictate alternative
storage types.
- Document gp3 configuration standards and include in storage
provisioning procedures for consistent implementation across
environments.

## Resources

**Related documents:**

- [General
Purpose SSD (gp3) volumes](https://docs.aws.amazon.com/ebs/latest/userguide/general-purpose.html#gp3-ebs-volume-type)

**Related tools:**

- [Migrate
Amazon EBS volumes from gp2 to gp3](https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/ebs-migrate-gp2-gp3.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftperf03-bp01.html*

---

# MSFTPERF03-BP02 Consider Amazon EBS io2 Block Express volumes for high-intense I/O workloads

Amazon EBS io2 Block Express volumes are based on an updated storage
server architecture. They are designed to handle high I/O
requirements for applications running on Nitro System-based
instances. These volumes offer improved durability and lower
latency. As a result, they are suitable for resource-intensive
applications that require consistent performance, such as certain
database systems (For example, Oracle, SAP HANA, and Microsoft SQL
Server) and SAS Analytics.

**Desired outcome:** Achieve maximum
I/O performance and lowest latency for demanding Microsoft
workloads, particularly SQL Server databases and other I/O-intensive
applications, through io2 Block Express volumes that provide
consistent high-performance storage with enhanced durability and
reliability.

**Common anti-patterns:**

- Using general-purpose storage for high-performance Microsoft SQL
Server databases without evaluating io2 Block Express benefits,
potentially limiting application performance and user
experience.
- Implementing io2 Block Express for workloads that don't require
extreme I/O performance, leading to unnecessary costs without
proportional performance benefits.
- Choosing io2 Block Express without ensuring compatibility with
Nitro System-based instances, missing the full performance
potential of the storage technology.

**Benefits of establishing this best
practice:**

- Maximum I/O performance through io2 Block Express architecture
designed specifically for high-intensity workloads, enabling
optimal performance for demanding Microsoft applications.
- Enhanced reliability and durability through improved storage
architecture that provides consistent performance and reduced
latency for mission-critical workloads.
- Improved application responsiveness for I/O-intensive Microsoft
workloads including SQL Server databases, analytics
applications, and high-performance computing scenarios.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Implementing io2 Block Express volumes requires careful evaluation
of I/O requirements and cost considerations. Focus on workloads
that genuinely require extreme I/O performance and can justify the
additional costs through improved application performance and
business outcomes.

### Implementation steps

- Identify Microsoft workloads with high I/O requirements that
would benefit from io2 Block Express performance
characteristics, particularly SQL Server databases and
analytics applications.
- Analyze current I/O patterns including IOPS requirements,
throughput needs, and latency sensitivity to determine if
io2 Block Express is appropriate.
- Ensure compatibility with Nitro System-based instances that
can fully utilize io2 Block Express performance
capabilities.
- Configure io2 Block Express volumes with appropriate IOPS
provisioning based on workload requirements and performance
testing results.
- Implement performance testing in non-production environments
to validate expected performance improvements and cost
justification.
- Monitor storage performance metrics including IOPS
utilization, throughput, and latency to ensure optimal
configuration and utilization.
- Establish cost monitoring and optimization procedures to
ensure io2 Block Express usage remains cost-effective for
the performance benefits provided.
- Document io2 Block Express configuration standards and use
cases for consistent implementation across high-performance
Microsoft workloads.

## Resources

**Related documents:**

- [Provisioned
IOPS SSD (io2 Block Express) volumes](https://docs.aws.amazon.com/ebs/latest/userguide/provisioned-iops.html#io2-block-express)
- [Best
practices for Amazon RDS for SQL Server with Amazon EBS io2
Block Express volumes up to 64 TiB](https://aws.amazon.com/blogs/database/best-practices-for-amazon-rds-for-sql-server-with-amazon-ebs-io2-block-express-volumes-up-to-64-tib/)

**Related tools:**

- [io2
Block Express considerations](https://docs.aws.amazon.com/ebs/latest/userguide/provisioned-iops.html#io2-bx-considerations)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftperf03-bp02.html*

---

# MSFTPERF03-BP03 Consider Amazon FSx for Windows File Server

Amazon FSx for Windows File Server is a managed service that
provides file storage using Microsoft Windows file system
technology. It supports Windows file system features and uses the
Server Message Block (SMB) protocol for network file access, making
it compatible with various Windows-based enterprise workloads and
applications. The service offers integration with other AWS services
and performance optimized for enterprise applications, aiming to
provide low-latency file storage. FSx for Windows File Server is
designed for Windows workloads that require shared file storage,
such as File Servers, Application Server configuration stores, and
even Microsoft SQL Server databases.

**Desired outcome:** Achieve
high-performance, fully managed Windows file storage that seamlessly
integrates with Microsoft workloads, providing native Windows file
system features, SMB protocol support, and optimized performance
while reducing operational overhead through AWS-managed
infrastructure.

**Common anti-patterns:**

- Implementing self-managed Windows file servers on EC2 without
evaluating FSx benefits, missing opportunities to reduce
operational overhead and improve performance through managed
services.
- Using general-purpose storage solutions for Windows workloads
that require specific Windows file system features, potentially
limiting functionality and performance.
- Choosing FSx configurations without proper performance analysis,
leading to either over-provisioned resources that increase costs
or under-provisioned storage that impacts application
performance.

**Benefits of establishing this best
practice:**

- Reduced operational overhead through fully managed Windows file
storage that eliminates the need to manage file server
infrastructure, patching, and maintenance tasks.
- Enhanced performance and reliability through AWS-managed
infrastructure optimized for Windows workloads with built-in
high availability and backup capabilities.
- Native Windows integration providing full compatibility with
Windows file system features, Active Directory integration, and
SMB protocol support for seamless application integration.

**Level of risk exposed if this best practice
is not established:** Low

## Implementation guidance

Implementing Amazon FSx for Windows File Server requires
understanding your file storage requirements and migration
planning from existing file server infrastructure. Focus on
workloads that require Windows-native file system features and can
benefit from managed service advantages.

### Implementation steps

- Assess current Windows file storage requirements including
capacity, performance, and feature needs for your Microsoft
workloads.
- Evaluate existing file server infrastructure and identify
workloads suitable for migration to FSx for Windows File Server.
- Choose appropriate FSx deployment options including
Single-AZ or Multi-AZ configurations based on availability
and performance requirements.
- Configure FSx file systems with appropriate storage
capacity, throughput, and IOPS settings based on workload
analysis and performance testing.
- Plan migration procedures for existing file shares and data,
including user access permissions and Active Directory
integration.
- Implement backup and disaster recovery strategies using
FSx's built-in backup capabilities and cross-region
replication options.
- Monitor file system performance and utilization using
CloudWatch metrics to optimize configuration and identify
scaling needs.
- Establish operational procedures for FSx management
including access control, monitoring, and capacity planning
for ongoing operations.

## Resources

**Related documents:**

- [What
is Amazon FSx for Windows File Server?](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/what-is.html)
- [Optimizing
Amazon FSx for Windows File Server performance with new
metrics](https://aws.amazon.com/blogs/storage/optimizing-amazon-fsx-for-windows-file-server-performance-with-new-metrics/)

**Related tools:**

- [Amazon FSx performance](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/performance.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftperf03-bp03.html*

---

# MSFTPERF03-BP04 Consider Amazon FSx for NetApp ONTAP

Amazon FSx for NetApp ONTAP is a fully managed AWS service that
provides scalable, high-performance file storage based on the
widely-used NetApp ONTAP file system. It combines the familiar
features and capabilities of NetApp systems with the benefits of a
cloud-managed service. This service offers fast, flexible shared
file storage accessible from Linux, Windows, and macOS instances,
both in AWS and on-premises. FSx for ONTAP provides high-performance
SSD storage with very low latencies and also HDD storage. Amazon FSx for NetApp ONTAP offers robust file storage capabilities, including
support for petabyte-scale datasets in a single namespace and high
throughput of up to tens of GBps per file system.

**Desired outcome:** Achieve
enterprise-grade, high-performance file storage for Microsoft
workloads through FSx for ONTAP, providing multi-protocol
access, advanced data management features, and cost optimization
capabilities while maintaining compatibility with existing NetApp
environments and Microsoft applications.

**Common anti-patterns:**

- Using basic file storage solutions for enterprise Microsoft
workloads without evaluating FSx for ONTAP's advanced features,
missing opportunities for performance optimization and data
management capabilities.
- Implementing FSx for ONTAP without leveraging its multi-protocol
capabilities, limiting the potential for workload consolidation
and simplified architecture.
- Choosing FSx for ONTAP configurations without considering data
tiering and compression features, potentially missing
significant cost optimization opportunities.

**Benefits of establishing this best
practice:**

- Superior performance and scalability through NetApp ONTAP
technology providing high throughput, low latency, and support
for petabyte-scale datasets in a single namespace.
- Advanced data management capabilities including automatic
tiering, compression, deduplication, and snapshot technologies
that optimize both performance and costs.
- Multi-protocol flexibility supporting NFS, SMB, iSCSI, and NVMe
protocols, enabling consolidation of diverse Microsoft workload
storage requirements on a single platform.

**Level of risk exposed if this best practice
is not established:** Low

## Implementation guidance

Implementing Amazon FSx for NetApp ONTAP requires understanding
your enterprise storage requirements and planning for advanced
data management features. Focus on workloads that can benefit from
multi-protocol access, advanced data services, and cost
optimization through data efficiency features.

### Implementation steps

- Assess enterprise storage requirements for Microsoft
workloads including performance, capacity, protocol needs,
and data management requirements.
- Evaluate existing NetApp environments and plan migration
strategies to leverage familiar ONTAP features in the cloud.
- Configure FSx for ONTAP file systems with appropriate
performance tiers, capacity planning, and multi-protocol
access based on workload requirements.
- Implement data efficiency features including compression,
deduplication, and automatic tiering to optimize storage
costs and performance.
- Configure multi-protocol access (SMB, NFS, iSCSI) to support
diverse Microsoft workload requirements and enable workload
consolidation.
- Establish backup and disaster recovery procedures using
ONTAP's snapshot and replication capabilities for data
protection.
- Monitor storage performance, utilization, and cost
optimization through CloudWatch metrics and ONTAP management
tools.
- Implement ongoing data management policies including
tiering, retention, and capacity planning to maintain
optimal performance and costs.

## Resources

**Related documents:**

- [What
is Amazon FSx for NetApp ONTAP?](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/what-is-fsx-ontap.html)
- [Managing
storage on Windows servers with Amazon FSx for NetApp ONTAP](https://aws.amazon.com/blogs/storage/managing-storage-on-windows-servers-with-amazon-fsx-for-netapp-ontap/)
- [Best
practice configuration of Amazon FSx for NetApp ONTAP for
Microsoft SQL Server workloads](https://aws.amazon.com/blogs/storage/best-practice-configuration-of-amazon-fsx-for-netapp-ontap-for-microsoft-sql-server-workloads/)
- [AWS Guidance: Best Practices for running MSSQL workloads on FSx for ONTAP](https://repost.aws/articles/AROwbUp134QbGhtrPPEYeuog/aws-guidance-best-practices-for-running-mssql-workloads-on-fsx-for-netapp-ontap)

**Related tools:**

- [Amazon FSx for NetApp ONTAP performance](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/performance.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftperf03-bp04.html*

---

# MSFTPERF03-BP05 Leverage instance store temporary block storage for EC2 instances

An instance store is a form of temporary block-level storage for EC2
instances, provided by disks physically attached to the host
computer. It is well-suited for storing frequently changing data
such as buffers, caches, and scratch data, as well as temporary data
replicated across multiple instances like in a load-balanced web
server pool, and Microsoft SQL Server TempDB data. The capacity and
number of instance store volumes available vary depending on the
instance type and size, with some instance types not offering
instance stores at all.

**Desired outcome:** Maximize I/O
performance for temporary and cache data in Microsoft workloads by
leveraging instance store volumes that provide the highest possible
storage performance through direct attachment to the host computer,
particularly beneficial for SQL Server TempDB, application caches,
and high-performance computing scenarios.

**Common anti-patterns:**

- Using EBS volumes for temporary data and caches when instance
store volumes are available, missing opportunities for maximum
I/O performance and potentially increasing storage costs.
- Storing persistent or critical data on instance store volumes
without understanding their temporary nature, risking data loss
during instance stops or failures.
- Choosing instance types without instance store when workloads
could benefit from high-performance temporary storage, limiting
application performance potential.

**Benefits of establishing this best
practice:**

- Maximum I/O performance through direct-attached storage that
provides the highest possible throughput and lowest latency for
temporary data operations.
- Cost optimization by using included instance store volumes for
appropriate use cases instead of provisioning additional EBS
volumes for temporary storage needs.
- Enhanced application performance for Microsoft workloads that
heavily utilize temporary storage, such as SQL Server TempDB
operations and application-level caching.

**Level of risk exposed if this best practice
is not established:** Low

## Implementation guidance

Implementing instance store volumes requires careful planning to
ensure appropriate use cases and data management practices. Focus
on temporary, cache, and scratch data that can benefit from
maximum I/O performance while ensuring critical data remains on
persistent storage.

### Implementation steps

- Identify Microsoft workload components that generate
temporary data, caches, or scratch files that could benefit
from high-performance instance store volumes.
- Evaluate EC2 instance families that include instance store
volumes and assess their capacity and performance
characteristics for your workload requirements.
- Plan data placement strategies to ensure only appropriate
temporary data is stored on instance store volumes while
maintaining persistent data on EBS.
- Configure applications to utilize instance store volumes for
SQL Server TempDB, application caches, temporary files, and
other high-I/O temporary data.
- Implement data management procedures that account for the
temporary nature of instance store volumes, including
startup initialization and data replication strategies.
- Monitor instance store utilization and performance to
validate expected benefits and optimize usage patterns for
maximum efficiency.
- Establish operational procedures for instance lifecycle
management that properly handle instance store data during
maintenance and scaling operations.
- Document instance store usage patterns and include in
application deployment and disaster recovery procedures.

## Resources

**Related documents:**

- [Amazon EC2 instance store](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html)
- [Make
instance store volume available for use on an EC2
instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/making-instance-stores-available-on-your-instances.html)

**Related tools:**

- [Instance
store volumes limits for EC2 instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-store-volumes.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftperf03-bp05.html*

---
