# AGENTOPS06 — Testing, evaluation, and validation frameworks

**Pillar**: Operational Excellence  
**Best Practices**: 3

---

# AGENTOPS06-BP01 Design multi-layered testing frameworks

Traditional software testing, like exact-match assertions and
green-or-red unit tests, can miss important failure modes in agentic
systems. A testing pyramid that covers unit, integration, end-to-end
tests, and shadow layers helps teams catch behavioral regressions
before they reach users.

**Desired outcome:**

- Agent systems are covered by a testing pyramid that includes
unit tests, integration tests, end-to-end tests, and shadow
tests in production environments.
- Automated testing pipelines run on every code and configuration
change, providing rapid feedback on regressions.
- Test coverage metrics are tracked and maintained above defined
thresholds for all agent capabilities.
- Tests use semantic quality assessment rather than exact-match
comparison, so non-deterministic outputs don't break the suite.

**Common anti-patterns:**

- Testing only the happy path without covering edge cases, error
conditions, and adversarial inputs.
- Relying exclusively on unit tests without integration and
end-to-end tests, missing failures that only emerge when
components interact with real tools and services.
- Treating agent testing as equivalent to traditional software
testing without accounting for non-deterministic LLM outputs,
using exact string matching instead of semantic equivalence
checks.
- Running tests only in isolated environments without shadow
testing in production, missing environment-specific behaviors
that only manifest with real data and traffic patterns.
- Failing to maintain test datasets as capabilities evolve, so
tests become stale and lose regression-detection value.

**Benefits of establishing this best
practice:**

- A thorough testing framework provides the empirical evidence
needed to validate each behavioral iteration, enabling confident
deployment.
- Standardized testing procedures help validate every change
consistently, regardless of who made it or how urgent the
timeline.
- Semantic evaluation accepts legitimate output variation while
still catching regressions.
- Shadow testing validates behavioral changes against real traffic
without exposing users to the new version.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Four layers cover the testing surface for most agent systems.

Unit tests, the base layer, test individual components in
isolation: prompt templates, tool invocation logic, memory
retrieval, decision routing. LLM responses can be mocked where
determinism is needed, so unit tests stay fast and reproducible.

Integration tests, the second layer, validate agent-tool and
agent-to-agent interactions in a staging environment with real
endpoints, which is where many of the interesting failures emerge.

End-to-end tests, the third layer, validate complete workflows,
and this is where semantic evaluation matters more than exact
matching.
[Amazon
Bedrock Evaluations](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation.html) and
[Amazon
Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html) handle the semantic quality
assessment that end-to-end tests need. AgentCore Evaluations' 13
built-in evaluators provide standardized quality gates in CI/CD
pipelines (correctness, helpfulness, safety, and tool selection
accuracy), so regressions in output quality are detectable without
requiring bit-exact comparison. Custom evaluators cover
business-specific requirements.

Shadow tests, the top layer, run new versions in parallel with
production on real traffic using traffic mirroring, comparing
outputs without serving the new version's responses. This catches
environment-specific behavior that staging can't reproduce. The
cost is the infrastructure to run parallel inferences, and the
value is catching issues before users ever encounter them. For
teams developing agents with Kiro, hooks can trigger test runs on
file save and before deployment.

Integrate automated testing into CI/CD pipelines so every layer
blocks deployment on failure. Maintain test datasets with
versioning, and review them regularly to add new use cases and
failure modes discovered in production. The pyramid gets stronger
over time only if the suite grows with the system.

### Implementation steps

- **Define the four testing
layers:** Scope, tooling, and success criteria for
unit, integration, end-to-end, and shadow tests.
- **Implement unit and integration
tests:** Mock dependencies at the unit layer. Use
real staging endpoints for integration tests.
- **Create end-to-end scenarios with
semantic evaluation:** Use
[Amazon
Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html) for quality assessment
rather than exact-match assertions.
- **Add shadow testing with traffic
mirroring:** Validate behavioral changes against
real-world inputs without exposing users.
- **Integrate tests into
CI/CD:** Run the full suite on every commit and
block deployment on failures.

## Resources

**Related best practices:**

- [AGENTOPS06-BP02 Evaluate
and track ongoing agent performance](agentops06-bp02.html)
- [AGENTOPS06-BP03
Establish SME-driven validation and business approval
workflows](agentops06-bp03.html)
- [AGENTOPS03-BP02
Implement CI/CD pipelines tailored to agentic system
deployment (AgentOps)](agentops03-bp02.html)
- [AGENTPERF01-BP01
Define performance-aligned success criteria for agent
workloads](agentperf01-bp01.html)

