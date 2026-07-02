**Pillar**: Cost Optimization

# FSICOST04: How do you promote cost-awareness within your organization?

Awareness of usage at all levels in the organization is key to driving change, as
change in usage drives changes in cost. Consider taking a multi-faceted approach to becoming
aware of your usage and expenditures. Your team must gather data, analyze, and then report.

## FSICOST04-BP01 Promote a culture of transparency on costs

To promote transparency and accountability of costs, it is important to have standard
mechanisms that show or charge back the costs to business units or applications. Companies
use tags to allocate cost to teams, business units, or organizations within an enterprise
and to observe trends. Enforce a tagging taxonomy with tag policies within pipelines that
deploy infrastructure as code (IAC) and govern using SCPs at the organization-level and
configuration across all AWS accounts. For more information on tags, see: [Using
AWS cost allocation tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html).

For generative AI workloads, implement additional tagging for:

- Model inference costs
- Token usage
- Vector store operations
- Knowledge base storage
- Agent workflow execution

Adopt a generative AI cost scorecard per product or use-case team that tracks metrics
such as cost per 1K tokens, average context length, cache hit rates, and percentage of
calls by model tier (for example, gold, silver, and bronze). Visualize this data in
dashboards to drive accountability and promote informed optimization decisions across
engineering and business stakeholders.

In the large organization, some teams are very advanced in cost optimization and they
are aware of cost impacts while other teams are not that mature. Hence, team cooperation,
sharing importance of Cloud Finance Management, Cloud Center of Excellence is extremely
important to promote

a culture of cost optimization. For more information on tags, see [Using
AWS cost](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html)
[allocation tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html).

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsicost04.html*
