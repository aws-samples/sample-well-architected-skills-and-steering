# AGENTPERF02 — Core processing and reasoning pipeline optimization

**Pillar**: Performance Efficiency  
**Best Practices**: 4

---

# AGENTPERF02-BP01 Design efficient reasoning pipelines

Each iteration of the perceive-reason-act loop typically involves an
LLM inference call, so the number of iterations an agent takes
multiplies both latency and cost. An efficient pipeline reaches
accurate decisions in the fewest iterations the task requires, uses
bounded iteration limits and confidence-based early termination to
help prevent runaway loops, and handles retries within explicit
performance budgets rather than silently eroding them.

**Desired outcome:**

- You have per-task iteration limits and confidence-based early
termination configured, so reasoning loops can't run without
bounds.
- You have pipeline shapes that scale reasoning depth to task
complexity, with simple tasks resolving in one or two iterations
and complex tasks receiving the iterations they need.
- You have retry strategies bounded by explicit latency budgets,
with semantic re-prompting or graceful degradation engaged
before the end-to-end SLO is exceeded.
- You have average reasoning iterations per task tracked as a
first-class KPI, visible alongside latency and token metrics.

**Common anti-patterns:**

- Allowing agents to reason indefinitely without iteration limits
or early termination conditions, producing runaway loops that
consume tokens and time without improving output quality.
- Designing reasoning pipelines that always execute the same
sequence of steps regardless of task complexity, applying
heavyweight reasoning to simple tasks that could be resolved
with a single inference call.
- Designing retry strategies without performance budgets, so
exponential backoff retries accumulate latency that exceeds the
end-to-end SLO when semantic re-prompting or graceful
degradation would preserve performance targets.
- Retrying a failed LLM call with the identical prompt and model,
rather than re-prompting semantically, rephrasing the
instruction, simplifying the task, or falling back to a more
capable model, to increase the chance that the retry succeeds
inside the remaining latency budget.

**Benefits of establishing this best
practice:**

- Efficient pipeline design reduces the number of LLM inference
calls per task, which is one of the highest-impact optimizations
for agent latency and cost.
- Adaptive pipeline shape makes simple tasks resolve quickly while
complex tasks receive the iterations they need.
- Explicit retry budgets and semantic re-prompting keep tail
latency within SLO even when a tool or model call fails on the
first attempt.
- Iteration caps produce tighter latency distributions that
simplify capacity planning, auto scaling thresholds, and cost
forecasting.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Total latency and token spend scale with the number of iterations
the pipeline takes to reach an accepted output, so pipeline
design, how the loop is structured, when it terminates, and how
failures are handled has a multiplicative effect on both latency
and cost. A well-designed pipeline reaches an accepted output in
the fewest iterations the task actually requires.

The right pipeline shape depends on task complexity and
predictability.
[Basic
reasoning agents](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/basic-reasoning-agents.html) handle single-turn classification,
extraction, or summarization in one inference call and should not
be wrapped in iterative reasoning loops.
[ReAct-style
loops](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/agentic-ai.html), in which the agent interleaves reasoning, tool
calls, and observation, fit open-ended tasks where the next step
can't be predicted at design time.

