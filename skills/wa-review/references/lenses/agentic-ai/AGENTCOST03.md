# AGENTCOST03 — Agent memory and state cost management

**Pillar**: Cost Optimization  
**Best Practices**: 3

---

# AGENTCOST03-BP01 Design cost-effective retrieval systems with tiered memory

Agent memory has to serve two opposing needs at once: fast access
for active context, and cheap storage for history that is rarely
touched. Tiered memory matches each class of data to infrastructure
priced for its actual access pattern, and selective retrieval keeps
token costs proportional to what the current task needs.

**Desired outcome:**

- You have short-term working memory on high-performance storage
and long-term memory on cost-effective tiers, with automatic
lifecycle transitions between them.
- You retrieve only top-K relevant items per reasoning step rather
than loading full memory stores into context.
- You track retrieval operations per session and use the data to
tune tier assignments and access patterns.

**Common anti-patterns:**

- Storing all agent memory in expensive high-performance storage
regardless of access frequency, incurring unnecessary costs for
rarely accessed historical interactions.
- Retrieving entire memory stores for each reasoning step,
consuming excessive input tokens when targeted top-K retrieval
would suffice.
- Using single-tier storage for all memory regardless of access
pattern, wasting resources on uniform infrastructure for data
with distinct access profiles.
- Deploying memory systems without retrieval cost monitoring,
hiding inefficient access patterns inside aggregate session
cost.

**Benefits of establishing this best
practice:**

- Tiered storage matches each memory category to its access
pattern, reducing costs for historical data without sacrificing
active session performance.
- Selective top-K retrieval limits context to the most pertinent
items, avoiding token charges for irrelevant historical data.
- Automated tier lifecycle management scales across thousands of
sessions without manual intervention or over-provisioning.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

The cost of agent memory comes from two decisions: where data
lives and how much of it you pull into the model's context window.
[Amazon
Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) handles the first decision as a
managed service. Short-term memory stores turn-by-turn session
context on fast storage, while long-term memory extracts and
consolidates key insights across sessions into cheaper tiers.

For agents on
[Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html), this removes the need to build
storage tiers and promotion policies by hand. When a custom
implementation is required, define explicit promotion and demotion
policies based on access frequency so frequently accessed items
stay on low-latency storage and rarely accessed items migrate to
lower-cost tiers automatically.

Retrieval volume is the second decision, and it has a direct
effect on input token cost.
[Amazon
Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html) provides managed vector retrieval
with semantic search. *K* (the number of chunks
returned per query) is the central cost-quality knob: higher K
gives the agent more context but pushes more tokens into every
invocation. Start with K=5 and tune against the
trade-off between completeness and cost, not from a preference for
safety.

Index design is a less obvious but still important cost
consideration. For
[Amazon OpenSearch Service Serverless](https://aws.amazon.com/opensearch-service/features/serverless/)-backed Knowledge Bases, HNSW
parameters (ef_construction and
m) balance index build cost against query
accuracy and recall. OpenSearch Serverless charges based on
indexed data volume and query compute, so tuning these parameters
is a direct cost decision, not just a quality decision. Higher
ef_construction values improve recall but raise
both build and query cost, while lower values reduce cost but risk
missing relevant items.

Additionally, consider retrieval batching. Pre-fetching the full
task context at initiation and caching it in the agent's working
memory avoids per-step retrieval overhead.
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) provides
OpenTelemetry-compatible telemetry that identifies which retrieval
patterns drive the most token consumption, and Amazon CloudWatch Logs Insights queries reveal access patterns that should inform
tier reassignments.

### Implementation steps

- **Adopt managed tiered
memory:** Integrate
[Amazon
Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) for short-term and long-term
memory with automatic lifecycle management, and document
which namespaces each agent writes to and reads from.
- **Configure selective
retrieval:** Use
[Amazon
Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html) with top-K semantic search,
starting at K=5 and tuning based on observed reasoning
quality and token cost.
- **Tune vector index
parameters:** Adjust HNSW ef_construction and m on
the
[Amazon OpenSearch Service Serverless](https://aws.amazon.com/opensearch-service/features/serverless/) backing store to balance index
build cost, query latency, and recall accuracy for your
workload.
- **Pre-fetch context at task
initiation:** Replace per-step retrievals with a
single batch pre-fetch at task start, cached in working
context so the model doesn't pay retrieval overhead on every
reasoning step.
- **Instrument retrieval
operations:** Enable
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) and set Amazon CloudWatch alarms when retrieval frequency exceeds expected
bounds per session.
- **Review access patterns
weekly:** Run CloudWatch Logs Insights queries to
reveal expensive retrieval patterns and never-accessed
items, and use the results to reassign tiers and retire dead
entries.

