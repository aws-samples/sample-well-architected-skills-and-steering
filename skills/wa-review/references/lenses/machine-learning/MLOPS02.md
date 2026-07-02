# MLOPS02 — ML problem framing

**Pillar**: Operational Excellence  
**Best Practices**: 6

---

# MLOPS02-BP01 Establish ML roles and responsibilities

Clearly defining roles, responsibilities, and team interactions in
machine learning projects creates an efficient operational framework
that maximizes overall effectiveness. By understanding who does what
and how teams collaborate, organizations can streamline their ML
initiatives and deliver better business outcomes.

**Desired outcome:** You establish
well-defined roles and responsibilities across your ML teams,
enabling proper collaboration and accountability. You have
mechanisms to efficiently manage access controls for various ML
functions, providing your team members access to the tools and
resources they need while maintaining appropriate security
boundaries. This creates a foundation for successful ML operations
that supports both innovation and governance.

**Common anti-patterns:**

- Undefined or overlapping responsibilities causing confusion
among team members.
- Relying on a single person to perform ML-related tasks rather
than building specialized expertise.
- Over-privileged access controls that compromise security.
- Manual, one-time processes for managing user permissions that
don't scale.
- Siloed teams with poor communication channels between technical
and business stakeholders.

**Benefits of establishing this best
practice:**

- Clear accountability and ownership throughout the ML lifecycle.
- Improved collaboration between technical and business teams.
- Streamlined decision-making processes and faster project
initiation.
- Better governance and risk management through proper access
controls.
- Enhanced ability to scale ML operations across the organization.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Establishing clear ML roles and responsibilities requires
thoughtful planning about how teams will work together throughout
the entire ML lifecycle. Machine learning projects span multiple
domains including business expertise, data engineering, model
development, and operations, each requiring specialized skills.
Without clearly defined roles, projects often face delays, quality
issues, or governance challenges.

Begin by identifying which functions are critical for your
organization's ML initiatives. Consider your business objectives,
technical requirements, and regulatory constraints. Develop a team
structure that balances specialization with collaboration,
allowing for efficient workflows while maintaining appropriate
separation of duties for governance purposes.

For enterprise-grade ML solutions, establish cross-functional
teams with clear responsibilities for each role. Consider how
these roles interact throughout the ML lifecycle and create
communication channels to facilitate collaboration. Pay special
attention to governance responsibilities, as these are often
overlooked in early ML initiatives but become critical as projects
move into production.

### Implementation steps

- **Map ML functions to organizational
needs**. Begin by identifying the ML capabilities
required to support your business objectives. Consider the
entire ML lifecycle from problem definition through to
production monitoring. Review your current organizational
structure and identify gaps in skills or functions that need
to be addressed. Create a matrix showing the relationship
between ML functions and existing teams or roles.
- **Establish cross-functional teams
with defined roles**. Create a formal structure for
your ML organization with clear roles and responsibilities
for each team member. Gather representation from both
technical and business domains to maintain alignment with
business outcomes. The following roles should be considered:

**Domain expert:**
Provides functional knowledge about the business problem
and validates ML approaches against real-world
requirements.
- **Data engineer:**
Transforms raw data into formats suitable for analysis
and model training.
- **Data scientist:**
Applies statistical modeling and machine learning
techniques to derive insights from data.
- **ML engineer:** Converts
data science prototypes into production-ready software
systems.
- **MLOps engineer:**
Builds automation pipelines for model training, testing,
and deployment.
- **IT auditor:** Analyzes
system access, identifies anomalies, and recommends
remediations.
- **Model risk manager:**
Checks that models meet internal and external control
requirements.
- **Cloud security
engineer:** Configures and manages cloud
resources with appropriate security controls.
- **Prompt engineer:**
Designs effective interactions with foundation models
for generative AI applications.

