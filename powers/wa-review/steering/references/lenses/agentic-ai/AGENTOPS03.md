# AGENTOPS03 — Agent lifecycle and deployment processes

**Pillar**: Operational Excellence  
**Best Practices**: 4

---

# AGENTOPS03-BP01 Define an agent lifecycle with clear SME ownership, testing, and governance

An agent portfolio without lifecycle discipline becomes a graveyard
of undocumented services with forgotten owners. Explicit lifecycle
stages, named SME ownership, and clean decommissioning keep the
portfolio tractable as it grows from a handful of agents to dozens
or hundreds.

**Desired outcome:**

- Every agent has a documented lifecycle state (development,
pilot, production, deprecated, and decommissioned) with defined
transition criteria.
- Onboarding follows a standardized provisioning process that
configures required resources, permissions, and monitoring
before an agent handles production traffic.
- Decommissioning cleanly removes retired agents, no orphaned
resources, dangling permissions, or undocumented dependencies
left behind.
- Each agent has a named SME owner accountable for its behavior,
performance, and eventual retirement.

**Common anti-patterns:**

- Deploying agents to production without a defined lifecycle state
or designated owner, so no one is accountable when behavior
needs attention.
- Operating without decommissioning procedures, leaving retired
agents running with active permissions and consuming resources
long after they were replaced.
- Skipping the pilot stage and pushing agents from development
directly to full production, missing the chance to validate
behavior under real traffic with enhanced monitoring.
- Treating the agent registry as a one-time artifact that nobody
updates once the agent is live.

**Benefits of establishing this best
practice:**

- Standardized lifecycle procedures produce consistent
provisioning, operation, and retirement, reducing operational
complexity as the portfolio grows.
- Documented lifecycle states and transition criteria create an
auditable record of each agent's history for compliance and
governance.
- Named owners accelerate incident response. When an agent
misbehaves, the team knows who to engage without a search.
- Clean decommissioning helps prevent the slow accumulation of
abandoned resources that becomes a cost and security problem
over time.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Five stages cover the operational arc of almost any agent:

- Development (under active development, not serving production
traffic)
- Pilot (limited production use with enhanced monitoring and
cost validation)
- Production (full deployment with standard operational
procedures)
- Deprecated (scheduled for decommissioning, no new
integrations)
- Decommissioned (removed from service, resources cleaned up)

Each transition should carry explicit criteria, required
approvals, validation gates, and documentation requirements, so
stage changes are decisions rather than drift.

Pilot validates economic viability and identifies issues before
full deployment, reducing the cost of addressing problems. For
teams using spec-driven development with tools like Kiro, the spec
workflow produces the documentation needed for lifecycle
governance as a byproduct. This is a useful side effect worth
using rather than rebuilding.

An agent registry is a durable artifact that makes this process
coherent. It should track agent ID, lifecycle state, owner,
dependencies, capabilities, and operational metadata. Without a
registry, lifecycle state exists only in people's heads, making it
difficult to track and manage consistently across the
organization. The registry becomes the input for portfolio
reviews, decommissioning dependency analysis, and emergency
response.

