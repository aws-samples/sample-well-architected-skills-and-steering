# HPCPERF04 — Performance efficiency

**Pillar**: Performance Efficiency  
**Best Practices**: 1

---

## HPCPERF04-BP01 Select the optimal HPC storage solution based on your targeted individual application

The optimal storage solution for a particular HPC architecture
depends largely on the individual applications targeted for that
architecture. Workload deployment method, degree of automation,
and desired data lifecycle patterns are also factors. AWS offers
a wide range of storage options.

As with compute, the best performance is obtained when targeting
the specific storage needs of an application. AWS does not
require you to over-provision your storage for a
one-size-fits-all approach, and large, high-speed, shared file
systems are not always required. Optimizing the compute choice
is important for optimizing HPC performance and many HPC
applications will not benefit from the fastest storage solution
possible.

HPC deployments often require a shared or high-performance file
system that is accessed by the cluster compute nodes. There are
several architecture patterns you can use to implement these
storage solutions from AWS Managed Services, AWS Marketplace
offerings, APN Partner solutions, and open-source configurations
deployed on EC2 instances.

### Implementation guidance

- Amazon FSx is a suite of AWS managed services designed to
help customers to deploy and manage file systems in the
cloud. It supports a wide range of workloads with its
reliability, security, scalability, and broad set of
capabilities. In particular, Amazon FSx for Lustre is a
managed service that provides a cost effective and
performant solution for HPC architectures requiring a
high-performance parallel file system. Similarly, Amazon FSx for OpenZFS is a fully managed file storage service
that provides a ZFS file system. Based on your application
needs, you can explore additional file systems managed by
Amazon FSx such as NetApp ONTAP and Windows File Server
(SMB).
- Shared file systems can also be created from Amazon Elastic File System (EFS) or EC2 instances with Amazon Elastic Block Store (EBS) volumes or instance store
volumes. Frequently, a simple NFS mount is used to create
a shared directory.

When selecting your storage solution, you can use EBS for
either or both of your local and shared storages disks. EBS
volumes are often the basis for an HPC storage solution.
Various types of EBS volumes are available including magnetic
hard disk drives (HDDs), general-purpose solid-state drives
(SSDs), and provisioned IOPS SSDs for high IOPS solutions.
They differ in throughput, IOPS performance, and cost.

You can gain further performance enhancements by selecting an
Amazon EBS-optimized instance.

An [Amazon EBS-optimized instance types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-optimized.html) uses an optimized configuration stack and
provides additional, dedicated capacity for Amazon EBS I/O. This optimization provides the best
performance for your EBS volumes by minimizing contention between Amazon EBS I/O and other
network traffic to and from your instance. Choose an EBS-optimized instance for more
consistent performance and for HPC applications that rely on a low-latency network or have
intensive I/O data needs to EBS volumes.

To launch an EBS-optimized instance, choose an instance type
that enables EBS optimization by default, or choose an
instance type that allows enabling EBS optimization at launch.

Instance store volumes, including nonvolatile memory express
(NVMe) SSD volumes (only available on certain instance
families), can be used for temporary block-level storage. For
EBS optimization and instance-store volume support, see
[Amazon EC2 Instance types](https://aws.amazon.com/ec2/instance-types/).

When you select a storage solution, align the solution with
your access patterns to achieve the desired performance. It is
easy to experiment with different storage types and
configurations. With HPC workloads, the most expensive option
is not always the best performing solution.

### Key AWS services

- [Amazon FSx](https://aws.amazon.com/fsx/)
- [Amazon FSx for Lustre](https://aws.amazon.com/fsx/lustre/)
- [Amazon FSx for OpenZFS](https://aws.amazon.com/fsx/openzfs/)
- [Amazon Elastic File System](https://aws.amazon.com/efs/)
- [Amazon Elastic Block Store](https://aws.amazon.com/ebs/)
- [Instance
store temporary block storage for EC2 instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html)

### Resources

- [Amazon EC2 Instance types](https://aws.amazon.com/ec2/instance-types/)
- [Deep
dive on accelerating HPC and ML with Amazon FSx](https://www.youtube.com/watch?v=6848CCaIqSY)
- [Amazon FSx for Lustre performance](https://docs.aws.amazon.com/fsx/latest/LustreGuide/performance.html)
- [Using
Lustre to build very fast file systems with Amazon FSx for Lustre](https://www.youtube.com/watch?v=0AVdf3jKuvo&t=4s)
- [How
Amazon File Cache works](https://www.youtube.com/watch?v=I1-Vxwgzlbk)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/high-performance-computing-lens/storage-architecture.html*

---
