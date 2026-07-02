# MLREL05 — Monitoring

**Pillar**: Reliability  
**Best Practices**: 2

---

# MLREL05-BP01 Allow automatic scaling of the model endpoint

Implement capabilities that allow the automatic scaling of model
endpoints. This improves the reliable processing of predictions to
meet changing workload demands. Include monitoring on endpoints to
identify a threshold that initiates the addition or removal of
resources to support current demand.

**Desired outcome:** You can
efficiently handle varying workload demands by implementing
automatic scaling for your model endpoints. Your endpoints
dynamically adjust resources based on real-time needs, providing
consistent performance and availability without manual intervention.
This results in reliable prediction processing, optimal resource
utilization, and cost-effective operations.

**Common anti-patterns:**

- Manually scaling endpoints in response to traffic changes.
- Over-provisioning resources to handle peak loads at non-peak
times.
- Neglecting to set up monitoring for endpoint performance.
- Ignoring traffic patterns when configuring scaling policies.
- Using fixed infrastructure that can't adapt to changing
workloads.

**Benefits of establishing this best
practice:**

- Improves reliability and availability of prediction services.
- Optimizes costs through dynamic resource allocation.
- Enhances user experience with consistent response times.
- Reduces operational overhead through automation.
- Strengthens ability to handle unexpected traffic spikes.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Automatic scaling of model endpoints is critical for maintaining
reliable machine learning services in production. By implementing
auto scaling, your endpoints can handle varying loads efficiently
without manual intervention. This capability is especially
important for applications with fluctuating traffic patterns or
those that experience periodic spikes in demand.

When setting up automatic scaling, you need to consider
appropriate metrics that trigger scaling actions, such as CPU
utilization, memory usage, or request latency. Define appropriate
thresholds for these metrics so that your system scale at the
right time - not too early (which wastes resources) or too late
(which impacts performance).

Monitoring is an essential component of an auto scaling solution.
By implementing comprehensive monitoring, you gain visibility into
endpoint performance and scaling operations, allowing you to
optimize your configuration over time based on real usage
patterns.

### Implementation steps

