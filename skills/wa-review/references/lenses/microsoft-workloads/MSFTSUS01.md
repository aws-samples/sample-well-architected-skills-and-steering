# MSFTSUS01 — Efficient infrastructure

**Pillar**: Sustainability  
**Best Practices**: 2

---

# MSFTSUS01-BP01 Align business requirements with sustainable Microsoft architecture designs

When designing Microsoft environments in the cloud, business leaders
and architecture teams must actively prioritize sustainability. This
requires a clear understanding of the trade-offs involved and the
ability to articulate them effectively. In production workloads,
with reliability and performance traditionally taking precedence
over costs, sustainable designs may not always result in overall
cost savings. In fact, implementing more sustainable practices for
Microsoft workloads on AWS could potentially increase expenses in
areas such as software licensing, staffing, or other business
operations. To successfully meet sustainability goals, these
trade-offs must be carefully balanced against other business
priorities. It's crucial that stakeholders agree on clearly defined,
measurable sustainability objectives that align with broader
business needs and performance requirements. This approach
integrates sustainability efforts thoughtfully into the overall
business strategy, rather than being treated as an isolated
initiative.

**Desired outcome:** Your Microsoft
workload architecture design reflects clearly defined sustainability
objectives that are agreed upon by your stakeholders and balanced
effectively with business priorities, performance requirements, and
cost considerations.

**Common anti-patterns:**

- Treating sustainability as a secondary concern or add-on, rather
than integrating it into the core design process of Microsoft
workloads on AWS. This often results in missed opportunities for
environmental improvements and potential conflicts with
established architectures.
- Setting sustainability goals for Microsoft environments without
considering their impact on other business priorities,
performance requirements, or cost structures. This can lead to
unrealistic expectations, unintended consequences, and
resistance from stakeholders.
- Implementing sustainability measures for Microsoft workloads
without clear agreement and understanding among relevant
stakeholders. This often results in conflicting priorities,
inadequate support for sustainability initiatives, and
difficulty in measuring or achieving environmental objectives.

**Benefits of establishing this best
practice:**

- Clear prioritization of sustainability in Microsoft workload
design enables better alignment between environmental goals and
business objectives. This integrated approach verifies that
sustainability initiatives support rather than conflict with
other strategic priorities, leading to more successful and
sustainable outcomes.
- By establishing clear understanding of trade-offs and getting
stakeholder agreement on sustainability objectives,
organizations can make better-informed decisions about resource
allocation, performance requirements, and infrastructure
investments. This leads to more balanced and effective
implementation of sustainable practices.
- Having clearly defined, measurable sustainability objectives
allows organizations to effectively track and demonstrate the
environmental impact of their Microsoft workloads. This enables
better reporting, validates sustainability investments, and
supports continuous improvement while maintaining alignment with
business performance requirements.

**Level of risk exposed if this best practice
is not established:** Low

## Implementation guidance

Organizations must integrate sustainability into their Microsoft
workload designs on AWS by establishing clear environmental
objectives and gaining stakeholder alignment on trade-offs. This
approach balances environmental responsibility with operational
effectiveness, helping meet growing expectations from customers,
investors, and regulators while maintaining business performance.

### Implementation steps

- Integrate sustainability as a core consideration in
Microsoft workload design on AWS. Communicate clearly about
trade-offs, set measurable sustainability objectives, and
gain stakeholder consensus on balancing these goals with
other business priorities.
- Emphasize the importance of environmental responsibility in
the context of current business trends. Highlight how
sustainability efforts can meet the expectations of
customers, investors, and regulators.
- Align sustainability efforts with overall business strategy.
Focus on reducing environmental impact while maintaining
operational effectiveness. Demonstrate how this approach can
lead to competitive advantages and contribute to broader
corporate sustainability goals.

## Resources

**Related documents:**

