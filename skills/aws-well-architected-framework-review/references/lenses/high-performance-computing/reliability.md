# Reliability

**Pillar**: Reliability  
**Questions**: 3

---

# HPCREL01 — Reliability

**Pillar**: Reliability  
**Best Practices**: 2

---

## HPCREL01-BP01 Consider instance type flexibility for your workload

Consider using multiple instance types for your workload. HPC
orchestration services including Amazon Parallel Computing
Service and AWS Batch allow you to select multiple instance
types for a given workload. Additionally, in AWS ParallelCluster, multiple instance types can be selected for a
single Slurm partition. In AWS Batch, multiple instance types
can be specified for a single Compute Environment.

### Implementation guidance

- Allow for multiple instance types in your compute
environment, and cycle through different instance types if
need be.

With AWS Batch, users can list multiple instance types or
families for the Compute Environment. For more information,
see
[JobQueueDetail](https://docs.aws.amazon.com/batch/latest/APIReference/API_JobQueueDetail.html#compute_environment_compute_resources).
Multiple instance types can also be configured with AWS ParallelCluster and with Amazon Parallel Computing Service.
For more information, see
[Multiple
instance type allocation with Slurm](https://docs.aws.amazon.com/parallelcluster/latest/ug/slurm-multiple-instance-allocation-v3.html).

Consider starting with AWS HPC instances for best
price-performance, and if unavailable, consider cycling to
higher cost compute-optimized instances.

- Cycle through capacity pools in different Availability
Zones for specific instance types for tightly coupled
workloads.

Cycling through capacity pools allows you to identify which
Availability Zone within a region meets the capacity
requirements for your workload, and to run your job within
that Availability Zone. Cycling can be implemented with user
scripts, or alternatively within specific orchestrators on
AWS. With AWS ParallelCluster, for example, you can create
set a multi-availability zone queue (see
[Multiple
Availability Zones now supported in AWS ParallelCluster
3.4](https://aws.amazon.com/blogs/hpc/multiple-availability-zones-now-supported-in-aws-parallelcluster-3-4/)), and all or nothing scheduling ( see
[Minimize
HPC compute costs with all-or-nothing instance
launching](https://aws.amazon.com/blogs/hpc/minimize-hpc-compute-costs-with-all-or-nothing-instance-launching/)), to help take full advantage of any
available capacity pools.

Your shared storage location should match your selected
Availability Zone for compute resources. Specifically, if you
have an FSx for Lustre filesystem in one Availability Zone,
and compute in another, you will incur inter-AZ traffic costs.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/high-performance-computing-lens/workload-architecture.html*

---

## HPCREL01-BP02 Deploy loosely coupled workloads across multiple Availability Zones

Deploying across multiple Availability Zones can help improve capacity availability for
scale-out workloads, and can also help with disaster recovery. AWS ParallelCluster and
AWS Batch both allow for deploying architectures across multiple Availability Zones. Loosely
coupled jobs that do not have interdependency on each other should be deployed across
multiple Availability Zones. When deploying across multiple Availability Zones, consider
cost implications for transferring data across Availability Zones.

Tightly coupled workloads should be deployed within a single Availability Zone, and
within a placement group. Using a central data repository, such as Amazon FSx for Lustre or Amazon S3,
and utilizing infrastructure as code with CloudFormation templates, allows for recovering to
an alternative Availability Zone, even for tightly coupled, single-AZ workloads.

### Implementation guidance

Depending on services utilized in your architecture, evaluate and verify that each
service utilizes multiple availability zones.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/high-performance-computing-lens/workload-architecture.html*

---

# HPCREL02 — Reliability

**Pillar**: Reliability  
**Best Practices**: 2

---

## HPCREL02-BP01 Install software packages in a shared location to simplify multi-user, multi-resource software requirements management

Installing software packages on shared storage, such as Amazon Elastic File System (EFS), allows users
across compute environments and clusters access the same versioned set of packages.
Dependencies can also be installed using a custom AMI, or using a post-install script, such
as configured with [AWS ParallelCluster](https://docs.aws.amazon.com/parallelcluster/latest/ug/custom-bootstrap-actions-v3.html).

### Implementation guidance

Install software in shared location for multi-user or multi-resource environments.
Single resource environments can use a custom AMI or separate Amazon Elastic Block Store (Amazon EBS) volume,
and multi-resource environments can use shared storage, such as Amazon Elastic File System (Amazon EFS).

*Source: https://docs.aws.amazon.com/wellarchitected/latest/high-performance-computing-lens/change-management.html*

---

## HPCREL02-BP02 Use package managers to simplify software dependency management when possible

Managing HPC applications can potentially be simplified with
package managers, such as Spack, SBGrid, and EasyBuild. AWS
hosts a Spack binary cache for fast installation of commonly
used HPC packages and applications. Leveraging a package manager
simplifies dependency management for system admins while
providing exact versioning per user requirements.

### Implementation guidance

Consider a package manager to simplify software dependencies.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/high-performance-computing-lens/change-management.html*

---

# HPCREL03 — Reliability

**Pillar**: Reliability  
**Best Practices**: 2

---

## HPCREL03-BP01 Implement checkpointing

For long-running cases, incorporating regular checkpoints in
your code allows you to continue from a partial state in the
event of a failure. Checkpointing is a common feature of
application-level failure management already built into many HPC
applications.

Checkpointing is recommended for long running jobs on both on demand and Spot
Instances. When using Spot Instances, some applications may benefit from changing the
default Spot interruption behavior (for example, stopping or hibernating the instance rather
than terminating it). Consider the durability of the storage option when relying on
checkpointing for failure management.

### Implementation guidance

Implement checkpointing for long-running jobs

The most common approach is for applications to periodically
write out intermediate results. The intermediate results offer
potential insight into application errors and the ability to
restart the case as needed while only partially losing the
work. For example, you can implement checkpointing at the
application level ( see
[Running
cost-effective GROMACS simulations using Amazon EC2 Spot
Instances with AWS ParallelCluster](https://aws.amazon.com/blogs/hpc/running-gromacs-on-spot-with-checkpointing/)) and
[use
the Spot Interruption notices](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-instance-termination-notices.html).

*Source: https://docs.aws.amazon.com/wellarchitected/latest/high-performance-computing-lens/failure-management.html*

---

## HPCREL03-BP02 Use durable storage to store and back up datasets

HPC workloads often require parallel file systems for high
throughput I/O. In many cases, data also needs to be stored
securely and durably for several years. To achieve both these
requirements, store and back up data in durable storage, and use
high performant file systems primarily during data processing.

### Implementation guidance

Create a Data Repository Association (DRA) between Amazon FSx for Lustre and Amazon S3.

When using Amazon FSx for Lustre, create a data repository
association (DRA) with an Amazon S3 bucket. Amazon Simple Storage Service (S3) allows users to store data in highly
available, cost-effective object storage, with tiering to
manage hot through cold data. Amazon S3 improves reliability
by serving as a central repository for workload datasets. With
a DRA between S3 and FSx for Lustre, by default, data is
automatically transferred from Amazon S3 to Amazon FSx for Lustre when it is first accessed. Amazon FSx for Lustre also
supports additional ways of
[Importing
changes from your data repository](https://docs.aws.amazon.com/fsx/latest/LustreGuide/importing-files-dra.html) and
[Exporting
changes to the data repository](https://docs.aws.amazon.com/fsx/latest/LustreGuide/export-changed-data-meta-dra.html) data.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/high-performance-computing-lens/failure-management.html*

---

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
