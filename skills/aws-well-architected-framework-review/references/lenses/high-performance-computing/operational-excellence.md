# Operational Excellence

**Pillar**: Operational Excellence  
**Questions**: 7

---

# HPCOPS01 — Operational excellence

**Pillar**: Operational Excellence  
**Best Practices**: 1

---

## HPCOPS01-BP01 Start from business objectives and organizational priorities, and drive operational decisions about your HPC environment from them

Collect business objectives and priorities from your users and
organizational stakeholders to guide your operational decisions.
Use these in combination with price objectives to design the HPC
system, as opposed to starting with hardware requirements, in
order to take the most advantage of the cloud. Examples of
business requirements may include number of completed jobs per
month, wait times for jobs to begin, requirements for runtimes,
ability to specify priorities for jobs which affect the
scheduling, and managing cluster access for fair usage from all
users over time.

Traditional HPC environments are fixed and shared across users,
which brings the benefit of a familiar system for users.
However, in the cloud, there are flexible ways to build and
operate your HPC environment. One approach is to allow your
users, or individual departments the flexibility of creating and
evolving their own environments, while applying guardrails at
the account or organizational level to provide a safe
environment for experimentation. Examples of such guardrails
could be limiting access to particular instance types and AWS
services, and enforcing tagging on all deployed instances so
that you can use tag-based observability mechanisms to attribute
cost to business departments. Alternatively, you could provide a
managed cluster to all end-users with centralized
administration. This HPC environment would be similar to a
traditional HPC environment. In this case, end-users would not
require permissions to modify infrastructure in your cloud
environment but would need a unified interface to handle jobs
and data management.

Your organizational objectives will help you to choose the right
approach. For example, if your primary motivation is to increase
the pace of research in your organization by leveraging the
latest domain specific AWS products and features, and reducing
the dependency on central IT systems, then the first approach of
distributed infrastructure management would be a strong fit. If
it is more important to maintain ease of use for end-users and
get them up and running in a familiar environment, while
introducing background improvements such as performance uplift
through new instances, and reduced operational overhead through
managed service options, then the second approach is a more
natural starting point for your cloud deployment.

Additionally, the second approach also allows your central IT
team to enforce specific rules that you may require for security
and compliance reasons in a straightforward and familiar way.
Conversely, if your organization is split into departments with
very different IT requirements, or you need to clearly attribute
costs back to each department, a distributed infrastructure
across separated accounts in an AWS Organization will allow you
to simplify the management of separating environments and
handling chargeback.

### Implementation guidance

- Collect, organize and discuss your stakeholder
requirements.

After collecting requirements from your business stakeholders,
you are likely to end up with a combination of functional and
design implementation requirements that you should separate.
By starting your environment design from the functional
requirements, you may design architectures for example that do
not tie you into specific hardware configurations, specific
cluster sizes, and may highlight opportunities to simplify
your operational burden given that some of the restrictions in
fixed-cluster environments no longer apply.

Also aim to create a budgeting model that minimizes the need
for users to tie into particular hardware configurations, to
make it easier to leverage the flexible hardware choices and
take advantage of new hardware as it becomes available. Then
take the benefits of this cloud native design, and compare it
to the design implementation requirements. Where a discrepancy
exists, discuss with the original stakeholder to make an
informed tradeoff.

- If you grant users the ability to manage infrastructure,
implement guardrails that enforce your organizational
requirements.

