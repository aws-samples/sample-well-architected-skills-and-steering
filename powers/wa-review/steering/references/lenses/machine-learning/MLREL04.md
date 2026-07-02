# MLREL04 — Deployment

**Pillar**: Reliability  
**Best Practices**: 2

---

# MLREL04-BP01 Automate endpoint changes through a pipeline

Manual change management can be error prone and potentially incur a
high effort cost. Use automated pipelines (that integrate with a
change management tracking system) to deploy changes to your model
endpoints. Versioned pipeline inputs and artifacts allow you to
track the changes and automatically rollback after a failed change.

**Desired outcome:** You establish a
reliable and consistent deployment process for your machine learning
models. You gain the ability to track changes, perform automatic
rollbacks when needed, and improve adherence to change management
policies. This approach reduces manual errors, increases operational
efficiency, and provides you with better visibility into your ML
deployment lifecycle.

**Common anti-patterns:**

- Making manual updates directly to production endpoints.
- Using different deployment processes across teams or
environments.
- Lacking proper version control for model artifacts.
- Not having clear rollback mechanisms for failed deployments.
- Bypassing change management tracking systems.

**Benefits of establishing this best
practice:**

- Reduces human error during deployments.
- Increases deployment speed and reliability.
- Improves traceability and auditability of changes.
- Enables rollback to previous versions.
- Improves adherence to change management policies.
- Supports scalable ML operations across multiple models.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Implementing automated pipelines for model endpoint changes brings
consistency and reliability to your ML operations. By using a
standardized deployment approach, you can verify that that changes
to production endpoints follow the same validated process. This
reduces the risk of deployment errors and improves overall
operational efficiency.

The pipeline should include steps for testing, validation, and
approval of model changes before they reach production.
Integration with your existing change management system allows for
proper tracking and documentation of changes. The pipeline should
also maintain versioned artifacts of models deployed, enabling
rollback if issues arise in production.

### Implementation steps

