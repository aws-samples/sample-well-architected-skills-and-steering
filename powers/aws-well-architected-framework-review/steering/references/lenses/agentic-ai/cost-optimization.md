# Cost Optimization

**Pillar**: Cost Optimization  
**Questions**: 7

---

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

# AGENTCOST02 — Model invocation and token cost optimization

**Pillar**: Cost Optimization  
**Best Practices**: 4

---

# AGENTCOST02-BP01 Architect tiered model selection for cost-performance optimization

Running every agent task on the largest available model inflates
inference cost by an order of magnitude for work that smaller models
handle correctly. Match each task to the cheapest model capable of
acceptable quality, and escalate only when confidence drops.

**Desired outcome:**

- You have agent tasks classified into complexity tiers, with a
documented routing policy mapping each tier to a specific
foundation model.
- You have cascading patterns that escalate to higher-cost models
only when a lower tier's confidence falls below threshold.
- You track cost-per-correct-response across tiers and refresh
routing decisions with the data rather than with intuition.

**Common anti-patterns:**

- Using the largest available model for all agent tasks without
assessing task complexity, inflating inference costs for routine
operations.
- Hard-coding static model assignments without confidence-based
escalation, which either over-provisions routine tasks or
under-provisions complex edge cases.
- Tracking aggregate costs without decomposing agent performance
by model tier, hiding opportunities to shift workloads to
cheaper models.
- Failing to monitor customized model performance after switching
to a smaller tier, allowing cost savings to mask hidden quality
degradation.

**Benefits of establishing this best
practice:**

