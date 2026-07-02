# MSFTCOST03 — Databases

**Pillar**: Cost Optimization  
**Best Practices**: 6

---

# MSFTCOST03-BP01 Understand Microsoft SQL Server licensing and BYOL availability

AWS offers a range of flexible cost optimization choices for
licensing. These licensing options are designed to help you reduce
costs, maintain compliance, and meet your business needs. AWS offers
the license include option, which you can launch Windows EC2
instances with SQL Server installed and licensed on-demand, paying
only for what you use. With the right requirements, you can also
bring your own licenses to AWS, either to Amazon EC2 Dedicated Hosts
or default (shared) tenancy.

**Desired outcome:** Optimize costs
by thoroughly evaluating Microsoft SQL Server licensing options on
AWS, including both the license-included model for on-demand usage
and the Bring Your Own License (BYOL) approach for either Amazon EC2
Dedicated Hosts or default shared tenancy, ensuring that the chosen
licensing strategy aligns with compliance requirements, maximizes
cost savings, and effectively supports business objectives through
AWS's flexible licensing framework.

**Common anti-patterns:**

- Automatically defaulting to license-included instances without
analyzing BYOL cost benefits, potentially missing out on
significant savings from existing Microsoft Enterprise
Agreements or Software Assurance benefits that could be
leveraged on AWS.
- Failing to properly track and document SQL Server deployments
across different AWS environments, leading to over-provisioned
licenses or compliance risks from unintentionally running SQL
Server workloads on shared tenancy when BYOL requires dedicated
hosts.
- Choosing licensing models based solely on immediate costs
without considering long-term implications, such as selecting
on-demand licensing when workloads are actually stable and
predictable, resulting in higher total cost of ownership
compared to BYOL options.

**Benefits of establishing this best
practice:**

- Significant Cost Optimization: By carefully evaluating and
implementing the most appropriate licensing model (BYOL versus
license-included), organizations can achieve substantial cost
savings through efficient license utilization, maximizing
existing investments in Microsoft agreements, and aligning
licensing costs with actual usage patterns.
- Enhanced Compliance and Risk Management: Proper licensing
practices ensure continuous compliance with Microsoft's
licensing terms and AWS's infrastructure requirements, reducing
the risk of audit findings, unexpected true-up costs, and
potential penalties while maintaining clear documentation of
license deployment and usage.
- Improved Operational Flexibility: Understanding and implementing
the right licensing strategy enables organizations to scale
their SQL Server workloads more effectively, choose the most
cost-effective deployment options (dedicated hosts versus shared
tenancy), and maintain the agility to adjust licensing
approaches as business needs evolve.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

To implement effective Microsoft SQL Server licensing on AWS,
start by inventorying existing licenses and analyzing workload
patterns to determine the most cost-effective option between BYOL
and license-included models. Establish clear documentation and
tracking processes using AWS License Manager, and implement
regular reviews to optimize costs while maintaining compliance
with both Microsoft and AWS requirements.

### Implementation steps

- Conduct a comprehensive inventory of existing SQL Server
licenses and associated rights (AWS OLA can be useful as
well).
- Analyze workload characteristics and usage patterns to
determine the most cost-effective licensing model (BYOL
versus license-included).
- Set up AWS License Manager to track and manage SQL Server
deployments across your AWS environment.
- Implement a tagging strategy to accurately monitor and
allocate SQL Server licensing costs.
- Establish a regular review process to optimize licensing
strategy and ensure ongoing compliance with Microsoft and
AWS requirements.

## Resources

**Related documents:**

