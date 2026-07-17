# Performance efficiency

**Pages**: 3

---

# Assess

In the assess phase of migration to AWS, it's important to
evaluate performance requirements for your workloads and ensure
your existing OS platforms align with those needs. Efficient data
transfer methods and the selection of the most suitable storage
options are key considerations. Additionally, identifying network
requirements and implementing a strategy for managing IP address
conflicts and DNS requirements are vital steps for a smooth and
successful migration process.

MIG-PERF-01: Have you evaluated performance requirements for the workloads that you are migrating?

AWS has various options for instance class, sizes, purchase
options, scaling options, and managed services. Consider how
using these capabilities during and after migration can lead to
improved performance in your cloud infrastructure.

## MIG-PERF-BP-1.1: Understand the performance characteristics of your current infrastructure to select the best performant optimized cloud infrastructure

This BP applies to the following best practice areas:
Architecture selection

### Implementation guidance

**Suggestion 1.1.1:** Use discovery tools for a comprehensive view of IT inventory.

Discovery tools offer a comprehensive view of an organizations IT environment, including physical servers, virtual machines, applications and their inter-dependencies. This enhanced visibility enables better planning and decision-making during the migration process. Organizations can identify potential bottlenecks, performance issues, and optimization opportunities using [discovery tools](https://aws.amazon.com/prescriptive-guidance/migration-tools/migration-discovery-tools/).

Discovery tools collect various information, such server names, CPU, disk, and memory utilized. They also collect both server and database configuration information. Server information includes hostnames, IP addresses, and MAC addresses, as well as the resource allocation and utilization details of key resources such as CPU, network, memory, and disk. Collected database information includes the database engine identity, version, and edition. Once collected, this information can be used to size AWS resources as part of migration planning. Addressing these issues before migration can lead to improved performance in the cloud environment.

[Accurate information provided by the discovery tools](https://aws.amazon.com/blogs/architecture/selecting-the-appropriate-discovery-tool-for-your-cloud-migration/) helps determine the appropriate resource allocation and instance sizing on AWS. By understanding the resource utilization patterns and peak loads of application, organizations can provision the right type and size of AWS instance to support the migrated workloads efficiently.

MIG-PERF-02: Have you identified your existing OS platforms to meet your performance requirements?

Gain insights into the assessment and selection process for your
current OS platforms and the migration tools considered to meet
your performance requirements.

## MIG-PERF-BP-2.1: Evaluate operating systems and versions that are running in your environment

This BP applies to the following best practice areas: Compute
and hardware

### Implementation guidance

**Suggestion 2.1.1:** Consider an assessment for a legacy workload migration.

Many companies are still running legacy and non-x86 systems in their datacenters, such as mainframe, midrange, or UNIX proprietary systems. Additionally, some applications run on legacy operating systems like Windows Server 2003, 2008, and 2012. Migrating these workloads across hardware architectures to AWS can be a complex process, but there are several best practices to improve the likelihood of a successful transition.

To embark on a successful migration process, it is essential to conduct a comprehensive evaluation of your current systems, delving into their interdependencies, configurations, and resource demands. Pay close attention to any legacy operating system versions and non-x86 hardware that might still be in operation. Equipped with this understanding, create a migration plan that outlines clear objectives and a well-defined timeline. This plan should serve as the roadmap for a smooth transition, making the migration process efficient and minimizing potential disruptions to your operations.

**Suggestion 2.1.2:** When dealing with non-x86 architectures, there are primarily two approaches: emulation and virtualization. Evaluate both.

- Emulation involves the system simulating the behavior of
a different architecture. Essentially, it acts as if it
were the target architecture, translating instructions
as needed. While emulation is crucial when running
software designed for a completely distinct
architecture, it can be relatively slower and less
efficient than native running or virtualization. It
might also consume more system resources, potentially
impacting performance compared to the native
architecture.
- Virtualization, on the other hand, involves creating a
virtual machine (VM) that can run an operating system
designed for a specific architecture. Virtualization is
generally more efficient and provides better performance
compared to emulation because it leverages the
underlying hardware and allows multiple VMs to run on
the same physical server. While this approach often
requires more initial setup, it's a popular choice for
running non-x86 architectures in data centers.

The choice between emulation and virtualization depends on your specific use case, performance requirements, and the compatibility of the software you want to run with the chosen method.

For more detail, see the following:

- [Rehosting Legacy systems to AWS with Stromasys](https://aws.amazon.com/blogs/apn/re-hosting-sparc-alpha-or-other-legacy-systems-to-aws-with-stromasys/)
- [Refactoring applications with AWS Blue Age](https://docs.aws.amazon.com/m2/latest/userguide/refactoring-m2.html)
- [Legacy Migration Options to AWS cloud](https://aws.amazon.com/blogs/apn/demystifying-legacy-migration-options-to-the-aws-cloud/)

MIG-PERF-03: How do you find the best transfer methods for efficiently transferring storage data into and out of AWS?

Planning is crucial when migrating data to the cloud. Data is
the foundation for successful application deployments,
analytics, and machine learning. Customers frequently perform
bulk migrations of their application data when moving to the
cloud. There are different online and offline methods for moving
your data to the cloud. When proceeding with a data migration,
data owners must consider the amount of data, transfer time,
frequency, bandwidth, network costs, and security concerns. No
matter how data makes its way to the cloud, customers often ask
us how they can transfer their data to the cloud as quickly and
as efficiently as possible.

## MIG-PERF-BP-3.1: Evaluate the different methods to migrate data and select the one best for you use case: online mode, offline mode, or hybrid approach

This BP applies to the following best practice areas: Data
management

### Implementation guidance

**Suggestion 3.1.1:** Review [AWS Cloud Data Migration](https://aws.amazon.com/cloud-data-migration/) services for online, offline, and hybrid data transfer options.

Data is a cornerstone of successful application deployments, analytics workflows, and machine learning innovations. When moving data to the cloud, you need to understand where you are moving it for different use cases, the types of data you are moving, and the network resources available, among other considerations. AWS offers a wide variety of services and partner tools to help you migrate your data sets, whether they are files, databases, machine images, block volumes, or even tape backups. AWS provides a portfolio of data transfer services to provide the right solution for any data migration project. The connectivity is a major factor in data migration, and AWS has offerings that can address your hybrid cloud storage, online data transfer, and offline data transfer needs.

For more detail, see [Best practices for accelerating data migrations using AWS Snowball Edge Edge](https://aws.amazon.com/blogs/storage/best-practices-for-accelerating-data-migrations-using-aws-snowball-edge/).

MIG-PERF-04: How do you select the best-performing storage option for your workload?

AWS offers a broad portfolio of reliable, scalable, and secure
storage services for storing, accessing, protecting, and
analyzing your data. This makes it easier to match your storage
methods with your needs, and provides storage options that are
not easily achievable with on-premises infrastructure. When
selecting a storage service, aligning it with your access
patterns is critical to achieve the performance you want. You
can select from block, file, and object storage services, as
well as cloud data migration options for your workload.

## MIG-PERF-BP-4.1: Select the storage solution based on the characteristics of your workloads

Identify and document the workload storage needs and define the storage characteristics of each location. Examples of storage characteristics include: shareable access, file size, growth rate, throughput, IOPS, latency, access patterns, and persistence of data. Use these characteristics to evaluate if block, file, object, or instance storage services are the most efficient solution for your storage needs.

This BP applies to the following best practice areas: Data management

### Implementation guidance

**Suggestion 4.1.1:** Understand storage characteristics and requirements.

Identify your workload's most important storage performance metrics and implement improvements as part of a data-driven approach, using benchmarking or load testing. Use this data to identify where your storage solution is constrained, and examine configuration options to improve the solution. Determine the expected growth rate for your workload and choose a storage solution that meets those rates. Research AWS storage offerings to determine the correct storage solution for your various workload needs. Provisioning storage solutions in AWS provide the opportunity for you to test storage offerings and determine if they are appropriate for your workload needs.

**Suggestion 4.1.2:** Make decisions based on access patterns and metrics.

Choose storage systems based on your workload's access patterns and by determining how the workload accesses data. Configure the storage options you choose to match your data access patterns.

How you access data impacts how the storage solution performs. Select the storage solution that aligns best to your access patterns, or consider changing your access patterns to align with the storage solution to maximize performance.

For example, creating a RAID 0 array allows you to achieve a higher level of performance for a file system than what you can provision on a single volume. Consider using RAID 0 when I/O performance is more important than fault tolerance. For example, you could use it with a heavily used database where data replication is already set up separately.

For storage systems that are a fixed size, such as Amazon EBS or Amazon FSx, monitor the amount of storage used versus the overall storage size and create automation if possible to increase the storage size when reaching a threshold.

For more detail, see the following:

- [Amazon EBS Volume Types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html)
- [Amazon EC2 Storage](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Storage.html)
- [Amazon EFS: Amazon EFS Performance](https://docs.aws.amazon.com/efs/latest/ug/performance.html)
- [Amazon FSx for Lustre Performance](https://docs.aws.amazon.com/fsx/latest/LustreGuide/performance.html)
- [Amazon FSx for Windows File Server Performance](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/performance.html)
- [Amazon
Glacier: Amazon Glacier Documentation](https://docs.aws.amazon.com/amazonglacier/latest/dev/introduction.html)
- [Amazon S3: Request Rate and Performance Considerations](https://docs.aws.amazon.com/AmazonS3/latest/dev/request-rate-perf-considerations.html)
- [Cloud
Storage with AWS](https://aws.amazon.com/products/storage/)
- [EBS
I/O Characteristics](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/ebs-io-characteristics.html)
- [Monitoring and understanding Amazon EBS performance using Amazon CloudWatch](https://aws.amazon.com/blogs/storage/valuable-tips-for-monitoring-and-understanding-amazon-ebs-performance-using-amazon-cloudwatch/)

Related videos:

- [Deep
dive on Amazon EBS (STG303-R1)](https://www.youtube.com/watch?v=wsMWANWNoqQ)
- [Optimize
your storage performance with Amazon S3](https://www.youtube.com/watch?v=54AhwfME6wI)

Related examples:

- [Amazon EFS CSI Driver](https://github.com/kubernetes-sigs/aws-efs-csi-driver)
- [Amazon EBS CSI Driver](https://github.com/kubernetes-sigs/aws-ebs-csi-driver)
- [Amazon EFS Utilities](https://github.com/aws/efs-utils)
- [Amazon EBS Auto scale](https://github.com/awslabs/amazon-ebs-autoscale)
- [Amazon S3 Examples](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/s3-examples.html)

## MIG-PERF-BP-4.2: Choose the optimal storage solutions for specialized workloads, such as SAP and VMware cloud on AWS

This BP applies to the following best practice areas: Data
management

### Implementation guidance

**Suggestion 4.2.1:** Implement one of four categories of storage capabilities for VMware Cloud on AWS.

[VMware Cloud on AWS](https://aws.amazon.com/vmware/) is a jointly engineered solution by VMware and AWS that brings VMware's Software-Defined Data Center (SDDC) technologies to the global AWS infrastructure.

If you have workloads with varying storage requirements, it's important to understand the storage options available and how they could work best for different scenarios.

VMware Cloud on AWS offers VMware vSphere workloads with choice and flexibility to integrate with [multiple storage services](https://aws.amazon.com/blogs/storage/storage-options-and-designs-for-vmware-cloud-on-aws/). However, each service is optimized for a specific scenario and no single approach is ideal for all workloads. To choose the right service, you must first understand the storage requirements and performance profiles of your VMware vSphere workloads. With that in mind, you can plan and implement your storage with cost, availability, and performance requirements optimized for your workloads.

**Suggestion 4.2.2:** Select the [optimal storage solutions](https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/design-principle-14.html) for your SAP workloads.

AWS offers a wide range of services, including block, file, and object storage, to meet the storage needs of your SAP databases, applications, and backups. We recommend following the [guidelines](https://docs.aws.amazon.com/wellarchitected/latest/sap-lens/design-principle-14.html) that have been benchmarked and certified by SAP. For SAP HANA, there are very specific guidelines. Other databases require more analysis to match your workload.

## MIG-PERF-BP-4.3: Evaluate the different storage tiers at prices to meet your migrated workload's performance

This BP applies to the following best practice areas: Data management

By identifying the most appropriate destination for specific types of data, you can reduce Amazon Elastic Block Store (Amazon EBS) and Amazon Simple Storage Service (Amazon S3) cost while maintaining the required performance and availability. For example, where performance requirements are lower, using Amazon EBS Throughput Optimized HDD (st1) storage typically costs half as much as the default General Purpose SSD (gp2) storage option.

### Implementation guidance

**Suggestion
4.3.1:**
[Understand
EBS storage tiers](https://aws.amazon.com/blogs/storage/how-to-choose-the-best-amazon-ebs-volume-type-for-your-self-managed-database-deployment/) to balance performance and cost in
AWS.

- Use provisioned IOPS SSD (io1) volumes for high
performance databases and transactional workloads. io1
provides low latency and the ability to provision high
IOPS. However, it is more expensive than other EBS
types.
- Use general purpose SSD (gp2) volumes for most
workloads. gp2 provides a good blend of price and
performance. You can provision up to 16,000 IOPS per
volume.
- Use throughput optimized HDD (st1) for large, sequential
workloads like log processing. st1 provides low cost per
GB of storage.
- Use cold HDD (sc1) for infrequently accessed storage.
sc1 is the lowest cost EBS storage.
- Use EBS snapshots to take backups of EBS volumes.
Snapshots only copy changed blocks, minimizing storage
costs.
- Resize EBS volumes up or down as needed to right-size
storage to your current workload. This avoids
over-provisioning expensive storage.
- Use Elastic File System (EFS) for shared storage across
multiple EC2 instances. EFS storage auto-scales on
demand without needing to provision capacity ahead of
time.
- Use Lifecycle Manager to automatically move old EBS
snapshots to cheaper S3 storage. This reduces your EBS
storage costs.
- Monitor your storage metrics in CloudWatch and adjust.

For more detail, see
[Cost-optimizing Amazon EBS volumes using AWS Compute Optimizer](https://aws.amazon.com/blogs/storage/cost-optimizing-amazon-ebs-volumes-using-aws-compute-optimizer/).

**Suggestion 4.3.2:** [Lower your storage costs](https://aws.amazon.com/blogs/storage/5-ways-to-reduce-costs-using-amazon-s3-storage-lens/) without sacrificing performance with Amazon S3.

If you have an increasing number of [Amazon S3](https://aws.amazon.com/s3/storage-classes/) buckets, spread across tens or even hundreds of accounts, you might be in search of a tool that makes it easier to manage your growing storage footprint and improve cost efficiencies. [Amazon S3 Storage Lens](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage_lens.html) is an analytics feature built in to the Amazon S3 console to help you gain organization-wide visibility into your object storage usage and activity trends, and to identify cost savings opportunities. Amazon S3 Storage Lens is available for all Amazon S3 accounts. You can also upgrade to [advanced metrics](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage_lens_basics_metrics_recommendations.html#storage_lens_basics_metrics_selection) to receive additional metrics, insights, and an extended data retention period.

For more detail, see [Amazon S3 Storage Classes](https://aws.amazon.com/s3/storage-classes/#Performance_across_the_S3_Storage_Classes).

MIG-PERF-05: Have you identified the network requirements for your migration?

Establishing secure and reliable network connectivity is
paramount to facilitating workload migrations in the AWS Cloud.
In order to accomplish this, it is necessary to examine network
requirements in detail, including on-premises firewall rules,
traffic prioritization rules, and source change rates. This
practice creates seamless communication during and after
migration, minimizes disruptions, ensures optimal performance,
and maintains uninterrupted connectivity. AWS offers a wide
variety of connectivity options and features tailored to suit
the migration requirements and existing network infrastructure
of organizations.

## MIG-PERF-BP-5.1: Establish a reliable network connectivity from on-premises to AWS to ensure performance

### Implementation guidance

**Suggestion 5.1.1:** Use dedicated network connectivity options for reliably [connecting on-premises to AWS](https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/network-to-amazon-vpc-connectivity-options.html).

There are public and private connectivity options, but data transfer over the internet may not be a reliable means of data communication. VPNs provide private connectivity, but they too use internet in the background, therefore relying heavily on external factors of the network. Such customers use a dedicated network channel or option such as [AWS Direct Connect](https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/aws-direct-connect.html) to ensure performance over network. AWS Direct Connect creates highly resilient network connections between Amazon Virtual Private Cloud and your on-premises infrastructure. As a result, it is a viable solution for workloads requiring low latency and high bandwidth, such as real-time applications and large data transfers.

**Suggestion 5.1.2:** Identify the network bandwidth required and supported for ensuring performance.

First of all, network bandwidth *required* and *supported* are two different identification points. Let's first look at how to identify network bandwidths *required* to ensure performance. The requirement depends on workloads or applications that you are looking to migrate. Sensitive applications that are heavily write intensive require [continuous data protection](https://en.wikipedia.org/wiki/Continuous_Data_Protection) mechanisms in order to migrate them to the cloud. The change rate (in Mbps or Gbps) on these source applications determine how much bandwidth you want to provision. Accordingly, you can provision the network bandwidth higher than the source change rate. AWS Direct Connect provides multiple options for connection [speeds](https://aws.amazon.com/directconnect/faqs/) (1 Gbps, 10 Gbps, 100 Gbps) that you can leverage to provision higher network bandwidths than the source change rate.

Once the network is provisioned for migrating data, you need to identify how much bandwidth does it actually support. You can check that by running any [third-party network speed tests](https://docs.aws.amazon.com/drs/latest/userguide/perform-connectivity-bandwidth-test.html) (like [iperf](https://iperf.fr/)).

## MIG-PERF-BP-5.2: Assure that network performance is not impacted by external factors

### Implementation guidance

**Suggestion 5.2.1**: Identify network bottlenecks on-premises.

Identify network bottlenecks in your on-premises firewalls, perimeter networks, proxies, routers, or any other traffic de-prioritizations. This could impact the network throughputs required for migrating data to cloud.

**Suggestion
5.2.1:** Provision the right AWS
instance types and EBS volumes that support the required
network bandwidth.

Make sure that the AWS instance types you provision for your
target workloads support the network bandwidths required for
the data migration. Each AWS instance type support a
specific
[baseline
and burst bandwidth](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-network-bandwidth.html), so make sure that you correctly
right-size the instance type for your workload on AWS.
Similarly, provision the right EBS volume to support the
required IO performance.

For more detail, see the following:

- [Amazon EC2 instance network bandwidth](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-network-bandwidth.html)
- [RDS
Instance types and bandwidths supported](https://aws.amazon.com/rds/instance-types/)
- [EBS
volume types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volume-types.html) and the maximum throughput it supports

MIG-PERF-06: Do you have a strategy to manage IP address conflicts and DNS requirements as part of the migration process?

In cloud migrations, the key elements of DNS, DHCP, and IP address
considerations are essential for the seamless operation of
applications and services in the cloud environment.

## MIG-PERF-BP-6.1: Identify a migration strategy for your network components (DNS, IP addressing, and DHCP) migration

This BP applies to the following best practice areas: Networking
and content delivery

### Implementation guidance

**Suggestion 6.1.1:** Define a DNS management system for your migrated workloads on AWS.

The DNS management planning and setup is a pre-migration task. There are two options for setting up DNS for migrated workloads:

- Customers choose to use the same DNS management system
on-premises while their workloads are migrated to AWS. In
this scenario, customers can use AWS Route 53 Resolver
endpoints to create a
hybrid DNS solution between AWS and an on-premises
network.
- Customers can set up
[DNS
on Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/migrate-dns-domain-in-use.html) and migrate existing records, or
create new records from the on-premises DNS environment to
the public or private hosted zone on Amazon Route 53.

**Suggestion 6.1.2:** Design a migration strategy for IPs.

Request elastic IP addresses for resources requiring static public IP addresses, allocate appropriate CIDR blocks to VPCs and subnets to accommodate all migrated resources, and conduct meticulous IP range planning to prevent IP conflicts between on-premises and AWS environments post-migration. It is essential to determine if IP addresses need to be reassigned after migration to meet specific requirements during the migration process. A reassignment of IP addresses is likely necessary for compatibility with third-party systems that rely on fixed IP addresses to establish connections or communicate with the migrated resources.

It is also possible that certain regulatory requirements require the use of static private IP addresses for specific applications or services, necessitating the use of same private IP on AWS to comply with those requirements. For rehost migrations using AWS Application Migration service (AWS MGN), customer often use the *copy private IP* feature to use the same private IP from the source server on the target environment on AWS.

If you are looking to migrate from IPv4 to IPv6 within AWS, you can use the weighted routing feature with [Amazon VPC Lattice](https://aws.amazon.com/blogs/networking-and-content-delivery/accelerate-your-ipv6-adoption-on-aws-with-amazon-vpc-lattice/) to slowly shift the traffic.

**Suggestion 6.1.3:** Use Amazon-provided DHCP servers and option sets.

DHCP servers should be configured in the new infrastructure to provide IP addresses within the appropriate range if IP addresses are assigned using DHCP.

For more detail, see [Hybrid Cloud DNS Options for Amazon VPC](https://docs.aws.amazon.com/whitepapers/latest/hybrid-cloud-dns-options-for-vpc/hybrid-cloud-dns-options-for-vpc.html).

**Suggestion 6.1.4:** Consider the following network migration checklist.

Proper DNS configuration, IP planning, and DHCP are key factors to consider when migrating workloads to AWS. Familiarize yourself with the following items to plan for a successful network's components migration.

- Identify the most efficient method of collecting the
existing and new IP schemes for to-be migrated systems.
This fosters a seamless transition while ensuring accurate
addressing for optimal performance.
- Implement a well-defined process to acquire the new and
current DNS names for the systems undergoing migration.
This helps with accurate name resolution while preserving
seamless communication.
- Modify load balancers, proxies, or any other network
devices in order to redirect to the new IP addresses or
domains post-migration. This avoids interrupting
resources.
- Update DNS settings after the migration to point towards
the newly migrated cloud resources so that cloud-based
services are properly routed and accessible.
- The DHCP configuration may need to be adjusted in order to
accommodate the integration of new systems. This verifies
that IP allocation and network settings accurately reflect
the newly-migrated components.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/migration-lens/assess-perf.html*

---

# Mobilize

During the mobilize phase of your migration, you need to evaluate
the different components that make up the building blocks of your
migrated workloads and make trade-offs to select the performance
that fits your business requirements. To do this, you need to set
up the right metrics for performance monitoring, evaluate the
different options to build your architecture, and benchmark the
migrated workload against the on-premises workload to measure the
different components' performance and adjust if needed.

MIG-PERF-07: How do you verify that the shared services used for migration during the mobilize phase are performing efficiently?

The mobilize phase lays the foundation for tools, process, and
culture that accelerate your migration at scale. The account
planning, Architecture selection, monitoring, and observability
setup in the mobilize phase are building blocks for any future
migrations done. Some of the shared services we set up and
validate in the mobilize phase are landing zones, AWS Transit Gateway, and Amazon VPC Lattice.

## MIG-PERF-BP-7.1: Identify the right CloudWatch metrics to capture or detect anomaly and identify performance blockers for shared services

This BP applies to the following best practice areas:
Architecture selection

### Implementation guidance

**Suggestion 7.1.1:** Identify the right metrics and detect anomalies.

During cloud migration, it's essential to monitor AWS resource performance effectively. [CloudWatch Metrics Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/query_with_cloudwatch-metrics-insights.html) helps by providing a SQL query engine to analyze performance metrics in real-time, aiding in the detection of trends and patterns during the migration process. For more focused monitoring, [CloudWatch anomaly detection](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.html) can be enabled for critical metrics, using machine learning to forecast normal behavior and alert on anomalies. Additionally, [metrics explorer](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Metrics-Explorer.html) is a tag-based tool that allows for the organization and visualization of metrics by tags and resource properties, which is particularly useful for maintaining oversight during and after resource migration.

## MIG-PERF-BP-7.2: Select the best performing cloud infrastructure that can scale for additional workloads in future without any performance impact

This BP applies to the following best practice areas:
Architecture selection

### Implementation guidance

**Suggestion 7.2.1:** Select the best performing architecture from storage, database, compute, and network perspective.

During the mobilize phase, you are essentially laying the groundwork for your first wave of migration and any future migrations. In this phase, you define and implement an AWS landing zone, and other AWS security and network services that can scale as you migrate additional applications. There are multiple approaches and considerations when selecting the best performing architecture, like factoring cost requirements into decisions, or selecting the best compute, or storage, or database, or network architecture. The best performing architecture in your case would be what best fit your requirements.

For more detail, see the following:

- [Architecture
selection - Performance Efficiency Pillar](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/architecture-selection.html)
- [Compute
and hardware - Performance Efficiency Pillar](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/compute-and-hardware.html)
- [Data
management - Performance Efficiency Pillar](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/data-management.html)
- [Networking and content delivery - Performance Efficiency Pillar](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/networking-and-content-delivery.html)

**Suggestion 7.2.2:** Use existing reference patterns for your architecture to achieve a cost-effective solution.

AWS Solutions Architects, [AWS Reference Architectures](https://aws.amazon.com/architecture/), and [AWS Partner Network (APN)](https://aws.amazon.com/partners/) partners can help you select an architecture based on industry knowledge. You can maximize performance and efficiency by evaluating existing reference architectures and using your analysis to select services and configurations for your workload.

## MIG-PERF-BP-7.3: Reduce the blast radius for performance impact into a single account

This BP applies to the following best practice areas:
Architecture selection

### Implementation guidance

**Suggestion 7.3.1:** Organize your AWS accounts to isolate performance impact.

As you are laying the foundation during the mobilize phase of the migration, [account structuring](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/patterns-for-organizing-your-aws-accounts.html) is essential to safeguard performance. Account structuring or organizing can isolate performance impact to a single account, reducing the blast radius. Customers can use [AWS Organizations](https://aws.amazon.com/organizations/), an AWS service to centrally manage and govern multiple accounts. We looked at account structuring during the security pillar, but this specific best practice applies to multiple pillars of the Well-Architected Framework. There are several strategies for [multi-account landing zone accounts](https://docs.aws.amazon.com/managedservices/latest/onboardingguide/malz-net-arch-accounts.html).

## MIG-PERF-BP-7.4: Benchmark existing workloads for performance

### Implementation guidance

**Suggestion 7.4.1:** Benchmark the performance of an existing workload to understand how it performs on the cloud.

Use the data collected from benchmarks to drive architectural decisions. Benchmarking is generally quicker to set up than load testing and is used to evaluate the technology for a particular component. Benchmarking is often used at the start of a new project, when you lack a full solution to load test.

You can either build your own custom benchmark tests, or you can use an industry standard test, such as [TPC-DS](https://www.tpc.org/default5.asp), to benchmark your data warehousing workloads. Industry benchmarks are helpful when comparing environments. Custom benchmarks are useful for targeting specific types of operations that you expect to make in your architecture.

When benchmarking, it is important to pre-warm your test environment to ensure valid results. Run the same benchmark multiple times to capture any variance over time.

Because benchmarks are generally faster to run than load tests, they can be used earlier in the deployment pipeline and provide faster feedback on performance deviations. When you evaluate a significant change in a component or service, a benchmark can be a quick way to see if you can justify the effort to make the change. Using benchmarking in conjunction with load testing is important because load testing informs you about how your workload will perform in production.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/migration-lens/mobilize-perf.html*

---

# Migrate

As you migrate your workload, you need to consistently compare the
migrated workload against the performance requirements that you
identified through KPIs or benchmarks. To do this, you need to
perform the necessary testing on your migrated applications,
capture any issues or lessons learned, and iterate for the next
migration wave.

MIG-PERF-08: How do you ensure improved and consistent performance of your applications during migration?

Migration is an iterative process as most enterprise customers
are migrating thousands of servers and applications. Migration
is often planned in waves.

[Migration
waves](https://docs.aws.amazon.com/prescriptive-guidance/latest/application-portfolio-assessment-guide/wave-planning.html) typically span four to eight weeks, and they can
contain one or more migration events. Applications and their
dependencies are combined into waves so customers can meet the
challenges of dependency mapping. But how do you ensure good and
consistent performance during this whole process?

## MIG-PERF-BP-8.1: Perform stress and user acceptance tests on migrated workloads before the actual cutover.

This BP applies to the following best practice areas: Process
and culture

### Implementation guidance

**Suggestion 8.1.1:** Perform stress and user acceptance tests for quality check before the actual cutover.

Migration tools such as [AWS Application Migration Service (AWS MGN)](https://aws.amazon.com/application-migration-service/) provide features to [test and cutover](https://docs.aws.amazon.com/mgn/latest/ug/server-test-cutover-main.html) workloads. It is highly recommended to run tests in your test or staging environments so that performance is maintained after cutover. The test could be a stress test to test the systems with three to four times the load in production environments, or a user acceptance test to ensure the application can function properly in the organization. It is also recommended to perform tests at least two weeks prior to the cutover, so there is sufficient time to fix any issues before the cutover.

For more detail, see the following:

- [Testing
and cutover](https://docs.aws.amazon.com/whitepapers/latest/amazon-aurora-mysql-migration-handbook/testing-and-cutover.html)
- [Application
migration process](https://docs.aws.amazon.com/prescriptive-guidance/latest/cutover-runbook/app-migration.html)
- [Testing
Phase](https://docs.aws.amazon.com/whitepapers/latest/best-practices-for-migrating-from-rdbms-to-dynamodb/testing-phase.html)

## MIG-PERF-BP-8.2: Review and implement the lessons learned from previous migration waves

This BP applies to the following best practice areas: Process
and culture

### Implementation guidance

**Suggestion 8.2.1:** Take note of lessons learned from previous migration waves.

As the migration program moves forward and more waves are migrated, it is key to evolve the migration wave plan based on lessons learned and changing business priorities. In particular, for long-running migration programs, it is important to reassess business drivers and organizational change, and to verify that the migration [wave plan](https://docs.aws.amazon.com/prescriptive-guidance/latest/application-portfolio-assessment-guide/wave-planning.html) is still valid. Similarly, lessons learned from the migration influence the wave plan composition and the scope of each wave. To avoid losing visibility into what is happening, keep the [wave plan](https://docs.aws.amazon.com/prescriptive-guidance/latest/application-portfolio-assessment-guide/wave-planning.html) up to date. The plan should reflect and track what is being delivered, and it should manage and assess change to the migration scope.

## MIG-PERF-BP-8.3: Perform a Well-Architected Framework Review on each iteration of the migrated workload.

This BP applies to the following best practice areas: Process
and culture

### Implementation guidance

**Suggestion 8.3.1:** Review Well-Architected best practices after each iteration of your migration.

The review of architecture needs to be done in an iterative manner after each migration wave. This involves reviewing the current and target state architectures for future waves to see what can be improved performance wise. Each team member should take responsibility for the quality of their architecture. We recommend that the team members who build an architecture use the Well-Architected Framework to continually review their architecture after each migration wave, rather than conducting a formal performance review meeting.

For more detail, see the following:

- [How to perform a Well-Architected Framework Review- Part 1](https://aws.amazon.com/blogs/mt/how-to-perform-a-well-architected-framework-review-part1/)
- [How to perform a Well-Architected Framework Review- Part 2](https://aws.amazon.com/blogs/mt/how-to-perform-a-well-architected-framework-review-part2/)
- [How to perform a Well-Architected Framework Review- Part 3](https://aws.amazon.com/blogs/mt/how-to-perform-a-well-architected-framework-review-part3/)

**Suggestion 8.4.1:** Review the [7 Rs migration strategy](https://docs.aws.amazon.com/prescriptive-guidance/latest/application-portfolio-assessment-guide/iterating-7-rs-migration-strategy-selection.html).

After each migration wave, we recommend to review 7 R decision tree for your applications, considering the learnings throughout migration of the initial pilot applications or subsequent migration waves that had been completed. You need to ensure that the migration strategy continues to provide the best performance for the workload, and verify that it aligns with your initial assessment. The migration strategy is not only derived for the application component but also for the associated infrastructure. The final migration strategy should always provide and optimize the performance for the application and infrastructure. [AWS Migration Hub strategy recommendations](https://aws.amazon.com/migration-hub/features/) help automate the analysis of your application portfolios and review of the 7 R strategy. [Strategy recommendations](https://aws.amazon.com/blogs/aws/new-strategy-recommendations-service-helps-streamline-aws-cloud-migration-and-modernization/) analyzes your running applications to determine runtime environments and process dependencies, optionally analyzes source code and databases, and more.

For more detail, refer to the following:

- [Iterating the 7 Rs migration strategy selection](https://docs.aws.amazon.com/prescriptive-guidance/latest/application-portfolio-assessment-guide/iterating-7-rs-migration-strategy-selection.html)
- [AWS Migration Hub Strategy Recommendations](https://aws.amazon.com/blogs/aws/new-strategy-recommendations-service-helps-streamline-aws-cloud-migration-and-modernization/)

MIG-PERF-09: How do you monitor the performance through all the phases of your migration journey?

Monitoring performance during the mobilize and migrate phase is
essential for a successful migration. Monitoring can help
remediate issues before they impact your customers. Monitoring
metrics should be used to raise alarms when thresholds are
breached. During the mobilize and migrate phases, look at the
following best practices for setting up monitoring.

## MIG-PERF-BP-9.1: Generate alarm-based notifications for metric's threshold breach

This BP applies to the following best practice areas: Process
and culture

### Implementation guidance

**Suggestion 9.1.1:** Generate alarm-based notifications using [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html) and [Amazon SNS](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/US_SetupSNS.html).

As you are migrating workloads, system performance can degrade over time. It is recommended to monitor the workload's performance to identify degradations and bottlenecks, and remediate them automatically. Amazon CloudWatch generates system-defined metrics, and customers can also create [custom user-defined metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html). You can use these metrics to generate CloudWatch alarms and add an [Amazon SNS](https://aws.amazon.com/sns/) topic to send an email notification when the alarm changes state. These SNS notifications can also be integrated with [AWS Lambda](https://aws.amazon.com/lambda/) to take actions for remediating the issue.

[AWS X-Ray](https://aws.amazon.com/xray/) helps developers analyze and debug production in distributed applications. With AWS X-Ray, you can glean insights into how your application is performing, discover root causes, and identify performance bottlenecks. You can use these insights to react quickly and keep your workload running smoothly.

## MIG-PERF-BP-9.2: Determine the need for a real-time or a near real-time monitoring solution

This BP applies to the following best practice areas: Process
and culture

### Implementation guidance

**Suggestion 9.2.1:** Use a real-time or a near-real-time monitoring solution.

Most applications can tolerate some performance degradation and can be monitored in near-real-time. But some applications process data instantly, and therefore need to be monitored in real-time. It is essential to identify the performance needs for your migrated applications and implement a monitoring solution accordingly. Amazon CloudWatch delivers metrics and logs in near-real-time. [Metric streams](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Metric-Streams.html) send CloudWatch metrics to destinations like Amazon S3, with near-real-time delivery and low latency. You could also monitor microservices and cloud-native applications in real-time with [IBM Instana SaaS on AWS](https://aws.amazon.com/blogs/architecture/realtime-monitoring-of-microservices-and-cloud-native-applications-with-ibm-instana-saas-on-aws/).

## MIG-PERF-BP-9.3: Implement CloudWatch or a Quicksight dashboard as a single pane view for visualizing all metrics

This BP applies to the following best practice areas: Process and culture

### Implementation guidance

**Suggestion 9.3.1:** Implement CloudWatch or a Quicksight dashboard for monitoring metrics.

[CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html) or a [Quicksight dashboard](https://docs.aws.amazon.com/quicksight/latest/user/example-create-a-dashboard.html) can provide a single pane view of all the monitoring metrics. A single view for selected metrics and alarms help you assess the health of your resources and applications across regions. You can create [CloudWatch cross-account observability dashboard](https://aws.amazon.com/blogs/mt/creating-a-near-realtime-dashboard-on-amazon-cloudwatch-for-a-migration-usecase/) or [cross-account, cross-Region dashboards](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_xaxr_dashboard.html) to summarize your CloudWatch data from multiple AWS accounts and multiple Regions into one dashboard.

## MIG-PERF-BP-9.4: Set up automated testing for your application metrics

This BP applies to the following best practice areas: Process
and culture

### Implementation guidance

**Suggestion 9.4.1:** Use CloudWatch synthetic monitoring for setting up automated testing for your applications.

Using [CloudWatch synthetic monitoring](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.html), you can [create canaries](https://www.youtube.com/watch?v=DSx65wW7lr0) to [monitor your endpoints and APIs](https://www.youtube.com/watch?v=_PCs-ucZz7E). Canaries perform automated testing (perform same actions as a customer) to continually verify your customer experience, even when there is no load. This helps discover issues even before your customer do.

## MIG-PERF-BP-9.5: Re-evaluate your compute usage with AWS Trusted Advisor, AWS Compute Optimizer, or partner tools

This BP applies to the following best practice areas: Process
and culture

### Implementation guidance

**Suggestion 9.5.1:** Use Compute Optimizer for reviewing your performance metrics.

AWS Compute Optimizer collects resource utilization data and helps avoid over-provisioning and under-provisioning resources such as [Amazon Elastic Compute Cloud](https://aws.amazon.com/ec2/) (EC2), [Amazon Elastic Block Store](https://aws.amazon.com/ebs/) (EBS) volumes, [Amazon Elastic Container Service](https://aws.amazon.com/ecs/) (ECS) services on [AWS Fargate](https://aws.amazon.com/fargate/), and [AWS Lambda functions](https://aws.amazon.com/lambda/).

*Source: https://docs.aws.amazon.com/wellarchitected/latest/migration-lens/migrate-perf.html*

---

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
