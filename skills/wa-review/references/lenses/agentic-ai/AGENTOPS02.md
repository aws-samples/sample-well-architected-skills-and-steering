# AGENTOPS02 — Prompt and configuration lifecycle management

**Pillar**: Operational Excellence  
**Best Practices**: 4

---

# AGENTOPS02-BP01 Evolve agent prompts, tool calls, and configurations to reflect evolving business needs

A prompt shapes agent behavior more directly than almost any other
configuration artifact. Create a prompt lifecycle that applies
code-grade discipline, versioning, review, evaluation, and rollback
to prompts, which helps avoid unnoticed prompt drift and degraded
decisions in agent interactions.

**Desired outcome:**

- You manage agent prompts through a defined lifecycle: authoring,
review, testing, deployment, monitoring, and retirement.
- Every production prompt has a documented version history, an
evaluation record, and a clear owner.
- You deploy prompt updates independently of application code and
roll back to a previous version within minutes.
- You track the performance impact of each prompt change over time
and can attribute quality shifts to specific versions.

**Common anti-patterns:**

- Hardcoding prompts directly in application code, making it
impossible to update agent behavior without a full code
deployment and blocking independent prompt iteration.
- Deploying prompt changes directly to production without
evaluation against quality benchmarks, discovering regressions
only after users report them.
- Operating without prompt version history, making it impossible
to determine which prompt change caused a behavioral regression
or to roll back to a known-good version.
- Treating prompt changes as too small to require review, letting
ad-hoc edits accumulate into drift that no one owns.

**Benefits of establishing this best
practice:**

- Behavioral changes follow a consistent, auditable path from
authoring to deployment, reducing operational risk and enabling
reliable rollback.
- Prompt performance tracking and evaluation create an empirical
basis for iteration. Each update is validated against measurable
quality criteria before reaching production.
- Teams can deploy prompt changes independently of application
code, shortening the feedback loop between business need and
runtime behavior.
- Failed prompt updates revert in minutes rather than requiring an
incident response.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Treat prompts as first-class operational artifacts with the same
discipline applied to application code. Application code moves
through version control, code review, automated tests, staged
deployment, and documented rollback. Most organizations apply none
of these to prompts, which can result in agent behavior drifts.
Apply the same lifecycle to prompts as you do to code, where you
name the stages explicitly and require changes to follow them.

