# Reliability

**Pillar**: Reliability  
**Questions**: 5

---

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

# MLREL02 — Data processing

**Pillar**: Reliability  
**Best Practices**: 3

---

# MLREL02-BP01 Use a data catalog

Process data across multiple data stores using data catalog
technology. An advanced data catalog service can enable ETL process
integration. This approach improves reliability and efficiency.

**Desired outcome:** You establish a
centralized system that inventories your ML data assets across the
organization. You can track, discover, and manage data
transformations, and your stakeholders can find and use appropriate
datasets. With a complete data catalog in place, you gain better
data governance, reduce duplication of effort, increase data
quality, and accelerate ML model development through streamlined
data preparation workflows.

**Common anti-patterns:**

- Maintaining separate, isolated data silos without centralized
metadata.
- Manual tracking of data assets using spreadsheets or wiki pages.
- Failing to document data transformations and lineage.
- Rebuilding ETL processes for each new ML project.
- Relying on tribal knowledge for understanding data
characteristics.

**Benefits of establishing this best
practice:**

- Provides centralized visibility of available data assets.
- Improves data governance.
- Reduces time spent searching for and understanding data.
- Enhances data quality through consistent transformation
processes.
- Strengthens collaboration between data engineers and data
scientists.
- Accelerates ML model development with faster data preparation.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

A data catalog is critical infrastructure for machine learning
workloads to succeed. Without proper cataloging, data scientists
spend excessive time searching for, understanding, and preparing
data rather than analyzing it or building models. A comprehensive
data catalog provides a centralized inventory of your data assets,
complete with metadata, transformation history, and usage
information.

When implementing a data catalog for ML workloads, focus on
creating a single source of truth for data discovery. The catalog
should document where data resides, what transformations have been
applied, and how it can be accessed. This reduces the time spent
on data preparation, which typically consumes 60-80% of a data
scientist's time.

For AWS environments, the AWS AWS Glue Data Catalog offers a powerful
solution as it integrates seamlessly with other AWS analytics and
machine learning services. By implementing a data catalog as part
of your ML infrastructure, you create a foundation for consistent,
reliable data processing that supports both current and future ML
initiatives.

### Implementation steps

