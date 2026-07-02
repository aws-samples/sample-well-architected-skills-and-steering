# MLCOST02 — ML problem framing

**Pillar**: Cost Optimization  
**Best Practices**: 2

---

# MLCOST02-BP01 Identify if machine learning is the right solution

Evaluating whether machine learning is the appropriate solution for
your business problem is crucial for cost optimization. Not every
problem requires ML solutions, and sometimes simpler approaches may
be more effective and less costly. By thoroughly evaluating
alternatives against ML approaches, you can make informed decisions
that optimize both your technical resources and business outcomes.

**Desired outcome:** You identify
whether machine learning is truly the optimal solution for your
business problem by comparing it against simpler alternatives. You
make informed decisions about resource allocation, understanding the
cost implications of ML adoption including data preparation,
storage, training, hosting, and maintenance. You validate your
approach using tools like Amazon SageMaker AI Autopilot and Amazon SageMaker AI Clarify to verify that ML provides measurable benefits
over alternative solutions.

**Common anti-patterns:**

- Jumping directly to ML solutions without evaluating simpler
alternatives.
- Underestimating the total cost of implementing ML, including
data preparation and maintenance.
- Failing to establish a baseline for comparison with existing or
rules-based approaches.
- Overlooking specialized resource constraints such as data
scientist availability or model time-to-market.

**Benefits of establishing this best
practice:**

- Avoids unnecessary complexity and cost in solution design.
- Optimizes resource allocation based on actual business value.
- Reduces risk of project failure due to inappropriate technology
selection.
- Provides quantifiable metrics for evaluating ML solution
effectiveness.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

When considering machine learning for a business problem, start by
thoroughly evaluating whether ML is truly necessary. Many problems
can be effectively solved with simpler rule-based approaches that
may be less expensive to develop and maintain. Machine learning
requires significant investment in data preparation, specialized
hardware, and ongoing maintenance that must be justified by the
business value it delivers.

Begin by clearly articulating your problem and determining if it
requires the adaptive learning capabilities that ML provides.
Consider if the problem involves complex patterns that rules can't
simply capture, or if it requires continuous adaptation to
changing conditions. For example, fraud detection in financial
transactions might benefit from ML due to constantly evolving
fraudulent behaviors, while simple inventory management might be
better served by a rules-based system.

Evaluate costs associated with an ML solution, including data
preparation, storage, compute resources for training, potential
data labeling, model hosting, and ongoing maintenance. Compare
these costs against the business value gained from using ML versus
alternative approaches. Remember that specialized resources like
data scientists might be your most constrained resource, making
their time allocation a critical consideration.

### Implementation steps

- **Articulate your problem
clearly**. Define the business problem you're
trying to solve, the desired outcomes, and how success will
be measured. Be specific about what decisions need to be
made and what data is available to support those decisions.
- **Identify your data
sources**. Evaluate what data you already have,
what data you need to collect, and whether the quality and
quantity are sufficient for ML applications. Consider
[Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html) to catalog and manage your data assets.
- **Calculate comprehensive cost
implications**. Consider the aspects of
implementing an ML solution:

