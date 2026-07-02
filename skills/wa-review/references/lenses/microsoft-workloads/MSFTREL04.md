# MSFTREL04 — Automation and recovery management

**Pillar**: Reliability  
**Best Practices**: 1

---

# MSFTREL04-BP01 Use Amazon EC2 Auto Scaling in combination with Application Auto Scaling

Microsoft workloads often experience variable demand patterns that
require dynamic resource scaling to maintain performance and cost
efficiency. Applications like SharePoint farms, SQL Server
databases, and .NET web applications face fluctuating user loads,
batch processing requirements, and seasonal traffic variations that
make static resource provisioning ineffective and costly.

**Desired outcome:** Implement
automated scaling mechanisms that combine instance-level and
application-level auto scaling capabilities to optimize resource
utilization. Configure predictive scaling using historical data and
machine learning to anticipate capacity needs, while maintaining
regulatory requirements through dedicated host allocation. Automate
capacity management through system tooling that responds to
monitoring metrics and scheduled events.

**Common anti-patterns:**

- Relying on human intervention to adjust resources in response to
demand changes, leading to slow reactions and potential over- or
under-provisioning.
- Maintaining a fixed resource capacity based on peak demand
expectations, resulting in wasted resources during low-demand
periods and potential shortages during unexpected spikes.
- Focusing solely on infrastructure scaling without considering
the need for application-level scaling, potentially leading to
bottlenecks in database connections, caching, or other
application components.

**Benefits of establishing this best
practice:**

- Dynamically adjusts resource capacity to actual demand, reducing
waste from over-provisioning while reducing performance issues
from under-provisioning.
- Automatically responds to changes in workload patterns and
system failures, maintaining service availability without manual
intervention.
- Uses historical data and machine learning to anticipate and
prepare for demand spikes before they occur, reducing reactive
scaling delays.
- Maintains licensing and regulatory requirements through
controlled scaling of dedicated resources while still achieving
operational efficiency.
- Reduces administrative overhead through automated capacity
management, freeing up teams to focus on higher-value activities
while providing consistent performance.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Configure auto scaling groups to dynamically adjust compute
resources based on demand patterns. Enable predictive scaling
using historical metrics to proactively manage capacity before
peak loads occur. For applications with specific licensing
requirements, use dedicated hosts with auto scaling policies to
maintain adherence. Implement automation tools to handle routine
capacity management tasks, using monitoring alerts and scheduled
actions to control resource scaling.

Begin by establishing baseline metrics and performance thresholds
for both infrastructure and application components. Configure
scaling policies that combine predictive and dynamic adjustments,
using historical data to anticipate capacity needs while
maintaining real-time responsiveness to unexpected changes. Set up
monitoring and alerting to track scaling activities, and implement
gradual scaling steps to avoid resource thrashing. Document
scaling decisions and regularly review performance data to refine
thresholds and policies, providing optimal resource utilization
while maintaining service levels and regulatory requirements.

### Implementation steps

- Configure EC2 Auto Scaling groups with appropriate launch
templates and scaling policies for Windows instances,
including SQL Server and IIS workloads.
- Enable predictive scaling using AWS Auto Scaling with
machine learning forecasts, incorporating Microsoft workload
patterns and licensing considerations for dedicated hosts.
- Set up Amazon CloudWatch Application Insights to monitor
.NET and SQL Server applications, automatically detecting
anomalies and providing application-level metrics for
scaling decisions across IIS, SQL Server, and application
servers.
- Create CloudWatch alarms and custom metrics for Microsoft
applications including SQL Server connection counts, IIS
request queues, and .NET application performance counters to
trigger scaling actions, using Application Insights
automated dashboards.
- Implement application-level scaling automation for SQL
Server Always On Availability Groups, IIS worker process
scaling, and SharePoint farm expansion using Systems Manager
automation documents triggered by Application Insights
events.
- Configure session state management and connection pooling
strategies to support horizontal scaling of .NET
applications and SQL Server workloads across multiple
instances, using Application Insights correlation data for
optimization.

## Resources

**Related documents:**

- [Predictive
scaling for Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-predictive-scaling.html)
- [What
is Amazon EC2 Auto Scaling?](https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html)
- [Accelerate
Amazon EC2 Auto Scaling for Microsoft Windows workloads](https://aws.amazon.com/blogs/modernizing-with-aws/accelerate-amazon-ec2-auto-scaling-for-microsoft-windows-workloads/)
- [Automatically
scale your Amazon ECS service](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-auto-scaling.html)

**Related tools:**

- [AWS Auto Scaling](https://aws.amazon.com/autoscaling/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
- [Auto
Scaling launch templates](https://docs.aws.amazon.com/autoscaling/ec2/userguide/launch-templates.html)
- [Elastic Load Balancing](https://aws.amazon.com/elasticloadbalancing/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftrel04-bp01.html*

---