Plan-then-execute shapes such as ReWOO and plan-and-solve hybrids
separate planning from execution and bound iteration by plan
length rather than by the model's willingness to keep looping, and
reflect-and-revise shapes such as Reflexion introduce explicit
critique cycles with hard caps on revision passes. Both patterns
are described in
[Customize
agent workflows with advanced orchestration techniques using
Strands Agents](https://aws.amazon.com/blogs/machine-learning/customize-agent-workflows-with-advanced-orchestration-techniques-using-strands-agents/).

Iteration caps and early termination are the two controls that
keep a loop from consuming resources without producing value, and
they serve complementary roles. A per-task iteration cap is an
upper bound that helps prevent pathological runaway (a model that
keeps calling tools without converging), and it must be set per
task class because a ceiling appropriate for multi-step research
is wasteful for a simple lookup.

Early termination ends the loop before the cap when additional
iterations would not improve the output. For example, when a
critique step returns a structured "no further revision
needed" signal, when the agent's own confidence assessment
exceeds a threshold, or when a deterministic validator (schema
check, grounding check, policy check) confirms the output is
acceptable.

Together, caps help prevent the worst case while termination
removes the common case of paying for unnecessary iterations.

Failure recovery is part of the latency budget, not an exception
to it. When a tool call or model inference fails, naive
exponential backoff can consume more time than the end-to-end
target allows. Every retry strategy should be bounded by an
explicit performance budget that specifies how much latency and
how many tokens retries can consume before the pipeline falls back
to a degraded response.

Identical retries against the same prompt and model frequently
fail for the same reasons:

- Semantic re-prompting (rephrasing the instruction, simplifying
the task, or tightening the output contract)
- Model escalation (routing the retry to a more capable model)
- Tool substitution (using an alternative data source)

Each of these failures change a variable in the failure mode and
increase the chance that the retry succeeds within the remaining
budget. To preserve user trust, implement strategies like graceful
degradation, returning a partial answer with marked gaps, a
lower-confidence answer with explicit uncertainty, or a clear
"can't complete" response before the latency target
is exceeded.

Average reasoning iterations per task belongs alongside latency,
tokens, and cost as a first-class performance KPI. It is the
earliest signal that pipeline shape, prompt quality, or upstream
tool reliability has drifted, because a rising iteration count
typically precedes a latency or cost regression. Each extra
iteration compounds with the others downstream before the
user-facing metric shifts enough to trigger an alarm.

Tracked by task class and by pipeline shape, iteration count also
reveals misrouted tasks like simple requests running through
heavyweight loops or complex tasks capped before they converge.
Both of these patterns are invisible to metrics that only measure
the end result.

### Implementation steps

- **Classify each agent task by
reasoning complexity:** Group tasks by the
reasoning depth they require, single-step extraction or
classification, multi-step reasoning over known steps, and
open-ended investigation where the path isn't knowable in
advance. Use this classification as the input to
pipeline-shape selection and iteration budgets, because
applying the same shape and budget to every class either
wastes iterations on simple work or under-reasons on complex
work. Document the classification alongside the workload's
success criteria so routing decisions can be audited and
revisited as task distributions change.
- **Select a pipeline shape that matches
each task class:** Map each class to a reasoning
pattern documented in
[Agentic
AI patterns and workflows on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/introduction.html), a
[basic
reasoning pattern](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/basic-reasoning-agents.html) for single-step tasks, a
[ReAct
loop](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/agentic-ai.html) for open-ended reasoning where tool use drives
the next step, and a plan-then-execute or reflect-and-revise
shape for tasks that benefit from an explicit planner or
critique stage as described in
[Customize
agent workflows with advanced orchestration techniques using
Strands Agents](https://aws.amazon.com/blogs/machine-learning/customize-agent-workflows-with-advanced-orchestration-techniques-using-strands-agents/). Avoid wrapping single-step tasks in
iterative loops, which inflates cost and latency with no
accuracy gain.
- **Set per-task iteration caps sized to
the complexity class:** Configure a hard maximum on
reasoning iterations for each task class using the
iteration-control primitive exposed by the agent framework
in use, and size the cap to a value the workload will hit
only on pathological cases. Caps are a floor on the worst
case, tasks that converge early still terminate early
through the confidence signals configured next, so tune caps
to the most complex variant of each class rather than to the
typical case.
- **Define early-termination conditions
so loops stop when iterations stop adding value:**
Specify structured signals that end the loop before the cap,
a critique step returning a boolean "revision
needed" flag, a confidence score exceeding a defined
threshold, or a deterministic validator (schema, grounding,
or policy check) confirming the output is acceptable. Treat
these signals as data the pipeline produces and logs, not as
implicit model behavior, so termination decisions are
observable and auditable rather than hidden inside a chain
of thought.
- **Establish a retry budget bounded by
the end-to-end latency target:** Allocate an
explicit portion of the end-to-end latency target to retry
handling and enforce it at the pipeline level so accumulated
retries can't silently exceed the target. Decompose the
budget into latency and token components, because a retry
that stays inside the latency budget but triples token
consumption still degrades unit economics. Align the budget
with the service level objective the workload is graded on
so retry behavior is measured against the same target as
everything else in the pipeline.
- **Replace identical retries with
semantic re-prompting, model escalation, or tool
substitution:** When a call fails, retry with a
rephrased instruction, a simpler task decomposition, a more
capable model, or an alternative tool, each changes a
variable in the failure mode instead of repeating the same
failing call. Select the substitution based on the failure
signal: a timeout suggests model escalation or tool
substitution, a parsing failure suggests re-prompting with a
stricter output contract, and a grounding failure suggests
retrieval expansion.
- **Configure graceful degradation paths
that return before the target is exceeded:** Define
the fallback response for each task class, a partial answer
with marked gaps, a lower-confidence answer with explicit
uncertainty, or a clear "unable to complete"
response, and invoke the fallback when the retry budget is
exhausted or the latency budget is within a configured
safety margin of being exceeded. Predictable tail behavior
and a clear failure response preserve user trust better than
maximizing the chance of an eventual success on every
request.
- **Emit reasoning iterations, retries,
and terminations as first-class telemetry:**
Publish iteration count, termination cause (early
termination, cap hit, retry-budget exhausted, graceful
degradation), and retry count for every invocation as
metrics that can be thresholded and alarmed alongside
latency and token metrics using a capability such as
[Amazon CloudWatch generative AI observability](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/GenAI-observability.html) or an
equivalent pipeline on the agent's runtime. Put average
iterations per task on the same dashboards as latency
percentiles and cost per completion, since it is the
earliest indicator that pipeline shape, prompt quality, or
tool reliability has drifted.
- **Review pipeline shape, caps, and
budgets against production telemetry on a defined
cadence:** Schedule regular reviews of iteration
distributions, early-termination rates, retry-budget
consumption, and degradation frequency so pipeline
parameters track actual behavior rather than launch-time
assumption. Tighten caps that are consistently
under-utilized, relax caps that are being hit on legitimate
complex tasks, and re-classify tasks whose iteration
distribution reveals they belong to a different complexity
class than originally assigned.

## Resources

**Related best practices:**

- [AGENTPERF02-BP02
Implement task-appropriate model selection strategies](agentperf02-bp02.html)
- [AGENTPERF02-BP03
Optimize agent execution paths for reduced latency](agentperf02-bp03.html)
- [AGENTPERF03-BP02
Optimize context window utilization and prompt
management](agentperf03-bp02.html)

**Related documents:**

- [Blog:
Customize agent workflows with advanced orchestration
techniques using Strands Agents](https://aws.amazon.com/blogs/machine-learning/customize-agent-workflows-with-advanced-orchestration-techniques-using-strands-agents/)
- [Foundations
of agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-foundations/introduction.html)
- [Agentic
AI patterns and workflows on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/introduction.html)
- [Agentic
AI - Generative AI Lens (Well-Architected Framework)](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/agentic-ai.html)
- [Amazon CloudWatch generative AI observability](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/GenAI-observability.html)

**Related tools:**

- [Strands
Agents](https://strandsagents.com/)

**Related services:**

- [Amazon
Bedrock](https://aws.amazon.com/bedrock/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentperf02-bp01.html*

---

# AGENTPERF02-BP02 Implement task-appropriate model selection strategies

Agent tasks vary widely in the reasoning they require, but default
routing often sends every task to the same large model, paying the
latency cost of a heavyweight model even for work a smaller one
resolves as well. Matching model capability to task demand is one of
the highest-use performance decisions in an agent system, because
inference latency and throughput scale directly with model size.
Done systematically, model selection reduces per-task latency
without sacrificing quality on complex reasoning.

**Desired outcome:**

- You have agent tasks classified by reasoning complexity, with
each class mapped to the smallest model that meets its quality
bar.
- You have routing logic that directs each request to its assigned
model at runtime, with a cascading fallback to a more capable
model when the assigned model produces low-confidence or failed
outputs.
- You have model assignments validated against benchmarked quality
and latency on the workload's own task distribution rather than
on generic leaderboard rankings.
- You have model selection treated as a runtime-configurable
parameter so new model releases can be evaluated and rolled out
without redeploying the agent.
- You have inference latency and task quality tracked per task
class, so routing decisions are continually validated against
both.

**Common anti-patterns:**

- Using a single large model for every agent task regardless of
complexity, paying the latency and cost premium of a heavyweight
model on work a smaller one resolves as well.
- Using a small or general-purpose model for tasks that require
deeper reasoning, producing low-quality outputs that trigger
retries, extra reasoning iterations, or manual escalation and
eroding the latency savings the small model was meant to
provide.
- Selecting models from general benchmark rankings rather than
from benchmarks run on the workload's own task distribution,
producing choices that are optimal for the leaderboard but
suboptimal for actual traffic.
- Treating model choice as a one-time architectural decision baked
into application code, so evaluating or rolling out a newly
released model requires a code change and redeploy rather than a
configuration update.
- Operating without a fallback path when the assigned model
returns low-confidence or failing outputs, forcing the pipeline
to return a poor answer or fail entirely rather than escalating
that request to a more capable model.

**Benefits of establishing this best
practice:**

- Routing lightweight work to smaller, faster models avoids paying
the inference time of a large model for tasks that don't require
it.
- Explicit routing to capable models and cascading fallback when a
smaller model underperforms protect user-facing accuracy on
complex tasks.
- Benchmarks against the workload's actual task distribution
continually improve assignments as new evaluation data
accumulates.
- Runtime-configurable selection lets capability and latency
improvements from new models reach production without redeploy
cycles.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

The reasoning pipeline's dominant cost component is the inference
call, and inference latency and throughput scale directly with
model size. Typical agent workloads have heterogeneous task mixes
and simple classification alongside multi-step reasoning, so
applying the largest model uniformly forces the blended latency
and cost to track the most capable option even though most
requests don't need it. Systematic model selection shifts this by
assigning each task to the smallest model that still meets its
quality bar.

Two approaches fit together:

- Explicit task classification, where the agent assigns each
task to a class and each class to a model or model tier, gives
fine-grained control and works across providers and model
families.
- Managed routing such as
[Amazon
Bedrock intelligent prompt routing](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-routing.html) predicts response
quality per request within a model family and routes to the
smallest model predicted to meet the quality bar, which hands
off the per-request pick when the decision is purely
capability-compared to-cost inside one family.

Many workloads combine both. The agent picks the tier by task type
while the router selects the specific model within that tier.
Purpose-built services such as
[Amazon
Bedrock Data Automation](https://docs.aws.amazon.com/bedrock/latest/userguide/bda.html) for intelligent document processing
are also worth considering as a model for document-heavy tasks,
where a dedicated pipeline is typically faster and more accurate
than routing documents through a general-purpose vision model.

Routing decisions are only as good as the benchmarks behind them.
Public leaderboards rank models on averages across heterogeneous
benchmarks whose task distributions can bear little resemblance to
a specific workload, so a model that leads a general benchmark can
underperform on the traffic a particular agent actually serves.

[Amazon
Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html) provides built-in evaluators,
LLM-as-a-Judge, ground-truth correctness, and trajectory matching
that make it practical to benchmark candidate models against an
evaluation set representative of actual traffic. Without
workload-specific evaluation, routing choices are effectively
guesses.

Selection is the starting point of a request, not the end of the
decision. Cascading fallback preserves quality without forcing the
whole task class to the larger model. Fallback differs from retry:
retries repeat the same call hoping for a better draw, while
fallback changes a variable by switching models. To promote new
models through progressive rollouts with automated rollback, hold
model identifiers, tier mappings, and fallback rules as runtime
configuration in
[AWS AppConfig](https://docs.aws.amazon.com/appconfig/latest/userguide/what-is-appconfig.html) feature flags (or a comparable config service),
combined with
[deployment
strategies](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-deployment-strategy-create.html) gated by CloudWatch alarms on latency and
quality.

Per-class latency, token consumption, quality scores, and
fallback-escalation rate belong on the same performance dashboards
as total latency and reasoning iteration counts. A rising fallback
rate on a class is an early indicator that the primary model no
longer fits, either because traffic has shifted or because a newly
available model would serve the class better. This typically shows
up before the user-facing regression is large enough to alarm.

### Implementation steps

- **Classify agent tasks by reasoning
complexity:** Group the workload's tasks into
classes based on the reasoning they require, for example,
single-step extraction or classification, structured
multi-step reasoning over known steps, and open-ended
investigation. Document representative examples per class so
routing decisions are auditable and can be revisited as task
distributions shift. Use the classification as the input to
model assignment rather than letting each caller pick a
model case by case.
- **Benchmark candidate models on the
workload's own task distribution:** Build an
evaluation set representative of production traffic and
score candidate models against it using
[Amazon
Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html) or an equivalent
evaluation harness. Capture quality signals (correctness,
goal success rate, tool-trajectory match) alongside latency
and tokens so you can identify the smallest model meeting
the quality bar for each class. Treat leaderboard rankings
as a starting shortlist, not as the decision.
- **Map each task class to a model or
model tier:** Define a small set of tiers, for
example, fast, standard, and advanced, and assign each class
to the tier that benchmarks demonstrate is sufficient. For
each tier, select a specific model or Amazon Bedrock
inference profile. Where routing within a family is the
goal,
[Amazon
Bedrock intelligent prompt routing](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-routing.html) can make the
per-request pick automatically. For document-heavy tasks,
consider
[Amazon
Bedrock Data Automation](https://docs.aws.amazon.com/bedrock/latest/userguide/bda.html) as the right example rather
than a general-purpose vision LLM.
- **Implement routing logic that
dispatches requests to the assigned model at
runtime:** Resolve the task-class-to-model mapping
at the start of each request and issue the inference call
against the chosen model. When crossing providers or model
families, a framework abstraction such as
[Strands
Agents model providers](https://strandsagents.com/docs/user-guide/concepts/model-providers/) keeps the routing code stable
as providers change underneath it.
- **Configure a cascading fallback to a
more capable model for low-confidence or failing
outputs:** Define structured signals, confidence
score below a threshold, schema validation failure, parse
error, or an explicit incomplete response, that escalate the
specific request to a more capable model. Limit the
escalation to a single step so tail latency stays
predictable, and log both the primary and fallback decision
for each request that escalates.
- **Externalize model assignments and
routing rules as runtime configuration:** Hold
model identifiers, task-class-to-tier mappings, and fallback
rules in
[AWS AppConfig](https://docs.aws.amazon.com/appconfig/latest/userguide/what-is-appconfig.html) feature flags (or an equivalent config
service) and read them at request time. Decoupling selection
from deployment lets new models be evaluated, promoted, or
rolled back without redeploying the agent.
- **Roll out model changes progressively
with automated rollback:** Use
[AWS AppConfig deployment strategies](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-deployment-strategy-create.html) to shift traffic to a
new model in steps with bake-time validation, and attach
CloudWatch alarms on latency and quality so the change rolls
back automatically when the alarm fires. Treating a model
swap as a monitored deployment makes frequent model updates
safe.
- **Emit per-task-class telemetry for
latency, tokens, quality, and fallback rate:**
Publish per-class metrics so the effect of each routing
decision is visible on dashboards and can be alarmed. Use
[Amazon CloudWatch generative AI observability](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/GenAI-observability.html) together with
[AgentCore
Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability-telemetry.html) to attribute latency, tokens, and
evaluation scores to the class and model that served each
request.
- **Review routing decisions against
production telemetry on a defined cadence:**
Schedule periodic reviews of per-class latency
distributions, fallback-escalation rates, and quality
scores, and re-run AgentCore Evaluations against newly
released models using the same task-distribution benchmark.
Promote, demote, or re-tier models based on observed data
rather than provider release cadence.

## Resources

**Related best practices:**

- [AGENTPERF01-BP03
Profile end-to-end agent latency and identify optimization
targets](agentperf01-bp03.html)
- [AGENTPERF02-BP01 Design
efficient reasoning pipelines](agentperf02-bp01.html)
- [AGENTPERF02-BP03
Optimize agent execution paths for reduced latency](agentperf02-bp03.html)
- [AGENTPERF02-BP04
Optimize streaming responses and time-to-first-token for agent
interactions](agentperf02-bp04.html)

**Related documents:**

- [Understanding
intelligent prompt routing in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-routing.html)
- [Evaluate
agent performance with Amazon Bedrock AgentCore
Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html)
- [Amazon
Bedrock Data Automation](https://docs.aws.amazon.com/bedrock/latest/userguide/bda.html)
- [What
is AWS AppConfig?](https://docs.aws.amazon.com/appconfig/latest/userguide/what-is-appconfig.html)
- [Create
a deployment strategy (AWS AppConfig)](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-deployment-strategy-create.html)
- [Amazon CloudWatch generative AI observability](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/GenAI-observability.html)
- [Foundations
of agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-foundations/introduction.html)
- [Economics
for agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-economics/introduction.html)
- [Blog:
Build reliable AI agents with Amazon Bedrock AgentCore
Evaluations](https://aws.amazon.com/blogs/machine-learning/build-reliable-ai-agents-with-amazon-bedrock-agentcore-evaluations/)
- [Strands
Agents Model Providers](https://strandsagents.com/docs/user-guide/concepts/model-providers/)

**Related videos:**

- [AWS re:Invent 2025 - Mastering model choice: The 3-step Amazon
Bedrock advantage (AIM391)](https://www.youtube.com/watch?v=Vu91YwZxskY)

**Related examples:**

- [GitHub:
Amazon Bedrock AgentCore samples, Evaluations](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/07-AgentCore-evaluations)

**Related workshops:**

- [Diving
Deep into Bedrock AgentCore, Evaluations](https://catalog.workshops.aws/agentcore-deep-dive/en-US/80-agentcore-evaluations)

**Related tools:**

- [Strands
Agents](https://strandsagents.com/)

**Related services:**

- [Amazon
Bedrock](https://aws.amazon.com/bedrock/)
- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [AWS AppConfig](https://aws.amazon.com/systems-manager/features/appconfig/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentperf02-bp02.html*

---

# AGENTPERF02-BP03 Optimize agent execution paths for reduced latency

Most of an agent request's total latency time is spent waiting on
model inference, retrieval, tool invocations, and memory lookups
rather than on CPU work inside the agent process. Executing
independent operations concurrently, reusing warm connections and
runtimes, and deduplicating repeated lookups within a single request
cut total latency without changing models or prompts.

**Desired outcome:**

- You have independent operations within an agent request executed
concurrently sequential execution is reserved for operations
with genuine data dependencies.
- You have connections to downstream services, model endpoints,
tool APIs, memory stores, vector indexes, pooled and reused
across requests rather than reestablished per invocation.
- You have runtime cold starts removed from the critical path or
bounded through provisioned capacity, pre-warming, or persistent
execution environments.
- You have repeated lookups within a single request resolved from
a request-scoped cache, so duplicate work isn't paid twice
inside one invocation.

**Common anti-patterns:**

- Executing independent operations sequentially when they share no
data dependencies, making total latency the sum of operation
durations rather than the slowest operation.
- Establishing new connections to model endpoints, tool APIs, or
data stores on every invocation, paying connection setup and TLS
handshake costs on the critical path.
- Running agent code on compute that pays a cold-start penalty on
the critical path without provisioned capacity, pre-warming, or
a persistent runtime to absorb it.
- Re-executing the same lookup multiple times within a single
request, for example, fetching the same knowledge base passage
or user profile across consecutive reasoning steps, with no
request-scoped cache to deduplicate the work.
- Introducing parallelism without respecting downstream rate
limits or connection pool capacity, so concurrent calls throttle
or queue and the intended latency win turns into added latency
plus failures.

**Benefits of establishing this best
practice:**

- Overlapping independent operations makes the critical path track
the slowest operation rather than the sum of every operation.
- Amortizing connection setup and runtime initialization across
requests avoids paying those costs on every invocation.
- Parallel calls that respect downstream capacity avoid the
throttling and retry storms naive parallelism triggers.
- Overlapping I/O-bound waits, retrievals and tool calls, with
compute-bound work such as inference and parsing keeps the agent
productive during waits.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Most of an agent request's total latency time is spent waiting, on
model inference, retrieval, tool invocations, and memory lookups,
rather than on CPU work inside the agent process. The structure of
how those waits are composed dominates total latency more than the
speed of any single downstream dependency. Four structural
decisions typically affect latency:

- Running independent operations concurrently rather than
sequentially
- Reusing warm connections and runtimes across invocations
- Removing cold starts from the critical path
- Deduplicating repeated lookups within a single request.

Each decision is independent of model and prompt choices, so the
gains compound with the reasoning-loop and model-selection
optimizations addressed elsewhere in this pillar.

Concurrency is the largest impact when the agent fans out across
independent data sources or tool calls. Dependency analysis
identifies operations that share no data dependency (for example,
a personalization lookup and a knowledge-base query issued from
the same reasoning step, and executes them in parallel so the
step's latency equals the slowest operation rather than the sum).

Agent frameworks expose this directly. Strands Agents executes
independent tool calls emitted in a single reasoning step
concurrently, and graph-based orchestrators such as LangGraph fan
out across independent edges. The constraint is downstream
capacity, where concurrent model calls and tool invocations must
respect
[Amazon
Bedrock service quotas](https://docs.aws.amazon.com/bedrock/latest/userguide/quotas.html) (requests-per-minute and
tokens-per-minute) and tool-API rate limits, or parallelism
converts into throttling and retry storms that undo the latency
win.

Connection reuse and cold-start removal address the per-invocation
setup costs that compound with concurrency. HTTP connections to
model endpoints and tool APIs should persist across invocations
through the SDK or HTTP-client connection pool rather than be
opened and torn down per request. Each fresh connection pays
TLS-handshake and connection-setup overhead on the critical path
that a pooled connection avoids entirely, and that overhead
accumulates across fan-out and across invocations.

Database connections follow the same principle.
[Amazon RDS Proxy](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy.html) pools connections to Aurora and RDS so serverless
agents don't exhaust database connection limits or pay
connection-setup latency per invocation. At runtime,
[Amazon
Bedrock AgentCore Runtime sessions](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-sessions.html) reuse a dedicated
microVM across invocations that share a session identifier, which
removes cold starts while a session is active and preserves
in-memory state across reasoning steps.

For agents hosted on AWS Lambda,
[Lambda
provisioned concurrency](https://docs.aws.amazon.com/lambda/latest/dg/provisioned-concurrency.html) pre-initializes execution
environments and
[Lambda
SnapStart](https://docs.aws.amazon.com/lambda/latest/dg/snapstart.html) restores from a cached snapshot on supported
runtimes, reducing first-invocation latency to sub-second at the
cost of continuous capacity or per-restoration charges.

Request-scoped caching addresses redundant work that happens
inside a single invocation rather than across invocations. A
reasoning loop that calls the same tool twice, retrieves the same
passage across successive steps, or refetches the same user
profile in the planner and the executor wastes latency budget on
repeated I/O. A cache keyed by the request or session identifier
deduplicates these lookups for the remainder of the request
without the consistency complexity of a cross-request cache.

The scope is deliberately narrow, persistent and cross-request
caches such as Amazon Bedrock prompt caching and semantic caches
are higher-level optimizations addressed in context- and
memory-focused best practices. However, request-scoped
deduplication is frequently the lowest-risk caching optimization
available, because the cache is discarded at the end of the
invocation and can't serve stale data to a subsequent request.

### Implementation steps

- **Profile the critical path to
identify parallelizable operations:** Trace a
representative sample of production requests with the
performance telemetry already in place to decompose each
invocation into per-operation durations and dependencies.
Identify operations that share no data dependency, separate
tool calls, independent retrievals, personalization lookups
alongside knowledge queries, and flag the sequential
segments where concurrency would collapse wall-clock latency
onto the slowest operation. Revisit the inventory as prompts
and tools change, because dependency graphs shift with them.
- **Execute independent operations
concurrently within downstream capacity limits:**
Configure the agent framework to fan out independent tool
calls and retrievals in the same reasoning step, Strands
Agents, LangGraph, and similar frameworks expose this as a
native primitive. Bound concurrency to the downstream
service's capacity,
[Amazon
Bedrock service quotas](https://docs.aws.amazon.com/bedrock/latest/userguide/quotas.html), tool-API rate limits, and
database connection ceilings, so a step that fans out to 10
concurrent calls doesn't trigger throttling that costs more
latency than it saves.
- **Reuse connections to model endpoints
and external APIs across invocations:** Configure
the HTTP client's connection pool so TLS sessions to Amazon
Bedrock and tool APIs persist across invocations rather than
being reestablished per request. On runtimes that preserve
memory across invocations,
[AWS Lambda execution environments](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtime-environment.html), container-based
services, and long-running services, initialize the client
once per execution environment rather than per invocation so
its connection pool survives across calls. A warm invocation
should pay zero connection-setup latency on downstream
calls.
- **Pool database connections through a
managed connection pool:** For agents that read
from or write to relational data, front Aurora and RDS
databases with
[Amazon RDS Proxy](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy.html) so serverless invocations share a bounded
pool of database connections rather than opening a new
connection each time. Without a pooler, concurrent agent
invocations exhaust the database's connection ceiling and
pay per-invocation setup latency on the critical path, both
failure modes worsen as parallelism increases.
- **Remove cold starts from the agent
execution runtime:** Select a runtime that keeps
the agent's execution environment warm on the critical path.
[Amazon
Bedrock AgentCore Runtime sessions](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-sessions.html) reuse a dedicated
microVM across invocations that share a session identifier,
preserving in-memory state and avoiding per-invocation cold
starts while the session is active. For Lambda-hosted
agents,
[Lambda
provisioned concurrency](https://docs.aws.amazon.com/lambda/latest/dg/provisioned-concurrency.html) pre-initializes execution
environments and
[Lambda
SnapStart](https://docs.aws.amazon.com/lambda/latest/dg/snapstart.html) restores from a cached snapshot on
supported runtimes. Always-on container services such as
Amazon ECS or Amazon EKS avoid cold starts entirely at the
cost of continuous capacity. Choose based on traffic shape
rather than runtime preference.
- **Deduplicate repeated lookups within
a single request using a request-scoped cache:**
Add an in-memory cache scoped to the lifetime of the request
or session that memoizes idempotent lookups, tool responses,
retrieved passages, user-profile reads, keyed by input. A
reasoning loop that calls the same tool twice or retrieves
the same passage across successive steps resolves the second
call from the cache, recovering that latency without the
consistency complexity of a cross-invocation cache. The
cache is discarded at the end of the request, so it can't
serve stale data to a subsequent invocation.
- **Re-measure the critical path after
each structural change and as traffic grows:**
After applying concurrency, pooling, cold-start, or caching
changes, re-profile the critical path under representative
production load to confirm the optimization held and did not
introduce new failure modes such as throttling or
connection-pool saturation. Repeat the measurement as
traffic grows, because parallelism bounded correctly at
launch frequently exceeds quotas at higher scale and the
latency profile silently regresses before an SLO is
exceeded.

## Resources

**Related best practices:**

- [AGENTPERF01-BP03
Profile end-to-end agent latency and identify optimization
targets](agentperf01-bp03.html)
- [AGENTPERF02-BP02
Implement task-appropriate model selection strategies](agentperf02-bp02.html)
- [AGENTPERF02-BP04
Optimize streaming responses and time-to-first-token for agent
interactions](agentperf02-bp04.html)
- [AGENTPERF03-BP04
Establish efficient agent caching and data access
patterns](agentperf03-bp04.html)

**Related documents:**

- [Amazon
Bedrock service quotas](https://docs.aws.amazon.com/bedrock/latest/userguide/quotas.html)
- [Amazon
Bedrock AgentCore Runtime sessions](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-sessions.html)
- [Amazon
Bedrock latency-optimized inference](https://docs.aws.amazon.com/bedrock/latest/userguide/latency-optimized-inference.html)
- [Amazon RDS Proxy](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy.html)
- [AWS Lambda execution environments](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtime-environment.html)
- [AWS Lambda provisioned concurrency](https://docs.aws.amazon.com/lambda/latest/dg/provisioned-concurrency.html)
- [AWS Lambda SnapStart](https://docs.aws.amazon.com/lambda/latest/dg/snapstart.html)
- [Building
serverless architectures for agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-serverless/introduction.html)

**Related tools:**

- [Strands
Agents](https://strandsagents.com/)

**Related services:**

- [Amazon
Bedrock](https://aws.amazon.com/bedrock/)
- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [AWS Lambda](https://aws.amazon.com/lambda/)
- [Amazon RDS Proxy](https://aws.amazon.com/rds/proxy/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentperf02-bp03.html*

---

# AGENTPERF02-BP04 Optimize streaming responses and time-to-first-token for agent interactions

User-facing agents are judged on perceived latency, not total
processing time. Time-to-first-token (TTFT), the delay before the
first output reaches the user, is the dominant perceived-performance
signal, and streaming delivery keeps TTFT short even when total
processing takes several seconds. Agentic streaming is complicated
by reasoning loops that must pause mid-stream to invoke tools and by
multi-agent workflows where the final agent streams while upstream
agents are still producing.

**Desired outcome:**

- You have TTFT tracked as a distinct KPI from end-to-end latency,
with a target bounded by the interaction type.
- You have LLM output streamed to the user as it is generated, so
the user begins seeing output well before the reasoning loop
finishes.
- You have pre-inference latency, context assembly, prompt
construction, retrieval, kept short enough that it doesn't
dominate TTFT.
- You have tool invocations handled within streams so the user
receives progress feedback rather than an unexplained pause when
the agent calls a tool mid-response.
- You have multi-agent workflows designed so the user-facing agent
begins streaming as soon as its inputs are available, rather
than blocking until every upstream agent fully completes.

**Common anti-patterns:**

- Waiting for the complete agent response before delivering any
output, making perceived latency equal to total processing time
rather than time-to-first-token.
- Streaming the LLM inference call but not the pre-inference
pipeline, so context retrieval and prompt construction add
seconds of delay before the first token reaches the user.
- Pausing the output stream with no indication when the agent
invokes a tool mid-response, so the user sees partial output
followed by an unexplained pause.
- Blocking multi-agent workflows until every upstream agent
finishes before the user-facing agent begins streaming,
converting sequential coordination delay into user-visible
latency.
- Treating TTFT as interchangeable with end-to-end latency in KPIs
and alarms, so regressions in time-to-first-token go unnoticed
while total-duration metrics look unchanged.

**Benefits of establishing this best
practice:**

- Sub-second time-to-first-token keeps the agent feeling fast even
when total processing time spans several seconds.
- Progress feedback replaces the unexplained pauses that would
otherwise appear to the user as a stall when tools run
mid-stream.
- Tracking TTFT as a distinct KPI surfaces drift in perceived
responsiveness that end-to-end latency dashboards would
otherwise hide.
- Progressive streaming in multi-agent workflows lets the
user-facing agent deliver output concurrently with upstream
processing rather than blocking until every upstream step
completes.
- A short TTFT reduces the share of users who abandon interactive
workloads before any output appears.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Time-to-first-token (TTFT) is typically the performance metric
that most directly shapes user perception of an interactive agent.
A response that begins within a few hundred milliseconds typically
feels fast to users even when total generation takes several
seconds. End-to-end latency and TTFT move independently. A faster
model improves total duration but leaves TTFT unchanged when the
pre-inference pipeline is the bottleneck, so tracking only total
latency hides the regressions users actually feel. The difference
lies in instrumenting TTFT as a distinct metric, separate from
total-duration dashboards.

Streaming the model's output is necessary but not sufficient: by
the time the first token leaves the model, the agent can already
have consumed the entire TTFT budget on work that happens before
inference begins. Context assembly, prompt construction,
retrieval, and serial pre-checks all count, and streaming recovers
nothing from that window.

The pre-inference path is usually where the most significant TTFT
improvements come from: compressing retrieval, narrowing retrieved
context, and parallelizing independent pre-inference steps. The
same concurrency and warm-connection patterns that reduce total
latency elsewhere in this pillar apply to the pre-inference path,
and they pay back specifically against TTFT. Post-inference
filtering is also in the budget.
[Amazon
Bedrock Guardrails streaming modes](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-streaming.html) introduce an explicit
trade-off between moderation accuracy and TTFT that must be tuned
to the workload rather than left at default.

On Amazon Bedrock,
[ConverseStream](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_ConverseStream.html)
is the model-agnostic streaming inference API recommended for chat
and agent workloads, while
[InvokeModelWithResponseStream](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeModelWithResponseStream.html)
remains available when a model-specific payload shape is required.
Both emit an event stream of content-block start, delta, and stop
events that the agent layer translates into user-visible output.

Tool invocation introduces a discontinuity. When the model decides
to call a tool, the event stream opens a content block of type
toolUse, streams the tool's input as deltas,
and then pauses while the agent runs the tool and feeds results
back. A client that receives no signal during this gap shows the
user partial output followed by a silent stall. The baseline
pattern, buffer-and-resume with an explicit progress indicator,
forwards a user-visible status the moment a tool-use block appears
and resumes streaming when the next content block starts. More
advanced patterns such as speculative streaming exist, but the
baseline is that no silent pause reaches the user.

Multi-agent pipelines amplify the TTFT problem when every upstream
agent must fully complete before the user-facing agent begins.
Each serial handoff contributes its full duration to TTFT rather
than overlapping with downstream work. Progressive streaming is
the alternative, where the user-facing agent begins reasoning as
soon as its minimum required inputs are available, and upstream
agents' intermediate outputs stream into its context as they are
produced.

Agent frameworks expose this pattern directly:
[Strands
Agents](https://strandsagents.com/) yields agent events (tokens, tool calls, messages)
as an async iterator that downstream consumers can subscribe to,
and graph-based orchestrators such as LangGraph expose equivalent
streaming primitives. Reserve synchronous full-response handoff
for workflows where the downstream agent genuinely can't begin
until the upstream result is complete.

Two AWS capabilities reduce inter-token latency and coordination
overhead beyond what API choice alone can deliver.
[Amazon
Bedrock latency-optimized inference](https://docs.aws.amazon.com/bedrock/latest/userguide/latency-optimized-inference.html) (in preview at
publication) reduces inter-token latency on supported models
through routing and capacity optimizations, at the cost of tighter
throughput limits and model-specific token ceilings. For voice and
real-time interactive workloads,
[Amazon
Bedrock AgentCore Runtime bi-directional streaming](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-bidirectional-streaming.html) over
WebSocket or WebRTC allows the client to send input while the
agent is still streaming output, the prerequisite for natural
interrupt and turn-taking behavior in voice agents.

[Amazon
Nova Sonic](https://docs.aws.amazon.com/nova/latest/userguide/speech.html) provides a speech-to-speech path on Amazon
Bedrock. You can route voice through Amazon Nova Sonic rather than
separate speech-to-text, text-generation, and text-to-speech
stages, collapsing multiple sequential stages into one
bidirectional stream. This approach typically provides substantial
TTFT improvements for voice workloads.

### Implementation steps

- **Define TTFT targets for each
user-facing interaction type:** Set a TTFT target
per workload based on how the user consumes output, text
chat tolerates hundreds of milliseconds, voice tolerates far
less, batch pipelines have no user-facing TTFT at all. Treat
the target as a budget to be allocated across pre-inference
work, model first-token latency, and any post-processing,
and anchor it to user research or published
interaction-design norms rather than a round number.
- **Instrument TTFT as two distinct
metrics, pipeline TTFT and model TTFT:** Emit
*pipeline TTFT* at the user-facing
boundary (the first output byte reaching the client) as the
SLO KPI, and *model TTFT* at the first
text delta from the inference call whose output first
streams to the user, which isolates model and routing
behavior from pre-inference and post-processing
contributions. Publish both through
[OpenTelemetry
through the CloudWatch OTLP endpoint](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html) or
[CloudWatch
Embedded Metric Format](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Embedded_Metric_Format_Specification.html). When pipeline TTFT and model
TTFT diverge, the gap points at the non-model contributors.
- **Extend TTFT instrumentation to
multi-inference and voice workloads:** When an
agent makes multiple inference calls per request, planners,
routers, sub-agent fan-outs, treat silent upstream calls as
part of the pre-inference budget and emit per-call TTFT as a
tagged dimension so the contribution of each inference call
remains visible for diagnosis. For voice workloads, add
time-to-first-audio-chunk because text-token arrival is an
upstream signal, not the user boundary.
- **Reduce pre-inference latency on the
critical path to the first token:** Profile the
work that happens between request arrival and the first
inference call, context assembly, retrieval, prompt
construction, pre-checks, and compress or parallelize it so
most of the TTFT budget remains when the model begins
generating. The concurrency and connection-reuse patterns
applied elsewhere to reduce end-to-end latency pay back
specifically against TTFT when applied to the pre-inference
path. Streaming token delivery can't recover any time lost
before the first model call.
- **Use streaming inference APIs rather
than synchronous inference for user-facing
agents:** Call
[ConverseStream](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_ConverseStream.html)
as the model-agnostic default for chat and agent workloads.
Use
[InvokeModelWithResponseStream](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeModelWithResponseStream.html)
only when a model-specific payload shape is required.
Consume the event stream as it arrives and forward each
content-block delta to the client rather than buffering the
full response server-side.
- **Tune Amazon Bedrock Guardrails
streaming mode when guardrails are in the critical
path:** If
[Amazon
Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-streaming.html) filters output on the user-facing
path, choose the stream processing mode based on the
workload's policy tolerance, synchronous processing raises
moderation accuracy and raises TTFT, asynchronous processing
preserves TTFT at the cost of potentially emitting a token
that is later retracted. Drive the decision for mode by the
content-risk profile of the workload.
- **Surface tool-invocation events to
the user rather than pausing the stream silently:**
When the model emits a tool-use event mid-stream, forward a
user-visible progress indicator to the client before the
agent begins executing the tool, and resume streaming when
the next content block starts. Use the explicit start and
stop boundaries of the tool-use content block as the signal
to transition the UI between streaming and working states,
rather than letting the client see a silent gap.
- **Stream multi-agent workflows
progressively rather than blocking on upstream
completion:** Design the orchestration so the
user-facing agent begins reasoning as soon as its minimum
required inputs are available, and pipe upstream
intermediate events into its context as they are produced.
Agent frameworks expose this streaming-handoff pattern
directly through async-iterator primitives such as
[Strands
Agents'](https://strandsagents.com/) streaming API and equivalent mechanisms in
graph-based orchestrators. Reserve synchronous full-response
handoff for workflows where the downstream agent genuinely
can't begin until the upstream result is complete.
- **Evaluate latency-optimized inference
for inter-token latency on supported models:**
[Amazon
Bedrock latency-optimized inference](https://docs.aws.amazon.com/bedrock/latest/userguide/latency-optimized-inference.html) (in preview at
publication) reduces inter-token latency on supported
models, Amazon Nova Pro, Anthropic Claude 3.5 Haiku, and
Meta Llama 3.1 70B/405B, through routing and capacity
optimizations, at the cost of tighter throughput limits and
model-specific token ceilings. Enable the latency mode on
the runtime API and validate with the two-metric TTFT
instrumentation that the reduction is real for the workload
rather than a cache-warmed artifact.
- **Use AgentCore Runtime bi-directional
streaming and Amazon Nova Sonic for voice and real-time
workloads:** For voice agents and other workloads
where the user must interrupt or turn-take, run the agent on
[Amazon
Bedrock AgentCore Runtime bi-directional streaming](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-bidirectional-streaming.html)
over WebSocket or WebRTC so the client can send input while
the agent is streaming output. Route voice specifically
through
[Amazon
Nova Sonic](https://docs.aws.amazon.com/nova/latest/userguide/speech.html), which collapses the separate
speech-to-text, text-generation, and text-to-speech stages
of a traditional voice pipeline into a single bidirectional
stream, typically a substantial TTFT improvement for voice
workloads.
- **Re-measure TTFT after each change
and as traffic shifts:** Re-profile both pipeline
TTFT and model TTFT under representative production load
after applying streaming, pre-inference, tool-handling, or
runtime changes, because optimizations that work in
isolation frequently regress at scale. Alert on TTFT
percentile violations distinct from end-to-end latency SLOs
so regressions in perceived responsiveness surface before
they reach users.

## Resources

**Related best practices:**

- [AGENTPERF01-BP03
Profile end-to-end agent latency and identify optimization
targets](agentperf01-bp03.html)
- [AGENTPERF02-BP02
Implement task-appropriate model selection strategies](agentperf02-bp02.html)
- [AGENTPERF02-BP03
Optimize agent execution paths for reduced latency](agentperf02-bp03.html)
- [AGENTPERF05-BP04
Implement efficient agent delegation and handoff
patterns](agentperf05-bp04.html)

**Related documents:**

- [Amazon
Bedrock ConverseStream API](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_ConverseStream.html)
- [Amazon
Bedrock InvokeModelWithResponseStream API](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_InvokeModelWithResponseStream.html)
- [Amazon
Bedrock latency-optimized inference](https://docs.aws.amazon.com/bedrock/latest/userguide/latency-optimized-inference.html)
- [Amazon
Bedrock Guardrails streaming](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-streaming.html)
- [Amazon
Bedrock AgentCore Runtime bi-directional streaming](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-bidirectional-streaming.html)
- [Get
started with bidirectional streaming using WebSocket on
AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-get-started-websocket.html)
- [Amazon
Nova Sonic, real-time conversational speech](https://docs.aws.amazon.com/nova/latest/userguide/speech.html)
- [CloudWatch
Embedded Metric Format specification](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Embedded_Metric_Format_Specification.html)
- [Publishing
custom metrics to Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html)
- [AWS blog: Bi-directional streaming for real-time agent
interactions now available in Amazon Bedrock AgentCore
Runtime](https://aws.amazon.com/blogs/machine-learning/bi-directional-streaming-for-real-time-agent-interactions-now-available-in-amazon-bedrock-agentcore-runtime/)

**Related examples:**

- [Amazon
Bedrock AgentCore samples, Runtime tutorials](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/01-AgentCore-runtime)
- [Amazon
Bedrock AgentCore samples, Nova Sonic integration](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/03-integrations/nova/nova-sonic)

**Related workshops:**

- [Diving
Deep into Bedrock AgentCore, Runtime](https://catalog.workshops.aws/agentcore-deep-dive/en-US/20-agentcore-runtime)

**Related tools:**

- [Strands
Agents](https://strandsagents.com/)

**Related services:**

- [Amazon
Bedrock](https://aws.amazon.com/bedrock/)
- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentperf02-bp04.html*

---
