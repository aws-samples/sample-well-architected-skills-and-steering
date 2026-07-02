# RAIDP04 — Dataset access and versioning

**Best Practices**: 5

---

# RAIDP04-BP01 Create a dataset registry

Create a registry to track dataset versions, metadata, and usage
across training, evaluation, and operational contexts. Store
datasets with version control, including local copies of public
benchmarks to assist builders with reproducibility as external
datasets evolve. Document the provenance, characteristics, and
intended use of each dataset version to enable others to understand
appropriate usage and limitations. Link dataset versions to specific
system training events and evaluation results to maintain
traceability between data changes and performance outcomes.

**Level of risk exposed if this best practice
is not established:** High

## Implementation considerations

- Build a centralized registry system that captures essential
metadata for each dataset including version numbers, creation
dates, source information, and intended use cases. Start with
a simple database or structured file system that can track
when datasets were created, who created them, and what they're
designed to test.
- Create version control workflows that automatically snapshot
datasets whenever changes are made like a version-controlled
code repository. Test your versioning system by making small
changes to a dataset and verifying you can retrieve both the
current and previous versions reliably.
- Set up local storage for copies of external benchmarks and
public datasets you use, rather than pulling from external
sources. Test this by comparing results from your local copy
against the original source to catch differences that could
affect reproducibility.
- Build linking mechanisms that connect specific dataset
versions to the training runs and evaluations that used them.
Test this traceability by picking a model performance result
and verifying you can trace back to the exact dataset version
that produced it.

## Resources

**Related documents:**

- [Onboarding
data in Amazon SageMaker AI Unified Studio](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/data-onboarding.html)

