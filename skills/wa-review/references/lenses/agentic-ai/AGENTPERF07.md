# AGENTPERF07 — Multi-tenancy and resource optimization

**Pillar**: Performance Efficiency  
**Best Practices**: 2

---

# AGENTPERF07-BP01 Design efficient multitenant agent deployment models

Organizations that serve multiple tenants from a shared agent
service get better resource efficiency and faster tenant onboarding
when the deployment model delivers consistent performance for every
tenant. Siloed deployments provide strong isolation at higher cost.
Pooled deployments maximize efficiency but need mechanisms to help
prevent noisy neighbor effects. Hybrid models combine both, using
pooled resources for standard tenants and dedicated resources for
premium tenants.

**Desired outcome:**

- You have multitenant agent deployments that use deployment
models matched to tenant requirements.
- You have deployment models documented with clear performance
characteristics and SLA commitments for each tier.
- You have a deployment model that supports efficient tenant
onboarding through configuration rather than infrastructure
provisioning.

**Common anti-patterns:**

- Deploying fully siloed infrastructure for every tenant
regardless of their performance requirements, creating resource
waste for tenants that would be well-served by pooled resources.
- Using a single pooled deployment without isolation mechanisms,
allowing high-volume tenants to consume disproportionate
resources and degrade performance for others.
- Skipping tenant tiers with different performance SLAs, treating
all tenants identically regardless of business value.

**Benefits of establishing this best
practice:**

- Resource investment stays proportional to tenant value and
performance requirements.
- Appropriate isolation mechanisms deliver consistent performance
for every tenant.
- Configuration-driven provisioning speeds tenant onboarding.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Define tenant tiers based on performance requirements and business
value:

- A standard tier using pooled resources with best-effort
performance
- A premium tier using dedicated resources with stronger SLA
targets
- (Optional) An enterprise tier with fully isolated
infrastructure

