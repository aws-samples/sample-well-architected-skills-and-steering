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