- **Set up a CI/CD pipeline for ML
workloads**. Establish a continuous integration and
continuous delivery pipeline specifically designed for
machine learning workloads.
[Amazon SageMaker AI Pipelines](https://aws.amazon.com/sagemaker/pipelines/) provides a purpose-built solution
for creating end-to-end ML workflows at scale.
- **Integrate with change management
systems**. Connect your pipeline to existing change
management tracking systems to document endpoint changes.
This improves adherence with your organization's governance
requirements and provides a full audit trail of deployment
activity.
- **Implement artifact
versioning**. Store model artifacts, code, and
configuration files in version control. Use
[Amazon SageMaker AI Model Registry](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry.html) to catalog and version your
models, making it straightforward to track which model
versions are deployed to which endpoints.
- **Define automated testing and
validation**. Include automated testing steps in
your pipeline to validate model performance before
deployment. This should include unit tests, integration
tests, and model quality evaluations using metrics specific
to your use case.
- **Establish approval gates**.
Configure approval checkpoints in your pipeline where
stakeholders can review changes before they are promoted to
production. These gates maintain quality control and improve
adherence to business requirements.
- **Implement automated rollback
mechanisms**. Create automated procedures to roll
back to the previous stable version if a deployment fails or
if issues are detected after deployment. This minimizes
downtime and impact on users.
- **Monitor deployment
metrics**. Track the success rate of deployments
and time-to-deployment metrics to continuously improve your
pipeline. Use
[Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) to monitor these operational metrics.

## Resources

**Related documents:**

- [Pipelines
overview](https://docs.aws.amazon.com/sagemaker/latest/dg/pipelines-sdk.html)
- [Model
Registration Deployment with Model Registry](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry.html)
- [Data
and model quality monitoring with Amazon SageMaker AI Model
Monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html)
- [Build
a CI/CD pipeline for deploying custom machine learning models
using AWS services](https://aws.amazon.com/blogs/machine-learning/build-a-ci-cd-pipeline-for-deploying-custom-machine-learning-models-using-aws-services/)
- [Building,
automating, managing, and scaling ML workflows using Amazon SageMaker AI Pipelines](https://aws.amazon.com/blogs/machine-learning/building-automating-managing-and-scaling-ml-workflows-using-amazon-sagemaker-pipelines/)

**Related videos:**

- [Implementing
MLOps practices with Amazon SageMaker AI](https://youtu.be/fuXUi_hoK78)

**Related examples:**

- [SageMaker AI
Pipelines and SageMaker AI Model Registry](https://github.com/aws/amazon-sagemaker-examples/tree/default/%20%20%20ml_ops)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlrel04-bp01.html*

---

# MLREL04-BP02 Use an appropriate deployment and testing strategy

Select the right deployment and testing strategy for your machine
learning models to create smoother transitions to production,
minimize disruption, and allow for careful evaluation of model
performance before full implementation.

**Desired outcome:** You can
confidently deploy machine learning models to production using
strategies that minimize risk and maximize availability. You have
established processes to monitor model performance, allowing you to
make data-driven decisions about when to roll back to previous
versions or roll forward with new updates. Your deployment pipelines
include appropriate testing, validation, and metrics collection to
improve model quality and performance in production environments.

**Common anti-patterns:**

- Deploying new models directly to production without testing
strategies.
- Lacking version control for model artifacts.
- Not implementing monitoring metrics to evaluate model
performance.
- Using the same deployment strategy for models without
considering specific use case requirements.
- Failing to plan for rollbacks when model performance degrades.

**Benefits of establishing this best
practice:**

- Minimizes disruption to production services during model
updates.
- Enables testing models with real production traffic before full
deployment.
- Reduces risk through controlled deployment strategies.
- Improves visibility into model performance.
- Provides better mechanisms for recovering from poor-performing
model deployments.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Machine learning models require special consideration when
deploying to production environments because their behavior can be
complex and sometimes unpredictable. Unlike traditional software
where functionality is explicitly coded, ML models learn patterns
from data, making it crucial to validate their performance with
production data before full deployment.

Different deployment strategies provide varying levels of risk
mitigation and testing capabilities. Blue/green deployments allow
for instantaneous rollback by maintaining two identical
environments. Canary deployments reduce risk by exposing only a
small portion of traffic to new models. A/B testing enables you to
compare performance metrics between model versions. Shadow
deployments let you test new models without affecting user
experience by running them alongside the production model but not
using their predictions.

Your choice of deployment strategy should be guided by your
specific requirements for availability, risk tolerance, and the
criticality of the ML application. For high-stakes applications
like fraud detection or medical diagnostics, more cautious
approaches like canary or shadow deployments may be appropriate.
For less critical applications, simpler strategies might suffice.

### Implementation steps

- **Perform a deployment strategy
trade-off analysis**. Evaluate your business
requirements and risk tolerance to determine which
deployment strategies are most appropriate for your ML
models. Consider factors like required availability,
acceptable downtime, criticality of predictions, and
monitoring capabilities. Document your analysis and
selection criteria for each model deployment.
- **Implement robust model
versioning**. Establish a system to version model
artifacts, including the model itself, preprocessing
components, and associated configurations. Use
[Amazon SageMaker AI Model Registry](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry.html) to catalog models and track
their lineage, approval status, and deployment history.
Then, you can quickly identify what model version is running
and roll back if needed.
- **Set up blue/green deployments with
SageMaker AI**. Implement blue/green deployments for
your real-time inference endpoints to maximize availability
during updates. SageMaker AI automatically provisions new
infrastructure (green fleet) before transitioning traffic
from the old infrastructure (blue fleet), providing nearly
continuous service. Configure the appropriate
[traffic
shifting mode](https://docs.aws.amazon.com/sagemaker/latest/dg/deployment-guardrails-blue-green.html) based on your risk tolerance.
- **Configure canary deployments for
higher-risk updates**. For model updates where you
want additional safety, implement canary deployments that
route a small percentage of traffic to the new model version
first. Use
[SageMaker AI
deployment guardrails](https://docs.aws.amazon.com/sagemaker/latest/dg/deployment-guardrails-blue-green-canary.html) to set up canary testing with
baking periods to monitor model performance before shifting
the remaining traffic.
- **Establish linear traffic shifting
for granular control**. For the most controlled
deployments, set up
[linear
traffic shifting](https://docs.aws.amazon.com/sagemaker/latest/dg/deployment-guardrails-blue-green-linear.html) in SageMaker AI to gradually move
traffic from the blue fleet to the green fleet in multiple
steps. Define appropriate step sizes and baking periods
between shifts to carefully monitor model behavior at each
stage.
- **Implement A/B testing for model
comparison**. When you need to validate that a new
model performs better than the existing one, set up A/B
testing to compare metrics between versions with real
production traffic. Use
[SageMaker AI
A/B testing](https://docs.aws.amazon.com/sagemaker/latest/dg/model-ab-testing.html) to route defined percentages of traffic
to different model variants and collect performance data.
- **Deploy shadow models to reduce the
risk of testing**. For high-risk applications,
consider implementing shadow deployments where the new model
runs alongside the production model but doesn't affect
customer-facing decisions. This allows you to compare how
the new model would have performed using real production
data while minimizing the risk.
- **Define and implement model
performance metrics**. Establish clear metrics to
evaluate model performance in production, such as prediction
accuracy, latency, throughput, and business KPIs. Set up
monitoring with
[Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) to track these metrics and create alarms
that can run automatic or manual interventions when
performance degrades.
- **Create automatic rollback
mechanisms**. Implement automated procedures to
roll back to previous model versions when performance
metrics indicate problems. Define specific thresholds for
metrics that would trigger a rollback, and establish the
process for rolling back with minimal disruption.
- **Build comprehensive CI/CD
pipelines**. Integrate your deployment strategies
into complete CI/CD pipelines that automate the testing,
deployment, and monitoring of models. Use
[AWS CodePipeline](https://aws.amazon.com/codepipeline/) and
[AWS CodeDeploy](https://aws.amazon.com/codedeploy/) in conjunction with SageMaker AI to create
reliable deployment workflows.

## Resources

**Related documents:**

- [Deployment
guardrails for updating models in production](https://docs.aws.amazon.com/sagemaker/latest/dg/deployment-guardrails.html)
- [Blue/Green
Deployments](https://docs.aws.amazon.com/sagemaker/latest/dg/deployment-guardrails-blue-green.html)
- [Testing
models with production variants](https://docs.aws.amazon.com/sagemaker/latest/dg/model-ab-testing.html)
- [Model
Registration Deployment with Model Registry](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry.html)
- [Data
and model quality monitoring with Amazon SageMaker AI Model
Monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html)
- [Take
advantage of advanced deployment strategies using Amazon SageMaker AI deployment guardrails](https://aws.amazon.com/blogs/machine-learning/take-advantage-of-advanced-deployment-strategies-using-amazon-sagemaker-deployment-guardrails/)
- [A/B
Testing ML models in production using Amazon SageMaker AI](https://aws.amazon.com/blogs/machine-learning/a-b-testing-ml-models-in-production-using-amazon-sagemaker/)

**Related videos:**

- [Deliver
high-performance ML models faster with MLOps tools](https://www.youtube.com/watch?v=T9llSCYJXxc)
- [Canaries
in the code mines: Monitoring deployment pipelines](https://www.youtube.com/watch?v=IHbY897uEbQ)

**Related examples:**

- [Amazon SageMaker AI Inference Deployment Guardrails](https://github.com/aws/amazon-sagemaker-examples/tree/main/sagemaker-inference-deployment-guardrails)
- [Amazon SageMaker AI A/B Testing Pipeline](https://github.com/aws-samples/amazon-sagemaker-ab-testing-pipeline)
- [Amazon SageMaker AI Safe Deployment Pipeline](https://github.com/aws-samples/amazon-sagemaker-safe-deployment-pipeline)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlrel04-bp02.html*

---
