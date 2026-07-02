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