- **Configure automatic scaling for
Amazon SageMaker AI endpoints**. Amazon SageMaker AI
supports
[automatic
scaling (auto scaling)](https://docs.aws.amazon.com/sagemaker/latest/dg/endpoint-auto-scaling.html) for your hosted models.
SageMaker AI endpoints can be configured with auto scaling to
maintain service availability as traffic increases.
Automatic scaling automatically provisions new resources
horizontally to handle increased user demand or system load.
- **Set up appropriate scaling
policies**. Define target metrics for scaling such
as CPU utilization, memory usage, or request count.
Configure appropriate minimum and maximum instance counts
based on your expected traffic patterns and performance
requirements. Consider implementing both scale-out policies
(adding capacity when load increases) and scale-in policies
(removing capacity when load decreases) to optimize resource
utilization.
- **Implement comprehensive
monitoring**. Use
[Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) to monitor the performance of your
endpoint and collect metrics that can inform scaling
decisions. Create dashboards to visualize endpoint
performance and scaling activities. Set up alerts to notify
you of issues or anomalies with your endpoints.
- **Leverage SageMaker AI Serverless
Inference**. For workloads with intermittent or
unpredictable traffic patterns, consider using
[Amazon SageMaker AI Serverless Inference](https://docs.aws.amazon.com/sagemaker/latest/dg/serverless-endpoints.html), which automatically
scales compute capacity up and down based on traffic,
avoiding the need to choose instance types or manage scaling
policies.
- **Utilize SageMaker AI Inference
Recommender**. Before deploying models to
production, use
[Amazon SageMaker AI Inference Recommender](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-recommender.html) to get
recommendations on instance types and configurations that
will best meet your performance and cost requirements,
assisting you in optimizing your scaling policies.
- **Implement load testing**.
Perform load testing on your endpoints to understand how
they behave under different traffic conditions. This
information can fine-tune your scaling policies so that
they're effective when real traffic increases occur.

## Resources

**Related documents:**

- [Automatic
scaling of Amazon SageMaker AI models](https://docs.aws.amazon.com/sagemaker/latest/dg/endpoint-auto-scaling.html)
- [Deploy
models with Amazon SageMaker AI Serverless Inference](https://docs.aws.amazon.com/sagemaker/latest/dg/serverless-endpoints.html)
- [Amazon SageMaker AI Inference Recommender](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-recommender.html)
- [Configuring
autoscaling inference endpoints in Amazon SageMaker AI](https://aws.amazon.com/blogs/machine-learning/configuring-autoscaling-inference-endpoints-in-amazon-sagemaker/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlrel05-bp01.html*

---

# MLREL05-BP02 Create a recoverable endpoint with a managed version control strategy

Establish a fully recoverable system for model prediction endpoints
by implementing proper version control and lineage tracking for
components that generate these endpoints.

**Desired outcome:** You have a
robust infrastructure where components related to model deployment,
including model artifacts, container images, and endpoint
configurations, are version controlled and traceable. You can
recover quickly from issues by identifying and reverting to previous
stable versions, and you can audit the full lineage of model
deployments for governance and regulatory requirements.

**Common anti-patterns:**

- Storing model artifacts without proper versioning.
- Using deployment processes only when needed without
infrastructure as code.
- Failing to track dependencies between model artifacts,
containers, and configurations.
- Not maintaining a centralized registry for models.
- Relying on manual processes for endpoint recovery.

**Benefits of establishing this best
practice:**

- Reduces recovery time when endpoint issues occur.
- Improves auditability and adherence through comprehensive
lineage tracking.
- Enhances collaboration between data scientists and operations
teams.
- Improves the consistency and reliability of model deployments.
- Enables reproduction of model endpoints exactly as they were at
specific points in time.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Machine learning model endpoints represent the interface where
your business delivers value from AI/ML investments. Verifying
that these endpoints are recoverable is critical for business
continuity. Recoverability depends on having comprehensive version
control for components involved in creating the endpoint.

A properly implemented MLOps framework for endpoint recoverability
tracks not just the model artifacts, but components that influence
the prediction service—training data, feature transformations,
container definitions, and infrastructure configurations. When
incidents occur, you need to understand the complete lineage of
your model endpoint, including which data trained the model, which
code created the container, and which configurations defined the
infrastructure.

By implementing proper version control and lineage tracking, you
create a system that is both resilient to failures and compatible
with governance requirements. You can trace exactly how each
endpoint was created and recreate it precisely when needed.

### Implementation steps

- **Implement MLOps with Amazon SageMaker AI Pipelines and Projects**.
[Amazon SageMaker AI Pipelines](https://aws.amazon.com/sagemaker/pipelines/) automates ML workflows by
providing a service for building, running, and managing ML
pipelines. It handles every step from data preparation to
model deployment in a versioned, predictable manner.
- **Implement a model registry
system**. Use
[Amazon SageMaker AI Model Registry](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry.html) to catalog your models for
production. The registry tracks model versions and their
approval status, creating a system of record for models in
your organization. Define a clear approval workflow for
moving models from development to production for proper
governance at each stage. For each model, register metadata
including performance metrics, training datasets, and
intended use cases.
- **Track experiments with SageMaker AI
MLflow**. MLflow in SageMaker AI allows you to create,
manage, analyze, and compare experiments. This way, data
scientists can view and track the experiments for the
current project. Each experiment logs every metric and
hyperparameter automatically, along with model artifacts and
dataset information.
- **Use infrastructure as code (IaC)
tools**. Define and build your infrastructure,
including model endpoints, using
[AWS CloudFormation](https://aws.amazon.com/cloudformation/) or
[AWS CDK](https://aws.amazon.com/cdk/). IaC makes your infrastructure version
controlled, repeatable, and able to be reverted to previous
states if needed. Store your infrastructure code in git
repositories alongside your model code, creating a unified
version history. This approach reduces configuration drift
between environments and verifies that your production
deployment exactly matches your tested configuration.
- **Store containers in Amazon Elastic Container Registry**. Use
[Amazon ECR](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html) to version and store the Docker containers that
serve your models. Amazon ECR automatically creates version
hashes for containers as you update them, enabling rollbacks
to previous versions. Implement image scanning to detect
security vulnerabilities, and apply lifecycle policies to
manage older versions of your containers.
- **Implement automated testing and
deployment pipelines**. Create CI/CD pipelines
using
[AWS CodePipeline](https://aws.amazon.com/codepipeline/) to automate the testing and deployment
of your models. These pipelines should validate models
before deployment, deploy infrastructure changes through
CloudFormation, and update model endpoints with minimal
downtime. Integrate automated quality checks to avoid
problematic models from reaching production.
- **Configure automated backups and
recovery processes**. Establish automated backup
procedures for your model artifacts, container images, and
endpoint configurations. Use
[Amazon S3 versioning](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html) for model artifacts and
[AWS Backup](https://aws.amazon.com/backup/) to protect configuration data. Document and
test recovery procedures regularly to verify that they work
when needed.

## Resources

**Related documents:**

- [AWS CloudFormation Documentation](https://docs.aws.amazon.com/cloudformation/index.html)
- [Infrastructure
as code](https://docs.aws.amazon.com/whitepapers/latest/introduction-devops-aws/infrastructure-as-code.html)
- [Pipelines
overview](https://docs.aws.amazon.com/sagemaker/latest/dg/pipelines-sdk.html)
- [What
is Amazon Elastic Container Registry?](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html)
- [Model
Registration Deployment with Model Registry](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry.html)
- [Fully
managed MLflow 3.0 on Amazon SageMaker AI](https://aws.amazon.com/blogs/machine-learning/accelerating-generative-ai-development-with-fully-managed-mlflow-3-0-on-amazon-sagemaker-ai/)
- [Building,
automating, managing, and scaling ML workflows using Amazon SageMaker AI Pipelines](https://aws.amazon.com/blogs/machine-learning/building-automating-managing-and-scaling-ml-workflows-using-amazon-sagemaker-pipelines/)
- [Multi-account
model deployment with Amazon SageMaker AI Pipelines](https://aws.amazon.com/blogs/machine-learning/multi-account-model-deployment-with-amazon-sagemaker-pipelines/)
- [Automate
feature engineering pipelines with Amazon SageMaker AI](https://aws.amazon.com/blogs/machine-learning/automate-feature-engineering-pipelines-with-amazon-sagemaker/)

**Related videos:**

- [Next-generation
CDK development with Amazon Q Developer](https://www.youtube.com/watch?v=WEYuvh3YqkI)
- [Infrastructure
as Code on AWS - AWS Online Tech Talks](https://www.youtube.com/watch?v=cKQtPZwf97s)
- [How
to create fully automated ML workflows with Amazon SageMaker AI
Pipelines](https://www.youtube.com/watch?v=W7uabCTfLrg)

**Related examples:**

- [Amazon SageMaker AI MLOps](https://github.com/aws/amazon-sagemaker-examples/tree/default/%20%20%20ml_ops)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlrel05-bp02.html*

---
