# AGENTCOST01 — Reasoning and execution cost optimization

**Pillar**: Cost Optimization  
**Best Practices**: 4

---

# AGENTCOST01-BP01 Use the reflection pattern to design efficient agent reasoning loops

Unbounded reasoning loops consume tokens unpredictably and can result in higher than
expected token consumption for routine tasks. A bounded reflection pattern gives you predictable
token budgets and preserves decision quality.

**Desired outcome:**

- You have explicit termination conditions for every agent: a maximum iteration count, a
confidence threshold, and a per-session token budget.
- You apply reflection selectively, triggering full self-correction only when initial
output quality falls below a threshold.
- You track per-cycle token consumption and decision quality so termination parameters
can be tuned from data rather than guesswork.

**Common anti-patterns:**

- Running agents without iteration limits or cost caps, allowing indefinite token
consumption without progress toward the task.
- Applying expensive reflection and self-correction to every output, regardless of
whether the initial answer was already good.
- Operating without per-cycle token instrumentation, so no one can tell which reasoning
phase drives cost.
- Using fixed iteration counts instead of confidence thresholds, which either wastes
tokens on unnecessary iterations or cuts off complex reasoning prematurely.
- Building reflection patterns without budget guardrails, so unbounded loops consume
tokens before alerts fire.

**Benefits of establishing this best practice:**

- Predictable token consumption through bounded reasoning cycles with explicit
termination conditions.
- Selective reflection preserves decision quality for ambiguous cases while reducing
token waste on straightforward tasks.
- Cost-quality baselines reveal which reasoning patterns deliver the best trade-offs,
enabling data-driven tuning of thresholds.

**Level of risk exposed if this best practice is not established:**
Medium

## Implementation guidance

Every reflection loop assumes that another iteration will improve the answer more than it
costs, which works with ambiguous tasks but often loses value on straightforward ones. Without
that contract, agents reflect on every output regardless of whether reflection improves
quality. The discipline is to emit a structured confidence signal alongside each action,
inspect it in the orchestration layer, and short-circuit the loop when confidence clears a
threshold. Otherwise the loop runs until it hits a hard iteration ceiling, which is both the
slowest and most expensive outcome for the common case.

Enforcement matters as much as the contract. Iteration caps expressed only in the system
prompt can drift past under adversarial inputs or prompt injections. [Amazon Bedrock
AgentCore Policy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html) applies Cedar policies at the [Amazon Bedrock AgentCore
Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) boundary, so iteration and token limits are rejected at the traffic layer
rather than noticed after they're exceeded. [Amazon Bedrock AgentCore
Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html) provides session-isolated execution and consumption-based pricing, so each
session carries its own budget and one runaway session doesn't corrupt accounting for others.

Selective reflection separates ambiguity handling from cheaper routine work. Score the
initial output against a lightweight rubric, a small model or heuristic, and gate full
reflection on that score. Tag reflection outcomes with the task category so you can see where
reflection consistently improves quality and where it adds cost with no benefit. Categories
that never benefit from reflection should have the trigger disabled entirely. [Amazon Bedrock
AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html) supports LLM-as-a-Judge assessment of decision quality, which
gives you an objective confidence signal rather than a self-reported one from the agent being
evaluated.

The plan, execute, verify, and reflect phases within a reflection cycle have different
reasoning intensities. Routing planning and verification to smaller, faster models while
reserving the largest model for execution captures cumulative savings on the frequent low-cost
phases, offsetting the higher per-token cost of the infrequent high-intensity phase.

### Implementation steps

