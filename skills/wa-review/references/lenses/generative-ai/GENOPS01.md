# GENOPS01 — Model performance evaluation

**Pillar**: Operational Excellence  
**Best Practices**: 2

---

# GENOPS01-BP01 Periodically evaluate functional performance

Implement periodic evaluations using stratified sampling and custom
metrics to maintain the performance and reliability of large
language models. This practice verifies that models remain accurate
and relevant over time by regularly assessing their performance
against ground truth data and specific evaluation criteria. By
employing stratified sampling, organizations can obtain a
representative subset of data that reflects the diversity of
real-world inputs, leading to more reliable performance metrics.
Custom metrics allow for tailored assessments that align with
specific business goals and user expectations. This practice helps
customers achieve consistent model performance, detect and address
model drift promptly, and integrate evaluation results into
continuous improvement processes.

**Desired outcome:** When
implemented, this best practice improves the ability to identify and
remediate performance degradation issues in model responses.

**Benefits of establishing this best
practice:**

- [Implement
observability for actionable insights](https://docs.aws.amazon.com/wellarchitected/latest/framework/oe-design-principles.html) - Model responses
to prompts can be observed using key performance indicators
(KPIs) to determine adherence to or deviation from acceptable
performance levels.
- [Anticipate
failure](https://docs.aws.amazon.com/wellarchitected/latest/framework/oe-design-principles.html) - Periodic review of the model's performance
levels helps you proactively identify deviations in its
performance. This is because foundation models are inherently
non-deterministic with a realistic chance of failure.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Evaluations can be conducted by periodically running ground truth
data and applying sampling techniques to run metrics for
monitoring purposes. Feed your prompts into the model to generate
outputs, compare those outputs to the known ground truth values,
and analyze the results to track the model's performance over
time, identifying potential drifts or degradation.

You can employ stratified sampling techniques to verify diverse
data representation within the sample set. Divide your ground
truth data into relevant categories (for example, different user
personas), and randomly sample from each category to provide a
balanced representation in the evaluation set. Consider
periodically updating your ground truth dataset as the inputs and
usage of your workload change over time. Address data drift where
actual usage diverges from your initial ground truth set.

You can use the model evaluation feature built-in with Amazon Bedrock or open-source libraries like
[fmeval](https://github.com/aws/fmeval) or
[ragas](https://docs.ragas.io/en/stable/).
Use Amazon Bedrock model invocation logging to collect metadata,
requests, and responses for model invocations in your account.

For Amazon SageMaker AI, you can set up manual evaluations for a
human workforce using Studio, automatically evaluate your model
with an algorithm using Studio, or automatically evaluate your
model with a customized workflow using the fmeval library.

The fmeval library provides a framework for defining and using
custom metrics. By creating a custom metric class, you can
encapsulate the logic for calculating a specific evaluation
criterion tailored to your use case. Use this to continuously
assess your language models using both standard metrics provided
by fmeval and your own specialized metrics.

Your organization’s AI policy should define the effective minimum performance levels for generative AI workloads, as well as how to validate performance on an ongoing basis. Consider identifying a single-threaded workload owner responsible for the operational considerations pertaining to ongoing performance evaluations. Run these evaluations when new candidate models are available, or when model customization techniques are applied. For example, fine-tuned and customized models should be subject to the same evaluation criteria and cadence as non-customized models.

### Implementation steps

- Create a ground truth dataset.

Verify that you have diverse data representation
- Consider various user personas and use cases

- Apply stratified sampling techniques.

Categorize ground truth data into relevant groups
- Randomly sample from each group to achieve balanced
representation

- Establish periodic evaluation processes.

For Amazon Bedrock:

Use the built-in model evaluation feature
- Implement model invocation logging

- For Amazon SageMaker AI:

Configure manual evaluations using Amazon SageMaker AI
Studio.
- Set up automatic evaluations using Amazon SageMaker AI
Studio or the fmeval library

- Define custom metrics.

Use the fmeval library to create custom metric classes
- Encapsulate logic for calculating specific evaluation
criteria

- Perform model evaluations.

Input prompts into the model
- Generate outputs and compare them to ground truth values
- Analyze results to track performance over time

- Monitor for performance drifts.

Identify potential degradation in model performance
- Address data drift where actual usage diverges from the
initial ground truth

- Regularly update the ground truth dataset.

Reflect changes in workload inputs and usage patterns
- Maintain the relevance of evaluation data

**Additional recommendations**

- Use open-source libraries.

Consider using libraries like ragas for additional
evaluation capabilities
- Explore complementary metrics and evaluation techniques

- Implement automated workflows.

Integrate evaluation processes into CI/CD pipelines
- Set up alerts for significant performance changes

## Resources

**Related best practices:**

- [OPS11-BP11](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_evolve_ops_metrics_review.html)

**Related documents:**

- [Amazon SageMaker AI Model Evaluation](https://docs.aws.amazon.com/sagemaker/latest/dg/model-optimize-evaluate.html)
- [Evaluating
Models in Amazon Bedrock](https://aws.amazon.com/bedrock/evaluations/)
- [Data
and model quality monitoring with Amazon SageMaker AI Model
Monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html)

**Related videos:**

- [AWS re:Invent 2024 - Streamline RAG and model evaluation with
Amazon Bedrock (AIM359)](https://www.youtube.com/watch?v=7BP9nwFlFws)

**Related examples:**

- [SageMaker AI
Model Evaluation Examples](https://docs.aws.amazon.com/sagemaker/latest/dg/ex1-test-model.html)
- [Bedrock
Model Evaluation Demo](https://aws.amazon.com/awstv/watch/1a5442fac30/)
- [Examples
with fmeval](https://github.com/aws/fmeval/tree/main/examples)

**Related tools:**

- [Amazon SageMaker AI Model Monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html)
- [fmeval
library](https://github.com/aws/fmeval)
- [Amazon CloudWatch](https://docs.aws.amazon.com/sagemaker/latest/dg/monitoring-cloudwatch.html)
- [AWS Step Functions](https://aws.amazon.com/blogs/aws/build-generative-ai-apps-using-aws-step-functions-and-amazon-bedrock/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/genops01-bp01.html*

---

# GENOPS01-BP02 Collect and monitor user feedback

Supplement model performance evaluation with direct feedback from
users. Implement continuous feedback loops to optimize application
performance and enhance user satisfaction. Systematically collect,
analyze, and act on user feedback to drive continuous improvement.
By integrating this approach, you can achieve higher operational
excellence and reliability, which keeps applications performant and
aligned with user expectations. This proactive strategy helps to
improve user satisfaction and foster a culture of ongoing
enhancement and innovation.

**Desired outcome:** When
implemented, this best practice improves the ability to surface
performance degradation issues with foundation models as they happen
without requiring ground truth data.

**Benefits this practice helps
achieve:**

- [Implement
observability for actionable insights](https://docs.aws.amazon.com/wellarchitected/latest/framework/oe-design-principles.html) - User feedback
from model responses to prompts can inform the efficacy of a
model, a prompt, or both in addressing a customer problem.
- [Anticipate
failure](https://docs.aws.amazon.com/wellarchitected/latest/framework/oe-design-principles.html) - Periodic review of the user feedback helps you
proactively identify deviations in subjective evaluation of a
model's performance. This is because foundation models are
inherently non-deterministic with a realistic chance
of failure.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Collect and monitor user feedback to establish continuous
improvement and optimization of your applications. User feedback
can be as simple as thumbs up or thumbs down, which you can
capture in your application and store in a database. This approach
helps detect issues early in the process and serves as a feedback
mechanism for prompt engineering.

Regularly review monitoring data, user feedback, and incident
reports related to your application's integration with Amazon Bedrock and Amazon SageMaker AI models. Use these insights to
identify potential improvements, such as optimizing data
pipelines, refining integration patterns, or exploring new model
capabilities.

[Amazon Q Business](https://aws.amazon.com/q/business/) offers tools to monitor and analyze user feedback.
These include an analytics dashboard in the console that provides
usage trends, user conversations, query trends, and user feedback.
Use these insights to optimize your application and identify areas
for improvement. Use the `PutFeedback` API action
to allow end users to provide feedback on chat responses. This
captures user sentiment and helps improve response quality.

Consult your organization’s AI policy document for guidance on how to use user feedback for workload improvements. Direct techniques for incorporating user feedback like reinforcement learning through human feedback may not be applicable for all workloads. Workload owners may be best positioned to identify the appropriate feedback incorporation strategy for a given task.

### Implementation steps

- For Amazon Q Business, set up user feedback collection.

Integrate simple feedback options within the application
- Use the `PutFeedback` API action
through AWS SDK for application integration
- Use Amazon Q Business usage trends and query analysis
- Consider storing feedback in Amazon DynamoDB for
scalable, low-latency storage
- Enable conversation logging to get more insights from
user interactions

Configure log delivery (choose between Amazon S3,
CloudWatch Logs, or Amazon Data Firehose)
- Set up filtering if you need to exclude sensitive
information
- Enable logging to start streaming conversation and
feedback data

- For Amazon Bedrock, set up user feedback collection.

Create an Amazon S3 bucket to store user feedback
- Develop a web form or API endpoint to collect user
feedback
- Create an AWS Lambda function to process incoming
feedback
- Set up an Amazon EventBridge rule to run the Lambda
function when new feedback is added to the S3 bucket

- Establish a regular review process.

Schedule periodic reviews of monitoring data, user
feedback, and incident reports
- Create an AWS Step Functions workflow to manage the
feedback processing pipeline
- Consider Amazon Bedrock's large language models to
analyze the feedback
- Consider Quick to create dashboards and
visualizations of the feedback data

- Implement and test improvements.

Identify optimizations in data pipelines, integration
patterns, or model capabilities
- Track KPIs before and after improvements
- Develop and deploy optimizations
- Validate improvements using A/B testing

## Resources

**Related best practices:**

- [OPS04-BP03](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_observability_customer_telemetry.html)

**Related documents:**

- [Guidance
for Capturing and Analyzing Unstructured Customer Feedback on
AWS](https://aws.amazon.com/solutions/guidance/capturing-and-analyzing-unstructured-customer-feedback-on-aws/)
- [Build
an automated insight extraction framework for customer
feedback analysis with Amazon Bedrock and Quick](https://aws.amazon.com/blogs/machine-learning/build-an-automated-insight-extraction-framework-for-customer-feedback-analysis-with-amazon-bedrock-and-amazon-quicksight/)
- [Guidance
for Automated Customer Feedback Analysis with Amazon Bedrock](https://aws.amazon.com/solutions/guidance/automated-customer-feedback-analysis-with-amazon-bedrock/)

**Related examples:**

- [PutFeedback
- Amazon Q Business](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_PutFeedback.html)
- [Configure
agent to request information from user to increase accuracy of
function prediction - Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-user-input.html)

**Related tools:**

- [Amazon Q Business](https://aws.amazon.com/q/business/)
- [Amazon Bedrock](https://aws.amazon.com/bedrock/)
- [Amazon DynamoDB](https://aws.amazon.com/dynamodb/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
- [Quick](https://aws.amazon.com/quicksight/)
- [AWS Step Functions](https://aws.amazon.com/step-functions/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/genops01-bp02.html*

---