We inherit broader cloud best-practices and learnings for
setting up cloud environments with distributed infrastructure
administration, which are well documented in the
[Operational
Excellence](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/operational-excellence.html) pillar of the AWS Well Architected
whitepaper, many of which can be carried over into HPC
contexts. Specifically for HPC environments, see
[The
plumbing: best-practice infrastructure to facilitate HPC on
AWS](https://aws.amazon.com/blogs/hpc/the-plumbing-best-practice-infrastructure-to-facilitate-hpc-on-aws/). The
[Landing
Zone Accelerator on AWS](https://aws.amazon.com/solutions/implementations/landing-zone-accelerator-on-aws/) Solution is discussed, which
proposes a solution with multiple AWS accounts. Such a design
logically separates different HPC clusters and customizes them
to specific groups or departments while providing a boundary
for administration and reducing impact on other environments.
While it is possible to self-build and manage a landing zone,
best-practices (including for Landing Zone Accelerator)
leverage AWS Control Tower, which is a managed service
purpose-built for this task.

- Aim to map any architecture decisions to managed products
and services, or supported solutions to reduce your
operational burden.

Once the stakeholder requirements have been organized, aim to
map their infrastructure implementation to managed products
and services which have defined support models. Understand
which parts of your environment will be supported and at what
level, and identify early where any operational risks remain.
Reference or illustrative solutions can help to stitch
together complex infrastructures quickly for demonstrative
purposes, but for your production environments lean towards
using supported building blocks that can be assembled together
in a well-understood fashion. This will reduce your
operational burden for proactive maintenance, and give you
clear points of contact for reactive support of your
environments.

For more information on the latest AWS supported HPC
components, see
[High
Performance Computing](https://aws.amazon.com/hpc/). Each of these components offer
functionality for common sets of requirements in HPC
environments. For example,
[AWS Parallel
Computing Service](https://aws.amazon.com/pcs/) offers features to scale compute
capacity to run submitted jobs and manage cluster operations.
[Research
and Engineering Studio on AWS](https://aws.amazon.com/hpc/res/) offers features that
allow administrators to manage projects and map user
identities to their cloud AWS HPC environment, and allows
users to manage sessions and run interactive applications with
remote visualization.

[AWS HPC Partner organizations](https://partners.amazonaws.com/search/partners?facets=Use%20Case%20%3A%20High%20Performance%20Computing%20%3A%20HPC%20Management) can provide solutions with
additional functionality, a range of implementation and
maintenance support options, and industry focused guidance.
The [AWS HPC blogs](https://aws.amazon.com/blogs/hpc/) highlight common architectural patterns that
combine various solutions and services, and also offer
guidance on industry specific patterns. These patterns and
partner offerings can combine to help you build up your
environment with clear lines of support.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/high-performance-computing-lens/organization.html*

---

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

# HPCOPS04 — Operational excellence

**Pillar**: Operational Excellence  
**Best Practices**: 2

---

## HPCOPS04-BP01 Minimize impact when migrating users and their jobs between HPC environments

Standardize access across HPC environments, and retain and
migrate data in the cases of environment upgrades or migrations.
If you are using a scheduling mechanism, understand how these
can be migrated to different environments, and the impact on
running jobs. In some HPC cluster environments there are long
running jobs that run over time periods that may otherwise be
used as maintenance windows such as weekends. In such cases you
may consider having a longer period for blue or green
migrations, where new jobs are submitted to the new cluster and
the old cluster is given multiple days before deleting to
complete all jobs.

Separate your file system from the lifecycle of your HPC
environment, and implement regular backups. For example, while a
tool like AWS ParallelCluster is able to create an
[FSx for Lustre](https://aws.amazon.com/fsx/lustre/) file system for you, choose to create a file
system separately and reference that in your cluster deployment.
This will allow you to implement strategies such as ephemeral
compute clusters and upgrade your clusters independently of
non-scratch data. These file systems can also be simultaneously
mounted to your new cluster and old cluster, helping provide a
seamless transition between environments for end-users.

Consider decoupling the cluster access from the user access, for
example with an
[Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html) (ALB),
[Elastic
IP addresses](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html), or abstracting the submission to the
scheduler with a user facing submission form that can be
connected to different schedulers, such as
[Open
OnDemand](https://openondemand.org/). This will allow you to replace the cluster
transparently to the user and allow you to implement migration
mechanisms such as gradual weighted blue or green deployments.

### Implementation guidance

Manage your data operations separately to the lifecycle of your compute environment.

When migrating between compute environments, users' data
should be preserved as far as possible. Create file systems
separately to the infrastructure as code stacks that define
the compute environments, and reference the file systems to
import them into your cluster where possible. If using AWS ParallelCluster for example, you should mount existing file
systems in the
[SharedStorage](https://docs.aws.amazon.com/parallelcluster/latest/ug/SharedStorage-v3.html)
section of the cluster configuration file. You can then handle
the operations of different compute environments flexibly, and
for example integrate different compute orchestration
services, while providing a single location for end-users to
store their data.

Educate users if you intend to treat particular file systems
as ephemeral or scratch, so that they know any data stored on
these file systems will be lost between environment changes.
This may be desirable for some use cases where temporary data
is created during job runs and not automatically deleted, and
in such cases an intentional choice can be made to not carry
this data between clusters. This also allows you to handle the
operations of your data in a more tailored way. For example,
performing automated backups of your persistent file systems,
whilst optimizing costs on your scratch file systems.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/high-performance-computing-lens/prepare.html*

---

## HPCOPS04-BP02 Implement your environments with infrastructure as code and version control your deployments

Implementing your environment with infrastructure as code (IaC)
as much as feasible, and complementing it with clear
documentation steps for components that cannot be automated
allows you to automate your deployments. These templates can
then also be put under version control, which allows you to
track changes between deployment versions, and provides a
centralized location for different stakeholders in your
organization to observe and approve operational changes. This
also gives you the ability to reproduce environments for use
cases such as results verification and reproducibility, and the
ability to fail back to old versions in the case of regressions.

See
[Operational
excellence](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/operational-excellence.html) pillar of the AWS Well Architected whitepaper
for guidance on using infrastructure as code for your
deployments. There are a few common customizations to this for
HPC environments. One aspect is that HPC codes are often
compiled such that a shared POSIX compatible file system is
required, and these compilations can also be lengthy. Therefore,
it often makes sense to leave the shared file system which
stores the applications running even if the rest of the
environment scales up and down elastically.

Another aspect is that HPC instance capacity may be deployed in
specific availability zones (AZ). If you use this capacity,
parametrize or create a mapping of desired availability zones in
your infrastructure as code (IaC) templates to keep them
flexible across regions. Similarly, if you have deployed file
systems in a particular availability zone that need to be
mounted to your environment, your cluster should also be
deployed in that availability zone to prevent data transfer
between availability zones.

### Implementation guidance

- Utilize tools such as AWS CloudFormation and bootstrap
scripts to define your HPC environments with code.

Tools such as AWS ParallelCluster themselves are forms of IaC,
but can also sit within broader AWS CloudFormation IaC
scripts, as detailed in the tutorial:
[Creating
a cluster with AWS CloudFormation](https://docs.aws.amazon.com/parallelcluster/latest/ug/tutorials_09_cfn-custom-resource-v3.html). This allows you to
provision full stack deployments from these scripts, and
examples of such environments and helper scripts for further
customization are documented in the
[HPC
Recipes for AWS](https://github.com/aws-samples/aws-hpc-recipes) repository.

HPCOPS05: How will your system respond to failures and anomalies?

- Have you designed your architecture to mitigate
predictable failure modes of your system and user jobs?
- How easy will it be to diagnose and correct various error
sources, and are there opportunities to automate
responses?

While we will test the system and implement recovery strategies in the [Reliability pillar](./reliability.html) of the lens, planning for predictable
failure modes and working backwards to architect solutions will have implications for your
operational decisions.**

*Source: https://docs.aws.amazon.com/wellarchitected/latest/high-performance-computing-lens/prepare.html*

---

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

# HPCOPS06 — Operational excellence

**Pillar**: Operational Excellence  
**Best Practices**: 1

---

## HPCOPS06-BP01 Test and observe job-level performance for every change

Before moving users to a new cluster environment, you should run
a set of representative HPC job benchmarks to confirm that your
system is performing as expected. To verify that this
performance is maintained, consider periodically rerunning these
benchmarks or a subset so that any unexpected changes can be
localized and investigated early.

As the projects of your users evolve, the requirements and usage
of your HPC environment will also change from the initial set of
jobs on which your representative set of testcases were built.
To verify that the performance tests are relevant, you could
periodically update your testcases, or you can consider
alternative methods such as monitoring the jobs that your users
are running. For example, by monitoring job logs or percent
usage by department or user, you may proactively detect
anomalies. You can then investigate whether these anomalies were
caused by a known change in usage patterns, or an unexplained
performance regression. Set alerts and automated responses where
appropriate.

Performance regressions can go undetected as they may not throw
any errors, but can result in longer running jobs and increased
cost per job. Consider adding operational mechanisms to track
metrics of your jobs and building them into a cohesive
dashboard. You can use these collected metrics to tune your
environment based on real usage, such as rightsizing the tier of
throughput and capacity of your file systems, or adding new
compute options similar to hardware configurations that are
currently oversubscribed.

### Implementation guidance

Log job-level statistics, track anomalies and integrate your
environment logging into a dashboard.

There are a number of options for tracking the operational
performance of your HPC environment which vary in the level of
granularity the offer and operational overhead required to run
them. Most HPC schedulers have their own tools to track job
level metrics, and these can be the easiest place to start as
they natively integrate with the scheduler.

If using AWS ParallelCluster with Slurm, leverage
[Slurm
accounting with AWS ParallelCluster](https://docs.aws.amazon.com/parallelcluster/latest/ug/slurm-accounting-v3.html) to log job-level
statistics in an external database. You can then add a method
to visualize these metrics so you can easily gain a view
across your environment. The
[ParallelCluster
Monitoring dashboard](https://github.com/aws-samples/parallelcluster-monitoring-dashboard) repository is an example of how
you can construct a dashboard to track job data. If using AWS Batch, a similar tool is the
[AWS Batch Runtime Monitoring Dashboards Solution](https://github.com/aws-samples/aws-batch-runtime-monitoring).

Higher level alternative or complementary tracking methods
such as tagging cloud resources by project and using them to
drill down into cost reports using AWS cost allocation tags to
detect anomalies can offer a similar effect with lower
operational overhead but reduced granularity. For more
information, see
[Organizing
and tracking costs using AWS cost allocation tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html). Many
tools such as
[AWS ParallelCluster resources and tagging](https://docs.aws.amazon.com/parallelcluster/latest/ug/resources-tags-v3.html) and AWS Batch
resource tagging:
[Tag
your AWS Batch](https://docs.aws.amazon.com/batch/latest/userguide/using-tags.html) resources integrate with this mechanism
natively to simplify automated tagging.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/high-performance-computing-lens/operate.html*

---

# HPCOPS07 — Operational excellence

**Pillar**: Operational Excellence  
**Best Practices**: 1

---

## HPCOPS07-BP01 Review and test the latest service, product and software updates for business fit and reduction in operational overhead

Consider creating a test environment where you can review your
representative workload benchmarks on new instances and software
versions. If using AWS Organizations, create your test
environment within a designated Sandbox organizational unit
(OU). For more information, see
[Organizing
Your AWS Environment Using Multiple Accounts](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.html). Consider
also new storage options and configurations which may offer
additional functionality such as increased resiliency. Software
updates such as communication library upgrades can provide
performance improvements on existing hardware, and so should
also be tested periodically with your representative benchmarks,
as well as new functionality that can improve the user
experience.

In addition to performance improvements, new services and
products may offer reduced operational overhead. This may be by
managing more of the operations of the cluster for you in a
prescriptive approach, or may be by offering domain or workload
specific interfaces that make it easier for end-users to
interact with the system and reduce the customization you have
to maintain from a single generic environment. By being able to
integrate these new modules into your existing environment, for
example by mounting the same file systems, you can enable
experimentation and provide a mechanism to asses business fit.

### Implementation guidance

Test the latest versions of your chosen products, and review the latest HPC on AWS
news.

If using AWS ParallelCluster, periodically deploy test
environments with the latest release, as these often have
software upgrades included. New major releases also often add
new functionality that you can explore to see if it helps your
use case. AWS Parallel Computing Service is a good example of
a service that offers a way for you to reduce your operational
overhead in the management of your cluster, and introduces
prescriptive implementations of patterns and features that are
commonly required in HPC environments.

To keep updated on new releases relevant to the HPC space more
broadly and learn from continuously evolving best practices,
periodically review the
[AWS HPC community
site, Day1HPC](https://day1hpc.com/). Updates such as new instance launches
can offer price and performance improvements, and new features
can improve the end-user experience or reduce your operations
management overhead.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/high-performance-computing-lens/evolve.html*

---

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
