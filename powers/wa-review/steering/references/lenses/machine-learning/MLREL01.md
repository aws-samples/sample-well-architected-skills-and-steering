# MLREL01 — ML problem framing

**Pillar**: Reliability  
**Best Practices**: 2

---

# MLREL01-BP01 Use APIs to abstract change from model consuming applications

APIs abstract changes from model-consuming applications, keeping
machine learning solutions flexible and resilient. Establishing an
abstraction layer between ML models and consuming applications
enables model updates, replacements, or enhancements without
disrupting existing workloads.

**Desired outcome:** You have a
flexible application and API design that isolates machine learning
model implementations from consuming applications. You make changes
to ML models with minimal or no disruption to existing applications.
Your ML endpoints are well-documented and accessible, and changes to
underlying models do not require extensive modifications to
downstream applications.

**Common anti-patterns:**

- Directly embedding model code within applications.
- Hardcoding model versions or parameter specifications in client
applications.
- Lacking proper API documentation and version control.
- Designing rigid interfaces that break when model inputs or
outputs change.
- Creating tight coupling between ML models and consuming
applications.

**Benefits of establishing this best
practice:**

- Reduces downtime when updating or replacing ML models.
- Simplifies model deployment and versioning processes.
- Increases agility and flexibility when evolving ML capabilities.
- Lowers maintenance costs for applications using ML models.
- Enhances ability to A/B test different model versions.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Abstracting changes from model-consuming applications requires
thoughtful API design and implementation. Create a well-designed
API layer between ML models and applications so that you can make
modifications to models without disrupting services. This approach
involves developing stable interfaces that hide underlying
complexity and implementation details of ML models.

When designing these APIs, focus on creating contracts that are
flexible enough to accommodate model evolution while maintaining
backward compatibility. Document APIs thoroughly so developers
consuming models understand how to interact with them correctly.
Consider implementing versioning strategies that allow introducing
new model capabilities while supporting existing clients.

### Implementation steps

