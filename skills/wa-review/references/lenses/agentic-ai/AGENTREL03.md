# AGENTREL03 — Agent memory and state management

**Pillar**: Reliability  
**Best Practices**: 4

---

# AGENTREL03-BP01 Design an information classification model to identify short-term and long-term memories

A single undifferentiated memory store blurs conversation context
with durable knowledge and pulls stale or irrelevant data into
active tasks. Classifying memory at ingestion time and routing each
item to the right tier keeps retrieval predictable and storage costs
aligned with how long each type actually needs to live.

**Desired outcome:**

- You have an explicit memory taxonomy distinguishing short-term
session context from long-term persistent knowledge.
- Your agents classify information at ingestion time and route it
to the appropriate tier with metadata tags.
- You retain each memory type according to a policy matched to its
persistence requirement.

**Common anti-patterns:**

- Storing all memory in a single undifferentiated store, so agents
retrieve stale or irrelevant items during active tasks.
- Running without retention or eviction policies for short-term
memory, letting session context accumulate indefinitely.
- Skipping classification at ingestion, making targeted retrieval
and appropriate retention impossible.

**Benefits of establishing this best
practice:**

- Predictable retrieval through explicit classification that
routes information to the correct store.
- Storage costs aligned with persistence requirements instead of a
one-size-fits-all retention window.
- Reduced context pollution because transient session data can't
contaminate long-term knowledge.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

A memory taxonomy is the foundation. At minimum, distinguish
short-term (scoped to a single conversation) from long-term
(durable across sessions). For complex agents, extend the taxonomy
to include episodic memory (records of specific past interactions)
and semantic memory (general domain knowledge). The taxonomy
should be documented in accessible reference materials in addition
to code, because classification decisions happen at ingestion and
must be consistent across agents that write to shared memory.

[Amazon
Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) provides session-scoped and
persistent memory namespaces, handling the underlying
infrastructure. Use session memory for short-term context scoped
to a single conversation, persistent memory for cross-session
knowledge, and shared memory for facts multiple agents consume.
[Amazon
Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html) handles RAG over external document
corpora, policy documents, product catalogs, and domain reference
material that supplement agent memory with organizational
knowledge.

Classification logic belongs in a dedicated component of the
agent's processing flow, not scattered across prompts. Evaluate
each piece of information against source (conversation turn
vs. task outcome), temporal scope (session-specific
vs. cross-session), and content type (procedural vs. factual).
Route accordingly and tag with metadata so later retrieval can
filter precisely. Monitor memory access patterns through
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) to catch misclassified
memories. The signal is usually unexpectedly high retrieval rates
from the wrong tier.

### Implementation steps

- **Define a memory taxonomy:**
Document classification criteria for each memory type
(session context, persistent knowledge, episodic records)
and the retention policy that fits each.
- **Configure AgentCore Memory
namespaces:** Provision
[Amazon
Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) with session-scoped and
persistent namespaces that map to the taxonomy.
- **Implement classification logic at
ingestion:** Evaluate each item against the
taxonomy criteria and route to the appropriate tier with
metadata tags.
- **Use Amazon Bedrock Knowledge Bases
for external corpora:** Supplement agent memory
with
[Amazon
Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html) for RAG over organizational
knowledge.
- **Monitor access patterns to detect
classification errors:** Use
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) to spot unexpectedly
high retrieval rates from wrong tiers.

## Resources

**Related best practices:**

- [AGENTREL03-BP02
Architect fault-tolerant memory stores with redundancy and
failover](agentrel03-bp02.html)
- [AGENTREL03-BP03
Implement comprehensive state management and checkpoint-based
recovery](agentrel03-bp03.html)
- [AGENTREL03-BP04
Implement graceful degradation for memory and state
operations](agentrel03-bp04.html)
- [AGENTSUS02-BP01
Optimize context management and memory utilization](agentsus02-bp01.html)

**Related documents:**

