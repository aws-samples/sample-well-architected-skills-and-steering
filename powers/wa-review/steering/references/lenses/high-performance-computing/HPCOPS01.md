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