- Tiered selection reserves expensive models for genuinely complex
reasoning and routes routine tasks to cost-effective
alternatives.
- Model cascading minimizes premium model invocations through
confidence-based escalation.
- Specialized models for domain-specific tasks deliver higher
accuracy at lower cost than general-purpose alternatives.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Task complexity is an important property to measure. At every
agent invocation, the reasoning you need is either lightweight
(classification, format conversion, intent extraction), moderate
(multi-step reasoning, summarization), or genuinely complex
(open-ended analysis, multi-constraint optimization). These three
classes map to different price points across the
[Amazon
Bedrock](https://aws.amazon.com/bedrock/) model catalog, and treating them identically means
you pay the complex-class price for every low-complexity task.
Classifying upfront and routing accordingly is where most of the
cost headroom sits.

A lightweight pre-classifier gives you that routing decision
without invoking the main model first. Rule-based heuristics or a
small model can analyze request characteristics like input length,
structured or unstructured format, constraint count, and reasoning
depth, assigning scores that map to tier thresholds (for example,
below 0.3 for simple, 0.3 to 0.7 for moderate, above 0.7 for
complex). The pre-classifier must cost less than the tier price
differential to produce net savings on first-attempt routing. For
multimodal tasks the principle extends further. Route document
extraction to Amazon Bedrock Data Automation and audio
interactions to Amazon Nova Sonic rather than sending raw images
or audio through expensive general-purpose vision models.

Model cascading is a fallback mechanism when the classifier is
uncertain. Have the lower-tier model return a structured response
with a self-assessed confidence score and escalate to the next
tier only when confidence falls below a threshold. Primary,
secondary, and tertiary fallback chains catch timeouts and
failures by moving up a tier rather than retrying the same one,
improving completion rates without retry waste.
[Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html) is designed to support multiple
frameworks and LLM providers, and
[Amazon
Bedrock AgentCore Policy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html) enforces guardrails that help
prevent expensive model calls when task complexity doesn't justify
the cost.

Pricing tier is independent of model size.
[Amazon
Bedrock capacity, limits, and cost optimization](https://docs.aws.amazon.com/bedrock/latest/userguide/capacity-limits-cost-optimization.html) documents
Flex for development and testing at the lowest per-token cost,
Standard for production, and Priority only for latency-sensitive
user-facing interactions where throttling risk must be minimized.
Batch inference offers up to 50% savings for non-time-sensitive
workloads like report generation, training data preparation, or
offline evaluation. For consistent high-volume traffic, Reserved
Tier commitments provide 30 to 50% savings against on-demand
pricing. With
[Amazon
Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html), you can benchmark multiple
model options against your actual task distribution, measuring
cost-per-correct-response and refreshing the routing policy
quarterly as new models become available.

### Implementation steps

- **Classify agent tasks into complexity
tiers:** Document a model routing policy mapping
each tier (simple, moderate, and complex) to a specific
[Amazon
Bedrock](https://aws.amazon.com/bedrock/) model, and commit the policy as an
architectural decision record so downstream reviewers can
audit the rationale.
- **Select pricing tier per
environment:** Use Flex for development and
testing, Standard for production, and Priority only for
latency-sensitive user-facing agents, and evaluate
[Amazon
Bedrock Reserved Tier](https://docs.aws.amazon.com/bedrock/latest/userguide/capacity-limits-cost-optimization.html) commitments for consistent
high-volume workloads.
- **Insert a task complexity
pre-classifier:** Deploy rule-based heuristics or a
small-model call that scores each request on input length,
structure, constraint count, and reasoning depth before the
main invocation, and make sure the classifier costs less
than the tier price differential.
- **Implement model cascading on
confidence:** Have each lower-tier response include
a self-assessed confidence score, and escalate to the next
tier when confidence falls below the configured threshold
rather than retrying at the same tier.
- **Configure fallback chains per task
category:** Define primary, secondary, and tertiary
model options, with automatic escalation on timeout or
failure instead of retry, so transient failures move up a
tier rather than repeating the same cost.
- **Route non-time-sensitive tasks to
batch inference:** Use
[Amazon
Bedrock batch inference](https://docs.aws.amazon.com/bedrock/latest/userguide/batch-inference.html) for report generation, data
enrichment, and offline evaluation to capture up to 50%
savings over on-demand pricing.
- **Benchmark specialized compared to
general-purpose models:** Run
[Amazon
Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html) on your actual task
distribution, measuring cost-per-correct-response so routing
choices are grounded in outcome data.
- **Review routing policies
quarterly:** Use AWS Cost Explorer and Amazon CloudWatch dashboards to inspect observed escalation rates,
and adjust tier assignments when cascade escalation patterns
indicate mis-tuned thresholds.

## Resources

**Related best practices:**

- [AGENTCOST01-BP01
Use the reflection pattern to design efficient agent reasoning
loops](agentcost01-bp01.html)
- [AGENTCOST01-BP04
Design agent hierarchies and delegation patterns that reduce
coordination overhead](agentcost01-bp04.html)
- [AGENTCOST02-BP02 Cost
optimize token consumption through efficient prompt
engineering](agentcost02-bp02.html)
- [AGENTCOST02-BP04
Implement model customization for long-term cost
reduction](agentcost02-bp04.html)
- [AGENTCOST05-BP01
Establish agent-level reasoning cost tracking and
attribution](agentcost05-bp01.html)

**Related documents:**

- [Amazon
Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html)
- [Effective
cost optimization strategies for Amazon Bedrock](https://aws.amazon.com/blogs/machine-learning/effective-cost-optimization-strategies-for-amazon-bedrock/)
- [Use
Amazon Bedrock Intelligent Prompt Routing for cost and latency
benefits](https://aws.amazon.com/blogs/machine-learning/use-amazon-bedrock-intelligent-prompt-routing-for-cost-and-latency-benefits/)
- [Optimizing
cost for using foundational models with Amazon Bedrock](https://aws.amazon.com/blogs/aws-cloud-financial-management/optimizing-cost-for-using-foundational-models-with-amazon-bedrock/)
- [Economics
for agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-economics/index.html)
- [Guidance
for Cost Analysis and Optimization with Amazon Bedrock
Agents](https://aws.amazon.com/solutions/guidance/cost-analysis-and-optimization-with-amazon-bedrock-agents/)
- [Agentic
AI patterns and workflows on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/introduction.html)
- [Amazon
Bedrock model pricing](https://aws.amazon.com/bedrock/pricing/)
- [Amazon
Bedrock capacity, limits, and cost optimization](https://docs.aws.amazon.com/bedrock/latest/userguide/capacity-limits-cost-optimization.html)
- [Amazon
Bedrock batch inference](https://docs.aws.amazon.com/bedrock/latest/userguide/batch-inference.html)

**Related videos:**

- [AWS re:Invent 2024 - Balance cost, performance & reliability
for AI at enterprise scale (AIM3304)](https://www.youtube.com/watch?v=Lwvv8Q33eeE)
- [AWS re:Invent 2024 - Mastering model choice: The 3-step Amazon
Bedrock advantage (AIM391)](https://www.youtube.com/watch?v=Vu91YwZxskY)

**Related examples:**

- [GitHub:
awslabs/amazon-bedrock-agentcore-samples - Evaluations
tutorials](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/07-AgentCore-evaluations)

**Related tools:**

- [Strands
Agents Model Providers](https://strandsagents.com/docs/user-guide/concepts/model-providers/)

**Related services:**

- [Amazon
Bedrock](https://aws.amazon.com/bedrock/)
- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
- [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentcost02-bp01.html*

---

# AGENTCOST02-BP02 Cost optimize token consumption through efficient prompt engineering

Every token in a system prompt is paid for on every invocation, so
prompt bloat compounds linearly with traffic. Compressing system
prompts, tool descriptions, and output formats makes the fixed cost
of each agent call proportional to the decision it has to make, not
the verbosity of its instructions.

**Desired outcome:**

- You have agent system prompts compressed to the minimum tokens
needed for accurate task completion.
- You have tool descriptions presented dynamically based on the
current task rather than transmitted in full on every call.
- You constrain output length explicitly so verbose responses
don't compound across multi-turn reasoning.
- You version prompts and track cost-per-task per version so
efficiency changes are measurable over time.

**Common anti-patterns:**

- Writing verbose system prompts with lengthy persona descriptions
and redundant explanations, inflating the fixed token cost on
every invocation.
- Including every tool description in every invocation regardless
of task relevance, which inflates input tokens when only a
subset of tools applies.
- Allowing unconstrained output length without formatting
directives, enabling verbose responses that compound across
multi-turn reasoning cycles.
- Treating prompts as uncontrolled strings rather than versioned
artifacts, so regressions in token efficiency go unnoticed until
a billing review.

**Benefits of establishing this best
practice:**

- Fixed-cost reductions from prompt compression compound across
every agent invocation in high-volume deployments.
- Dynamic tool loading transmits only task-relevant tools,
reducing tool description overhead in proportion to catalog
size.
- Prompt versioning with token tracking makes compression an
ongoing, measurable practice rather than a one-off cleanup.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

The system prompt is the largest fixed cost in every model
invocation, which means every unnecessary sentence is paid for
again each time the agent is called. Start by auditing prompts
with
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) to measure token
footprints, then compress systematically. Replace verbose
instructions with structured directives, tighten role definitions,
and remove redundant explanations.

Tool descriptions behave the same way. If the prompt carries the
full tool catalog even when only three tools are relevant, you are
paying for the rest of the catalog on every call.
[Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) uses MCP-based Semantic Tool
Selection to present only the tools relevant to the current
intent, and
[Amazon
Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) manages conversation state across
multi-turn sessions so you don't pay for manual history
concatenation.

In your context window, allocate tokens across the system prompt
(20 to 30%), user context (30 to 40%), few-shot examples (10 to
20%), and agent scratchpad (20 to 30%), and adjust based on your
agent's reasoning patterns. For few-shot examples in particular,
test whether the model performs well zero-shot before paying for
examples on every call. When examples are needed, identify the
minimum count that maintains task accuracy against the quality
baseline. Two or three examples are typically enough, and dynamic
example selection from a semantic index keeps only the relevant
ones in context.

Output length is the last thing to adjust. Explicit formatting
directives in the system prompt (response structure, maximum
length) directly control output token costs. Treat prompts as
versioned artifacts. Record token count, task success rate, and
cost-per-task for each version using AgentCore Observability
telemetry, and establish a monthly review cadence that tracks
cumulative savings in AWS Cost Explorer.

### Implementation steps

- **Audit and compress system
prompts:** Use
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) to measure token
footprints for every prompt, then apply compression to
minimize prompt size while maintaining decision accuracy.
- **Present tools dynamically through
Gateway:** Use
[Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) Semantic Tool Selection to
present only relevant tools per invocation, and compress
tool descriptions to tool name, one-sentence description,
and concise parameter schema.
- **Constrain output length:**
Add explicit output formatting directives to the system
prompt and configure model-specific token limit parameters
to enforce hard caps on response size.
- **Use managed memory for multi-turn
context:** Configure
[Amazon
Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) so conversation state is
maintained automatically instead of re-transmitted as full
history.
- **Reduce few-shot example
overhead:** Evaluate whether each agent task needs
examples at all, then reduce to the minimum effective count
of two to three. Load examples dynamically from an Amazon S3-hosted library using semantic similarity retrieval.
- **Version prompts and track
efficiency:** Record token count and task success
rate per prompt version, and establish a monthly
optimization review cadence that tracks cumulative savings
against cost-per-task targets.

## Resources

**Related best practices:**

- [AGENTCOST01-BP01
Use the reflection pattern to design efficient agent reasoning
loops](agentcost01-bp01.html)
- [AGENTCOST02-BP01
Architect tiered model selection for cost-performance
optimization](agentcost02-bp01.html)
- [AGENTCOST02-BP03 Use
intelligent caching to reduce redundant model
invocations](agentcost02-bp03.html)

**Related documents:**

- [Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html)
- [Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html)
- [Amazon
Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html)
- [Economics
for agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-economics/index.html)

**Related videos:**

- [AWS re:Invent 2024 - Sustainable and cost-efficient generative AI
with agentic workflows (AIM333)](https://www.youtube.com/watch?v=tFiDkSG2ess)
- [Strands
Tools: Building Custom AI Agents with Python](https://www.youtube.com/watch?v=EGhIZCfOvG4)

**Related examples:**

- [GitHub:
awslabs/amazon-bedrock-agentcore-samples - Runtime
tutorials](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/01-AgentCore-runtime)

**Related tools:**

- [Strands
Agents Custom Tools](https://strandsagents.com/docs/user-guide/concepts/tools/custom-tools/)

**Related services:**

- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentcost02-bp02.html*

---

# AGENTCOST02-BP03 Use intelligent caching to reduce redundant model invocations

Agents repeat work constantly: identical prompts, semantically
equivalent requests, the same planning steps across similar tasks.
Caching at the prompt, semantic, and plan-template layers changes
repetition from a recurring expense into a one-time cost paid on the
first invocation.

**Desired outcome:**

- You have prompt caching enabled for stable system prompts so the
cacheable prefix is reused across invocations at reduced rates.
- You have a semantic cache that serves responses for functionally
equivalent requests above a configurable similarity threshold.
- You have plan templates cached and instantiated for recurring
task patterns rather than regenerated each time.
- You track cache hit rates and cost savings per caching layer.

**Common anti-patterns:**

- Transmitting identical system prompts and tool descriptions on
every invocation at full input token cost rather than cached
prefix rates.
- Using exact-match lookups when functionally equivalent requests
use different wording, causing cache misses on semantically
identical tasks.
- Applying one cache TTL across all task types without
distinguishing static reference data from time-sensitive
information, returning stale responses that degrade quality.
- Deploying customized models without monitoring cache-assisted
performance, missing opportunities to validate that expected
cost reductions actually materialize.

**Benefits of establishing this best
practice:**

- Prompt caching reduces input token costs by reusing cached
system instructions across invocations at reduced rates.
- Semantic caching helps prevent redundant reasoning by serving
cached responses for functionally equivalent tasks.
- Plan template reuse reduces model invocations for the planning
phase of recurring task patterns.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Caching for agents works at three distinct layers, and each layer
has a different failure mode.

[Amazon
Bedrock prompt caching](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-caching.html) is the highest-impact layer for
agents with large stable system prompts. Amazon Bedrock stores the
key-value state of the cached prefix and reuses it at reduced
rates. Design so that the cacheable prefix (system prompt, tool
descriptions) is stable across invocations, because any dynamic
content mixed in invalidates the cache. Refactor to move
user-specific or session-specific content out of the cacheable
prefix.

Semantic caching addresses the idea that two requests that mean
the same thing are rarely identical in wording. Generate an
embedding of each incoming request with a lightweight model and
query
[Amazon OpenSearch Service Serverless](https://aws.amazon.com/opensearch-service/features/serverless/) for similar prior requests above a
configurable threshold such as cosine similarity greater than
0.95. The threshold helps you tune, as higher values reduce false
positives but lower hit rates, and the right value depends on how
much response variance your agent tolerates. Store cache entries
with TTLs calibrated to each task type's freshness requirements,
so reference data cached for hours doesn't pollute tasks that need
up-to-date market or inventory information.

Don't overlook plan template caching. Agent planning outputs are
highly repeatable for recurring task patterns, like an onboarding
checklist, a support triage decomposition, or a reporting workflow
plan. Store these plans keyed by task type and input parameter
signature, and instantiate cached templates with current
parameters rather than regenerating new plans each time.
[Amazon
Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) manages conversation state by
extracting and persisting key information, reducing input token
costs from repeated history transmission.

Cache correctness depends on invalidation. Event-driven
invalidation purges stale entries the moment source data changes,
which is what makes aggressive caching safe for moderately
volatile data. Measure impact with AWS Cost Explorer and Amazon CloudWatch integrated with
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html), and alarm when hit rates
fall below targets.

### Implementation steps

- **Enable prompt caching for stable
prefixes:** Turn on
[Amazon
Bedrock prompt caching](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-caching.html) for agents with system prompts
larger than 1,000 tokens, and refactor the prompt to move
dynamic content out of the cacheable prefix.
- **Deploy a semantic cache
layer:** Stand up an OpenSearch Serverless index
with embedding-based similarity, configure similarity
thresholds per task type, and set per-task TTLs. Accept
quantization only when accuracy loss remains below two
percent on task success rate.
- **Cache plan templates:** Key
plan templates by task type and input parameter signature,
and perform a pre-invocation lookup before generating a new
plan.
- **Use managed memory for session
state:** Configure
[Amazon
Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) session identifiers so
multi-turn conversation state is maintained without manual
history concatenation.
- **Design event-driven invalidation and
monitor hit rates:** Wire event-driven cache
invalidation to source data changes, and create CloudWatch
dashboards that display hit rates across prompt, semantic,
and plan-template caches with alarms when hit rates fall
below target.

## Resources

**Related best practices:**

- [AGENTCOST02-BP01
Architect tiered model selection for cost-performance
optimization](agentcost02-bp01.html)
- [AGENTCOST02-BP02 Cost
optimize token consumption through efficient prompt
engineering](agentcost02-bp02.html)
- [AGENTCOST03-BP01
Design cost-effective retrieval systems with tiered
memory](agentcost03-bp01.html)

**Related documents:**

- [Amazon
Bedrock Prompt Caching](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-caching.html)
- [Effectively
use prompt caching on Amazon Bedrock](https://aws.amazon.com/blogs/machine-learning/effectively-use-prompt-caching-on-amazon-bedrock/)
- [Optimize
LLM response costs and latency with effective caching](https://aws.amazon.com/blogs/database/optimize-llm-response-costs-and-latency-with-effective-caching/)
- [Amazon
Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html)
- [Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html)
- [Economics
for agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-economics/index.html)

**Related videos:**

- [AWS re:Invent 2024 - Balance cost, performance & reliability
for AI at enterprise scale (AIM3304)](https://www.youtube.com/watch?v=Lwvv8Q33eeE)

**Related examples:**

- [GitHub:
awslabs/amazon-bedrock-agentcore-samples - Memory
tutorials](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/04-AgentCore-memory)

**Related services:**

- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon OpenSearch Service](https://aws.amazon.com/opensearch-service/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentcost02-bp03.html*

---

# AGENTCOST02-BP04 Implement model customization for long-term cost reduction

Customizing smaller models for a high-volume recurring task can
optimize per-invocation costs into a one-time training expense that
amortizes across every future call. The math only works when volume
and task stability are high enough to justify the investment, so the
decision needs to start with a break-even calculation, not an
enthusiasm for fine-tuning.

**Desired outcome:**

- You have specialized models handling high-volume recurring tasks
at materially lower per-invocation cost than general-purpose
foundation models.
- You have a customization pipeline that captures decision
patterns from production and refreshes models on a scheduled
cadence.
- You validate decision quality with A/B testing against
foundation models before routing production traffic to a
customized model.
- You track inference cost savings and decision quality side by
side so positive ROI is provable rather than assumed.

**Common anti-patterns:**

- Fine-tuning on synthetic data that misrepresents production task
distributions, causing underperformance that offsets cost
savings through lower task completion rates.
- Applying customization to low-volume task categories where
training costs exceed projected inference savings, wasting
effort on optimization that doesn't reach positive ROI.
- Treating customization as a one-time project without continuous
adaptation, allowing specialized models to drift as workload
patterns change.
- Routing production traffic to customized models without A/B
testing against foundation models, risking quality degradation
that undermines cost savings.
- Deploying customized models without instrumenting inference
latency, token costs, and quality metrics, reducing the risk of
validation that the expected cost reduction materialized.

**Benefits of establishing this best
practice:**

- Fine-tuned smaller models achieve comparable accuracy at lower
per-invocation cost through reduced token consumption and faster
inference.
- One-time training costs amortize across thousands of
invocations, delivering compounding returns for high-volume
tasks.
- Continuous adaptation pipelines keep specialized models aligned
with evolving workload patterns rather than decaying silently.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Calculate current monthly inference cost for the target task
category using
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html), estimate the reduction
from a smaller customized model, and compare against one-time
customization costs plus ongoing refresh. When monthly inference
costs exceed $500 and task volume exceeds 10,000 invocations per
month, customization typically reaches break-even within 6 to 12
months. Make the break-even explicit: (one-time training cost +
quarterly refresh cost × planning horizon in quarters) divided by
monthly inference savings. For a $5,000 training run that saves
$400 per month, break-even lands at month 13, which is acceptable
for workloads with multi-year lifespans but not for experimental
projects.

[Knowledge
distillation](https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models.html) transfers capability from a large teacher
model to a smaller student model at lower per-invocation cost. The
training data should come from production invocation logs filtered
for high-confidence, successful completions. Parameter-efficient
fine-tuning methods like QLoRA quantize base model weights to
four-bit precision and train only adapter parameters, making
single-GPU fine-tuning viable for smaller teams.
[Amazon
Bedrock model customization](https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models.html) jobs and
[Amazon SageMaker AI AI Training Jobs](https://docs.aws.amazon.com/sagemaker/latest/dg/train-model.html) with QLoRA support fine-tuning
without managing training infrastructure, and
[Amazon
Bedrock Custom Model Import](https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html) brings the results into Amazon
Bedrock for serving.

Validation helps prevent quality regressions that occur from these
cost optimizations. With
[Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html), you can split production traffic
between foundation and customized models during A/B testing, and
[Amazon
Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html) runs LLM-as-a-Judge
assessments against both arms. Accept quantization only when
accuracy loss stays within your acceptable quality threshold on
task success rate. Treat customization as a pipeline: periodically
extract high-quality examples from production logs, schedule
quarterly refresh jobs, and gate promotion on A/B validation so
drift doesn't compound silently between refreshes.

### Implementation steps

- **Conduct a customization cost-benefit
analysis:** Calculate current monthly inference
costs for high-volume task categories, identify where
training costs amortize within your planning horizon, and
compare fine-tuning investment (training compute plus
ongoing maintenance) against projected cumulative inference
savings.
- **Curate training data from production
logs:** Extract high-quality examples from
production invocation logs by filtering for invocations with
low error rates and acceptable latency using AgentCore
Observability metrics. Target 500 to 1,000 examples per task
category. Query Amazon CloudWatch for invocations where
latency falls within the p50 to p90 range and error_type is
absent, review a sample manually to verify quality, and
store the curated dataset in Amazon S3.
- **Run distillation or
fine-tuning:** Use
[Amazon
Bedrock model customization](https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models.html) jobs or
[Amazon SageMaker AI AI Training Jobs](https://docs.aws.amazon.com/sagemaker/latest/dg/train-model.html) with QLoRA, and validate
using
[Amazon
Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html) against a held-out test
set.
- **Import and A/B test customized
models:** Use
[Amazon
Bedrock Custom Model Import](https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html) and deploy through
[Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html), routing a traffic slice to
the customized model before promoting it to handle
production volume.
- **Schedule quarterly refresh
jobs:** Automate training data extraction and
retraining on a quarterly cadence, with A/B validation as
the promotion gate to catch drift at each refresh rather
than at annual review.

## Resources

**Related best practices:**

- [AGENTCOST02-BP01
Architect tiered model selection for cost-performance
optimization](agentcost02-bp01.html)
- [AGENTCOST02-BP02 Cost
optimize token consumption through efficient prompt
engineering](agentcost02-bp02.html)
- [AGENTCOST05-BP01
Establish agent-level reasoning cost tracking and
attribution](agentcost05-bp01.html)

**Related documents:**

- [Model
customization in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models.html)
- [Amazon
Bedrock Custom Model Import](https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html)
- [Amazon
Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html)
- [Evaluate
models in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation-judge.html)
- [Economics
for agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-economics/index.html)
- [Guidance
for Cost Analysis and Optimization with Amazon Bedrock
Agents](https://aws.amazon.com/solutions/guidance/cost-analysis-and-optimization-with-amazon-bedrock-agents/)

**Related videos:**

- [AWS re:Invent 2024 - Mastering model choice: The 3-step Amazon
Bedrock advantage (AIM391)](https://www.youtube.com/watch?v=Vu91YwZxskY)

**Related examples:**

- [GitHub:
awslabs/amazon-bedrock-agentcore-samples - Evaluations
tutorials](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/07-AgentCore-evaluations)

**Related services:**

- [Amazon
Bedrock](https://aws.amazon.com/bedrock/)
- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon SageMaker AI AI](https://aws.amazon.com/sagemaker-ai/)
- [Amazon S3](https://aws.amazon.com/s3/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentcost02-bp04.html*

---

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

# AGENTCOST06 — Agent discovery and deployment cost optimization

**Pillar**: Cost Optimization  
**Best Practices**: 3

---

# AGENTCOST06-BP01 Implement lightweight discovery and registry for cost-effective collaboration

Deploying service-mesh infrastructure for agent discovery carries a
fixed cost that doesn't scale down when traffic does. You can keep
registry cost proportional to fleet size through managed discovery
through tool exposure, consumption-based registries, and aggressive
metadata caching.

**Desired outcome:**

- You use consumption-based infrastructure for agent discovery,
charging only for actual operations.
- You serve repeated capability lookups from a metadata cache
instead of the database.
- You keep costs proportional to fleet size through efficient
indexing and batched writes.
- You monitor per-query costs so they don't grow silently as the
fleet expands.

**Common anti-patterns:**

- Deploying managed service mesh for simple capability lookups
when a NoSQL database with consumption-based pricing would
suffice.
- Making repeated registry lookups for the same agent metadata on
every invocation without caching.
- Using full-table scans instead of targeted queries with proper
indexes, consuming unnecessary read capacity.
- Operating agent discovery registries without monitoring
per-query costs, which scale with fleet size and grow silently
as the fleet expands.

**Benefits of establishing this best
practice:**

- Consumption-based registry avoids fixed infrastructure overhead,
charging only for actual read and write operations.
- Metadata caching serves repeated capability lookups without
database queries, avoiding most read charges.
- Batched capability updates reduce write costs by accumulating
changes into single operations.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Agent discovery through
[Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) removes the need for custom
registry infrastructure in many scenarios. When you expose
specialized agents as tools through Gateway's MCP server
capabilities, other agents discover and invoke them without a
separate registry. AgentCore Gateway handles credential exchange,
protocol translation, and composition of multiple tools into
unified endpoints under consumption-based pricing. This approach
fits when agents primarily interact through tool invocation
patterns and Gateway's built-in discovery semantics match your
collaboration requirements.

When those conditions don't hold, you can build a custom
lightweight registry using
[Amazon DynamoDB](https://aws.amazon.com/dynamodb/) with on-demand capacity mode and global secondary
indexes for filtered capability queries. Index agent capabilities
by category and task type so discovery queries read only relevant
partitions rather than scanning the full registry. As agent fleets
grow, inefficient discovery queries that scan entire capability
sets multiply costs and degrade latency at the same time, so
targeted queries through global secondary indexes become the
operational baseline, not an optimization.

Metadata caching helps you cost optimize a registry designed for
scalability. A capability lookup that hits the cache costs
effectively nothing, while a lookup that falls through to DynamoDB
incurs a read charge. Configure TTLs that reflect how often
capability metadata actually changes (typically hours, not
seconds), and use the persistent filesystem on
[Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html) to cache registry metadata across
session stop and resume cycles.

Monitoring becomes increasingly important, as registry read costs
scale with query volume, and per-query charges accumulate as the
fleet grows.
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) and Amazon CloudWatch track
read costs, cache hit rates, and discovery API call volumes, with
alarms for anomalous patterns before they become a line item worth
investigating.

### Implementation steps

- **Evaluate Gateway-based discovery
first:** Determine whether
[Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) semantic tool selection
meets your discovery requirements. If so, expose agents
through Gateway's MCP server capabilities and avoid the
custom registry entirely.
- **Use consumption-based storage with
efficient indexing:** For custom registries, use
[Amazon DynamoDB](https://aws.amazon.com/dynamodb/) with on-demand capacity mode. Design a
global secondary index on capability-category so filtered
queries by capability type or task category read only
relevant partitions.
- **Deploy a metadata cache:**
Configure TTLs appropriate to how often capability metadata
changes, and use the
[Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html) persistent filesystem to
cache across session cycles.
- **Monitor registry costs:**
Track read costs and cache hit rates using
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) and Amazon CloudWatch, with alarms for anomalous patterns.

## Resources

**Related best practices:**

- [AGENTCOST02-BP03
Use intelligent caching to reduce redundant model
invocations](agentcost02-bp03.html)
- [AGENTCOST06-BP02 Cost
optimize versioning and deployment through efficient artifact
management](agentcost06-bp02.html)
- [AGENTCOST06-BP03 Design
cost-efficient initialization through warm pools and
caching](agentcost06-bp03.html)

**Related documents:**

- [Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html)
- [Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html)

**Related videos:**

- [AWS 2025 - AgentCore Deep Dive: Gateway](https://www.youtube.com/watch?v=atWXM5lziY8)
- [AWS 2025 - AgentCore Registry: Discover, Govern, and Reuse AI
Agents at Scale](https://www.youtube.com/watch?v=rIcOJrE-fTk)

**Related examples:**

- [GitHub:
awslabs/amazon-bedrock-agentcore-samples - Gateway
tutorials](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/02-AgentCore-gateway)

**Related services:**

- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon DynamoDB](https://aws.amazon.com/dynamodb/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentcost06-bp01.html*

---

# AGENTCOST06-BP02 Cost optimize versioning and deployment through efficient artifact management

Agent runtimes that create an immutable version on every
configuration change accumulate hundreds of versions during normal
development, each holding references to container images that can't
be managed easily. Layered base images, endpoint-based traffic
routing, and automated cleanup policies keep deployment cost
proportional to real usage rather than to the number of past
configurations.

**Desired outcome:**

- You have container layer deduplication storing shared
dependencies once across agent versions.
- You use endpoint-based traffic routing for blue/green and canary
deployments without duplicate running infrastructure.
- You have automated lifecycle policies that delete unused
versions, helping prevent indefinite storage accumulation.
- You monitor version inventory and catch unused versions before
they become a material cost.

**Common anti-patterns:**

- Retaining all agent versions indefinitely without lifecycle
policies, accumulating storage costs for versions that receive
zero invocations.
- Creating separate container images without sharing common base
layers, multiplying storage costs across agent versions.
- Running full parallel environments for blue/green deployments
instead of routing only test traffic percentages.
- Allowing unused agent versions to accumulate without monitoring,
reducing the risk of automated cleanup and steadily increasing
storage overhead without visibility into version invocation
patterns.

**Benefits of establishing this best
practice:**

- Container layer deduplication stores shared dependencies once,
reducing storage costs proportionally to version reuse. Verify
deduplication by comparing total repository storage in ECR
(reported in CloudWatch metrics under
RepositorySize) against the sum of individual
image manifest sizes. Effective deduplication shows repository
storage significantly smaller than the sum of manifests.
- Endpoint-based routing enables deployment transitions without
duplicate running infrastructure.
- Automated cleanup deletes unused versions, helping prevent
indefinite storage cost growth.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

[Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html) creates an immutable version on
every configuration update. The version itself is lightweight
metadata (container image reference, protocol settings, and
network configuration), but each version holds a reference to
container images that
[Amazon ECR](https://aws.amazon.com/ecr/)
can't be managed until all references are removed. Updating an
environment variable, changing a protocol setting, or modifying
network configuration all trigger a new version. Without a cleanup
policy, active development produces hundreds of versions, each
anchoring its referenced images in place.

The first mitigation is layer structure. Build agent containers
with a common base layer containing shared dependencies (runtime,
SDK, common tools) and agent-specific layers on top. ECR
automatically deduplicates identical layers across images, so
agents that share most dependencies share most storage. The second
mitigation is traffic routing. The AgentCore Runtime endpoint
system supports blue/green and canary deployments without parallel
infrastructure: create a production endpoint pointing to the
stable version and use weighted routing to send a small traffic
percentage to new versions during validation.
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) provides the per-version
metrics (error rates, latency percentiles,
cost-per-task-completion) that drive the promotion decision.

Traditional canary promotion criteria look at error rates and
latency, but agent versions can differ significantly on reasoning
cost (a new prompt might produce correct answers that take 30%
more tokens). Including cost-per-task-completion in the promotion
criteria helps prevent a cost regression from slipping into
production behind good quality metrics.

Define a maximum version retention (a reasonable starting point is
the last five versions plus any version currently serving traffic
through an endpoint) and configure
[Amazon ECR lifecycle policies](https://docs.aws.amazon.com/AmazonECR/latest/userguide/LifecyclePolicies.html) to delete untagged images and images
older than 90 days not referenced by active versions. Automated
deletion of versions beyond the retention limit, gated on
verification that no endpoints reference the version and it has
had zero invocations during the retention window, keeps ECR from
turning into a graveyard of development iterations.

### Implementation steps

- **Structure containers for layer
sharing:** Build agent containers with common base
layers and agent-specific layers so
[Amazon ECR](https://aws.amazon.com/ecr/) layer deduplication is effective.
- **Use endpoint-based traffic
routing:** Deploy agents to
[Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html) and configure custom
endpoints for production traffic with weighted routing for
blue/green and canary deployments.
- **Include cost in promotion
criteria:** Monitor deployment quality using
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) metrics before
updating production endpoints, including
cost-per-task-completion alongside error rates and latency.
- **Set version retention
policies:** Define a retention policy such as the
last five versions plus active traffic, and configure
[Amazon ECR lifecycle policies](https://docs.aws.amazon.com/AmazonECR/latest/userguide/LifecyclePolicies.html) to delete unused images
automatically.
- **Monitor version inventory
weekly:** Deploy a weekly version inventory
function that queries AgentCore Runtime APIs for all agent
versions, identifies versions with zero invocations through
Amazon CloudWatch metrics, and stores the usage metadata for
historical analysis before the ECR lifecycle policy deletes
the images.

## Resources

**Related best practices:**

- [AGENTCOST05-BP01
Establish agent-level reasoning cost tracking and
attribution](agentcost05-bp01.html)
- [AGENTCOST06-BP01
Implement lightweight discovery and registry for
cost-effective collaboration](agentcost06-bp01.html)
- [AGENTCOST06-BP03 Design
cost-efficient initialization through warm pools and
caching](agentcost06-bp03.html)

**Related documents:**

- [Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html)
- [Amazon ECR lifecycle policies](https://docs.aws.amazon.com/AmazonECR/latest/userguide/LifecyclePolicies.html)
- [Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html)

**Related videos:**

- [AWS 2025 - AgentCore Deep Dive: Runtime](https://www.youtube.com/watch?v=wizEw5a4gvM)

**Related examples:**

- [GitHub:
awslabs/amazon-bedrock-agentcore-samples - Runtime
tutorials](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/01-AgentCore-runtime)

**Related services:**

- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon ECR](https://aws.amazon.com/ecr/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentcost06-bp02.html*

---

# AGENTCOST06-BP03 Design cost-efficient initialization through warm pools and caching

Cold starts are a significant per-invocation cost in agent
infrastructure, where model loading, tool registration, and memory
hydration run on every fresh session. You can reduce those
per-invocation costs through persistent filesystems, session
affinity, and lazy context loading to reuse results while still
scaling to zero for agents that are rarely called.

**Desired outcome:**

- You amortize initialization costs across many invocations by
caching artifacts on a persistent filesystem.
- You have frequently invoked agents reusing warm sessions and
infrequent agents scaling to zero without idle charges.
- You defer non-essential context retrieval to on-demand, keeping
initialization under a fixed time budget.
- You track cold start rates and initialization costs per agent
type.

**Common anti-patterns:**

- Performing expensive initialization on every invocation instead
of caching artifacts across sessions.
- Allowing frequently invoked agents to repeatedly incur cold
starts without session persistence or warm pool patterns.
- Loading all potentially relevant context at startup instead of
lazy-loading on demand, increasing initialization latency with
data that may never be used.
- Operating agents without cold start visibility, missing
opportunities to apply warm pool patterns or optimize
initialization for high-impact agents. Agent cold starts include
model loading, tool registration, and memory hydration, not just
container startup.

**Benefits of establishing this best
practice:**

- Persistent filesystem caching amortizes initialization costs
across many invocations, avoiding repeated overhead.
- Session lifecycle management maintains warm sessions for
frequent agents while scaling to zero for infrequent ones
without idle charges.
- Lazy context loading reduces initialization time by deferring
non-essential retrieval until reasoning requires it.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

[Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html) implements warm pool behavior
through its session lifecycle. Sessions move through Active, Idle,
and Terminated states. Active handles processing, Idle maintains
session readiness after inactivity timeout without compute
charges, and Terminated ends the session at expiration or maximum
lifetime. Frequently invoked agents keep warm sessions through the
idle window while infrequent agents scale to zero, so you don't
pay idle capacity for agents that are not being called. Tune idle
timeout based on invocation frequency to balance responsiveness
with session overhead.

The persistent filesystem makes initialization caching worthwhile
to implement. The filesystem survives session stop and resume
cycles for up to 14 days, so expensive initialization artifacts
(model state, tool configurations, and preloaded reference data)
can be computed once on the first invocation and reused across
many later sessions. The 14-day retention shapes your caching
strategy: plan artifact refresh and cache invalidation to fit
inside the window, so cached data never ages out silently and
never gets stale beyond the refresh point.

Session affinity optimizes costs by keeping the same
runtimeSessionId across related invocations so
loaded models and cached tool configurations are reused. Implement
session tracking in the orchestration layer so user workflows map
to consistent session identifiers, and monitor session reuse rates
to confirm routing is avoiding unnecessary initialization
overhead. If cold start rates rise above 10%, investigate affinity
or idle timeout misconfiguration before optimizing the
initialization logic itself.

Consider *lazy context loading*, where data is
fetched or parsed only when it is required.
[Amazon
Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) supports retrieving only minimal
startup context (the user's current task and immediate session
history), deferring long-term memory and knowledge base retrieval
until the agent actually needs the data. This keeps initialization
time under a 2-second target covering model loading and tool
registration. Monitor cold start rates and initialization costs
through
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html), build Amazon CloudWatch
dashboards for initialization duration and session reuse by agent
type, and review idle timeout configuration monthly based on
observed invocation patterns.

### Implementation steps

- **Cache initialization artifacts on
persistent storage:** Configure
[Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html) with persistent filesystem
(surviving up to 14 days across session cycles) and
implement initialization logic that checks for cached
artifacts before performing expensive operations.
- **Apply session affinity:**
Maintain consistent runtimeSessionId values across related
invocations so warm session state (loaded models, cached
tool configurations) is reused.
- **Defer non-essential
context:** Configure
[Amazon
Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) for lazy loading of startup
context, deferring additional retrieval to on-demand during
reasoning, with an initialization time target under 2
seconds.
- **Monitor cold start rates per agent
type:** Instrument agents with
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) to track session
creation latency, initialization duration (model loading and
tool registration), and cold start rates, with alarms for
rates exceeding 10%.

## Resources

**Related best practices:**

- [AGENTCOST02-BP03
Use intelligent caching to reduce redundant model
invocations](agentcost02-bp03.html)
- [AGENTCOST06-BP01
Implement lightweight discovery and registry for
cost-effective collaboration](agentcost06-bp01.html)
- [AGENTCOST06-BP02 Cost
optimize versioning and deployment through efficient artifact
management](agentcost06-bp02.html)

**Related documents:**

- [Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html)
- [Amazon
Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html)
- [Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html)

**Related videos:**

- [AWS 2025 - AgentCore Deep Dive: Runtime](https://www.youtube.com/watch?v=wizEw5a4gvM)
- [AWS 2025 - AgentCore Deep Dive: Memory](https://www.youtube.com/watch?v=-N4v6-kJgwA)

**Related examples:**

- [GitHub:
awslabs/amazon-bedrock-agentcore-samples - Runtime advanced
concepts](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/01-AgentCore-runtime/03-advanced-concepts)

**Related services:**

- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentcost06-bp03.html*

---

# AGENTCOST07 — Agent cost governance and continuous optimization

**Pillar**: Cost Optimization  
**Best Practices**: 3

---

# AGENTCOST07-BP01 Implement automated cost controls with intelligent cutoffs

Autonomous agents that invoke tools and accumulate memory without
caps are a primary cost risk of agentic systems. Hierarchical budget
limits, automatic cutoffs on runaway sessions, and graduated
throttling help keep your costs bounded without forcing the agent to
stop working at the first sign of pressure.

**Desired outcome:**

- You enforce per-cycle, per-task, and per-day budget limits as
pre-invocation checks, not alerts after the fact.
- You have automatic cutoffs that halt reasoning loops at
iteration or cost thresholds.
- You have graduated throttling that slows invocations as budgets
approach limits rather than forcing binary shutdown.
- You require approval for capability expansions that materially
increase cost profiles.

**Common anti-patterns:**

- Deploying agents without budget limits, causing unexpected cost
overruns during production operations.
- Allowing agents to enter unbounded reasoning loops that consume
tokens each cycle without progress toward completion.
- Permitting unbounded tool invocations and memory growth: agents
autonomously invoke tools and accumulate memory, and without
caps, costs grow unbounded. This is a primary cost risk of
autonomous agents.
- Treating cost controls and agent autonomy as mutually exclusive,
either restricting agents excessively or granting unlimited
spending authority.

**Benefits of establishing this best
practice:**

- Hierarchical budget limits (like per-cycle, per-task, and
per-day) create multiple defensive barriers against cost
overruns.
- Automatic cutoffs halt reasoning loops at configured thresholds,
addressing one of the most expensive failure modes in autonomous
systems.
- Graduated throttling is designed to preserve agent functionality
at reduced throughput rather than forcing abrupt shutdown.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Implement cost controls outside the agent's control loop for
reliable enforcement.
[Amazon
Bedrock AgentCore Policy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html) applies Cedar policies at the
[Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) boundary, helping prevent agents
from bypassing budget limits through prompt manipulation.
[Amazon
Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html) complements this by enforcing
topic-based restrictions that help prevent tangential reasoning
chains, which reduces token waste from off-topic exploration.

Hierarchical budgets give you multiple defensive barriers:

- Per-cycle limits catch individual runaway loops
- Per-task limits catch aggregate work inside a single user
request
- Per-day limits catch sustained elevated usage

Automatic cutoffs track both iteration count and cumulative token
cost per session, halting reasoning loops when thresholds are
exceeded. Tool invocation caps per session matter as a separate
control because each tool call incurs both the external API cost
and the token cost of processing returned data. Uncapped tool use
can drain the token budget from the other direction. Memory growth
guardrails cap context window growth rate because every token in
context is paid on every subsequent invocation, turning unbounded
accumulation into a compounding cost driver.

Throttling is another useful automated control. Amazon API Gateway
usage plans or custom Lambda-based rate limiting reduce maximum
throughput as daily budgets approach limits, slowing token
consumption without forcing hard cutoffs. Throttling and cutoffs
operate at different scales. Throttling handles sustained high
usage, while cutoffs handle individual runaway sessions. A
well-designed control stack uses both, so normal high traffic is
slowed rather than stopped, and pathological sessions are stopped
rather than slowed.

Monitor these controls by using
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html), which feeds Amazon CloudWatch dashboards for budget utilization, cutoff activations,
and throttling events. For cost-impacting configuration changes
(adding expensive tools, upgrading models, or expanding autonomous
capabilities), integrate cost review gates into the CI/CD pipeline
so significant cost impacts receive review before deployment.

### Implementation steps

- **Enforce budget limits through Cedar
policies:** Configure
[Amazon
Bedrock AgentCore Policy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html) with Cedar policies
enforcing per-cycle, per-task, and per-day budget limits at
the Gateway boundary, including tool invocation caps per
session and memory growth guardrails that trigger
summarization when context approaches model limits.
- **Deploy automatic cutoffs and topic
guardrails:** Track iteration counts and cumulative
costs per session with automatic cutoffs, and use
[Amazon
Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html) for topic-based restrictions on
tangential reasoning.
- **Add graduated throttling:**
Implement progressive throttling that slows invocations as
budgets approach limits, keeping agent operations at reduced
throughput rather than forcing binary shutdown.
- **Visualize and alarm on governance
metrics:** Create Amazon CloudWatch dashboards
displaying budget utilization, cutoff activations, and
throttling events using
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) metrics.

## Resources

**Related best practices:**

- [AGENTCOST01-BP01
Use the reflection pattern to design efficient agent reasoning
loops](agentcost01-bp01.html)
- [AGENTCOST05-BP01
Establish agent-level reasoning cost tracking and
attribution](agentcost05-bp01.html)
- [AGENTCOST07-BP02
Establish proactive anomaly detection for agent cost
patterns](agentcost07-bp02.html)
- [AGENTCOST07-BP03 Create
systematic optimization feedback loops for continuous
improvement](agentcost07-bp03.html)

**Related documents:**

- [Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html)
- [Amazon
Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html)
- [Amazon
Bedrock AgentCore Policy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html)
- [AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html)
- [Amazon
Bedrock capacity, limits, and cost optimization](https://docs.aws.amazon.com/bedrock/latest/userguide/capacity-limits-cost-optimization.html)
- [Guidance
for Cost Analysis and Optimization with Amazon Bedrock
Agents](https://aws.amazon.com/solutions/guidance/cost-analysis-and-optimization-with-amazon-bedrock-agents/)

**Related videos:**

- [AWS re:Invent 2024 - Balance cost, performance & reliability
for AI at enterprise scale (AIM3304)](https://www.youtube.com/watch?v=Lwvv8Q33eeE)

**Related examples:**

- [GitHub:
awslabs/amazon-bedrock-agentcore-samples - Policy
tutorials](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/08-AgentCore-policy)

**Related workshops:**

- [Diving
Deep into Bedrock AgentCore - Policy](https://catalog.workshops.aws/agentcore-deep-dive/en-US/90-agentcore-policy)

**Related services:**

- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
- [AWS Budgets](https://aws.amazon.com/aws-cost-management/aws-budgets/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentcost07-bp01.html*

---

# AGENTCOST07-BP02 Establish proactive anomaly detection for agent cost patterns

Generic billing alerts help you find cost escalation more quickly
after it starts. Agent-specific anomaly detection catches reasoning
loop token spikes, tool invocation storms, and memory growth
quickly, and routing those alerts correctly means that you can alert
the team that owns the agent instead of the operations team.

**Desired outcome:**

- You establish ML-based anomaly detection with statistical
baselines and deviation thresholds.
- You have custom detectors for agent-specific failure modes
beyond generic infrastructure monitoring.
- You pair every anomaly type with an investigation runbook to
accelerate resolution.
- You correlate anomalies to route agent-driven issues to
development teams and infrastructure issues to operations teams.

**Common anti-patterns:**

- Deploying anomaly detection without sufficient baseline data,
generating excessive false positives that undermine team
confidence.
- Relying solely on generic infrastructure monitoring that misses
agent-specific failure modes driving the highest costs.
- Detecting anomalies without investigation runbooks, leaving
costs escalating while teams figure out diagnostic procedures as
issues occur.
- Treating all cost spikes as equivalent when agent spikes have
different root causes (reasoning loops, tool storms, memory
growth) that require different remediation.
- Collecting anomaly insights without feeding them back into agent
design changes (tighter iteration limits, better prompts, tool
caching) that help prevent recurrence.

**Benefits of establishing this best
practice:**

- Proactive detection identifies cost escalation from
agent-specific failure modes within minutes rather than days.
- Investigation runbooks reduce mean time to resolution by
replacing ad-hoc analysis with guided diagnostic execution.
- Correlation analysis routes alerts to the right team (agent
development or operations), helping prevent triage delays.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Anomaly detection needs real baselines before it is useful.
Collect 2 to 4 weeks of baseline operational data before setting
thresholds, because detectors configured on insufficient history
produce false positives that erode confidence in the whole system.
[Amazon CloudWatch Anomaly Detection](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.html) automatically learns
statistical baselines for agent cost metrics and generates dynamic
anomaly bands that adapt to seasonality and trends. Apply it to
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) metrics including token
consumption per session, tool invocation frequency, memory growth,
and cost-per-task-completion. Use 2σ for
warning and 3σ for critical alerts.

Generic infrastructure monitoring doesn't catch the failure modes
that cost agents the most money. Reasoning loop token spikes, tool
invocation storms, and memory growth are agent-specific patterns,
and they need agent-specific detectors. Reasonable initial
thresholds include:

- Reasoning loop token spikes at 5x session average
- Tool invocation storms at 3x baseline rate
- Memory storage growth at 2x per hour
- Multi-agent workflow cost escalation at 2x historical average

These catch pathological behavior early enough to help prevent
material cost impact.

Correlation analysis helps make routing a sensible choice. An
agent-driven anomaly correlates with specific agent IDs in cost
allocation tags and shows up in AgentCore Observability token
consumption or invocation patterns. An infrastructure anomaly
happens independently of agent behavior and shows up in generic
service metrics. Routing agent-driven anomalies to development
teams (with context about which reasoning pattern triggered the
spike) and infrastructure anomalies to operations teams (with
context about constrained resources) keeps alerts in front of the
people who can act on them. AgentCore Observability span analysis
drills further. Is the spike in planning tokens, tool calls, or
memory growth? That determines whether the fix is a prompt change,
a tool cache, or a tighter memory policy.

[AWS Cost Anomaly Detection](https://docs.aws.amazon.com/cost-management/latest/userguide/manage-ad.html) provides a billing-level backstop.
Configured per agent cost allocation tag, it catches gradual
escalations that are not visible in operational metrics.
Investigation runbooks for each anomaly type (diagnostic queries,
likely root causes, and immediate mitigation actions) live in AWS Systems Manager OpsCenter, with CloudWatch Logs Insights queries
for traces, AWS X-Ray for distributed workflows, and AgentCore
Observability span analysis for token patterns.

### Implementation steps

- **Baseline, then detect:**
Collect 2 to 4 weeks of baseline data using
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html), then configure
[Amazon CloudWatch Anomaly Detection](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.html) on key cost indicators
with 2σ warning and 3σ critical thresholds.
- **Implement agent-specific
detectors:** Deploy Lambda-based detectors for
reasoning loop token spikes (5x session average), tool
invocation storms (3x baseline rate), memory growth
anomalies (2x per hour), and workflow cost escalation (2x
historical average), publishing structured anomaly events to
Amazon EventBridge.
- **Add billing-level anomaly
coverage:** Configure
[AWS Cost Anomaly Detection](https://docs.aws.amazon.com/cost-management/latest/userguide/manage-ad.html) monitors per agent cost
allocation tag as a backstop for gradual escalations.
- **Create investigation
runbooks:** Store runbooks for each anomaly type in
AWS Systems Manager OpsCenter, with diagnostic queries
(Amazon CloudWatch Logs Insights for traces, AWS X-Ray for
distributed workflows, AgentCore Observability span analysis
for token patterns) and mitigation actions.
- **Route anomalies through correlation
analysis:** Classify anomalies using cost
allocation tags and AgentCore Observability dimensions,
routing agent-driven anomalies to development teams and
infrastructure anomalies to operations teams.

## Resources

**Related best practices:**

- [AGENTCOST01-BP01
Use the reflection pattern to design efficient agent reasoning
loops](agentcost01-bp01.html)
- [AGENTCOST05-BP01
Establish agent-level reasoning cost tracking and
attribution](agentcost05-bp01.html)
- [AGENTCOST07-BP01
Implement automated cost controls with intelligent
cutoffs](agentcost07-bp01.html)
- [AGENTCOST07-BP03 Create
systematic optimization feedback loops for continuous
improvement](agentcost07-bp03.html)

**Related documents:**

- [Amazon CloudWatch Anomaly Detection](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.html)
- [AWS Cost Anomaly Detection](https://docs.aws.amazon.com/cost-management/latest/userguide/manage-ad.html)
- [Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html)

**Related examples:**

- [GitHub:
awslabs/amazon-bedrock-agentcore-samples - Observability
tutorials](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/06-AgentCore-observability)

**Related services:**

- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
- [AWS Cost Management](https://aws.amazon.com/aws-cost-management/)
- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentcost07-bp02.html*

---

# AGENTCOST07-BP03 Create systematic optimization feedback loops for continuous improvement

One-time optimization projects can miss compounding gains, as
cost-performance characteristics of agent systems shift as prompts
change, tools evolve, and traffic patterns drift. A monthly review
cadence, A/B-tested changes, and cost gates in the deployment
pipeline turn optimization into a continual practice that can keep
pace with the system.

**Desired outcome:**

- You hold monthly cost optimization reviews following a
structured agenda.
- You A/B test cost-impacting changes through controlled traffic
routing before fleet-wide promotion.
- You calculate cost-quality efficiency ratios to prioritize
optimizations by business value.
- You have cost gates in deployment pipelines helping prevent
accidental regressions.

**Common anti-patterns:**

- Cutting costs without measuring quality impact, degrading agent
performance and undermining business value.
- Treating cost optimization as an occasional initiative without
regular cadence, allowing inefficiencies to accumulate.
- Promoting optimizations across the entire fleet without A/B
testing, exposing all users to potential quality degradation.
- Tracking costs without correlating them to business outcomes or
setting quantitative improvement targets, reducing the risk of
data-driven prioritization.

**Benefits of establishing this best
practice:**

- Systematic review cycles continually identify high-impact
optimization opportunities with accountability for progress.
- A/B testing validates optimization hypotheses before deployment,
helping prevent costly mistakes from untested changes.
- Cost gates in deployment pipelines block changes that increase
costs without corresponding capability improvements.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Monthly reviews drive continual optimization. Structure it with
four sections:

- Cost efficiency trends (cost-per-decision,
cost-per-task-completion against targets)
- Top optimization opportunities ranked by impact and effort
- Experiment results from the previous month
- Next-month planning

[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) provides granular tracing
that can reveal opportunities invisible in aggregate metrics.
AgentCore Runtime tracing decomposes spend by reasoning pattern,
tool invocation, and memory operation, so you can see where to act
rather than just that action is needed. Set quarterly improvement
targets and track progress in Amazon CloudWatch dashboards and AWS Cost Explorer.

A/B testing is critical for continual optimizations. Use
[Amazon
Bedrock agent alias routing](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-manage.html) to split traffic between
control and treatment configurations. For each experiment, define
a hypothesis, success metrics covering both cost and quality, and
a minimum observation period for statistical significance. For
agent workloads where task completion quality varies more than in
traditional request-response patterns, plan on at least a 1-week
observation, a 10% traffic split, and at least 1,000 task
completions before calling a result.
[Amazon
Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html) runs standardized quality
assessments before and after each optimization so the cost
reduction isn't accompanied by a quality regression.

Prioritization needs a decision framework. Calculate a
cost-quality efficiency ratio as cost reduction percentage divided
by quality degradation percentage. Ratios above 10 indicate strong
opportunities where most of the quality is preserved per dollar
saved, and ratios below 2 signal that quality degradation is too
large relative to cost savings and should be deprioritized. This
framework lets reviewers rank candidate optimizations consistently
against each other.

[Amazon
Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) cost allocation features identify
memory-driven costs that should inform retention policy changes.
When expanding agent tool capabilities through
[Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html), measure tool invocation
frequency and reasoning cost before promotion rather than after.
[Amazon
Bedrock AgentCore Policy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html) provides deterministic constraints
if cost analysis shows agents over-invoking expensive tools. Cost
gates in the CI/CD pipeline compare estimated cost-per-task
against the current version and block deployment when the increase
exceeds threshold without a corresponding capability improvement.

### Implementation steps

- **Run a monthly optimization
review:** Use Amazon CloudWatch dashboards and AWS Cost Explorer for trend visualization, with a structured
agenda covering efficiency trends, opportunities, experiment
results, and next-month plans.
- **A/B test cost-impacting
changes:** Use
[Amazon
Bedrock agent alias routing](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-manage.html) with defined hypotheses
and success criteria covering both cost and quality.
Configure 10% traffic splits, 1-week minimum observation
periods, and 1,000 task completion minimums for statistical
significance.
- **Prioritize with cost-quality
ratios:** Use
[Amazon
Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html) to measure cost-quality
trade-offs and calculate efficiency ratios. Target ratios
above 10 for strong opportunities and deprioritize ratios
below 2.
- **Analyze phase and memory
costs:** Use
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) Runtime tracing to
identify per-phase reasoning cost patterns, and
[Amazon
Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) cost allocation to tune
retention policies.
- **Assess tool expansion cost before
promotion:** When adding capabilities through
[Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html), measure tool invocation
frequency and reasoning cost before promotion, and use
[Amazon
Bedrock AgentCore Policy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html) to constrain expensive tool
usage.
- **Add cost gates to CI/CD:**
Block deployments that exceed cost increase thresholds
without corresponding capability improvements.
- **Set quarterly improvement
targets:** Track progress against targets in the
monthly review so optimization is measurable, not
aspirational.

## Resources

**Related best practices:**

- [AGENTCOST02-BP02
Cost optimize token consumption through efficient prompt
engineering](agentcost02-bp02.html)
- [AGENTCOST05-BP01
Establish agent-level reasoning cost tracking and
attribution](agentcost05-bp01.html)
- [AGENTCOST05-BP04
Create chargeback and ROI reporting](agentcost05-bp04.html)
- [AGENTCOST07-BP01
Implement automated cost controls with intelligent
cutoffs](agentcost07-bp01.html)
- [AGENTCOST07-BP02
Establish proactive anomaly detection for agent cost
patterns](agentcost07-bp02.html)

**Related documents:**

- [Economics
for agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-economics/index.html)
- [Effective
cost optimization strategies for Amazon Bedrock](https://aws.amazon.com/blogs/machine-learning/effective-cost-optimization-strategies-for-amazon-bedrock/)
- [Operationalizing
agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-operationalizing-agentic-ai/introduction.html)
- [Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html)
- [Amazon
Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html)
- [Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html)
- [Amazon
Bedrock AgentCore Policy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html)
- [Guidance
for Cost Analysis and Optimization with Amazon Bedrock
Agents](https://aws.amazon.com/solutions/guidance/cost-analysis-and-optimization-with-amazon-bedrock-agents/)

**Related videos:**

- [AWS re:Invent 2024 - Sustainable and cost-efficient generative AI
with agentic workflows (AIM333)](https://www.youtube.com/watch?v=tFiDkSG2ess)

**Related examples:**

- [GitHub:
awslabs/amazon-bedrock-agentcore-samples - Observability
tutorials](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/06-AgentCore-observability)

**Related services:**

- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
- [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentcost07-bp03.html*

---

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
