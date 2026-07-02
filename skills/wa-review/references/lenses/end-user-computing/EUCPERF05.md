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
