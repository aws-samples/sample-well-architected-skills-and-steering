# AGENTPERF04 — Communication and protocol efficiency

**Pillar**: Performance Efficiency  
**Best Practices**: 3

---

# AGENTPERF04-BP01 Optimize asynchronous message handling patterns

Asynchronous messaging lets agents operate independently at their
optimal pace, with message queues absorbing throughput variations
and leveling load across the workflow. Synchronous request-response
patterns create tight coupling that makes a slow downstream agent
block the entire upstream chain. Async decouples producers from
consumers so fast agents are not held up by slow ones.

**Desired outcome:**

- You have agent-to-agent and agent-to-service communications
using asynchronous patterns by default, with synchronous
communication reserved for interactions that genuinely require
immediate responses.
- You have compact message payloads that pass references rather
than inline data.
- You have agents processing messages at their own pace without
being overwhelmed by upstream producers.

**Common anti-patterns:**

- Using synchronous HTTP request-response for all agent
communications, creating tight coupling where a slow downstream
agent blocks the entire upstream chain.
- Including large payloads (like full documents or base64-encoded
files) in messages rather than passing references (like S3 URIs
or document IDs) and letting the consumer retrieve the data when
needed.
- Skipping backpressure mechanisms, allowing fast-producing agents
to overwhelm slow-consuming agents with messages that queue up
and eventually cause timeouts.

**Benefits of establishing this best
practice:**

- Decoupled agent execution helps prevent slow agents from
blocking fast agents.
- Each agent scales independently based on its own queue depth and
processing rate.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

