# AGENTSUS02 — Resource right-sizing

**Pillar**: Sustainability  
**Best Practices**: 4

---

# AGENTSUS02-BP01 Optimize context management and memory utilization

Agent memory that grows without bounds forces every retrieval to
search through increasingly large stores and every turn to reprocess
history the agent has already seen. Tiered memory with retention
policies keeps infrastructure scaled to the context that actually
matters, so memory operations stay fast and memory cost stays
proportional to use.

**Desired outcome:**

- You have tiered memory with active session context separated
from archival data, so hot and cold tiers are not competing for
the same storage.
- Retention, archival, and pruning policies keep memory bounded
and automatically move aging context to the appropriate tier.
- Multi-agent systems share persistent context through namespaces
rather than duplicating it per agent.
- Agents incrementally build context rather than reprocessing full
interaction histories on every turn.

**Common anti-patterns:**

- Implementing flat memory without tiering, so hot session context
competes with archival data for the same storage and access
path.
- Skipping retention, archival, and pruning policies, letting
memory accumulate indefinitely and forcing each retrieval to
scan a larger and larger store.
- Reprocessing complete historical context on every turn instead
of pulling only the relevant slice, producing redundant
retrieval operations that don't improve response quality.
- Duplicating shared context across each agent's memory store
rather than reading from a shared namespace, producing linear
storage growth with agent count.

**Benefits of establishing this best
practice:**

- Memory infrastructure scales with the context that actually
matters, not with cumulative history.
- Semantic retrieval returns the relevant slice of context in
constant time rather than scaling with store size.
- Multi-agent systems share storage for common context, reducing
duplicated memory across the fleet.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Not all agent context is equally active. A recent turn in an
ongoing session behaves very differently from a transcript from
three months ago. The first needs millisecond access on every
turn, and the second needs availability for occasional retrieval.
[Amazon
Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) provides built-in tiering that
separates these cases, with working memory optimized for active
sessions and long-term storage for older context. Retention
policies move context between tiers automatically, so the hot tier
stays small and the cold tier stays cheap.

Shared persistent context is a part of the architecture where many
multi-agent systems fail. When five agents each maintain their own
copy of the same reference material, storage grows five times
faster than the organizational demand warrants. AgentCore Memory's
namespace-based organization lets multiple agents read from and
write to common namespaces scoped by IAM policies, one store and
many readers. This is shared storage, not shared in-process
memory, so consistency and access control stay explicit.
Separately,
[Amazon
Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html) is the right home for
organizational knowledge, FAQs, and reference documentation that
agents query to enrich context. It complements AgentCore Memory
rather than replaces it.

Sending the full interaction history into every model call looks
correct but pays to reprocess information the model already saw.

The better pattern is incremental. Maintain stateful sessions that
preserve working context across turns, summarize older segments
into compact representations when they age out of the immediate
window, and use semantic search through Knowledge Bases with
vector embeddings to retrieve only the relevant slice of history
rather than the whole transcript.
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) exposes which memory
operations are frequent and which tiers are under- or
over-utilized, so allocation stays grounded in actual usage.

### Implementation steps

- **Configure tiered memory with
lifecycle policies:** Use
[Amazon
Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) for active session context
with retention policies that automatically move aging
context to long-term storage.
- **Set up shared namespaces for
multi-agent context:** Create AgentCore Memory
namespaces that multiple agents read from and write to,
scoped by IAM policies, so shared persistent context is
stored once rather than duplicated per agent.
- **Use semantic retrieval for
historical context:** Configure
[Amazon
Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html) with vector embeddings so
queries retrieve only the relevant slice of historical
context rather than full transcripts.
- **Compress aging context:**
Apply summarization using Amazon Bedrock foundation models
to condense older interaction segments into compact
representations that preserve meaning at a fraction of the
token cost.
- **Monitor memory access patterns and
rebalance tiers:** Track tier hit rates, retrieval
latency, and store size through
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) and adjust retention
windows and tier allocations based on observed usage.

## Resources

**Related best practices:**

- [AGENTSUS02-BP02
Establish efficient agent caching strategies](agentsus02-bp02.html)
- [AGENTSUS02-BP03
Appropriately scale data, networking, and compute
dependencies](agentsus02-bp03.html)
- [SUS02-BP01
Scale workload infrastructure dynamically](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_user_a2.html)

