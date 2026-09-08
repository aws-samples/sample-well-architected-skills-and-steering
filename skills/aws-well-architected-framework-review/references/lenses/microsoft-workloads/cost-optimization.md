# Cost Optimization

**Pillar**: Cost Optimization  
**Questions**: 8

---

# MSFTCOST01 — Assessment

**Pillar**: Cost Optimization  
**Best Practices**: 3

---

# MSFTCOST01-BP01 Run discovery tools

Migration Evaluator is a migration assessment service that helps you
create a directional business case for AWS cloud planning and
migration. The information that the AWS Migration Evaluator collects
includes server profile information (for example, OS, number of
CPUs, amount of RAM), SQL Server metadata (for example, version and
edition), utilization metrics, and network connections. AWS
Application Discovery Service helps you plan cloud migration
projects, by gathering information about your on-premises data
centers. It discovers the connections between applications and
servers to uncover unknown servers, better understand dependencies,
and establish move groups.

**Desired outcome:** Gain
comprehensive visibility into your infrastructure environment by
collecting detailed server profiles, SQL Server configurations,
utilization patterns, and application dependencies to create an
accurate business case for cloud migration and optimize resource
planning.

**Common anti-patterns:**

- Relying on manual inventory tracking and documentation, leading
to incomplete or outdated infrastructure information and missed
optimization opportunities.
- Making migration decisions based solely on static server
specifications without considering actual utilization patterns
and application dependencies.
- Planning cloud migrations in isolation without understanding the
full scope of application relationships, resulting in overlooked
servers and disrupted service connections.

**Benefits of establishing this best
practice:**

- Accurate cost projections and resource planning through
automated discovery of server configurations, SQL Server
metadata, and utilization metrics.
- Reduced migration risks by identifying hidden dependencies and
establishing appropriate move groups based on discovered
application connections.
- Optimized infrastructure spend by right-sizing resources based
on actual utilization patterns rather than assumptions or
outdated documentation.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Implementing comprehensive infrastructure discovery through tools
like AWS Migration Evaluator and AWS Application Discovery Service
is crucial for successful cloud migrations and cost optimization.
These tools automatically collect detailed information about
server configurations, SQL Server deployments, resource
utilization, and application dependencies, replacing error-prone
manual tracking methods. This automated approach not only provides
accurate data for building business cases and planning migrations
but also helps organizations avoid the common pitfalls of
oversizing resources or missing critical application connections,
ultimately leading to more successful and cost-effective cloud
deployments.

### Implementation steps

- Deploy AWS Application Discovery Agent on target servers or
configure AWS Application Discovery Agentless Collector for
VMware environments
- Enable data collection in AWS Migration Hub
- Monitor and analyze collected data, including server
profiles, utilization patterns, and application dependencies
- Generate reports and recommendations for migration business
case, infrastructure requirements, migration waves, and
resource optimization strategies

## Resources

**Related documents:**

