# Performance Efficiency

**Pillar**: Performance Efficiency  
**Questions**: 4

---

# GENPERF01 — Establish performance evaluation processes

**Pillar**: Performance Efficiency  
**Best Practices**: 2

---

# GENPERF01-BP01 Define a ground truth data set of prompts and responses

*Ground truth data* facilitates model testing
for use case specific scenarios and should be developed and
curated for generative AI workloads. Ground truth data is a
curated set of prompts and responses that describe the ideal
workflow with a model.

**Desired outcome:** When
implemented, this best practice enables the measurement of a
model's performance for a set of tasks, accelerating model
evaluation and enabling model customization workflows.

**Benefits of establishing this best
practice:**
[Experiment
more often](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel-dp.html) - Ground truth testing facilitates rapid
experimentation and customization for models on tasks specific
to your workload's unique requirements.

**Level of risk exposed if this best
practice is not established:** Medium

## Implementation guidance

*Ground truth data*, also known as a
*golden dataset*, is data considered to be
of the highest quality in regard to a specific use case.
Ground truth data for generative AI workloads are oftentimes
prompt-response pairs. For a simple workflow, a golden dataset
might be dozens, hundreds, thousands or more sample prompts
and their corresponding expected responses. There may be
several prompts containing variations of the same ask, with
several responses describing variations of an acceptable
response. More complex workflows like retrieval augmented
generation or agentic workflows may require variations on this
paradigm.

Ground truth data is vital for the efficient testing of
data-driven and generative AI workloads. Develop ground truth
data for your generative AI applications to facilitate the
rigorous and uniform testing of large language models. When
equipped with a ground truth dataset for a use case, you can
automate the testing and evaluation of models. New models can
quickly be evaluated to determine if their performance for a
specific use case meets the current model's high bar.

Ground truth prompts should be clear and succinct, grouped
together by variations of the same ask. Ground truth responses
should similarly be clear and succinct, covering a range of
acceptable responses. When developing a ground truth data set,
don't be overly concerned with slight differences in prompts
that essentially ask a model to perform the same task. Prompts
in the ground truth data set should be specific to the kinds
of tasks you expect a model to solve. Consider ground truth
data as a living artifact, one that changes and extends based
on the use cases being tested and the usage paradigms being
implemented.

Prompt-responses pairs are the core of a ground truth dataset,
but ground truth data needs additional meta-data to be viable
for the extent of generative AI usage paradigms that could be
tested. For example, agent workflows perform tasks on behalf
of a requester, using its judgment to discern how to interpret
a response from an external system. An agent workflow may
synthesize several intermediary responses before the language
model delivers a final response to the user. Ground truth data
should be able to capture an ideal prompt flow, tracing the
workflow of the agent through various systems. This same
practice could be applied to workflows interacting with
multiple models.

Develop ground truth data in accordance with your
organization's AI policy. For example, if your organization's
AI policy prohibits testing models against production data,
your golden dataset should contain references to data which is
functionally equivalent to production data. Develop mock data
sets for testing, and mock endpoints for testing agentic
flows. The golden dataset should contain the instructions
required for a testing harness to run tests autonomously
against any model endpoint available, including self-hosted
language models.

In addition to facilitating rapid model testing and
evaluation, golden datasets can be used to quickly fine-tune
models or distill student models from teacher models. Model
customization workflows require high-quality data for
customization. Maintaining a robust golden dataset for each
use case can accelerate your ability to customize models.

### Implementation steps

- Define a series of prompts and their expected responses.

Consider using Amazon SageMaker Ground Truth or similar
to scale the curation of this dataset.
- Enrich prompt-response pairs with relevant meta-data in
accordance with your organization's AI policy.

- Store the data in a way which facilitates a
dictionary-style lookup of the data.

The first several layers could be organizational,
referring to abstractions like language, business
domain, or use case.
- The last layer includes the prompt-response pairs, where
the prompt is the key and the expected response is the
value.
- Store the data in an object-store such as Amazon S3.

- Create a data dictionary to facilitate access to the
ground truth data.

Crawl the object-store using an AWS Glue Crawler to
build the data dictionary.

- Develop a testing harness that can automatically test
models as they are made available using the ground truth
data.

Query segments of the ground-truth dataset using a
federated query solution such as Amazon Athena.
- Incorporate mock production data and tooling for more
advanced workflows such as agents or RAG.

