# AGENTPERF03 — Memory, context, and RAG optimization

**Pillar**: Performance Efficiency  
**Best Practices**: 5

---

# AGENTPERF03-BP01 Implement tiered memory management systems

Agents that carry context across turns and sessions deliver more
personalized and accurate responses, but only when memory retrieval
doesn't become the latency bottleneck on every reasoning iteration.
A tiered memory architecture separates fast, transient session state
from durable cross-session knowledge so each tier's storage
technology, access pattern, and lifecycle can be optimized
independently rather than forced through a single store.

**Desired outcome:**

- You have agent memory separated into a short-term tier for
in-session context and a long-term tier for cross-session
knowledge, each backed by storage matched to its access pattern.
- You have automated lifecycle policies that extract durable
insights from short-term memory into long-term strategies
(semantic, episodic, summary, and user preference) and evict
stale short-term state without manual intervention.
- You have per-tier retrieval latency tracked as a first-class
KPI, with budgets that keep memory access from dominating the
reasoning loop.
- You have long-term memory scoped and namespaced per user,
session, or tenant so retrievals return only the records
relevant to the current actor.

**Common anti-patterns:**

- Storing all agent memory in a single database regardless of
access pattern, forcing sub-second session reads and large-scale
semantic searches through the same storage layer.
- Persisting every turn of short-term memory indefinitely without
extraction into long-term strategies or eviction, allowing
session stores to grow without bounds and retrieval latency to
degrade over time.
- Treating long-term memory as a single bag of records rather than
differentiating between semantic facts, episodic events,
conversation summaries, and user preferences, which forces every
query to search all record types.
- Scoping long-term memory globally rather than per user, session,
or tenant, so retrievals return cross-actor records that inflate
context and leak information.
- Building custom tiered memory infrastructure from scratch
instead of evaluating managed services that provide session
stores, extraction strategies, and vector retrieval as
primitives.

**Benefits of establishing this best
practice:**

- Fast in-memory stores serve session reads in single-digit
milliseconds while vector stores handle long-term semantic
queries without coupling the two.
- Automated extraction and eviction policies keep each tier's
footprint and retrieval latency stable as usage scales.
- Separating long-term memory into distinct strategies, semantic,
episodic, summary, preference, lets the agent query only the
record type relevant to its current reasoning step.
- Namespacing long-term memory by user, session, or tenant helps
prevent cross-actor retrievals and keeps context relevant.
- Managed memory primitives remove the need to operate session
stores, extraction pipelines, and vector indexes as bespoke
infrastructure.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Memory access sits on the hot path of every reasoning iteration.
An agent that reads session context and retrieves relevant
long-term knowledge at every step pays that retrieval latency
multiplied by the iteration count, which makes memory one of the
largest use points in the reasoning loop.

The root cause of poor memory performance is typically an
access-pattern mismatch. Using a single storage layer for both
sub-millisecond session reads and large-scale semantic searches
forces one pattern to carry cost and latency characteristics
suited to the other. Tiering resolves the mismatch by splitting
memory into a short-term tier for in-session context and a
long-term tier for cross-session knowledge, then matching each
tier to storage with the right latency, durability, and query
model.

Short-term memory holds the turn-by-turn state an agent reads and
writes within a single session: the last N turns, intermediate
reasoning, tool outputs, and transient user-provided context.
[Amazon
Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) provides a managed short-term tier
that stores session events and integrates with extraction into the
long-term tier, removing the need to operate a separate session
store or extraction pipeline.

For workloads that need sub-millisecond short-term reads or prefer
to own the extraction pipeline,
[Amazon ElastiCache (Valkey)](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/agentic-memory-why-elasticache.html) provides in-memory reads, TTL-based
expiration, and native structures (hashes, lists, sorted sets)
that map well to session data. Durability requirements for
short-term memory are typically low, state can be regenerated or
discarded on session end, so the tier should be sized for latency,
not for archival.

Long-term memory holds durable knowledge that persists across
sessions: user preferences, domain facts, past-interaction
summaries, and episodic records of past task outcomes. Access is
less frequent but operates over a much larger corpus and typically
relies on semantic similarity rather than key lookup. AgentCore
Memory provides a managed long-term tier with
[four
built-in strategies](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/long-term-configuring-built-in-strategies.html), semantic, episodic, summary, and user
preference, each extracted from session events and indexed
separately, so the agent can query only the store relevant to its
current reasoning step.

For teams that prefer to own the long-term store directly,
[agentic
memory in Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/application-agentic-memory.html) provides dense and
hybrid retrieval over long-term records, and
[Amazon Neptune Analytics](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/what-is-neptune-analytics.html) provides a graph-based alternative for
domains where long-term memory is defined by relationships between
entities, enabling multi-hop queries that vector similarity can't
answer on its own. Separating strategies (managed or self-indexed)
matters for performance, as every irrelevant record retrieved is
latency and context budget spent on noise.

Tiers are only high-performing when their lifecycle is automated.
Short-term state that isn't evicted grows until reads slow and
session stores run out of memory, while long-term records that are
not extracted from short-term events represent knowledge the agent
has to relearn every session.

Managed services handle both movements: AgentCore Memory extracts
long-term strategies from short-term events asynchronously and
applies TTLs to short-term records, while self-managed stacks must
build extraction and eviction explicitly, either by adopting an
open source orchestration layer such as Mem0 or by writing bespoke
pipelines on top of primitives like ElastiCache, OpenSearch, or
Neptune Analytics.

Long-term memory must also be namespaced by actor (user, session,
or tenant), because unscoped retrievals return records from other
actors that inflate context and, depending on the deployment, leak
information across isolation boundaries. Scoping is both a
performance control (a smaller search space per query returns
faster) and a correctness control.

### Implementation steps

