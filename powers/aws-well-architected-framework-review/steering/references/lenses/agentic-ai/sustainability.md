# Sustainability

**Pillar**: Sustainability  
**Questions**: 3

---

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

# AGENTSUS02 — Resource right-sizing

**Pillar**: Sustainability  
**Best Practices**: 4

---

# AGENTSUS02-BP01 Optimize context management and memory utilization

Agent memory that grows without bounds forces every retrieval to
search through increasingly large stores and every turn to reprocess
history the agent has already seen. Tiered memory with retention
policies keeps infrastructure scaled to the context that actually
matters, so memory operations stay fast and memory cost stays
proportional to use.

**Desired outcome:**

- You have tiered memory with active session context separated
from archival data, so hot and cold tiers are not competing for
the same storage.
- Retention, archival, and pruning policies keep memory bounded
and automatically move aging context to the appropriate tier.
- Multi-agent systems share persistent context through namespaces
rather than duplicating it per agent.
- Agents incrementally build context rather than reprocessing full
interaction histories on every turn.

**Common anti-patterns:**

- Implementing flat memory without tiering, so hot session context
competes with archival data for the same storage and access
path.
- Skipping retention, archival, and pruning policies, letting
memory accumulate indefinitely and forcing each retrieval to
scan a larger and larger store.
- Reprocessing complete historical context on every turn instead
of pulling only the relevant slice, producing redundant
retrieval operations that don't improve response quality.
- Duplicating shared context across each agent's memory store
rather than reading from a shared namespace, producing linear
storage growth with agent count.

**Benefits of establishing this best
practice:**

- Memory infrastructure scales with the context that actually
matters, not with cumulative history.
- Semantic retrieval returns the relevant slice of context in
constant time rather than scaling with store size.
- Multi-agent systems share storage for common context, reducing
duplicated memory across the fleet.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Not all agent context is equally active. A recent turn in an
ongoing session behaves very differently from a transcript from
three months ago. The first needs millisecond access on every
turn, and the second needs availability for occasional retrieval.
[Amazon
Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) provides built-in tiering that
separates these cases, with working memory optimized for active
sessions and long-term storage for older context. Retention
policies move context between tiers automatically, so the hot tier
stays small and the cold tier stays cheap.

Shared persistent context is a part of the architecture where many
multi-agent systems fail. When five agents each maintain their own
copy of the same reference material, storage grows five times
faster than the organizational demand warrants. AgentCore Memory's
namespace-based organization lets multiple agents read from and
write to common namespaces scoped by IAM policies, one store and
many readers. This is shared storage, not shared in-process
memory, so consistency and access control stay explicit.
Separately,
[Amazon
Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html) is the right home for
organizational knowledge, FAQs, and reference documentation that
agents query to enrich context. It complements AgentCore Memory
rather than replaces it.

Sending the full interaction history into every model call looks
correct but pays to reprocess information the model already saw.

The better pattern is incremental. Maintain stateful sessions that
preserve working context across turns, summarize older segments
into compact representations when they age out of the immediate
window, and use semantic search through Knowledge Bases with
vector embeddings to retrieve only the relevant slice of history
rather than the whole transcript.
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) exposes which memory
operations are frequent and which tiers are under- or
over-utilized, so allocation stays grounded in actual usage.

### Implementation steps

- **Configure tiered memory with
lifecycle policies:** Use
[Amazon
Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) for active session context
with retention policies that automatically move aging
context to long-term storage.
- **Set up shared namespaces for
multi-agent context:** Create AgentCore Memory
namespaces that multiple agents read from and write to,
scoped by IAM policies, so shared persistent context is
stored once rather than duplicated per agent.
- **Use semantic retrieval for
historical context:** Configure
[Amazon
Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html) with vector embeddings so
queries retrieve only the relevant slice of historical
context rather than full transcripts.
- **Compress aging context:**
Apply summarization using Amazon Bedrock foundation models
to condense older interaction segments into compact
representations that preserve meaning at a fraction of the
token cost.
- **Monitor memory access patterns and
rebalance tiers:** Track tier hit rates, retrieval
latency, and store size through
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) and adjust retention
windows and tier allocations based on observed usage.

## Resources

**Related best practices:**

- [AGENTSUS02-BP02
Establish efficient agent caching strategies](agentsus02-bp02.html)
- [AGENTSUS02-BP03
Appropriately scale data, networking, and compute
dependencies](agentsus02-bp03.html)
- [SUS02-BP01
Scale workload infrastructure dynamically](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_user_a2.html)

**Related documents:**

