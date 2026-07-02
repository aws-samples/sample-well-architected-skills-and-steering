# AGENTSEC01 — Secure agent memory and state

**Pillar**: Security  
**Best Practices**: 3

---

# AGENTSEC01-BP01 Implement memory isolation and integrity controls

Shared agent memory is the shortest path for a single affected
session to contaminate every other one. Partitioning memory along
the boundaries that matter for the workload, and verifying what
comes back out, contains the scope of memory poisoning to the
partition it touched.

**Desired outcome:**

- You partition agent memory along the isolation axes that match
the workload (session, user, tenant, agent, or group), with no
cross-contamination between contexts.
- You detect unauthorized modifications to stored memories through
integrity checks and keep a tamper-evident history of state
changes.
- You scope memory access per agent through least-privilege IAM
policies, so each agent can read or write only the namespaces it
is authorized for.

**Common anti-patterns:**

- Sharing memory across agents or sessions by default, so an
affected session can read or overwrite another's context and
poisoning spreads laterally.
- Storing agent memory in plaintext without encryption at rest,
exposing reasoning context, intermediate tool results, and user
data if the underlying storage is reached through a
misconfigured IAM policy or storage exposure.
- Skipping integrity checks on memory reads, letting silently
corrupted or injected memories influence decisions and compound
across sessions.
- Granting every agent broad read/write access to the full memory
store, producing a flat trust model where any affected agent
reaches unrelated workflows.

**Benefits of establishing this best
practice:**

- Per-session and per-agent memory partitioning contains the scope
of any single affected agent.
- Cryptographic integrity verification on memory reads catches
poisoning attempts before affected data influences decisions.
- IAM-scoped memory access limits each agent to only the
partitions it requires, reducing lateral movement.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Memory poisoning is a lateral-movement problem. If every agent
reads from the same pool, one affected write becomes every agent's
input, and the cost of a single successful injection is the
correctness of the entire system. The design shift is to treat
memory like a tenant-aware data store from the start. Partition it
along the boundaries that actually matter for the workload:

- Session
- User
- Tenant
- Agent
- Group

Make cross-partition access the exception you must explicitly
grant, not the default you must explicitly prevent.

[Amazon
Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) expresses this partitioning
through a hierarchical namespace system built on
actorId and sessionId
identifiers, with dynamic placeholders like
{actorId} and {sessionId}
that resolve at call time. A namespace template like
/support-agent/{actorId}/preferences gives each
user an automatically scoped partition without hardcoding
identifiers. The invoking session determines which namespace the
agent reads from or writes to, and the IAM policy on the agent's
role bounds which namespace prefixes it can touch, so even a
namespace constructed incorrectly by the agent is denied by the
authorization layer.

Shared namespaces are not an anti-pattern when they are
intentional. A common product knowledge base read by every support
agent, a team-scoped working context, or a coordination memory
where cooperating agents exchange intermediate results are
legitimate shared partitions. Model them as named namespaces (for
example,
/support-agent/shared/product-knowledge or
/team-{teamId}/shared/working-context) and
scope each agent role's IAM policy to the specific shared
namespaces that agent is authorized to reach. The failure mode to
help prevent is sharing by default, not sharing that has been
designed and authorized.

Integrity is the other half of the pattern. AgentCore Memory keeps
an append-only audit trail where the consolidation process marks
outdated records as INVALID rather than
deleting them, so the full sequence of changes is recoverable for
forensic analysis. That helps protect history, but it doesn't
detect whether a specific record was silently modified outside the
normal consolidation flow. AWS KMS HMAC signatures layer tamper
detection on individual records: sign on write, recompute and
compare on read, and treat a mismatch as evidence the record was
altered. Pair that with customer-managed AWS KMS keys on the
memory resource itself (through the
encryptionKeyArn parameter) for sensitive
reasoning context, and the built-in memory strategies filter
personally identifiable information (PII) from long-term records
by default.

Monitoring completes the control. Route memory access events to
Amazon CloudWatch Logs, alarm on cross-namespace retrieval
attempts and high-frequency writes from a single agent, and run
red-team exercises that simulate memory poisoning to verify
isolation controls hold under pressure.

### Implementation steps