For pooled deployments,
[Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html) provides session-isolated
execution that naturally helps prevent cross-tenant interference
at the agent execution level. For tenants that need custom
container environments, deploy on
[Amazon EKS](https://aws.amazon.com/eks/)
or [Amazon ECS](https://aws.amazon.com/ecs/) with namespace-level or task-level isolation. For
simpler tenant needs such as team-specific chat assistants or
enterprise Q&A,
[Amazon Quick
Suite](https://aws.amazon.com/quicksuite/) provides a managed no-code option where business
users create and deploy agents without custom infrastructure.

Tenant-aware routing at the API layer uses
[Amazon API Gateway](https://aws.amazon.com/api-gateway/) with usage plans that enforce per-tenant rate
limits and throttling. At the inference layer, Amazon Bedrock's
provisioned throughput gives premium tenants reserved capacity
while standard tenants use on-demand capacity. Tenant context
propagates through the agent stack so every component (runtime,
memory, tools) applies tenant-specific configurations. For data
isolation, use
[Amazon DynamoDB](https://aws.amazon.com/dynamodb/) with tenant partition keys for pooled access, or
separate tables for siloed tenants. Tenant onboarding automated
through [AWS CDK](https://aws.amazon.com/cdk/) or CloudFormation makes new standard tenants a
configuration change rather than an infrastructure provisioning
project.

### Implementation steps

- **Define tenant tiers with specific
performance SLAs, isolation requirements, and
pricing:** Define standard, premium, and optional
enterprise tiers with explicit SLAs and isolation
expectations.
- **Design the deployment architecture
for each tier:** Architect pooled (shared AgentCore
Runtime, on-demand Amazon Bedrock), premium (dedicated
resources, provisioned throughput), and enterprise (fully
isolated) deployments.
- **Implement tenant-aware routing using
API Gateway with per-tenant usage plans and rate
limits:** Use
[Amazon API Gateway](https://aws.amazon.com/api-gateway/) usage plans with per-tenant rate and
burst limits.
- **Configure data isolation using
DynamoDB tenant partition keys (pooled) or separate tables
(siloed):** Enforce data isolation at the data
layer with partition keys or separate tables as appropriate
for the tier.
- **Automate tenant onboarding for each
tier using CDK/CloudFormation templates:** Template
onboarding so new tenants are provisioned through
configuration rather than manual infrastructure work.
- **Monitor per-tenant performance
metrics to validate SLA compliance:** Publish
per-tenant metrics to CloudWatch and alert when observed
performance drifts outside SLA.

## Resources

**Related best practices:**

- [AGENTPERF07-BP02
Implement tenant-aware performance isolation and
throttling](agentperf07-bp02.html)
- [AGENTPERF02-BP01
Design efficient reasoning pipelines](agentperf02-bp01.html)

**Related documents:**

- [Building
multi-tenant architectures for agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-multitenant/introduction.html)
- [Enforcing
tenant isolation, Multi-tenant agentic AI](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-multitenant/enforcing-tenant-isolation.html)
- [Operationalizing
agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-operationalizing-agentic-ai/introduction.html)

**Related videos:**

- [Building
multi-tenant SaaS agents with AgentCore (SAS407)](https://www.youtube.com/watch?v=uwXrtyXXuy8)
- [Transforming
from SaaS to multi-tenant agentic SaaS (SAS304)](https://www.youtube.com/watch?v=YOQlbZojPB4)
- [Deploy
Production-Ready Agents in 22 Minutes with AgentCore
Runtime](https://www.youtube.com/watch?v=Q-tYIAuv9WI)

**Related services:**

- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon API Gateway](https://aws.amazon.com/api-gateway/)
- [Amazon
Bedrock](https://aws.amazon.com/bedrock/)
- [Amazon DynamoDB](https://aws.amazon.com/dynamodb/)
- [Amazon EKS](https://aws.amazon.com/eks/)
- [AWS CDK](https://aws.amazon.com/cdk/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentperf07-bp01.html*

---

# AGENTPERF07-BP02 Implement tenant-aware performance isolation and throttling

Trust in a shared agent service is built through consistent,
predictable performance for every tenant, even during demand spikes.
In pooled multitenant deployments, effective isolation requires
throttling at multiple layers (API, inference, memory, and tools),
monitoring per-tenant resource consumption, and adaptive fairness
mechanisms that distribute shared resources equitably based on
current load.

**Desired outcome:**

- You have per-tenant throttling enforced at every shared resource
layer.
- You have tenant resource consumption monitored in real time with
alerts for tenants approaching their limits.
- You have graceful throttling that provides clear feedback to
throttled tenants.
- You have performance isolation validated through regular load
testing that simulates noisy neighbor scenarios.

**Common anti-patterns:**

- Applying throttling only at the API gateway layer without
enforcing limits at downstream shared resources, letting tenants
bypass API-level limits through long-running operations.
- Using static throttling limits that don't adapt to current
system load, wasting available capacity during low-load periods
or failing to protect isolation during high-load periods.
- Throttling all tenants equally regardless of their service tier,
failing to honor premium SLAs.

**Benefits of establishing this best
practice:**

- Multi-layer throttling distributes shared resources fairly
across tenants.
- Real-time per-tenant consumption metrics support proactive
management.
- Per-tenant performance monitoring validates SLA compliance.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Multi-layer throttling enforces tenant limits at every shared
resource. At the API layer,
[Amazon API Gateway](https://aws.amazon.com/api-gateway/) usage plans with per-tenant API keys enforce
request rate and burst limits. At the inference layer,
tenant-aware request queuing caps concurrent
[Amazon
Bedrock](https://aws.amazon.com/bedrock/) inference calls per tenant. At the memory and tool
layers, per-tenant rate limiting applies to shared endpoints. For
agents deployed on
[Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html), the runtime's session isolation
provides natural per-session resource boundaries.

Adaptive throttling adjusts limits based on current system load:
during low-load periods, tenants can burst above their baseline
limits to use available capacity, and during high-load periods,
strict limits protect isolation. Per-tenant
[Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) dashboards and metrics track request volume,
inference consumption, latency percentiles, throttle rates, and
error rates. Alarms fire when a tenant approaches their limits or
when per-tenant latency exceeds SLA thresholds. Regular noisy
neighbor testing, simulating high-load scenarios for individual
tenants, validates that other tenants' performance stays within
SLA bounds.

### Implementation steps

- **Define per-tenant throttling limits
for each resource layer:** Set per-tenant limits
for API requests per second, concurrent inference calls,
memory storage quota, and tool invocations per minute.
- **Implement API Gateway usage plans
with per-tenant API keys and rate/burst limits:**
Use
[Amazon API Gateway](https://aws.amazon.com/api-gateway/) usage plans with per-tenant API keys to
enforce rate and burst limits at ingress.
- **Deploy tenant-aware inference
queuing with per-tenant concurrency limits:** Queue
[Amazon
Bedrock](https://aws.amazon.com/bedrock/) inference calls per tenant so no single
tenant can consume all inference capacity.
- **Configure adaptive throttling that
adjusts limits based on current system load:**
Allow bursts during low-load periods and enforce strict
limits during high-load periods to protect isolation.
- **Create per-tenant CloudWatch
dashboards and configure SLA-based alarms:**
Publish per-tenant metrics in
[Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) and alarm on consumption approaching
limits or latency exceeding SLA thresholds.
- **Establish regular noisy neighbor
load testing to validate isolation effectiveness:**
Schedule noisy neighbor load tests that simulate high-load
scenarios for individual tenants and verify others stay
within SLA.

## Resources

**Related best practices:**

- [AGENTPERF07-BP01 Design
efficient multi-tenant agent deployment models](agentperf07-bp01.html)
- [AGENTPERF04-BP02
Implement efficient protocol-based agent communications](agentperf04-bp02.html)
- [AGENTSUS01-BP04
Scale cognitive processing pathways appropriately](agentsus01-bp04.html)

**Related documents:**

- [Building
multi-tenant architectures for agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-multitenant/introduction.html)
- [Enforcing
tenant isolation, Multi-tenant agentic AI](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-multitenant/enforcing-tenant-isolation.html)

**Related videos:**

- [Building
multi-tenant SaaS agents with AgentCore (SAS407)](https://www.youtube.com/watch?v=uwXrtyXXuy8)

**Related services:**

- [Amazon API Gateway](https://aws.amazon.com/api-gateway/)
- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
- [Amazon DynamoDB](https://aws.amazon.com/dynamodb/)
- [Amazon
Bedrock](https://aws.amazon.com/bedrock/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentperf07-bp02.html*

---
