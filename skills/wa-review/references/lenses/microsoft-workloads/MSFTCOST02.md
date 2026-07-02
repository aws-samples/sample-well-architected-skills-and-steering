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
