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