- [Amazon
Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html)
- [Amazon
Bedrock AgentCore Memory: Building context-aware agents](https://aws.amazon.com/blogs/machine-learning/amazon-bedrock-agentcore-memory-building-context-aware-agents/)
- [Building
smarter AI agents: AgentCore long-term memory deep dive](https://aws.amazon.com/blogs/machine-learning/building-smarter-ai-agents-agentcore-long-term-memory-deep-dive/)
- [Amazon
Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html)
- [Strands
Agents Session Management](https://strandsagents.com/docs/user-guide/concepts/agents/conversation-management/)

**Related videos:**

- [AWS 2025 - AgentCore Deep Dive: Memory](https://www.youtube.com/watch?v=-N4v6-kJgwA)
- [AWS re:Invent 2024 - Make agents remember with AgentCore Memory
(AIM331)](https://www.youtube.com/watch?v=Sh0Ro00_rpA)

**Related workshops:**

- [Getting
started with Amazon Bedrock AgentCore - Lab 2: Memory](https://catalog.workshops.aws/agentcore-getting-started/en-US/30-add-memory)
- [Diving
Deep into Bedrock AgentCore - Memory](https://catalog.workshops.aws/agentcore-deep-dive/en-US/50-agentcore-memory)

**Related services:**

- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon
Bedrock](https://aws.amazon.com/bedrock/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentrel03-bp01.html*

---

# AGENTREL03-BP02 Architect fault-tolerant memory stores with redundancy and failover

Memory failures don't need to mean agent failures. With redundancy,
fallback paths, and a discipline of testing failover under
controlled conditions, an agent keeps serving reduced-capability
responses until its primary stores recover instead of becoming
completely unavailable.

**Desired outcome:**

- You have primary memory infrastructure with built-in durability
and availability, backed by explicit fallback stores for
degraded operation.
- You have fail-fast logic on memory access that routes to
fallback when primary stores are unavailable.
- You exercise failover regularly in non-production environments
to validate degraded-mode behavior.

**Common anti-patterns:**

- Running memory stores as single points of failure without
replication or failover, causing complete memory loss during
outages.
- Leaving failover manual, so recovery waits on operators and
extends agent downtime.
- Skipping failover testing, discovering the gaps only when
production incidents force the issue.

**Benefits of establishing this best
practice:**

- Downtime drops because automated failover takes over before
operators can intervene.
- Agents keep behaving consistently during memory store failures
through graceful degradation.
- Memory replication across Availability Zones helps protect
against data loss.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

[Amazon
Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) provides managed memory
infrastructure with built-in durability and availability, so the
default path is already fault-tolerant. The design work is on the
degraded path: what does the agent do when even the managed store
is briefly unreachable, or when a custom store sits alongside it?
Fail-fast logic on memory access is the first answer. When a store
shows elevated error rates, the caller stops waiting and routes to
a fallback. For short-term memory, that fallback is an in-process
cache. For long-term memory, it is a read-through cache of
frequently accessed items.

For agents running on
[Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html), the runtime's managed session
storage persists filesystem-level state across stop and resume
cycles. For workflow-stage-aware checkpointing with redrive from
specific failure points, use
[AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html) or framework-level orchestration such as
LangGraph with AgentCore Memory. The choice depends on how
granular the recovery needs to be. Step Functions gives you
durability for each step, while managed session storage gives you
whole-agent durability at session boundaries.

Regular testing validates that failover mechanisms work as
designed.
[AWS Fault Injection Service](https://docs.aws.amazon.com/fis/latest/userguide/what-is.html) simulates memory store failures in
non-production environments so you can validate that failover
mechanisms activate correctly and agents continue operating in
degraded mode. Document expected behavior for each failure
scenario and compare observed behavior against the expectations
every time you run the test. Drift between what you expect and
what actually happens is the signal that a regression slipped in.

### Implementation steps

- **Use AgentCore Memory as the primary
managed store:** Default to
[Amazon
Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) for its built-in durability
and availability.
- **Implement fail-fast logic for memory
access:** Detect elevated error rates on memory
calls and route to fallback stores.
- **Maintain in-process fallback caches
for short-term memory:** Keep current sessions
moving through a last-resort cache that lets the task
complete.
- **Implement read-through caching for
long-term memory:** Serve cached copies of
frequently accessed items during temporary unavailability.
- **Test failover with AWS Fault
Injection Service:** Use
[AWS Fault Injection Service](https://docs.aws.amazon.com/fis/latest/userguide/what-is.html) to validate degraded-mode
behavior against documented expectations on a regular
schedule.

## Resources

**Related best practices:**

- [AGENTREL01-BP02
Establish modular, fault-isolated layers](agentrel01-bp02.html)
- [AGENTREL03-BP01 Design
an information classification model to identify short-term and
long-term memories](agentrel03-bp01.html)
- [AGENTREL03-BP03
Implement comprehensive state management and checkpoint-based
recovery](agentrel03-bp03.html)
- [AGENTREL03-BP04
Implement graceful degradation for memory and state
operations](agentrel03-bp04.html)

**Related documents:**

- [Amazon
Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html)
- [Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html)
- [AWS Fault Injection Service](https://docs.aws.amazon.com/fis/latest/userguide/what-is.html)
- [AWS fail-fast pattern](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/circuit-breaker.html)

**Related examples:**

- [GitHub:
awslabs/amazon-bedrock-agentcore-samples - Memory
tutorials](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/04-AgentCore-memory)

**Related services:**

- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [AWS Fault
Injection Service](https://aws.amazon.com/fis/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentrel03-bp02.html*

---

# AGENTREL03-BP03 Implement comprehensive state management and checkpoint-based recovery

Long-running workflows without checkpoints pay the full restart cost
for every failure, no matter how late it happens. Persisting state
at natural boundaries and designing every step to be idempotent lets
an agent resume from the last completed checkpoint rather than redo
work.

**Desired outcome:**

- You have workflow state persisted at regular checkpoints, so
interruptions resume from the last completed point rather than
the beginning.
- You have idempotent workflow steps that produce the same result
when replayed with the same input.
- You have a checkpoint lifecycle with TTL-based expiration and
explicit cleanup after completion.

**Common anti-patterns:**

- Running long-duration agent workflows without intermediate state
persistence, forcing complete restarts on any failure.
- Implementing checkpoints without idempotency guarantees,
producing data corruption or duplicate side effects on resume.
- Skipping checkpoint cleanup, accumulating storage indefinitely.

**Benefits of establishing this best
practice:**

- Workflow restart cost drops because resume starts from the last
checkpoint.
- Duplicate work is prevented through idempotent checkpoint-based
recovery.
- Compute efficiency improves because recovery avoids redundant
recomputation.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Checkpointing is only useful if recovery is safe, and recovery is
only safe if steps are idempotent. An idempotent step produces the
same result whether it runs once or five times with the same
input, which means a retry or a resume doesn't add duplicate side
effects. This constraint shapes everything downstream. External
calls need idempotency keys, state mutations need conditional
writes, and event emissions need deduplication logic. Without
idempotency guarantees, checkpoint-based recovery can produce
duplicate side effects or data corruption. Design each step to be
idempotent before implementing checkpointing.

Runtime choice determines how much checkpointing discipline you
need to build yourself.
[Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html) supports long-running workloads
with managed session storage that persists filesystem state across
stop and resume cycles, which covers the coarse-grained case. For
workflow-stage-aware checkpointing with redrive from specific
failure points, orchestrate through
[AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html). Step Functions persists execution state at
every transition and enables restart from the point of failure
rather than from the beginning. For dynamic workflows driven by
supervisor agents, callback patterns pause execution while the
supervisor decides the next action, preserving state persistence
benefits.

Lifecycle management keeps the checkpoint store from growing
without bound. TTL-based expiration handles the common case:
workflows that never complete eventually age out. Explicit cleanup
after successful completion reclaims space immediately. Use
[Amazon
Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) to persist checkpoint state and
specification context for agents requiring custom checkpointing.
Monitor checkpoint store health through
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) so storage growth or access
latency surfaces before recovery starts failing.

### Implementation steps

- **Deploy agents on AgentCore Runtime
with managed session storage:** Use
[Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html) for filesystem-level state
persistence across stop and resume cycles.
- **Orchestrate multi-step workflows
through Step Functions:** Use
[AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html) for state persistence at every
transition with redrive capability from the point of
failure.
- **Design every workflow step to be
idempotent:** Require idempotency keys on external
calls and conditional writes on state mutations so retries
and resumes don't introduce duplicate side effects.
- **Use AgentCore Memory for custom
checkpoint state:** Persist checkpoint state and
specification context through
[Amazon
Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) for agents with bespoke
checkpointing needs.
- **Implement checkpoint lifecycle
management:** Set TTL-based expiration and explicit
cleanup after successful completion so the checkpoint store
stays bounded.

## Resources

**Related best practices:**

- [AGENTREL03-BP01 Design
an information classification model to identify short-term and
long-term memories](agentrel03-bp01.html)
- [AGENTREL03-BP02
Architect fault-tolerant memory stores with redundancy and
failover](agentrel03-bp02.html)
- [AGENTREL07-BP01
Design workflows in stages with incremental recovery](agentrel07-bp01.html)

**Related documents:**

- [Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html)
- [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html)
- [Amazon
Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html)
- [Build
resilient generative AI agents](https://aws.amazon.com/blogs/architecture/build-resilient-generative-ai-agents)

**Related services:**

- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [AWS Step Functions](https://aws.amazon.com/step-functions/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentrel03-bp03.html*

---

# AGENTREL03-BP04 Implement graceful degradation for memory and state operations

Treating every memory failure as fatal turns recoverable issues into
total outages. An explicit degradation hierarchy with documented
modes and automatic recovery keeps agents partially useful and
transparent about their reduced state.

**Desired outcome:**

- You have a memory degradation hierarchy with distinct
operational modes and documented behaviors for each.
- You transition modes automatically based on memory health
signals, and recover to full mode when stores return.
- You communicate degradation state to users and orchestration
systems so they know what to expect.

**Common anti-patterns:**

- Treating all memory failures as fatal, producing complete
unavailability for conditions that could be handled with reduced
functionality.
- Failing to communicate degraded memory state to users, who then
get confused when responses lack expected context.
- Implementing degradation without a recovery path, leaving agents
in degraded mode indefinitely after primary stores return.

**Benefits of establishing this best
practice:**

- Partial service availability persists through memory store
failures instead of becoming a full outage.
- Users and orchestrators see transparent indications of current
capability.
- Full capability returns automatically when memory stores come
back online.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Start with the mode hierarchy. Three modes cover most agent
workloads. Full mode has all memory tiers available. Session-only
mode operates without long-term memory, using only session
context. Stateless mode has both tiers unavailable and processes
each request independently. For each mode, define the agent's
behavior explicitly:

- In session-only mode, inform users that previous session
context is unavailable
- In stateless mode, request all necessary context within the
current interaction.

Without this definition, the fallback path is whatever the code
happens to do, which is rarely what you want during an incident.

Health signals drive the transitions.
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) and Amazon CloudWatch
together track memory store availability and error rates.
Configure automated mode transitions when health degrades below
thresholds you set in advance, and automatic recovery when stores
return. For short-term memory degradation, in-process fallback
caches let the current session continue.
[Amazon
Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) session management maintains
working context even when long-term stores are degraded, which
keeps most conversations coherent through a partial outage.

Communicate degradation state through structured status indicators
so users and downstream systems understand the current
limitations. "I don't have access to your previous
conversations right now" is a better experience than an
agent that silently pretends it does and hallucinates. The same
signals feed orchestration systems that might choose to route
requests elsewhere or surface a banner to users.

### Implementation steps

- **Define a memory degradation
hierarchy with documented modes:** Specify full,
session-only, and stateless modes, with the agent behavior
each mode dictates.
- **Implement automated mode
transitions:** Trigger transitions through health
metrics from
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) and Amazon CloudWatch.
- **Maintain in-process fallback caches
for short-term memory:** Allow active sessions to
continue when short-term memory degrades.
- **Communicate degradation state to
users:** Surface structured status indicators so
users see the reduced capability instead of guessing.
- **Configure automatic recovery
detection:** Return agents to full mode when stores
become available, without operator intervention.

## Resources

**Related best practices:**

- [AGENTREL03-BP01 Design
an information classification model to identify short-term and
long-term memories](agentrel03-bp01.html)
- [AGENTREL03-BP02
Architect fault-tolerant memory stores with redundancy and
failover](agentrel03-bp02.html)
- [AGENTREL08-BP04
Track agent memory utilization metrics](agentrel08-bp04.html)

**Related documents:**

- [Amazon
Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html)
- [Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html)
- [Build
resilient generative AI agents](https://aws.amazon.com/blogs/architecture/build-resilient-generative-ai-agents)

**Related examples:**

- [GitHub:
awslabs/amazon-bedrock-agentcore-samples - Memory
tutorials](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/04-AgentCore-memory)

**Related services:**

- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentrel03-bp04.html*

---