- **Implement role-based access
control**. Design a permissions framework that
follows the principle of least privilege while enabling
teams to be productive. Avoid one-time methods for managing
access policies that don't scale. Instead, use
[Amazon SageMaker AI Role Manager](https://docs.aws.amazon.com/sagemaker/latest/dg/role-manager.html) to efficiently control
access based on pre-defined templates aligned with your
organizational roles. This allows administrators to quickly
create appropriate access policies within minutes, reducing
the time and effort required to onboard users and manage
permissions over time.
- **Establish governance
processes**. Create clear processes for model
lifecycle management, including approval workflows,
validation requirements, and regulatory checks. Document who
is responsible for key decisions at each stage of
development. Implement model monitoring mechanisms to track
performance and alert when intervention is needed. Use
[Amazon SageMaker AI Model Dashboard](https://docs.aws.amazon.com/sagemaker/latest/dg/model-dashboard.html) to maintain visibility
across your model inventory and track performance metrics.
- **Develop collaboration
frameworks**. Establish standard communication
channels and collaboration tools to facilitate interaction
between different roles. Create documentation templates that
promote knowledge sharing and make handoffs between teams
more efficient. Schedule regular cross-functional reviews to
gain alignment throughout the ML lifecycle. Consider using
[Amazon SageMaker AI Unified Studio](https://aws.amazon.com/sagemaker/unified-studio/) as a collaborative
environment that unifies data and AI workflows where data
scientists and engineers can work together.
- **Train teams on responsibilities and
interfaces**. Provide training to verify that your
team members understand not only their own responsibilities
but also how their work impacts others in the ML lifecycle.
Create reference materials that clarify handoff points and
dependencies between different roles. Consider establishing
a center of excellence or community of practice to share
knowledge and best practices across teams.
- **Adapt roles for generative AI
initiatives**. When implementing generative AI
projects, consider how traditional ML roles need to adapt.
Prompt engineers may be needed to design effective
interactions with foundation models. Ethical AI specialists
can address concerns around bias, transparency, and
responsible use. Integration engineers may be required to
connect foundation models from services like
[Amazon
Bedrock](https://aws.amazon.com/bedrock/) with enterprise applications and data
sources.

## Resources

**Related documents:**

- [Amazon SageMaker AI Role Manager](https://docs.aws.amazon.com/sagemaker/latest/dg/role-manager.html)
- [Personas
for an ML platform](https://docs.aws.amazon.com/whitepapers/latest/build-secure-enterprise-ml-platform/personas-for-an-ml-platform.html)
- [ML
Learning Paths](https://aws.amazon.com/training/learning-paths/machine-learning/)
- [Amazon SageMaker AI Model Dashboard](https://docs.aws.amazon.com/sagemaker/latest/dg/model-dashboard.html)
- [Why
should you use MLOps?](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-projects-why.html)
- [Amazon SageMaker AI ML Governance](https://aws.amazon.com/sagemaker/ml-governance/)
- [Define
customized permissions in minutes with Amazon SageMaker AI
Role Manager](https://aws.amazon.com/blogs/machine-learning/define-customized-permissions-in-minutes-with-amazon-sagemaker-role-manager/)
- [New
ML Governance Tools for Amazon SageMaker AI – Simplify Access
Control and Enhance Transparency Over Your ML Projects](https://aws.amazon.com/blogs/aws/new-ml-governance-tools-for-amazon-sagemaker-simplify-access-control-and-enhance-transparency-over-your-ml-projects/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlops02-bp01.html*

---

# MLOPS02-BP02 Prepare an ML profile template

Creating an ML profile template allows you to systematically capture
machine learning workload characteristics across different lifecycle
phases. Use this template to evaluate your ML workload's current
maturity status and strategically plan for improvements that align
with your business requirements.

**Desired outcome:** You gain a
comprehensive understanding of your ML workload's deployment
characteristics by creating templated profiles that capture critical
metrics and thresholds. By maintaining current and target profiles,
you can effectively track your ML workload maturity journey and make
data-driven decisions about architecture, resources, and deployment
options that best align with your business needs.

**Common anti-patterns:**

- Creating ML profiles without clear thresholds or maturity
rankings.
- Failing to document rationale for architectural and deployment
choices.
- Focusing on technical metrics without connecting to business
requirements.
- Not considering future state or alternative deployment options.
- Ignoring cost implications of different deployment scenarios.

**Benefits of establishing this best
practice:**

- Enables objective assessment of ML workload maturity status.
- Provides a structured approach to planning ML workload
improvements.
- Creates alignment between technical implementation and business
requirements.
- Facilitates better resource planning and cost optimization.
- Supports strategic decision-making with documented rationale.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Machine learning workloads have unique characteristics that impact
their deployment architecture, infrastructure requirements, and
operational management. Create a standardized ML profile template
to document these characteristics systematically across the stages
of the ML lifecycle. By capturing key metrics and establishing
thresholds, you can objectively assess the maturity level of your
ML workloads and identify areas for improvement.

For each ML workload, you should maintain at least two profiles:
one representing the current state and another representing the
target or future state. This approach creates a clear path for
improvement while documenting the rationale behind architectural
and deployment decisions.

When developing your ML profile template, focus on the most
impactful characteristics that influence infrastructure choices,
deployment options, and operational considerations. Include
metrics that span model characteristics, architectural decisions,
and operational requirements. For each characteristic, establish a
spectrum from lower to higher ranges to position your workload on
a maturity scale.

### Implementation steps

- **Capture ML workload deployment
characteristics**. Identify and document the most
impactful deployment characteristics of your ML workload.
These characteristics can determine optimal deployment
architecture, computing requirements, and instance sizing.
Use
[Amazon SageMaker AI Inference Recommender](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-recommender.html), which includes more
sophisticated instance selection algorithms and support for
multi-model endpoints, to optimize instance selection based
on your model's performance and cost requirements.
- **Document model deployment
characteristics**. Record key metrics about your ML
models, including:

Model size (model.tar.gz) in bytes
- Number of models deployed per endpoint
- Instance size (for example,
r5dn.4x.large) as suggested by the
inference recommender
- Retraining and model endpoint update frequency (hourly,
daily, weekly, monthly, or per-event)
- Model deployment location (on premises, Amazon EC2,
container, serverless, or edge)

- **Map architectural deployment
characteristics**. Capture information about the
internal architecture of your ML solution:

Inference pipeline architecture (single endpoint or
chained endpoints)
- Neural architecture (single framework like Scikit-learn
or multi-framework like PyTorch, Scikit-learn,
TensorFlow)
- Containers (SageMaker AI prebuilt container, bring your
own container)
- Location of containers and models (on premises, cloud,
or hybrid)
- Serverless inferencing (pay as you go) options like
Amazon SageMaker AI Serverless Inference
- [Inference
Components](https://docs.aws.amazon.com/sagemaker/latest/dg/multi-model-endpoints.html) for modular inference pipeline
architecture (mix and match pre-processing, model
serving, and post-processing components)

- **Define traffic pattern
characteristics**. Document how your ML model will
be used:

Traffic pattern (steady or spiky)
- Input size (number of bytes)
- Latency requirements (low, medium, high, or batch)
- Concurrency needs (single thread or multi-thread)

- **Determine cold start
tolerance**. Document the acceptable latency for
cold starts in milliseconds, as this impacts the choice
between always-on and serverless deployment options.
- **Evaluate network deployment
characteristics**. Assess and document
network-related requirements, including AWS KMS encryption
needs, multi-variant endpoints, network isolation
requirements, and use of third-party Docker repositories.
- **Analyze cost
considerations**. Document cost considerations for
different deployment options, including the potential use of
Amazon EC2 Spot Instances for non-critical workloads, Amazon SageMaker AI Serverless Inference for pay-per-use models, or
multi-model endpoints for cost sharing.
- **Create a provisioning
matrix**. Develop a matrix of expected capacity
requirements across different environments (development,
staging, production) and regions. This should include the
number and types of instances needed for training, batch
inference, real-time inference, and development notebooks.
- **Map workload characteristics across
maturity spectrum**. For each characteristic in
your profile, establish a spectrum from lower to higher
maturity. This spectrum positions your current
implementation and defines targets for improvement.
- **Document rationale for target
profile**. Provide clear justification for the
values selected in your target profile, linking them to
specific business requirements and expected outcomes.
- **Evaluate and update profiles
regularly**. Revisit your ML profiles periodically
to check that they remain aligned with evolving business
requirements and to incorporate learnings from production
experience.
- **Foundation model deployment
considerations**. For generative AI workloads,
include additional profile characteristics such as model
quantization level, context window requirements, token
processing speed, and memory footprint using
[optimized
foundation model containers](https://docs.aws.amazon.com/sagemaker/latest/dg/large-model-inference.html) to properly size
infrastructure for these resource-intensive models.

## Resources

**Related documents:**

- [SageMaker AI
Inference Recommender](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-recommender.html)
- [AWS Pricing Calculator - SageMaker AI](https://calculator.aws/#/addService/SageMaker AI)
- [Deploy
models with Amazon SageMaker AI Serverless Inference](https://docs.aws.amazon.com/sagemaker/latest/dg/serverless-endpoints.html)
- [Multi-model
endpoints](https://docs.aws.amazon.com/sagemaker/latest/dg/multi-model-endpoints.html)
- [Amazon EC2 Instance Types](https://aws.amazon.com/ec2/instance-types/)
- [What
is Amazon SageMaker AI?](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html)
- [Improved
ML model deployment using Amazon SageMaker AI Inference
Recommender](https://aws.amazon.com/blogs/machine-learning/improved-ml-model-deployment-using-amazon-sagemaker-inference-recommender/)
- [Unlock
cost savings with the new scale down to zero feature in
SageMaker AI Inference](https://aws.amazon.com/blogs/machine-learning/unlock-cost-savings-with-the-new-scale-down-to-zero-feature-in-amazon-sagemaker-inference/)
- [Beyond
the basics: A comprehensive foundation model selection
framework for generative AI](https://aws.amazon.com/blogs/machine-learning/beyond-the-basics-a-comprehensive-foundation-model-selection-framework-for-generative-ai/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlops02-bp02.html*

---

# MLOPS02-BP03 Establish model improvement strategies

Planning improvement drivers for optimizing machine learning model
performance is essential before development begins. By establishing
a clear strategy for model enhancement, you can systematically
improve your ML models through techniques like data collection,
cross-validation, feature engineering, hyperparameter tuning, and
ensemble methods.

**Desired outcome:** By implementing
this best practice, you establish a systematic approach for
improving your machine learning models. You create a structured
methodology for experimentation that allows you to progressively
enhance model performance by testing different improvement
strategies. You gain visibility into which approaches yield the best
results for your specific use case, enabling you to make data-driven
decisions about model development and optimization.

**Common anti-patterns:**

- Starting with overly complex models without establishing a
baseline performance.
- Ignoring data quality issues and focusing solely on model
complexity.
- Making arbitrary hyperparameter changes without systematic
experimentation.
- Neglecting to document experimental results and configurations.
- Implementing advanced techniques without understanding
fundamental model performance issues.

**Benefits of establishing this best
practice:**

- Enables structured experimentation and measurable model
improvements.
- Provides clarity on which improvement strategies deliver the
best results.
- Reduces time spent on ineffective optimization approaches.
- Creates a systematic pathway from simple to more advanced
modeling techniques.
- Identifies the most important features and data for your
specific business problem.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Effective model improvement requires a structured approach that
follows a progression from simple to complex. Begin by
establishing clear performance metrics tied to your business
objectives, as these will guide your improvement efforts. Develop
a baseline model using straightforward algorithms and minimal
feature engineering to set initial performance benchmarks.

Organizing your experiments systematically is crucial. Document
your approach, model configurations, and results to track
improvements and understand the impact of different strategies.
This documentation serves as institutional knowledge that can
guide future model development and improvement efforts.

Work closely with domain experts who understand the business
context. Their insights can identify key features, validate model
outputs, and align your improvements with business objectives.
Remember that model improvement is an iterative process requiring
patience and methodical experimentation.

### Implementation steps

- **Create a baseline model with minimal
complexity**. Start with minimal data cleaning and
the most obvious data features. Train simple classical
models using algorithms like linear regression or logistic
regression for classification tasks. This establishes a
performance benchmark against which you can measure
improvements. Use
[Amazon SageMaker AI](https://aws.amazon.com/sagemaker/) to quickly develop these baseline models.
- **Organize and track experiments using
MLFlow on Amazon SageMaker AI**. Use
[Amazon SageMaker AI MLFlow](https://docs.aws.amazon.com/sagemaker/latest/dg/mlflow.html) to organize and track multiple
tests comparing different configurations and algorithms.
This allows you to maintain a structured approach to
experimentation and compare results across different model
versions so you can identify which changes lead to
meaningful improvements.
- **Implement effective feature
selection**. Collaborate with subject matter
experts to identify the most significant features related to
target values. Iteratively add more complex features and
remove less important ones to improve model accuracy and
robustness. Test different feature engineering techniques
such as one-hot encoding, normalization, and dimensionality
reduction to understand their impact on model performance.
- **Consider deep learning for complex
patterns**. When you have large volumes of training
data, consider deep learning models to discover previously
unknown features and improve model accuracy.
[Amazon SageMaker AI](https://aws.amazon.com/sagemaker/) provides built-in algorithms for deep
learning and supports popular frameworks like TensorFlow and
PyTorch, making it simpler to experiment with neural network
architectures.
- **Explore ensemble methods**.
Ensemble methods can provide further accuracy improvements
by combining the best characteristics of various algorithms.
Consider techniques like random forests, gradient boosting,
or stacking different models. Be aware of the tradeoffs with
computational performance and maintenance complexity,
evaluating whether these approaches align with your specific
business use case.
- **Apply automatic machine learning
(AutoML)**. Use
[Amazon SageMaker AI Canvas](https://aws.amazon.com/sagemaker/canvas/) for no-code/low-code ML model
development with natural language support for data
exploration and preparation. Canvas includes
[Amazon Q integration](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-q-integration.html) for conversational data analysis and
can directly deploy models to production.
- **Optimize hyperparameters
systematically**. Fine-tune hyperparameters for
each algorithm to obtain optimal performance. Use
[Amazon SageMaker AI Hyperparameter Optimization](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning-how-it-works.html) to automate
this process through techniques like Bayesian optimization,
grid search, or random search to find the most effective
parameter combinations.
- **Integrate experiments into automated
workflows**.
[Automate
your experimental trials using SageMaker AI Pipelines](https://docs.aws.amazon.com/sagemaker/latest/dg/pipelines-experiments.html) by
using the integration with experiments. This fosters
reproducibility and creates a systematic approach to model
improvement that can be incorporated into your ML operations
workflow.
- **Use generative AI for synthetic data
creation**. For scenarios with limited training
data, use generative AI techniques like generative
adversarial networks (GANs) to create synthetic data that
can expand your training dataset.
[Amazon SageMaker AI JumpStart](https://aws.amazon.com/sagemaker/jumpstart/) provides an expanded library of
pre-built generative AI models and more industry-specific
solutions, while
[Amazon
Bedrock](https://aws.amazon.com/bedrock/knowledge-bases/) offers foundation models that can augment
your training data, especially for scenarios with limited or
imbalanced datasets.
- **For generative AI workloads, apply
foundation models with RAG for knowledge-intensive
tasks**. For tasks requiring domain knowledge,
implement retrieval-augmented generation (RAG) using
[Amazon
Bedrock](https://aws.amazon.com/bedrock/knowledge-bases/) to enhance foundation models with your
organization's specific information, combining the power of
large language models with your proprietary data.

## Resources

**Related documents:**

- [Amazon SageMaker AI Experiments in Studio Classic](https://docs.aws.amazon.com/sagemaker/latest/dg/experiments.html)
- [Accelerate
generative AI development using managed MLFlow on SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/mlflow.html)
- [Amazon SageMaker AI Canvas](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas.html)
- [Automatic
model tuning with SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/automatic-model-tuning.html)
- [SageMaker AI
JumpStart pretrained models](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-jumpstart.html)
- [Amazon SageMaker AI Experiments Integration](https://docs.aws.amazon.com/sagemaker/latest/dg/pipelines-experiments.html)
- [Create,
store, and share features with Feature Store](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store.html)
- [Model
Registration Deployment with Model Registry](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry.html)
- [LLM
experimentation at scale using Amazon SageMaker AI Pipelines and
MLFlow](https://aws.amazon.com/blogs/machine-learning/llm-experimentation-at-scale-using-amazon-sagemaker-pipelines-and-mlflow/)

**Related examples:**

- [Amazon SageMaker AI Experiments Examples](https://github.com/aws/amazon-sagemaker-examples/tree/main/sagemaker-experiments)
- [Hyperparameter
Tuning Examples](https://github.com/aws/amazon-sagemaker-examples/tree/main/hyperparameter_tuning)
- [Ensemble
Predictions from Multiple Models](https://sagemaker-examples.readthedocs.io/en/latest/introduction_to_applying_machine_learning/ensemble_modeling/EnsembleLearnerCensusIncome.html)
- [Amazon SageMaker AI Autopilot Examples](https://github.com/aws/amazon-sagemaker-examples/tree/main/autopilot)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlops02-bp03.html*

---

# MLOPS02-BP04 Establish a lineage tracker system

Maintain a system that tracks changes for each release to enable
reproducibility, speed up problem diagnosis, and improve regulatory
adherence. Tracking lineage for model development includes changes
in documentation, environment, model, data, code, and
infrastructure.

**Desired outcome:** You have a
comprehensive lineage tracking system that records the history of
artifacts involved in your ML model development and deployment
lifecycle. This system enables you to reproduce previous model
versions, diagnose issues quickly, roll back to stable versions when
needed, and improve your regulatory adherence. Your organization can
trace model results back to their originating data sources, code
versions, and infrastructure configurations.

**Common anti-patterns:**

- Manually tracking changes in spreadsheets or documents.
- Not capturing all dependent artifacts necessary for model
reproduction.
- Inconsistent tracking practices across teams.
- Lacking integration between different components of the ML
pipeline.
- Failing to track infrastructure and environment configurations.

**Benefits of establishing this best
practice:**

- Enables reproducibility of model versions for debugging.
- Accelerates problem diagnosis and resolution when issues arise.
- Supports regulatory adherence and audit requirements.
- Facilitates rollback to previous stable versions when needed.
- Improves collaboration among team members with transparent
tracking.
- Enhances model governance and responsible AI practices.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Implementing a comprehensive lineage tracker system is essential
for maintaining the traceability and reproducibility of your
machine learning models. Without proper lineage tracking, your
organization may struggle to debug issues, comply with
regulations, or reproduce previous model versions when needed. The
lineage tracker should capture information about components that
influence your model's behavior, including the data used for
training, preprocessing steps, hyperparameters, model
architecture, evaluation metrics, and deployment environment.

A robust lineage tracking system starts with identifying the key
artifacts that need to be tracked throughout the ML lifecycle.
Once identified, you can use AWS services like SageMaker AI ML
Lineage Tracking to automatically record and store the
relationships between these artifacts. This information becomes
invaluable when you need to audit your models, reproduce results,
or diagnose issues in production.

For example, if a model suddenly begins producing unexpected
results in production, your lineage tracking system should allow
you to trace back to the exact version of the model, the data it
was trained on, the code used to train it, and the infrastructure
configuration at the time of deployment. This comprehensive
tracking enables faster problem resolution and maintains trust in
your ML systems.

### Implementation steps

- **Identify artifacts needed for
tracking**. Begin by identifying artifacts that
contribute to your model's development and deployment. This
includes raw data, processed data, feature sets, model
parameters, code versions, training environments, and
deployment configurations. Understanding what needs to be
tracked is essential for meeting regulatory requirements and
enabling reproducibility. Refer to
[Data
and artifacts lineage tracking](https://docs.aws.amazon.com/whitepapers/latest/build-secure-enterprise-ml-platform/data-and-artifacts-lineage-tracking.html) for guidance on the
artifacts to include.
- **Implement SageMaker AI ML Lineage
Tracking**. Use
[Amazon SageMaker AI ML Lineage Tracking](https://docs.aws.amazon.com/sagemaker/latest/dg/lineage-tracking-entities.html) to automatically record
information about the steps in your ML workflow. SageMaker AI
tracks relationships between datasets, algorithms, training
jobs, and model artifacts, enabling you to reproduce
workflows, track model and dataset lineage, and establish
governance standards. The service creates entities for your
ML workflow components and stores their relationships,
making it more straightforward to audit and verify model
provenance.
- **Set up SageMaker AI Unified
Studio**. Use
[Amazon SageMaker AI Unified Studio](https://aws.amazon.com/sagemaker/unified-studio/) as your integrated
development environment that unifies data and AI workflows.
SageMaker AI Unified Studio provides enhanced collaborative
features, team sharing capabilities, and visual tools to
track the lineage of your ML pipelines, making it more
straightforward to understand the relationships between
different components across data and AI personas.
- **Configure SageMaker AI Feature
Store**. Implement
[Amazon SageMaker AI Feature Store](https://aws.amazon.com/sagemaker/feature-store/) to create a centralized
repository for storing, sharing, and managing features with
enhanced feature management capabilities. This purpose-built
repository enables you to organize features in a consistent
way, making them easily accessible across teams. SageMaker AI
Feature Store fosters feature consistency between training
and inference phases without requiring additional code, and
maintains a record of feature versions over time.
- **Use SageMaker AI Model
Registry**. Implement
[Amazon SageMaker AI Model Registry](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry.html) to catalog models for
production, manage model versions, and associate metadata
with models. The Model Registry enables lineage tracking by
maintaining a history of model versions, approval status,
and deployment details. This creates a centralized
repository for managing model lifecycles, which facilitates
governance and improves adherence to regulations.
- **Build ML pipelines with SageMaker AI
Pipelines**. Create reproducible ML workflows using
[Amazon SageMaker AI Pipelines](https://aws.amazon.com/sagemaker/pipelines/) to automate and standardize the
steps in your ML process. SageMaker AI Pipelines allows you to
track data history within the pipeline and integrates with
SageMaker AI ML Lineage Tracking to analyze input data, its
sources, and generated outputs. This integration creates
comprehensive lineage tracking across your entire ML
workflow.
- **Implement version control
practices**. Use version control systems like Git
for code, model configurations, and pipeline definitions.
Integrate these systems with your lineage tracking to
properly link code changes to model versions and training
runs. This practice maintains a complete history of how your
models have evolved over time.
- **Establish model attributes for
training runs**. Use model attributes in SageMaker AI
to track specific details about your training runs. This
allows you to compare different experiments, understand
which parameters led to better model performance, and
maintain records of training decisions. For more detail, see
[Using
model attributes to track your training runs on Amazon SageMaker AI](https://aws.amazon.com/blogs/machine-learning/amazon-sagemaker-now-comes-with-new-capabilities-for-accelerating-machine-learning-experimentation/).
- **Implement access controls and
auditing**. Set up appropriate access controls for
your lineage data and implement auditing capabilities to
track who accesses or modifies lineage information. Use
[AWS Lake Formation](https://aws.amazon.com/lake-formation/) with SageMaker AI Studio to control and
audit data exploration activities, as demonstrated in this
[example](https://github.com/aws-samples/amazon-sagemaker-studio-audit).
- **Develop regular verification
processes**. Establish procedures to regularly
verify that your lineage tracking system is capturing
necessary information for compliance-aligned purposes.
Create automated reports that demonstrate the completeness
of your lineage tracking to adhere to regulatory
requirements.
- **Foundation model lineage
tracking**. Consider implementing
[Amazon
Bedrock](https://aws.amazon.com/bedrock/knowledge-bases/) for tracking lineage in generative AI
applications. With foundation models becoming increasingly
important, tracking prompt engineering changes, model
parameters, and fine-tuning datasets is critical for
reproducibility and governance of generative AI systems. Use
Amazon Bedrock's governance features to maintain
comprehensive lineage tracking when working with foundation
models.

## Resources

**Related documents:**

- [Lineage
Tracking Entities](https://docs.aws.amazon.com/sagemaker/latest/dg/lineage-tracking-entities.html)
- [Track
the lineage of a pipeline](https://docs.aws.amazon.com/sagemaker/latest/dg/pipelines-lineage-tracking.html)
- [MLOps
Automation With SageMaker AI Projects](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-projects.html)
- [Data
and artifacts lineage tracking](https://docs.aws.amazon.com/whitepapers/latest/build-secure-enterprise-ml-platform/data-and-artifacts-lineage-tracking.html)
- [Pipelines](https://docs.aws.amazon.com/sagemaker/latest/dg/pipelines.html)
- [Model
Registration Deployment with Model Registry](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry.html)
- [Create,
store, and share features with Feature Store](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store.html)

**Related examples:**

- [End-to-End
MLOps with Amazon SageMaker AI](https://github.com/aws-samples/amazon-sagemaker-mlops-workshop)
- [Controlling
and auditing data exploration activities with SageMaker AI Studio
and AWS Lake Formation](https://github.com/aws-samples/amazon-sagemaker-studio-audit)
- [SageMaker AI
Feature Store Examples](https://github.com/aws/amazon-sagemaker-examples/tree/master/sagemaker-featurestore)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlops02-bp04.html*

---

# MLOPS02-BP05 Establish feedback loops across ML lifecycle phases

Establishing feedback loops across machine learning (ML) lifecycle
phases is essential for continuous improvement of ML workloads. By
implementing robust mechanisms to share successful experiments,
analyze failures, and document operational activities, you can
enhance model performance and adapt to changing data patterns over
time. Feedback loops can identify model drifts and enable
practitioners to refine monitoring and retraining strategies,
allowing for experimentation with data augmentation and different
algorithms until optimal outcomes are achieved.

**Desired outcome:** You have
established comprehensive feedback mechanisms across your ML
lifecycle that facilitate continuous learning and improvement. Your
organization can detect model drift early, automatically initiate
retraining when needed, and incorporate human review when
appropriate. This creates a culture of experimentation where
successes and failures contribute equally to knowledge advancement,
improving both model quality and operational efficiency over time.

**Common anti-patterns:**

- Treating model deployment as the final step without ongoing
evaluation.
- Failing to document experiments and operational learnings.
- Ignoring model drift until it significantly impacts performance.
- Working in silos without sharing insights across ML teams.
- Lacking automated processes to respond to detected model issues.

**Benefits of establishing this best
practice:**

- Early detection of model performance degradation.
- Reduced manual effort through automated monitoring and
retraining.
- Improved model quality through systematic experimentation.
- Knowledge retention and sharing across teams.
- Enhanced ability to adapt to changing data patterns.
- Accelerated innovation through documented learnings.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Feedback loops are crucial to maintaining the effectiveness of ML
models over time. As real-world data evolves, the performance of
deployed models can deteriorate due to concept drift or model
drift. By establishing systematic feedback mechanisms, you can
monitor these changes, learn from them, and adapt your models
accordingly.

A comprehensive feedback loop strategy begins with monitoring
model performance metrics and comparing them against baseline
expectations. When deviations occur, automated alerts can notify
teams or run retraining pipelines. The results of these actions
should be documented to inform future development decisions. This
creates a continuous cycle of learning where each iteration builds
upon previous insights.

For example, a financial services company deployed a fraud
detection model that began showing decreased accuracy after six
months. Their established feedback system detected this drift,
automatically started a retraining pipeline using recent data, and
documented the patterns that caused the drift. Data scientists can
use this information to improve feature engineering in subsequent
model versions, resulting in more resilient performance.

Human review is also an essential component of feedback loops,
especially for sensitive applications. Including human validation
through tools like Amazon A2I provides ground truth data that can
be used to further refine models and build trust in automated
decisions.

### Implementation steps

- **Establish comprehensive model
monitoring with SageMaker AI Model Monitor**.
Amazon SageMaker AI Model Monitor provides capabilities to
continuously monitor the quality of machine learning models
in production. Configure it to detect data and concept drift
by comparing production data statistics against the
baseline. SageMaker AI Model Monitor supports monitoring data
quality, model quality, bias drift, and feature attribution
drift, providing a complete view of your model's performance
over time.
- **Configure CloudWatch alerts and
notifications**. Set up
[Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) to monitor metrics generated by SageMaker AI
Model Monitor and create custom dashboards to visualize
model performance. Configure CloudWatch Alarms to send
notifications when thresholds are exceeded, indicating
potential model drift. These notifications can be delivered
using SNS topics to email, SMS, or other channels for prompt
attention.
- **Implement the SageMaker AI Model
Dashboard**. Use the
[SageMaker AI Model Dashboard](https://docs.aws.amazon.com/sagemaker/latest/dg/model-dashboard.html) as the central interface for
tracking models and their performance. The dashboard
provides a comprehensive view of deployed models, their
endpoints, monitoring schedules, and historical behavior.
This allows teams to quickly identify issues and understand
performance trends across multiple models.
- **Automate retraining
pipelines**. Create automated retraining workflows
using
[AWS Step Functions](https://aws.amazon.com/step-functions/) and
[SageMaker AI
Pipelines](https://docs.aws.amazon.com/sagemaker/latest/dg/pipelines.html). Configure
[EventBridge
Events](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) rules to run these pipelines when SageMaker AI
Model Monitor detects drift or anomalies. This verifies that
models are retrained with fresh data when performance begins
to degrade, maintaining high accuracy with minimal manual
intervention.
- **Incorporate human review with Amazon
A2I**. Implement
[Amazon
Augmented AI (A2I)](https://aws.amazon.com/augmented-ai/) to route predictions with low
confidence scores to human reviewers. This creates a
human-in-the-loop feedback mechanism where reviewers can
validate model outputs and provide corrections. The reviewed
data becomes valuable ground truth that can be used to
improve model performance in future iterations.
- **Document and share
learnings**. Create a knowledge repository using
services like
[Quick with GenBI capabilities](https://aws.amazon.com/quicksight/generative-bi/) to automatically
generate visualizations and dashboards, and
[Amazon S3](https://aws.amazon.com/s3/) for storing experiment results and operational
reports. This documentation should include successful
approaches, failed experiments, and operational insights to
facilitate knowledge sharing across teams.
- **Establish regular feedback review
sessions**. Schedule recurring meetings with
stakeholders to review monitoring results, discuss model
performance, and prioritize improvements. These sessions
should include data scientists, ML engineers, and business
stakeholders to align between technical improvements and
business outcomes.

## Resources

**Related documents:**

- [Data
and model quality monitoring with Amazon SageMaker AI Model
Monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html)
- [Amazon SageMaker AI Model Dashboard](https://docs.aws.amazon.com/sagemaker/latest/dg/model-dashboard.html)
- [Amazon
Augmented AI (A2I)](https://aws.amazon.com/augmented-ai/)
- [Train
a machine learning model using Amazon SageMaker AI](https://docs.aws.amazon.com/step-functions/latest/dg/sample-train-model.html)
- [Pipelines](https://docs.aws.amazon.com/sagemaker/latest/dg/pipelines.html)
- [Creating
rules that react to events in Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-create-rule.html)
- [Monitoring
Amazon ML with Amazon CloudWatch Metrics](https://docs.aws.amazon.com/machine-learning/latest/dg/cw-doc.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlops02-bp05.html*

---

# MLOPS02-BP06 Review fairness and explainability

Evaluating model fairness and explainability verifies that your
machine learning solutions are ethical, transparent, and equitable
across user groups. By systematically addressing these concerns
throughout the ML lifecycle, you build trust with stakeholders and
reduce the risk of harmful bias in your models.

**Desired outcome:** You implement a
comprehensive approach to fairness and explainability across your
machine learning lifecycle. You can identify potential biases in
data and models, explain model predictions to stakeholders, and know
that your AI systems make equitable decisions across user segments.
Your ML systems are continuously monitored for fairness, comply with
relevant regulations, and maintain transparency that builds trust
with users and stakeholders.

**Common anti-patterns:**

- Treating fairness as an afterthought rather than integrating it
throughout the ML lifecycle.
- Focusing solely on model accuracy without considering ethical
implications.
- Using non-representative training data that leads to biased
outcomes.
- Deploying complex, opaque models when explainability is
required.
- Failing to monitor models in production for drift in fairness
metrics.

**Benefits of establishing this best
practice:**

- Builds trust with customers and stakeholders through transparent
AI systems.
- Reduces the risk of regulatory issues related to algorithmic
fairness.
- Identifies and mitigates harmful biases before models enter
production.
- Enables better understanding of model decisions through
explainability techniques.
- Creates more inclusive AI systems that work equitably for user
groups.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Fairness and explainability should be considered fundamental
components of your machine learning development process rather
than optional add-ons. Approaching these concerns proactively can
verify that your models work equitably for your users while
providing transparency into how decisions are made.

Start by assessing the ethical implications of your ML solution
during problem framing. Consider whether an algorithm is the
appropriate approach and what impacts it might have on different
user groups. For data management, analyze whether your training
data adequately represents the diversity of your user population,
and check for existing biases in labels or features that could be
perpetuated by your model.

During training and evaluation, consider incorporating fairness
constraints directly into your optimization functions. Evaluate
models using appropriate fairness metrics alongside traditional
performance measures. When deploying models, carefully assess
whether the deployment context matches the training conditions,
especially regarding population characteristics. Finally,
implement robust monitoring systems to track fairness metrics over
time and detect emerging bias.

Amazon SageMaker AI Clarify provides comprehensive tools for
addressing fairness and explainability throughout the ML
lifecycle. It offers bias detection capabilities for both data and
models, along with explainability features through SHAP (Shapley
Additive Explanations) values that provide an understanding of how
individual features contribute to predictions.

### Implementation steps

- **Assess ethical implications during
problem framing**. Before building an ML model,
evaluate whether an algorithmic approach is ethical for your
specific use case. Consider potential unintended
consequences and whether the benefits outweigh potential
risks. Document your assessment and decision-making process
for transparency.
- **Evaluate and prepare representative
training data**. Use
[Amazon SageMaker AI Clarify](https://aws.amazon.com/sagemaker/clarify/) with enhanced bias detection and
new fairness metrics to analyze your training data for
potential biases, particularly regarding protected
attributes or sensitive groups. Verify that your data
accurately represents the population on which the model will
be deployed. Apply appropriate sampling or augmentation
techniques to address identified representation gaps.
- **Implement bias detection in the
model development process**. Configure SageMaker AI
Clarify to evaluate pre-training bias metrics that assess
imbalances in your training data. These metrics can identify
issues like class imbalance, label imbalance across groups,
or feature distribution disparities that could lead to
unfair outcomes.
- **Select appropriate fairness metrics
for evaluation**. Depending on your specific use
case, choose relevant fairness metrics such as disparate
impact, difference in positive proportions, or equal
opportunity difference. These metrics quantify whether your
model treats different groups equitably and should be
tracked alongside traditional performance metrics.
- **Apply explainability techniques to
understand model decisions**. Implement
[SHAP
(Shapley Additive Explanations)](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-shapley-values.html) through SageMaker AI
Clarify to understand feature importance and how different
features influence model predictions. This can identify
whether protected attributes or proxies for them are
disproportionately influencing outcomes.
- **Consider model complexity tradeoffs
with explainability requirements**. If
explainability is a critical requirement, consider using
simpler model architectures (like linear models or decision
trees) that are inherently more interpretable. For complex
models like deep neural networks, implement robust
explainability tools.
- **Implement bias monitoring in
production environments**. Configure
[SageMaker AI
Model Monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html) to continuously track fairness metrics
for deployed models. Set up alerts for drift in fairness
metrics that might indicate emerging bias issues requiring
intervention.
- **Establish governance processes for
addressing detected bias**. Create clear procedures
for when bias is detected, including who is responsible for
review, what remediation steps should be taken, and how
stakeholders should be informed. Document these processes to
verify that they are consistently applied.
- **Train teams on fairness and
explainability concepts**. Verify that data
scientists, ML engineers, and other stakeholders understand
fairness concepts, bias mitigation techniques, and how to
interpret explainability outputs. Regular training sessions
build organizational capacity for responsible AI.
- **Document fairness and explainability
considerations**. Maintain comprehensive
documentation of fairness evaluations, explainability
analyses, and mitigation strategies applied. This
documentation supports transparency, aids regulatory
adherence efforts, and communicates your responsible AI
approach to stakeholders.
- **Foundation model fairness
considerations**. Use foundation models and
generative AI to enhance fairness and explainability efforts
by generating diverse synthetic data to address
representation gaps, creating plain-language explanations of
complex model decisions for different stakeholder groups,
and automating the generation of comprehensive documentation
about model fairness evaluations and mitigations.

## Resources

**Related documents:**

- [Model
Explainability](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-model-explainability.html)
- [Feature
Attributions that Use Shapley Values](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-shapley-values.html)
- [Fairness,
model explainability and bias detection with SageMaker AI
Clarify](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-configure-processing-jobs.html)
- [Amazon SageMaker AI Clarify](https://aws.amazon.com/sagemaker/clarify/)
- [Responsible
AI Practices](https://aws.amazon.com/ai/responsible-ai/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlops02-bp06.html*

---
