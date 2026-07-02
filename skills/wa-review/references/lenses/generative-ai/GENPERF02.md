# GENPERF02 — Maintaining model performance

**Pillar**: Performance Efficiency  
**Best Practices**: 3

---

# GENPERF02-BP01 Load test model endpoints

Hosting architecture is a significant factor in determining the
performance efficiency of a foundation model. Load test model
endpoints to determine a baseline level of performance. Load
tests should evaluate foundation model performance under average
workload throughput, as well as extremes. Capturing a
comprehensive understanding of model endpoint performance under
a variety of workload demands helps improve architectural
decision-making in regard to performance efficiency and endpoint
selection.

**Desired outcome:** When
implemented, this best practice helps you identify the optimal
load of a foundation model endpoint. This baseline should be
used to inform monitoring and alerting at the upper-threshold of
acceptable performance limitations for your workload.

**Benefits of establishing this best
practice:**
[Experiment
more often](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel-dp.html) - Load testing model endpoints assists in the
ongoing performance of foundation models at scale.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Workloads have unique performance requirements, such as low
latency, rapid scalability, or intermittent demand scaling.
Methods for achieving clearly defined performance requirements
should be outlined in your organization's AI policy.
Generalize guidelines for implementing real-time or batch
inference, with clear processes defined for testing and
scaling workloads with exceptional performance demands.

One mechanism for implementing this is a test suite, designed
to simulate the heaviest expected load to an application
before anticipated performance degradation. Test models and
model endpoints against these requirements to determine if
additional architectural considerations are required to bridge
the gap between performance needs and observed performance
results. Consider using a ground truth data set to standardize
results across multiple models.

On Amazon Bedrock, review the published metrics for inference
latency and throughput before testing if they are available.
If these metrics are not available, benchmark the model
against a golden dataset provided by you or curated by a
third-party. The golden dataset should effectively test the
model for the task in question. Use the performance benchmarks
for that model to influence the model selection process. If a
model has throughput limitations, consider introducing
provisioned throughput capabilities or using cross-Region
inference endpoints. Identify the performance bottleneck and
architect accordingly.

On Amazon SageMaker AI, test inference endpoints with respect
to the inference endpoint instance type and size. Load test
inference endpoints as you might load test other
high-performance compute options. Depending on the model being
hosted, there may be an opportunity to modify inference
parameters to optimize performance or to use advanced model
customization techniques such as quantization or LoRa.
Research the inference options available to the model you are
hosting, and test the effect of different inference parameters
on your performance criteria.

For SageMaker AI hosted models, you can optimize memory, I/O,
and computation by selecting an appropriate serving stack and
instance type. SageMaker AI large model inference (LMI) deep
learning containers provide options for request batching,
quantization options, and support for the newest versions of
vLLM, a performance optimized library for LLM serving and
inference. You can use these capabilities to balance
performance with other workload metrics like complexity and
cost.

To improve performance bottlenecks on a foundation model,
consider optimizing the flow of prompts. Some low latency and
real-time application use cases with repeated prompts may
benefit from prompt caching using Amazon Bedrock prompt
caching. Prompt caching can improve the latency and
performance of model endpoints by reducing the load on those
endpoints for regularly submitted prompts. Instead of the
model servicing each prompt, a cached response is returned
instead, reducing the load on the foundation model.
Additionally, implementing streaming model responses can also
improve a user's perceived latency on responses not in the
cache.

Consider the usage requirements of some generative AI
workloads, batch inference may be a potent alternative to
traditional inference requests for model endpoints. Batch
inference is more efficient for processing large volumes of
prompts, especially when evaluating, experimenting, or
performing offline analysis on foundation models. You can use
this to aggregate responses and analyze them in batches. If
higher latency is acceptable in your scenario, batch inference
may be a better choice than real-time invoke model. Batch
processing by definition introduce additional latency compared
to real-time inference, so you should use it in scenarios
where load testing permits long-running job executions.

