# MLOPS04 — Model development

**Pillar**: Operational Excellence  
**Best Practices**: 2

---

# MLOPS04-BP01 Automate operations through MLOps and CI/CD

Automate ML workload operations using infrastructure as code (IaC)
and configuration as code (CaC). Select appropriate MLOps mechanisms
to orchestrate your ML workflows and integrate with CI/CD pipelines
for automated deployments. This approach creates consistency across
your staging and production deployment environments. Enable model
observability and version control across your hosting
infrastructure.

**Desired outcome:** You establish
automated ML operations through MLOps practices and CI/CD pipelines
for repeatable, consistent deployments across environments. Your ML
workflows are orchestrated through infrastructure as code, providing
traceability, version control, and model observability. This enables
your teams to deliver ML models faster, with higher quality, and
maintain governance throughout the model lifecycle from development
to production.

**Common anti-patterns:**

- Manually deploying ML models to production environments.
- Using different tools and processes across development and
production environments.
- Not versioning infrastructure, configuration, or model
artifacts.
- Lacking automated testing for ML models before deployment.
- Creating one-off scripts for deployment instead of reusable
templates.

**Benefits of establishing this best
practice:**

- Accelerated ML model development and deployment cycles.
- Consistent, reproducible environments across development and
production.
- Improved collaboration between data scientists and operations
teams.
- Enhanced governance and traceability for model artifacts and
infrastructure.
- Improved rollbacks and version management.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

MLOps combines machine learning, DevOps practices, and data
engineering to streamline and automate the end-to-end ML
lifecycle. By implementing infrastructure as code and
configuration as code principles, you create consistent,
reproducible environments while minimizing manual steps that can
introduce errors. This approach makes ML operations more reliable,
scalable, and maintainable.

Creating automated CI/CD pipelines for ML workloads requires
special consideration compared to traditional software
applications. You need to track not only code changes but also
data, model parameters, and training configurations. Using AWS
services for MLOps provides integrated tools to manage these
complexities while maintaining proper governance and
observability.

When implementing MLOps practices, start by defining your workflow
patterns and choosing appropriate orchestration tools based on
your specific requirements. AWS offers multiple options for ML
workflow orchestration, from purpose-built services like SageMaker AI
Pipelines to more general workflow engines like AWS Step Functions. Each provides different levels of abstraction, control,
and integration capabilities.

Model observability is crucial for ML systems in production,
allowing you to monitor model performance, detect drift, and run
retraining when necessary. Implementing comprehensive monitoring
assists you to quickly identify and respond to changes in model
behavior or data distributions.

### Implementation steps