- [Amazon
Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html)
- [Amazon
Bedrock AgentCore Memory: Building context-aware agents](https://aws.amazon.com/blogs/machine-learning/amazon-bedrock-agentcore-memory-building-context-aware-agents/)
- [Building
smarter AI agents: AgentCore long-term memory deep dive](https://aws.amazon.com/blogs/machine-learning/building-smarter-ai-agents-agentcore-long-term-memory-deep-dive/)
- [Amazon
Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html)
- [Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html)

**Related videos:**

- [AWS 2025 - AgentCore Deep Dive: Memory](https://www.youtube.com/watch?v=-N4v6-kJgwA)

**Related examples:**

- [GitHub:
awslabs/amazon-bedrock-agentcore-samples - Memory
tutorials](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/04-AgentCore-memory)

**Related services:**

- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon
Bedrock](https://aws.amazon.com/bedrock/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsus02-bp01.html*

---

# AGENTSUS02-BP02 Establish efficient agent caching strategies

Every duplicate model call, tool invocation, and memory lookup is
work the agent fleet has already done once. Caching at each
integration point turns repeated work into a one-time cost amortized
across every caller, so resource efficiency improves as usage
patterns stabilize rather than scaling linearly with traffic.

**Desired outcome:**

- You have caching applied at each integration point, prompt
prefixes, tool results, memory lookups, and credential
validation, with TTLs matched to data volatility.
- Cache layers are shared across the agent fleet so one agent's
cached result benefits every other agent.
- Cache hit rates are tracked per integration point and improve as
usage patterns stabilize.
- Invalidation policies help prevent stale responses where data
volatility demands freshness.

**Common anti-patterns:**

- Making repeated calls to the same foundation model with the same
stable prompt prefix instead of caching it, paying to reprocess
the same tokens on every invocation.
- Caching tool results and model responses without invalidation or
TTL policies, producing stale answers that appear fresh.
- Running caches isolated to each agent that don't share across
the fleet, so each agent has to re-warm its own cache rather
than benefiting from cached results elsewhere.
- Skipping cache instrumentation, so nobody knows which
integration points have low hit rates and would benefit from a
different caching strategy.

**Benefits of establishing this best
practice:**

- Redundant processing, API calls, and network traffic are reduced
at each integration point, so infrastructure cost grows
sublinearly with agent usage.
- Shared cache layers mean adding agents to the fleet increases
cache hit rate rather than cache pressure.
- Resource efficiency compounds over time as cache hit rates climb
toward their steady-state maximum.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

The sustainability view of prompt caching adds one additional
consideration to this lens' existing performance and cost
perspectives. The value of caching isn't just latency or cost for
each call. It's cumulative compute and energy footprint across the
lifetime of the fleet, and the way caching is shared determines
how that cumulative footprint grows.

Caches isolated to each agent don't compound. If five agents each
maintain their own cache, the fleet warms five caches instead of
one, and cross-agent hits never happen. Shared cache layers
exposed through
[Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) MCP server capabilities reverse
this. Every agent reads from and writes to the same cache tier, so
one agent's tool result becomes the next agent's cache hit. The
same principle applies at the authentication layer.
[Amazon
Bedrock AgentCore Identity](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity.html) caches tokens so credential
validation happens once per session across the fleet rather than
once for each agent.

[Amazon
Bedrock prompt caching](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-caching.html) pays off fastest. Stable system
prompts, the long preambles that set agent behavior, can be cached
at the model layer so subsequent invocations skip reprocessing the
prefix. Semantic caching adds a complementary layer where similar
(not identical) queries serve cached responses after an
embedding-based match, which is especially valuable for the long
tail of paraphrased questions users ask.

Invalidation is where caching strategies can fail. A cache TTL
calibrated to daily refresh on data that actually changes hourly
serves stale content. A TTL too short to matter wastes the cache's
whole purpose. Pick TTLs based on how often the underlying data
actually changes, and track hit rates through
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) so low-performing
strategies get tuned rather than left in place.

### Implementation steps

- **Enable prompt caching for stable
prefixes:** Turn on
[Amazon
Bedrock prompt caching](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-caching.html) for stable system prompts
following the patterns in
[AGENTPERF03-BP04
Establish efficient agent caching and data access
patterns](agentperf03-bp04.html) and
[AGENTCOST02-BP03
Leverage intelligent caching to reduce redundant model
invocations](agentcost02-bp03.html).
- **Share cache layers across the
fleet:** Expose tool result and semantic caches
through
[Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) MCP server capabilities so
every agent reads from and writes to the same store.
- **Cache credential
validation:** Use
[Amazon
Bedrock AgentCore Identity](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity.html) to cache tokens so
authentication overhead happens once per session rather than
once per agent invocation.
- **Set TTLs based on data
volatility:** Pick invalidation policies calibrated
to how often the underlying data actually changes, shorter
for live operational data, longer for stable reference
material.
- **Monitor and refine hit
rates:** Track cache hit rates per integration
point through
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) and adjust strategies
where hit rates are below expectations.

## Resources

**Related best practices:**

- [AGENTPERF03-BP04
Establish efficient agent caching and data access
patterns](agentperf03-bp04.html)
- [AGENTCOST02-BP03
Leverage intelligent caching to reduce redundant model
invocations](agentcost02-bp03.html)
- [AGENTSUS02-BP01 Optimize
context management and memory utilization](agentsus02-bp01.html)
- [SUS03-BP03
Optimize areas of code that consume the most time or
resources](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_software_a4.html)

**Related documents:**

- [Amazon
Bedrock prompt caching](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-caching.html)
- [Effectively
use prompt caching on Amazon Bedrock](https://aws.amazon.com/blogs/machine-learning/effectively-use-prompt-caching-on-amazon-bedrock/)
- [Optimize
LLM response costs and latency with effective caching](https://aws.amazon.com/blogs/database/optimize-llm-response-costs-and-latency-with-effective-caching/)
- [Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html)

**Related services:**

- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon
Bedrock](https://aws.amazon.com/bedrock/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsus02-bp02.html*

---

# AGENTSUS02-BP03 Appropriately scale data, networking, and compute dependencies

Agent workloads have a shape that general-purpose infrastructure
defaults don't fit, with bursty inference, variable-length tool
execution, and unpredictable multi-step reasoning. Sizing hosting,
network, and storage to the observed pattern rather than a
theoretical maximum keeps infrastructure proportional to agentic
work.

**Desired outcome:**

- Agent processes run on serverless infrastructure that scales
with demand instead of static provisioning for peak load.
- Private connectivity is used where security or latency
requirements justify it, not by default for every workload.
- Agent infrastructure is deployed close to the services it
depends on, so cross-Region data transfer is minimized.
- Streaming responses are used for user-facing interactions to
reduce memory footprint and improve time-to-first-token.
- Utilization is monitored continually and provisioning tracks
actual workload demand.

**Common anti-patterns:**

- Applying general-purpose infrastructure configurations without
analyzing the bursty inference call patterns and variable tool
execution durations specific to agent workloads, producing
wasteful over-allocation or performance-degrading
under-provisioning.
- Maintaining static provisioning regardless of demand, reducing
the ability for infrastructure to contract during low-activity
periods.
- Sizing for theoretical maximum scenarios instead of right-sizing
against actual demand, producing low utilization during normal
operations.
- Deploying agent infrastructure far from the services it depends
on, producing cross-Region network traffic that adds latency and
transfer cost.

**Benefits of establishing this best
practice:**

- Infrastructure consumption tracks demand, contracting when
agents are idle and expanding during peak periods.
- Energy consumption stays proportional to the work agents deliver
rather than their theoretical peak capacity.
- Private connectivity and Region colocation reduce network path
length and latency where it matters.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Running agents on serverless infrastructure solves most of the
static-provisioning problem by design.
[Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime.html) right-sizes compute per
invocation with session-isolated execution, so the orchestration
overhead is scoped to the session that's actually running. There's
no fleet of idle EC2 instances to size against worst-case demand,
because the execution unit is the invocation rather than the
instance. This default makes bursty workloads affordable.

Private networking is about matching the connection pattern to the
workload's actual needs. Some agents process sensitive data or
have latency requirements tight enough that public internet
routing is the bottleneck. For those workloads,
[VPC
interface endpoints for Amazon Bedrock AgentCore (AWS PrivateLink)](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/vpc-interface-endpoints.html) establishes private paths that reduce latency
and keep traffic off the public internet. For workloads without
those requirements, PrivateLink adds operational complexity
without proportional benefit. Default to the public endpoint and
promote workloads to PrivateLink when security or latency demands
it.

Deploying agent infrastructure in the same AWS Region as
frequently accessed Amazon Bedrock endpoints and AgentCore
services reduces cross-Region data transfer overhead that
compounds across thousands of daily invocations. For availability,
[Amazon
Bedrock cross-region inference](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html) distributes foundation model
requests across Regions. This is complementary rather than
contradictory. Use cross-Region inference for failover and burst
capacity, and keep the primary data path local.

Streaming responses change the memory profile of user-facing
interactions. Without streaming, the agent accumulates the full
response in memory before returning it, which means peak memory is
proportional to response length. With streaming, tokens flow as
they're generated and memory stays bounded. Turning on streaming
in AgentCore reduces footprint for long-form interactions and
improves time-to-first-token for users.
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) exposes the utilization
data that keeps provisioning tied to actual workload demand.

### Implementation steps

- **Run agent processes on serverless
runtime:** Deploy to
[Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime.html) for automatic scaling and
session isolation, so execution capacity scales with demand
rather than peak estimates.
- **Apply private connectivity where
justified:** Configure
[VPC
interface endpoints for Amazon Bedrock AgentCore (AWS PrivateLink)](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/vpc-interface-endpoints.html) for workloads with security or latency
requirements that warrant it. Default to public endpoints
otherwise.
- **Deploy in the same Region as
dependencies:** Place agent infrastructure in the
Region hosting the Amazon Bedrock endpoints and AgentCore
services it uses most, and turn on
[Amazon
Bedrock cross-region inference](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html) for availability.
- **Enable streaming for user-facing
responses:** Turn on AgentCore streaming so
response tokens flow as they're generated, reducing memory
footprint and improving time-to-first-token.
- **Validate utilization
continually:** Track infrastructure utilization
through
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) and adjust
provisioning where observed demand is meaningfully below
allocation.

## Resources

**Related best practices:**

- [AGENTSUS02-BP01 Optimize
context management and memory utilization](agentsus02-bp01.html)
- [AGENTSUS02-BP04 Measure
and optimize the environmental footprint of agent
workloads](agentsus02-bp04.html)
- [SUS02-BP01
Scale workload infrastructure dynamically](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_user_a2.html)

**Related documents:**

- [Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime.html)
- [VPC
interface endpoints for Amazon Bedrock AgentCore (AWS PrivateLink)](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/vpc-interface-endpoints.html)
- [Amazon
Bedrock cross-region inference](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html)
- [Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html)

**Related services:**

- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon
Bedrock](https://aws.amazon.com/bedrock/)
- [AWS PrivateLink](https://aws.amazon.com/privatelink/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsus02-bp03.html*

---

# AGENTSUS02-BP04 Measure and optimize the environmental footprint of agent workloads

Without measurement, sustainability claims are aspirational and
optimizations are not tracked against real-world data. Tracking the
environmental footprint of agent workloads makes sustainability an
engineering metric. Baselines show where effort is worth investing,
and trends show whether changes are actually working.

**Desired outcome:**

- You have carbon emissions baselines for agent infrastructure
established across a defined observation period.
- Resource efficiency metrics for each task (tokens per successful
completion, compute hours per workflow, and cache hit rates) are
tracked alongside business outcomes.
- Deferrable workloads are scheduled during off-peak periods or
routed to Regions with favorable energy profiles.
- Operational and sustainability metrics are combined in
dashboards that inform periodic optimization reviews.

**Common anti-patterns:**

- Claiming sustainability benefits from agent optimizations
without establishing baselines, making it impossible to validate
whether changes actually reduced impact.
- Treating every workload as equally time-sensitive, running batch
processing and background tasks during peak hours when deferring
them would reduce contention and energy consumption.
- Ignoring regional differences in energy infrastructure when
selecting deployment Regions for workloads with flexible latency
requirements.
- Tracking only infrastructure utilization without tying it to
business outcomes, so efficiency gains in compute don't connect
to value delivered.

**Benefits of establishing this best
practice:**

- Measurable baselines make sustainability improvements verifiable
instead of aspirational.
- Optimization effort flows to the workloads with the largest
environmental impact, rather than being applied uniformly.
- Deferrable workloads run when infrastructure is underutilized,
improving fleet-wide efficiency without affecting user-facing
performance.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

[AWS Sustainability](https://docs.aws.amazon.com/sustainability/latest/userguide/what-is-sustainability.html) provides carbon emissions tracking with
service and Region breakdowns for the infrastructure side, and
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) adds agent-specific
metrics, tokens per successful task, compute hours per workflow,
and cache hit rates that tie consumption to business outcomes.
Establish baselines across a 30-day observation window so that
normal workload variation is included, and track trends monthly
afterward so optimization work can be validated against measured
change rather than claimed change.

Not every agent workload has the same latency sensitivity.
User-facing interactions need low-latency responses. Batch jobs,
periodic knowledge base indexing, bulk data enrichment, evaluation
runs, and non-interactive research workflows can wait hours or
overnight without affecting the user. Shifting deferrable work to
off-peak periods reduces resource contention on shared
infrastructure and takes advantage of time windows when the
broader grid is cleaner.
[Amazon
Bedrock cross-region inference](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html) extends the same principle
across geographies. Batch workloads without tight latency
constraints can run in Regions with favorable energy profiles
rather than defaulting to the closest one.

Amazon CloudWatch dashboards that combine operational metrics with
sustainability indicators make sustainability visible in the same
place operators already look. Track resource utilization
efficiency, waste metrics (failed or abandoned executions as a
percentage of total), and peak compared to off-peak utilization
rates. Incorporate these dashboards into periodic optimization
reviews so environmental impact is a standing input to engineering
priorities rather than an annual afterthought.

### Implementation steps

- **Enable carbon emissions
tracking:** Turn on
[AWS Sustainability](https://docs.aws.amazon.com/sustainability/latest/userguide/what-is-sustainability.html) and establish environmental baselines
for agent infrastructure across a 30-day observation window.
- **Instrument resource efficiency per
task:** Configure
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) to track tokens per
successful completion, compute hours per workflow execution,
and cache hit rates.
- **Schedule deferrable workloads
off-peak:** Identify non-interactive workloads and
shift them to off-peak windows:

Batch processing
- Knowledge base indexing
- Periodic AgentCore Evaluations runs
- Bulk data enrichment

- **Evaluate Region placement for batch
work:** For workloads with flexible latency, use
[Amazon
Bedrock cross-region inference](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html) to route requests to
Regions with favorable energy profiles.
- **Build combined dashboards and review
on a cadence:** Create Amazon CloudWatch dashboards
pairing operational metrics with sustainability indicators
(resource utilization efficiency, waste percentage, and peak
compared to off-peak utilization), and review them as part
of periodic optimization cycles.

## Resources

**Related best practices:**

- [AGENTSUS02-BP01 Optimize
context management and memory utilization](agentsus02-bp01.html)
- [AGENTSUS02-BP03
Appropriately scale data, networking, and compute
dependencies](agentsus02-bp03.html)
- [SUS01-BP01
Choose Region based on both business requirements and
sustainability goals](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_region_a2.html)

**Related documents:**

- [AWS Sustainability User Guide](https://docs.aws.amazon.com/sustainability/latest/userguide/what-is-sustainability.html)
- [Announcing
the AWS Sustainability console](https://aws.amazon.com/blogs/aws/announcing-the-aws-sustainability-console-programmatic-access-configurable-csv-reports-and-scope-1-3-reporting-in-one-place/)
- [Sustainability
Pillar - AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)
- [Amazon
Bedrock cross-region inference](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html)
- [Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html)

**Related videos:**

- [AWS re:Invent 2024 - Sustainable and cost-efficient generative AI
with agentic workflows (AIM333)](https://www.youtube.com/watch?v=tFiDkSG2ess)

**Related services:**

- [AWS Sustainability](https://aws.amazon.com/sustainability/)
- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon
Bedrock](https://aws.amazon.com/bedrock/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsus02-bp04.html*

---

# AGENTSUS03 — Agent governance

**Pillar**: Sustainability  
**Best Practices**: 4

---

# AGENTSUS03-BP01 Maintain organizational skills and competencies

Organizations that automate without deliberately preserving the
human expertise behind the automation lose the capacity to train new
staff, handle edge cases, and recover when automated systems reach
their limits. Keeping a clear distinction between what agents handle
autonomously and what stays with human experts sustains
organizational capability across the whole lifetime of the
deployment.

**Desired outcome:**

- You have a competency taxonomy that separates human-owned,
agent-augmented, and fully automated tasks, with documented
criteria for each tier.
- Routing in the agent layer escalates high-stakes, ambiguous, or
edge-case decisions to human experts automatically.
- Rotation programs and workshops keep subject matter experts
proficient with the workflows agents otherwise execute.
- You monitor escalation rates and expert task distribution to
confirm critical competencies stay actively practiced.

**Common anti-patterns:**

- Automating domain workflows without maintaining documented
runbooks or periodic manual execution exercises, reducing the
organization's capacity to operate when agent systems are
unavailable.
- Running agents without clear boundaries between autonomous
action and human oversight, producing cases where agents make
high-stakes decisions that should have routed to experts.
- Scaling agent adoption without workforce planning to preserve
critical skills, so short-term productivity gains erode
long-term organizational capacity.
- Treating escalation as an exception rather than an expected
outcome, so the hand-off paths between agents and human experts
are undertested and fail when they are needed most.

**Benefits of establishing this best
practice:**

- The organization retains the capacity to operate manually when
agent systems are unavailable or encounter situations beyond
their training.
- Critical expertise stays available for onboarding, edge cases,
and evolving business processes that automation has not caught
up to.
- Adoption paces the organization's ability to maintain oversight,
rather than outrunning it.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

The threshold question is which competencies must stay with humans
and which can move to agents or automation. A three-tier taxonomy,
human-owned, agent-augmented, and fully automated, gives teams a
shared vocabulary for that decision. The categorization criteria
matter more than the labels:

- Human-owned means decisions where error tolerance is low and
context is highly variable (regulatory judgment, customer
escalations, and strategic trade-offs)
- Agent-augmented means work where an agent accelerates human
output but the human remains the decision-maker (code review,
document drafting, and data analysis)
- Fully automated means routine tasks where agent accuracy
exceeds the cost of errors (routing, classification, and
standard form processing)

Categorization is reviewed as agent capabilities improve and as
organizational priorities shift.

[Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) with Policies and code
interceptors can invoke human-in-the-loop workflows based on
complexity thresholds, confidence scores, or stakes assessment.
[Amazon
Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html) enforces the decision boundaries so that
high-stakes cases escalate automatically rather than depending on
the agent to self-report low confidence.
[Amazon
Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html) runs agent outputs against
expert-generated baselines, which is how you detect drift in
categories where the agent was trusted but is now degrading.

The automation that removes a task from expert workflows also
removes the practice that kept expertise sharp. Rotation programs
assign experts to handle a fraction of cases manually on a
recurring basis. For business-critical competencies, a defined
minimum (a percentage of cases per quarter, a weekly shift, or a
monthly workshop) keeps practice active. Document runbooks for
workflows agents now execute so the manual path remains viable
when the automated one is unavailable.
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) tracks escalation rates and
task distribution, showing whether experts are being kept in the
loop often enough to stay sharp.

### Implementation steps

- **Define a competency
taxonomy:** Categorize organizational skills into
human-owned, agent-augmented, and fully automated tiers with
documented criteria and a review cadence.
- **Configure automated
escalation:** Use
[Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) Policies and
[Amazon
Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html) to route high-stakes, ambiguous,
or low-confidence decisions to human experts.
- **Establish rotation
programs:** Assign subject matter experts to handle
a defined percentage of cases manually each quarter for
competencies critical to business resilience, and maintain
runbooks for manual execution.
- **Validate agent outputs against
expert baselines:** Run
[Amazon
Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html) against baselines
produced by subject matter experts to detect drift in
categories that have been trusted to automation.
- **Monitor escalation and task
distribution:** Track escalation rates and expert
task distribution through
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) to confirm that
critical competencies remain actively practiced.

## Resources

**Related best practices:**

- [AGENTSUS03-BP02 Build
agents to mirror your organizational skills and
competencies](agentsus03-bp02.html)
- [AGENTSUS03-BP03 Maintain
comprehensive specifications for agents and agentic
systems](agentsus03-bp03.html)
- [MLPERF06-BP01
Include human-in-the-loop monitoring](https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlperf-06.html)

**Related documents:**

- [Amazon
Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html)
- [Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html)
- [Human-in-the-loop
(HITL) - Amazon Nova Act](https://docs.aws.amazon.com/nova/latest/userguide/nova-act-hitl.html)
- [Build
reliable AI agents with Amazon Bedrock AgentCore
Evaluations](https://aws.amazon.com/blogs/machine-learning/build-reliable-ai-agents-with-amazon-bedrock-agentcore-evaluations/)
- [Amazon
Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html)

**Related examples:**

- [GitHub:
awslabs/amazon-bedrock-agentcore-samples - Evaluations](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/07-AgentCore-evaluations)

**Related services:**

- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon
Bedrock](https://aws.amazon.com/bedrock/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsus03-bp01.html*

---

# AGENTSUS03-BP02 Build agents to mirror your organizational skills and competencies

Agents built to codify proven workflows deliver immediate value.
Agents built to automate processes the organization has not mastered
itself usually waste resources learning what could have been
documented first. Focusing automation on well-understood work is the
difference between agent adoption that pays back quickly and
adoption that consumes resources on untested methodology.

**Desired outcome:**

- You select processes for automation where steps, decision
criteria, and success metrics are documented and consistently
executed by human experts.
- Agents mirror the decision trees, validation checkpoints, and
escalation paths that experts already use.
- Institutional knowledge is captured in knowledge bases that
ground agent decisions, rather than relying solely on foundation
model training data.
- Readiness criteria, minimum documentation maturity, gate agent
development projects before resources are committed.

**Common anti-patterns:**

- Building agents to automate unfamiliar or poorly understood
processes where steps, decision criteria, and success metrics
are not documented, so the automation becomes an experiment
rather than a productivity gain.
- Skipping the step of codifying expert practices before writing
agent logic, missing the opportunity to replicate proven
approaches.
- Generating agent code without understanding it, producing
implementations the team can't maintain or evolve and
accumulating technical debt.
- Automating processes that vary widely in execution across
experts, so the agent picks one variant and discovers at runtime
that the choice did not match the business context.

**Benefits of establishing this best
practice:**

- Agent automation starts from proven practice, so the automation
runs correctly at deployment instead of being debugged in
production.
- Human expertise remains the source of truth and is amplified
rather than replaced, preserving adaptation capacity.
- Development resources flow to workflows where ROI is defensible,
rather than being spent on speculative automation.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

The criterion for a good automation candidate is straightforward.
The process is well understood, the steps are documented, the
decision criteria are explicit, and multiple experts execute it
the same way. Processes that fail that test should not be the
first things an organization automates. The agent will replicate
whichever variant the documentation captures, and if the
documentation captures the wrong variant, every agent invocation
reinforces the error. The documentation exercise itself is the
first return on investment. Writing down what experts do
encourages consistency even before any agent is built.

Once the documentation exists, the agent is a translation of it.
You configure Amazon Bedrock AgentCore agents to follow the same
decision trees, validation checkpoints, and escalation paths as
human experts. This gives the automation the same runtime behavior
as the manual process.
[Amazon
Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html) holds the documented expertise as a
RAG source, which grounds agent decisions in institutional
knowledge rather than leaving them to foundation model training
data.
[Amazon
Bedrock AgentCore tools](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/tools.html) mirror the external systems experts
use (the same APIs, the same data sources, and the same validation
services), so the agent's view of the task matches the expert's.

Routing creates a distinction between automated and human-owned
work.
[Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) can direct routine tasks to full
automation while escalating complex or ambiguous work to human
experts, implementing the three-tier taxonomy described in
[AGENTSUS03-BP01 Maintain
organizational skills and competencies](agentsus03-bp01.html) at runtime.
[Amazon
Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html) assesses whether agent
outputs match expert-generated baselines, and
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) exposes patterns where
agent behavior has drifted from documented practice. Gate agent
development projects behind readiness criteria, inputs, outputs,
decision criteria, and success metrics need to be specified before
development starts, so the documentation discipline becomes a
precondition rather than an afterthought.

Spec-driven development tools like Kiro apply the same discipline
to the implementation side. Agent code written from a
specification is more maintainable, more reviewable, and less
likely to bake in assumptions no one can trace later. The tradeoff
is upfront effort on the specification, which is generally
recouped during review, debugging, and evolution.

### Implementation steps

- **Document workflows before automating
them:** Capture the following from subject matter
experts before approving agent development:

Decision logic
- Exception handling
- Success criteria
- Readiness criteria (inputs, outputs, decision criteria,
and metrics)

- **Store institutional knowledge as RAG
sources:** Load documented expertise into
[Amazon
Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html) so agent decisions ground in
the organization's knowledge rather than foundation model
defaults.
- **Mirror expert system
access:** Configure
[Amazon
Bedrock AgentCore tools](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/tools.html) to give agents the same
external systems and data sources human experts use.
- **Route routine vs. complex
work:** Use
[Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) to send routine tasks to
full automation and escalate complex or ambiguous work to
human experts.
- **Validate behavior against expert
baselines:** Run
[Amazon
Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html) against
expert-generated baselines and monitor drift through
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html).

## Resources

**Related best practices:**

- [AGENTSUS03-BP01 Maintain
organizational skills and competencies](agentsus03-bp01.html)
- [AGENTSUS03-BP03 Maintain
comprehensive specifications for agents and agentic
systems](agentsus03-bp03.html)
- [OPS08-BP01
Use runbooks to perform procedures](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_ready_to_support_use_runbooks.html)

**Related documents:**

- [Amazon
Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html)
- [Amazon
Bedrock AgentCore tools](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/tools.html)
- [Amazon
Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html)
- [Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html)
- [AI
agents in enterprises: Best practices with Amazon Bedrock
AgentCore](https://aws.amazon.com/blogs/machine-learning/ai-agents-in-enterprises-best-practices-with-amazon-bedrock-agentcore/)

**Related services:**

- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon
Bedrock](https://aws.amazon.com/bedrock/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsus03-bp02.html*

---

# AGENTSUS03-BP03 Maintain comprehensive specifications for agents and agentic systems

Agents without specifications become systems that only their
original developers understand. Thorough documentation, purpose,
boundaries, integration points, and decision logic keep
institutional knowledge available to the whole team and verify that
agent behavior is traceable as teams and business processes change.

**Desired outcome:**

- Each deployed agent has a specification covering business
purpose, operational boundaries, decision criteria, and
escalation paths.
- Specifications are stored in version-controlled artifacts
alongside the agent implementation.
- A centralized agent catalog lets team members discover, review,
and reuse agent capabilities.
- Runtime behavior is documented automatically and compared
against design specifications to detect drift.
- Governance requires specification validation before agents reach
production.

**Common anti-patterns:**

- Deploying agents without thorough documentation of purpose,
boundaries, or decision-making logic, so institutional knowledge
is held only by the original developers.
- Letting documentation fall out of date as agents evolve,
producing specifications that describe yesterday's behavior
rather than today's.
- Treating agent configuration as code only, without capturing the
expert decision-making patterns and business logic rationale
that informed the design.
- Skipping specification validation in the promotion path, so
agents reach production with documentation that doesn't match
their actual behavior.

**Benefits of establishing this best
practice:**

- Institutional knowledge survives personnel changes and
organizational restructuring, preserved in documentation rather
than memory.
- Teams develop against specifications informed by business
process, reducing the experimentation cost of each new agent.
- Documented decision logic and operational boundaries make
oversight of automated processes tractable.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

A specification decouples the agent's behavior from its author.
When the original developer moves on, the next maintainer picks up
the system through the specification rather than through reverse
engineering. Amazon Bedrock AgentCore enables declarative
specifications that capture prompt templates, tool definitions,
guardrail policies, and orchestration logic as version-controlled
artifacts. The documentation and the configuration are the same
artifact rather than two copies that drift.

Spec-driven development tools like Kiro extend the discipline into
how agents get written in the first place. When specifications are
the starting point rather than an afterthought, documentation is
produced as a byproduct of development rather than a retrospective
task. The upfront investment in writing the specification is
recovered during code review, testing, and ongoing evolution,
because every subsequent change happens against a clear baseline.

Discovery needs a central home, like a catalog based on
[Amazon
Bedrock AgentCore Registry](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/registry.html) registry capabilities that makes
agents discoverable, governable, and reusable across the
organization. Each entry captures business purpose, version
history, dependencies, and operational characteristics, so a team
evaluating whether to build something new can check what already
exists.

Specifications can drift if an organization lacks validation
mechanisms.
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) generates runtime
documentation from actual execution patterns. When runtime
behavior diverges from design specifications, the telemetry shows
it before the divergence becomes undocumented institutional
knowledge.

For multi-agent systems, document coordination protocols and
delegation patterns explicitly, because the emergent behavior of a
multi-agent system is rarely obvious from any individual agent's
specification. Portfolio-level monitoring, specification
compliance, documentation currency, and behavioral drift, keeps
documentation usable as the agent count scales.

### Implementation steps

- **Set documentation
standards:** Require each agent to carry
specifications using AgentCore's declarative configuration
artifacts. Each specification must cover:

Business purpose
- Operational boundaries
- Decision criteria
- Escalation paths

- **Adopt spec-driven
development:** Use Kiro or similar spec-driven
tools so documentation is produced as a natural byproduct of
the development process rather than a retrospective task.
- **Register agents in a central
catalog:** Record each agent in
[Amazon
Bedrock AgentCore Registry](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/registry.html) with the following
metadata:

Purpose
- Version history
- Dependencies
- Operational characteristics

- **Generate runtime
documentation:** Use
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) to produce runtime
documentation that can be compared against design
specifications to detect drift.
- **Gate promotion on specification
validation:** Require documentation validation as
part of the pipeline that promotes agents to production, so
production agents always have current specifications.

## Resources

**Related best practices:**

- [AGENTSUS03-BP01 Maintain
organizational skills and competencies](agentsus03-bp01.html)
- [AGENTSUS03-BP04
Decommission unused agents and prevent agent sprawl](agentsus03-bp04.html)
- [OPS11-BP01
Have a process for continuous improvement](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_evolve_ops_process_cont_imp.html)

**Related documents:**

- [Amazon
Bedrock AgentCore Registry](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/registry.html)
- [The
future of managing agents at scale: AWS Agent Registry now in
preview](https://aws.amazon.com/blogs/machine-learning/the-future-of-managing-agents-at-scale-aws-agent-registry-now-in-preview/)
- [Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html)
- [Amazon
Bedrock Agents Documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html)

**Related examples:**

- [GitHub:
awslabs/amazon-bedrock-agentcore-samples - End-to-end use
cases](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/02-use-cases)

**Related services:**

- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsus03-bp03.html*

---

# AGENTSUS03-BP04 Decommission unused agents and prevent agent sprawl

Every agent that stays deployed past its usefulness consumes
infrastructure, expands the attack surface, and adds operational
overhead that never shows up as an explicit line item. Active
portfolio management helps prevent the silent accumulation of cost
and complexity that comes with scaled adoption.

**Desired outcome:**

- Every deployed agent has a documented owner, a clear business
purpose, and measurable usage.
- Agents that no longer deliver value move through a structured
decommissioning lifecycle and are retired.
- Teams search the agent registry for existing capabilities before
initiating new agent development.
- Portfolio health, total agent count, percentage with active
usage, percentage with current documentation, is visible at the
organizational level.

**Common anti-patterns:**

- Deploying agents without ownership assignment or usage tracking,
so no one can tell which agents still deliver value.
- Allowing abandoned agents to persist indefinitely because no
decommissioning process exists, accumulating infrastructure cost
and expanding the attack surface.
- Building new agents for capabilities that already exist in
deployed agents elsewhere in the organization, creating
redundant implementations.
- Relying on informal knowledge of which agents are still useful
instead of automated usage tracking, so the decommissioning
decision depends on whoever happens to remember which agents are
deployed.

**Benefits of establishing this best
practice:**

- Portfolio-level decisions about resource consumption are tied to
actual business value delivered, rather than historical
deployment patterns.
- Decommissioning reclaims infrastructure resources and reduces
the operational surface area.
- Discoverability of existing capabilities reduces redundant
implementations and reinforces reusable architecture patterns.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

[Amazon
Bedrock AgentCore Registry](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/registry.html) provides the authoritative
catalog of deployed agents, with each entry capturing business
purpose, designated owner, deployment date, dependencies, and
usage metrics. Semantic capability search lets teams discover
existing agents before building new ones, which is the preventive
side of avoiding agent sprawl. Pair the registry with
[Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/working_with_metrics.html) metrics tracking invocation frequency and
last-invocation timestamp for each agent. Inactive agents then
surface automatically for owner review instead of being discovered
during audits.

Decommissioning becomes routine when it has a defined lifecycle.
Active, under review, deprecated, and decommissioned stages give
owners clear transitions and give the organization consistent
visibility into which agents are on the path to retirement. When
an agent is flagged for low usage, the owner's first question is
whether it serves a seasonal or infrequent-but-critical purpose.
Tax-season agents, quarterly reporting agents, and
disaster-recovery agents appear idle most of the time but are
essential when they are invoked. A structured review makes that
distinction before deprecation happens.

During quarterly portfolio rationalization, teams evaluate the
full agent inventory against current business priorities, identify
overlapping capabilities, and merge redundant implementations into
shared patterns (following
[AGENTSUS01-BP02
Implement reusable workflow patterns](agentsus01-bp02.html)). They retire agents
whose business context has changed. Portfolio health metrics
tracked through
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html), total agent count,
percentage with active usage, and percentage with current
documentation, make sustainability outcomes visible at the
organizational level.

### Implementation steps

- **Register every deployed agent with
ownership metadata:** Record each agent in
[Amazon
Bedrock AgentCore Registry](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/registry.html) with the following:

Business purpose
- Designated owner
- Deployment date
- Dependencies

- **Track invocation metrics and flag
inactive agents:** Instrument agents with
[Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/working_with_metrics.html) metrics capturing invocation frequency and
last-invocation timestamp, and flag agents that cross a
defined inactivity threshold for owner review.
- **Define a decommissioning
lifecycle:** Establish the following stages with
transition criteria and owner responsibilities at each:

Active
- Under review
- Deprecated
- Decommissioned

- **Require registry search before new
agent development:** Add a pre-development check to
the intake process so teams discover and evaluate existing
capabilities before initiating new work.
- **Run quarterly portfolio
reviews:** Evaluate the full agent inventory
against current business priorities, consolidate overlapping
capabilities into shared patterns, and retire agents whose
business context has changed.

## Resources

**Related best practices:**

- [AGENTSUS01-BP02
Implement reusable workflow patterns](agentsus01-bp02.html)
- [AGENTSUS03-BP03 Maintain
comprehensive specifications for agents and agentic
systems](agentsus03-bp03.html)
- [AGENTSUS02-BP04
Measure and optimize the environmental footprint of agent
workloads](agentsus02-bp04.html)
- [SUS03-BP02
Remove or refactor workload components with low or no
use](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_software_a3.html)

**Related documents:**

- [Amazon
Bedrock AgentCore Registry](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/registry.html)
- [The
future of managing agents at scale: AWS Agent Registry now in
preview](https://aws.amazon.com/blogs/machine-learning/the-future-of-managing-agents-at-scale-aws-agent-registry-now-in-preview/)
- [Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html)
- [Amazon CloudWatch metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/working_with_metrics.html)

**Related videos:**

- [AgentCore
Registry: Discover, Govern, and Reuse AI Agents at
Scale](https://www.youtube.com/watch?v=rIcOJrE-fTk)

**Related services:**

- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsus03-bp04.html*

---

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
