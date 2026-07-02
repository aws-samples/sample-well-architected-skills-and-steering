# AGENTSEC06 — Secure multi-agent orchestration

**Pillar**: Security  
**Best Practices**: 4

---

# AGENTSEC06-BP01 Encrypt and sign inter-agent messages

Transport-level encryption stops protecting the payload the moment a
message lands in a queue or event bus. Message-level signing and
encryption keyed per trust zone gives receiving agents cryptographic
proof of sender identity and content integrity no matter how many
hops the message made.

**Desired outcome:**

- You protect inter-agent messages at the message level with
encryption and signing, independent of transport-level security.
- Receiving agents verify message signatures before acting on
instructions from other agents.
- Messages stored in queues or event buses are encrypted at rest
with keys scoped to the appropriate trust zone.
- Agents can't forge messages that appear to originate from other
agents in the coordination workflow.

**Common anti-patterns:**

- Relying solely on transport-level encryption (TLS) without
message-level signing, so messages stored in queues or event
buses can't be verified for tampering at consumption time.
- Using a single shared encryption key across all agents, so one
key exposure affects every inter-agent message rather than only
those in one trust zone.
- Not verifying message signatures before acting on inter-agent
instructions, letting an agent act on forged or tampered
instructions without any integrity check.

**Benefits of establishing this best
practice:**

- Message-level integrity verification persists beyond the
transport layer, so messages stored in queues or event buses can
be verified at consumption time.
- Scoped key management limits the impact of a key exposure to a
single trust zone rather than the entire multi-agent system.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Two distinct properties are at stake: who sent the message
(covered by AGENTSEC03-BP01 for authentication) and whether the
content is what the sender actually sent. Transport-level
encryption provides the second property only while the message is
in transit. The moment the message lands in an Amazon SQS queue,
Amazon EventBridge bus, or AWS Step Functions state machine, there
is no transport to protect it, and any modification between
delivery and consumption is invisible. Message-level signing
provides cryptographic proof that a specific message was sent by a
specific agent and has not been modified, regardless of how many
intermediary services it passed through.

Scope matters. For direct agent-to-agent communication within a
single trust zone, the transport-level security and authentication
provided by
[Amazon
Bedrock AgentCore Runtime](https://aws.amazon.com/blogs/machine-learning/introducing-agent-to-agent-protocol-support-in-amazon-bedrock-agentcore-runtime/) (TLS 1.2+ with OAuth 2.0 or
SigV4) is typically sufficient. Layer message signing on top when
payload integrity needs to persist beyond the transport, or when a
receiving agent needs cryptographic proof of which specific agent
sent an instruction.

AWS KMS asymmetric keys are the mechanism. The sending agent signs
the message payload through the KMS Sign API, and the receiving
agent verifies the signature through the KMS Verify API before
acting on the message. This gives end-to-end integrity
verification that is independent of the transport layer: even if a
message passes through multiple intermediary services (load
balancers, queues, event buses), the signature proves it was
created by the claimed sender and has not been modified. Separate
keys per trust zone limit the scope affected by a single key
exposure.

For asynchronous agent messaging through Amazon SQS, enable
server-side encryption using AWS KMS customer-managed keys.
Configure separate keys for different agent trust zones so a key
exposure in one zone doesn't affect messages in other zones, and
use SQS message attributes to carry the message signature
alongside the encrypted payload so receiving agents verify both
authenticity and integrity at consumption time.

AgentCore Runtime provides session isolation and built-in
authentication for agents using the Agent-to-Agent (A2A) protocol.
A2A handles authentication for inter-agent interactions, but for
messages that cross trust boundaries, carry sensitive data, or
pass through intermediary services, message-level signing layers
on top of the protocol's built-in protections.

AWS PrivateLink routes inter-agent communications through private
network endpoints, keeping traffic off the public internet. That
complements message-level encryption by reducing the network
exposure of inter-agent traffic. Store signing key ARNs in
Parameter Store, a capability of AWS Systems Manager, configure
automatic key rotation in AWS KMS with a rotation period matching
your security requirements, and configure Amazon CloudWatch alarms
for key usage anomalies (unexpected signing operations from agents
that should only be verifying, signing volume spikes suggesting a
runaway loop).

