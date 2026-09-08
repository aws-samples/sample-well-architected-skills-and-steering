# Cost Optimization

**Pillar**: Cost Optimization  
**Questions**: 6

---

# MLCOST01 — Business goal identification

**Pillar**: Cost Optimization  
**Best Practices**: 2

---

# MLCOST01-BP01 Define overall return on investment (ROI) and opportunity cost

Machine learning projects require careful evaluation of their
business value and resource requirements. By analyzing the ROI and
opportunity costs of ML implementations, you can make informed
decisions that optimize resource allocation while delivering maximum
business impact.

**Desired outcome:** When you
implement this practice, you have a clear understanding of the
financial and business implications of your ML projects. You can
differentiate between research-oriented and development-oriented ML
initiatives, track costs effectively through tagging mechanisms, and
make data-driven decisions about resource allocation. You have
established processes to continuously evaluate the cost-benefit
ratio of ML initiatives as business conditions evolve, and your
investments deliver measurable value while managing risks
appropriately.

**Common anti-patterns:**

- Initiating ML projects without defining clear business
objectives or expected outcomes.
- Failing to distinguish between research projects (long-term
returns) and development projects (near-term returns).
- Not implementing cost tracking mechanisms for ML projects.
- Overlooking the ongoing operational costs of maintaining ML
models in production.
- Failing to reassess the cost-benefit model when business
conditions change.

**Benefits of establishing this best
practice:**

- Improved allocation of limited resources to ML initiatives with
highest potential returns.
- Clear visibility into project costs and benefits for better
budgeting and planning.
- Reduced risk of project failure through upfront analysis and
ongoing monitoring.
- Enhanced ability to communicate ML value to stakeholders.
- Accelerated time-to-value through focus on high-impact use
cases.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Understanding the financial implications of machine learning
initiatives is crucial for making strategic technology
investments. Machine learning projects can vary significantly in
terms of resource requirements, timeline to value, and overall
business impact. By carefully evaluating the ROI and opportunity
costs, you can prioritize initiatives that deliver the most
significant business value while managing costs effectively.

Start by working with both technical and business teams to clearly
define whether an ML project is research-oriented (focused on
exploring potential future value) or development-oriented
(applying established methods to deliver immediate business
value). This distinction assists to set appropriate expectations
around timelines, resources, and outcomes. Implement comprehensive
cost tracking through tagging mechanisms to maintain visibility
into project expenses across data engineering, model development,
and production deployment phases.

When assessing ML project costs, consider both direct expenses
(infrastructure, tools, services) and indirect costs (staff time,
training requirements, maintenance). Factor in potential costs
associated with data preparation, model accuracy, and production
errors. Develop a comprehensive cost-benefit model that accounts
for these elements while considering business-specific factors
like competitive advantage and strategic positioning.

### Implementation steps

