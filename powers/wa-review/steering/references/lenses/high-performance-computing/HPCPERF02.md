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
