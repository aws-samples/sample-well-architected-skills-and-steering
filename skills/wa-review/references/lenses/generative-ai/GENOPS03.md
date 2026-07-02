# GENOPS03 — Observability in workloads

**Pillar**: Operational Excellence  
**Best Practices**: 2

---

# GENOPS03-BP01 Implement prompt template management

Implement and maintain a versioned prompt template management system
to achieve consistent and optimized performance of language models.
This best practice aims to provide a structured approach to managing
prompt templates, which helps teams systematically version, test,
and optimize prompts. By adhering to this practice, you can achieve
greater predictability in model behavior, enhance traceability of
changes, and improve overall operational efficiency. This leads to
more reliable language model deployments, reduced risks associated
with prompt modifications, and the ability to quickly roll back to
previous versions if needed. Ultimately, this best practice helps
you deliver higher-quality outputs and maintain compliance with
security and governance standards.

**Desired outcome:** You have a
robust, versioned prompt template management system in place. Key
processes involve testing and comparing different prompt variants,
capturing baseline model outputs, and regularly reviewing and
optimizing prompts based on performance metrics.

**Benefits of establishing this best
practice:**
[Safely
automate where possible](https://docs.aws.amazon.com/wellarchitected/latest/framework/oe-design-principles.html) - Automate prompt management,
reducing the undifferentiated heavy lifting associated with
traditional prompt management techniques.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Implement versioning for your prompt templates. Test and compare
different prompt variants to identify the most effective one, and
use variables for flexibility. Capture baseline metrics of the
model output and validate whether there are deviations from the
expected results. The baseline should be your functional
performance evaluation, which uses your ground truth data. This
evaluation constitutes the set of metrics you should use for
managing your prompt templates. Versioning should include
hyperparameters or ranges where applicable, as these can influence
the output of the model, similar to the prompt contents, and are
paired with the prompt itself during evaluation.

Amazon Bedrock Prompt Management is designed to help you with the
creation and testing of prompts for foundation models. You can use
Bedrock Prompt Management to create, edit, version, and share
prompts across teams. Its components include the prompts
themselves, their variables to be filled at runtime, variants, and
a visual builder interface. This can be integrated into
applications by specifying the prompt during model inference and
supports adding a prompt node to a flow.

Amazon Bedrock Flows is a feature that allows you to create
and manage advanced workflows without writing code. Using the
visual builder interface, you can link various elements including
foundation models, prompts, agents, knowledge bases, and other AWS
services. Flows supports versioning, rollback, and A/B testing.
You can test your flows directly in the AWS Management Console or
using the
[SDK
APIs](https://docs.aws.amazon.com/bedrock/latest/userguide/sdk-general-information-section.html).

### Implementation steps

- Set up Amazon Bedrock Prompt Management.

Create the initial prompt templates by developing a
foundational set of prompt templates tailored to your
use case
- Incorporate variables within prompts to enhance
flexibility and adaptability
- Implement a robust versioning system to track changes
and iterations of prompt templates

- Implement a baseline performance evaluation.

Compile a dataset of ground truth examples to serve as a
benchmark for model evaluation
- Identify and establish performance metrics relevant to
your application
- Conduct preliminary performance assessments to establish
a baseline

- Create and test prompt variants.

Develop several versions of each prompt to explore
different phrasings and structures
- Use Amazon Bedrock Flows to configure A/B testing
workflows for prompt variants
- Analyze the performance of each prompt variant to
determine the most effective options

- Integrate prompts into applications.

Use the Amazon Bedrock SDK to incorporate prompts during
model inference
- Integrate prompt nodes into Amazon Bedrock Flows
where appropriate to streamline application workflows

- Establish a regular review and optimization process.

Plan periodic performance evaluations to assess model
effectiveness
- Review evaluation outcomes to pinpoint areas requiring
enhancement
- Update and version prompts based on evaluation insights
to continually improve performance

- Set up cross-team collaboration.

Share prompts across teams using Amazon Bedrock Prompt
Management
- Establish and disseminate guidelines for prompt creation
and modification to maintain consistency and quality

## Resources

**Related best practices:**

- [OPS05-BP10](https://docs.aws.amazon.com/wellarchitected/latest/framework/ops_dev_integ_auto_integ_deploy.html)
- [OPS05-BP01](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_dev_integ_version_control.html)

**Related documents:**

- [Amazon Bedrock Prompt Template Examples](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-templates-and-examples.html)
- [AWS re:Invent 2023 - Prompt engineering best practices for LLMs on
Amazon Bedrock (AIM377)](https://www.youtube.com/watch?v=jlqgGkh1wzY)

**Related examples:**

- [Evaluating
prompts at scale with Prompt Management and Prompt Flows for
Amazon Bedrock](https://aws.amazon.com/blogs/machine-learning/evaluating-prompts-at-scale-with-prompt-management-and-prompt-flows-for-amazon-bedrock/)

**Related tools:**

- [Amazon Bedrock](https://aws.amazon.com/bedrock/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
- [AWS SDK for Python (Boto3)](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/genops03-bp01.html*

---

# GENOPS03-BP02 Enable tracing for agents and RAG workflows

Implement comprehensive tracing for generative AI agents and RAG
workflows to enhance operational excellence and performance
efficiency. This practice offers clear visibility into model
decision-making, which helps you identify inefficiencies, optimize
performance, and debug efficiently. By adopting tracing, customers
achieve more reliable and efficient workflows, which improves model
accuracy, speeds up decision-making, and enhances overall system
performance. This approach supports continuous improvement while
keeping data secure throughout the tracing process.

**Desired outcome:** After
implementing tracing, you have enhanced agent decision-making and
RAG workflows.

**Benefits of establishing this best
practice:**
[Learn
from all operational events and metrics](https://docs.aws.amazon.com/wellarchitected/latest/framework/oe-design-principles.html) - Gain insights from
tracing for agents and RAG workflows.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Tracing can be a powerful tool for optimizing the decision-making
process of agents and RAG workflows. To improve your agent's
performance, tracing provides a detailed view of the agent's
step-by-step reasoning process. By examining these steps, you can
identify areas where the agent might be making suboptimal
decisions, taking unnecessary actions, or taking longer than
expected.

To optimize your RAG knowledge base, the structure and content
should be refined to provide relevant information to the agent. By
examining the inputs and outputs at each step, you can refine your
prompt templates to guide the agent towards more effective
decision-making. When the agent produces unexpected results, the
trace can help you understand why those decisions were made and
address the root cause.

Each response from an Amazon Bedrock agent is accompanied by a
trace that details the steps being orchestrated by the agent. The
trace helps you follow the agent's reasoning process that leads it
to the response it gives at that point in the conversation. If you
enable the trace, in the InvokeAgent response,
each chunk in the stream is accompanied by a trace field that maps
to a TracePart object. The
TracePart object contains information about the
agent and sessions, alongside the agent's reasoning process and
results.

To optimize the performance of multiple agents working in parallel
using trace data in Amazon Bedrock. To optimize data transfer
between agents and reduce latency in your multi-agent system using
Amazon Bedrock, consider using the supervisor with routing mode.
This mode allows the supervisor agent to route information
directly to the appropriate collaborator agent, reducing
unnecessary data transfers and overall latency.

Alternatively, considering using Amazon AgentCore, which supports agent tracing by default. AgentCore gives visibility into an agent’s behavior by capturing and visualizing both the traces and spans that capture each step of the agent workflow, including tool invocations and memory. AgentCore supports OpenTelemetry to help integrate agent telemetry data with existing observability systems, including Amazon CloudWatch, Datadog, LangSmith, and Langfuse.

### Implementation steps

- Collect and aggregate trace data.

Implement a system to collect trace data from agents
involved in your parallel processing workflow
- After running an Amazon Bedrock Agent, view the trace in
real-time as your agent performs orchestration
- When making an InvokeAgent request to
the Amazon Bedrock runtime endpoint, set the
enableTrace field to
TRUE. This will include a
trace field in the InvokeAgent
response for each chunk in the stream
- Store this data in a centralized location, such as
Amazon S3 or Amazon CloudWatch Logs, for quick access
and analysis

- Secure trace data.

Implement appropriate access controls to verify that
only authorized personnel can view trace data
- Be mindful of any sensitive information that might be
included in traces and handle it according to your
organization's security policies

- Analyze the trace components.

The trace is structured as a JSON object containing
fields such as agentId,
sessionId, and
trace
- PreProcessingTrace shows how the
agent contextualizes and categorizes user input
- OrchestrationTrace reveals how the
agent interprets input, invokes action groups, and
queries knowledge bases
- PostProcessingTrace demonstrates how
the agent handles the final output and prepares the
response
- FailureTrace indicates reasons for
step failures
- GuardrailTrace shows actions taken by
the Guardrail feature

- Analyze runtimes.

Review the timestamps in the trace data to identify
which agents or steps are taking the longest to complete
- Look for patterns or bottlenecks that might be causing
delays in the overall process

- Examine resource utilization.

Use the trace data to understand how each agent is
utilizing resources such as knowledge bases or action
groups
- Identify overutilization or underutilization of
resources that might be affecting performance

- Optimize agent configurations.

Based on the analysis, adjust the configuration of
individual agents to improve their performance
- This may include fine-tuning prompts, adjusting
knowledge base queries, or modifying action group
structures

- Implement load balancing across agents

Use the insights gained from trace data to distribute
workloads more evenly across agents
- Consider implementing a dynamic load balancing system
that can adjust based on real-time performance metrics

- Optimize data transfer between agents

Use the supervisor with routing mode, which allows the
supervisor agent to route information directly to the
appropriate collaborator agent, reducing unnecessary
data transfers and overall latency
- Use the session state feature to maintain context
between agent interactions, reducing the need to
transfer redundant information
- Where possible, design your multi-agent system to
process tasks concurrently, reducing overall runtime
- Where appropriate, cache frequently accessed data to
reduce repeated transfers between agents
- Deploy your agents in AWS Regions closest to your users
or data sources to minimize network latency

- Optimize your knowledge bases.

Verify that each agent's knowledge base is
well-structured and contains only relevant information
to minimize unnecessary data processing

- Set up performance monitoring.

Use Amazon CloudWatch to create custom metrics based on
the trace data
- Set up alarms to alert you when performance falls below
expected thresholds

- Conduct iterative testing.

After making optimizations, run comprehensive tests to
measure the change in overall system performance
- Use the trace data from these tests to identify further
areas for improvement

- Document and share insights.

Keep a record of optimizations made and their effects on
performance
- Share these insights with your team to improve future
multi-agent system designs

## Resources

**Related best practices:**

- [OPS08-BP03](https://docs.aws.amazon.com/wellarchitected/latest/framework/ops_workload_observability_analyze_workload_traces.html)

**Related documents:**

- [Amazon Bedrock AgentCore Samples](https://github.com/awslabs/amazon-bedrock-agentcore-samples/)
- [Track
agent's step-by-step reasoning process using trace - Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html)
- [Track
each step in your flow by viewing its trace in Amazon Bedrock
- Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-trace.html)
- [Create
multi-agent collaboration - Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/create-multi-agent-collaboration.html)

**Related examples:**

- [Introducing Amazon Bedrock AgentCore: Securely deploy and operate AI agents at any scale (preview)](https://aws.amazon.com/blogs/aws/introducing-amazon-bedrock-agentcore-securely-deploy-and-operate-ai-agents-at-any-scale/)
- [Optimize
model inference for latency - Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/latency-optimized-inference.html)
- [Optimize
performance for Amazon Bedrock agents using a single knowledge
base - Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-optimize-performance.html)

**Related tools:**

- [Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html)
- [OpenTelemetry](https://opentelemetry.io/)
- [LangFuse](https://langfuse.com/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/genops03-bp02.html*

---