- [Discover
on-premises resources using AWS Migration Hub discovery
tools](https://docs.aws.amazon.com/migrationhub/latest/ug/gs-new-user-discovery.html)

**Related tools:**

- [Migration
Evaluator](https://aws.amazon.com/migration-evaluator/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftcost01-bp01.html*

---

# MSFTCOST01-BP02 Run assessment tools

AWS Optimization and Licensing Assessment (OLA) is a complimentary
program for new and existing customers to assess and optimize
current on-premises and cloud environments, based on actual resource
utilization, third-party licensing, and application dependencies.

**Desired outcome:** The desired
outcome of an AWS OLA is to significantly reduce costs and improve
efficiency in both on-premises and cloud environments by optimizing
resource utilization, streamlining third-party licensing, and
understanding application dependencies, resulting in a more
cost-effective and agile IT infrastructure aligned with business
needs.

**Common anti-patterns:**

- Overprovisioning resources based on peak usage estimates rather
than actual utilization data, leading to unnecessary costs and
wasted capacity across both on-premises and cloud environments.
- Maintaining duplicate or redundant software licenses without
understanding application dependencies and actual usage
patterns, resulting in excessive licensing costs and complicated
compliance management.

**Benefits of establishing this best
practice:**

- Immediate cost reduction through the elimination of
underutilized resources and redundant licensing, delivering
significant savings on cloud and software spending.
- Enhanced operational efficiency through data-driven decision
making, enabling better capacity planning and resource
allocation based on actual usage patterns rather than
assumptions.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

To implement an AWS OLA, form a cross-functional team and collect
comprehensive utilization data across all environments. Document
software licenses and map application dependencies. Develop a
prioritized optimization plan addressing immediate opportunities
like resource right-sizing and license consolidation, followed by
long-term strategic initiatives. Establish regular review cycles
to ensure continuous optimization and alignment with business
goals.

### Implementation steps

- Contact your AWS account manager or AWS Sales
- Schedule an initial discovery meeting
- Sign the OLA agreement
- Provide access to required systems and data
- Participate in data collection and assessment workshops
- Review preliminary findings with AWS team
- Receive and analyze final OLA report
- Develop action plan based on recommendations
- Schedule follow-up meetings for implementation support
- Implement optimization strategies with AWS guidance

## Resources

**Related documents:**

- [AWS Optimization and Licensing Assessment](https://aws.amazon.com/optimization-and-licensing-assessment/)
- [AWS Prescriptive Guidance - OLA](https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/aws-ola.html)
- [How
to optimize costs for Microsoft workloads on AWS](https://aws.amazon.com/blogs/modernizing-with-aws/how-to-optimize-costs-for-microsoft-workloads-on-aws/)
- [Reduce
software licensing costs with an AWS Optimization and
Licensing Assessment](https://aws.amazon.com/blogs/mt/reduce-software-licensing-costs-with-an-aws-optimization-and-licensing-assessment/)

**Related videos:**

- [AWS re:Invent 2022 - How to save costs and optimize Microsoft
workloads on AWS (ENT205)](https://www.youtube.com/watch?v=Zyhd2FmdtJs)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftcost01-bp02.html*

---

# MSFTCOST01-BP03 Run platform-specific tools

Platform-specific tools, such as Azure Resource Discovery Tool, are
useful for environment understanding. This is a PowerShell script
provided by AWS that generates an inventory report including
detailed metrics of an Azure environment to which you have read
access for the previous 30 days. Especially useful for non-virtual
machine(VM) resources.

**Desired outcome:** Generate a
comprehensive 30-day inventory report using platform-specific tools
to provide detailed resource metrics, asset visibility, and usage
patterns across the Azure environment, enabling informed decisions
for cloud resource management and optimization, while documenting
key metrics that would be essential for planning a potential AWS
migration.

**Common anti-patterns:**

- Manual Resource Tracking: Relying solely on manual methods or
spreadsheets to track cloud resources and their usage, instead
of leveraging automated platform-specific tools. This approach
is error-prone, time-consuming, and often results in incomplete
or outdated information about the environment.
- One-Size-Fits-All: Using generic assessmetn tools that are not
tailored to the specific cloud platform (in this case, Azure).
This can lead to missed insights, inability to capture
platform-specific metrics, and incomplete understanding of
resource utilization and costs, especially for non-VM resources
that may have unique characteristics in Azure.

**Benefits of establishing this best
practice:**

- Comprehensive Resource Visibility: Platform-specific tools
provide detailed, accurate insights into all resources within
the Azure environment, including often overlooked non-VM
resources. This comprehensive view enables better resource
management, cost optimization, and capacity planning.
- Time and Effort Efficiency: Automated platform-specific tools
can quickly generate detailed reports that would take
significantly longer to compile manually. This efficiency allows
IT teams to focus on analyzing the data and making strategic
decisions rather than spending time on data collection and
organization.

**Level of risk exposed if this best practice
is not established:** Low

## Implementation guidance

To implement this best practice, start by identifying and
selecting appropriate platform-specific tools for Azure, such as
Resource Discovery. Ensure you have the necessary read permissions
across your Azure environment. Schedule regular automated runs of
these tools, ideally on a monthly basis, to capture a rolling
30-day window of resource utilization. Set up a process to review
and analyze the generated reports, focusing on resource
allocation, usage patterns, and potential optimization
opportunities. Integrate these insights into your cloud management
and decision-making processes, and use the data to inform capacity
planning, cost optimization strategies, and potential migration
assessments. Regularly update and refine your use of these tools
as your Azure environment evolves and as new features become
available.

### Implementation steps

- Verify the required access permissions across all target
Azure subscriptions and resource groups
- Install and configure the chosen platform-specific tool (for
example, Azure Resource Discovery Tool)
- Save the output data
- Contact your AWS account team to help analyzing Azure
resources in preparation for potential AWS migration
scenarios

## Resources

**Related tools:**

- [Azure
Resource Discovery Tool](https://github.com/awslabs/resource-discovery-for-azure)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftcost01-bp03.html*

---

# MSFTCOST02 — Operating system

**Pillar**: Cost Optimization  
**Best Practices**: 3

---

# MSFTCOST02-BP01 Right size Windows instances

AWS Compute Optimizer uses machine learning to analyze the
performance metrics and utilization patterns of Microsoft workloads
running on AWS, including Windows Server instances and SQL Server
deployments. By examining historical resource usage data across CPU,
memory, and network dimensions, Compute Optimizer provides tailored
recommendations for right-sizing EC2 instances running Microsoft
applications, helping organizations optimize both performance and
cost. The service can identify when Windows workloads are
over-provisioned or under-provisioned, suggesting instance types
that are aligned with actual resource requirements. This is valuable
for Microsoft-heavy enterprises that have migrated to AWS, as
Windows workloads often have different resource consumption patterns
and proper sizing is crucial for managing the additional licensing
costs associated with Windows Server and SQL Server instances.

**Desired outcome:** Optimize
Microsoft workload deployments on AWS to substantially reduce
compute costs while maintaining or improving application performance
through right-sized instances, resulting in lower Windows licensing
fees and improved resource utilization metrics across CPU, memory,
and network resources as validated by AWS Compute Optimizer
recommendations.

**Common anti-patterns:**

- Deploying Microsoft workloads on the largest available EC2
instance types as a precautionary measure regardless of actual
resource requirements, leading to severe over-provisioning and
unnecessary Windows licensing costs for unused capacity.
- Ignoring AWS Compute Optimizer's recommendations and maintaining
static instance sizes based on initial deployment
configurations, even when utilization metrics consistently show
periods of low resource usage or performance bottlenecks that
indicate the need for right-sizing.

**Benefits of establishing this best
practice:**

- Cost Efficiency: Organizations can eliminate resource waste by
precisely matching instance types to actual workload
requirements, reducing both EC2 instance costs and associated
Microsoft licensing fees which are typically tied to instance
size and processor count.
- Performance Optimization: Workloads receive the right balance of
compute resources, preventing both performance bottlenecks from
under-provisioning and excess capacity from over-provisioning,
leading to consistent and reliable application performance for
end users.
- Data-Driven Decision Making: IT teams can make instance sizing
decisions based on machine learning-analyzed historical
performance data rather than guesswork, reducing the operational
overhead of manual monitoring and enabling proactive capacity
planning for Microsoft workloads.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

This implementation guide provides a high-level approach to
leveraging AWS Compute Optimizer for Microsoft workload
optimization on AWS. By following these best practices,
organizations can establish a systematic process for analyzing and
right-sizing their Windows-based instances while ensuring optimal
performance and cost efficiency. The guide covers essential steps
from initial Compute Optimizer activation and baseline assessment
through to ongoing monitoring and adjustment phases. Whether you
are running Windows Server applications, SQL Server databases, or
other Microsoft workloads, these recommendations will help you
implement a data-driven optimization strategy that aligns with
both AWS architectural principles and Microsoft licensing
considerations.

### Implementation steps

- Enable AWS Compute Optimizer and verify data collection
across accounts
- Create inventory of Microsoft workloads and licenses
- Define performance baselines and thresholds for each
workload type
- Review initial optimization recommendations after 14-day
analysis period
- Create prioritized migration schedule for instance
right-sizing
- Execute instance changes during maintenance windows
- Set up automated monitoring and reporting

## Resources

**Related documents:**

- [Right
size Windows workloads](https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/rightsize.html)
- [Reduce
Microsoft SQL Server licensing costs with AWS Compute Optimizer](https://aws.amazon.com/blogs/modernizing-with-aws/reduce-microsoft-sql-server-licensing-costs-with-aws-compute-optimizer/)
- [Optimizing
your cost with rightsizing recommendations](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-rightsizing.html)

**Related tools:**

- [AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftcost02-bp01.html*

---

# MSFTCOST02-BP02 Automate stop and start schedules

Leverage the Instance Scheduler on AWS to reduce the use of Amazon EC2 and Amazon Relational Database Service instances that do not
need to run continuously. The Instance Scheduler helps reduce
operational costs by stopping and starting resources as needed.

**Desired outcome:** Achieve
significant cost reduction in non-production environments by
implementing automated start/stop schedules for EC2 instances and
RDS databases that are only required during business hours (for
example, 8 AM - 6 PM on weekdays), while ensuring zero impact to
business operations and development activities during working hours.

**Common anti-patterns:**

- Always-On Resources: Keeping all development, testing, and
staging environments running 24/7, even when they're not
actively used, resulting in unnecessary costs and resource
waste.
- Manual Start/Stop Management: Relying on developers or
operations teams to manually start and stop instances based on
their work schedules, leading to inconsistent resource
management, potential delays in availability, and increased risk
of human error.

**Benefits of establishing this best
practice:**

- Cost Optimization: Significant reduction in operational costs by
automatically shutting down non-essential resources during
off-hours, weekends, and holidays, directly impacting the
organization's cloud spending.
- Operational Efficiency: Elimination of manual intervention for
resource management, allowing IT teams to focus on more
strategic tasks while ensuring consistent and reliable resource
availability when needed.
- Environmental Impact: Reduced energy consumption and carbon
footprint by minimizing unnecessary compute resource usage,
supporting organizational sustainability goals and responsible
cloud computing practices.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Begin by identifying and tagging non-production resources suitable
for automated scheduling. Configure AWS Instance Scheduler with
appropriate start/stop periods aligned with business hours and
team schedules. Implement a gradual rollout strategy, starting
with a small subset of resources to validate functionality.
Establish monitoring mechanisms to track schedule execution and
create override procedures for exceptional situations.

### Implementation steps

- Identify and tag non-production resources for scheduling
- Install and configure AWS Instance Scheduler
- Define business hours and create scheduling periods
- Test schedule on pilot group of resources
- Monitor and validate functionality
- Roll out to remaining resources

## Resources

**Related documents:**

- [Automate
stop and start schedules](https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/windows-ec2-schedules.html)

**Related tools:**

- [Instance
Scheduler on AWS](https://aws.amazon.com/solutions/implementations/instance-scheduler-on-aws/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftcost02-bp02.html*

---

# MSFTCOST02-BP03 Bring Your Own Licenses (BYOL)

If you have already invested in licenses for your Microsoft
workload, such as having enterprise licensing agreements, you can
choose to bring your own licenses to AWS and save costs on EC2.
Depending on when the licenses were acquired and the version,
Windows Server licenses can be brought to Amazon EC2 Dedicated
Hosts. Other products covered by Software Assurance and License
Mobility in the agreement, like SQL Server, can be brought to
default (shared) tenancy.

AWS License Manager provides the flexibility to convert between
Bring Your Own License (BYOL) and License Included configurations,
allowing you to optimize licensing costs based on your needs and
eligibility. This conversion capability enables you to switch
between license models without having to rebuild instances, making
it easier to adapt to changing licensing requirements or to take
advantage of different cost models. For more information on
licensing options, see the Microsoft FAQ on the AWS public page, or
contact your account team to help you engage with a Microsoft expert
on AWS to guide you through the options.

**Desired outcome:** Successfully
optimize costs and maintain compliance by leveraging existing
Microsoft licenses through BYOL implementation on AWS, while
ensuring seamless license management and flexibility to convert
between license models as needed, resulting in documented cost
savings and efficient resource utilization without service
disruption.

**Common anti-patterns:**

- Misaligned license deployment: Incorrectly deploying Windows
Server licenses on shared tenancy instead of required Dedicated
Hosts, or placing SQL Server with software assurance on
Dedicated Hosts when it could run on shared tenancy, resulting
in unnecessary costs and compliance violations.
- Missed conversion opportunities: Failing to utilize AWS License Manager's conversion capabilities between BYOL and license
included configurations, leading to unnecessary instance
rebuilds and downtime when licensing requirements change or cost
optimization opportunities arise.
- Independent license decision-making: Making BYOL decisions
without consulting AWS account teams or Microsoft licensing
experts, resulting in missed opportunities for cost savings,
improper license mobility implementation, and potential
compliance issues with enterprise agreements.

**Benefits of establishing this best
practice:**

- By leveraging existing Microsoft licenses through BYOL,
organizations can significantly reduce EC2 instance costs
compared to License Included options. This maximizes the value
of existing enterprise licensing agreements and allows for more
efficient allocation of IT budgets.
- AWS License Manager's ability to convert between BYOL and
License Included configurations provides unprecedented
flexibility. This allows organizations to adapt quickly to
changing business needs, licensing requirements, or cost
structures without service interruptions or time-consuming
instance rebuilds.
- Properly implementing BYOL with guidance from AWS and Microsoft
experts ensures compliance with complex licensing terms. This
minimizes the risk of unexpected costs or penalties during
audits, while also ensuring that licenses are correctly applied
to the right types of instances (for example, Windows Server on
Dedicated Hosts, SQL Server on shared tenancy when applicable).

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Start with a comprehensive audit of existing Microsoft licenses,
then engage AWS account teams for expert guidance on BYOL
implementation. Deploy AWS License Manager to track and manage
licenses, ensuring proper instance placement (Dedicated Hosts
versus shared tenancy) based on license terms. Regularly review
and optimize configurations, maintaining thorough documentation
for compliance purposes.

### Implementation steps

- Audit existing Microsoft licenses and enterprise agreements
- Consult AWS and Microsoft experts for BYOL eligibility and
options
- Set up AWS License Manager for tracking and conversion
capabilities
- Deploy licenses correctly (for example, Windows Server on
Dedicated Hosts, SQL Server on shared tenancy)
- Establish regular review process for ongoing optimization
and compliance

## Resources

**Related documents:**

- [Amazon Web Services and Microsoft FAQs](https://aws.amazon.com/windows/faq/)
- [Bring
licenses for Windows and SQL Server workloads](https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/byol-ded-hosts.html)

**Related tools:**

- [What
is AWS License Manager?](https://docs.aws.amazon.com/license-manager/latest/userguide/license-manager.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftcost02-bp03.html*

---

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

# MSFTCOST04 — Databases

**Pillar**: Cost Optimization  
**Best Practices**: 3

---

# MSFTCOST04-BP01 Use caching to enhance SQL Server workloads

Caching in .NET applications reduces costs and improves performance
by storing frequently accessed data, lowering the load on backend
databases like SQL Server. While especially useful for read-heavy
operations, choose a caching method that fits your needs,
considering that local caching has scalability limitations. Evaluate
the trade-off between performance gains and caching costs when
implementing your strategy.

**Desired outcome:** Implement an
effective caching strategy for our .NET applications with SQL Server
backends to reduce database load, cut costs, and improve
performance. This tailored approach will optimize workloads and
initiate our application modernization efforts, balancing
performance gains with implementation costs.

**Common anti-patterns:**

- Over-Caching: Caching all data indiscriminately without
considering data volatility or access patterns. This leads to
stale data issues, increased memory consumption, and potentially
higher costs than direct database queries would incur.
- Local Cache Sprawl: Implementing isolated local caches across
multiple application instances without a coherent invalidation
strategy, resulting in data inconsistencies, increased
maintenance overhead, and poor scalability in distributed
environments.

**Benefits of establishing this best
practice:**

- Reduced load on SQL Server instances leads to lower database
sizing requirements and decreased infrastructure costs, as fewer
resources are needed to handle the same workload volume.
- Faster application response times through immediate access to
cached data, eliminating repetitive database queries and
reducing network latency for frequently accessed information.

**Level of risk exposed if this best practice
is not established:** Low

## Implementation guidance

Identify frequently accessed, static data for caching. Use
distributed caching solutions like Redis for scalability.
Implement robust cache invalidation to maintain data freshness.
Apply cache-aside pattern for seamless database fallback.
Regularly monitor cache hit rates and performance metrics to
optimize your strategy as your application evolves.

### Implementation steps

- Configure a distributed cache service (like Redis) and
integrate it with your .NET application using appropriate
client libraries and connection strings
- Implement cache-aside pattern in your data access layer,
wrapping database calls with cache checks and updates using
appropriate timeouts and invalidation logic
- Set up monitoring for cache performance metrics (hit rates,
memory usage, latency) using Application Insights or similar
tools to validate and optimize caching effectiveness

## Resources

**Related documents:**

- [Use
caching to reduce database demand](https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/net-caching.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftcost04-bp01.html*

---

# MSFTCOST04-BP02 Consider Babelfish for Amazon Aurora PostgreSQL

Babelfish is an Amazon Aurora PostgreSQL feature that allows SQL
Server client applications to connect directly to PostgreSQL
databases. It works by understanding SQL Server's TDS protocol and
common SQL statements, providing a dedicated endpoint for SQL Server
connections. This functionality enables organizations to migrate
from SQL Server to PostgreSQL while maintaining application
compatibility and minimizing the need for code modifications.

**Desired outcome:** By implementing
Babelfish for Amazon Aurora PostgreSQL, we aim to efficiently
migrate our SQL Server-based applications while minimizing
development effort, reducing migration costs, and maintaining
application compatibility. This will enable a smoother transition to
PostgreSQL without extensive code refactoring.

**Common anti-patterns:**

- Complete rewrite approach: Unnecessarily rewriting entire
applications to migrate from SQL Server to PostgreSQL, instead
of leveraging Babelfish's compatibility features. This approach
often leads to extended project timelines, increased costs, and
potential introduction of new bugs.
- Ignoring dialect differences: Assuming full SQL Server
compatibility and neglecting to test and adjust for specific
T-SQL features not supported by Babelfish. This can result in
unexpected behavior or errors in production after migration.

**Benefits of establishing this best
practice:**

- Reduces costs and complexity by minimizing code changes when
transitioning from SQL Server to PostgreSQL, accelerating the
migration process.
- Enables quick transition to Amazon Aurora PostgreSQL while
maintaining application compatibility, allowing organizations to
leverage cloud benefits with minimal disruption.

**Level of risk exposed if this best practice
is not established:** Low

## Implementation guidance

Begin by identifying SQL Server applications suitable for
Babelfish migration and assess their T-SQL compatibility using the
Babelfish Compass tool. Create a test environment to validate
application functionality with Babelfish-enabled Amazon Aurora
PostgreSQL cluster, focusing on critical database operations and
stored procedures. Implement the migration in phases, starting
with non-critical applications, and maintain detailed
documentation of any required code adjustments or workarounds for
unsupported features.

### Implementation steps

- Assess application compatibility using the Babelfish Compass
tool or the AWS Schema Convertion Tool.
- Set up a Babelfish-enabled Amazon Aurora PostgreSQL cluster
and configure the TDS listener port.
- Modify application connection strings to point to the
Babelfish endpoint instead of the SQL Server instance.
- Test thoroughly, focusing on critical database operations,
stored procedures, and application functionality before
migrating production workloads.

## Resources

**Related documents:**

- [Using
Babelfish for Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish.html)
- [Migrating
a SQL Server database to Babelfish for Aurora
PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-migration.html)
- [Prepare
for Babelfish migration with the AWS SCT assessment
report](https://aws.amazon.com/blogs/database/prepare-for-babelfish-migration-with-the-aws-sct-assessment-report/)

**Related tools:**

- [Babelfish
Compass](https://github.com/babelfish-for-postgresql/babelfish_compass)
- [What
is the AWS Schema Conversion Tool?](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Welcome.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftcost04-bp02.html*

---

# MSFTCOST04-BP03 Consider purpose-built databases

Purpose-built databases are gaining traction among businesses
adopting modern architectures like microservices, as they can
precisely accommodate specific data access patterns. These
databases, whether SQL or NoSQL, offer application teams benefits
like reduced costs, enhanced scalability, and improved resilience.
By selecting the right database for each specific use case, teams
can optimize their data management while leveraging cloud advantages
for more efficient solutions.

**Desired outcome:** By adopting
purpose-built databases tailored to specific workload requirements,
application teams will optimize data management, reduce costs, and
enhance scalability and resilience. This approach will lead to more
efficient cloud-based solutions, whether using SQL or NoSQL
databases, and minimize undifferentiated heavy lifting in database
operations.

**Common anti-patterns:**

- Using a single database technology for all applications and
workloads, regardless of their specific data access patterns or
requirements. This can lead to suboptimal performance,
scalability issues, and increased costs.
- Adopting multiple specialized databases for every minor
variation in data needs, resulting in a fragmented and overly
complex data architecture that increases management overhead and
potentially negates cost savings.

**Benefits of establishing this best
practice:**

- Purpose-built databases are designed to handle specific data
access patterns, resulting in improved query performance and
overall system efficiency tailored to each application's unique
needs.
- By choosing databases that align closely with workload
requirements, organizations can avoid over-provisioning
resources and reduce unnecessary licensing costs associated with
general-purpose database solutions.
- Purpose-built databases often come with built-in features for
horizontal scaling and high availability, making it easier for
applications to handle growth in data volume and user traffic
while maintaining robust performance and reliability.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Begin by analyzing your application's data access patterns, query
requirements, and scalability needs. Identify distinct workload
characteristics across your application portfolio and map them to
appropriate purpose-built database solutions. For new
applications, design the data architecture with these specific
requirements in mind from the start. For existing applications,
consider a phased migration approach, starting with the components
that would benefit most from purpose-built databases. Evaluate AWS
purpose-built database options such as Amazon DynamoDB for
high-performance NoSQL needs, Amazon RDS for traditional
relational workloads, or Amazon Redshift for data warehousing,
ensuring each choice aligns with both technical requirements and
cost optimization goals.

### Implementation steps

- Analyze current data access patterns and requirements across
your application portfolio
- Identify suitable purpose-built database solutions for each
distinct workload
- Develop a migration strategy, prioritizing components that
will benefit most from the change
- Implement and test the new database solutions in a staging
environment
- Gradually migrate production workloads, monitoring
performance and costs throughout the process

## Resources

**Related documents:**

- [Consider
purpose-built databases](https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/net-purpose.html)

**Related tools:**

- [What
is the AWS Schema Conversion Tool?](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Welcome.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftcost04-bp03.html*

---

# MSFTCOST05 — Storage

**Pillar**: Cost Optimization  
**Best Practices**: 4

---

# MSFTCOST05-BP01 Migrate Amazon EBS volumes from gp2 to gp3

General Purpose SSD (gp3) volumes are the latest generation of
General Purpose SSD volumes, and the lowest cost SSD volume offered
by Amazon EBS. This volume type helps to provide the right balance
of price and performance for most applications. It also helps you to
scale volume performance independently of volume size. This means
that you can provision the required performance with no need to
provision additional block storage capacity. Additionally, gp3
volumes offer a 20 percent lower price per GiB than General Purpose
SSD (gp2) volumes.

**Desired outcome:** By migrating
Amazon EBS volumes from gp2 to gp3, we aim to achieve a 20%
reduction in storage costs while gaining the ability to
independently scale volume performance without increasing capacity.
This transition will optimize our storage expenses and provide
better performance control for our workloads, ultimately resulting
in improved cost efficiency without compromising performance
requirements.

**Common anti-patterns:**

- Some organizations maintain large gp2 volumes to achieve higher
IOPS, unnecessarily increasing costs. They fail to recognize
that gp3 volumes allow separate scaling of IOPS and throughput,
potentially leading to significant overspending on storage.
- Some teams might hastily migrate all gp2 volumes to gp3 without
analyzing workload-specific performance needs. This can result
in performance degradation for applications that require higher
baseline performance than what's provided by the default gp3
configuration, leading to potential application issues and the
need for retroactive adjustments.

**Benefits of establishing this best
practice:**

- Immediate 20% reduction in per-GiB storage costs compared to gp2
volumes, leading to significant cost savings across the storage
infrastructure, especially for large-scale deployments with
multiple volumes.
- Independent scaling of IOPS and throughput without increasing
volume size, allowing precise performance tuning based on
application needs while avoiding unnecessary storage capacity
expenses.
- The ability to maintain smaller volume sizes while still
achieving desired performance levels eliminates the need to
overprovision storage for performance reasons, resulting in more
efficient resource utilization and easier capacity management.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Begin by identifying all existing gp2 volumes using AWS Cost Explorer or AWS Systems Manager. Create a phased migration plan,
prioritizing non-production environments first to validate the
performance impact. Use AWS CloudFormation templates or AWS CLI
scripts to automate the modification process, ensuring each
volume's baseline performance requirements are properly configured
during the transition to gp3. Monitor performance metrics through
Amazon CloudWatch before and after migration to verify that
application performance remains optimal. Include snapshot backups
in your migration strategy as a rollback mechanism, and schedule
migrations during low-traffic periods to minimize potential impact
on business operations.

### Implementation steps

- Conduct an inventory analysis using AWS Cost Explorer and
Systems Manager to identify all gp2 volumes, documenting
their current size, IOPS requirements, and associated
workloads.
- Create automated scripts using AWS CLI or Infrastructure as
Code (IaC) to modify volumes from gp2 to gp3, including
proper configuration of baseline IOPS and throughput based
on historical performance data.
- Implement the migration in phases, starting with development
and test environments, followed by non-critical production
workloads, and finally business-critical applications, with
performance validation at each stage.
- Monitor post-migration performance using Amazon CloudWatch
metrics and establish a feedback loop to adjust gp3 volume
configurations as needed, ensuring optimal performance while
maintaining cost savings.

## Resources

**Related documents:**

- [Amazon EBS General Purpose SSD volumes](https://docs.aws.amazon.com/ebs/latest/userguide/general-purpose.html)
- [Migrate
Amazon EBS volumes from gp2 to gp3](https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/ebs-migrate-gp2-gp3.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftcost05-bp01.html*

---

# MSFTCOST05-BP02 Control Amazon EBS volumes or snapshots lifecycle

EBS snapshots are incremental backups stored in S3, saving only
changed blocks since the last snapshot. They can backup unattached
volumes before deletion. Two storage tiers available: Standard
(higher storage cost and free retrieval) and Archive (lower storage
cost and paid retrieval). Managing snapshot lifecycles and removing
unused volumes helps optimize costs.

**Desired outcome:** Implement an
effective EBS volume and snapshot management strategy that
automatically identifies and removes unused volumes while
maintaining cost-efficient snapshot lifecycles across appropriate
storage tiers, resulting in optimized storage costs for Microsoft
workloads on AWS.

**Common anti-patterns:**

- Neglecting to delete unattached EBS volumes: Keeping unused
volumes active, leading to unnecessary ongoing storage costs for
resources that are no longer needed.
- Inconsistent or manual snapshot management: Relying on manual
processes or ad-hoc scripts for creating and managing snapshots,
leading to inconsistent backup coverage, potential data loss,
and inefficient use of storage resources.

**Benefits of establishing this best
practice:**

- By systematically managing EBS volumes and snapshots, you can
significantly reduce storage costs by removing unused resources
and efficiently tiering snapshots based on access needs.
- Regular lifecycle management ensures that your backup strategy
is consistent and up-to-date, reducing the risk of data loss and
maintaining appropriate retention periods for compliance and
disaster recovery purposes.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

To effectively control EBS volume and snapshot lifecycles, start
by implementing automated tools such as AWS Data Lifecycle
Manager. Configure policies to regularly identify and delete
unattached volumes, create consistent snapshot schedules, and
manage snapshot retention across appropriate storage tiers. Use
tags to categorize resources and enable granular control.
Regularly review and adjust your policies to ensure they align
with changing business needs and cost optimization goals.
Implement monitoring and alerting to track resource usage and
potential cost savings opportunities.

### Implementation steps

- Set up AWS Data Lifecycle Manager policies to automate
snapshot creation and deletion based on defined schedules
and retention rules.
- Implement a tagging strategy to categorize EBS volumes and
snapshots, enabling easier management and cost allocation.
- Create an automated process to identify and alert on
unattached EBS volumes, with an option to delete them after
a specified period.
- Establish a tiering policy to move infrequently accessed
snapshots from Standard to Archive tier after a set duration
to optimize storage costs.

## Resources

**Related documents:**

- [Modify
Amazon EBS snapshots](https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/ebs-migrate-ebs-snapshots.html)
- [Delete
unattached Amazon EBS volumes](https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/ebs-delete-ebs-volumes.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftcost05-bp02.html*

---

# MSFTCOST05-BP03 Use Amazon FSx for NetApp ONTAP

Amazon FSx for NetApp ONTAP offers a file system that supports SMB
and iSCSI protocols. Useful for critical Microsoft SQL Server
environments, as ONTAP volumes can be mapped to Windows Server
instances as block storage devices using the iSCSI model, also
providing shared storage for cluster-aware applications. FSx for ONTAP has two capacity settings (HDD and SSD), data
deduplication, and cache layers. Smaller EC2 instances can leverage
the FSx solution to achieve high performance storage levels.

**Desired outcome:** By implementing
Amazon FSx for NetApp ONTAP, an organization can achieve a highly
available and performant storage solution for Microsoft workloads.
The implementation will leverage both SMB and iSCSI protocols,
enabling efficient block storage access while benefiting from
advanced features like data deduplication and multi-tiered caching.
This will result in optimized storage costs, improved performance
even with smaller EC2 instances, and reduced operational overhead
for managing Microsoft workloads.

**Common anti-patterns:**

- Running Microsoft SQL Server or other Microsoft workloads with
directly attached EBS volumes may limit high availability and
scalability, making failover scenarios complex and
time-consuming. This approach also lacks the advanced storage
management features and efficiency benefits provided by FSx for ONTAP, potentially leading to higher costs and
operational overhead.
- Compensating for storage performance requirements by using
oversized EC2 instances with local storage or multiple EBS
volumes, rather than leveraging FSx for ONTAP's efficient
storage architecture. This results in unnecessary compute costs
and doesn't address the underlying need for enterprise-grade
storage features like deduplication and efficient snapshots.

**Benefits of establishing this best
practice:**

- FSx for ONTAP provides high-performance storage, allowing
even small EC2 instances to achieve excellent I/O capabilities.
- Easily scale storage capacity and performance independently of
compute resources, adapting to changing workload demands.
- Reduce management overhead with built-in features like data
deduplication, snapshots, and multi-protocol support.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

To implement FSx for ONTAP for Microsoft workloads, create
an FSx file system in your VPC. Configure SVMs and volumes for
your applications, setting up SMB shares and iSCSI LUNs as needed.
Connect Windows instances to these resources using native tools.
For high availability, use Windows Server Failover Clustering with
FSx as shared storage. Migrate your data, then update backup and
recovery processes to leverage FSx features like snapshots and
replication.

### Implementation steps

- Create FSx for ONTAP file system within your VPC,
configuring the appropriate storage capacity and throughput
based on workload requirements
- Set up Storage Virtual Machines (SVMs) and configure storage
volumes with proper protocols (SMB/iSCSI) based on your
Microsoft application needs
- Connect Windows Server instances to FSx storage using native
tools (File Explorer for SMB, iSCSI Initiator for block
storage)
- Configure Windows Server Failover Clustering if high
availability is required, using FSx for ONTAP as the shared
storage
- Migrate existing data to FSx storage and implement
backup/recovery procedures using ONTAP's snapshot and
replication capabilities

## Resources

**Related documents:**

- [What
is Amazon FSx for NetApp ONTAP?](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/what-is-fsx-ontap.html)
- [Provisioning
iSCSI for Windows](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/mount-iscsi-windows.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftcost05-bp03.html*

---

# MSFTCOST05-BP04 Use Amazon FSx for Windows File Server

Amazon FSx for Windows File Server is a fully managed file storage service that's optimized for Microsoft
workloads. It provides an SMB file system that can be accessed by applications, including
Windows web servers and Microsoft SQL Server. FSx for Windows File Server is a scalable solution that offers
Single AZ or Multi AZ availability, automatic data deduplication, different pricing options, and
two capacity settings (HDD and SSD), being flexible to fit your Microsoft workloads. Fairly
small EC2 instances can leverage the FSx solution to achieve high performance storage levels.

**Desired outcome:** Implement Amazon FSx for Windows File Server to optimize storage
for Microsoft workloads, reducing operational overhead while enhancing scalability and
performance. This change aims to improve efficiency, simplify management, and potentially reduce
costs associated with file storage for Windows-based applications in AWS.

**Common anti-patterns:**

- Running Windows file servers on EC2 instances with attached EBS volumes, requiring
manual management of storage capacity, backups, and Windows Server maintenance while
incurring higher operational costs and complexity.
- Using non-Windows-optimized storage solutions for Windows workloads, resulting in
compatibility issues, degraded performance, and the need for additional software or
configurations to handle SMB protocol requirements.

**Benefits of establishing this best practice:**

- Eliminates the need for manual file server management, Windows patching, and backup
administration through AWS's fully managed service.
- Provides high-performance storage with automatic capacity management and the ability to
scale up or down based on workload demands, while supporting both Single-AZ and Multi-AZ
deployments.
- Offers flexible storage options (HDD/SSD) and pricing models, allowing organizations to
align costs with actual needs while eliminating the overhead of maintaining dedicated
Windows file servers and associated licenses.

**Level of risk exposed if this best practice is not established:**
Medium

## Implementation guidance

Begin by assessing your current Windows workload requirements, including storage
capacity, performance needs, and availability requirements. Choose between Single-AZ or
Multi-AZ deployment based on your reliability needs, and select the appropriate storage type
(HDD for general purpose or SSD for performance-intensive workloads). Start with a pilot
migration of a non-critical workload to validate the setup and performance. Configure your
existing Windows applications and services to connect to the FSx file system using standard
SMB protocol, and implement appropriate security groups and Active Directory integration. Once
validated, proceed with a phased migration approach for remaining workloads while monitoring
performance metrics through CloudWatch.

### Implementation steps

- Assess workload requirements and select appropriate FSx configuration
(Single/Multi-AZ, HDD/SSD, and storage capacity) based on performance needs and budget
constraints.
- Configure network security by setting up VPC security groups, ensuring proper
routing, and establishing Active Directory integration for authentication.
- Migrate existing file data to FSx using AWS DataSync or standard file copy tools,
validating data integrity and permissions post-migration.
- Update application configurations to point to the new FSx file share endpoints and
verify connectivity, performance, and functionality across all dependent services.

## Resources

**Related documents:**

- [Amazon FSx for Windows File Server](https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/storage-fsx.html)

**Related tools:**

- [AWS DataSync](https://aws.amazon.com/datasync/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftcost05-bp04.html*

---

# MSFTCOST06 — Active directory

**Pillar**: Cost Optimization  
**Best Practices**: 3

---

# MSFTCOST06-BP01 Use AWS Managed Microsoft Active Directory

AWS Managed Microsoft AD provides redundant Windows Server domain
controllers across two Availability Zones in your VPC. It handles
all maintenance tasks automatically, including monitoring,
replication, backups, and updates. The service supports
directory-aware workloads like SharePoint and .NET applications, and
can integrate with on-premises Active Directory through trust
relationships. Based on size requirements, you can either choose the
Standard or the Enterprise edition.

**Desired outcome:** By implementing
AWS Managed Microsoft Active Directory, you aim to reduce
operational overhead and costs associated with managing Active
Directory in the AWS Cloud. This solution provides a highly
available, fully managed directory service that automatically
handles maintenance tasks, supports directory-aware workloads, and
enables integration with on-premises Active Directory. The result is
a more efficient, scalable, and cost-effective approach to directory
services in your cloud environment.

**Common anti-patterns:**

- Managing your own domain controllers on EC2 instances, resulting
in unnecessary operational overhead from manual patching,
backups, monitoring, and high availability configuration.
- Creating multiple standalone Active Directory environments
across different workloads instead of using a centralized
managed service, leading to increased costs and management
complexity.

**Benefits of establishing this best
practice:**

- Reduced operational overhead: AWS handles maintenance tasks such
as patching, backups, and monitoring, freeing up IT staff to
focus on core business activities.
- Improved reliability and availability: The service automatically
deploys domain controllers across multiple Availability Zones,
ensuring high availability and disaster recovery capabilities.
- Seamless integration: Enables easy connection with on-premises
Active Directory through trust relationships, facilitating
hybrid cloud scenarios and simplifying user access management
across environments.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

To implement AWS Managed Microsoft AD effectively, start by
assessing your directory service needs and selecting the
appropriate edition (Standard or Enterprise) based on your
organization's size and requirements. Plan your VPC and network
configuration to ensure proper connectivity for your domain
controllers. If you have an existing on-premises Active Directory,
establish a trust relationship to enable seamless integration.
Migrate your directory-aware workloads gradually, beginning with
less critical applications to gain experience and confidence.
Leverage AWS IAM Identity Center for unified access management
across your AWS environment. Finally, regularly review and
optimize your setup to ensure it continues to meet your evolving
needs while maximizing cost efficiency.

### Implementation steps

- Prepare your environment by configuring VPC with appropriate
subnets across multiple AZs and setting up required network
connectivity for hybrid scenarios
- Deploy AWS Managed Microsoft AD by selecting the appropriate
edition, choosing target VPC and subnets, and configuring
directory administrator credentials and DNS settings
- Establish connectivity and access through security group
configuration, trust relationship setup with on-premises AD
if needed, and AWS IAM Identity Center integration
- Migrate workloads gradually, starting with test
applications, followed by directory-aware workloads, while
updating DNS settings and application configurations
- Monitor and maintain the environment using CloudWatch
metrics, managing directory users and groups, and performing
regular access permission audits

## Resources

**Related documents:**

- [AWS Managed Microsoft AD](https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/active-directory-aws-managed.html)
- [How
to migrate your on-premises domain to AWS Managed Microsoft AD
using ADMT](https://aws.amazon.com/blogs/security/how-to-migrate-your-on-premises-domain-to-aws-managed-microsoft-ad-using-admt/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftcost06-bp01.html*

---

# MSFTCOST06-BP02 Use AD Connector

AD Connector is a directory gateway with which you can redirect
directory requests to your on-premises Microsoft Active Directory
without caching any information in the cloud. AD Connector comes in
two sizes, small and large. A small AD Connector is designed for
smaller organizations and is intended to handle a low number of
operations per second. A large AD Connector is designed for larger
organizations and is intended to handle a moderate to high number of
operations per second. You can spread application loads across
multiple AD Connectors to scale to your performance needs. There are
no enforced user or connection limits.

**Desired outcome:** By implementing
AD Connector, the organization may achieve seamless integration
between on-premises Microsoft Active Directory and AWS Cloud
services without data replication or cloud caching. The solution
will be appropriately sized (small or large) based on operational
requirements, with the flexibility to add multiple AD Connectors for
increased performance as needed, ensuring cost-effective directory
services management while maintaining security and scalability.

**Common anti-patterns:**

- Replicating the entire on-premises Active Directory to AWS using
AWS Managed Microsoft AD or EC2 instances running AD Domain
Controllers, when only authentication and authorization services
are required, leading to increased attack surface, higher costs,
and unnecessary data duplication.
- Implementing AWS Managed Microsoft AD when only directory
authentication is needed, resulting in higher operational costs
and unnecessary complexity when AD Connector could provide the
same functionality through simple proxying of authentication
requests to the existing on-premises Active Directory.

**Benefits of establishing this best
practice:**

- AD Connector eliminates the need for complex directory
synchronization solutions or maintaining separate directory
infrastructures in the cloud, reducing both capital and
operational expenses associated with directory services
management.
- By not storing or caching any directory information in the
cloud, AD Connector minimizes the risk of data breaches and
maintains a smaller attack surface, while still allowing AWS
resources to leverage existing on-premises Active Directory for
authentication and authorization.

**Level of risk exposed if this best practice
is not established:** Low

## Implementation guidance

To implement AD Connector effectively, start by assessing your
organization's directory service needs and sizing requirements.
Choose between small and large AD Connector options based on your
expected operation volume. Ensure your on-premises Active
Directory is properly configured and accessible from your AWS VPC
through a secure connection, such as AWS Direct Connect or a VPN.
Set up the AD Connector in your VPC, configure the necessary
security groups, and test the connection thoroughly. For high
availability, consider deploying AD Connectors in multiple
Availability Zones. Finally, integrate your AWS resources and
applications with AD Connector for seamless authentication and
authorization using your existing Active Directory credentials.

### Implementation steps

- Establish network connectivity between AWS and on-premises
environment through either AWS Direct Connect or AWS Site-to-Site VPN, ensuring proper routing and security group
configurations are in place.
- Deploy AD Connector in your VPC, selecting the appropriate
size (small or large) based on your organization's
authentication operation volume and configuring it with your
on-premises Active Directory service account credentials.
- Test AD Connector functionality by verifying authentication
flows and ensuring proper communication between AWS
resources and your on-premises Active Directory.
- Enable and configure AWS services and applications to use AD
Connector for authentication, including AWS Management Console access and AWS Enterprise Applications that support
SAML 2.0.

## Resources

**Related documents:**

- [AD
Connector](https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/active-directory-connector.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftcost06-bp02.html*

---

# MSFTCOST06-BP03 Use self-managed Active Directory on Amazon EC2

Depending on the requirements, your Microsoft workload may require
the use of a self-managed Active Directory deployment (either a new
forest or extending an existing one). Deploying Active Directory
domains controllers to Amazon EC2 is fairly simple. Domain
controllers are usually good candidates to run on Amazon EC2
burstable instance family, saving on compute costs. Make sure to
evaluate the capacity planning recommendations provided by Microsoft
to address your workload requirements.

**Desired outcome:** Deploy
self-managed Active Directory domain controllers on Amazon EC2,
leveraging burstable instance families where appropriate to optimize
costs. The implementation will follow Microsoft's capacity planning
guidelines and support either new or extended Active Directory
forests based on organizational requirements, ensuring a robust and
cost-effective directory service solution.

**Common anti-patterns:**

- Deploying Active Directory domain controllers on oversized EC2
instances, such as using high-performance compute-optimized
instances when not required. This leads to unnecessary costs and
underutilized resources, contradicting the goal of cost
optimization.
- Implementing Active Directory on EC2 without properly evaluating
Microsoft's capacity planning recommendations. This can result
in performance issues, scalability problems, and potential
service disruptions, ultimately affecting the reliability of the
Microsoft workload and potentially increasing long-term costs
due to necessary remediation efforts.

**Benefits of establishing this best
practice:**

- Cost-effective directory services through optimized EC2 instance
selection and burstable computing, reducing operational expenses
while maintaining performance requirements.
- Enhanced control and flexibility in deploying and managing
Active Directory infrastructure, supporting both new
implementations and extensions of existing directory services.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

To implement self-managed Active Directory on Amazon EC2, begin by
assessing your workload requirements and consulting Microsoft's
capacity planning recommendations. Choose appropriate EC2 instance
types, favoring burstable instances where suitable. Deploy at
least two domain controllers across different Availability Zones
for high availability. Use Amazon EBS volumes for storage,
ensuring proper backups and snapshots. Implement security best
practices, including network segmentation with VPCs and security
groups. Finally, establish monitoring and alerting using Amazon CloudWatch to maintain optimal performance and availability of
your Active Directory infrastructure.

### Implementation steps

- Size and deploy EC2 instances based on Microsoft's capacity
planning guidelines, utilizing burstable instance families
where appropriate, and ensure distribution across multiple
Availability Zones for high availability.
- Configure networking components including VPC design,
security groups, and DHCP options to support Active
Directory requirements and establish secure communication
paths.
- Install and configure Active Directory Domain Services,
establishing either a new forest or extending an existing
one, following Microsoft's recommended configurations and
security baselines.
- Implement monitoring and backup solutions using Amazon CloudWatch and automated EBS snapshots to maintain service
health and enable disaster recovery capabilities.

## Resources

**Related documents:**

- [Self-managed
Active Directory on Amazon EC2](https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/active-directory-self-managed.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftcost06-bp03.html*

---

# MSFTCOST07 — Containers

**Pillar**: Cost Optimization  
**Best Practices**: 3

---

# MSFTCOST07-BP01 Optimize AWS Fargate tasks with AWS Compute Optimizer

AWS Compute Optimizer can be used to help right size and optimize your workloads running on
AWS Fargate. If not reviewed, long running tasks can be overprovisioned and increase compute
costs.

**Desired outcome:** Aim to achieve optimal resource allocation and
cost efficiency. Right-size our Fargate tasks, avoiding overprovisioning and reducing
unnecessary compute costs. Through regular review and implementation of Compute Optimizer's recommendations,
we expect to maintain well-optimized workloads that balance performance and cost-effectiveness,
ultimately leading to improved resource utilization and significant cost savings in our AWS
environment.

**Common anti-patterns:**

- Deploying Fargate tasks with initial resource configurations and never reviewing or
adjusting them over time, ignoring Compute Optimizer's recommendations and missing significant cost
optimization opportunities.
- Deliberately configuring Fargate tasks with excessive CPU and memory as a
precautionary measure, leading to consistent overprovisioning and unnecessary costs despite
Compute Optimizer showing opportunities for right-sizing.

**Benefits of establishing this best practice:**

- Regular review and implementation of Compute Optimizer recommendations leads to right-sized
Fargate tasks, eliminating waste from overprovisioning and reducing monthly compute costs
while maintaining required performance levels.
- Leveraging Compute Optimizer's ML-powered analytics provides objective, metrics-based insights for
resource allocation decisions, replacing guesswork with actual usage patterns and ensuring
optimal task configurations across your workloads.

**Level of risk exposed if this best practice is not established:**
Medium

## Implementation guidance

Enable AWS Compute Optimizer for your organization or account. Establish a monthly review process for
Fargate task recommendations. Implement changes gradually, starting with non-production
workloads. Monitor performance before and after optimizations. Create a feedback loop to
inform future deployments, and consider automating recommendation implementation through
Infrastructure as Code practices for consistency and efficiency.

### Implementation steps

- Enable AWS Compute Optimizer in your environment through the AWS Management Console and verify it begins
collecting task utilization data for analysis.
- Schedule monthly review meetings with relevant stakeholders to assess Compute Optimizer's
Fargate task recommendations and prioritize which optimizations to implement.
- Create a change management process that includes testing optimizations in
non-production environments first, with clear rollback procedures if needed.
- Implement approved recommendations through your existing Infrastructure as Code
(IaC) framework, ensuring changes are tracked and reproducible.
- Set up CloudWatch dashboards or alerts to monitor performance metrics post-optimization,
ensuring the changes maintain desired service levels while achieving cost savings.

## Resources

**Related documents:**

- [Optimize costs for AWS Fargate tasks on Amazon ECS](https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/optimizer-ecs-fargate.html)

**Related tools:**

- [What is
AWS Compute Optimizer?](https://docs.aws.amazon.com/compute-optimizer/latest/ug/what-is-compute-optimizer.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftcost07-bp01.html*

---

# MSFTCOST07-BP02 Improve Amazon Elastic Kubernetes Service cost tracking with Kubecost

Kubecost improves the cost tracking for your Windows containers.
Kubecost helps right sizing cluster nodes, container requests, and
manages underutilized infrastructure.

**Desired outcome:** Aim to achieve
improved cost tracking for our Windows containers. The desired
outcome is to optimize cluster resource utilization through
right-sizing of nodes and container requests, while effectively
managing underutilized infrastructure. This implementation may
provide better visibility into EKS costs, enabling more informed
decision-making and ultimately leading to cost savings in Kubernetes
deployments.

**Common anti-patterns:**

- Lack of cost monitoring tools, leading to untracked spending and
no visibility into workload-specific costs across Amazon Elastic Kubernetes Service (EKS) clusters.
- Blindly overprovisioning Windows container resources without
usage data, resulting in unnecessary infrastructure costs and
resource waste.

**Benefits of establishing this best
practice:**

- Gain detailed insights into container-level expenses, enabling
accurate cost allocation across teams, projects, and workloads.
- Identify and right-size underutilized resources, leading to
significant cost savings and improved cluster efficiency for
Windows containers.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Start by deploying Kubecost into your environment. Configure it to
integrate with your EKS cluster and AWS Cost and Usage Reports.
Set up proper tagging for resources to ensure accurate cost
allocation. Regularly review Kubecost dashboards to identify
cost-saving opportunities, such as right-sizing nodes and
optimizing container requests. Use Kubecost's recommendations to
adjust resource allocations and implement cost controls.
Continuously monitor and refine your cost optimization strategy
based on the insights provided by Kubecost.

### Implementation steps

- Deploy Kubecost to your EKS clusters, ensuring proper IAM
roles and permissions are configured
- Set up AWS Cost and Usage Report integration and configure
Kubecost to access your billing data
- Implement a comprehensive resource tagging strategy to
accurately track costs across teams and applications
- Configure alerts and thresholds for cost anomalies and
resource utilization metrics
- Review initial baseline metrics and identify immediate
optimization opportunities for Windows containers
- Establish regular review cycles to analyze Kubecost reports
and implement recommended optimizations

## Resources

**Related documents:**

- [Gain
visibility into your Amazon EKS costs](https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/kubecost-main.html)
- [Learn
more about Kubecost](https://docs.aws.amazon.com/eks/latest/userguide/cost-monitoring-kubecost-bundles.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftcost07-bp02.html*

---

# MSFTCOST07-BP03 Change your scale strategy for Windows Containers on Kubernetes using Karpenter

Karpenter is a Kubernetes cluster autoscaler that dynamically
provisions EC2 instances based on your workload demands,
automatically launching right-sized instances in response to pending
pods and continuously evaluating the cluster to optimize costs by
consolidating workloads onto more efficient instance types. The tool
proactively replaces outdated nodes with newer ones to maintain
security compliance and supports diverse compute requirements by
selecting from a broad range of instance types and purchasing
options, including both On-Demand and Spot instances.

**Desired outcome:** Expect to
achieve improved resource utilization, reduced operational overhead,
and optimized cloud costs. EKS clusters will dynamically scale to
meet application demands, maintain up-to-date and secure
infrastructure, and efficiently manage diverse workloads without
manual intervention, ultimately leading to a more responsive,
cost-effective, and easily managed Kubernetes environment on AWS.

**Common anti-patterns:**

- Teams often configure Karpenter with unnecessarily specific
instance type constraints or narrow capacity requirements,
limiting its ability to efficiently provision nodes and
potentially increasing costs by forcing the use of suboptimal
instance types.
- Organizations frequently deploy Karpenter without properly
configuring Pod Disruption Budgets (PDBs), leading to unexpected
application downtime during node consolidation or replacement
operations, as Karpenter may terminate nodes without ensuring
proper workload migration.

**Benefits of establishing this best
practice:**

- By allowing Karpenter to intelligently select from a broad range
of instance types and automatically consolidate workloads,
organizations can significantly reduce their AWS compute costs
while maintaining optimal performance for their applications.
- Teams spend less time on manual cluster management and capacity
planning, as Karpenter automates node provisioning, scaling, and
replacement activities, enabling engineers to focus on
higher-value development tasks.
- With Karpenter's automated node replacement feature, clusters
maintain better security hygiene through regular updates and
patches, reducing the risk of vulnerabilities while ensuring
compliance with security standards without manual intervention.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

To implement Karpenter effectively, define flexible provisioner
configurations that accommodate both Linux and Windows workloads,
ensuring appropriate instance types are available for each OS. Set
up distinct provisioners with OS-specific requirements, configure
Pod Disruption Budgets for critical applications, and establish
proper taints and tolerations to ensure workloads land on
compatible nodes. Regularly monitor cluster behavior and costs to
optimize your configuration.

### Implementation steps

- Install and configure Karpenter in your EKS cluster,
ensuring proper IAM permissions and VPC settings
- Create flexible provisioner configurations for both Linux
and Windows workloads, specifying appropriate instance types
and purchasing options
- Set up Pod Disruption Budgets for critical applications to
maintain availability during node consolidation
- Configure monitoring and alerting to track Karpenter's
performance and cluster resource utilization
- Regularly review and adjust Karpenter settings based on
observed cluster behavior and cost metrics

## Resources

**Related documents:**

- [Karpenter](https://docs.aws.amazon.com/eks/latest/best-practices/karpenter.html)
- [Getting
Started with Karpenter](https://karpenter.sh/docs/getting-started/getting-started-with-karpenter/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftcost07-bp03.html*

---

# MSFTCOST08 — .NET

**Pillar**: Cost Optimization  
**Best Practices**: 2

---

# MSFTCOST08-BP01 Refactor to cross-platform .NET and move to Linux

Migrating .NET Framework applications to .NET 8 or later enables
cross-platform deployment, improved security, and better
performance. This modernization allows applications to run on Linux
systems, leverage cloud-native features, and benefit from the latest
optimizations, resulting in more efficient and maintainable systems.

**Desired outcome:** Aim to achieve
reduced licensing costs, improved performance, and enhanced
security. The modernized applications run efficiently on Linux
environments, including AWS Graviton processors, while leveraging
the latest .NET features and cloud-native capabilities. This
transformation results in a more cost-effective, scalable, and
maintainable application portfolio that aligns with modern cloud
architecture principles.

**Common anti-patterns:**

- Continuing to rely on Windows-specific dependencies and COM
components without evaluating modern alternatives, making the
migration to Linux impossible and perpetuating technical debt
and higher operational costs.
- Attempting to run portions of the application on Linux while
keeping critical components on Windows servers, creating a
complex hybrid architecture that increases operational overhead
and negates the cost benefits of the migration while introducing
potential compatibility issues.

**Benefits of establishing this best
practice:**

- Moving to Linux eliminates Windows licensing costs while
enabling the use of cost-effective infrastructure options like
AWS Graviton processors, resulting in significant operational
cost savings and improved performance metrics through modern
.NET optimizations.
- Cross-platform .NET applications can be deployed across diverse
environments using containerization technologies, enabling
efficient CI/CD pipelines, simplified scaling strategies, and
better resource utilization in cloud environments, leading to
improved application reliability and reduced maintenance
overhead.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Begin with an AWS Transform-assisted assessment to identify
Windows dependencies, then implement an incremental migration
strategy focusing on high-impact components first. Utilize
automated refactoring tools for conversion to cross-platform .NET,
containerize the application, and establish comprehensive testing
protocols to ensure successful deployment on Linux environments
while maintaining application performance and reliability.

### Implementation steps

- Conduct application assessment using AWS Transform to
identify Windows dependencies and migration challenges
- Develop a phased migration plan, prioritizing components for
maximum cost-benefit impact
- Refactor code to cross-platform .NET using AWS Transform's
AI-powered tools and manual adjustments
- Containerize the application and implement a robust testing
strategy for Linux environments
- Deploy the refactored application to Linux servers,
including AWS Graviton instances, and monitor performance

## Resources

**Related documents:**

- [Refactor
to modern .NET and move to Linux](https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/net-refactor-linux.html)

**Related tools:**

- [Modernizing
.NET with AWS Transform](https://docs.aws.amazon.com/transform/latest/userguide/dotnet.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftcost08-bp01.net-and-move-to-linux.html*

---

# MSFTCOST08-BP02 Consider serverless architecture for your Microsoft .NET applications

AWS Lambda enables .NET developers to build serverless applications
without managing servers, paying only for actual usage. Using modern
.NET versions, developers can create scalable functions in C# or F#
that run on-demand in the cloud, reducing costs and development
time.

**Desired outcome:** By adopting
serverless architecture with AWS Lambda for .NET applications,
organizations may achieve improved scalability and cost efficiency,
paying only for resources used while eliminating server management
overhead. Using AWS tools like Microservice Extractor may further
simplify the modernization of existing applications.

**Common anti-patterns:**

- Maintaining continuously operational and over-sized servers for
.NET applications instead of leveraging serverless architecture,
resulting in unnecessary costs and underutilized resources.
- Keeping large and monolithic .NET applications intact rather
than breaking them down into microservices or serverless
functions, leading to reduced flexibility and scalability.

**Benefits of establishing this best
practice:**

- Organizations only pay for actual compute resources consumed
during function execution, eliminating costs associated with
idle server capacity and infrastructure management.
- Development teams can focus on code rather than server
maintenance, reducing operational overhead and accelerating
deployment cycles.
- Applications automatically scale based on demand without manual
intervention, ensuring optimal performance during peak loads
while maintaining cost efficiency during low-usage periods.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Begin by identifying suitable .NET applications or components that
can benefit from serverless architecture. Start small by migrating
discrete functions to AWS Lambda using modern .NET versions (Core
or later). Utilize AWS Microservice Extractor for .NET to analyze
and decompose existing monolithic applications into smaller,
manageable services. Implement proper monitoring and logging from
the outset using AWS CloudWatch, and establish clear deployment
pipelines using AWS CI/CD tools. Gradually, expand the serverless
footprint as the team gains experience and confidence with the
architecture.

### Implementation steps

- Install and configure AWS Microservice Extractor for .NET to
analyze existing monolithic applications and identify
potential microservice candidates
- Assess existing .NET applications and identify functions
suitable for serverless migration, prioritizing stateless
operations and event-driven processes
- Set up the AWS Lambda development environment with .NET SDK
and necessary AWS tools (AWS Toolkit for Visual Studio and
AWS CLI)
- Create and test initial Lambda functions using modern .NET
versions, implementing proper error handling and logging
- Configure automated deployment pipelines using AWS CI/CD
services (CodePipeline and CodeBuild) for consistent
function updates
- Monitor function performance and costs using AWS CloudWatch,
and optimize resource allocation based on actual usage
patterns

## Resources

**Related documents:**

- [Consider
serverless .NET](https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/net-serverless.html)

**Related tools:**

*[What
Is AWS Microservice Extractor for .NET?](https://docs.aws.amazon.com/microservice-extractor/latest/userguide/what-is-microservice-extractor.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftcost08-bp02.net-applications.html*

---

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