- **Adopt best practices in API
design**. Expose ML endpoints through APIs so
changes to the model can be introduced without disrupting
upstream communications. Create a well-designed API contract
that focuses on business capabilities rather than technical
implementation details. Document your API in a central
repository or documentation site so calling services can
understand API routes and flags. Communicate changes to your
API with calling services.
- **Implement API versioning**.
Use versioning strategies for APIs to enable backward
compatibility while supporting new features. Consider using
URL path versioning (for example,
/v1/predict), header-based versioning, or
query parameter versioning depending on organizational
standards. This allows introducing new model versions
without breaking existing client applications.
- **Deploy models in Amazon SageMaker AI**. After training your model, deploy it
using
[Amazon SageMaker AI](https://aws.amazon.com/sagemaker/) to get predictions. To establish a
persistent endpoint for one prediction at a time, use
SageMaker AI hosting services. For predictions on entire
datasets, use SageMaker AI batch transform. SageMaker AI provides
flexibility in deployment options, including
[multi-model
endpoints](https://docs.aws.amazon.com/sagemaker/latest/dg/multi-model-endpoints.html),
[serverless
inference](https://docs.aws.amazon.com/sagemaker/latest/dg/serverless-endpoints.html), and
[asynchronous
inference](https://docs.aws.amazon.com/sagemaker/latest/dg/async-inference.html).
- **Use Amazon API Gateway to create
APIs**.
[Amazon API Gateway](https://aws.amazon.com/api-gateway/) is a fully managed service that enables
developers to create, publish, maintain, monitor, and secure
APIs. Using API Gateway, you can create RESTful APIs and
WebSocket APIs that enable real-time two-way communication
applications. API Gateway supports containerized and
serverless workloads, as well as web applications.
- **Implement request and response
transformations**. Use API Gateway's mapping
templates to transform client requests to match your model's
input format and transform model responses to maintain a
consistent API contract. This allows changing model
implementations without requiring client applications to
change how they format requests or interpret responses.
- **Add caching and
throttling**. Configure API Gateway's caching
capability to improve performance and reduce costs for
frequently accessed predictions. Implement throttling to
protect ML endpoints from traffic spikes and provide
consistent performance. Use
[SageMaker AI
Inference Recommender](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-recommender.html) to optimize endpoint
configurations for optimal latency and cost performance.
- **Monitor and analyze API
usage**. Set up monitoring and logging for APIs to
understand how they are being used and identify potential
issues. Use
[Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) metrics and logs to track API performance,
errors, and usage patterns. This data can optimize ML
endpoints and identify opportunities for improvement.
- **Consider inference components for
shared endpoints**. Use
[SageMaker AI
inference components](https://docs.aws.amazon.com/sagemaker/latest/dg/realtime-endpoints-deploy-models.html) to deploy multiple models to
shared endpoints, improving resource utilization and
reducing costs while maintaining API abstraction.

## Resources

**Related documents:**

- [Model
deployment options in Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/how-it-works-deployment.html)
- [What
is Amazon API Gateway?](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html)
- [Real-time
inference](https://docs.aws.amazon.com/sagemaker/latest/dg/realtime-endpoints.html)
- [Multi-model
endpoints](https://docs.aws.amazon.com/sagemaker/latest/dg/multi-model-endpoints.html)
- [Deploy
models with Amazon SageMaker AI Serverless Inference](https://docs.aws.amazon.com/sagemaker/latest/dg/serverless-endpoints.html)
- [Asynchronous
inference](https://docs.aws.amazon.com/sagemaker/latest/dg/async-inference.html)
- [Deploying
ML models using SageMaker AI Serverless Inference](https://aws.amazon.com/blogs/machine-learning/deploying-ml-models-using-sagemaker-serverless-inference-preview/)
- [Optimize
deployment cost of Amazon SageMaker AI JumpStart foundation
models with Amazon SageMaker AI asynchronous endpoints](https://aws.amazon.com/blogs/machine-learning/optimize-deployment-cost-of-amazon-sagemaker-jumpstart-foundation-models-with-amazon-sagemaker-asynchronous-endpoints/)

**Related videos:**

- [Amazon
Sagemaker Serverless Inference](https://www.youtube.com/watch?v=esG_Q8egwMU)

**Related examples:**

- [Amazon SageMaker AI Examples Repository](https://github.com/aws/amazon-sagemaker-examples)
- [Amazon SageMaker AI MLOps Workshop](https://github.com/aws-samples/amazon-sagemaker-mlops-workshop)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlrel01-bp01.html*

---

# MLREL01-BP02 Adopt a machine learning microservice strategy

Machine learning systems can be effectively implemented through a
microservice architecture that breaks down complex business problems
into smaller, loosely coupled components. This approach enables
distributed development, improves scalability, and facilitates
change management while reducing the impact of single failures on
the overall workload.

**Desired outcome:** You decompose
complex business problems into manageable components with clear
interfaces. You have a more resilient ML system architecture that
can scale individual components independently, enable faster
iterations, and allow specialized teams to work simultaneously on
different parts of the solution. Your organization benefits from
improved fault isolation, simplified testing, and greater
flexibility to update or replace individual ML models without
affecting the entire system.

**Common anti-patterns:**

- Building monolithic ML applications where functionality is
tightly coupled in a single runtime.
- Creating overly complex microservices that serve multiple
purposes.
- Implementing microservices without clear business domain
boundaries.
- Neglecting proper service interfaces and communication patterns
between microservices.
- Overlooking the operational complexity introduced by distributed
systems.

**Benefits of establishing this best
practice:**

- Improves resilience through isolation of failures to individual
components.
- Enhances scalability by allowing independent scaling of
individual services.
- Accelerates development cycles through parallel work streams.
- Simplifies testing and deployment of individual components.
- Provides flexibility to use different technologies for different
ML model requirements.
- Aligns technical components with business domains.
- Eases integration of new ML models and capabilities.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

When implementing ML systems, adopt a microservice architecture to
break down complex problems into manageable components. Rather
than creating one large monolithic application that handles the
entirety of of your machine learning workflow, you can develop
specialized services that handle specific functions like data
preprocessing, model training, inference, and business logic
integration. This approach is particularly valuable for machine
learning applications where different models may have varying
resource requirements, development cycles, and deployment
frequencies.

Microservices provide the flexibility to use different
technologies for different parts of your ML system. For example,
you might use Python-based services for data science tasks while
implementing Java-based services for integration with enterprise
systems. By establishing clear service interfaces, you verify that
these components work together seamlessly while maintaining
freedom.

When designing your ML microservices, focus on business domains
rather than technical functions. Instead of creating a generic
prediction service, you might create more specific services like
*customer churn prediction* or
*product recommendation* that align with
business capabilities. This domain-driven approach makes your
architecture more intuitive and adaptable to changing business
needs.

### Implementation steps

- **Adopt a microservice
strategy**. Implement a service-oriented
architecture (SOA) by making software components reusable
through service interfaces. Break your monolithic
application into separate components along business
boundaries or logical domains. Focus on building
single-purpose applications that can be composed in
different ways to deliver various end-user experiences.
Design clear APIs between services to implement proper
isolation and communication patterns.
- **Define domain boundaries**.
Analyze your machine learning workflow and identify natural
boundaries between different functional areas. Map out the
data flow and determine where service boundaries make sense.
Consider creating separate microservices for data ingestion,
preprocessing, feature engineering, model training, model
serving, and business logic integration. Verify that each
microservice has a clear, single responsibility within your
ML system.
- **Choose appropriate AWS
services**. Select AWS services that best support
your microservice architecture.
[AWS Lambda](https://aws.amazon.com/lambda/) provides serverless compute that scales
automatically and charges only for the compute time
consumed. For container-based deployments, use
[AWS Fargate](https://aws.amazon.com/fargate/) to run containers without managing
infrastructure. Consider
[Amazon ECS](https://aws.amazon.com/ecs/) or
[Amazon EKS](https://aws.amazon.com/eks/) for container orchestration needs, and
[Amazon API Gateway](https://aws.amazon.com/api-gateway/) to manage and secure your microservice
APIs.
- **Implement model serving
infrastructure**. Set up efficient model serving
using services like
[Amazon SageMaker AI](https://aws.amazon.com/sagemaker/) for deploying, monitoring, and scaling ML
models. SageMaker AI endpoints provide a managed solution for
hosting models and handling inference requests.
Alternatively, use
[AWS Lambda](https://aws.amazon.com/lambda/) for lightweight, event-driven inferencing or
containers on
[AWS Fargate](https://aws.amazon.com/fargate/) for more complex requirements.
- **Establish communication
patterns**. Design how your microservices will
communicate with each other. Use synchronous REST APIs for
direct request-response patterns, and asynchronous
communication through
[Amazon SNS](https://aws.amazon.com/sns/) or
[Amazon SQS](https://aws.amazon.com/sqs/) for event-driven architectures. Implement
[AWS EventBridge](https://aws.amazon.com/eventbridge/) to create event-driven workflows between
your ML microservices and other AWS services.
- **Implement monitoring and
observability**. Set up comprehensive monitoring
for your ML microservices using
[Amazon CloudWatch](https://aws.amazon.com/cloudwatch/). Track operational metrics like latency,
throughput, and error rates along with ML-specific metrics
such as prediction accuracy or drift. Implement distributed
tracing with
[AWS X-Ray](https://aws.amazon.com/xray/) to troubleshoot issues across service
boundaries and identify performance bottlenecks.
- **Automate deployments**.
Implement CI/CD pipelines using
[AWS CodePipeline](https://aws.amazon.com/codepipeline/) and
[AWS CodeBuild](https://aws.amazon.com/codebuild/) to automate the testing and deployment of
your ML microservices. Use infrastructure as code with
[AWS CloudFormation](https://aws.amazon.com/cloudformation/) or
[AWS CDK](https://aws.amazon.com/cdk/) to define and provision your microservice
infrastructure consistently.
- **Implement security best
practices**. Secure your ML microservices by
implementing proper authentication and authorization using
[Amazon Cognito](https://aws.amazon.com/cognito/) or
[AWS IAM](https://aws.amazon.com/iam/). Use
[AWS WAF](https://aws.amazon.com/waf/) to protect your APIs from common web exploits,
and encrypt sensitive data using
[AWS KMS](https://aws.amazon.com/kms/) to improve data privacy and adhere to regulatory
requirements.

## Resources

**Related documents:**

- [Implementing
Microservices on AWS](https://docs.aws.amazon.com/whitepapers/latest/microservices-on-aws/microservices-on-aws.html)
- [AWS Lambda Documentation](https://docs.aws.amazon.com/lambda/index.html)
- [Architect
for AWS Fargate for Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/userguide/what-is-fargate.html)
- [What
is Amazon SageMaker AI?](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html)
- [What
is the AWS Serverless Application Model (AWS SAM)?](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/what-is-sam.html)
- [Build
and deploy ML inference applications from scratch using Amazon SageMaker AI](https://aws.amazon.com/blogs/machine-learning/build-and-deploy-ml-inference-applications-from-scratch-using-amazon-sagemaker/)

**Related examples:**

- [Run
a Serverless "Hello, World" with AWS Lambda](https://aws.amazon.com/getting-started/hands-on/run-serverless-code/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlrel01-bp02.html*

---