- **Inventory the memory the agent reads
and writes:** List the distinct pieces of state the
agent maintains, last-N-turn context, intermediate
reasoning, tool outputs, user preferences, past-interaction
summaries, domain facts, and for each note the access
pattern (read per iteration, read per session, read per task
class), retention requirement (session-scoped or durable),
and query shape (key lookup or semantic search). This
inventory is the input to tier selection, as without it,
tier boundaries are drawn by guess and either fragment
naturally grouped data or collapse patterns that should be
separated. Record the inventory alongside the workload's
performance budgets so tiering decisions can be audited and
revisited.
- **Assign each inventoried item to a
short-term or long-term tier:** Place
session-scoped, high-frequency, latency-critical items in
the short-term tier and durable, cross-session items queried
semantically in the long-term tier. Avoid intermediate
"working memory" tiers unless a concrete access
pattern justifies one, most "working memory" is
either active short-term state or a long-term record that
has not been extracted. Document the tier boundary so every
new memory item has a clear home.
- **Choose storage for each tier based
on the tier's access pattern:** For the short-term
tier, select
[Amazon
Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) if you also want managed
long-term extraction, or
[Amazon ElastiCache (Valkey)](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/agentic-memory-why-elasticache.html) if you prefer to own the
extraction pipeline. For the long-term tier, use AgentCore
Memory's built-in strategies or
[Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/application-agentic-memory.html) for dense and hybrid retrieval.
Resist using one storage layer for both tiers. It is the
single most common cause of memory-bound latency
regressions.
- **Configure long-term memory with
strategies that match what the agent retrieves:**
Enable the subset of
[AgentCore's
built-in long-term strategies](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/long-term-configuring-built-in-strategies.html), semantic, episodic,
summary, and user preference, that correspond to the
retrieval patterns in the inventory. Each strategy extracts
a different shape of record from short-term events and
indexes it separately, so the agent can query only the store
relevant to its current step. In self-managed stacks, create
equivalent per-strategy indexes rather than a single
general-purpose corpus.
- **Namespace every memory record to its
actor (user, session, or tenant):** Attach an actor
identifier to every short-term and long-term record and
filter every retrieval by that identifier using AgentCore
Memory's
[actor
and session scoping](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-organization.html) or an equivalent filter in
self-managed stacks. Scoping reduces the search space (lower
retrieval latency) and helps prevent cross-actor context
leakage (correctness and isolation). Align the actor key
with the authentication identity used by the agent so
scoping can't be bypassed by a missing filter in application
code.
- **Automate extraction from short-term
to long-term and eviction of stale short-term
state:** Configure the managed extraction pipeline,
AgentCore Memory's asynchronous strategy extraction, or
build an equivalent job in self-managed stacks that reads
session events, derives long-term records per enabled
strategy, and writes them to the long-term index. Apply TTLs
or sliding-window eviction to short-term state so session
stores don't grow without bounds. Both movements must run
without manual intervention. If either requires human
action, memory growth and extraction lag will exceed design
targets.
- **Emit per-tier retrieval latency as a
first-class performance metric and set budgets:**
Publish short-term read latency and long-term query latency
as distinct time-series through
[Amazon CloudWatch generative AI observability](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/GenAI-observability.html) or an
equivalent pipeline, alongside tier size, hit rate, and
extraction lag. Allocate each tier an explicit portion of
the per-iteration latency budget so memory can't silently
consume time reserved for inference or tool calls. Treat
per-tier latency as an early indicator: sustained growth in
long-term query latency usually signals index size or scope
drift before it registers on end-to-end metrics.
- **Review tier sizing, strategies, and
budgets against production telemetry on a defined
cadence:** Schedule reviews of short-term tier size
distributions, long-term strategy growth rates, extraction
lag, and per-tier latency against budget. Tighten TTLs on
short-term stores that are consistently oversized, disable
long-term strategies that are never queried, and re-scope
memory if retrievals are returning more cross-actor records
than the scope intended. Tiering parameters set at launch
rarely match production traffic unless they are reviewed on
an ongoing basis.

## Resources

**Related best practices:**

- [AGENTPERF03-BP02
Optimize context window utilization and prompt
management](agentperf03-bp02.html)
- [AGENTPERF03-BP03
Optimize RAG retrieval pipelines for latency and
precision](agentperf03-bp03.html)
- [AGENTPERF03-BP04
Establish efficient agent caching and data access
patterns](agentperf03-bp04.html)
- [AGENTPERF03-BP05
Implement agentic retrieval patterns for dynamic, agent-driven
knowledge access](agentperf03-bp05.html)

**Related documents:**