- **Define explicit termination conditions per agent:** Set a
maximum iteration count, a confidence threshold, and a per-session token budget, and
enforce them through [Amazon Bedrock AgentCore
Policy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html) Cedar policies at the AgentCore Gateway boundary so enforcement happens
at the traffic layer rather than in application code.
- **Instrument per-cycle token consumption:** Enable [Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) to capture per-session token counts through
OpenTelemetry, and configure Amazon CloudWatch alarms on anomalous per-cycle patterns.
- **Establish objective confidence thresholds:** Configure
[Amazon Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html) to score decision quality through
LLM-as-a-Judge, and anchor early-termination thresholds to measured quality rather than
self-reported confidence.
- **Gate reflection on initial output quality:** Score each
initial output with a lightweight rubric and trigger the full reflection pass only when
the score falls below a configurable threshold, keeping reflection overhead off the
straightforward cases.
- **Recalibrate thresholds on a cadence:** Review
cost-quality baselines monthly (or quarterly for stable workloads) and adjust confidence
thresholds, iteration limits, and reflection triggers based on the distribution of
observed outcomes.

## Resources

**Related best practices:**

- [AGENTCOST01-BP02 Optimize multi-agent collaboration cost
through efficient handoff patterns](agentcost01-bp02.html)
- [AGENTCOST01-BP03 Implement cost-effective patterns like
hybrid supervisor for multi-agent coordination](agentcost01-bp03.html)
- [AGENTCOST02-BP01 Architect tiered model
selection for cost-performance optimization](agentcost02-bp01.html)
- [AGENTCOST07-BP01 Implement automated cost
controls with intelligent cutoffs](agentcost07-bp01.html)

**Related documents:**