### Implementation steps

- **Create trust-zone-scoped KMS key
pairs:** Provision AWS KMS asymmetric key pairs for
message signing, with separate keys for each agent trust
zone.
- **Sign messages on send:**
Implement message signing in sending agents through the AWS KMS Sign API, attaching the signature as a message metadata
attribute.
- **Verify signatures on
receive:** Implement signature verification in
receiving agents through the AWS KMS Verify API, rejecting
any message that fails verification before processing.
- **Encrypt SQS queues with
customer-managed keys:** Enable server-side
encryption on Amazon SQS queues used for asynchronous
inter-agent messaging, using customer-managed AWS KMS keys
scoped per trust zone.
- **Layer signing on top of A2A for
cross-boundary traffic:** For agents on AgentCore
Runtime using A2A, add message-level signing for
communications that cross trust boundaries on top of the
protocol's built-in authentication.
- **Route through
PrivateLink:** Configure AWS PrivateLink for
inter-agent service communications to keep traffic on
private network endpoints.
- **Manage keys and alert on
anomalies:** Store signing key ARNs in Parameter
Store, a capability of AWS Systems Manager, configure
automatic key rotation in AWS KMS, and set Amazon CloudWatch
alarms for key usage anomalies.

## Resources

**Related best practices:**

- [AGENTSEC03-BP01
Implement strong authentication for agent identities](agentsec03-bp01.html)
- [AGENTSEC06-BP02
Implement workflow orchestration security controls](agentsec06-bp02.html)
- [AGENTSEC06-BP03
Establish trust boundaries between agents](agentsec06-bp03.html)

**Related documents:**

