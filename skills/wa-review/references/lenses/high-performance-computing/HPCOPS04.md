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