- **Create the memory resource with
customer-managed encryption:** Provision an
[Amazon
Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) resource, specify
encryptionKeyArn with a customer-managed
AWS KMS key for sensitive workloads, and set
eventExpiryDuration to match your data
retention requirements.
- **Design a hierarchical namespace
schema:** Use dynamic placeholders
({actorId},
{sessionId}) to partition memory per user
and per session automatically, for example
/support-agent/{actorId}/preferences for
user-scoped data and
/support-agent/shared/product-knowledge
for intentional shared context.
- **Configure memory strategies at the
correct isolation level:** Apply semantic, user
preferences, summary, or custom strategies with namespaces
scoped to the partition you want, and use custom strategy
overrides where domain-specific extraction and consolidation
prompts are needed.
- **Scope IAM roles to authorized
namespaces only:** Give each agent a dedicated IAM
role with resource-based policies that allow only the
namespace prefixes it requires, denying all other namespaces
by default.
- **Enforce namespace-scoped retrieval
in agent code:** Call
retrieve_memory_records and
list_events within the agent's authorized
namespaces only, so cross-tenant data is blocked at the
application layer as well as the authorization layer.
- **Layer HMAC integrity verification on
sensitive records:** For workloads that need tamper
detection beyond the built-in audit trail, store a
KMS-generated HMAC alongside each memory entry and verify it
on read before the content influences agent decisions.
- **Alarm on memory access
anomalies:** Configure Amazon CloudWatch alarms for
cross-namespace retrieval attempts, high-frequency writes
from a single agent, and spikes in memory extraction
failures, and route alerts through Amazon EventBridge for
automated incident response.
- **Audit strategies and run red-team
exercises:** Periodically review extraction and
consolidation patterns with list_memories
and retrieve_memory_records to verify
strategies are capturing the right information and that PII
filtering is working, and simulate memory poisoning
scenarios to validate the isolation controls hold.

## Resources

**Related best practices:**

- [AGENTSEC01-BP02 Validate
and sanitize memory inputs](agentsec01-bp02.html)
- [AGENTSEC01-BP03 Monitor
for hallucination propagation](agentsec01-bp03.html)
- [AGENTSEC03-BP03
Implement least privilege with dynamic boundaries](agentsec03-bp03.html)

**Related documents:**