- **Specify the objectives of the ML
project as research or development**. Work with
both business stakeholders and data science teams to
determine if your ML initiative is exploratory research with
long-term returns or development applying established
methods for faster ROI. Align between technical teams and
business leaders on project classification, timelines, and
expected outcomes.
- **Use tagging to track costs by
project and business unit**. Implement
comprehensive tagging in your AWS environment using
[AWS Cost Categories](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-categories.html) and
[AWS Tagging](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) strategies to allocate ML-related expenses to
specific projects and business functions. Monitor these
costs through
[AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) to maintain clear visibility of ROI by
project.
- **Evaluate and assess the data
pipeline, the ML model, and the expected quality of
production inferences**. Analyze the infrastructure
requirements, operational costs, and potential business
impact of errors in your ML system. Use
[Amazon SageMaker AI Clarify](https://aws.amazon.com/sagemaker/clarify/) to assess model quality and
identify potential bias that could impact business outcomes
and add remediation costs.
- **Develop a cost-benefit
model**. Create a comprehensive financial model
that accounts for initial development costs, ongoing
operational expenses, and expected business benefits.
Regularly reassess this model as business conditions change
or when considering new data sources. Use
[Quick](https://aws.amazon.com/quicksight/) to build dashboards tracking ML costs
against business KPIs.
- **Understand, evaluate, and monitor
project risks**. Identify technical, operational,
and business risks associated with your ML project.
Establish monitoring systems to track these risks through
development and production phases. Use
[Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) to monitor technical metrics and
[AWS Budgets](https://aws.amazon.com/aws-cost-management/aws-budgets/) to track spending against forecasts.
- **Estimate the cost of resources
needed for production maintenance**. Calculate the
ongoing expenses required to maintain your ML model in
production, including data engineers, data scientists,
infrastructure costs, and monitoring systems. Consider using
[AWS Application Cost Profiler](https://aws.amazon.com/aws-cost-management/aws-application-cost-profiler/) to attribute costs
accurately across your ML applications.
- **Leverage enhanced cost tracking and
optimization tools**. Use
[AWS Cost Anomaly Detection](https://docs.aws.amazon.com/cost-management/latest/userguide/getting-started-ad.html) to automatically identify
unusual spending patterns in your ML workloads and receive
alerts for unexpected cost increases.
- **Consider model selection trade-offs
for generative AI projects**. When implementing
generative AI solutions, carefully evaluate the balance
between model size, performance, and cost. Smaller,
domain-specific models may be more cost-effective than large
foundation models for certain use cases. Consider using
[Amazon
Bedrock](https://aws.amazon.com/bedrock/) for access to multiple foundation models
through a single API, allowing for streamlined model
selection and optimization.

## Resources

**Related documents:**

- [AWS Pricing Calculator](https://calculator.aws/#/createCalculator)
- [What
is AWS Billing and Cost Management and Cost Management?](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-categories.html)
- [Optimizing
cost for building AI models with Amazon EC2 and SageMaker AI](https://aws.amazon.com/blogs/aws-cloud-financial-management/optimizing-cost-for-developing-custom-ai-models-with-amazon-ec2-and-sagemaker-ai/)
- [Analyze
Amazon SageMaker AI spend and determine cost optimization
opportunities based on usage, Part 4: Training jobs](https://aws.amazon.com/blogs/machine-learning/part-4-analyze-amazon-sagemaker-spend-and-determine-cost-optimization-opportunities-based-on-usage-part-4-training-jobs/)
- [AWS Application Cost Profiler](https://aws.amazon.com/aws-cost-management/aws-application-cost-profiler/)
- [Getting
started with AWS Cost Anomaly Detection](https://docs.aws.amazon.com/cost-management/latest/userguide/getting-started-ad.html)
- [Managing
costs with AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html)
- [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/)
- [AWS Cost and Usage Report](https://aws.amazon.com/aws-cost-management/aws-cost-and-usage-reporting/)
- [Generative
AI Cost Optimization Strategies](https://aws.amazon.com/blogs/enterprise-strategy/generative-ai-cost-optimization-strategies/)

**Related videos:**

- [Maximizing
ML ROI: Amazon SageMaker AI's High-Performance Inference and Cost
Optimization Strategies](https://aws.amazon.com/awstv/watch/3cf59d4c5e5/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlcost01-bp01.html*

---

# MLCOST01-BP02 Use managed services to reduce total cost of ownership (TCO)

Using managed machine learning services enables organizations to
operate more efficiently with reduced resources and costs compared
to self-managed options. This approach reduces undifferentiated
heavy lifting, reduces operational burden, and allows teams to focus
on delivering business value.

**Desired outcome:** By adopting
managed services and pay-per-usage models, you significantly reduce
your total cost of ownership while gaining access to a comprehensive
suite of AI/ML tools. You can use pre-built capabilities instead of
developing custom solutions, automatically scale resources based on
demand, and benefit from AWS's continuous innovations without
additional investment. Your teams can focus on creating business
value rather than managing infrastructure.

**Common anti-patterns:**

- Building and maintaining custom ML infrastructure on EC2 or
Kubernetes.
- Overprovisioning resources for peak ML workloads.
- Failing to use commitment discounts for persistent workloads.
- Developing proprietary AI services when managed services would
suffice.
- Not analyzing workload patterns to optimize instance selection.

**Benefits of establishing this best
practice:**

- Significantly lower total cost of ownership compared to
self-managed options.
- Reduced operational overhead and simplified management.
- Increased team productivity with focus on core business
problems.
- Access to continuously updated and improved AI/ML capabilities.
- Flexibility to scale resources based on actual demand.
- Ability to use commitment-based pricing for additional savings.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Managed services remove the operational burden of maintaining
infrastructure, allowing you to concentrate on developing ML
models and applications that drive business value. Using AWS's
managed ML services provides a comprehensive environment for
building, training, and deploying models with significantly lower
costs than self-managed options.

When evaluating your ML strategy, consider the total cost of
ownership including infrastructure, operational personnel,
maintenance, scaling, and upgrades. Amazon SageMaker AI provides a
fully managed service that avoids many of these costs while
offering advanced ML capabilities. Similarly, AWS's pre-trained AI
services can address common use cases without requiring ML
expertise, further reducing implementation time and costs.

To maximize cost efficiency, analyze your workload patterns and
determine which components would benefit from commitment
discounts. By using Savings Plans, you can significantly reduce
your AWS usage costs while maintaining flexibility across instance
families, sizes, regions, and components.

### Implementation steps

- **Use Amazon SageMaker AI as your
fully managed ML solution.**
[Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html) enables building, training, and
deploying models at scale with significantly lower costs.
The total cost of ownership (TCO) of SageMaker AI over a
three-year period is much lower than other self-managed
cloud-based ML options, such as
[Amazon Elastic Compute Cloud](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html) (Amazon EC2) and
[Amazon Elastic Kubernetes Service](https://docs.aws.amazon.com/eks/latest/userguide/getting-started.html) (Amazon EKS). SageMaker AI
includes technologies such as
[Autopilot](https://aws.amazon.com/sagemaker/autopilot/),
[Feature
Store](https://aws.amazon.com/sagemaker/feature-store/),
[Clarify](https://aws.amazon.com/sagemaker/clarify/),
[Debugger](https://aws.amazon.com/sagemaker/debugger/),
[Studio](https://aws.amazon.com/sagemaker/studio/),
[Training](https://docs.aws.amazon.com/sagemaker/latest/dg/how-it-works-training.html),
Model deployment,
[Monitoring](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html),
and
[Pipelines](https://aws.amazon.com/sagemaker/pipelines/).
- **Use Amazon managed AI services for
common use cases.** AWS pre-trained AI services
provide ready-made intelligence for your applications and
workflows. These services address common use cases such as
personalized recommendations, contact center modernization,
safety and security improvement, and customer engagement
enhancement. They don't require machine learning expertise,
are fully managed, and offer pay-as-you-go pricing with no
upfront commitment.
- **Perform pricing model analysis for
cost optimization.** Analyze each component of your
ML workload to determine if it will run for extended
periods, making it eligible for commitment discounts such as
[AWS Savings Plans](https://docs.aws.amazon.com/savingsplans/latest/userguide/what-is-savings-plans.html). You can use Savings Plans to reduce
AWS usage costs by committing to a consistent amount of
usage.
[Amazon SageMaker AI Savings Plans](https://aws.amazon.com/savingsplans/ml-pricing/) offer flexible attributes
such as instance family, instance size, AWS Region, and
component for your SageMaker AI instance usage.
- **Implement right-sizing strategies
for ML resources.** Evaluate your actual ML
workload resource requirements and adjust instance types and
sizes accordingly. This blocks overprovisioning and assists
to control costs while maintaining performance. Use
SageMaker AI's automatic scaling capabilities to match
resources with demand.
- **Use serverless options when
appropriate.** For intermittent workloads or those
with variable demand, consider serverless options like
[Amazon SageMaker AI Serverless Inference](https://docs.aws.amazon.com/sagemaker/latest/dg/serverless-endpoints.html) to avoid paying for
idle resources.
- **Use Amazon Bedrock for foundation
model access.**
[Amazon
Bedrock](https://aws.amazon.com/bedrock/) provides a unified API for accessing various
foundation models, making it simple to experiment with and
integrate generative AI capabilities without investing in
model training infrastructure. This fully managed service
assists to reduce costs while allowing flexibility to choose
the right model for your use case.
- **Use Foundation Model Hub for
centralized model access**. Use the Foundation
Model Hub to access a centralized catalog of popular
foundation models with simplified deployment and performance
benchmarking tools, reducing the time and cost of model
selection and deployment.
- **Use AI-powered code generation
tools.** Use
[Amazon Q Developer](https://aws.amazon.com/q/developer/) and AI-powered IDEs like Kiro to
accelerate ML development through AI-assisted coding,
automated code generation, and intelligent troubleshooting,
significantly reducing developer time and associated costs.

## Resources

**Related documents:**

- [Amazon
managed AI services](https://aws.amazon.com/machine-learning/ai-services/)
- [AWS AI Services overview](https://aws.amazon.com/machine-learning/)
- [ML
Savings Plans](https://aws.amazon.com/savingsplans/ml-pricing/)
- [AWS Pricing Calculator for SageMaker AI](https://calculator.aws/#/createCalculator/SageMaker AI)
- [Viewing
resource recommendations](https://docs.aws.amazon.com/compute-optimizer/latest/ug/viewing-recommendations.html)
- [What
is Amazon Bedrock?](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html)
- [What
is AWS Migration Hub?](https://docs.aws.amazon.com/migrationhub/latest/ug/whatishub.html)
- [What
are AWS Cost and Usage Reports?](https://docs.aws.amazon.com/cur/latest/userguide/what-is-cur.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlcost01-bp02.html*

---

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

# MLCOST03 — Data processing

**Pillar**: Cost Optimization  
**Best Practices**: 4

---

# MLCOST03-BP01 Use managed data labeling

Use managed labeling tools that provide automation and access to
cost-effective teams of human data labelers. These tools should
offer flexibility to choose a variable number of labelers for each
input, include a user-friendly interface, and incorporate learning
capabilities to improve labeling efficiency over time.

**Desired outcome:** You have access
to high-quality labeled datasets for your machine learning models
without building and managing your own labeling infrastructure. Your
data labeling process is streamlined, cost-efficient, and scales
according to your needs, allowing you to focus on model development
rather than data preparation logistics.

**Common anti-patterns:**

- Building custom data labeling infrastructure from scratch.
- Relying solely on in-house teams for labeling tasks regardless
of scale.
- Using labeling solutions that don't improve through machine
learning.
- Managing inconsistent labeling quality without proper oversight
tools.

**Benefits of establishing this best
practice:**

- Reduce time-to-market for ML models by accelerating the data
labeling process.
- Lower total labeling costs through efficient automation and
on-demand workforce.
- Improve labeling quality and consistency through specialized
tools and workflows.
- Scale labeling operations up or down based on project
requirements.
- Focus your team's effort on model development rather than
labeling infrastructure.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

To build effective machine learning models, you need large,
high-quality labeled datasets. Creating these datasets manually is
time-consuming, expensive, and difficult to scale. By using
managed data labeling services, you can accelerate this critical
step in the ML development process while controlling costs and
maintaining quality.

Managed data labeling combines human intelligence with machine
learning to improve efficiency over time. As your models process
more data, they can begin to automate parts of the labeling
process, reducing costs and time required. These services also
provide quality control mechanisms through consensus models, where
multiple labelers evaluate the same data to check accuracy.

When selecting a managed data labeling solution, consider factors
like the types of data you need to label (like images, text, and
video), the complexity of your labeling tasks, integration with
your existing ML workflow, and cost structure. The right solution
will scale with your needs and provide consistent, high-quality
labeled data.

### Implementation steps

- **Assess your data labeling
requirements**. Define what types of data you need
labeled (images, text, audio, or video), the complexity of
annotations required, expected volume, and quality
standards. Determine whether you need specialized domain
expertise for your labeling tasks.
- **Use Amazon SageMaker Ground Truth**. To train a machine learning model, you
need a large, high-quality, labeled dataset.
[Amazon SageMaker Ground Truth](https://docs.aws.amazon.com/sagemaker/latest/dg/sms.html) assists you to build
high-quality training datasets for your ML models. With
Ground Truth, you can use ML along with workers from a
vendor company that you choose, or an internal, private
workforce to create a labeled dataset. You can use the
labeled dataset output from Ground Truth to train your own
models. You can also use the output as a training data set
for an Amazon SageMaker AI model.
- **Use Amazon SageMaker Ground Truth
Plus**. Ground Truth Plus is a turn-key service
that uses an expert workforce to deliver high-quality
training datasets fast, and reduces costs by up to 40
percent.
[Amazon SageMaker Ground Truth Plus](https://docs.aws.amazon.com/sagemaker/latest/dg/gtp.html) enables you to create
high-quality training datasets without having to build
labeling applications and manage the labeling workforce on
your own. By using this approach, you don't need to have
deep ML expertise or extensive knowledge of workflow design
and quality management. You simply provide data along with
labeling requirements and Ground Truth Plus sets up the data
labeling workflows and manages them on your behalf in
accordance with your requirements.
- **Configure active learning
workflows**. Set up your labeling projects to use
active learning, where the system learns from human
annotations and begins to automate labeling for similar
items. This reduces the number of items requiring manual
labeling over time, improving efficiency and reducing costs.
Amazon SageMaker Ground Truth provides built-in support for
active learning.
- **Implement quality control
mechanisms**. Configure your labeling jobs to use
multiple workers per data item and determine consensus
approaches based on your quality requirements. Monitor
labeling performance and adjust your quality control
parameters as needed.
- **Set up real-time data labeling
pipelines**. For ongoing ML projects, establish
continuous data labeling pipelines that can process new data
as it becomes available. This way, your models can be
regularly retrained with fresh data.
- **Create custom labeling interfaces
when needed**. For specialized labeling tasks, use
Ground Truth's custom template capabilities to create
tailored labeling interfaces that make the process more
efficient for your specific use case.
- **Use enhanced Ground Truth
capabilities**. Use improved Ground Truth Plus
features that provide up to 40% cost reduction through
expert workforce management and automated quality control
mechanisms.
- **Use foundation models for
pre-labeling**. Use generative AI models through
Amazon Bedrock to assist with initial data labeling, which
can then be verified by human labelers. This hybrid approach
can significantly accelerate the labeling process while
maintaining quality control.

## Resources

**Related documents:**

- [Training
data labeling using humans with Amazon SageMaker Ground Truth](https://docs.aws.amazon.com/sagemaker/latest/dg/sms.html)
- [Use
Amazon SageMaker Ground Truth Plus to Label Data](https://docs.aws.amazon.com/sagemaker/latest/dg/gtp.html)
- [Using
the Amazon Mechanical Turk Workforce](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-workforce-management-public.html)
- [Automate
data labeling](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-automated-labeling.html)
- [Custom
labeling workflows](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-custom-templates.html)
- [Annotation
consolidation](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-annotation-consolidation.html)
- [Ground
Truth streaming labeling jobs](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-streaming-labeling-job.html)
- [Implementing
a custom labeling GUI with built-in processing logic with
Amazon SageMaker Ground Truth](https://aws.amazon.com/blogs/machine-learning/implementing-a-custom-labeling-gui-with-built-in-processing-logic-with-amazon-sagemaker-ground-truth/)

**Related examples:**

- [Bring
your own model for SageMaker AI labeling workflows with active
learning](https://github.com/aws/amazon-sagemaker-examples/blob/master/ground_truth_labeling_jobs/bring_your_own_model_for_sagemaker_labeling_workflows_with_active_learning/bring_your_own_model_for_sagemaker_labeling_workflows_with_active_learning.ipynb)
- [SageMaker AI
Ground Truth recipe](https://github.com/aws-samples/aws-sagemaker-ground-truth-recipe)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlcost03-bp01.html*

---

# MLCOST03-BP02 Use no-code or low-code and code generation tools for interactive analysis

Prepare data through data wrangler tools for interactive data
analysis and model building. The no-code/low-code, automation, and
visual capabilities improve productivity and reduce the cost for
interactive analysis. Integrate with generative AI code generation
tools.

**Desired outcome:** You will be able
to streamline your data preparation workflow using visual interfaces
with minimal coding required. By implementing no-code or low-code
tools like Amazon SageMaker AI Canvas and Data Wrangler, you reduce
time spent on data preprocessing tasks and gain improved insights
through interactive visualizations. Amazon Q integration provides
intelligent assistance for data preparation and code generation,
enabling faster iteration cycles on model development while
maintaining data quality and consistency across your machine
learning projects.

**Common anti-patterns:**

- Writing custom data preparation scripts for every analysis task.
- Using disjointed tools for data import, transformation, and
visualization.
- Manually performing repetitive data cleaning operations.
- Creating non-reproducible data preparation workflows.

**Benefits of establishing this best
practice:**

- Reduced time and cost for data preparation and feature
engineering.
- Improved productivity through visual interfaces and automation.
- Streamlined workflow from data import to model deployment.
- Support for code and no-code approaches to accommodate different
skill levels.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Data preparation is often cited as the most time-consuming aspect
of machine learning projects, typically consuming 60-80% of data
scientists' time. Data wrangler tools provide visual interfaces to
simplify and accelerate this process through automation and
low-code solutions.

Amazon SageMaker AI Data Wrangler offers an end-to-end solution for
data preparation that integrates directly with your machine
learning workflow. By using a visual interface, you can import
data from various sources, identify and fix data quality issues,
transform features, and generate insights—all with minimal coding
required. The tool provides transparency by generating code for
your transformations, fostering reproducibility and allowing
customization when needed.

Data wrangler tools are particularly valuable for exploratory data
analysis, where quick iteration and visualization are essential.
They allow you to rapidly identify patterns, outliers, and
relationships in your data, accelerating the feature engineering
process. With built-in data quality and insights features, you can
understand your data characteristics and address issues before
model training begins.

### Implementation steps

- **Set up Amazon SageMaker AI Canvas or
Studio environment**. Access SageMaker AI Canvas for a
no-code experience or SageMaker AI Studio for more advanced
capabilities through the AWS Management Console. Canvas
provides a visual, drag-and-drop interface for business
analysts and citizen data scientists, while Studio offers
Data Wrangler for more technical users. Both environments
support the complete machine learning workflow with varying
levels of coding requirements.
- **Import data from various
sources**. Use SageMaker AI Canvas or Data Wrangler to
connect to multiple data sources including Amazon S3, Amazon Athena, Amazon Redshift, Snowflake, and various databases.
Canvas provides a simplified point-and-click interface for
business users, while Data Wrangler offers more advanced
data source connectivity options. Both tools avoid the need
for custom connector code.
- **Explore and visualize your
data**. USe Data Wrangler's built-in data
visualizations to understand distributions, correlations,
and outliers. These visualizations assist to identify
potential issues early and inform feature engineering
decisions without writing complex plotting code.
- **Use Amazon Q for generative
AI-powered data preparation and code generation**.
Use Amazon Q integrated within SageMaker AI Canvas and Data
Wrangler to get natural language assistance for data
preparation tasks, automated code generation, and
intelligent suggestions for data transformations. Amazon Q
can explain data patterns, suggest optimal preprocessing
steps, and generate code snippets for custom
transformations, significantly reducing the time needed for
data preparation tasks. Additionally, use AI-powered
development tools like Kiro for intelligent code generation
and optimization of your data processing workflows.
- **Apply transformations to prepare
your data**. Use the visual transformation
interface to clean and prepare data through operations like
handling missing values, encoding categorical features,
scaling numerical values, and feature extraction. Data
Wrangler provides over 300 built-in transformations while
allowing custom Python transformations when needed.
- **Analyze data quality and generate
insights**. Use the built-in data quality and
insights features to detect anomalies, check for imbalanced
data, and understand feature importance. These automated
analyses identify potential issues before model training
begins.
- **Balance your datasets**.
Address imbalanced datasets using built-in techniques like
random oversampling, random undersampling, and synthetic
minority oversampling (SMOTE). Data Wrangler provides visual
controls to implement these techniques without specialized
knowledge.
- **Scale to larger datasets**.
Process larger datasets by configuring instance types and
using distributed processing capabilities. Data Wrangler
supports processing wide datasets with thousands of columns
and large datasets with billions of rows through appropriate
resource allocation.
- **Prepare time series data**.
Use specialized time series transformations to handle
temporal data, including resampling, lagged feature
creation, and time-based aggregations. These operations
simplify working with sequential data patterns.
- **Export your data flow for
production**. Deploy your data preparation workflow
by exporting to various destinations including Amazon S3,
SageMaker AI Feature Store, or directly to model building
workflows. Data Wrangler generates Python code that can be
integrated into production pipelines. Canvas workflows can
also be exported to SageMaker AI notebooks for further
customization and integration into production pipelines.
- **Use enhanced Canvas
capabilities**. Use SageMaker AI Canvas's improved
natural language support and Q integration for
conversational data analysis, enabling business users to
perform complex data preparation tasks without technical
expertise.
- **Integrate with the broader machine
learning workflow**. Connect your prepared data
directly to SageMaker AI's model building capabilities like
SageMaker AI Autopilot for automated model development or
custom model training. This integration creates a seamless
path from data to deployed models.

## Resources

**Related documents:**

- [Amazon SageMaker AI Canvas](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas.html)
- [Get
Started with Data Wrangler](https://docs.aws.amazon.com/sagemaker/latest/dg/data-wrangler-getting-started.html)
- [Prepare
ML Data with Amazon SageMaker AI Data Wrangler](https://docs.aws.amazon.com/sagemaker/latest/dg/data-wrangler.html)
- [What
is Amazon Q Developer?](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/what-is.html)
- [What
is AWS Glue DataBrew?](https://docs.aws.amazon.com/databrew/latest/dg/what-is.html)
- [Create,
store, and share features with Feature Store](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store.html)
- [Accelerate
data preparation with data quality and insights in Amazon SageMaker AI Data Wrangler](https://aws.amazon.com/blogs/machine-learning/accelerate-data-preparation-with-data-quality-and-insights-in-amazon-sagemaker-data-wrangler/)
- [Process
larger and wider datasets with Amazon SageMaker AI Data
Wrangler](https://aws.amazon.com/blogs/machine-learning/process-larger-and-wider-datasets-with-amazon-sagemaker-data-wrangler/)
- [Fuel
Your Data with Generative AI](https://aws.amazon.com/blogs/enterprise-strategy/fuel-your-data-with-generative-ai/)

**Related examples:**

- [Prepare
ML Data with Amazon SageMaker AI Data Wrangler](https://github.com/awsdocs/amazon-sagemaker-developer-guide/blob/master/doc_source/data-wrangler.md)
- [SageMaker AI
Data Wrangler Examples GitHub Repository](https://github.com/aws/amazon-sagemaker-examples/tree/main/sagemaker-datawrangler)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlcost03-bp02.html*

---

# MLCOST03-BP03 Use managed data processing capabilities

With managed data processing, you can use a simplified, managed
experience to run your data processing workloads, such as feature
engineering, data validation, model evaluation, and model
interpretation.

**Desired outcome:** By implementing
managed data processing capabilities, you can streamline your
machine learning workflow with fully managed infrastructure for data
preprocessing and postprocessing tasks. You gain the ability to run
processing jobs that integrate with popular frameworks while
maintaining operational efficiency, allowing your team to focus on
creating valuable ML models rather than managing infrastructure.

**Common anti-patterns:**

- Building and maintaining custom data processing infrastructure.
- Managing your own compute clusters for data processing tasks.
- Manually handling scaling, deployment, and cleanup of processing
resources.
- Using inconsistent processing environments across development
and production.

**Benefits of establishing this best
practice:**

- Reduced operational overhead with fully managed infrastructure.
- Simplified integration with popular ML frameworks and AWS
services.
- Enhanced productivity by focusing on ML development rather than
infrastructure management.
- Seamless integration with other SageMaker AI capabilities.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Amazon SageMaker AI Processing provides a managed solution for
running these data processing workloads. Instead of provisioning
and managing your own infrastructure, SageMaker AI handles the
provisioning, scaling, and cleanup of resources. Processing jobs
accept data from Amazon S3 as input and store processed results
back to S3 as output. You can use AWS-provided container images
that come pre-configured with popular data science frameworks, or
you can bring your own custom containers for specialized
processing needs.

By using SageMaker AI Processing, you can integrate data processing
steps seamlessly into your ML pipelines and create consistency
between development and production environments while reducing
operational overhead. This allows your data scientists and ML
engineers to focus on extracting insights from data rather than
managing infrastructure.

### Implementation steps

- **Set up your processing job
environment**. Create an Amazon SageMaker AI notebook
instance or Studio environment from which you'll configure
and launch your processing jobs. This provides an
interactive environment for development and testing of your
data processing scripts before scaling to larger datasets.
- **Select or create a processing
container**. Choose from SageMaker AI's built-in
processing containers for frameworks like scikit-learn,
PyTorch, TensorFlow, or Apache Spark. Alternatively, create
a custom Docker container if you have specialized framework
requirements. The container will include the runtime
environment and dependencies needed for your processing
tasks.
- **Prepare your processing
script**. Develop a script that runs within the
processing container to perform your data transformation,
feature engineering, model evaluation, or other processing
tasks. This script should read input data, process it
according to your requirements, and write output to the
designated locations.
- **Configure storage
locations**. Set up Amazon S3 buckets to store your
input data, processing scripts, and output results.
SageMaker AI Processing jobs use S3 as the primary storage
mechanism for exchanging data between steps in your ML
workflow.
- **Launch a processing job**.
Use the SageMaker AI Python SDK or AWS console to configure and
start your processing job. Specify parameters such as
instance type, instance count, environment variables, and
input and output configurations. SageMaker AI will provision
the requested resources, run your processing script, and
then automatically clean up the resources when the job
completes.
- **Monitor job progress and analyze
results**. Track your processing job through the
SageMaker AI console or API. Review logs to debug issues. Once
completed, access the processed data in the specified S3
output locations for use in subsequent ML workflow steps.
- **Integrate with ML
pipelines**. Incorporate your processing jobs into
[SageMaker AI
Pipelines](https://aws.amazon.com/sagemaker/pipelines/) to create automated end-to-end ML
workflows. This enables you to orchestrate data
preprocessing, model training, evaluation, and deployment
steps in a repeatable manner.
- **Optimize resource utilization and
costs**. Review processing job metrics to identify
opportunities for optimizing instance selection and
parallelization strategies. Consider using Spot instances
for cost savings on non-time-sensitive processing jobs.
- **Use enhanced processing
capabilities**. Use SageMaker AI Processing with
better integration to popular ML frameworks and enhanced
monitoring capabilities for more efficient data processing
workflows.
- **Use AI-powered code generation for
data processing**. Use AI-powered development tools
like
[Amazon Q Developer](https://aws.amazon.com/q/developer/) and
[Kiro](https://kiro.ai/) to generate
data processing scripts, automate pipeline creation, and
accelerate the development of custom data transformation
workflows.
- **Implement data validation and
quality checks**. Incorporate data validation steps
in your processing jobs to check data quality before model
training. Use SageMaker AI Clarify within processing jobs to
detect bias in your datasets and implement model
explainability.

## Resources

**Related documents:**

- [Data
transformation workloads with SageMaker AI Processing](https://docs.aws.amazon.com/sagemaker/latest/dg/processing-job.html)
- [CreateProcessingJob](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateProcessingJob.html)
- [Managed
Spot Training in Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/model-managed-spot-training.html)
- [Amazon SageMaker AI Feature Store](https://aws.amazon.com/sagemaker/feature-store/)
- [Amazon SageMaker AI Data Wrangler](https://aws.amazon.com/sagemaker/data-wrangler/)

**Related examples:**

- [Amazon SageMaker AI Processing jobs](https://sagemaker-examples.readthedocs.io/en/latest/sagemaker_processing/scikit_learn_data_processing_and_model_evaluation/scikit_learn_data_processing_and_model_evaluation.html)
- [SageMaker AI
Processing with Spark](https://github.com/aws/amazon-sagemaker-examples/tree/main/sagemaker_processing/spark_distributed_data_processing)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlcost03-bp03.html*

---

# MLCOST03-BP04 Enable feature reusability

Reduce duplication and the rerunning of feature engineering code
across teams and projects by using feature storage. The store should
have online and offline storage, and data encryption capabilities.
An online store with low-latency retrieval capabilities is ideal for
real-time inference. An offline store maintains a history of feature
values and is suited for training and batch scoring.

**Desired outcome:** You gain a
centralized repository for storing, sharing, and managing machine
learning features that reduces redundant work across teams and
projects. You access features with low latency for real-time
applications while maintaining a historical record for training
purposes. Your feature store integrates seamlessly with your ML
workflows, enhancing collaboration and accelerating model
development while maintaining data security through robust
encryption.

**Common anti-patterns:**

- Recreating the same features repeatedly across different teams
and projects.
- Storing features in isolated data silos that avoid reuse.
- Lacking version control for features, leading to inconsistencies
between training and inference.
- Using separate systems for real-time and batch feature access.
- Implementing homegrown feature storage solutions that lack
scalability and proper governance.

**Benefits of establishing this best
practice:**

- Reduces redundant work and computational costs.
- Creates consistency between training and inference environments.
- Enables collaboration and knowledge sharing across teams.
- Provides feature governance, lineage, and traceability.
- Reduces time to production for ML models.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Feature engineering is often one of the most time-consuming
aspects of machine learning development. When teams work in silos,
they frequently recreate the same features, wasting valuable time
and resources. By implementing a centralized feature store, you
create a single source of truth for ML features that promotes
reusability across your organization.

A well-designed feature store addresses the dual requirements of
offline storage for training and batch inference and online
storage for low-latency real-time inference. This dual-storage
paradigm creates consistency between training and serving
environments while optimizing for different access patterns. The
feature store should also provide capabilities for feature
versioning, access control, and monitoring to maintain data
quality and governance.

Amazon SageMaker AI Feature Store offers these capabilities as a
fully managed service, which reduces the need to build and
maintain complex infrastructure. It seamlessly integrates with
your ML pipelines and supports both batch and real-time inference
workflows, making it an ideal solution for feature reusability.

### Implementation steps

- **Identify common features across
projects**. Begin by analyzing your existing ML
workflows to identify frequently used features that would
benefit from centralization. Look for redundancies in
feature engineering code across different teams and
prioritize these for migration to the feature store.
- **Set up Amazon SageMaker AI Feature
Store**. Create feature groups in
[Amazon SageMaker AI Feature Store](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store.html) to organize related
features. Define the schema for each feature group,
including feature names, data types, and primary keys.
Consider the access patterns for both training and inference
when designing your feature groups.
- **Configure storage options based on
requirements**. Determine whether each feature
group needs online storage, offline storage, or both.
Configure the appropriate storage options:

**Online store:** Set up
for low-latency access (milliseconds) needed for
real-time inference
- **Offline store:**
Configure Amazon S3 storage for training and batch
inference workloads
- **Online and offline:**
Implement both for maximum flexibility

- **Implement data ingestion
pipelines**. Develop automated pipelines to ingest
data into your feature store. You can use
[Amazon SageMaker AI Data Wrangler](https://aws.amazon.com/sagemaker/data-wrangler/) for data preparation and
[Amazon SageMaker AI Pipelines](https://aws.amazon.com/sagemaker/pipelines/) for orchestration.
- **Establish feature access
patterns**. Create standardized methods for
retrieving features for both training and inference. For
training, use the offline store with Amazon Athena queries
to efficiently access historical data. For real-time
inference, implement API calls to the online store for
low-latency feature retrieval.
- **Enable cross-account and cross-team
sharing**. Configure resource policies to enable
feature sharing across different teams and AWS accounts.
This promotes collaboration and maximizes feature reuse
across your organization while maintaining appropriate
access controls.
- **Implement feature versioning and
lineage tracking**. Track changes to features over
time using versioning capabilities. Link features to models
through
[Amazon SageMaker AI Model Registry](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry.html) to maintain full lineage
tracking from data source to deployed model.
- **Monitor feature usage and
drift**. Implement monitoring for your feature
store to detect data drift and track feature usage patterns.
Use
[Amazon SageMaker AI Model Monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html) to detect changes in feature
distributions that might impact model performance.
- **Create documentation and discovery
mechanisms**. Document features and their intended
use cases to facilitate discovery and reuse. Implement
tagging and search capabilities so that data scientists can
find relevant features for their projects.
- **Use enhanced Feature Store
capabilities**. Use improved SageMaker AI Feature
Store with better performance, enhanced monitoring
capabilities, and improved integration with other SageMaker AI
services for more efficient feature management.
- **Use generative AI for feature
discovery and documentation**. Use large language
models through
[Amazon
Bedrock](https://aws.amazon.com/bedrock/) to automatically generate feature
descriptions, identify potential feature relationships, and
improve feature discoverability through natural language
search capabilities.

## Resources

**Related documents:**

- [Create,
store, and share features with Feature Store](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store.html)
- [Amazon SageMaker AI Feature Store resources](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store-notebooks.html)
- [Understanding
the key capabilities of Amazon SageMaker AI Feature
Store](https://aws.amazon.com/blogs/machine-learning/understanding-the-key-capabilities-of-amazon-sagemaker-feature-store/)

**Related examples:**

- [Amazon SageMaker AI Feature Store Notebook Examples](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store-notebooks.html)

**Related videos:**

- [Training
and Tuning State-of-the-Art Models with Amazon SageMaker AI](https://aws.amazon.com/awstv/watch/90cac7f03b4/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlcost03-bp04.html*

---

# MLCOST04 — Model development

**Pillar**: Cost Optimization  
**Best Practices**: 14

---

# MLCOST04-BP01 Select optimal computing instance size

Right size your machine learning training instances according to the
algorithm and workload requirements to maximize efficiency and
reduce costs. By selecting the most appropriate computing resources,
you can improve performance while minimizing unnecessary expenses.

**Desired outcome:** You can identify
and select the optimal computing instance types for your machine
learning workloads based on actual resource utilization metrics. You
can systematically evaluate different instance options, understand
their cost implications, and optimize your machine learning
infrastructure spending while maintaining or improving performance.

**Common anti-patterns:**

- Using oversized instances for training jobs regardless of model
complexity.
- Ignoring resource utilization metrics during training.
- Failing to experiment with different instance types to find the
optimal cost-performance balance.
- Not considering the communication overhead in distributed
training scenarios.

**Benefits of establishing this best
practice:**

- Reduced infrastructure costs for machine learning workloads.
- Improved resource utilization and efficiency.
- Better understanding of ML workload performance characteristics.
- Optimization of price-performance ratio for different model
types.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Machine learning training workloads vary significantly in their
resource requirements based on model complexity, dataset size, and
algorithm characteristics. Simple models might not train faster on
larger instances because they cannot effectively utilize
additional compute resources, and might even train slower due to
high GPU communication overhead. By evaluating your workload's
resource needs, you can identify the most cost-effective instance
configuration.

The key to optimizing instance selection is understanding the
actual resource utilization patterns of your machine learning
workloads. Start with smaller instances and scale up only when
necessary based on performance data. Amazon SageMaker AI provides
tools like Debugger to monitor resource utilization and
Experiments to compare training performance across different
instance configurations. This data-driven approach assists you to
avoid paying for unused resources while maintaining optimal
training performance.

### Implementation steps

- **Understand your algorithm's resource
requirements**. Begin by analyzing whether your
machine learning algorithm is compute-bound, memory-bound,
or I/O-bound. Different algorithms have different scaling
characteristics and resource needs. For deep learning
workloads, consider whether GPU acceleration would provide
significant benefits or if CPU instances would be more
cost-effective for your specific model.
- **Use Amazon SageMaker AI
Experiments**.
[Amazon EC2](https://aws.amazon.com/ec2/instance-types/) provides a wide selection of instance types
optimized to fit different use cases. Machine learning
workloads can use either a CPU or a GPU instance. Select an
instance type from
[the
available EC2 instance types](https://aws.amazon.com/ec2/instance-types/) depending on the needs
of your ML algorithm. Experiment with both CPU and GPU
instances to learn which one gives you the best cost
configuration. Amazon SageMaker AI lets you use a single
instance or a distributed cluster of GPU instances. Use
[Amazon SageMaker AI Experiments](https://aws.amazon.com/sagemaker/ai/experiments/) to evaluate alternative
options, and identify the size resulting in optimal outcome.
With the pricing broken down by time and resources, you can
optimize the cost of Amazon SageMaker AI and only pay for
what is needed.
- **Use Amazon SageMaker AI
Debugger**.
[Amazon SageMaker AI Debugger](https://docs.aws.amazon.com/sagemaker/latest/dg/train-debugger.html) automatically monitors the
utilization of system resources, such as GPUs, CPUs,
network, and memory, and profiles your training jobs to
collect detailed ML framework metrics. You can inspect
resource metrics visually through SageMaker AI Studio and
take corrective actions if the resource is under-utilized to
optimize cost.
- **Start small and scale
gradually**. Begin with smaller instance sizes for
new models and monitor performance. Only increase instance
size when you have data showing that your workload can
benefit from additional resources. This approach assists you
to avoid overprovisioning and unnecessary costs.
- **Consider the communication
overhead**. For distributed training across
multiple GPUs or instances, evaluate the communication
overhead between nodes. In some cases, adding more compute
resources might actually slow down training due to increased
coordination requirements.
- **Monitor and analyze training
metrics**. Track key metrics like CPU/GPU
utilization, memory usage, I/O patterns, and training
throughput across different instance types to identify
bottlenecks and optimization opportunities.
- **Use Spot Instances for cost
savings**. For non-critical training jobs, consider
using
[Amazon EC2 Spot Instances](https://aws.amazon.com/ec2/spot/) through SageMaker AI to reduce costs
by up to 90%. Configure your training jobs to checkpoint
regularly to minimize the impact of potential interruptions.
- **Use SageMaker AI Inference Recommender
for optimal instance selection**. Use
[SageMaker AI
Inference Recommender](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-recommender.html) with enhanced algorithms and
support for multi-model endpoints to get sophisticated cost
optimization recommendations for your specific workloads.
- **For generative AI workloads, use
foundation model optimization techniques**. For
generative AI workloads, consider techniques like
quantization, distillation, and efficient fine-tuning
methods to reduce the computational resources needed while
maintaining model quality.
[Amazon SageMaker AI JumpStart](https://aws.amazon.com/sagemaker/jumpstart/) provides optimized foundation
models that can significantly reduce training time and
resource requirements.

## Resources

**Related documents:**

- [Amazon SageMaker AI Debugger](https://docs.aws.amazon.com/sagemaker/latest/dg/train-debugger.html)
- [Accelerate
generative AI development with Amazon SageMaker AI and
MLflow](https://aws.amazon.com/sagemaker/ai/experiments/)
- [Amazon EC2 instance types](https://aws.amazon.com/ec2/instance-types/)
- [Managed
Spot Training in Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/model-managed-spot-training.html)
- [Amazon SageMaker AI Training Compiler](https://docs.aws.amazon.com/sagemaker/latest/dg/training-compiler.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlcost04-bp01.html*

---

# MLCOST04-BP02 Use managed build environments

Using managed build environments for machine learning development
instead of local setups provides significant cost, time, and
resource advantages. Managed notebooks come pre-configured with
security, networking, storage, and compute capabilities that would
otherwise require extensive development and maintenance effort.
These environments also offer flexible machine selection, including
access to powerful GPUs and high-memory instances that may be
impractical in local setups.

**Desired outcome:** You can quickly
start machine learning development work without spending time
setting up infrastructure, managing dependencies, or configuring
development environments. You gain access to scalable compute
resources, including specialized hardware like GPUs, and benefit
from built-in security and collaboration features, allowing you to
focus on building ML models rather than managing infrastructure.

**Common anti-patterns:**

- Spending excessive time configuring local development
environments for each project.
- Encountering hardware limitations when training complex models
locally.
- Struggling with inconsistent development environments across
team members.
- Managing security and networking configurations manually.
- Inability to scale resources up or down based on workload
requirements.

**Benefits of establishing this best
practice:**

- Reduced time to start development with pre-configured
environments.
- Access to powerful compute resources on demand.
- Consistent development environments for team members.
- Built-in security, networking, and storage capabilities.
- Simplified collaboration and sharing of notebooks and models.
- Cost optimization through pay-for-what-you-use model.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

When implementing machine learning projects, your development
environment plays a critical role in productivity and efficiency.
Local development environments often lead to inconsistencies
between team members, dependency conflicts, and hardware
limitations. Managed build environments address these challenges
by providing standardized, scalable, and secure solutions for ML
development.

Amazon SageMaker AI offers several managed environment options
tailored to different user needs and expertise levels. These
include SageMaker AI Notebook Instances for individual developers,
SageMaker AI Studio for comprehensive ML development, and SageMaker AI
Canvas for no-code ML solutions. These environments come
pre-configured with the necessary tools and libraries, saving
setup time and fostering consistency.

These managed environments integrate seamlessly with other AWS
services, making it simple to access data stored in Amazon S3, use
specialized hardware like GPUs, and deploy models to production
endpoints. They also provide built-in security features, version
control, and collaboration capabilities that would be difficult to
implement in a local setup.

### Implementation steps

- **Evaluate your ML development
needs**. Begin by assessing your team's
requirements, including technical expertise, project
complexity, and compute resource needs. Identify which
SageMaker AI offering best matches these requirements.
- **Use Amazon SageMaker AI Notebook
Instances**. Set up SageMaker AI Notebook Instances
which provide a fully managed Jupyter notebook environment.
These instances come pre-loaded with popular ML frameworks
and libraries, allowing you to start working immediately.
- **Implement Amazon SageMaker AI
Studio**. Deploy SageMaker AI Studio as your
comprehensive ML development environment. SageMaker AI Studio
provides a web-based visual interface where your team can
perform ML development steps from data preparation to model
deployment. Access Studio by creating a SageMaker AI domain
through the SageMaker AI console, which enables team management
and resource sharing capabilities.
- **Deploy SageMaker AI Canvas for business
users**. Implement SageMaker AI Canvas for business
analysts and non-technical team members who need to create
ML models without coding. Canvas provides an intuitive
visual interface for importing data, creating models, and
generating predictions.
- **Set up proper IAM roles and
permissions**. Configure appropriate IAM roles for
your SageMaker AI environments to provide secure access to AWS
resources. Create specific roles that follow the principle
of least privilege, granting only the permissions necessary
for your ML workflows.
- **Configure data access and
storage**. Set up connections between your
SageMaker AI environments and data sources such as Amazon S3,
Amazon Redshift, or Amazon RDS. Configure appropriate
permissions to access these data sources securely.
- **Implement version control and
collaboration**. Integrate your managed
environments with version control systems like Git to track
changes to notebooks and code. Use SageMaker AI Studio's
built-in collaboration features to share work among team
members.
- **Optimize for cost
efficiency**. Configure auto-shutdown policies for
notebook instances when they're idle to reduce costs.
Monitor resource usage and adjust instance types as needed
to balance performance and cost.
- **Use SageMaker AI HyperPod for
large-scale training**. For distributed training of
large models, use
[SageMaker AI
HyperPod](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod.html) which provides purpose-built infrastructure
with automatic checkpoint storage and recovery, optimizing
resource utilization for long-running training jobs.
- **Enable SageMaker AI JupyterLab 3
features**. Take advantage of the productivity
improvements in JupyterLab 3, which is available in both
SageMaker AI Studio and Notebook Instances, providing better
performance and enhanced features for developers.

## Resources

**Related documents:**

- [Amazon SageMaker AI Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/studio.html)
- [Amazon SageMaker AI Canvas](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas.html)
- [Amazon SageMaker AI Pricing](https://aws.amazon.com/sagemaker/pricing/)
- [Amazon SageMaker AI notebook instances](https://docs.aws.amazon.com/sagemaker/latest/dg/nbi.html)
- [SageMaker AI
JumpStart pretrained models](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-jumpstart.html)
- [Pipelines](https://docs.aws.amazon.com/sagemaker/latest/dg/pipelines.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlcost04-bp02.html*

---

# MLCOST04-BP03 Select local training for small scale experiments

When developing machine learning models, choosing the right training
environment is crucial for both cost efficiency and rapid
experimentation. By evaluating whether to train your ML model
locally or in the cloud, you can optimize your development workflow
and appropriately match resources to the scale of your experiment.

**Desired outcome:** You can rapidly
iterate on machine learning experiments with small datasets by
training models locally, while having a clear path to scale up to
cloud-based training when working with larger datasets. This
approach enables faster development cycles during the
experimentation phase and cost-effective scaling when required for
production workloads.

**Common anti-patterns:**

- Deploying cloud-based training clusters regardless of dataset
size.
- Using oversized compute instances for small-scale
experimentation.
- Not considering the time and cost implications of repeatedly
launching training clusters during the experimentation phase.
- Failing to right-size compute resources based on specific
workload requirements.

**Benefits of establishing this best
practice:**

- Reduced development costs during experimentation phases.
- Faster iteration cycles when testing various algorithms and
configurations.
- Simplified workflow for early-stage development.
- Clear scaling path from local experimentation to production
deployment.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

When developing machine learning models, you often need to
experiment with multiple algorithms, configurations, and
hyperparameters before finding an optimal solution. The choice
between local training and cloud-based training significantly
impacts both development speed and cost efficiency.

Local training is most advantageous during early experimentation
phases when working with small datasets. This approach reduces the
overhead of provisioning cloud resources and waiting for training
clusters to spin up for each experiment iteration. Your
development cycle becomes more agile as you can quickly test
hypotheses and make adjustments without incurring additional cloud
costs.

As your models and datasets grow in size and complexity,
transitioning to cloud-based training becomes necessary. Cloud
environments offer scalable computing resources that can handle
large datasets and complex models that would be impractical to
process on local machines. By right-sizing your compute instances
based on your specific workload requirements, you can maintain
cost efficiency while gaining the performance benefits of cloud
infrastructure.

### Implementation steps

- **Evaluate your training
requirements**. Before deciding on local or
cloud-based training, assess your dataset size, model
complexity, and computational requirements. Small datasets
(typically under a few gigabytes) and simpler models are
generally good candidates for local training, especially
during initial experimentation.
- **Set up Amazon SageMaker AI local
mode**. When experimenting with small datasets, use
Amazon SageMaker AI's local mode to train models directly on
your notebook instance. This approach allows you to test and
iterate on your code without provisioning separate training
clusters. To implement local mode:

```
`from sagemaker.estimator import Estimator

estimator = Estimator(
image_uri="your-container-image",
role="your-sagemaker-role",
instance_count=1,
instance_type="local"
)

estimator.fit({"train": "s3://your-bucket/train-data"})`
```
- **Use local development environment
with SageMaker AI SDK**. For development outside of
SageMaker AI notebooks, install the SageMaker AI Python SDK on
your local machine. This allows you to develop and test
locally while still having the ability to deploy models to
AWS:

```
`pip install sagemaker`
```
- **Profile your workloads for cloud
deployment**. As your models mature and datasets
grow, prepare for cloud deployment by profiling your
workloads. Identify memory usage, CPU and GPU requirements,
and processing time to determine appropriate instance types
for cloud-based training.
- **Right-size cloud-based training
clusters**. When moving to cloud training, select
appropriate instance types based on your workload profiling.
Consider factors such as:

Model architecture (CPU and GPU requirements)
- Memory needs
- Dataset size and I/O patterns
- Training time constraints
- Cost constraints

- **Implement distributed training for
large-scale workloads**. For large datasets or
complex models, configure distributed training across
multiple instances to reduce training time.
- **Monitor and optimize cloud resource
usage**. Regularly review your training job metrics
to identify opportunities for optimization. Use SageMaker AI
Experiments to track and compare resource utilization across
different training configurations.
- **Use enhanced local development
capabilities**. Use improved SageMaker AI local mode
with better debugging and monitoring capabilities, allowing
for more efficient local experimentation before scaling to
cloud resources.
- **For generative AI workloads, use
foundation models efficiently**. When working with
generative AI and foundation models, consider using Amazon SageMaker AI JumpStart for local experimentation with smaller,
distilled versions of foundation models before fine-tuning
larger models in the cloud. This approach allows for rapid
prototyping while managing costs effectively.

## Resources

**Related documents:**

- [Model
training](https://docs.aws.amazon.com/sagemaker/latest/dg/train-model.html)
- [AWS Pricing Calculator](https://calculator.aws/#/createCalculator/SageMaker AI)
- [What
is Amazon SageMaker AI?](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html)
- [SageMaker AI
Python SDK Documentation](https://sagemaker.readthedocs.io/en/stable/)
- [SageMaker AI
JumpStart pretrained models](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-jumpstart.html)
- [Generative
AI Cost Optimization Strategies](https://aws.amazon.com/blogs/enterprise-strategy/generative-ai-cost-optimization-strategies/)

**Related videos:**

- [Train
with Amazon SageMaker AI on your local machine](https://www.youtube.com/watch?v=K3ngZKF31mc)

**Related examples:**

- [SageMaker AI
Local Mode Examples](https://github.com/aws-samples/amazon-sagemaker-local-mode)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlcost04-bp03.html*

---

# MLCOST04-BP04 Select an optimal ML framework

Selecting the most cost-effective machine learning (ML) framework
for your requirements can significantly impact your operational
efficiency and return on investment. By systematically comparing
frameworks like TensorFlow, PyTorch, and Scikit-learn, you can
determine which delivers the best performance for your specific use
cases at the optimal cost.

**Desired outcome:** You establish a
systematic approach for evaluating ML frameworks and instance types,
and you can select the optimal combination based on performance,
cost, and use case requirements. You can track, compare, and analyze
experiments across different frameworks, leading to informed
decisions that maximize performance while minimizing costs.

**Common anti-patterns:**

- Selecting ML frameworks based on popularity rather than
suitability for your specific use case.
- Using a single framework for ML projects regardless of workload
characteristics.
- Not tracking experiment metrics systematically across different
frameworks.
- Failing to benchmark performance and cost metrics before moving
to production.

**Benefits of establishing this best
practice:**

- Reduced operational costs through optimized infrastructure
selection.
- Improved model performance by selecting the most suitable
framework.
- Enhanced productivity by streamlining experiment tracking and
comparison.
- Faster iteration and deployment of ML models.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Selecting the optimal ML framework involves evaluating different
options against your specific requirements and constraints.
Consider factors such as model complexity, data volume,
performance requirements, and team expertise when choosing between
frameworks. Tracking experiments systematically assists you to
compare approaches objectively and make data-driven decisions.

When implementing this best practice, use AWS' comprehensive ML
infrastructure, which supports major frameworks and provides tools
for experiment tracking and resource optimization. Regular
performance benchmarking and cost analysis should become standard
procedures in your ML development process.

### Implementation steps

- **Implement systematic experiment
tracking with SageMaker AI Experiments**. Amazon SageMaker AI Experiments enables you to organize, track,
compare, and evaluate your machine learning experiments.
Create experiments to group related trials, assign
parameters, metrics, and artifacts to each trial, and track
the lineage of model artifacts to experiments for governance
and reproducibility.
- **Compare multiple ML
frameworks**. Evaluate frameworks like TensorFlow,
PyTorch, Apache MXNet, and Scikit-learn for your specific
use cases. Use
[AWS Deep Learning AMIss](https://aws.amazon.com/machine-learning/amis/) and
[AWS Deep Learning Containers](https://aws.amazon.com/machine-learning/containers/) to experiment with different
frameworks using consistent infrastructure. These AMIs come
with popular frameworks preinstalled, making it simple to
switch between them for comparison.
- **Benchmark framework
performance**. Design standardized benchmarking
tests for your specific workloads across different
frameworks. Track metrics such as training time, inference
latency, memory usage, and accuracy to determine which
framework performs best for your use case.
- **Implement right-sizing strategies
for ML instances**. Use SageMaker AI's managed
instances to automatically select the most appropriate and
cost-effective instance type for your workloads. Experiment
with different instance types to find the optimal balance
between performance and cost.
- **Use SageMaker AI's
bring-your-own-container capability**. If you need
to use specialized ML frameworks or versions not available
in standard containers, use SageMaker AI's flexibility to bring
your own containers so that you can use a framework while
maintaining the benefits of SageMaker AI's managed
infrastructure.
- **Implement automatic resource
scaling**. Configure automatic scaling for
inference endpoints based on traffic patterns to optimize
costs during varying load conditions. Use SageMaker AI
Inference Recommender to identify the best configuration for
deployment.
- **Use enhanced experiment tracking
with MLflow**. Use
[managed
MLflow on SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/mlflow.html) to create, manage, analyze, and
compare your machine learning experiments across different
frameworks with better organization and tracking
capabilities.
- **Monitor and optimize costs
continuously**. Implement cost monitoring using AWS Cost Explorer and SageMaker AI's built-in monitoring
capabilities. Set up alerts for unusual spending patterns
and regularly review resource utilization to identify
optimization opportunities.

## Resources

**Related documents:**

- [AWS Deep Learning AMIss](https://aws.amazon.com/machine-learning/amis/)
- [Machine
Learning Frameworks and Languages](https://docs.aws.amazon.com/sagemaker/latest/dg/frameworks.html)
- [Accelerate
generative AI development with Amazon SageMaker AI and
MLflow](https://aws.amazon.com/sagemaker/ai/experiments/)
- [Amazon SageMaker AI Studio Classic](https://docs.aws.amazon.com/sagemaker/latest/dg/studio.html)
- [Amazon SageMaker AI Inference Recommender](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-recommender.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlcost04-bp04.html*

---

# MLCOST04-BP05 Use automated machine learning

Automate your model development process by using systems that
experiment with and select the best algorithms from high-performing
options. These automated systems test various solutions and
parameter settings to achieve optimal models, significantly speeding
up development while reducing the need for manual experimentation
and comparisons.

**Desired outcome:** You gain the
ability to develop high-quality machine learning models in a
fraction of the time traditionally required. By using automated
machine learning tools like Amazon SageMaker AI Autopilot, you can
focus on business problems rather than algorithm selection and
parameter tuning. Your team can produce optimized models with better
performance, reduce development costs, and accelerate time-to-market
for ML-powered solutions.

**Common anti-patterns:**

- Manually testing multiple algorithms and configurations one by
one.
- Spending excessive time on hyperparameter tuning without
systematic approach.
- Using the same algorithm for each problem without considering
alternatives.
- Neglecting cross-validation during model selection.

**Benefits of establishing this best
practice:**

- Dramatically reduced time to develop production-ready models.
- Access to a broader range of algorithms and optimization
techniques.
- Improved model performance through systematic evaluation.
- Lower costs through optimized resource utilization.
- Ability for domain experts to build models without deep ML
expertise.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Automated machine learning (AutoML) systems democratize the
process of building machine learning models. By automating key
steps in model development—from data preparation to algorithm
selection and hyperparameter tuning—these systems enable even
those without extensive machine learning expertise to develop
high-quality models.

When using AutoML solutions like Amazon SageMaker AI Autopilot,
you provide your dataset and define your objective, and the system
handles the complex work of exploring potential algorithms,
optimizing parameters, and evaluating model performance. The
system applies cross-validation procedures automatically to check
that models can generalize well to new data. By ranking optimized
models by their performance, AutoML can identify the best solution
for your specific problem.

Beyond simply producing models, modern AutoML systems provide
visibility into the development process, allowing you to
understand what choices were made and why. This transparency
builds trust in the models and provides learning opportunities for
your team to understand what approaches work best for different
problem types.

### Implementation steps

- **Evaluate your use case
compatibility**. Determine if your ML problem is
suitable for automated machine learning solutions. AutoML
works particularly well for standard machine learning tasks
like classification, regression, and some time series
forecasting scenarios.
- **Prepare your data for
AutoML**. Clean your dataset, handle missing
values, and convert categorical features appropriately.
While AutoML handles feature engineering, providing
high-quality data improves results. Use
[Amazon SageMaker AI Data Wrangler](https://aws.amazon.com/sagemaker/data-wrangler/) to simplify this preparation
process.
- **Set up Amazon SageMaker AI Autopilot
with Canvas**. Open
[Amazon SageMaker AI Canvas](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas.html), import your dataset into Amazon S3,
and configure to access this data. Define your target
variable and specify your problem type (classification or
regression) if known.
- **Launch the automated ML
job**. Start Canvas training and let it analyze
your data, select algorithms, and optimize models. Specify
resources like maximum runtime and instance types to control
costs. Canvas will automatically handle data preprocessing,
feature engineering, algorithm selection, and hyperparameter
optimization.
- **Review candidate models**.
Examine the generated models along with their performance
metrics. Autopilot provides detailed reports on the data
exploration, feature engineering decisions, and model
optimization steps it performed.
- **Deploy the best model**.
Select the best-performing model from the Canvas
recommendations and deploy it using Amazon SageMaker AI's
deployment capabilities. You can deploy as a real-time
endpoint or for batch inference depending on your needs.
- **Monitor and evaluate
performance**. Set up model monitoring to track
your model's performance in production and detect concept
drift. Use
[Amazon SageMaker AI Model Monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html) to automate this process.
- **Customize and refine
models**. If needed, extract and customize the
models generated by Autopilot. The solution provides full
visibility into the notebooks and artifacts it creates,
allowing you to further refine specific aspects of the
model.
- **Enhance model development with
foundation models**. Use
[Amazon
Bedrock](https://aws.amazon.com/bedrock/) to incorporate foundation model capabilities
into your AutoML workflow for tasks like text processing,
content generation, and multimodal applications. Foundation
models can complement traditional ML approaches handled by
Autopilot.
- **Use enhanced Canvas capabilities
with Q integration**. Use
[SageMaker AI
Canvas](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas.html) with improved natural language support and Q
integration for conversational data analysis, enabling
business users to build models through natural language
interactions.
- **Implement intelligent preprocessing
with generative AI**. Use generative AI tools to
enhance data preprocessing, augment training datasets,
generate synthetic data for edge cases, and improve feature
engineering through intelligent text and image processing.

## Resources

**Related documents:**

- [Getting
started with using Amazon SageMaker AI Canvas](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-getting-started.html)
- [SageMaker AI
Canvas](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas.html)
- [Amazon SageMaker AI Data Wrangler](https://aws.amazon.com/sagemaker/data-wrangler/)

**Related examples:**

- [SageMaker AI Autopilot](https://github.com/aws/sagemaker-python-sdk/blob/master/src/sagemaker/automl/README.rst)
- [Amazon SageMaker AI Autopilot Sample Notebooks](https://github.com/aws/amazon-sagemaker-examples/tree/main/autopilot)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlcost04-bp05.html*

---

# MLCOST04-BP06 Use managed training capabilities

Machine learning model training can be an iterative,
compute-intensive, and time-consuming process. Instead of using the
notebook itself, which might be running on a small instance,
offloading the training to a managed cluster of compute resources
including both CPUs and GPUs enables more efficient and
cost-effective model training.

**Desired outcome:** By using managed
training capabilities, you optimize your machine learning training
workflows and infrastructure management. You gain access to scalable
computing resources that automatically adjust based on your workload
needs, from single GPUs to thousands, without managing the
underlying infrastructure. You can significantly reduce training
costs through specialized hardware options, compiler optimizations,
and spot instance utilization while maintaining visibility into
metrics and logs for proper monitoring and governance.

**Common anti-patterns:**

- Running complex model training jobs on notebook instances,
leading to resource constraints and inefficiency.
- Managing your own GPU clusters for training, requiring
significant operational overhead.
- Using exclusively on-demand instances for training jobs,
resulting in higher costs.
- Not using specialized training optimizations like distributed
training or compiler acceleration.

**Benefits of establishing this best
practice:**

- Lower training costs by up to 90% using managed spot instances.
- Accelerate training time by up to 50% with training compiler
optimizations.
- Scale resources automatically based on training job
requirements.
- Track and monitor training experiments and resource utilization
effectively.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Machine learning training is computationally intensive and can
become prohibitively expensive when not optimized properly. Using
managed training capabilities allows you to focus on model
development while the infrastructure scales and optimizes
automatically to your needs. Managed training services provide a
range of optimization options from distributed training across
multiple GPUs to cost-saving options through spot instances.
Additionally, these services integrate with monitoring tools to
track resource utilization, model metrics, and training progress
to continually refine your training approach.

For example, when training large language models, you can use
SageMaker AI's distributed training libraries to split the model
across multiple GPUs and instances, reducing training time from
weeks to days while maintaining control over your training costs
through automatic scaling and spot instance usage.

### Implementation steps

- **Use Amazon SageMaker AI managed
training capabilities**. Amazon SageMaker AI
reduces the time and cost to train and tune ML models
without the need to manage infrastructure. With SageMaker AI, you can train and tune ML models using built-in tools to
manage and track training experiments, automatically choose
optimal hyperparameters, debug training jobs, and monitor
the utilization of system resources such as GPUs, CPUs, and
network bandwidth. SageMaker AI can automatically scale
infrastructure up or down based on your training job
requirements, from one GPU to thousands, or from terabytes
to petabytes of storage. SageMaker AI also offers the
highest-performing ML compute infrastructure currently
available-including
[Amazon EC2 P4d instances](https://aws.amazon.com/ec2/instance-types/p4/), which can reduce ML training costs
by up to 60% compared with previous generations. And, since
you pay only for what you use, you can manage your training
costs more effectively.
- **Use Spot Instances for cost
optimization**. Amazon SageMaker AI makes it simple
to train machine learning models using managed Amazon EC2
Spot Instances. Managed Spot training can optimize the cost
of training models up to 90% over On-demand Instances.
SageMaker AI manages the Spot interruptions on your behalf.
You can specify which training jobs use Spot Instances and a
stopping condition that specifies how long SageMaker AI
waits for a job to run using Spot Instances. Metrics and
logs generated during training runs are available in Amazon CloudWatch.
- **Configure optimal data
sources**. Select the appropriate data source for
your training job to optimize performance and cost. Consider
using [Amazon S3](https://aws.amazon.com/s3/) for persistent storage,
[Amazon FSx for Lustre](https://aws.amazon.com/fsx/lustre/) for high-performance file systems, or
[Amazon EFS](https://aws.amazon.com/efs/) based on your specific training requirements and
dataset characteristics.
- **Implement experiment tracking and
management**. Use
[Amazon SageMaker AI Experiments](https://aws.amazon.com/sagemaker/ai/experiments/) to track training jobs, compare
results, and manage different versions of your models. This
provides visibility into model performance, resource
utilization, and training metrics to optimize future
iterations.
- **Use SageMaker AI HyperPod for
large-scale training**. Use
[SageMaker AI
HyperPod](https://aws.amazon.com/sagemaker/ai/hyperpod/) to scale and accelerate generative AI model
development across thousands of AI accelerators with
purpose-built infrastructure, automatic checkpoint storage
and recovery, and support for both Slurm and Amazon EKS for
cluster orchestration.
- **For generative AI, optimize large
language model training**. Use
[SageMaker AI
Model Parallelism](https://docs.aws.amazon.com/sagemaker/latest/dg/model-parallel-v2.html) to efficiently distribute model
parameters across multiple devices and instances. Consider
using
[Amazon
Bedrock](https://aws.amazon.com/bedrock/) for foundation model access and fine-tuning
capabilities to further reduce the computational cost of
training generative AI models from scratch.

## Resources

**Related documents:**

- [SageMaker AI
HyperPod](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod.html)
- [Managed
Spot Training in Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/model-managed-spot-training.html)
- [Train
a Model with Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/how-it-works-training.html)
- [Model
training](https://docs.aws.amazon.com/sagemaker/latest/dg/train-model.html)
- [Distributed
training in Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/distributed-training.html)
- [Accelerate
generative AI development with Amazon SageMaker AI and
MLflow](https://aws.amazon.com/sagemaker/ai/experiments/)

**Related examples:**

- [SageMaker AI
Examples GitHub Repository](https://github.com/aws/amazon-sagemaker-examples)
- [SageMaker AI
Training Workshop](https://github.com/aws-samples/amazon-sagemaker-immersion-day)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlcost04-bp06.html*

---

# MLCOST04-BP07 Use distributed training

Accelerate your machine learning model training process by utilizing
distributed computing resources, which can significantly reduce
training time and optimize costs. Amazon SageMaker AI distributed
training capabilities enable efficient processing of large models
and datasets across multiple compute instances.

**Desired outcome:** You achieve
faster training times for your machine learning models by
distributing the workload across multiple instances. You optimize
resource utilization and reduce overall training costs by using
SageMaker AI's managed distributed training capabilities, which
automatically handle infrastructure provisioning and termination
when training completes. This approach allows you to train complex
models that may be too large for a single machine or train standard
models much faster through parallel processing.

**Common anti-patterns:**

- Training large models on a single instance even when they could
benefit from distribution.
- Manually managing distributed training infrastructure rather
than using managed services.
- Keeping training instances running after training is complete.
- Implementing custom distributed training code when built-in
libraries would suffice.

**Benefits of establishing this best
practice:**

- Significantly reduced training time for large models and
datasets.
- Cost optimization through efficient resource utilization.
- Ability to train models that are too large to fit on a single
GPU.
- Automatic infrastructure management with no need to maintain
distributed training clusters.
- Enhanced team productivity by reducing waiting time for model
results.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Distributed training allows you to split your machine learning
workloads across multiple compute instances to accelerate the
training process. This approach is particularly valuable when
working with large models or datasets that would otherwise take
too long to train on a single instance. Amazon SageMaker AI provides
built-in support for distributed training through its specialized
libraries that handle the complexity of distributing workloads
efficiently.

When implementing distributed training, you need to consider the
most appropriate approach based on your model architecture and
data size. Data parallelism works by dividing your dataset across
multiple GPUs, with each GPU having a complete copy of the model.
This approach is ideal for scenarios where your model fits on a
single GPU but training on the full dataset is time-consuming.
Alternatively, model parallelism is designed for situations where
your model is too large to fit on a single GPU. In this case, the
model itself is partitioned across multiple GPUs.

SageMaker AI's distributed training libraries automatically handle
the communication between nodes and optimize the distribution
strategy, making it straightforward to scale your training
workloads without managing the underlying infrastructure.

### Implementation steps

- **Evaluate your workload for
distributed training suitability**. Assess if your
training job would benefit from distribution by considering
factors like model size, dataset size, and current training
times. Ideal candidates are models that take hours or days
to train on a single instance or models too large to fit in
a single GPU's memory.
- **Choose the appropriate distributed
training approach**. Select between data
parallelism and model parallelism based on your specific
needs. Use data parallelism when your model fits on a single
GPU but you want to process data faster. Use model
parallelism when your model is too large to fit on a single
GPU.
- **Utilize Amazon SageMaker AI distributed
training libraries**. Implement distributed
training using
[SageMaker AI's
distributed training libraries](https://aws.amazon.com/sagemaker/distributed-training/), which automatically
handle the complexities of distributing workloads across
multiple instances. These libraries provide optimized
implementations for both data parallelism and model
parallelism strategies.
- **Configure your training
cluster**. Define the number and type of instances
for your training cluster in your SageMaker AI training job
configuration. Consider using GPU-optimized instance types
like P3, P4d, or G4dn based on your model requirements and
budget constraints.
- **Adapt your training script for
distributed processing**. Modify your training code
to work with SageMaker AI's distributed training libraries. For
data parallelism, you'll need to use the SageMaker AI data
parallelism library to distribute data across workers. For
model parallelism, you'll integrate the SageMaker AI model
parallelism library to partition your model across devices.
- **Monitor and optimize training
performance**. Use
[Amazon SageMaker AI Debugger](https://docs.aws.amazon.com/sagemaker/latest/dg/train-debugger.html) to monitor your distributed
training jobs, identify bottlenecks, and optimize resource
utilization. Analyze metrics like GPU utilization,
communication overhead, and training throughput to fine-tune
your distributed training configuration.
- **Consider Amazon SageMaker AI HyperPod
for persistent training clusters of foundation
models**. For workloads requiring long-running or
repeated distributed training jobs, use
[Amazon SageMaker AI HyperPod](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod.html) to create persistent, managed
clusters that can handle multiple training jobs efficiently
while maintaining cost optimization through automatic
scaling and resource management.
- **Use SageMaker AI HyperPod for
persistent training clusters**. Use
[SageMaker AI
HyperPod](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod.html) for workloads requiring long-running or
repeated distributed training jobs, providing persistent,
managed clusters with automatic scaling, checkpoint storage
and recovery, and support for various instance types
including P5e, G6, and Trn2.
- **Use AI-powered code generation for
distributed training implementation**. Use
AI-powered development tools like
[Amazon Q Developer](https://aws.amazon.com/q/developer/) and
[Kiro](https://kiro.ai/) to generate
complex distributed training code, automate infrastructure
setup scripts, and accelerate the implementation of
distributed training workflows.
- **Consider Amazon Bedrock for
fine-tuning foundation models**. For generative AI
applications, consider using
[Amazon
Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/custom-model-fine-tuning.html/) for fine-tuning foundation models, model
distillation, or continued pretraining, which provides
optimized distributed training capabilities specifically
designed for large language models.

## Resources

**Related documents:**

- [Run
distributed training with the SageMaker AI distributed data
parallelism library](https://docs.aws.amazon.com/sagemaker/latest/dg/data-parallel.html)
- [SageMaker AI
model parallelism library v2](https://docs.aws.amazon.com/sagemaker/latest/dg/model-parallel-v2.html)
- [Amazon SageMaker AI HyperPod](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-hyperpod.html)
- [Distributed
Training](https://sagemaker-examples.readthedocs.io/en/latest/training/distributed_training/index.html)
- [Amazon SageMaker AI XGBoost now offers fully distributed GPU
training](https://aws.amazon.com/blogs/machine-learning/amazon-sagemaker-xgboost-now-offers-fully-distributed-gpu-training/)

**Related examples:**

- [Distributed
Training](https://github.com/aws/amazon-sagemaker-examples/blob/master/training/distributed_training/index.rst)
- [Distributed
training using Amazon SageMaker AI Distributed Data Parallel
library and debugging using Amazon SageMaker AI Debugger](https://github.com/aws-samples/amazon-sagemaker-dist-data-parallel-with-debugger)
- [SageMaker AI
developer guide on distributed training](https://github.com/awsdocs/amazon-sagemaker-developer-guide/blob/master/doc_source/distributed-training.md#distributed-training-optimize)
- [Distributed
Training Examples](https://github.com/aws/amazon-sagemaker-examples/tree/main/training/distributed_training)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlcost04-bp07.html*

---

# MLCOST04-BP08 Stop resources when not in use

Stop resources that are not in use to reduce cost. For example,
hosted Jupyter environments used to explore small samples of data
can be stopped when not actively in use. Where practical, commit the
work, stop them, and restart when needed. The same approach can be
used to stop the computing and the data storage services.

**Desired outcome:** You
significantly reduce your ML infrastructure costs by only paying for
resources when they are actively being used. You have automated
systems in place to monitor and shut down idle resources, along with
proper alerts to track spending patterns and avoid unexpected
charges. You maintain the ability to quickly restart resources when
needed while minimizing wasteful spending on idle compute and
storage.

**Common anti-patterns:**

- Leaving development environments running regardless of actual
usage.
- Neglecting to set up automatic shutdown mechanisms for idle
resources.
- Ignoring cost monitoring tools and billing alerts.
- Using persistent storage for temporary data that could be
deleted.

**Benefits of establishing this best
practice:**

- Significant cost savings (up to 75% by running resources only
during business hours compared to running continually).
- Better alignment of spending with actual usage patterns.
- Reduced environmental impact through more efficient resource
consumption.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Optimizing costs is a crucial aspect of running machine learning
workloads in the cloud. ML workloads often require significant
computational resources, but those resources aren't needed
continuously. By implementing automatic shutdown mechanisms for
idle resources, you can achieve substantial cost savings while
maintaining the ability to rapidly resume work when needed.

For ML development environments like SageMaker AI notebooks, the
cost-optimization opportunity is particularly significant since
these environments are typically used intermittently during the
exploration and development phases. By committing code to
repositories regularly and shutting down environments when not in
use, you improve both cost efficiency and version control of your
work.

Additionally, proper monitoring of spending patterns assists you
in identifying optimization opportunities and avoiding unexpected
costs. With AWS tools, you can set up alerts, track resource
utilization, and implement automated responses to idle resources.

### Implementation steps

- **Set up Amazon CloudWatch billing
alarms**. Use
[Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/monitor_estimated_charges_with_cloudwatch.html) to monitor your estimated AWS charges.
When you enable monitoring of estimated charges, these
calculations are sent several times daily to CloudWatch as
metric data. Configure alerts to be notified when your
resource charges exceed predefined thresholds to stay within
budget and quickly identify unexpected spending patterns.
- **Configure Amazon SageMaker AI notebook
lifecycle configurations**. Create
[lifecycle
configurations](https://docs.aws.amazon.com/sagemaker/latest/dg/notebook-lifecycle-config.html) that include shell scripts to run when
you create or start notebook instances. These scripts can
check for notebook instance activity and automatically shut
down idle instances. This way, you're not paying for compute
resources when they aren't actively processing workloads.
- **Implement Amazon SageMaker AI Studio
idle shutdown**. For
[Amazon SageMaker AI Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-idle-shutdown.html) environments, install the
auto-shutdown JupyterLab extension either
[manually
or automatically](https://github.com/aws-samples/sagemaker-studio-auto-shutdown-extension). This extension detects idle Studio
resources and can shut down individual components, including
notebooks, terminals, kernels, applications, and instances
when they're not being used.
- **Use AWS Cost Explorer to identify
optimization opportunities**. Regularly analyze
your ML infrastructure spending patterns using
[AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) to identify resources that might be
consistently underutilized. Look for patterns that indicate
resources could benefit from scheduled shutdowns during
off-hours.
- **Implement instance
scheduling**. Use the
[AWS Instance Scheduler](https://aws.amazon.com/solutions/implementations/instance-scheduler/) to create automated schedules for
starting and stopping resources based on your team's working
hours. This is particularly useful for development
environments that are only needed during business hours.
- **Train teams on cost-aware
practices**. Educate your ML teams on the
importance of shutting down resources when not in use and
committing their work regularly. Create a cost-aware culture
where resource efficiency is valued alongside development
productivity.
- **Implement enhanced auto-shutdown
capabilities**. Use improved SageMaker AI Studio
auto-shutdown features with better idle detection and more
granular control over resource shutdown policies to minimize
costs from unused resources.
- **Use Spot Instances for interruptible
workloads**. For ML training jobs that can handle
interruptions, use
[Amazon EC2 Spot Instances](https://aws.amazon.com/ec2/spot/) to achieve significant cost
savings compared to on-demand pricing. Make sure your
workloads are designed to checkpoint progress and can resume
from interruptions.

## Resources

**Related documents:**

- [Idle
shutdown](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-idle-shutdown.html)
- [Customization
of a SageMaker AI notebook instance using an LCC script](https://docs.aws.amazon.com/sagemaker/latest/dg/notebook-lifecycle-config.html)
- [Instance
Scheduler on AWS](https://aws.amazon.com/solutions/implementations/instance-scheduler/)
- [Create
a billing alarm to monitor your estimated AWS charges](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/monitor_estimated_charges_with_cloudwatch.html)
- [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/)
- [Amazon SageMaker AI Pricing](https://aws.amazon.com/sagemaker/pricing/)
- [Cloud
Financial Management with AWS](https://aws.amazon.com/aws-cost-management/)

**Related videos:**

- [Saving
cost on your machine learning training and inference on
AWS](https://www.youtube.com/watch?v=keowy9YfxlcDeploy)
- [Deploy
an ML model for best performance, cost, and prediction
quality](https://www.youtube.com/watch?v=ftCFf57dQQY)

**Related examples:**

- [AWS CloudFormation templates for automated instance
scheduling](https://github.com/aws-solutions/aws-instance-scheduler)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlcost04-bp08.html*

---

# MLCOST04-BP09 Start training with small datasets

Start experimentation with smaller datasets on a small compute
instance or local system. This approach allows you to iterate
quickly at low cost. After the experimentation period, scale up to
train with the full dataset available on a separate compute cluster.
Choose the appropriate storage layer for training data based on the
performance requirements.

**Desired outcome:** You can develop
your machine learning models cost-effectively by starting with small
datasets for rapid iteration and experimentation. When you're
confident in your approach, you scale up to the full dataset on
appropriate compute resources. This progressive scaling methodology
optimizes both development time and infrastructure costs while
maintaining the flexibility to refine your models before committing
to full-scale training.

**Common anti-patterns:**

- Immediately training with the full dataset on large instances,
leading to excessive costs during experimentation.
- Using the same compute resources for both experimentation and
full-scale training.
- Not planning for the transition from small-scale to large-scale
training.

**Benefits of establishing this best
practice:**

- Reduced costs during the experimentation phase.
- Faster iteration cycles for model development.
- More efficient use of compute resources.
- Ability to identify and fix issues early in the development
process.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Machine learning development often requires multiple iterations to
achieve optimal results. Using smaller, representative samples of
your dataset during initial experimentation can significantly
reduce costs and increase productivity. This approach lets you
rapidly test various model architectures, hyperparameters, and
preprocessing techniques without the expense and time required to
process the full dataset.

When implementing this approach, check that your smaller dataset
properly represents the characteristics of your full dataset to
avoid developing models that don't generalize well. Once you've
established effective approaches using the smaller dataset, you
can scale up your training to use the complete dataset on
appropriately sized compute resources.

The cloud makes this approach particularly powerful, as you can
scale your compute resources to match your current phase of
development. For example, you might use a notebook instance with
modest resources during experimentation, then transition to
distributed training on a cluster of more powerful instances when
you're ready for full-scale training.

### Implementation steps

- **Create a representative subset of
your data**. Extract a small but representative
sample of your full dataset that maintains the same
distribution of features and classes as your original data.
Aim for 10-20% of your data or a size that can be processed
on your local machine or small instance.
- **Set up SageMaker AI notebook instances
for experimentation**.
[Amazon SageMaker AI notebook instances](https://docs.aws.amazon.com/sagemaker/latest/dg/nbi.html) provide a hosted Jupyter
environment ideal for exploring and experimenting with your
sample dataset. Choose a smaller instance type to keep costs
low during experimentation.
- **Configure notebook lifecycle
management**. Use
[lifecycle
configuration scripts](https://github.com/aws-samples/amazon-sagemaker-notebook-instance-lifecycle-config-samples) to automate the setup of your
development environment, including installing necessary
libraries and dependencies when your notebook instance
starts.
- **Develop and iterate on your
model**. Use the notebook environment to build,
train and evaluate your models on the sample data. Take
advantage of this faster iteration cycle to explore
different approaches, hyperparameters, and preprocessing
techniques.
- **Test scaling
considerations**. Before moving to full-scale
training, test your code with slightly larger data samples
to identify scaling issues that might arise when processing
the full dataset.
- **Prepare for distributed
training**. Once your approach is validated with
the sample data, refactor your code as needed to support
distributed training using SageMaker AI's distributed training
capabilities.
- **Scale up compute resources for full
training**. Launch appropriately sized training
instances or clusters for your full-scale training job.
SageMaker AI training jobs allow you to select the instance
type and count that matches your workload requirements.
- **Monitor training metrics and
costs**. Use Amazon CloudWatch to track the
performance and resource utilization of your training jobs
to check that they're running efficiently.

## Resources

**Related documents:**

- [Amazon SageMaker AI notebook instances](https://docs.aws.amazon.com/sagemaker/latest/dg/nbi.html)
- [Amazon SageMaker AI Studio Lab](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-lab.html)
- [Customization
of a SageMaker AI notebook instance using an LCC script](https://docs.aws.amazon.com/sagemaker/latest/dg/notebook-lifecycle-config.html)
- [Distributed
training in Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/distributed-training.html)

**Related examples:**

- [SageMaker AI
Notebook Instance Lifecycle Config Samples](https://github.com/aws-samples/amazon-sagemaker-notebook-instance-lifecycle-config-samples)
- [SageMaker AI
Local Mode](https://github.com/aws-samples/amazon-sagemaker-local-mode)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlcost04-bp09.html*

---

# MLCOST04-BP10 Use warm start and checkpointing hyperparameter tuning

When training machine learning models, you can significantly reduce
time and costs by using previous training efforts. This practice
shows how to use warm start and checkpointing techniques in
hyperparameter tuning to accelerate your model development process
and optimize resource utilization.

**Desired outcome:** You can create
more efficient hyperparameter tuning jobs by using knowledge from
previous tuning efforts and saved model states. By implementing warm
start capabilities, you can initialize new tuning jobs with
information from previous runs, avoiding unnecessary repetition.
With checkpointing, you can save intermediate model states during
training, allowing you to resume jobs from the last checkpoint
rather than starting from scratch. These techniques enable you to
accelerate your model development process, reduce computational
costs, and find optimal hyperparameter configurations more
efficiently.

**Common anti-patterns:**

- Starting every hyperparameter tuning job from scratch without
using previous knowledge.
- Not saving model checkpoints during lengthy training jobs,
risking complete loss of progress if interrupted.
- Using unnecessarily wide hyperparameter search ranges when
previous jobs have already identified promising areas.

**Benefits of establishing this best
practice:**

- Lower computational costs through more efficient resource
utilization.
- Accelerated convergence to optimal model configurations.
- Improved resilience to training interruptions through checkpoint
recovery.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Hyperparameter tuning is an essential but computationally
intensive part of machine learning model development. Without warm
start capabilities, each tuning job begins with no prior
knowledge, potentially wasting resources by exploring
already-evaluated hyperparameter combinations. Without
checkpointing, an interrupted training job must restart from the
beginning, losing progress.

You can overcome these inefficiencies by implementing warm start
and checkpointing strategies in your ML workflow. Warm start
allows you to use knowledge from previous hyperparameter tuning
jobs, focusing the search on promising areas of the hyperparameter
space. Checkpointing enables you to save model states periodically
during training, providing a recovery point if training is
interrupted.

Amazon SageMaker AI offers built-in support for both warm start and
checkpointing capabilities. For warm start, you can specify one or
more parent tuning jobs whose results inform the new job's
hyperparameter search. SageMaker AI offers two warm start types:
TRANSFER_LEARNING for adapting knowledge to new
datasets and IDENTICAL_DATA_AND_ALGORITHM for
continuing tuning with the same dataset. For checkpointing, you
can configure your training jobs to periodically save model states
to Amazon S3, which can be used to resume training if needed.

### Implementation steps

- **Configure warm start for
hyperparameter tuning jobs**. Set up a new
hyperparameter tuning job that builds upon the knowledge
gained from previous tuning jobs. In Amazon SageMaker AI, you
can configure this by specifying one or more parent tuning
jobs and selecting an appropriate warm start type. This
approach is particularly effective when you want to refine
hyperparameter search after initial exploration or adapt a
model to a similar dataset.
- **Select appropriate parent jobs for
warm start**. Choose parent jobs that are relevant
to your current tuning objective. The best parent jobs are
those that used similar datasets, algorithms, or
optimization objectives. In SageMaker AI, you can specify up to
five parent jobs when configuring a warm start tuning job.
- **Choose the right warm start
type**. Select
IDENTICAL_DATA_AND_ALGORITHM when
continuing tuning with the same dataset and algorithm, or
TRANSFER_LEARNING when adapting knowledge
to a new but related dataset or problem. The warm start type
determines how SageMaker AI will use information from the
parent jobs.
- **Configure checkpointing for training
jobs**. Enable checkpointing in your training
script by saving model states at regular intervals. In
SageMaker AI, specify a checkpoint S3 location where these
model states will be stored. This allows you to resume
training from the last saved checkpoint if a job is
interrupted or if you want to extend training later.
- **Implement checkpoint saving in your
training code**. Add callback functions in your ML
framework (such as TensorFlow, PyTorch, or MXNet) to
periodically save model states during training. These
frameworks typically provide built-in checkpoint
functionality that you can configure with minimal code
changes.
- **Set up checkpoint recovery
mechanisms**. Configure your training jobs to check
for existing checkpoints at startup and resume from the
latest checkpoint if available. In SageMaker AI, you can
specify the checkpoint configuration when creating a
training job, including the S3 location where checkpoints
are stored.
- **Optimize hyperparameter search
ranges based on previous results**. When using warm
start, refine your hyperparameter search ranges based on
promising values identified in parent jobs. Narrowing search
ranges around previously successful values can significantly
improve tuning efficiency.
- **Run parallel hyperparameter tuning
jobs strategically**. Use warm start to distribute
the hyperparameter tuning workload across multiple jobs that
can share knowledge. This approach is particularly effective
for exploring large hyperparameter spaces efficiently.
- **Monitor and evaluate warm start
efficiency**. Track the performance and efficiency
gains from warm start by comparing with cold-start
approaches. This analysis refines your warm start strategy
for future jobs.
- **Use enhanced hyperparameter tuning
capabilities**. Use improved SageMaker AI
hyperparameter tuning with better algorithms and support for
multi-objective optimization to find optimal configurations
more efficiently.
- **Use generative AI for hyperparameter
selection**. Use large language models to suggest
promising hyperparameter ranges based on model architecture
and dataset characteristics. Generative AI can identify
sensible starting points for hyperparameter tuning jobs,
especially for new model architectures.

## Resources

**Related documents:**

- [Run
a Warm Start Hyperparameter Tuning Job](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-warm-start.html)
- [Checkpoints
in Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/model-checkpoints.html)
- [Automatic
model tuning in Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning.html)
- [HyperparameterTuner](https://sagemaker.readthedocs.io/en/stable/api/training/tuner.html)

**Related examples:**

- [Automatic
Model Tuning: Warm Starting Tuning Jobs](https://github.com/aws/amazon-sagemaker-examples/blob/master/hyperparameter_tuning/image_classification_warmstart/hpo_image_classification_warmstart.ipynb)
- [Hyperparameter
Optimization with Checkpointing Example](https://github.com/aws/amazon-sagemaker-examples/tree/master/hyperparameter_tuning)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlcost04-bp10.html*

---

# MLCOST04-BP11 Use hyperparameter optimization technologies

Optimize your machine learning models through automatic
hyperparameter tuning to find the optimal model configuration with
minimal manual effort, reducing the time and resources needed to
achieve peak model performance.

**Desired outcome:** You achieve
better performing machine learning models by using automatic
hyperparameter optimization technologies that run multiple training
jobs in parallel. You can efficiently explore a wide range of
hyperparameter combinations to find the optimal configuration that
maximizes model performance according to your specified metrics,
ultimately delivering better business results while reducing the
time and resources spent on manual tuning.

**Common anti-patterns:**

- Manually tuning hyperparameters through trial and error.
- Using a narrow range of hyperparameter values that don't
adequately explore the solution space.
- Selecting arbitrary hyperparameter values without considering
the specific requirements of your business problem.
- Running one training job at a time instead of using parallel
capabilities.

**Benefits of establishing this best
practice:**

- Reduced time to develop high-performing machine learning models.
- Lower computational costs by efficiently exploring the
hyperparameter space.
- Consistent and repeatable approach to model optimization.
- Ability to scale hyperparameter tuning efforts across multiple
algorithms.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

*Hyperparameter optimization (HPO)* is a
critical aspect of developing effective machine learning models.
Unlike model parameters that are learned during training,
hyperparameters are configuration variables that govern the
training process itself and significantly impact model
performance. Finding the optimal combination of hyperparameters
manually is time-consuming and inefficient.

By implementing automatic hyperparameter tuning, you can
systematically explore the hyperparameter space and identify the
configuration that maximizes model performance. SageMaker AI's
automatic model tuning service employs techniques like Bayesian
optimization to intelligently search through the hyperparameter
space, focusing computational resources on the most promising
regions and accelerating the discovery of the optimal
configuration.

When implementing hyperparameter optimization, you should define
appropriate search spaces for your hyperparameters based on domain
knowledge and previous experiments. You also need to select
relevant evaluation metrics that align with your business
objectives. For classification problems, this might include
accuracy, F1 score, or AUC-ROC, while for regression problems, it
could be mean squared error or mean absolute error.

### Implementation steps

- **Identify key hyperparameters for
your model**. Begin by determining which
hyperparameters have the greatest impact on your model's
performance. For neural networks, this might include
learning rate, batch size, and network architecture
parameters. For tree-based models, this could include tree
depth, number of trees, and minimum samples per leaf.
- **Define appropriate hyperparameter
ranges**. Establish meaningful ranges for each
hyperparameter based on domain knowledge and best practices
for your chosen algorithm. Use logarithmic scales for
parameters that span multiple orders of magnitude (like
learning rate) for efficient exploration.
- **Select relevant evaluation
metrics**. Choose metrics that align with your
business requirements and the problem you're solving. Check
that these metrics provide a meaningful assessment of model
performance in the context of your specific application.
- **Configure SageMaker AI automatic model
tuning**. Create a hyperparameter tuning job using
the
[SageMaker AI
Python SDK](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning.html) or the SageMaker AI console. Specify the
algorithm or framework you're using, the hyperparameter
ranges, and the evaluation metric to optimize.
- **Implement early stopping for
efficiency**. Enable early stopping features to
automatically terminate poorly performing training jobs,
saving computational resources. SageMaker AI can monitor the
evaluation metric during training and stop jobs that are
unlikely to produce competitive models.
- **Use warm start for incremental
tuning**. Use the warm start feature to accelerate
new hyperparameter tuning jobs by using information from
previous tuning jobs, reducing the time and resources needed
to find optimal configurations.
- **Implement parallel training
jobs**. Configure SageMaker AI to run multiple
training jobs concurrently to explore different
hyperparameter combinations simultaneously, dramatically
reducing the time required to find optimal values.
- **Analyze tuning job
results**. Review the performance of different
hyperparameter combinations to understand how each parameter
affects model performance. Use this information to refine
your hyperparameter ranges for future tuning jobs.
- **Select the best model for
deployment**. After the tuning job completes,
identify the best-performing model based on your evaluation
metric and deploy it using SageMaker AI's deployment
capabilities.
- **Use no-code hyperparameter
optimization**. Use
[SageMaker AI
Canvas](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas.html) with enhanced capabilities for business users
to perform hyperparameter optimization through natural
language interfaces without requiring deep technical
expertise.
- **Document hyperparameter
configurations**. Maintain comprehensive
documentation of hyperparameter configurations, tuning
strategies, and results to facilitate knowledge sharing and
reproducibility.

## Resources

**Related documents:**

- [Automatic
model tuning with SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning.html)
- [Stop
Training Jobs Early](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-early-stopping.html)
- [Best
Practices for Hyperparameter Tuning](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-considerations.html)
- [Create
a Hyperparameter Optimization Tuning Job for One or More
Algorithms (Console)](https://docs.aws.amazon.com/sagemaker/latest/dg/multiple-algorithm-hpo-create-tuning-jobs.html)
- [Run
a Warm Start Hyperparameter Tuning Job](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-warm-start.html)

**Related examples:**

- [SageMaker AI
examples - hyperparameter tuning](https://github.com/aws/amazon-sagemaker-examples/tree/main/hyperparameter_tuning)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlcost04-bp11.html*

---

# MLCOST04-BP12 Set up a budget and use resource tagging to track costs

Setting up budgets and implementing resource tagging for machine
learning workloads provides clear visibility into your ML-related
expenses and optimizes costs across your organization. By tracking
costs effectively, you can make data-driven decisions about resource
allocation and identify opportunities for cost optimization.

**Desired outcome:** You gain
complete visibility into your machine learning costs across
development, training, and production environments. You can track
expenses by project, business unit, or environment, allowing for
accurate cost allocation and forecasting. Through tagging and
budgeting tools, you can proactively manage your ML spending,
receive alerts before exceeding budgeted amounts, and make informed
decisions about resource provisioning and termination.

**Common anti-patterns:**

- Running ML workloads without cost monitoring mechanisms in
place.
- Using generic cost tracking that doesn't differentiate between
ML projects or environments.
- Failing to tag ML resources consistently, making cost allocation
difficult.
- Ignoring budget alerts or failing to take action when exceeding
thresholds.

**Benefits of establishing this best
practice:**

- Clear visibility into where ML spending occurs across your
organization.
- Ability to accurately allocate costs to specific projects or
business units.
- Early warning through alerts when costs exceed or are forecasted
to exceed budgeted amounts.
- Improved governance and financial accountability for ML
initiatives.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Cost management is a critical aspect of running machine learning
workloads in the cloud. Without proper cost tracking and budget
controls, ML expenses can quickly escalate due to
compute-intensive training jobs, large storage requirements for
datasets, and continuous inference endpoints. By implementing
comprehensive budgeting and tagging strategies, you gain
visibility and control over these costs.

AWS provides several tools that work together to track, analyze,
and optimize your ML costs. AWS Budgets allows you to set custom
budgets for your SageMaker AI resources, while AWS Cost Explorer
provides visualization and analysis capabilities to understand
spending patterns. Resource tagging serves as the foundation for
detailed cost tracking, enabling you to categorize expenses by
project, team, environment, or other dimension important to your
organization.

For example, you might tag resources related to a fraud detection
model with a Project tag value of
FraudDetection and an
Environment tag value of
Production. This allows you to track the total
cost of this specific ML use case across its components, from
development notebooks to training jobs to deployment endpoints.

### Implementation steps

- **Set up AWS Budgets for ML cost
tracking**. Create customized budgets in AWS
Budgets to monitor your Amazon SageMaker AI costs across
development, training, and hosting. Configure the budget to
track specific services (such as SageMaker AI) or specific
tagged resources. Set thresholds for actual costs and
forecasted costs to receive notifications before you exceed
your budget. This gives you time to make adjustments to your
resource usage if needed. Access your budgets through the
[AWS Budgets console](https://aws.amazon.com/aws-cost-management/aws-budgets/) to track progress and make
adjustments as necessary.
- **Implement a tagging strategy for ML
resources**. Develop a consistent tagging strategy
for all your ML resources. Define mandatory tags such as
Project, BusinessUnit, Environment (dev/test/prod), and
Owner. Document your tagging standards and verify that team
members understand and follow these standards. Apply these
tags to relevant resources, including
[Amazon SageMaker AI](https://aws.amazon.com/sagemaker/) notebook instances, training jobs, models,
endpoints, and related resources like
[Amazon S3](https://aws.amazon.com/s3/) buckets for dataset storage.
- **Activate cost allocation
tags**. After implementing your tagging strategy,
activate your tags as cost allocation tags in the AWS Billing and Cost Management console. Note that it may take up to 24 hours for
newly activated tags to appear in your cost management
tools. Once activated, you can use your tags to filter and
group costs in AWS Cost Explorer and other cost reporting
tools.
- **Configure detailed cost analysis
using AWS Cost Explorer**. Use
[AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) to visualize and analyze your ML costs
over time. Create custom reports that filter costs by
specific tags (like Project or Environment) or by specific
services like SageMaker AI. Set up regular reports to track
spending trends, identify cost spikes, and understand usage
patterns. Use the insights gained to optimize your resource
allocation and scheduling for ML workloads.
- **Create cost anomaly
detection**. Set up
[AWS Cost Anomaly Detection](https://aws.amazon.com/aws-cost-management/aws-cost-anomaly-detection/) to automatically identify
unusual spending patterns in your ML workloads. Configure
alerts to notify relevant stakeholders when anomalies are
detected. This assists you in quickly identifying and
addressing unexpected cost increases, which can happen with
ML workloads due to extended training times or inefficient
resource usage.
- **Establish cost governance
processes**. Create clear processes for reviewing
costs, responding to budget alerts, and making cost
optimization decisions. Assign responsibility for cost
monitoring to specific individuals or teams. Conduct regular
cost reviews with stakeholders to discuss spending trends,
identify optimization opportunities, and align ML resource
usage with business priorities. Document cost-saving actions
taken and their impact on the overall budget.
- **Optimize ML resources based on cost
data**. Use the cost insights gained from your
tagging and budgeting tools to optimize ML resource usage.
Identify underutilized notebook instances that can be
stopped when not in use. Select appropriate instance types
based on workload requirements. Consider using
[Amazon SageMaker AI Managed Spot Training](https://docs.aws.amazon.com/sagemaker/latest/dg/model-managed-spot-training.html) to reduce training
costs by up to 90%. Implement auto-scaling for inference
endpoints to match capacity with demand.

## Resources

**Related documents:**

- [Managing
your costs with AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html)
- [Organizing
and tracking costs using AWS cost allocation tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html)
- [Getting
started with AWS Cost Anomaly Detection](https://docs.aws.amazon.com/cost-management/latest/userguide/getting-started-ad.html)
- [Best
Practices for Tagging AWS Resources](https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/tagging-best-practices.html)
- [Cost
Optimization Pillar - AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/welcome.html)
- [Amazon SageMaker AI Pricing](https://aws.amazon.com/sagemaker/pricing/)
- [AWS Cloud Financial Management](https://aws.amazon.com/aws-cost-management/)
- [Analyze
Amazon SageMaker AI spend and determine cost optimization
opportunities based on usage, Part 4: Training jobs](https://aws.amazon.com/blogs/machine-learning/part-4-analyze-amazon-sagemaker-spend-and-determine-cost-optimization-opportunities-based-on-usage-part-4-training-jobs/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlcost04-bp12.html*

---

# MLCOST04-BP13 Enable data and compute proximity

Positioning data and compute resources in the same AWS Region
reduces data transfer costs and improves processing speeds for
machine learning workloads. By minimizing the physical distance
between data storage and compute resources, you can significantly
decrease latency and avoid cross-region data transfer fees.

**Desired outcome:** You achieve
cost-efficient and high-performance machine learning operations by
placing your data and compute resources in the same AWS Region. You
experience faster training times, reduced latency, and avoid
unnecessary data transfer costs that can significantly impact your
ML project budgets.

**Common anti-patterns:**

- Storing data in one Region and running compute resources in
another Region.
- Repeatedly transferring large datasets across Regions for
training or inference.
- Failing to consider the impact of data transfer costs on overall
ML project budgets.

**Benefits of establishing this best
practice:**

- Decreased latency for data access during model training and
inference.
- Improved overall machine learning workflow performance.
- Simplified management of data compliance and sovereignty
requirements.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Data transfer costs between AWS Regions can significantly impact
your machine learning project's budget, especially when working
with large datasets that are repeatedly accessed during model
training. By keeping your compute resources in the same Region as
your data storage, you minimize these costs and improve
performance.

When planning your machine learning infrastructure on AWS,
consider data locality as a primary design principle. For example,
if your organization stores datasets in Amazon S3 buckets in the
US West (Oregon) Region, you should provision EC2 instances,
SageMaker AI notebooks, or other ML compute resources in that same
Region.

This principle applies to various machine learning scenarios,
including model training, data preprocessing, and inference. Even
though AWS provides high-speed network connections between
Regions, the laws of physics still impose latency limitations, and
cross-Region data transfers incur additional costs that can be
avoided.

### Implementation steps

- **Identify data storage
locations**. Determine where your primary data is
stored on AWS. Check which Regions contain your Amazon S3
buckets, Amazon EFS file systems, or other storage services
holding your training data. Use the AWS Management Console,
AWS CLI, or infrastructure as code tools to inventory your
data storage resources across Regions.
- **Audit compute resource
placement**. Review your current machine learning
compute resources, including Amazon EC2 instances, Amazon SageMaker AI notebooks, and training jobs. Verify if they are
in the same Regions as your data sources. Use AWS Cost Explorer and AWS Trusted Advisor to identify cross-Region
data transfer costs that may indicate misaligned resources.
- **Consolidate resources by
Region**. When creating new compute resources for
machine learning workloads, consistently provision them in
the same Region as your data. For example, if using
[Amazon SageMaker AI](https://aws.amazon.com/sagemaker/), create your notebook instances, training
jobs, and endpoints in the Region where your training data
is stored in Amazon S3.
- **Use Regional data transfer
analysis**. Review your AWS billing information to
identify and quantify cross-Region data transfer costs. The
[AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) service can assist you in analyzing
data transfer costs between AWS services and across Regions.
Set up cost allocation tags to track expenses related to
machine learning projects specifically.
- **Consider data replication for
specific use cases**. In scenarios requiring
multi-Region deployments for high availability or disaster
recovery, implement a data replication strategy to maintain
copies of datasets in each Region where compute resources
exist. Services like
[Amazon S3 Cross-Region Replication](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html) can automate this process
while managing costs.
- **Leverage edge computing for
distributed ML workloads**. When working with data
that exists at the edge of the network, consider using
[AWS Outposts](https://aws.amazon.com/outposts/),
[AWS Wavelength](https://aws.amazon.com/wavelength/), or
[AWS Local Zones](https://aws.amazon.com/about-aws/global-infrastructure/localzones/) to bring compute resources closer to your
data sources, especially for applications requiring
low-latency inference.
- **Implement data caching
strategies**. For frequently accessed data,
implement caching solutions like
[Amazon ElastiCache](https://aws.amazon.com/elasticache/) or
[Amazon DynamoDB Accelerator (DAX)](https://aws.amazon.com/dynamodb/dax/) in the same Region as your
compute resources to further reduce latency and data
transfer costs.

## Resources

**Related documents:**

- [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/)
- [Replicating
objects within and across Regions](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html)
- [AWS Data Transfer Pricing](https://aws.amazon.com/ec2/pricing/on-demand/#Data_Transfer)
- [AWS Local Zones](https://aws.amazon.com/about-aws/global-infrastructure/localzones/)
- [AWS Outposts](https://aws.amazon.com/outposts/)
- [Regions
and Zones](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html)
- [AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlcost04-bp13.html*

---

# MLCOST04-BP14 Select optimal algorithms

Selecting optimal algorithms for machine learning (ML) workloads is
crucial for balancing cost efficiency and performance. By
identifying appropriate ML paradigms and carefully evaluating
algorithmic choices, you can optimize both technical performance and
business outcomes while managing costs.

**Desired outcome:** You are able to
identify the most suitable ML algorithm for your specific use case
that balances accuracy, explainability, computational requirements,
and cost efficiency. You can conduct effective trade-off analyses
between different approaches and use AWS services to optimize
algorithm selection, training, and deployment.

**Common anti-patterns:**

- Using complex deep learning solutions without first exploring
simpler algorithms.
- Ignoring the explainability requirements of the business use
case.
- Failing to consider data constraints when selecting algorithms.
- Not evaluating computational and maintenance costs alongside
accuracy metrics.

**Benefits of establishing this best
practice:**

- Reduced computational costs by using algorithms appropriate for
the specific problem.
- Improved model performance through systematic comparison of
algorithm options.
- Enhanced model explainability when required by business
stakeholders.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Selecting the optimal algorithm requires understanding your
specific ML problem type and the business constraints around it.
Begin by categorizing your problem into basic ML paradigms:
supervised learning (for labeled data), unsupervised learning (for
unlabeled data), or reinforcement learning (for sequential
decision problems). Consider what matters most for your use case,
whether it's prediction accuracy, model explainability, inference
speed, or a balance of these factors.

Algorithm selection significantly impacts both the performance and
cost efficiency of your ML solutions. A computationally expensive
algorithm might deliver marginally better accuracy but at
substantially higher operational costs. Similarly, a complex but
highly accurate algorithm might sacrifice the explainability
needed for regulatory adherence or business transparency. Finding
the right balance requires systematic experimentation and
evaluation against your business requirements.

AWS provides various services test, compare, and optimize
algorithms, allowing you to make data-driven decisions about which
approach delivers the best value for your specific use case.

### Implementation steps

- **Define your machine learning problem
type**. Categorize your problem as supervised
learning (classification, regression), unsupervised learning
(clustering, dimensionality reduction), or reinforcement
learning. This initial classification narrows down the
appropriate algorithms to consider.
- **Determine business requirements and
constraints**. Document specific accuracy targets,
explainability needs, inference time requirements, and
budget constraints. These requirements will serve as
criteria for evaluating algorithm options.
- **Start with simple algorithms
first**. Begin experimentation with simpler
algorithms like linear or logistic regression, decision
trees, or k-means clustering before moving to more complex
approaches. These algorithms are computationally efficient,
simpler to interpret, and establish important baselines for
performance comparison.
- **Conduct structured
experimentation**. Use
[Amazon SageMaker AI Experiments](https://docs.aws.amazon.com/sagemaker/latest/dg/experiments.html) to track different algorithm
trials, hyperparameter configurations, and their results.
This creates reproducibility and facilitates comparison
between approaches.
- **Perform comprehensive trade-off
analysis**. When comparing algorithms, consider
multiple dimensions beyond accuracy:

Data requirements (amount needed for training)
- Computational resources required for training and
inference
- Model explainability and interpretability
- Deployment complexity and operational overhead
- Long-term maintenance costs

- **Use AWS optimized algorithms and
frameworks**. Use
[Amazon SageMaker AI built-in algorithms](https://docs.aws.amazon.com/sagemaker/latest/dg/algos.html) that are optimized for
performance and cost-efficiency on AWS infrastructure. AWS
also provides optimized versions of popular frameworks like
TensorFlow, PyTorch, and MXNet that include performance
enhancements for training across
[Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html) instance families.
- **Consider automated ML
approaches**. For exploratory projects or when
seeking optimal performance with minimal manual tuning, use
SageMaker AI Canvas for rapid algorithm prototyping with the
ability to export generated code to notebooks for further
customization.
- **Explore pre-trained
models**. Search AWS Marketplace for pre-trained
models that can accelerate development through transfer
learning or direct deployment. Pre-trained models can
significantly reduce computational costs and development
time.
- **Implement continuous
evaluation**. As new algorithms and model versions
emerge, periodically reassess whether your chosen approach
remains optimal. Business requirements and available
technologies evolve over time.
- **Document algorithm selection
rationale**. Create clear documentation explaining
why specific algorithms were selected, what trade-offs were
accepted, and how these decisions align with business
requirements.
- **For generative AI projects, consider
foundation models from
[Amazon
Bedrock](https://aws.amazon.com/bedrock/) for natural language processing, image
generation, and other tasks where these models can provide
state-of-the-art performance with lower development
costs.** Use techniques like prompt engineering and
fine-tuning to adapt foundation models to your specific
business needs while avoiding the computational expense of
training from scratch.

## Resources

**Related documents:**

- [Built-in
algorithms and pretrained models in Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/algos.html)
- [Accelerate
generative AI development using managed MLflow on Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/mlflow.html#mlflow-tracking)
- [How
custom models work](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-build-model.html)
- [Types
of Algorithms](https://docs.aws.amazon.com/sagemaker/latest/dg/algorithms-choose.html)
- [SageMaker AI
JumpStart pretrained Models](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-jumpstart.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlcost04-bp14.html*

---

# MLCOST05 — Deployment

**Pillar**: Cost Optimization  
**Best Practices**: 3

---

# MLCOST05-BP01 Use an appropriate deployment option

Use the right deployment option for your machine learning models to
optimize cost and performance based on your specific use case
requirements. Select real-time inference for low latency
applications, batch transform for large datasets, or edge deployment
for applications that require local processing.

**Desired outcome:** You have an
optimized model deployment strategy that balances performance and
cost efficiency. You can choose the appropriate deployment option
based on your specific use case requirements, whether that's
real-time inference for low-latency applications, batch processing
for large datasets, or edge deployment for scenarios requiring local
processing.

**Common anti-patterns:**

- Using real-time endpoints for deployment scenarios regardless of
traffic patterns.
- Overlooking serverless or asynchronous options when they would
be more cost-effective.
- Deploying separate endpoints for each model when multiple models
could be hosted more efficiently together.
- Running inference in the cloud when edge deployment would be
more efficient for local data processing.
- Overprovisioning compute resources for inference endpoints.

**Benefits of establishing this best
practice:**

- Cost optimization through selection of the most efficient
deployment option for each use case.
- Improved performance by matching deployment options to specific
latency requirements.
- Increased operational efficiency through managed inference
services.
- Flexibility to handle varying inference workloads and traffic
patterns.
- Simplified ML model management across cloud and edge
environments.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

When deploying machine learning models, selecting the right
deployment option is crucial for achieving optimal performance and
cost efficiency. Amazon SageMaker AI provides multiple deployment
options that can be tailored to your specific use case
requirements. Real-time inference is ideal for applications
requiring low latency responses, such as real-time recommendations
or fraud detection. Batch transform is better suited for
processing large datasets in offline mode, such as document
processing or periodic scoring jobs. Edge deployment brings
inference capabilities directly to edge devices, reducing latency
and bandwidth requirements while enabling offline processing.

Consider the pattern of requests your application needs to handle.
If you need consistent, low-latency responses for interactive
applications with steady traffic, real-time inference is
appropriate. If you process data in batches without immediate
response requirements, batch transform offers cost efficiency. For
applications with unpredictable or bursty traffic patterns,
serverless inference can automatically scale to match demand while
minimizing costs during idle periods. For workloads with large
payloads or long processing times, asynchronous inference provides
a queuing mechanism that improves efficiency.

Also consider resource utilization. Multi-model endpoints and
multi-container endpoints enable you to optimize costs by sharing
resources across multiple models or containers. This approach is
particularly valuable when you have many models with variable
usage patterns or complementary resource requirements.

### Implementation steps

- **Evaluate your inference
requirements**. Determine your application's needs
for latency, throughput, payload size, and traffic patterns.
Consider whether your application requires real-time
responses or can process data in batches. Assess if your
models should run in the cloud or at the edge based on
connectivity, latency requirements, and data privacy
considerations.
- **Use Amazon SageMaker AI for model
deployment**.
[Amazon SageMaker AI](https://aws.amazon.com/sagemaker/) offers a comprehensive set of deployment
options to optimize price-performance for most use cases.
It's a fully managed service that integrates with MLOps
tools for effective model management in production with
reduced operational burden.
- **Select the appropriate inference
option based on your use case**. Choose from
several SageMaker AI inference options:

[Amazon SageMaker AI Real-time Inference](https://docs.aws.amazon.com/sagemaker/latest/dg/realtime-endpoints.html) for low-latency,
interactive applications requiring immediate responses
- [Amazon SageMaker AI Serverless Inference](https://docs.aws.amazon.com/sagemaker/latest/dg/serverless-endpoints.html) for workloads with
intermittent or unpredictable traffic patterns
- [Amazon SageMaker AI Asynchronous Inference](https://docs.aws.amazon.com/sagemaker/latest/dg/async-inference.html) for large
payload sizes, long processing times, or when immediate
responses aren't required
- [Amazon SageMaker AI Batch Transform](https://docs.aws.amazon.com/sagemaker/latest/dg/batch-transform.html) for offline processing
of large datasets

- **Implement multi-model endpoints for
cost optimization**. Use
[Amazon SageMaker AI Multi-Model Endpoints](https://docs.aws.amazon.com/sagemaker/latest/dg/multi-model-endpoints.html) to deploy multiple
models on a single endpoint with shared container resources.
This approach improves endpoint utilization and reduces
hosting costs compared to single-model endpoints. SageMaker AI
manages the loading of models into memory and scales them
based on traffic patterns.
- **Deploy multiple containers on a
single endpoint**. Implement
[SageMaker AI
multi-container endpoints](https://docs.aws.amazon.com/sagemaker/latest/dg/multi-container-endpoints.html) to deploy multiple
containers using different models or frameworks on a single
endpoint. Run containers in sequence as an inference
pipeline or access each container individually through
direct invocation to improve endpoint utilization and
optimize costs.
- **Automate endpoint changes through a
pipeline**. Use
[Amazon SageMaker AI Pipelines](https://docs.aws.amazon.com/sagemaker/latest/dg/pipelines.html) to automate the model deployment
process. Create CI/CD pipelines that handle model training,
evaluation, and deployment, enabling consistent and
repeatable deployment processes.
- **Monitor and optimize your
deployment**. Implement continuous monitoring of
your inference endpoints to track performance metrics, cost,
and resource utilization. Use this data to fine-tune your
deployment strategy and make adjustments as needed to
optimize for cost efficiency and performance.
- **Use AI-powered code generation for
deployment automation**. Use AI-powered development
tools like
[Amazon Q Developer](https://aws.amazon.com/q/developer/) and
[Kiro](https://kiro.ai/) to generate
deployment scripts, automate infrastructure configuration,
and accelerate the implementation of optimal deployment
strategies.
- **For generative AI workloads,
consider deployment options for foundation
models**. Evaluate specialized deployment options
like
[Amazon
Bedrock](https://aws.amazon.com/bedrock/) for fully managed foundation models or
[SageMaker AI
JumpStart](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart.html) for pre-trained models with optimized
deployment configurations.

## Resources

**Related documents:**

- [Deploy
models for inference](https://docs.aws.amazon.com/sagemaker/latest/dg/deploy-model.html)
- [Deploy
models with Amazon SageMaker AI Serverless Inference](https://docs.aws.amazon.com/sagemaker/latest/dg/serverless-endpoints.html)
- [Multi-model
endpoints](https://docs.aws.amazon.com/sagemaker/latest/dg/multi-model-endpoints.html)
- [Batch
transform for inference with Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/batch-transform.html)
- [Hosting
options](https://docs.aws.amazon.com/sagemaker/latest/dg/realtime-endpoints-options.html)
- [Asynchronous
inference](https://docs.aws.amazon.com/sagemaker/latest/dg/async-inference.html)
- [Model
deployment at the edge with SageMaker AI Edge Manager](https://docs.aws.amazon.com/sagemaker/latest/dg/edge.html)
- [Inference
pipelines in Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-pipelines.html)

**Related examples:**

- [SageMaker AI
Serverless Inference Walkthrough](https://github.com/aws/amazon-sagemaker-examples/blob/main/serverless-inference/Serverless-Inference-Walkthrough.ipynb)
- [SageMaker AI
Edge Manager Workshop](https://github.com/aws-samples/amazon-sagemaker-edge-manager-workshop)
- [SageMaker AI
Asynchronous Inference Examples](https://github.com/aws/amazon-sagemaker-examples/tree/main/async-inference)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlcost05-bp01.html*

---

# MLCOST05-BP02 Explore cost effective hardware options

Machine learning models that power AI applications are becoming
increasingly complex resulting in rising underlying compute
infrastructure costs. Up to 90% of the infrastructure spend for
developing and running ML applications is often on inference. Look
for cost-effective infrastructure solutions for deploying their ML
applications in production.

**Desired outcome:** You achieve
significant cost savings while maintaining or improving the
performance of your machine learning inference workloads. By
implementing cost-effective hardware options, you optimize your
infrastructure spend, reduce operational costs, and can allocate
resources more efficiently across your ML applications. Your ML
models run on purpose-built hardware that provides the right balance
of performance and cost for your specific use case.

**Common anti-patterns:**

- Using general-purpose compute instances for ML workloads without
considering specialized hardware options.
- Over-provisioning inference resources to handle peak loads
without implementing scaling strategies.
- Ignoring model optimization opportunities before deploying to
production.
- Selecting hardware based solely on performance metrics without
considering cost-efficiency.

**Benefits of establishing this best
practice:**

- Reduced infrastructure costs for ML model inference.
- Improved inference throughput and latency.
- More efficient use of computational resources.
- Lower total cost of ownership for AI applications.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Machine learning inference costs represent a significant portion
of the total expenses associated with running ML workloads in
production. As models become more complex, their computational
requirements increase, which can lead to higher infrastructure
costs. Selecting the right hardware for your ML workloads is
crucial for maintaining cost efficiency without sacrificing
performance.

AWS offers multiple options to optimize the cost and performance
of your ML inference workloads. These include services that
optimize models for specific hardware targets, instances that
provide cost-effective acceleration for inference workloads, and
deployment options that match your specific latency and throughput
requirements.

Evaluating your specific workload requirements is essential before
selecting hardware options. Consider factors such as latency
requirements, throughput needs, model complexity, batch size
capabilities, and budget constraints. This evaluation will assist
you to determine the most appropriate hardware solution for your
use case.

### Implementation steps

- **Use Amazon SageMaker AI Neo for model
optimization**. Amazon SageMaker AI Neo automatically
optimizes machine learning models for inference on cloud
instances and edge devices. For inference in the cloud,
SageMaker AI Neo speeds up inference and saves cost by creating
an inference optimized container in SageMaker AI hosting. For
inference at the edge, SageMaker AI Neo saves developers months
of manual tuning by automatically tuning the model for the
selected operating system and processor hardware. Neo
optimizes models trained in TensorFlow, PyTorch, MXNet, and
other frameworks for deployment on ARM, Intel, and NVIDIA
processors.
- **Deploy on Amazon EC2 Inf2
Instances**. Amazon EC2 Inf1 instances deliver
high-performance ML inference at the lowest cost in the
cloud. They deliver up to 2.3-times higher throughput and up
to 70% lower cost per inference than comparable current
generation GPU-based Amazon EC2 instances. Inf1 instances
are built from the ground up to support machine learning
inference applications. They feature up to 16 AWS Inferentia
chips, high-performance machine learning inference chips
designed and built by AWS. Additionally, Inf1 instances
include second generation Intel Xeon Scalable processors and
up to 100 Gbps networking to deliver high throughput
inference.
- **Explore Amazon EC2 Inf2
Instances**. The second generation of AWS
Inferentia-based instances, EC2 Inf2 instances, offer even
greater performance improvements over previous generations.
These instances are powered by AWS Inferentia2 chips and
provide up to 4x higher throughput and up to 10x lower
latency than Inf1 instances. They're ideal for more complex
generative AI models and large language models (LLMs) that
require high performance and cost-effective inference
solutions.
- **Consider Amazon SageMaker AI serverless
inference**. SageMaker AI serverless inference is a
purpose-built inference option that automatically
provisions, scales, and shuts down compute capacity based on
your workload needs. This pay-per-use model can reduce costs
by avoiding the need to continuously run instances when
there are no inference requests, making it ideal for
workloads with intermittent traffic patterns.
- **Evaluate batch and asynchronous
inference options**. For non-real-time inference
requirements, consider using SageMaker AI batch transform for
offline inference processing or SageMaker AI asynchronous
inference for workloads that can tolerate higher latency.
These options often allow for more efficient resource
utilization and lower costs compared to real-time inference
endpoints.
- **Implement automated scaling
policies**. Configure auto-scaling for your
SageMaker AI endpoints to dynamically adjust the number of
instances based on workload demands. This way, you can pay
for the resources you need while maintaining performance
requirements during peak usage periods.
- **Use enhanced SageMaker AI Inference
Recommender**. Use
[SageMaker AI
Inference Recommender](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-recommender.html) with enhanced algorithms and
support for multi-model endpoints to get sophisticated cost
optimization recommendations for your specific workloads.
- **Regularly monitor and analyze
inference costs**. Use AWS Cost Explorer and Amazon CloudWatch metrics to track your inference costs and
performance metrics. Regularly review this data to identify
optimization opportunities and adjust your hardware strategy
accordingly.

## Resources

**Related documents:**

- [Model
performance optimization with SageMaker AI Neo](https://docs.aws.amazon.com/sagemaker/latest/dg/neo.html)
- [Amazon EC2 Inf2 Instances](https://aws.amazon.com/ec2/instance-types/inf2/)
- [AWS Inferentia](https://aws.amazon.com/machine-learning/inferentia/)
- [Amazon SageMaker AI Inference Recommender](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-recommender.html)
- [Deploy
models for inference](https://docs.aws.amazon.com/sagemaker/latest/dg/deploy-model.html)
- [Deploy
models with Amazon SageMaker AI Serverless Inference](https://docs.aws.amazon.com/sagemaker/latest/dg/serverless-endpoints.html)
- [Asynchronous
inference](https://docs.aws.amazon.com/sagemaker/latest/dg/async-inference.html)

**Related examples:**

- [AWS Neuron SDK Examples for Inferentia and Trainium
instances](https://github.com/aws-neuron/aws-neuron-sdk)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlcost05-bp02.html*

---

# MLCOST05-BP03 Right-size the model hosting instance fleet

Use efficient compute resources to run models in production. In many
cases, up to 90% of the infrastructure spend for developing and
running an ML application is on inference, making it critical to use
high-performance, cost-effective ML inference infrastructure.
Selecting the right way to host and the right type of instance can
have a large impact on the total cost of ML projects. Use automatic
scaling for your hosted models. Auto scaling dynamically adjusts the
number of instances provisioned for a model in response to changes
in your workload.

**Desired outcome:** You optimize
your ML infrastructure costs while maintaining performance by using
the right instance types and quantities for your model deployments.
You use automated tools to recommend the most cost-effective
configurations and implement dynamic scaling that adjusts capacity
based on actual demand patterns, resulting in significant cost
savings and consistent performance.

**Common anti-patterns:**

- Using the same instance types for each model regardless of their
specific requirements.
- Maintaining static instance counts rather than scaling with
workload demands.
- Selecting instance types based solely on performance without
considering cost implications.
- Not distributing model instances across multiple availability
zones for resilience.

**Benefits of establishing this best
practice:**

- Reduced ML infrastructure costs by up to 90% through optimal
instance selection.
- Improved model performance through use of appropriately sized
resources.
- Enhanced reliability through automatic scaling and multi-AZ
deployment.
- Better handling of variable workloads without performance
degradation.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Optimizing ML inference costs requires a careful balance between
performance and cost. When selecting compute resources for model
hosting, consider both the model's specific requirements and the
expected workload patterns. CPU instances may be sufficient for
many traditional ML models, while GPU instances deliver better
performance for deep learning models but at a higher cost. The key
is using the right resource for the specific workload.

Amazon SageMaker AI provides tools that can automatically select
the optimal instance type and size for your models. By testing
different configurations, you can find the sweet spot that
delivers the required performance at the lowest possible cost.
Additionally, implementing auto scaling assists in verifying that
your deployment can handle varying loads efficiently, scaling up
during peak demand and down during quiet periods to avoid
unnecessary costs.

### Implementation steps

- **Use Amazon SageMaker AI Inference
Recommender for instance selection**. Amazon SageMaker AI Inference Recommender automatically selects the
right compute instance type, instance count, container
parameters, and model optimizations for inference to
maximize performance and minimize cost. You can use
SageMaker AI Inference Recommender from SageMaker AI Studio,
the AWS Command Line Interface (AWS CLI), or the AWS SDK,
and within minutes, get recommendations to deploy your ML
model. You can then deploy your model to one of the
recommended instances or run a fully managed load test on a
set of instance types you choose without worrying about
testing infrastructure. You can review the results of the
load test in SageMaker AI Studio and evaluate the tradeoffs
between latency, throughput, and cost to select the most
optimal deployment configuration.
- **Configure auto scaling for SageMaker AI
endpoints**. Amazon SageMaker AI supports an auto
scaling feature that monitors your workloads and dynamically
adjusts the capacity to maintain steady and predictable
performance at the lowest possible cost. When the workload
increases, auto scaling brings more instances online. When
the workload decreases, auto scaling removes unnecessary
instances, which can reduce your compute cost. SageMaker AI
automatically attempts to distribute your instances across
Availability Zones. So, we strongly recommend that you
deploy multiple instances for each production endpoint for
high availability. If you're using a VPC, configure at least
two subnets in different Availability Zones so Amazon SageMaker AI can distribute your instances across those
Availability Zones.
- **Implement proper scaling
policies**. Define appropriate scaling policies
based on your model's performance characteristics and usage
patterns. Set scaling metrics such as CPU utilization, GPU
utilization, model latency, or custom metrics that reflect
your workload's needs. Define appropriate target values and
cooldown periods to avoid rapid scaling oscillations.
- **Consider serverless inference
options**. For workloads with unpredictable or
intermittent traffic patterns, evaluate
[Amazon SageMaker AI Serverless Inference](https://docs.aws.amazon.com/sagemaker/latest/dg/serverless-endpoints.html), which automatically
provisions and scales compute capacity based on traffic.
This option reduces the need to select instance types or
manage scaling policies while providing pay-per-use pricing.
- **Regularly review and optimize
deployments**. Set up a process to periodically
review your model deployments' performance and cost metrics.
As your models evolve and usage patterns change, rerun
Inference Recommender tests to keep your infrastructure
optimized. Look for opportunities to consolidate models or
use multi-model endpoints where appropriate.
- **Use SageMaker AI Training Plans for
predictable access**. Use
[SageMaker AI
Training Plans](https://aws.amazon.com/sagemaker/pricing/) as a compute reservation system for
predictable access to high-demand GPU resources, managing
large-scale AI training workloads more efficiently with
better resource planning and scheduling capabilities.
- **Use model optimization
techniques**. For large language models and other
generative AI workloads, consider techniques like
quantization, distillation, or pruning to reduce model size
and computational requirements. Amazon SageMaker AI supports
optimization techniques through
[SageMaker AI
Neo](https://docs.aws.amazon.com/sagemaker/latest/dg/neo.html) and integration with
[AWS Neuron](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/) for optimized inference on AWS Inferentia and
Trainium chips.

## Resources

**Related documents:**

- [Amazon SageMaker AI Inference Recommender](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-recommender.html)
- [Automatic
scaling of Amazon SageMaker AI models](https://docs.aws.amazon.com/sagemaker/latest/dg/endpoint-auto-scaling.html)
- [Deploy
models with Amazon SageMaker AI Serverless Inference](https://docs.aws.amazon.com/sagemaker/latest/dg/serverless-endpoints.html)
- [Multi-model
endpoints](https://docs.aws.amazon.com/sagemaker/latest/dg/multi-model-endpoints.html)
- [Model
performance optimization with SageMaker AI Neo](https://docs.aws.amazon.com/sagemaker/latest/dg/neo.html)

**Related examples:**

- [SageMaker AI Inference Recommender](https://github.com/aws/amazon-sagemaker-examples/blob/main/sagemaker-inference-recommender/inference-recommender.ipynb)
- [Right-sizing
your Amazon SageMaker AI Endpoints](https://github.com/aws-samples/aws-marketplace-machine-learning/blob/master/right_size_your_sagemaker_endpoints/Right-sizing%20your%20Amazon%20SageMaker AI%20Endpoints.ipynb)
- [SageMaker AI
Serverless Inference Examples](https://github.com/aws/amazon-sagemaker-examples/tree/main/serverless-inference)
- [Automatically
Scale Amazon SageMaker AI Models](https://github.com/awsdocs/amazon-sagemaker-developer-guide/blob/master/doc_source/endpoint-auto-scaling.md)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlcost05-bp03.html*

---

# MLCOST06 — Monitoring

**Pillar**: Cost Optimization  
**Best Practices**: 4

---

# MLCOST06-BP01 Monitor usage and cost by ML activity

Use cloud resource tagging to manage, identify, organize, search
for, and filter resources. Tags categorize resources by purpose,
owner, environment, or other criteria. Associate costs with
resources using ML activity categories, such as re-training and
hosting, by using tagging to manage and optimize cost in deployment
phases. Tagging can be useful for generating billing reports with
breakdown of cost by associated resources.

**Desired outcome:** You gain
visibility into your machine learning costs by activity type,
allowing for better allocation, forecasting, and optimization of ML
resources. You can track expenses across different phases of the ML
lifecycle including development, training, and deployment. This
enables data-driven decisions about resource allocation and
identifies cost-saving opportunities while maintaining performance.

**Common anti-patterns:**

- Using default AWS account structure without proper tagging
strategy for ML resources.
- Not separating costs between development, training, and
production environments.
- Failing to automate tagging as part of resource provisioning.
- Overlooking unused or idle resources that continue to incur
costs.

**Benefits of establishing this best
practice:**

- Clear visibility into costs associated with different ML
activities.
- Ability to allocate costs to appropriate business units or
projects.
- Improved forecasting and budgeting for ML initiatives.
- Identification of cost-saving opportunities across the ML
lifecycle.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Monitoring and optimizing costs for machine learning workloads
requires a systematic approach to resource tagging and usage
tracking. ML workloads typically have distinct phases—development,
training, inference, and experimentation—each with different
resource requirements and cost profiles. By implementing a
comprehensive tagging strategy, you can track and attribute costs
to specific ML activities, making it more straightforward to
understand where your cloud spend is going and identify
opportunities for optimization.

AWS provides various tools and services to implement cost
monitoring for ML workloads. With proper tagging, you can generate
detailed cost reports, set up budgets with alerts, and make
data-driven decisions about resource allocation. This practice is
particularly important for ML workloads, which can be
compute-intensive and potentially costly if not properly managed.

### Implementation steps

- **Establish a tagging strategy for ML
resources**. Create a consistent tagging schema
that captures relevant dimensions for ML activities. Include
tags for project name, environment (development, testing,
and production), ML phase (training, inference, and
experiment), owner, and cost center. Document this strategy
and verify that your team members understand and follow it
when creating resources.
- **Implement AWS tagging**. A
[tag](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html)
is a label that you or AWS assigns to an AWS resource. Each
tag consists of a key and a value. For each resource, each
tag key must be unique, and each tag key can have only one
value. You can use tags to organize your resources, and cost
allocation tags to track your AWS costs on a detailed level.
AWS uses the cost allocation tags to organize your resource
costs on your cost allocation report. This streamlines
categorizing and tracking your AWS costs. AWS provides two
types of cost allocation tags, an AWS-generated tag and
user-defined tags.
- **Activate cost allocation
tags**. After creating your tags, you need to
activate them for cost tracking in the AWS Billing and Cost Management and Cost
Management console. Note that it can take up to 24 hours for
new tags to appear in your billing reports.
- **Automate resource
tagging**. Use AWS CloudFormation templates, AWS CDK, or Terraform to automate the application of tags when
provisioning resources. For SageMaker AI resources, implement
tagging in your deployment pipelines and notebook
initialization scripts. Consider using AWS Tag Editor for
bulk tagging operations on existing resources.
- **Use AWS Budgets to keep track of
cost**. AWS Budgets can track your Amazon SageMaker AI cost, including development, training, and hosting. You
can also set alerts and get a notification when your cost or
usage exceeds (or is forecasted to exceed) your budgeted
amount. After you create your budget, you can track the
progress on the AWS Budgets console.
- **Implement cost monitoring and
reporting**. Use AWS Cost Explorer to visualize and
analyze your ML costs across different dimensions. Create
custom reports filtered by your ML activity tags to
understand spending patterns. Schedule regular exports of
cost reports for stakeholders review.
- **Establish cost optimization
processes**. Regularly review resource utilization
and costs to identify optimization opportunities. Implement
automated shutdown of idle resources such as SageMaker AI
notebooks when not in use. Consider using SageMaker AI Managed
Spot Training to reduce training costs by up to 90%.
- **Create governance for
tagging**. Use AWS Config Rules or AWS CloudFormation Hooks to enforce tagging policies. Implement
processes to review and correct untagged or incorrectly
tagged resources. Consider using AWS Organizations Tag
Policies to standardize tags across multiple accounts.
- **Implement enhanced cost tracking
with improved tagging**. Use enhanced AWS tagging
capabilities with better automation and governance features
to make your cost allocation more consistent across ML
workloads and improve your visibility into spending
patterns.
- **Use cost optimization
services**. Use AWS Cost Anomaly Detection to
identify unusual spending patterns in your ML workloads.
Consider AWS Compute Optimizer for recommendations on
right-sizing your ML compute resources based on historical
utilization data.

## Resources

**Related documents:**

- [Organizing
and tracking costs using AWS cost allocation tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html)
- [Managing
your costs with AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html)
- [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/)
- [Getting
started with AWS Cost Anomaly Detection](https://docs.aws.amazon.com/cost-management/latest/userguide/getting-started-ad.html)
- [What
is Tag Editor?](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html)
- [Best
Practices for Tagging AWS Resources](https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/tagging-best-practices.html)
- [Analyze
Amazon SageMaker AI spend and determine cost optimization
opportunities based on usage, Part 1: Overview](https://aws.amazon.com/blogs/machine-learning/part-1-analyze-amazon-sagemaker-spend-and-determine-cost-optimization-opportunities-based-on-usage-part-1/)
- [Analyze
Amazon SageMaker AI spend and determine cost optimization
opportunities based on usage, Part 4: Training jobs](https://aws.amazon.com/blogs/machine-learning/part-4-analyze-amazon-sagemaker-spend-and-determine-cost-optimization-opportunities-based-on-usage-part-4-training-jobs/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlcost06-bp01.html*

---

# MLCOST06-BP02 Monitor return on investment for ML models

Once a model is deployed into production, establish a reporting
capability to track the value which is being delivered. For example:

- **If a model is used to support customer
acquisition:** How many new customers are acquired and what
is their spend when the model's advice is used compared with a
baseline?
- **If a model is used to predict
when maintenance is needed:** What savings are being made
by optimizing the maintenance cycle?

Effective reporting compares the value delivered by an ML model
against the ongoing runtime cost and to take appropriate action. If
the ROI is substantially positive, are there ways in which this
might be scaled to similar challenges, for example. If the ROI is
negative, could this be addressed by remedial action, such as
reducing the model latency by using serverless inference, or
reducing the run time cost by changing the compromise between model
accuracy and model complexity, or layering in an additional simpler
model to triage or filter the cases that are submitted to the full
model.

**Desired outcome:** By implementing
this practice, you establish a clear line of sight between your ML
investments and business outcomes. You can continuously track the
value delivered by your ML models in terms of measurable business
KPIs, enabling data-driven decisions about scaling successful
models, optimizing underperforming ones, or sunsetting those with
negative ROI. Your organization has transparency into the
cost-effectiveness of ML initiatives and can strategically allocate
resources based on proven business value.

**Common anti-patterns:**

- Deploying ML models without defining success metrics or business
KPIs.
- Focusing only on technical metrics like accuracy without linking
to business outcomes.
- Measuring ROI only once after initial deployment rather than
continuously.
- Failing to account for the full costs of ML model operation in
ROI calculations.
- Ignoring opportunities to scale successful models to similar
business challenges.

**Benefits of establishing this best
practice:**

- Clear visibility into the business value generated by ML
investments.
- Ability to make data-driven decisions about model optimization
or retirement.
- Improved accountability for ML investments across the
organization.
- Better allocation of ML resources to high-impact use cases.
- Enhanced stakeholder confidence in ML initiatives through
transparent reporting.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Monitoring the return on investment for your ML models requires an
intentional approach that connects technical model performance
with tangible business outcomes. You need to establish a
continuous feedback loop between model operations and business
metrics to understand the true value being generated. This means
going beyond traditional ML metrics like accuracy or precision and
focusing on how the model's predictions translate into business
results.

Start by defining clear business KPIs that your model is expected
to influence before deployment. These KPIs should be measurable
and directly tied to business objectives, such as increased
revenue, reduced costs, or improved customer satisfaction. For
customer acquisition models, track metrics like conversion rates,
customer lifetime value, and acquisition costs. For predictive
maintenance models, measure metrics like maintenance cost savings,
reduced downtime, and extended equipment lifespan.

Once deployed, collect data on both the model's performance and
these business metrics to establish correlation between the two.
Use A/B testing where possible to compare outcomes with and
without the model's influence. This can isolate the specific
impact of your ML investment against other factors that might
affect business outcomes.

Regularly review the ROI of your models and be prepared to take
action based on the findings. For models with strong positive ROI,
explore opportunities to scale the approach to similar business
problems or increase the scope of the current implementation. For
models with marginal or negative ROI, consider optimization
strategies like reducing inference costs through more efficient
infrastructure, simplifying model complexity while maintaining
acceptable accuracy, or implementing a multi-tiered approach where
simpler models handle routine cases and complex models only
process edge cases.

### Implementation steps

- **Define business-oriented success
metrics.** Before deploying your ML model, clearly
define the business KPIs that will be used to measure its
impact. Work with business stakeholders to connect these
metrics directly to business outcomes and measure them
practically. For example, for a customer churn prediction
model, success metrics might include reduction in churn
rate, increase in retention-driven revenue, and decreased
cost of retention campaigns.
- **Establish baseline
performance.** Measure and document the current
performance on your defined KPIs before implementing the ML
model. This baseline is essential for determining the
incremental value the model delivers. Consider using A/B
testing approaches where feasible, sending some cases
through the ML-driven process and others through the
traditional approach.
- **Implement data collection
pipelines.** Set up automated data collection for
both model metrics and business outcomes. Use AWS services
like
[Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) to monitor technical aspects of your model
and
[Amazon Kinesis](https://aws.amazon.com/kinesis/) to capture business event data. Store this
data in [Amazon S3](https://aws.amazon.com/s3/) or
[Amazon Redshift](https://aws.amazon.com/redshift/) for further analysis.
- **Create ROI dashboards using Quick.** Develop business-focused dashboards
in
[Quick](https://aws.amazon.com/quicksight/) that visualize the relationship between
model performance and business outcomes. Include metrics
that show both the value generated (increased revenue, cost
savings) and costs incurred (infrastructure, maintenance,
human review). Use QuickSight's ML Insights to automatically
identify trends and anomalies in your ROI data.
- **Schedule regular ROI
reviews.** Establish a cadence for reviewing model
ROI with both technical and business stakeholders. These
reviews should assess whether the model continues to deliver
positive business impact and identify opportunities for
optimization. Use these sessions to make data-driven
decisions about continuing investment, scaling successful
approaches, or adjusting underperforming models.
- **Optimize underperforming
models.** For models not meeting ROI targets,
implement strategic improvements. Consider
[Amazon SageMaker AI](https://aws.amazon.com/sagemaker/) Serverless Inference to reduce costs for
infrequent or variable workloads. Explore model compression
techniques like
[SageMaker AI
Neo](https://docs.aws.amazon.com/sagemaker/latest/dg/neo.html) to improve inference efficiency without
sacrificing accuracy. Implement tiered prediction approaches
where simple, low-cost models filter cases before routing to
more complex models.
- **Scale successful models.**
When models demonstrate strong positive ROI, look for
opportunities to expand their impact. Apply similar modeling
approaches to related business problems, increase the scope
of existing models, or integrate the model with additional
business processes to maximize value creation.
- **Use enhanced QuickSight capabilities
for ROI analysis**. Use improved
[Quick](https://aws.amazon.com/quicksight/) with generative AI insights and natural
language query capabilities to automatically identify
trends, anomalies, and optimization opportunities in your
ROI data.
- **Use generative AI for enhanced
insights.** Use generative AI capabilities through
[Amazon
Bedrock](https://aws.amazon.com/bedrock/) to analyze patterns in your ROI data and
suggest optimization strategies. Generative AI can identify
non-obvious correlations between model configurations and
business outcomes, leading to better ROI optimization
decisions.

## Resources

**Related documents:**

- [What
is Quick?](https://docs.aws.amazon.com/quicksight/latest/user/welcome.html)
- [Publish
custom metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html)
- [Data
and model quality monitoring with Amazon SageMaker AI Model
Monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html)
- [What
are AWS Cost and Usage Reports?](https://docs.aws.amazon.com/cur/latest/userguide/what-is-cur.html)
- [Quick](https://aws.amazon.com/quicksight/)
- [Cost
Optimization Pillar - AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/welcome.html)
- [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlcost06-bp02.html*

---

# MLCOST06-BP03 Monitor endpoint usage and right-size the instance fleet

Use efficient compute resources to run models in production. Monitor
your endpoint usage and right-size the instance fleet. Use automatic
scaling (auto scaling) for your hosted models. *Auto
scaling* dynamically adjusts the number of instances
provisioned for a model in response to changes in your workload.

**Desired outcome:** You have
optimized SageMaker AI endpoints that automatically adjust to workload
demands while maintaining performance and minimizing costs. Your
model deployment uses appropriately sized instances that are neither
over-provisioned nor under-provisioned, and you have continuous
monitoring in place to inform scaling decisions.

**Common anti-patterns:**

- Provisioning static endpoint configurations that remain
unchanged regardless of workload fluctuations.
- Over-provisioning instances "just to be safe"
without analyzing actual resource utilization.
- Ignoring endpoint metrics and failing to adjust resource
allocation based on usage patterns.
- Deploying resources across different Availability Zones without
consideration for data transfer costs.
- Using default instance types without evaluating performance
requirements.

**Benefits of establishing this best
practice:**

- Reduced compute costs by reducing over-provisioned resources.
- Improved performance during peak usage periods through automatic
scaling.
- Higher resource utilization through right-sizing.
- Increased availability by distributing instances across
Availability Zones.
- Better understanding of model usage patterns to inform future
optimizations.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Monitoring and optimizing your SageMaker AI endpoints is essential
for maintaining cost-efficiency while providing high availability
and performance. By implementing CloudWatch monitoring and auto
scaling, your deployments use only the resources they needs when
they need them. Start by establishing baseline metrics for your
endpoints to understand typical usage patterns and resource
requirements. Then implement auto scaling policies based on these
metrics to automatically adjust capacity in response to changing
workloads.

For production environments, distribute your endpoint deployment
across multiple Availability Zones to maintain high availability.
Consider the placement of related resources, such as data storage
solutions like FSx for Lustre, to minimize cross-AZ data transfer
costs and optimize performance. Regular review of your metrics and
scaling configurations assists you to continuously refine your
deployment for optimal cost and performance.

### Implementation steps

- **Monitor Amazon SageMaker AI endpoints
with Amazon CloudWatch**. You can monitor Amazon SageMaker AI using
[Amazon CloudWatch](https://aws.amazon.com/cloudwatch/), which collects raw data and processes it
into readable, near real-time metrics. Use metrics such as
CPUUtilization, GPUUtilization, MemoryUtilization, and
DiskUtilization to view your endpoint's resource utilization
and make informed decisions about right-sizing your endpoint
instances. Set up CloudWatch dashboards to visualize these
metrics over time and identify patterns in resource usage.
- **Implement CloudWatch alarms for
proactive monitoring**. Configure alarms for key
metrics that can indicate when an endpoint is
under-provisioned or over-provisioned. For example, set up
alarms that go off when CPU utilization consistently exceeds
80% (indicating potential under-provisioning) or remains
below 20% (indicating over-provisioning). These alarms can
notify your team to take action or run automated responses
through AWS Lambda functions.
- **Configure auto scaling for SageMaker AI
endpoints**.
[Amazon SageMaker AI](https://aws.amazon.com/sagemaker/) supports auto scaling that monitors your
workloads and dynamically adjusts capacity to maintain
steady performance at the lowest possible cost. When
workload increases, auto scaling brings more instances
online. When workload decreases, auto scaling removes
unnecessary instances, which can reduce compute costs.
Define appropriate scaling policies based on your
application's requirements, including minimum and maximum
instance counts, target metrics, and scale-in and scale-out
cooldown periods.
- **Distribute instances across
Availability Zones**. SageMaker AI automatically
attempts to distribute your instances across Availability
Zones, so deploy multiple instances for each production
endpoint to provide high availability. If you're using a
VPC, configure at least two subnets in different
Availability Zones to allow SageMaker AI to distribute your
instances across those zones, providing resilience against
zone failures.
- **Optimize resource placement for data
access**. When using
[Amazon FSx for Lustre](https://aws.amazon.com/fsx/lustre/) as an input data source for SageMaker AI,
deploy FSx for Lustre and SageMaker AI in the same Availability
Zone to avoid cross-AZ data transfer costs. This
configuration removes the initial Amazon S3 download step,
accelerating ML training jobs while minimizing costs.
Consider similar placement strategies for other related
resources to optimize performance and cost.
- **Regularly review and adjust instance
types**. Periodically evaluate whether your
selected instance types are appropriate for your workload.
SageMaker AI offers a variety of
[instance
types](https://aws.amazon.com/sagemaker/pricing/) optimized for different workload
characteristics. Analyze your CloudWatch metrics to
determine if you could achieve better price-performance by
switching to a different instance family, such as
compute-optimized, memory-optimized, or GPU instances.
- **Use inference optimization
techniques**. Implement model optimization
techniques such as
[Amazon SageMaker AI Neo](https://docs.aws.amazon.com/sagemaker/latest/dg/neo.html) to automatically optimize models for
your target hardware, improving performance and potentially
allowing you to use smaller instance types. Consider
techniques like model compression, quantization, and
batching to improve inference efficiency and throughput.
- **Use enhanced SageMaker AI Inference
Recommender**. Use
[SageMaker AI
Inference Recommender](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-recommender.html) with enhanced algorithms and
support for multi-model endpoints to get sophisticated
instance selection and cost optimization recommendations.
- **Implement specialized instance types
for generative AI models**. For large language
models and other generative AI workloads, use specialized
instances like
[AWS Inferentia](https://aws.amazon.com/machine-learning/inferentia/) or
[AWS Trainium](https://aws.amazon.com/machine-learning/trainium/), which are designed specifically for machine
learning inference and training. These instances can provide
significant cost savings compared to general-purpose GPU
instances when running transformer-based models. Consider
[Amazon
Bedrock](https://aws.amazon.com/bedrock/) for fully managed generative AI capabilities
with built-in scaling.

## Resources

**Related documents:**

- [Amazon SageMaker AI metrics in Amazon CloudWatch](https://docs.aws.amazon.com/sagemaker/latest/dg/monitoring-cloudwatch.html)
- [Automatic
scaling of Amazon SageMaker AI models](https://docs.aws.amazon.com/sagemaker/latest/dg/endpoint-auto-scaling.html)
- [Amazon SageMaker AI Inference Recommender](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-recommender.html)
- [AWS Inferentia](https://aws.amazon.com/machine-learning/inferentia/)
- [Best
practices for deploying models on SageMaker AI Hosting
Services](https://docs.aws.amazon.com/sagemaker/latest/dg/deployment-best-practices.html)
- [Data
and model quality monitoring with Amazon SageMaker AI Model
Monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlcost06-bp03.html*

---

# MLCOST06-BP04 Enable debugging and logging

Implementing comprehensive logging and debugging capabilities for
your machine learning workflows assists you to understand resource
consumption patterns and identify optimization opportunities. By
collecting and analyzing runtime metrics, you can reduce costs and
enhance the efficiency of your ML training operations.

**Desired outcome:** You gain
visibility into training jobs through metrics and logs that reveal
resource consumption patterns. This practice identifies optimization
opportunities, reduces costs, and improves ML model training
performance. You implement monitoring systems to track compute and
storage utilization, and instrument code to record key metrics.

**Common anti-patterns:**

- Training ML models without performance visibility.
- Ignoring resource consumption data until costs become
problematic.
- Deploying ML solutions without adequate logging infrastructure.
- Using manual methods to track performance metrics.
- Waiting for issues to arise before implementing monitoring.

**Benefits of establishing this best
practice:**

- Early identification of model training inefficiencies.
- Reduced compute and storage costs through resource optimization.
- Faster troubleshooting of training job issues.
- Enhanced visibility into ML pipelines.
- Data-driven decisions for infrastructure provisioning.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Proper debugging and logging are crucial for cost management in
machine learning workflows. As ML models grow in complexity, the
computational resources required for training also increase. By
implementing comprehensive monitoring, you can identify
inefficiencies, optimize resource allocation, and reduce overall
costs.

Effective logging and debugging require instrumentation at
multiple levels, from the ML code itself to the underlying
infrastructure. This visibility provides an understanding of how
resources are being utilized during training jobs and identifies
bottlenecks so that you can make data-driven decisions about when
and how to scale resources. The metrics and logs collected can
reveal patterns of inefficient resource utilization that might
otherwise go unnoticed.

Additionally, monitoring storage consumption is important as data
preparation and feature engineering can generate large
intermediate datasets. By tracking both compute and storage
metrics, you can identify opportunities for optimization across
your entire ML pipeline.

### Implementation steps

- **Set up Amazon SageMaker AI
Debugger**.
[Amazon SageMaker AI Debugger](https://docs.aws.amazon.com/sagemaker/latest/dg/train-debugger.html) captures training job states at
regular intervals, providing visibility into the ML training
process. It monitors, records, and analyzes data during
training, enabling you to:

Track model parameters, gradients, and tensor values
- Identify training issues like vanishing gradients or
tensor explosions
- Receive automated alerts for common training problems
- Visualize and analyze captured data interactively

- **Implement CloudWatch
logging**. Integrate
[Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html) with your SageMaker AI training jobs to
centralize and analyze log data. Configure CloudWatch to:

Collect standard output and error logs from training
jobs
- Encrypt log data using an
[AWS KMS key](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) for security
- Set up custom log groups and streams for different ML
workflows
- Create log retention policies to manage storage costs

- **Instrument ML code for metrics
collection**. Add instrumentation code to your ML
training scripts to capture performance metrics and resource
utilization data:

Track timing information for different training phases
- Monitor memory usage during training operations
- Record batch processing statistics and convergence
metrics
- Log hyperparameter values and their impact on training
performance

- **Configure resource
monitoring**. Set up monitoring for compute and
storage resources used by your ML workflows:

Use CloudWatch metrics to track instance utilization
- Monitor data transfer volumes between storage and
compute resources
- Set up alerts for abnormal resource consumption patterns
- Create dashboards to visualize resource utilization
trends

- **Implement automated
alerting**. Configure notification systems to alert
you when resource consumption exceeds expected thresholds:

Set up CloudWatch alarms for high CPU, memory, or GPU
utilization
- Create alerts for extended training job durations
- Configure notifications for storage capacity issues
- Establish alerting for debugging rule violations in
SageMaker AI Debugger

- **Analyze and optimize training
jobs**. Use the collected metrics and logs to
identify optimization opportunities:

Review resource utilization patterns to identify
right-sizing opportunities
- Analyze training job logs for inefficient code paths
- Examine data loading and preprocessing bottlenecks
- Optimize hyperparameters based on performance metrics

- **Use enhanced debugging
capabilities**. Use improved SageMaker AI Studio
debugging and monitoring capabilities with better
integration to popular ML frameworks and enhanced
visualization tools for more efficient troubleshooting.
- **Use generative AI for log
analysis**. Use generative AI capabilities to
analyze and extract insights from ML training logs. Utilize
Q Diagnostics integrated into the console or your preferred
IDE for log analysis.

Implement natural language processing to summarize log
patterns
- Use Amazon Bedrock to build intelligent log analysis
assistants
- Deploy ML models that can predict resource needs based
on historical data
- Create automated reports of cost optimization
opportunities from log data

## Resources

**Related documents:**

- [Amazon SageMaker AI Debugger](https://docs.aws.amazon.com/sagemaker/latest/dg/train-debugger.html)
- [What
is Amazon CloudWatch Logs?](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html)
- [Analyzing
log data with CloudWatch Logs Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html)
- [Logging
and Monitoring](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-incident-response.html)
- [Logging
Amazon ML API Calls with AWS CloudTrail](https://docs.aws.amazon.com/machine-learning/latest/dg/logging-using-cloudtrail.html)
- [Amazon SageMaker AI Debugger API](https://sagemaker.readthedocs.io/en/stable/api/training/debugger.html)

**Related examples:**

- [Debugger
example notebooks](https://github.com/aws/amazon-sagemaker-examples/tree/main/sagemaker-debugger))
- [SageMaker AI
Debugger GitHub Repository](https://github.com/awslabs/sagemaker-debugger)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlcost06-bp04.html*

---

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
