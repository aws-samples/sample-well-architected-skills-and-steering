# AGENTSUS01 — Resource reusability

**Pillar**: Sustainability  
**Best Practices**: 5

---

# AGENTSUS01-BP01 Design specialized agents with explicit resource boundaries

Monolithic agents that over-provision for worst-case inputs waste
compute without reliable audit trails to track consumption. To make
consumption traceable at every layer, use specialized agents with
single atomic capabilities and explicit resource boundaries. Give
each agent a timeout, a memory ceiling, and a token budget. Each
unit of resource spend then maps back to the task that caused it.

**Desired outcome:**

- You have decomposed workflows into specialized agents, each
responsible for one atomic capability with declared resource
limits.
- Parent agents cascade resource budgets to child agents through
the orchestration layer, so delegation has predictable compute
and token costs.
- You track resource consumption for each agent (duration, tokens,
and error rates) across delegation chains so over-provisioning
is visible.
- Reusable specialized agents are exposed through a shared tool
layer, so one well-bounded agent serves many parent workflows.

**Common anti-patterns:**

- Provisioning compute and memory for worst-case inputs regardless
of actual task requirements, producing low utilization and
unnecessary cost.
- Delegating from parent agents to child agents without passing
timeout, retry, or token budgets, so downstream work has no
enforceable cost ceiling.
- Deploying monolithic agents that bundle multiple capabilities in
one process, which prevents independent scaling and makes
per-capability cost attribution infeasible.
- Duplicating implementations of a capability (validation,
extraction, or transformation) across workflows because no
shared agent exists with known resource bounds.

**Benefits of establishing this best
practice:**

- Resource consumption stays proportional to the task, because
each agent runs within bounds appropriate to its single
capability.
- Cost attribution is visible at the agent level. Over-provisioned
or underperforming agents are straightforward to identify and
right-size.
- Specialized agents amortize their development cost across many
parent workflows when exposed as reusable tools.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

The right unit of resource accountability is the capability, not
the deployment. When a single process handles validation,
enrichment, extraction, and decision-making, the only safe way to
size it is to assume every call does all four. Splitting those
capabilities into separate agents lets each one carry the timeout,
memory ceiling, and token budget that fit its actual work.
Right-sizing becomes a question about each capability rather than
a compromise across the whole workflow.

Budgets stop being useful the moment a delegation crosses a
boundary without carrying them along. The orchestration layer has
to propagate remaining time, remaining tokens, and retry budget
into every child invocation. In
[AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-nested-workflows.html), that means setting
TimeoutSeconds and retry counts on each nested
state. In a Strands-based orchestrator, it means passing the
remaining budget as part of the child invocation parameters.
Without that cascade, total workflow cost is unbounded regardless
of what the top-level agent promises.

When a single well-bounded data validation agent serves dozens of
parent workflows through
[Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) MCP server capabilities, its
development and optimization cost is amortized across every
caller.
[Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime.html) provides the session-isolated
execution environment that makes each invocation carry its own
resource context.
[Amazon
Bedrock AgentCore Policy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html) acts at the traffic boundary to
reject invocations that exceed declared limits before they consume
capacity.

[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) captures duration, token
counts, and error rates for each invocation across delegation
chains, so the utilization picture for each agent is the same at
every level of the hierarchy. Review consumption by agent monthly
to find agents that consistently run well below their declared
limits. Those are the first candidates for right-sizing.

### Implementation steps

- **Decompose workflows into
single-capability agents:** Identify atomic
functions in each workflow and deploy each as its own agent
on
[Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime.html) with explicit timeout,
memory, and token limits. Common atomic functions include:

Validation
- Extraction
- Transformation
- Decision

- **Cascade budgets across delegation
boundaries:** Configure the orchestration layer
([AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-nested-workflows.html) or a Strands-based orchestrator) to
pass the following into every child invocation so downstream
work inherits the parent's cost ceiling:

Remaining time
- Retry count
- Token budget

- **Expose specialized agents as
reusable tools:** Publish agents through
[Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) MCP server capabilities so
parent workflows invoke them without each embedding its own
copy.
- **Enforce limits at the traffic
layer:** Apply
[Amazon
Bedrock AgentCore Policy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html) Cedar rules at the Gateway
boundary to reject invocations that exceed declared resource
limits before they consume capacity.
- **Instrument consumption and review
monthly:** Turn on
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) to capture the
following for each agent:

