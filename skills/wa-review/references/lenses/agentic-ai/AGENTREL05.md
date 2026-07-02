# AGENTREL05 — Agent cognition

**Pillar**: Reliability  
**Best Practices**: 3

---

# AGENTREL05-BP01 Design modular, fault-tolerant agentic reasoning components

A monolithic reasoning pipeline fails completely whenever any stage
fails. Splitting cognition into modular stages with clear interfaces
and stage-specific fallbacks lets an agent keep reasoning, with
reduced quality, even when one stage is degraded.

**Desired outcome:**

- You have the reasoning pipeline decomposed into modular stages
with explicit input/output schemas.
- You have stage-specific fallbacks that activate automatically
when error rates climb.
- You log the retrieval tier and model tier used in each
invocation so quality analysis is possible after the fact.

**Common anti-patterns:**

- Running agent cognition as a monolithic pipeline where any
component failure causes complete cognition failure.
- Skipping interfaces between reasoning components, reducing the
ability for independent testing and replacement.
- Treating all reasoning components as equally critical without
distinguishing essential from quality-enhancing components.

**Benefits of establishing this best
practice:**

- Partial cognition survives individual component failures through
modular fault isolation.
- Reasoning components can be optimized or replaced independently,
without full pipeline rewrites.
- Clear component boundaries isolate the source of errors and
speed up debugging.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

The first architectural decision is where the stage boundaries go.
Useful boundaries for most agents are context retrieval, prompt
construction, model inference, output parsing, and action
selection. Each stage has a narrow contract: inputs, outputs, and
the error conditions it signals. Deploy each stage on
[Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html) with its own error handling and
fallback behavior. Without this decomposition, all errors appear
as generic reasoning failures, making debugging difficult. Clear
stage boundaries enable precise error identification and faster
resolution.

Tiering is where the stages earn their modularity. For context
retrieval, primary tier uses
[Amazon
Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html) for semantic search, with fallback
to simpler retrieval methods when the primary is unavailable. For
model inference, implement model tier fallback using
[Bedrock
cross-region inference](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html) for availability, substituting
alternative models when the primary is degraded. For multimodal
agents,
[Amazon
Bedrock Data Automation](https://docs.aws.amazon.com/bedrock/latest/userguide/bda.html) preprocesses documents, images,
audio, and video as a distinct reasoning stage before text-based
reasoning, with independent fallbacks per modality.

Track per-stage error rates, latency, and fallback activation
frequency through
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html). Configure alarms that
trigger automatic cutoffs when stage health degrades. The cutoff
activates the fallback immediately rather than waiting for the
next failed invocation. Log the retrieval tier and model tier used
in each invocation so you can see, months later, which tier
produced the answer and whether the fallback path is being taken
more often than expected.

### Implementation steps

- **Decompose the reasoning pipeline
into distinct stages:** Define explicit
input/output schemas and deploy each stage on
[Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html).
- **Implement automatic cutoffs between
stages:** Activate stage-specific fallbacks when
error rates exceed thresholds.
- **Build tiered context
retrieval:** Use
[Amazon
Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html) as primary with progressively
simpler fallbacks.
- **Implement model tier
fallback:** Use
[Bedrock
cross-region inference](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html) for availability during
primary model degradation.
- **Monitor per-stage health:**
Track error rates, latency, and fallback activation through
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) with alarms that
trigger automatic cutoffs.

## Resources

**Related best practices:**

- [AGENTREL01-BP02
Establish modular, fault-isolated layers](agentrel01-bp02.html)
- [AGENTREL05-BP02
Facilitate reliable adaptation through evaluation-driven
improvement cycles](agentrel05-bp02.html)
- [AGENTREL05-BP03 Ground
agent cognition in real information](agentrel05-bp03.html)

**Related documents:**