## Resources

**Related best practices:**

- [AGENTCOST01-BP02
Optimize multi-agent collaboration cost through efficient
handoff patterns](agentcost01-bp02.html)
- [AGENTCOST02-BP03
Use intelligent caching to reduce redundant model
invocations](agentcost02-bp03.html)
- [AGENTCOST03-BP02 Cost
optimize through intelligent compression and pruning of
context windows](agentcost03-bp02.html)
- [AGENTCOST03-BP03
Implement cost-optimized state persistence and lifecycle
management](agentcost03-bp03.html)

**Related documents:**

- [Amazon
Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html)
- [Amazon
Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html)
- [Economics
for agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-economics/index.html)
- [Guidance
for Cost Analysis and Optimization with Amazon Bedrock
Agents](https://aws.amazon.com/solutions/guidance/cost-analysis-and-optimization-with-amazon-bedrock-agents/)

**Related videos:**

- [AWS 2025 - AgentCore Deep Dive: Memory](https://www.youtube.com/watch?v=-N4v6-kJgwA)
- [AWS 2025 - AgentCore Memory: Episodic Memory & Patterns](https://www.youtube.com/watch?v=1EEIGsKIjGA)

**Related examples:**

- [GitHub:
awslabs/amazon-bedrock-agentcore-samples - Memory
tutorials](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/04-AgentCore-memory)

**Related workshops:**

- [Getting
started with Amazon Bedrock AgentCore - Lab 2: Memory](https://catalog.workshops.aws/agentcore-getting-started/en-US/30-add-memory)
- [Diving
Deep into Bedrock AgentCore - Memory](https://catalog.workshops.aws/agentcore-deep-dive/en-US/50-agentcore-memory)

**Related services:**

- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentcost03-bp01.html*

---

# AGENTCOST03-BP02 Cost optimize through intelligent compression and pruning of context windows

In long-running agent sessions, raw conversation history can
silently drive costs up, as every turn gets paid for again on every
subsequent invocation. Compression, selective retrieval, and pruning
keep context proportional to what the agent needs for the current
decision rather than growing with session length.

**Desired outcome:**

- You compress older conversation turns into summaries so
historical context doesn't multiply per-invocation token cost.
- You retrieve only the top-K most relevant memory items per
reasoning step.
- You prune duplicates, superseded reasoning, and irrelevant tool
results before each invocation.
- You monitor context window utilization and alert on sessions
approaching overflow.

**Common anti-patterns:**

- Including full conversation history in every invocation
regardless of task relevance, causing linear token cost growth
with session length.
- Allowing raw interaction history to accumulate without
compression, so context windows are dominated by historical
turns with diminishing value.
- Deploying agents without context utilization monitoring, missing
sessions that approach overflow thresholds and trigger costly
re-invocation errors.
- Retrieving excessive RAG chunks or oversized chunk lengths when
smaller, targeted retrievals would maintain reasoning quality at
lower cost.
- Failing to prune duplicate or superseded information, paying
tokens on content that doesn't contribute to the current
reasoning task.

**Benefits of establishing this best
practice:**

- History compression helps prevent linear token cost growth in
long-running sessions, making persistent assistants economically
viable.
- Selective retrieval includes only high-value context relevant to
the current task, reducing token waste from marginally relevant
data.
- Context window monitoring helps prevent overflow errors that
trigger costly re-invocation with truncated context.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

[Amazon
Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) separates short-term and long-term
memory, which is the architectural pattern behind rolling
summarization. Short-term memory holds raw recent turns, and
long-term memory automatically extracts and consolidates key
insights across sessions. For agents on AgentCore Runtime, this
dual-tier behavior implements rolling summarization without custom
code, and it is the difference between a persistent assistant
whose token cost is bounded and one whose cost grows linearly with
conversation age.

Selective retrieval helps handle the problem of conversation
history cost. AgentCore Memory's
RetrieveMemoryRecords operation performs
semantic search with relevance scoring and metadata filtering, so
you can pre-filter by recency or topic before the similarity
search runs. Configure top-K between three and five items per
reasoning step.

Context pruning assists with retrieval by removing duplicates
between summaries and recent turns before each invocation,
dropping superseded reasoning steps, and stripping irrelevant tool
results. The goal is a target context utilization of 60 to 80% of
the model's window, which leaves enough headroom for responses
while still benefiting from available context.

RAG chunk sizing also helps solve this problem. When retrieving
from
[Amazon
Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html), chunk sizes of 256 to 512 tokens
balance retrieval precision against context bloat, and limiting
retrieved chunks to the minimum needed helps prevent marginally
relevant data from crowding out the current task. The verification
that compression isn't silently hurting quality is a correlation
check: pair context utilization with task success rate in
CloudWatch Logs Insights and track whether aggressive pruning
correlates with success-rate degradation.

[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) exposes token usage metrics
that feed CloudWatch dashboards and alarms. Alarms on sessions
consistently above 80% utilization flag the candidates for tighter
summarization, correlating those same metrics with task success
rates confirms whether the compression is paying off in cost
without paying in quality.

### Implementation steps

- **Adopt managed rolling
summarization:** Integrate
[Amazon
Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) for managed compression, or
implement custom rolling summarization that compresses the
oldest N turns after every N turns.
- **Configure relevance-scored
retrieval:** Use AgentCore Memory's
RetrieveMemoryRecords with relevance thresholds and metadata
filtering, retrieving only the top-K most relevant items per
reasoning step.
- **Prune context before each
invocation:** Remove duplicates, superseded
reasoning steps, and irrelevant tool results before each
model call so the context window reflects what the current
decision needs.
- **Tune RAG chunk size:**
Optimize
[Amazon
Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html) chunk sizes to 256 to 512
tokens, limit retrieved chunks to the minimum needed, and
add re-ranking to maximize relevance.
- **Alarm on context
utilization:** Build Amazon CloudWatch dashboards
for context window utilization and set alarms for sessions
exceeding 80% utilization.
- **Correlate utilization with task
success:** Use CloudWatch Logs Insights to
correlate context utilization with task success rates,
validating that compression strategies reduce cost without
degrading reasoning quality.

## Resources

**Related best practices:**

- [AGENTCOST02-BP02
Cost optimize token consumption through efficient prompt
engineering](agentcost02-bp02.html)
- [AGENTCOST02-BP03
Use intelligent caching to reduce redundant model
invocations](agentcost02-bp03.html)
- [AGENTCOST03-BP01 Design
cost-effective retrieval systems with tiered memory](agentcost03-bp01.html)
- [AGENTCOST03-BP03
Implement cost-optimized state persistence and lifecycle
management](agentcost03-bp03.html)

**Related documents:**

- [Amazon
Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html)
- [Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html)
- [Economics
for agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-economics/index.html)

**Related videos:**

- [AWS 2025 - AgentCore Deep Dive: Memory](https://www.youtube.com/watch?v=-N4v6-kJgwA)
- [AWS 2025 - AgentCore Observability: Monitor and Debug with
OpenTelemetry](https://www.youtube.com/watch?v=wWQgawUPr1k)

**Related examples:**

- [GitHub:
awslabs/amazon-bedrock-agentcore-samples - Memory
tutorials](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/04-AgentCore-memory)

**Related services:**

- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentcost03-bp02.html*

---

# AGENTCOST03-BP03 Implement cost-optimized state persistence and lifecycle management

Agent state grows quickly when every reasoning step triggers a
checkpoint, and it stays forever when no lifecycle policy removes
it. Saving state at meaningful decision points, tiering by access
pattern, and automating archival keeps recoverability without paying
for a growing backlog of stale sessions.

**Desired outcome:**

- You checkpoint at meaningful decision points rather than after
every reasoning step.
- You have session state tiered by access pattern, with
high-performance storage reserved for active work.
- You have automated lifecycle policies that archive or purge
stale context.
- You track storage cost per agent and session, with alarms for
unexpected growth.

**Common anti-patterns:**

- Checkpointing after every reasoning step with synchronous writes
when asynchronous checkpoints at meaningful decision points
would suffice.
- Keeping all session state on high-performance storage regardless
of activity level, paying unnecessary costs for inactive or
archived sessions.
- Allowing agent memory to accumulate indefinitely without
archival or deletion, producing unbounded storage growth.
- Storing agent state uncompressed when compression could reduce
storage costs proportionally.
- Deploying state persistence without cost monitoring, hiding
high-cost patterns and optimization opportunities.

**Benefits of establishing this best
practice:**

- Automated lifecycle management helps prevent unbounded storage
growth without manual intervention across thousands of sessions.
- Managed memory separates durable learning from ephemeral state,
keeping knowledge that improves agent performance while cleaning
up temporary artifacts.
- Session timeout configuration balances responsiveness with cost
by controlling the compute lifecycle.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

[Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html) provides a persistent filesystem
that handles tiered storage and lifecycle automatically. The
filesystem survives session stop and resume cycles for up to 14
days of inactivity before automatic deletion, and the two
lifecycle parameters that shape cost are
idleRuntimeSessionTimeout (default 15 minutes)
and maxLifetime (up to 8 hours). The 15-minute
default suits interactive workloads, while longer timeouts reduce
session state transitions for batch workloads. Session storage
automatically synchronizes filesystem writes to durable storage
throughout the session lifecycle, with data flushed during
graceful shutdown when sessions stop.

Make a deliberate design choice about checkpointing. For use cases
that require explicit checkpoints at application-defined decision
points, implement custom checkpoint logic that writes state
snapshots to the persistent filesystem. Checkpoint interval is a
trade-off between recovery granularity and storage consumption:
more frequent checkpoints enable finer-grained recovery but
increase storage cost. Some agent frameworks provide built-in
checkpoint capabilities using the same filesystem, which avoids
reinventing the pattern.

Consider how you accomplish durable learning.
[Amazon
Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) persists insights across sessions
(short-term memory for recent interactions, long-term memory for
consolidated learning), which is different from per-session
filesystem state. For compliance retention beyond the 14-day
Runtime filesystem window, export completed session data to
[Amazon S3](https://aws.amazon.com/s3/)
with Intelligent-Tiering enabled, and configure lifecycle rules
for cost-effective long-term storage. Monitor consumption per
agent type using
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) with custom dimensions, and
set Amazon CloudWatch alarms when growth exceeds expected bounds.

### Implementation steps

- **Deploy on AgentCore Runtime with
tuned lifecycle parameters:** Use
[Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html) for automatic session
lifecycle management, configuring idleRuntimeSessionTimeout
and maxLifetime based on workload patterns.
- **Integrate managed memory for durable
learning:** Configure
[Amazon
Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) short-term memory for recent
context and long-term memory for persistent insights,
keeping durable learning separate from ephemeral filesystem
state.
- **Archive compliance-required sessions
to S3:** Export completed session histories to
[Amazon S3 Intelligent-Tiering](https://aws.amazon.com/s3/storage-classes/intelligent-tiering/) and set lifecycle rules for
cost-effective long-term retention.
- **Monitor storage per agent
type:** Configure
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) with custom
dimensions to track storage cost per agent type, and set
Amazon CloudWatch alarms for unexpected storage growth.

## Resources

**Related best practices:**

- [AGENTCOST01-BP01
Use the reflection pattern to design efficient agent reasoning
loops](agentcost01-bp01.html)
- [AGENTCOST03-BP01 Design
cost-effective retrieval systems with tiered memory](agentcost03-bp01.html)
- [AGENTCOST03-BP02 Cost
optimize through intelligent compression and pruning of
context windows](agentcost03-bp02.html)
- [AGENTCOST05-BP01
Establish agent-level reasoning cost tracking and
attribution](agentcost05-bp01.html)

**Related documents:**

- [Amazon
Bedrock AgentCore Runtime Sessions](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-sessions.html)
- [Amazon
Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html)
- [Amazon S3 Intelligent-Tiering](https://aws.amazon.com/s3/storage-classes/intelligent-tiering/)
- [Economics
for agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-economics/index.html)

**Related videos:**

- [AWS 2025 - AgentCore Deep Dive: Runtime](https://www.youtube.com/watch?v=wizEw5a4gvM)

**Related examples:**

- [GitHub:
awslabs/amazon-bedrock-agentcore-samples - Runtime advanced
concepts](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/01-AgentCore-runtime/03-advanced-concepts)

**Related services:**

- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon S3](https://aws.amazon.com/s3/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentcost03-bp03.html*

---