- Define test scenarios corresponding to your golden
dataset and adhere to your organization's AI policy.

Define metrics to test models against as may be required
by your organization's AI policy.
- Track model performance across various tests and
metrics, carefully evaluating the trade-offs across
models.

## Resources

**Related best practices:**

- [PERF05-BP01](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_process_culture_establish_key_performance_indicators.html)
- [PERF05-BP03](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_process_culture_workload_performance.html)
- [MLPER03](https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlper-03.html)
- [MLPER04](https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlper-04.html)
- [MLPER16](https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlper-16.html)

**Related documents:**

- [Understand
options for evaluating large language models with SageMaker AI
Clarify](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-foundation-model-evaluate.html)
- [Customize
your model to improve its performance for your use case](https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models.html)
- [Amazon SageMaker AI JumpStart Foundation Models](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-foundation-models.html)
- [Automate
data labeling](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-automated-labeling.html)

**Related examples:**

- [Customize
models in Amazon Bedrock with your own data using fine-tuning
and continued pre-training](https://aws.amazon.com/blogs/aws/customize-models-in-amazon-bedrock-with-your-own-data-using-fine-tuning-and-continued-pre-training/)
- [High-quality
human feedback for your generative AI applications from Amazon SageMaker Ground Truth Plus](https://aws.amazon.com/blogs/machine-learning/high-quality-human-feedback-for-your-generative-ai-applications-from-amazon-sagemaker-ground-truth-plus/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/genperf01-bp01.html*

---

# GENPERF01-BP02 Collect performance metrics from generative AI workloads

Foundation model performance on specific tasks is measured and
quantified in different ways depending on the desired outcome.
It is important to discern the performance of a model over time
when selecting foundation models for generative AI workloads by
identifying performance metrics and evaluating model
performance. This is true not just for model inference, but
model training and customization workloads as well.

**Desired outcome:** When
implemented, your organization improves its ability to evaluate
model performance against the identified performance metric.

**Benefits of establishing this best
practice:**
[Experiment
more often](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel-dp.html) - Testing model performance using quantifiable
evaluation metrics assists in the selection of foundation models
for generative AI workloads.

**Level of risk exposed if this best
practice is not established:** Medium

## Implementation guidance

Traditional performance monitoring and optimization focus on
the efficiency of compute, network, memory and storage
resources. Generative AI workloads add new dimensions to the
performance considerations, particularly concerning response
quality. Inaccurate model responses or models responding in an
overly casual, dismissive, or even toxic manner may be
considered under-performing. Consult your organization's AI
policy for more details on what constitutes an
under-performing language model with respect to your use case.

Different use cases may have several relevant metrics for use
in evaluating model performance. Performance metrics for
inference workloads may capture model response latency or
throughput. Performance metrics for model customization or
training workloads are likely focused on model training times.
Ultimately, a model should respond with accurately, robustly,
and somewhat predictably. Capturing model performance against
these metrics and evaluating model performance against your
organization's AI performance requirements helps to provide
consistently high performing generative AI workloads.

Generative AI tasks should report metrics, telemetry and logs
to a centralized logging and monitoring solution such as
Amazon CloudWatch. By configuring Amazon CloudWatch or
similar, customers can collect performance metrics from model
endpoints hosted in Amazon SageMaker AI or generative AI
services like Amazon Q for Amazon Bedrock. These metrics can
be used to identify which models perform well against a
metric, and which need additional performance improvements.

Performance metrics may also be collected by applications and
services that interact with models. Collect metrics and
application traces pertaining to the flow of information
rather than a specific piece of the workflow. Work to
determine how your entire application performs when
interacting with generative AI solutions. This can help you
triage performance concerns faster and improve resolution
times.

Use internal golden datasets or external benchmarking datasets
to evaluate model performance on specific tasks. Consult model
cards to identify model strengths and weaknesses, evaluating
on selected datasets where appropriate. Benchmark custom
models on a suite of tests using internal and external data to
develop a well-rounded understanding of your model's
performance.

Note that a model may not excel at all tasks. Be judicious
when selecting a performance metric for your model, and
consult your organization's AI policy to identify which
performance metric to prioritize for your use case.

### Implementation steps

- Identify the performance metrics to prioritize for your
generative AI use case.
- Develop a mechanism to capture the performance metrics.

- Implement a trace framework like
[OpenLLMetry](https://github.com/traceloop/openllmetry)
to capture additional metrics.
- Capture metrics using Amazon CloudWatch or a similar
centralized logging and monitoring solution.
- Use a benchmarking dataset within an evaluation
framework such as
[fmeval](https://github.com/aws/fmeval).

- Establish reasonable performance thresholds and alert
accordingly.

- Use Amazon CloudWatch alarms for production alerting on
latency, throughput, or other traditional performance
metrics.
- Incorporate regular benchmarking using internal golden
datasets, and update the dataset as your customer's
usage changes.
- Consult model cards for new models, and perform custom
benchmarking of new models where appropriate.

- Identify, capture, and log remediation actions in your
organization's AI policy.

- For example, increased latency on self-hosted models may
call for horizontal scaling to remediate the issue. Your
organization's AI policy should define acceptable
latency thresholds.
- For example, a model response which is identified as a
hallucination may call for updates to a system prompt.
Such an update should require testing against internal
golden datasets to verify that system prompt changes do
not adversely affect related prompt workflows.

- Implement a centralized experiment tracking solution
such as Amazon SageMaker AI with MLflow.

## Resources

**Related best practices:**

- [PERF05-BP01](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_process_culture_establish_key_performance_indicators.html)
- [PERF05-BP02](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_process_culture_use_monitoring_solutions.html)
- [PERF05-BP03](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_process_culture_workload_performance.html)
- [PERF05-BP05](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_process_culture_automation_remediate_issues.html)
- [MLPER-03](https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlper-03.html)
- [MLPER-06](https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlper-06.html)
- [MLPER-07](https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlper-07.html)
- [MLPER-09](https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlper-09.html)
- [MLPER-15](https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlper-15.html)
- [MLPER-16](https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlper-16.html)

**Related documents:**

- [Monitor
the health and performance of Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/monitoring.html)
- [Customize
your workflow using the fmeval library](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-foundation-model-evaluate-auto-lib-custom.html)
- [Machine
learning experiments using Amazon SageMaker AI with
MLflow](https://docs.aws.amazon.com/sagemaker/latest/dg/mlflow.html)

**Related examples:**

- [Track
LLM model evaluation using Amazon SageMaker AI managed MLFlow and
FMEval](https://aws.amazon.com/blogs/machine-learning/track-llm-model-evaluation-using-amazon-sagemaker-managed-mlflow-and-fmeval/)
- [Evaluate
large language models for quality and responsibility](https://aws.amazon.com/blogs/machine-learning/evaluate-large-language-models-for-quality-and-responsibility/)
- [Monitoring
Generative AI application using Amazon Bedrock and Amazon CloudWatch integration](https://aws.amazon.com/blogs/mt/monitoring-generative-ai-applications-using-amazon-bedrock-and-amazon-cloudwatch-integration/)

**Related tools:**

- [Traceloop
OpenLLMetry](https://github.com/traceloop/openllmetry)
- [AWS fmeval
Model Evaluation Library](https://github.com/aws/fmeval)
- [AWS Samples fm-evaluation-at-scale](https://github.com/aws-samples/fm-evaluation-at-scale)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/genperf01-bp02.html*

---

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

# GENPERF03 — Optimize consumption of high-performance compute

**Pillar**: Performance Efficiency  
**Best Practices**: 1

---

# GENPERF03-BP01 Use managed solutions for model hosting, customization, and data access where appropriate

There are several industry-leading model providers, with new
model families, sizes, and capabilities being introduced
regularly. As foundation model capabilities expand, additional
operational requirements are required for hosting the models,
serving inference, and providing models access to data sources
and external systems. Alleviate operational burden on your
generative AI workload by using managed solutions where
appropriate.

**Desired outcome:** When
implemented, this best practice facilitates model hosting and
customization for highly performant generative AI workloads.

**Benefits of establishing this best
practice:**
[Use
serverless architectures](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel-dp.html) - Serverless architectures
enhance the performance of infrastructure-bound workloads,
without the operational overhead.

**Level of risk exposed if this best
practice is not established:** Medium

## Implementation guidance

Amazon Bedrock is the primary method for managed model hosting
on AWS. Customers select from a variety of models from
industry-leading model families, using their selected model
through an API. You can use Bedrock's
[Custom
Model Import](https://aws.amazon.com/bedrock/custom-model-import/) capability to host your own models within
Bedrock's hosting layer. These options help you host
foundation models using managed hosting options.

If you prefer more control than Amazon Bedrock, but less
operational overhead than native Amazon EC2, you can host on
managed model endpoints using Amazon SageMaker AI's model
endpoints. Hosting on Amazon SageMaker AI managed model
endpoints provides more flexibility than Bedrock's fully
managed hosting and less operational overhead than a
completely self-managed hosting solution.

These principles similarly apply to model customization
workloads as well. Amazon Bedrock offers fully managed model
customization workloads for foundation models, including
continuous pre-training, fine-tuning, and distillation. Use
these managed model customization workflows to reap the
benefits of model customization without having to manage these
complex workflows yourself.

More advanced model customization workflows can be run on
managed model endpoints within Amazon SageMaker AI as well.
You maintain more control over these endpoints, enabling
advanced model customization at inference time, such as LoRA,
all without increasing the operational burden on your
endpoint.

When you want to build your own proprietary foundation models
using your own data, you can do so using AWS compute
infrastructure. The operational overhead required to manage a
fleet of EC2 instances performing distributed training over
long-periods of time can distract engineering teams from the
primary goal of creating a foundation model.

Consider managed alternatives such as
[Amazon SageMaker AI HyperPod](https://aws.amazon.com/sagemaker-ai/hyperpod/), which you can use for managed
infrastructure for long-running foundation model training
workloads. This simplifies the model training process and
helps your customers deliver foundation models using managed
infrastructure.

Foundation models often require customization to suit your
domain. The recommended approach to initially adapt a domain
is through prompt engineering without altering model weights.
You can use RAG, which augments the model's outputs with
relevant information grounded from supplied domain specific
sources. Where these options are not sufficient, consider
customizing models using managed model customization
workflows.

You can bring open-source models from model hubs like
HuggingFace to your AWS environment through
[Amazon SageMaker AI JumpStart](https://aws.amazon.com/sagemaker-ai/jumpstart/). Models imported from services
like HuggingFace are hosted on Amazon SageMaker AI Inference
Endpoints. Then, you can manage the underlying infrastructure
manually. Manual infrastructure hosting requires owners to
manage endpoints and preserve the model's performance for the
duration of the model's usefulness.

Instead of manually optimizing model infrastructure and
uptime, consider importing the model to a managed model
hosting service like Amazon Bedrock using Amazon Bedrock
Custom Model Import. This capability automates the performance
management and maintenance of hosted models in your AWS
environment, reducing the undifferentiated heavy lifting of
model hosting.

Consider using managed data integrations for generative AI
workloads such as retrieval-augmented generation or generative
business intelligence. A federated data access layer helps
facilitate the scaling of your data-driven generative AI
workloads. Consult your organization's AI usage or data
governance policy to provide your generative AI workflows
appropriate access to data.

When using Amazon SageMaker AI HyperPod with both Amazon EKS and
Slurm orchestration, use the system's built-in managed
capabilities to optimize high-performance compute resources
and reduce operational overhead during model development
workflows.

For Amazon EKS-based HyperPod, use the managed Kubernetes
orchestration with automated scaling, deep health checks, and
resiliency features that automatically detect and replace
faulty nodes. Configure containerized workloads using the
SageMaker AI HyperPod recipes that provide pre-configured
training stacks with built-in support for model parallelism,
automated distributed checkpointing, and optimized performance
on NVIDIA H100, A100, and AWS Trainium accelerators. Implement
task governance capabilities that automatically manage task
queues and prioritize critical training jobs while efficiently
allocating compute resources.

For Slurm-based HyperPod, take advantage of the managed
cluster provisioning and lifecycle configuration support that
customizes computing environments with Amazon SageMaker AI
distributed training libraries for optimal performance. Both
systems benefit from the managed resiliency infrastructure
that monitors cluster instances, automatically detects
hardware failures, and replaces faulty components with minimal
downtime—reducing total training time by up to 32% in large
clusters.

Additionally, integrate with the new observability
capabilities through Amazon Managed Grafana and Prometheus for
unified monitoring dashboards that reduce troubleshooting time
from days to minutes, which helps your training workloads
achieve peak performance while minimizing operational
complexity.

### Implementation steps

- Determine the level of control your team needs to exert
over the hosting solution.
- For fully managed hosting workload, use API-based
hosting solutions such as Amazon Bedrock.
- For managed hosting with more control over the endpoint,
use Amazon SageMaker AI model endpoints.
- Apply the same logic to model customization workflows.
- Model training workloads should be done Amazon SageMaker AI
HyperPod.
- Provide hosted models access to the appropriate data
using a robust permissions model and federated data
access.

## Resources

**Related best practices:**

- [PERF02-BP01](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_compute_hardware_select_best_compute_options.html)

**Related documents:**

- [Amazon SageMaker AI HyperPod](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod.html)
- [Customize
your model to improve its performance for your use case](https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models.html)
- [Observability
for Amazon SageMaker AI HyperPod cluster orchestrated by Amazon EKS](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-eks-cluster-observability.html)
- [SageMaker AI
HyperPod cluster resources monitoring](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-cluster-observability-slurm.html)

**Related examples:**

- [Amazon Bedrock
Model Customization Workshop](https://github.com/aws-samples/amazon-bedrock-customization-workshop)
- [Efficient and cost-effective multi-tenant LoRA serving with Amazon SageMaker AI](https://aws.amazon.com/blogs/machine-learning/efficient-and-cost-effective-multi-tenant-lora-serving-with-amazon-sagemaker/)
- [Choosing
Between Amazon SageMaker AI Training Jobs and Amazon SageMaker AI HyperPod: A Quick Decision-Making Guide for ML Workloads](https://repost.aws/articles/ARqYgZU7-kTjOYeoi8pZ94ZA/choosing-between-amazon-sagemaker-training-jobs-and-amazon-sagemaker-hyperpod-a-quick-decision-making-guide-for-ml-workloads)
- [Introducing Amazon SageMaker AI HyperPod to train foundation models at scale](https://aws.amazon.com/blogs/machine-learning/introducing-amazon-sagemaker-hyperpod-to-train-foundation-models-at-scale/)
- [Customize
models in Amazon Bedrock with your own data using fine-tuning
and continued pre-training](https://aws.amazon.com/blogs/aws/customize-models-in-amazon-bedrock-with-your-own-data-using-fine-tuning-and-continued-pre-training/)
- [Accelerate
foundation model development with one-click observability in Amazon SageMaker AI HyperPod](https://aws.amazon.com/blogs/machine-learning/accelerate-foundation-model-development-with-one-click-observability-in-amazon-sagemaker-hyperpod/)
- [Amazon SageMaker AI HyperPod launches model deployments to accelerate the generative AI model development lifecycle](https://aws.amazon.com/blogs/machine-learning/amazon-sagemaker-hyperpod-launches-model-deployments-to-accelerate-the-generative-ai-model-development-lifecycle/)
- [Implementing
inference observability on HyperPod clusters](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod-model-deployment-observability.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/genperf03-bp01.html*

---

# GENPERF04 — Vector store optimization

**Pillar**: Performance Efficiency  
**Best Practices**: 2

---

# GENPERF04-BP01 Test vector embeddings for latency and relevant performance

Optimizing a data retrieval system for generative AI may have
more to do with data architecture and meta-data than the
foundation model selected. This best practice encourages high
data quality and data architecture to accelerate data-driven
generative AI workloads.

**Desired outcome:** When
implemented, this best practice facilitates expedient data
storage and access, with accurate and relevant data retrieval.

**Benefits of establishing this best
practice:**
[Consider
mechanical sympathy](https://docs.aws.amazon.com/wellarchitected/latest/framework/perf-dp.html) - Optimizing a data storage system
for a generative AI workload can be as simple as changing vector
indexes or modifying the chunking strategy. Familiarize yourself
with how the system performs data storage and retrieval to best
optimize the database.

**Level of risk exposed if this best
practice is not established:** Medium

## Implementation guidance

Optimizing vector store features for generative AI requires a
holistic approach to search architecture. Begin with effective
chunking and embedding strategies, as these have greater
effects on performance and can only be addressed before data
enters the data store. There are several popular chunking
strategies to select from, including fixed-size, hierarchical,
or semantic. Some vector base solutions like Amazon Bedrock
allow for custom chunking strategies that can be defined with
an AWS Lambda function. There are several factors to consider
when selecting a chunking strategy, including the data being
chunked and how that data is to be retrieved. Evaluate the
available options when configuring a vector store, testing
document retrieval performance against each chunking strategy.

Search algorithms form the backbone of how vectors are
retrieved from vector stores. When selecting an approximate
nearest neighbor (ANN) algorithm, consider the trade-offs
between accuracy, speed, memory usage, and scalability. Common
options include locality-sensitive hashing (LSH) for fast
indexing, hierarchical navigable small world (HNSW) for high
accuracy, inverted file index (IVF) for balance, and product
quantization (PQ) for compact storage. Benchmark multiple
algorithms with your specific dataset to find the optimal
balance based on your prioritized performance metrics.

Organize indices hierarchically, with top-level indices for
general information and lower-level indices for detailed data.
This approach generally outperforms single indices.

For search optimization in AI-driven queries, focus on
machine-to-machine interactions. Implement query expansion
using AI-generated context, and shift fuzzy matching towards
semantic similarity. Leverage hybrid search approaches that
combine semantic understanding with traditional retrieval
techniques to enhance result relevance.

Continually monitor performance across all system components,
including embedding generation, index construction, query
processing, and result retrieval. Track latency, throughput,
and resource utilization. Prepare for scenarios where
performance bottlenecks may shift between layers as your
system scales and usage patterns change. You may have to
re-architect elements of your data storage solution based on
shifting usage patterns. Develop operational runbooks to
facilitate such changes.

Maintain data quality through regular assessments of
freshness, accuracy, and representativeness. Monitor for data
drift and implement processes for continuous data ingestion
and periodic re-embedding. Use automated checks, human review,
and AI output analysis to maintain data quality. Establish
clear governance policies, and maintain version control of
your vector store.

Remember that optimizations in one area can affect the entire
system. Stay adaptable to new techniques and algorithms to
maintain a high-performing, efficient knowledge retrieval
system that delivers accurate, contextually relevant
information for your generative AI application.

### Implementation steps

- Identify the most important performance KPI for this
workload (for example, accuracy, speed, memory usage, or
scalability). Consider implementing a custom search
algorithm that supports this KPI.
- Organize indices based on a hierarchy, where more detail
is introduced towards the bottom of the hierarchy.
- Establish query latency monitoring on the data retrieval
system to verify the database latency is consistently
monitored and alerted upon.
- Perform regular data quality checks, verifying that data
is assessed for quality before being placed into a
database.
- Develop an operational runbook to facilitate rapid
architecture changes to accommodate shifting usage
patterns.
- Develop an operational runbook to facilitate rapid
architecture changes to accommodate shifting usage
patterns.

## Resources

**Related best practices:**

- [PERF05-BP02](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_process_culture_use_monitoring_solutions.html)
- [PERF05-BP03](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_process_culture_workload_performance.html)

**Related documents:**

- [Working
with vector search collections](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-vector-search.html)
- [Vector
search features and limits](https://docs.aws.amazon.com/memorydb/latest/devguide/vector-search-limits.html)

**Related examples:**

- [Accelerate
performance using a custom chunking mechanism with Amazon Bedrock](https://aws.amazon.com/blogs/machine-learning/accelerate-performance-using-a-custom-chunking-mechanism-with-amazon-bedrock/)
- [Amazon Bedrock Knowledge Bases now supports advanced parsing, chunking, and query reformulation giving greater control of accuracy in RAG based applications](https://aws.amazon.com/blogs/machine-learning/amazon-bedrock-knowledge-bases-now-supports-advanced-parsing-chunking-and-query-reformulation-giving-greater-control-of-accuracy-in-rag-based-applications/)
- [Amazon OpenSearch Service's vector database capabilities
explained](https://aws.amazon.com/blogs/big-data/amazon-opensearch-services-vector-database-capabilities-explained/)
- [Building
scalable, secure, and reliable RAG applications using Amazon Bedrock Knowledge Bases](https://aws.amazon.com/blogs/machine-learning/building-scalable-secure-and-reliable-rag-applications-using-amazon-bedrock-knowledge-bases/)
- [Dive
deep into vector data stores using Amazon Bedrock Knowledge
Bases](https://aws.amazon.com/blogs/machine-learning/dive-deep-into-vector-data-stores-using-amazon-bedrock-knowledge-bases/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/genperf04-bp01.html*

---

# GENPERF04-BP02 Optimize vector sizes for your use case

Embedding models may offer support for different sizes of vectors
when embedding data. Optimizing the vector size for an embedding may
introduce long-term performance gains.

**Desired outcome:** When
implemented, this best practice helps verify that vector sizes are
optimized for a specific use case, which can lead to improved
performance over time.

**Benefits of establishing this best
practice:**
[Consider
mechanical sympathy](https://docs.aws.amazon.com/wellarchitected/latest/framework/perf-dp.html) - Optimizing vector sizes for supported
vector embedding models may improve performance of your application.
Familiarize yourself with how your selected embedding model performs
embeddings and retrievals when optimizing.

**Level of risk exposed if this best practice
is not established:** Low

## Implementation guidance

When embedding unstructured data into a vector database, it's
important to test multiple embedding models with various
vector sizes to optimize data retrieval and identify
performance trade-offs. While there's a general relationship
between vector size and accuracy within a model family, this
correlation isn't universal across all embedding models. The
performance of your embeddings depends on several factors: the
specific data you're encoding, the chosen embedding model, and
the vector size used within that model. Consider checking
popular leaderboards like
[HuggingFace's
Massive Text Embedding Benchmark (MTEB) Leaderboard](https://huggingface.co/mteb/leaderboard)
when selecting an embedding model.

Start with a more compact encoding, and increase the vector
size if warranted by your use cases to improve accuracy or
minimize loss. Consider the nature of your dataset and how
focused the topics or language are. The more narrow and deep
the content, the more likely fine-tuning is to improve
accuracy while potentially reducing vector size.

For use cases where higher latency is acceptable, larger
vector sizes within a given model may offer more accuracy and
response nuance. Conversely, for low-latency requirements,
smaller vector sizes typically result in faster retrieval.
However, it's crucial to note that a well-tuned model with
smaller dimensions (like 256) can sometimes outperform a more
generic model with larger dimensions (1024 or greater) in both
accuracy and speed.

Keep in mind that some models offer a limited range of
permissible vector dimensions. This is particularly true for
managed embedding model access through Amazon Bedrock. A wider
variety of embedding models can be incorporated into a
generative AI workflow using Amazon SageMaker AI model endpoints
or SageMaker AI JumpStart. Always test and evaluate the
performance of different models and vector sizes with your
specific dataset to find the optimal balance between accuracy
and latency for your use case.

### Implementation steps

- Identify the most important performance KPI for this
workload (like accuracy, speed, memory usage, or
scalability).
- Determine the number of vector options supported by your
selected embedding model and design experiments meant to
test each option.

Experiment on a variety of data to get a clear
determination of which embedding size is best for this
workload.
- Consider self-hosting an open-source embedding model
using Amazon SageMaker AI model endpoints if available
embedding options are not sufficient.

- Run the experiment and determine the most performant
embedding model for this scenario.

## Resources

**Related best practices:**

- [PERF03-BP01](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_data_use_purpose_built_data_store.html)
- [PERF03-BP02](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_data_evaluate_configuration_options_data_store.html)
- [PERF03-BP03](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_data_collect_record_data_store_performance_metrics.html)
- [PERF03-BP04](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_data_implement_strategies_to_improve_query_performance.html)

**Related documents:**

- [Customizing
your knowledge base](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-how-customization.html)
- [Working
with vector search collections](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-vector-search.html)
- [Vector
search features and limits](https://docs.aws.amazon.com/memorydb/latest/devguide/vector-search-limits.html)

**Related examples:**

- [Amazon OpenSearch Service's vector database capabilities
explained](https://aws.amazon.com/blogs/big-data/amazon-opensearch-services-vector-database-capabilities-explained/)
- [Building
scalable, secure, and reliable RAG applications using Amazon Bedrock Knowledge Bases](https://aws.amazon.com/blogs/machine-learning/building-scalable-secure-and-reliable-rag-applications-using-amazon-bedrock-knowledge-bases/)
- [Dive
deep into vector data stores using Amazon Bedrock Knowledge
Bases](https://aws.amazon.com/blogs/machine-learning/dive-deep-into-vector-data-stores-using-amazon-bedrock-knowledge-bases/)

**Related tools:**

- [HuggingFace's
MTEB Leaderboard](https://huggingface.co/spaces/mteb/leaderboard)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/genperf04-bp02.html*

---

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
