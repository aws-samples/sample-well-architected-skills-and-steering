# GENREL03 — Prompt remediation and recovery actions

**Pillar**: Reliability  
**Best Practices**: 2

---

# GENREL03-BP01 Use logic to manage prompt flows and gracefully recover from failure

Leverage conditions, loops, and other logical structures at the
prompt management or application layer to reduce the risk of an
unreliable experience.

**Desired outcome:** When
implemented, this best practice improves the reliability of your
generative AI workload by reducing the likelihood of performance
degradation logical errors in your prompt flows.

**Benefits of establishing this best
practice:**
[Automatically
recover from failure](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel-dp.html) - Implementing recovery logic in
generative AI workflows helps to reduce potentially blocking
failures, while encouraging generative AI applications to gracefully
recover automatically.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Define expected behavior for generative AI applications
before, during, and after prompts. Create layers of
abstraction between users and models to facilitate retries,
error handling, and graceful failures. For multi-step prompt
flows, implement logic statements to check if your prompts
contain the expected information. Apply similar logic to
verify your model's respond with expected content.

For prompt flows containing data from external sources,
implement logic to verify the relevant data from the external
source exists. Define a fallback action or default modality in
the absence of relevant data. Apply similar reasoning to model
responses enriched with embeddings from a vector search
engine. Consider applying checks on the model's response to
identify the relevance of the returned data or a fallback
action if no data is returned at all.

Agentic workflows commonly make calls to external systems.
Develop agents with error handling in mind. Consider how
errors are propagated back up to agents. Upon receiving an
error, an agent should take appropriate action to retry or
gracefully fail. One way to accomplish this is to have the
agent classify responses from external systems as actionable
or not. Actionable responses are anticipated and
well-understood responses (for example, a database query
returning at least one result). An inactionable response
traditionally requires error handling at the software layer
(for example, error codes or empty responses). Agents can be
prompted to classify responses in these cases and take action
appropriately. This method may serve to reduce non-determinism
and increase reliability of agent workflows.

When developing multistep prompt flows or prompt chains,
consider using Amazon Bedrock Flows to orchestrate multistep
prompts. Bedrock Flows enables graceful failure and recovery
for long prompt chains, which allows your applications to take
appropriate action on failure. Bedrock Flows has nodes for
controlling flow logic, which include iterator nodes and
condition nodes. Customers may consider using these nodes to
implement graceful recovery instead of developing a custom
abstraction layer.

### Implementation steps

- Establish error classification system:

Categorize common failure types
- Define severity levels
- Create response templates for each error category
- Set up automated detection mechanisms

- Implement recovery mechanisms:

Design retries strategies with exponential backoff
- Create fallback prompt templates
- Develop circuit breaker implementations
- Set up automated recovery workflows

- Configure monitoring and alerting:

Track recovery success rates
- Monitor remediation effectiveness
- Set up alerts for repeated failures
- Implement performance tracking

- Create continuous improvement process:

Analyze failure patterns
- Update remediation strategies
- Refine prompt templates
- Optimize recovery workflows

## Resources

**Related best practices:**

- [REL05-BP01](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_mitigate_interaction_failure_graceful_degradation.html)

**Related documents:**

- [Demo
- Amazon Bedrock Flows](https://www.youtube.com/watch?v=_Bmk6peAHao)
- [Build
an end-to-end generative AI workflow with Amazon Bedrock
Flows](https://docs.aws.amazon.com/bedrock/latest/userguide/flows.html)

**Related examples:**

- [Amazon Bedrock Flows is now generally available with enhanced safety
and traceability](https://aws.amazon.com/blogs/machine-learning/amazon-bedrock-flows-is-now-generally-available-with-enhanced-safety-and-traceability/)
- [Simplifying
the Prompts Lifecycle with Prompt Management and Prompt Flows
for Amazon Bedrock Workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/c81935bc-0b43-4bd6-bd01-db45f847d6bd/en-US)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/genrel03-bp01.html*

---

# GENREL03-BP02 Implement timeout mechanisms on agentic workflows

Implement controls to detect and terminate long-running unexpected
workflows.

**Desired outcome:** When
implemented, this best practice improves the reliability of your
generative AI workload by freeing resources that might have been
consumed by unexpected long-running execution loops.

**Benefits of establishing this best
practice:**
[Automatically
recover from failure](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel-dp.html) - Implementing agent timeouts helps to
reduce the likelihood of blocking failures on agentic workflows and
executions.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Agentic workflows act on behalf of a user by making calls to
external systems. External systems may themselves perform
several time-consuming tasks which the agent is not aware of,
resulting in idle agents that could run for an extended
period. To maintain a reliable agentic system, implement
controls to manage agentic timeout.

One approach to controlling agentic runtime or lifecycle is to
implement runtime timeouts on the external infrastructure. For
example, if an agent makes a call to a function through an
Action Group, consider applying a timeout to the corresponding
function. The timeout should be set to include the maximum
allowable time needed to complete a process, accounting for
additional latency for edge cases such as cold starts. You may
consider rounding this value up to avoid unnecessary early
terminations.

Alternatively, consider connecting agentic workflows to an
event system, developing an asynchronous process management
architecture. Introducing an asynchronous event system gives
users the most flexibility and visibility into agent process
lifecycle or flow. By requiring the compute underpinning an
Action Group to publish events, workload owners maintain
insight into where an agent may encounter stalled flow or
process. Consider using events to publish agent updates and
act appropriately to stop long-running invocations.

Error handling at the agent layer should be transparent to
users. When errors occur, communicate clear details about the
issue while maintaining system security by avoiding exposure
of sensitive internal information. The response should outline
specific next steps so that users can complete their tasks
independently if the agent remains unavailable. This approach
promotes operational resilience while maintaining security
best practices, as users receive actionable guidance without
compromising system integrity.

### Implementation steps

- Create an agent workflow configuration:

Define maximum runtime thresholds
- Set up timeout controls at function and workflow levels
- Configure event publishing for process monitoring

- Implement timeout mechanisms:

Add timeouts at the agent layer to terminate sessions waiting for user input
- Configure timeouts on external compute resources
- Set up dead letter queues for timed-out processes

- Establish monitoring and alerting:

Track agent execution times
- Monitor timeout frequency
- Alert on repeated timeouts

- Define recovery procedures:

Create graceful termination processes
- Implement cleanup routines for timed-out sessions
- Set up automated retry mechanisms where appropriate

## Resources

**Related best practices:**

- [REL05-BP05](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_mitigate_interaction_failure_client_timeouts.html)

**Related documents:**

- [AWS re:Invent 2023
- Simplify generative AI app development with Agents for
Amazon Bedrock (AIM353)](https://www.youtube.com/watch?v=JNZPW82uv7w)
- [Automate tasks in
your application using AI agents](https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html)

**Related examples:**

- [Best
practices for building robust generative AI applications with
Amazon Bedrock Agents - Part 1](https://aws.amazon.com/blogs/machine-learning/best-practices-for-building-robust-generative-ai-applications-with-amazon-bedrock-agents-part-1/)
- [Best
practices for building robust generative AI applications with
Amazon Bedrock Agents - Part 2](https://aws.amazon.com/blogs/machine-learning/best-practices-for-building-robust-generative-ai-applications-with-amazon-bedrock-agents-part-2/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/genrel03-bp02.html*

---