### Implementation steps

- Reference your organization's AI policy for information
concerning appropriate performance metrics for model
endpoint load testing.
- Develop a load testing harness that prompts a foundation
model at configurable rates. Consider incorporating the
ability test against internal golden datasets and
external third-party benchmarking data.
- Collect performance information from the model from the
load test, carefully evaluating where the bottleneck
exists. Bottlenecks in the model's ability to serve
inference requests may be addressed through model
customization techniques or increasing the size and
power of the inference endpoint. Bottlenecks inherited
from usage patterns may benefit from cross-Region
inference, prompt caching, or an entirely different
inference paradigm.

## Resources

**Related best practices:**

- [PERF05-BP04](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_process_culture_load_test.html)
- [MLPER-01](https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlper-01.html)
- [MLPER-03](https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlper-03.html)
- [MLPER-05](https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlper-05.html)
- [MLPER-07](https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlper-07.html)

**Related documents:**

- [Monitor
the health and performance of Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/monitoring.html)
- [Supercharge
your LLM performance with Amazon SageMaker AI Large Model
Inference container v15](https://aws.amazon.com/blogs/machine-learning/supercharge-your-llm-performance-with-amazon-sagemaker-large-model-inference-container-v15/)
- [Model
management for LoRA fine-tuned models using Llama2 and Amazon SageMaker AI](https://aws.amazon.com/blogs/machine-learning/model-management-for-lora-fine-tuned-models-using-llama2-and-amazon-sagemaker/)
- [Efficient
and cost-effective multi-tenant LoRA serving with Amazon SageMaker AI](https://aws.amazon.com/blogs/machine-learning/efficient-and-cost-effective-multi-tenant-lora-serving-with-amazon-sagemaker/)

**Related examples:**

- [Load
testing applications](https://docs.aws.amazon.com/prescriptive-guidance/latest/load-testing/welcome.html)
- [Deploy
models with DJL Serving](https://docs.aws.amazon.com/sagemaker/latest/dg/deploy-models-frameworks-djl-serving.html)
- [The
large model inference (LMI) container documentation](https://docs.aws.amazon.com/sagemaker/latest/dg/large-model-inference-container-docs.html)
- [Amazon Bedrock model evaluation is now generally available](https://aws.amazon.com/blogs/aws/amazon-bedrock-model-evaluation-is-now-generally-available/)
- [Best
practices for load testing Amazon SageMaker AI real-time
inference endpoints](https://aws.amazon.com/blogs/machine-learning/best-practices-for-load-testing-amazon-sagemaker-real-time-inference-endpoints/)

**Related tools:**

- [Bedrock
Latency Benchmarking](https://github.com/gilinachum/bedrock-latency)
- [vLLM](https://docs.vllm.ai/en/latest/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/genperf02-bp01.html*

---

# GENPERF02-BP02 Optimize inference parameters to improve response quality

Foundation model response quality can be affected by inference
hyperparameters. Optimize inference hyperparameters for your use
case to help maintain consistent response quality and to help control the
non-deterministic nature of foundation models.

**Desired outcome:** When
implemented, you can reduce the variability of foundation models by
setting hyperparameters and identifying optimum ranges and
values for a use case.

**Benefits of establishing this best
practice:** [Experiment
more often](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel-dp.html) - Optimize hyperparameters through experimentation
to discern the best range and values for a use case.

**Level of risk exposed if this best practice
is not established:** Low

## Implementation guidance

Workloads have unique requirements for response quality.
Response quality can be modified by configuring inference
parameters. Inference parameters vary from model to model. For
example, in text-based scenarios, the parameters
temperature, p, and
k are common.

Image, sound, and video models have other common
hyperparameters. Hyperparameter values and ranges can impact
the quality of a model's response, especially for different
task types. When determining the inference parameters required
for your workload, first identify the task for the model to
complete. Common tasks for textual responses include
summarization or question answering; image models may be asked
to generate or modify images. The task helps inform which
hyperparameters are most important in the context of your
workload.

Consider a structured approach to determining the best range
of values for a hyperparameter. An example is testing the
highest and lowest values for each hyperparameter and
comparing the results of each test to your golden data. The
configurations that generate responses most appropriate for
the ground truth prompt should be accepted and iterated on.
You might then adopt a Newtonian approach to finding the ideal
hyperparameter value by incrementing or decrementing a
hyperparameter by half to see the effect this has on the
model's response. Continue in this way until the affects of
the hyperparameter changes are negligible.

The *LLM-as-a-judge* pattern is a powerful
technique for automating the iterative nature of
hyperparameter tuning. The LLM-as-a-judge pattern uses a
separate LLM to evaluate the performance of a model in
generating a response which is appropriate for the given
prompt. This could be favorable for a large set of ground
truth prompts or in the case where you lack sufficient
resources to facilitate a full human-in-the-loop testing
process. Consider adopting such a robust process for
hyperparameter optimization in the case where workload
requirements change regularly.

Recommendations for task-specific hyperparameter ranges could
be incorporated into an internal development guide for AI
workloads. Consider identifying recommended hyperparameter
ranges broken out by task into your organization's AI policy,
clearly defining the process for changing these ranges.

### Implementation steps

- Identify the task required of the foundation model.
- Identify the ground truth data to use for optimizing
inference hyperparameters.
- Select the most important hyperparameters for the task.
- Use an optimization method to maximize response quality.
- Use these values or ranges to encourage consistent
high-performance of your applications.

## Resources

**Related best practices:**

- [PERF05-BP01](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_process_culture_establish_key_performance_indicators.html)
- [MLPER-03](https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlper-03.html)

**Related documents:**

- [Monitor
the health and performance of Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/monitoring.html)
- [Influence
response generation with inference parameters](https://docs.aws.amazon.com/bedrock/latest/userguide/inference-parameters.html)
- [Optimize
model inference for latency](https://docs.aws.amazon.com/bedrock/latest/userguide/latency-optimized-inference.html)

**Related examples:**

- [Load
testing applications](https://docs.aws.amazon.com/prescriptive-guidance/latest/load-testing/welcome.html)
- [Amazon Bedrock model evaluation is now generally available](https://aws.amazon.com/blogs/aws/amazon-bedrock-model-evaluation-is-now-generally-available/)
- [Best
practices for load testing Amazon SageMaker AI real-time
inference endpoints](https://aws.amazon.com/blogs/machine-learning/best-practices-for-load-testing-amazon-sagemaker-real-time-inference-endpoints/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/genperf02-bp02.html*

---

# GENPERF02-BP03 Select and customize the appropriate model for your use case

There are several industry-leading model providers, and each
offers different model families and sizes. When you select a
model, choose the appropriate model family and size for your use
case to provide consistent performance for your workload.

**Desired outcome:** When
implemented, this best practice helps you select the ideal model
for your use case. You understand the reasons a specific model
was chosen, and your chosen model provides robust performance
and consistency for your use case.

**Benefits of establishing this best
pracice:**

- [Experiment
more often](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel-dp.html) - Identify the best model for your use case,
developing a mechanism to update the appropriate model quickly.
- [Consider
mechanical sympathy](https://docs.aws.amazon.com/wellarchitected/latest/framework/perf-dp.html) - Not all foundation models are
created equal, and some have significant advantages over others.
Select the appropriate model for your use case by understanding
how models perform on different tasks.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

When selecting a model for a task, curate a suite of tests
sourced from your ground truth data set, and test model
performance against those prompt-response pairs. These tests
should emulate the specific task a model will be performing as
part of the use case, such as summarization or question
answering. Consider testing across model family or model size
to surface candidate models.

In addition to testing ground truth data, consider testing
challenging prompts or prompts created deliberately with
questionable or unconventional intent. Evaluate the model's
ability to respond to this class of prompts before finally
selecting a model. Consider using public benchmarks and
metrics to augment your ground truth data. Amazon Bedrock
Evaluations or the open-source fmeval library test foundation
models against open-source performance evaluation data sets
and return results in the form of metrics like accuracy or
toxicity scores.

Automate model selection using an intelligent model router.
Model routers, such as Amazon Bedrock's Prompt Routing
capability, are a powerful capability if your testing suite
yields inconclusive results within a model family. If a family
of models performs well against a prompt testing suite, but
different model sizes within that family show varied
performance with no clear leader, use a model router. Amazon
Bedrock model routers forward prompts to the best model based
on the prompt itself. This technique simplifies the model
selection process but may not be appropriate for all use
cases, especially for self-hosted models. For situations where
your workload is serviced primarily by self-hosted models,
carefully evaluate open-source prompt routing options or
develop your own.

In some scenarios, there may be room to improve a model which
outperforms alternatives through model customization. In these
scenarios, consider fine-tuning.
*Fine-tuning* is a technique that improves
a model's performance on a specific set of tasks, which
requires a small amount of labeled data. Ground truth
prompt-response data can be used to fine-tune a model.

Additionally, models can be domain adapted through continuous
pre-training. *Continuous pre-training*
requires more data than fine-tuning, but the result is a model
which is highly performant on a domain of knowledge or tasks.
These customization techniques require significant investment,
consider doing this after reducing the number of candidate
models through traditional model testing techniques.

*Model distillation* is another
customization option to consider. Distillation generates
synthetic data from a large foundation model (teacher) and
uses the synthetic data to fine-tune a smaller model (student)
for your specific use case. Model distillation helps preserve
performance and avoid scenarios where you might over-provision
a large model for a fine-tuned use case.

Track the dominant model family and size for each workload's
task. While your organization's AI usage policy may be too
broad, consider developing an AI usage document for each
workload to maintain a permanent understanding of your
organization's decisions around AI models for each workload.
As models continue to be developed with new capabilities,
reference this document to discern if it is appropriate to
re-test the current leading model for a workload.

### Implementation steps

- Define minimum performance and response quality
thresholds for your workload.
- Select a range of models from different model providers.
- Implement tests to facilitate rapid testing for each of
the models.
- Test each model against the ground truth data set, and
identify which models surpass the minimum performance
and response quality thresholds.
- Select the model which performs best on average for the
given use case.
- Consider elevating model performance situationally, and
use techniques like prompt routing or customization
where appropriate.
- Document results in an AI usage document to track model
usage and encourage data-driven decision-making within
the organization.

## Resources

**Related best practices:**

- [PERF02-BP01](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_compute_hardware_select_best_compute_options.html)
- [MLPER-06](https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlper-06.html)
- [MLPER-16](https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlper-16.html)

**Related documents:**

- [Understanding
intelligent prompt routing in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-routing.html)
- [Supported
foundation models in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/models-supported.html)
- [Optimize
model inference for latency](https://docs.aws.amazon.com/bedrock/latest/userguide/latency-optimized-inference.html)

**Related examples:**

- [Enhance
conversational AI with advanced routing techniques with Amazon
Bedrock](https://aws.amazon.com/blogs/machine-learning/enhance-conversational-ai-with-advanced-routing-techniques-with-amazon-bedrock/)
- [Multi-LLM
routing strategies for generative AI applications on
AWS](https://aws.amazon.com/blogs/machine-learning/multi-llm-routing-strategies-for-generative-ai-applications-on-aws/)
- [FMEval
Library](https://github.com/aws/fmeval)
- [Evaluate,
compare, and select the best foundation models for your use
case in Amazon Bedrock (preview)](https://aws.amazon.com/blogs/aws/evaluate-compare-and-select-the-best-foundation-models-for-your-use-case-in-amazon-bedrock-preview/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/genperf02-bp03.html*

---
