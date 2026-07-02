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