Emergency lifecycle transitions deserve their own processes.
Automated emergency termination switch mechanisms allow immediate
revocation of an agent's permissions and halting of operations,
enabling rapid response to operational issues. The decommissioning
runbook does similar work for the planned case. It removes
resources, revokes permissions, updates the registry, and notifies
dependent systems as automated steps rather than as checklist
items. For agents built through no-code platforms like
[Amazon Quick
Suite](https://aws.amazon.com/quicksuite/), the same lifecycle rules apply. The registry tracks
them, portfolio reviews consider them, and decommissioning cleans
them up.

### Implementation steps

- **Document the five lifecycle
stages:** Specify transition criteria, required
approver roles, and validation gates for each stage.
- **Build the agent registry:**
Track agent ID, lifecycle state, owner, dependencies,
capabilities, and operational metadata in a durable store.
- **Automate lifecycle state
transitions:** Validate criteria, trigger
stage-specific actions, and record transitions with
attribution, deployments, permission changes, monitoring
setup, and decommissioning steps.
- **Create standardized provisioning
templates:** Configure required resources,
permissions, and monitoring automatically so new agents
enter production with a consistent baseline.
- **Implement emergency termination
switch and decommissioning runbooks:** Include
dependency analysis before running so decommissioning
doesn't break upstream consumers.
- **Establish quarterly portfolio
reviews:** Identify agents for deprecation or
decommissioning, including those built with no-code
platforms like
[Amazon Quick](https://aws.amazon.com/quicksuite/).

## Resources

**Related best practices:**

- [AGENTOPS01-BP01
Establish well-defined agent roles, responsibilities, and
success criteria](agentops01-bp01.html)
- [AGENTOPS03-BP02
Implement CI/CD pipelines tailored to agentic system
deployment (AgentOps)](agentops03-bp02.html)
- [AGENTOPS03-BP03
Implement agent-specific scaling policies and capacity
planning](agentops03-bp03.html)
- [AGENTOPS02-BP02
Implement configuration drift detection and remediation](agentops02-bp02.html)
- [AGENTCOST06-BP02
Cost optimize versioning and deployment through efficient
artifact management](agentcost06-bp02.html)

**Related documents:**

- [Operationalizing
agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-operationalizing-agentic-ai/introduction.html)
- [Focus
area 5: Manage the lifecycle](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-operationalizing-agentic-ai/focus-areas-lifecycle.html)
- [Evolving
software delivery for agentic AI](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-operationalizing-agentic-ai/software-delivery.html)
- [Preparing
the business for agentic AI at scale](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-operationalizing-agentic-ai/preparing-business.html)
- [Kiro
Specs](https://kiro.dev/docs/specs/)
- [Operationalizing
Agentic AI Part 1: A Stakeholder's Guide](https://aws.amazon.com/blogs/machine-learning/operationalizing-agentic-ai-part-1-a-stakeholders-guide/)

**Related videos:**

- [AWS re:Invent 2024 - Agents in the enterprise: Best practices with
AgentCore (AIM3310)](https://www.youtube.com/watch?v=w5XJxCpUADY)
- [AWS re:Invent 2024 - Cox Automotive's Blueprint for Agentic AI on
AgentCore (IND3329)](https://www.youtube.com/watch?v=ICA8-d_Nt9Q)
- [AWS re:Invent 2024 - Bridging from POC to production: Intro to
AgentCore (AIM2204)](https://www.youtube.com/watch?v=oDjESsByBmM)

**Related workshops:**

- [Getting
started with Amazon Bedrock AgentCore](https://catalog.workshops.aws/agentcore-getting-started/en-US)

**Related services:**

- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentops03-bp01.html*

---

# AGENTOPS03-BP02 Implement CI/CD pipelines tailored to agentic system deployment (AgentOps)

Manual agent deployments and informal testing can keep a project
stuck in the pilot phase. An agent-aware pipeline, with behavioral
evaluation gates, staged rollout, and automated rollback can help
your organization realize the goal of daily deployment of behavioral
improvements.

**Desired outcome:**

- Agent deployments run fully through CI/CD with agent-specific
validation gates for prompt quality, tool integration
correctness, behavioral regression, and security.
- Deployment strategies (blue/green, canary) limit the scope of
impact when a regression does slip through.
- Automated rollback restores the previous version within minutes
if quality thresholds are exceeded.
- Infrastructure is defined as code so deployments are
reproducible and environments stay consistent.

**Common anti-patterns:**

- Deploying agent changes through manual console clicks or one-off
scripts without automated validation gates, making deployments
inconsistent and error-prone.
- Running only traditional unit tests without agent-specific
behavioral evaluation (prompt quality, tool selection accuracy,
hallucination rate), missing regressions that unit tests can't
detect.
- Deploying directly to production without staged rollout (canary,
blue/green), maximizing the scope of impact of any regression.
- Treating rollback as a theoretical capability that has never
been exercised, so the first time anyone uses it is during an
incident.

**Benefits of establishing this best
practice:**

- Automated pipelines help every deployment follow the same
validated path regardless of who starts it, reducing deployment
inconsistency.
- Behavioral validation gates provide empirical evidence that each
deployment meets quality standards before reaching production.
- Staged rollout and automated rollback compress incident response
time from hours to minutes when regressions appear.
- Infrastructure as code makes deployments reproducible across
environments, removing a common source of failures.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Agent CI/CD shares most of its structure with software CI/CD, with
one substantive addition: behavioral evaluation. The stages that
fit most agent workloads are:

- Source (code, prompts, configurations, and evaluation
datasets)
- Build (package artifacts and run unit tests)
- Evaluate (run behavioral evaluation through
[Amazon
Bedrock Evaluations](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation.html))
- Security scan (prompt injection vulnerabilities and IAM scope)
- Deploy to production

Task completion accuracy, hallucination rate, and tool selection
accuracy need explicit thresholds that block promotion when
exceeded. Thresholds that are set too loose produce false passes,
but thresholds that are set too tight block legitimate iteration.
To calibrate, start with thresholds tuned to the current baseline,
then tighten them as the agent's quality track record grows.

Production deployment uses
[Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html) for managed scaling, versioning,
and observability. agentcore deploy pushes new
versions, and endpoint-based weighted routing handles blue/green
and canary patterns.
[Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) alarms watch quality metrics post-deployment and
trigger automated rollback when thresholds are exceeded. The same
alarms that run during staged rollout double as rollback triggers.
Infrastructure as code through
[AWS CDK](https://aws.amazon.com/cdk/) or
[AWS CloudFormation](https://aws.amazon.com/cloudformation/) helps make every resource reproducible.

A rollback procedure that has never been exercised is a procedure
that may not work when the team needs it. Deliberate rollback
drills during pipeline validation confirm the revert works before
the team is depending on it.

### Implementation steps

- **Build the pipeline
stages:** Configure source, build, behavioral
evaluation, security scan, and production deployment stages
with the appropriate tools for each.
- **Set behavioral evaluation as a
gate:** Integrate
[Amazon
Bedrock Evaluations](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation.html) with task completion accuracy and
hallucination rate thresholds that block promotion when
exceeded.
- **Deploy to
[Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html):** Use built-in
versioning and endpoint-based weighted routing for
blue/green or canary rollouts.
- **Automate rollback on quality
threshold exceedance:** Wire
[Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) alarms to revert-deployment workflows so
quality threshold violations trigger immediate revert.
- **Version all deployment
artifacts:** Tag each artifact set with the
pipeline run ID for traceability, and store in a durable
versioned store.
- **Validate the full
pipeline:** Deliberately trigger a rollback during
pipeline validation to confirm revert procedures work before
they are needed for real.

## Resources

**Related best practices:**

- [AGENTOPS03-BP01 Define
an agent lifecycle with clear SME ownership, testing, and
governance](agentops03-bp01.html)
- [AGENTOPS02-BP03
Implement agent behavior versioning and rollback
capabilities](agentops02-bp03.html)
- [AGENTOPS06-BP03
Establish SME-driven validation and business approval
workflows](agentops06-bp03.html)
- [AGENTCOST06-BP02
Cost optimize versioning and deployment through efficient
artifact management](agentcost06-bp02.html)

**Related documents:**

- [Operationalizing
agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-operationalizing-agentic-ai/introduction.html)
- [Evolving
software delivery for agentic AI](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-operationalizing-agentic-ai/software-delivery.html)
- [Deploy
AI agents on Amazon Bedrock AgentCore using GitHub
Actions](https://aws.amazon.com/blogs/machine-learning/deploy-ai-agents-on-amazon-bedrock-agentcore-using-github-actions/)
- [Strands
Agents](https://strandsagents.com/)
- [CI/CD
and automation for serverless AI](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-serverless/cicd-and-automation.html)
- [Kiro
Hooks](https://kiro.dev/docs/hooks/)

**Related videos:**

- [AWS 2025 - Deploy Production-Ready Agents in 22 Minutes with
AgentCore Runtime](https://www.youtube.com/watch?v=Q-tYIAuv9WI)
- [AWS 2025 - Deploy ANY AI Agent to Production in Minutes -
AgentCore Tutorial](https://www.youtube.com/watch?v=N7FGbBq1mI4)
- [AWS 2025 - Strands Agents Observability, Evaluation, &
Deployment](https://www.youtube.com/watch?v=VgN-6_tmQHE)
- [AWS re:Invent 2024 - Building AI Agents with Serverless, Strands,
and MCP (NTA405)](https://www.youtube.com/watch?v=LwubRSoJcIM)
- [AWS re:Invent 2024 - Develop AI Agents faster with SageMaker AI
Studio & AgentCore (AIM388)](https://www.youtube.com/watch?v=UL_7a2GEu10)

**Related workshops:**

- [Getting
started with Amazon Bedrock AgentCore, Lab 4: Deploy to
Production](https://catalog.workshops.aws/agentcore-getting-started/en-US/60-add-runtime)

**Related services:**

- [Amazon
Bedrock](https://aws.amazon.com/bedrock/)
- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [AWS Cloud Development Kit (AWS CDK)](https://aws.amazon.com/cdk/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentops03-bp02.html*

---

# AGENTOPS03-BP03 Implement agent-specific scaling policies and capacity planning

Scaling policies designed for typical web workloads don't fit
agents. Model inference latency, tool dependency availability, and
downstream service capacity all shape the right response to load,
and a policy that ignores them either over-provisions during quiet
hours or under-provisions during peaks.

**Desired outcome:**

- Agent compute scales dynamically in response to demand while
respecting cost, performance, and governance constraints.
- Scaling decisions account for agent-specific factors: model
inference latency, tool availability, and downstream service
capacity.
- Per-environment scaling boundaries help prevent runaway scaling
in development while preserving capacity headroom in production.
- Monthly capacity reviews keep deployments right-sized as usage
patterns evolve.

**Common anti-patterns:**

- Using identical scaling configurations across all environments,
either over-provisioning development or under-provisioning
production during traffic spikes.
- Scaling based solely on CPU and memory utilization without
considering agent-specific metrics like request queue depth or
inference latency, missing the real bottleneck.
- Setting scaling policies once at deployment and never revisiting
them as usage patterns evolve.
- Treating capacity planning as a quarterly finance exercise
rather than an ongoing operational one, so policies fall out of
step with reality.

**Benefits of establishing this best
practice:**

- Scaling policies adapt to deployment context and agent compute
model, keeping capacity appropriate as workloads move from
prototype to production scale.
- Per-environment boundaries and centralized configuration make
scaling behavior consistent, auditable, and governed across
environments.
- Monthly reviews catch drift between configured capacity and
actual usage patterns before it becomes a cost or latency
problem.
- Agent-specific scaling metrics expose the real bottleneck, often
downstream service capacity or model throttling, that generic
metrics hide.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

[Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html) handles the scaling question for
most teams through its built-in consumption-based scaling and
pricing model. AgentCore Runtime allocates compute automatically
based on demand, so custom scaling policies are not required. For
agents deployed outside AgentCore Runtime, on
[AWS Lambda](https://aws.amazon.com/lambda/) or
[Amazon ECS](https://aws.amazon.com/ecs/)
for example, scaling triggers must be configured against
agent-specific signals: request queue depth, average response
latency, and concurrent invocation count. CPU and memory alone
miss the mark because agents often wait on model inference or
downstream tools rather than saturating local compute.

Configure environment-appropriate maximums to control cost in
development and maintain performance in production. Development
can run with permissive minimums and tight maximums. Cost is the
first consideration, so the policy should expect spikes and
throttle them. In production, maximums should be generous enough
to absorb traffic bursts without latency degradation, and minimums
should hold enough warm capacity to avoid cold starts during
demand ramps. Staging is the midpoint between development and
production, so maximums and minimums should match that as well.

Store scaling configurations centrally (like in a parameter store
integrated with the agent registry) so boundaries adjust
automatically when an agent transitions between lifecycle stages.
A configuration store also gives the team a single place to audit
and adjust policies, instead of chasing them through individual
service consoles.

The operations team should perform monthly reviews, analyzing
scaling event history, peak utilization patterns, and capacity
headroom across the portfolio using
[Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) metrics. The outputs are concrete:

- Agents to scale down
- Agents to increase ceilings for
- Demand forecasts for the upcoming period

Without this review, scaling policies drift from the workload they
were tuned against. For fleet-level operational visibility
including dashboards, anomaly detection, and behavioral
monitoring, see
[AGENTOPS05-BP05
Create workflow-specific dashboards for operational health](agentops05-bp05.html).

### Implementation steps

- **Choose the right scaling
foundation:** Deploy agents on
[Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html) for built-in scaling, or
configure auto scaling policies with agent-specific metrics
for non-Runtime deployments.
- **Set per-environment
boundaries:** Use permissive policies for
development, moderate for staging, and production with
higher minimums to absorb traffic spikes.
- **Centralize scaling
configurations:** Store policies in a parameter
store integrated with the agent registry so boundaries
adjust as agents transition between lifecycle stages.
- **Review capacity monthly:**
Analyze scaling events, peak utilization, and capacity
headroom in
[Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) to right-size deployments and forecast
demand.

## Resources

**Related best practices:**

- [AGENTOPS03-BP01 Define
an agent lifecycle with clear SME ownership, testing, and
governance](agentops03-bp01.html)
- [AGENTOPS03-BP02
Implement CI/CD pipelines tailored to agentic system
deployment (AgentOps)](agentops03-bp02.html)
- [AGENTOPS02-BP02
Implement configuration drift detection and remediation](agentops02-bp02.html)
- [AGENTOPS05-BP04
Define and track KPIs for agent workflows](agentops05-bp04.html)

**Related documents:**

- [Operationalizing
agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-operationalizing-agentic-ai/introduction.html)
- [Preparing
the business for agentic AI at scale](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-operationalizing-agentic-ai/preparing-business.html)
- [Introducing
Amazon Bedrock AgentCore: Securely deploy and operate AI
agents at any scale](https://aws.amazon.com/blogs/aws/introducing-amazon-bedrock-agentcore-securely-deploy-and-operate-ai-agents-at-any-scale/)
- [Securely
launch and scale your agents and tools on Amazon Bedrock
AgentCore Runtime](https://aws.amazon.com/blogs/machine-learning/securely-launch-and-scale-your-agents-and-tools-on-amazon-bedrock-agentcore-runtime/)

**Related videos:**

- [AWS 2025 - AgentCore Deep Dive: Runtime](https://www.youtube.com/watch?v=wizEw5a4gvM)

**Related services:**

- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentops03-bp03.html*

---

# AGENTOPS03-BP04 Implement organizational agent portfolio management and governance at scale

A handful of agents built by one team is a project. Dozens of agents
built by multiple teams is a portfolio, and portfolios need
different operational mechanisms. Without cross-organizational
visibility, teams build redundant agents, break each other's
integrations, and lose track of which agents still earn their keep.

**Desired outcome:**

- A centralized catalog gives the organization a current view of
every agent, owner, capabilities, dependencies, lifecycle state,
cost profile, and business value.
- Teams discover existing agents before building new ones, so
effort goes to capability gaps rather than duplicates.
- Cross-team dependencies are tracked and managed through
coordinated deprecation processes.
- Quarterly portfolio reviews reveal underutilized agents for
consolidation or retirement, keeping the portfolio aligned with
business priorities.

**Common anti-patterns:**

- Allowing teams to build agents independently without checking
for existing capabilities, creating redundant agents that
duplicate development cost, infrastructure cost, and operational
burden.
- Maintaining agent registries only within individual teams, so no
one has the cross-organizational view needed to identify
redundancy or assess overall system health.
- Deprecating or modifying agents without notifying dependent
teams, causing cascading failures when orchestrators or
delegating agents invoke agents that have changed.
- Treating agent creation as a no-justification-required activity,
so the portfolio grows faster than the organization's ability to
operate, monitor, and maintain it.
- Failing to measure business value relative to operational cost,
reducing the risk of data-driven decisions about which agents
warrant continued investment.

**Benefits of establishing this best
practice:**

- Portfolio governance scales operational practices from
individual agents to enterprise environments, so governance
overhead grows sub-linearly with agent count.
- A centralized catalog with ownership, dependency tracking, and
lifecycle state provides the auditable record needed for
compliance and organizational accountability.
- Capability search before build reduces redundant development,
freeing engineering effort for capability gaps.
- Quarterly reviews help prevent sprawl by revealing candidates
for consolidation and retirement before the portfolio becomes
unmanageable.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Portfolio governance extends the team-level registry into an
organizational catalog that spans team boundaries (for more
detail, see [AGENTOPS03-BP01
Define an agent lifecycle with clear SME ownership, testing, and
governance](agentops03-bp01.html)). The fields added at this layer are the ones
that support cross-team decisions:

- Owning team
- Business domain
- Upstream dependencies (agents or systems that invoke this
agent)
- Downstream dependencies (agents, tools, or services this agent
invokes)
- Cost-per-month (derived from CloudWatch and Cost Explorer)
- Business value indicators (task completion volume, business
outcome metrics).

[AWS Agent Registry](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/registry.html) provides the centralized catalog with
built-in approval workflows, flexible metadata, and hybrid search
(semantic and keyword) so cross-organizational queries run
efficiently. Enrich registry records with dependency metadata,
cost attribution, and business value indicators so the catalog
supports portfolio-level decisions beyond simple discovery.

The pre-creation review gate helps prevent duplicate builds. Teams
searching for specific agents by purpose will not find one through
keyword matching against agent names.
[AWS Agent Registry](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/registry.html) provides built-in hybrid search that
combines semantic understanding with keyword matching, so
natural-language capability queries reveal existing agents with
overlapping capabilities. When overlap exists, the requesting team
documents why the existing agent is insufficient before
proceeding.

This applies to code-based agents (Strands Agents, LangGraph) and
no-code agents built through
[Amazon Quick
Suite](https://aws.amazon.com/quicksuite/) alike. A lightweight CI/CD gate that checks the
registry and flags potential duplicates is enough for most
organizations, while heavy approval processes encourage bypass.

Implement cross-team dependency tracking as a managed practice.
Agents declare their upstream and downstream dependencies at
registration and update declarations when dependencies change.
[Amazon EventBridge](https://aws.amazon.com/eventbridge/) publishes events when agents are deprecated,
modified, or decommissioned so downstream teams receive advance
notice. Agents exposed through
[Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) benefit from Gateway's tool
registration metadata, which automatically tracks which agents
consume which tools and reduces manual declaration burden. A
dependency graph in
[Amazon Neptune](https://aws.amazon.com/neptune/) enables impact analysis for determining how a
change to one agent will affect others.

Quarterly portfolio reviews help prevent gradual drift. The review
assesses four dimensions:

- Utilization (which agents are actively used and which are
idle)
- Cost efficiency (which agents deliver business value
proportional to cost)
- Redundancy (which agents overlap with others)
- Health (which agents show elevated error rates, degraded
performance, or stale configurations)

The catalog is the primary data source, enriched with
[Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) metrics,
[AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) attribution, and the dependency graph.
Reviews produce concrete recommendations. These include agents to
consolidate, deprecate, or invest in, and cross-team dependency
risks to address.

### Implementation steps

- **Extend the agent registry into an
organizational catalog:** Use
[AWS Agent Registry](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/registry.html) to catalog agents with metadata for
owning team, business domain, upstream and downstream
dependencies, cost-per-month, and business value indicators.
- **Enable semantic capability
search:** Use Agent Registry's built-in hybrid
search so natural-language queries reveal overlapping
capabilities before new development begins.
- **Gate new agent creation on registry
search:** Add a pre-creation CI/CD check that
requires justification when overlapping agents exist.
- **Track cross-team
dependencies:** Use
[Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) to notify downstream teams when upstream
agents are deprecated, modified, or decommissioned.
- **Build a dependency graph:**
Use
[Amazon Neptune](https://docs.aws.amazon.com/neptune/latest/userguide/intro.html) to answer impact-analysis questions before
agent modifications.
- **Run quarterly portfolio
reviews:** Assess utilization, cost efficiency,
redundancy, and health, producing specific recommendations
for consolidation, deprecation, and investment.

## Resources

**Related best practices:**

- [AGENTOPS03-BP01 Define
an agent lifecycle with clear SME ownership, testing, and
governance](agentops03-bp01.html)
- [AGENTOPS03-BP02
Implement CI/CD pipelines tailored to agentic system
deployment (AgentOps)](agentops03-bp02.html)
- [AGENTOPS04-BP01
Implement tool registry and catalog management](agentops04-bp01.html)
- [AGENTOPS05-BP04
Define and track KPIs for agent workflows](agentops05-bp04.html)
- [AGENTCOST06-BP01
Implement lightweight discovery and registry for
cost-effective collaboration](agentcost06-bp01.html)

**Related documents:**

- [Operationalizing
agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-operationalizing-agentic-ai/introduction.html)
- [Preparing
the business for agentic AI at scale](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-operationalizing-agentic-ai/preparing-business.html)
- [AI
agents in enterprises: Best practices with Amazon Bedrock
AgentCore](https://aws.amazon.com/blogs/machine-learning/ai-agents-in-enterprises-best-practices-with-amazon-bedrock-agentcore/)

**Related videos:**

- [AWS re:Invent 2024 - Agents in the enterprise: Best practices with
AgentCore (AIM3310)](https://www.youtube.com/watch?v=w5XJxCpUADY)
- [AWS 2025 - AgentCore Registry: Discover, Govern, and Reuse AI
Agents at Scale](https://www.youtube.com/watch?v=rIcOJrE-fTk)
- [AWS re:Invent 2024 - Cox Automotive's Blueprint for Agentic AI on
AgentCore (IND3329)](https://www.youtube.com/watch?v=ICA8-d_Nt9Q)

**Related services:**

- [AWS Agent Registry](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/registry.html)
- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon EventBridge](https://aws.amazon.com/eventbridge/)
- [Amazon Neptune](https://aws.amazon.com/neptune/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
- [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentops03-bp04.html*

---