- **Set up AWS AWS Glue Data Catalog**. Establish the
[AWSAWS Glue Data Catalog](https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html) as your central metadata
repository. This fully managed service provides a unified
view of your data across multiple data stores, making it
accessible to various AWS services like
[Amazon SageMaker AI](https://aws.amazon.com/sagemaker/),
[Amazon EMR](https://aws.amazon.com/emr/),
[Amazon Athena](https://aws.amazon.com/athena/), and
[Amazon Redshift](https://aws.amazon.com/redshift/).
- **Define your metadata
strategy**. Determine what metadata to capture
about each dataset, including business definitions, data
lineage, quality metrics, and usage patterns.
Well-documented metadata assists data scientists in quickly
understanding if a dataset is appropriate for their modeling
needs.
- **Populate the data
catalog**. Use
[AWS Glue crawlers](https://docs.aws.amazon.com/glue/latest/dg/add-crawler.html) to automatically discover schemas, data
types, and statistics from your data sources. Crawlers can
scan various data stores including Amazon S3, Amazon RDS,
and other database systems. Systematically add your data
sources to build comprehensive coverage.
- **Implement ETL processes with AWS Glue**. Create ETL jobs that transform raw data
into formats optimized for machine learning.
[AWS Glue](https://aws.amazon.com/glue/) can automatically generate Python or Scala code
for these transformations, reducing development time and
improving consistency across different data processing
pipelines.
- **Establish data lineage
tracking**. Configure your data catalog to track
transformations and maintain clear lineage information. With
data lineage tracking, data scientists can understand data
provenance, which builds trust in the datasets used for
model training.
- **Integrate with ML
workflows**. Connect your AWS AWS Glue Data Catalog
with Amazon SageMaker AI to streamline data access for model
training. For enterprise environments, implement
[Amazon SageMaker AI Catalog](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-projects-templates-sm.html) as a central metadata hub for ML
and data assets, enabling secure sharing and governed access
via Amazon DataZone integration. This integration allows
data scientists to discover and use properly prepared
datasets directly from their modeling environments.
- **Implement access controls and
governance**. Configure appropriate permissions for
your data catalog using
[AWS IAM](https://aws.amazon.com/iam/) roles. Verify that data scientists have access to
the metadata and datasets they need while maintaining
security and regulatory adherence.
- **Automate catalog
maintenance**. Set up automated processes to keep
your data catalog current as new data arrives and
transformations occur. Regular updates verify that data
scientists have access to the latest information about
available datasets.
- **Monitor and measure
impact**. Track key metrics like time saved in data
discovery, reduction in redundant data preparation work, and
improvements in model development cycles to quantify the
benefits of your data catalog implementation.

## Resources

**Related documents:**

- [Amazon SageMaker AI and when to use Amazon SageMaker AI vs Amazon
DataZone](https://docs.aws.amazon.com/datazone/latest/userguide/sagemaker-datazone.html)
- [The
lakehouse architecture of Amazon SageMaker AI](https://aws.amazon.com/sagemaker/lakehouse/)
- [Amazon SageMaker AI Unified Studio](https://aws.amazon.com/sagemaker/unified-studio/)
- [Catalog
and search](https://docs.aws.amazon.com/whitepapers/latest/building-data-lakes/data-cataloging.html)
- [Getting
started with serverless ETL on AWS Glue](https://docs.aws.amazon.com/prescriptive-guidance/latest/serverless-etl-aws-glue/metadata-management.html)
- [Using
crawlers to populate the Data Catalog](https://docs.aws.amazon.com/glue/latest/dg/add-crawler.html)
- [AWS modern data architecture](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-aws-data/aws-architecture.html)
- [Moving
from development to automated ML pipelines using Amazon SageMaker AI and AWS Glue](https://aws.amazon.com/blogs/machine-learning/moving-from-notebooks-to-automated-ml-pipelines-using-amazon-sagemaker-and-aws-glue/)
- [How
Genworth built a serverless ML pipeline on AWS using Amazon SageMaker AI and AWS Glue](https://aws.amazon.com/blogs/machine-learning/how-genworth-built-a-serverless-ml-pipeline-on-aws-using-amazon-sagemaker-and-aws-glue/)
- [How
to build and automate a serverless data lake using AWS Glue](https://aws.amazon.com/blogs/big-data/build-and-automate-a-serverless-data-lake-using-an-aws-glue-trigger-for-the-data-catalog-and-etl-jobs/)

**Related videos:**

- [Amazon SageMaker AI Lakehouse - Unified, open, and secure data
lakehouse](https://www.youtube.com/watch?v=wH0dZLtS88Y)
- [Understanding
Amazon S3 Tables: Architecture, performance, and
integration](https://www.youtube.com/watch?v=e1ypMWSHgsM)
- [Accelerate
your Analytics and AI with Amazon SageMaker AI LakeHouse](https://www.youtube.com/watch?v=qZTbS0xPN-U)
- [Unifying
data governance with Immuta and AWS Lake Formation](https://www.youtube.com/watch?v=X09-n2jJZKw)

**Related examples:**

- [Explaining
Credit Decisions with Amazon SageMaker AI](https://github.com/awslabs/sagemaker-explaining-credit-decisions)
- [How
to build an end-to-end Machine Learning pipeline using AWS Glue, Amazon S3, Amazon SageMaker AI and Amazon Athena](https://github.com/aws-samples/amazon-sagemaker-predict-accessibility)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlrel02-bp01.html*

---

# MLREL02-BP02 Use a data pipeline

Automate the processing, movement, and transformation of data
between different compute and storage services. This automation
enables data processing that is fault tolerant, repeatable, and
highly available.

**Desired outcome:** You achieve
streamlined and consistent data processing workflows that
automatically handle data movement and transformations. You can
process your machine learning data with increased reliability,
repeatability, and availability, while reducing manual effort and
potential errors. Your data processing becomes more efficient and
scalable, enabling you to focus on deriving insights rather than
managing data logistics.

**Common anti-patterns:**

- Manually moving and transforming data between systems.
- Creating one-off scripts for data processing tasks.
- Inconsistent data transformation processes across teams.
- Neglecting error handling and recovery mechanisms in data
workflows.
- Not versioning data processing code or configurations.

**Benefits of establishing this best
practice:**

- Reduces manual errors and inconsistencies in data processing.
- Increases repeatability and reliability of data transformations.
- Enables fault tolerance and automatic recovery mechanisms.
- Improves scalability of data processing workflows.
- Facilitates collaboration through standardized data processing
patterns.
- Enhances traceability and governance of data transformations.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Data is the foundation of a machine learning workload, and how you
handle this data directly impacts the quality of your ML models.
Data pipelines automate and standardize the process of collecting,
cleaning, transforming, and delivering data to your ML workflows.
Without proper data pipelines, your ML initiatives can suffer from
inconsistent data quality, limited reproducibility, and
operational inefficiencies.

Creating effective data pipelines requires careful planning around
data sources, transformation logic, error handling, and monitoring
capabilities. By implementing automated data pipelines, you verify
that your data preparation follows a consistent, repeatable
process that can scale with your ML workload demands. This
approach leads to more reliable models and faster deployment
cycles.

AWS provides a comprehensive set of tools specifically designed to
build robust ML data pipelines, with Amazon SageMaker AI offering
integrated capabilities for the entire ML lifecycle. These tools
enable you to focus on deriving insights from your data rather
than managing infrastructure.

### Implementation steps

- **Assess your data processing
requirements**. Begin by identifying your data
sources, required transformations, and destination systems.
Document the flow of data from source to consumption, noting
data quality requirements, validation rules, or business
logic that must be applied during processing.
- **Implement data preparation and
wrangling processes**. Establish comprehensive data
preparation workflows that transform raw data into ML-ready
formats. Use a combination of AWS services and tools to:

Connect to data sources including
[Amazon S3](https://aws.amazon.com/s3/),
[Amazon Athena](https://aws.amazon.com/athena/),
[Amazon Redshift](https://aws.amazon.com/redshift/), and other databases using appropriate
connectors
- Explore and profile your data using
[Amazon EMR](https://aws.amazon.com/emr/) with Apache Spark or
[AWS Glue](https://aws.amazon.com/glue/) interactive sessions to identify patterns,
anomalies, and data quality issues
- Transform your data using
[AWS Glue ETL jobs](https://docs.aws.amazon.com/glue/latest/dg/author-job.html),
[Amazon EMR](https://aws.amazon.com/emr/) clusters, or
[SageMaker AI
Processing](https://docs.aws.amazon.com/sagemaker/latest/dg/processing-job.html) jobs with custom transformation
scripts
- Generate data quality reports and validation checks
using
[AWS Glue DataBrew](https://aws.amazon.com/glue/features/databrew/) or custom validation scripts to
identify issues before model training
- Create reusable data preparation workflows using
[AWS Glue workflows](https://docs.aws.amazon.com/glue/latest/dg/workflows_overview.html) or
[SageMaker AI
Pipelines](https://aws.amazon.com/sagemaker/pipelines/) that verify consistency across
different datasets and projects

- **Build automated ML workflows with
SageMaker AI Pipelines**. After creating your data
preparation workflow, export it to
[Amazon SageMaker AI Pipelines](https://aws.amazon.com/sagemaker/pipelines/) to automate your entire ML
workflow. SageMaker AI Pipelines helps you:

Create end-to-end ML workflows that combine data
preparation, model training, evaluation, and deployment
- Automate pipeline execution on a schedule or
trigger-based approach
- Track lineage of ML artifacts for governance
- Implement quality gates to verify that models meet
performance criteria
- Version control your pipelines for reproducibility

- **Implement error handling and
monitoring**. Configure your pipelines to handle
errors gracefully and provide visibility into pipeline
performance:

Set up retry mechanisms for transient failures
- Create notification systems for critical pipeline
failures
- Implement logging throughout your pipeline steps
- Use
[Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) to monitor pipeline metrics and set up
alerts

- **Version and store your data
artifacts**. Maintain traceability of your data
processing:

Store processed datasets in Amazon S3 with appropriate
versioning
- Use
[Amazon SageMaker AI Feature Store](https://aws.amazon.com/sagemaker/feature-store/) to create reusable
feature repositories
- Document data transformations and their business logic
- Implement data lineage tracking to understand data
provenance

- **Integrate with your existing ML
workflow**. Connect your data pipelines to other
components of your ML environment:

Feed processed data directly into model training jobs
- Integrate with model registries and deployment pipelines
- Establish feedback loops from model performance back to
data preparation

- **Scale your data processing as
needed**. Configure your pipelines to handle
growing data volumes:

Use distributed processing for large datasets with
services like
[Amazon EMR](https://aws.amazon.com/emr/)
- Implement incremental processing patterns for streaming
data
- Configure compute resources appropriately for each
pipeline stage

## Resources

**Related documents:**

- [Data
transformation workloads with SageMaker AI Processing](https://docs.aws.amazon.com/sagemaker/latest/dg/processing-job.html)
- [Pipelines](https://docs.aws.amazon.com/sagemaker/latest/dg/pipelines.html)
- [Get
started with Amazon SageMaker AI Feature Store](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store-getting-started.html)
- [Data
preparation and cleaning](https://docs.aws.amazon.com/prescriptive-guidance/latest/modern-data-centric-use-cases/data-preparation-cleaning.html)
- [Run
secure processing jobs using PySpark in Amazon SageMaker AI
Pipelines](https://aws.amazon.com/blogs/machine-learning/run-secure-processing-jobs-using-pyspark-in-amazon-sagemaker-pipelines/)
- [Building,
automating, managing, and scaling ML workflows using Amazon SageMaker AI Pipelines](https://aws.amazon.com/blogs/machine-learning/building-automating-managing-and-scaling-ml-workflows-using-amazon-sagemaker-pipelines/)

**Related videos:**

- [AWS Glue and Amazon SageMaker AI Studio Integration](https://aws.amazon.com/awstv/watch/5d00e03ffe3/)
- [Build,
automate, manage, and scale ML workflows using Amazon SageMaker AI Pipelines](https://www.youtube.com/watch?v=Hvz2GGU3Z8g)

**Related examples:**

- [Amazon SageMaker AI Examples GitHub Repository](https://github.com/aws/amazon-sagemaker-examples)
- [MLOps
Workshop with Amazon SageMaker AI Pipelines](https://catalog.us-east-1.prod.workshops.aws/workshops/741835d3-a2bf-4cb6-81f0-d0bb4a62edca/en-US)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlrel02-bp02.html*

---

# MLREL02-BP03 Automate managing data changes

Effective management of machine learning training data changes is
crucial for maintaining model reproducibility and providing
consistent performance over time. By implementing automated version
control for training data, you can precisely recreate a model
version when needed and maintain a clear audit trail of data
transformations.

**Desired outcome:** You establish
automated processes for tracking and managing changes to your
training data using version control technology. You gain the ability
to reproduce model versions exactly as they were originally created,
track data lineage through your ML pipeline, and maintain consistent
model performance across deployments. Your ML operations become more
reliable, transparent, and compatible with governance requirements.

**Common anti-patterns:**

- Manually tracking data versions in spreadsheets or
documentation.
- Storing multiple versions of datasets with inconsistent naming
conventions.
- Neglecting to record relationships between datasets and
resulting models.
- Not preserving feature engineering transformations applied to
training data.
- Relying on ad-hoc backup processes instead of systematic version
control.

**Benefits of establishing this best
practice:**

- Enables reproducible machine learning by maintaining exact data
version history.
- Improves troubleshooting by allowing precise recreation of model
versions.
- Enhances collaboration among data scientists through shared
version control.
- Provides audit trail for governance requirements.
- Reduces errors in model deployment by providing consistent
training data.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Managing changes to training data is fundamental to maintaining
reproducible machine learning models. As your data evolves through
acquisition, cleaning, and feature engineering, implementing
automated version control allows you to track these changes
systematically. This provides confidence that you can recreate any
model version precisely when needed, which is essential for
troubleshooting, compliance alignment, and proviidng consistent
performance.

By implementing automated data versioning, you create a traceable
history of your training data that integrates seamlessly with your
ML pipeline. This approach mirrors software development best
practices by treating data as a critical asset requiring the same
level of version control as code. When data changes occur, whether
through new acquisitions or transformations, your versioning
system automatically captures these changes, making it possible to
track model lineage from training data to deployment.

### Implementation steps

- **Implement a data version control
system**. Begin by setting up a data version
control system that can handle ML datasets efficiently.
Tools like Git LFS, DVC (Data Version Control), or AWS
solutions can be used to track changes in your training
datasets. These tools provide mechanisms to capture dataset
metadata and references without storing the entire dataset
in the version control repository.
- **Establish a data management
strategy**. Define clear workflows for how data
should be versioned, including naming conventions, branching
strategies, and metadata requirements. Document how data
should flow through your ML pipeline and how versions will
be tracked at each stage.
- **Use AWS MLOps Framework**.
Implement the
[AWS MLOps Framework](https://aws.amazon.com/sagemaker/ai/mlops/) to establish a standardized interface
for managing ML pipelines. This framework works with both
Amazon Machine Learning services and third-party services,
providing a comprehensive solution for ML operations. The
framework allows you to upload trained models (bring your
own model), configure pipeline orchestration, and monitor
operations—all while maintaining version control of data
assets.
- **Integrate with SageMaker AI Model
Registry**. Use
[Amazon SageMaker AI Model Registry](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry.html) to track model versions and
their associated artifacts. Model Registry maintains
comprehensive records of model lineage, including which
datasets were used for training and validation, preserving
the connection between models and their source data.
- **Establish CI/CD for ML
pipelines**. Set up continuous integration and
continuous deployment (CI/CD) pipelines specifically
designed for ML workflows using
[Amazon SageMaker AI Pipelines](https://aws.amazon.com/sagemaker/pipelines/). This assists you to version and
test changes to both code and data properly before moving to
production.
- **Create reproducible training
environments**. Use container technology to package
your training environment along with references to specific
data versions.
[Amazon SageMaker AI](https://aws.amazon.com/sagemaker/) provides mechanisms to create reproducible
training jobs that can reference specific versions of your
datasets stored in
[Amazon S3](https://aws.amazon.com/s3/).
- **Implement data quality
monitoring**. Set up automated monitoring of data
quality metrics to detect drift or anomalies in incoming
data. Tools like
[Amazon SageMaker AI Model Monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html) can identify when new data
differs from the baseline training data, allowing you to
make informed decisions about model retraining.
- **Configure automated
testing**. Implement automated tests that validate
data consistency and model performance when data versions
change. This verifies that new data meets quality standards
before being used in training or inference.
- **Document data versioning
procedures**. Create comprehensive documentation
that describes your data versioning strategy, including how
to retrieve specific versions of datasets and how to match
models with their corresponding training data versions.

## Resources

**Related documents:**

- [Implement
MLOps](https://docs.aws.amazon.com/sagemaker/latest/dg/mlops.html)
- [Model
Registration Deployment with Model Registry](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry.html)
- [Amazon SageMaker AI Feature Store](https://aws.amazon.com/sagemaker/feature-store/)
- [Data
and model quality monitoring with Amazon SageMaker AI Model
Monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html)
- [Amazon SageMaker AI Pipelines Brings DevOps Capabilities to your Machine
Learning Projects](https://aws.amazon.com/blogs/machine-learning/promote-pipelines-in-a-multi-environment-setup-using-amazon-sagemaker-model-registry-hashicorp-terraform-github-and-jenkins-ci-cd/)
- [Building,
automating, managing, and scaling ML workflows using Amazon SageMaker AI Pipelines](https://aws.amazon.com/blogs/machine-learning/building-automating-managing-and-scaling-ml-workflows-using-amazon-sagemaker-pipelines/)
- [Fully
managed MLflow 3.0 on Amazon SageMaker AI](https://aws.amazon.com/blogs/machine-learning/accelerating-generative-ai-development-with-fully-managed-mlflow-3-0-on-amazon-sagemaker-ai/)

**Related videos:**

- [Implementing
End-to-End MLOps Solutions with Amazon SageMaker AI](https://aws.amazon.com/awstv/watch/5057107a7fc/)
- [Accelerate
production for gen AI using Amazon SageMaker AI MLOps &
FMOps](https://www.youtube.com/watch?v=-3Otl7GVeCc)
- [Deliver
high-performance ML models faster with MLOps tools](https://www.youtube.com/watch?v=T9llSCYJXxc)

**Related examples:**

- [Amazon SageMaker AI secure MLOps](https://github.com/aws-samples/amazon-sagemaker-secure-mlops)
- [ML
Pipelines using Amazon SageMaker AI](https://github.com/aws/amazon-sagemaker-examples/tree/default/%20%20%20ml_ops/sm-mlflow_pipelines)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlrel02-bp03.html*

---

# MLREL03 — Model development

**Pillar**: Reliability  
**Best Practices**: 4

---

# MLREL03-BP01 Enable CI/CD/CT automation with traceability

Enable source code, data, and artifact version control of ML
workloads to enable roll back to a specific version. Incorporate
continuous integration (CI), continuous delivery (CD), and
continuous training (CT) practices to ML workload operations,
providing automation with added traceability.

**Desired outcome:** You establish
automated pipelines that handle the entire machine learning
lifecycle from development to deployment and continuous training.
You gain the ability to track every artifact, model version,
dataset, and code change throughout the ML workflow, enabling
transparent auditing, reproducibility of experiments, and the
capability to quickly roll back to previous versions when needed.

**Common anti-patterns:**

- Manual deployment and training processes without version
control.
- Lack of documentation on model lineage and data provenance.
- Inability to reproduce ML experiments due to missing environment
configurations.
- Performing model training only when necessary without automated
testing and validation.
- Siloed development and operations teams working separately on ML
workflows.

**Benefits of establishing this best
practice:**

- Increases productivity through automation of repetitive ML
development tasks.
- Improves reproducibility of ML experiments and model training.
- Enhances collaboration between data scientists and operations
teams.
- Accelerates time-to-market for ML-powered features and
applications.
- Reduces risk through ability to quickly roll back problematic
deployments.
- Improves adherence to audit requirements through comprehensive
traceability.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Implementing CI/CD/CT for machine learning workloads requires a
different approach than traditional software development due to
the data-centric nature of ML systems. While software CI/CD
focuses primarily on code, ML pipelines must also track data,
model artifacts, and training environments for full
reproducibility.

MLOps combines DevOps practices with machine learning to automate
and streamline the entire lifecycle of ML systems. By implementing
MLOps with traceability, you create a foundation that supports
reproducible science, auditability, and operational excellence.
This allows your organization to deploy ML models with confidence
while maintaining the ability to understand exactly how each model
was created and what data influenced its behavior.

Amazon SageMaker AI provides a comprehensive solution to implement
MLOps practices with built-in version control, lineage tracking,
and pipeline automation. By using SageMaker AI and complementary AWS
services, you can establish a robust MLOps framework that makes
your ML workflows reproducible, traceable, and maintainable.

### Implementation steps

- **Implement version control for ML
artifacts**. Set up repositories for code, data,
models, and configurations using version control systems.
Use
[AWS CodeCommit](https://aws.amazon.com/codecommit/) or integrate with GitHub to version your
ML code and configurations. For data and models, use
[Amazon SageMaker AI Model Registry](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry.html) to version and catalog your
models, creating a system of record that tracks the lineage
of each model.
- **Set up data versioning and lineage
tracking**. Implement data version control to track
changes in your datasets over time. Use
[Amazon SageMaker AI Feature Store](https://aws.amazon.com/sagemaker/feature-store/) to store, share, and manage
features for ML development, which you can use to track and
version feature values. Implement Lineage Tracking to track
the relationships between ML artifacts including data,
models, training jobs, and deployments.
- **Establish continuous integration
practices**. Configure automated tests that verify
both code quality and model performance. Set up CI pipelines
using
[AWS CodeBuild](https://aws.amazon.com/codebuild/) that run unit tests, integration tests, and
model quality tests when changes are pushed to your
repositories. Implement automated code review practices to
maintain quality standards across your ML codebase.
- **Build continuous delivery pipelines
for models**. Create automated deployment pipelines
for ML models using
[Amazon SageMaker AI Pipelines](https://aws.amazon.com/sagemaker/pipelines/) or
[AWS CodePipeline](https://aws.amazon.com/codepipeline/). Configure pipelines to include stages
for data preparation, model training, evaluation, and
deployment. Implement approval gates for human validation
before models are deployed to production environments.
- **Implement continuous training
mechanisms**. Set up automated retraining pipelines
that can be triggered by data drift, scheduled intervals, or
on-demand. Use Amazon SageMaker AI Pipelines to create
end-to-end workflows for model retraining. Implement
monitoring for model drift using
[SageMaker AI
Model Monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html) and trigger retraining when performance
degrades below thresholds.
- **Establish model governance and
approval workflows**. Create a governance framework
that requires appropriate reviews and approvals before
models move to production. Use SageMaker AI Model Registry to
implement model approval workflows with different approval
stages. Configure integration with notification services
like [Amazon SNS](https://aws.amazon.com/sns/) to alert stakeholders when models need review.
- **Implement immutable infrastructure
for reproducibility**. Use infrastructure as code
(IaC) to define your ML environments consistently. Leverage
[AWS CloudFormation](https://aws.amazon.com/cloudformation/) or
[AWS CDK](https://aws.amazon.com/cdk/) to define your SageMaker AI environments,
maintaining consistency across development, testing, and
production. Create standardized container images for
training and inference to improve environment
reproducibility.
- **Set up comprehensive monitoring and
logging**. Implement monitoring for your ML
pipelines and deployed models. Use
[CloudWatch](https://aws.amazon.com/cloudwatch/)
to track operational metrics of your pipeline runs and model
endpoints. Configure SageMaker AI Model Monitor to track data
drift, model drift, and prediction quality over time.
- **Create rollback mechanisms for
models and pipelines**. Establish automated
rollback procedures that can quickly revert to previous
model versions when issues are detected. Configure SageMaker AI
endpoints with production variants to support blue/green
deployments and canary testing, enabling safe rollbacks when
needed.

## Resources

**Related documents:**

- [Implement
MLOps](https://docs.aws.amazon.com/sagemaker/latest/dg/mlops.html)
- [Pipelines
overview](https://docs.aws.amazon.com/sagemaker/latest/dg/pipelines-sdk.html)
- [AWS DevOps Guidance](https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/devops-guidance.html)
- [Model
Registration Deployment with Model Registry](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry.html)
- [Building,
automating, managing, and scaling ML workflows using Amazon SageMaker AI Pipelines](https://aws.amazon.com/blogs/machine-learning/building-automating-managing-and-scaling-ml-workflows-using-amazon-sagemaker-pipelines/)
- [Create
Amazon SageMaker AI projects with image building CI/CD
pipelines](https://aws.amazon.com/blogs/machine-learning/create-amazon-sagemaker-projects-with-image-building-ci-cd-pipelines/)

**Related videos:**

- [Deliver
high-performance ML models faster with MLOps tools](https://www.youtube.com/watch?v=T9llSCYJXxc)
- [Accelerate
production for gen AI using Amazon SageMaker AI MLOps &
FMOps](https://www.youtube.com/watch?v=-3Otl7GVeCc)

**Related examples:**

- [Amazon
Sagemaker MLOps](https://github.com/aws/amazon-sagemaker-examples/tree/default/%20%20%20ml_ops)
- [Amazon SageMaker AI secure MLOps](https://github.com/aws-samples/amazon-sagemaker-secure-mlops)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlrel03-bp01.html*

---

# MLREL03-BP02 Verify feature consistency across training and inference

Provide consistent, scalable, and highly available features between
training and inference using a feature storage. This results in
reducing the training-serving skew by keeping feature consistency
between training and inference.

**Desired outcome:** You create a
centralized feature repository where feature definitions are stored,
versioned, and shared across your organization. This makes the same
features used during model training consistently available during
inference, which reduces training-serving skew. You can discover,
reuse, and share features across different ML projects, reducing
duplicate work and standardizing feature engineering practices.

**Common anti-patterns:**

- Recreating feature transformations separately for training and
inference pipelines.
- Storing features in different formats or locations for training
versus production.
- Lack of versioning for features, leading to inconsistencies when
models are updated.
- Duplicating feature engineering work across different teams or
projects.
- Using non-standardized approaches to feature storage and
retrieval.

**Benefits of establishing this best
practice:**

- Reduces training-serving skew, leading to more reliable model
performance in production.
- Increases developer productivity through feature reusability.
- Standardizes feature definitions across the organization.
- Improves model governance and auditability through feature
versioning.
- Saves costs by avoiding redundant feature computation and
storage.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Feature consistency between training and inference is critical for
machine learning system reliability. When the features used to
train a model differ from those used during inference, model
performance can degrade, a problem known as training-serving skew.
To avoid this issue, you need a centralized feature repository
that provides consistent access to the same feature definitions
and transformations across both training and inference
environments.

A feature store serves as this centralized repository, enabling
you to define, store, and retrieve features consistently. It
provides mechanisms for versioning features, which verifies that
you can maintain compatibility between models and the features
they expect as your data and feature engineering processes evolve.
Additionally, a feature store allows for the sharing and reuse of
features across multiple ML projects, increasing efficiency and
standardizing feature engineering practices across your
organization.

### Implementation steps

- **Set up Amazon SageMaker AI Feature
Store**. Create and configure a
[SageMaker AI
Feature Store](https://aws.amazon.com/sagemaker/feature-store/) to serve as your centralized repository
for ML features. SageMaker AI Feature Store provides both
online and offline storage capabilities: the online store
supports low-latency, real-time inference use cases, while
the offline store supports training and batch inference
processes. Create a feature group that defines your feature
structure, data types, and storage configurations using the
SageMaker AI SDK or console.
- **Define feature groups and
schemas**. Organize your features into logical
groups based on business domains, data sources, or ML use
cases. Define schemas for your features, including data
types, descriptions, and metadata. This organization makes
features more discoverable and more straightforward to
manage across your organization.
- **Implement feature ingestion
pipelines**. Build automated pipelines to ingest
and process raw data into features. Use
[SageMaker AI
Processing](https://docs.aws.amazon.com/sagemaker/latest/dg/processing-job.html),
[AWS Glue](https://aws.amazon.com/glue/), or
[Amazon EMR](https://aws.amazon.com/emr/) to transform raw data into feature values.
Configure both batch ingestion for historical data and
streaming ingestion for real-time updates using services
like
[Amazon Kinesis](https://aws.amazon.com/kinesis/) with SageMaker AI Feature Store.
- **Develop feature retrieval
mechanisms**. Create standardized ways to retrieve
features for both training and inference. For training
datasets, implement code that pulls features from the
offline store, while for inference, develop services that
query the online store. Verify that both paths use the same
feature definitions and transformations.
- **Integrate with ML
workflows**. Connect your feature store to your ML
pipelines by integrating it with
[SageMaker AI
Pipelines](https://aws.amazon.com/sagemaker/pipelines/) or your custom ML workflows. This makes
feature retrieval consistent throughout the ML lifecycle,
from experimentation to production deployment.
- **Monitor and validate
features**. Implement monitoring for your feature
store to detect data drift, missing values, or other quality
issues. Use
[SageMaker AI
Model Monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html) or custom validation scripts for
feature consistency and quality over time. Set up alerts for
deviations in feature distributions.
- **Enable feature discovery and
sharing**. Document your features with metadata and
descriptions to make them discoverable across your
organization. Integrate with data catalogs like
[AWSAWS Glue Data Catalog](https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html) to enhance discoverability and
governance of features.

## Resources

**Related documents:**

- [Get
started with Amazon SageMaker AI Feature Store](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store-getting-started.html)
- [Feature
Store concepts](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store-concepts.html)
- [Store,
Discover, and Share Machine Learning Features with Amazon SageMaker AI Feature Store](https://aws.amazon.com/blogs/machine-learning/unlock-ml-insights-using-the-amazon-sagemaker-feature-store-feature-processor/)
- [Unlock
ML insights using the Amazon SageMaker AI Feature Store Feature
Processor](https://aws.amazon.com/blogs/machine-learning/unlock-ml-insights-using-the-amazon-sagemaker-feature-store-feature-processor/)

**Related videos:**

- [Amazon SageMaker AI Feature Store: Store, discover, & share features
for ML apps](https://www.youtube.com/watch?v=pEg5c6d4etI)
- [Deep
dive on Amazon SageMaker AI Feature Store](https://www.youtube.com/watch?v=mHEUlPFT6xg)

**Related examples:**

- [Introduction
to Feature Store](https://sagemaker-examples.readthedocs.io/en/latest/sagemaker-featurestore/feature_store_introduction.html)
- [Amazon SageMaker AI Feature Store SageMaker AI Examples](https://github.com/aws/amazon-sagemaker-examples/tree/master/sagemaker-featurestore)
- [Amazon SageMaker AI Feature Store: Streaming Aggregation](https://github.com/aws-samples/amazon-sagemaker-feature-store-streaming-aggregation)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlrel03-bp02.html*

---

# MLREL03-BP03 Validate models with relevant data

Testing and validating machine learning models with appropriate data
is essential for reliable performance in production. Use real and
representative data that covers many possible patterns and scenarios
to avoid model failures when deployed in real-world environments.

**Desired outcome:** You establish
processes that validate your machine learning models with
real-world, representative data before deployment. You can identify
distribution mismatches between training, validation, test, and
inference data early, allowing you to address issues before they
impact production performance. Your validation approach includes
both real-world and engineered data to account for the scenarios
your model might encounter.

**Common anti-patterns:**

- Testing models with only synthetic data that doesn't represent
real-world conditions.
- Failing to check for distribution mismatch between training and
production data.
- Ignoring edge cases and rare scenarios in validation datasets.
- Using validation data that lacks diversity or has sampling
biases.
- Neglecting periodic revalidation after models are deployed.

**Benefits of establishing this best
practice:**

- Reduces risk of model failures in production environments.
- Enables early detection of data drift and model quality
degradation.
- Creates more robust models that perform well across expected
scenarios.
- Increases trust in model predictions from stakeholders.
- Improves alignment between model performance in testing and
production.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Validating your machine learning models with relevant data is a
critical step in the ML development lifecycle. Data that fails to
represent the full range of scenarios your model will encounter in
production can lead to poor performance, biased outputs, or
complete failures when deployed. The key challenge lies in
obtaining and using data that accurately mirrors your production
environment.

Begin by analyzing your data sources to capture the breadth and
depth of real-world scenarios. This includes common cases as well
as edge cases that might be rare but important. For example, a
model designed to detect fraudulent transactions needs exposure to
both typical and unusual fraud patterns. Missing these edge cases
can create vulnerabilities in your deployed model.

Pay particular attention to distribution mismatches, where the
statistical properties of your training, validation, test, and
eventual inference data differ. These mismatches often lead to
degraded model performance in production. For instance, if you
train a product recommendation model on data from one demographic
group but deploy it for a different group, the model may make
irrelevant recommendations.

Implement continuous monitoring after deployment to detect when
the data distribution shifts over time, which is common in
real-world applications. This allows you to retrain models before
performance degradation impacts business outcomes.

### Implementation steps

- **Establish data quality
criteria**. Define what constitutes representative
data for your use case. Include requirements for data
completeness, diversity, and coverage of edge cases.
Document these criteria as part of your ML development
process to create consistency across projects.
- **Implement cross-validation
techniques**. Use techniques like k-fold
cross-validation to verify that your model generalizes well
across different subsets of your data. This can identify
potential overfitting issues before deployment and provides
a more robust estimate of how your model will perform in
production.
- **Use Amazon SageMaker AI MLFlow
Tracking**. Set up experiments to track and compare
different training runs with various data configurations.
[SageMaker AI
MLFlow Tracking](https://docs.aws.amazon.com/sagemaker/latest/dg/mlflow-create-tracking-server.html) allows you to organize, monitor, and
evaluate your machine learning experiments systematically.
This can identify which data configurations lead to the best
performance and provides a historical record for future
reference.
- **Create engineered test
data**. Generate synthetic data to supplement
real-world data, especially for rare but important edge
cases. Verify that this synthetic data maintains the
statistical properties of real data while providing coverage
for scenarios that might be underrepresented in your
original dataset.
- **Implement data drift
detection**. Set up processes to continuously
compare the distribution of inference data with your
baseline training data. Use this comparison to identify when
the real-world data begins to diverge from what the model
was trained on, which can signal the need for retraining.
- **Use Amazon SageMaker AI Model
Monitor**. Deploy
[Model
Monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html) to automatically track and analyze model
behavior in production. Configure alerts for deviations in
model quality, data quality, bias drift, and feature
attribution drift. SageMaker AI Model Monitor continuously
evaluates your deployed models and notifies you when action
is needed.
- **Establish a regular validation
cadence**. Schedule periodic evaluations of your
model using fresh data, even if drift hasn't been detected.
This can catch subtle changes that might not trigger
automated alerts but could still affect model performance
over time.
- **Document validation
results**. Create detailed reports of validation
processes and outcomes for each model version. Include
metrics on data representativeness, performance across
different data segments, and identified gaps or biases.

## Resources

**Related documents:**

- [Evaluating
ML Models](https://docs.aws.amazon.com/machine-learning/latest/dg/evaluating_models.html)
- [Cross-Validation](https://docs.aws.amazon.com/machine-learning/latest/dg/cross-validation.html)
- [Accelerate
generative AI development using managed MLflow on Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/mlflow.html)
- [Data
and model quality monitoring with Amazon SageMaker AI Model
Monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html)
- [Amazon SageMaker AI Clarify](https://aws.amazon.com/sagemaker/clarify/)
- [Detect
data drift using Amazon SageMaker AI Model Monitor](https://aws.amazon.com/blogs/architecture/detecting-data-drift-using-amazon-sagemaker/)
- [Monitoring
in-production ML models at large scale using Amazon SageMaker AI
Model Monitor](https://aws.amazon.com/blogs/machine-learning/monitoring-in-production-ml-models-at-large-scale-using-amazon-sagemaker-model-monitor/)

**Related videos:**

- [How
To Efficiently Manage ML experiments using Amazon SageMaker AI ML
Flow](https://www.youtube.com/watch?v=3xkz_5HOP6k)
- [Detect
machine learning (ML) model drift in production](https://www.youtube.com/watch?v=J9T0X9Jxl_w)

**Related examples:**

- [Amazon SageMaker AI Model Monitor](https://github.com/aws/amazon-sagemaker-examples/tree/main/sagemaker_model_monitor)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlrel03-bp03.html*

---

# MLREL03-BP04 Establish data bias detection and mitigation

Detect and mitigate bias to avoid inaccurate model results.
Establish bias detection methodologies at data preparation stage
before training starts. Monitor, detect, and mitigate bias after the
model is in production. Establish feedback loops to track the drift
over time and initiate a re-training.

**Desired outcome:** You can identify
and address biases in your machine learning data and models,
providing fair and accurate predictions. You have established
systematic approaches for detecting bias before training and
continuously monitoring bias in production. Your AI systems produce
more reliable, fair, and trustworthy results through automated
detection and mitigation processes.

**Common anti-patterns:**

- Waiting until after model deployment to consider bias detection.
- Using a single bias metric for each use case without
understanding context-specific requirements.
- Focusing only on training data bias and ignoring bias that may
emerge in production.
- Failing to establish feedback mechanisms to monitor and address
drift over time.
- Treating bias detection as a one-time activity rather than an
ongoing process.

**Benefits of establishing this best
practice:**

- Improves model accuracy and fairness across different
demographic groups.
- Reduces risk of deploying models with harmful or discriminatory
outcomes.
- Enhances transparency and explainability for model predictions.
- Increases trust from users and stakeholders in AI systems.
- Improves adherence to emerging AI regulations and ethical
guidelines.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Bias in machine learning models can lead to unfair or inaccurate
outcomes that disproportionately impact certain groups. You need a
systematic approach to detect and mitigate bias throughout the
machine learning lifecycle. This begins with careful analysis of
your training data to identify potential imbalances or historical
biases that could be propagated by your models. By implementing
bias detection methodologies before training, you can address
issues early in the development process.

Once your models are in production, ongoing monitoring is
essential as new data patterns may introduce unexpected biases
over time. Setting up automated detection systems allows you to
continuously evaluate model fairness and take corrective actions
when necessary. Building feedback loops provides the data needed
to understand how bias manifests in real-world applications and
informs model retraining strategies.

Amazon SageMaker AI provides comprehensive tools like SageMaker AI
Clarify to implement bias detection and mitigation strategies
throughout the ML lifecycle. These tools offer quantitative
metrics to measure different types of bias and provide
explanations for model predictions to understand and address the
root causes of unfairness.

### Implementation steps

- **Understand different types of
bias**. Begin by educating your team about various
forms of bias that can affect machine learning models,
including selection bias, measurement bias, aggregation
bias, and evaluation bias. Educate your team members on how
bias can be introduced at different stages of the ML
lifecycle and the potential impacts on model predictions.
- **Analyze your training
data**. Use
[Amazon SageMaker AI Clarify](https://aws.amazon.com/sagemaker/clarify/) to examine your training data for
potential bias before model development. Analyze the
distribution of sensitive attributes and identify imbalances
or correlations that could lead to unfair outcomes. Address
data imbalances through techniques like resampling,
weighting, or generating synthetic data for underrepresented
groups.
- **Select appropriate bias
metrics**. Choose bias metrics that align with your
specific use case and fairness requirements. SageMaker AI
Clarify provides multiple pre-training bias metrics
including class imbalance, difference in proportions of
labels, and conditional demographic disparity. For
post-training, metrics like disparate impact, difference in
positive proportions across predicted labels, and accuracy
difference can evaluate model fairness.
- **Run SageMaker AI Clarify processing
jobs**. Integrate
[SageMaker AI
Clarify processing jobs](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-processing-job-run.html) into your ML pipeline to
analyze bias and provide explainability. Configure these
jobs to calculate bias metrics on your training data and
model predictions, identifying potential issues before
deployment.
- **Implement bias mitigation
strategies**. Address identified biases using
techniques like preprocessing (modifying training data),
in-processing (incorporating fairness constraints during
training), or post-processing (adjusting model outputs).
Experiment with different approaches and measure their
impact on both fairness metrics and model performance.
- **Set up production
monitoring**. Configure
[Amazon SageMaker AI Model Monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html) to continuously track bias
metrics on production data. Create alerts that alarm when
bias metrics exceed predefined thresholds, enabling prompt
investigation and remediation of emerging issues.
- **Establish feedback loops**.
Implement mechanisms to collect and analyze feedback on
model predictions, particularly focusing on cases where bias
may be present. Use this feedback to improve your
understanding of real-world bias patterns and inform model
retraining strategies.
- **Generate model governance
reports**. Use SageMaker AI Clarify to create
comprehensive reports on model fairness and explainability
for stakeholders, including risk and compliance-aligned
teams and external regulators. These reports should document
your bias detection and mitigation efforts, providing
transparency into your responsible AI practices.
- **Conduct regular model
reviews**. Schedule periodic reviews of your
models' fairness performance, bringing together
cross-functional teams to evaluate bias metrics, examine
challenging cases, and decide on necessary interventions or
improvements.

## Resources

**Related documents:**

- [Run
SageMaker AI Clarify Processing Jobs for Bias Analysis and
Explainability](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-processing-job-run.html)
- [Data
and model quality monitoring with Amazon SageMaker AI Model
Monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html)
- [Fairness,
model explainability and bias detection with SageMaker AI
Clarify](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-configure-processing-jobs.html)
- [Amazon SageMaker AI Clarify Detects Bias and Increases the Transparency
of Machine Learning Models](https://aws.amazon.com/blogs/aws/new-amazon-sagemaker-clarify-detects-bias-and-increases-the-transparency-of-machine-learning-models/)
- [Build
a secure enterprise machine learning platform on AWS](https://docs.aws.amazon.com/whitepapers/latest/build-secure-enterprise-ml-platform/build-secure-enterprise-ml-platform.html)

**Related videos:**

- [Introducing
Amazon SageMaker AI Clarify, part 1 - Bias detection](https://www.youtube.com/watch?v=jvcPZmnXaxo)
- [Introducing
Amazon SageMaker AI Clarify, part 2 - Model explainability](https://www.youtube.com/watch?v=1IGMG_c280E)
- [Responsible
use of artificial intelligence and machine learning](https://pages.awscloud.com/Responsible-Use-of-Artificial-Intelligence-and-Machine-Learning_2022_1007-MCL_OD.html)

**Related examples:**

- [Amazon SageMaker AI Clarify: ML Bias Detection and Explainability](https://github.com/aws/amazon-sagemaker-examples/tree/main/sagemaker-clarify)
- [Amazon SageMaker AI Model Monitoring](https://github.com/aws/amazon-sagemaker-examples/tree/default/%20%20%20ml_ops)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlrel03-bp04.html*

---

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

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
