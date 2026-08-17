# Performance Efficiency

**Pillar**: Performance Efficiency  
**Questions**: 10

---

# EUCPERF01 — Architecture selection

**Pillar**: Performance Efficiency  
**Best Practices**: 3

---

# EUCPERF01-BP01 Check Regional support for the required EUC services

Not all AWS regions support EUC services such as WorkSpaces Applications, WorkSpaces and WorkSpaces
Secure Browser.

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

Check to see if the relevant AWS EUC service is available in your most proximal
Region. If the required service is not available in this Region, check to be sure that you
can deliver the required performance from the Region closest to you or with lowest
latency. For information on EUC Regional support, see:

- [WorkSpaces Regional Support](https://docs.aws.amazon.com/workspaces/latest/adminguide/azs-workspaces.html)
- [WorkSpaces Applications Regional
Support](https://www.aws-services.info/appstream.html)
- [WorkSpaces Secure Browser
Regional Support](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/availability-zones.html)

The [WorkSpaces Connection
Health Checker](https://clients.amazonworkspaces.com/Health.html) details the latency between a specific endpoint device and the
WorkSpaces service running in each available Region. This data is also a good indicator of
latency for WorkSpaces Secure Browser and WorkSpaces Applications if they are running in the same Region.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucperf01-bp01.html*

---

# EUCPERF01-BP02 Consider the requirements of your Availability Zones when architecting your AWS EUC services

Within each Region, only select Availability Zones support each AWS EUC service. This
is important if you are architecting solutions with extreme performance or security
requirements that demand that applications and desktops reside on the same subnet as the
user data they need to access.

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

For the WorkSpaces service line, explore the Availability Zone information.

- [Amazon WorkSpaces Availability Zone Support](https://docs.aws.amazon.com/workspaces/latest/adminguide/azs-workspaces.html)
- [Amazon WorkSpaces Secure Browser](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/availability-zones.html)

For WorkSpaces Applications, selecting a subnet when creating a new fleet automatically checks
if the associated Availability Zone can support the requested requirements, which are
based on several criteria such as instance type and availability.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucperf01-bp02.html*

---

# EUCPERF01-BP03 Consider disaster recovery (DR) requirements when architecting your AWS EUC solution

Will a secondary Region support the latency that is acceptable to support the selected
AWS EUC service in a DR scenario, or can you accept degraded performance and relaxed
service level agreements to continue to do business?

**Level of risk exposed if this best practice is not
established:** Low

## Implementation guidance

For WorkSpaces, the use of cross-Region redirection or Multi-Region Resilience allows the
manual or partially automated process of using alternate regions to support your WorkSpaces
users in the event of a serious outage.

For WorkSpaces Applications, the master images created in one Region can be copied to a
secondary Region to enable the configuration of identical regional deployment for DR
purposes.

Review each of these DR features to be sure that they offer adequate performance and
capabilities depending on the Region that is selected for the purpose.

You should also replicate user data and other critical backend services in each
Region to provide localized access if similar levels of performance are expected in a DR
scenario.

For more detail on Cross-Region redirection and Multi-Region Resilience, see [Business continuity for WorkSpaces Personal](https://docs.aws.amazon.com/workspaces/latest/adminguide/business-continuity.html).

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucperf01-bp03.html*

---

# EUCPERF02 — Architecture selection

**Pillar**: Performance Efficiency  
**Best Practices**: 3

---

# EUCPERF02-BP01 Identify geographic distribution of end users and design to minimize latency

When migrating to or implementing AWS EUC services, consider the location of each
group of users with respect to the service endpoints for AWS WorkSpaces, WorkSpaces Applications, or
WorkSpaces Secure Browser. You should deliver services from the Region with the lowest latency to
most users.

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

Capture the location of each user group, and calculate the average latency between
each group and their most proximal AWS Region that supports the required AWS EUC
service. Due to Regional network routing and capabilities, it is possible the most
proximal AWS Region does not necessarily offer the lowest latency.

If you must deploy AWS EUC services in a non-optimal Region (which is sometimes
necessary to access other AWS services which have already been deployed), then be sure
that you test your application to verify that they offer acceptable performance at the
latency levels being experienced.

For an example of how latency might affect the user experience, see [EUC latency
trade-offs](https://guide.aws.dev/en/articles/ARiy3h1QGUSWePxGqdV_SYLA).

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucperf02-bp01.html*

---

# EUCPERF02-BP02 Scale your EUC environment to accommodate the required number of end users

The number of users accessing the selected AWS EUC service should not affect the
performance of the service itself, as AWS provides both scale and resilience for the
components that affect authentication and streaming of user sessions. Many supporting
components, however, need to be scaled to support the user numbers you intend to deploy.

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

Understand the backend requirements for your deployment and scale them accordingly.
For example, a WorkSpaces compute instance with 2 vCPU and 4Gb of RAM may offer acceptable
performance to run a targeted application set, but if access to user data or an
application database backend is compromised by server performance or network constraints,
then the user may complain that WorkSpaces is performing badly. Ideally, perform end to end
testing for each application set using scalability testing tools to be sure that they will
deliver acceptable performance in production as the services scale.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucperf02-bp02.html*

---

# EUCPERF02-BP03 Evaluate external data sources that your environment integrates with, and assess its impact on performance

The location of user data and the services used to deliver access to this data are key
to providing the best performance for consumers of an AWS EUC deployment. Latency incurred
while accessing data sources may incur additional delays and contribute to end user
frustration and lack of engagement, as well as increased support calls.

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

Define a data architecture that describes how data is managed, from collection
through transformation, distribution, and consumption. This informs the EUC architects
where to place key application and desktop delivery services and where optimization may be
required to avoid performance degradation.

If migrating from an existing on-premises EUC architecture, you may need to deploy
[AWS Direct Connect](https://aws.amazon.com/directconnect/) or [AWS Site-to-Site VPN](https://aws.amazon.com/vpn/site-to-site-vpn/) connections to provide
access between AWS and your on-premises infrastructure. For best practices related to
networking for Amazon WorkSpaces and descriptions for how and when to use Direct Connect and VPN
connections, see [Best Practices for VPCs and Networking in Amazon WorkSpaces Deployments](https://d1.awsstatic.com/whitepapers/best-practices-vpcs-networking-amazon-workspaces-deployments.pdf).

Be sure to architect network solutions with low enough latency and sufficient
bandwidth to support appropriate data access between desktops, applications, and any
on-premises data sources.

If your AWS EUC solution integrates with services offered by other cloud providers,
such as email, collaboration tools, or SaaS applications, be sure to size internet
connections or private networks accordingly to avoid high latency and bandwidth
constraints.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucperf02-bp03.html*

---

# EUCPERF03 — Architecture selection

**Pillar**: Performance Efficiency  
**Best Practices**: 1

---

# EUCPERF03-BP01 Consider modernization of backend services to use managed services from AWS for best performance

By using AWS EUC services, you are already taking advantage of the reduced
infrastructure and management overheads of maintaining your own environment. Taking the same
approach to other backend services which support the EUC deployment can further increase
operational efficiency.

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

Review the backend services required for your AWS EUC deployment, and determine if
transitioning to managed service equivalents from AWS might improve performance,
simplify cost modelling, and reduce the administrative and support overheads of delivering
these in-house. Examples include:

- **Amazon FSx for Windows File Server**: Resilient, high performance file
shares, user data storage and profile management.
- **Amazon RDS**: A range of high-performance managed SQL
services.
- **Amazon CloudWatch**: Insight into operational metrics and
alerting to maintain performance and efficiency.
- **AWS CloudTrail**: Records logs that provide insight into
activities undertaken within an AWS account.

Reduce the overhead of managing your own infrastructure, and invest the time saved to
perform continual service improvement, increasing the performance efficiency of your EUC
deployment.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucperf03-bp01.html*

---

# EUCPERF04 — Compute and hardware

**Pillar**: Performance Efficiency  
**Best Practices**: 3

---

# EUCPERF04-BP01 Evaluate available instance types (AppStream) and hardware bundles (WorkSpaces)

WorkSpaces Applications groups instances into families, such as General Purpose (stream.standard).
Within each family, there are different instance sizes, such as stream.standard.medium and
stream.standard.large. Each size has a different number of vCPUs and memory. Graphics
optimized families include instances with one or more GPUs. For more information on the
Graphics G4 (stream.graphics.g4dn), Graphics G5 (stream.graphics.g5), and Memory Optimized
(stream.memory.z1d) families, see [Amazon EC2
Instance Types](https://aws.amazon.com/ec2/instance-types/).

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

WorkSpaces bundle selection begins with determining if your workload requires a GPU. If it
does, evaluate the Graphics G4 and Graphics G5 families. If it does not require a GPU,
evaluate the General Purpose, Compute Optimized, and Memory Optimized families. In
addition to large amounts of memory, stream.memory.z1d instances offer the highest CPU
clock rates of the WorkSpaces Applications instance family.

WorkSpaces provides hardware bundles with different amounts of vCPUs and memory.
Graphics.G4dn and GraphicsPro.G4dn bundles include GPUs.

For specifications and recommended uses cases, see [Amazon WorkSpaces](https://aws.amazon.com/workspaces-family/workspaces/pricing/).

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucperf04-bp01.html*

---

# EUCPERF04-BP02 Identify all user types, and deploy required fleet types and instance types as needed

Not all end users necessarily require the same level of performance. Users who perform
routine tasks such as data entry, document review, or customer service may need a low level
of performance, while content or video editors, investment and securities traders, or
graphics users may require performant desktops. Other users may require moderate levels of
performance as their workloads may be unpredictable.

It's important to have a high degree of familiarity with the applications that need to
be delivered using Amazon WorkSpaces Applications in terms of their compute resource requirements. By
understanding core compute requirements such as the amount of memory, CPU, network
bandwidth, latency, and disk space that applications require, you can determine the optimum
fleet type and instance sizes required for the workload.

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

Determine the compute requirements for your applications.

- Assess your users' applications and tasks, and deploy a sufficient level of fleet
types and instance types as are needed.
- Monitor the resulting user feedback to verify that performance meets their needs
without overprovisioning their instance types.
- If performance or productivity suffers for various users, increase the
performance of their instances. This can be achieved by using larger instances with
more CPU or in the case of WorkSpaces Applications using a different instance family that
provides higher clock speed for CPU cores.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucperf04-bp02.html*

---

# EUCPERF04-BP03 Determine the running mode and size of hardware bundles needed to support each user type's applications

It's important to have a high degree of familiarity with the applications that need to
be delivered using Amazon WorkSpaces Personal in terms of their compute resource requirements and
their usage pattern. By understanding core compute requirements such as the amount of
memory, CPU, network bandwidth, latency, and disk space that applications require, you can
more effectively determine the optimum WorkSpaces Personal bundle type. The optimal running mode
required to support the workload is determined by understanding the pattern of usage of the
application.

## Implementation guidance

Determine the compute requirements for your applications.

- Assess your users' applications and tasks and deploy a sufficient level of
performance as is needed.
- Monitor the resulting user feedback to verify that performance meets their needs
without overprovisioning their hardware types.
- If performance or productivity suffers for various users, increase the size of
their instances.
- For Personal WorkSpaces, establish the current or required pattern of usage of the
applications or desktops being delivered. Select an Always-On running mode for user
environments that are broadly used throughout each month (> 80 hours), select the
Auto-Stop running mode where usage will be

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucperf04-bp03.html*

---

# EUCPERF05 — Data management

**Pillar**: Performance Efficiency  
**Best Practices**: 5

---

# EUCPERF05-BP01 Understand your existing storage requirements, policies, and solutions

If your EUC workload already uses storage volumes, operations policies, and vendor
solutions, make sure that you not only understand what products and services they are based
on, but also identify the features, advantages, and benefits associated with each in your
existing workload. Decide whether these are best suited to your applications and technical
goals. Otherwise, develop a set of new functional requirements and solutions that will
better address your requirements.

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

Begin by understanding the storage requirements for each use case. Relevant
requirements include the following:

- Individual file size
- Total data size
- Average and peak IOPS
- Whether storage is per-user or shared
- File and folder permissions

Also, consider organizational policies and existing solutions (for example, if policy
dictates that users store all files in a central repository).

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucperf05-bp01.html*

---

# EUCPERF05-BP02 Understand integrated storage capabilities (AppStream)

For persistent, per-user storage, WorkSpaces Applications offers built-in connectors to Amazon S3 home
folders, Google Drive for Google Workspace, and OneDrive for Business. For more information
on these connectors, see [Enable and Administer
Persistent Storage for Your WorkSpaces Applications Users](https://docs.aws.amazon.com/appstream2/latest/developerguide/persistent-storage.html).

**Level of risk exposed if this best practice is not
established:** Low

## Implementation guidance

Use Amazon S3 home folders when you need a simple, fully-managed solution for persisting
user files between sessions and users don't need to access their files from outside their
WorkSpaces Applications sessions. Use Google Drive for Google Workspaces or OneDrive for Business
when you use Windows fleets and your users have a license for one of the services.

If the integrated storage features of Amazon WorkSpaces Applications do not offer the
capabilities you require, consider Amazon FSx for Windows File Server, Amazon FSx for NetApp ONTAP, or Amazon EC2 hosted file
sharing. You can use these fully or partly-managed solutions to store user data or user
profiles, such as FSLogix, close to your AWS EUC control plane.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucperf05-bp02.html*

---

# EUCPERF05-BP03 Understand integrated storage capabilities (WorkSpaces)

Most existing workloads, either physical or virtual, will make use of integrated
storage that provides the system drive and data drives. For virtualized desktops and
servers, this will be virtual drives created from hyperconverged storage. Some workloads, if
not already virtualized, may also have fast boot and data drives (like SSD or NVMe) or
additional integrated storage in the form of internal hard drives or externally-connected
hard drives that deliver large or faster storage for specific applications.

**Level of risk exposed if this best practice is not
established:** Low

## Implementation guidance

If any of the workloads you are migrating to AWS EUC services have been configured
with and require high performance or additional high-density storage, carefully review the
AWS instance types that provide higher performance storage. The Graphics G4 instance
types offer a local NVMe instance store which may meet your requirements.

This may also be an opportunity to review alternate networked AWS Storage solutions
as they might provide the speed and density you require.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucperf05-bp03.html*

---

# EUCPERF05-BP04 Use instance storage when available and appropriate

An instance store provides temporary block-level storage for your instance. This
storage is located on disks that are physically attached to the host computer. Instance
store is ideal for temporary storage of information that changes frequently, such as
buffers, caches, scratch data, and other temporary content.

For WorkSpaces Applications, the Graphics G4, Graphics G5, and Memory Optimized
(stream.memory.z1d) instance families include NVMe instance storage volumes. For further
information related to the instance storage volumes and initializing, see [Instance store
temporary block storage for EC2 instances](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/InstanceStorage.html).

For WorkSpaces, the graphics.g4dn and GraphicsPro.G4dn bundles provide NVMe instance storage
volumes.

**Level of risk exposed if this best practice is not
established:** Low

## Implementation guidance

Use the local instance store on instances that support it to optimize the performance
of end user applications. When doing so, consider that the instance store is not backed up
and should only be used to satisfy temporary storage requirements. See [Local Instance Store for GPU-enabled Bundles](https://aws.amazon.com/workspaces/features/#Local_Instance_Store_for_GPU-enabled_Bundles) for more information.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucperf05-bp04.html*

---

# EUCPERF05-BP05 Consider the benefits of additional AWS storage services

As an alternative to internal storage, some workloads benefit from shared storage for
collaboration or to enable persisting data in centralized locations. Using non-internal
storage services delivers storage with customizable performance, which gives administrators
more control for common storage attributes like IOPS, throughput, and volume size that
directly impact performance and user experience.

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

Review additional storage services if any of the workloads you are migrating to AWS
EUC services require tunable performance, larger volume sizes exceeding those provided by
the EUC services, or granular control over throughput and IOPs, including
Amazon FSx for Windows File Server, Amazon FSx for NetApp ONTAP , and Amazon EFS.

For more information, see [Persistent storage for Amazon WorkSpaces Applications Linux Fleets on Amazon Elastic File System](https://aws.amazon.com/blogs/desktop-and-application-streaming/persistent-storage-for-amazon-appstream-2-0-linux-fleets-on-amazon-elastic-file-system/) and
[Connect Amazon FSx for NetApp ONTAP to Amazon WorkSpaces Applications Linux instances](https://aws.amazon.com/blogs/desktop-and-application-streaming/connect-amazon-fsx-for-netapp-ontap-to-amazon-appstream-2-0-linux-instances/).

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucperf05-bp05.html*

---

# EUCPERF06 — Networking and content delivery

**Pillar**: Performance Efficiency  
**Best Practices**: 3

---

# EUCPERF06-BP01 Minimize latency between end users and EUC services

Like many other vendors, AWS EUC solutions deliver their services using a remote
display protocol to stream the pixel information to the endpoint device, which is highly
efficient and capable of tolerating a variety of network conditions. Low latency, low packet
loss, and jitter are key to delivering the best service for end users.

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

Minimize latency between end user devices (like desktops, laptops, and thin clients)
and the AWS EUC service endpoints by avoiding proxies, inspection appliances, and VPNs.

Determine whether there are any conditions which might introduce latency between your
end users and the AWS EUC service endpoints. Test connectivity under various conditions
to identify the maximum latency that can be tolerated by the application set being
deployed, and verify that your network can scale to reliably deliver the number of users
being deployed.

If end users will be working from home, try to establish a minimum level of network
connectivity that should provide a good user experience. Most home broadband connections
are more than capable of delivering low latency for home working, but problems with home
networks can be difficult to diagnose.

Verify that endpoint devices can run the local client application (WorkSpaces or AppStream
Client) that processes and displays the encrypted pixel stream which flows between the end
user and the AWS EUC service connection points (streaming gateways). If the workload
delivers collaboration tools such as Microsoft TEAMs, Zoom, or Webex, optimization
capabilities will try to offload processing to the local endpoint device, which must be
capable of handling this additional load.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucperf06-bp01.html*

---

# EUCPERF06-BP02 Minimize latency between EUC instances and dependent services

In most cases, EUC users require connections to resources outside their EUC instances.
Common dependencies include web or application servers, database servers, and storage
services.

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

When possible, deploy these dependencies in the same AWS Region and ideally the same
Availability Zone. If the system of record must reside elsewhere, consider deploying
caches or replicas. For example, if your Active Directory domain controllers are on your
on-premises network, deploy replicas on Amazon EC2.

When connecting to Amazon S3, use gateway VPC endpoints. For more information on
configuring gateway endpoints, see [Gateway endpoints for
Amazon S3](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-s3.html).

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucperf06-bp02.html*

---

# EUCPERF06-BP03 Make sure that EUC network configurations don't interfere with service management connections

WorkSpaces Applications instances use a dedicated management network interface (eth0) for
streaming and service management connections.

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

Do not configure applications or the operating system to interfere with the
connections listed in [Amazon WorkSpaces Applications Connections to Your VPC](https://docs.aws.amazon.com/appstream2/latest/developerguide/appstream2-port-requirements-appstream2.html#management_ports). If private network connectivity
from WorkSpaces Applications instances to resources outside your VPC is required, use a VPC-level
solution such as AWS Site-to-Site VPN or AWS Transit Gateway. Do not use a client VPN on the WorkSpaces Applications
instance, as this is complex and error-prone to configure properly.

WorkSpaces instances use a dedicated management network interface (eth0) for streaming and
service management connections.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucperf06-bp03.html*

---

# EUCPERF07 — Process and culture

**Pillar**: Performance Efficiency  
**Best Practices**: 1

---

# EUCPERF07-BP01 Conduct realistic end-to-end testing aligned with organizational objectives

When planning to conduct testing, consider how your users interact with the EUC service
and on an everyday basis. Create tests that align with the primary use of the service
initially and expand to edge cases over time or in response to incidents to verify that they
do not arise in future iterations of the service.

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

Conduct tests that align with the expected use of the service. Work backwards from
organizational objectives to conduct realistic tests. For example, consider any use case
where remote users process invoices in an accounting application. Key metrics may include
the number of invoices that each user processes per hour and their accuracy. A realistic
test would include experienced application users processing actual invoices, using
representative client devices under typical network conditions.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucperf07-bp01.html*

---

# EUCPERF08 — Process and culture

**Pillar**: Performance Efficiency  
**Best Practices**: 4

---

# EUCPERF08-BP01 Establish and monitor service metrics and KPIs

When using an AWS EUC service to deliver a service to your users, it's important to
consider the service metrics that are key to the delivery of the service for your
organization to verify that the service is operating at the required service levels.

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

Determine service metrics and KPIs for your service. Some examples of key measures to
consider are:

- Service availability
- Mean time to repair (MTTR)
- First call resolution (FCR)
- SLA breach rate
- User and customer satisfaction (CSAT)
- Cost per contact
- Net promoter score
- Incident volume
- Problem resolution time

Consider how metrics available within the AWS EUC services outlined in the
following sections can be used to support or determine your service metrics.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucperf08-bp01.html*

---

# EUCPERF08-BP02 Monitor Amazon WorkSpaces Applications CloudWatch metrics

Use Amazon CloudWatch to establish and monitor your WorkSpaces Applications workload's performance against
the KPIs established for your service. [Use the Automatic
dashboard](https://docs.aws.amazon.com/workspaces/latest/adminguide/cloudwatch-dashboard.html) in Amazon CloudWatch to monitor your fleet capacity over time or consider
creating a custom dashboard tailored to your environment.

**Level of risk exposed if this best practice is not
established:** Low

## Implementation guidance

Measure your workload's performance across [Amazon AppStream
2.0 fleets and fleet instances](https://docs.aws.amazon.com/appstream2/latest/developerguide/monitoring-with-cloudwatch.html).

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucperf08-bp02.html*

---

# EUCPERF08-BP03 Monitor Amazon WorkSpaces Personal CloudWatch metrics

Use CloudWatch to establish and monitor your Amazon WorkSpaces workload's performance against these
KPIs and requirements.

**Level of risk exposed if this best practice is not
established:** Low

## Implementation guidance

Monitor the Amazon WorkSpaces service and instances using Amazon CloudWatch. Use the guidance provided
in the following articles to measure your workload's performance.

- [Monitor your WorkSpaces using CloudWatch metrics](https://docs.aws.amazon.com/workspaces/latest/adminguide/cloudwatch-metrics.html)
- [Creating custom Amazon CloudWatch dashboards and widgets for Amazon WorkSpaces](https://aws.amazon.com/blogs/desktop-and-application-streaming/creating-custom-amazon-cloudwatch-dashboards-and-widgets-for-amazon-workspaces/)
- [Monitor your WorkSpaces health using the CloudWatch automatic dashboard](https://docs.aws.amazon.com/workspaces/latest/adminguide/cloudwatch-dashboard.html)
- [Utilizing CloudWatch Internet Monitor with Amazon WorkSpaces](https://aws.amazon.com/blogs/desktop-and-application-streaming/utilizing-cloudwatch-internet-monitor-with-amazon-workspaces-personal/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucperf08-bp03.html*

---

# EUCPERF08-BP04 Monitor operating system metrics

Operating systems can add significant variations in performance to your Workload
depending on the compute, storage, and memory resources required. Test with all operating
systems that are intended to be supported by your deployment.

**Level of risk exposed if this best practice is not
established:** Low

## Implementation guidance

Monitor the performance of instances delivering end user services.

- Use operating system metrics such as Windows Performance Counters for detailed
insight into instance performance.
- [Use
the EUC Toolkit to manage Amazon WorkSpaces Applications and Amazon WorkSpaces](https://aws.amazon.com/blogs/desktop-and-application-streaming/euc-toolkit/).
- For ongoing monitoring and analysis, consider using the [Amazon Kinesis Agent for Windows](https://docs.aws.amazon.com/kinesis-agent-windows/latest/userguide/what-is-kinesis-agent-windows.html) to monitor Windows Performance Counters for
performance trend analysis of key system metrics.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucperf08-bp04.html*

---

# EUCPERF09 — Process and culture

**Pillar**: Performance Efficiency  
**Best Practices**: 1

---

# EUCPERF09-BP01 Follow AWS EUC news sources

Many customers can benefit from keeping up with news from software publishers and
partners in the end user computing domain. Stay updated on developments by following news
feeds and social media.

**Level of risk exposed if this best practice is not
established:** Low

## Implementation guidance

Subscribe to AWS feeds and blogs to keep up to date. Follow the [Desktop and Application
Streaming blog](https://aws.amazon.com/blogs/desktop-and-application-streaming/) and [End User Computing What's New Feed](https://aws.amazon.com/new/?whats-new-content-all.sort-by=item.additionalFields.postDateTime&whats-new-content-all.sort-order=desc&awsf.whats-new-categories=marketing-marchitecture%23desktop-and-app-streaming).

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucperf09-bp01.html*

---

# EUCPERF10 — Process and culture

**Pillar**: Performance Efficiency  
**Best Practices**: 5

---

# EUCPERF10-BP01 Align the instance type and instance size of a fleet with the workload

As needed, user environments can be updated on a pre-determined schedule or in response
to periodic changes in performance to satisfy a change in the anticipated demand for
resources.

**Level of risk exposed if this best practice is not
established:** Low

## Implementation guidance

Determine the optimal instance family and size for your applications.

- The non-graphics instance families can utilize the same image across them. This
provides image portability across these instance families and the instance sizes
associated with them and allows varying requirements for compute resources to be
catered for.
- Images created for a graphics instance family (for example, stream.graphics.g5)
can only be associated with that family due to the specific GPU drivers for the
associated GPU. Consequently, choose a graphics instance family carefully from the
outset to avoid the need to create a new image for a different GPU family.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucperf10-bp01.html*

---

# EUCPERF10-BP02 Enable self-service WorkSpaces Personal management capabilities, and allow users to request changes by an administrator

The WorkSpaces Personal self-service options allow users to ramp up or down instance
performance over time.

**Level of risk exposed if this best practice is not
established:** Low

## Implementation guidance

Enable user self-service where possible to optimize processes.

- Identify the most flexible compute types for users to anticipate required changes
in performance. Consider the following:

You can change the compute type from Graphics.g4dn to GraphicsPro.g4dn, or
from GraphicsPro.g4dn to Graphics.g4dn.
- However, you cannot change the compute type of Graphics.g4dn and
GraphicsPro.g4dn to other types.
- You cannot change the compute type of Graphics and GraphicsPro to another
type.

- Consider these capabilities and limitations when initially configuring your
users' environments.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucperf10-bp02.html*

---

# EUCPERF10-BP03 Install only the application features required by end users

Some applications provide the ability to tailor an installation to remove features that
are not required by users.

**Level of risk exposed if this best practice is not
established:** Low

## Implementation guidance

Do not install application features not required by users. Install the minimal set of
features in applications that are required by users to perform their roles. This helps to
reduce compute requirements and also helps to remove potential security risks that may
arise that are associated with those features.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucperf10-bp03.html*

---

# EUCPERF10-BP04 Remove caches, temporary data, log files, and unneeded files such as tutorials and sample data before creating an image

Remove non-required files that are installed, downloaded, or created by applications to
optimize storage consumption.

**Level of risk exposed if this best practice is not
established:** Low

## Implementation guidance

Remove unneeded files from images to optimize storage consumption.

Unnecessary files included in an Amazon WorkSpaces golden image use space for each WorkSpace
provisioned using that image. Similarly, for Amazon WorkSpaces Applications where the image builder
volume size is limited, removing unneeded files can provide additional storage space for
other applications.

Consider data access patterns and whether data not included in an image can be
downloaded when needed. For example, if 10% of users access an application library that
can be downloaded when needed, omit the library from images.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucperf10-bp04.html*

---

# EUCPERF10-BP05 Tune application performance where possible to optimize compute resource usage

To provide the optimal access to compute resource for your applications, consider
tuning the performance of applications or software where possible to reduce their compute
resource utilization.

**Level of risk exposed if this best practice is not
established:** Low

## Implementation guidance

By reducing the compute resource utilization for software used to provide non-end
user facing functionality, such as security agents, additional resources are made
available to benefit the applications users interact with. The disabling of non-essential
functionality within software can yield a performance benefit for end user software.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucperf10-bp05.html*

---

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
