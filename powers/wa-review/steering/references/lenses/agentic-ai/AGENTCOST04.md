# AGENTCOST04 — Agent tool serving cost optimization

**Pillar**: Cost Optimization  
**Best Practices**: 3

---

# AGENTCOST04-BP01 Design cost effective tool selection to minimize unnecessary invocations

Often, the most cost-effective tool call is the one an agent decides
not to make because the answer is already in context. Context-first
reasoning, cost-ranked selection, and duplicate detection tie tool
invocation to the value of the information retrieved.

**Desired outcome:**

- You have agents checking context and managed memory before
invoking tools.
- You have a cost-ranked selection rubric that points agents to
cheaper alternatives first.
- You batch requests where possible and cache results within
sessions to avoid duplicate calls.
- You monitor per-tool invocation frequency and cache hit rates as
distinct metrics.

**Common anti-patterns:**

- Invoking tools without checking whether required information
already exists in context or managed memory, adding cost without
improving results.
- Creating narrow tool interfaces that return minimal data,
forcing follow-up calls to assemble complete context.
- Implementing retry logic without exponential backoff or
automatic cutoffs, causing retry storms that multiply costs
during service degradation.
- Operating without tool invocation metrics, so no one can
identify which tools are most expensive or most frequently
called.

**Benefits of establishing this best
practice:**

- Context-first evaluation reduces unnecessary tool invocations
for agents with rich context from prior reasoning steps.
- Cost-ranked tool selection rubrics direct agents to cheaper
alternatives, reserving expensive external APIs for cases where
lower-cost options are insufficient.
- Batched tool interfaces and complete result sets reduce per-call
overhead and the need for follow-up invocations.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Tool necessity belongs in the agent's reasoning prompt, not as an
afterthought in monitoring. The system prompt should instruct the
model to assess whether the answer can be derived from information
already in context, from conversation history stored in
[Amazon
Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html), or from prior tool results within
the same reasoning cycle, before selecting a tool. Pair this with
a cost-ranked selection rubric that places cheaper alternatives
first: if a local computation or a cached result produces the same
answer as an external API call, the agent should take the cheaper
path.

Tool interface design matters as much as agent instructions.
Narrow interfaces that return minimal data force agents to make
follow-up calls to assemble the context they need, which inflates
per-reasoning-cycle tool cost.
[Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) provides MCP-based tool discovery
with composition features that combine multiple APIs into single
endpoints, reducing invocation overhead. Design tool interfaces to
accept batch inputs and return complete result sets so a single
call does the work of many.

Consider how you implement duplicate detection. Agents often
invoke the same tool with identical parameters across reasoning
iterations, especially when revisiting a branch. Implement a
session-scoped tool result cache in your action group Lambda
functions or AgentCore Gateway MCP servers so the agent doesn't
re-invoke the same tool with the same parameters. Store results in
AgentCore Memory's short-term memory so the agent's reasoning
prompt can reveal prior results before deciding to make another
call.

For enforcement and measurement,
[Amazon
Bedrock AgentCore Policy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html) applies Cedar policies that halt
retries when failure rates indicate persistent degradation and cap
tool calls per reasoning cycle.
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) exposes tool selection
patterns, Amazon CloudWatch tracks invocation frequency and
deduplication hit rates, and
[Amazon
Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html) scores tool selection
accuracy so patterns of over-invocation appear as quality data,
not just cost data.

### Implementation steps

- **Embed tool necessity evaluation in
system prompts:** Direct the model to check context
and
[Amazon
Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) before invoking tools, and
include a cost-ranked selection rubric that places cheaper
alternatives first.
- **Redesign tool interfaces for
batching:** Expose tools through
[Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) with batch inputs and
complete result sets so one call carries the payload that
previously required several.
- **Cache tool results within
sessions:** Implement session-scoped caches in
action group Lambda functions or Gateway MCP servers to
deduplicate identical tool calls, storing results in
AgentCore Memory so the agent can surface them before the
next call.
- **Apply automatic cutoffs through
policy:** Configure
[Amazon
Bedrock AgentCore Policy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html) Cedar policies that cap tool
calls per reasoning cycle and halt retries on persistent
failures.
- **Monitor tool selection
patterns:** Use
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) to surface tool
selection patterns and create Amazon CloudWatch metrics for
tool invocation frequency and deduplication hit rates.
- **Score tool selection
accuracy:** Use
[Amazon
Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html) to periodically score
tool selection accuracy, flagging patterns where agents
choose expensive tools when cheaper alternatives would
suffice.

