# AGENTPERF05 — Workflow orchestration and multi-agent collaboration

**Pillar**: Performance Efficiency  
**Best Practices**: 4

---

# AGENTPERF05-BP01 Design efficient workflow orchestration patterns

Agents that coordinate specialized sub-agents can solve complex
tasks faster than any single agent, and the orchestration pattern
you choose determines whether that coordination adds milliseconds or
seconds. Orchestration patterns range from static workflows (the
execution graph is fully defined at design time) to dynamic
workflows (the agent's reasoning determines the next step at
runtime). Efficient orchestration means decomposing tasks for
parallelism, minimizing data passed between steps, and matching the
orchestration pattern to the task's dependency structure.

**Desired outcome:**

- You have multi-agent workflows that execute with minimal
orchestration overhead, with independent subtasks running in
parallel and dependent tasks executing as soon as prerequisites
complete.
- You have task routing decisions that are fast and accurate.
- You have end-to-end workflow latency that approaches the
theoretical minimum defined by the critical path of dependent
operations.

**Common anti-patterns:**

- Running all workflow steps sequentially even when some steps
have no data dependencies and could run in parallel, making
end-to-end latency equal to the sum of all step durations rather
than the critical path.
- Using the orchestrator agent as a pass-through for all data
between worker agents, creating a serialization bottleneck at
every step instead of having workers write results directly to
shared storage.
- Implementing dynamic graph orchestration without cycle detection
or maximum depth limits, allowing LLM-driven routing decisions
to produce infinite loops where agents repeatedly invoke each
other without converging.

**Benefits of establishing this best
practice:**

- Parallel execution of independent subtasks reduces end-to-end
latency.
- Managed orchestration with built-in retry and error handling
improves reliability.
- Scalable orchestration handles dynamic fan-out patterns without
code changes.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Most agentic workflows are dynamic, meaning that the LLM's
reasoning determines which tool or sub-agent to invoke next based
on intermediate results. For these workflows, use your agentic
framework's built-in orchestration capabilities:

- Strands Agents provides graph-based orchestration
(GraphBuilder), supervisor patterns, and swarm coordination
- LangGraph offers stateful graph workflows
- CrewAI provides role-based crew orchestration

These framework-driven patterns are the natural fit for agent
workloads because the execution path emerges from the model's
reasoning rather than being predefined. To keep dynamic
orchestration high-performing, implement cycle detection (track
visited nodes with input hashing), maximum depth limits (10–15
steps), and bounded fan-out cardinality (5–10 concurrent branches)
to help prevent unbounded execution chains.

