# Security

**Pillar**: Security  
**Questions**: 9

---

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

# AGENTSEC02 — Secure agent tool usage

**Pillar**: Security  
**Best Practices**: 3

---

# AGENTSEC02-BP01 Implement tool authorization

An agent with unconstrained tool access has no meaningful privilege
boundary. Externally enforced authorization at the gateway, combined
with identity propagation and human review for mutating operations,
enforces bounded autonomy at the tool layer.

**Desired outcome:**

- You authorize every tool invocation against a defined policy
before execution, with agent identity and user context
propagated through the authorization chain.
- Agents can invoke only the tools within their approved scope,
and attempts to access unauthorized tools are blocked and
logged.
- Human-in-the-loop checkpoints intercept high-risk mutating
operations so consequential actions receive review before
execution.

**Common anti-patterns:**

- Granting agents blanket access to every available tool rather
than scoping access to the tools each agent requires.
- Relying on the agent's own judgment to decide whether a tool
invocation is appropriate, with no independent check at the tool
or API layer.
- Failing to propagate user identity context through tool
invocations, so downstream services can't enforce user-level
access controls and every call runs with the agent's
permissions.
- Skipping human-in-the-loop controls for mutating operations
because they add latency, accepting unbounded risk for actions
that are difficult or impossible to reverse.

**Benefits of establishing this best
practice:**