## Resources

**Related best practices:**

- [AGENTCOST01-BP01
Use the reflection pattern to design efficient agent reasoning
loops](agentcost01-bp01.html)
- [AGENTCOST02-BP02
Cost optimize token consumption through efficient prompt
engineering](agentcost02-bp02.html)
- [AGENTCOST04-BP02 Cost
optimize tool serving through serverless and resource
sharing](agentcost04-bp02.html)
- [AGENTCOST04-BP03
Implement intelligent caching and failure handling for tool
results](agentcost04-bp03.html)
- [AGENTCOST05-BP01
Establish agent-level reasoning cost tracking and
attribution](agentcost05-bp01.html)

**Related documents:**

- [Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html)
- [Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html)
- [Amazon
Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html)
- [Guidance
for Cost Analysis and Optimization with Amazon Bedrock
Agents](https://aws.amazon.com/solutions/guidance/cost-analysis-and-optimization-with-amazon-bedrock-agents/)

**Related videos:**

- [AWS 2025 - AgentCore Deep Dive: Gateway](https://www.youtube.com/watch?v=atWXM5lziY8)
- [AWS re:Invent 2024 - Scale agent tools with AgentCore Gateway
(AIM3313)](https://www.youtube.com/watch?v=DlIHB8i6uyE)
- [Integrating
MCP Tools with Strands Agents](https://www.youtube.com/watch?v=bHSbjCZZFjE)

**Related examples:**

- [GitHub:
awslabs/amazon-bedrock-agentcore-samples - Gateway
tutorials](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/02-AgentCore-gateway)

**Related workshops:**

- [Diving
Deep into Bedrock AgentCore - Gateway](https://catalog.workshops.aws/agentcore-deep-dive/en-US/30-agentcore-gateway)

**Related tools:**

- [Strands
Agents MCP Tools](https://strandsagents.com/docs/user-guide/concepts/tools/mcp-tools/)

**Related services:**

- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentcost04-bp01.html*

---

# AGENTCOST04-BP02 Cost optimize tool serving through serverless and resource sharing

Tool infrastructure that runs constantly to serve unpredictable
agent traffic carries the highest idle cost in an agent stack.
Serverless tool serving with shared infrastructure across agents
aligns spend with actual invocations and removes the fixed overhead
of per-agent dedicated instances.

**Desired outcome:**

- You have tool-serving infrastructure that scales dynamically
with agent usage and charges only for actual invocations.
- You share stateless tool services across agents while
maintaining security isolation.
- You use private networking and compact serialization to reduce
data transfer costs on high-frequency tool invocations.
- You track per-agent cost attribution for targeted optimization.

**Common anti-patterns:**

- Running persistent servers for tool serving that incur charges
during hours or days when no agents invoke tools.
- Creating dedicated tool server instances per agent rather than
shared stateless services, producing dozens of underutilized
servers.
- Routing tool invocations through NAT Gateways when agents and
tools live in the same VPC, incurring unnecessary per-GB data
processing charges.

**Benefits of establishing this best
practice:**

- Serverless tool serving scales to zero when agents are inactive,
reducing idle costs through consumption-based pricing.
- Shared tool infrastructure spreads fixed hosting overhead across
all agents while maintaining security isolation.
- VPC endpoints and compact serialization reduce data transfer
costs for high-frequency tool invocations.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Agent tool traffic is inherently bursty. An agent fleet is active
during business hours, idle overnight, and heavily uneven across
agent types. Provisioned tool infrastructure pays for that shape
by keeping compute warm through idle hours, which can be a
significant hidden cost in agent stacks.
[Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) provides fully-managed,
serverless tool serving that converts APIs and existing services
into MCP-compatible tools without infrastructure management.
AgentCore Gateway handles authentication, scales automatically,
and combines multiple APIs into unified endpoints.

Because tools exposed through AgentCore Gateway are available to
all authorized agents, one endpoint can serve an entire fleet
rather than one endpoint per agent.
[Amazon
Bedrock AgentCore Identity](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity.html) and
[Amazon
Bedrock AgentCore Policy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html) supply the fine-grained access
control that keeps sharing safe.

For tools that need extended execution,
[Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html) supports workloads up to 8 hours
with consumption-based pricing calculated at per-second
increments. Consumption pricing is the right default for
unpredictable tool invocation patterns because it charges only
during active processing.

Cold starts are a failure mode worth planning for. A cold tool
extends the agent's reasoning cycle and may trigger retries, which
can push per-session token costs up on cold paths. Monitor cold
start frequency in Amazon CloudWatch and evaluate Lambda SnapStart
or scheduled warming when cold starts are material.

Networking and serialization are the foundation of planning for
these failure modes. VPC endpoints for private data paths avoid
NAT Gateway processing charges for high-frequency tool invocations
between agents and tools in the same VPC. Compact JSON (or binary
formats where supported) reduces payload sizes on repeated
high-frequency calls. Tagging every invocation with agent ID and
workflow ID lets
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) and AWS Cost Explorer
reveal which agents and tools drive the highest spend.

### Implementation steps

- **Expose tools through serverless
Gateway:** Deploy agent tools through
[Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) MCP server capabilities for
serverless infrastructure with automatic scaling and shared
access across agents.
- **Apply fine-grained access
control:** Configure
[Amazon
Bedrock AgentCore Policy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html) Cedar policies for per-agent
tool access, preserving security isolation while sharing
infrastructure.
- **Attribute cost per agent:**
Use
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) telemetry tags with
agent ID and workflow ID, and generate periodic AWS Cost Explorer reports by agent and tool type.
- **Monitor invocation patterns and cold
starts:** Expose tool invocation patterns through
AgentCore Observability, and set Amazon CloudWatch alarms
for patterns that exceed expected bounds, including cold
start frequency.

## Resources

**Related best practices:**

- [AGENTCOST04-BP01 Design
cost effective tool selection to minimize unnecessary
invocations](agentcost04-bp01.html)
- [AGENTCOST04-BP03
Implement intelligent caching and failure handling for tool
results](agentcost04-bp03.html)
- [AGENTCOST05-BP01
Establish agent-level reasoning cost tracking and
attribution](agentcost05-bp01.html)

**Related documents:**

- [Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html)
- [Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html)
- [Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html)
- [Guidance
for Cost Analysis and Optimization with Amazon Bedrock
Agents](https://aws.amazon.com/solutions/guidance/cost-analysis-and-optimization-with-amazon-bedrock-agents/)

**Related videos:**

- [AWS 2025 - AgentCore Deep Dive: Gateway](https://www.youtube.com/watch?v=atWXM5lziY8)
- [AWS 2025 - AgentCore Deep Dive: Runtime](https://www.youtube.com/watch?v=wizEw5a4gvM)

**Related examples:**

- [GitHub:
awslabs/amazon-bedrock-agentcore-samples - Gateway
tutorials](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/02-AgentCore-gateway)

**Related workshops:**

- [Getting
started with Amazon Bedrock AgentCore - Lab 3: Gateway,
Identity & Policy](https://catalog.workshops.aws/agentcore-getting-started/en-US/50-add-tool-gateway)
- [Diving
Deep into Bedrock AgentCore - Gateway](https://catalog.workshops.aws/agentcore-deep-dive/en-US/30-agentcore-gateway)

**Related services:**

- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
- [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentcost04-bp02.html*

---

# AGENTCOST04-BP03 Implement intelligent caching and failure handling for tool results

Tool costs can be unpredictable when agents repeat identical or
equivalent calls, and they can spike sharply when retries run
unbounded through a service outage. Two-layer caching, schema
validation, and automatic cutoffs convert those failure modes into
predictable, bounded costs.

**Desired outcome:**

- You have session-scoped and cross-session semantic caches
reducing redundant tool invocations.
- You validate tool inputs against JSON Schema before invocation
to help prevent wasted calls on malformed requests.
- You have automatic cutoffs that halt retries when failure rates
exceed thresholds, with automatic fallback to alternative tools.
- You track cache hit rates and retry costs as distinct metrics.

**Common anti-patterns:**

- Not caching frequently used tool results, making repeated
identical calls within the same session that waste compute and
external API costs.
- Using only exact-match caching when agents phrase the same
request differently, missing cache hits for semantically
identical calls.
- Retrying failed tool invocations indefinitely without automatic
cutoffs, multiplying cost during service degradation without
resolving the underlying issue.
- Not validating tool input schemas before invocation, allowing
malformed calls to waste invocation cost without producing
usable results.

**Benefits of establishing this best
practice:**

- Two-layer caching reduces redundant tool invocations and
external API charges.
- Automatic cutoffs halt retries when failure rates exceed
thresholds, helping prevent expensive retry storms.
- Event-driven cache invalidation supports aggressive caching of
volatile data by purging stale results promptly when source data
changes.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Tool caching has to work at two scopes to cover both obvious and
non-obvious repetition. The session-scoped layer works through
[Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html) and catches duplicate calls
within a single agent session, which is a common failure mode when
agents revisit a reasoning branch. The cross-session layer uses
[Amazon OpenSearch Service Serverless](https://aws.amazon.com/opensearch-service/features/serverless/) for semantic caching: generate
embeddings of tool parameters and query for similar prior calls
above a cosine similarity threshold before invoking the tool. Each
cache entry's TTL should be calibrated to the underlying data's
volatility. For example, a weather API's freshness requirement is
minutes, while a static reference knowledge base tolerates hours
or days.

Schema validation can help prevent waste. Agents sometimes
generate tool calls with incorrect parameter types, missing
required fields, or invalid enum values, and those calls pay
tool-serving and external API costs for a response that can't be
used. JSON schema validation in the action group Lambda function
rejects malformed requests before they reach external APIs and
returns a validation error to the agent for correction.

Cache invalidation can help make aggressive caching safer.
Event-driven invalidation listens for source-data changes and
purges affected cache entries immediately, so volatile data can
still be cached without returning stale results. Without
event-driven invalidation, teams end up choosing between
aggressive TTLs (stale results) or short TTLs (low hit rates), and
both options leave cost on the table.

For failure handling,
[Amazon
Bedrock AgentCore Policy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html) Cedar policies enforce automatic
cutoffs when failure rates exceed thresholds, halting retry storms
during service degradation. Automatic fallback to alternative
tools maintains agent functionality during outages, and retry
budgets per reasoning session cap total retry attempts using
exponential backoff with jitter. Cache and retry telemetry is
exposed through
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) and Amazon CloudWatch: hit
rates per layer, cutoff state transitions, and retry cost as a
percentage of total tool cost. For caching that extends beyond
tool results into model invocations, see
[AGENTCOST02-BP03
Use intelligent caching to reduce redundant model
invocations](agentcost02-bp03.html).

### Implementation steps

- **Deploy two-layer caching:**
Implement a session-scoped in-process cache on
[Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html) and an
[Amazon OpenSearch Service Serverless](https://aws.amazon.com/opensearch-service/features/serverless/) semantic cache for
cross-session reuse, with TTLs calibrated per tool (short
for volatile data, long for static reference data).
- **Deploy semantic caching:**
Generate parameter embeddings and query OpenSearch
Serverless for similar prior calls above a cosine similarity
threshold before invoking the tool.
- **Validate tool inputs:**
Implement JSON Schema validation in action group Lambda
functions to reject malformed requests before they reach
external APIs, returning validation errors for the agent to
correct.
- **Enforce cutoffs and fallback
tools:** Configure
[Amazon
Bedrock AgentCore Policy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html) Cedar policies for automatic
cutoffs, wire automatic fallback to alternative tools when
cutoffs activate, and set retry budgets per reasoning
session.
- **Monitor cache and retry
metrics:** Create Amazon CloudWatch metrics for
cache hit rates, cutoff transitions, and retry costs using
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html), with alarms for
degraded performance.

## Resources

**Related best practices:**

- [AGENTCOST02-BP03
Use intelligent caching to reduce redundant model
invocations](agentcost02-bp03.html)
- [AGENTCOST04-BP01 Design
cost effective tool selection to minimize unnecessary
invocations](agentcost04-bp01.html)
- [AGENTCOST04-BP02 Cost
optimize tool serving through serverless and resource
sharing](agentcost04-bp02.html)
- [AGENTCOST05-BP01
Establish agent-level reasoning cost tracking and
attribution](agentcost05-bp01.html)

**Related documents:**

- [Amazon
Bedrock AgentCore Policy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html)
- [Optimize
LLM response costs and latency with effective caching](https://aws.amazon.com/blogs/database/optimize-llm-response-costs-and-latency-with-effective-caching/)
- [Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html)
- [Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html)
- [Economics
for agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-economics/index.html)

**Related videos:**

- [AWS 2025 - AgentCore Deep Dive: Runtime](https://www.youtube.com/watch?v=wizEw5a4gvM)

**Related examples:**

- [GitHub:
awslabs/amazon-bedrock-agentcore-samples - Gateway
tutorials](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/02-AgentCore-gateway)

**Related services:**

- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon OpenSearch Service](https://aws.amazon.com/opensearch-service/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentcost04-bp03.html*

---