For deterministic workflows where the run graph is fully known at
design time, batch processing pipelines, approval workflows, data
transformation chains, use
[AWS Step Functions](https://aws.amazon.com/step-functions/) with Parallel and Map states to run steps
concurrently, Choice states for conditional branching, and
built-in Catch and Retry for error handling. Step Functions is
also valuable as a hybrid layer that handles durable orchestration
and state persistence while invoking LLM-based agents only at
decision points that require reasoning.

Keep state payloads small by storing large intermediate results in
[Amazon S3](https://aws.amazon.com/s3/) or
[Amazon DynamoDB](https://aws.amazon.com/dynamodb/) and passing only references through the
orchestration layer.

For all orchestration patterns, configure per-step and
workflow-level timeouts that help prevent slow agents from
blocking the entire workflow. For dynamic graph workflows,
allocate per-branch latency budgets derived from the overall task
SLO, if a branch exceeds its budget, terminate it and proceed with
the best available partial result. Design workflows to maximize
parallelism by analyzing task dependencies and executing
independent subtasks concurrently.

Monitor workflow execution metrics including step duration,
parallel efficiency, state payload sizes, and graph depth
distribution.

### Implementation steps

- **Analyze multi-agent task
dependencies and classify each workflow:** Classify
each workflow as dynamic graph (LLM-driven routing, most
agent workflows), hybrid (deterministic flow with LLM
decision points), or static (fully predefined execution
graph), and use the classification to drive the
orchestration choice.
- **For dynamic graph workflows, use
your agentic framework's native orchestration:**
Use Strands GraphBuilder, LangGraph, or equivalent with
cycle detection, maximum depth limits, and bounded fan-out
cardinality to help prevent unbounded execution chains.
- **For static/hybrid workflows,
implement using Step Functions with Parallel and Map
states:** Use
[AWS Step Functions](https://aws.amazon.com/step-functions/) Parallel and Map states to run steps
concurrently with built-in retry and error handling on
deterministic paths.
- **Implement efficient state passing
using S3/DynamoDB references rather than inline
payloads:** Keep orchestration payloads small by
storing large intermediate results in S3 or DynamoDB and
passing only references.
- **Configure per-step and
workflow-level timeouts with fallback strategies for slow
agents:** Set timeouts at both the step and
workflow level, and define fallback behavior so a single
slow agent can't stall the whole workflow.
- **Monitor workflow execution metrics:
step duration, parallel efficiency, state payload sizes, and
graph depth distribution:** Publish these metrics
to CloudWatch so orchestration performance can be tuned from
data rather than assumption.

## Resources

**Related best practices:**

- [AGENTPERF05-BP02
Implement optimized multi-agent collaboration models](agentperf05-bp02.html)
- [AGENTPERF05-BP03
Optimize multi-stage AI pipeline execution](agentperf05-bp03.html)
- [AGENTPERF02-BP01
Design efficient reasoning pipelines](agentperf02-bp01.html)

**Related documents:**

- [Blog:
Customize agent workflows with advanced orchestration
techniques using Strands Agents](https://aws.amazon.com/blogs/machine-learning/customize-agent-workflows-with-advanced-orchestration-techniques-using-strands-agents/)
- [Agentic
AI patterns and workflows on AWS, Workflow orchestration
agents](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/workflow-orchestration-agents.html)
- [Building
serverless architectures for agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-serverless/introduction.html)
- [Blog:
Effectively building AI agents on AWS Serverless](https://aws.amazon.com/blogs/compute/effectively-building-ai-agents-on-aws-serverless/)

**Related videos:**

- [Architecting
scalable and secure agentic AI with AgentCore (AIM431)](https://www.youtube.com/watch?v=wqmeZOT6mmc)
- [Build
Your First Agent Workflow with Strands](https://www.youtube.com/watch?v=oGzEKQVhKQU)
- [Build
Reliable AI Agents with LangGraph](https://www.youtube.com/watch?v=E0BtW2yt2pA)

**Related examples:**

- [GitHub:
Guidance for multi-agent orchestration using Bedrock
AgentCore](https://github.com/aws-solutions-library-samples/guidance-for-multi-agent-orchestration-using-bedrock-agentcore-on-aws)

**Related tools:**

- [Strands
Agents](https://strandsagents.com/)

**Related services:**

- [AWS Step Functions](https://aws.amazon.com/step-functions/)
- [Amazon
Bedrock AgentCore Runtime](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon S3](https://aws.amazon.com/s3/)
- [Amazon DynamoDB](https://aws.amazon.com/dynamodb/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentperf05-bp01.html*

---

# AGENTPERF05-BP02 Implement optimized multi-agent collaboration models

Multi-agent systems typically deliver the strongest results when
each collaboration pattern is matched to the task it was designed
for (for example, supervisor-worker for structured decomposition,
swarm for creative exploration, and pipeline for sequential
processing). Before picking any multi-agent pattern, decide whether
a capability should be a sub-agent or a tool that a single agent
invokes. A tool call completes in milliseconds, while a sub-agent
delegation is a full LLM reasoning loop that costs time and tokens.

**Desired outcome:**

- You have multi-agent workflows that use collaboration models
matched to their task characteristics.
- You have each capability implemented at the right abstraction
level, tool for deterministic single-step operations, sub-agent
for tasks that require independent reasoning.
- You have coordination overhead minimized through appropriate
pattern selection and implementation.

**Common anti-patterns:**

- Delegating to a sub-agent for capabilities that are
deterministic, stateless, and single-step, API calls, database
lookups, or format conversions, paying the full cost of an LLM
reasoning loop for work that a tool call would handle in
milliseconds.
- Using a supervisor-worker model for all multi-agent workflows,
creating a bottleneck at the supervisor that must process every
intermediate result and make every delegation decision.
- Deploying swarm patterns without explicit convergence criteria
or resource budgets, letting agents continue exploring
indefinitely without converging on a shared outcome.

**Benefits of establishing this best
practice:**

- Matching the collaboration model to task structure minimizes
coordination overhead.
- Appropriate model selection for decomposable tasks maximizes
parallelism.
- Timeouts and fallback mechanisms keep collaboration resilient
when individual agents fail or slow down.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Use a sub-agent when the capability requires its own reasoning
(LLM inference for ambiguous inputs or judgment calls), its own
context or memory scope, multi-step tool orchestration where
sequencing requires reasoning, a different model or prompt, or
independent failure isolation.

Use a tool when the capability is deterministic, stateless,
single-step, and fast (under 2-3 seconds).

For borderline cases, start with a tool and promote to a sub-agent
only when frequent re-invocation patterns indicate the capability
needs its own reasoning loop.

Once multi-agent architecture is warranted, select the
collaboration model based on task characteristics. Use
supervisor-worker when the task has clear decomposition and
centralized quality control is needed. Strands Agents's
agent-as-tool pattern and Amazon Bedrock Agents' multi-agent
collaboration provide supervisor-worker orchestration with
automatic context passing and result aggregation.

Use pipeline when the task has a natural sequential flow, balance
stage durations and use your framework's graph orchestration to
chain agents sequentially.

Use peer-to-peer or blackboard when multiple agents need to
contribute partial solutions asynchronously, implement a shared
workspace using AgentCore Memory or DynamoDB with event-driven
notifications.

Use swarm when the task benefits from parallel exploration and
emergent behavior, implement convergence detection and per-swarm
token budgets to help prevent unbounded resource consumption.

For deterministic delegation logic or durable long-running
workflows,
[AWS Step Functions](https://aws.amazon.com/step-functions/) remains a strong alternative for orchestrating
agent invocations.

For all collaboration models, implement timeout and fallback
mechanisms that help prevent a single slow or failed agent from
blocking the entire workflow. Deploy multi-agent systems on
[Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html) for managed scaling and
observability, or on Amazon EKS or Amazon ECS for custom
container-based deployments. Monitor collaboration overhead
metrics including coordination latency, redundant work rate, and
throughput per model.

### Implementation steps

- **Evaluate whether each capability
should be a tool or a sub-agent:** Default to tools
and promote to sub-agents only when re-invocation patterns
indicate the need for independent reasoning.
- **Classify multi-agent workflows by
task characteristics:** Assess decomposability,
dependency structure, latency requirements, and whether the
task benefits from parallel exploration.
- **Select the collaboration
model:** Use supervisor-worker for clear
decomposition, pipeline for sequential flow, peer-to-peer
for shared problem spaces, and swarm for parallel
exploration.
- **Implement using your framework's
native multi-agent patterns:** Use Strands
agent-as-tool, Amazon Bedrock multi-agent collaboration, or
an equivalent, and use
[Amazon
Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) for shared context across
agents.
- **Implement timeout and fallback
mechanisms for all collaboration models:** Set
per-agent timeouts and define fallback behavior so one slow
or failed agent can't block the full workflow.
- **Monitor collaboration overhead
metrics and optimize model selection over time:**
Track coordination latency, redundant work rate, and
throughput per model, and re-evaluate the collaboration
choice as traffic shifts.

## Resources

**Related best practices:**

- [AGENTPERF05-BP01 Design
efficient workflow orchestration patterns](agentperf05-bp01.html)
- [AGENTPERF05-BP04
Implement efficient agent delegation and handoff
patterns](agentperf05-bp04.html)
- [AGENTPERF04-BP02
Implement efficient protocol-based agent communications](agentperf04-bp02.html)

**Related documents:**

- [Blog:
Multi-agent collaboration patterns with Strands Agents and
Amazon Nova](https://aws.amazon.com/blogs/machine-learning/multi-agent-collaboration-patterns-with-strands-agents-and-amazon-nova/)
- [Blog:
Multi-agent collaboration with Strands](https://aws.amazon.com/blogs/devops/multi-agent-collaboration-with-strands/)
- [Agentic
AI patterns and workflows on AWS, Multi-agent
collaboration](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/multi-agent-collaboration.html)
- [Agentic
AI patterns and workflows on AWS, Workflow orchestration
agents](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/workflow-orchestration-agents.html)
- [Use
multi-agent collaboration with Amazon Bedrock Agents](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-multi-agent-collaboration.html)

**Related videos:**

- [Amazon
Bedrock Agents and AgentCore Design Patterns (TNC322)](https://www.youtube.com/watch?v=GYlPFmrATjU)

**Related examples:**

- [GitHub:
Bedrock multi-agent collaboration workshop](https://github.com/aws-samples/bedrock-multi-agents-collaboration-workshop)
- [GitHub:
Multi-agent collaboration with Strands](https://github.com/aws-samples/sample-multi-agent-collaboration-with-strands)

**Related tools:**

- [Strands
Agents](https://strandsagents.com/)

**Related services:**

- [Amazon
Bedrock Agents](https://aws.amazon.com/bedrock/agents/)
- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [AWS Step Functions](https://aws.amazon.com/step-functions/)
- [Amazon DynamoDB](https://aws.amazon.com/dynamodb/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentperf05-bp02.html*

---

# AGENTPERF05-BP03 Optimize multi-stage AI pipeline execution

Real-world agent tasks rarely complete in a single step. Document
processing, data analysis, and customer service workflows all
involve multiple sequential stages where each stage's throughput is
limited by the slowest process or mechanism. Each stage transition
introduces overhead (like serialization, network transfer, or cold
starts), and streaming or micro-batching allows downstream stages to
begin processing before upstream stages complete, overlapping
execution to cut total latency.

**Desired outcome:**

- You have multi-stage AI pipelines that execute with minimal
inter-stage overhead, with data flowing efficiently between
stages.
- You have pipeline throughput balanced across stages with no
single stage creating a persistent bottleneck.
- You have streaming implemented where possible to overlap
processing.
- You have each stage's compute resources right-sized for its
specific requirements.

**Common anti-patterns:**

- Waiting for an entire batch to complete one stage before
starting the next, when streaming or micro-batching would let
downstream stages begin processing as upstream results become
available.
- Using the same compute configuration for all pipeline stages
regardless of their processing requirements, over-provisioning
lightweight stages and under-provisioning compute-intensive
stages.
- Serializing large intermediate results to persistent storage
between every stage when in-memory passing or streaming would be
more efficient for stages that execute in close succession.

**Benefits of establishing this best
practice:**

- Streaming and micro-batching overlap stage processing, reducing
end-to-end latency.
- Balanced stage capacity and buffered inter-stage communication
improve throughput.
- Right-sized compute per stage optimizes cost.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Implement multi-stage pipelines using
[AWS Step Functions](https://aws.amazon.com/step-functions/) with stage-specific
[AWS Lambda](https://aws.amazon.com/lambda/) functions,
[Amazon ECS](https://aws.amazon.com/ecs/)
tasks, or agents hosted on
[Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html), where each stage's compute
configuration is independently tuned. For pipelines with high
throughput requirements, Step Functions Distributed Map processes
items in parallel across stages. Right-size compute for each
stage, using Lambda for lightweight processing, ECS for
compute-intensive stages, and AgentCore Runtime for stages that
require LLM-based reasoning.

Streaming between stages is the single largest latency win when it
applies. Use Amazon Bedrock's streaming inference API to begin
post-processing output tokens as they are generated rather than
waiting for the complete response. For data-intensive pipelines,
[Amazon Kinesis Data Streams](https://aws.amazon.com/kinesis/data-streams/) acts as an inter-stage buffer that
supports streaming data flow, so downstream stages begin
processing as soon as upstream results are available. For batch
pipelines, micro-batching sends small groups of items to
downstream stages as they complete rather than waiting for the
entire batch.

Pipeline-level observability through
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) or
[AWS X-Ray](https://aws.amazon.com/xray/)
traces requests across all stages, identifying the critical path
and the stage that contributes most to end-to-end latency. Balance
stage durations by profiling each stage and adjusting processing
granularity, split slow stages into parallel sub-stages or combine
fast stages to reduce inter-stage transitions.

### Implementation steps

- **Map the multi-stage pipeline and
identify dependencies between stages:** Document
stage dependencies, opportunities for streaming, and the
critical path so optimization effort lands on the stages
that drive end-to-end latency.
- **Implement each stage as an
independent compute unit with stage-specific resource
configurations:** Use
[AWS Lambda](https://aws.amazon.com/lambda/) for lightweight processing,
[Amazon ECS](https://aws.amazon.com/ecs/) for compute-intensive stages, and AgentCore
Runtime for stages that require LLM reasoning, and tune each
stage's resources to its own profile.
- **Enable streaming between stages
using the Amazon Bedrock streaming API and Kinesis Data
Streams where applicable:** Use the streaming
inference API to post-process output tokens as they are
generated, and
[Amazon Kinesis Data Streams](https://aws.amazon.com/kinesis/data-streams/) as an inter-stage buffer so
downstream stages begin processing as upstream results
arrive.
- **Implement micro-batching for batch
pipelines to reduce end-to-end latency:** Send
small groups of items to downstream stages as they complete
rather than waiting for the full batch.
- **Configure AgentCore Observability or
X-Ray tracing across all pipeline stages for end-to-end
latency visibility:** Use
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) or
[AWS X-Ray](https://aws.amazon.com/xray/) to trace requests across every stage.
- **Monitor per-stage latency,
throughput, and resource utilization to identify and resolve
bottlenecks:** Publish metrics for each stage so
bottleneck stages are visible and can be split,
parallelized, or resized.

## Resources

**Related best practices:**

- [AGENTPERF05-BP01 Design
efficient workflow orchestration patterns](agentperf05-bp01.html)
- [AGENTPERF02-BP04
Optimize streaming responses and time-to-first-token for agent
interactions](agentperf02-bp04.html)
- [AGENTPERF02-BP03
Optimize agent execution paths for reduced latency](agentperf02-bp03.html)

**Related documents:**

- [Multi-stage
AI workflow pattern, Building serverless architectures for
agentic AI](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-serverless/pattern-multi-stage-ai.html)
- [Blog:
Effectively building AI agents on AWS Serverless](https://aws.amazon.com/blogs/compute/effectively-building-ai-agents-on-aws-serverless/)
- [Agentic
AI patterns and workflows on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/introduction.html)

**Related examples:**

- [GitHub:
Build GenAI agent workflows with Step Functions](https://github.com/aws-samples/build-genai-agent-workflows-with-step-functions)

**Related services:**

- [AWS Step Functions](https://aws.amazon.com/step-functions/)
- [AWS Lambda](https://aws.amazon.com/lambda/)
- [Amazon ECS](https://aws.amazon.com/ecs/)
- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon Kinesis Data Streams](https://aws.amazon.com/kinesis/data-streams/)
- [Amazon
Bedrock](https://aws.amazon.com/bedrock/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentperf05-bp03.html*

---

# AGENTPERF05-BP04 Implement efficient agent delegation and handoff patterns

Smooth agent-to-agent transitions make multi-agent workflows feel
like a single cohesive experience, where the receiving agent picks
up exactly where the delegating agent left off. Delegation and
handoff both require efficient context transfer. The receiving agent
needs enough context to act, but transferring too much wastes time
and tokens.

**Desired outcome:**

- You have agent delegation and handoff operations that complete
with minimal latency, transferring precisely the context needed
by the receiving agent.
- You have receiving agents that begin productive processing
immediately without re-deriving context the delegating agent
already possessed.
- You have standardized context transfer mechanisms that let any
agent delegate to or receive handoffs from any other agent.
- You have handoff latency measured and optimized as part of the
overall workflow performance budget.

**Common anti-patterns:**

- Transferring the entire conversation history and all accumulated
context during every delegation, regardless of what the
receiving agent actually needs, wasting serialization time and
context window capacity.
- Requiring receiving agents to re-derive context (re-query
databases, re-retrieve documents) that the delegating agent
already had, duplicating work and adding latency.
- Implementing delegation as synchronous blocking calls where the
parent agent waits idle for the child agent to complete, wasting
the parent's compute resources.

**Benefits of establishing this best
practice:**

- Selective context transfer and shared context stores reduce
delegation latency.
- Receiving agents reuse context already gathered by delegating
agents instead of repeating the work.
- Asynchronous delegation patterns improve parent agent
throughput.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Implement a shared context store using
[Amazon
Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) or
[Amazon DynamoDB](https://aws.amazon.com/dynamodb/) where delegating agents write context and
receiving agents read it, avoiding the need to serialize and
transfer large context payloads through the orchestration layer.
Context transfer schemas define the minimum context required for
each delegation type, a data validation agent needs the data and
validation rules, not the full conversation history. For agents
built with Strands Agents, the built-in agent-as-tool pattern
automatically inherits relevant context from the parent agent's
session.

For handoff patterns in conversational agents, context
summarization compresses the conversation into a concise handoff
summary tailored to the receiving agent's role, rather than
transferring raw conversation history. For predictable delegation
patterns, for example, a triage agent that consistently delegates
to one of several specialist agents, pre-warming through
[AWS Lambda](https://aws.amazon.com/lambda/) provisioned concurrency or warm session pools on
AgentCore Runtime removes cold-start latency from the receiving
side. Asynchronous delegation lets the parent agent continue
processing other tasks while the child agent works, using
callbacks or
[Amazon EventBridge](https://aws.amazon.com/eventbridge/) notifications to receive results.

[Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) standardizes delegation
interfaces, letting any agent delegate to any other agent through
a consistent API that handles context transfer, authentication,
and result delivery. Handoff latency belongs in agent performance
dashboards as a distinct metric, measured from delegation
initiation to the receiving agent's first productive action.

### Implementation steps

- **Identify delegation and handoff
patterns in existing multi-agent workflows and measure
current transition latency:** Map delegation and
handoff points and measure the current transition latency so
optimization targets are grounded in data.
- **Implement shared context stores
using AgentCore Memory or DynamoDB for context transfer
between agents:** Use
[Amazon
Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) or
[Amazon DynamoDB](https://aws.amazon.com/dynamodb/) so delegating agents write context once and
receiving agents read it without serializing large payloads.
- **Define minimum context schemas for
each delegation type, specifying exactly what the receiving
agent needs:** Keep the delegation payload small
and purpose-specific so receivers only get the context
required for their role.
- **Implement context summarization for
conversational handoffs that compresses history into
role-appropriate summaries:** Summarize raw
conversation history into a handoff summary tailored to the
receiving agent's role rather than forwarding the full
transcript.
- **Configure pre-warming for
predictable delegation patterns using provisioned
concurrency or warm session pools:** For recurring
delegation targets, use
[AWS Lambda](https://aws.amazon.com/lambda/) provisioned concurrency or warm session pools
on AgentCore Runtime to remove cold-start latency.
- **Convert synchronous delegations to
asynchronous patterns with callback-based result
delivery:** Let the parent agent continue other
work while the child agent runs, receiving results through
callbacks or EventBridge notifications.

## Resources

**Related best practices:**

- [AGENTPERF05-BP01 Design
efficient workflow orchestration patterns](agentperf05-bp01.html)
- [AGENTPERF05-BP02
Implement optimized multi-agent collaboration models](agentperf05-bp02.html)
- [AGENTPERF04-BP01
Optimize asynchronous message handling patterns](agentperf04-bp01.html)

**Related documents:**

- [Blog:
Multi-agent collaboration patterns with Strands Agents and
Amazon Nova](https://aws.amazon.com/blogs/machine-learning/multi-agent-collaboration-patterns-with-strands-agents-and-amazon-nova/)
- [Agentic
AI patterns and workflows on AWS, Multi-agent
collaboration](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/multi-agent-collaboration.html)
- [Operationalizing
agentic AI on AWS, Design for composability and
collaboration](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-operationalizing-agentic-ai/introduction.html)
- [Amazon
Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html)

**Related videos:**

- [AgentCore
Memory: Episodic Memory & Patterns](https://www.youtube.com/watch?v=1EEIGsKIjGA)

**Related examples:**

- [GitHub:
Guidance for multi-agent orchestration using Bedrock
AgentCore](https://github.com/aws-solutions-library-samples/guidance-for-multi-agent-orchestration-using-bedrock-agentcore-on-aws)
- [GitHub:
Amazon Bedrock AgentCore samples, Memory tutorials](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/04-AgentCore-memory)

**Related tools:**

- [Strands
Agents](https://strandsagents.com/)

**Related services:**

- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon DynamoDB](https://aws.amazon.com/dynamodb/)
- [AWS Lambda](https://aws.amazon.com/lambda/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentperf05-bp04.html*

---
