# AGENTCOST05 — Agent cost visibility and attribution

**Pillar**: Cost Optimization  
**Best Practices**: 4

---

# AGENTCOST05-BP01 Establish agent-level reasoning cost tracking and attribution

Account-level billing shows what an agent fleet costs, but it
doesn't show where the specific costs come from. Granular tracking
by agent, workflow, and reasoning phase provides trackable detail
about your spending, which makes opaque costs into the input for
targeted optimization.

**Desired outcome:**

- You have a standard tag taxonomy applied consistently across all
agent invocations.
- You track per-phase token consumption (planning, execution,
reflection, and verification) separately.
- You monitor tool invocation costs separately from model
inference costs.
- You calculate cost-per-decision, cost-per-reasoning-cycle, and
cost-per-task-completion as primary agent metrics.

**Common anti-patterns:**

- Tracking only account-level AWS billing without per-agent or
per-workflow attribution, reducing the risk of identification of
cost drivers.
- Deploying agents without consistent resource tagging across
model invocations, function executions, and data operations.
- Monitoring total agent costs without distinguishing between
supervisor overhead, worker execution, and individual reasoning
phases.
- Monitoring only infrastructure costs without calculating
cost-per-autonomous-task-completion, reducing the risk of
economic evaluation of agent efficiency.

**Benefits of establishing this best
practice:**

- Agent-specific metrics identify cost anomalies and enable
comparison of agent performance across the fleet.
- Per-phase token tracking reveals which reasoning phases consume
disproportionate tokens, enabling targeted optimization.
- Business-relevant metrics like cost-per-task-completion enable
economic evaluation of different reasoning strategies.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

The foundation of agent cost visibility is a tag taxonomy applied
consistently everywhere spend happens, like:

- agent-id
- agent-role (like supervisor, worker, and
specialist)
- workflow-id
- task-type
- Environment on every
[Amazon
Bedrock](https://aws.amazon.com/bedrock/) invocation and
[Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html) session

These tags are the primary key for all downstream cost
attribution. Activating tag-based cost allocation in AWS Cost Explorer generates per-agent and per-workflow reports without
custom pipeline work, so as soon as tagging is consistent, the
reports become usable.

[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) decomposes agent execution
into individual operations with token counts and latency through
distributed tracing. Per-phase tracking becomes possible because
you can attribute tokens to planning, execution, reflection, and
verification without manual instrumentation. The AgentCore Runtime
consumption-based pricing and microVM session isolation keep cost
boundaries aligned with execution boundaries, so the telemetry and
the billing see the same unit of work.

A single user request triggers multiple agents, each making
multiple model calls, tool invocations, and memory operations, so
raw invocation cost has to roll up through a hierarchy to be
useful. The aggregation pattern is:

- Collect per-invocation costs from Amazon Bedrock API responses
- Associate them with the parent agent using session tags
- Roll agent costs into workflow totals using
workflow-id
- Attribute workflow costs to tenants for multitenant
deployments

Once aggregation is in place, cost reports work at every level:
invocation-level for optimization, agent-level for performance
comparison, workflow-level for business justification, and
tenant-level for billing.

Publishing per-phase token counts as Amazon CloudWatch custom
metrics enables you to build dashboards for cost-per-decision,
cost-per-reasoning-cycle, and cost-per-task-completion segmented
by agent type. CloudWatch alarms on cost-per-task-completion
thresholds and AWS Budgets alerts for per-agent monthly spending
limits turn the tracking from a passive report into an active
signal that tells the team when an agent's economics have shifted.

### Implementation steps

- **Define and apply a standard tag
taxonomy:** Apply agent-id,
agent-role,
workflow-id,
task-type, and environment tags
consistently to all
[Amazon
Bedrock](https://aws.amazon.com/bedrock/) invocations and
[Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html) sessions, and enable AWS Cost Explorer tag-based cost allocation.
- **Enable end-to-end cost
traces:** Configure
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) to capture
distributed traces, and export telemetry to Amazon CloudWatch for per-operation cost analysis.
- **Aggregate costs
hierarchically:** Implement a Lambda function that
runs every 15 minutes to collect model inference, tool
invocation, and memory costs, storing aggregated results by
agent and session in a DynamoDB cost tracking table with
rollups from invocation to agent to workflow to tenant.
- **Build cost-per-task
dashboards:** Create CloudWatch dashboards
displaying cost-per-decision, cost-per-reasoning-cycle, and
cost-per-task-completion by agent type.
- **Configure alerts and
budgets:** Set AWS Budgets alerts for per-agent
monthly spending limits and CloudWatch alarms for
cost-per-task-completion thresholds.

## Resources

**Related best practices:**

- [AGENTCOST05-BP02
Implement distributed cost tracing for multi-agent
workflows](agentcost05-bp02.html)
- [AGENTCOST05-BP03 Design
tenant-aware cost allocation for AaaS pricing models](agentcost05-bp03.html)
- [AGENTCOST05-BP04 Create
chargeback and ROI reporting](agentcost05-bp04.html)
- [AGENTCOST07-BP02
Establish proactive anomaly detection for agent cost
patterns](agentcost07-bp02.html)

**Related documents:**

- [Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html)
- [Using
cost allocation tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html)
- [Economics
for agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-economics/index.html)
- [Guidance
for Cost Analysis and Optimization with Amazon Bedrock
Agents](https://aws.amazon.com/solutions/guidance/cost-analysis-and-optimization-with-amazon-bedrock-agents/)

**Related videos:**

- [AWS 2025 - AgentCore Observability: Monitor and Debug with
OpenTelemetry](https://www.youtube.com/watch?v=wWQgawUPr1k)

**Related examples:**

- [GitHub:
awslabs/amazon-bedrock-agentcore-samples - Observability
tutorials](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/06-AgentCore-observability)

**Related workshops:**

- [Diving
Deep into Bedrock AgentCore - Observability](https://catalog.workshops.aws/agentcore-deep-dive/en-US/70-agentcore-observability)

**Related services:**

- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
- [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/)
- [AWS Budgets](https://aws.amazon.com/aws-cost-management/aws-budgets/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentcost05-bp01.html*

---

# AGENTCOST05-BP02 Implement distributed cost tracing for multi-agent workflows

In multi-agent workflows, aggregate cost tells you how much you
spent but not where those specific costs came from. Tracing with
workflow IDs propagating across agent boundaries makes workflow
costs more clear, as it is broken down into worker execution, tool
invocations, and memory operations, which helps you make data-driven
architectural optimization decisions.

**Desired outcome:**

- You propagate workflow trace IDs through every agent invocation,
tool call, and memory operation.
- You calculate true cost-per-workflow-completion, with
orchestration overhead tracked separately from execution cost.
- You compare efficiency across different collaboration patterns
using real cost data.
- You visualize workflow cost by pattern, agent role, and business
outcome.

**Common anti-patterns:**

- Tracking costs for individual agents without workflow-level
correlation, making it impossible to calculate true
cost-per-workflow-completion.
- Combining supervisor and worker costs into a single metric,
obscuring whether workflows suffer from excessive orchestration
overhead.
- Deploying one multi-agent pattern without measuring cost
differences between alternatives, missing architectural cost
reduction.
- Analyzing total costs without role-based breakdowns, reducing
the risk of identification of which agent types drive the
highest spending and require targeted optimization.

**Benefits of establishing this best
practice:**

- Full workflow cost visibility enables calculation of true
cost-per-workflow-completion across agent boundaries.
- Orchestration overhead ratios reveal when coordination consumes
a disproportionate share of workflow spending.
- Cost comparison across collaboration patterns turns architecture
decisions from guesswork into data-driven choices.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Workflow-level cost visibility starts with a workflow trace ID
generated at workflow initiation and propagated through every
agent invocation, tool call, and memory operation. Without that
correlation key, per-agent costs can't be stitched into a
per-workflow total, and it becomes difficult to determine how
expensive it is to deliver one business outcome.
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) provides a three-tiered
hierarchy that maps directly to this problem: sessions for
complete workflows, traces for individual agent invocations, and
spans for operation-level granularity. For agents on
[Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html), session isolation keeps cost
boundaries aligned with agent execution boundaries, so no complex
allocation formulas are required.

The most useful decomposition within a workflow is the
orchestrator-compared to-worker split. Tag supervisor invocations
with agent-role:orchestrator and worker
invocations with agent-role:worker, then
compute the orchestration overhead ratio as orchestrator cost
divided by total workflow cost. A high ratio indicates
coordination is dominating execution, which typically signals a
hierarchy that needs flattening or manifests that need
compression. Breaking workflow cost further into orchestration
tokens, worker execution tokens, tool invocation costs, and memory
retrieval costs tells you which component to optimize first.

Cost data alone can be misleading without quality data to
correlate.
[Amazon
Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html) measures output quality
alongside cost, which turns optimization into a trade-off decision
rather than a single-axis minimization. A cheaper workflow pattern
that degrades quality isn't actually cheaper in business terms,
and the evaluation overlay makes that trade-off explicit.

Routing a percentage of executions to alternative collaboration
patterns and comparing cost-per-workflow-completion across
patterns in Amazon CloudWatch dashboards and AWS Cost Explorer
lets teams pick architectures based on real behavior, not
theoretical cost models. For patterns that specifically optimize
supervisor costs, see
[AGENTCOST01-BP03
Implement cost-effective patterns like hybrid supervisor for
multi-agent coordination](agentcost01-bp03.html).

### Implementation steps

- **Enable distributed tracing across
agents:** Configure
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) to capture
distributed traces, exporting telemetry to Amazon CloudWatch
with workflow trace IDs propagated through every invocation.
- **Apply role-based tagging and compute
overhead ratios:** Tag every invocation with
agent-role (orchestrator or worker), and calculate the
orchestration overhead ratio per workflow type.
- **Visualize cost by pattern and alarm
on thresholds:** Build CloudWatch dashboards
showing workflow cost distributions by collaboration pattern
and agent role, with alarms when orchestration overhead
exceeds thresholds.
- **Run pattern experiments:**
Route a percentage of executions to alternative
collaboration patterns and compare
cost-per-workflow-completion across patterns.
- **Compare workflow efficiency in Cost Explorer:** Use AWS Cost Explorer to compare
efficiency across different collaboration patterns over
time.
- **Decompose workflow cost:**
Deploy cost aggregation functions that break total workflow
cost into orchestration tokens, worker execution tokens,
tool invocation costs, and memory retrieval costs for each
workflow type.

## Resources

**Related best practices:**

- [AGENTCOST01-BP02
Optimize multi-agent collaboration cost through efficient
handoff patterns](agentcost01-bp02.html)
- [AGENTCOST01-BP03
Implement cost-effective patterns like hybrid supervisor for
multi-agent coordination](agentcost01-bp03.html)
- [AGENTCOST05-BP01
Establish agent-level reasoning cost tracking and
attribution](agentcost05-bp01.html)
- [AGENTCOST05-BP03 Design
tenant-aware cost allocation for AaaS pricing models](agentcost05-bp03.html)

**Related documents:**

- [Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html)
- [Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html)
- [Economics
for agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-economics/index.html)
- [Guidance
for Cost Analysis and Optimization with Amazon Bedrock
Agents](https://aws.amazon.com/solutions/guidance/cost-analysis-and-optimization-with-amazon-bedrock-agents/)

**Related videos:**

- [AWS 2025 - AgentCore Observability: Monitor and Debug with
OpenTelemetry](https://www.youtube.com/watch?v=wWQgawUPr1k)
- [AWS re:Invent 2024 - Balance cost, performance & reliability
for AI at enterprise scale (AIM3304)](https://www.youtube.com/watch?v=Lwvv8Q33eeE)

**Related examples:**

- [GitHub:
awslabs/amazon-bedrock-agentcore-samples - Observability
tutorials](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/06-AgentCore-observability)

**Related services:**

- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
- [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentcost05-bp02.html*

---

# AGENTCOST05-BP03 Design tenant-aware cost allocation for agent as a service (AaaS) pricing models

Agent as a service (AaaS) offerings without per-tenant cost
attribution can bill only by capacity estimates, can't detect noisy
neighbors until infrastructure has already scaled, and can't decide
when a tenant should move to dedicated infrastructure. Propagating
tenant context through every operation and tracking cost at the
tenant level fixes all three problems at once.

**Desired outcome:**

- You propagate tenant identifiers through all agent operations:
model invocations, tool executions, memory operations, and data
storage.
- You have flexible cost allocation models supporting
per-decision, per-task, and per-agent-hour pricing.
- You detect noisy neighbors before they drive infrastructure
scaling that affects all customers.
- You enforce tenant-level budget controls that cap per-tenant
spending.

**Common anti-patterns:**

- Tracking agent costs only at the account level without tenant
context, making it impossible to generate accurate tenant
invoices.
- Allowing high-usage tenants to consume shared resources without
detection, driving infrastructure scaling costs that affect all
customers.
- Implementing only one billing approach because the cost
allocation system can't support multiple pricing dimensions.
- Allowing unbounded agent costs without tenant-level usage
limits, creating financial risk when unexpected usage spikes
occur.
- Building agent as a service offerings with a single fixed
pricing model, reducing the risk of revenue optimization based
on actual usage patterns.

**Benefits of establishing this best
practice:**

- Per-tenant cost tracking enables billing based on actual
resource consumption rather than capacity-based estimates.
- Noisy neighbor detection and tenant-level throttling help
prevent unexpected infrastructure scaling from aggressive usage
patterns.
- Cost allocation data enables data-driven decisions about when
dedicated infrastructure becomes more cost-effective than pooled
resources.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Tenant context has to travel with every billable event.
[Amazon
Bedrock AgentCore Identity](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity.html) tags workload identities,
credential providers, and API key providers with tenant metadata
that propagates through downstream operations. Those tags
integrate with AWS Cost Explorer for per-tenant cost breakdowns
without requiring separate AWS accounts per tenant. For agents on
[Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html), session-based architecture
provides natural tenant boundaries, and consumption-based pricing
means each session's bill reflects actual work done for that
tenant.

[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) captures all billable
events with tenant identifiers in metric dimensions: token
consumption, tool invocation costs from
[Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html), and memory operation costs from
[Amazon
Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html). Tenant-level quota enforcement
lives in
[Amazon
Bedrock AgentCore Policy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html) with Cedar policies, which is how
you cap per-tenant spending without pushing the enforcement into
application code where it can be bypassed.

A *noisy neighbor* is a virtual machine or
container that consumes disproportionate system resources. Noisy
neighbor detection needs a baseline and a deviation threshold that
reflect how agent reasoning depth actually varies. Some tenants
execute simple single-step decisions, while others trigger complex
multi-turn reasoning chains. An Amazon CloudWatch alarm when a
tenant's consumption exceeds three times their historical baseline
catches abnormal usage early enough to help prevent infrastructure
scaling that increases costs for every customer. The threshold is
tuned per workload to avoid under- or over-firing.

Resource-sharing decisions need a cost model. Pooled
infrastructure achieves higher utilization and lower per-tenant
costs but requires strong isolation. Dedicated infrastructure
provides stronger isolation and predictable performance at higher
fixed costs. Build a per-tenant break-even model that calculates
when a tenant's usage would be cheaper on dedicated infrastructure
than on their proportional share of pooled resources, and use it
to offer dedicated deployments to tenants who have crossed that
line.

### Implementation steps

- **Tag identities for tenant
attribution:** Configure
[Amazon
Bedrock AgentCore Identity](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity.html) with tenant-specific tags
on workload identities, and activate the
tenant-id cost allocation tag in the AWS
billing console.
- **Deploy agents with session-level
tenant tags:** Run agents on
[Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html) with session-level tenant
tagging so cost attribution follows the session, not the
pool.
- **Capture all cost dimensions per
tenant:** Configure
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) to export telemetry
to Amazon CloudWatch with tenant identifiers in metric
dimensions.
- **Enforce tenant quotas and noisy
neighbor detection:** Implement tenant-level quota
enforcement through
[Amazon
Bedrock AgentCore Policy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html), and set CloudWatch alarms
for consumption spikes exceeding three times the tenant's
historical baseline.
- **Build a flexible pricing
engine:** Support per-decision, per-task, and
per-agent-hour billing models with tenant-specific
configurations so pricing can evolve without re-architecting
the billing pipeline.
- **Model pooled compared to dedicated
break-even:** Use AWS Cost Explorer API data to
calculate the break-even point per tenant, identifying
tenants approaching the threshold where dedicated AgentCore
deployments become cost-effective.

## Resources

**Related best practices:**

- [AGENTCOST05-BP01
Establish agent-level reasoning cost tracking and
attribution](agentcost05-bp01.html)
- [AGENTCOST05-BP02
Implement distributed cost tracing for multi-agent
workflows](agentcost05-bp02.html)
- [AGENTCOST05-BP04 Create
chargeback and ROI reporting](agentcost05-bp04.html)

**Related documents:**

- [Amazon
Bedrock AgentCore Identity](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity.html)
- [Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html)
- [Manage
multi-tenant Amazon Bedrock costs using application inference
profiles](https://aws.amazon.com/blogs/machine-learning/manage-multi-tenant-amazon-bedrock-costs-using-application-inference-profiles/)
- [AWS SaaS Lens](https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/saas-lens.html)
- [Using
cost allocation tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html)

**Related videos:**

- [AWS re:Invent 2024 - Building multi-tenant SaaS agents with
AgentCore (SAS407)](https://www.youtube.com/watch?v=uwXrtyXXuy8)

**Related examples:**

- [GitHub:
awslabs/amazon-bedrock-agentcore-samples - Observability
tutorials](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/06-AgentCore-observability)

**Related services:**

- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentcost05-bp03.html*

---

# AGENTCOST05-BP04 Create chargeback and ROI reporting

Raw token counts and execution durations are the wrong unit of
measure for business stakeholders deciding whether to fund agent
capabilities. Translating technical cost into business metrics like
cost-per-customer-interaction and comparing against the manual
processes agents replace turns agent economics into something
non-technical leaders can evaluate against familiar frameworks.

**Desired outcome:**

- You translate technical agent costs into business metrics
through automated chargeback reports.
- You demonstrate agent ROI by comparing agent costs against the
manual processes they replace.
- You allocate cost by business unit to create accountability.
- You provide self-service cost dashboards so business teams can
act without engineering bottlenecks.

**Common anti-patterns:**

- Providing only raw technical cost data (like token counts or
Lambda execution times) without converting to business metrics
like cost-per-customer-interaction.
- Reporting agent costs in isolation without comparing to the
manual processes they replace, reducing the risk of stakeholders
evaluating automation ROI.
- Restricting cost data access to engineering teams, creating
bottlenecks that delay optimization decisions.
- Presenting only quantitative dashboards without qualitative
context, requiring business stakeholders to rely on engineering
to interpret cost changes and recommend actions.

**Benefits of establishing this best
practice:**

- Business-aligned metrics enable non-technical stakeholders to
evaluate agent investments using familiar frameworks.
- ROI comparison against manual processes demonstrates automation
value and justifies continued investment.
- Self-service cost dashboards reduce dependency on engineering
for cost analysis, accelerating optimization decisions.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Business metrics work together with technical telemetry, but they
require a translation layer to make sense to stakeholders.
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) produces the raw data
(session count, token usage, execution duration) through Amazon CloudWatch integration, and
[Amazon
Bedrock AgentCore Identity](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity.html) tags resources with business
dimensions (like business-unit,
product-line, and
customer-segment). Enabling AWS Cost Explorer
tag-based cost allocation generates per-business-unit reports. The
translation layer converts those technical units into
cost-per-customer-interaction, cost-per-automated-decision, and
cost-per-business-outcome, Those are the units that stakeholders
can compare against other investments.

ROI demonstration needs a baseline cost model for the manual
process the agent replaces: handling time, fully-loaded labor
cost, error rate, and throughput limitations. The ROI calculation
is the delta between that baseline and the agent's actual cost.
Executives may not read CloudWatch dashboards, so build a BI layer
with [Amazon Quick](https://aws.amazon.com/quicksuite/) fed by
[AWS Cost and Usage Reports](https://aws.amazon.com/aws-cost-management/aws-cost-and-usage-reporting/) and AgentCore Observability data.
CloudWatch dashboards remain the operational tool for engineering,
while Amazon Quick becomes the executive-facing tool for chargeback
and ROI.

Narrative generation makes cost reports useful for non-technical
audiences. Use a small
[Amazon
Bedrock](https://aws.amazon.com/bedrock/) model invoked weekly by AWS Lambda to produce
plain-language summaries of cost drivers with specific
optimization recommendations and quantified savings estimates.
Schedule the narrative generation with Amazon EventBridge
Scheduler and distribute through Amazon SNS to business unit
owners. A monthly review cadence helps you share cumulative
savings and recommendations with stakeholders.

### Implementation steps

- **Propagate business dimension
tags:** Configure
[Amazon
Bedrock AgentCore Identity](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity.html) with business-unit and
product-line tags propagated through all agent resources for
AWS Cost Explorer reporting.
- **Build a baseline cost
model:** Capture pre-automation process costs (like
handling time, fully-loaded labor cost, error rate, and
throughput) and implement ROI calculation logic comparing
agent costs against the baseline.
- **Translate technical costs to
business metrics:** Implement a cost translation
layer that maps raw invocation costs to cost-per-decision
and cost-per-task-completion, capturing how many business
outcomes each dollar of agent spending delivers.
- **Build executive-facing BI
dashboards:** Use
[Amazon Quick](https://aws.amazon.com/quicksuite/) fed by
[AWS Cost and Usage Reports](https://aws.amazon.com/aws-cost-management/aws-cost-and-usage-reporting/) and
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) data, displaying ROI
trends and cost allocation by business unit.
- **Automate narrative
generation:** Invoke a small
[Amazon
Bedrock](https://aws.amazon.com/bedrock/) model weekly from AWS Lambda to produce
plain-language cost summaries that explain cost drivers,
optimization actions taken, and specific recommendations
with estimated savings.
- **Keep operational dashboards in
CloudWatch:** Use Amazon CloudWatch dashboards for
operational cost monitoring by engineering teams, separate
from executive-facing reporting.
- **Establish a monthly review
cadence:** Share cost narratives and optimization
recommendations with business stakeholders each month,
closing the loop between reporting and action.

## Resources

**Related best practices:**

- [AGENTCOST05-BP01
Establish agent-level reasoning cost tracking and
attribution](agentcost05-bp01.html)
- [AGENTCOST05-BP03 Design
tenant-aware cost allocation for AaaS pricing models](agentcost05-bp03.html)
- [AGENTCOST07-BP03
Create systematic optimization feedback loops for continuous
improvement](agentcost07-bp03.html)

**Related documents:**

- [Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html)
- [Economics
for agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-economics/index.html)
- [Preparing
the business for agentic AI at scale](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-operationalizing-agentic-ai/preparing-business.html)
- [Guidance
for Cost Analysis and Optimization with Amazon Bedrock
Agents](https://aws.amazon.com/solutions/guidance/cost-analysis-and-optimization-with-amazon-bedrock-agents/)
- [Amazon Quick User Guide](https://docs.aws.amazon.com/quicksuite/latest/user/welcome.html)
- [AWS Cost and Usage Reports](https://docs.aws.amazon.com/cur/latest/userguide/what-is-cur.html)

**Related examples:**

- [GitHub:
awslabs/amazon-bedrock-agentcore-samples - Observability
tutorials](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/06-AgentCore-observability)

**Related services:**

- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon Quick](https://aws.amazon.com/quicksuite/)
- [AWS Cost and Usage Reports](https://aws.amazon.com/aws-cost-management/aws-cost-and-usage-reporting/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
- [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentcost05-bp04.html*

---