- [Amazon
Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html)
- [Amazon
Bedrock Data Automation](https://docs.aws.amazon.com/bedrock/latest/userguide/bda.html)
- [Amazon
Bedrock cross-region inference](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html)
- [Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html)
- [AWS fail-fast pattern](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/circuit-breaker.html)
- [Strands
Agents Agent Loop](https://strandsagents.com/docs/user-guide/concepts/agents/agent-loop/)

**Related videos:**

- [AWS re:Invent 2024 - Using Strands Agents to build autonomous,
self-improving AI agents (AIM426)](https://www.youtube.com/watch?v=RQfW7eQsXqk)

**Related examples:**

- [GitHub:
awslabs/amazon-bedrock-agentcore-samples - Runtime
tutorials](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/01-AgentCore-runtime)

**Related tools:**

- [Strands
Agents](https://strandsagents.com/)

**Related services:**

- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon
Bedrock](https://aws.amazon.com/bedrock/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentrel05-bp01.html*

---

# AGENTREL05-BP02 Facilitate reliable adaptation through evaluation-driven improvement cycles

Agents degrade quietly when no one is watching, and runtime
self-modification based on noisy feedback makes things worse.
Structured feedback collection with offline evaluation and validated
deployments keeps adaptation reliable because every change is
measured before it reaches users.

**Desired outcome:**

- You collect action-level, task-level, and session-level feedback
signals on every agent interaction.
- You run automated and LLM-as-a-judge evaluations periodically,
comparing current behavior against golden-path examples.
- You validate prompt and configuration changes offline before
deploying through gradual rollout.

**Common anti-patterns:**

- Deploying agents without feedback collection, missing the chance
to identify systematic errors.
- Applying automated behavioral changes at runtime without offline
validation, risking regression from noisy feedback.
- Skipping monitoring of the feedback loop itself, so silent
pipeline failures block adaptation from happening.

**Benefits of establishing this best
practice:**

- Task execution quality improves steadily through structured
feedback collection and validated adjustments.
- Systematic errors get identified and corrected faster because
automated analysis catches patterns humans miss.
- Manual intervention drops because evaluation-driven prompt
optimization with controlled rollout replaces manual tuning.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Feedback is only useful at the granularity you collect it. Three
tiers cover most of the signal. Action-level captures whether a
tool call succeeded, task-level captures whether the agent
completed the task correctly, and session-level captures whether
the interaction achieved the user's goal. Action-level feedback
tends to come from automated validators that compare outputs
against expected schemas. Task-level feedback can be automated for
deterministic success criteria and needs LLM-as-a-judge for
subjective quality dimensions. Session-level feedback usually
comes from users, either directly or through behavioral signals
like follow-up questions.

[Amazon
Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html) runs the periodic quality
assessments against representative task sets, comparing outputs
against golden-path examples and flagging regressions. Store
evaluation results alongside task records so the agent's
performance over time becomes a labeled dataset you can query.
When evaluations indicate systematic degradation, that is the
signal to trigger an offline prompt optimization workflow, test
alternative formulations against evaluation benchmarks and deploy
the highest-performing version through gradual rollout.

The discipline that keeps this reliable is validated before
deployed, not modified at runtime. Runtime self-modification is
tempting because it produces faster feedback, but noisy feedback
can push agents into worse behavior. The scope of impact of a bad
auto-update is the entire production fleet. Offline validation
with gradual rollout keeps improvements under control. Monitor
feedback loop health through
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html). Track collection rates,
processing latency, and evaluation frequency, with alarms when
pipeline failures block the improvement cycle from operating.

### Implementation steps

- **Implement multi-tier feedback
collection:** Capture action-level, task-level, and
session-level signals for every interaction.
- **Deploy automated outcome validators
for deterministic criteria:** Compare outputs
against expected schemas where the success criteria are
unambiguous.
- **Use AgentCore Evaluations with
LLM-as-a-judge for subjective quality:** Run
[Amazon
Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html) on a periodic schedule
against golden-path examples.
- **Trigger offline prompt optimization
when evaluations show degradation:** Validate
candidates against benchmarks offline, then deploy through
gradual rollout rather than runtime self-modification.
- **Monitor feedback loop
health:** Track collection rates, processing
latency, and evaluation frequency through
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) with alarms for
pipeline failures.

## Resources

**Related best practices:**

- [AGENTREL02-BP03
Implement behavioral anomaly detection and monitoring](agentrel02-bp03.html)
- [AGENTREL05-BP01 Design
modular, fault-tolerant agentic reasoning components](agentrel05-bp01.html)
- [AGENTREL05-BP03 Ground
agent cognition in real information](agentrel05-bp03.html)

**Related documents:**

- [Amazon
Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html)
- [Evaluate
models in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation-judge.html)
- [Build
reliable AI agents with Amazon Bedrock AgentCore
Evaluations](https://aws.amazon.com/blogs/machine-learning/build-reliable-ai-agents-with-amazon-bedrock-agentcore-evaluations/)
- [Evaluating
AI agents: Real-world lessons from building agentic systems at
Amazon](https://aws.amazon.com/blogs/machine-learning/evaluating-ai-agents-real-world-lessons-from-building-agentic-systems-at-amazon/)

**Related videos:**

- [AWS re:Invent 2024 - Using Strands Agents to build autonomous,
self-improving AI agents (AIM426)](https://www.youtube.com/watch?v=RQfW7eQsXqk)

**Related services:**

- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon
Bedrock](https://aws.amazon.com/bedrock/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentrel05-bp02.html*

---

# AGENTREL05-BP03 Ground agent cognition in real information

Training data has a cutoff and an agent reasoning only from model
knowledge can hallucinate about the present. Retrieval-augmented
generation grounds each answer in current, domain-specific
information and reduces hallucination rates as a byproduct.

**Desired outcome:**

- You have retrieval pipelines that ground agent reasoning in
current, domain-specific information.
- You validate knowledge freshness and flag content that exceeds
staleness thresholds.
- You handle retrieval failures gracefully, letting agents
continue with model knowledge while communicating the
uncertainty.

**Common anti-patterns:**

- Relying only on model training data for domain-specific
knowledge, producing outputs that may be outdated or inaccurate.
- Running retrieval without freshness validation, causing agents
to reason from stale data.
- Treating retrieval as a hard dependency, so retrieval failures
cascade into agent failures.

**Benefits of establishing this best
practice:**

- Hallucination rates drop because reasoning is grounded in
retrieved factual information.
- Factual accuracy improves through access to current,
domain-specific knowledge.
- Reliability holds as the operational environment evolves through
knowledge base updates.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

[Amazon
Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html) handles the mechanics of RAG,
document ingestion, chunking, embedding, and vector storage, so
most of the setup is configuration rather than infrastructure.
Configure data sources that reflect the agent's domain and set up
automated synchronization to keep content current. S3 event
notifications trigger sync operations when source documents are
updated, and the Knowledge Bases direct ingestion API handles
programmatic content. Chunking strategy matters. Smaller chunks
produce precise factual retrieval, while larger chunks produce
better contextual understanding. Reranking models re-score
retrieved passages for higher-quality context.

A knowledge base populated at launch and never refreshed becomes a
source of wrong answers over time. Track ingestion timestamps and
flag content that exceeds staleness thresholds before it is
served. For information that requires real-time accuracy (prices,
inventory, and system status), caches are not sufficient.
Implement tool functions that agents invoke to retrieve data from
authoritative sources through
[Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html), and treat the authoritative
source as the single source of truth.

[Amazon
Bedrock Data Automation](https://docs.aws.amazon.com/bedrock/latest/userguide/bda.html) extracts structured data from
documents, forms, and tables, so agents reason over extracted
content rather than raw images. Retrieved context quality
assessment filters low-relevance results and deduplicates
redundant passages before injection into prompts. Otherwise the
context window fills with noise that drowns out the signal. Handle
retrieval failures by allowing the agent to continue with model
knowledge while communicating uncertainty about information
currency. A transparent "I'm working from general knowledge
rather than current data" beats silent reliance on training
data.

### Implementation steps

- **Configure Amazon Bedrock Knowledge
Bases with automated synchronization:** Set up
[Amazon
Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html) with domain-appropriate data
sources and sync pipelines triggered by source changes.
- **Implement knowledge freshness
validation:** Track ingestion timestamps and flag
stale content before it is served.
- **Use Knowledge Bases
reranking:** Re-score retrieved passages for
higher-quality context injection.
- **Implement real-time data retrieval
tools through AgentCore Gateway:** Use
[Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) tool functions for
information that requires current accuracy.
- **Handle retrieval failures
gracefully:** Allow agents to continue with model
knowledge while communicating uncertainty about information
currency.

## Resources

**Related best practices:**

- [AGENTREL03-BP01
Design an information classification model to identify
short-term and long-term memories](agentrel03-bp01.html)
- [AGENTREL05-BP01 Design
modular, fault-tolerant agentic reasoning components](agentrel05-bp01.html)
- [AGENTREL05-BP02
Facilitate reliable adaptation through evaluation-driven
improvement cycles](agentrel05-bp02.html)

**Related documents:**

- [Amazon
Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html)
- [Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html)
- [Amazon
Bedrock Data Automation](https://docs.aws.amazon.com/bedrock/latest/userguide/bda.html)

**Related videos:**

- [AWS re:Invent 2024 - Advanced agentic RAG Systems: Deep dive with
Bedrock (AIM425)](https://www.youtube.com/watch?v=bu2cD1pCFTs)

**Related examples:**

- [GitHub:
awslabs/amazon-bedrock-agent-samples - Knowledge Base
integration](https://github.com/awslabs/amazon-bedrock-agent-samples/tree/main/examples/agents/agent_with_knowledge_base_integration)

**Related services:**

- [Amazon
Bedrock](https://aws.amazon.com/bedrock/)
- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentrel05-bp03.html*

---