- [Amazon Bedrock
AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html)
- [Amazon Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html)
- [Amazon
Bedrock AgentCore Policy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html)
- [Amazon Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html)
- [Evaluate
models in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation-judge.html)
- [Agentic AI
patterns and workflows on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/introduction.html)
- [Guidance for Cost Analysis and Optimization with Amazon Bedrock Agents](https://aws.amazon.com/solutions/guidance/cost-analysis-and-optimization-with-amazon-bedrock-agents/)

**Related videos:**

- [AWS 2025 - AgentCore
Observability: Monitor and Debug with OpenTelemetry](https://www.youtube.com/watch?v=wWQgawUPr1k)
- [AWS re:Invent 2024 - Balance
cost, performance & reliability for AI at enterprise scale (AIM3304)](https://www.youtube.com/watch?v=Lwvv8Q33eeE)
- [AWS re:Invent 2024 -
Sustainable and cost-efficient generative AI with agentic workflows (AIM333)](https://www.youtube.com/watch?v=tFiDkSG2ess)

**Related examples:**

- [GitHub: awslabs/amazon-bedrock-agentcore-samples - Runtime tutorials](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/01-AgentCore-runtime)

**Related workshops:**

- [Diving Deep into Bedrock AgentCore - Evaluations](https://catalog.workshops.aws/agentcore-deep-dive/en-US/80-agentcore-evaluations)

**Related services:**

- [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentcost01-bp01.html*

---

# AGENTCOST01-BP02 Optimize multi-agent collaboration cost through efficient handoff patterns

In multi-agent systems, the largest hidden cost is redundant context
that travels with every handoff. Structured handoff messages and
shared memory keep coordination cost proportional to task complexity
rather than conversation length.

**Desired outcome:**

- You have handoff messages carrying only the task specification,
relevant facts, and constraints, not full conversation
transcripts.
- You have collaborating agents sharing common context through a
managed memory layer instead of re-transmitting it on every
handoff.
- You track per-handoff and per-workflow coordination costs as
distinct metrics.

**Common anti-patterns:**

- Passing full conversation history in every handoff, causing
input token cost to scale with conversation length regardless of
relevance to the receiving agent.
- Building deep supervisor hierarchies where multi-level nesting
adds orchestration model invocations at each layer, so
coordination cost exceeds execution value.
- Skipping shared memory for collaborating agents, re-transmitting
common facts in every agent's context window and causing linear
cost growth with agent count.
- Running multi-agent workflows without handoff cost tracking,
reducing the risk of identification of workflows where
coordination overhead has grown disproportionate to the
execution work.

**Benefits of establishing this best
practice:**

- Coordination overhead stays proportional to task complexity
rather than conversation length or agent count.
- Shared memory removes redundant context transmission, reducing
per-handoff token cost.
- Per-handoff cost visibility enables data-driven tuning of
multi-agent interaction patterns.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

The most expensive thing an agent can send is context the receiver
already has (or doesn't need). Every handoff that copies the full
conversation across the boundary pays again for information that
never changed. Treat handoff messages as structured summaries
containing the task specification, relevant facts, and constraints
the worker must respect.
[Amazon
Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) enables write-once, read-many
patterns where one agent stores a fact under a session ID and
actor ID, and every collaborator reads it without re-embedding it
in their own prompt.
[Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) adds the corresponding discipline
on the tool side, using MCP-compatible Semantic Tool Selection to
present only tools relevant to the current intent rather than the
full catalog.

Context distillation means that a small model call or a Lambda
function can compress incoming context into the minimum sufficient
information for the next agent's task before the handoff crosses
the boundary. The cost of the distillation call is typically less
than the cost of repeatedly transmitting untrimmed context through
deeper workflows.

Every supervisor-worker layer adds at least one inference for
delegation and one for synthesis. Hierarchies deeper than three
levels compound that overhead quickly, and most deep hierarchies
can be flattened by replacing intermediate supervisors with direct
worker-to-worker communication through the AgentCore Runtime
Agent-to-Agent protocol. The diagnostic metric is the
orchestration-to-execution token ratio. Supervisors should consume
no more than 20% of total workflow tokens, leaving 80% for workers
doing execution. A ratio that drifts above 20% means coordination
has grown disproportionate to work.

Visibility is a prerequisite for these patterns.
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) provides distributed
tracing so agent-to-agent communication costs appear as their own
category rather than hidden inside aggregate workflow cost.
[Amazon
Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html) runs in real time against
live tool-call traces and as offline test suites in CI/CD
pipelines, so redundant or unnecessary invocations are caught
early.

### Implementation steps

- **Design structured handoff
messages:** Replace full conversation history with
a summary object containing the task specification, relevant
facts, and the constraints the receiving agent must respect.
Version the message schema so receivers can reject malformed
handoffs.
- **Insert context distillation at
boundaries:** Add a small-model call or Lambda
function that extracts minimum sufficient context before
each handoff, so input tokens at transitions reflect current
task needs rather than accumulated history.
- **Configure shared memory with
ownership rules:** Provision
[Amazon
Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) accessible to all
collaborating agents, and document which agent owns writes
to each namespace so shared state has a clear provenance.
- **Flatten deep hierarchies:**
Audit multi-agent workflows for supervisor-worker depth
greater than three levels, and replace intermediate
supervisors with direct worker-to-worker communication
through the AgentCore Runtime Agent-to-Agent protocol where
the routing can be made explicit.
- **Expose specialized agents through
Gateway:** Publish agents as tools through
[Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) MCP server capabilities,
and turn on Semantic Tool Selection so collaborating agents
see only tools relevant to the current request.
- **Evaluate tool-call efficiency in CI
and in production:** Run
[Amazon
Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html) against live tool-call
traces to flag inefficient usage at runtime, and against
offline test suites in the CI/CD pipeline to catch
regressions before deployment.
- **Track the orchestration-to-execution
ratio:** Tag every invocation with workflow-id and
agent-role, build CloudWatch dashboards that display the
supervisor-to-worker token ratio per workflow, and configure
AWS Budgets alerts when orchestration overhead exceeds 20%
of total workflow token cost.

## Resources

**Related best practices:**

- [AGENTCOST01-BP01 Use
the reflection pattern to design efficient agent reasoning
loops](agentcost01-bp01.html)
- [AGENTCOST01-BP03
Implement cost-effective patterns like hybrid supervisor for
multi-agent coordination](agentcost01-bp03.html)
- [AGENTCOST01-BP04 Design
agent hierarchies and delegation patterns that reduce
coordination overhead](agentcost01-bp04.html)
- [AGENTCOST05-BP02
Implement distributed cost tracing for multi-agent
workflows](agentcost05-bp02.html)

**Related documents:**

- [Amazon
Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html)
- [Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html)
- [Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html)
- [Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html)
- [Amazon
Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html)
- [Agentic
AI patterns and workflows on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/introduction.html)

**Related videos:**

- [AWS 2025 - AgentCore Deep Dive: Memory](https://www.youtube.com/watch?v=-N4v6-kJgwA)
- [AWS re:Invent 2024 - Balance cost, performance & reliability
for AI at enterprise scale (AIM3304)](https://www.youtube.com/watch?v=Lwvv8Q33eeE)

**Related examples:**

- [GitHub:
awslabs/amazon-bedrock-agentcore-samples - Multi-agent
tutorials](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/01-AgentCore-runtime/03-advanced-concepts)
- [GitHub:
awslabs/amazon-bedrock-agentcore-samples - Evaluations
tutorials](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/07-AgentCore-evaluations)

**Related services:**

- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentcost01-bp02.html*

---

# AGENTCOST01-BP03 Implement cost-effective patterns like hybrid supervisor for multi-agent coordination

Many multi-agent workflows pay for AI reasoning at the coordination
layer for decisions that rules could make at no additional charge.
Matching each orchestration decision to the cheapest mechanism
capable of handling it removes that hidden cost.

**Desired outcome:**

- You select orchestration patterns from workflow determinism
analysis rather than defaulting to AI supervision.
- You have deterministic routing running without model
invocations, and AI supervisors reserved for genuinely ambiguous
cases that need natural language understanding.
- You track orchestration cost separately from worker cost and
maintain documented pattern-selection criteria.

**Common anti-patterns:**

- Using AI supervisors for deterministic workflows, invoking
expensive foundation models for routing decisions that
straightforward rules handle.
- Defaulting to AI supervision without evaluating whether the
routing logic follows explicit rules.
- Tracking only aggregate workflow cost without decomposing
orchestrator compared to worker spend, which hides
disproportionate coordination overhead.

**Benefits of establishing this best
practice:**

- Rule-based routing handles deterministic branches without model
invocations, reducing per-routing-decision cost to near zero.
- Hybrid patterns match each routing decision to the cheapest
capable mechanism.
- Documented pattern-selection criteria help prevent
over-provisioning AI supervision for new workflows.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Workflow determinism is a property, not an assumption. At every
orchestration point, the routing decision is either a selection
across a finite, enumerable set of conditions (task type, output
classification, error code) or a judgment call across an
open-ended input space. The first class costs nothing to route
with rules, and the second requires model reasoning. Most
multi-agent workflows contain both, but teams often pay for AI
supervision across the whole workflow because the pattern defaults
that way. Conducting the determinism analysis up front is the
difference between spending model tokens on routing that a
conditional could handle and spending them only where the input
genuinely demands natural-language interpretation.

Enforcement happens outside the agent code.
[Amazon
Bedrock AgentCore Policy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html) runs Cedar policies at the
[Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) boundary, applying deterministic
routing rules based on task attributes, user identity, or tool
requirements without invoking an inference. Worker agents deploy
on
[Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html) at the leaf nodes where reasoning
actually happens. Keeping routing and reasoning on separate rails
lets each one evolve independently and be monitored on its own
metrics.

For partially deterministic routing, a tiered hybrid pattern helps
you align costs. A lightweight classifier (a small Amazon Bedrock
model or a rule-based heuristic) attempts rule-based routing first
and escalates to the full AI supervisor only when its confidence
falls below a configured threshold. The escalation rate is the
signal for whether the tier is tuned correctly. If the rate is too
high, the classifier needs refinement. If it is too low, the
supervisor is over-provisioned and the classifier can absorb more
cases.

Quantitative thresholds provide rule-based routing for workflows
with fewer than ten deterministic branches, a lightweight
classifier for routing across ten to fifty categories, and AI
supervisors only for unbounded category spaces that require
natural-language understanding. The orchestration overhead ratio
(supervisor tokens divided by total workflow tokens) is the
ongoing diagnostic. When it drifts above the baseline, the pattern
needs reassessment, not a larger budget.

### Implementation steps

- **Conduct workflow determinism
analysis:** At each orchestration point in the
workflow, classify the routing decision as fully
deterministic, partially deterministic, or open-ended, and
record the rationale as an architectural decision record so
downstream reviewers can audit why each pattern was chosen.
- **Apply Cedar policies for
deterministic routing:** Configure
[Amazon
Bedrock AgentCore Policy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html) with Cedar policies at
[Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) for every fully
deterministic branch, so these routing decisions run without
model invocations.
- **Insert a lightweight classifier for
partially deterministic routing:** Deploy a small
model or rule-based heuristic that attempts rule-based
routing first and escalates to a full AI supervisor only
when its confidence falls below a configurable threshold,
and log the escalation rate as a tuning signal.
- **Separate orchestration cost from
worker cost:** Configure
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) to attribute tokens
to orchestrator and worker tiers separately, calculate the
orchestration overhead ratio per workflow, and alert when
the ratio drifts above the baseline recorded for that
pattern.

## Resources

**Related best practices:**

- [AGENTCOST01-BP01 Use
the reflection pattern to design efficient agent reasoning
loops](agentcost01-bp01.html)
- [AGENTCOST01-BP02
Optimize multi-agent collaboration cost through efficient
handoff patterns](agentcost01-bp02.html)
- [AGENTCOST01-BP04 Design
agent hierarchies and delegation patterns that reduce
coordination overhead](agentcost01-bp04.html)
- [AGENTCOST05-BP02
Implement distributed cost tracing for multi-agent
workflows](agentcost05-bp02.html)

**Related documents:**

- [Amazon
Bedrock AgentCore Policy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html)
- [Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html)
- [Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html)
- [Agentic
AI patterns and workflows on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/introduction.html)

**Related videos:**

- [AWS re:Invent 2024 - Balance cost, performance & reliability
for AI at enterprise scale (AIM3304)](https://www.youtube.com/watch?v=Lwvv8Q33eeE)
- [AWS re:Invent 2024 - Sustainable and cost-efficient generative AI
with agentic workflows (AIM333)](https://www.youtube.com/watch?v=tFiDkSG2ess)

**Related examples:**

- [GitHub:
awslabs/amazon-bedrock-agentcore-samples - Policy
tutorials](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/08-AgentCore-policy)

**Related services:**

- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentcost01-bp03.html*

---

# AGENTCOST01-BP04 Design agent hierarchies and delegation patterns that reduce coordination overhead

Supervisor cost in agent hierarchies grows with the verbosity of
capability descriptions and the frequency of check-ins. Compact
manifests and autonomous workers keep coordination cost proportional
to workflow complexity rather than step count.

**Desired outcome:**

- Your agent hierarchies use the shallowest orchestration
structure capable of managing the workflow.
- You have supervisor agents operating on compressed capability
manifests that minimize input tokens per routing decision.
- Your worker agents complete multi-step sub-tasks autonomously,
escalating to supervisors only for task assignment and result
validation.
- You track orchestrator cost as a distinct category with a target
supervisor-to-worker cost ratio.

**Common anti-patterns:**

- Including verbose natural-language descriptions of every
worker's capabilities in routing prompts, which inflates token
cost that then scales linearly with worker count.
- Requiring supervisor check-ins after each sub-step, which
multiplies coordination overhead when workers could complete
multi-step work autonomously.
- Tracking only aggregate workflow cost without decomposing
orchestrator compared to worker expense, so disproportionate
coordination overhead hides in the total.

**Benefits of establishing this best
practice:**

- Compressed capability manifests reduce supervisor input-token
cost per routing decision.
- Autonomous workers remove supervisor round-trips for
intermediate decisions.
- Per-tier cost attribution surfaces optimization opportunities
where coordination overhead exceeds execution value.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Supervisor cost has two main drivers: how expensive each routing
decision is and how many times routing happens.

The first is controlled by manifest size. Supervisors that
describe workers in paragraphs of natural language pay for those
paragraphs on every routing call, and that cost scales linearly
with worker count. Short, structured capability manifests
(description, input schema, output schema, under 200 tokens each)
cut this cost without sacrificing routing quality, because the
supervisor doesn't need prose to choose between workers that have
distinct schemas.

The second is controlled by context relay. When context flows from
parent to worker through the supervisor, every byte of that
context is transmitted twice: once into the supervisor, and once
into the worker as part of the routing response.
[Amazon
Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) removes that doubling by letting
workers read shared context directly from memory using the
session's actor ID and session ID, so the supervisor only routes
rather than relays.
[Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) reduces it further by supporting
runtime tool discovery through Model Context Protocol, so the
supervisor prompt doesn't need to enumerate every tool the workers
can call.
[Amazon
Bedrock AgentCore Policy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html) controls which tools each worker
is allowed to invoke autonomously, making it safe to shift
decisions downward without losing governance.

Workers designed with sufficient tool autonomy and clear success
criteria can complete multi-step sub-tasks, returning a single
structured result with a confidence score. The supervisor then
makes an efficient accept-or-reject decision rather than
re-reasoning from scratch at each intermediate step. For workflows
with repeatable decomposition patterns, a plan-then-execute
approach compresses this further, where one supervisor invocation
generates the full task plan, then workers execute the plan
without further supervision.

Track the supervisor-to-worker cost ratio. Set a target (for
example, supervisor tokens no more than 15% of worker tokens) and
alert when it is exceeded. A breach typically signals that
manifest compression, worker autonomy, or plan-then-execute
adoption is needed.

### Implementation steps

- **Compress worker capability
descriptions:** Replace natural-language capability
descriptions with structured manifests (description, input
schema, output schema) under 200 tokens each, and use
[Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) runtime tool discovery to
avoid listing tools in the supervisor prompt.
- **Redesign workers for autonomous
multi-step completion:** Give each worker
sufficient tool autonomy and clear success criteria to
complete its sub-task end-to-end, and require the worker to
emit a confidence score in every response so the supervisor
can make accept-or-reject decisions without re-reasoning.
- **Apply policy and shared memory for
direct context access:** Configure
[Amazon
Bedrock AgentCore Policy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html) through Gateway to enforce
worker tool-access boundaries, and provision
[Amazon
Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) so workers read shared
context directly instead of receiving it relayed through the
supervisor.
- **Track supervisor-to-worker cost
ratio:** Configure
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) to attribute tokens
per tier, build Amazon CloudWatch dashboards showing the
supervisor-to-worker ratio per workflow, and alert when the
ratio exceeds a 15% target.

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
- [AGENTCOST05-BP02
Implement distributed cost tracing for multi-agent
workflows](agentcost05-bp02.html)

**Related documents:**

- [Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html)
- [Amazon
Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html)
- [Amazon
Bedrock AgentCore Policy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html)
- [Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html)
- [Agentic
AI patterns and workflows on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/introduction.html)

**Related videos:**

- [AWS 2025 - AgentCore Deep Dive: Gateway](https://www.youtube.com/watch?v=atWXM5lziY8)
- [AWS 2025 - AgentCore Observability: Monitor and Debug with
OpenTelemetry](https://www.youtube.com/watch?v=wWQgawUPr1k)

**Related examples:**

- [GitHub:
awslabs/amazon-bedrock-agentcore-samples - Multi-agent
tutorials](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/01-AgentCore-runtime/03-advanced-concepts)

**Related services:**

- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentcost01-bp04.html*

---