- [Amazon
Bedrock AgentCore Memory documentation](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html)
- [Amazon
Bedrock AgentCore Memory: Building context-aware agents](https://aws.amazon.com/blogs/machine-learning/amazon-bedrock-agentcore-memory-building-context-aware-agents/)
- [Building
smarter AI agents: AgentCore long-term memory deep dive](https://aws.amazon.com/blogs/machine-learning/building-smarter-ai-agents-agentcore-long-term-memory-deep-dive/)
- [AWS IAM best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)

**Related services:**

- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [AWS Key Management Service](https://aws.amazon.com/kms/)
- [AWS Identity and Access Management](https://aws.amazon.com/iam/)
- [Amazon DynamoDB](https://aws.amazon.com/dynamodb/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsec01-bp01.html*

---

# AGENTSEC01-BP02 Validate and sanitize memory inputs

Unvalidated writes into agent memory let adversarial content persist
and influence every subsequent session that reads the same context.
Layered validation at ingestion keeps the memory store free of
injection payloads, policy-violating content, and context
inconsistent with the current task.

**Desired outcome:**

- You validate all data entering agent memory for type, format,
and content before storage, and reject or quarantine
policy-violating inputs before they influence agent behavior.
- You detect and block injection attempts at the memory ingestion
layer and route suspicious inputs to human review.
- Your memory store contains only schema-conformant, sanitized
data that downstream agents can consume safely.

**Common anti-patterns:**

- Storing raw, unvalidated user inputs directly into agent memory,
letting prompt injection payloads persist and influence future
sessions as agents build reasoning chains on top of affected
context.
- Validating only at the public API boundary while skipping
validation for content that enters memory from other write
paths, including tool outputs, inter-agent messages, and memory
consolidation.
- Failing to scan for encoded or obfuscated injection payloads,
missing base64-encoded instructions, Unicode homoglyph
substitutions, and other obfuscation that bypasses keyword-based
filters but is still interpreted by downstream models.

**Benefits of establishing this best
practice:**

- Multi-layer validation catches issues at syntactic, semantic,
and contextual levels before data reaches the memory store.
- Blocking adversarial content at the ingestion boundary helps
prevent it from influencing agent reasoning or propagating to
downstream agents.
- Validation metrics surface trends in rejection rates and issue
patterns, turning ingestion controls into operational signal.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Every write into agent memory is a trust decision. Raw user inputs
are the obvious write path, but they are not the only one. Tool
outputs arrive from search APIs, databases, and third-party
services the agent queries. Inter-agent messages carry content one
agent wrote into another's scope, and memory consolidation
generates long-term records by summarizing or merging existing
events. Each of these is a distinct ingestion path, and each needs
the same validation treatment. Validating only at the public API
boundary leaves the other three open.

A layered pipeline gives each category of issue somewhere to be
caught. Syntactic validation against a JSON Schema rejects wrong
types, over-long strings, and missing fields before anything
semantic happens. Semantic validation with
[Amazon
Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html) detects prompt injection attempts,
denied topics, and content that violates organizational guidelines
through the ApplyGuardrail API, which evaluates content
independently of model invocations so you can run it at any point
in the pipeline. Contextual validation checks whether an input is
consistent with the current task and flags anomalies for review.

[Amazon
Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) gives this pipeline a natural
integration point. Because long-term memory extraction runs
asynchronously from event ingestion, running Guardrails before
events are written through the create_event API
blocks harmful content from entering the extraction pipeline, and
running Guardrails again before consolidation catches anything
that made it past the first check. The built-in memory strategies
already filter PII from long-term records by default, but that
isn't a substitute for injection and policy enforcement, which
must be added on top.

The shared responsibility model matters here. AWS is responsible
for the AgentCore Memory infrastructure. You are responsible for
secure application development, input validation, and helping
prevent prompt injection in the memory extraction service. The
[AgentCore
Memory best practices](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/best-practices.html) specifically recommend sanitizing
user input with guardrails before persisting through
CreateEvent. If your memory writes originate
from HTTP APIs you already operate, AWS WAF in front of those APIs
adds a network-layer tier, and Amazon API Gateway request
validation enforces schema constraints at the same layer. For
writes that happen entirely in agent code through direct SDK
calls, validating in the agent code before
create_event is the simpler path.

Failed inputs need a tiered response. Clearly harmful inputs are
blocked and logged. Ambiguous inputs go to an Amazon SQS
quarantine queue for human review, stored with enough context
(agent ID, session ID, timestamp, and source) to support
investigation. All validation failures emit Amazon CloudWatch
metrics so rejection-rate trends become visible and configurable
into alarms when something changes.

### Implementation steps

- **Define JSON schemas for every memory
input type:** Specify field types, length limits,
allowed values, and required fields so the first validation
layer can reject malformed inputs deterministically.
- **Configure Guardrails for semantic
validation:** Configure
[Amazon
Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html) with denied topics, word filters,
and sensitive information filters tuned to your security
policies, and use the ApplyGuardrail API so validation is
independent of model invocations.
- **Validate every write path, not just
user input:** Apply Guardrails to tool outputs and
inter-agent messages as well as user-provided content before
any of them reach the memory store.
- **Validate before
create_event:** Run validation
on events before they enter
[Amazon
Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) short-term storage through
create_event, so harmful content doesn't
enter the asynchronous long-term extraction pipeline.
- **Add AWS WAF on API-fronted memory
writes:** Deploy AWS WAF managed rule groups on
Amazon API Gateway endpoints that accept memory inputs,
enforcing network-layer injection filtering before requests
reach application code.
- **Quarantine ambiguous inputs for
review:** Route failures into an Amazon SQS queue
with agent ID, session ID, timestamp, and source, so humans
can review without blocking the pipeline.
- **Emit validation
telemetry:** Publish Amazon CloudWatch metrics for
every validation outcome (pass, block, or quarantine) and
alarm on elevated rejection rates that suggest an active
issue.
- **Review quarantined inputs
regularly:** Use the quarantine queue to identify
new attack patterns, update Guardrail configurations, and
refine validation rules over time.
- **Test for injection
continually:** Apply penetration testing, static
code analysis, and dynamic application security testing
(DAST) to the memory write paths as part of regular security
validation.
- **Enforce IAM conditions on
CreateEvent:** Use IAM Access Analyzer to validate that memory resource policies follow
least privilege, and add policy conditions that restrict
which roles can call the CreateEvent API
for specific AgentCore Memory resources.

## Resources

**Related best practices:**

- [AGENTSEC01-BP01
Implement memory isolation and integrity controls](agentsec01-bp01.html)
- [AGENTSEC01-BP03 Monitor
for hallucination propagation](agentsec01-bp03.html)
- [AGENTSEC08-BP01
Multi-layer input validation and prompt injection
defense](agentsec08-bp01.html)

**Related documents:**

- [Amazon
Bedrock Guardrails documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html)
- [Amazon
Bedrock AgentCore Memory best practices](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/best-practices.html)
- [Amazon
Bedrock AgentCore Memory: Building context-aware agents](https://aws.amazon.com/blogs/machine-learning/amazon-bedrock-agentcore-memory-building-context-aware-agents/)
- [AWS WAF developer guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html)

**Related services:**

- [Amazon
Bedrock Guardrails](https://aws.amazon.com/bedrock/guardrails/)
- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [AWS WAF](https://aws.amazon.com/waf/)
- [Amazon SQS](https://aws.amazon.com/sqs/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
- [Amazon API Gateway](https://aws.amazon.com/api-gateway/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsec01-bp02.html*

---

# AGENTSEC01-BP03 Monitor for hallucination propagation

A single hallucinated fact stored as memory becomes ground truth for
every agent that reads it next. Continuous grounding checks and
confidence scoring keep fabricated content from entering memory or
cascading across a multi-agent workflow.

**Desired outcome:**

- You detect false information before it propagates through agent
memory or cascades across multi-agent workflows.
- You use confidence scoring to surface low-certainty outputs for
validation, and fact-checking to help prevent hallucinated data
from being stored as ground truth.
- When hallucination propagation is detected, affected memory
entries are flagged or quarantined, and downstream agents are
notified to discard potentially corrupted context.

**Common anti-patterns:**

- Storing model outputs directly into memory without a confidence
threshold or grounding check, letting hallucinated facts persist
and influence future decisions.
- Relying on the generating model to self-report uncertainty,
which produces confident-sounding assessments even for
fabricated content.
- Failing to propagate hallucination flags to downstream agents
that consume shared memory, so corrupted context silently
spreads through the workflow and each agent amplifies the error.
- Not logging hallucination detection events, reducing the risk of
measurement of frequency or impact and blocking teams from
tuning detection thresholds or identifying systemic patterns.

**Benefits of establishing this best
practice:**

- Early detection catches hallucinated outputs before they
propagate to downstream agents and compound into systemic
errors.
- Confidence scoring gives a quantitative basis for deciding
whether outputs are safe to store and act on.
- Ongoing monitoring surfaces new hallucination patterns for
threshold tuning and rule refinement over time.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Hallucinations compound. A fabricated fact stored during one
session is retrieved as context in the next, and the second agent,
reasoning on that input, produces a second output that looks
self-consistent with a false premise. In multi-agent systems the
problem is worse because each downstream consumer treats shared
memory as ground truth. The design response is to catch
fabrications at the point they are about to enter memory, flag
them with evidence, and propagate that flag to anything that
already read the affected context.

[Amazon
Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html) contextual grounding is the first layer.
It scores each model output against a provided reference context
and rejects or flags anything below the threshold. Safety-critical
applications run with higher thresholds, and creative tasks can
run with lower ones. Pair contextual grounding with an
LLM-as-a-Judge pattern for complex reasoning chains: route outputs
through a secondary model invocation that receives the original
context, the agent's output, and a structured evaluation prompt,
and returns a confidence assessment. Keyword matching alone isn't
sufficient at this layer. The judge catches contradictions and
unsupported claims that simple filters miss.

[Amazon
Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) gives the check a natural home.
The long-term memory consolidation process retrieves semantically
similar existing memories and uses an LLM to decide whether to
add, update, or skip new information, and outdated memories are
marked as INVALID rather than deleted. That
produces an immutable trail you can walk to trace how hallucinated
content entered and propagated. Running grounding checks before
create_event helps keep fabrications out of the
extraction pipeline, and custom memory strategy overrides let you
bake grounding validation into the extraction and consolidation
prompts for your domain.

Detection without traceability is expensive. Enable Amazon Bedrock
model invocation logging and build Amazon CloudWatch Logs Insights
queries that look for hallucination indicators (references to
non-existent resources, contradictory statements within a single
response, outputs that deviate significantly from input context).
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) provides a session, trace,
and span hierarchy that lets you correlate a session-level anomaly
back to the specific span where the hallucinated content
originated. AgentCore emits default span data for memory
resources, viewable in Amazon CloudWatch Logs and Amazon CloudWatch Application Signals, and session-level metrics are
available on the CloudWatch generative AI observability page. For
deeper visibility, instrument agent code with AWS Distro for
OpenTelemetry (ADOT) to capture custom metrics for grounding
scores, confidence thresholds, and validation outcomes at each
step.

The circuit breaker keeps a single hallucination from cascading.
When detection fires in one agent, flag every memory entry that
agent wrote during the current session for re-validation before
downstream agents consume it, and broadcast the detection event
through Amazon EventBridge so every agent in the workflow can
discard potentially corrupted context. Tag memory entries with
confidence scores and grounding results so the evidence basis for
every decision is auditable.

### Implementation steps

- **Configure contextual grounding
thresholds per use case:** Set
[Amazon
Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html) contextual grounding thresholds
that match each agent's risk profile, with higher thresholds
for safety-critical applications and lower ones for creative
tasks.
- **Add an LLM-as-a-Judge step for
high-stakes outputs:** Route outputs through a
secondary model invocation that evaluates factual
consistency against the original context before the output
is committed to memory.
- **Run grounding checks before
create_event:** Apply grounding
validation at the
[Amazon
Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) event ingestion boundary, so
hallucinated content is filtered before reaching the
long-term extraction and consolidation pipeline.
- **Use custom memory strategy overrides
for domain-specific grounding:** Incorporate
grounding validation logic into the extraction and
consolidation prompts through custom strategy overrides
where your domain has specific factuality requirements.
- **Enable Amazon Bedrock model
invocation logging:** Turn on Amazon Bedrock model
invocation logging and create Amazon CloudWatch Logs
Insights queries that detect references to non-existent
resources, contradictory statements, and significant
deviations from input context.
- **Alarm on output-consistency
anomalies:** Configure Amazon CloudWatch anomaly
detection on output-consistency metrics to baseline normal
patterns and alert on deviations that suggest systematic
hallucination.
- **Instrument with ADOT and AgentCore
Observability:** Use AWS Distro for OpenTelemetry
to capture custom spans for grounding scores and validation
outcomes, and use the session/trace/span hierarchy in
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) to correlate
detections back to the originating interaction.
- **Wire a circuit breaker for
propagation:** When a hallucination fires, flag
every memory entry from the current session and broadcast
the detection event through Amazon EventBridge so downstream
agents can discard potentially corrupted context.
- **Tag memory entries with
evidence:** Store confidence scores and grounding
check results alongside each memory entry to produce an
auditable record of the evidence basis for agent decisions.
- **Review detection logs
periodically:** Tune thresholds, update detection
rules, and identify systemic patterns by reviewing
hallucination detection logs on a regular cadence.

## Resources

**Related best practices:**

- [AGENTSEC01-BP01
Implement memory isolation and integrity controls](agentsec01-bp01.html)
- [AGENTSEC01-BP02 Validate
and sanitize memory inputs](agentsec01-bp02.html)
- [AGENTSEC05-BP01
Implement comprehensive logging and decision artifact
storage](agentsec05-bp01.html)
- [AGENTREL05-BP03
Ground agent cognition in real information](agentrel05-bp03.html)

**Related documents:**

- [Amazon
Bedrock Guardrails contextual grounding](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-grounding.html)
- [Amazon
Bedrock model invocation logging](https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html)
- [AgentCore
Observability: Sessions, traces, and spans](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-telemetry.html)
- [Amazon
Bedrock AgentCore Memory best practices](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/best-practices.html)
- [Building
smarter AI agents: AgentCore long-term memory deep dive](https://aws.amazon.com/blogs/machine-learning/building-smarter-ai-agents-agentcore-long-term-memory-deep-dive/)

**Related services:**

- [Amazon
Bedrock Guardrails](https://aws.amazon.com/bedrock/guardrails/)
- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
- [Amazon EventBridge](https://aws.amazon.com/eventbridge/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsec01-bp03.html*

---
