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