- [Amazon
Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html)
- [AgentCore
Memory, memory organization](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory-organization.html)
- [AgentCore
Memory, long-term built-in strategies](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/long-term-configuring-built-in-strategies.html)
- [Agentic
memory in Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/application-agentic-memory.html)
- [Why
use ElastiCache for agentic memory](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/agentic-memory-why-elasticache.html)
- [Foundations
of agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-foundations/introduction.html)
- [Blog:
Amazon Bedrock AgentCore Memory, Building context-aware
agents](https://aws.amazon.com/blogs/machine-learning/amazon-bedrock-agentcore-memory-building-context-aware-agents/)
- [Blog:
Building smarter AI agents, AgentCore long-term memory deep
dive](https://aws.amazon.com/blogs/machine-learning/building-smarter-ai-agents-agentcore-long-term-memory-deep-dive/)
- [Blog:
Build agents to learn from experiences using AgentCore
episodic memory](https://aws.amazon.com/blogs/machine-learning/build-agents-to-learn-from-experiences-using-amazon-bedrock-agentcore-episodic-memory/)
- [Blog:
Build persistent memory for agentic AI applications with Mem0,
ElastiCache for Valkey, and Neptune Analytics](https://aws.amazon.com/blogs/database/build-persistent-memory-for-agentic-ai-applications-with-mem0-open-source-amazon-elasticache-for-valkey-and-amazon-neptune-analytics/)

**Related videos:**

- [AWS re:Invent 2024 - Make agents remember with Amazon Bedrock
AgentCore Memory (AIM331)](https://www.youtube.com/watch?v=Sh0Ro00_rpA)
- [AgentCore
Deep Dive: Memory](https://www.youtube.com/watch?v=-N4v6-kJgwA)
- [Solving
LLM Amnesia: Cross Session Memory](https://www.youtube.com/watch?v=ZY5WXDDp9g8)

**Related examples:**

- [GitHub:
Amazon Bedrock AgentCore samples, Memory tutorials](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/04-AgentCore-memory)

**Related workshops:**

- [Diving
Deep into Bedrock AgentCore, Memory](https://catalog.workshops.aws/agentcore-deep-dive/en-US/50-agentcore-memory)

**Related services:**

- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon ElastiCache](https://aws.amazon.com/elasticache/)
- [Amazon OpenSearch Service](https://aws.amazon.com/opensearch-service/)
- [Amazon Neptune Analytics](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/what-is-neptune-analytics.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentperf03-bp01.html*

---

# AGENTPERF03-BP02 Optimize context window utilization and prompt management

Every token sent to an LLM competes for the model's attention,
consumes input-token cost, and adds inference latency, which makes
prompt content a first-order performance lever. Effective context
window management budgets tokens across prompt components, assembles
only what the current task needs, and compresses or summarizes the
rest. Without this discipline, conversation history and tool schemas
crowd out reasoning capacity and inflate latency on every iteration.

**Desired outcome:**

- You have an explicit token budget allocated across prompt
components, system instructions, conversation history, retrieved
knowledge, and tool schemas, with per-component token usage
measured on every request.
- You have context assembled dynamically per request, including
only the tool definitions, retrieved passages, and conversation
context relevant to the current task rather than a fixed maximal
payload.
- You have conversation history bounded by summarization, sliding
windows, or semantic compression so prompt size doesn't grow
linearly with session length.
- You have prompt templates versioned and evaluated so changes to
wording, ordering, or component composition are measured against
quality and token-cost baselines before rollout.

**Common anti-patterns:**

- Including the full conversation history in every prompt without
summarization or truncation, causing prompt size and inference
latency to grow linearly with session length.
- Injecting the full tool catalog in every prompt regardless of
task relevance, spending context budget on schemas the agent
will not invoke for the current request.
- Passing RAG retrievals straight into the prompt without
per-passage filtering or truncation, so low-relevance chunks
displace more useful context.
- Treating the prompt as a single opaque string rather than a
composition of components, making it impossible to attribute
token consumption to system instructions, history, retrievals,
or tool schemas.
- Shipping prompt changes without versioning or side-by-side
evaluation, so quality or token-cost regressions are detected
only after rollout.

**Benefits of establishing this best
practice:**

- Removing tokens from the prompt can reduce request cost and
shorten time-to-first-token on each iteration.
- Pruned, high-density context leaves more of the model's
effective attention on the current task instead of parsing stale
history or unused tool schemas.
- Summarization and sliding-window strategies decouple prompt size
from conversation length, keeping per-turn latency and cost
stable.
- Stable, component-structured prompts with invariant prefixes
compose with prompt caching, turning a large portion of input
tokens into cached reads at a fraction of standard input cost.
- Versioned templates with evaluation gates let prompt changes
ship with quality and cost evidence rather than by guess.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Prompts behave as compositions of discrete components, system
instructions, tool schemas, retrieved knowledge, conversation
history, and the current user turn. Treating them as a single
opaque string makes runaway growth impossible to attribute.
Per-component token attribution on every request demystifies
issues, such as a tool catalog that doubled when a new tool was
registered. Component-level budgets that sum to the workload's
input-length target make the trade-offs explicit: more budget for
retrievals means less for history, and every reallocation becomes
a deliberate decision.

The
[Amazon
Bedrock prompt design guidance](https://docs.aws.amazon.com/bedrock/latest/userguide/design-a-prompt.html) describes how clear
instructions, output indicators, and question placement at the end
of the prompt shape the system-instruction and user-turn
components individually.

The cheapest tokens are the ones never sent. Most agents register
many more tools than any single turn will invoke, so injecting the
full tool catalog on every request spends context budget on
schemas the model ignores.
[Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-advanced-performance.html) addresses this with semantic
search that returns only the tools relevant to the current user
intent.

Retrieval-augmented context suffers from the same failure mode,
passing raw top-K passages into the prompt without a relevance
threshold or per-passage cap lets low-signal chunks displace
higher-signal context.

Conversation history is the third inflation source: the
[SummaryMemoryStrategy
in Amazon Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/long-term-configuring-built-in-strategies.html#long-term-session-summaries-strategy) maintains a running
per-session summary that replaces raw turns after the session
exceeds a threshold, decoupling prompt size from session length so
per-turn latency remains stable as conversations grow.

Static prefixes unlock large, recurring input-token savings.
[Amazon
Bedrock prompt caching](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-caching.html) accepts cache checkpoints in the
system, tools, and
messages fields on the Converse API, with cache
reads charged at a reduced rate on a 5-minute default TTL, or a
1-hour TTL on Claude Opus 4.5, Haiku 4.5, and Sonnet 4.5 for
longer-running or intermittent agent traffic.

Invariant content (system instructions, stable tool definitions,
and pinned context) belongs before the checkpoint, and variable
content (current user turn and session-specific retrievals)
belongs after it so the cached prefix remains identical across
turns. Simplified cache management for Claude models looks back
approximately 20 content blocks for the longest matching prefix,
so the most-reused content should sit within that range.

Prompts behave like code, so a change to wording, component order,
or a tool description can shift quality, token count, and
cache-hit rate simultaneously, while the effects remain invisible
until rollout unless they are measured.
[Amazon
Bedrock Prompt management](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-create.html) stores prompts as versioned
artifacts with variables, inference configuration, and optional
prompt-caching settings, and its console variant comparison
surfaces quality and token differences side by side before
promotion.

[Prompt
Optimization](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-optimize.html) generates model-specific rewrites that serve
as candidate variants rather than drop-in replacements, and
quality plus token-cost benchmarks on representative test sets
should gate promotion of any variant.

### Implementation steps

- **Define the prompt component taxonomy
and per-component token budget:** Decompose every
prompt into a fixed set of components, system instructions,
tool schemas, retrieved knowledge, conversation history, and
the current user turn, and allocate a token budget to each
that sums to the input-length target derived from the
workload's latency and cost SLO. Apply the
[Amazon
Bedrock prompt design guidance](https://docs.aws.amazon.com/bedrock/latest/userguide/design-a-prompt.html) to keep the
system-instruction component clear, concise, and consistent
with the user query placed at the end of the prompt.
- **Instrument per-component token usage
on every request:** Emit token counts for each
component as structured logs or CloudWatch metrics alongside
the inputTokens and
outputTokens returned by the
[Amazon
Bedrock Converse API](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html), dimensioned by agent ID and
task type. Include cacheReadInputTokens
and cacheWriteInputTokens from the
Converse response so cache effectiveness is measured
alongside component growth, and alert when any component
trends outside its budget before it impacts the end-to-end
SLO.
- **Assemble tool schemas dynamically
with just-in-time selection:** Replace full-catalog
injection with task-relevant selection so the prompt carries
only the tools the agent might invoke for the current turn.
For agents using
[Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-advanced-performance.html), enable semantic search by
setting
"searchType": "SEMANTIC"
on the mcp protocol in the gateway's
protocolConfiguration so tool retrieval
narrows on user intent. Keep each tool's schema compact with
clear parameter descriptions and required fields to reduce
its per-invocation token weight.
- **Bound conversation history with
summarization and a sliding window:** Cap raw-turn
retention and replace older turns with a running summary
after the session exceeds a threshold expressed in turns or
tokens. Configure the
[SummaryMemoryStrategy
in Amazon Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/long-term-configuring-built-in-strategies.html#long-term-session-summaries-strategy) with a
namespaceTemplates entry such as
/summaries/{actorId}/{sessionId}/ and
inject the summary rather than the raw transcript into the
prompt, paired with a small sliding window of recent turns
to preserve near-term conversational detail.
- **Filter and truncate retrieved
passages before prompt assembly:** Apply a
relevance threshold, a per-passage token cap, and a total
retrieval budget so low-signal chunks can't displace
higher-signal context. Rank passages by relevance score,
drop any below the threshold, and truncate long passages to
the per-passage cap before composing the retrieved-knowledge
component.
- **Structure prompts so they compose
with prompt caching:** Order every prompt so
invariant content (system instructions, stable tool
definitions, pinned reference material) appears before
variant content (user turn, per-request retrievals), then
place
[Amazon
Bedrock prompt cache checkpoints](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-caching.html) in the
system, tools, and
messages fields at the boundary between
static and dynamic content. For long-running or intermittent
sessions on supported Claude models, set
"ttl": "1h" on the
cachePoint to extend the cache window
beyond the 5-minute default, keeping the 1-hour entry ahead
of any 5-minute entries in the same request.
- **Version prompts and gate changes on
evaluation:** Store prompts as versioned artifacts
in
[Amazon
Bedrock Prompt management](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-create.html) with variables for dynamic
inputs and inference configuration tied to the version, then
use
[Create
version](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-version-create.html) to snapshot known-good drafts. Use the
side-by-side variant comparison in the prompt builder to
evaluate candidates against each other, and promote a new
version only after it clears quality and token-cost
baselines on a representative test set.
- **Generate model-tuned rewrites with
prompt optimization:** Run candidate prompts
through
[Amazon
Bedrock Prompt Optimization](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-optimize.html) to produce model-specific
rewrites, passing the target model through
targetModelId when using the
OptimizePrompt API. Treat the optimized
output as a candidate variant rather than a drop-in
replacement, and compare it against the original on the same
evaluation set so token-count reductions are weighed against
any quality impact before promotion.

## Resources

**Related best practices:**

- [AGENTPERF03-BP01
Implement tiered memory management systems](agentperf03-bp01.html)
- [AGENTPERF03-BP03
Optimize RAG retrieval pipelines for latency and
precision](agentperf03-bp03.html)
- [AGENTPERF03-BP04
Establish efficient agent caching and data access
patterns](agentperf03-bp04.html)
- [AGENTPERF06-BP01
Design optimized tool integration strategies](agentperf06-bp01.html)

**Related documents:**

- [Amazon
Bedrock, Prompt caching for faster model inference](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-caching.html)
- [Amazon
Bedrock, Create a prompt using Prompt management](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-create.html)
- [Amazon
Bedrock, Create a version of a prompt in Prompt
management](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-version-create.html)
- [Amazon
Bedrock, Optimize a prompt](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-optimize.html)
- [Amazon
Bedrock, Design a prompt](https://docs.aws.amazon.com/bedrock/latest/userguide/design-a-prompt.html)
- [AgentCore
Gateway, Performance optimization (refined tool schemas and
semantic search)](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-advanced-performance.html)
- [AgentCore
Memory, Long-term built-in strategies (semantic, episodic,
summary, user preference)](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/long-term-configuring-built-in-strategies.html)
- [Foundations
of agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-foundations/introduction.html)

**Related services:**

- [Amazon
Bedrock](https://aws.amazon.com/bedrock/)
- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentperf03-bp02.html*

---

# AGENTPERF03-BP03 Optimize RAG retrieval pipelines for latency and precision

Retrieval-augmented generation gives agents access to knowledge
beyond the model's training data, but every reasoning iteration that
queries a retrieval pipeline pays its latency and inherits the
quality of its results. A well-tuned RAG pipeline returns
high-relevance passages within a small latency budget. Without this
discipline, retrieval either dominates per-iteration latency or
returns noisy context that degrades reasoning quality.

**Desired outcome:**

- You have a chunking strategy matched to the structure and query
shape of each source corpus, with chunk size and boundaries
tuned against retrieval precision rather than defaulted to a
single fixed size.
- You have retrieval latency tracked per stage (embedding, search,
and re-ranking) with explicit budgets so retrieval can't
silently consume time allocated to reasoning or tool calls.
- You have hybrid retrieval and re-ranking used where the corpus
and query mix justify their added latency, rather than stacked
by default.
- You have query reformulation ahead of every retrieval, so recall
holds when agent phrasing diverges from corpus vocabulary.
- You have retrieval precision and relevance continually evaluated
against a representative query set so quality regressions are
caught before they reach production behavior.

**Common anti-patterns:**

- Using a single fixed chunk size across all document types,
forcing structured content (tables, code, lists) through the
same boundaries as flowing prose and splitting related
information across chunks.
- Passing raw top-K retrieval results to the LLM without
re-ranking or relevance filtering, letting low-signal passages
displace high-signal context in the agent's prompt.
- Embedding the agent's raw query without reformulation, missing
relevant documents that use different terminology than the query
phrasing.
- Running every retrieval through pure dense similarity search
when the corpus contains exact identifiers, code, or numeric
values that keyword search recovers more reliably.
- Choosing an embedding model once and never revisiting it,
missing precision gains from newer models or domain-tuned
alternatives.
- Treating retrieval latency as a single metric rather than
attributing it across embedding, search, and re-ranking stages,
so performance regressions can't be localized.

**Benefits of establishing this best
practice:**

- Stage-level attribution and index tuning keep embedding, search,
and re-ranking within a predictable per-retrieval budget.
- Matching chunking strategy to document structure, hybrid
retrieval where warranted, and re-ranking before context
delivery keeps noise out of the prompt.
- High-precision first retrievals reduce the number of reasoning
iterations that retry retrieval with reformulated queries.
- Continuous evaluation against a representative query set detects
relevance drift before it reaches production.
- Tighter, more relevant retrievals consume less of the context
window, leaving more budget for reasoning.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

At ingest, four decisions fix what any future retrieval can see
before a single query runs: parsing, chunking, embedding, and the
choice of
[vector
store](https://docs.aws.amazon.com/prescriptive-guidance/latest/choosing-an-aws-vector-database-for-rag-use-cases/introduction.html). Query-time stages can filter and reorder what ingest
produced, but they can't recover information ingest discarded.
This asymmetry is the architectural reason RAG pipelines can't be
tuned as a single knob. Errors that are built in at ingest require
re-ingesting the whole corpus to fix. Query-time misconfigurations
can be patched without touching storage. When designers treat RAG
as an unknown, they inherit both sides of that commitment without
seeing where it was made.

Chunking is an ingest-time commitment with no cheap fix.
Fixed-size chunks fragment tables and mix unrelated passages when
topics shift mid-chunk. Hierarchical chunking preserves
nested-document relationships but roughly doubles the index
footprint because parent chunks are indexed alongside their
children. Semantic chunking breaks on meaning rather than token
count and can disagree with domain experts about where a topic
actually shifts.
[Advanced
parsing](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-advanced-parsing.html) recovers figures and tables from PDFs before
chunking runs but adds a foundation-model invocation per document.
Getting any of these wrong isn't a query-time tuning problem,
requiring a full re-embedding of the corpus to fix.

Three query-time stages each convert latency into precision, and
the embedding model used at ingest sets the floor for all three.

- Hybrid retrieval adds BM25 scoring alongside vector
similarity, recovering exact-match queries but doubling
first-stage work.
- Re-ranking runs a second, heavier model over a broad top-k to
earn back prompt tokens, spending milliseconds per passage.
- Query reformulation expands a single query into several,
trading fan-out latency for recall when agent phrasing misses
corpus terminology.

Stacking these stages doesn't give additive precision gains:
rerank over hybrid often matches rerank over dense-only, and
reformulation paired with re-ranking can overlap in what each
fixes. Layering all three yields a precision return that flattens
before the last layer contributes, and a latency cost that
doesn't.

Between one deploy and the next, corpora grow, embedding models
update, re-rankers retrain, and agent query patterns shift. Each
change can move retrieval quality in either direction with no
in-band signal. Drift is only detectable against a representative
query set labeled with expected passages.

Recall@k and nDCG@k quantify whether the right passages were
returned, and the RAG triad (context relevance, answer relevance,
groundedness) extends the measurement to whether retrieved context
actually supported the answer. The eval set is also the joint
between corpus owners, who update documents, and pipeline owners,
who tune stages. Without shared evaluation, teams can ship
regressions that other teams aren't aware of.

### Implementation steps

- **Inventory source corpora and query
patterns:** For each knowledge corpus the agent
will query, record document type (prose, hierarchical
document, PDF with figures, structured tables, code),
typical query shape (conceptual intent vs. exact
identifier), expected query volume, and precision/latency
budget. This inventory drives every downstream choice
(chunking strategy, embedding model, index configuration,
and re-ranker placement). Without it, the pipeline is tuned
by guess against an imagined average.
- **Choose a chunking and parsing
strategy per corpus:** For flowing prose, use
semantic chunking to break on meaning. For nested documents,
use hierarchical chunking to preserve parent-child context.
For PDFs and multimodal content with figures or tables,
enable
[advanced
parsing](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-advanced-parsing.html) via a foundation model or Amazon Bedrock Data
Automation before chunking. Configure the strategy in the
[Knowledge
Base chunking configuration](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-chunking.html) per data source rather
than defaulting every source to fixed-size chunks.
- **Select an embedding model and
dimensionality:** Pick an embedding model that
covers the modalities, languages, and domain of the corpora
and whose cost and latency fit the per-retrieval budget.
[Amazon
Titan Text Embeddings V2](https://docs.aws.amazon.com/bedrock/latest/userguide/titan-embedding-models.html) exposes configurable output
dimensions so text-corpus index size, recall, and query
latency can be balanced against each other, and
[Amazon
Nova Multimodal Embeddings](https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-amazon-amazon-nova-multimodal-embeddings.html) produces a single
embedding space across text, images, video, and audio for
corpora that contain mixed modalities. Re-evaluate the
choice when new models are released, because embedding
quality improvements translate directly into retrieval
precision.
- **Configure the index for the
retrieval pattern:** For corpora with both
conceptual and exact-match queries, enable hybrid search
rather than relying on pure dense similarity. With Amazon
Bedrock Knowledge Bases backed by Amazon OpenSearch Service
Serverless, set
[overrideSearchType: HYBRID](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html)
on the Retrieve request to combine vector and raw-text
scoring in a single call. For direct OpenSearch workloads,
configure
[neural
and hybrid search](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-configure-neural-search.html) explicitly. Apply metadata filters
on the retrieve request to narrow the search space by
document source, freshness, or scope before vector
similarity runs, and tune
[vector
index parameters](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/vector-search.html) against retrieval precision on a
representative query set so the index favors recall or
latency according to the workload's budget.
- **Add re-ranking before context
delivery:** Run first-stage retrieval at a wider
top-K than the prompt context budget allows, then pass the
results through
[Amazon
Bedrock Rerank](https://docs.aws.amazon.com/bedrock/latest/userguide/rerank.html) to produce a higher-precision subset.
The re-ranker compensates for vector-search noise and lets
the LLM receive fewer but higher-relevance passages, which
both tightens prompt quality and reduces input tokens.
Configure the re-ranker on the Knowledge Base retrieve
request rather than orchestrating it client-side so the hop
stays inside the retrieval path.
- **Enable query
reformulation:** Transform agent-generated queries
before they hit the index so retrieval doesn't fail on
terminology mismatches with the source corpus. Knowledge
Bases supports
[query
reformulation and decomposition](https://aws.amazon.com/blogs/machine-learning/amazon-bedrock-knowledge-bases-now-supports-advanced-parsing-chunking-and-query-reformulation-giving-greater-control-of-accuracy-in-rag-based-applications/) through the Retrieve
API, expanding a broad question into focused sub-queries
executed against the index. Prefer the managed reformulation
path over a bespoke preprocessing step so it stays colocate
with the retrieval hop and benefits from future improvements
to the feature.
- **Instrument per-stage retrieval
latency and relevance:** Emit distinct metrics for
embedding latency, search latency, re-ranker latency, top-k
size, and the relevance score distribution of returned
passages, dimensioned by data source and query class.
Per-stage attribution makes it possible to localize
regressions. A rising re-ranker latency with a stable search
latency points at a different root cause than the reverse.
Set per-stage budgets that sum to the pipeline's end-to-end
latency target so any single stage exceeding its budget
alerts before end-to-end performance is affected.
- **Evaluate the pipeline on a
representative query set on a defined cadence:**
Maintain a fixed evaluation set that spans the corpora and
query shapes in the inventory, and run it against the
pipeline on every significant change (new data source,
chunking change, embedding or re-ranker upgrade, index
parameter tuning), following the approach in
[Evaluate
and improve performance of Amazon Bedrock Knowledge
Bases](https://aws.amazon.com/blogs/machine-learning/evaluate-and-improve-performance-of-amazon-bedrock-knowledge-bases/). Track Recall@k, nDCG@k, and RAG triad scores
per change so quality regressions are caught before rollout,
and refresh the evaluation set as real query patterns drift.

## Resources

**Related best practices:**

- [AGENTPERF03-BP01
Implement tiered memory management systems](agentperf03-bp01.html)
- [AGENTPERF03-BP02
Optimize context window utilization and prompt
management](agentperf03-bp02.html)
- [AGENTPERF03-BP04
Establish efficient agent caching and data access
patterns](agentperf03-bp04.html)
- [AGENTPERF03-BP05
Implement agentic retrieval patterns for dynamic, agent-driven
knowledge access](agentperf03-bp05.html)

**Related documents:**

- [Amazon
Bedrock Knowledge Bases, How content chunking works](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-chunking.html)
- [Amazon
Bedrock Knowledge Bases, Parsing options for your data
source](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-advanced-parsing.html)
- [Amazon
Bedrock Knowledge Bases, Query configurations](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html)
- [Amazon
Bedrock, Improve the relevance of query responses with a
re-ranker model](https://docs.aws.amazon.com/bedrock/latest/userguide/rerank.html)
- [Amazon
Titan Text Embeddings models](https://docs.aws.amazon.com/bedrock/latest/userguide/titan-embedding-models.html)
- [Amazon
Nova Multimodal Embeddings](https://docs.aws.amazon.com/bedrock/latest/userguide/model-card-amazon-amazon-nova-multimodal-embeddings.html)
- [Amazon OpenSearch Service, Vector search](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/vector-search.html)
- [Amazon OpenSearch Service Serverless, Configure Neural Search and Hybrid
Search](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-configure-neural-search.html)
- [Blog:
Amazon Bedrock Knowledge Bases, advanced parsing, chunking,
and query reformulation](https://aws.amazon.com/blogs/machine-learning/amazon-bedrock-knowledge-bases-now-supports-advanced-parsing-chunking-and-query-reformulation-giving-greater-control-of-accuracy-in-rag-based-applications/)
- [Blog:
Evaluate and improve performance of Amazon Bedrock Knowledge
Bases](https://aws.amazon.com/blogs/machine-learning/evaluate-and-improve-performance-of-amazon-bedrock-knowledge-bases/)
- [Choosing
an AWS vector database for RAG use cases](https://docs.aws.amazon.com/prescriptive-guidance/latest/choosing-an-aws-vector-database-for-rag-use-cases/introduction.html)

**Related videos:**

- [AWS re:Invent 2025 - Advanced agentic RAG Systems: Deep dive with
Amazon Bedrock (AIM425)](https://www.youtube.com/watch?v=bu2cD1pCFTs)

**Related examples:**

- [GitHub:
Amazon Bedrock samples, Knowledge Bases and RAG](https://github.com/aws-samples/amazon-bedrock-samples)

**Related tools:**

- [Amazon
Bedrock Knowledge Bases](https://aws.amazon.com/bedrock/knowledge-bases/)
- [Amazon OpenSearch Service](https://aws.amazon.com/opensearch-service/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentperf03-bp03.html*

---

# AGENTPERF03-BP04 Establish efficient agent caching and data access patterns

Agents that repeatedly fetch the same data benefit from caching,
breaking the cycle of redundant retrievals speeds up every reasoning
iteration. Agentic workloads often access the same tool outputs,
retrieved documents, computed embeddings, and configuration data
across multiple reasoning iterations, sessions, or agents in a
multi-agent workflow. Without caching, each access pays the full
latency and cost of the original operation.

**Desired outcome:**

- You have multi-layer caching that removes redundant computations
and data fetches across reasoning iterations, sessions, and
agents.
- You have cache hit rates monitored and optimized.
- You have cache invalidation policies tuned to balance freshness
requirements with performance benefits.

**Common anti-patterns:**

- Implementing no caching at all, forcing agents to re-fetch the
same documents, re-compute the same embeddings, and re-invoke
the same tools on every reasoning iteration.
- Using a single cache TTL for all data types without considering
freshness requirements, producing either stale data (TTL too
long) or poor hit rates (TTL too short).
- Designing cache keys based only on exact string matching,
missing cache hits for semantically equivalent queries that use
different phrasing.

**Benefits of establishing this best
practice:**

- Cache hits substantially reduce latency for repeated data
access.
- Removing redundant LLM inference calls and external API
invocations lowers cost.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Caching is applied at multiple layers of the agent stack, and each
layer has its own invalidation discipline.

At the LLM inference layer,
[Amazon
Bedrock prompt caching](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-caching.html) caches and reuses common prompt
prefixes (like system instructions and tool definitions) across
invocations, reducing both latency and cost for repeated portions
of prompts, prompt caching savings compound further when combined
with Amazon Bedrock's Flex pricing tier for development and
testing workloads.

At the retrieval layer, caching RAG query results under semantic
cache keys (embedding-based similarity) rather than exact string
matching lets semantically similar queries share cached results.

At the tool invocation layer, caching tool outputs based on input
parameters with TTLs matched to the data's freshness requirements,
a cached stock price has a very different TTL than a cached
company description.

Cache warming is valuable where access patterns are predictable.
If agents frequently access the same knowledge base sections
during business hours, pre-warming the cache before peak periods
avoids the first-miss penalty for early users. Data access
patterns benefit from batching: retrieving multiple items in a
single round trip rather than making sequential individual
requests reduces both latency and connection overhead.

Monitoring cache hit rates, latency savings, and cost savings per
cache layer in Amazon CloudWatch makes caching a tunable
parameter.

### Implementation steps

- **Identify cacheable data across the
agent stack:** Enumerate LLM prompt prefixes, RAG
results, tool outputs, session state, and configuration
data, each has its own access pattern, freshness
requirement, and cache layer.
- **Enable Amazon Bedrock prompt caching
for common prompt prefixes shared across
invocations:** Turn on
[Amazon
Bedrock prompt caching](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-caching.html) and structure prompts so
system instructions and tool definitions appear before
variable content, letting the cached prefix be reused across
requests.
- **Implement retrieval result caching
with semantic cache keys and data-type-specific
TTLs:** Cache RAG results under embedding-based
similarity keys so semantically equivalent queries share
results, and tune TTLs to the freshness needs of each data
type rather than applying a single global TTL.
- **Implement tool output caching with
TTLs calibrated to data freshness requirements:**
Cache tool outputs under input-parameter keys with TTLs that
match how fast each tool's data changes, short TTLs for
real-time data, long TTLs for static reference data.
- **Monitor cache hit rates and latency
savings per cache layer using CloudWatch:** Publish
hit rate, miss rate, and latency savings per cache layer as
CloudWatch metrics so TTLs and warming strategies can be
tuned from data rather than assumption.

## Resources

**Related best practices:**

- [AGENTPERF03-BP01
Implement tiered memory management systems](agentperf03-bp01.html)
- [AGENTPERF03-BP03
Optimize RAG retrieval pipelines for latency and
precision](agentperf03-bp03.html)
- [AGENTPERF02-BP03
Optimize agent execution paths for reduced latency](agentperf02-bp03.html)

**Related documents:**

- [Amazon
Bedrock prompt caching](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-caching.html)
- [Blog:
Effectively use prompt caching on Amazon Bedrock](https://aws.amazon.com/blogs/machine-learning/effectively-use-prompt-caching-on-amazon-bedrock/)
- [Blog:
Optimize LLM response costs and latency with effective
caching](https://aws.amazon.com/blogs/database/optimize-llm-response-costs-and-latency-with-effective-caching/)
- [Foundations
of agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-foundations/introduction.html)

**Related services:**

- [Amazon
Bedrock](https://aws.amazon.com/bedrock/)
- [Amazon ElastiCache](https://aws.amazon.com/elasticache/)
- [Amazon DynamoDB](https://aws.amazon.com/dynamodb/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentperf03-bp04.html*

---

# AGENTPERF03-BP05 Implement agentic retrieval patterns for dynamic, agent-driven knowledge access

Complex questions often require information from multiple sources,
iterative refinement, or real-time data that a single retrieval pass
can't provide. In agentic retrieval the agent actively controls the
retrieval process as part of its reasoning loop, deciding when to
retrieve, what to retrieve, which retrieval tool to use, and whether
the retrieved context is sufficient before proceeding. Each
iteration adds embedding generation, vector search, re-ranking, and
context injection overhead, so the retrieval loop needs explicit
termination conditions.

**Desired outcome:**

- You have agents retrieving the right information in the minimum
number of iterations required.
- You have simple questions answered with a single retrieval and
complex questions handled through structured multi-hop retrieval
with explicit termination conditions.
- You have the agent selecting the most appropriate retrieval tool
for each query type.
- You have retrieval iteration counts, per-iteration latency, and
sufficiency rates tracked and optimized.

**Common anti-patterns:**

- Treating all retrieval as a single-shot preprocessing step,
forcing the agent to work with whatever context was retrieved on
the first attempt regardless of sufficiency.
- Allowing agents to retrieve iteratively without retrieval
budgets or termination conditions, producing unbounded retrieval
loops that consume tokens and latency without converging.
- Routing all retrieval through a single pipeline regardless of
query type, missing opportunities to use faster or more
appropriate retrieval tools for different information needs.

**Benefits of establishing this best
practice:**

- Parallel sub-query execution and retrieval-tool routing reduce
end-to-end latency by selecting the fastest appropriate source.
- Explicit budgets that cap iterations and total tokens keep
retrieval costs under control.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Design retrieval as a set of agent tools rather than a monolithic
pipeline. Distinct retrieval tools for different knowledge access
patterns let the agent route to the right source:

- A semantic search tool backed by
[Amazon
Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html) for conceptual questions
- A structured query tool for exact lookups by identifier
- A real-time data tool for information requiring current values
- A web search tool for questions beyond the organization's
knowledge base
- A document processing tool backed by
[Amazon
Bedrock Data Automation](https://docs.aws.amazon.com/bedrock/latest/userguide/bda.html) for extracting structured data
from images, forms, and tables

[Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) exposes retrieval tools as
MCP-compatible endpoints, and registering each tool with clear
descriptions, what question types it handles, what data sources it
accesses, and its expected latency guides the agent's tool
selection.

Retrieval sufficiency evaluation is a lightweight assessment after
each retrieval iteration, typically run by a smaller, faster
model. The evaluator judges whether the retrieved context is
sufficient, identifies gaps, and formulates refined queries. A
maximum retrieval iteration limit (typically 2-3 iterations) helps
prevent unbounded loops. If the agent has not retrieved sufficient
context within the budget, it proceeds with the best available
context and communicates uncertainty.

For complex questions requiring multiple sources, query
decomposition breaks the question into focused sub-queries and
runs independent sub-queries concurrently. Per-task retrieval
performance budgets, derived from the task's overall latency SLO,
keep the iterative pattern inside the workload's target.

### Implementation steps

- **Implement distinct retrieval tools
for different knowledge access patterns:** Register
a semantic search tool, a structured-query tool, a real-time
data tool, a web search tool, and a document processing tool
through
[Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) with clear descriptions
that guide the agent's tool selection.
- **Implement retrieval sufficiency
evaluation as a lightweight post-retrieval
assessment:** Use a small, fast model to judge
whether retrieved context is sufficient, identify gaps, and
formulate refined queries for the next iteration.
- **Configure maximum retrieval
iteration limits with graceful fallback to best-available
context:** Cap iterations at 2-3 for most tasks,
and when the budget is exhausted proceed with the best
context obtained and communicate uncertainty rather than
looping without bounds.
- **Implement query decomposition for
complex questions, running independent sub-queries
concurrently:** Break multi-source questions into
focused sub-queries and fan them out in parallel so
sub-query latency doesn't accumulate serially.
- **Define per-task retrieval
performance budgets based on the overall latency
SLO:** Allocate an explicit portion of the task's
latency SLO to retrieval so the iterative pattern can't
silently consume the budget reserved for inference or
downstream tool calls.

## Resources

**Related best practices:**

- [AGENTPERF03-BP03
Optimize RAG retrieval pipelines for latency and
precision](agentperf03-bp03.html)
- [AGENTPERF03-BP02
Optimize context window utilization and prompt
management](agentperf03-bp02.html)
- [AGENTPERF02-BP01
Design efficient reasoning pipelines](agentperf02-bp01.html)
- [AGENTREL05-BP03
Ground agent cognition in real information](agentrel05-bp03.html)
- [AGENTCOST03-BP02
Cost optimize through intelligent compression and pruning of
context windows](agentcost03-bp02.html)

**Related documents:**

- [Amazon
Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html)
- [Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html)
- [Amazon
Bedrock Data Automation](https://docs.aws.amazon.com/bedrock/latest/userguide/bda.html)
- [Agentic
AI patterns and workflows on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/introduction.html)
- [Blog:
Building intelligent search with Amazon Bedrock and Amazon OpenSearch Service for hybrid RAG solutions](https://aws.amazon.com/blogs/machine-learning/building-intelligent-search-with-amazon-bedrock-and-amazon-opensearch-for-hybrid-rag-solutions/)

**Related examples:**

- [GitHub:
Advanced RAG using Bedrock and SageMaker AI](https://github.com/aws-samples/sample-advanced-rag-using-bedrock-and-sagemaker)

**Related services:**

- [Amazon
Bedrock Knowledge Bases](https://aws.amazon.com/bedrock/knowledge-bases/)
- [Amazon
Bedrock AgentCore Gateway](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon OpenSearch Service](https://aws.amazon.com/opensearch-service/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentperf03-bp05.html*

---