- [AWS Well-Architected Framework - Sustainability pillar](https://docs.aws.amazon.com/wellarchitected/latest/framework/sustainability.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftsus01-bp01.html*

---

# MSFTSUS01-BP02 Monitor Microsoft workload sustainability performance

Monitoring and reporting on Microsoft workload sustainability in AWS
provides essential feedback on the effectiveness of implemented
changes. This data supports sustainability reporting for
shareholders, regulators, and eco-conscious customers. Using metrics
from the operational excellence pillar, these reports can showcase
improvements in your Microsoft landscape's operational
sustainability, demonstrating alignment with corporate
sustainability goals. This process creates a continuous feedback
loop, allowing for ongoing optimization and validation of
sustainability efforts in your Microsoft environment.

**Desired outcome:** Regular
monitoring and comprehensive reporting demonstrates measurable
improvements in Microsoft workload sustainability metrics on AWS,
enabling data-driven decisions, validating green initiatives, and
meeting stakeholder sustainability reporting requirements while
maintaining operational excellence.

**Common anti-patterns:**

- Organizations collect extensive sustainability metrics for
Microsoft workloads on AWS but fail to translate data into
actionable improvements. Despite sophisticated monitoring tools
and regular reporting, the information remains unused, leading
to stagnant sustainability initiatives and wasted resources in
data collection while missing opportunities for meaningful
environmental impact.
- Sustainability monitoring and reporting for Microsoft workloads
operate in isolation from other operational metrics and business
processes. This disconnected approach, where sustainability
teams work separately from IT operations, results in missed
opportunities for integrated improvements and limited
understanding of sustainability metrics across departments,
ultimately reducing the effectiveness of environmental
initiatives.

**Benefits of establishing this best
practice:**

- By monitoring and reporting on Microsoft workload sustainability
in AWS, organizations gain valuable insights into their
environmental impact. This data enables informed
decision-making, allowing companies to identify areas of high
resource consumption or inefficiency. With this knowledge, they
can implement targeted improvements, optimize workloads, and
reduce their carbon footprint more effectively. The result is a
measurable decrease in energy use and emissions, contributing
significantly to corporate sustainability goals.
- Regular sustainability reporting builds transparency and trust
with shareholders, regulators, and environmentally conscious
customers. By providing clear, quantifiable data on
sustainability efforts and improvements in Microsoft workloads,
companies demonstrate their commitment to environmental
responsibility. This transparency not only aids in regulatory
adherence but also strengthens the company's reputation,
potentially attracting eco-minded investors and customers. It
can lead to improved stakeholder relationships, better market
positioning, and even competitive advantages in an increasingly
sustainability-focused business landscape.

**Level of risk exposed if this best practice
is not established:** Low

## Implementation guidance

Create a structured approach for monitoring and reporting
Microsoft workload sustainability in AWS. Identify metrics, set up
AWS tools, integrate with operational processes, establish
reporting cycles, implement improvement loops, and and align with
stakeholder needs. This comprehensive system enables organizations
to measure, improve, and communicate their environmental impact
effectively.

### Implementation steps

- Set up custom metrics and dashboards in Amazon CloudWatch to
monitor key sustainability indicators for Microsoft
workloads, such as CPU utilization, storage efficiency, and
network traffic. Establish alarms for thresholds that
indicate potential sustainability issues or opportunities
for optimization.
- Enable and configure AWS Cost and Usage Reports to track
resource consumption and associated costs for Microsoft
workloads. Use these reports to identify patterns in usage,
pinpoint areas of high energy consumption, and inform
decisions on rightsizing and optimizing workloads for
improved sustainability.

## Resources

**Related documents:**

- [What
are AWS Cost and Usage Reports?](https://docs.aws.amazon.com/cur/latest/userguide/what-is-cur.html)
- [Increasing
sustainability for your Microsoft workloads on AWS](https://aws.amazon.com/blogs/modernizing-with-aws/increasing-sustainability-microsoft-workloads-aws/)

**Related tools:**

- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftsus01-bp02.html*

---