- RBAC policies scope each agent to the tools its defined tasks
require, implementing least-privilege tool access.
- Identity propagation lets downstream services enforce user-level
access controls on resources reached through agent tool calls.
- Rate limiting and human-in-the-loop controls constrain
autonomous execution to operations with acceptable risk
profiles.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Authorization implemented only through prompt instructions is
insufficient because prompts can be manipulated through
adversarial phrasing or prompt injection. Implement authorization
as an external, deterministic check that happens before the tool
executes, regardless of how the agent arrived at the call.
[Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock/latest/userguide/agentcore-gateway.html) is the enforcement point, and
[Policy
in Amazon Bedrock AgentCore](https://aws.amazon.com/blogs/machine-learning/secure-ai-agents-with-policy-in-amazon-bedrock-agentcore/) is the rules engine.

Gateway runs a dual-sided security model. On the inbound side, it
follows the MCP authorization specification and acts as an OAuth
resource server, working with Amazon Cognito, Okta, Auth0, or your
own OAuth provider. You configure approved client IDs and
audiences to control which applications and agents can reach your
tools, and Gateway supports both authorization code flow (3LO) and
client credentials flow (2LO) for service-to-service
communication. On the outbound side, the authentication model
depends on target type: AWS Lambda and Smithy model targets use
IAM-based authorization through a role you configure with scoped
permissions, and OpenAPI targets support API key or OAuth 2LO
client credentials grant.
[Amazon
Bedrock AgentCore Identity](https://docs.aws.amazon.com/bedrock/latest/userguide/agentcore-identity.html) resource credentials providers
handle token caching and secure storage, and each target is
associated with exactly one authentication configuration for clear
boundaries and auditability.

Policy is where fine-grained authorization lives. Cedar policies
evaluate every agent-to-tool request at the gateway before
execution, with a default-deny posture where forbid always wins
over permit. Conditions can reference OAuth claims from the JWT
token (user role, scopes, tenant-level identifiers like patient
ID), tool input parameters, and runtime context such as time of
day. That lets you express rules like "role=clinician can
reschedule appointments for patients in their own panel" as
a deterministic policy rather than a hope about the prompt.
Policies can be authored directly in Cedar or generated from
natural language, and Gateway supports a LOG_ONLY mode so you can
validate policy behavior against live traffic before switching to
enforce mode.

Tool overload is its own risk. Presenting an agent with hundreds
of tools increases the chance it selects the wrong one or follows
an inefficient execution path. Gateway's built-in
x_amz_bedrock_agentcore_search tool exposes
semantic tool discovery so agents locate relevant tools through
natural language rather than seeing the full inventory. That
reduces the surface the model reasons across on any given turn.

For tools that perform mutating operations (writes to databases,
outbound emails, financial transactions), human-in-the-loop review
belongs in the execution path, not the prompt. AWS Step Functions
callback patterns let an agent pause and wait for approval. The
workflow sends an approval request through Amazon SNS or Amazon SES and resumes only after a human responds within a defined
timeout. Configure escalation paths for timeouts so a non-response
doesn't silently block a legitimate action. Rate limiting at both
the Gateway and tool API levels helps prevent resource exhaustion:
Amazon API Gateway usage plans and throttling enforce per-agent
rate limits, and AWS Lambda reserved concurrency caps the maximum
parallel tool invocations. Gateway publishes usage, invocation,
performance, and error metrics to Amazon CloudWatch and integrates
with AWS CloudTrail for a full audit trail, so runaway loops and
unexpected call patterns surface as signal.

### Implementation steps

- **Configure Gateway inbound
OAuth:** Create an
[Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock/latest/userguide/agentcore-gateway.html) and wire inbound OAuth
authorization to your identity provider (Amazon Cognito,
Okta, Auth0, or your own OAuth provider), specifying
approved client IDs and audiences.
- **Add targets with scoped outbound
credentials:** Register tool APIs as gateway
targets, configuring IAM roles for Lambda and Smithy targets
and API key or OAuth 2LO for OpenAPI targets, and manage
outbound credentials through
[Amazon
Bedrock AgentCore Identity](https://docs.aws.amazon.com/bedrock/latest/userguide/agentcore-identity.html) resource credentials
providers.
- **Author Cedar policies for
authorization:** Create a policy engine in
[Policy
in Amazon Bedrock AgentCore](https://aws.amazon.com/blogs/machine-learning/secure-ai-agents-with-policy-in-amazon-bedrock-agentcore/) and define Cedar policies
with identity-aware conditions on OAuth claims (user role,
scopes, user ID) and tool input parameters. Author directly
in Cedar or generate policies from natural language
descriptions.
- **Validate policies in LOG_ONLY before
enforcing:** Associate the policy engine with
Gateway in LOG_ONLY mode, review observability logs to
confirm the policies produce the expected permit and deny
decisions, then switch to enforce mode.
- **Enable semantic tool
discovery:** Opt in to the built-in
x_amz_bedrock_agentcore_search tool so
agents locate relevant tools through natural language
queries rather than reasoning over the full inventory.
- **Add human-in-the-loop approvals for
mutating tools:** Wire AWS Step Functions callback
patterns for high-risk tools, send approval requests through
Amazon SNS or Amazon SES, and configure escalation paths for
reviewer timeouts.
- **Cap concurrency and request
rates:** Enforce per-agent rate limits through
Amazon API Gateway usage plans and cap parallel invocations
with AWS Lambda reserved concurrency to help prevent
resource exhaustion.
- **Monitor authorization
decisions:** Use Gateway's Amazon CloudWatch
metrics and AWS CloudTrail integration to track tool
invocations, authorization failures, and rate-limit events,
and configure alarms for authorization-failure spikes.
- **Review tool authorization
quarterly:** Remove unused permissions and tighten
access boundaries on a regular cadence as workloads and
tools evolve.

## Resources

**Related best practices:**

- [AGENTSEC02-BP02 Validate
tool inputs and outputs](agentsec02-bp02.html)
- [AGENTSEC02-BP03 Maintain
approved tool registry with security assessments](agentsec02-bp03.html)
- [AGENTSEC03-BP03
Implement least privilege with dynamic boundaries](agentsec03-bp03.html)
- [AGENTREL02-BP02
Limit agent permissions to minimum required access](agentrel02-bp02.html)
- [AGENTCOST04-BP01
Design cost effective tool selection to minimize unnecessary
invocations](agentcost04-bp01.html)

**Related documents:**

- [Amazon
Bedrock AgentCore Gateway documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/agentcore-gateway.html)
- [Introducing
Amazon Bedrock AgentCore Gateway: Transforming enterprise AI
agent tool development](https://aws.amazon.com/blogs/machine-learning/introducing-amazon-bedrock-agentcore-gateway-transforming-enterprise-ai-agent-tool-development/)
- [Apply
fine-grained access control with Bedrock AgentCore Gateway
interceptors](https://aws.amazon.com/blogs/machine-learning/apply-fine-grained-access-control-with-bedrock-agentcore-gateway-interceptors/)
- [Secure
AI agents with Policy in Amazon Bedrock AgentCore](https://aws.amazon.com/blogs/machine-learning/secure-ai-agents-with-policy-in-amazon-bedrock-agentcore/)
- [Amazon
Bedrock AgentCore Identity documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/agentcore-identity.html)

**Related examples:**

- [Healthcare
appointment agent with Policy enforcement (GitHub)](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/02-use-cases/healthcare-appointment-agent)

**Related services:**

- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [AWS Step Functions](https://aws.amazon.com/step-functions/)
- [Amazon API Gateway](https://aws.amazon.com/api-gateway/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
- [AWS CloudTrail](https://aws.amazon.com/cloudtrail/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsec02-bp01.html*

---

# AGENTSEC02-BP02 Validate tool inputs and outputs

Agents generate tool parameters from model output, which means
malformed or adversarial inputs can reach tools through ordinary
reasoning, not just through unauthorized callers. Schema-driven
validation on inputs and sanitization on outputs keep tools
operating inside their intended parameter space and help prevent
error messages from disclosing internal system details.

**Desired outcome:**

- You validate every parameter passed to tools against a defined
schema before execution, and sanitize tool outputs before
returning them to the agent.
- Injection through tool parameters is blocked, oversized inputs
are prevented from exhausting resources, and error messages are
sanitized to avoid leaking sensitive system information.
- Tool invocations operate predictably within defined boundaries,
and validation failures are logged for security analysis.

**Common anti-patterns:**

- Passing raw agent-generated parameters directly to tools without
type checking or range validation, letting malformed inputs
cause unexpected behavior or injection.
- Returning raw tool error messages to the agent without
sanitization, exposing internal system details, stack traces, or
infrastructure information usable for further probing.
- Validating only user-provided inputs and skipping validation for
parameters produced by the agent's reasoning, on the assumption
the model can't generate malformed output.

**Benefits of establishing this best
practice:**

- Schema-enforced input validation helps prevent tools from
operating outside their intended parameter space.
- Sanitized error responses return failure categories without
exposing internal system details.
- Timeout controls, memory limits, and output-size enforcement
help prevent resource exhaustion from oversized or long-running
tool invocations.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Validation is more useful when it happens at several layers than
when any single layer tries to do all the work. The cheapest and
most specific layer is at the model itself. Amazon Bedrock
structured outputs with strict tool use constrain the model's
decoding so that generated tool parameters always conform to the
defined input schema. Setting strict: true on
the tool definition, together with
additionalProperties: false and
enum constraints on fields with a closed set of
values, helps prevent malformed parameters as a class before they
ever reach the tool. That doesn't replace application validation,
but it removes a large chunk of the work from it. The
[Structured
outputs on Amazon Bedrock blog](https://aws.amazon.com/blogs/machine-learning/structured-outputs-on-amazon-bedrock-schema-compliant-ai-responses/) covers the parameter shapes
and the model-level enforcement.

The next layer is schema validation in the tool invocation
pipeline. For tools deployed as AWS Lambda functions, a JSON
Schema check inside the Lambda handler, or a shared Lambda Layer,
enforces type constraints, value ranges, string length limits, and
format patterns before the function logic runs. This is the place
to catch the edge cases strict tool use doesn't cover, anything
involving relationships between fields, external-state
constraints, or values the model can't know.

Policy in Amazon Bedrock AgentCore provides a third layer at the
gateway. Cedar policies can evaluate conditions on tool input
parameters through context.input, so business
rules like "financial amount below an approved
threshold" or "date parameter within an acceptable
range" are enforced deterministically at the gateway before
the call reaches the backend. The value of this layer is that the
rules are auditable and managed independently of tool code. The
value of keeping it separate from the first two layers is that
changes to business rules don't require redeploying tools.

Logical constraints that are not expressible as schema or simple
comparisons need a different mechanism.
[Amazon
Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html) Automated Reasoning checks verify that
tool parameters conform to logical constraints, a date range with
start before end, a set of values that must be mutually
consistent. Apply Guardrails at the AWS Organization level where
consistent policy enforcement is required across all agent
deployments.

Resource protection and error sanitization complete the picture.
AWS Lambda function timeout and memory limits, sized to each
tool's measured execution profile, bound what any single call can
consume, and Lambda reserved concurrency caps total parallel
invocations. Tool outputs that return large datasets need size
limits and pagination. Truncation events belong in the log so an
agent doesn't silently reason on a partial response. Error
handling catches exceptions and returns structured responses that
describe the failure category without exposing internal details,
stack traces, or infrastructure information. AWS WAF managed rule
groups on API-based tool endpoints add a network-layer filter for
common injection patterns before requests reach tool code.

### Implementation steps

- **Constrain parameters at the model
layer:** Enable strict tool use
(strict: true) on tool definitions in
Amazon Bedrock, set
additionalProperties: false on all input
schemas, and define enum constraints for
fields with a limited set of valid values to block malformed
parameters at decoding.
- **Enforce schemas in the invocation
pipeline:** Define JSON Schema specifications for
every tool and validate parameters as a middleware layer
inside the Lambda handler or a shared Lambda Layer before
the tool function runs.
- **Add Cedar policy checks at the
gateway:** Define policies in AgentCore Policy with
conditions on context.input to enforce
business rules and parameter constraints deterministically,
complementing application-level schema validation.
- **Use Automated Reasoning for logical
constraints:** Configure
[Amazon
Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html) Automated Reasoning policies for
tool inputs and outputs that require logical constraint
validation beyond schema and Cedar rules.
- **Right-size Lambda limits per
tool:** Set AWS Lambda timeout and memory limits
based on measured execution profiles, with conservative
limits that help prevent resource exhaustion, and use
reserved concurrency to cap parallel invocations.
- **Sanitize errors:**
Implement structured error handling in every tool that
returns sanitized responses without internal system details,
stack traces, or infrastructure information.
- **Paginate and truncate large
outputs:** Apply output size limits for tools that
may return large datasets, truncate responses before
returning them to the agent, and log every truncation event.
- **Add AWS WAF in front of API-based
tools:** Deploy AWS WAF with managed rule groups on
API-based tool endpoints to filter common injection patterns
at the network layer.
- **Alarm on validation-failure
rates:** Publish Amazon CloudWatch metrics for
validation outcomes and configure alarms for elevated
failure rates that suggest active injection attempts or
misconfigured parameters.

## Resources

**Related best practices:**

- [AGENTSEC02-BP01
Implement tool authorization](agentsec02-bp01.html)
- [AGENTSEC02-BP03 Maintain
approved tool registry with security assessments](agentsec02-bp03.html)
- [AGENTSEC08-BP01
Multi-layer input validation and prompt injection
defense](agentsec08-bp01.html)

**Related documents:**

- [Amazon
Bedrock Guardrails automated reasoning checks](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-automated-reasoning.html)
- [Structured
outputs on Amazon Bedrock: Schema-compliant AI
responses](https://aws.amazon.com/blogs/machine-learning/structured-outputs-on-amazon-bedrock-schema-compliant-ai-responses/)
- [Secure
AI agents with Policy in Amazon Bedrock AgentCore](https://aws.amazon.com/blogs/machine-learning/secure-ai-agents-with-policy-in-amazon-bedrock-agentcore/)
- [AWS Lambda best practices](https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html)

**Related services:**

- [Amazon
Bedrock Guardrails](https://aws.amazon.com/bedrock/guardrails/)
- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [AWS Lambda](https://aws.amazon.com/lambda/)
- [AWS WAF](https://aws.amazon.com/waf/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
- [Amazon API Gateway](https://aws.amazon.com/api-gateway/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsec02-bp02.html*

---

# AGENTSEC02-BP03 Maintain approved tool registry with security assessments

Every tool an agent can reach is part of its effective privilege
surface. A version-controlled registry with documented security
boundaries, enforced at invocation time, keeps unvetted or
deprecated tools off the agent's call path.

**Desired outcome:**

- You maintain a centralized, version-controlled registry of
approved tools, each with documented security boundaries,
required permissions, data classification levels, and a current
vulnerability assessment.
- Agents can access only tools present in the registry, and
unapproved tools are blocked by default.
- You continually validate the registry for compliance, and
deprecated tools are removed from agent access automatically.

**Common anti-patterns:**

- Allowing agents to discover and invoke any available tool or MCP
server without prior security review and registry approval.
- Maintaining the tool registry as a static document rather than
an enforced control, so agents can bypass it and invoke
unapproved tools directly.
- Failing to distinguish between locally hosted tools and remote
MCP servers in the risk assessment, underestimating the expanded
scope from external network connectivity.
- Skipping version pinning for approved tools, so agents pick up
new versions that have not undergone security review.

**Benefits of establishing this best
practice:**

- A deny-by-default posture constrains agent capabilities to a
pre-approved, security-reviewed set of tools and operations.
- Version control helps prevent agents from using tool versions
that have not been reviewed and provides an audit trail of which
versions were approved and when.
- Automated compliance checks detect drift from the approved
registry and trigger remediation workflows.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

A tool registry must be enforced at runtime to be effective.
Document approved tools in a registry and configure the invocation
path to refuse tools that are not on the list. The design pattern
is a registry that agents can't bypass: tools reachable only
through a gateway target, agents authorized only through a policy
engine with default-deny semantics, and an out-of-band compliance
process that detects drift between the registry and what is
actually configured.

[Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock/latest/userguide/agentcore-gateway.html) provides the consolidation point
for agent-to-tool traffic. Each gateway target represents a
backend service or group of APIs exposed as tools to agents, with
defined tool schemas, authentication configurations, and access
controls. Gateway alone isn't deny-by-default, however: adding a
target makes it immediately accessible as an MCP tool to any agent
that reaches the gateway endpoint. To restrict which agents can
invoke which tools, layer
[Policy
in Amazon Bedrock AgentCore](https://aws.amazon.com/blogs/machine-learning/secure-ai-agents-with-policy-in-amazon-bedrock-agentcore/) Cedar policies with a
default-deny posture, Gateway Interceptor for custom Lambda-based
access logic, or both. The policy layer is what turns a populated
registry into enforced authorization.

Development environments need a second control. When developers
and agents interact with MCP servers through IDE-based tools, an
MCP registry, a JSON allowlist of approved servers hosted on an
HTTPS endpoint such as Amazon S3 or an internal web server, gives
clients a list of servers to fetch at startup and re-sync
periodically (typically every 24 hours). Servers not in the
registry are blocked, and if a locally installed server is removed
from the registry, the client terminates it and helps prevent it
from being re-added. The registry supports version pinning so that
a new version automatically relaunches clients with the updated
version, and the file format follows the
[MCP
Registry open standard](https://github.com/modelcontextprotocol/registry) so the investment isn't tied to a
single tool or provider. MCP registry governance can be configured
at the organization level with account-level overrides, for
example disabling MCP for the organization by default but enabling
it with a specific allowlist for certain teams.

At enterprise scale, a centralized MCP server hub consolidates
what would otherwise become a proliferation of team-specific
connections. Teams develop MCP servers for their specific
functions, but servers are hosted centrally and accessible across
the organization through a shared registry or discovery API backed
by Amazon DynamoDB that catalogs available servers with their
descriptions, tool definitions, and access requirements.
Network-level access uses AWS PrivateLink and VPC endpoints so
agents connect only to trusted organization-hosted servers, and
each server runs as an isolated container on Amazon ECS with AWS Fargate for independent scaling without impact on other servers.

Remote MCP servers need a heightened security review. They
introduce network connectivity to external services, expanding
scope beyond the organization's direct control. Assess
authentication mechanisms, data handling practices, and network
exposure, and apply network controls such as VPC endpoints and
security groups to restrict connectivity to the required
endpoints. When onboarding tools to Gateway or the MCP registry,
scan API specifications for security risks, validate
authentication, assess data handling, enrich tool metadata with
descriptions, usage examples, and performance characteristics, and
group APIs into gateway targets by business domain, outbound
authorization requirements, and API type.

Gateway supports six target types:

- Lambda functions
- API Gateway REST APIs
- OpenAPI schemas
- Smithy models
- External MCP servers
- Built-in templates from integration providers

Built-in templates provide pre-configured, curated integrations
for popular SaaS platforms including Salesforce, Slack, Jira,
Asana, Zendesk, and ServiceNow, with a vetted subset of provider
APIs exposed through the gateway. Routing all tool access through
Gateway (internal services, external MCP servers, and native SaaS
integrations) consolidates authentication, schema enforcement, and
policy evaluation under one endpoint. IDEs such as Kiro, Claude
Code, and Cursor connect through the Amazon Bedrock AgentCore MCP
Server, which bridges IDE-based MCP clients to the gateway
endpoint.

Continuous compliance detection keeps the registry enforceable
over time. Maintain a configuration store in Parameter Store, a
capability of AWS Systems Manager or AWS AppConfig alongside the
gateway configuration, with entries for tool name, approved
version, required IAM permissions, data classification level,
security review date, and expiration date. Use AWS Config rules to
validate that agent deployments reference only registry-approved
tools, and trigger Amazon EventBridge notifications for
non-compliance. Automated deprecation workflows remove expired
tools from the registry, update agent configurations, and help
prevent continued use.

### Implementation steps

- **Build the structured
registry:** Create a tool registry in Parameter
Store, a capability of AWS Systems Manager or AWS AppConfig
with entries for each approved tool covering version,
permissions, data classification, and review metadata.
- **Add approved tools as Gateway
targets:** For agent-to-tool traffic, register
approved tools as
[Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock/latest/userguide/agentcore-gateway.html) targets with defined tool
schemas, outbound authentication configurations, and access
controls. Group targets by business domain, authorization
requirements, and API type.
- **Publish an MCP registry for
development:** Create an MCP registry JSON file
that follows the
[MCP
Registry open standard](https://github.com/modelcontextprotocol/registry), host it on an HTTPS endpoint,
and configure it in your organization's admin settings with
version pinning for each server entry.
- **Define the security review
process:** Establish a review covering API
specification scanning, permission assessment, data flow
mapping, and authentication mechanism validation, with
findings documented in the registry entry and a review
expiration date.
- **Build a centralized hub at
enterprise scale:** For multi-LOB deployments,
implement a centralized MCP server hub with an Amazon DynamoDB-backed discovery API, network-level access through
AWS PrivateLink and VPC endpoints, and isolated container
hosting on Amazon ECS with AWS Fargate.
- **Enforce default-deny through
Policy:** Configure Cedar policies in AgentCore
Policy so only explicitly permitted tools can be invoked,
providing a second enforcement layer beyond Gateway target
configuration.
- **Apply heightened review to remote
MCP servers:** Assess network exposure and external
authentication, and apply VPC endpoints and security groups
to restrict connectivity.
- **Detect registry drift
continually:** Deploy AWS Config rules to detect
agent configurations referencing unapproved tools, and
trigger Amazon EventBridge notifications for remediation.
- **Automate deprecation:**
Expire tools past their review date, remove them from
Gateway targets and the MCP registry, and update agent
configurations to help prevent continued use.

## Resources

**Related best practices:**

- [AGENTSEC02-BP01
Implement tool authorization](agentsec02-bp01.html)
- [AGENTSEC02-BP02 Validate
tool inputs and outputs](agentsec02-bp02.html)
- [AGENTSEC03-BP03
Implement least privilege with dynamic boundaries](agentsec03-bp03.html)

**Related documents:**

- [Amazon
Bedrock AgentCore Gateway documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/agentcore-gateway.html)
- [Introducing
Amazon Bedrock AgentCore Gateway: Transforming enterprise AI
agent tool development](https://aws.amazon.com/blogs/machine-learning/introducing-amazon-bedrock-agentcore-gateway-transforming-enterprise-ai-agent-tool-development/)
- [Transform
your MCP architecture: Unite MCP servers through AgentCore
Gateway](https://aws.amazon.com/blogs/machine-learning/transform-your-mcp-architecture-unite-mcp-servers-through-agentcore-gateway/)
- [Enterprise
governance: control your MCP servers and models](https://kiro.dev/blog/enterprise-governance-mcp-and-models/)
- [MCP
governance for Q Developer](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/mcp-governance.html)
- [Accelerating
AI innovation: Scale MCP servers for enterprise workloads with
Amazon Bedrock](https://aws.amazon.com/blogs/machine-learning/accelerating-ai-innovation-scale-mcp-servers-for-enterprise-workloads-with-amazon-bedrock/)
- [Secure
AI agents with Policy in Amazon Bedrock AgentCore](https://aws.amazon.com/blogs/machine-learning/secure-ai-agents-with-policy-in-amazon-bedrock-agentcore/)
- [Parameter
Store, a capability of AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html)

**Related examples:**

- [Accelerating
AI Innovation: Scaling Model Context Protocol Servers for
Enterprise Workloads on AWS (GitHub)](https://github.com/aws-samples/sample-deploy-mcp-servers-at-scale-on-aws)

**Related services:**

- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [AWS Systems Manager](https://aws.amazon.com/systems-manager/)
- [AWS Config](https://aws.amazon.com/config/)
- [Amazon EventBridge](https://aws.amazon.com/eventbridge/)
- [AWS AppConfig](https://aws.amazon.com/systems-manager/features/appconfig/)
- [Amazon ECS](https://aws.amazon.com/ecs/)
- [Amazon DynamoDB](https://aws.amazon.com/dynamodb/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsec02-bp03.html*

---

# AGENTSEC03 — Agent identity and permission management

**Pillar**: Security  
**Best Practices**: 4

---

# AGENTSEC03-BP01 Implement strong authentication for agent identities

Shared API keys and one-way TLS give agents enough network
reachability to be useful and enough ambiguity to be impersonated.
Cryptographic identity for both sides of every call, with automated
lifecycle and immediate revocation, is the control that makes every
agent communication auditable and reversible.

**Desired outcome:**

- You authenticate all agent-to-agent and agent-to-service
communications using strong cryptographic mechanisms, with
mutual authentication that helps prevent impersonation and
interception.
- You automate certificate lifecycle management so expired
certificates don't cause authentication failures or security
gaps.
- You can revoke affected agent identities immediately, cutting
off unauthorized access within minutes.

**Common anti-patterns:**

- Using shared API keys or static tokens for agent authentication
instead of certificate-based or OAuth mechanisms, producing
credentials that are hard to rotate and straightforward to
exfiltrate.
- Implementing one-way TLS (server authentication only) without
mutual authentication, so any client on a permitted network path
can reach the endpoint without proof of its agent identity.
- Managing certificate lifecycles manually, leading to expired
certificates that either cause outages or are renewed without
proper security review.

**Benefits of establishing this best
practice:**

- Certificate-based or OAuth authentication provides cryptographic
proof of identity for both parties in every agent communication.
- Automated certificate lifecycle management reduces the risk of
expired certificates causing outages or security gaps.
- CRL and OCSP revocation provides the ability to cut off
unauthorized access within minutes when an agent identity is
affected.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Authentication for agents has two distinct jobs: proving the agent
is who it claims to be, and proving that to the receiver
cryptographically rather than through network-path heuristics.
Static credentials fail both tests. They are trivial to copy, hard
to rotate, and their holder is indistinguishable from their
issuer. The design pattern is cryptographic identity managed
centrally, with lifecycle automation and revocation as first-class
operations rather than afterthoughts.

[Amazon
Bedrock AgentCore Identity](https://docs.aws.amazon.com/bedrock/latest/userguide/agentcore-identity.html) handles the OAuth side of that
pattern. It provides managed OAuth 2.0 flows and identity
federation for agentic workloads, issuing, validating, and
rotating tokens without the operational burden of running that
infrastructure. Each agent registers in the centralized agent
identity directory and receives a unique identity. The
GetWorkloadAccessTokenForJWT API issues
agent-specific access tokens bound to the requesting agent's
identity. The token vault secures OAuth tokens with AWS KMS
encryption (customer-managed keys supported) and enforces
per-agent access controls so one agent can't retrieve another's
tokens.

For services that require certificate-based authentication rather
than OAuth, AWS Private Certificate Authority (AWS Private CA) is
the managed path for issuing internal mTLS client and server
certificates. AWS Private CA handles issuance and supports
automated renewal lifecycles, and certificate revocation through
CRL or OCSP provides the cutoff when an identity is affected.
Mutual TLS (mTLS) on AWS Application Load Balancers or Amazon API Gateway configurations gives agent-to-agent traffic symmetric
proof: both sides present certificates, both sides verify. Private
keys live in AWS Secrets Manager or Parameter Store, a capability
of AWS Systems Manager with AWS KMS encryption at rest and
automatic rotation policies, so the key itself never becomes a
long-lived static credential.

Detection rounds out the pattern. Amazon GuardDuty flags unusual
authentication patterns, agents authenticating from unexpected IP
addresses or at unusual times, and findings route into AWS Security Hub CSPM for centralized event management. That gives the
security team a single place to see when an identity is being used
in ways that don't match its normal profile, whether the
credentials themselves have been revoked.

### Implementation steps

- **Deploy AgentCore
Identity:** Deploy
[Amazon
Bedrock AgentCore Identity](https://docs.aws.amazon.com/bedrock/latest/userguide/agentcore-identity.html) for agent authentication,
configure identity federation for cross-service access, and
register each agent in the centralized identity directory
for unique, trackable identities.
- **Secure tokens in the
vault:** Configure the AgentCore Identity token
vault for OAuth token storage using customer-managed AWS KMS
keys for encryption, and enforce strict per-agent access
controls for credential retrieval.
- **Issue agent certificates from AWS Private CA:** Set up AWS Private Certificate Authority for agent identity certificates, with automated
renewal lifecycles configured.
- **Enforce mutual TLS
end-to-end:** Configure mTLS on all agent-to-agent
communication endpoints through Application Load Balancers
or Amazon API Gateway with mTLS authentication.
- **Store keys in Secrets Manager with
rotation:** Store all agent private keys and
credentials in AWS Secrets Manager with encryption at rest
and automatic rotation policies enabled.
- **Turn on revocation
checking:** Implement certificate revocation
through CRL or OCSP so affected agent certificates can be
invalidated immediately.
- **Alarm on authentication
anomalies:** Configure Amazon GuardDuty to detect
unusual authentication patterns and route findings to AWS Security Hub CSPM for centralized security event management.
- **Review certificate inventory
quarterly:** Identify and remediate certificates
approaching expiration or using deprecated algorithms on a
quarterly cadence.

## Resources

**Related best practices:**

- [AGENTSEC03-BP02 Separate
agent and human user permission](agentsec03-bp02.html)
- [AGENTSEC03-BP03
Implement least privilege with dynamic boundaries](agentsec03-bp03.html)
- [AGENTSEC06-BP01
Encrypt and sign inter-agent messages](agentsec06-bp01.html)

**Related documents:**

- [Securing
AI agents with Amazon Bedrock AgentCore Identity](https://aws.amazon.com/blogs/security/securing-ai-agents-with-amazon-bedrock-agentcore-identity/)
- [Amazon
Bedrock AgentCore Identity documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/agentcore-identity.html)
- [AgentCore
Identity supported authentication patterns](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/common-use-cases.html)
- [AWS Private CA documentation](https://docs.aws.amazon.com/privateca/latest/userguide/PcaWelcome.html)

**Related services:**

- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [AWS Private CA](https://aws.amazon.com/private-ca/)
- [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/)
- [Amazon GuardDuty](https://aws.amazon.com/guardduty/)
- [AWS Security Hub CSPM](https://aws.amazon.com/security-hub/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsec03-bp01.html*

---

# AGENTSEC03-BP02 Separate agent and human user permission

Identity propagation alone isn't enough when agents act on behalf of
users. Distinct agent service identities, with hard trust boundaries
helping prevent assumption of human-designated roles, keep audit
attribution unambiguous and stop a misconfigured agent from
escalating into a human identity space.

**Desired outcome:**

- Agent actions and human actions are distinguishable in audit
logs, with separate identities that help prevent agents from
inheriting or assuming human user permissions.
- Dedicated agent service identities are scoped to only the
permissions required for automated operations, and audit logs
attribute every action unambiguously to either an agent or a
human actor.
- Trust policies help prevent agents from assuming
human-designated identities, with organization-level guardrails
providing a secondary boundary in multi-account environments.

**Common anti-patterns:**

- Reusing human user IAM credentials or roles for agent
authentication, making it impossible to distinguish agent
actions from human actions in audit logs.
- Allowing agents to assume human IAM roles through role chaining,
enabling access to resources that should be restricted to human
users and creating a privilege-escalation path.
- Using a single shared service account for multiple agents,
reducing the risk of attribution of specific actions to
individual agents and complicating incident response.
- Relying only on agent-level IAM policies without role trust
policy restrictions or multi-account guardrails, leaving open
the assumption path where an affected agent role could still
assume a human role.

**Benefits of establishing this best
practice:**

- Separate identities produce unambiguous audit attribution that
clearly distinguishes agent actions from human actions.
- Trust policies refuse assumption by agent principals, with
optional organization-level guardrails adding a multi-account
ceiling.
- Consistent agent identity tagging and naming conventions enable
filtering and analysis of agent activity patterns during
incident investigations.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Two separations matter here and they are often collapsed in
practice. Identity separation means the agent operates under a
service identity distinct from any human identity, whether that
human is an operator managing AWS resources or an application user
interacting with the agent's service. Permission separation means
the agent's identity carries only the permissions it needs for its
tasks and never inherits the permissions of human identities.
These apply to both patterns (agents acting autonomously and
agents acting on behalf of a user), but the way user context flows
through a call differs: autonomous agents operate under their
service identity alone, while agents acting on behalf of a user
carry that user's context forward as token claims without the
agent ever assuming the user's credentials. Human operator
identities (which authenticate through IAM Identity Center for AWS
access) and application user identities (which authenticate
through a separate customer-facing identity provider and have no
AWS identity at all) are themselves distinct layers.

For agents that operate on AWS, create dedicated IAM roles for
each agent type as the agent's service identity, with a naming
convention (for example,
agent-role-) that
distinguishes them from human operator roles, and apply
PrincipalType: Agent as a consistent tag.
Principal tags surface in AWS CloudTrail events primarily for
management-plane API calls made with session tags. For
service-specific events that don't surface principal tags, filter
by the agent role ARN naming convention as the primary signal and
treat the tag as a secondary filter. Use AWS IAM Identity Center
for all human operator access and migrate any human operators
still using account-specific IAM users off those identities.
Application users are typically outside this migration, they
authenticate through the application's own identity provider, and
their identity flows into agent calls as token claims. Configure
Service Control Policies (SCPs) in AWS Organizations that
explicitly deny agents (identified by tag) from assuming roles in
the human operator identity boundary, for example denying
sts:AssumeRole for any principal tagged as an
agent attempting to assume roles tagged as human-operator.

Amazon Bedrock AgentCore introduces two identity constructs that
support this separation. The AgentCore Runtime
**execution role** is a regular IAM
role assumed by the Runtime process to reach AWS services the
agent depends on (model invocations, tool calls to AWS APIs,
memory reads and writes). The AgentCore
**Workload Identity** is an
agent-specific identity registered in the AgentCore Identity
directory, distinct from any IAM role, and used to issue and
verify agent-scoped tokens and vault third-party tokens obtained
on behalf of users. When an agent acts on behalf of an application
user, it calls GetWorkloadAccessTokenForJWT
with the user's access token from the application's identity
provider.
[Amazon
Bedrock AgentCore Identity](https://docs.aws.amazon.com/bedrock/latest/userguide/agentcore-identity.html) verifies the user token and
returns an agent-specific workload access token that embeds the
user context as claims, so the call chain carries both "who
the agent is" and "who the user is" without
the agent ever assuming the user's credentials or an IAM role on
the user's behalf.

For agents that need to reach third-party OAuth resources on
behalf of users, AgentCore Identity orchestrates the authorization
code grant flow and secures the resulting access tokens in a token
vault scoped per agent identity and per user. One agent can't
retrieve tokens obtained for a different user, and as long as the
third-party access token remains valid the agent can retrieve it
from the vault without requiring the user to re-authenticate.

Amazon Cognito provides an alternative for organizations already
standardized on Cognito user pools. The same principle (the agent
carries both its own identity and the user's context as token
claims) can be implemented outside AgentCore Identity. The pattern
described in
[Empower
AI agents with user context using Amazon Cognito](https://aws.amazon.com/blogs/security/empower-ai-agents-with-user-context-using-amazon-cognito/) uses
[Amazon Cognito](https://aws.amazon.com/cognito/) user pools: the agent authenticates through the
client credentials flow while passing the user's token as
additional context through the
aws_client_metadata request parameter, and a
[pre-token-generation
Lambda trigger](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-pre-token-generation.html) verifies the user token and injects an
onBehalfOf claim into the agent's access token
before issuance. The resulting JWT identifies the agent in its
sub claim and the user in its
onBehalfOf claim, producing a single token that
downstream authorization layers can evaluate. This is a custom
extension built on Cognito trigger hooks, not a native Cognito
feature, and it complements the AgentCore pattern rather than
replacing it. For authorization on top of the resulting token,
resource servers can evaluate claims directly, or externalize
policy to a service such as
[Amazon Verified Permissions](https://aws.amazon.com/verified-permissions/) using Cedar (a choice orthogonal to
whether you use AgentCore Identity or the Cognito pattern).

When an agent invokes a tool through AgentCore Gateway, the
gateway operates under its own execution role (one per gateway)
and the outbound authentication applied to the target depends on
the target type (see the
[AgentCore
Gateway outbound auth reference](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-outbound-auth.html) for details). User context
propagates through the gateway so downstream services can enforce
user-level authorization, and the gateway never substitutes an IAM
identity for the user or re-authenticates as the user against
downstream services.

Configure
[CloudTrail
with advanced event selectors](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html) to capture agent API calls,
including data events for agent-invoked services where visibility
beyond management-plane events matters. Enable AgentCore data
events so operations against AgentCore Memory, Gateway, and
Runtime are logged alongside management-plane events. Amazon CloudWatch Logs Insights queries filtered by agent role ARN
patterns give dedicated agent activity dashboards. For SQL-based
analysis over time, deliver CloudTrail logs to Amazon S3 and query
them with Amazon Athena (see AGENTSEC05-BP01).

For multi-agent systems where a parent agent directly assumes a
sub-agent's IAM role (for example, calling
sts:AssumeRole before invoking the sub-agent in
the same account), use role session names that include the parent
agent's identifier so the chain is visible in CloudTrail. For A2A
communication that routes through AgentCore Runtime, each agent
runs under its own independent execution role session and there is
no IAM role chain. Use correlation identifiers propagated through
the A2A message (see AGENTSEC05-BP02) to reconstruct the
agent-to-agent call graph.

### Implementation steps

- **Audit and rename agent
roles:** Identify any IAM roles shared between
agents and human users, and create dedicated agent-specific
roles with a consistent naming convention (for example,
agent-role-).
- **Tag agent roles
consistently:** Apply
PrincipalType: Agent and
AgentName: tags to every
agent IAM role for filtering and monitoring.
- **Move human operators to IAM Identity Center:** Configure AWS IAM Identity Center for all
human operator access and migrate any operators still on
account-specific IAM users.
- **Enforce the agent-to-human boundary
through SCPs:** Deploy Service Control Policies in
AWS Organizations that deny agents (identified by tag) from
assuming human-operator roles, creating a hard boundary
between the identity spaces.
- **Register Workload Identities for
on-behalf-of flows:** Register agent Workload
Identities in
[Amazon
Bedrock AgentCore Identity](https://docs.aws.amazon.com/bedrock/latest/userguide/agentcore-identity.html) for agents that act on
behalf of users, and use
GetWorkloadAccessTokenForJWT to create
agent-scoped tokens that embed user context as claims for
downstream authorization.
- **Enable CloudTrail with AgentCore
data events:** Turn on advanced event selectors
including AgentCore data events, and build Amazon CloudWatch Logs Insights queries filtered by agent role ARN patterns
for dedicated agent activity dashboards.
- **Analyze with Athena over
time:** Deliver AWS CloudTrail logs to Amazon S3
and use Amazon Athena for SQL-based analysis of agent
compared to human activity patterns over time for compliance
reporting and long-term trend analysis.
- **Name sessions for
attribution:** Implement role session naming
conventions that include agent identifiers (and parent agent
identifiers for delegation chains) for clear attribution in
multi-agent systems.

## Resources

**Related best practices:**

- [AGENTSEC03-BP01
Implement strong authentication for agent identities](agentsec03-bp01.html)
- [AGENTSEC03-BP03
Implement least privilege with dynamic boundaries](agentsec03-bp03.html)
- [AGENTSEC05-BP01
Implement comprehensive logging and decision artifact
storage](agentsec05-bp01.html)

**Related documents:**

- [AWS CloudTrail best practices](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/best-practices-security.html)
- [AWS IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html)
- [Securing
AI agents with Amazon Bedrock AgentCore Identity](https://aws.amazon.com/blogs/security/securing-ai-agents-with-amazon-bedrock-agentcore-identity/)
- [Empower
AI agents with user context using Amazon Cognito](https://aws.amazon.com/blogs/security/empower-ai-agents-with-user-context-using-amazon-cognito/)
- [Amazon
Bedrock AgentCore Identity documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/agentcore-identity.html)
- [AgentCore
Identity supported authentication patterns](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/common-use-cases.html)

**Related services:**

- [AWS Identity and Access Management](https://aws.amazon.com/iam/)
- [AWS IAM Identity Center](https://aws.amazon.com/iam/identity-center/)
- [AWS CloudTrail](https://aws.amazon.com/cloudtrail/)
- [AWS Organizations](https://aws.amazon.com/organizations/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon Cognito](https://aws.amazon.com/cognito/)
- [Amazon Verified Permissions](https://aws.amazon.com/verified-permissions/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsec03-bp02.html*

---

# AGENTSEC03-BP03 Implement least privilege with dynamic boundaries

Broad permissions grant an affected agent access well beyond the
task it was asked to do. Scoping privilege at each identity layer,
backing it with temporary credentials, and layering contextual IAM
conditions limits the scope of any single compromised or misprompted
call.

**Desired outcome:**

- Agents operate with the minimum permissions required to complete
their defined tasks, with temporary credentials that expire
automatically and dynamic permission boundaries that tighten
when handling sensitive data or high-risk operations.
- Just-in-time access patterns help limit elevated permissions to
the duration of the operation that requires them.
- You continually validate policy scoping as workloads evolve,
removing drift before it accumulates.

**Common anti-patterns:**

- Assigning broad IAM policies (for example,
s3:* or *) to agent roles
for convenience, granting far more access than any individual
task requires.
- Using long-lived static credentials instead of temporary
credentials from AWS STS, extending the window of exposure if
credentials are inadvertently disclosed.
- Failing to implement IAM permission boundaries, allowing agents
to create or modify IAM policies and escalate their own
privileges.
- Expanding agent permissions in response to access errors without
investigating whether the access pattern is legitimate,
accumulating excessive permissions through reactive grants that
are never revoked.

**Benefits of establishing this best
practice:**

- Least-privilege IAM roles limit an affected agent to only the
resources required for its current task.
- Temporary AWS STS credentials with short session durations
reduce the risk of long-lived credential exposure.
- IAM Conditions on region, resource tags, time windows, and
source network add defense-in-depth that limits the impact of
credential exposure.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

An agent operates under multiple identity layers, and each is a
separate place to apply scoping. The **agent
identity** is what this specific agent is as an entity in
your directory (for example, an AgentCore Workload Identity with a
unique ARN). The **service
identity** is what the agent runs as when it invokes AWS
services (for AgentCore Runtime. This is the IAM execution role
assumed by the Runtime process). The
**transaction identity** is the
per-invocation context carried with a single agent call, typically
expressed through AWS STS session credentials with session tags
and session policies. When an agent acts on behalf of a user, a
**user identity** is additionally
carried in the call context as token claims propagated through the
agent's call chain. Permission scoping applies differently at each
layer:

- Broad capability limits belong on the service identity (IAM
role, permission boundary)
- Per-operation constraints belong on the transaction (session
policy, session tags, and IAM Conditions)
- User-context constraints belong on the user identity
(token-based authorization evaluated at the resource)

At the service identity layer, design agent IAM roles using the
principle of least privilege, starting with no permissions and
adding only what is required for each specific task. AWS IAM Access Analyzer generates least-privilege policies based on actual
access patterns observed in AWS CloudTrail logs, giving you a
data-driven baseline for scoping. IAM permission boundaries on all
agent roles establish a maximum permission ceiling that can't be
exceeded even if the agent's policies are modified, which matters
because it is the control that helps prevent privilege escalation
when something about the policy itself changes.

[Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock/latest/userguide/agentcore-gateway.html) operates under a single execution
role per gateway, with outbound authentication that depends on
target type (see the
[AgentCore
Gateway outbound auth reference](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-outbound-auth.html)). Scope the gateway
execution role to only the actions and resources the set of
targets collectively requires, and constrain per-target access
through the target-specific outbound auth configuration. User
context propagated through the gateway lets downstream services
enforce user-level access controls in addition to the
gateway-level role, so operations are further constrained by the
originating user's permissions even if the gateway role has access
to a target.

Temporary credentials are how the transaction layer stays scoped.
AWS STS AssumeRole with session policies generates credentials
scoped to the specific permissions required for each task
execution, and short session durations (15 to 60 minutes) make
expiration automatic. For agents that require elevated permissions
for specific operations, just-in-time access through AWS IAM Identity Center or custom Lambda-based access request workflows
grants and revokes permissions programmatically.

IAM Conditions are the defense-in-depth layer that makes exposed
credentials less useful. aws:RequestedRegion
limits agent actions to approved regions.
aws:ResourceTag restricts access to resources
tagged for agent use. aws:CurrentTime enforces
time-window restrictions. aws:SourceVpc
requires that agent API calls originate from approved VPCs. These
conditions don't reduce the policy's stated permissions, but they
bound the contexts under which those permissions apply. At the
organization level, Service Control Policies in AWS Organizations
establish organization-wide guardrails that apply to all agent
accounts, helping prevent agents from accessing services or
performing actions that are never appropriate regardless of
task-level permissions.

### Implementation steps

- **Generate least-privilege policies
from usage data:** Audit existing agent IAM roles
with AWS IAM Access Analyzer to identify overly permissive
policies and generate least-privilege recommendations based
on actual access patterns in AWS CloudTrail logs.
- **Apply permission
boundaries:** Set IAM permission boundaries on all
agent roles to establish a maximum permission ceiling that
can't be exceeded even if the agent's task-level policies
are modified.
- **Scope the Gateway execution
role:** Restrict the
[Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock/latest/userguide/agentcore-gateway.html) execution role to only the
actions and resources its targets require, configure
target-specific outbound auth per target type, and use
AgentCore Identity to propagate user context for downstream
user-level enforcement.
- **Issue temporary credentials with
session policies:** Use AWS STS AssumeRole with
session policies and short session durations (15 to 60
minutes) for all agent credential issuance.
- **Add contextual IAM
Conditions:** Restrict access by region
(aws:RequestedRegion), resource tags
(aws:ResourceTag), time windows
(aws:CurrentTime), and source network
(aws:SourceVpc).
- **Deploy organization-wide
SCPs:** Establish organization-wide guardrails
through Service Control Policies in AWS Organizations that
apply to all agent accounts.
- **Implement just-in-time access for
elevated permissions:** Use IAM Identity Center or
custom Lambda-based access request workflows with automatic
revocation when the operation completes or the session
expires.
- **Review IAM drift
quarterly:** Schedule IAM Access Analyzer reviews
every quarter to detect permission drift, identify unused
access, and remove permissions that are no longer required.

## Resources

**Related best practices:**

- [AGENTSEC02-BP01
Implement tool authorization](agentsec02-bp01.html)
- [AGENTSEC03-BP01
Implement strong authentication for agent identities](agentsec03-bp01.html)
- [AGENTSEC03-BP02 Separate
agent and human user permission](agentsec03-bp02.html)
- [AGENTSEC03-BP04 Regular
permission audits and access reviews](agentsec03-bp04.html)
- [AGENTREL02-BP02
Limit agent permissions to minimum required access](agentrel02-bp02.html)

**Related documents:**

- [AWS IAM best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)
- [AWS IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html)
- [Amazon
Bedrock AgentCore Identity documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/agentcore-identity.html)
- [Amazon
Bedrock AgentCore Gateway documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/agentcore-gateway.html)
- [Service
control policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html)

**Related services:**

- [AWS Identity and Access Management](https://aws.amazon.com/iam/)
- [AWS IAM Access Analyzer](https://aws.amazon.com/iam/features/analyze-access/)
- [AWS Organizations](https://aws.amazon.com/organizations/)
- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsec03-bp03.html*

---

# AGENTSEC03-BP04 Regular permission audits and access reviews

Agent roles accumulate permissions over time. Scheduled automated
analysis paired with periodic human-led reviews catches drift before
it turns into significant over-privilege and produces the documented
audit trail that compliance needs.

**Desired outcome:**

- You continually monitor agent permissions and review them on a
cadence matched to the agent's risk profile, identifying and
removing unused access regularly.
- Automated alerts fire immediately when agent permissions are
modified, enabling rapid detection of unauthorized policy
changes.
- You document access reviews with timestamped findings and
remediation actions for compliance purposes.

**Common anti-patterns:**

- Conducting permission reviews only annually or in response to
incidents, letting drift accumulate undetected for months.
- Setting a single review cadence for every agent regardless of
risk, so high-risk agents (those with broad permissions,
mutating tool access, or production data reach) receive the same
scrutiny as low-risk informational agents.
- Reviewing permissions manually without tooling support, making
it impractical to assess the full scope of agent access across
dozens or hundreds of roles.
- Treating IAM Access Analyzer findings as informational rather
than as practical remediation items, so identified
over-privilege persists indefinitely.
- Not alerting on permission changes in real time, discovering
unauthorized policy modifications only during the next scheduled
review cycle weeks or months later.

**Benefits of establishing this best
practice:**

- Ongoing permission monitoring detects drift before it
accumulates into significant over-privilege.
- Timestamped findings and remediation actions support compliance
requirements and security investigations.
- Usage-based evidence from AWS CloudTrail drives permission
reduction with data rather than guesswork about which
permissions are still needed.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Two review modes are both necessary. Automated analysis provides
speed and coverage, the ability to scan every agent role across
every account every day. Periodic human-led reviews provide the
context that automation can't supply, such as whether a
technically unused permission is still needed for upcoming work,
whether a recent policy change was expected, and whether the
current privilege level matches the current role of the agent in
the business. Running only one of the two leaves a gap: automation
alone produces findings no one acts on, and manual-only reviews
happen too infrequently to catch drift in time.

AWS IAM Access Analyzer at the organization level continually
analyzes agent IAM policies and generates findings for permissions
that grant access to resources outside the intended scope. Its
unused-permissions analysis uses AWS CloudTrail activity data to
identify access that has not been exercised, giving a data-driven
basis for permission reduction rather than a guess. Weekly review
and remediation of Access Analyzer findings, prioritized by
severity, keeps the backlog bounded and turns findings into change
tickets.

AWS Config rules detect changes to agent IAM policies, roles, and
permission boundaries in near real time. Configure managed rules
such as
iam-policy-no-statements-with-admin-access
along with custom rules that validate agent-specific policy
constraints, and route rule violations through Amazon EventBridge
to an Amazon SNS topic so the security team is notified
immediately rather than during the next scheduled review.

For the formal periodic review, correlate Access Analyzer findings
with CloudTrail usage data to identify permissions that have not
been exercised in the period. The review cadence should match the
risk profile of the agent: high-risk agents (those with broad
permissions, write access to production data, or mutating tool
privileges) warrant frequent review, while low-risk informational
agents can be reviewed less often.
[AWS CloudTrail Lake](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-lake.html) provides queryable long-term retention for
this analysis, and AWS Lambda functions can automate the
generation of review reports by querying IAM and CloudTrail data
and publishing results to Amazon S3. The output feeds the review
meeting and produces the documented evidence compliance requires.

AWS Security Hub CSPM is the aggregation layer for large agent fleets.
Findings from IAM Access Analyzer, AWS Config, and Amazon GuardDuty flow into a single view where severity and business
impact drive prioritization, so the team is working from one list
instead of three consoles.

### Implementation steps

- **Enable organization-level IAM Access Analyzer:** Turn on AWS IAM Access Analyzer at the
organization level and configure it to analyze all agent IAM
roles for unused and overly permissive access.
- **Detect policy changes with AWS Config:** Deploy AWS Config rules to detect changes
to agent IAM policies and trigger Amazon EventBridge
notifications for immediate alerting to the security team.
- **Retain activity data in CloudTrail
Lake:** Configure AWS CloudTrail Lake for long-term
retention of agent API activity data, supporting access
review correlation and compliance reporting.
- **Automate weekly finding
reviews:** Implement automated weekly reviews of
Access Analyzer findings, generating reports that prioritize
high-severity findings for remediation.
- **Run a formal access review on a
risk-based cadence:** Set the review cadence per
agent based on its risk profile (high-risk agents reviewed
frequently, low-risk informational agents reviewed less
often). Correlate Access Analyzer findings with CloudTrail
usage data, document findings and remediation actions, and
record sign-off for each review cycle.
- **Aggregate findings in Security Hub CSPM:** Pull IAM findings from Access Analyzer, AWS Config, and Amazon GuardDuty into AWS Security Hub CSPM for a
unified view of permission-related issues across the agent
fleet.

## Resources

**Related best practices:**

- [AGENTSEC03-BP03
Implement least privilege with dynamic boundaries](agentsec03-bp03.html)
- [AGENTSEC03-BP02 Separate
agent and human user permission](agentsec03-bp02.html)
- [AGENTSEC05-BP01
Implement comprehensive logging and decision artifact
storage](agentsec05-bp01.html)

**Related documents:**

- [AWS IAM Access Analyzer documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html)
- [AWS Config managed rules](https://docs.aws.amazon.com/config/latest/developerguide/managed-rules-by-aws-config.html)

**Related services:**

- [AWS IAM Access Analyzer](https://aws.amazon.com/iam/features/analyze-access/)
- [AWS Config](https://aws.amazon.com/config/)
- [Amazon EventBridge](https://aws.amazon.com/eventbridge/)
- [AWS CloudTrail](https://aws.amazon.com/cloudtrail/)
- [AWS Security Hub CSPM](https://aws.amazon.com/security-hub/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsec03-bp04.html*

---

# AGENTSEC04 — Agent goal alignment and manipulation prevention

**Pillar**: Security  
**Best Practices**: 2

---

# AGENTSEC04-BP01 Implement guardrails and alignment controls

Instruction-following alone doesn't provide reliable enforcement.
Layered controls (deterministic where possible, probabilistic where
necessary) help keep agents inside operational boundaries even when
prompts are adversarial and model behavior is unpredictable.

**Desired outcome:**

- You define agent operational and policy boundaries up front and
enforce them through layered controls, with deterministic
controls (IAM, schema validation, technical policy checks)
handling what is expressible deterministically and probabilistic
controls (content filters, behavioral evaluation) handling what
isn't.
- Multiple validation layers at different stages of the agent call
chain can reduce the likelihood that a single control failure
results in a boundary violation.
- You log, alert on, and periodically review guardrail
interventions, policy violations, and behavioral evaluation
results to tune the controls and surface emerging patterns.

**Common anti-patterns:**

- Relying on a single guardrail configuration for all agent use
cases, applying the same constraints to low-risk informational
agents and high-risk operational agents.
- Applying content filtering only to model outputs without
validating inputs first, letting adversarial content reach the
model before any check runs.
- Defining operational boundaries in natural-language system
prompts alone, relying on the model's instruction-following as
the sole constraint, which can be bypassed through prompt
injection or adversarial framing.

**Benefits of establishing this best
practice:**

- Deterministic technical controls (IAM, schema validation)
combined with probabilistic content controls (Guardrails) at
distinct stages reduce reliance on instruction-following alone.
- Layered validation catches policy violations at multiple stages,
so a bypass at one layer is less likely to result in an
unchecked boundary violation.
- Logged guardrail interventions and evaluation results feed
policy updates as new patterns emerge, keeping boundaries
current with evolving use cases.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Operational boundaries written only in system prompts typically
don't provide reliable enforcement. A prompt can be overridden by
adversarial framing, prompt injection, or the model's own creative
reinterpretation, and none of those failure modes produces an
audit signal before the boundary has already been crossed. The
design pattern is layered. Express what can be expressed
deterministically as hard checks:

- IAM scoping
- Schema validation
- Cedar policies
- Permission boundaries

Use probabilistic controls (content filters, behavioral
evaluation) to cover the content-shaped risks that determinism
can't reach.

[Amazon
Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html) is the probabilistic layer. Configure a
base guardrail with universal constraints (no generation of
harmful content, no disclosure of system prompts), then overlay
use-case-specific configurations for each agent's operational
context. Content filter strengths need calibration to use case
sensitivity: HIGH strength for consumer-facing agents handling
categories like hate speech, violence, and sexual content, MEDIUM
strength for internal enterprise agents, and custom thresholds for
specialized domains (medical, legal) with their own content norms.
Content moderation needs to apply to every output path, including
outputs used in internal agent workflows and inter-agent messages,
not just user-facing responses. Use Guardrails versioning for
change management with rollback.

Pre-execution validation matters for two reasons. Applying
Guardrails to user inputs before they reach the model blocks
adversarial content before it influences reasoning, and it rejects
bad inputs before they consume inference capacity. When an agent
invokes an Amazon Bedrock model with a guardrail attached, the
check runs automatically on inputs and outputs. The
ApplyGuardrail API runs the same policy
independently when the automatic path doesn't apply, agents that
invoke non-Amazon Bedrock models (third-party APIs, self-hosted
models), pipelines that need to filter content before deciding
whether to invoke a model at all (for example, checking retrieved
content before it enters the prompt), or additional validation
checkpoints beyond the model invocation.

Monitoring closes the feedback loop. The
[Amazon
Bedrock Guardrails CloudWatch metrics](https://docs.aws.amazon.com/bedrock/latest/userguide/monitoring-guardrails-cw-metrics.html) include
InvocationsIntervened, broken down by
Operation (ApplyGuardrail)
and GuardrailContentSource
(Input / Output) so
input-side and output-side interventions are visible separately.
Amazon CloudWatch alarms on intervention rates route through
Amazon SNS to the security team. For the detail (what was blocked,
which policy triggered, which part of the content was affected),
enable Amazon Bedrock model invocation logging, which captures the
full guardrail trace for each call. Analyze intervention patterns
over time to find emerging techniques that require policy updates
and to catch filter categories generating excessive false
positives or false negatives.

[Amazon
Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html) assesses goal attainment
correctness and tracks whether agents are achieving their intended
objectives rather than drifting into misaligned goals. Built-in
evaluators cover correctness, helpfulness, tool selection
accuracy, and safety. Custom model-based evaluators extend
coverage to organization-specific alignment requirements. Run
evaluations on a regular cadence and after any significant change
to agent prompts, tools, or guardrail configurations. Results
publish to Amazon CloudWatch alongside AgentCore Observability
insights for a unified view, and CloudWatch alarms on evaluation
scores catch behavioral drift outside acceptable thresholds.

### Implementation steps

- **Map ethical constraints to guardrail
categories:** Define organizational ethical
constraints and operational boundaries per agent use case
and map them to guardrail policy categories with
risk-appropriate differentiation.
- **Build tiered guardrail
configurations:** Create base and use-case-specific
[Amazon
Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html) configurations, apply them to all
deployments, and use versioning for rollback capability.
- **Validate inputs before
inference:** Call the ApplyGuardrail API on inputs
before they reach the model, checking against denied topics,
word filters, and sensitive information patterns.
- **Alarm on intervention
metrics:** Configure Amazon CloudWatch alarms on
Guardrails metrics (especially
InvocationsIntervened), route alerts
through Amazon SNS, and enable Amazon Bedrock model
invocation logging for detailed intervention records.
- **Deploy AgentCore Evaluations with
drift alarms:** Deploy
[Amazon
Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html) with built-in and
custom evaluators, and configure Amazon CloudWatch alarms on
evaluation scores to detect behavioral drift.
- **Review intervention logs
monthly:** Establish a monthly review of guardrail
intervention logs to identify emerging patterns and update
policies accordingly.

## Resources

**Related best practices:**

- [AGENTSEC04-BP02
Human-in-the-loop for critical decisions](agentsec04-bp02.html)
- [AGENTSEC05-BP01
Implement comprehensive logging and decision artifact
storage](agentsec05-bp01.html)
- [AGENTSEC08-BP01
Multi-layer input validation and prompt injection
defense](agentsec08-bp01.html)

**Related documents:**

- [Amazon
Bedrock Guardrails documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html)
- [Amazon
Bedrock Guardrails content filters](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-content-filter.html)
- [Build
responsible AI applications with Amazon Bedrock
Guardrails](https://aws.amazon.com/blogs/machine-learning/build-responsible-ai-applications-with-amazon-bedrock-guardrails/)
- [Amazon
Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html)
- [Amazon
Bedrock AgentCore adds quality evaluations and policy
controls](https://aws.amazon.com/blogs/aws/amazon-bedrock-agentcore-adds-quality-evaluations-and-policy-controls-for-deploying-trusted-ai-agents/)
- [AI
agents in enterprises: Best practices with Amazon Bedrock
AgentCore](https://aws.amazon.com/blogs/machine-learning/ai-agents-in-enterprises-best-practices-with-amazon-bedrock-agentcore/)

**Related services:**

- [Amazon
Bedrock Guardrails](https://aws.amazon.com/bedrock/guardrails/)
- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon EventBridge](https://aws.amazon.com/eventbridge/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
- [Amazon SNS](https://aws.amazon.com/sns/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsec04-bp01.html*

---

# AGENTSEC04-BP02 Human-in-the-loop for critical decisions

Routing every agent action through human review produces
rubber-stamp approvals. Routing none produces unbounded autonomy.
Risk-tiered approval pauses agents only for the decisions where
human judgment actually changes the outcome, with enough context to
make those decisions meaningful.

**Desired outcome:**

- You pause high-risk agent operations for human review before
execution, and reviewers receive enough context to make informed
decisions within a defined time window.
- Escalation paths handle cases where primary reviewers are
unavailable.
- You log human approval decisions with timestamps and reviewer
identities, creating an auditable record of human oversight for
compliance purposes.

**Common anti-patterns:**

- Routing all agent actions through human review regardless of
risk level, creating reviewer fatigue and rubber-stamp
approvals.
- Providing reviewers with insufficient context (the proposed
action only, without the reasoning chain, data sources, or
potential consequences), turning review into a formality.
- Implementing approval workflows without timeout policies or
escalation paths, so agent execution stalls indefinitely when
reviewers are unavailable.

**Benefits of establishing this best
practice:**

- Risk-tiered approval workflows focus reviewer attention on the
decisions where human judgment matters most.
- Logged approval decisions with reviewer identity and timestamps
produce an auditable record that satisfies compliance
requirements.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

A risk classification framework is what lets human attention go
where it adds value. Combine static properties of the operation
(what kind of action, against what resource) with dynamic signals
about the request (frequency, time of day, source location, recent
anomalies). Risk classification itself can't rely on an LLM
exposed to the same untrusted content as the request being
evaluated, because adversarial content could influence the
classifier into marking the request as low-risk. Use deterministic
logic (policy engines, rule-based classifiers) as the
authoritative signal, with LLM-assisted classification as an
optional input that a deterministic layer re-checks. As a
baseline: read-only operations proceed autonomously, low-risk
writes require single-reviewer approval, and higher-risk
operations (financial transactions, data deletion, external
communications) require stricter approval, which can be
single-reviewer, multi-reviewer, or out-of-band depending on your
risk policy. For established risk framing approaches to adapt, see
the
[AWS Agentic AI Security Scoping Matrix](https://aws.amazon.com/ai/security/agentic-ai-scoping-matrix/) and
[this
guide to building AI agents in GxP environments](https://aws.amazon.com/blogs/machine-learning/a-guide-to-building-ai-agents-in-gxp-environments/).

Persistent trust grants, where a reviewer approves a specific
operation pattern once and future operations matching the pattern
proceed without re-approval, are a useful escape valve for
genuinely routine operations, but they shift where human judgment
is applied from moment-to-moment to at-grant time. If you
implement persistent trust, bound each grant to a specific
command, parameter shape, or resource. Tier grants by risk so
higher-risk operations are ineligible for persistent trust or
require re-confirmation at a defined cadence, and make grants
themselves auditable and revocable. Wildcard trust grants
(approving all future operations of a given type with no parameter
scoping) effectively remove human oversight from an entire class
of operations and should not be issued.

Once the classifier says human approval is required, route the
request to the approval mechanism appropriate for the agent's
execution environment. Three patterns cover most deployments. For
agents embedded in step-function-driven workloads,
[AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/connect-to-resource.html) .waitForTaskToken
callback pattern introduces an approval step. The workflow emits a
task token and pauses, the token is delivered to an approval
application through a channel appropriate to the reviewer
population (Amazon SNS to a queue that the approval app consumes,
Amazon SES to a reviewer mailbox, or a webhook endpoint on the
approval app), the application presents the decision to the
reviewer, and the application calls
SendTaskSuccess or
SendTaskFailure with the task token on the
reviewer's behalf. Reviewers don't typically call Step Functions
APIs directly. The approval app holds the credentials, and the
reviewer interacts with the app. See the
[human
approval in Step Functions tutorial](https://docs.aws.amazon.com/step-functions/latest/dg/tutorial-human-approval.html) for a worked example.

For agents built on
[Amazon
Bedrock Agents](https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html), two built-in patterns handle
human-in-the-loop confirmation without external workflow
orchestration.
[User
confirmation](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-userconfirmation.html) pauses the agent before executing a specific
function and returns the function name and parameter values to the
calling application for yes/no presentation to the user.
[Return
of control (ROC)](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-returncontrol.html) goes further by returning the function
call itself so the application decides what to do (present to a
user, run validation, modify parameters, or reject). ROC is
configured at the action group level and covers all actions in
that group. Both patterns assume the application is the component
implementing the human approval UX. These are better suited for
interactive use cases where the end user of the application is
also the approver, while Step Functions callback patterns fit
asynchronous workflows with separate reviewer roles.

For agents that need long-running approval processing,
[Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-long-run.html) supports both synchronous and
asynchronous processing through a unified API, enabling an agent
to start a task that may take minutes or hours, immediately
acknowledge the request, continue approval workflows in the
background, and let the user check back later for results. The SDK
provides explicit task lifecycle management through
add_async_task and
complete_async_task APIs, which track
processing status and report agent health through the
/ping endpoint. An agent reports
HealthyBusy while background approval tasks are
in progress and Healthy when idle. This is
particularly useful for multi-reviewer consensus workflows where
approval collection spans extended periods. Blocking operations
such as waiting for reviewer responses need to run in separate
threads or use async methods to avoid blocking the health-check
endpoint, which would cause the runtime session to terminate after
15 minutes of unresponsive pings.

Reviewers need enough context to make informed decisions without
wading through raw logs. Decisions involving agent reasoning often
produce a large volume of intermediate content (prompts, tool
outputs, retrieved documents, model responses) that is too much to
deliver in a notification payload and may be accessed by reviewers
who are not signed into the agent's application. Store the full
decision context in durable storage such as Amazon S3 before
sending the approval notification, including the agent's reasoning
chain, the proposed action, relevant data sources, and potential
consequences. Make the context available through the same
authenticated interface the reviewer uses to approve or deny. When
reviewers don't have access to the approval system's UI (for
example, approvals through email), presigned S3 URLs with short
expiration times provide temporary access to the context document.
Structure the context to highlight the key decision factors.

Timeout policies and escalation paths are specific to each
approval mechanism. In Step Functions,
TimeoutSeconds or
HeartbeatSeconds on the task state waiting for
the approval token triggers a timeout transition, and
Catch clauses route timed-out executions to an
escalation state (notify secondary reviewers, escalate to
management, or default to a safe fallback, typically blocking the
operation). See
[Step
Functions error handling](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-error-handling.html) for the attribute details. For
Amazon Bedrock Agents user-confirmation and ROC flows, timeouts
and escalation are handled by the calling application. For
AgentCore Runtime async tasks, the underlying Step Functions
timeouts apply because the async task typically waits on a Step
Functions callback or equivalent external signal.

Approval decisions need to be logged for compliance and audit.
Capture reviewer identity, notification and response timestamps,
the operation under review, the decision, and any escalation
events. Step Functions emits execution history to Amazon CloudWatch Logs when logging is enabled at the workflow level (see
[Step
Functions logging](https://docs.aws.amazon.com/step-functions/latest/dg/monitoring-logging.html)). Augment this with application-level
logs from the approval app so reviewer identity and decision
rationale are captured alongside the
SendTaskSuccess/SendTaskFailure
calls. For AgentCore-based agents, the AgentCore Observability
session and trace hierarchy captures agent-side events and pairs
with the approval-app logs for a complete record. Retain logs
consistent with your compliance requirements and AGENTSEC05-BP01.

### Implementation steps

- **Define a deterministic risk
classifier:** Map agent operation types to approval
tier requirements (autonomous, single-reviewer,
multi-reviewer), combine static classification with dynamic
request-time signals, and implement the classifier as
deterministic logic rather than an LLM.
- **Match approval mechanism to
execution environment:** Use
[AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/connect-to-resource.html) callbacks for step-function-driven
agents,
[Amazon
Bedrock Agents](https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html) user confirmation or return-of-control
for agents on Amazon Bedrock Agents, and
[Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-long-run.html) async tasks for agents that
need long-running approval processing, and implement the
corresponding pattern for each tier that requires human
approval.
- **Bound any persistent trust
grants:** Scope each grant narrowly (specific
command, parameter shape, or resource), tier grants by risk,
and make them auditable and revocable.
- **Store decision context
durably:** Write full decision context to Amazon S3
before sending approval notifications, and make the context
available through the authenticated approval interface or
through short-lived presigned URLs when that isn't possible.
- **Configure timeouts with safe
fallbacks:** Implement timeout policies and
escalation paths for each approval mechanism, with safe
fallback actions (typically blocking the operation) when no
reviewer responds in the defined window.
- **Log every approval:**
Capture reviewer identity, timestamps, operation under
review, decision, and escalation events, aligned with
AGENTSEC05-BP01 retention and compliance requirements.
- **Review workflow metrics
periodically:** Look for patterns that suggest
reviewer fatigue or process inefficiencies and adjust
risk-tier thresholds accordingly.

## Resources

**Related best practices:**

- [AGENTSEC04-BP01
Implement guardrails and alignment controls](agentsec04-bp01.html)
- [AGENTSEC07-BP01
Implement cognitive load management](agentsec07-bp01.html)
- [AGENTSEC07-BP03
Multiple reviewers for critical operations](agentsec07-bp03.html)

**Related documents:**

- [AWS Step Functions callback patterns](https://docs.aws.amazon.com/step-functions/latest/dg/connect-to-resource.html)
- [Human
approval in Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/tutorial-human-approval.html)
- [Step
Functions error handling](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-error-handling.html)
- [Step
Functions logging](https://docs.aws.amazon.com/step-functions/latest/dg/monitoring-logging.html)
- [Implement
human-in-the-loop confirmation with Amazon Bedrock
Agents](https://aws.amazon.com/blogs/machine-learning/implement-human-in-the-loop-confirmation-with-amazon-bedrock-agents/)
- [Amazon
Bedrock Agents user confirmation](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-userconfirmation.html)
- [Amazon
Bedrock Agents return of control](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-returncontrol.html)
- [Amazon
Bedrock AgentCore Runtime asynchronous processing](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-long-run.html)
- [AWS Agentic AI Security Scoping Matrix](https://aws.amazon.com/ai/security/agentic-ai-scoping-matrix/)
- [A
guide to building AI agents in GxP environments](https://aws.amazon.com/blogs/machine-learning/a-guide-to-building-ai-agents-in-gxp-environments/)

**Related services:**

- [AWS Step Functions](https://aws.amazon.com/step-functions/)
- [Amazon SNS](https://aws.amazon.com/sns/)
- [Amazon SES](https://aws.amazon.com/ses/)
- [Amazon S3](https://aws.amazon.com/s3/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsec04-bp02.html*

---

# AGENTSEC05 — Agent observability and non-repudiation

**Pillar**: Security  
**Best Practices**: 2

---

# AGENTSEC05-BP01 Implement comprehensive logging and decision artifact storage

Agent decisions are only auditable if the reasoning behind them is
captured, preserved intact, and reachable at the speed
investigations actually move. Tamper-evident artifact storage,
attribution to the original trigger, and a queryable index turn raw
log volume into forensic capability.

**Desired outcome:**

- You capture every agent decision, action, and reasoning step in
tamper-evident, queryable storage, producing a complete and
verifiable record of agent behavior.
- Each logged action includes attribution to the initiating source
(a human user session, an upstream event, a schedule, or another
agent), so logged actions can typically be traced back to what
triggered them.
- You can reconstruct the full decision-making process for any
agent action from stored artifacts, independent of the agent's
own account of its reasoning.
- Cryptographic validation verifies log integrity, the agent's
operational IAM role can't modify or delete its own decision
history, and sensitive data (PII, secrets, regulated fields) is
masked or redacted before logs are written to long-term storage.

**Common anti-patterns:**

- Logging only final agent outputs without intermediate reasoning,
tool invocations, or decision points, making incident
reconstruction impossible.
- Storing logs and decision artifacts in mutable storage without
write-once protection, so logs can be deleted or modified after
the fact.
- Storing decision artifacts in the same account and with the same
permissions as the agent's operational resources, letting an
affected agent modify or delete its own history.
- Retaining artifacts without a queryable index, so scanning raw
S3 objects becomes impractical during time-sensitive
investigations.

**Benefits of establishing this best
practice:**

- Detailed logging of reasoning chains, tool invocations, and
intermediate steps, stored independently from the agent's
operational resources, supports reconstruction of agent behavior
during investigations.
- Amazon S3 Object Lock and AWS CloudTrail log file validation
provide cryptographic proof of log integrity for compliance and
forensic purposes.
- Queryable artifact stores support retrospective behavioral
analysis that surfaces patterns missed by real-time alerts.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Logging for agents has three hard requirements that ordinary
application logging doesn't:

- Completeness (the reasoning chain, not just the outputs)
- Immutability (the agent whose behavior you are investigating
can't be the entity that controls its own logs)
- Queryability at investigation speed (S3 scans are not fast
enough when minutes matter)

Each of those requirements shapes a different piece of the
architecture.

Start with the model invocation layer. Enable Amazon Bedrock model
invocation logging to capture all inference requests and responses
(input prompts, model outputs, token counts, latency metrics) with
delivery to Amazon CloudWatch Logs for operational monitoring and
Amazon S3 for long-term retention. Because agent prompts and model
outputs often contain PII, secrets, or regulated data, apply data
protection before content lands in long-term storage.
[Amazon CloudWatch Logs data protection policies](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/mask-sensitive-log-data.html) automatically
detect and mask sensitive types (credentials, personal
identifiers, financial data) in log events.
[Amazon
Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html) sensitive information filters anonymize
or redact PII in input prompts and model responses at inference
time, but that is distinct from what the logs capture. Verify
masking behavior across each destination in use (Amazon Bedrock
Model Invocation Logs, AgentCore Observability, CloudWatch Logs,
the S3 artifact store) and add write-time masking in agent code
wherever the source doesn't mask on its own.

Decision artifacts require a separate trust boundary. Create a
dedicated S3 bucket in a separate AWS account with versioning
enabled, and use bucket policies that allow write from the agent
account but deny delete and overwrite operations. That gives you
an append-only artifact store the agent's operational IAM role
can't tamper with. A consistent key schema (agent ID, session ID,
timestamp, decision type) makes retrieval predictable during
investigations. Capture the initiator on every decision. An agent
can be invoked by:

- A human user session
- An Amazon EventBridge event
- An Amazon SQS message
- An Amazon CloudWatch alarm
- A scheduled rule
- Another agent

Log the identifiers that describe the trigger (IAM session or
Amazon Cognito user for human requests, event source and event ID
for events, alarm ARN for alarms, calling agent and session IDs
for inter-agent calls) as structured fields so investigation
queries can filter by trigger source.

For tamper-evidence on the bucket itself, default to bucket
policies that deny delete and overwrite, MFA delete on the bucket,
and versioning. Where compliance requirements call for stronger
guarantees, consider enabling Amazon S3 Object Lock in governance
mode, which allows users with specific IAM permissions to override
retention settings when needed. Compliance mode helps prevent any
user (including the root account) from deleting or shortening
retention periods for the duration of the lock. Once configured,
this mode is irreversible, and a misconfiguration of the retention
period or scope can leave a customer unable to delete data they
need to delete (for example, to meet right-to-be-forgotten
requests). Use compliance mode only when there is a specific
regulatory requirement for it, and validate the retention
configuration against representative test data before applying it
broadly.

[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-telemetry.html) captures agent reasoning
chains, tool invocations, and decision artifacts automatically for
agents running on AgentCore Runtime. The session, trace, and span
hierarchy records reasoning steps, tool calls with inputs and
outputs, and memory operations. AgentCore outputs span data for
memory resources by default and publishes session-level metrics
viewable on the Amazon CloudWatch generative AI observability
page. For artifacts that need retention beyond the default
observability window or specific compliance controls, write the
full decision context to the dedicated S3 artifact store at each
significant decision point. AWS Distro for OpenTelemetry (ADOT)
extends coverage with custom metrics, logs, and spans in agent
code.

[Amazon
Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html) complements logging by
continually scoring agent behavior on correctness, helpfulness,
tool selection accuracy, and safety. Results publish to Amazon CloudWatch alongside observability data for a unified view, and
Amazon CloudWatch alarms on evaluation scores detect behavioral
drift outside acceptable thresholds.

Tamper-evidence at the audit-trail level uses AWS CloudTrail with
log file validation across all accounts and regions where agents
operate. Log file validation produces SHA-256 hashes and RSA
signatures in a digest file that verifies log files have not been
modified, deleted, or forged after delivery. A dedicated S3 bucket
with cross-account access controls helps prevent the agent's own
IAM role from modifying or deleting logs.

Amazon Athena with AWS Glue Data Catalog makes the decision
artifact store queryable: an AWS Glue crawler scans the S3
artifact bucket and creates tables in the Data Catalog based on
the artifact schema, and Athena runs SQL queries directly against
S3 without loading data into a separate database. Investigation
queries such as "find all decisions made by agent X that
involved tool Y between dates A and B" become cheap to run.
Document standard investigation queries for common security
scenarios so investigators can work immediately during an
incident. This pattern (logs to Amazon S3, cataloged by AWS Glue,
queried with Amazon Athena) is an established forensic log
analytics approach recommended in the AWS Well-Architected
Security Pillar.

A lifecycle policy keeps storage costs proportional to access
patterns. Hot logs live in Amazon CloudWatch Logs for operational
monitoring (30 to 90 days), transition to Amazon S3 Standard for
medium-term retention (1 to 2 years), and archive to Amazon Glacier for long-term compliance retention (7+ years). Tag objects
with data classification and retention policy metadata so
lifecycle transitions are automated.

### Implementation steps

- **Enable Amazon Bedrock model
invocation logging:** Turn on Amazon Bedrock model
invocation logging and deliver to both Amazon CloudWatch Logs and Amazon S3.
- **Mask sensitive data before it lands
in long-term storage:** Configure Amazon CloudWatch Logs data protection policies, verify masking behavior
across every logging destination in use, and add write-time
masking in agent code where the destination doesn't mask on
its own.
- **Create a dedicated, append-only
artifact bucket in a Log Archive account:** Create
an Amazon S3 bucket in a separate Log Archive account,
aligned with the
[AWS Security Reference Architecture](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/welcome.html), with versioning
enabled and cross-account access controls that allow agent
write access but deny delete and overwrite operations.
- **Choose a retention-protection
model:** Default to bucket-policy-based protection
(deny delete, deny overwrite, MFA delete, versioning).
Evaluate Amazon S3 Object Lock in governance mode where
compliance requires stronger guarantees, and reserve
compliance mode for cases where there is a specific
regulatory requirement for it after validating the retention
scope and duration against representative test data.
- **Capture full traces through
AgentCore Observability:** Use
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-telemetry.html) to capture full agent
execution traces, and for artifacts needing longer retention
or compliance controls, write the full decision context to
the dedicated S3 artifact store at each significant decision
point.
- **Record initiator attributes on every
artifact:** Capture human session, event source and
event ID, alarm ARN, schedule rule ARN, calling agent ID,
and similar identifiers as structured fields on decision
artifacts and log entries.
- **Apply a consistent artifact key
schema:** Use
`agentId`, `sessionId`, `timestamp`, and `decisionType`
as the key schema for efficient retrieval during
investigations.
- **Deploy AgentCore Evaluations with
drift alarms:** Deploy
[Amazon
Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html) with built-in and
custom evaluators, publish results to Amazon CloudWatch, and
configure alarms on evaluation scores to detect behavioral
drift.
- **Enable CloudTrail log file
validation:** Turn on AWS CloudTrail with log file
validation across all accounts and regions, storing logs in
a dedicated S3 bucket with cross-account access controls.
- **Make artifacts queryable with Athena
and AWS Glue:** Set up an AWS Glue crawler to scan
the S3 artifact bucket and create tables in the Data
Catalog, use Amazon Athena to query artifacts directly in
S3, and document standard investigation queries for common
security scenarios.
- **Implement tiered retention with
automation:** Define retention tiers (CloudWatch Logs for operational monitoring, S3 Standard for
medium-term, Amazon Glacier for long-term compliance) with
automated lifecycle transitions and data classification
tagging.
- **Encrypt all log and artifact
storage:** Use customer-managed AWS KMS keys with
key rotation enabled on every logging destination.

## Resources

**Related best practices:**

- [AGENTSEC03-BP02
Separate agent and human user permission](agentsec03-bp02.html)
- [AGENTSEC04-BP02
Human-in-the-loop for critical decisions](agentsec04-bp02.html)
- [AGENTSEC05-BP02
Implement distributed tracing for agent interactions](agentsec05-bp02.html)
- [AGENTREL07-BP03
Implement distributed tracing to track system dependencies and
facilitate recovery](agentrel07-bp03.html)

**Related documents:**

- [Amazon
Bedrock model invocation logging](https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html)
- [AgentCore
Observability: Sessions, traces, and spans](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-telemetry.html)
- [Build
trustworthy AI agents with Amazon Bedrock AgentCore
Observability](https://aws.amazon.com/blogs/machine-learning/build-trustworthy-ai-agents-with-amazon-bedrock-agentcore-observability/)
- [Amazon
Bedrock AgentCore adds quality evaluations and policy
controls](https://aws.amazon.com/blogs/aws/amazon-bedrock-agentcore-adds-quality-evaluations-and-policy-controls-for-deploying-trusted-ai-agents/)
- [AWS CloudTrail log file validation](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-log-file-validation-intro.html)
- [Amazon S3 Object Lock](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html)
- [Amazon CloudWatch Logs data protection](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/mask-sensitive-log-data.html)
- [Amazon Athena documentation](https://docs.aws.amazon.com/athena/latest/ug/what-is.html)
- [Querying
AWS service logs with Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/querying-aws-service-logs.html)
- [Create
a customizable cross-company log lake for compliance (AWS Big
Data Blog)](https://aws.amazon.com/blogs/big-data/create-a-customizable-cross-company-log-lake-part-ii-build-and-add-amazon-bedrock/)
- [AWS Well-Architected Security Pillar SEC04-BP01: Configure service
and application logging](https://docs.aws.amazon.com/wellarchitected/latest/framework/sec_detect_investigate_events_app_service_logging.html)
- [Considerations
for addressing the core dimensions of responsible AI for
Amazon Bedrock applications](https://aws.amazon.com/blogs/machine-learning/considerations-for-addressing-the-core-dimensions-of-responsible-ai-for-amazon-bedrock-applications/)
- [Security
reference architecture for generative AI](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-generative-ai/gen-ai-sra.html)

**Related services:**

- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [AWS CloudTrail](https://aws.amazon.com/cloudtrail/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
- [Amazon S3](https://aws.amazon.com/s3/)
- [Amazon Athena](https://aws.amazon.com/athena/)
- [AWS Glue](https://aws.amazon.com/glue/)
- [AWS Key Management Service](https://aws.amazon.com/kms/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsec05-bp01.html*

---

# AGENTSEC05-BP02 Implement distributed tracing for agent interactions

A request that hops across agents, queues, and event buses is only
investigable if a single identifier follows it end-to-end. Tracing
with both a trace ID for instrumented services and an
application-level correlation ID for asynchronous boundaries makes
cross-agent incidents reconstructable.

**Desired outcome:**

- You trace every request that flows through a multi-agent system
end-to-end with a single correlation identifier, so security
teams can reconstruct the complete chain of agent interactions
for traced operations.
- Service maps give real-time visibility into agent dependencies
and communication patterns.

**Common anti-patterns:**

- Generating new trace IDs at each agent boundary rather than
propagating the original, breaking the correlation chain and
making it impossible to link related actions.
- Tracing only synchronous agent interactions and omitting
asynchronous operations (Amazon SQS messages, Amazon EventBridge
events), creating gaps that obscure the full execution path.
- Not instrumenting tool invocations within agent traces, losing
visibility into which external services were called and what
data was exchanged during execution.

**Benefits of establishing this best
practice:**

- Correlated traces across agent boundaries make every agent
execution reconstructable after the fact.
- Service maps and trace analysis surface unexpected communication
patterns, such as agents interacting with services outside their
normal dependency graph.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Two identifiers do the work together. A *trace
ID* is generated by the tracing system (Amazon CloudWatch Application Signals, AWS X-Ray, OpenTelemetry) and
follows a request through instrumented services. It is the
identifier the tracing backend uses to reconstruct spans into a
trace tree. A *correlation ID* is generated by
the application and propagated end-to-end, and it survives
boundaries where trace context is re-generated (most commonly
asynchronous messaging channels, where the consumer frequently
starts a new trace). Trace IDs give you the automatic correlation
where instrumentation is continuous. Correlation IDs give you
reliable linkage across the boundaries that instrumentation can't
traverse.

[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-telemetry.html) provides built-in tracing
for agents deployed on AgentCore Runtime. Sessions represent
complete user interactions, traces represent individual
request-response cycles, and spans represent specific operations
within a trace. AgentCore outputs span data for memory resources
by default, and session-level metrics are viewable on the Amazon CloudWatch generative AI observability page. The built-in
instrumentation captures the agent execution loop and propagates
trace context across agent boundaries without custom code.

For deeper visibility or for agents not running on AgentCore
Runtime, instrument agent code with AWS Distro for OpenTelemetry
(ADOT) to generate traces compatible with AWS X-Ray and
third-party observability platforms. Create spans for each
significant operation within an agent (model invocations, tool
calls, memory reads and writes, inter-agent communications) and
configure X-Ray sampling rules to capture 100% of traces for
security-critical operations while using statistical sampling for
high-volume routine operations.

Correlation ID propagation is the primary concern in all
agent-to-agent communications. Include both the correlation ID and
the current trace ID in inter-agent messages, API calls, and event
payloads, so the full execution chain can be reconstructed from
any point. For asynchronous operations through Amazon SQS or
Amazon EventBridge, propagate both IDs through message attributes.
The correlation ID preserves end-to-end linkage even when the
tracing system starts a new trace on the consumer side.

The Amazon CloudWatch generative AI observability page provides
agent-specific session and trace metrics for AgentCore Runtime.
For cross-service visualization that covers non-agent components
in the same request path (databases, queues, downstream services),
Amazon CloudWatch ServiceLens renders a service map of agent
interactions and surfaces unexpected communication patterns.
Amazon CloudWatch Logs Insights queries identify traces with
unusual patterns: agents calling unexpected services, traces with
abnormally high tool invocation counts, or traces that span
unexpected geographic regions.

### Implementation steps

- **Verify built-in AgentCore
tracing:** For agents on AgentCore Runtime, confirm
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-telemetry.html) is capturing session,
trace, and span data and review the default metrics on the
Amazon CloudWatch generative AI observability page.
- **Instrument custom agents with
ADOT:** For custom agents or deeper visibility,
instrument agent code with AWS Distro for OpenTelemetry to
generate spans for model invocations, tool calls, memory
operations, and inter-agent communications.
- **Propagate correlation IDs through
async boundaries:** Include the correlation ID and
current trace ID in all inter-agent messages, API calls, and
event payloads, and propagate them through Amazon SQS
message attributes and Amazon EventBridge event detail for
asynchronous operations.
- **Configure X-Ray sampling by
risk:** Capture 100% of traces for
security-critical operations and statistical sampling for
routine operations through AWS X-Ray sampling rules.
- **Visualize service maps and detect
anomalies:** Use Amazon CloudWatch ServiceLens to
visualize agent service maps and build Amazon CloudWatch Logs Insights queries to detect anomalous trace patterns.
- **Set trace retention:**
Configure trace retention policies that match your incident
investigation and compliance requirements.

## Resources

**Related best practices:**

- [AGENTSEC05-BP01
Implement comprehensive logging and decision artifact
storage](agentsec05-bp01.html)
- [AGENTSEC06-BP04
Monitor and detect coordination anomalies](agentsec06-bp04.html)
- [AGENTREL07-BP03
Implement distributed tracing to track system dependencies and
facilitate recovery](agentrel07-bp03.html)
- [AGENTPERF01-BP03
Profile end-to-end agent latency and identify optimization
targets](agentperf01-bp03.html)

**Related documents:**

- [AgentCore
Observability: Sessions, traces, and spans](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-telemetry.html)
- [Build
trustworthy AI agents with Amazon Bedrock AgentCore
Observability](https://aws.amazon.com/blogs/machine-learning/build-trustworthy-ai-agents-with-amazon-bedrock-agentcore-observability/)
- [AWS X-Ray documentation](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html)
- [AWS Distro for
OpenTelemetry](https://aws-otel.github.io/)
- [Amazon CloudWatch ServiceLens](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ServiceLens.html)

**Related services:**

- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [AWS X-Ray](https://aws.amazon.com/xray/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsec05-bp02.html*

---

# AGENTSEC06 — Secure multi-agent orchestration

**Pillar**: Security  
**Best Practices**: 4

---

# AGENTSEC06-BP01 Encrypt and sign inter-agent messages

Transport-level encryption stops protecting the payload the moment a
message lands in a queue or event bus. Message-level signing and
encryption keyed per trust zone gives receiving agents cryptographic
proof of sender identity and content integrity no matter how many
hops the message made.

**Desired outcome:**

- You protect inter-agent messages at the message level with
encryption and signing, independent of transport-level security.
- Receiving agents verify message signatures before acting on
instructions from other agents.
- Messages stored in queues or event buses are encrypted at rest
with keys scoped to the appropriate trust zone.
- Agents can't forge messages that appear to originate from other
agents in the coordination workflow.

**Common anti-patterns:**

- Relying solely on transport-level encryption (TLS) without
message-level signing, so messages stored in queues or event
buses can't be verified for tampering at consumption time.
- Using a single shared encryption key across all agents, so one
key exposure affects every inter-agent message rather than only
those in one trust zone.
- Not verifying message signatures before acting on inter-agent
instructions, letting an agent act on forged or tampered
instructions without any integrity check.

**Benefits of establishing this best
practice:**

- Message-level integrity verification persists beyond the
transport layer, so messages stored in queues or event buses can
be verified at consumption time.
- Scoped key management limits the impact of a key exposure to a
single trust zone rather than the entire multi-agent system.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Two distinct properties are at stake: who sent the message
(covered by AGENTSEC03-BP01 for authentication) and whether the
content is what the sender actually sent. Transport-level
encryption provides the second property only while the message is
in transit. The moment the message lands in an Amazon SQS queue,
Amazon EventBridge bus, or AWS Step Functions state machine, there
is no transport to protect it, and any modification between
delivery and consumption is invisible. Message-level signing
provides cryptographic proof that a specific message was sent by a
specific agent and has not been modified, regardless of how many
intermediary services it passed through.

Scope matters. For direct agent-to-agent communication within a
single trust zone, the transport-level security and authentication
provided by
[Amazon
Bedrock AgentCore Runtime](https://aws.amazon.com/blogs/machine-learning/introducing-agent-to-agent-protocol-support-in-amazon-bedrock-agentcore-runtime/) (TLS 1.2+ with OAuth 2.0 or
SigV4) is typically sufficient. Layer message signing on top when
payload integrity needs to persist beyond the transport, or when a
receiving agent needs cryptographic proof of which specific agent
sent an instruction.

AWS KMS asymmetric keys are the mechanism. The sending agent signs
the message payload through the KMS Sign API, and the receiving
agent verifies the signature through the KMS Verify API before
acting on the message. This gives end-to-end integrity
verification that is independent of the transport layer: even if a
message passes through multiple intermediary services (load
balancers, queues, event buses), the signature proves it was
created by the claimed sender and has not been modified. Separate
keys per trust zone limit the scope affected by a single key
exposure.

For asynchronous agent messaging through Amazon SQS, enable
server-side encryption using AWS KMS customer-managed keys.
Configure separate keys for different agent trust zones so a key
exposure in one zone doesn't affect messages in other zones, and
use SQS message attributes to carry the message signature
alongside the encrypted payload so receiving agents verify both
authenticity and integrity at consumption time.

AgentCore Runtime provides session isolation and built-in
authentication for agents using the Agent-to-Agent (A2A) protocol.
A2A handles authentication for inter-agent interactions, but for
messages that cross trust boundaries, carry sensitive data, or
pass through intermediary services, message-level signing layers
on top of the protocol's built-in protections.

AWS PrivateLink routes inter-agent communications through private
network endpoints, keeping traffic off the public internet. That
complements message-level encryption by reducing the network
exposure of inter-agent traffic. Store signing key ARNs in
Parameter Store, a capability of AWS Systems Manager, configure
automatic key rotation in AWS KMS with a rotation period matching
your security requirements, and configure Amazon CloudWatch alarms
for key usage anomalies (unexpected signing operations from agents
that should only be verifying, signing volume spikes suggesting a
runaway loop).

### Implementation steps

- **Create trust-zone-scoped KMS key
pairs:** Provision AWS KMS asymmetric key pairs for
message signing, with separate keys for each agent trust
zone.
- **Sign messages on send:**
Implement message signing in sending agents through the AWS KMS Sign API, attaching the signature as a message metadata
attribute.
- **Verify signatures on
receive:** Implement signature verification in
receiving agents through the AWS KMS Verify API, rejecting
any message that fails verification before processing.
- **Encrypt SQS queues with
customer-managed keys:** Enable server-side
encryption on Amazon SQS queues used for asynchronous
inter-agent messaging, using customer-managed AWS KMS keys
scoped per trust zone.
- **Layer signing on top of A2A for
cross-boundary traffic:** For agents on AgentCore
Runtime using A2A, add message-level signing for
communications that cross trust boundaries on top of the
protocol's built-in authentication.
- **Route through
PrivateLink:** Configure AWS PrivateLink for
inter-agent service communications to keep traffic on
private network endpoints.
- **Manage keys and alert on
anomalies:** Store signing key ARNs in Parameter
Store, a capability of AWS Systems Manager, configure
automatic key rotation in AWS KMS, and set Amazon CloudWatch
alarms for key usage anomalies.

## Resources

**Related best practices:**

- [AGENTSEC03-BP01
Implement strong authentication for agent identities](agentsec03-bp01.html)
- [AGENTSEC06-BP02
Implement workflow orchestration security controls](agentsec06-bp02.html)
- [AGENTSEC06-BP03
Establish trust boundaries between agents](agentsec06-bp03.html)

**Related documents:**

- [Introducing
agent-to-agent protocol support in Amazon Bedrock AgentCore
Runtime](https://aws.amazon.com/blogs/machine-learning/introducing-agent-to-agent-protocol-support-in-amazon-bedrock-agentcore-runtime/)
- [Digital
signing with the new asymmetric keys feature of AWS KMS](https://aws.amazon.com/blogs/security/digital-signing-asymmetric-keys-aws-kms/)
- [Code
signing using ACM Private CA and AWS KMS asymmetric
keys](https://aws.amazon.com/blogs/security/code-signing-aws-certificate-manager-private-ca-aws-key-management-service-asymmetric-keys/)
- [AWS KMS documentation](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html)
- [Amazon SQS security best practices](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-security-best-practices.html)

**Related services:**

- [AWS Key Management Service](https://aws.amazon.com/kms/)
- [Amazon SQS](https://aws.amazon.com/sqs/)
- [AWS Systems Manager](https://aws.amazon.com/systems-manager/)
- [AWS PrivateLink](https://aws.amazon.com/privatelink/)
- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsec06-bp01.html*

---

# AGENTSEC06-BP02 Implement workflow orchestration security controls

The orchestration layer is where a single weak check cascades into a
system-wide failure. Access controls on state machines, input
validation on transitions, and circuit breakers on agent tasks keep
multi-agent workflows on approved execution paths instead of
unexpected ones.

**Desired outcome:**

- The workflow orchestration layer enforces strict access controls
that help prevent unauthorized modification of workflow
definitions or execution state.
- State machine validation helps keep workflows on expected
execution patterns, and circuit breakers are designed to stop
failures in one agent from cascading through the entire
workflow.
- You log all workflow executions with enough detail to
reconstruct the execution path for security investigations.

**Common anti-patterns:**

- Granting broad IAM permissions to start, stop, or modify Step
Functions workflows without restricting access to specific state
machines, letting any principal with workflow permissions modify
or trigger any workflow in the account.
- Not implementing input validation in state machine definitions,
letting crafted input payloads direct workflows into unexpected
execution paths.
- Failing to implement circuit breakers, so a single failing agent
cascades failures through the entire workflow with no automatic
mechanism to stop retrying a broken step.
- Using overly permissive retry configurations, letting an agent
repeatedly attempt the same operation before any circuit breaker
triggers and potentially amplifying the original issue.

**Benefits of establishing this best
practice:**

- State validation and input schema enforcement keep workflows
within defined boundaries.
- Circuit breakers automatically stop cascading failures and route
affected executions to quarantine paths for investigation.
- AWS Step Functions logging captures every state transition,
input, output, and error event for full execution
reconstructability.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Two orchestration patterns are in scope here. AWS Step Functions
state machines handle deterministic workflows where the execution
path is defined in JSON and the orchestrator enforces sequencing.
[Amazon
Bedrock AgentCore Runtime](https://aws.amazon.com/blogs/machine-learning/introducing-agent-to-agent-protocol-support-in-amazon-bedrock-agentcore-runtime/) with the A2A protocol handles
agent-delegated workflows where an orchestrator agent dynamically
decides which sub-agents to invoke. Most of the controls below
apply to both, and the differences are called out inline.

Start with IAM. Configure policies for AWS Step Functions that
restrict workflow start, stop, and modification permissions to
specific principals and state machines, use resource-based
policies on state machine definitions to help prevent unauthorized
modification, and implement IAM Conditions that restrict execution
to approved input schemas. Manage state machine definitions as
infrastructure as code through AWS CloudFormation or AWS CDK,
which helps prevent informal modifications and provides
version-controlled change history.

Input validation belongs inside the state machine definition, not
outside it. With Step Functions' built-in JSONPath filtering and
AWS Lambda validation functions, you can validate that workflow
inputs conform to expected schemas before passing them to agent
tasks, rejecting inputs that deviate from expected patterns. Step
Functions' error handling catches and logs validation failures
without exposing error details to callers.

Circuit breakers use Step Functions' error handling and retry
logic. Set conservative retry limits with exponential backoff for
agent task failures, and implement catch states that route failed
executions to a quarantine path rather than retrying indefinitely.
Amazon EventBridge emits circuit breaker events when failure
thresholds are exceeded, triggering alerts and automated
remediation. For multi-agent workflows using the A2A protocol on
AgentCore Runtime, the structured request lifecycle (agent card
discovery, task delegation, result collection) provides natural
points to validate inputs, check authorization, and apply circuit
breaker logic before proceeding.

Execution logging makes the orchestration auditable. Enable Step
Functions execution logging to Amazon CloudWatch Logs at the ALL
level to capture all state transitions, input/output data, and
error events. Configure log retention policies aligned with
compliance requirements and create Amazon CloudWatch Logs Insights
queries for common investigation scenarios such as identifying
workflows that took unexpected execution paths or triggered
circuit breakers.

### Implementation steps

- **Scope Step Functions IAM to specific
state machines:** Configure IAM policies with
least-privilege access scoped to specific state machines and
execution operations.
- **Manage state machines as
IaC:** Use AWS CloudFormation or AWS CDK for state
machine definitions to help prevent unauthorized
modifications and keep version history.
- **Validate inputs inside state
machines:** Implement input validation in state
machine definitions using JSONPath filtering and AWS Lambda
validation functions, rejecting inputs that deviate from
expected schemas.
- **Configure circuit breakers with
catch states:** Set conservative retry limits and
implement catch states that route failures to quarantine
paths rather than retrying indefinitely.
- **Log every execution at the ALL
level:** Enable Step Functions execution logging to
Amazon CloudWatch Logs at the ALL level with retention
policies aligned to compliance requirements.
- **Alarm on circuit breaker
events:** Create Amazon CloudWatch alarms for
circuit breaker triggers and Amazon EventBridge rules to
route workflow security events to the monitoring pipeline.

## Resources

**Related best practices:**

- [AGENTSEC04-BP02
Human-in-the-loop for critical decisions](agentsec04-bp02.html)
- [AGENTSEC06-BP01 Encrypt
and sign inter-agent messages](agentsec06-bp01.html)
- [AGENTSEC06-BP03
Establish trust boundaries between agents](agentsec06-bp03.html)
- [AGENTREL07-BP01
Design workflows in stages with incremental recovery](agentrel07-bp01.html)
- [AGENTREL07-BP02
Enable automatic recovery from agent execution failures](agentrel07-bp02.html)

**Related documents:**

- [AWS Step Functions security documentation](https://docs.aws.amazon.com/step-functions/latest/dg/security.html)
- [Step
Functions error handling](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-error-handling.html)
- [Using
the circuit breaker pattern with Step Functions and
DynamoDB](https://aws.amazon.com/blogs/compute/using-the-circuit-breaker-pattern-with-aws-step-functions-and-amazon-dynamodb/)
- [AWS Prescriptive Guidance: Circuit breaker pattern](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/circuit-breaker.html)
- [Introducing
agent-to-agent protocol support in Amazon Bedrock AgentCore
Runtime](https://aws.amazon.com/blogs/machine-learning/introducing-agent-to-agent-protocol-support-in-amazon-bedrock-agentcore-runtime/)

**Related services:**

- [AWS Step Functions](https://aws.amazon.com/step-functions/)
- [AWS Identity and Access Management](https://aws.amazon.com/iam/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
- [Amazon EventBridge](https://aws.amazon.com/eventbridge/)
- [AWS CloudFormation](https://aws.amazon.com/cloudformation/)
- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsec06-bp02.html*

---

# AGENTSEC06-BP03 Establish trust boundaries between agents

A flat agent network gives every affected agent a direct path to
every other one. Trust zones segmented at the network and IAM
layers, with application-layer verification of caller identity, stop
one affected agent from escalating across the whole system.

**Desired outcome:**

- Agents operate within clearly defined trust zones, accepting
instructions only from authorized coordinators and rejecting
requests from agents outside their trust boundary.
- Network segmentation enforces trust boundaries at the
infrastructure layer and IAM policies enforce them at the API
layer.
- An affected agent in one trust zone can't directly issue
instructions to agents in higher-trust zones without passing
through authorization controls.

**Common anti-patterns:**

- Deploying all agents in a flat network without segmentation,
letting any agent communicate directly with any other regardless
of trust level so an issue spreads laterally.
- Relying on network-level trust boundaries alone without
application-layer authorization, so any agent that reaches
another agent's endpoint can issue instructions.
- Not validating the identity of the coordinator agent before
executing instructions, letting any agent impersonate a
coordinator and issue unauthorized commands.
- Treating all internal agents as implicitly trusted while
implementing trust boundaries only for external-facing agents,
producing a flat internal trust model that amplifies the impact
of any internal issue.

**Benefits of establishing this best
practice:**

- Trust zone segmentation contains the impact of an affected agent
to its own trust zone, helping prevent lateral movement.
- Layered enforcement at both the network level (VPC segmentation,
security groups) and the application level (IAM policies, agent
identity validation) provides defense-in-depth.
- Documented trust architecture supports automated compliance
checks that catch drift as configurations evolve.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Trust boundary controls apply regardless of the inter-agent
protocol used, whether A2A, MCP, or custom REST. The network-layer
controls (VPC segmentation, security groups, AWS PrivateLink) and
IAM-layer controls (resource-based policies, IAM Conditions)
enforce boundaries independent of the application protocol.
Protocol-specific guidance applies on top of these common
controls.

A trust zone architecture starts with tiers that reflect actual
risk: public, internal operational, privileged. Enforce the tiers
at the network with separate Amazon VPCs or VPC security groups,
and use Amazon VPC peering or AWS Transit Gateway with route table
controls to restrict inter-zone communication to only the required
paths. Network segmentation alone doesn't verify the caller's
identity, so pair it with application-layer authorization.

[Amazon
Bedrock AgentCore Runtime](https://aws.amazon.com/blogs/machine-learning/introducing-agent-to-agent-protocol-support-in-amazon-bedrock-agentcore-runtime/) A2A protocol support provides a
structured framework for inter-agent communication with built-in
session isolation and authentication. When agents discover peers
through A2A agent cards, the card schema advertises the agent's
capabilities and authentication requirements. Configure agents to
accept A2A connections only from coordinators whose agent cards
match the expected identity and trust level. For agents not using
A2A, Amazon API Gateway with AWS Lambda authorizers implements
custom agent-to-agent authorization logic that validates agent
identity tokens and enforces trust level requirements.

Resource-based policies on agent endpoints explicitly list the IAM
principals authorized to invoke each agent. IAM Conditions
restrict invocations to agents within the same trust zone or to
specific coordinator agent roles. AWS PrivateLink keeps cross-zone
agent communications on private network paths.
[Policy
in Amazon Bedrock AgentCore](https://aws.amazon.com/blogs/machine-learning/secure-ai-agents-with-policy-in-amazon-bedrock-agentcore/) reinforces trust boundaries at
the tool layer: Cedar policies can include conditions on the
calling principal's identity and trust level, so even if an agent
can reach another agent's tools through the gateway, the policy
engine blocks tool calls that violate trust zone rules.

Compliance validation detects drift from the intended network
posture. AWS Config managed rules,
vpc-sg-open-only-to-authorized-ports for
unintended public ingress, restricted-ssh for
SSH access from 0.0.0.0/0,
vpc-sg-port-restriction-check for port-level
restrictions, cover baseline network hygiene. Trust-zone-specific
validation (that security group rules reference only CIDR ranges
or security group IDs from the same trust zone) needs custom AWS Config rules backed by AWS Lambda, and alarms fire on any
configuration change that would create unauthorized cross-zone
connectivity.

### Implementation steps

- **Design trust zone tiers:**
Define tiers (public, internal operational, privileged) and
document the authorized communication paths between zones.
- **Segment at the network
layer:** Create separate Amazon VPCs or security
groups for each trust zone and configure network controls
(VPC peering, AWS Transit Gateway route tables) to enforce
zone boundaries.
- **Enforce identity at the application
layer:** For agents on
[Amazon
Bedrock AgentCore Runtime](https://aws.amazon.com/blogs/machine-learning/introducing-agent-to-agent-protocol-support-in-amazon-bedrock-agentcore-runtime/), configure A2A agent card
discovery with authentication requirements that enforce
trust-level validation. For agents not on AgentCore Runtime,
use Amazon API Gateway with AWS Lambda authorizers for
custom trust boundary enforcement.
- **Apply resource-based IAM
policies:** List only authorized coordinator
principals in each agent endpoint's resource policy, with
IAM Conditions restricting invocations by trust zone.
- **Reinforce at the tool layer with
Policy:** Configure Cedar policies in
[Policy
in Amazon Bedrock AgentCore](https://aws.amazon.com/blogs/machine-learning/secure-ai-agents-with-policy-in-amazon-bedrock-agentcore/) with conditions on
calling principal identity and trust level.
- **Keep cross-zone traffic
private:** Implement AWS PrivateLink for cross-zone
agent communications.
- **Validate configurations
continually:** Deploy AWS Config managed rules
(vpc-sg-open-only-to-authorized-ports,
restricted-ssh,
vpc-sg-port-restriction-check) for
baseline hygiene and custom AWS Config rules for
trust-zone-specific validation, alarming on any change that
would create unauthorized cross-zone connectivity.

## Resources

**Related best practices:**

- [AGENTSEC03-BP03
Implement least privilege with dynamic boundaries](agentsec03-bp03.html)
- [AGENTSEC06-BP01 Encrypt
and sign inter-agent messages](agentsec06-bp01.html)
- [AGENTSEC06-BP02
Implement workflow orchestration security controls](agentsec06-bp02.html)

**Related documents:**

- [Introducing
agent-to-agent protocol support in Amazon Bedrock AgentCore
Runtime](https://aws.amazon.com/blogs/machine-learning/introducing-agent-to-agent-protocol-support-in-amazon-bedrock-agentcore-runtime/)
- [Secure
AI agents with Policy in Amazon Bedrock AgentCore](https://aws.amazon.com/blogs/machine-learning/secure-ai-agents-with-policy-in-amazon-bedrock-agentcore/)
- [AWS VPC security best practices](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-best-practices.html)
- [AWS Config managed rules reference](https://docs.aws.amazon.com/config/latest/developerguide/managed-rules-by-aws-config.html)
- [AWS Config custom rules with Lambda](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_develop-rules_lambda-functions.html)
- [Security
reference architecture for generative AI](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-generative-ai/gen-ai-sra.html)

**Related services:**

- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [AWS Identity and Access Management](https://aws.amazon.com/iam/)
- [Amazon VPC](https://aws.amazon.com/vpc/)
- [Amazon API Gateway](https://aws.amazon.com/api-gateway/)
- [AWS PrivateLink](https://aws.amazon.com/privatelink/)
- [AWS Config](https://aws.amazon.com/config/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsec06-bp03.html*

---

# AGENTSEC06-BP04 Monitor and detect coordination anomalies

Distributed tracing tells you what happened on one request.
Coordination monitoring tells you when many requests start behaving
differently from the baseline. Tracking inter-agent message rates,
workflow frequencies, and topology changes against established
baselines catches issues through their observable impact on
coordination before they escalate into security events.

**Desired outcome:**

- You detect anomalous coordination patterns such as unexpected
agent communication paths, unusual interaction frequencies, or
coordination latency spikes in near real time and trigger alerts
for investigation.
- You establish baseline coordination profiles for each agent
workflow, so statistical anomaly detection catches deviations
before they cause significant impact.

**Common anti-patterns:**

- Monitoring only infrastructure metrics (CPU, memory, and
network) without tracking agent-specific coordination metrics,
missing the coordination-level signals most indicative of
multi-agent issues.
- Not establishing coordination baselines before deploying anomaly
detection, which produces either excessive false positives or
missed detections.
- Treating Amazon GuardDuty findings and agent coordination logs
as separate data streams, leaving investigators without the
multi-agent context that turns API-level anomalies into useful
signal.

**Benefits of establishing this best
practice:**

- Behavioral baselines catch coordination deviations before they
propagate across the multi-agent system.
- Service maps compare observed communication paths against the
expected trust boundary architecture, validating topology
continually.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Distributed tracing (AGENTSEC05-BP02) reconstructs what happened
during a specific request. Coordination anomaly detection is a
different problem. It is a proactive early-warning system that
watches whether coordination patterns across many requests over
time are drifting from the baseline. Tracing is reactive and
investigation-focused. Coordination monitoring is preventive and
baseline-focused.

Start by defining coordination metrics for each multi-agent
workflow:

- Inter-agent message rates
- Workflow execution frequencies
- Agent response latencies
- Error rates per agent pair
- Coordination graph topology changes

Publish these as Amazon CloudWatch custom metrics, establish
baselines by collecting them during normal operation, and
configure Amazon CloudWatch anomaly detection to automatically
identify statistical deviations.

[Amazon
Bedrock AgentCore Observability](https://aws.amazon.com/blogs/machine-learning/build-trustworthy-ai-agents-with-amazon-bedrock-agentcore-observability/) provides the foundation.
The session, trace, and span hierarchy captures inter-agent
interactions, and the default metrics on the Amazon CloudWatch
generative AI observability page surface session-level patterns.
For agents using the A2A protocol on AgentCore Runtime, the
structured request lifecycle (agent card discovery, task
delegation, result collection) generates observable events at each
coordination step, which you can use to build coordination
topology maps and detect when agents communicate outside their
expected patterns.

[Amazon
Bedrock AgentCore Evaluations](https://aws.amazon.com/blogs/aws/amazon-bedrock-agentcore-adds-quality-evaluations-and-policy-controls-for-deploying-trusted-ai-agents/) complements coordination
monitoring by continually scoring agent behavior on tool selection
accuracy, correctness, and other quality dimensions. If a
coordinating agent starts selecting unexpected tools or producing
incorrect outputs, evaluation-score drops can serve as an early
warning signal before the coordination anomaly becomes visible at
the workflow level. Amazon CloudWatch alarms on evaluation scores
layered with coordination metrics give you a two-stage detection
approach.

Amazon GuardDuty monitors API call patterns for all agent IAM
roles. Its machine learning models detect unusual call patterns:
an agent suddenly calling services it has never accessed before,
or calling APIs at unusual times or from unexpected locations.
Integrate GuardDuty findings with AWS Security Hub CSPM for centralized
prioritization, and correlate them with agent coordination logs to
connect API-level anomalies to specific multi-agent workflows.
Amazon CloudWatch Logs Insights queries add another layer,
analyzing agent coordination logs for patterns such as agents
receiving instructions from unexpected sources, coordination loops
that may indicate runaway behavior, and agents attempting to
access resources outside their defined scope. Schedule these
queries to run periodically and publish results to a security
dashboard.

### Implementation steps

- **Define and publish coordination
metrics:** Capture inter-agent message rates,
execution frequencies, response latencies, and error rates
per agent pair through Amazon CloudWatch custom metrics for
each multi-agent workflow.
- **Establish baselines and enable
anomaly detection:** Collect metrics during normal
operation and configure Amazon CloudWatch anomaly detection
on key metrics.
- **Build topology maps:** Use
[Amazon
Bedrock AgentCore Observability](https://aws.amazon.com/blogs/machine-learning/build-trustworthy-ai-agents-with-amazon-bedrock-agentcore-observability/) service maps and A2A
request lifecycle events to build coordination topology
maps, and alert on unexpected topology changes that deviate
from the documented trust boundary architecture.
- **Layer evaluations as early
warning:** Deploy
[Amazon
Bedrock AgentCore Evaluations](https://aws.amazon.com/blogs/aws/amazon-bedrock-agentcore-adds-quality-evaluations-and-policy-controls-for-deploying-trusted-ai-agents/) to continually score
agent behavior, and configure Amazon CloudWatch alarms on
evaluation scores as an early-warning layer for coordination
issues.
- **Correlate GuardDuty with
coordination logs:** Enable Amazon GuardDuty for
all agent accounts, integrate findings with AWS Security Hub CSPM, and create correlation rules that connect API anomalies
to specific agent coordination logs.
- **Run Logs Insights queries on a
schedule:** Build Amazon CloudWatch Logs Insights
queries for coordination security event patterns and publish
results to a security dashboard on a scheduled cadence.
- **Document the response
runbook:** Establish an incident response runbook
for coordination anomaly alerts that defines investigation
steps, escalation paths, and remediation actions.

## Resources

**Related best practices:**

- [AGENTSEC06-BP01 Encrypt
and sign inter-agent messages](agentsec06-bp01.html)
- [AGENTSEC06-BP03
Establish trust boundaries between agents](agentsec06-bp03.html)
- [AGENTSEC07-BP04
Behavioral anomaly detection and agent containment](agentsec07-bp04.html)
- [AGENTREL02-BP03
Implement behavioral anomaly detection and monitoring](agentrel02-bp03.html)

**Related documents:**

- [Build
trustworthy AI agents with Amazon Bedrock AgentCore
Observability](https://aws.amazon.com/blogs/machine-learning/build-trustworthy-ai-agents-with-amazon-bedrock-agentcore-observability/)
- [Amazon
Bedrock AgentCore adds quality evaluations and policy
controls](https://aws.amazon.com/blogs/aws/amazon-bedrock-agentcore-adds-quality-evaluations-and-policy-controls-for-deploying-trusted-ai-agents/)
- [Amazon GuardDuty documentation](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html)
- [Amazon CloudWatch anomaly detection](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.html)

**Related services:**

- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
- [Amazon GuardDuty](https://aws.amazon.com/guardduty/)
- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [AWS Security Hub CSPM](https://aws.amazon.com/security-hub/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsec06-bp04.html*

---

# AGENTSEC07 — Human oversight protection and agent containment

**Pillar**: Security  
**Best Practices**: 5

---

# AGENTSEC07-BP01 Implement cognitive load management

A human reviewer is only as effective as the workload lets them be.
Prioritization, queue management, and maximum review rates keep
human oversight grounded in genuine judgment rather than
fatigue-driven rubber-stamping.

**Desired outcome:**

- Human reviewers receive a manageable volume of well-prioritized
decisions, with sufficient context and time to make informed
judgments.
- You monitor review queues for backlog accumulation, with
automatic escalation or load balancing helping prevent any
single reviewer from being overwhelmed.
- Review quality metrics detect signs of rubber-stamping that
indicate cognitive overload.

**Common anti-patterns:**

- Routing all agent decisions requiring review to a single queue
without prioritization, so high-priority security decisions wait
behind routine approvals.
- Not monitoring reviewer workload or queue depth, letting
backlogs accumulate silently until reviewers begin approving
without adequate evaluation.
- Setting no maximum review rate per person, so a single reviewer
can be assigned an unlimited number of decisions in a short
period.

**Benefits of establishing this best
practice:**

- Workload management keeps reviewers in a position to make
genuine, informed decisions rather than rubber-stamping under
pressure.
- Review quality metrics (average review time, approval rate)
surface when the oversight process is breaking down, enabling
intervention before it fails silently.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Amazon SQS standard queues don't support priority ordering
natively, so the prioritization layer has to sit above the queue.
A coarse-grained option is separate Amazon SQS queues per priority
tier (high, medium, low), where the assignment function polls
high-priority first and falls back to lower tiers only when the
upper one is empty. A more flexible option uses a single ingest
queue consumed by an AWS Lambda function that classifies each
request by priority and writes it to an Amazon DynamoDB table with
a sort key based on priority and submission time. The reviewer
assignment function queries DynamoDB for the highest-priority
unassigned items, marks them as assigned, and delivers them to the
reviewer. The DynamoDB pattern gives you full control over
prioritization logic, supports re-prioritization of pending items,
and keeps a durable record of all review requests regardless of
their current state. Items that are not immediately assigned stay
in DynamoDB rather than sitting in a queue with an expiring
visibility timeout.

Priority classification is about potential impact of the action
proceeding incorrectly: the more damaging a mistaken approval
would be, the higher the priority. Concrete factors include data
sensitivity (PII, financial records, healthcare information),
reversibility (deletes, external communications, and financial
transactions can't be undone), whether the action is a first-time
operation for this agent (no behavioral baseline, so reviewers
can't pattern-match to shortcut judgment, and the first-time
operation is itself a signal worth investigating), and time
sensitivity (operations that become harder to reverse over time,
or where delay has its own cost). Automate the classification by
tagging review requests with metadata from the agent's tool
invocation context, data classification tags on target resources,
and the agent's historical usage patterns.

Amazon CloudWatch watches the DynamoDB review table for backlog
accumulation (unassigned items by priority tier), average
time-to-assignment, and average time-to-decision. Alarms fire on
high-priority items remaining unassigned beyond defined
thresholds.

Reviewer load balancing distributes decisions across available
reviewers based on current workload. Amazon DynamoDB tracks
reviewer assignment counts and availability, and an AWS Lambda-based assignment function routes new decisions to the
reviewer with the lowest current load. Configure maximum
assignment limits per reviewer per time window to help prevent
overload.

Review quality metrics are the trailing indicator. Track average
review time, approval rate, and decision reversal rate (cases
where a second reviewer overrides the first), publish the metrics
to Amazon CloudWatch, and alarm on patterns that suggest
rubber-stamping: unusually short review times or abnormally high
approval rates during periods of high queue volume. Automatic
escalation routes unreviewed decisions past defined time
thresholds to senior reviewers, or triggers a safe default
(typically blocking the operation) to help prevent indefinite
delays.

Approval bounds, how long an approval remains valid, whether it
can be revoked, whether high-risk operations require step-up
re-confirmation, are covered in AGENTSEC04-BP02, which details the
persistent-trust patterns that determine the scope and lifetime of
each approval decision.

### Implementation steps

- **Set up the ingest-classify-store
pipeline:** Use an Amazon SQS ingest queue, an AWS Lambda classifier that assigns priority, and an Amazon DynamoDB review table with a sort key on priority and
submission time.
- **Build the reviewer assignment
function:** Query the DynamoDB table for the
highest-priority unassigned items, mark them as assigned,
and deliver them to the appropriate reviewer.
- **Cap assignments per reviewer and
escalate:** Set maximum review assignment limits
per reviewer per time window and configure automatic
escalation when limits are reached or high-priority items
age beyond thresholds.
- **Measure review quality:**
Track average review time, approval rate, and reversal rate
in Amazon CloudWatch, and configure alarms on patterns that
suggest rubber-stamping.
- **Monitor the review table:**
Alarm on backlog accumulation by priority tier, average
time-to-assignment, and average time-to-decision, and alert
when high-priority items age beyond thresholds.
- **Review load metrics
periodically:** Use cognitive load metrics to
refine prioritization logic and reviewer capacity planning
on a regular cadence.

## Resources

**Related best practices:**

- [AGENTSEC04-BP02
Human-in-the-loop for critical decisions](agentsec04-bp02.html)
- [AGENTSEC07-BP03 Multiple
reviewers for critical operations](agentsec07-bp03.html)
- [AGENTSEC07-BP04
Behavioral anomaly detection and agent containment](agentsec07-bp04.html)

**Related documents:**

- [Amazon SQS documentation](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html)
- [AWS Step Functions human approval](https://docs.aws.amazon.com/step-functions/latest/dg/tutorial-human-approval.html)
- [Implement
human-in-the-loop confirmation with Amazon Bedrock
Agents](https://aws.amazon.com/blogs/machine-learning/implement-human-in-the-loop-confirmation-with-amazon-bedrock-agents/)

**Related services:**

- [Amazon SQS](https://aws.amazon.com/sqs/)
- [Amazon DynamoDB](https://aws.amazon.com/dynamodb/)
- [AWS Lambda](https://aws.amazon.com/lambda/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
- [Amazon SNS](https://aws.amazon.com/sns/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsec07-bp01.html*

---

# AGENTSEC07-BP02 Clear confidence indicators and manipulation warnings

Workload-managed reviewers still make poor decisions when they lack
the context to evaluate what the agent is recommending. Surfacing
agent confidence, manipulation flags, and historical comparisons
lets reviewers calibrate scrutiny to the actual risk of each
decision.

**Desired outcome:**

- Human reviewers see agent confidence scores, uncertainty
indicators, and manipulation warning flags alongside each
decision, letting them calibrate scrutiny appropriately.
- Historical context and similar past decisions are surfaced so
reviewers can identify when an agent is recommending an action
that deviates from established patterns.

**Common anti-patterns:**

- Presenting agent decisions without confidence scores or
uncertainty indicators, leaving reviewers unable to distinguish
high-confidence recommendations from speculative outputs.
- Not surfacing historical context or similar past decisions, so
every recommendation looks equally plausible without a baseline
of "what normally happens here."
- Displaying confidence scores without explaining their meaning or
limitations, leading reviewers to over-trust high-confidence
outputs without appropriate skepticism.

**Benefits of establishing this best
practice:**

- Confidence scores and historical context help reviewers
calibrate scrutiny to the actual risk of each decision.
- Deviation flags draw reviewer attention to the decisions that
most need it when an agent's recommendation differs from
historical patterns.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Start with what the reviewer is being asked to decide. Two
patterns are common and require different signals. In the
**evaluator pattern**, the agent
recommends an action and the reviewer decides whether the
recommendation is correct. The useful signal is the agent's
confidence in its own output (a low score suggests the
recommendation may be wrong). In the **gate
pattern**, the agent wants to perform a high-risk action
and the reviewer is a policy gate deciding whether the action
should be allowed. The agent's own confidence is less useful
because the agent would not have proposed the action if it thought
it was wrong. For gate-pattern reviews, the useful signal comes
from systems independent of the agent: anomaly detection, policy
checks, and manipulation-warning flags from the input-validation
pipeline.

For evaluator-pattern reviews, configure
[Amazon
Bedrock Guardrails contextual grounding](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-contextual-grounding-check.html) to generate a
grounding score that checks whether the response is supported by
the source material the agent was given. Surface that score
alongside review notifications with plain-language explanations
(for example, "the agent's response isn't well supported by
the source material, and independent verification is
recommended") so reviewers know what the score means rather
than guessing. For gate-pattern reviews, draw from checks
independent of the agent: anomaly detection (AGENTSEC07-BP04)
evaluates whether the action deviates from baseline behavior, and
manipulation-warning flags raised by the input-validation pipeline
(AGENTSEC04-BP01 and AGENTSEC08-BP01) signal when the request
itself looks adversarial.
[Amazon
Bedrock Guardrails automated reasoning](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-automated-reasoning-policy.html) provides a
complementary deterministic check that validates agent outputs
against a formally authored policy (for example, "users in
region X can't perform operation Y"). It is most useful as
context on the reviewer's screen ("this passed policy check
X at Y time") rather than as the primary decision signal,
because actions that pass automated reasoning typically don't need
human gating unless the policy itself is known to have gaps or the
action is irreversible enough to warrant redundant human sign-off.
Surface each signal with the same plain-language framing so the
reviewer knows what each number or flag means.

Historical context makes anomalies visible. Store decisions and
their confidence scores in Amazon DynamoDB for fast retrieval
during review. When a new decision comes up, query DynamoDB for
similar past decisions (same operation type, same agent, similar
parameters) and surface them alongside the current request. Flag
the current decision if its confidence score deviates
significantly from the historical average for that operation type.

[Amazon
Bedrock AgentCore Evaluations](https://aws.amazon.com/blogs/aws/amazon-bedrock-agentcore-adds-quality-evaluations-and-policy-controls-for-deploying-trusted-ai-agents/) adds the quality-trend
signal. Built-in evaluators cover correctness (does the output
match expected answers on a test set), helpfulness, tool-selection
accuracy (does the agent pick the right tool for the task), and
safety. Add custom evaluators for domain-specific criteria: policy
adherence, format conformance (does the output match the schema
downstream systems expect), and goal attainment (did the agent
actually accomplish what the user asked). Prioritize evaluators
that measure things a reviewer could not easily verify themselves
in the time they have during a review. If the reviewer can check
it in ten seconds, it isn't what the evaluator is for. An agent
whose evaluation scores are trending downward is a signal the
reviewer needs to see alongside the specific decision in front of
them.

Amazon Quick dashboards visualize decision patterns and anomalies
over time. These dashboards help reviewers and security teams
identify systemic trends, a particular agent consistently
producing low-confidence outputs for a specific operation type,
for example, that individual decision reviews miss.

### Implementation steps

- **Configure contextual grounding and
automated reasoning:** Generate confidence scores
for agent outputs through
[Amazon
Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html) contextual grounding and automated
reasoning, and include plain-language explanations alongside
numeric scores in review notifications.
- **Store historical decisions for
similarity lookup:** Persist decisions and
confidence scores in Amazon DynamoDB and implement a
similarity query that surfaces past decisions for the same
operation type alongside each new review request.
- **Flag deviations from historical
patterns:** When a confidence score deviates
significantly from the historical average for that operation
type, highlight it for the reviewer.
- **Surface AgentCore Evaluations
trends:** Integrate
[Amazon
Bedrock AgentCore Evaluations](https://aws.amazon.com/blogs/aws/amazon-bedrock-agentcore-adds-quality-evaluations-and-policy-controls-for-deploying-trusted-ai-agents/) quality scores into the
review context so reviewers can see whether overall agent
quality is stable or declining.
- **Build dashboards for systemic
trends:** Create Amazon Quick dashboards that
visualize decision patterns, confidence score distributions,
and anomaly trends over time for security team review.

## Resources

**Related best practices:**

- [AGENTSEC04-BP01
Implement guardrails and alignment controls](agentsec04-bp01.html)
- [AGENTSEC07-BP01
Implement cognitive load management](agentsec07-bp01.html)
- [AGENTSEC07-BP04
Behavioral anomaly detection and agent containment](agentsec07-bp04.html)

**Related documents:**

- [Amazon
Bedrock Guardrails documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html)
- [Amazon
Bedrock AgentCore adds quality evaluations and policy
controls](https://aws.amazon.com/blogs/aws/amazon-bedrock-agentcore-adds-quality-evaluations-and-policy-controls-for-deploying-trusted-ai-agents/)
- [Amazon Quick documentation](https://docs.aws.amazon.com/quicksuite/latest/user/welcome.html)

**Related services:**

- [Amazon
Bedrock Guardrails](https://aws.amazon.com/bedrock/guardrails/)
- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon DynamoDB](https://aws.amazon.com/dynamodb/)
- [Amazon Quick](https://aws.amazon.com/quicksuite/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsec07-bp02.html*

---

# AGENTSEC07-BP03 Multiple reviewers for critical operations

A single reviewer is a single point of failure, both for honest
errors and for social engineering. Independent, blind reviews for
high-risk decisions are the defense-in-depth pattern, well known as
the four-eyes principle, that keeps unilateral approval off the
path.

**Desired outcome:**

- High-risk agent decisions receive independent review from
multiple qualified reviewers, with blind review processes
helping prevent anchoring bias.
- You resolve disagreements through escalation rather than
defaulting to approval.
- You log all review decisions with reviewer identities and
timestamps for audit purposes.

**Common anti-patterns:**

- Showing each reviewer the previous reviewer's decision before
they submit their own, introducing anchoring bias that
undermines independence.
- Defaulting to approval when reviewers disagree, letting a single
approving reviewer effectively override a blocking reviewer.
- Assigning multiple reviews to reviewers from the same team or
reporting chain, reducing the independence of the process.

**Benefits of establishing this best
practice:**

- Multiple independent reviews provide defense-in-depth for human
oversight, removing the single point of failure in the review
process.
- Logged individual reviewer decisions, identities, and timestamps
support compliance and enable investigation of approval
anomalies.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Parallel execution orchestrates multi-reviewer workflows well. AWS Step Functions parallel execution branches send an independent
review request to a different reviewer through Amazon SNS, and the
workflow waits for all branches to complete before evaluating
consensus. Blind review comes from not including previous reviewer
decisions in the notification content, so each reviewer evaluates
the decision independently.

Consensus logic belongs in an AWS Lambda function that evaluates
the collected decisions. Two-reviewer workflows require unanimous
approval. Three or more reviewers use majority rules with
escalation for split decisions, and escalation paths route
disagreements to a senior reviewer with full visibility into
individual decisions and their rationale.

Reviewer selection matters as much as the mechanism. Choose
reviewers from different teams or organizational units to maximize
independence. Reviewers who share a manager or work closely
together tend to reach the same conclusion for social rather than
analytical reasons. AWS IAM Identity Center manages reviewer
identities so assignments are tracked and auditable.

Audit records live in Amazon S3 with reviewer identity, timestamp,
decision (approve or reject), and optional rationale. Tag records
with the associated agent operation ID to enable correlation with
agent execution logs during investigations.

### Implementation steps

- **Orchestrate blind parallel
reviews:** Design multi-reviewer workflows in AWS Step Functions with parallel branches, one per reviewer,
that send independent blind review requests through Amazon SNS.
- **Implement consensus and
escalation:** Evaluate collected decisions in an
AWS Lambda function, unanimous for two-reviewer flows,
majority rules with escalation for three or more.
- **Route split decisions to senior
reviewers:** Configure escalation paths that give
senior reviewers visibility into the individual decisions
and rationale.
- **Select reviewers from different
teams:** Use AWS IAM Identity Center to manage
reviewer identities and track assignments, and draw
reviewers from different organizational units.
- **Persist decisions to S3:**
Store all review decisions in Amazon S3 with reviewer
identity, timestamp, and decision rationale, tagging records
with the agent operation ID for correlation with execution
logs.

## Resources

**Related best practices:**

- [AGENTSEC04-BP02
Human-in-the-loop for critical decisions](agentsec04-bp02.html)
- [AGENTSEC07-BP01
Implement cognitive load management](agentsec07-bp01.html)
- [AGENTSEC07-BP04
Behavioral anomaly detection and agent containment](agentsec07-bp04.html)

**Related documents:**

- [AWS Step Functions parallel states](https://docs.aws.amazon.com/step-functions/latest/dg/amazon-states-language-parallel-state.html)
- [Human
approval in Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/tutorial-human-approval.html)
- [Implement
human-in-the-loop confirmation with Amazon Bedrock
Agents](https://aws.amazon.com/blogs/machine-learning/implement-human-in-the-loop-confirmation-with-amazon-bedrock-agents/)

**Related services:**

- [AWS Step Functions](https://aws.amazon.com/step-functions/)
- [Amazon SNS](https://aws.amazon.com/sns/)
- [Amazon S3](https://aws.amazon.com/s3/)
- [AWS Lambda](https://aws.amazon.com/lambda/)
- [AWS IAM Identity Center](https://aws.amazon.com/iam/identity-center/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsec07-bp03.html*

---

# AGENTSEC07-BP04 Behavioral anomaly detection and agent containment

Detection without containment leaves issues identified but running.
Containment without detection relies on manual observation.
Per-agent baselines paired with automated credential revocation and
forensic capture stop affected agents within minutes while
preserving what investigators need.

**Desired outcome:**

- You establish behavioral baselines per agent and trigger
real-time alerts when deviations cross defined thresholds.
- You automatically isolate agents exhibiting anomalous behavior
within minutes of detection through credential revocation and
circuit breaker activation.
- You capture forensic state before isolation, and manual override
capabilities allow incident responders to quarantine or restore
agents when human judgment is required.

**Common anti-patterns:**

- Monitoring only infrastructure metrics without agent-specific
behavioral indicators, missing signals such as API call
patterns, decision frequencies, and data access volumes.
- Deploying anomaly detection without establishing behavioral
baselines first, producing excessive false positives or missed
detections.
- Relying on manual quarantine processes that require human
intervention, letting an affected agent continue operating for
hours while waiting for human response.
- Implementing quarantine by stopping the agent process without
revoking credentials, so the agent can be restarted with the
same identity and permissions.
- Not preserving agent state and logs before quarantine, losing
forensic evidence from the agent's memory, active sessions, and
pending operations.

**Benefits of establishing this best
practice:**

- Automated credential revocation and circuit breaker activation
isolate affected agents within minutes of detection.
- Forensic preservation through state capture before isolation
provides evidence for investigation without relying on the
agent's own logs.
- Circuit breakers route dependent workflows to safe fallback
paths rather than allowing cascading failures.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Behavioral signals differ by agent type. A RAG agent and a coding
agent have very different normal patterns, so generic thresholds
produce either false alarms or missed detections. Start with the
general categories (API call rate, data access volume, decision
frequency, error rate, resource consumption) but pick the specific
measurements that actually make sense for each agent. A
customer-support agent might track outbound email volume and
cross-customer retrievals, a coding agent might track commit rates
and commands executed, and a data-analysis agent might track query
volume and cross-table joins. Amazon CloudWatch anomaly detection
on the selected metrics establishes dynamic baselines that adapt
to normal variation patterns, reducing false positives compared to
static thresholds, and alarms fire when metrics deviate beyond the
anomaly detection band.

[Amazon
Bedrock AgentCore Evaluations](https://aws.amazon.com/blogs/aws/amazon-bedrock-agentcore-adds-quality-evaluations-and-policy-controls-for-deploying-trusted-ai-agents/) adds a detection layer at the
behavior-quality level. Built-in evaluators (correctness,
tool-selection accuracy, helpfulness, safety) are a starting
point, but custom evaluators capture the quality dimensions that
matter for your agent, whether outputs conform to your
organization's policy, whether the agent is using the expected
tools for its domain, and whether it accomplishes the task it was
assigned. A sudden drop in evaluation scores serves as an
early-warning signal that behavior is drifting before
infrastructure-level anomaly alarms fire. Amazon CloudWatch alarms
on evaluation scores alongside behavioral metrics give you layered
detection.

Two AWS security services add complementary signals you don't need
to instrument yourself. Amazon GuardDuty analyzes AWS CloudTrail,
VPC flow logs, and DNS logs to detect anomalous API call patterns
for IAM roles (unexpected regions, unusual service combinations,
known-malicious IPs), which catches agent behavior CloudWatch
metrics would miss unless you explicitly measured it. Amazon Macie
inspects Amazon S3 objects and access patterns for sensitive-data
exposure (agent-accessed buckets containing unusual volumes of PII
or credentials), which is orthogonal to API-level metrics. AWS Security Hub CSPM centralizes CloudWatch anomaly alarms, GuardDuty, and
Macie findings so one source's anomaly can be correlated with the
others during investigation rather than treated in isolation.

When anomaly detection triggers above a defined severity
threshold, Amazon EventBridge rules invoke either an AWS Lambda
function or an AWS Systems Manager Automation document. Lambda
fits containment logic with custom code paths, external API calls,
or conditional branching that benefits from full programming
flexibility. SSM Automation fits when the containment sequence is
a series of well-defined steps (native step definitions,
parameters, and rollback without code) and you want the same
runbook pattern for automatic and manual containment. Either way,
the sequence runs in this order: capture a forensic snapshot of
the agent's current memory, active sessions, and pending
operations to Amazon S3, then revoke the agent's credentials by
attaching a deny-all policy to its IAM role (preserving the role
for forensic analysis), then broadcast a quarantine event through
Amazon EventBridge to notify dependent workflows to activate their
circuit breaker logic.

Circuit breakers in AWS Step Functions workflows that depend on
quarantinable agents handle the downstream impact. Catch states
detect agent unavailability and route workflow execution to a safe
fallback path rather than failing with an unhandled error. A
manual override interface through AWS Systems Manager Automation
runbooks lets incident responders quarantine or restore agents
through a controlled, auditable process, and multi-person
authorization for restoration helps prevent premature
re-activation.

### Implementation steps

- **Choose agent-specific metrics and
baseline them:** Pick meaningful metrics for each
agent from the general categories, configure Amazon CloudWatch anomaly detection on them, and establish
baselines during normal operation.
- **Add evaluation-based early
warning:** Deploy
[Amazon
Bedrock AgentCore Evaluations](https://aws.amazon.com/blogs/aws/amazon-bedrock-agentcore-adds-quality-evaluations-and-policy-controls-for-deploying-trusted-ai-agents/) with built-in and
custom evaluators, and configure Amazon CloudWatch alarms on
evaluation scores.
- **Centralize security
findings:** Enable Amazon GuardDuty and Amazon Macie for all agent accounts and centralize findings in AWS Security Hub CSPM.
- **Automate containment on threshold
exceedance:** Implement Amazon EventBridge rules
that invoke AWS Lambda or AWS Systems Manager Automation
when anomaly severity exceeds thresholds, and sequence
forensic capture, credential revocation, and quarantine
event broadcast.
- **Wire circuit breakers into dependent
workflows:** Configure catch states in AWS Step Functions workflows that depend on quarantinable agents,
routing to safe fallback paths on agent unavailability.
- **Provide a manual runbook with
multi-person auth:** Create AWS Systems Manager
Automation runbooks for manual quarantine and restoration
with multi-person authorization required for restoration.
- **Test quarterly:** Run
containment procedure tests every quarter to validate
isolation, circuit breakers, and forensic capture.

## Resources

**Related best practices:**

- [AGENTSEC05-BP01
Implement comprehensive logging and decision artifact
storage](agentsec05-bp01.html)
- [AGENTSEC06-BP02
Implement workflow orchestration security controls](agentsec06-bp02.html)
- [AGENTSEC06-BP04
Monitor and detect coordination anomalies](agentsec06-bp04.html)
- [AGENTREL02-BP03
Implement behavioral anomaly detection and monitoring](agentrel02-bp03.html)
- [AGENTREL07-BP02
Enable automatic recovery from agent execution failures](agentrel07-bp02.html)

**Related documents:**

- [Amazon CloudWatch anomaly detection](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.html)
- [Amazon
Bedrock AgentCore adds quality evaluations and policy
controls](https://aws.amazon.com/blogs/aws/amazon-bedrock-agentcore-adds-quality-evaluations-and-policy-controls-for-deploying-trusted-ai-agents/)
- [Amazon GuardDuty documentation](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html)
- [Amazon Macie documentation](https://docs.aws.amazon.com/macie/latest/user/what-is-macie.html)
- [AWS Step Functions error handling](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-error-handling.html)

**Related services:**

- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon GuardDuty](https://aws.amazon.com/guardduty/)
- [Amazon Macie](https://aws.amazon.com/macie/)
- [AWS Security Hub CSPM](https://aws.amazon.com/security-hub/)
- [Amazon EventBridge](https://aws.amazon.com/eventbridge/)
- [AWS Lambda](https://aws.amazon.com/lambda/)
- [AWS Step Functions](https://aws.amazon.com/step-functions/)
- [AWS Systems Manager](https://aws.amazon.com/systems-manager/)
- [AWS Identity and Access Management](https://aws.amazon.com/iam/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsec07-bp04.html*

---

# AGENTSEC07-BP05 Regular security assessments and red teaming

Untested security controls degrade quietly as techniques evolve and
configurations drift. A combination of continuous automated scanning
and periodic human-led red team exercises validates that guardrails,
detection rules, and response procedures still work against current
attacks.

**Desired outcome:**

- You run automated security scanning continuously against agent
deployments (on each deploy and on schedule) and conduct
human-led red team exercises on a regular cadence with scenarios
targeting agent manipulation, including prompt injection, goal
hijacking, and tool misuse.
- You document findings, track them to remediation, and use them
to update security controls and detection rules.

**Common anti-patterns:**

- Conducting generic application security assessments without
agent-specific scenarios, missing prompt injection, memory
poisoning, and multi-agent coordination issues that traditional
testing doesn't cover.
- Performing red team exercises only at initial deployment without
scheduling regular assessments, missing techniques that emerge
as the threat environment evolves.
- Not tracking findings to remediation, letting identified issues
persist so the assessment produces work but no posture
improvement.
- Conducting red team and blue team activities in isolation
without purple team collaboration, limiting the knowledge
transfer that improves detection and response.

**Benefits of establishing this best
practice:**

- Realistic testing confirms guardrails, detection rules, and
response procedures work against current techniques.
- Assessment findings drive updates to guardrail configurations,
permission boundaries, and detection rules in a continuous
feedback loop.
- Purple team activities transfer knowledge from red to blue
teams, improving the organization's ability to detect and
respond to agent-specific issues.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

The assessment cadence needs to match the risk level of each agent
deployment. Automated scanning runs continuously, and manual red
team exercises run on a schedule. For automated agentic testing,
[AWS Security Agent](https://aws.amazon.com/security-agent/) provides on-demand penetration testing that
executes attack chains adapted to the target application, covering
prompt injection, jailbreaking, goal hijacking, and related
patterns (see AGENTSEC09-BP02 for integrating it into broader
penetration testing workflows). Supplement automated testing with
manual exercises that explore novel scenarios specific to your
agent architecture.

Red team scenarios need structure. The
[OWASP
Top 10 for Agentic Applications (2026)](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/) covers agent
manipulation risks specifically, prompt injection, tool misuse,
identity and privilege abuse, and agent behavior hijacking, and
the
[OWASP
Top 10 for LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/) covers model-level risks that
still apply. Build a scenario library that covers multi-agent
coordination issues, memory poisoning, tool misuse, and
human-in-the-loop bypass techniques, and document each scenario
with description, expected detection mechanism, and success
criteria.

[Amazon
Bedrock AgentCore Evaluations](https://aws.amazon.com/blogs/aws/amazon-bedrock-agentcore-adds-quality-evaluations-and-policy-controls-for-deploying-trusted-ai-agents/) supports the assessment
process by providing a continuous quality baseline. Running
evaluations before and after red team exercises measures whether
the exercise exposed quality degradation that the existing
evaluators did not catch, and the results refine custom evaluator
prompts and scoring thresholds.

Durable, versioned storage keeps the historical record intact.
Store scenarios, execution results, and remediation tracking in
Amazon S3 with versioning enabled, or in a dedicated test
management system that maintains change history. Map red team
findings to your compliance control framework so assessment
results produce audit evidence consistent with your regulatory
requirements.

Purple team activities close the loop. Bringing red team and blue
team together to review scenarios and detection responses updates
Amazon CloudWatch alarms, Guardrails configurations, and incident
response runbooks based on observed patterns. Tracking
improvements in detection time and response effectiveness across
cycles demonstrates the program's value.

### Implementation steps

- **Establish an assessment
schedule:** Set a cadence appropriate for each
agent deployment's risk level.
- **Build a scenario library:**
Develop red team scenarios based on the OWASP Top 10 for
Agentic Applications (primary) and the OWASP Top 10 for LLM
Applications (supplementary), covering prompt injection,
memory poisoning, tool misuse, and HITL bypass.
- **Integrate automated agentic
testing:** Deploy agentic AI red teaming tools and
include them in the assessment workflow for automated
coverage of common patterns.
- **Measure quality impact before and
after:** Run
[Amazon
Bedrock AgentCore Evaluations](https://aws.amazon.com/blogs/aws/amazon-bedrock-agentcore-adds-quality-evaluations-and-policy-controls-for-deploying-trusted-ai-agents/) before and after red
team exercises to measure quality impact and refine
evaluator configurations.
- **Persist and map findings:**
Store scenarios, results, and remediation tracking in
durable, versioned storage (Amazon S3 with versioning
enabled), and map findings to your compliance control
framework for audit evidence.
- **Run purple team sessions:**
Update detection rules, guardrail configurations, and
incident response runbooks based on each assessment cycle's
findings.

## Resources

**Related best practices:**

- [AGENTSEC04-BP01
Implement guardrails and alignment controls](agentsec04-bp01.html)
- [AGENTSEC07-BP04
Behavioral anomaly detection and agent containment](agentsec07-bp04.html)
- [AGENTSEC08-BP01
Multi-layer input validation and prompt injection
defense](agentsec08-bp01.html)

**Related documents:**

- [OWASP
Top 10 for Agentic Applications (2026)](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)
- [OWASP
Top 10 for Large Language Model Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
- [AWS Security Agent](https://aws.amazon.com/security-agent/)
- [Responsible
AI in action: How Data Reply red teaming supports generative
AI safety on AWS](https://aws.amazon.com/blogs/machine-learning/responsible-ai-in-action-how-data-reply-red-teaming-supports-generative-ai-safety-on-aws/)
- [Protect
DeepSeek model deployments with Protect AI and Amazon
Bedrock](https://aws.amazon.com/blogs/apn/protect-deepseek-model-deployments-with-protect-ai-and-amazon-bedrock/)
- [Amazon
Bedrock AgentCore adds quality evaluations and policy
controls](https://aws.amazon.com/blogs/aws/amazon-bedrock-agentcore-adds-quality-evaluations-and-policy-controls-for-deploying-trusted-ai-agents/)

**Related services:**

- [Amazon S3](https://aws.amazon.com/s3/)
- [Amazon
Bedrock Guardrails](https://aws.amazon.com/bedrock/guardrails/)
- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsec07-bp05.html*

---

# AGENTSEC08 — Secure agent inputs and outputs

**Pillar**: Security  
**Best Practices**: 2

---

# AGENTSEC08-BP01 Multi-layer input validation and prompt injection defense

Agents take input from many surfaces and only one needs to be
unvalidated for adversarial content to reach the agent's reasoning
process. A layered validation architecture covers every surface, and
in particular catches the indirect prompt injection embedded in
retrieved external content.

**Desired outcome:**

- Every input surface has a validation layer appropriate to its
risk profile, and no input reaches the agent's reasoning process
without passing through at least one validation control.
- You specifically address indirect prompt injection through
retrieved external content, which is the surface most commonly
missed when validation is applied only to direct user inputs.

**Common anti-patterns:**

- Applying input validation only to direct user inputs while
skipping validation for data retrieved from external sources,
letting embedded instructions in web pages, documents, and API
responses bypass user-facing validation.
- Validating at one input surface but not others (for example,
validating user inputs with Guardrails but not validating tool
outputs before they enter the agent's context), creating gaps
that can be targeted.
- Defining denied topics with vague or overly broad descriptions
that generate false positives on legitimate content, eroding
trust and prompting teams to weaken or disable guardrails
entirely.

**Benefits of establishing this best
practice:**

- Defense-in-depth architecture where each input surface has
validation appropriate to its risk profile helps cover every
surface.
- Validation of external content before it enters the agent's
context closes the most commonly missed gap: indirect prompt
injection.
- Confidence-based assessment modes let organizations tune
validation strictness per filter category based on the
likelihood and impact of each risk scenario.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Input surfaces to an agent are not one thing. Direct user
messages, tool outputs, inter-agent messages, retrieved external
content (web pages, documents, API responses), and memory reads
are all paths by which data reaches the agent's context, and each
needs a validation control. Surface-specific guidance lives in
AGENTSEC01-BP02 (memory inputs), AGENTSEC02-BP02 (tool
parameters), and AGENTSEC04-BP01 (goal alignment guardrails). This
best practice is the architectural framing and focuses on the
cross-cutting concern those others don't cover: indirect prompt
injection through external content retrieval.

External content retrieval is the most commonly missed surface.
When an agent uses RAG, web browsing, or API calls to gather
information during task execution, the retrieved content becomes
part of the agent's context, and adversarial instructions embedded
in that content (indirect prompt injection) influence the agent's
behavior as effectively as a direct user injection. Apply
[Amazon
Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html) with prompt attack detection to all
retrieved content before it enters the agent's context, and
implement content source validation that restricts the agent to
retrieving content from approved domains or data sources where
feasible.

Guardrails provides a unified validation mechanism that can be
applied across multiple input surfaces through the ApplyGuardrail
API. Configure a guardrail with prompt attack detection, denied
topics, and word filters once, and apply it at each input
boundary. That gives you consistent policy enforcement across
surfaces with surface-specific tuning through guardrail
versioning.

Two assessment modes matter: block mode returns a binary allow or
deny decision, and detect mode returns confidence scores for each
filter category without blocking the request. Use block mode for
prompt attack detection, where even low-confidence matches warrant
intervention given the severity of potential impact. For content
safety filters on internal or lower-risk applications, detect mode
lets the application make risk-proportionate decisions based on
the confidence scores returned. Score each risk scenario by
likelihood and impact to determine appropriate confidence
thresholds per filter category rather than applying uniform
thresholds.

Denied topics use probabilistic, LLM-based evaluation to determine
whether content matches a topic definition, and definition quality
drives accuracy. Use the full 1,000-character limit for each
denied topic definition with specific and unambiguous
descriptions, and populate all five sample prompt fields (up to
200 characters each) with representative examples that illustrate
the boundary between restricted and permitted content. Vague or
broad definitions inflate false positive rates, which erodes user
trust and pressures teams to weaken or disable guardrails.

When using the ApplyGuardrail API directly (rather than through
the Converse API or Amazon Bedrock Agents), guardrail assessment
results are not automatically published to Amazon CloudWatch. You
are responsible for the telemetry pipeline that captures
assessment outcomes, confidence scores, and blocked content. Set
the outputScope parameter to
full on ApplyGuardrail API calls to receive
complete assessment data including per-filter confidence scores,
which are essential for adjusting thresholds and feeding the
Guardrails Optimizer. Log both the request content and the
assessment response for blocked items, this data is required for
ongoing configuration refinement and false-positive analysis.

The Amazon Bedrock Guardrails Optimizer is a reference
implementation on AWS Samples that automates guardrail
configuration refinement. It uses a Strands Agent to iteratively
adjust denied topic definitions, sample prompts, and filter
thresholds based on annotated test data. As opposed to model
fine-tuning, this is policy configuration optimization. The agent
analyzes failed test cases, rewrites the guardrail configuration,
re-evaluates against the test dataset, and repeats until target
accuracy is reached. Prepare a representative dataset annotated
with expected outcomes (allow or deny for each filter category),
run the Optimizer during initial guardrail setup, and schedule
periodic re-runs (monthly or quarterly) using samples from
production traffic to adapt to evolving content patterns and
reduce false positive rates over time.

### Implementation steps

- **Map input surfaces and assign
controls:** Identify all input surfaces for each
agent and the validation control covering each surface,
flagging any that are currently unvalidated.
- **Validate retrieved external
content:** Configure
[Amazon
Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html) with prompt attack detection and
apply it to external content (RAG results, web content, API
responses) before it enters the agent's context.
- **Pick assessment mode by
risk:** Use block mode for prompt attack detection
filters and consider detect mode for content safety filters
on lower-risk applications, implementing application-level
logic to make risk-proportionate decisions based on returned
confidence scores.
- **Write precise denied
topics:** Use the full 1,000-character limit for
each denied topic definition and populate all five sample
prompt fields with representative examples that illustrate
the boundary between restricted and permitted content.
- **Capture ApplyGuardrail
telemetry:** Set outputScope to
full on all ApplyGuardrail API calls and
implement a telemetry pipeline to capture assessment
outcomes, confidence scores, and blocked content in Amazon CloudWatch.
- **Run the Guardrails
Optimizer:** Run the Amazon Bedrock Guardrails
Optimizer with an annotated test dataset during initial
setup, then schedule periodic re-optimization (monthly or
quarterly) using samples from production traffic.
- **Restrict content sources where
feasible:** Implement content source validation
that restricts agents to retrieving content from approved
domains or data sources.
- **Verify surface-specific controls
exist:** Confirm that the controls described in
AGENTSEC01-BP02 (memory inputs), AGENTSEC02-BP02 (tool
parameters), and AGENTSEC04-BP01 (goal alignment guardrails)
are implemented for each applicable agent.
- **Log and review blocked
inputs:** Log all blocked inputs across surfaces
and review patterns periodically to identify new techniques
and surfaces that may need additional coverage.

## Resources

**Related best practices:**

- [AGENTSEC01-BP02
Validate and sanitize memory inputs](agentsec01-bp02.html)
- [AGENTSEC02-BP02
Validate tool inputs and outputs](agentsec02-bp02.html)
- [AGENTSEC04-BP01
Implement guardrails and alignment controls](agentsec04-bp01.html)
- [AGENTSEC08-BP02 Output
filtering for sensitive information](agentsec08-bp02.html)

**Related documents:**

- [Amazon
Bedrock Guardrails prompt attack detection](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-prompt-attack.html)
- [Amazon
Bedrock Guardrails denied topics](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-denied-topics.html)
- [Amazon
Bedrock Guardrails ApplyGuardrail API reference](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_ApplyGuardrail.html)
- [Build
responsible AI applications with Amazon Bedrock
Guardrails](https://aws.amazon.com/blogs/machine-learning/build-responsible-ai-applications-with-amazon-bedrock-guardrails/)
- [Best
practices with Amazon Bedrock Guardrails filter
configuration](https://aws.amazon.com/blogs/machine-learning/build-safe-generative-ai-applications-like-a-pro-best-practices-with-amazon-bedrock-guardrails/)
- [Amazon
Bedrock AgentCore Memory best practices](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/best-practices.html)

**Related examples:**

- [Amazon
Bedrock Guardrails Evaluation and Optimization
Framework](https://github.com/aws-samples/amazon-bedrock-samples/tree/main/responsible_ai/bedrock-guardrails-optimizer)

**Related services:**

- [Amazon
Bedrock Guardrails](https://aws.amazon.com/bedrock/guardrails/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsec08-bp01.html*

---

# AGENTSEC08-BP02 Output filtering for sensitive information

Filtering user-facing responses leaves internal data paths
(inter-agent messages, memory writes, audit logs) as open channels
for PII and credentials to escape. Scanning every output path with a
data classification policy keeps sensitive content inside the
agent's authorized handling scope.

**Desired outcome:**

- You scan agent outputs for PII, credentials, and other sensitive
data before returning them to users or downstream systems, with
content masked or blocked based on data classification policies.
- Agent outputs containing credentials, private keys, or regulated
PII are blocked or masked before they reach end users or
external systems.
- You log output filtering decisions for compliance auditing.

**Common anti-patterns:**

- Relying on the model to self-censor sensitive information, when
models do generate outputs containing PII or credentials
(especially when that information is in the agent's context from
tool outputs or retrieved documents).
- Applying output filtering only to user-facing responses while
skipping filtering for outputs passed to other agents or stored
in memory, creating data-leakage paths through internal
communications.
- Using overly broad masking rules that mask legitimate content
alongside sensitive data, degrading output quality to the point
users work around the filter.

**Benefits of establishing this best
practice:**

- Data classification enforcement at the agent boundary helps keep
sensitive information within the agent's authorized
data-handling scope regardless of what the model generates.
- Logged filtering decisions support compliance with data
protection regulations.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Every output path is a potential exfiltration path. User-facing
responses are the obvious one, but an agent also writes to memory,
passes content to other agents, and emits logs. Filtering only the
user-facing path leaves the others as open channels for sensitive
data, and adversarial inputs designed to exfiltrate data don't
consistently target the user-facing channel. The architectural
requirement is that every output surface passes through the same
filter, not just the ones users see.

[Amazon
Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-sensitive-info.html) sensitive information filters cover the
data types relevant to most use cases:

- PII categories (names, addresses, phone numbers, email
addresses, SSNs, and financial account numbers)
- Credentials (API keys, passwords, and private keys)
- Custom entity types specific to your organization

Configure the filter action as MASK for most sensitive data types
to preserve output utility while protecting sensitive content, and
BLOCK for the most sensitive categories such as credentials and
private keys where masking isn't enough.

Apply the filter as middleware in the agent output pipeline, so
every output destination, user-facing responses, inter-agent
messages,
[Amazon
Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/best-practices.html) writes through the
create_event API, and audit logs, flows through
it. AgentCore Memory's built-in long-term memory strategies
already filter PII from extracted long-term records by default,
but short-term memory (raw events) retains original content, so
compliance requirements that prohibit PII in any stored form
require applying Guardrails sensitive information filters before
writing events to short-term memory as well.

For organization-specific sensitive data types not covered by
built-in categories, Amazon Comprehend custom entity recognizers
extend coverage. Train recognizers on examples of your sensitive
data types and integrate them into the output filtering pipeline
through AWS Lambda functions that call the Amazon Comprehend API
before returning outputs.

Logging every filtering decision (the type of sensitive data
detected, the action taken (mask or block), the output
destination) produces the data loss prevention report and catches
patterns where the agent is systematically generating outputs
containing sensitive data (a signal of prompt injection or data
exfiltration). Amazon CloudWatch alarms on elevated detection
rates turn that signal into an active alert.

### Implementation steps

- **Configure sensitive information
filters:** Set up
[Amazon
Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-sensitive-info.html) with filters for all relevant PII
and credential categories, choosing MASK or BLOCK per
category based on data classification policy.
- **Filter every output path:**
Apply output filtering as a middleware layer for user-facing
responses, inter-agent messages, memory writes, and audit
logs.
- **Filter before short-term memory
writes when required:** For compliance requirements
that prohibit PII in any stored form, apply Guardrails
filtering before writing events to
[Amazon
Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/best-practices.html) short-term storage.
- **Extend with Amazon Comprehend custom
entities:** Train Amazon Comprehend custom entity
recognizers for organization-specific sensitive data types
and integrate them into the filtering pipeline.
- **Log and alarm on
detections:** Log all output filtering decisions
with data type, action, and destination metadata, and
configure Amazon CloudWatch alarms for elevated sensitive
data detection rates.
- **Review configurations
periodically:** Adjust output filtering to match
evolving data classification policies and new regulated data
types.

## Resources

**Related best practices:**

- [AGENTSEC05-BP01
Implement comprehensive logging and decision artifact
storage](agentsec05-bp01.html)
- [AGENTSEC08-BP01
Multi-layer input validation and prompt injection
defense](agentsec08-bp01.html)

**Related documents:**

- [Amazon
Bedrock Guardrails sensitive information filters](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-sensitive-info.html)
- [Amazon
Bedrock AgentCore Memory best practices](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/best-practices.html)
- [Amazon Comprehend documentation](https://docs.aws.amazon.com/comprehend/latest/dg/what-is.html)

**Related services:**

- [Amazon
Bedrock Guardrails](https://aws.amazon.com/bedrock/guardrails/)
- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon Comprehend](https://aws.amazon.com/comprehend/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
- [AWS Lambda](https://aws.amazon.com/lambda/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsec08-bp02.html*

---

# AGENTSEC09 — Agent vulnerability scanning and penetration testing

**Pillar**: Security  
**Best Practices**: 5

---

# AGENTSEC09-BP01 Integrate AI-powered vulnerability scanning across the development lifecycle

Pattern-matching scanners find common bugs but miss
context-dependent flaws in agent orchestration, tool interactions,
and authorization chains. AI-powered scanning that reasons about
code and design documents the way a human security researcher does
catches these issues at the phase when remediation is cheapest.

**Desired outcome:**

- Vulnerability scanning is embedded at every phase of the agentic
AI development lifecycle, covering design documents, pull
requests, and deployed applications.
- You review design documents for security risks before code is
written, analyze pull requests for common and agent-specific
vulnerabilities during development, and continually scan
deployed applications for emerging threats.
- Findings carry severity ratings, confidence scores, and
practical remediation guidance so teams can prioritize and fix
issues efficiently.

**Common anti-patterns:**

- Relying on rule-based static analysis that matches known
vulnerability patterns, missing context-dependent issues in
agent orchestration logic, insecure tool parameter handling, or
broken access control in multi-agent delegation chains.
- Performing security scanning only at deployment time rather than
across design and development phases, letting vulnerabilities
accumulate and making late-discovery remediation expensive.
- Treating AI-generated code the same as human-written code for
security review, ignoring the distinct vulnerability patterns AI
coding assistants introduce (hallucinated API calls, insecure
default configurations, and outdated library usage).

**Benefits of establishing this best
practice:**

- Design-phase security reviews identify architectural risks
before code is written, reducing remediation cost and
development delays.
- AI-powered scanning that reasons about application context and
agent behavior catches complex vulnerabilities that
pattern-matching tools miss.
- Automated scanning integrated into CI/CD pipelines scales
security expertise across development teams without creating
bottlenecks.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Pattern matching against known signatures isn't enough for agentic
systems. A SQL injection signature doesn't catch a broken
multi-agent authorization chain, and a missing-input-validation
rule doesn't catch a tool parameter manipulated through a prompt
injection. The scanning that reaches those issues has to reason
about how components interact, trace data flows through the
orchestration layer, and understand what the agent was actually
intended to do. That is the capability AI-powered scanning adds,
and why it is effective on agent-specific flaws.

Deploy scanning across the full lifecycle. At the design phase,
use tools that analyze architecture documents, product
specifications, and technical designs for security risks before
code is written. During development, integrate scanning into code
review workflows to analyze pull requests for both common
vulnerabilities (SQL injection, missing input validation) and
agent-specific issues (insecure tool invocations, insufficient
permission scoping). At deployment, run on-demand scans against
running applications to validate that security controls hold under
realistic conditions.

[AWS Security Agent](https://aws.amazon.com/security-agent/) provides this lifecycle coverage as a single
capability. Security teams define organizational security
requirements once in the AWS Management Console (approved authorization
libraries, logging standards, data access policies), and AWS
Security Agent enforces them throughout development, evaluating
design documents and code against the standards and providing
specific guidance when it detects violations. For code security
reviews, configure AWS Security Agent to monitor repositories and
analyze pull requests so evaluation scales across codebases while
keeping oversight on critical issues.

AI-generated code needs extra scrutiny. AI coding assistants
introduce vulnerability patterns that differ from typical
human-written code (hallucinated API calls, insecure default
configurations, outdated dependency usage), and scanning tools
need to flag these explicitly. Tools like Claude Code Security use
multi-stage verification where findings are re-examined to prove
or disprove results and filter out false positives before they
reach analysts, which reduces noise and lets teams focus on
validated issues.

### Implementation steps

- **Codify security requirements
centrally:** Define organizational security
requirements (approved libraries, logging standards, data
access policies) and configure them in
[AWS Security Agent](https://aws.amazon.com/security-agent/) for automated enforcement across
development teams.
- **Run design-phase reviews:**
Configure AWS Security Agent to analyze architecture
documents and technical specifications before development
begins.
- **Enable PR-level code
review:** Connect AWS Security Agent to your code
repositories to cover both human-written and AI-generated
code on every pull request.
- **Configure multi-stage
verification:** Set up AI-powered scanning with
multi-stage verification to reduce false positives and
assign severity ratings to validated findings.
- **Triage and track to
resolution:** Route validated vulnerabilities to
the appropriate team with remediation guidance, and track
findings through to resolution.

## Resources

**Related best practices:**

- [AGENTSEC07-BP05
Regular security assessments and red teaming](agentsec07-bp05.html)
- [AGENTSEC08-BP01
Multi-layer input validation and prompt injection
defense](agentsec08-bp01.html)
- [AGENTSEC09-BP02 Conduct
context-aware penetration testing with multi-agent attack
simulation](agentsec09-bp02.html)

**Related documents:**

- [AWS Security Agent](https://aws.amazon.com/security-agent/)
- [Security
Considerations for AWS Security Agent and AI assisted
penetration testing](https://docs.aws.amazon.com/securityagent/latest/userguide/security-guidance.html)
- [Claude
Code Security, Making frontier cybersecurity capabilities
available to defenders](https://www.anthropic.com/news/claude-code-security)
- [OWASP
Top 10 for LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/)

**Related services:**

- [Amazon
Bedrock Guardrails](https://aws.amazon.com/bedrock/guardrails/)
- [Amazon CodeGuru Security](https://aws.amazon.com/codeguru/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsec09-bp01.html*

---

# AGENTSEC09-BP02 Conduct context-aware penetration testing with multi-agent attack simulation

Generic scanners miss vulnerabilities that only surface in agent
orchestration, tool parameter construction, and inter-agent
delegation. Context-aware testing driven by specialized attacker
agents that adapt to what the application reveals finds the chained
exploits that static scripts can't reach.

**Desired outcome:**

- You use context-aware, multi-agent attack simulation for
penetration testing that adapts to the specific application
under test.
- The testing system develops deep understanding of the
application's architecture, data flows, and agent interactions,
then executes sophisticated attack chains combining multiple
vulnerability types.
- Findings are validated through actual exploitation, prioritized
by real-world exploitability, and documented with reproducible
attack paths and ready-to-implement fixes.

**Common anti-patterns:**

- Running generic vulnerability scanners against agentic AI
systems without adapting test scenarios to the agent's specific
capabilities and tool integrations, missing tool parameter
injection, memory poisoning, and delegation-chain privilege
escalation.
- Testing individual agent components in isolation without
exercising multi-agent coordination paths, missing trust
boundary violations and cascading failures from a compromised
agent in an orchestration chain.
- Relying on predefined test scripts that don't adapt based on
application responses, missing vulnerabilities that require
dynamic exploration because agentic systems behave differently
based on context and prior interactions.

**Benefits of establishing this best
practice:**

- Context-aware testing adapts to the specific application,
discovering vulnerabilities that static test scripts and generic
scanners miss.
- Actual exploitation validates findings, reducing false positives
and letting teams prioritize based on real risk.
- Specialized agents collaborate on reconnaissance, vulnerability
analysis, exploit validation, and finding prioritization,
identifying chained vulnerabilities that combine information
disclosure with privilege escalation.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Penetration testing that chases agent vulnerabilities has to look
like the attack it is simulating. Attacker agents don't run the
same script on every target. They map the surface, probe for
weaknesses, adapt to responses, and chain findings. Testing tools
need to do the same or they miss exactly the scenarios that matter
most for agentic systems.

A multi-agent penetration testing system orchestrates specialized
security agents collaboratively. The system begins with baseline
scanning to establish coverage, then conducts broad reconnaissance
to map the application surface and identify initial attack
vectors. Building on these findings, it dynamically generates
focused test tasks tailored to the specific application context,
reasoning about discovered endpoints, business logic patterns, and
potential vulnerability chains.

[AWS Security Agent](https://aws.amazon.com/security-agent/) provides on-demand penetration testing with
this multi-agent approach. It deploys specialized AI agents that
develop application context from provided documentation and
credentials, then execute attack chains to identify complex
vulnerabilities conventional tools miss. The architecture includes
agents for attack surface mapping, business logic analysis,
finding validation, and vulnerability prioritization based on
actual exploitability scored using the Common Vulnerability
Scoring System (CVSS). The system performs chained attacks,
combining an information disclosure flaw with privilege escalation
to reach sensitive resources, or chaining insecure direct object
references with authentication bypass, rather than stopping at
single-vulnerability detection.

AWS Security Agent starts with the OWASP Top 10 and then
customizes its approach based on the context it learns from
documents and code. The agent adapts to the responses it receives,
building a custom attack plan for each application. Provide target
URLs, authentication details, source code, and documentation so
the agent can develop deep application understanding before
testing begins.

Agent-specific scenarios need manual supplementation. Prompt
injection chains across agent boundaries, tool parameter
manipulation, memory poisoning through crafted tool outputs, and
human-in-the-loop bypass techniques all require scenarios that go
beyond the OWASP baseline. Use the findings from AGENTSEC07-BP05
to inform the scenario library.

### Implementation steps

- **Provide application context to the
testing agent:** Configure
[AWS Security Agent](https://aws.amazon.com/security-agent/) with target application details
including URLs, authentication credentials (stored in AWS Secrets Manager), source code, and architecture
documentation.
- **Run tests across the full
surface:** Execute on-demand penetration tests that
exercise agent orchestration endpoints, tool invocation
paths, and multi-agent communication channels.
- **Triage validated findings by
exploitability:** Review findings with reproducible
attack paths, impact analysis, and suggested code fixes, and
prioritize remediation based on CVSS scores and actual
exploitability.
- **Add agent-specific scenarios
manually:** Supplement automated testing with
scenarios targeting prompt injection chains, tool parameter
manipulation, and multi-agent trust boundary violations.
- **Track posture over time:**
Store penetration test results and compare them across test
cycles to measure security posture improvement.

## Resources

**Related best practices:**

- [AGENTSEC07-BP05
Regular security assessments and red teaming](agentsec07-bp05.html)
- [AGENTSEC02-BP02
Validate tool inputs and outputs](agentsec02-bp02.html)
- [AGENTSEC09-BP01
Integrate AI-powered vulnerability scanning across the
development lifecycle](agentsec09-bp01.html)

**Related documents:**

- [Inside
AWS Security Agent: A multi-agent architecture for automated
penetration testing](https://aws.amazon.com/blogs/security/inside-aws-security-agent-a-multi-agent-architecture-for-automated-penetration-testing/)
- [AWS Security Agent FAQs](https://aws.amazon.com/security-agent/faqs/)
- [Security
Considerations for AWS Security Agent and AI assisted
penetration testing](https://docs.aws.amazon.com/securityagent/latest/userguide/security-guidance.html)
- [OWASP
Top 10 for LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/)

**Related services:**

- [AWS Security Agent](https://aws.amazon.com/security-agent/)
- [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsec09-bp02.html*

---

# AGENTSEC09-BP03 Implement continuous security validation with automated remediation

Periodic assessments leave newly deployed agent capabilities exposed
for weeks or months. On-demand validation integrated into the
development pipeline, paired with automated fix suggestions,
compresses the discovery-to-resolution loop from weeks to hours.

**Desired outcome:**

- You run security validation continually or on-demand as part of
the development and deployment pipeline rather than only during
periodic assessment windows.
- Validated findings arrive with ready-to-implement code fixes and
configuration recommendations, so development teams remediate
issues without waiting for security team intervention.
- You track remediation progress automatically, and regression
testing confirms fixes are effective and don't introduce new
vulnerabilities.

**Common anti-patterns:**

- Limiting penetration testing to annual or quarterly cycles,
leaving newly deployed agent capabilities untested for long
periods because agentic systems evolve rapidly with new tool
integrations and capability expansions.
- Delivering vulnerability findings without practical remediation
guidance, creating a bottleneck where development teams wait for
security expertise to understand how to fix issues.
- Treating remediation as separate from discovery, losing context
between the team that identified the issue and the team that
must fix it and leading to incomplete fixes that address
symptoms rather than root causes.

**Benefits of establishing this best
practice:**

- On-demand testing validates security whenever new capabilities
are deployed or significant changes are made, compressing the
exposure window.
- Automated fix suggestions give development teams
ready-to-implement code changes, closing the loop between
discovery and resolution.
- Automated re-testing confirms fixes are effective and don't
introduce new vulnerabilities.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

The value of security validation is proportional to how fast it
runs relative to how fast the application changes. Quarterly
testing against a code base that changes weekly leaves most of the
application untested most of the time, and agentic systems change
faster than traditional applications because new tool integrations
and capability expansions ship continuously. Integrating
validation into CI/CD pipelines so it runs on every significant
change keeps testing coverage aligned with application evolution.

Configure triggers for on-demand testing when new agent
capabilities are added, tool integrations are modified, or
permission boundaries are changed.
[AWS Security Agent](https://aws.amazon.com/security-agent/) transforms penetration testing from a
weeks-long manual process into an on-demand capability that
completes in hours. Each validated finding carries impact
analysis, a reproducible attack path, and a ready-to-implement
code fix, which is what lets development teams remediate without
waiting for specialized security expertise. Security teams define
organizational requirements once and AWS Security Agent validates
them during every design and code review, providing consistent
enforcement at scale.

Remediation tracking monitors fix progress from discovery through
resolution. Store test results and remediation status in a
centralized system, and configure automated regression testing
that re-runs relevant test scenarios after fixes are applied to
confirm effectiveness. Amazon CloudWatch captures the security
validation metrics that matter: time-to-detection,
time-to-remediation, and fix effectiveness rates.

Agentic systems need validation triggers that traditional
applications don't. Trigger security validation whenever agent
system prompts are modified, new tools are registered, permission
scopes are changed, or multi-agent orchestration patterns are
updated. These changes introduce vulnerabilities that are not
caught by standard code-level scanning because they affect agent
behavior at the reasoning and orchestration layer.

### Implementation steps

- **Wire validation into
CI/CD:** Integrate
[AWS Security Agent](https://aws.amazon.com/security-agent/) into CI/CD pipelines with triggers for
on-demand security validation when agent capabilities, tool
integrations, or permission boundaries change.
- **Run code and design review on every
PR:** Configure automated code and design security
reviews that run on every pull request, giving developers
real-time feedback during development.
- **Route findings with fixes to
owners:** Establish a remediation workflow that
routes validated findings with suggested code fixes to the
appropriate development team and tracks progress to
resolution.
- **Re-test after fixes
automatically:** Implement regression testing that
re-runs relevant security test scenarios after fixes are
applied to confirm effectiveness.
- **Measure and improve:**
Monitor security validation metrics (time-to-detection,
time-to-remediation, fix effectiveness) in Amazon CloudWatch
and review trends to identify process improvements.

## Resources

**Related best practices:**

- [AGENTSEC09-BP01
Integrate AI-powered vulnerability scanning across the
development lifecycle](agentsec09-bp01.html)
- [AGENTSEC09-BP02 Conduct
context-aware penetration testing with multi-agent attack
simulation](agentsec09-bp02.html)
- [AGENTSEC07-BP05
Regular security assessments and red teaming](agentsec07-bp05.html)

**Related documents:**

- [AWS Security Agent](https://aws.amazon.com/security-agent/)
- [AWS Security Agent FAQs](https://aws.amazon.com/security-agent/faqs/)
- [Amazon
Bedrock AgentCore adds quality evaluations and policy
controls](https://aws.amazon.com/blogs/aws/amazon-bedrock-agentcore-adds-quality-evaluations-and-policy-controls-for-deploying-trusted-ai-agents/)

**Related services:**

- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
- [AWS CodePipeline](https://aws.amazon.com/codepipeline/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsec09-bp03.html*

---

# AGENTSEC09-BP04 Establish scoped and controlled testing environments for agent security assessments

Penetration testing that runs real exploit attempts against
production agents can trigger tool calls, corrupt memory, or expose
sensitive data. Scoped test environments with dedicated credentials
and isolated agent state let teams run thorough assessments without
risking production impact.

**Desired outcome:**

- You conduct security assessments for agentic AI systems in
controlled environments with clearly defined scope, dedicated
credentials, and isolation from production systems.
- You manage test credentials through secure vaulting services
with automatic rotation, and testing activities are logged in
your account for full auditability.
- The testing environment replicates production agent behavior
closely enough to produce valid findings while containing the
scope of exploit attempts.

**Common anti-patterns:**

- Running penetration tests directly against production agentic
systems without scope controls, risking agents executing tool
calls against production databases, sending messages to real
users, or triggering downstream workflows in response to test
inputs.
- Using shared or long-lived credentials for security testing,
creating credential exposure risk where test credentials could
be captured in logs, test artifacts, or finding reports.
- Not isolating test agent instances from production agent memory
and state, letting test inputs and attack payloads pollute
production agent memory and influence future agent behavior for
real users.

**Benefits of establishing this best
practice:**

- Environment isolation allows thorough security assessment,
including real exploit attempts, without risking production
impact or data corruption.
- Vaulting services limit credential exposure during testing and
support automatic rotation after assessment cycles.
- Test logs stored in your account provide full visibility into
testing activities for compliance and incident investigation.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

An agent under security test is an agent executing exploit
attempts. In production, an agent running an exploit payload will
actually call the tool it was told to call, send the email it was
told to send, and write to the memory it was told to modify. The
containment requirement is therefore structural: the test
environment needs to look enough like production to produce valid
findings, and it needs to be separated enough from production that
exploit attempts can't reach real resources.

Provision dedicated testing environments that replicate the agent
architecture, tool integrations, and data flows of production
while maintaining isolation. Use separate agent instances with
their own memory stores, tool endpoints, and permission
boundaries. Configure test environments to use mock or sandboxed
versions of external services where full production connectivity
isn't required for valid testing results.

Manage test credentials through AWS Secrets Manager, storing
static credentials (username and password) securely and supporting
dynamic credential provisioning through AWS Lambda functions for
more complex authentication scenarios.
[AWS Security Agent](https://aws.amazon.com/security-agent/) supports both static credentials stored in
AWS Secrets Manager and dynamic credentials accessed through AWS Lambda functions, giving flexible authentication that adapts to
different application architectures. Rotate test credentials after
each assessment cycle and audit credential access logs to detect
any unauthorized usage.

Scope definition is a precondition, not an afterthought. Specify
before each assessment which agent endpoints, tool integrations,
and data stores are in scope and which are explicitly excluded.
For AWS Security Agent penetration testing, provide target URLs,
authentication details, source code, and documentation so the
agent can develop application context within the defined scope.
All test logs are stored in Amazon CloudWatch in your account for
full visibility.

For multi-agent systems, test agent-to-agent communication paths
in isolation before testing the full orchestration chain. That
approach identifies trust boundary violations and delegation
issues at the individual interaction level before they compound in
complex multi-agent scenarios. Network segmentation and IAM
policies help prevent test agent instances from reaching
production resources.

### Implementation steps

- **Provision isolated test
environments:** Replicate production agent
architecture with isolated memory stores, tool endpoints,
and permission boundaries.
- **Manage credentials in Secrets Manager:** Store test credentials in AWS Secrets Manager with automatic rotation policies, or use AWS Lambda
functions for dynamic credential provisioning for complex
authentication scenarios.
- **Define and document test
scope:** Specify in-scope agent endpoints, tool
integrations, and data stores for each assessment, with
explicit exclusions for sensitive production resources.
- **Contain the scope at the network and
IAM layers:** Configure network segmentation and
IAM policies that help prevent test agent instances from
accessing production resources.
- **Verify test logging in
CloudWatch:** Confirm all test logs are captured in
Amazon CloudWatch in your account, and review logs after
each assessment to confirm scope adherence and identify
unintended interactions.

## Resources

**Related best practices:**

- [AGENTSEC09-BP02 Conduct
context-aware penetration testing with multi-agent attack
simulation](agentsec09-bp02.html)
- [AGENTSEC03-BP03
Implement least privilege with dynamic boundaries](agentsec03-bp03.html)
- [AGENTSEC07-BP04
Behavioral anomaly detection and agent containment](agentsec07-bp04.html)

**Related documents:**

- [Security
Considerations for AWS Security Agent and AI assisted
penetration testing](https://docs.aws.amazon.com/securityagent/latest/userguide/security-guidance.html)
- [AWS Security Agent FAQs](https://aws.amazon.com/security-agent/faqs/)
- [AWS Secrets Manager documentation](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html)
- [AWS Well-Architected Framework, Security Pillar](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/welcome.html)

**Related services:**

- [AWS Security Agent](https://aws.amazon.com/security-agent/)
- [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/)
- [AWS Lambda](https://aws.amazon.com/lambda/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
- [AWS Identity and Access Management](https://aws.amazon.com/iam/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsec09-bp04.html*

---

# AGENTSEC09-BP05 Implement runtime threat detection, security event correlation, and automated remediation for agents

Scanning finds latent weaknesses. Runtime detection catches the
attacks happening now. Correlating events across agent interaction
surfaces and triggering automated remediation compresses the gap
between an active exploit and the response that contains it.

**Desired outcome:**

- You continually monitor security events from agent activity,
correlate them across interaction surfaces, and analyze them for
multi-step attack sequences.
- You detect active threats targeting agentic systems within
minutes, with critical attack sequences surfaced at the highest
severity.
- Automated remediation workflows trigger containment actions and
generate ready-to-implement fixes, reducing mean time to
detection and mean time to remediation.
- Security teams have a unified view of agent-related threats
alongside findings from vulnerability scanning and penetration
testing.

**Common anti-patterns:**

- Treating agent security events in isolation rather than
correlating them across interaction surfaces, missing multi-step
attack sequences where individual events look benign but
together constitute a coordinated attack.
- Relying on pre-deployment vulnerability scanning alone without
runtime threat detection, leaving a gap where vulnerabilities
introduced through configuration drift, new tool integrations,
or novel attack techniques go undetected until the next
scheduled assessment.
- Generating security alerts without automated remediation
workflows, creating alert fatigue where security teams are
overwhelmed by findings but lack the tooling to act quickly.
- Not correlating penetration testing findings with runtime threat
detection signals, missing the connection between known
vulnerabilities and active exploitation attempts that together
provide a high-confidence remediation prioritization signal.

**Benefits of establishing this best
practice:**

- AI/ML-powered event correlation identifies coordinated attacks
spanning multiple agent interaction surfaces, time periods, and
resources.
- Automated workflows trigger containment actions and generate fix
recommendations when threats are detected, closing the loop
between detection and response.
- Centralized findings from vulnerability scanning, penetration
testing, and runtime threat detection enable risk-based
prioritization across the full threat lifecycle.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Scanning and penetration testing find weaknesses before exploit.
Runtime detection catches the exploit as it happens. Both are
necessary because neither alone is sufficient. An agentic system
adds surface area (tools, APIs, memory stores, other agents) that
is exploited through prompt injection chains, credential misuse,
data exfiltration sequences, and privilege escalation paths.
Detection has to correlate across that surface, not treat each
channel in isolation.

Deploy Amazon GuardDuty across all accounts where agents operate
to provide continuous threat detection for agent IAM roles, API
activity, and data access patterns.
[GuardDuty
Extended Threat Detection](https://aws.amazon.com/blogs/aws/introducing-amazon-guardduty-extended-threat-detection-aiml-attack-sequence-identification-for-enhanced-cloud-security/) correlates security signals to
identify active attack sequences (privilege discovery followed by
API manipulation, persistence activities, and data exfiltration)
and surfaces them as critical-severity attack sequence findings
with natural language summaries, MITRE ATT&CK mapping, and
prescriptive remediation recommendations.

For agent-specific threat detection, configure GuardDuty
monitoring across the data sources most relevant to agentic
workloads:

- AWS CloudTrail management events for API call patterns
- Amazon VPC Flow Logs for network behavior
- DNS logs for command-and-control detection
- Amazon S3 data events for data access monitoring

Enable GuardDuty Runtime Monitoring for compute resources running
agent workloads to detect threats at the operating system level,
including suspicious process execution and network connections.

AWS Security Hub CSPM is the aggregation layer. Findings from Amazon GuardDuty (runtime threats),
[AWS Security Agent](https://aws.amazon.com/security-agent/) (vulnerability scanning and penetration
testing), Amazon Macie (sensitive data exposure), and Amazon Inspector (software vulnerability scanning) normalize into the AWS
Security Finding Format (ASFF) for consistent prioritization and
automated response regardless of source. Security Hub CSPM insights
correlate penetration testing findings with runtime detection
signals, identifying cases where known vulnerabilities are being
actively exploited (a high-confidence prioritization signal).

Amazon EventBridge rules trigger AWS Lambda functions or AWS Step Functions workflows when high-severity findings are generated. For
agent-specific threats, the remediation workflow captures forensic
state (agent memory, active sessions, recent tool invocations) to
Amazon S3, applies containment actions (credential revocation,
network isolation) as described in AGENTSEC07-BP04, generates
remediation recommendations based on the finding type, and creates
tracked remediation tasks. Findings from AWS Security Agent
penetration testing that include suggested code fixes route
directly to development teams through the existing remediation
tracking workflow.

[Amazon
Bedrock AgentCore Evaluations](https://aws.amazon.com/blogs/aws/amazon-bedrock-agentcore-adds-quality-evaluations-and-policy-controls-for-deploying-trusted-ai-agents/) adds a complementary
detection layer. Continuous evaluation scoring detects behavioral
drift that precedes or accompanies security incidents. A sudden
drop in safety or correctness scores combined with a GuardDuty
finding for the same agent is a high-confidence signal that
warrants immediate investigation. Amazon CloudWatch composite
alarms triggered when both evaluation score degradation and a
GuardDuty finding occur within the same time window surface those
cases automatically.

### Implementation steps

- **Enable GuardDuty across agent
accounts:** Turn on Amazon GuardDuty with
monitoring configured for AWS CloudTrail events, Amazon VPC
Flow Logs, DNS logs, Amazon S3 data events, and GuardDuty
Runtime Monitoring for agent compute resources.
- **Centralize findings in Security Hub CSPM:** Aggregate findings from Amazon GuardDuty,
[AWS Security Agent](https://aws.amazon.com/security-agent/), Amazon Macie, and Amazon Inspector in
AWS Security Hub CSPM, and configure Security Hub CSPM insights to
correlate penetration testing findings with runtime threat
detection signals.
- **Automate containment on
high-severity findings:** Use Amazon EventBridge
rules and AWS Lambda functions to trigger containment
actions and generate fix recommendations when high-severity
findings are generated.
- **Combine evaluation drift with
GuardDuty findings:** Configure Amazon CloudWatch
composite alarms that combine
[Amazon
Bedrock AgentCore Evaluations](https://aws.amazon.com/blogs/aws/amazon-bedrock-agentcore-adds-quality-evaluations-and-policy-controls-for-deploying-trusted-ai-agents/) score degradation with
GuardDuty findings to surface high-confidence threat
signals.
- **Route fixes to developers and
measure MTTR:** Route remediation recommendations,
including code fixes from AWS Security Agent, to development
teams through a tracked workflow, and monitor mean time to
detection and mean time to remediation as key security
metrics.
- **Tune detection quarterly:**
Review detection rules, remediation workflows, and finding
correlation logic quarterly based on observed threat
patterns and false positive rates.

## Resources

**Related best practices:**

- [AGENTSEC05-BP01
Implement comprehensive logging and decision artifact
storage](agentsec05-bp01.html)
- [AGENTSEC07-BP04
Behavioral anomaly detection and agent containment](agentsec07-bp04.html)
- [AGENTSEC09-BP01
Integrate AI-powered vulnerability scanning across the
development lifecycle](agentsec09-bp01.html)
- [AGENTSEC09-BP02 Conduct
context-aware penetration testing with multi-agent attack
simulation](agentsec09-bp02.html)

**Related documents:**

- [Amazon GuardDuty Extended Threat Detection](https://aws.amazon.com/blogs/aws/introducing-amazon-guardduty-extended-threat-detection-aiml-attack-sequence-identification-for-enhanced-cloud-security/)
- [Amazon GuardDuty documentation](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html)
- [AWS Security Hub CSPM documentation](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html)
- [Automate
cloud security vulnerability assessment and alerting using
Amazon Bedrock](https://aws.amazon.com/blogs/machine-learning/automate-cloud-security-vulnerability-assessment-and-alerting-using-amazon-bedrock/)
- [How
government agencies can transform cybersecurity operations
with Amazon Bedrock AgentCore](https://aws.amazon.com/blogs/publicsector/how-government-agencies-can-transform-cybersecurity-operations-with-amazon-bedrock-agentcore/)
- [AWS Security Agent](https://aws.amazon.com/security-agent/)

**Related services:**

- [Amazon GuardDuty](https://aws.amazon.com/guardduty/)
- [AWS Security Hub CSPM](https://aws.amazon.com/security-hub/)
- [Amazon EventBridge](https://aws.amazon.com/eventbridge/)
- [AWS Lambda](https://aws.amazon.com/lambda/)
- [AWS Step Functions](https://aws.amazon.com/step-functions/)
- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
- [Amazon Macie](https://aws.amazon.com/macie/)
- [Amazon Inspector](https://aws.amazon.com/inspector/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsec09-bp05.html*

---

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
