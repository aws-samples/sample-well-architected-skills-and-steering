# Cost optimization

**Pages**: 1

---

# Cost optimization pillar

The cost optimization pillar includes the ability to run services which deliver policy
intent and user outcome at the best value.

The following question and best practices are designed to
complement the best practices in the
[Cost
Optimization Pillar whitepaper](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/welcome.html).

GL-COST-01: How do you
demonstrate an understanding of “value for money” in the
customer’s context?

Most government entities have clear rules around how they assess *value for
money*, but this can be subtly different across jurisdictions. For some countries,
value for money is considered whatever is the best functionality for the cost to deliver the
desired policy outcome. Other countries take into account the best balance of social, public,
and environmental benefits along with cost.

These procurement rules translate to how cost optimization is
perceived, with broader analysis of the public value or policy
realization sometimes considered as pure cost efficiencies. For
this reason, running services at the lowest price point to deliver
policy outcomes may or may not be considered cost optimization for
the government department, although it's still a generally useful
goal.

The following is a list of considerations and good practices to explore with the customer
and to document to make sure that value for money is achieved in a government context.

- **Document the definition of value for
money** for the jurisdictional and portfolio context, and how this
service meets that definition.

**Improvement plan** – Engage with the government
organization to understand and document their value for money definition. Work with
your AWS account team to optimise costs. If you're on AWS Enterprise Support, your
Technical Account Manager (TAM) can help with this. The [AWS Tools for Reporting and Cost Optimization whitepaper](https://docs.aws.amazon.com/whitepapers/latest/cost-optimization-laying-the-foundation/reporting-cost-optimization-tools.html) can provide
guidance.

- **Define how the cost and value is
reported** to oversight and governance bodies (for
example, parliament, and public scrutiny).

**Improvement plan** – Encourage the organization to
automate and provide ease of cost/value reporting for the service. AWS provides
several reporting and cost-optimization tools, including
AWS Cost Explorer Service, AWS Budgets, and AWS Cost and Usage Report. Serverless applications
running on services like AWS Lambda and Amazon DynamoDB can help by providing insight into
costs per event.

- **Build in-house capability manage costs** through training,
tools, and equipping teams.

**Improvement plan** – Provide delivery teams with
the services and tools that they need to be able to actively understand and manage
their costs.

- **Leverage existing solutions and capabilities where
possible.** Support the reuse of platforms, panels, marketplaces, research,
design systems, and existing solutions or components where possible.

**Improvement plan** – Encourage the organization to
identify and leverage reusable tools, solutions, research and methods for the service.
See the [AWS Solutions Library](https://aws.amazon.com/solutions/).

- **Leverage professional networks and user groups.**
Identify and engage with cross-governmental networks, professional networks and relevant
user groups to engage peer review and feedback on the solution.

**Improvement plan** – Encourage the organization to
identify and leverage networks and communities of practice, and establish peer review
sessions.

- **Optimize for speed of change.**.  It’s sometimes necessary
to optimize for speed to respond to a citizen need or department mandate rapidly.
Government solutions might need to initially overcompensate on capacity to maintain
service reliability during peak popularity, for example, at the time of a press release,
to avoid breaking citizen trust. Fortunately, this necessary choice is temporary and works
well with cloud economics. Service delivery teams can cost optimize and consider automatic
scaling after release events, when utilization and popularity have normalized.

**Improvement plan** – Provide guidance and support
on automated resource optimization.

- **Optimize for budget planning processes in the
jurisdiction.** Provide decision makers with the key metrics that they need to
balance citizen needs with service costs. Support the organization to take into account
funding cycles and ensure continuity of service. Often, there is low flexibility in these
cycles, however, government customers can be supported to build more flexibility into the
program, project, or product-based funding mechanisms.

**Improvement plan** – Encourage the organization to
automate and provide ease of cost/value reporting for the service, especially for
delivery teams and decision makers.

## Resources

- [AWS Tools for Reporting and Cost Optimization whitepaper](https://docs.aws.amazon.com/whitepapers/latest/cost-optimization-laying-the-foundation/reporting-cost-optimization-tools.html)****
- AWS reusable solutions, patterns, and applications:

[AWS Solutions Library](https://aws.amazon.com/solutions/)
- [AWS Construct Library](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-construct-library.html)
- [AWS Serverless Application Repository](https://serverlessrepo.aws.amazon.com/applications)

- [How cloud can help agencies enhance security, save costs, and improve mission
delivery through the Technology Modernization Fund (TMF)](https://aws.amazon.com/blogs/publicsector/how-cloud-help-agencies-enhance-security-improve-mission-delivery-technology-modernization-fund-tmf/)
- [For Small Governments – The Cloud is Only as Big as You Want it to Be](https://aws.amazon.com/blogs/publicsector/for-small-governments-the-cloud-is-only-as-big-as-you-want-it-to-be/)
- [Optimizing nonprofits’ costs in the cloud](https://aws.amazon.com/blogs/publicsector/optimizing-nonprofits-costs-cloud/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/government-lens/cost-optimization-pillar.html*

---