**Related documents:**

- [Amazon
Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html)
- [Amazon
Bedrock AgentCore Memory: Building context-aware agents](https://aws.amazon.com/blogs/machine-learning/amazon-bedrock-agentcore-memory-building-context-aware-agents/)
- [Building
smarter AI agents: AgentCore long-term memory deep dive](https://aws.amazon.com/blogs/machine-learning/building-smarter-ai-agents-agentcore-long-term-memory-deep-dive/)
- [Amazon
Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html)
- [Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html)

**Related videos:**

- [AWS 2025 - AgentCore Deep Dive: Memory](https://www.youtube.com/watch?v=-N4v6-kJgwA)

**Related examples:**

- [GitHub:
awslabs/amazon-bedrock-agentcore-samples - Memory
tutorials](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/04-AgentCore-memory)

**Related services:**

- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon
Bedrock](https://aws.amazon.com/bedrock/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsus02-bp01.html*

---

# AGENTSUS02-BP02 Establish efficient agent caching strategies

Every duplicate model call, tool invocation, and memory lookup is
work the agent fleet has already done once. Caching at each
integration point turns repeated work into a one-time cost amortized
across every caller, so resource efficiency improves as usage
patterns stabilize rather than scaling linearly with traffic.

**Desired outcome:**

- You have caching applied at each integration point, prompt
prefixes, tool results, memory lookups, and credential
validation, with TTLs matched to data volatility.
- Cache layers are shared across the agent fleet so one agent's
cached result benefits every other agent.
- Cache hit rates are tracked per integration point and improve as
usage patterns stabilize.
- Invalidation policies help prevent stale responses where data
volatility demands freshness.

**Common anti-patterns:**

- Making repeated calls to the same foundation model with the same
stable prompt prefix instead of caching it, paying to reprocess
the same tokens on every invocation.
- Caching tool results and model responses without invalidation or
TTL policies, producing stale answers that appear fresh.
- Running caches isolated to each agent that don't share across
the fleet, so each agent has to re-warm its own cache rather
than benefiting from cached results elsewhere.
- Skipping cache instrumentation, so nobody knows which
integration points have low hit rates and would benefit from a
different caching strategy.

**Benefits of establishing this best
practice:**

- Redundant processing, API calls, and network traffic are reduced
at each integration point, so infrastructure cost grows
sublinearly with agent usage.
- Shared cache layers mean adding agents to the fleet increases
cache hit rate rather than cache pressure.
- Resource efficiency compounds over time as cache hit rates climb
toward their steady-state maximum.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

The sustainability view of prompt caching adds one additional
consideration to this lens' existing performance and cost
perspectives. The value of caching isn't just latency or cost for
each call. It's cumulative compute and energy footprint across the
lifetime of the fleet, and the way caching is shared determines
how that cumulative footprint grows.

Caches isolated to each agent don't compound. If five agents each
maintain their own cache, the fleet warms five caches instead of
one, and cross-agent hits never happen. Shared cache layers
exposed through
[Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) MCP server capabilities reverse
this. Every agent reads from and writes to the same cache tier, so
one agent's tool result becomes the next agent's cache hit. The
same principle applies at the authentication layer.
[Amazon
Bedrock AgentCore Identity](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity.html) caches tokens so credential
validation happens once per session across the fleet rather than
once for each agent.

[Amazon
Bedrock prompt caching](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-caching.html) pays off fastest. Stable system
prompts, the long preambles that set agent behavior, can be cached
at the model layer so subsequent invocations skip reprocessing the
prefix. Semantic caching adds a complementary layer where similar
(not identical) queries serve cached responses after an
embedding-based match, which is especially valuable for the long
tail of paraphrased questions users ask.

Invalidation is where caching strategies can fail. A cache TTL
calibrated to daily refresh on data that actually changes hourly
serves stale content. A TTL too short to matter wastes the cache's
whole purpose. Pick TTLs based on how often the underlying data
actually changes, and track hit rates through
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) so low-performing
strategies get tuned rather than left in place.

### Implementation steps

- **Enable prompt caching for stable
prefixes:** Turn on
[Amazon
Bedrock prompt caching](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-caching.html) for stable system prompts
following the patterns in
[AGENTPERF03-BP04
Establish efficient agent caching and data access
patterns](agentperf03-bp04.html) and
[AGENTCOST02-BP03
Leverage intelligent caching to reduce redundant model
invocations](agentcost02-bp03.html).
- **Share cache layers across the
fleet:** Expose tool result and semantic caches
through
[Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) MCP server capabilities so
every agent reads from and writes to the same store.
- **Cache credential
validation:** Use
[Amazon
Bedrock AgentCore Identity](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity.html) to cache tokens so
authentication overhead happens once per session rather than
once per agent invocation.
- **Set TTLs based on data
volatility:** Pick invalidation policies calibrated
to how often the underlying data actually changes, shorter
for live operational data, longer for stable reference
material.
- **Monitor and refine hit
rates:** Track cache hit rates per integration
point through
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) and adjust strategies
where hit rates are below expectations.

## Resources

**Related best practices:**

- [AGENTPERF03-BP04
Establish efficient agent caching and data access
patterns](agentperf03-bp04.html)
- [AGENTCOST02-BP03
Leverage intelligent caching to reduce redundant model
invocations](agentcost02-bp03.html)
- [AGENTSUS02-BP01 Optimize
context management and memory utilization](agentsus02-bp01.html)
- [SUS03-BP03
Optimize areas of code that consume the most time or
resources](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_software_a4.html)

**Related documents:**

- [Amazon
Bedrock prompt caching](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-caching.html)
- [Effectively
use prompt caching on Amazon Bedrock](https://aws.amazon.com/blogs/machine-learning/effectively-use-prompt-caching-on-amazon-bedrock/)
- [Optimize
LLM response costs and latency with effective caching](https://aws.amazon.com/blogs/database/optimize-llm-response-costs-and-latency-with-effective-caching/)
- [Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html)

**Related services:**

- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon
Bedrock](https://aws.amazon.com/bedrock/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsus02-bp02.html*

---

# AGENTSUS02-BP03 Appropriately scale data, networking, and compute dependencies

Agent workloads have a shape that general-purpose infrastructure
defaults don't fit, with bursty inference, variable-length tool
execution, and unpredictable multi-step reasoning. Sizing hosting,
network, and storage to the observed pattern rather than a
theoretical maximum keeps infrastructure proportional to agentic
work.

**Desired outcome:**

- Agent processes run on serverless infrastructure that scales
with demand instead of static provisioning for peak load.
- Private connectivity is used where security or latency
requirements justify it, not by default for every workload.
- Agent infrastructure is deployed close to the services it
depends on, so cross-Region data transfer is minimized.
- Streaming responses are used for user-facing interactions to
reduce memory footprint and improve time-to-first-token.
- Utilization is monitored continually and provisioning tracks
actual workload demand.

**Common anti-patterns:**

- Applying general-purpose infrastructure configurations without
analyzing the bursty inference call patterns and variable tool
execution durations specific to agent workloads, producing
wasteful over-allocation or performance-degrading
under-provisioning.
- Maintaining static provisioning regardless of demand, reducing
the ability for infrastructure to contract during low-activity
periods.
- Sizing for theoretical maximum scenarios instead of right-sizing
against actual demand, producing low utilization during normal
operations.
- Deploying agent infrastructure far from the services it depends
on, producing cross-Region network traffic that adds latency and
transfer cost.

**Benefits of establishing this best
practice:**

- Infrastructure consumption tracks demand, contracting when
agents are idle and expanding during peak periods.
- Energy consumption stays proportional to the work agents deliver
rather than their theoretical peak capacity.
- Private connectivity and Region colocation reduce network path
length and latency where it matters.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Running agents on serverless infrastructure solves most of the
static-provisioning problem by design.
[Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime.html) right-sizes compute per
invocation with session-isolated execution, so the orchestration
overhead is scoped to the session that's actually running. There's
no fleet of idle EC2 instances to size against worst-case demand,
because the execution unit is the invocation rather than the
instance. This default makes bursty workloads affordable.

Private networking is about matching the connection pattern to the
workload's actual needs. Some agents process sensitive data or
have latency requirements tight enough that public internet
routing is the bottleneck. For those workloads,
[VPC
interface endpoints for Amazon Bedrock AgentCore (AWS PrivateLink)](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/vpc-interface-endpoints.html) establishes private paths that reduce latency
and keep traffic off the public internet. For workloads without
those requirements, PrivateLink adds operational complexity
without proportional benefit. Default to the public endpoint and
promote workloads to PrivateLink when security or latency demands
it.

Deploying agent infrastructure in the same AWS Region as
frequently accessed Amazon Bedrock endpoints and AgentCore
services reduces cross-Region data transfer overhead that
compounds across thousands of daily invocations. For availability,
[Amazon
Bedrock cross-region inference](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html) distributes foundation model
requests across Regions. This is complementary rather than
contradictory. Use cross-Region inference for failover and burst
capacity, and keep the primary data path local.

Streaming responses change the memory profile of user-facing
interactions. Without streaming, the agent accumulates the full
response in memory before returning it, which means peak memory is
proportional to response length. With streaming, tokens flow as
they're generated and memory stays bounded. Turning on streaming
in AgentCore reduces footprint for long-form interactions and
improves time-to-first-token for users.
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) exposes the utilization
data that keeps provisioning tied to actual workload demand.

### Implementation steps

- **Run agent processes on serverless
runtime:** Deploy to
[Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime.html) for automatic scaling and
session isolation, so execution capacity scales with demand
rather than peak estimates.
- **Apply private connectivity where
justified:** Configure
[VPC
interface endpoints for Amazon Bedrock AgentCore (AWS PrivateLink)](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/vpc-interface-endpoints.html) for workloads with security or latency
requirements that warrant it. Default to public endpoints
otherwise.
- **Deploy in the same Region as
dependencies:** Place agent infrastructure in the
Region hosting the Amazon Bedrock endpoints and AgentCore
services it uses most, and turn on
[Amazon
Bedrock cross-region inference](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html) for availability.
- **Enable streaming for user-facing
responses:** Turn on AgentCore streaming so
response tokens flow as they're generated, reducing memory
footprint and improving time-to-first-token.
- **Validate utilization
continually:** Track infrastructure utilization
through
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) and adjust
provisioning where observed demand is meaningfully below
allocation.

## Resources

**Related best practices:**

- [AGENTSUS02-BP01 Optimize
context management and memory utilization](agentsus02-bp01.html)
- [AGENTSUS02-BP04 Measure
and optimize the environmental footprint of agent
workloads](agentsus02-bp04.html)
- [SUS02-BP01
Scale workload infrastructure dynamically](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_user_a2.html)

**Related documents:**

- [Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime.html)
- [VPC
interface endpoints for Amazon Bedrock AgentCore (AWS PrivateLink)](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/vpc-interface-endpoints.html)
- [Amazon
Bedrock cross-region inference](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html)
- [Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html)

**Related services:**

- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon
Bedrock](https://aws.amazon.com/bedrock/)
- [AWS PrivateLink](https://aws.amazon.com/privatelink/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsus02-bp03.html*

---

# AGENTSUS02-BP04 Measure and optimize the environmental footprint of agent workloads

Without measurement, sustainability claims are aspirational and
optimizations are not tracked against real-world data. Tracking the
environmental footprint of agent workloads makes sustainability an
engineering metric. Baselines show where effort is worth investing,
and trends show whether changes are actually working.

**Desired outcome:**

- You have carbon emissions baselines for agent infrastructure
established across a defined observation period.
- Resource efficiency metrics for each task (tokens per successful
completion, compute hours per workflow, and cache hit rates) are
tracked alongside business outcomes.
- Deferrable workloads are scheduled during off-peak periods or
routed to Regions with favorable energy profiles.
- Operational and sustainability metrics are combined in
dashboards that inform periodic optimization reviews.

**Common anti-patterns:**

- Claiming sustainability benefits from agent optimizations
without establishing baselines, making it impossible to validate
whether changes actually reduced impact.
- Treating every workload as equally time-sensitive, running batch
processing and background tasks during peak hours when deferring
them would reduce contention and energy consumption.
- Ignoring regional differences in energy infrastructure when
selecting deployment Regions for workloads with flexible latency
requirements.
- Tracking only infrastructure utilization without tying it to
business outcomes, so efficiency gains in compute don't connect
to value delivered.

**Benefits of establishing this best
practice:**

- Measurable baselines make sustainability improvements verifiable
instead of aspirational.
- Optimization effort flows to the workloads with the largest
environmental impact, rather than being applied uniformly.
- Deferrable workloads run when infrastructure is underutilized,
improving fleet-wide efficiency without affecting user-facing
performance.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

[AWS Sustainability](https://docs.aws.amazon.com/sustainability/latest/userguide/what-is-sustainability.html) provides carbon emissions tracking with
service and Region breakdowns for the infrastructure side, and
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) adds agent-specific
metrics, tokens per successful task, compute hours per workflow,
and cache hit rates that tie consumption to business outcomes.
Establish baselines across a 30-day observation window so that
normal workload variation is included, and track trends monthly
afterward so optimization work can be validated against measured
change rather than claimed change.

Not every agent workload has the same latency sensitivity.
User-facing interactions need low-latency responses. Batch jobs,
periodic knowledge base indexing, bulk data enrichment, evaluation
runs, and non-interactive research workflows can wait hours or
overnight without affecting the user. Shifting deferrable work to
off-peak periods reduces resource contention on shared
infrastructure and takes advantage of time windows when the
broader grid is cleaner.
[Amazon
Bedrock cross-region inference](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html) extends the same principle
across geographies. Batch workloads without tight latency
constraints can run in Regions with favorable energy profiles
rather than defaulting to the closest one.

Amazon CloudWatch dashboards that combine operational metrics with
sustainability indicators make sustainability visible in the same
place operators already look. Track resource utilization
efficiency, waste metrics (failed or abandoned executions as a
percentage of total), and peak compared to off-peak utilization
rates. Incorporate these dashboards into periodic optimization
reviews so environmental impact is a standing input to engineering
priorities rather than an annual afterthought.

### Implementation steps

- **Enable carbon emissions
tracking:** Turn on
[AWS Sustainability](https://docs.aws.amazon.com/sustainability/latest/userguide/what-is-sustainability.html) and establish environmental baselines
for agent infrastructure across a 30-day observation window.
- **Instrument resource efficiency per
task:** Configure
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) to track tokens per
successful completion, compute hours per workflow execution,
and cache hit rates.
- **Schedule deferrable workloads
off-peak:** Identify non-interactive workloads and
shift them to off-peak windows:

Batch processing
- Knowledge base indexing
- Periodic AgentCore Evaluations runs
- Bulk data enrichment

- **Evaluate Region placement for batch
work:** For workloads with flexible latency, use
[Amazon
Bedrock cross-region inference](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html) to route requests to
Regions with favorable energy profiles.
- **Build combined dashboards and review
on a cadence:** Create Amazon CloudWatch dashboards
pairing operational metrics with sustainability indicators
(resource utilization efficiency, waste percentage, and peak
compared to off-peak utilization), and review them as part
of periodic optimization cycles.

## Resources

**Related best practices:**

- [AGENTSUS02-BP01 Optimize
context management and memory utilization](agentsus02-bp01.html)
- [AGENTSUS02-BP03
Appropriately scale data, networking, and compute
dependencies](agentsus02-bp03.html)
- [SUS01-BP01
Choose Region based on both business requirements and
sustainability goals](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_region_a2.html)

**Related documents:**

- [AWS Sustainability User Guide](https://docs.aws.amazon.com/sustainability/latest/userguide/what-is-sustainability.html)
- [Announcing
the AWS Sustainability console](https://aws.amazon.com/blogs/aws/announcing-the-aws-sustainability-console-programmatic-access-configurable-csv-reports-and-scope-1-3-reporting-in-one-place/)
- [Sustainability
Pillar - AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)
- [Amazon
Bedrock cross-region inference](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html)
- [Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html)

**Related videos:**

- [AWS re:Invent 2024 - Sustainable and cost-efficient generative AI
with agentic workflows (AIM333)](https://www.youtube.com/watch?v=tFiDkSG2ess)

**Related services:**

- [AWS Sustainability](https://aws.amazon.com/sustainability/)
- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon
Bedrock](https://aws.amazon.com/bedrock/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsus02-bp04.html*

---