Invocation duration
- Token counts
- Error rates

Review utilization in Amazon CloudWatch each month to
right-size boundaries against actual usage.

## Resources

**Related best practices:**

- [AGENTSUS01-BP02
Implement reusable workflow patterns](agentsus01-bp02.html)
- [AGENTSUS01-BP03 Optimize
resource utilization through shared services](agentsus01-bp03.html)
- [SUS03-BP01
Optimize software and architecture for asynchronous and
scheduled jobs](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_software_a2.html)
- [COST09-BP03
Supply resources dynamically](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_manage_demand_resources_dynamic.html)

**Related documents:**

- [Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime.html)
- [Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html)
- [Amazon
Bedrock AgentCore Policy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html)
- [Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html)
- [AWS Step Functions - Nested workflows](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-nested-workflows.html)
- [Introducing
Amazon Bedrock AgentCore Gateway: Transforming enterprise AI
agent tool development](https://aws.amazon.com/blogs/machine-learning/introducing-amazon-bedrock-agentcore-gateway-transforming-enterprise-ai-agent-tool-development/)
- [Strands
Agents](https://strandsagents.com/)

**Related examples:**

- [Build
multi-agent systems with LangGraph and Amazon Bedrock](https://aws.amazon.com/blogs/machine-learning/build-multi-agent-systems-with-langgraph-and-amazon-bedrock/)
- [GitHub:
awslabs/amazon-bedrock-agentcore-samples - Runtime
tutorials](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/01-AgentCore-runtime)

**Related services:**

- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [AWS Step Functions](https://aws.amazon.com/step-functions/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsus01-bp01.html*

---

# AGENTSUS01-BP02 Implement reusable workflow patterns

When every team rebuilds data retrieval, validation, and
transformation workflows from scratch, each rebuild costs
development time and pays for its own separate optimization cycle. A
library of parameterized patterns shifts that cost into a one-time
investment and makes subsequent projects compose from tested
building blocks instead of starting over.

**Desired outcome:**

- You have a catalog of parameterized workflow patterns for
recurring agent tasks (retrieval, validation, transformation,
and decision-making) that teams can discover and instantiate.
- Teams compose new agent systems from existing patterns before
writing new implementations.
- Each pattern has a documented interface, version history, and
declared resource profile, and a single pattern serves many
callers through a shared tool layer.
- You monitor pattern invocation frequency and failure rates so
optimizations to a pattern propagate to every caller.

**Common anti-patterns:**

- Building single-use workflows for each new project without
considering reuse, duplicating effort across teams and
accumulating technical debt as similar capabilities are
reimplemented with slight variations.
- Hardcoding workflow logic and decision points into individual
implementations instead of parameterizing them, making reuse of
proven patterns impractical.
- Developing reusable components without a central catalog or
documentation, so teams rebuild workflows that already exist
elsewhere in the organization.
- Treating workflows as disposable code rather than maintained
assets, skipping the testing, documentation, and versioning that
keeps patterns usable past their first deployment.

**Benefits of establishing this best
practice:**

- Each new agent project starts from proven, tested building
blocks instead of rebuilding from scratch, reducing the
redundant development and test cycles that dominate early
adoption.
- Behavior stays consistent across teams because every caller of a
pattern gets the same validated implementation.
- A single optimization to a shared pattern improves every caller
at once, amortizing future tuning work across the whole fleet.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

A pattern only becomes reusable when its parameters, inputs,
outputs, and failure modes are explicit. The recurring workflows
in agent systems, a retrieval chain with source selection, a
validation pipeline with schema checks, and a transformation stage
with format conversion, look the same across projects because the
shape of the work is the same. The part that varies is narrow.
It's which source, which schema, and which format. Making those
parameters part of the interface, rather than hardcoding them into
each implementation, allows one implementation to serve many
callers.

Discovery has to work at two different times. At design time, a
team evaluating whether to build something new needs to find out
what already exists. That is a documentation repository problem.
At runtime, an orchestrating agent needs to resolve a capability
to a concrete endpoint. That is a registry problem.
[Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) exposes patterns as MCP tools
with well-defined interfaces, so runtime discovery is built in.
The design-time catalog (a wiki page, a service catalog, or a
README) has to be maintained alongside the registry so teams can
browse capabilities, limitations, and resource requirements before
writing code.

Access controls and versioning keep shared patterns from being
forked silently by every team. Apply
[Amazon
Bedrock AgentCore Identity](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity.html) and Gateway policies so pattern
usage has a known footprint. Keep pattern versions explicit so
consumers can adopt a new version deliberately. Deploy the
underlying implementations on
[Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime.html) so each pattern has the same
operational baseline.

[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) exposes invocation
frequency, execution duration, and failure rates per pattern in
Amazon CloudWatch, so owners can tell which patterns are heavily
used (and therefore worth investing in) and which are sitting
unused (and are probably the wrong abstraction or undiscoverable).

### Implementation steps

- **Identify and extract recurring
patterns:** Audit existing agent workflows for
repeated sequences and pull each one out into a
parameterized template with a documented interface. Common
sequences include:

Retrieval
- Validation
- Transformation
- Decision

- **Deploy patterns as reusable
components:** Implement each pattern on
[Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime.html) and publish it through
[Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) as an MCP tool so
orchestrating agents can discover and invoke it at runtime.
- **Maintain a design-time
catalog:** Keep a documentation repository
alongside the Gateway registry where teams can browse the
following before writing new code:

Pattern purpose
- Parameters
- Resource profile
- Usage examples

- **Govern pattern access and
versions:** Apply
[Amazon
Bedrock AgentCore Identity](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity.html) and Gateway policies to
control who can invoke each pattern, and publish new
versions alongside old ones so consumers migrate
deliberately.
- **Monitor usage and feed improvements
back:** Track the following for each pattern
through
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html):

Invocation frequency
- Duration
- Failure rates

Use the telemetry to find heavily used patterns worth
investing in and stagnant patterns worth retiring.

## Resources

**Related best practices:**

- [AGENTSUS01-BP01 Design
specialized agents with explicit resource boundaries](agentsus01-bp01.html)
- [AGENTSUS01-BP03 Optimize
resource utilization through shared services](agentsus01-bp03.html)
- [SUS03-BP01
Optimize software and architecture for asynchronous and
scheduled jobs](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_software_a2.html)
- [OPS11-BP03
Iterate to improve](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_evolve_ops_iterate_to_improve.html)

**Related documents:**

- [Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html)
- [Introducing
Amazon Bedrock AgentCore Gateway: Transforming enterprise AI
agent tool development](https://aws.amazon.com/blogs/machine-learning/introducing-amazon-bedrock-agentcore-gateway-transforming-enterprise-ai-agent-tool-development/)
- [AWS Step Functions - State machine templates](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-templates.html)
- [Strands
Agents](https://strandsagents.com/)
- [Guidance
for Multi-Agent Orchestration on AWS](https://aws.amazon.com/solutions/guidance/multi-agent-orchestration-on-aws/)

**Related videos:**

- [AWS 2025 - Building AI Agents with Serverless, Strands, and MCP
(NTA405)](https://www.youtube.com/watch?v=LwubRSoJcIM)

**Related examples:**

- [GitHub:
aws-samples/aws-stepfunctions-examples](https://github.com/aws-samples/aws-stepfunctions-examples)

**Related services:**

- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [AWS Step Functions](https://aws.amazon.com/step-functions/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsus01-bp02.html*

---

# AGENTSUS01-BP03 Optimize resource utilization through shared services

Every agent that provisions its own connection pool, cache, or
processing queue pays the cost of infrastructure nobody else in the
fleet benefits from. Shared services turn those duplications into
one piece of infrastructure that every agent uses, so infrastructure
scales with organizational demand rather than agent count.

**Desired outcome:**

- You have common infrastructure, connection pools, caches, and
processing queues, consolidated into shared service layers that
every agent invokes rather than duplicates.
- Agents consume shared services through a tool abstraction, so
implementations can change without coupling to the callers.
- Shared caching and pooling reduce the total number of redundant
calls to external systems.
- Utilization of shared services is monitored so capacity scales
with actual demand rather than theoretical peaks.

**Common anti-patterns:**

- Deploying a separate cache, connection pool, and queue per
agent, so infrastructure cost scales linearly with agent count.
- Letting each agent open its own connections to external services
and fetch the same reference data repeatedly, producing
redundant network traffic and wasted compute.
- Treating each agent workflow as an isolated system, missing
opportunities to consolidate common functions like
authentication, logging, or queuing into a shared layer.
- Maintaining static allocations regardless of actual demand, so
shared infrastructure carries peak capacity even during
low-utilization periods.

**Benefits of establishing this best
practice:**

- A single optimization to shared infrastructure improves every
agent that uses it, amortizing operational work across the
fleet.
- Infrastructure investment grows with organizational demand
rather than proportional to agent count.
- Dynamic scaling on shared components contracts resources when
demand is low, which is hard to do when each agent runs its own
isolated stack.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

The infrastructure agents need is more repetitive than the work
they do. Authentication, caching, queuing, connection pooling, and
cross-agent retrieval all look the same no matter which agent is
calling them. When every agent provisions its own copy of this
plumbing, the organization pays for the same infrastructure N
times and optimizes it one team at a time. Consolidating into
shared layers reverses this. Infrastructure is optimized once and
every caller benefits.

A shared cache that agents call directly by host name creates
tight coupling. Swapping the implementation means updating every
caller. Exposing shared services through
[Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) MCP server capabilities puts a
stable interface in front of the implementation. The cache tier,
queue backend, or connection pool can change without the agents
noticing.
[Amazon
Bedrock AgentCore Identity](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity.html) centralizes authentication so
individual agents don't manage credentials independently, which is
the simplest form of shared infrastructure with immediate return.

For caching specifically, the implementation choice depends on the
data pattern.
[Amazon ElastiCache](https://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/BestPractices.html) fits general-purpose hot data with flexible
access patterns, and
[Amazon DynamoDB Accelerator (DAX)](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.html) fits DynamoDB-backed agent state
that needs microsecond reads without a separate cache layer. Both
are shared across agents once provisioned.
[Amazon
Bedrock cross-region inference](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html) distributes foundation model
requests across Regions so availability is shared at the inference
tier, not just at the application tier.

Deploy the agents themselves on
[Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime.html). Its serverless model means there
is no infrastructure footprint for each agent to consolidate in
the first place, which complements the shared-services pattern on
the supporting tier.
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) exposes cache hit rates,
queue depth, and invocation frequency for each shared service, so
utilization data drives scaling decisions rather than theoretical
peak estimates.

### Implementation steps

- **Identify common infrastructure
needs:** List the plumbing duplicated across
current deployments and consolidate each into a shared
service layer:

Connection pools
- Caches
- Queues
- Authentication

- **Deploy shared caching:**
Provision
[Amazon ElastiCache](https://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/BestPractices.html) for general-purpose hot data or
[Amazon DynamoDB Accelerator (DAX)](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.html) for DynamoDB-backed state,
so frequently accessed data is read from one cache rather
than refetched per agent.
- **Expose shared services through a
stable interface:** Publish shared infrastructure
as MCP tools through
[Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) so agents consume it
without coupling to the implementation.
- **Centralize
authentication:** Use
[Amazon
Bedrock AgentCore Identity](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity.html) to manage credentials once
rather than having every agent manage its own.
- **Distribute model
inference:** Turn on
[Amazon
Bedrock cross-region inference](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html) so foundation model
capacity is pooled across Regions for availability.
- **Track utilization and scale on
data:** Monitor the following through
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html), and adjust capacity
based on observed usage rather than worst-case estimates:

Cache hit rates
- Queue depth
- Invocation patterns

## Resources

**Related best practices:**

- [AGENTSUS01-BP01 Design
specialized agents with explicit resource boundaries](agentsus01-bp01.html)
- [AGENTSUS01-BP02
Implement reusable workflow patterns](agentsus01-bp02.html)
- [SUS03-BP02
Remove or refactor workload components with low or no
use](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_software_a3.html)

**Related documents:**

- [Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html)
- [Amazon ElastiCache best practices](https://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/BestPractices.html)
- [Amazon DynamoDB Accelerator (DAX)](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.html)
- [Amazon
Bedrock cross-region inference](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html)
- [Strands
Agents Tools](https://github.com/strands-agents/tools)

**Related examples:**

- [GitHub:
aws-samples/serverless-patterns](https://github.com/aws-samples/serverless-patterns)

**Related services:**

- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon ElastiCache](https://aws.amazon.com/elasticache/)
- [Amazon DynamoDB](https://aws.amazon.com/dynamodb/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsus01-bp03.html*

---

# AGENTSUS01-BP04 Scale cognitive processing pathways appropriately

Foundation model inference is the single most energy-intensive
operation in an agent workflow, and it runs hundreds or thousands of
times a day. Matching model size, retrieval depth, and memory scope
to actual task complexity keeps cognitive resource consumption
proportional to the value delivered, rather than defaulting every
call to the largest available model.

**Desired outcome:**

- You have tiered model routing in place, so each task goes to the
smallest model that meets its quality bar.
- Retrieval depth and context window size are scoped to task
complexity, so routine tasks don't carry the retrieval overhead
of complex reasoning.
- Multimodal extraction uses purpose-built services where
applicable, not raw vision models for every document.
- Agents operate within token budgets and rate limits enforced at
the runtime layer for each agent.

**Common anti-patterns:**

- Routing every request to the largest foundation model without
checking whether a smaller model or cached response would meet
the quality bar, which is the largest single opportunity for
energy reduction.
- Allowing agents to call models without token budgets or
concurrency limits, enabling single agents to consume
disproportionate resources under load.
- Configuring retrieval-augmented generation to return the same
context depth for every task regardless of complexity, producing
oversized context windows and redundant vector queries.
- Sending raw document images to large vision models when a
purpose-built extraction service would return the same
structured data at a fraction of the compute cost.

**Benefits of establishing this best
practice:**

- Cognitive resource consumption scales with task demand rather
than agent count, so the energy cost of scaling up agent fleets
stays proportional to the work they do.
- Token budgets for each agent help prevent one agent from
starving the rest of the fleet under load.
- Right-sizing across hundreds of daily model calls compounds into
substantial energy savings that are not visible on a single-call
basis.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

The Performance Efficiency pillar covers tiered model selection in
[AGENTPERF02-BP02
Implement task-appropriate model selection strategies](agentperf02-bp02.html). The
Cost Optimization pillar covers model cascading in
[AGENTCOST02-BP01
Architect tiered model selection for cost-performance
optimization](agentcost02-bp01.html). The sustainability view adds one thing. The
objective isn't latency or cost alone, but total energy and
compute footprint per unit of business value delivered. A task
taxonomy that ranks requests by reasoning complexity, then routes
them to appropriately sized
[Amazon
Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/models-supported.html) models, makes the routing data-driven rather than
default-to-biggest.

Tracking successful task completions divided by total compute
consumed gives a better signal than either metric alone. A
workflow that gets the right answer on the first try with a small
model is more sustainable than one that uses the largest model and
still retries. Tag invocations so this ratio can be calculated per
task category, and use it to shift routing thresholds over time.
With
[Amazon
Bedrock cross-region inference](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html), you can distribute
non-urgent requests to Regions with favorable energy profiles when
latency constraints permit.

Retrieval depth in
[Amazon
Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html) should be a parameter of the task,
not a constant. A routine question with a bounded answer doesn't
need the same retrieval fanout as a complex reasoning task.
Oversized retrieval wastes vector queries and bloats context
windows. For document-heavy workloads,
[Amazon
Bedrock Data Automation](https://docs.aws.amazon.com/bedrock/latest/userguide/bda.html) extracts structured data from
documents at a fraction of the compute cost of routing raw images
through a vision model. The cheaper path is often the better one.

Configure AgentCore Memory with tiered TTLs and automated pruning
so working memory doesn't grow unboundedly, and add semantic
caching so similar queries serve cached responses instead of
repeated invocations. Enforce token budgets and concurrency limits
for each agent through AgentCore Runtime execution constraints.
Measure actual consumption through
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) so thresholds stay tied to
observed reality.

### Implementation steps

- **Implement tiered model
routing:** Follow the patterns in
[AGENTPERF02-BP02
Implement task-appropriate model selection strategies](agentperf02-bp02.html)
and
[AGENTCOST02-BP01
Architect tiered model selection for cost-performance
optimization](agentcost02-bp01.html) to direct tasks to appropriately sized
[Amazon
Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/models-supported.html) models based on a complexity taxonomy.
- **Scope retrieval depth to task
complexity:** Parameterize
[Amazon
Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html) retrieval so vector queries
and context tokens scale with the work. Use tighter limits
for routine tasks and broader retrieval only for complex
reasoning.
- **Route document extraction to
purpose-built services:** For multimodal tasks, use
[Amazon
Bedrock Data Automation](https://docs.aws.amazon.com/bedrock/latest/userguide/bda.html) instead of sending raw images
through large vision models.
- **Apply memory lifecycle
policies:** Configure AgentCore Memory with tiered
TTLs and automated pruning so working memory stays bounded
and stale entries are removed automatically.
- **Enforce budgets and track
efficiency:** Set token budgets and rate limits for
each agent through AgentCore Runtime execution constraints,
and track successful completions per unit of compute
consumed through
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) to adjust routing
thresholds from data.

## Resources

**Related best practices:**

- [AGENTPERF02-BP02
Implement task-appropriate model selection strategies](agentperf02-bp02.html)
- [AGENTCOST02-BP01
Architect tiered model selection for cost-performance
optimization](agentcost02-bp01.html)
- [AGENTSUS01-BP01 Design
specialized agents with explicit resource boundaries](agentsus01-bp01.html)
- [SUS02-BP02
Align SLAs with sustainability goals](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_user_a3.html)

**Related documents:**

- [Amazon
Bedrock model support](https://docs.aws.amazon.com/bedrock/latest/userguide/models-supported.html)
- [Amazon
Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html)
- [Amazon
Bedrock Data Automation](https://docs.aws.amazon.com/bedrock/latest/userguide/bda.html)
- [Effective
cost optimization strategies for Amazon Bedrock](https://aws.amazon.com/blogs/machine-learning/effective-cost-optimization-strategies-for-amazon-bedrock/)
- [Build
trustworthy AI agents with Amazon Bedrock AgentCore
Observability](https://aws.amazon.com/blogs/machine-learning/build-trustworthy-ai-agents-with-amazon-bedrock-agentcore-observability/)
- [Agentic
AI patterns and workflows on AWS - Routing dynamic dispatch
patterns](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/routing.html)

**Related videos:**

- [AWS re:Invent 2024 - Sustainable and cost-efficient generative AI
with agentic workflows (AIM333)](https://www.youtube.com/watch?v=tFiDkSG2ess)

**Related examples:**

- [GitHub:
awslabs/amazon-bedrock-agentcore-samples - Evaluations
tutorials](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/07-AgentCore-evaluations)

**Related services:**

- [Amazon
Bedrock](https://aws.amazon.com/bedrock/)
- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsus01-bp04.html*

---

# AGENTSUS01-BP05 Adopt specification-driven tasks for frontier agents and long-running workflows

Long-running agents without explicit success criteria and resource
budgets drift into exploration that never quite terminates,
consuming compute hours on paths that don't deliver value.
Specifications that declare acceptable outputs, cost ceilings, and
termination conditions up front make extended execution a bounded
investment rather than an open-ended one.

**Desired outcome:**

- You have specifications for each frontier agent declaring
maximum execution duration, token budget, memory allocation, and
termination triggers before deployment.
- Long-running workflows pause at defined checkpoints to evaluate
progress against the specification, and decisions about
continuing, modifying, or terminating are informed by that
evaluation.
- Parent frontier agents cascade remaining budget and time to
child agents they spawn, so delegation inherits the parent's
ceiling.
- Specification compliance is monitored in production and feeds
back into template refinement for future frontier workflows.

**Common anti-patterns:**

- Deploying long-running agents without explicit resource budgets
or termination conditions, so unbounded exploration is
structurally possible.
- Omitting success criteria and decision-making boundaries from
frontier workflow configuration, producing wasteful execution
patterns where compute is consumed without commensurate value.
- Running extended workflows without checkpoint-based evaluation,
so nobody can make an informed decision about modifying or
terminating a run in progress.
- Spawning child agents from frontier workflows without passing
remaining budget downstream, breaking the cost ceiling at the
first delegation.

**Benefits of establishing this best
practice:**

- Extended workflows come with accountability, compute investment
is matched against business value generated rather than consumed
open-endedly.
- Checkpoint evaluations give operators a chance to redirect or
halt work before it burns disproportionate infrastructure.
- Specification templates accumulate institutional knowledge about
expected behavior for common frontier workload patterns.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Frontier agents, code writers, deep research agents, and
autonomous planners, are open-ended by design. That makes them the
place where resource discipline matters most, because the cost of
an unbounded exploration is many orders of magnitude higher than
the cost of a single misrouted call. A specification written
before deployment gives the agent something to terminate against:

- A success criterion that says "this is done"
- A token budget that caps total consumption
- A duration limit that helps prevent indefinite runs
- Explicit termination triggers for conditions where
continuation has become pointless

Without that contract, the agent runs until it happens to produce
something or hits an infrastructure-imposed ceiling.

Budgets must cascade for the specification to hold. When a
frontier parent delegates to child agents, the parent's ceiling
becomes meaningless unless the children inherit it. This is an
orchestration concern, not a platform feature. In
[AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-standard-vs-express.html), remaining budget is passed as parameters
into child workflow invocations. In a Strands-orchestrated system,
it is included in the child agent's system prompt or invocation
context. Make cascading explicit in the design rather than
assuming children inherit by convention.

Structure long-running workflows to pause at defined points, after
plan generation, after information gathering, and after each major
phase, and evaluate whether progress to date justifies continued
investment. Persist checkpoint state in AgentCore Memory so the
evaluation can pause and resume the agent without restarting it,
which preserves the sunk cost of work already done. Define the
specifications themselves through
[Strands
Agents](https://strandsagents.com/) as first-class configuration delivered at invocation
time through
[Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime.html). This way the contract travels
with the agent. Spec-driven development tools like
[Kiro](https://www.aboutamazon.com/news/aws/amazon-ai-frontier-agents-autonomous-kiro)
apply the same pattern to code-writing agents, giving them
directed and bounded instructions instead of open interpretation.

[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) tracks how often
specifications are violated, what checkpoints are producing useful
decisions, and where budgets are binding. Specifications that
never bind and workflows that always pass checkpoints signal
templates that should be loosened. Specifications that often bind
signal workloads that need tighter scoping or smaller sub-agents.

### Implementation steps

- **Write specifications before
deployment:** For each frontier agent, declare the
following and record the success criteria that define done:

Maximum execution duration
- Token budget
- Memory allocation
- Termination triggers

- **Deliver specifications at invocation
time:** Pass specifications into
[Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime.html) through
[Strands
Agents](https://strandsagents.com/) as first-class configuration, so the contract
is part of the invocation rather than implicit in the agent
code.
- **Cascade budgets to child
agents:** When a parent frontier agent delegates,
pass the remaining duration, token budget, and memory budget
into the child invocation through
[AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-standard-vs-express.html) parameters or Strands orchestration,
so the ceiling holds across delegation.
- **Implement checkpoint-based
evaluation:** Structure long-running workflows to
pause at defined points, evaluate progress against the
specification, and persist state in AgentCore Memory so the
agent resumes from the checkpoint after a
continue/modify/terminate decision.
- **Monitor adherence and refine
templates:** Track the following through
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html), and feed the data
back into specification templates for common frontier
workload patterns:

Specification violations
- Checkpoint outcomes
- Budget utilization

## Resources

**Related best practices:**

- [AGENTSUS01-BP01 Design
specialized agents with explicit resource boundaries](agentsus01-bp01.html)
- [AGENTSUS01-BP04 Scale
cognitive processing pathways appropriately](agentsus01-bp04.html)
- [SUS02-BP03
Stop the creation and maintenance of unused assets](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_software_a4.html)
- [COST02-BP02
Implement goals and targets](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_govern_usage.html)

**Related documents:**

- [AWS Frontier Agents](https://aws.amazon.com/ai/frontier-agents/)
- [Introducing
AWS Frontier Agents and Kiro](https://www.aboutamazon.com/news/aws/amazon-ai-frontier-agents-autonomous-kiro)
- [AWS Step Functions - Standard workflows](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-standard-vs-express.html)
- [Strands
Agents](https://strandsagents.com/)

**Related examples:**

- [Build
multi-step applications and AI workflows with AWS Lambda
durable functions](https://aws.amazon.com/blogs/aws/build-multi-step-applications-and-ai-workflows-with-aws-lambda-durable-functions/)

**Related services:**

- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [AWS Step Functions](https://aws.amazon.com/step-functions/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsus01-bp05.html*

---