For agents deployed on
[Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html), the runtime's built-in session
management handles message passing and state management for
agent-to-agent communication inside a workflow. For workflows that
need custom messaging patterns or cross-system integration,
[Amazon SQS](https://aws.amazon.com/sqs/)
provides reliable point-to-point messaging and
[Amazon SNS](https://aws.amazon.com/sns/)
provides fan-out where a single agent event triggers multiple
downstream agents. Message payloads should stay compact: pass S3
URIs, DynamoDB keys, or document IDs rather than inline data, and
let the consumer retrieve the bytes on demand.

Dead letter queues (DLQs) capture messages that fail processing
after retries, so failure analysis doesn't block the main flow.
When consumer queues exceed depth thresholds, producers should be
throttled or consumers scaled. Amazon CloudWatch alarms on queue
depth are the signal that triggers either response. For
high-volume workflows, SQS batch size and long polling let you
balance latency and throughput, long polling reduces empty
receives, and larger batch sizes amortize request overhead across
more messages.

### Implementation steps

- **Use AgentCore Runtime session
management for agent-to-agent communication where possible,
and use SQS or SNS for custom messaging patterns:**
Let the runtime handle message passing and state inside a
workflow, and fall back to Amazon SQS or Amazon SNS only for
custom patterns or cross-system integration.
- **Design compact message payloads
using references rather than inline data:** Pass S3
URIs, DynamoDB keys, or document IDs in messages and let the
consumer retrieve the full payload on demand.
- **Implement dead letter queues for
failed message processing with alerting on DLQ
depth:** Route messages that fail after retries to
a DLQ and alert when DLQ depth grows, so failure analysis
happens off the main path.
- **Add backpressure mechanisms that
throttle producers when consumer queues exceed depth
thresholds:** Use Amazon CloudWatch alarms on queue
depth to trigger producer throttling or consumer scaling
before queues reach timeout-triggering depths.
- **Configure long polling and batch
sizes for SQS consumers based on latency and throughput
requirements:** Tune long polling and batch size on
SQS consumers to balance empty-receive cost, per-message
latency, and throughput.

## Resources

**Related best practices:**

- [AGENTPERF04-BP02
Implement efficient protocol-based agent communications](agentperf04-bp02.html)
- [AGENTPERF04-BP03 Design
performant event-driven integration patterns](agentperf04-bp03.html)
- [AGENTPERF05-BP01
Design efficient workflow orchestration patterns](agentperf05-bp01.html)

**Related documents:**

- [Building
serverless architectures for agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-serverless/introduction.html)
- [Foundations
of agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-foundations/introduction.html)

**Related services:**

- [Amazon
Bedrock AgentCore Runtime](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon SQS](https://aws.amazon.com/sqs/)
- [Amazon SNS](https://aws.amazon.com/sns/)
- [AWS Lambda](https://aws.amazon.com/lambda/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentperf04-bp01.html*

---

# AGENTPERF04-BP02 Implement efficient protocol-based agent communications

Standardized protocols such as the Model Context Protocol (MCP) and
agent-to-agent (A2A) give agents a consistent way to communicate
with tools and each other, reducing per-interaction overhead and
enabling interoperability. Different protocols have different
performance profiles, connection establishment, serialization,
streaming, multiplexing, which makes protocol selection a meaningful
performance decision for high-frequency agent communication.

**Desired outcome:**

- You use MCP for tool integration, A2A for agent-to-agent
coordination, and streaming protocols for real-time agent-user
interactions.
- You have protocol overhead minimized through connection reuse
and efficient serialization.
- You have documented protocol selection guidelines for the
organization.

**Common anti-patterns:**

- Using HTTP or REST APIs with JSON serialization for all agent
communications regardless of interaction pattern, paying
connection establishment and verbose serialization overhead for
high-frequency internal communications.
- Implementing custom communication protocols instead of adopting
standards like MCP and A2A, creating maintenance burden and
blocking interoperability with the broader agent ecosystem.
- Establishing new connections for every agent interaction rather
than pooling and reusing them, adding unnecessary handshake
latency.

**Benefits of establishing this best
practice:**

- Protocol-appropriate connection management reduces
per-interaction overhead.
- Standard protocols open interoperability with the broader agent
ecosystem.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Adopt MCP as the standard protocol for agent-to-tool
communication.
[Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) exposes tools as MCP-compatible
endpoints that agents discover and invoke through a consistent
interface. For agent-to-agent communication, the A2A protocol
supported by AgentCore Runtime provides structured inter-agent
coordination with agent card discovery, task delegation, and
result collection. Frameworks such as Strands Agents and LangGraph
provide MCP and A2A support.

For real-time agent-user interactions that need streaming,
WebSocket connections through
[Amazon API Gateway](https://aws.amazon.com/api-gateway/) keep a persistent channel open rather than
reestablishing connections per turn. Connection pooling belongs on
every protocol path, and protocol-level compression pays off once
payloads exceed a few kilobytes.

Authentication overhead is part of the protocol performance
profile. In complex multi-agent workflows, token validation,
credential issuance, and policy evaluation accumulate into a
measurable latency contributor. AgentCore Identity provides agent
authentication with token caching, and AWS IAM roles for
service-to-service authentication remove explicit credential
exchange from the critical path.

### Implementation steps

- **Adopt MCP for agent-to-tool
communications through AgentCore Gateway:** Expose
tools as MCP-compatible endpoints through
[Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) so agents discover and
invoke tools through a consistent interface.
- **Use A2A protocol through AgentCore
Runtime for agent-to-agent coordination:** Use the
A2A protocol supported by AgentCore Runtime for
agent-to-agent coordination, with agent card discovery, task
delegation, and result collection.
- **Implement WebSocket connections
through API Gateway for real-time streaming agent-user
interactions:** Use WebSocket connections through
[Amazon API Gateway](https://aws.amazon.com/api-gateway/) for real-time streaming so the channel
stays open rather than reestablishing on each turn.
- **Enable connection pooling and
protocol-level compression for all
communications:** Pool connections on every
protocol path and enable compression once payloads exceed a
few kilobytes.
- **Budget for authentication overhead
and implement token caching through AgentCore
Identity:** Use AgentCore Identity with token
caching for agent authentication, and use AWS IAM roles for
service-to-service calls so credential exchange isn't on the
critical path.

## Resources

**Related best practices:**

- [AGENTPERF04-BP01
Optimize asynchronous message handling patterns](agentperf04-bp01.html)
- [AGENTPERF06-BP01
Design optimized tool integration strategies](agentperf06-bp01.html)
- [AGENTPERF05-BP02
Implement optimized multi-agent collaboration models](agentperf05-bp02.html)

**Related documents:**

- [Agentic
AI frameworks, protocols, and tools on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-frameworks/introduction.html)
- [Blog:
Open Protocols for Agent Interoperability Part 1: Inter-Agent
Communication on MCP](https://aws.amazon.com/blogs/opensource/open-protocols-for-agent-interoperability-part-1-inter-agent-communication-on-mcp)
- [Blog:
Open Protocols for Agent Interoperability Part 4: Inter-Agent
Communication on A2A](https://aws.amazon.com/blogs/opensource/open-protocols-for-agent-interoperability-part-4-inter-agent-communication-on-a2a/)
- [Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html)

**Related videos:**

- [AgentCore
Deep Dive: Gateway](https://www.youtube.com/watch?v=atWXM5lziY8)
- [Building
Scalable, Self-Orchestrating AI Workflows with A2A and MCP
(DEV415)](https://www.youtube.com/watch?v=9O9zZ1lQWiI)

**Related examples:**

- [GitHub:
Amazon Bedrock AgentCore samples, Gateway tutorials](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/02-AgentCore-gateway)

**Related tools:**

- [Strands
Agents](https://strandsagents.com/)
- [LangGraph](https://langchain-ai.github.io/langgraph/)

**Related services:**

- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon API Gateway](https://aws.amazon.com/api-gateway/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentperf04-bp02.html*

---

# AGENTPERF04-BP03 Design high-performing event-driven integration patterns

Agents that react to events in real time, data changes, user
actions, and system alerts deliver faster business outcomes than
agents that poll for work. Overly broad event subscriptions trigger
agents for irrelevant events, missing filtering causes agents to
process and discard events they don't need. Inefficient routing adds
delays that push response time past user expectations.

**Desired outcome:**

- You have agent workflows triggered by precisely filtered events
that match their processing requirements, with minimal latency
between event emission and agent invocation.
- You have efficient event schemas that include only routing
metadata, with agents retrieving full context on demand.
- You have event-driven patterns that support both real-time and
batch processing modes.

**Common anti-patterns:**

- Subscribing agents to broad event streams without filtering,
forcing agents to receive and process events they immediately
discard and wasting compute resources.
- Using polling-based event detection instead of push-based event
delivery, adding latency and consuming compute during idle
periods.
- Including full data payloads in events rather than event
references, inflating event size and network transfer time when
most consumers only need a subset.

**Benefits of establishing this best
practice:**

- Push-based delivery reduces latency between event occurrence and
agent invocation.
- Filtering at the event bus reduces compute waste by invoking
agents only for relevant events.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Use [Amazon EventBridge](https://aws.amazon.com/eventbridge/) as the primary event bus for agent workflow
triggers, with content-based filtering rules that route events to
specific agents based on event attributes. For high-throughput
streams,
[Amazon Kinesis Data Streams](https://aws.amazon.com/kinesis/data-streams/) with Lambda event source mappings
supports batch processing without forcing agents into per-event
invocation. Event payloads should carry metadata, identifiers, and
routing information, the full data belongs in
[Amazon S3](https://aws.amazon.com/s3/) or
[Amazon DynamoDB](https://aws.amazon.com/dynamodb/), with references in the event. EventBridge Schema
Registry standardizes event formats across the organization so
consumers can generate code bindings from the schema rather than
parsing one-time JSON.

For agents that need to react to database changes,
[Amazon DynamoDB Streams](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Streams.html) triggers agents directly from data changes
without polling. Event deduplication using idempotency keys helps
prevent agents from processing the same event twice, relevant
whenever at-least-once delivery is the default. For complex event
processing that requires correlation of multiple events before
triggering an agent,
[AWS Step Functions](https://aws.amazon.com/step-functions/) or
[EventBridge
Pipes](https://aws.amazon.com/eventbridge/pipes/) aggregate and transform events before agent
invocation.

### Implementation steps

- **Configure EventBridge rules with
content-based filtering to route events to specific
agents:** Use content-based filtering on
[Amazon EventBridge](https://aws.amazon.com/eventbridge/) so agents receive only the events whose
attributes match their responsibilities.
- **Design minimal event schemas with
references rather than full payloads, registered in
EventBridge Schema Registry:** Keep event payloads
to routing metadata and identifiers, store full data in S3
or DynamoDB, and register schemas in EventBridge Schema
Registry so consumers can generate bindings.
- **Implement DynamoDB Streams for
data-change-driven agent triggers:** Use
[Amazon DynamoDB Streams](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Streams.html) to trigger agents directly from data
changes without polling.
- **Implement idempotency keys for event
deduplication in agent processing logic:** Apply
idempotency keys so agents don't process the same event
twice under at-least-once delivery.
- **Monitor event processing metrics:
event-to-invocation latency, filter efficiency, and
throughput:** Publish these metrics to CloudWatch
so filtering and routing can be tuned from measured
behavior.

## Resources

**Related best practices:**

- [AGENTPERF04-BP01
Optimize asynchronous message handling patterns](agentperf04-bp01.html)
- [AGENTPERF05-BP01
Design efficient workflow orchestration patterns](agentperf05-bp01.html)
- [AGENTPERF01-BP03
Profile end-to-end agent latency and identify optimization
targets](agentperf01-bp03.html)

**Related documents:**

- [Building
serverless architectures for agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-serverless/introduction.html)
- [Blog:
Effectively building AI agents on AWS Serverless](https://aws.amazon.com/blogs/compute/effectively-building-ai-agents-on-aws-serverless/)

**Related services:**

- [Amazon EventBridge](https://aws.amazon.com/eventbridge/)
- [Amazon Kinesis Data Streams](https://aws.amazon.com/kinesis/data-streams/)
- [AWS Lambda](https://aws.amazon.com/lambda/)
- [Amazon DynamoDB](https://aws.amazon.com/dynamodb/)
- [AWS Step Functions](https://aws.amazon.com/step-functions/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentperf04-bp03.html*

---