Data preparation and engineering costs
- Data storage requirements and associated costs using
[Amazon S3](https://aws.amazon.com/s3/) or other storage services
- Model training expenses on various hardware options in
[Amazon SageMaker AI Model Training](https://aws.amazon.com/sagemaker/ai/train/)
- Data labeling costs if supervised learning is required
- Potential retraining costs due to model drift or bias
- Model hosting and inference costs
- Ongoing maintenance and monitoring expenses

- **Establish a baseline
solution**. Evaluate how the problem is currently
being solved or how it could be solved with a simpler
approach. If a rules-based solution exists, use it as a
baseline for comparison. For basic ML approaches, consider
pre-built solutions from
[AWS Marketplace](https://aws.amazon.com/marketplace/solutions/machine-learning) or
[Amazon SageMaker AI JumpStart](https://aws.amazon.com/sagemaker/jumpstart/).
- **Build and evaluate an ML
prototype**. Use
[Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html) or
[Amazon SageMaker AI Autopilot](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-automate-model-development.html) to quickly develop an ML model.
Compare the performance metrics of this solution against
your baseline approach, including accuracy, inference time,
and total cost of operation.
- **Analyze model
explainability**. Use
[Amazon SageMaker AI Clarify](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-fairness-and-explainability.html) to understand how your ML model
makes decisions and evaluate if these explanations align
with business expectations and requirements.
- **Make a data-driven
decision**. Based on your comparative analysis,
determine if the ML approach demonstrates sufficient
improvement over simpler solutions to justify the
investment. Consider both quantitative metrics and
qualitative factors like flexibility and scalability.
- **Use no-code ML for rapid
validation**. Use
[SageMaker AI
Canvas](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas.html) with natural language support to quickly
validate whether ML approaches provide value over simpler
solutions, reducing the time and cost of initial feasibility
assessment. Export Canvas-generated models and code to
notebooks for further customization and integration into
production workflows.
- **Use AI-powered code generation for
rapid prototyping**. Use AI-powered development
tools like
[Amazon Q Developer](https://aws.amazon.com/q/developer/) and
[Kiro](https://kiro.ai/) to quickly
generate ML prototype code, automate data preprocessing
scripts, and accelerate the validation process for
determining if ML is the right solution.
- **Assess hybrid approaches**.
Consider whether combining rules-based systems with ML or
generative AI could provide the optimal balance of cost,
performance, and explainability for your specific use case.

## Resources

**Related documents:**

- [Amazon SageMaker AI Canvas](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas.html)
- [SageMaker AI
autopilot](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-automate-model-development.html)
- [Amazon SageMaker AI JumpStart](https://aws.amazon.com/sagemaker/jumpstart/)
- [Machine
Learning solutions in AWS Marketplace](https://aws.amazon.com/marketplace/solutions/machine-learning)
- [Cost
Optimization Pillar - AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/welcome.html)
- [What
is Amazon SageMaker AI?](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html)
- [What
is Amazon Bedrock?](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlcost02-bp01.html*

---

# MLCOST02-BP02 Perform a tradeoff analysis between custom and pre-trained models

Optimize machine learning costs by carefully analyzing the tradeoffs
between developing custom models and using pre-trained models. This
analysis should maintain security and performance efficiency within
acceptable thresholds while minimizing unnecessary expenses.

**Desired outcome:** You achieve
optimal cost efficiency in your machine learning initiatives by
making informed decisions about when to use pre-trained models
versus developing custom solutions. You balance development costs,
time-to-market, model performance, and specific business
requirements while maintaining appropriate security standards. This
strategic approach allows you to accelerate ML development while
optimizing your investment in AI/ML resources.

**Common anti-patterns:**

- Building custom models for every use case without considering
available pre-trained alternatives.
- Using pre-trained models without evaluating if they meet your
specific business requirements.
- Ignoring the total cost of ownership including data scientist
time, infrastructure, and ongoing maintenance.
- Overlooking security and compliance requirements when selecting
pre-trained models.

**Benefits of establishing this best
practice:**

- Reduced time-to-market for ML solutions.
- Lower development and operational costs.
- Ability to use state-of-the-art models without needing extensive
expertise.
- More efficient use of data scientist and ML engineer resources.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

When implementing machine learning solutions, the decision between
building custom models and using pre-trained ones significantly
impacts costs, time-to-market, and solution effectiveness. Custom
models offer greater flexibility and potential performance
advantages for specialized tasks but require substantial
investment in data collection, training infrastructure, and
expertise. Pre-trained models provide rapid deployment and reduced
initial costs but may not perfectly align with specific business
needs.

Your analysis should consider factors including data availability,
task specificity, performance requirements, available expertise,
and long-term maintenance costs. For many common use cases like
sentiment analysis, image classification, or document processing,
pre-trained models can deliver excellent results without the
overhead of custom development. For highly specialized domains or
when competitive advantage depends on model performance, custom
development may justify the additional investment.

### Implementation steps

- **Assess your machine learning
needs**. Begin by clearly defining your business
use case, required model accuracy, latency requirements, and
available data. Understand whether your use case is standard
(for example, image classification or sentiment analysis) or
highly specialized to guide your decision-making process.
- **Use Amazon SageMaker AI built-in
algorithms and AWS Marketplace**.
[Amazon SageMaker AI](https://aws.amazon.com/sagemaker/ai/?nc=sn&loc=1) provides a suite of built-in algorithms
for data scientists and machine learning practitioners to
get started on training and deploying machine learning
models. Pre-trained ML models are ready-to-use models that
can be quickly deployed on Amazon SageMaker AI. By pre-training
the ML models for you, solutions in the
[AWS Marketplace](https://aws.amazon.com/marketplace/solutions/machine-learning/pre-trained-models) take care of the heavy lifting so that
you can deliver AI- and ML-powered features faster and at a
lower cost. Evaluate the cost of your data scientists' time
and other resource requirements to develop your own custom
model vs. bringing a pre-trained model and deploying it on
SageMaker AI for inferencing. The advantage of a custom model
is the flexibility to fine-tune it to match the needs of
your business use case. A pre-trained model can be difficult
to modify and you might have to use it as is.
- **Use Amazon SageMaker AI
JumpStart**. Use
[Amazon SageMaker AI JumpStart](https://aws.amazon.com/sagemaker/jumpstart/) to access pre-trained models and
accelerate the ML development process. SageMaker AI JumpStart
provides a set of solutions for the most common use cases
that can be deployed readily with just a few clicks. The
solutions are fully customizable and showcase the use of AWS CloudFormation templates and reference architectures so you
can accelerate your ML journey. Amazon SageMaker AI JumpStart
also supports one-click deployment and fine-tuning of more
than 150 popular open-source models such as natural language
processing, object detection, and image classification
models.
- **Conduct a cost-benefit
analysis**. Calculate the total cost of ownership
for both custom and pre-trained approaches, including
development time, infrastructure costs, and ongoing
maintenance. Consider factors such as data preparation,
training resources, and the expertise required. Compare
these costs against expected business value and performance
requirements to determine the most cost-effective approach.
- **Implement cost monitoring and
optimization**. Use
[AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) and
[AWS Budgets](https://aws.amazon.com/aws-cost-management/aws-budgets/) to monitor and manage your ML workload costs.
Implement automatic shutdown of idle resources to reduce
unnecessary expenses. Consider using
[AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/) to get cost optimization
recommendations for your ML infrastructure.
- **Explore model customization
options**. When pre-trained models don't fully meet
your requirements, explore customization options like
fine-tuning or transfer learning before committing to full
custom development. This approach can provide a middle
ground between cost and performance and access to existing
models while adapting them to your specific needs.
- **Implement a multi-model
approach**. For complex use cases, consider using
different models for different components of your solution
based on their requirements. This allows you to optimize
costs by using simpler, more economical models where
appropriate while reserving more powerful models for tasks
that require them.
- **Evaluate foundation models in Amazon
Bedrock**.
[Amazon
Bedrock](https://aws.amazon.com/bedrock/) provides a fully managed service that offers
foundation models from leading AI companies through a single
API. Consider using these models for text, image, and
multimodal generative AI applications instead of building
custom models. You can customize these models to your
specific needs using retrieval-augmented generation (RAG) or
fine-tuning while maintaining cost efficiency.
- **Use expanded pre-trained model
libraries**. Use the expanded
[SageMaker AI
JumpStart](https://aws.amazon.com/sagemaker/jumpstart/) catalog which now includes broader
selection of pre-trained models and industry-specific
solutions, reducing the need for custom model development
and associated costs.
- **For generative AI workloads,
consider retrieval-augmented generation (RAG)**.
For many generative AI applications, implementing RAG can
enhance the performance of foundation models by providing
them with relevant context from your organization's data.
This approach can be more cost-effective than fine-tuning
and still provide customized outputs tailored to your
business domain.

## Resources

**Related documents:**

- [Amazon SageMaker AI JumpStart](https://aws.amazon.com/sagemaker/jumpstart/)
- [Pre-trained
machine learning models available in AWS Marketplace](https://aws.amazon.com/marketplace/solutions/machine-learning/pre-trained-models)
- [Amazon SageMaker AI pricing](https://aws.amazon.com/sagemaker/pricing/)
- [Cloud
Financial Management with AWS](https://aws.amazon.com/aws-cost-management/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlcost02-bp02.html*

---
