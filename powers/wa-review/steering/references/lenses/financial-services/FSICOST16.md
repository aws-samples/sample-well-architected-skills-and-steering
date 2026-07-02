**Pillar**: Cost Optimization

# FSICOST16: Are you continuously assessing the ongoing costs and usage of your cloud implementations?

There is a process to examine existing cloud spend, and identify cost optimization
opportunities using manual analysis, or the use of tools (AWS Billing and Cost Management and AWS Cost Management tools, AWS
Partner tools, open-source tools, or DIY tools). As your requirements change, be aggressive
in decommissioning resources, components, and workloads that you no longer require.

## FSICOST16-BP01 Use AWS cost management tools to perform retrospective, audit-based cost optimization on existing cloud workloads

There is a process to examine existing cloud spend, and identify cost optimization
opportunities using manual analysis, or the use of tools (AWS Billing and Cost Management and Cost Management and
Cost Management tools, AWS Partner tools, open-source tools, or DIY tools).

For generative AI workloads, this includes:

- Regular review of model selection and performance against cost
- Token usage optimization
- Vector store and embedding efficiency
- Knowledge base storage optimization
- Agent workflow cost analysis

Cost optimization opportunities are identified, prioritized, and implemented in a
continuous, programmatic manner, verifying that all cloud workloads run as lean as
possible while meeting all functional and non-functional requirements.

**Tools**

Extend cost management by introducing a standard KPI stack for generative AI
workloads, tracked using AWS CFM dashboards or custom Amazon CloudWatch metrics like:

- Cost per 1,000 tokens (input and output)
- Cost per successful user or agent task
- Cache hit percentage (RAG efficiency)
- Average context length and output token size
- Model tier mix ratio (percentage of bronze, silver, and gold routing)

These KPIs provide actionable visibility into generative AI spend patterns,
supporting data-driven optimizations across model selection, prompt engineering, and
caching strategy.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsicost16.html*
