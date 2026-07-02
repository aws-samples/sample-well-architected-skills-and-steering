# GENCOST03 — Cost-aware prompting

**Pillar**: Cost Optimization  
**Best Practices**: 4

---

# GENCOST03-BP01 Optimize prompt token length

Long prompts tend to be filled with lots of context, additional
information, and requests for a foundation model when it is
conducting inference. Reducing prompt length lowers the amount of
compute needed to serve inference.

**Desired outcome:** When
implemented, this best practices encourages prompts to be as short
as possible while meeting performance requirements.

**Benefits of establishing this best
practice:**
[Adopt
a consumption model](https://docs.aws.amazon.com/wellarchitected/latest/framework/cost-dp.html) - Foundation models on a consumption
based pricing model charge by the token. Reducing prompt length has
the effect of reducing the cost of processing the prompt.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Whether your foundation model charges by tokens processed or not,
prompt length can directly or indirectly contribute to the cost of
inference. For self-hosted model infrastructure or provisioned
throughput, longer prompts require increased computation time and
increase the scale of infrastructure required to host your
workload. For managed model infrastructure, the increased token
count of longer prompts results in higher per-inference costs.
Consider shortening prompts through rigorous testing. You may even
use a separate large language model to shorten a prompt without
reduction in performance. Reducing even a few tokens off the
prompt contributes to cost optimization in the long-run.

### Implementation steps

- Identify a verbose prompt which could be optimized.
- Engineer the prompt to reduce the token count, trimming as many unnecessary words as possible.
- Consider using a separate LLM to offer a shortened prompt
that satisfies the end goal.

Amazon Bedrock Prompt Optimization can typically optimize prompt language to help provide consistent results.

- Continue testing and optimizing the prompt to validate it
meets the workload requirements.

Experiment with zero-shot prompting techniques for
common knowledge tasks.
- Consider chain-of-thought or tree-of-thought for logical
reasoning.
- Evaluate the benefits of least-to-most prompting for
complex problems with nuanced solutions.
- Research prompt engineering techniques to find the most
cost-effective approach to your problem.

## Resources

**Related best practices:**

- [COST10-BP01](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_evaluate_new_services_review_process.html)

**Related documents:**

- [AWS re:Invent 2023
- Prompt Engineering Best Practices for LLMs on Amazon Bedrock
(AIM377)](https://www.youtube.com/watch?v=jlqgGkh1wzY)

**Related examples:**

- [Improve the performance of your Generative AI applications with Prompt Optimization on Amazon Bedrock](https://aws.amazon.com/blogs/machine-learning/improve-the-performance-of-your-generative-ai-applications-with-prompt-optimization-on-amazon-bedrock/)
- [Amazon Bedrock Prompt Optimization Drives LLM Applications Innovation for Yuewen Group](https://aws.amazon.com/blogs/machine-learning/amazon-bedrock-prompt-optimization-drives-llm-applications-innovation-for-yuewen-group/)
- [Amazon Bedrock Prompt Management is now Available in GA](https://aws.amazon.com/blogs/machine-learning/amazon-bedrock-prompt-management-is-now-available-in-ga/)
- [Prompt
Engineering Guide](https://www.promptingguide.ai/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/gencost03-bp01.html*

---

# GENCOST03-BP02 Control model response length

The costs of a foundation model are often measured in the lengths of
the model's responses. This best practice describes how to control
model responses to reduce costs.

**Desired outcome:** When
implemented, this best practices encourages model responses to be as
short as possible without sacrificing usability.

**Benefits of establishing this best
practice:**
[Adopt
a consumption model](https://docs.aws.amazon.com/wellarchitected/latest/framework/cost-dp.html) - Foundation models on a consumption
based pricing model charge by the token. Reducing model response
length has the effect of reducing the cost of inference.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Model response length should be kept as concise as possible, so
long as it satisfies the use case. In Amazon Bedrock, consider
specifying a response length hyperparameter to control and predict
the upper-limit of the response length. Additionally, you may
consider adding a phrase to your prompts which encourages the
model to be succinct, further reducing the length of the model's
response while encouraging the model to maintain a high degree of
performance. Small optimizations in token count for model
responses can improve model's generated output cost.

In scenarios where a full-text response is unnecessary,
consider introducing determinism to the model. You might
instruct the model to evaluate its response against a set of
keyed options, returning the key which maps to the model's
response. For example:

End of prompt template

If after carefully evaluating all of the information
available to you that you respond in the affirmative,
simply respond with the word True. Otherwise, respond
False, providing a detailed explanation for your
decision.

Such behavior as the one shown above encourages model
responses to be succinct. Moreover, this behavior has the
added benefit introducing determinism into the system for
*True* responses.

### Implementation steps

- Understand how the model response is to be used, defined a
minimalist response scheme (for example, 0 for affirmative
and 1 for rejection).
- Inform the model in the prompt of the requested model
response scheme, and ask the model to respond in kind.
- Introduce a response length control to limit response
tokens.

Set a hard limit on the response length by configuring
the response length hyperparameter accordingly.
- Extend the prompt template to encourage deterministic
responses.

- Set a hard limit on the response length by configuring the
response length hyperparameter accordingly.
- Continue testing and optimizing the model's response to
verify it satisfies the workload requirements.

## Resources

**Related best practices:**

- [COST10-BP01](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_evaluate_new_services_review_process.html)

**Related documents:**

- [AWS re:Invent 2023
- Prompt Engineering Best Practices for LLMs on Amazon Bedrock
(AIM377)](https://www.youtube.com/watch?v=jlqgGkh1wzY)

**Related examples:**

- [Amazon Bedrock Prompt Management is now Available in GA](https://aws.amazon.com/blogs/machine-learning/amazon-bedrock-prompt-management-is-now-available-in-ga/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/gencost03-bp02.html*

---

# GENCOST03-BP03 Implement prompt caching to reduce token costs

Implement prompt caching for supported foundation models to
reduce inference response latency and input token costs. This
best practice helps organizations optimize costs by caching
frequently used portions of prompts to avoid recomputation,
while maintaining performance and reliability.

**Desired outcome:** Reduce
inference costs by caching commonly used prompt components and
using cached tokens at a reduced rate.

**Benefits of establishing this best
practice:**

- [Control
resource consumption parameters](https://docs.aws.amazon.com/wellarchitected/latest/framework/cost-dp.html) - Reduce token costs by
reusing cached prompt components.
- [Optimize
model and inference selection](https://docs.aws.amazon.com/wellarchitected/latest/framework/cost-dp.html) - Decrease latency by
avoiding recomputation of cached prompt sections.

**Level of risk exposed if this best
practice is not established:** Medium

## Implementation guidance

Prompt caching is an optional feature available on supported
models in Amazon Bedrock that can reduce inference response
latency and input token costs. By caching portions of your
context, the model can use the cache to skip recomputation,
allowing Bedrock to achieve cost savings through lower token
rates.

Prompt caching can help when you have workloads with long and
repeated contexts that are frequently reused across multiple
queries. For example, if you have a chatbot where users can
upload documents and ask questions about them, caching the
document content avoids reprocessing it for each user query.

When using prompt caching, cached tokens are charged at a
reduced rate. Depending on the model, tokens written to cache
may be charged at a higher rate than uncached input tokens.
Tokens not read from or written to cache are charged at the
standard input token rate.

Cache checkpoints have model-specific minimum and maximum
token requirements. You can only create a checkpoint if your
prompt prefix meets the minimum token count. For example,
Claude 3.7 Sonnet requires at least 1,024 tokens per
checkpoint. The cache has a five minute TTL that resets with
each successful hit.

### Implementation steps

- Identify opportunities for caching:

Review workload for repeated prompt components
- Verify prompts meet minimum token requirements
- Assess potential cost savings from reduced token
rates

- Enable prompt caching for supported models:

Turn on caching in Amazon Bedrock console
- For APIs, set appropriate caching flags
- Configure cache checkpoints at optimal locations

- Monitor caching metrics:

Track cache hit and miss rates
- Monitor token costs for cached compared to uncached
content
- Analyze latency improvements

- Optimize cache usage:

Tune checkpoint placement
- Adjust prompt structure to maximize cache hits
- Balance cache write costs with read savings

## Resources

**Related best practices:**

- [COST10-BP01](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_evaluate_new_services_review_process.html)

**Related documents:**

- [Effectively
use prompt caching on Amazon Bedrock](https://aws.amazon.com/blogs/machine-learning/effectively-use-prompt-caching-on-amazon-bedrock/)
- [Prompt
caching for faster model inference](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-caching.html)

**Related examples:**

- [Effectively
use prompt caching on Amazon Bedrock](https://aws.amazon.com/blogs/machine-learning/effectively-use-prompt-caching-on-amazon-bedrock/)
- [Supercharge
your development with Claude Code and Amazon Bedrock prompt
caching](https://aws.amazon.com/blogs/machine-learning/supercharge-your-development-with-claude-code-and-amazon-bedrock-prompt-caching/)
- [Reduce
costs and latency with Amazon Bedrock Intelligent Prompt
Routing and prompt caching (preview)](https://aws.amazon.com/blogs/aws/reduce-costs-and-latency-with-amazon-bedrock-intelligent-prompt-routing-and-prompt-caching-preview/)
- [Amazon
Bedrock Prompt Management is now Available in GA](https://aws.amazon.com/blogs/machine-learning/amazon-bedrock-prompt-management-is-now-available-in-ga/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/gencost03-bp03.html*

---

# GENCOST03-BP04 Annotate user input to enable cost-aware content filtering

Annotate specific sections of input prompts to selectively apply
content filtering and reduce token usage costs. By using input
tags to mark only the user-provided content for filtering, you
can avoid unnecessary processing of system prompts, search
results, and conversation history while maintaining essential
safeguards.

**Desired outcome:** Enable more
efficient and cost-effective content filtering by processing
only the relevant portions of input that require guardrails
evaluation.

**Benefits of establishing this best
practice:**

- [Control
resource consumption parameters](https://docs.aws.amazon.com/wellarchitected/latest/framework/cost-dp.html) - By filtering only
selected content rather than entire prompts, you minimize the
number of tokens processed by content filters.
- [Optimize
model and inference selection](https://docs.aws.amazon.com/wellarchitected/latest/framework/cost-dp.html) - Selective filtering
reduces the volume of text evaluated, leading to faster response
times.

**Level of risk exposed if this best
practice is not established:** Medium

## Implementation guidance

By implementing selective content filtering through input
tags, you can significantly reduce token costs while
preserving the effectiveness of your content safeguards.
Please note that the input tags are not supported when using
ApplyGuardrail API, so you need to
implement content filtering on your application side to derive
the benefits of input tags.

- Review your application architecture to identify where
content filtering is needed.
- Determine which content sections require filtering or
trusted content.
- Implement input tagging following the Amazon Bedrock
documentation.
- Test filtering effectiveness and performance impact.
- Monitor costs and adjust tag usage to optimize spend while
maintaining safety.

### Implementation steps

- Use XML-style tags to mark specific sections of input
prompts for content filtering. Add tags using the
format:

```
`
[Content to be filtered]
`
```

Generate a unique random tag suffix (xyz)
for each request to reduce prompt injection attacks. Use
alphanumeric characters between 1-20 characters.

Include the tag suffix in the
guardrailConfig:

```
`{
"amazon-bedrock-guardrailConfig": {
"tagSuffix": "xyz"
}
}`
```

- Apply tags selectively to user queries and input,
current conversation turns, and new or unverified
content.
- Leave system prompts, verified search result, historical
conversation context, and other trusted content
untagged.
- Define a minimalist response scheme (for example,
0 for affirmative and
1 for rejection).
- Inform the model in the prompt of the requested model
response scheme, and ask the model to respond in kind.
- Set a hard limit on the response length by configuring
the response length hyperparameter accordingly.
- Continue testing and optimizing the model's response to
verify it satisfies the workload requirements. Monitor
and optimize your implementation by:

Tracking token usage with and without selective
filtering
- Measuring latency impact across different tag
configurations
- Verifying filtering effectiveness on tagged vs
untagged content
- Adjusting tag placement based on application needs

**Example implementation**

The following use cases are well-suited for input tagging:

- **RAG applications:**
Tag only user queries while leaving retrieved passages
unfiltered .
- **Chat applications:**
Tag new user messages while preserving conversation
history.
- **Content moderation:**
Tag user-generated content while allowing verified
content to pass through.
- **Document
processing:** Tag extracted text portions
needing review while trusting source material.

## Resources

**Related best practices:**

- [COST10-BP01](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_evaluate_new_services_review_process.html)

**Related videos:**

- [AWS re:Invent 2023 - Prompt Engineering Best Practices for LLMs on
Amazon Bedrock (AIM377)](https://www.youtube.com/watch?v=jlqgGkh1wzY)

**Related examples:**

- [Amazon
Bedrock Prompt Management is now Available in GA](https://aws.amazon.com/blogs/machine-learning/amazon-bedrock-prompt-management-is-now-available-in-ga/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/gencost03-bp04.html*

---