**Related documents:**

- [Operationalizing
agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-operationalizing-agentic-ai/introduction.html)
- [Amazon
Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html)
- [Evaluating
AI agents: Real-world lessons from building agentic systems at
Amazon](https://aws.amazon.com/blogs/machine-learning/evaluating-ai-agents-real-world-lessons-from-building-agentic-systems-at-amazon/)
- [LLM-as-a-judge
on Amazon Bedrock Model Evaluation](https://aws.amazon.com/blogs/machine-learning/llm-as-a-judge-on-amazon-bedrock-model-evaluation/)
- [Evaluate
models in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation-judge.html)
- [Evaluating
AI agents for production: A practical guide to Strands
Evals](https://aws.amazon.com/blogs/machine-learning/evaluating-ai-agents-for-production-a-practical-guide-to-strands-evals/)
- [From
AI agent prototype to product: Lessons from building AWS
DevOps Agent](https://aws.amazon.com/blogs/devops/from-ai-agent-prototype-to-product-lessons-from-building-aws-devops-agent)
- [Kiro
Hooks](https://kiro.dev/docs/hooks/)

**Related videos:**

- [AWS 2025 - Strands Agents Observability, Evaluation, &
Deployment](https://www.youtube.com/watch?v=VgN-6_tmQHE)

**Related examples:**

- [GitHub:
awslabs/amazon-bedrock-agentcore-samples, Evaluations
tutorials](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/07-AgentCore-evaluations)
- [GitHub:
awslabs/amazon-bedrock-agent-samples, RAGAS evaluation](https://github.com/awslabs/amazon-bedrock-agent-samples/tree/main/examples/agents/ragas_evaluation_bedrock_agents)

**Related workshops:**

- [Getting
started with Amazon Bedrock AgentCore, Lab 5: Evaluate Agent
Performance](https://catalog.workshops.aws/agentcore-getting-started/en-US/65-evaluation)
- [Diving
Deep into Bedrock AgentCore, Evaluations](https://catalog.workshops.aws/agentcore-deep-dive/en-US/80-agentcore-evaluations)

**Related services:**

- [Amazon
Bedrock](https://aws.amazon.com/bedrock/)
- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentops06-bp01.html*

---

# AGENTOPS06-BP02 Evaluate and track ongoing agent performance

Pre-deployment evaluation validates that an agent is ready to ship.
Post-deployment evaluation validates that it still works. Without
continuous assessment, gradual quality degradation from data drift,
model updates, and shifting user patterns goes unnoticed until it is
expensive to fix.

**Desired outcome:**

- Agent performance is continually evaluated against defined
quality benchmarks.
- Automated pipelines detect degradation in output quality,
reasoning accuracy, and business outcome alignment.
- Teams have clear visibility into performance trends over time
and can correlate quality changes with specific configuration,
model, or data updates.
- Evaluation results drive prioritized improvement actions and
provide objective evidence for stakeholder reporting.

**Common anti-patterns:**

- Evaluating agent performance only at deployment time without
continuous post-deployment assessment, missing gradual
degradation from data drift, model updates, or changing user
patterns.
- Relying solely on automated metrics without periodic human
evaluation, missing quality dimensions that automated metrics
can't fully capture (like nuance, appropriateness, and business
context alignment).
- Using generic evaluation criteria across all agents without
tailoring metrics to each agent's specific use case and business
objectives, producing evaluation results that don't reflect
actual value.
- Treating evaluation as separate from operations rather than
integrating it into the operational workflow, creating
evaluation debt that accumulates over time.

**Benefits of establishing this best
practice:**

- Continuous evaluation provides an empirical foundation for
evidence-based improvement, identifying which agents need
attention and which changes produce measurable gains.
- Performance trend tracking reveals patterns that inform
systematic improvement, turning evaluation data into practical
insights.
- Multi-dimensional scoring catches quality issues that a single
metric would miss.
- Correlation between quality shifts and configuration changes
compresses root-cause analysis.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

[Amazon
Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html) is an evaluation service for
continuous assessment. Its on-demand mode runs benchmarks during
development, and its online mode samples and evaluates live
interactions in production without requiring manual triggers.
Thirteen built-in evaluators cover correctness, helpfulness,
safety, and tool selection accuracy, with custom evaluators
available for business-specific requirements.
[Amazon
Bedrock Evaluations](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation.html) supplements this with model-level
assessment, and periodic human evaluation covers the dimensions
automated metrics miss.

Evaluation frameworks need multiple dimensions because a single
metric misses too much. For example:

- Output quality (relevance, accuracy, coherence) measures
whether responses are good.
- Safety (hallucination rate, toxicity, guardrail adherence)
measures whether responses are safe.
- Efficiency (task completion rate, tool invocation success)
measures whether the agent is economical.
- Business alignment (outcome achievement, user satisfaction,
SLA compliance) measures whether the agent delivers value.

Weighting depends on the use case. For instance, a
customer-support agent might weigh satisfaction higher than
efficiency, while an internal automation agent might weigh
efficiency higher than relevance. Generic weighting produces
generic results.

Dashboards that show evaluation scores over time make degradation
visible before it becomes an incident. Alerting on threshold
violations and on persistent negative trends, as opposed to
single-point dips, catches the slow-moving problems that are
hardest to diagnose after the fact. Correlate evaluation shifts
with configuration and model changes so attribution is fast when a
metric moves.

LLM-as-a-Judge patterns can use multiple evaluator prompts
covering different quality dimensions to produce a composite score
that is more reliable than any single prompt. Periodic human
review validates the automated scores and catches the blind spots.

### Implementation steps

- **Configure
[Amazon
Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html):** Use
on-demand mode for development benchmarking and online mode
for continuous production monitoring.
- **Define a multi-dimensional
evaluation framework:** Apply use-case-specific
weighting across quality, safety, efficiency, and business
alignment.
- **Implement LLM-as-judge
patterns:** Use multiple evaluator prompts and
supplement with periodic human evaluation.
- **Build evaluation
dashboards:** Show trends over time with alerting
for threshold violations and persistent negative trends.
- **Correlate evaluation results with
change events:** Tag deployments, configuration
updates, and model changes so quality shifts can be
attributed quickly.

## Resources

**Related best practices:**

- [AGENTOPS06-BP01 Design
multi-layered testing frameworks](agentops06-bp01.html)
- [AGENTOPS06-BP03
Establish SME-driven validation and business approval
workflows](agentops06-bp03.html)
- [AGENTOPS02-BP04
Maintain feedback control loops for continuous
improvement](agentops02-bp04.html)
- [AGENTOPS05-BP04
Define and track KPIs for agent workflows](agentops05-bp04.html)
- [AGENTPERF01-BP01
Define performance-aligned success criteria for agent
workloads](agentperf01-bp01.html)

**Related documents:**

- [Amazon
Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html)
- [Evaluate
models in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation-judge.html)
- [Operationalizing
agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-operationalizing-agentic-ai/introduction.html)
- [Build
reliable AI agents with Amazon Bedrock AgentCore
Evaluations](https://aws.amazon.com/blogs/machine-learning/build-reliable-ai-agents-with-amazon-bedrock-agentcore-evaluations/)
- [LLM-as-a-judge
on Amazon Bedrock Model Evaluation](https://aws.amazon.com/blogs/machine-learning/llm-as-a-judge-on-amazon-bedrock-model-evaluation/)
- [Evaluating
AI agents for production: A practical guide to Strands
Evals](https://aws.amazon.com/blogs/machine-learning/evaluating-ai-agents-for-production-a-practical-guide-to-strands-evals/)
- [From
AI agent prototype to product: Lessons from building AWS
DevOps Agent](https://aws.amazon.com/blogs/devops/from-ai-agent-prototype-to-product-lessons-from-building-aws-devops-agent)

**Related workshops:**

- [Getting
started with Amazon Bedrock AgentCore, Lab 5: Evaluate Agent
Performance](https://catalog.workshops.aws/agentcore-getting-started/en-US/65-evaluation)
- [Diving
Deep into Bedrock AgentCore, Evaluations](https://catalog.workshops.aws/agentcore-deep-dive/en-US/80-agentcore-evaluations)

**Related services:**

- [Amazon
Bedrock](https://aws.amazon.com/bedrock/)
- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentops06-bp02.html*

---

# AGENTOPS06-BP03 Establish SME-driven validation and business approval workflows

Heavy approval processes slow routine work and get bypassed in
emergencies. On the other hand, a lack of approval processes can
produce unforeseen incidents. To keep your teams moving while
protecting against the changes that actually warrant scrutiny,
implement risk-tiered validation (light for minor changes, thorough
for autonomy increases).

**Desired outcome:**

- Significant agent changes pass through documented validation and
approval workflows before reaching production.
- Validation checkpoints verify that changes meet quality
thresholds, maintain behavioral alignment, and comply with
operational boundaries.
- Rollback procedures are defined and tested for every change
type.
- Approval burden scales with change risk, not uniformly across
all changes.

**Common anti-patterns:**

- Applying the same lightweight approval process to all changes
regardless of risk, treating a minor prompt wording adjustment
the same as a change that increases agent autonomy or adds new
tool access.
- Implementing approval workflows that require human sign-off for
every change without risk-based tiering, creating bottlenecks
that slow iteration and incentivize bypass.
- Defining validation checkpoints without specifying the criteria
that must be met to pass, leaving approvers without objective
standards and producing inconsistent decisions.
- Failing to test rollback procedures before they are needed,
discovering that rollback is broken only when an incident
requires rapid recovery.
- Treating validation as a one-time deployment gate rather than a
continuous process, missing quality degradation after
deployment.

**Benefits of establishing this best
practice:**

- Risk-tiered approval workflows help route changes with
significant potential impact to appropriate human scrutiny,
while low-risk changes proceed with minimal friction.
- Documented validation and approval create an auditable record of
every change decision for compliance purposes.
- Tested rollback procedures compress incident response time when
validated changes still produce unexpected outcomes.
- Automated validation gates catch regressions before human
approvers ever see the change.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Risk tiering creates a workable approval process.

- Tier 1, low risk, covers minor prompt wording changes, logging
configuration adjustments, and similar edits that can't
materially alter agent behavior. These require automated
validation only.
- Tier 2, medium risk, covers new tool integrations, prompt
structural changes, and model parameter adjustments. These
require automated validation plus peer review.
- Tier 3, high risk, covers autonomy level increases, new tool
categories, model changes, and guardrail modifications. These
require automated validation plus multi-stakeholder approval
including technical lead and business owner.

Automated validation should run before any human approval.
[Amazon
Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html) score thresholds, behavioral
regression tests, security scans, and performance benchmarks all
gate promotion. A change that fails automated validation never
consumes human review time, as the team stays focused on the
decisions that genuinely require judgment.

Approval routing needs to handle timeouts. A change waiting on an
unavailable approver for multiple days risks being bypassed or
dropped. Timeout escalation, either through automatic approval for
low-risk changes or escalation to a backup approver for
higher-risk ones, keeps the process moving.

Rollback is a recovery path for changes that passed validation and
still produced unexpected outcomes. Automated rollback triggered
by post-deployment quality threshold violations is the default,
while manual rollback remains available for edge cases. For tiered
human oversight patterns in reliability contexts, see
[AGENTREL02-BP05
Establish tiered human oversight and approval workflows](agentrel02-bp05.html).

### Implementation steps

- **Define a risk-tiered change
classification:** Spell out the criteria for Tier
1, Tier 2, and Tier 3 so changes are classified
consistently.
- **Define automated validation
checkpoints:** Include evaluation score thresholds
from
[Amazon
Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html), regression tests,
security scans, and performance benchmarks.
- **Implement approval
workflows:** Route changes by tier with timeout
escalation for non-responsive approvers.
- **Automate rollback on quality
threshold exceedance:** Wire post-deployment
quality metrics to revert workflows.
- **Test rollback procedures
quarterly:** Document results and update procedures
as the runtime evolves.

## Resources

**Related best practices:**

- [AGENTOPS06-BP01 Design
multi-layered testing frameworks](agentops06-bp01.html)
- [AGENTOPS06-BP02 Evaluate
and track ongoing agent performance](agentops06-bp02.html)
- [AGENTOPS03-BP02
Implement CI/CD pipelines tailored to agentic system
deployment (AgentOps)](agentops03-bp02.html)
- [AGENTREL02-BP05
Establish tiered human oversight and approval workflows](agentrel02-bp05.html)
- [AGENTSEC04-BP02
Human-in-the-loop for critical decisions](agentsec04-bp02.html)

**Related documents:**

- [Operationalizing
agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-operationalizing-agentic-ai/introduction.html)
- [Operationalizing
agentic AI, Part 1: A stakeholder's guide](https://aws.amazon.com/blogs/machine-learning/operationalizing-agentic-ai-part-1-a-stakeholders-guide/)
- [Preparing
your business for agentic AI](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-operationalizing-agentic-ai/preparing-business.html)
- [Advancing
AI agent governance with Boomi and AWS: A unified approach to
observability and compliance](https://aws.amazon.com/blogs/machine-learning/advancing-ai-agent-governance-with-boomi-and-aws-a-unified-approach-to-observability-and-compliance)

**Related services:**

- [Amazon
Bedrock](https://aws.amazon.com/bedrock/)
- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentops06-bp03.html*

---
