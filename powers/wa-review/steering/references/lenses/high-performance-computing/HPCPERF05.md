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
