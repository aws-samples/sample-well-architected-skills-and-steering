# Cost Optimization

**Pillar**: Cost Optimization  
**Questions**: 5

---

# GENCOST01 — Model selection and cost optimization

**Pillar**: Cost Optimization  
**Best Practices**: 1

---

# GENCOST01-BP01 Right-size model selection to optimize inference costs

Foundation model costs vary greatly across the various foundation
model providers, model families and sizes, and model hosting
paradigms. It can be advantageous to use cost as a factor when
selecting models. Understand the models available to you, as well as
the requirements of your workload, to make an informed, cost-aware
decision.

**Desired outcome:** When
implemented, this best practice helps you manage spend on foundation
model inference without guessing at the capacity requirements for a
foundation model.

**Benefits of establishing this best
practice:** [Measure
overall efficiency](https://docs.aws.amazon.com/wellarchitected/latest/framework/cost-dp.html) - It is helpful to understand inference
and hosting costs associated with the performance requirements of
foundation model.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Foundation models have several cost-dimensions, some of which
change depending on the hosting paradigm (managed or self-hosted).
Traditionally, managed models charge for consumption measured in
token input and token output. Self-hosted models charge using
traditional infrastructure costs.

For managed models hosted on Amazon Bedrock, different models
charge differently for the number of tokens input and output.
Oftentimes, newer and larger models may have higher cost compared
to older or smaller models. Self-hosted models on Amazon EC2 or
Amazon SageMaker AI inference endpoints charge based on uptime, as
well as additional costs storage and network costs.

When optimizing for cost, consider testing with a smaller model
first, and gradually increase model size and capabilities until an
acceptable model is selected. The criteria for an acceptable model
will change based on the use case of the workload. By starting
with the smallest model, you improve the chances of selecting a
model with the most cost-effective token input and output cost.
Alternatively, optimize self-hosted model infrastructure based on the model used and the workload's usage pattern. Consult the model card or technical documentation for recommendations on instance size and capacity, right-sizing based on usage patterns.

Deploy multiple models to a single, multi-model endpoint where appropriate. Right-size as an ongoing activity. As newer models become
available, the workload needs change, and as prompting and
orchestration are refined, smaller, more cost-effective models
should be evaluated against your workload's needs to continually
optimize.

Consider decomposing your workload and routing to
different sized models based on the specific needs of each
inference request. Route less complicated inferences to smaller,
more cost-effective models while assessing quality to maintain
high quality across variably complicated inference requests. For
managed models hosted on Amazon Bedrock, consider intelligent
prompt routing for dynamic routing between models in the same
model family. Alternatively, weight the benefits of developing a
custom prompt routing layer. In some cases, real-time inference may not be required. In those instances, elect for a less expensive inference paradigm such as batch inference.

### Implementation steps

- Identify the minimum performance requirements for a
foundation model.
- Determine the models available which meet that minimum
performance bar.
- Select the most cost-efficient model based on the
prioritized cost dimensions (like hosting paradigm, model
size, or token cost).
- Continuously evaluate model selection to validate the
highest performance is being achieved at the lowest possible
price-point.

## Resources

**Related best practices:**

- [COST01-BP02](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_cloud_financial_management_partnership.html)
- [COST05-BP01](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_select_service_requirements.html)
- [COST06-BP01](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_type_size_number_resources_cost_modeling.html)
- [COST07-BP03](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_pricing_model_third_party.html)
- [COST09-BP01](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_manage_demand_resources_cost_analysis.html)

**Related documents:**

- [Tagging
Amazon Bedrock resources](https://docs.aws.amazon.com/bedrock/latest/userguide/tagging.html)

**Related examples:**

- [Track,
allocate and manage your generative AI cost and usage with
Amazon Bedrock](https://aws.amazon.com/blogs/machine-learning/track-allocate-and-manage-your-generative-ai-cost-and-usage-with-amazon-bedrock/)
- [Optimizing
costs of generative AI applications on AWS](https://aws.amazon.com/blogs/machine-learning/optimizing-costs-of-generative-ai-applications-on-aws/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/gencost01-bp01.html*

---

# GENCOST02 — Generative AI pricing model

**Pillar**: Cost Optimization  
**Best Practices**: 2

---

# GENCOST02-BP01 Balance cost and performance when selecting inference paradigms

Hosting a foundation model for inference requires many choices, and
many of these decisions can affect the cost of your workload. One of
these choices includes the selection of a managed, serverless
deployment of a foundation model against a self-hosted option.

**Desired outcome:** When
implemented, this best practice describes a relationship between
cost and performance contextualized against model hosting and
inference paradigms. This relationship helps you evaluate
cost-benefit choices associated with the selection of an inference
paradigm.

**Benefits of establishing this best
practice:**

- [Measure
overall efficiency](https://docs.aws.amazon.com/wellarchitected/latest/framework/cost-dp.html) - It is helpful to understand
inference and hosting costs associated with the performance
requirements of foundation model.
- [Lower
spend on undifferentiated heavy lifting](https://docs.aws.amazon.com/wellarchitected/latest/framework/cost-dp.html) - More often than
not, it is beneficial to opt for a managed or serverless hosting
paradigm, due to the intractability of the total cost of
ownership for foundation model hosting.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Throughput sensitive workloads often require additional resources
to service inference requests at the rate they are being
submitted. Provisioned throughput, available through Amazon Bedrock, provides increased throughput capability for large
language models supporting generative AI workloads. If your
workload requires provisioned throughput to meet its performance
requirements, consider preferring longer commitment terms for
better unit costs. Validate your scaling requirements with shorter
duration commitments to avoid over-provisioning your workload.
Provisioned throughput is available for purchase in Amazon Bedrock. If the model you are using has throughput performance
needs or continuous model inference scale supports provisioned
throughput, consider purchasing a short-term. Test the improvement
and determine if the provisioned throughput improves your
application's performance. If there is a strong case for
provisioned throughput, consider purchasing a six-month plan, as
the unit cost for six months is usually lower than purchasing
month-over-month.

Consider a scenario where you want to serve inference capabilities for a single model for small, periodic workloads. Evaluate the cost of hosting this model on an Amazon SageMaker AI inference endpoint. Compare these costs against the cost of importing the model to Amazon Bedrock using Amazon Bedrock's Custom Model Import feature and using API-based inference. Evaluate the cost to deploy this model using either paradigm and compare them with respect to the total cost of ownership. Where performance trade-offs are negligible, deploy to the most cost-effective inference paradigm.

### Implementation steps

- Identify the nature of the demand for this workload.
- Compare the demand to the available hosting options, and
remove the high-cost options that do not satisfy the
workloads hosting requirements.
- Select and test the available optinos that satisfy the workload requirements for latency, throughput, and response quality.
- Implement the most appropriate, lower-cost hosting option for your model serving paradigm (for example, managed or self-hosted).

## Resources

**Related best practices:**

- [COST06-BP01](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_type_size_number_resources_cost_modeling.html)
- [COST06-BP02](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_type_size_number_resources_data.html)
- [COST09-BP01](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_manage_demand_resources_cost_analysis.html)

**Related documents:**

- [Tagging
Amazon Bedrock resources](https://docs.aws.amazon.com/bedrock/latest/userguide/tagging.html)
- [Inference
cost optimization best practices](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-cost-optimization.html)

**Related examples:**

- [Track,
allocate and manage your generative AI cost and usage with
Amazon Bedrock](https://aws.amazon.com/blogs/machine-learning/track-allocate-and-manage-your-generative-ai-cost-and-usage-with-amazon-bedrock/)
- [Optimizing
costs of generative AI applications on AWS](https://aws.amazon.com/blogs/machine-learning/optimizing-costs-of-generative-ai-applications-on-aws/)
- [Analyze
Amazon SageMaker AI spend and determine cost optimization
opportunities based on usage, Part 1](https://aws.amazon.com/blogs/machine-learning/part-1-analyze-amazon-sagemaker-spend-and-determine-cost-optimization-opportunities-based-on-usage-part-1/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/gencost02-bp01.html*

---

# GENCOST02-BP02 Optimize resource consumption to minimize hosting costs

Hosting a foundation model for inference requires myriad choices,
all of which affect cost. These cost dimensions can be optimized to
reduce cost while meeting performance goals.

**Desired outcome:** When
implemented, this best practice describes a relationship between
cost and performance contextualized in self-hosted foundation model
hosting.

**Benefits of establishing this best
practice:**

- [Measure
overall efficiency](https://docs.aws.amazon.com/wellarchitected/latest/framework/cost-dp.html) - It is helpful to understand
inference and hosting costs associated with the performance
requirements of foundation model.
- [Stop
spending money on undifferentiated heavy lifting](https://docs.aws.amazon.com/wellarchitected/latest/framework/cost-dp.html) - More
often than not, it is beneficial to opt for a managed or
serverless hosting paradigm, due to the intractability of the
total cost of ownership for foundation model hosting.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Self-hosted model infrastructure should be optimized based on the
model used and the workload's usage pattern. Customers
self-hosting models should also consider optimizing the model's
hosting infrastructure. Consider right-sizing the inference
endpoint to the smallest instance available that allows you to
meet performance goals. In some scenarios, it may be appropriate
to shut down the hosting instance and restart it during relevant
hours. This is particularly useful for workloads with predictable
usage patterns. You may also consider purchasing [Amazon EC2 Reserved
Instances](https://aws.amazon.com/ec2/pricing/reserved-instances/) or Savings Plans to further reduce the cost of a hosted
model endpoint. Before committing to compute reservation, consider
Amazon SageMaker AI Inference Recommender to evaluate if you are
using the ideal inference endpoint type, generation, and size.

In SageMaker AI HyperPod with both Amazon EKS and Slurm
orchestration, use the system's advanced task governance
capabilities and flexible training plans to dynamically
allocate compute resources based on priority and demand,
reducing costs through improved utilization.

For EKS-based HyperPod, implement the managed Kubernetes
orchestration with Hyperpod Task Governance. Configure
automated scaling policies, priority classes, and node
selectors to verify that your production workloads use
cost-effective committed capacity while development tasks use
On-Demand or Spot Instances when appropriate. Use the usage
reporting feature to provide granular visibility into GPU,
CPU, and Neuron Core consumption at both team and task levels,
enabling transparent cost attribution and reducing guesswork
in resource allocation.

For Slurm-based HyperPod, use Slurm's native job scheduling
and resource management features combined with HyperPod's
auto-resume functionality to minimize wasted compute cycles
during hardware failures, potentially reducing total training
time in large clusters. Both systems benefit from implementing
right-sizing strategies through SageMaker AI HyperPod Recipes
that provide pre-configured, benchmarked training stacks
optimized for specific model architectures like Llama and
Mistral, providing optimized performance while minimizing
resource waste.

Additionally, establish flexible training plans that can set
timeline and budget constraints, and allow HyperPod to
automatically find the best combination of capacity blocks and
create cost-optimized execution plans that avoid overspending
by overprovisioning servers for training jobs.

Inference workloads can be optimized using advanced techniques
such as quantization or LoRA adaptation. These advanced
capabilities are available for certain models in Amazon
Bedrock or on self-hosted models on Amazon SageMaker AI. These
advanced inference techniques can further optimize resource
consumption for inference, thus reducing hosting and inference
serving costs.

### Implementation steps

- Identify the nature of the demand for this workload.
- Deploy selected foundation model on acceptable
infrastructure, even if it may be over-provisioned.
- Establish an inference or demand profile for the hosted
workload.
- Optimize the hosting infrastructure in accordance with the
workload's demands, and select the most cost optimized
infrastructure that meets performance requirements.

## Resources

**Related best practices:**

- [COST06-BP01](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_type_size_number_resources_cost_modeling.html)
- [COST06-BP02](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_type_size_number_resources_data.html)
- [COST09-BP01](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_manage_demand_resources_cost_analysis.html)

**Related videos and documents:**

- [Tagging
Amazon Bedrock resources](https://docs.aws.amazon.com/bedrock/latest/userguide/tagging.html)
- [Inference
cost optimization best practices](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-cost-optimization.html)
- [Get
Started with Amazon SageMaker AI HyperPod Flexible Training
Plans](https://www.youtube.com/watch?v=Itcw8zhdArY)

**Related examples:**

- [Easily
deploy and manage hundreds of LoRA adapters with SageMaker AI
efficient multi-adapter inference](https://aws.amazon.com/blogs/machine-learning/easily-deploy-and-manage-hundreds-of-lora-adapters-with-sagemaker-efficient-multi-adapter-inference/)
- [Track,
allocate and manage your generative AI cost and usage with
Amazon Bedrock](https://aws.amazon.com/blogs/machine-learning/track-allocate-and-manage-your-generative-ai-cost-and-usage-with-amazon-bedrock/)
- [Optimizing
costs of generative AI applications on AWS](https://aws.amazon.com/blogs/machine-learning/optimizing-costs-of-generative-ai-applications-on-aws/)
- [SageMaker AI
Inference Recommender for HuggingFace BERT Sentiment
Analysis](https://github.com/aws/amazon-sagemaker-examples/blob/main/sagemaker-inference-recommender/huggingface-inference-recommender/huggingface-inference-recommender.ipynb)
- [Analyze
Amazon SageMaker AI spend and determine cost optimization
opportunities based on usage, Part 1](https://aws.amazon.com/blogs/machine-learning/part-1-analyze-amazon-sagemaker-spend-and-determine-cost-optimization-opportunities-based-on-usage-part-1/)
- [Maximize
Accelerator Utilization for Model Development with New Amazon SageMaker AI HyperPod Task Governance](https://aws.amazon.com/blogs/aws/maximize-accelerator-utilization-for-model-development-with-new-amazon-sagemaker-hyperpod-task-governance/)
- [Introducing
Amazon SageMaker AI HyperPod to train foundation models at
scale](https://aws.amazon.com/blogs/machine-learning/introducing-amazon-sagemaker-hyperpod-to-train-foundation-models-at-scale/)
- [Best
practices for Amazon SageMaker AI HyperPod task governance](https://aws.amazon.com/blogs/machine-learning/best-practices-for-amazon-sagemaker-hyperpod-task-governance/)
- [Get
started with Amazon SageMaker AI HyperPod task governance](https://www.youtube.com/watch?v=_wDhBAPwhoM)
- [Usage
reporting for cost attribution in SageMaker AI HyperPod](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-usage-reporting.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/gencost02-bp02.html*

---

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

# GENCOST04 — Cost-informed vector stores

**Pillar**: Cost Optimization  
**Best Practices**: 1

---

# GENCOST04-BP01 Reduce vector length on embedded tokens

Using a smaller vector size for data embeddings results in a reduced
response length for data-driven generative AI workflows. By keeping
vector lengths small, we can save on model output as well as vector
database computation requirements.

**Desired outcome:** A reduced total
cost of ownership for embeddings and data-driven generative AI
workflows.

**Benefits of establishing this best
practice:**

- [Measure
overall efficiency](https://docs.aws.amazon.com/wellarchitected/latest/framework/cost-dp.html) - Vector stores introduce a new
component for cost optimization into a generative AI
application. By increasing the efficiency of a vector store, you
also optimize the cost of running your application.
- [Analyze
and attribute expenditure](https://docs.aws.amazon.com/wellarchitected/latest/framework/cost-dp.html) - Reducing vector length can
help to lower the costs attributed to a vector store.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Consider using a smaller vector when embedding documents into a
vector store. The vector size hyperparameter specifies the size of
the resulting vector when embedding unstructured data. A smaller
resulting vector implies the embedding model will generate fewer
tokens on output, thus resulting in a reduced cost to embed
documents. This approach may result in less performant data
retrieval, so using a smaller vector should be done deliberately
with the cost-performance trade-off in mind.

Alternatively, some embedding models feature compressed vector
types. Compressed vector types are smaller than uncompressed
vectors, further reducing the cost of inference for search and
embedding tasks. Consider this element when selecting an embedding
model, as not all embedding models support compressed vectors.

### Implementation steps

- Identify the smallest vector length supported by the
selected embedding foundation model.
- Embed data using the smallest vector length.

You may have to modify the chunk size of the document or
introduce overlapping chunks to maintain high relevance
on output.

- Perform latency and load testing on your data retrieval workloads to verify that model response quality is still sufficient.
- Re-test with increased vector size or modified document chunking strategy to improve model response quality.

In some cases, changing the search algorithm may improve model response quality as well.

## Resources

**Related best practices:**

- [COST08-BP01](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_data_transfer_modeling.html)
- [COST08-BP02](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_data_transfer_optimized_components.html)
- [COST08-BP03](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_data_transfer_implement_services.html)

**Related documents:**

- [AWS re:Invent 2023
- Prompt Engineering Best Practices for LLMs on Amazon Bedrock
(AIM377)](https://www.youtube.com/watch?v=jlqgGkh1wzY)

**Related examples:**

- [Amazon Bedrock Prompt Management is now Available in GA](https://aws.amazon.com/blogs/machine-learning/amazon-bedrock-prompt-management-is-now-available-in-ga/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/gencost04-bp01.html*

---

# GENCOST05 — Cost-informed agents

**Pillar**: Cost Optimization  
**Best Practices**: 1

---

# GENCOST05-BP01 Create stopping conditions to control long-running workflows

Agentic workflows can be long-running, which can incur additional cost
to your application. Develop controls to limit agents from running
for extended periods of time without stopping.

**Desired outcome:** Maximum costs
for an agent's runtime can be predicted based on the implemented
stopping conditions.

**Benefits of establishing this best
practice:**
[Measure
overall efficiency](https://docs.aws.amazon.com/wellarchitected/latest/framework/cost-dp.html) - Agentic workflows can be long-running, which can add additional cost to your workload. By establishing stopping conditions for long-running agentic workflows, you can optimize resources, improve user experience, and optimize workload costs.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

For generative AI prompt flows where you lack control over the
duration of the workflow, consider introducing a time-out
mechanism or regaining control over the flow. This scenario is
particularly common within agentic architectures. Agent
architectures assist customers by taking on additional tasks.
Sometimes these tasks can run for an extended duration, which may
incur additional cost considerations, especially when they call
external resources. Consider introducing a timeout over the agent
to limit long-running processes from incurring costs
unnecessarily. Additionally, evaluate asynchronous workflows
orchestrated through events. Asynchronous workflows create
opportunities to interrupt or halt long-running events after an
extended duration. Consider the entire architecture before
determining the best place to interrupt long-running workflows for
cost savings.

### Implementation steps

- Estimate the maximum time needed for an agent to complete
its runtime.

Include model response times, tool execution times, and network latency in the estimation.

- Implement stopping conditions that enable an agent to run to
the maximum duration.

Stopping conditions may be a timeout mechanism like the
one in Amazon Bedrock.
- Alternatively, stopping conditions may be implemented in
the prompt flow layer or within a software abstraction
layer.

- Re-architect your workflows to facilitate stopping conditions.

Set timeouts on external tools such as Lambda functions or API endpoints, verify that your prompts understand how to handle timeout responses.
- Set token limits on model responses to simulate timeout functionality by stopping models from printing long-running responses.

## Resources

**Related best practices:**

- [COST01-BP06](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/cost_cloud_financial_management_proactive_process.html)

**Related documents:**

- [AWS re:Invent 2023
- Simplify generative AI app development with Agents for
Amazon Bedrock (AIM353)](https://www.youtube.com/watch?v=JNZPW82uv7w)
- [User
Guide: Amazon Bedrock Agents](https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html)

**Related examples:**

- [Best
practices for building robust generative AI applications with
Amazon Bedrock Agents - Part 1](https://aws.amazon.com/blogs/machine-learning/best-practices-for-building-robust-generative-ai-applications-with-amazon-bedrock-agents-part-1/)
- [Best
practices for building robust generative AI applications with
Amazon Bedrock Agents - Part 2](https://aws.amazon.com/blogs/machine-learning/best-practices-for-building-robust-generative-ai-applications-with-amazon-bedrock-agents-part-2/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/gencost05-bp01.html*

---

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
