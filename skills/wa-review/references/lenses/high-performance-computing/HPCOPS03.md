# HPCOPS03 — Operational excellence

**Pillar**: Operational Excellence  
**Best Practices**: 1

---

## HPCOPS03-BP01 Understand your data movement requirements

In general, moving data back and forth regularly should be
avoided unless absolutely necessary. Identify early however if
data needs to be loaded to a location before a job starts and if
results need to be copied out on job completion, and whether
this can occur asynchronously or not. Identify how users are
interacting with each of your environments, and whether they are
taking advantage of the benefits of each one as far as
reasonable.

For example, some environments may offer latency benefits to
large datasets and some may offer more flexible hardware
choices, and jobs should be distributed accordingly. Being
intentional about these trade-offs at job submission time helps
you verify that you are only moving data when it is beneficial
to do so.

Consider extending the HPC system to include virtual desktop
infrastructure (VDI) solutions and/or automated data processing
steps to avoid the need for data movement for pre-processing and
post-processing, centralize access control, and reduce the
security exposure of your files, whilst reducing the need to
manage the operations to handle regular data movement.

### Implementation guidance

- Implement remote visualization solutions to minimize data
movement, saving movement time and cost, and centralizing
file access controls.

Start by implementing
[AWS Research and Engineering Studio](https://docs.aws.amazon.com/res/latest/ug/overview.html) to streamline your VDI
requirements while addressing other HPC management needs like
project budgeting. Another option if you are using a
traditional HPC scheduler is to implement visualization
queues, as demonstrated in the blog post for AWS ParallelCluster:
[Elastic
visualization queues with Amazon DCV in AWS ParallelCluster](https://aws.amazon.com/blogs/hpc/elastic-visualization-queues-with-nice-dcv-in-aws-parallelcluster/). VDI solutions offer the additional
advantage of accessing graphics-accelerated instances when
required.

- Schedule jobs to run near existing data

Configure automatic job scheduling to run computations close
to data sources, eliminating separate data transfer
operations. Alternatively, if user-controlled job placement is
preferred, ensure data location visibility to help users
select optimal computing environments. For data movement and
hybrid storage considerations, see the
[Performance Efficiency
pillar](./performance-efficiency.html).

HPCOPS04: How will you handle future environment updates with minimal user
impact?

With constantly improving hardware, service, and product
offerings and patches, it is worthwhile considering how you
can design your system upfront to allow for easy replacement
of modules and phased migrations between environments with
minimal effort and automated testing.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/high-performance-computing-lens/prepare.html*

---
