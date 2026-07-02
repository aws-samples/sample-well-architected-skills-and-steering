# HPCOPS05 — Operational excellence

**Pillar**: Operational Excellence  
**Best Practices**: 1

---

## HPCOPS05-BP01 Predict how your system will respond to failures and design your operational management to mitigate these

For some of the potential failure modes you identify, you may be
able to mitigate them entirely by considering alternative
services and products early that reduce your operational burden.
For others you may have to implement automated responses or
documented runbooks as part of your reliability planning.

Specifically, for HPC environments, there are a number of
operational procedures you can modify when considering failure
modes. Determine and configure the behavior of your scheduler in
the case of compute node failures, for example if it resubmits
jobs and/or notifies users. If the head node is self-hosted,
consider designing procedures to handle its failure. For
example, you may choose to implement an alerting operation so
you can manually intervene or opt to add an active failover head
node to avoid interruption in cluster operations.

For tightly coupled HPC jobs, architecting for job-level
resiliency at runtime may come at the expense of job performance
or not be possible at all (i.e. any compute node failure will
result in total job failure), and so alternatives such as
checkpointing your state for long running jobs and resubmitting
jobs automatically in the case of infrastructure failure should
be implemented where possible.

### Implementation guidance

- Minimize your operational burden by choosing managed
services where possible and configuring your environment
to automate recovery.

Choosing managed services and features for your storage and
scheduling systems reduces your operational burden, for
example [AWS Parallel Computing Service](https://aws.amazon.com/pcs/), and using the persistent
file system mode in
[Amazon FSx for Lustre](https://aws.amazon.com/fsx/lustre/). At the scheduler level, implement job
retries on failure.

For example, if using AWS Batch you can implement
[Automated
job retries](https://docs.aws.amazon.com/batch/latest/userguide/job_retries.html) strategies to take action based on the
reason for failure.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/high-performance-computing-lens/prepare.html*

---
