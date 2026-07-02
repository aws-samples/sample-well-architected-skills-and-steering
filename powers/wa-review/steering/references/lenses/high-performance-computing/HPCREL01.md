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