[Amazon
Bedrock Prompt Management](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management.html) provides versioning, metadata,
and integration with
[Amazon
Bedrock Evaluations](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation.html). For no-code paths built with
[Amazon Quick
Suite](https://aws.amazon.com/quicksuite/), the same stages apply through the identity and
instructions configuration. A four-stage lifecycle works for most
teams:

- Draft (under development, not deployed)
- Review (under peer review and evaluation)
- Active (deployed to production)
- Archived (retired but retained for audit)

Gate stage transitions by approval workflows implemented in
[AWS CodePipeline](https://aws.amazon.com/codepipeline/) or
[AWS Step Functions](https://aws.amazon.com/step-functions/), not by convention.

Every prompt entry needs required metadata: purpose, target agent,
expected behavior, evaluation criteria, and owner.
Parameterization should be used to reduce duplication across
related agents. Steering files in Kiro or equivalent conventions
codify these standards so they are applied automatically during
development rather than enforced after the fact.

[Amazon
Bedrock Evaluations](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation.html) runs each prompt version against a
standardized dataset and produces scores for task success,
response relevance, and adherence to behavioral guidelines. A
prompt that can't meet its minimum thresholds doesn't advance from
review to active. Once in production, quality metrics published to
[Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) as custom metrics give the team an early warning
when a prompt that passed evaluation starts degrading in the real
world, triggering a review workflow.

### Implementation steps

- **Stand up the central prompt
repository:** Configure
[Amazon
Bedrock Prompt Management](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management.html) with four lifecycle stages
(draft, review, active, archived) and required metadata
fields (purpose, target agent, expected behavior, evaluation
criteria, owner).
- **Define prompt authoring
standards:** Specify required metadata, formatting
conventions, and documentation requirements. Apply them
through shared templates or steering files so they are
enforced during development.
- **Build versioned evaluation
datasets:** Create datasets for each agent's
primary use cases and store them with versioning enabled so
evaluation results are reproducible.
- **Gate transitions on automated
evaluation:** Configure an
[Amazon
Bedrock Evaluations](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation.html) pipeline that runs on every
transition from draft to review, with minimum quality
thresholds.
- **Enforce lifecycle stages in
CI/CD:** Use
[AWS CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html) to block promotion to active without
approval and evaluation threshold checks.
- **Reference prompts by ID, not by
value:** Deploy agents with parameterized
references to the prompt repository rather than hardcoded
strings, so prompts evolve independently of application
code.
- **Monitor active prompts in
production:** Publish quality metrics to
[Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html), build dashboards per agent, and configure
alarms that trigger review workflows when thresholds are
exceeded.

## Resources

**Related best practices:**

- [AGENTOPS01-BP03 Develop test scenarios that accurately capture failures of dependent components, orchestration protocols, and business processes](agentops01-bp03.html)
- [AGENTOPS02-BP03
Implement agent behavior versioning and rollback capabilities](agentops02-bp03.html)
- [AGENTOPS06-BP01
Design multi-layered testing frameworks](agentops06-bp01.html)
- [AGENTREL02-BP04
Develop clear instruction protocols for agents](agentrel02-bp04.html)

**Related documents:**

- [Operationalizing agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-operationalizing-agentic-ai/introduction.html)
- [Evolving software delivery for agentic AI](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-operationalizing-agentic-ai/software-delivery.html)
- [AI agents in enterprises: Best practices with Amazon Bedrock AgentCore](https://aws.amazon.com/blogs/machine-learning/ai-agents-in-enterprises-best-practices-with-amazon-bedrock-agentcore/)
- [Kiro](https://kiro.dev/)
- [Kiro
Steering](https://kiro.dev/docs/steering/)

**Related videos:**

- [AWS 2025 - Amazon Bedrock Prompt Management Demo](https://www.youtube.com/watch?v=CE_-zrMvcuk)
- [AWS re:Invent 2024 - Responsible generative AI: Evaluation best practices and tools (AIM342)](https://www.youtube.com/watch?v=wuVpCc5a81Y)

**Related examples:**

- [GitHub:
Sample Bedrock Evaluation Adapter](https://github.com/aws-samples/sample-bedrock-evaluation-adapter)
- [GitHub:
Sample Bedrock Model Evaluation](https://github.com/aws-samples/sample-bedrock-model-evaluation)
- [GitHub:
Amazon Bedrock Samples, GenAI Quick-Start PoCs](https://github.com/aws-samples/genai-quickstart-pocs)

**Related services:**

- [Amazon
Bedrock](https://aws.amazon.com/bedrock/)
- [AWS CodePipeline](https://aws.amazon.com/codepipeline/)
- [Amazon S3](https://aws.amazon.com/s3/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentops02-bp01.html*

---

# AGENTOPS02-BP02 Implement configuration drift detection and remediation

Configurations can drift, creating outdated or unstable versions
over time. For example, a manual tweak in one environment, a
guardrail flag changed during an incident, or an experimental
override never reverted can produce agents that behave differently
in production than in testing. Automated drift detection catches
these events before they turn into incidents.

**Desired outcome:**

- Agent configurations stay consistent with approved baselines
across every environment.
- Unauthorized or unintended changes are detected and remediated
automatically.
- Every configuration change follows a documented approval
workflow with a full audit trail.
- Cross-environment consistency is validated continually so
development, staging, and production don't drift apart.

**Common anti-patterns:**

- Managing agent configurations through manual console changes
without version control, making it impossible to track what
changed, when, and by whom.
- Allowing different environments to drift apart without automated
consistency checks, so agents behave differently in production
than in testing.
- Detecting configuration drift only after it causes a production
incident rather than through proactive monitoring.
- Treating behavioral configurations (system prompts, guardrail
settings) as low-risk and skipping approval workflows for
changes that fundamentally alter agent behavior.

**Benefits of establishing this best
practice:**

- Automated drift detection helps keep agent configurations inside
approved boundaries continually, supporting audit requirements
and reducing the risk of unauthorized behavioral change.
- Configuration monitoring provides visibility beyond runtime
metrics, exposing issues at the configuration layer before they
manifest as behavioral problems.
- Cross-environment consistency validation helps detect failures
that passed in testing or staging environments by detecting
divergence between environments early.
- Change events are captured with full attribution, making
root-cause analysis faster when incidents do occur.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

First, determine your source of truth for configuration. If
approved baselines live in a wiki, a shell history, or in the AWS
console, then drift detection has nothing to compare against.
Storing baselines as infrastructure as code (IaC) in
[AWS CloudFormation](https://aws.amazon.com/cloudformation/) or the
[AWS Cloud Development Kit (AWS CDK)](https://aws.amazon.com/cdk/) gives every deployment a reproducible
reference point and makes the IaC definition the single artifact
that authoritatively determines what resources should look like.

[AWS CloudFormation drift detection](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html) reveals when deployed
resources have diverged from their stack definitions.
[AWS Config](https://aws.amazon.com/config/) rules add the runtime layer, monitoring agent
infrastructure continuously and triggering automated remediation
when deviations appear.
[AWS CloudTrail](https://aws.amazon.com/cloudtrail/) captures every configuration change event with
full attribution, so when drift is detected, the team can
determine exactly how a change was made without reconstructing
events.

Behavioral configurations, system prompts, guardrail settings,
tool permissions, and decision boundaries need a parallel track
because they don't consistently sit in CloudFormation-manageable
resources. A versioned configuration store with strict access
controls and change notifications handles this layer. Production
changes should require documented justification and sign-off.

The goal isn't to slow teams down but to send a prompt adjustment
that alters downstream behavior through the same review as a code
change. Teams using steering files in Kiro or equivalent can
codify configuration standards so drift is less likely to be
introduced at the source.

Scheduled cross-environment validation catches the slow category
of drift that single-event detection misses. Snapshot the
configuration of each environment on a cadence, compare the
snapshots, and alert on any discrepancy that isn't explained by an
approved change. This check reveals drift that accumulated
gradually over months rather than arriving in a single event.

### Implementation steps

- **Define configuration baselines as
IaC:** Store agent infrastructure definitions in
[AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) or
[AWS CDK](https://docs.aws.amazon.com/cdk/v2/guide/home.html) under version control, with the IaC definition as
the single source of truth.
- **Configure drift
detection:** Use
[AWS CloudFormation drift detection](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html) for infrastructure and
[AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html) rules for agent-specific configurations
(guardrail settings, model parameters) against approved
baselines.
- **Enable change event capture with
full attribution:** Turn on
[AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) and route change events to alerting and
automated remediation workflows.
- **Version behavioral
configurations:** Store prompts, guardrail
settings, and decision boundaries in a versioned
configuration store with access controls and mandatory
approval workflows for production changes.
- **Validate cross-environment
consistency on a schedule:** Compare configuration
snapshots across development, staging, and production, and
alert on unexplained discrepancies.

## Resources

**Related best practices:**

- [AGENTOPS02-BP01 Evolve
agent prompts, tool calls, and configurations to reflect
evolving business needs](agentops02-bp01.html)
- [AGENTOPS02-BP03
Implement agent behavior versioning and rollback
capabilities](agentops02-bp03.html)
- [AGENTOPS03-BP01
Define an agent lifecycle with clear SME ownership, testing,
and governance](agentops03-bp01.html)
- [AGENTREL08-BP01
Establish consistent configuration management practices](agentrel08-bp01.html)

**Related documents:**

- [Operationalizing
agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-operationalizing-agentic-ai/introduction.html)
- [Guidance
for Agentic AI Operational Foundations on AWS](https://aws.amazon.com/solutions/guidance/agentic-ai-operational-foundations-on-aws/)
- [Kiro
Steering](https://kiro.dev/docs/steering/)
- [Evolving
software delivery for agentic AI](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-operationalizing-agentic-ai/software-delivery.html)

**Related videos:**

- [AWS re:Invent 2024 - Architecting scalable and secure agentic AI
with AgentCore (AIM431)](https://www.youtube.com/watch?v=wqmeZOT6mmc)

**Related examples:**

- [GitHub:
Sample Agentic Platform on AWS](https://github.com/aws-samples/sample-agentic-platform)

**Related services:**

- [AWS Config](https://aws.amazon.com/config/)
- [AWS CloudTrail](https://aws.amazon.com/cloudtrail/)
- [AWS CloudFormation](https://aws.amazon.com/cloudformation/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentops02-bp02.html*

---

# AGENTOPS02-BP03 Implement agent behavior versioning and rollback capabilities

Teams with versioned behavior and tested rollback can recover in
minutes when an agent behaves unexpectedly, while teams without
spend hours debugging under pressure. Rapid reversibility improves
your organization's ability to confidently iterate on an agentic
system.

**Desired outcome:**

- Every agent behavioral configuration (system prompts, reasoning
instructions, tool permissions, and decision boundaries) is
versioned with a complete change history.
- You can roll back to any previous behavioral version within
minutes when a change produces undesired outcomes.
- Rollback procedures are automated and tested regularly, not
improvised during incidents.
- Staged rollouts limit the scope of impact of behavioral changes,
and A/B testing supports data-driven comparison of variants
before full deployment.

**Common anti-patterns:**

- Deploying behavioral changes to 100% of traffic immediately
without staged rollout, maximizing the scope of impact when a
change produces undesired outcomes.
- Operating without a defined behavioral baseline, the last
known-good configuration, so rollback becomes a manual search
for which previous version was stable.
- Treating prompt changes as low-risk because they don't involve
code changes, skipping evaluation and staged rollout for
modifications that can fundamentally alter agent behavior.
- Running A/B tests without statistical discipline, making
deployment decisions from noise rather than signal.

**Benefits of establishing this best
practice:**

- Systematic versioning and rollback create a safety net that lets
teams iterate on agent behavior confidently, knowing any change
can be reversed quickly.
- A/B testing frameworks and behavioral baselines provide the
empirical foundation for continuous improvement, validating that
each iteration produces measurable gains.
- Staged rollouts limit the users affected by a regression, giving
the team detection and correction time before full exposure.
- Change impact assessment ties quality metric shifts to specific
behavioral versions, making attribution direct instead of
inferred.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

[Amazon
Bedrock Prompt Management](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management.html) handles prompt-based
configurations with built-in semantic versioning, metadata, and
integration with evaluation. Non-prompt configurations (tool
permissions, decision boundaries, and escalation thresholds)
should be stored in a versioned configuration store with change
tracking. Each version should carry a semantic version number, a
change description, an author, and a reference to its evaluation
results.

A behavioral baseline is a version that the team has explicitly
designated as known-good, not just the previous version, because
the previous version might have been shipped an hour ago and never
proven stable. Rollback should restore the baseline, not the last
change, unless the team has explicitly promoted that change to
baseline status. Without a designated baseline, rollback requires
searching through multiple versions to find a stable
configuration.

Rollback itself should be automated and rehearsed. Design rollback
as an automated workflow triggered by either manual approval or by
automated quality threshold violations from
[Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) alarms. The target time-to-restore should be
under five minutes for behavioral changes. Anything longer means
the workflow has too many manual steps or too many dependencies
that aren't pre-staged. Exercise the rollback quarterly so the
procedure stays current with the runtime. For example, a rollback
that was written six months ago and never run is a rollback that
may not work.

Staged rollout limits the scope of impact before rollback is ever
needed.
[Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html) endpoint-based weighted routing
makes this straightforward. Start a new behavioral version at
5–10% of traffic, monitor quality metrics, and promote only when
the signal is clean. A/B testing uses the same machinery for
different ends, splitting traffic between variants to measure
which performs better. The critical additions are per-variant
metrics in CloudWatch and statistical significance testing before
deployment decisions. Document the evaluation criteria and results
alongside the behavioral version record so the comparison is
reproducible.

Perform impact assessments where you correlate version deployment
timestamps with changes in quality metrics to attribute metric
shifts to specific behavioral updates. When a metric moves, the
team should quickly determine which version caused the issue as
opposed to pattern-matching different dashboards to find the
problematic version.

### Implementation steps

- **Enable semantic versioning for
prompts:** Configure
[Amazon
Bedrock Prompt Management](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management.html) with metadata fields for
change description, author, and evaluation results on every
version.
- **Version non-prompt
configurations:** Store tool permissions, decision
boundaries, and escalation thresholds in a versioned
configuration store with change tracking and notifications.
- **Designate behavioral
baselines:** Tag and document the last known-good
configuration for each agent as the rollback target,
distinct from the most recent version.
- **Automate rollback:** Build
workflows that restore baselines within five minutes,
triggered by manual approval or automated quality threshold
violations from
[Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) alarms.
- **Configure staged rollout:**
Use
[Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html) endpoint-based weighted
routing starting at 5–10% traffic for new behavioral
versions, with automated promotion gates.
- **Set up A/B testing
infrastructure:** Capture per-variant metrics in
[Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) with statistical significance tracking
before deployment decisions.
- **Correlate deployments to metric
shifts:** Record deployment timestamps alongside
quality metric trends so changes can be attributed to
specific versions.

## Resources

**Related best practices:**

- [AGENTOPS02-BP01 Evolve
agent prompts, tool calls, and configurations to reflect
evolving business needs](agentops02-bp01.html)
- [AGENTOPS02-BP02
Implement configuration drift detection and remediation](agentops02-bp02.html)
- [AGENTOPS03-BP02
Implement CI/CD pipelines tailored to agentic system
deployment (AgentOps)](agentops03-bp02.html)

**Related documents:**

- [Operationalizing
agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-operationalizing-agentic-ai/introduction.html)
- [Evolving
software delivery for agentic AI](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-operationalizing-agentic-ai/software-delivery.html)
- [Deploy
AI agents on Amazon Bedrock AgentCore using GitHub
Actions](https://aws.amazon.com/blogs/machine-learning/deploy-ai-agents-on-amazon-bedrock-agentcore-using-github-actions/)

**Related videos:**

- [AWS re:Invent 2024 - Architecting scalable and secure agentic AI
with AgentCore (AIM431)](https://www.youtube.com/watch?v=wqmeZOT6mmc)
- [AWS re:Invent 2024 - Amazon Bedrock Agents and AgentCore Design
Patterns (TNC322)](https://www.youtube.com/watch?v=GYlPFmrATjU)

**Related examples:**

- [GitHub:
Sample Agentic Platform on AWS](https://github.com/aws-samples/sample-agentic-platform)
- [GitHub:
Amazon Bedrock Samples, GenAI Quick-Start PoCs](https://github.com/aws-samples/genai-quickstart-pocs)

**Related services:**

- [Amazon
Bedrock](https://aws.amazon.com/bedrock/)
- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentops02-bp03.html*

---

# AGENTOPS02-BP04 Maintain feedback control loops for continuous improvement

Agents that improve in step with real-world usage outperform agents
frozen at deployment. A working feedback loop connects quality
signals, user feedback, behavioral cues, and business outcomes to
prioritized improvement actions.

**Desired outcome:**

- You collect and correlate agent performance data, user feedback,
and business outcome metrics systematically, not through ad-hoc
surveys.
- Feedback loops operate continually, detecting quality trends in
near real time rather than through quarterly reviews.
- Improvement actions are tracked from identification through
implementation and validation.
- Feedback signals are attributable to specific agent versions, so
teams know which improvements are responding to which problems.

**Common anti-patterns:**

- Collecting user feedback (like thumbs up and down or ratings)
without connecting it to specific agent behaviors or prompt
versions, making it impossible to attribute quality changes to
improvements.
- Relying solely on periodic manual reviews rather than continuous
automated feedback processing, allowing quality degradation to
persist for weeks before detection.
- Collecting feedback data without a defined process for turning
insights into improvement actions, creating a growing backlog of
signals that never translate into agent changes.
- Mixing signal types into a single bucket, so a surge in
automated quality alerts drowns out a handful of high-severity
user reports that deserve immediate attention.

**Benefits of establishing this best
practice:**

- Structured feedback turns operational data into a continuous
source of improvement signals, so agents evolve in response to
real usage rather than staying static after deployment.
- Feedback-driven prioritization directs development effort toward
changes with the greatest measurable impact.
- Trend tracking over time reveals patterns (data drift, concept
drift, and scope drift) that inform targeted refinement rather
than scattershot tweaking.
- Improvement validation gives the team evidence that each change
delivered the expected gain.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Feedback loops should watch more than one signal to be truly
useful.

Automated quality metrics from
[Amazon
Bedrock Evaluations](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation.html) and
[Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) show measurable shifts in output quality.

To watch subjective perception, consider checking:

- Explicit user feedback
- Thumbs up and down
- Ratings
- Free-text comments

To determine whether users are finding what they need, consider
checking:

- Implicit behavioral signals
- Task abandonment
- Escalation rates
- Retry patterns

To determine if the agent is adhering to your organization's
goals, consider checking:

- Business outcome metrics
- Conversion rate
- Resolution time
- Customer satisfaction

Each channel catches failures the others miss, so collecting all
four of these metric pathways and routing them through a unified
processing pipeline is the minimum viable design.

Use event-driven ingestion to keep your pipeline scalable.
[Amazon EventBridge](https://aws.amazon.com/eventbridge/) or an equivalent event bus takes feedback
events from every channel and routes them to a processing layer
that classifies by type (quality issue, capability gap, tool
failure, behavioral misalignment), severity, and affected
component. Storing processed feedback in
[Amazon DynamoDB](https://aws.amazon.com/dynamodb/) with indexing by agent, feedback type, and time
period makes trend analysis and querying practical instead of
painful.

Consider implementing severity-based routing to avoid drowning
your teams in constant alerts. High-severity feedback, a user
reporting the agent did something dangerous, or a sudden drop in a
quality metric goes straight to an immediate-review queue.
Lower-severity feedback aggregates into batch reviews that surface
patterns over days rather than requiring immediate reactions.

Verify that you have an effective improvement tracking workflow.
To keep your feedback process useful and actionable, you need:

- A durable workflow
- Identification
- Root cause analysis
- Improvement design
- Implementation
- Validation
- Correlation to the specific feedback that prompted the action
- Metrics compared before and after each change

Validation is the step most often skipped, and the one that tells
the team whether an improvement was truly effective.

Dashboards help you address visibility of both feedback and
improvements. Feedback trends alongside improvement outcomes
provide a clear view of whether the agent's quality trajectory is
rising, flat, or falling, and which improvements are responsible
for each inflection.

### Implementation steps

- **Implement multi-channel feedback
collection:** Cover automated quality metrics
(through
[Amazon
Bedrock Evaluations](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation.html) and
[Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html)), explicit user feedback, implicit
behavioral signals, and business outcome metrics.
- **Classify feedback at
ingestion:** Categorize by type (quality issue,
capability gap, tool failure, behavioral misalignment),
severity, and affected component.
- **Store processed feedback for trend
analysis:** Use
[Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html) indexed by agent, feedback type, and time
period.
- **Route by severity:** Send
high-severity feedback to immediate review queues through
[Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html). Aggregate lower-severity items for batch
review.
- **Track improvements end to
end:** Build a workflow that moves each item from
identification through root-cause analysis, implementation,
and validation, with metrics compared before and after.
- **Build visibility into trends and
outcomes:** Create dashboards that show feedback
trends, improvement outcomes, and quality trajectory over
time.

## Resources

**Related best practices:**

- [AGENTOPS02-BP01 Evolve
agent prompts, tool calls, and configurations to reflect
evolving business needs](agentops02-bp01.html)
- [AGENTOPS05-BP02
Monitor agent behavior patterns and detect anomalies](agentops05-bp02.html)
- [AGENTPERF01-BP01
Define performance-aligned success criteria for agent
workloads](agentperf01-bp01.html)

**Related documents:**

- [Operationalizing
agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-operationalizing-agentic-ai/introduction.html)
- [Evaluating
AI agents: Real-world lessons from building agentic systems at
Amazon](https://aws.amazon.com/blogs/machine-learning/evaluating-ai-agents-real-world-lessons-from-building-agentic-systems-at-amazon/)
- [Guidance
for Agentic AI Operational Foundations on AWS](https://aws.amazon.com/solutions/guidance/agentic-ai-operational-foundations-on-aws/)

**Related videos:**

- [AWS re:Invent 2024 - Elevate application and generative AI
observability (COP326)](https://www.youtube.com/watch?v=vxzq8GthOLs)
- [AWS re:Invent 2024 - Responsible generative AI: Evaluation best
practices and tools (AIM342)](https://www.youtube.com/watch?v=wuVpCc5a81Y)

**Related examples:**

- [GitHub:
Open Source Bedrock Agent Evaluation](https://github.com/aws-samples/open-source-bedrock-agent-evaluation)
- [GitHub:
Sample Bedrock Evaluation Adapter](https://github.com/aws-samples/sample-bedrock-evaluation-adapter)

**Related services:**

- [Amazon
Bedrock](https://aws.amazon.com/bedrock/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon EventBridge](https://aws.amazon.com/eventbridge/)
- [Amazon DynamoDB](https://aws.amazon.com/dynamodb/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentops02-bp04.html*

---
