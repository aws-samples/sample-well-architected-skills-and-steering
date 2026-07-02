# HPCOPS02 — Operational excellence

**Pillar**: Operational Excellence  
**Best Practices**: 1

---

## HPCOPS02-BP01 Evaluate options for scheduling jobs in your cloud environment

If you have an existing system, consider how you currently
schedule and manage jobs and if it meets your current
requirements. Considering whether you want to complement,
augment or replace your current system with your cloud system,
determine the level of integration needed between your hybrid
environments. Determine whether you want to integrate a
traditional scheduler with flexible cloud provisioning, use a
cloud native scheduling mechanism, such as
[AWS Batch](https://aws.amazon.com/batch/), or develop job orchestration to create an
ephemeral cluster for each job. Cloud offers various flexible
and efficient ways to manage jobs and orchestrate
infrastructure.

### Implementation guidance

If you have a simple workflow where you need to run a single job or a small set of
jobs without the overhead of a scheduler, implement an event-driven pattern that can run
your job directly and tear down the resources automatically.

In a case where batch jobs are not running continuously and
there is significant time where your cloud cluster is unused,
it may be worth considering additional operations of tearing
down your cluster and recreating it either on a fixed schedule
or on-demand. This may increase the latency with which the
first job begins running and forces any environment
customizations to be scripted for repeatability, but can
optimize costs. It is important to separate the compute and
storage requirements in such a scenario, so that the compute
cluster can be deleted and recreated without affecting files
on shared file systems. To carry this process even further,
you may consider mounting multiple file systems into your
cluster and persisting some of them but deleting others.

The infrastructure as code example on GitHub:
[Event-driven
weather forecasts](https://github.com/aws-samples/event-driven-weather-forecasts) shows you how this case can be
implemented using an event driven pattern to create an
ephemeral cluster to run a single job and store the results
without manual intervention. In this case, it is for weather
simulations that need to occur periodically, and when not in
use, as much of the infrastructure as possible is removed to
optimize costs.

- If using a scheduler, evaluate cloud-native schedulers and
traditional HPC schedulers with cloud integrations with
the level of operations management.

A traditional HPC scheduler can offer benefits such as
familiarity for your system end-users, and minimal or no
changes to your existing job scripts. Implementations such as
[AWS ParallelCluster](https://docs.aws.amazon.com/parallelcluster/latest/ug/what-is-aws-parallelcluster.html) enable you to leverage these
traditional schedulers while still taking advantage of cloud
benefits by scaling compute capacity up when jobs are
submitted to the scheduler, and down when there are no more
remaining jobs to optimize cost. Managed implementations such
as [AWS Parallel
Computing Service](https://aws.amazon.com/pcs/) take this one level further, and
handle the operational management of the head-node for you,
including aspects such as failover and system upgrades.

Meanwhile, cloud-native schedulers can offer reduced
operational overhead, and workflow level integrations to
abstract away concepts such as head nodes and compute pools
from end-users. They can be a great choice when running
standardized workflows and pipelines of tasks. For example
[AWS Batch](https://aws.amazon.com/batch/) is a cloud native scheduler that can integrate
with services such as
[AWS Step Functions](https://aws.amazon.com/step-functions/) for complex workflow logic, as well as
domain-specific workflow languages such as
[NextFlow](https://www.nextflow.io/).

You may choose to implement multiple types of scheduling
solutions to suit differing applications, user needs, and job
profiles. Alternatively, you might choose a traditional
scheduler to meet current user expectations and modernize
their workflow in phases. This is often an attractive choice
in large organizations with multiple research departments with
well-established workflows.

HPCOPS03: Does your use case require data movement between separated
environments, and how is this handled?

Will your users be moving data between separated environments,
such as an on-premises cluster and the cloud, and if so, do
you know the predicted amount and movement patterns? Do you
want to enable a seamless data management workflow for
movement and archiving for ease of use, or do you want users
to make an intentional choice of where they run their
workloads at submission time? Have you considered alternative
options to minimize the required data movement, such as remote
visualization solutions? See
[Scenarios](./scenarios.html) for additional
considerations.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/high-performance-computing-lens/prepare.html*

---