- [Understand
SQL Server licensing](https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/sql-server-licensing.html)
- [Amazon Web Services and Microsoft FAQs](https://aws.amazon.com/windows/faq/)

**Related tools:**

- [What
is AWS License Manager?](https://docs.aws.amazon.com/license-manager/latest/userguide/license-manager.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftcost03-bp01.html*

---

# MSFTCOST03-BP02 Consolidate Microsoft SQL Server instances

A SQL instance is part of the SQL Server Database Engine, that
provides the SQL service to clients or applications. It is common to
have SQL instances installed per server when it comes to large
production environments, to avoid resources issues and to follow
resource governance. Although, for smaller or non-critical workloads
organizations can leverage shared resources and have multiple SQL
instances installed on the same server or set of servers. This
approach will help your workload save costs on SQL licensing (less
cores running SQL) and often in compute resources as well.

**Desired outcome:** Optimize costs
and resource utilization by strategically consolidating Microsoft
SQL Server instances, particularly for smaller or non-critical
workloads. This approach aims to reduce SQL licensing expenses by
minimizing the number of cores running SQL Server, while also
potentially decreasing overall compute resource consumption. By
carefully assessing workload requirements and identifying
consolidation opportunities, organizations can achieve significant
cost savings without compromising performance for mission-critical
applications.

**Common anti-patterns:**

- Over-isolation: Deploying separate SQL Server instances for
every application or workload, regardless of size or
criticality, leading to unnecessary licensing costs and
underutilized resources.
- Indiscriminate consolidation: Merging SQL Server instances
without proper assessment of workload characteristics, resource
requirements, and potential conflicts, resulting in performance
degradation and operational issues for critical applications.

**Benefits of establishing this best
practice:**

- Reduced Licensing Costs: By consolidating multiple SQL Server
instances, particularly those running on less than 4 vCPUs,
organizations can significantly reduce licensing expenses since
SQL Server requires licensing for a minimum of 4 vCPUs per
instance regardless of actual usage.
- Optimized Resource Utilization: Consolidation enables more
efficient use of compute resources by sharing infrastructure
across multiple workloads, reducing the total number of servers
required and decreasing overall infrastructure costs.
- Simplified Management Overhead: Fewer SQL Server instances mean
reduced administrative effort for maintenance, patching, backup
management, and monitoring, leading to operational efficiency
and lower management costs.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

To implement SQL Server instance consolidation, assess workload
patterns and resource requirements to identify compatible
instances for merging, prioritizing non-critical workloads and
especially targeting instances with less than 4 vCPUs since SQL
Server requires licensing for a minimum of 4 vCPUs regardless of
actual usage. Use AWS migration tools for consolidation, implement
resource governance for effective management, and maintain regular
performance monitoring to ensure optimal efficiency while reducing
licensing costs.

### Implementation steps

- Conduct a comprehensive assessment of existing SQL Server
instances, identifying workloads using less than 4 vCPUs and
evaluating resource usage patterns, performance
requirements, and compatibility.
- Create a consolidation plan that groups compatible
workloads, prioritizing non-critical applications and
instances that can share resources without performance
impact.
- Implement database migrations between instances as needed,
leveraging AWS Database Migration Service to facilitate the
process.
- Establish monitoring and review processes to track
performance metrics, resource utilization, and cost savings
of the consolidated environment.

## Resources

**Related documents:**

- [Consolidate
instances](https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/consolidate-instances.html)

**Related tools:**

- [AWS Database Migration Service](https://aws.amazon.com/dms/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftcost03-bp02.html*

---

# MSFTCOST03-BP03 Check if your workload is running with the right SQL Server edition

Microsoft offers types of SQL Server editions, with a different set
of features and license cost. The Enterprise edition provides data
center capabilities with high performance, unlimited virtualization,
and several business intelligence tools. The Standard edition
provides basic data management and business intelligence for smaller
organizations and departments. The Web edition is suitable for
companies that are web hosts or web value added providers (VAPs) and
it should only be used to support public and internet accessible
webpages, websites, and web services; its license does not allow the
use for line-of-business applications. The Developer edition
includes all functionality of the Enterprise edition, but it is
intended for development purposes only. And the Express edition is a
free database that can be used for learning or for building desktop
applications. Over the release of SQL versions, Microsoft has added
more features to the Standard edition, and it is not so unusual to
see customers evaluating the downgrade from the Enterprise edition
to the Standard one.

**Desired outcome:** The workload
should run on the most cost-effective SQL Server edition that meets
its functional and performance requirements. After evaluating
feature usage, performance needs, and licensing costs across
available editions (Enterprise, Standard, Web, Developer, and
Express), the organization can confirm they are using the optimal
edition or identify opportunities to downgrade to a more
cost-effective edition without compromising workload functionality
or performance targets.

**Common anti-patterns:**

- Enterprise by Default: Automatically deploying SQL Server
Enterprise edition for all database workloads without analyzing
actual feature requirements, resulting in unnecessary licensing
costs for workloads that could run effectively on Standard or
Web editions.
- Feature Underutilization: Paying for Enterprise edition licenses
but only using features available in lower editions, such as
using Enterprise solely for basic OLTP workloads without
leveraging advanced features like in-memory OLTP, partitioning,
or advanced security features.

**Benefits of establishing this best
practice:**

- Cost Optimization: Significant cost savings through appropriate
edition selection, particularly when downgrading from Enterprise
to Standard edition where feasible. This can result in
significant reduction in licensing costs while maintaining
necessary functionality for workloads that do not require
Enterprise-specific features.
- Resource Efficiency: Better alignment of database capabilities
with actual workload requirements, ensuring resources are
allocated efficiently and preventing overprovisioning of
features that aren't being utilized. This leads to more
streamlined database management and reduced operational
overhead.
- Compliance and Risk Management: Appropriate edition selection
ensures compliance with licensing terms—particularly critical
for Web edition restrictions—while maintaining suitable feature
sets for different environments. This reduces both compliance
risks and potential audit findings.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Conduct a thorough assessment of your SQL Server workloads using
built-in monitoring tools to identify actual feature usage and
performance requirements. Compare these against available edition
features and costs, using AWS Prescriptive Guidance to evaluate
potential downgrades. Test thoroughly in non-production
environments before implementing any edition changes, and
establish a regular review process to ensure ongoing optimization.

### Implementation steps

- Audit current SQL Server workloads for feature usage and
performance requirements using proper tools or scripts.
- Compare workload needs against features available in
different SQL Server editions, using AWS Prescriptive
Guidance for potential downgrade scenarios.
- Test workload performance on proposed new editions in
non-production environments to validate functionality and
performance.
- Implement edition changes in a phased approach, starting
with non-critical workloads, and establish a regular review
process for ongoing edition optimization.

## Resources

**Related documents:**

- [Compare
SQL Server editions](https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/sql-server-editions.html)
- [Evaluate
downgrading Microsoft SQL Server from Enterprise edition to
Standard edition on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/evaluate-downgrading-sql-server-edition/welcome.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftcost03-bp03.html*

---

# MSFTCOST03-BP04 Evaluate SQL Server Developer edition

SQL Server Developer edition includes all functionality of the
Enterprise edition. It is a free edition that can be used in
non-production environments. A production environment is defined as
an environment that is accessed by the end users of an application
(for example, a website) and is used for more than gathering
feedback or acceptance testing of that application. The Developer
edition can be leveraged for development and testing your workload.

**Desired outcome:** By evaluating
and implementing SQL Server Developer edition in non-production
environments, the organization aims to reduce licensing costs while
maintaining full Enterprise edition functionality for development
and testing purposes. This change will optimize costs without
compromising the ability to develop and test workloads effectively,
ensuring that production environments remain properly licensed while
development environments leverage the free Developer edition.

**Common anti-patterns:**

- Using SQL Server Developer edition in production environments to
save costs, exposing the organization to licensing compliance
issues and violating Microsoft's terms of use while putting
end-user applications at risk.
- Maintaining Enterprise edition licenses across all development
and testing environments without evaluating Developer edition
alternatives, resulting in unnecessary licensing costs and
inefficient resource allocation for non-production workloads.

**Benefits of establishing this best
practice:**

- Significant cost savings: By implementing SQL Server Developer
edition in non-production environments, organizations can
substantially reduce licensing costs, as Developer edition is
free for use in development and testing scenarios.
- Full feature access for development: Teams gain access to all
Enterprise edition features in their development and testing
environments, ensuring that they can build and test applications
using the full range of SQL Server capabilities without
incurring additional costs.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Identify non-production SQL Server instances, create a migration
plan for downgrading to Developer edition, and implement controls
to ensure Developer edition is only used in development and
testing environments while maintaining proper licensing
compliance.

### Implementation steps

- Inventory all SQL Server instances, identifying
non-production environments.
- Develop a migration plan for downgrading eligible instances
to Developer edition.
- Implement the downgrade process following AWS documentation.
- Test applications thoroughly in the downgraded environments.
- Implement controls and monitoring to prevent Developer
edition use in production.

## Resources

**Related documents:**

- [Evaluate
SQL Server Developer edition](https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/sql-server-dev.html)
- [How
to manually downgrade SQL Server Enterprise edition to
Developer edition on AWS and save on licensing costs](https://aws.amazon.com/blogs/modernizing-with-aws/how-to-manually-downgrade-sql-server-enterprise-edition-to-developer-edition-on-aws-and-save-on-licensing-costs/)
- [Automate
downgrading SQL Server to Developer edition on Amazon EC2](https://aws.amazon.com/blogs/modernizing-with-aws/how-to-automate-downgrading-sql-server-to-developer-edition-on-amazon-ec2/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftcost03-bp04.html*

---

# MSFTCOST03-BP05 Evaluate SQL Server on Linux

Beginning on SQL Server 2017, Microsoft offers the option to run SQL
Server on Linux operating systems. SQL Server on Linux is enterprise
ready and offers flexibility, high performance, security features,
reduced TCO, HA/DR features, and a great user experience. You can
switch from SQL Server on Windows Server to SQL Server on Linux to
save on Windows Server licensing costs.

**Desired outcome:** Successfully
migrate compatible SQL Server workloads from Windows Server to
Linux, resulting in reduced Total Cost of Ownership (TCO) through
elimination of Windows Server licensing costs. This migration would
maintain enterprise-level performance, security, and high
availability features while leveraging the flexibility of SQL Server
on Linux, ultimately optimizing costs for Microsoft workloads in the
organization's IT infrastructure.

**Common anti-patterns:**

- Automatic Migration Without Compatibility Assessment:
Organizations hastily migrating SQL Server workloads to Linux
without first evaluating compatibility, resulting in application
failures, performance issues, and potential data loss due to
unsupported features or incompatible dependencies.
- Ignoring Total Cost of Operation: Companies focusing solely on
the potential licensing cost savings of moving to SQL Server on
Linux, while overlooking other operational costs such as
retraining staff, modifying existing scripts and tools, and
potential performance tuning needed in the new environment. This
narrow focus may lead to unexpected expenses and operational
challenges that offset the intended cost savings.

**Benefits of establishing this best
practice:**

- Cost Optimization: Elimination of Windows Server licensing fees
significantly reduces Total Cost of Ownership (TCO), enabling
better resource allocation across the organization.
- Simplified Cross-Platform Management: Standardization of
database management across Windows and Linux platforms reduces
complexity and streamlines operational processes.

**Level of risk exposed if this best practice
is not established:** Low

## Implementation guidance

To implement SQL Server on Linux evaluation, start with a
comprehensive workload compatibility assessment. Create a detailed
migration plan including testing and rollback procedures. Conduct
a pilot migration on a non-critical workload. Train IT staff on
Linux and SQL Server on Linux management. Implement the full
migration in stages, closely monitoring performance and
functionality throughout to ensure a smooth transition and achieve
cost savings and management simplification.

### Implementation steps

- Conduct workload compatibility assessment to identify SQL
Server instances suitable for Linux migration, reviewing
feature requirements and dependencies
- Develop migration plan with testing procedures, success
metrics, and rollback strategy, including pilot test
selection
- Implement pilot migration on selected non-critical workload
while providing Linux administration training to IT staff
- Implement phased migration of remaining workloads following
successful pilot, with continuous monitoring of performance
and costs

## Resources

**Related documents:**

- [Evaluate
SQL Server on Linux](https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/sql-server-linux.html)
- [Editions
and supported features of SQL Server 2022 on Linux](https://learn.microsoft.com/en-us/sql/linux/sql-server-linux-editions-and-components-2022?view=sql-server-ver16)

**Related tools:**
[Windows
to Linux replatforming assistant for Microsoft SQL Server
Databases](https://docs.aws.amazon.com/sql-server-ec2/latest/userguide/replatform-sql-server.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftcost03-bp05.html*

---

# MSFTCOST03-BP06 Evaluate Optimize CPU feature

Optimize CPUs for Amazon EC2 Instances provides customers greater
control of your EC2 instances on two fronts. First, you can specify
a custom number of vCPUs to save on vCPU-based licensing costs (such
as SQL Server). Second, you can disable multithreading for workloads
that perform well with single-threaded CPUs, like certain
high-performance computing (HPC) applications. Reducing the number
of vCPUs or disabling multithreading offers fewer cores to your SQL
Server workload on EC2 without affecting the other compute resources
available to the machine (such as RAM and storage), and most of the
time without compromising the workload performance. This feature is
available for both Bring Your Own License (BYOL) and License
Included (LI) deployments.

**Desired outcome:** By evaluating
and implementing CPU optimization for Amazon EC2 instances, we aim
to reduce vCPU-based licensing costs for SQL Server while
maintaining workload performance. This will be achieved by
specifying custom vCPU counts and, where appropriate, disabling
multithreading. The outcome will be a more cost-effective
utilization of resources, particularly for SQL Server workloads,
without compromising on performance or available compute resources
such as RAM and storage.

**Common anti-patterns:**

- Over-provisioning vCPUs: Organizations often provision EC2
instances with more vCPUs than necessary for their SQL Server
workloads, believing that more is better. This leads to
unnecessarily high licensing costs for vCPU-based software like
SQL Server, without providing any tangible performance benefits.
The excess vCPUs remain unused while still incurring licensing
fees.
- Ignoring multithreading optimization: Many teams leave
multithreading enabled by default for all workloads, including
those that do not benefit from it (such as certain HPC
applications or single-threaded workloads). This can result in
suboptimal performance for these specific workloads and
potentially higher licensing costs, as some software is licensed
per logical processor rather than physical core.

**Benefits of establishing this best
practice:**

- Reduced SQL Server licensing costs through optimized vCPU
allocation and core usage, resulting in direct cost savings.
- Better workload performance by matching CPU configurations to
specific needs, especially for single-threaded applications and
HPC workloads.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Start by analyzing your SQL Server workload performance and
resource utilization. Use AWS tools like CloudWatch to gather
metrics. Identify instances where you can reduce vCPU count
without impacting performance. Set instances with custom vCPU
counts to match your licensing. Test disabling multithreading for
workloads that benefit from single-threaded performance. Monitor
performance closely after changes to ensure workload efficiency is
maintained. Regularly review and adjust your configurations as
workload demands evolve.

### Implementation steps

- Analyze current SQL Server workload performance and resource
utilization using AWS CloudWatch and other monitoring tools.
- Set EC2 instances with custom vCPU counts that align with
your SQL Server licensing and workload requirements.
- Test and implement multithreading disablement for workloads
that perform better with single-threaded CPUs, monitoring
performance before and after the change.

## Resources

**Related documents:**

- [CPU
options for Amazon EC2 instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-optimize-cpu.html)
- [Optimize
CPUs for License-Included instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/optimize-cpu.html)
- [Optimize
CPU best practices for SQL Server workloads](https://aws.amazon.com/blogs/modernizing-with-aws/optimize-cpu-best-practices-for-sql-server-workloads/)
- [Optimize
CPUs best practices for SQL Server workloads –
continued](https://aws.amazon.com/blogs/modernizing-with-aws/optimize-cpus-best-practices-for-sql-server-workloads-continued/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftcost03-bp06.html*

---