- **Define your ML workflow
architecture**. Begin by mapping out your
end-to-end ML workflow, including data preparation, feature
engineering, model training, evaluation, deployment, and
monitoring stages. Identify which steps can be automated and
which require human intervention. Determine the appropriate
level of separation between development, testing, and
production environments based on your requirements.
- **Select an infrastructure as code
approach**. Choose either AWS CloudFormation or AWS CDK to define your infrastructure.
[AWS CloudFormation](https://aws.amazon.com/cloudformation/) enables you to create and provision
AWS deployments predictably and repeatedly using template
files. For teams more comfortable with programming
languages,
[AWS Cloud Development Kit (AWS CDK) (AWS CDK)](https://aws.amazon.com/cdk/) allows you to define cloud
resources using familiar languages like Python, TypeScript,
or Java.
- **Implement version control for
assets**. Establish a version control strategy for
ML assets including code, configurations, infrastructure
definitions, and model artifacts. Use AWS CodeCommit or
third-party repositories to store and version these assets.
Implement branching strategies that allow for
experimentation while maintaining stable production
environments. Version control enables you to track changes,
collaborate effectively, and roll back to previous versions
when needed.
- **Choose an MLOps orchestration
strategy**. Based on your workflow needs, select an
appropriate orchestration mechanism:

Use
[Amazon SageMaker AI Pipelines](https://aws.amazon.com/sagemaker/pipelines/) to create ML workflows with
Python SDK, visualize, and manage them in Amazon SageMaker AI Studio. SageMaker AI Pipelines automatically logs
every step, creating an audit trail of model components
including training data, configurations, parameters, and
learning gradients.
- Use
[AWS Step Functions Data Science SDK](https://docs.aws.amazon.com/step-functions/latest/dg/concepts-python-sdk.html) to automate ML
workflows with more complex orchestration requirements
or when integrating with other AWS services beyond
SageMaker AI.
- Use third-party tools such as
[Amazon
Managed Workflows for Apache Airflow (MWAA)](https://aws.amazon.com/managed-workflows-for-apache-airflow/) to
orchestrate workflows using Directed Acyclic Graphs
(DAGs) written in Python, especially when you need to
integrate with existing Apache Airflow deployments.

- **Build CI/CD pipelines for ML
models**. Implement CI/CD pipelines using
[AWS CodePipeline](https://aws.amazon.com/codepipeline/) to automate the building, testing, and
deployment of ML models. Include automated tests for data
quality, model performance, and API functionality. Configure
the pipeline to deploy to staging environments before
production and implement approval gates where needed.
Integrate model registration and versioning using Amazon SageMaker AI Model Registry.
- **Set up model monitoring and
observability**. Implement comprehensive monitoring
for your deployed models using
[Amazon SageMaker AI Model Monitor](https://aws.amazon.com/sagemaker/model-monitor/). Configure data quality
monitoring, model quality monitoring, bias drift monitoring,
and feature attribution drift monitoring. Use
[Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) to create dashboards and alerts for model
performance metrics.
- **Establish automated rollback
mechanisms**. Configure your deployment pipelines
to support automated rollbacks when quality thresholds are
not met. Implement canary or blue/green deployment
strategies using
[AWS CodeDeploy](https://aws.amazon.com/codedeploy/) to gradually shift traffic to new model
versions while monitoring for issues. This minimizes the
impact of problematic deployments and provides service
continuity.
- **Integrate security and governance
controls**. Implement security checks throughout
your MLOps pipeline. Use
[AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam/) to control access to
resources and
[AWS CloudTrail](https://aws.amazon.com/cloudtrail/) to log API calls for auditing. Configure
[Amazon SageMaker AI Model Cards](https://aws.amazon.com/sagemaker/ml-governance/) to document model information,
intended uses, limitations, and performance characteristics.
- **Create environments for
experimentation and testing**. Set up isolated
environments for experimentation that don't impact
production systems. Use
[Amazon SageMaker AI Unified Studio](https://aws.amazon.com/sagemaker/unified-studio/) to provide data scientists
with self-service environments for exploration while
maintaining governance through integrated data and AI
workflows. Implement environment-specific configurations
through parameter files or environment variables managed in
your IaC templates.

## Resources

**Related documents:**

- [Pipelines
overview](https://docs.aws.amazon.com/sagemaker/latest/dg/pipelines-sdk.html)
- [What
is AWS CodePipeline?](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html)
- [Amazon
Managed Workflows for Apache Airflow (MWAA)](https://aws.amazon.com/managed-workflows-for-apache-airflow/)
- [AWS CloudFormation Documentation](https://docs.aws.amazon.com/cloudformation/index.html)
- [What
is the AWS CDK?](https://docs.aws.amazon.com/cdk/latest/guide/home.html)
- [Step
Functions Data Science SDK](https://aws-step-functions-data-science-sdk.readthedocs.io/en/stable/)
- [Infrastructure
as code](https://docs.aws.amazon.com/whitepapers/latest/introduction-devops-aws/infrastructure-as-code.html)
- [Data
and model quality monitoring with Amazon SageMaker AI Model
Monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html)
- [Model
Registration Deployment with Model Registry](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry.html)

**Related videos:**

- [AWS re:Invent 2024 - Accelerate ML workflows with Amazon SageMaker AI
Studio](https://www.youtube.com/watch?v=SAeZMA0KaFA)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlops04-bp01.html*

---

# MLOPS04-BP02 Establish reliable packaging patterns to access approved public libraries

Establishing reliable packaging patterns enables data scientists to
access approved public libraries efficiently and consistently. By
implementing structured access to public libraries and creating
separate kernels for common ML frameworks, organizations can have
both flexibility and security in their machine learning development
environments.

**Desired outcome:** You create a
streamlined workflow where your data scientists have reliable access
to approved libraries through internal repositories. You maintain
separate kernels for common ML frameworks like TensorFlow, PyTorch,
Scikit-learn, and Keras. This approach improves development
productivity while improving security and adherence with
organizational requirements.

**Common anti-patterns:**

- Allowing uncontrolled direct downloads from public repositories.
- Using inconsistent or undocumented container configurations.
- Maintaining duplicate library versions across different
environments.
- Not having a centralized strategy for package management.
- Failing to version control dependencies.

**Benefits of establishing this best
practice:**

- Better security through controlled library usage.
- Improved reproducibility of ML workloads.
- Reduced dependency conflicts.
- Simplified adherence with organizational security policies.
- Faster onboarding of new data scientists.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Creating reliable packaging patterns is essential for maintaining
consistent, secure, and efficient machine learning workflows. You
need to establish infrastructure that gives data scientists access
to the libraries they need while maintaining organizational
control over those dependencies. Container technologies provide a
portable, consistent way to package ML environments with required
dependencies, making them ideal for this purpose. Internal
artifact repositories allow for centralized management of approved
packages so that team members use consistent, vetted versions.

Your packaging strategy should balance flexibility for data
scientists with security and regulatory requirements. This means
establishing both infrastructure (containers, repositories) and
processes (approval workflows, versioning policies) that work
together to create a streamlined experience. The use of
standardized environments with separate kernels for different ML
frameworks enables isolation when needed while providing the
specific tools required for different types of projects.

### Implementation steps

- **Set up container infrastructure for
ML workloads**. Create a container strategy using
[Amazon Elastic Container Registry](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html) (Amazon ECR) to store and
manage your ML container images. Containers provide
consistent environments that package dependencies,
libraries, and runtime components needed for ML workloads.
- **Create base container images for
common ML frameworks**. Build and maintain separate
base container images for frameworks like TensorFlow,
PyTorch, Scikit-learn, and Keras using
[optimized
foundation model containers](https://docs.aws.amazon.com/sagemaker/latest/dg/large-model-inference.html) for efficient training
and inference. These images should include standard
configurations and commonly used libraries for each
framework, with support for frameworks like Hugging Face
Transformers and quantization techniques, providing
consistency across your organization.
- **Implement versioning and tagging
policies**. Establish clear policies for versioning
containers and artifacts for reproducibility of ML
experiments and models. Use semantic versioning and proper
tagging to track container image changes and library
updates.
- **Develop automation for container
builds and updates**. Implement CI/CD pipelines
using
[AWS CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html) to automatically build, test, and deploy
updated container images when dependencies need to be
updated or security patches are required.
- **Document usage patterns and
onboarding procedures**. Create comprehensive
documentation that explains how data scientists should use
the established packaging patterns, including how to access
approved libraries and work with containerized environments.

## Resources

**Related documents:**

- [What
is Amazon Elastic Container Registry?](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html)
- [What
are AWS Deep Learning Containers?](https://docs.aws.amazon.com/deep-learning-containers/latest/devguide/what-is-dlc.html)
- [Docker
containers for training and deploying models](https://docs.aws.amazon.com/sagemaker/latest/dg/docker-containers.html)
- [What
is AWS CodePipeline?](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html)
- ["Publish
Docker image to an Amazon ECR image repository" sample
for CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/sample-docker.html)

**Related examples:**

- [SageMaker AI
Custom Container Examples](https://github.com/aws/amazon-sagemaker-examples/tree/main/advanced_functionality/custom-training-containers)
- [Deep
Learning Container Examples](https://github.com/aws/deep-learning-containers/tree/master/examples)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlops04-bp02.html*

---