- [Introducing
agent-to-agent protocol support in Amazon Bedrock AgentCore
Runtime](https://aws.amazon.com/blogs/machine-learning/introducing-agent-to-agent-protocol-support-in-amazon-bedrock-agentcore-runtime/)
- [Digital
signing with the new asymmetric keys feature of AWS KMS](https://aws.amazon.com/blogs/security/digital-signing-asymmetric-keys-aws-kms/)
- [Code
signing using ACM Private CA and AWS KMS asymmetric
keys](https://aws.amazon.com/blogs/security/code-signing-aws-certificate-manager-private-ca-aws-key-management-service-asymmetric-keys/)
- [AWS KMS documentation](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html)
- [Amazon SQS security best practices](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-security-best-practices.html)

**Related services:**

- [AWS Key Management Service](https://aws.amazon.com/kms/)
- [Amazon SQS](https://aws.amazon.com/sqs/)
- [AWS Systems Manager](https://aws.amazon.com/systems-manager/)
- [AWS PrivateLink](https://aws.amazon.com/privatelink/)
- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsec06-bp01.html*

---

# AGENTSEC06-BP02 Implement workflow orchestration security controls

The orchestration layer is where a single weak check cascades into a
system-wide failure. Access controls on state machines, input
validation on transitions, and circuit breakers on agent tasks keep
multi-agent workflows on approved execution paths instead of
unexpected ones.

**Desired outcome:**

- The workflow orchestration layer enforces strict access controls
that help prevent unauthorized modification of workflow
definitions or execution state.
- State machine validation helps keep workflows on expected
execution patterns, and circuit breakers are designed to stop
failures in one agent from cascading through the entire
workflow.
- You log all workflow executions with enough detail to
reconstruct the execution path for security investigations.

**Common anti-patterns:**

- Granting broad IAM permissions to start, stop, or modify Step
Functions workflows without restricting access to specific state
machines, letting any principal with workflow permissions modify
or trigger any workflow in the account.
- Not implementing input validation in state machine definitions,
letting crafted input payloads direct workflows into unexpected
execution paths.
- Failing to implement circuit breakers, so a single failing agent
cascades failures through the entire workflow with no automatic
mechanism to stop retrying a broken step.
- Using overly permissive retry configurations, letting an agent
repeatedly attempt the same operation before any circuit breaker
triggers and potentially amplifying the original issue.

**Benefits of establishing this best
practice:**

- State validation and input schema enforcement keep workflows
within defined boundaries.
- Circuit breakers automatically stop cascading failures and route
affected executions to quarantine paths for investigation.
- AWS Step Functions logging captures every state transition,
input, output, and error event for full execution
reconstructability.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Two orchestration patterns are in scope here. AWS Step Functions
state machines handle deterministic workflows where the execution
path is defined in JSON and the orchestrator enforces sequencing.
[Amazon
Bedrock AgentCore Runtime](https://aws.amazon.com/blogs/machine-learning/introducing-agent-to-agent-protocol-support-in-amazon-bedrock-agentcore-runtime/) with the A2A protocol handles
agent-delegated workflows where an orchestrator agent dynamically
decides which sub-agents to invoke. Most of the controls below
apply to both, and the differences are called out inline.

Start with IAM. Configure policies for AWS Step Functions that
restrict workflow start, stop, and modification permissions to
specific principals and state machines, use resource-based
policies on state machine definitions to help prevent unauthorized
modification, and implement IAM Conditions that restrict execution
to approved input schemas. Manage state machine definitions as
infrastructure as code through AWS CloudFormation or AWS CDK,
which helps prevent informal modifications and provides
version-controlled change history.

Input validation belongs inside the state machine definition, not
outside it. With Step Functions' built-in JSONPath filtering and
AWS Lambda validation functions, you can validate that workflow
inputs conform to expected schemas before passing them to agent
tasks, rejecting inputs that deviate from expected patterns. Step
Functions' error handling catches and logs validation failures
without exposing error details to callers.

Circuit breakers use Step Functions' error handling and retry
logic. Set conservative retry limits with exponential backoff for
agent task failures, and implement catch states that route failed
executions to a quarantine path rather than retrying indefinitely.
Amazon EventBridge emits circuit breaker events when failure
thresholds are exceeded, triggering alerts and automated
remediation. For multi-agent workflows using the A2A protocol on
AgentCore Runtime, the structured request lifecycle (agent card
discovery, task delegation, result collection) provides natural
points to validate inputs, check authorization, and apply circuit
breaker logic before proceeding.

Execution logging makes the orchestration auditable. Enable Step
Functions execution logging to Amazon CloudWatch Logs at the ALL
level to capture all state transitions, input/output data, and
error events. Configure log retention policies aligned with
compliance requirements and create Amazon CloudWatch Logs Insights
queries for common investigation scenarios such as identifying
workflows that took unexpected execution paths or triggered
circuit breakers.

### Implementation steps

- **Scope Step Functions IAM to specific
state machines:** Configure IAM policies with
least-privilege access scoped to specific state machines and
execution operations.
- **Manage state machines as
IaC:** Use AWS CloudFormation or AWS CDK for state
machine definitions to help prevent unauthorized
modifications and keep version history.
- **Validate inputs inside state
machines:** Implement input validation in state
machine definitions using JSONPath filtering and AWS Lambda
validation functions, rejecting inputs that deviate from
expected schemas.
- **Configure circuit breakers with
catch states:** Set conservative retry limits and
implement catch states that route failures to quarantine
paths rather than retrying indefinitely.
- **Log every execution at the ALL
level:** Enable Step Functions execution logging to
Amazon CloudWatch Logs at the ALL level with retention
policies aligned to compliance requirements.
- **Alarm on circuit breaker
events:** Create Amazon CloudWatch alarms for
circuit breaker triggers and Amazon EventBridge rules to
route workflow security events to the monitoring pipeline.

## Resources

**Related best practices:**

- [AGENTSEC04-BP02
Human-in-the-loop for critical decisions](agentsec04-bp02.html)
- [AGENTSEC06-BP01 Encrypt
and sign inter-agent messages](agentsec06-bp01.html)
- [AGENTSEC06-BP03
Establish trust boundaries between agents](agentsec06-bp03.html)
- [AGENTREL07-BP01
Design workflows in stages with incremental recovery](agentrel07-bp01.html)
- [AGENTREL07-BP02
Enable automatic recovery from agent execution failures](agentrel07-bp02.html)

**Related documents:**

- [AWS Step Functions security documentation](https://docs.aws.amazon.com/step-functions/latest/dg/security.html)
- [Step
Functions error handling](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-error-handling.html)
- [Using
the circuit breaker pattern with Step Functions and
DynamoDB](https://aws.amazon.com/blogs/compute/using-the-circuit-breaker-pattern-with-aws-step-functions-and-amazon-dynamodb/)
- [AWS Prescriptive Guidance: Circuit breaker pattern](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/circuit-breaker.html)
- [Introducing
agent-to-agent protocol support in Amazon Bedrock AgentCore
Runtime](https://aws.amazon.com/blogs/machine-learning/introducing-agent-to-agent-protocol-support-in-amazon-bedrock-agentcore-runtime/)

**Related services:**

- [AWS Step Functions](https://aws.amazon.com/step-functions/)
- [AWS Identity and Access Management](https://aws.amazon.com/iam/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
- [Amazon EventBridge](https://aws.amazon.com/eventbridge/)
- [AWS CloudFormation](https://aws.amazon.com/cloudformation/)
- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsec06-bp02.html*

---

# AGENTSEC06-BP03 Establish trust boundaries between agents

A flat agent network gives every affected agent a direct path to
every other one. Trust zones segmented at the network and IAM
layers, with application-layer verification of caller identity, stop
one affected agent from escalating across the whole system.

**Desired outcome:**

- Agents operate within clearly defined trust zones, accepting
instructions only from authorized coordinators and rejecting
requests from agents outside their trust boundary.
- Network segmentation enforces trust boundaries at the
infrastructure layer and IAM policies enforce them at the API
layer.
- An affected agent in one trust zone can't directly issue
instructions to agents in higher-trust zones without passing
through authorization controls.

**Common anti-patterns:**

- Deploying all agents in a flat network without segmentation,
letting any agent communicate directly with any other regardless
of trust level so an issue spreads laterally.
- Relying on network-level trust boundaries alone without
application-layer authorization, so any agent that reaches
another agent's endpoint can issue instructions.
- Not validating the identity of the coordinator agent before
executing instructions, letting any agent impersonate a
coordinator and issue unauthorized commands.
- Treating all internal agents as implicitly trusted while
implementing trust boundaries only for external-facing agents,
producing a flat internal trust model that amplifies the impact
of any internal issue.

**Benefits of establishing this best
practice:**

- Trust zone segmentation contains the impact of an affected agent
to its own trust zone, helping prevent lateral movement.
- Layered enforcement at both the network level (VPC segmentation,
security groups) and the application level (IAM policies, agent
identity validation) provides defense-in-depth.
- Documented trust architecture supports automated compliance
checks that catch drift as configurations evolve.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Trust boundary controls apply regardless of the inter-agent
protocol used, whether A2A, MCP, or custom REST. The network-layer
controls (VPC segmentation, security groups, AWS PrivateLink) and
IAM-layer controls (resource-based policies, IAM Conditions)
enforce boundaries independent of the application protocol.
Protocol-specific guidance applies on top of these common
controls.

A trust zone architecture starts with tiers that reflect actual
risk: public, internal operational, privileged. Enforce the tiers
at the network with separate Amazon VPCs or VPC security groups,
and use Amazon VPC peering or AWS Transit Gateway with route table
controls to restrict inter-zone communication to only the required
paths. Network segmentation alone doesn't verify the caller's
identity, so pair it with application-layer authorization.

[Amazon
Bedrock AgentCore Runtime](https://aws.amazon.com/blogs/machine-learning/introducing-agent-to-agent-protocol-support-in-amazon-bedrock-agentcore-runtime/) A2A protocol support provides a
structured framework for inter-agent communication with built-in
session isolation and authentication. When agents discover peers
through A2A agent cards, the card schema advertises the agent's
capabilities and authentication requirements. Configure agents to
accept A2A connections only from coordinators whose agent cards
match the expected identity and trust level. For agents not using
A2A, Amazon API Gateway with AWS Lambda authorizers implements
custom agent-to-agent authorization logic that validates agent
identity tokens and enforces trust level requirements.

Resource-based policies on agent endpoints explicitly list the IAM
principals authorized to invoke each agent. IAM Conditions
restrict invocations to agents within the same trust zone or to
specific coordinator agent roles. AWS PrivateLink keeps cross-zone
agent communications on private network paths.
[Policy
in Amazon Bedrock AgentCore](https://aws.amazon.com/blogs/machine-learning/secure-ai-agents-with-policy-in-amazon-bedrock-agentcore/) reinforces trust boundaries at
the tool layer: Cedar policies can include conditions on the
calling principal's identity and trust level, so even if an agent
can reach another agent's tools through the gateway, the policy
engine blocks tool calls that violate trust zone rules.

Compliance validation detects drift from the intended network
posture. AWS Config managed rules,
vpc-sg-open-only-to-authorized-ports for
unintended public ingress, restricted-ssh for
SSH access from 0.0.0.0/0,
vpc-sg-port-restriction-check for port-level
restrictions, cover baseline network hygiene. Trust-zone-specific
validation (that security group rules reference only CIDR ranges
or security group IDs from the same trust zone) needs custom AWS Config rules backed by AWS Lambda, and alarms fire on any
configuration change that would create unauthorized cross-zone
connectivity.

### Implementation steps

- **Design trust zone tiers:**
Define tiers (public, internal operational, privileged) and
document the authorized communication paths between zones.
- **Segment at the network
layer:** Create separate Amazon VPCs or security
groups for each trust zone and configure network controls
(VPC peering, AWS Transit Gateway route tables) to enforce
zone boundaries.
- **Enforce identity at the application
layer:** For agents on
[Amazon
Bedrock AgentCore Runtime](https://aws.amazon.com/blogs/machine-learning/introducing-agent-to-agent-protocol-support-in-amazon-bedrock-agentcore-runtime/), configure A2A agent card
discovery with authentication requirements that enforce
trust-level validation. For agents not on AgentCore Runtime,
use Amazon API Gateway with AWS Lambda authorizers for
custom trust boundary enforcement.
- **Apply resource-based IAM
policies:** List only authorized coordinator
principals in each agent endpoint's resource policy, with
IAM Conditions restricting invocations by trust zone.
- **Reinforce at the tool layer with
Policy:** Configure Cedar policies in
[Policy
in Amazon Bedrock AgentCore](https://aws.amazon.com/blogs/machine-learning/secure-ai-agents-with-policy-in-amazon-bedrock-agentcore/) with conditions on
calling principal identity and trust level.
- **Keep cross-zone traffic
private:** Implement AWS PrivateLink for cross-zone
agent communications.
- **Validate configurations
continually:** Deploy AWS Config managed rules
(vpc-sg-open-only-to-authorized-ports,
restricted-ssh,
vpc-sg-port-restriction-check) for
baseline hygiene and custom AWS Config rules for
trust-zone-specific validation, alarming on any change that
would create unauthorized cross-zone connectivity.

## Resources

**Related best practices:**

- [AGENTSEC03-BP03
Implement least privilege with dynamic boundaries](agentsec03-bp03.html)
- [AGENTSEC06-BP01 Encrypt
and sign inter-agent messages](agentsec06-bp01.html)
- [AGENTSEC06-BP02
Implement workflow orchestration security controls](agentsec06-bp02.html)

**Related documents:**

- [Introducing
agent-to-agent protocol support in Amazon Bedrock AgentCore
Runtime](https://aws.amazon.com/blogs/machine-learning/introducing-agent-to-agent-protocol-support-in-amazon-bedrock-agentcore-runtime/)
- [Secure
AI agents with Policy in Amazon Bedrock AgentCore](https://aws.amazon.com/blogs/machine-learning/secure-ai-agents-with-policy-in-amazon-bedrock-agentcore/)
- [AWS VPC security best practices](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-best-practices.html)
- [AWS Config managed rules reference](https://docs.aws.amazon.com/config/latest/developerguide/managed-rules-by-aws-config.html)
- [AWS Config custom rules with Lambda](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_develop-rules_lambda-functions.html)
- [Security
reference architecture for generative AI](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-generative-ai/gen-ai-sra.html)

**Related services:**

- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [AWS Identity and Access Management](https://aws.amazon.com/iam/)
- [Amazon VPC](https://aws.amazon.com/vpc/)
- [Amazon API Gateway](https://aws.amazon.com/api-gateway/)
- [AWS PrivateLink](https://aws.amazon.com/privatelink/)
- [AWS Config](https://aws.amazon.com/config/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsec06-bp03.html*

---

# AGENTSEC06-BP04 Monitor and detect coordination anomalies

Distributed tracing tells you what happened on one request.
Coordination monitoring tells you when many requests start behaving
differently from the baseline. Tracking inter-agent message rates,
workflow frequencies, and topology changes against established
baselines catches issues through their observable impact on
coordination before they escalate into security events.

**Desired outcome:**

- You detect anomalous coordination patterns such as unexpected
agent communication paths, unusual interaction frequencies, or
coordination latency spikes in near real time and trigger alerts
for investigation.
- You establish baseline coordination profiles for each agent
workflow, so statistical anomaly detection catches deviations
before they cause significant impact.

**Common anti-patterns:**

- Monitoring only infrastructure metrics (CPU, memory, and
network) without tracking agent-specific coordination metrics,
missing the coordination-level signals most indicative of
multi-agent issues.
- Not establishing coordination baselines before deploying anomaly
detection, which produces either excessive false positives or
missed detections.
- Treating Amazon GuardDuty findings and agent coordination logs
as separate data streams, leaving investigators without the
multi-agent context that turns API-level anomalies into useful
signal.

**Benefits of establishing this best
practice:**

- Behavioral baselines catch coordination deviations before they
propagate across the multi-agent system.
- Service maps compare observed communication paths against the
expected trust boundary architecture, validating topology
continually.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Distributed tracing (AGENTSEC05-BP02) reconstructs what happened
during a specific request. Coordination anomaly detection is a
different problem. It is a proactive early-warning system that
watches whether coordination patterns across many requests over
time are drifting from the baseline. Tracing is reactive and
investigation-focused. Coordination monitoring is preventive and
baseline-focused.

Start by defining coordination metrics for each multi-agent
workflow:

- Inter-agent message rates
- Workflow execution frequencies
- Agent response latencies
- Error rates per agent pair
- Coordination graph topology changes

Publish these as Amazon CloudWatch custom metrics, establish
baselines by collecting them during normal operation, and
configure Amazon CloudWatch anomaly detection to automatically
identify statistical deviations.

[Amazon
Bedrock AgentCore Observability](https://aws.amazon.com/blogs/machine-learning/build-trustworthy-ai-agents-with-amazon-bedrock-agentcore-observability/) provides the foundation.
The session, trace, and span hierarchy captures inter-agent
interactions, and the default metrics on the Amazon CloudWatch
generative AI observability page surface session-level patterns.
For agents using the A2A protocol on AgentCore Runtime, the
structured request lifecycle (agent card discovery, task
delegation, result collection) generates observable events at each
coordination step, which you can use to build coordination
topology maps and detect when agents communicate outside their
expected patterns.

[Amazon
Bedrock AgentCore Evaluations](https://aws.amazon.com/blogs/aws/amazon-bedrock-agentcore-adds-quality-evaluations-and-policy-controls-for-deploying-trusted-ai-agents/) complements coordination
monitoring by continually scoring agent behavior on tool selection
accuracy, correctness, and other quality dimensions. If a
coordinating agent starts selecting unexpected tools or producing
incorrect outputs, evaluation-score drops can serve as an early
warning signal before the coordination anomaly becomes visible at
the workflow level. Amazon CloudWatch alarms on evaluation scores
layered with coordination metrics give you a two-stage detection
approach.

Amazon GuardDuty monitors API call patterns for all agent IAM
roles. Its machine learning models detect unusual call patterns:
an agent suddenly calling services it has never accessed before,
or calling APIs at unusual times or from unexpected locations.
Integrate GuardDuty findings with AWS Security Hub CSPM for centralized
prioritization, and correlate them with agent coordination logs to
connect API-level anomalies to specific multi-agent workflows.
Amazon CloudWatch Logs Insights queries add another layer,
analyzing agent coordination logs for patterns such as agents
receiving instructions from unexpected sources, coordination loops
that may indicate runaway behavior, and agents attempting to
access resources outside their defined scope. Schedule these
queries to run periodically and publish results to a security
dashboard.

### Implementation steps

- **Define and publish coordination
metrics:** Capture inter-agent message rates,
execution frequencies, response latencies, and error rates
per agent pair through Amazon CloudWatch custom metrics for
each multi-agent workflow.
- **Establish baselines and enable
anomaly detection:** Collect metrics during normal
operation and configure Amazon CloudWatch anomaly detection
on key metrics.
- **Build topology maps:** Use
[Amazon
Bedrock AgentCore Observability](https://aws.amazon.com/blogs/machine-learning/build-trustworthy-ai-agents-with-amazon-bedrock-agentcore-observability/) service maps and A2A
request lifecycle events to build coordination topology
maps, and alert on unexpected topology changes that deviate
from the documented trust boundary architecture.
- **Layer evaluations as early
warning:** Deploy
[Amazon
Bedrock AgentCore Evaluations](https://aws.amazon.com/blogs/aws/amazon-bedrock-agentcore-adds-quality-evaluations-and-policy-controls-for-deploying-trusted-ai-agents/) to continually score
agent behavior, and configure Amazon CloudWatch alarms on
evaluation scores as an early-warning layer for coordination
issues.
- **Correlate GuardDuty with
coordination logs:** Enable Amazon GuardDuty for
all agent accounts, integrate findings with AWS Security Hub CSPM, and create correlation rules that connect API anomalies
to specific agent coordination logs.
- **Run Logs Insights queries on a
schedule:** Build Amazon CloudWatch Logs Insights
queries for coordination security event patterns and publish
results to a security dashboard on a scheduled cadence.
- **Document the response
runbook:** Establish an incident response runbook
for coordination anomaly alerts that defines investigation
steps, escalation paths, and remediation actions.

## Resources

**Related best practices:**

- [AGENTSEC06-BP01 Encrypt
and sign inter-agent messages](agentsec06-bp01.html)
- [AGENTSEC06-BP03
Establish trust boundaries between agents](agentsec06-bp03.html)
- [AGENTSEC07-BP04
Behavioral anomaly detection and agent containment](agentsec07-bp04.html)
- [AGENTREL02-BP03
Implement behavioral anomaly detection and monitoring](agentrel02-bp03.html)

**Related documents:**

- [Build
trustworthy AI agents with Amazon Bedrock AgentCore
Observability](https://aws.amazon.com/blogs/machine-learning/build-trustworthy-ai-agents-with-amazon-bedrock-agentcore-observability/)
- [Amazon
Bedrock AgentCore adds quality evaluations and policy
controls](https://aws.amazon.com/blogs/aws/amazon-bedrock-agentcore-adds-quality-evaluations-and-policy-controls-for-deploying-trusted-ai-agents/)
- [Amazon GuardDuty documentation](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html)
- [Amazon CloudWatch anomaly detection](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.html)

**Related services:**

- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
- [Amazon GuardDuty](https://aws.amazon.com/guardduty/)
- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [AWS Security Hub CSPM](https://aws.amazon.com/security-hub/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsec06-bp04.html*

---
