# Performance Efficiency

**Pillar**: Performance Efficiency  
**Questions**: 5

---

# HPCPERF01 — Performance efficiency

**Pillar**: Performance Efficiency  
**Best Practices**: 1

---

## HPCPERF01-BP01 Evaluate containers or serverless functions

When evaluating compute options, consider containers or
serverless functions for your HPC workload or for parts of your
surrounding workflow.

### Implementation guidance

- Containers are a method of operating system virtualization
that is attractive for many HPC workloads, particularly if
the applications have already been containerized. AWS
services such as AWS Batch, Amazon Elastic Container Service (Amazon ECS), and Amazon Elastic Kubernetes Service (Amazon EKS) help deploy containerized
applications.
- Serverless functions abstract the execution environment.
You can use AWS Lambda to run code without deploying,
running, or maintaining, an instance. Many AWS services
emit events based on activity inside the service, and
often a Lambda function can be initiated off of service
events. For example, a Lambda function can be run after an
object is uploaded to Amazon S3. Many HPC users use Lambda
to automatically run code as part of their workflow.

### Key AWS services

- [Amazon EC2](https://aws.amazon.com/ec2/)
- [AWS Nitro System](https://aws.amazon.com/ec2/nitro/)
- [AWS ParallelCluster](https://aws.amazon.com/hpc/parallelcluster/)
- [AWS Batch](https://aws.amazon.com/batch/)
- [Amazon Elastic Container Service (ECS)](https://aws.amazon.com/ecs/)
- [Amazon Elastic Kubernetes Service (EKS)](https://aws.amazon.com/eks/)
- [AWS Lambda](https://aws.amazon.com/lambda/)

### Resources

- [AWS HPC Blog: How to manage HPC jobs using a serverless
API](https://aws.amazon.com/blogs/hpc/how-to-manage-hpc-jobs-using-a-serverless-api/)
- [Bare
metal performance with the AWS Nitro System](https://aws.amazon.com/blogs/hpc/bare-metal-performance-with-the-aws-nitro-system/)
- [Deploying
and running HPC applications on AWS Batch](https://aws.amazon.com/blogs/hpc/deploying-and-running-hpc-applications-on-aws-batch/)
- [How
to manage HPC jobs using a serverless API](https://aws.amazon.com/blogs/hpc/how-to-manage-hpc-jobs-using-a-serverless-api/)
- [What
is AWS ParallelCluster?](https://www.youtube.com/watch?v=gmw7A3kOh60)
- [Performance
Efficiency Pillar: AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_compute_hardware_select_best_compute_options.html#implementation-steps)

HPCPERF02: How do you select your computing instances?

EC2 instances are virtualized servers and come in different
families and sizes to offer a wide variety of capabilities. Some
instance families target specific workloads, for example,
compute, memory, or GPU intensive workloads. Other instances are
general purpose.

Both the targeted-workload and general-purpose instance families
are useful for HPC applications. Instances of particular
interest to HPC include the HPC Optimized family, the Compute
Optimized family and Accelerated Computing instance types that
are powered by GPUs and FPGAs.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/high-performance-computing-lens/compute-architecture.html*

---

# HPCPERF02 — Performance efficiency

**Pillar**: Performance Efficiency  
**Best Practices**: 2

---

## HPCPERF02-BP01 Select the best computing instance type for your workload by measuring application performance

Select the optimal Amazon EC2 instance type for your workload
and consider factors, such as family and generation, to optimize
for your desired price-for-performance. With access to on-demand
instances, testing different configurations is the best way to
determine your desired configuration for each of your workloads.

### Implementation guidance

EC2 Instances are available in different generations. Previous
generation instances are still fully supported, but we
recommend you to use the
[Amazon EC2 instance types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html#current-gen-instances) to get the best performance.

Some instance families provide variants within the family for
additional capabilities. For example, an instance family may
have a variant with local storage, greater networking
capabilities, or a different processor. These variants can be
viewed in the
[Amazon EC2 Instance types](https://aws.amazon.com/ec2/instance-types/) and may improve the performance of
some HPC workloads.

Within each instance family, one or more instance sizes allow
vertical scaling of resources. Some applications require a
larger instance type (for example, 48xlarge) while others run
on smaller types (for example, 2xlarge) depending on the
number or processes supported by the application.

For tightly coupled workloads, optimum performance is obtained
when the memory of the computing node is not shared between
different virtual machines within the same physical host.
Therefore, it is recommended to use only EC2 instances whose
size is big enough to occupy the entire physical node. This is
usually obtained with the largest instance type even if there
are some noticeable exceptions. For example, in the 7th
generation of HPC instances, each size in the instance family
has the same engineering specs, memory access and price, and
differs only by the number of cores offered. That means that
all the cores in the instances will be able to access the
entire host memory regardless of the instance size. So, you
can select also a smaller size without warring about the
performance impact of sharing the host memory with other
virtual machines.

The T-series instance family is designed for applications with
moderate CPU usage that can benefit from bursting beyond a
baseline level of CPU performance. Most HPC applications are
compute-intensive and suffer a performance decline with the
T-series instance family.

Applications vary in their requirements (for example, desired
cores, processor speed, memory requirements, storage needs,
and networking specifications). When selecting an instance
family and type, begin with the specific needs of the
application. You can also split a specific workflow in its
individual steps (for example, mesher and solver in a CFD
simulation) and run each step on a different instance type.
Instance types can be mixed and matched for applications
requiring targeted instances for specific application
components. You can use the AWS Management Console or the AWC CLI to
search for instances that satisfy your needs.

As an example, you can use the following command to display
only current generation instance types with 64 GiB (65536 MiB)
of memory:

```
`AWS ec2 describe-instance-types --filters
"Name=current-generation,Values=true"
"Name=memory-info.size-in-mib,Values=65536" --query
"InstanceTypes[*].[InstanceType]" --output text |
sort`
```

Testing different instance types is affordable since you only
pay for active usage. Even after your initial choice, you can
switch instance types whenever your requirements shift.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/high-performance-computing-lens/compute-architecture.html*

---

## HPCPERF02-BP02 Default to virtualized over bare-metal instances

Virtualized instances have a faster initialization time and
offer indistinguishable performance when compared to bare-metal
instances. Unless you specifically require a bare-metal
instance, we recommend virtualized instances, especially in
dynamic HPC environments.

### Implementation guidance

New-generation EC2 instances run on the
**AWS Nitro System.** The Nitro
System delivers practically all of the compute and memory
resources of the host hardware to your instances resulting in
better overall performance. Dedicated Nitro Cards enable
high-speed networking, high-speed EBS, and I/O acceleration
without having to hold back host resources for management
software.

The Nitro Hypervisor is a lightweight hypervisor that manages
memory and CPU allocation and delivers performance that is
indistinguishable from bare metal. The Nitro System also makes
bare metal instances available to run without the Nitro
Hypervisor. Launching a bare metal instance boots the
underlying server, which includes verifying all hardware and
firmware components. This means it can take longer before the
bare metal instance becomes available to start your workload,
as compared to a virtualized instance. The additional
initialization time must be considered when operating in a
dynamic HPC environment where resources launch and terminate
based on demand.

Unless your application specifically requires a bare metal
node, we recommend using virtualized instances to avoid the
longer boot time with metal instances without a gain in
performance.

### Key AWS services

- [Amazon EC2](https://aws.amazon.com/ec2/)
- [AWS Nitro System](https://aws.amazon.com/ec2/nitro/)

### Resources

- [Amazon Elastic Compute Cloud: Amazon EC2 instance types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html#current-gen-instances)
- [Amazon EC2 Instance types](https://aws.amazon.com/ec2/instance-types/)
- [Find
an Amazon EC2 instance type](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-discovery.html)
- [Specify
CPU options for an Amazon EC2 instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-specify-cpu-options.html)
- [Getting
the best OpenFOAM Performance on AWS](https://aws.amazon.com/blogs/hpc/getting-the-best-openfoam-performance-on-aws/)
- [Optimizing
HPC workloads with Amazon EC2 instances](https://d1.awsstatic.com/products/ec2/hpc/Optimizing%20HPC%20workloads%20with%20Amazon%20EC2%20instances%201-Nov-2023.pdf)

HPCPERF03: How do you optimize the compute environment?

You can optimize your compute environment through multiple
components, including the operating system and hardware
features. Since running in the cloud provides flexibility, we
recommend testing different configurations before determining
your final implementation.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/high-performance-computing-lens/compute-architecture.html*

---

# HPCPERF03 — Performance efficiency

**Pillar**: Performance Efficiency  
**Best Practices**: 1

---

## HPCPERF03-BP01 Optimize your compute environment for your workload

We recommend optimizing your machine image, application-compile
options, instance configuration, and runtime environment when
running your HPC applications.

### Implementation guidance

- A current operating system running a modern kernel is
critical to achieve the best performance and ensuring
access to the most up-to-date libraries. An Amazon Machine
Image (AMI) is a template that contains the software
configuration (operating system, libraries, and
applications) required to launch your instance. You can
select an AMI with the latest version of the operating
system supported by your application. For MPI workloads,
it is also important to use a modern MPI version.
- In addition to choosing an AMI, you can further optimize
your environment by taking advantage of the hardware
features of the underlying processors. There are three
primary methods to consider when optimizing the underlying
hardware:

- Advanced processor features
- Simultaneous multithreading (SMT)
- Processor affinity

HPC applications can benefit from these advanced processor
features (for example, Advanced Vector Extensions) and can
increase their calculation speeds by compiling the software
for the target CPU architecture. The compiler options for
architecture-specific instructions vary by compiler (check the
usage guide for your compiler).

AWS enables Simultaneous multithreading (SMT), commonly
referred to as Hyper-Threading, by default on most of the EC2
instances. Multithreading improves performance for some
applications by allowing two threads to run on the same
physical core. This command will give you the list of the EC2
instances that are offered in a location (or Region) with two
threads per core:

```
`AWS ec2 describe-instance-types --filters
"Name=current-generation,Values=true"
"Name=vcpu-info.default-threads-per-core,Values=2"
--query "InstanceTypes[*].[InstanceType]" --output
text --region us-east-2 | sort`
```

Most HPC applications benefit from disabling multithreading,
and therefore, it tends to be the preferred environment for
HPC applications. Multithreading is easily disabled in Amazon EC2 by
[Specify
CPU options for an Amazon EC2 instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-specify-cpu-options.html) for your
instance. Unless an application has been tested with
multithreading enabled, it is recommended that multithreading
be disabled and that processes are launched and individually
pinned to cores when running HPC applications. CPU or
processor affinity allows process pinning to easily happen.

Processor affinity can be controlled in a variety of ways. For
example, it can be configured at the operating system level
(available in both Windows and Linux), set as a compiler flag
within the threading library, or specified as an MPI flag
during execution. The chosen method of controlling processor
affinity depends on your workload and application.

There are many compute options available to optimize a compute
environment. Cloud deployment allows experimentation on every
level from operating system to instance type, to bare-metal
deployments. Because clusters are tuned before deployment,
time spent experimenting with cloud-based clusters is vital to
achieving the desired performance.

### Key AWS services

- [Amazon EC2](https://aws.amazon.com/ec2/)
- [AWS Nitro System](https://aws.amazon.com/ec2/nitro/)

### Resources

- [Specify
CPU options for an Amazon EC2 instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-specify-cpu-options.html)
- [Processor
state control for Amazon EC2 Linux instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/processor_state_control.html)
- [Instance
sizes in the Amazon EC2 Hpc7 family – a different
experience](https://aws.amazon.com/blogs/hpc/instance-sizes-in-the-amazon-ec2-hpc7-family-a-different-experience/)
- [Application
deep-dive into the AWS Graviton3E-based Amazon EC2 Hpc7g
instance](https://aws.amazon.com/blogs/hpc/application-deep-dive-into-the-graviton3e-based-amazon-ec2-hpc7g-instance/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/high-performance-computing-lens/compute-architecture.html*

---

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

# HPCPERF05 — Performance efficiency

**Pillar**: Performance Efficiency  
**Best Practices**: 1

---

## HPCPERF05-BP01 Consider latency, bandwidth, and throughput requirements for HPC workloads

The optimal network solution for an HPC workload varies based on
latency, bandwidth, and throughput requirements. Tightly coupled
HPC applications often require the lowest latency possible for
network connections between compute nodes. For moderately sized,
tightly coupled workloads, it is possible to select a large
instance type with a large number of cores so that the
application fits entirely within the instance without crossing
the network at all.

Alternatively, some applications are network bound and require
high network performance. Instances with higher network
performance can be selected for these applications. The highest
network performance is usually obtained with the largest
instance type in a family. Refer to the
[Amazon EC2 Instance types](https://aws.amazon.com/ec2/instance-types/) for more details.

### Implementation guidance

Use cluster placement groups and Elastic Fabric Adapter for tightly coupled
applications.

Multiple instances with low latency between the instances are
required for large tightly coupled applications. On AWS, this
is achieved by launching compute nodes into a cluster
placement group, which is a logical grouping of instances
within an Availability Zone. A cluster placement group
provides non-blocking and non-oversubscribed connectivity,
including full bisection bandwidth between instances. Use
cluster placement groups for latency sensitive tightly coupled
applications spanning multiple instances.

In addition to cluster placement groups, tightly coupled
applications benefit from Elastic Fabric Adapter (EFA), a
network device that can attach to your Amazon EC2 instance.
EFA provides lower and more consistent latency and higher
throughput than the TCP transport traditionally used in
cloud-based HPC systems. It enables an OS-bypass access model
through the *Libfabric* API that allows HPC
applications to communicate directly with the network
interface hardware. EFA enhances the performance of MPI and
NCCL inter-instance communication, is optimized to work on the
existing AWS network infrastructure, and is critical for
scaling tightly coupled applications.

If an application cannot take advantage of EFA's OS-bypass
functionality, or an instance type does not support EFA,
optimal network performance can be obtained by selecting an
instance type that supports Elastic Network Adapter (ENA) or
ENA Express. ENA provides EC2 instances with higher networking
performance and lower CPU utilization through the use of
pass-through rather than hardware-emulated devices. This
method allows EC2 instances to achieve higher bandwidth,
higher packet-per-second processing, and lower inter-instance
latency compared to traditional device virtualization.

ENA is available on all current-generation instance types and
requires an AMI with supported drivers. Although most current
AMIs contain supported drivers, custom AMIs may require
updated drivers. For more information on enabling enhanced
networking and instance support, refer to the
[Enhanced
networking on Amazon EC2 instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/enhanced-networking.html).

ENA Express is an ENA feature that can be enabled on certain
EC2 instances and it is designed to increase the single flow
bandwidth and lower the tail latency of network traffic
between EC2 instances. Workloads such as distributed storage
systems and live media encoding that require large flows and
are sensitive to variance in latency can benefit from ENA
Express.

- Distribute your jobs across multiple Availability Zones or
Regions for loosely coupled workloads.

Loosely coupled workloads are generally not sensitive to very
low-latency networking and do not require the use of a cluster
placement group or the need to keep instances in the same
Availability Zone or Region.

- Use the Instance Type Matrix to determine the right
instance type for your network bandwidth needs.

In some cases, the available network bandwidth depends on the
type of network traffic. For example, HPC optimized instances,
can access a higher network bandwidth when used together with
EFA. The
[Amazon EC2 Instance types](https://aws.amazon.com/ec2/instance-types/) page contains all the networking
details that will help you to select the right instance type
for your network bandwidth needs.

### Key AWS services

- [Placement
groups for your Amazon EC2 instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html)
- [Elastic
Fabric Adapter for AI/ML and HPC workloads on Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa.html)
- [Enable
enhanced networking with ENA on your EC2 instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/enhanced-networking-ena.html)
- [Improve
network performance between EC2 instances with ENA
Express](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ena-express.html)

### Resources

- [Amazon EC2 Instance types](https://aws.amazon.com/ec2/instance-types/)
- [How
EFA works and why we don't use InfiniBand in the
cloud](https://www.youtube.com/watch?v=IgPWzhIHX68&t=1416s)
- [NCCL on
EFA](https://youtu.be/kDtHpRB5luw)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/high-performance-computing-lens/network-architecture.html*

---

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