- [Access
your existing data and Resources through Amazon SageMaker AI
Unified Studio, Part 1: AWSAWS Glue Data Catalog and Amazon Redshift](https://aws.amazon.com/blogs/big-data/access-your-existing-data-and-resources-through-amazon-sagemaker-unified-studio-part-1-aws-glue-data-catalog-and-amazon-redshift/)

[Automate
data lineage in Amazon SageMaker AI using AWS Glue Crawlers
supported data sources](https://aws.amazon.com/blogs/big-data/automate-data-lineage-in-amazon-sagemaker-using-aws-glue-crawlers-supported-data-sources/)
- [ISO/IEC
42001:2023](https://www.iso.org/standard/42001) A.7.5 Data provenance

**Related tools:**

- [Data
discovery and cataloging in AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/catalog-and-crawler.html)
- [AWS Glue](https://aws.amazon.com/glue/)
- [Amazon SageMaker AI Catalog](https://aws.amazon.com/sagemaker/catalog/)
- [Accelerate
generative AI development with Amazon SageMaker AI AI and
MLflow](https://aws.amazon.com/sagemaker/ai/experiments/)
- Amazon SageMaker AI Unified Studio

*Source: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raidp04-bp01.html*

---

# RAIDP04-BP02 Periodically evaluate and update datasets in the registry

Schedule regular review cycles that assess whether existing datasets
still meet your evolving requirements and quality standards.
Increment version numbers and update associated documentation
whenever datasets change, maintaining records of what changed and
why. Assess whether dataset updates require corresponding system
retraining or evaluation re-runs to maintain validity of previous
results. Remove or archive outdated dataset versions while
preserving the ability to reproduce historical results when needed
for auditing or comparison purposes.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation considerations

- Schedule review processes that automatically flag datasets for
evaluation based on age, usage patterns, or changes in your
system requirements.
- Create change management workflows that require documenting
the reason for a dataset modification along with version
increments.
- Compare new dataset versions against established quality
metrics to catch degradation over time.
- Design impact assessment procedures that assist you to decide
when dataset changes require retraining your models or
re-running evaluations.
- Set up archival processes that move old dataset versions to
long-term storage while keeping enough metadata to recreate
historical results if needed.

## Resources

**Related documents:**

- [Data
Analytics Lens : Best practice 7.2 – Monitor for data quality
anomalies](https://docs.aws.amazon.com/it_it/wellarchitected/latest/analytics-lens/best-practice-7.2---monitor-for-data-quality-anomalies..html)
- [Generative
AI lens: GENOPS02-BP02 Monitor foundation model metrics](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/genops02-bp02.html)
- [Data
quality in Amazon SageMaker AI Unified Studio](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/data-quality.html)
- [AWS Glue Data Quality](https://docs.aws.amazon.com/glue/latest/dg/glue-data-quality.html)
- [Detecting
data drift using Amazon SageMaker AI](https://aws.amazon.com/blogs/architecture/detecting-data-drift-using-amazon-sagemaker/)
- [ISO/IEC
42001:2023](https://www.iso.org/standard/42001) A.7.5 Data provenance

**Related tools:**

- [Amazon SageMaker AI Catalog](https://aws.amazon.com/sagemaker/catalog/)
- [AWS Glue Data Quality](https://aws.amazon.com/glue/features/data-quality/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raidp04-bp02.html*

---

# RAIDP04-BP03 Protect data from being manipulated or accessed for unintended purposes

Implement the principle of least privilege, only providing access to
relevant data to those who really need it for both automated systems
and human users accessing your datasets. Consider scanning datasets
for unwanted content, including adversarial prompts, disinformation,
malware, or other data poisoning attempts that could affect
downstream system behavior. Establish access controls and audit
trails that track who accesses datasets and what modifications are
made. Use cryptographic verification methods where appropriate to
detect unauthorized changes to critical datasets, particularly those
used for evaluation or system operation.

**Level of risk exposed if this best practice
is not established:** High

## Implementation considerations

- Build permission systems that align access controls with
specific role requirements, assisting to reduce broad access
to data.
- Set up scanning tools that look for unwanted content like
adversarial prompts, fake information, or suspicious patterns
before a dataset gets used. These scanners should
automatically flag potential data poisoning attempts or
embedded malware that could affect your models.
- Create detailed logs that track who looked at which datasets,
when they accessed them, and what changes they made to the
data. Your audit trail should be detailed enough that you can
reconstruct exactly what happened during dataset operations.
- Use checksums or digital signatures on your most important
datasets so you can tell immediately they were changed without
permission. This is especially important for evaluation
datasets and operational data that your system relies on.
- Plan out what your team will do when security problems happen,
including how to quickly isolate manipulated datasets and
figure out which models or evaluations might be affected.

## Resources

**Related best practice:**

- RAISP02-BP02 Privacy: Build privacy-preserving mechanisms
into the core AI system
- RAISP03-BP02 Security: Implement security safeguards to block
AI-specific threats

**Related documents:**

- [Security
control recommendations for protecting data](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-controls-by-caf-capability/data-controls.html)
- [Onboarding
data in Amazon SageMaker AI Unified Studi](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/adminguide/data-onboarding.html)o
- [Data
and model quality monitoring with Amazon SageMaker AI Model
Monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html)
- [Detect
and filter harmful content by using Amazon Bedrock
Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html)
- [Monitor
model invocation using CloudWatch Logs and Amazon S3](https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html)
- [ISO/IEC
42001:2023](https://www.iso.org/standard/42001) A.7.3 Acquisition of data
- [ISO/IEC
42001:2023](https://www.iso.org/standard/42001) A.7.5 Data provenance

**Related videos:**

- [Data
protection strategies for the cloud - AWS Online Tech
Talks:](https://www.youtube.com/watch?v=4PgoBjqpm8U)
- [AWS re:Inforce 2023 - Using AWS data protection services for
innovation and automation (DAP305)](https://www.youtube.com/watch?v=jpT45GrbWGE)
- [AWS re:Invent 2024 - Achieve seamless and secure data sharing
(ANT325)](https://www.youtube.com/watch?v=VFQjR2JQCQM)

**Related examples:**

- [Amazon SageMaker AI Lakehouse now supports attribute-based access
control](https://aws.amazon.com/blogs/big-data/amazon-sagemaker-lakehouse-now-supports-attribute-based-access-control/)

**Related tools:**

- [Amazon SageMaker AI](https://aws.amazon.com/sagemaker/)
- [AWS Lake Formation](https://aws.amazon.com/lake-formation/)
- [Amazon S3 Access Grants](https://aws.amazon.com/s3/features/access-grants/)
- [AWS Identity and Access Management](https://aws.amazon.com/iam/)
- [AWS Key Management Service](https://aws.amazon.com/kms/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raidp04-bp03.html*

---

# RAIDP04-BP04 Establish governance procedures for managing your datasets

Maintain procedures for managing dataset access, retention, and
deletion throughout the AI system lifecycle. Implement mechanisms to
handle individual data requests, including the ability to remove
individual data points when contributors withdraw consent. Document
data lineage and retention policies that specify how long different
types of data can be stored and used. Create procedures for handling
governance-related dataset updates.

**Level of risk exposed if this best practice
is not established:** High

## Implementation considerations

- Create clear retention policies that specify how long
different types of data can be kept and when they need to be
deleted.
- Build workflows that let you quickly find and remove specific
data points when people request deletion or withdraw their
consent. Your system should be able to trace individual data
samples across training sets, evaluation datasets, and cached
model outputs without disrupting other parts of your data.
- Document the complete journey of your data from collection to
deletion, including who accessed it, when it was modified, and
which models or evaluations used it. This data lineage assists
you to understand the impact when you need to remove or modify
datasets for compliance-aligned reasons.
- Consider governance reviews with your legal team where you
check that your data handling practices match your policies
and legal obligations, including, but not limited to data
retention schedules, deletion requests, and access
controls.

## Resources

**Related documents:**

- [Responsible
AI](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/responsible-ai.html)
- [Generative
AI lifecycle](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/generative-ai-lifecycle.html)
- [Responsible
AI Best Practices: Promoting Responsible and Trustworthy AI
Systems](https://aws.amazon.com/blogs/enterprise-strategy/responsible-ai-best-practices-promoting-responsible-and-trustworthy-ai-systems/)
- [AWS Generative AI Best Practices Framework v2](https://docs.aws.amazon.com/audit-manager/latest/userguide/aws-generative-ai-best-practices.html)
- [ISO/IEC
42001:2023](https://www.iso.org/standard/42001) A.7.5 Data provenance

*Source: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raidp04-bp04.html*

---

# RAIDP04-BP05 Document the characteristics of each dataset using a datasheet

Create datasheets that document the intended uses, composition, and
collection process for each dataset. Include information about data
sources, collection methodologies, potential unwanted biases, and
recommended and prohibited use cases to assist others to understand
appropriate applications. Document the characteristics of data
contributors and annotators, including demographic information and
potential sources of unwanted bias that could affect system
behavior. Maintain datasheets as living documents that are updated
when datasets change or when new insights about their
characteristics or limitations are discovered.

**Level of risk exposed if this best practice
is not established:** High

## Implementation considerations

- If needed, create standardized datasheet templates that
capture essential information about each dataset. Your
template should cover basic information such as intended uses,
inappropriate uses, data sources, data labels, collection
methods, volumes, formats, as well as more nuanced aspects
like known limitations and potential biases.
- Complete the template. As appropriate, capture distributions
of sources by label types, and note unexpected distribution
skews, gaps in representation, and missing data. Characterize
the types of human or machine annotators (for example,
experience, training, and potential sources of bias). This
assists others understand who's represented in your data and
what perspectives shaped the labels or annotations.
- Set up processes to keep your datasheets current as you learn
more about your datasets or make changes to them. Schedule
regular reviews to update datasheets when you discover new
limitations, modify the data, or find better ways to describe
the dataset's characteristics and appropriate uses.

## Resources

**Related documents**

- [Datasheets
for Datasets](https://arxiv.org/pdf/1803.09010)
- [ISO/IEC
42001:2023](https://www.iso.org/standard/42001) A.7.5 Data provenance

*Source: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raidp04-bp05.html*

---
