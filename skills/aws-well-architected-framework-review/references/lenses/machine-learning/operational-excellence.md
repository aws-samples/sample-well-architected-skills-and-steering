# Operational Excellence

**Pillar**: Operational Excellence  
**Questions**: 6

---

# MLOPS01 — Business goal identification

**Pillar**: Operational Excellence  
**Best Practices**: 3

---

# MLOPS01-BP01 Develop the right skills with accountability and empowerment

Artificial intelligence (AI) has many different and growing
branches, such as machine learning, deep learning, and computer
vision. Given the complexity and fast-growing nature of ML
technologies, plan to hire specialists with the understanding that
additional training will be needed as ML evolves. Keep teams
learning new skills, engaged, and motivated while encouraging
accountability and empowerment. Building ML models is a complex and
iterative process that can infuse bias or unfair predictions against
a certain entity. It's important to promote and enforce the ethical
use of AI across enterprises. AWS provides clear guidance to
customers for
[responsible
AI practices](https://aws.amazon.com/ai/responsible-ai/).

**Desired outcome:** You establish a
skilled, ethically responsible ML workforce that continuously
evolves with technology advancements. You create an environment
where your teams are empowered to innovate with AI/ML while
maintaining accountability for fair and unbiased AI solutions. Your
organization develops a strong foundation in ML concepts, end-to-end
lifecycle processes, and efficient use of AWS ML infrastructure and
tools, enabling you to maximize business value through ethical and
responsible AI implementation.

**Common anti-patterns:**

- Hiring ML specialists without a continuous learning plan.
- Focusing only on technical skills while ignoring ethical
considerations.
- Creating siloed ML teams without cross-functional collaboration.
- Assuming ML models are inherently unbiased and fair.

**Benefits of establishing this best
practice:**

- Increased innovation through skilled and empowered ML teams.
- Reduced risk of biased or unfair AI predictions.
- Improved ability to adapt to rapidly evolving ML technologies.
- Greater business value through responsible and ethical AI
implementation.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Building a successful ML workforce requires a comprehensive
approach that includes both technical and ethical skill
development. Organizations must invest in continuous learning
across various ML domains while also establishing clear
accountability frameworks for responsible AI. By developing these
capabilities together, you can maximize the benefits of ML while
minimizing potential risks.

Creating an environment that fosters innovation while maintaining
ethical standards is essential for sustainable ML success. This
includes establishing clear guidelines for model development,
testing for bias, and providing explainability of AI decisions.
Cross-functional teams that combine technical expertise with
domain knowledge and ethical considerations will deliver the most
robust ML solutions.

As ML technologies evolve rapidly, your organization must remain
adaptable and committed to ongoing skill development. This
includes staying current with AWS's latest ML services, tools, and
best practices while also keeping pace with advances in
responsible AI methodologies.

### Implementation steps

- **Develop comprehensive ML skills
training programs**. Create structured learning
paths for different roles within your ML teams. Provide
training on fundamental ML concepts and algorithms,
end-to-end ML lifecycle processes, and efficient use of ML
infrastructure with
[Amazon SageMaker AI](https://aws.amazon.com/sagemaker/). Include training on AI-assisted
development tools like
[Amazon Q Developer](https://aws.amazon.com/q/developer/) for code generation and productivity
enhancement. Incorporate specialized training in areas
aligned with your business needs, such as computer vision,
natural language processing (NLP), and reinforcement
learning. Utilize resources like
[AWS Skill Builder](https://aws.amazon.com/training/learn-about/), and
[Amazon Machine Learning University](https://www.amazon.science/tag/machine-learning-university-mlu)
- **Establish cross-functional ML
teams**. Form diverse teams with specialists from
multiple disciplines including data science, engineering,
ethics, legal, and domain experts. This multidisciplinary
approach provides a holistic perspective on ML
implementation and identifies potential issues early in the
development process. Encourage collaboration across teams to
share knowledge, best practices, and lessons learned from ML
initiatives.
- **Implement bias detection and
fairness protocols**. Use
[Amazon SageMaker AI Clarify](https://aws.amazon.com/sagemaker/clarify/) to detect and mitigate bias in your
datasets and model predictions. Establish guidelines for
evaluating models for fairness across different demographic
groups and protected attributes. Create checkpoints
throughout the ML lifecycle to assess and address potential
bias before models are deployed into production
environments.
- **Create an ML ethics
framework**. Develop clear guidelines and
principles for ethical AI use within your organization.
Establish an AI Ethics Board comprising representatives from
legal, ethics, IT, data science, and key business units.
Their responsibility should include creating policies for
responsible AI implementation, providing guidance on complex
ethical questions, and improving adherence to relevant
regulations and industry standards.
- **Foster accountability through
documentation and governance**. Implement
comprehensive documentation processes for each aspect of the
ML lifecycle, including data sources, model development
decisions, testing procedures, and deployment criteria.
Create clear ownership and accountability structures for ML
projects, with designated responsibilities for model
performance, fairness, and explainability. Use
[Amazon SageMaker AI Model Cards](https://docs.aws.amazon.com/sagemaker/latest/dg/model-cards.html) to document model details,
intended uses, limitations, and ethical considerations.
- **Empower continuous learning and
experimentation**. Create opportunities for teams
to expand their ML knowledge through immersion days,
hackathons, certification programs, and participation in the
broader ML community. Establish sandboxed environments using
[Amazon SageMaker AI Unified Studio](https://aws.amazon.com/sagemaker/unified-studio/) for integrated data and AI
workflows where teams can experiment with new ML techniques
and tools without risk to production systems.
- **Measure and improve ML
operations**. Implement metrics to evaluate the
effectiveness of your ML teams and processes, including
model performance, development efficiency, and ethics.
Regularly review these metrics to identify areas for
improvement and adjust your approach accordingly. Establish
feedback loops that incorporate insights from model
performance in production to continuously refine both
technical implementations and team capabilities.
- **Implement responsible generative AI
practices**. As you explore generative AI
capabilities, establish clear guardrails for using large
language models and other generative technologies. Use
[Amazon
Bedrock](https://aws.amazon.com/bedrock/) to access foundation models through a single
API with enterprise-grade security and compliance features.
Implement content filtering, safety measures, and human
review processes for generative AI outputs to align with
your organization's values and ethical standards.

## Resources

**Related documents:**

- [AWS ML Certification Paths](https://aws.amazon.com/certification/certified-machine-learning-specialty/)
- [AWS Ramp-Up Guides for Machine Learning](https://aws.amazon.com/training/ramp-up-guides/)
- [Create
a model card](https://docs.aws.amazon.com/sagemaker/latest/dg/model-cards-create.html)
- [Configure
a SageMaker AI Clarify Processing Job](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-processing-job-configure-parameters.html)
- [Responsible
use of Artificial Intelligence and Machine Learning](https://aws.amazon.com/ai/responsible-ai/)
- [What
is Amazon SageMaker AI?](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html)
- [Building
ML excellence: A practical training guide for Amazon SageMaker AI](https://aws.amazon.com/blogs/training-and-certification/building-ml-excellence-a-practical-training-guide-for-amazon-sagemaker-ai/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlops01-bp01.html*

---

# MLOPS01-BP02 Discuss and agree on the level of model explainability

Establish clear expectations with business stakeholders about the
level of model explainability needed for your machine learning use
case. Explainability provides an understanding of how and why a
model makes predictions, which builds trust, enables auditing, and
supports adherence to regulatory requirements.

**Desired outcome:** You establish
explainability requirements early in your machine learning project
lifecycle. You implement appropriate methods to provide the agreed
level of model explainability, building stakeholder trust and
improving your adherence to regulations. You use explainability
metrics in your evaluations and tradeoff analyses, verifying that
the model meets business needs while remaining interpretable.

**Common anti-patterns:**

- Treating explainability as an afterthought rather than a core
requirement.
- Choosing the most complex model without considering
explainability requirements.
- Failing to establish explainability metrics before model
development.
- Neglecting to communicate model decisions in terms
understandable to business stakeholders.

**Benefits of establishing this best
practice:**

- Increased stakeholder trust in model predictions.
- Better ability to troubleshoot and improve models.
- Enhanced ability to detect and address model biases.
- Improved model adoption by users who understand how decisions
are made.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

When implementing machine learning models, you need to balance
prediction accuracy with explainability. Highly complex models
like deep neural networks might provide superior predictive
performance but often function as an opaque system, making their
decision-making processes difficult to interpret. In contrast,
simpler models like decision trees offer greater transparency but
may sacrifice some accuracy.

The appropriate level of explainability depends on your specific
use case. In regulated industries like healthcare, finance, or
insurance, high explainability might be mandatory for
compliance-aligned reasons. For applications where human safety or
significant financial decisions are involved, understanding why a
model made a specific prediction becomes critical.

Work with your business stakeholders to understand their
explainability requirements before selecting modeling approaches.
Consider both technical and non-technical aspects of
explainability - technical stakeholders may need detailed feature
importance measures, while business users might need simple,
intuitive explanations of model decisions.

### Implementation steps

- **Understand business requirements for
explainability**. Meet with stakeholders to
determine how much transparency is needed based on use case,
industry regulations, and business objectives. In regulated
industries like healthcare and finance, regulations often
mandate that automated decisions be explainable to affected
individuals.
- **Evaluate model types based on
explainability needs**. Consider inherently
interpretable models (linear regression, decision trees) for
high explainability requirements, or more complex models
with following explanation techniques when higher accuracy
is the priority.
- **Set up SageMaker AI
Clarify**. Implement Amazon SageMaker AI Clarify to
create explainability reports and detect potential biases in
your datasets or models. Clarify includes enhanced bias
detection and new fairness metrics for more comprehensive
explainability analysis. SageMaker AI Clarify integrates
with SageMaker AI's model building, training, and deployment
capabilities.
- **Choose appropriate SHAP
baselines**. Shapley Additive exPlanations (SHAP)
values determine how each feature contributes to
predictions. Configure appropriate baselines in SageMaker AI
Clarify based on your data characteristics. You can choose
baselines with "low information content" (for
example, average values from the training dataset) or high
information content (representing a specific class of
interest).
- **Generate and interpret feature
attribution reports**. Use SageMaker AI Clarify to
generate feature attribution reports showing which features
most influenced model predictions and how they did so.
Review these reports with stakeholders to verify that they
provide the required level of understanding.
- **Create user-friendly explanation
interfaces**. Develop appropriate visualization
tools or explanation interfaces that present model insights
in ways that are meaningful to various stakeholders, from
data scientists to business users.
- **Implement continuous explainability
monitoring**. Set up ongoing monitoring of model
explanations to detect drift in feature importance or
unexpected behavior patterns over time.
- **Apply responsible AI principles to
generative models**. For generative AI
applications, implement additional explainability measures
such as prompt transparency, citation of sources, and
confidence scores to assist users in understanding how
outputs were generated.

## Resources

**Related documents:**

- [Model
Explainability](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-model-explainability.html)
- [Configure
a SageMaker AI Clarify Processing Job](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-processing-job-configure-parameters.html)
- [SHAP
Baselines for Explainability](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-feature-attribute-shap-baselines.html)
- [Explain
text classification model predictions using Amazon SageMaker AI
Clarify](https://aws.amazon.com/blogs/machine-learning/explain-text-classification-model-predictions-using-amazon-sagemaker-clarify/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlops01-bp02.html*

---

# MLOPS01-BP03 Monitor model adherence to business requirements

Machine learning models degrade over time due to changes in the real
world, such as *data drift* and *concept
drift*. If not monitored, these changes could lead to
models becoming inaccurate or even obsolete over time. It's
important to have a periodic monitoring process in place to make
sure that your ML models continue to comply to your business
requirements and that deviations are captured and acted upon
promptly.

**Desired outcome:** You implement a
robust model monitoring framework that continuously evaluates model
performance against your business requirements. This enables early
detection of model drift, keeping your ML models accurate and
effective over time. You establish clear metrics tied to business
outcomes and have automated processes to respond to detected drifts,
minimizing potential negative impacts.

**Common anti-patterns:**

- Implementing monitoring without clear metrics tied to business
requirements.
- Focusing only on technical metrics while ignoring business
impact metrics.
- Lacking a clear action plan for when drift is detected.
- Monitoring models infrequently or irregularly.
- Not establishing thresholds for acceptable levels of drift.

**Benefits of establishing this best
practice:**

- Early detection of model performance degradation.
- Maintained alignment between model outputs and business goals.
- Reduced risk of financial or operational impact from degraded
models.
- Increased stakeholder confidence in deployed ML systems.
- Improved model lifecycle management.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Model monitoring is a critical aspect of maintaining ML systems
that continue to deliver business value over time. As real-world
conditions evolve, your models can experience both data drift
(changes in the distribution of input data) and concept drift
(changes in the relationship between inputs and outputs). These
drifts can significantly impact model accuracy and reliability.

To effectively monitor model adherence to business requirements,
establish a comprehensive monitoring strategy that bridges
technical metrics with business outcomes. This involves defining
clear thresholds for acceptable performance, implementing
automated monitoring solutions, and creating response plans for
different drift scenarios.

Amazon SageMaker AI Model Monitor provides capabilities to
automatically monitor models in production and detect deviations
from the baseline. By using these capabilities, you can
proactively address potential issues before they impact your
business operations.

### Implementation steps

- **Define relevant metrics aligned with
business objectives.** Begin by clearly
establishing the metrics that are most relevant to your
business outcomes. Include both technical metrics (like
accuracy, precision, and recall) and business metrics (like
revenue impact and customer satisfaction). Make sure these
metrics directly relate to the business requirements the
model is expected to fulfill.
- **Establish baseline performance and
thresholds.** Create a performance baseline using
your validation dataset. Using Amazon SageMaker AI Model
Monitor, you can automatically generate statistics and
constraints from your baseline data that define normal
behavior. Set appropriate thresholds that will alert when
model performance deviates beyond acceptable limits.
- **Implement automated data quality
monitoring.** Configure SageMaker AI Model Monitor to
regularly check the quality of input data against the
baseline. This can detect data drift that could affect model
performance. Monitor features for statistical changes in
distributions, missing values, or other quality issues.
- **Configure model quality
monitoring.** Set up monitoring for model outputs
and quality metrics. SageMaker AI Model Monitor can track
prediction distributions and performance metrics over time,
alerting you when they deviate from expected patterns.
- **Set up bias drift
detection.** Use SageMaker AI Clarify integration with
Model Monitor to detect changes in bias metrics over time.
This keeps your model fair and unbiased as production data
evolves.
- **Create visualization
dashboards.** Implement dashboards using Amazon CloudWatch, Amazon Managed Grafana, or use
[Quick with GenBI capabilities](https://aws.amazon.com/quicksight/generative-bi/) to automatically
generate monitoring dashboards. These dashboards should
present both technical and business metrics in an
understandable format for stakeholders.
- **Develop response protocols for drift
detection.** Create clear action plans for
different types and severities of detected drift. These
might include automated retraining pipelines, manual
reviews, or temporary fallback strategies depending on the
scenario.
- **Implement alert
mechanisms.** Configure alerts using Amazon CloudWatch to notify appropriate team members when metrics
exceed thresholds. Check that your alerts provide actionable
information about the nature and potential impact of the
drift.
- **Establish regular review
processes.** Schedule periodic reviews of
monitoring results even when no alerts go off. This can
identify gradual drifts that might not immediately alert but
could impact performance over time.
- **Document monitoring systems and
processes.** Maintain comprehensive documentation
of your monitoring setup, including metrics definitions,
thresholds, alert configurations, and response protocols to
preserve organizational knowledge.
- **Leverage generative AI for root
cause analysis.** Use generative AI capabilities to
analyze complex patterns in your monitoring data and provide
human-readable explanations of potential drift causes. Tools
like
[Amazon
Bedrock Knowledge Bases](https://aws.amazon.com/bedrock/knowledge-bases/) can interpret changes in
model behavior and suggest remediation approaches.

## Resources

**Related documents:**

- [Data
and model quality monitoring with Amazon SageMaker AI Model
Monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html)
- [Schema
for Violations (constraint_violations.json file)](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-interpreting-violations.html)
- [Amazon SageMaker AI metrics in Amazon CloudWatch](https://docs.aws.amazon.com/sagemaker/latest/dg/monitoring-cloudwatch.html)
- [What
is Amazon CloudWatch?](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html)
- [Amazon SageMaker AI Clarify](https://aws.amazon.com/sagemaker/clarify/)
- [Amazon SageMaker AI ML Governance](https://aws.amazon.com/sagemaker/ml-governance/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlops01-bp03.html*

---

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

# MLOPS03 — Data processing

**Pillar**: Operational Excellence  
**Best Practices**: 2

---

# MLOPS03-BP01 Profile data to improve quality

Data profiling is essential for understanding data characteristics
such as distribution, descriptive statistics, data types, and
patterns. By systematically reviewing source data for content and
quality, you can filter out or correct problematic data, leading to
significant quality improvements in your machine learning workflows.

**Desired outcome:** You gain
comprehensive insights into your data's characteristics, enabling
you to identify and remediate quality issues before they impact your
machine learning models. Through systematic profiling, you establish
a robust data preprocessing pipeline that provides high-quality,
consistent data flows to your ML models, resulting in more accurate
predictions and better business outcomes.

**Common anti-patterns:**

- Skipping data profiling and moving directly to model training.
- Manually reviewing data without automated profiling tools.
- Performing one-time data quality checks without continuous
monitoring.
- Ignoring data distribution shifts between training and inference
data.
- Failing to document data quality issues and their resolutions.

**Benefits of establishing this best
practice:**

- Improved model performance through higher quality training data.
- Earlier detection of data anomalies and inconsistencies.
- Enhanced understanding of data characteristics and limitations.
- Reduced time spent debugging model issues caused by data
problems.
- More transparent and reproducible machine learning workflows.
- Increased stakeholder confidence in model outputs.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Data profiling is a critical step in the machine learning
workflow. By thoroughly examining your data before model training,
you gain valuable insights that improve data quality and
ultimately lead to better model performance. Data profiling
involves analyzing the statistical properties, distributions, and
patterns within your dataset to identify anomalies, missing
values, outliers, and other quality issues.

Effective data profiling requires both automated tools and human
judgment. While tools can quickly generate statistical summaries
and visualizations, subject matter experts should interpret these
findings to determine appropriate actions for data cleaning and
transformation. For instance, you might discover that a numerical
feature has an unexpected distribution that requires
normalization, or that categorical variables contain inconsistent
values requiring standardization.

Consider a retail company building a customer churn prediction
model. Through data profiling, they discover that 15% of customer
records have missing age values, 5% have impossibly high
transaction amounts, and several categorical fields contain
inconsistent formatting. By addressing these issues early, they
can significantly improve their model's performance.

### Implementation steps

- **Set up Amazon SageMaker AI Unified
Studio for visual data review**. Use
[Amazon SageMaker AI Unified Studio](https://aws.amazon.com/sagemaker/unified-studio/) with enhanced collaborative
features and team sharing capabilities to visually review
data characteristics and remediate data-quality problems
directly in your integrated environment. The unified
solution provides improved debugging and monitoring
capabilities for data processing workflows, automatically
generating charts to identify data quality issues and
suggesting transformations to fix common problems.
- **Implement Amazon SageMaker AI Data
Wrangler for comprehensive data preparation**.
Import, prepare, transform, visualize, and analyze data with
[SageMaker AI Data Wrangler](https://aws.amazon.com/sagemaker/data-wrangler/) with
[Q
integration for interactive analysis](https://docs.aws.amazon.com/sagemaker/latest/dg/data-wrangler-q-integration.html). You can
integrate Data Wrangler into your ML workflows to simplify
and streamline data pre-processing and feature engineering
with little to no coding. Import data from
[Amazon S3](https://aws.amazon.com/s3/),
[Amazon Redshift](https://aws.amazon.com/redshift/), or other data sources, and then query the
data using
[Amazon Athena](https://aws.amazon.com/athena/). Use Data Wrangler's built-in and custom data
transformations and analysis features, including feature
target leakage detection and quick modeling, to create
sophisticated machine learning data preparation workflows.
- **Build an automatic data profile and
reporting system**. Use
[AWS Glue Crawler](https://docs.aws.amazon.com/glue/latest/dg/add-crawler.html) to crawl your data sources and
automatically create a data schema. The crawler detects the
schema of your data and registers tables in the
[AWSAWS Glue Data Catalog](https://docs.aws.amazon.com/glue/latest/dg/populate-data-catalog.html), providing a comprehensive listing
of tables and schemas. Use
[Amazon Athena](https://aws.amazon.com/athena/) for serverless SQL querying to constantly
profile your data, and create
[Quick](https://aws.amazon.com/quicksight/) dashboards for data visualization and
monitoring.
- **Create a baseline dataset with
SageMaker AI Model Monitor**. The training dataset
used to train your model typically serves as a good baseline
dataset. Verify that the training dataset schema and the
inference dataset schema exactly match (the number and order
of the features). With
[SageMaker AI Model Monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-create-baseline.html), you can automatically detect
concept drift in deployed models by comparing production
data against this baseline.
- **Implement continuous data quality
monitoring**. Set up automated checks that
continuously monitor data quality metrics like completeness,
uniqueness, consistency, and validity. Configure alerts to
notify relevant stakeholders when data quality issues arise,
enabling prompt intervention and resolution. Use
[Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) to create dashboards and set up alerts for
key data quality metrics.
- **Document data profiling insights and
transformations**. Maintain comprehensive
documentation of data profiling findings, quality issues
discovered, and the transformations applied to address them.
This documentation promotes transparency, facilitates
knowledge sharing across teams, and supports regulatory
adherence in regulated industries.
- **Use generative AI for enhanced data
profiling**. Use large language models in
[Amazon
Bedrock](https://aws.amazon.com/bedrock/knowledge-bases/) or
[Amazon
Nova](https://aws.amazon.com/ai/generative-ai/nova/) to automatically extract and enrich metadata,
identify patterns in your data, and generate natural
language summaries of data quality issues. Generative AI can
analyze unstructured data fields and provide insights that
traditional data profiling tools might miss, though you
should validate AI-generated suggestions before
implementation.

## Resources

**Related documents:**

- [Prepare
ML Data with Amazon SageMaker AI Data Wrangler](https://docs.aws.amazon.com/sagemaker/latest/dg/data-wrangler.html)
- [Get
Started with Data Wrangler](https://docs.aws.amazon.com/sagemaker/latest/dg/data-wrangler-getting-started.html)
- [Data
quality](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-data-quality.html)
- [Create
a Baseline](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-create-baseline.html)
- [AWS Glue Data Quality](https://docs.aws.amazon.com/glue/latest/dg/glue-data-quality.html)
- [Data
discovery and cataloging in AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/catalog-and-crawler.html)
- [Amazon SageMaker AI notebooks](https://aws.amazon.com/sagemaker/notebooks/)
- [What
is Amazon Athena?](https://docs.aws.amazon.com/athena/latest/ug/what-is.html)
- [What
is Amazon Quick Suite?](https://docs.aws.amazon.com/quicksight/latest/user/welcome.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlops03-bp01.html*

---

# MLOPS03-BP02 Create tracking and version control mechanisms

Machine learning model development requires robust tracking and
version control mechanisms due to its iterative and exploratory
nature. By implementing proper tracking systems, you can maintain
visibility of your experiments, data processing techniques, and
model versions while enabling reproducibility and collaboration.

**Desired outcome:** You have
comprehensive tracking of ML model development with experiment
tracking capabilities, version-controlled data processing code, and
a model registry that enables you to identify the best performing
models. Your development processes are reproducible, collaborative,
and automated with CI/CD pipelines for model deployment.

**Common anti-patterns:**

- Manually tracking experiments in spreadsheets or documents.
- Not documenting data processing steps or model configurations.
- Keeping models and datasets in local environments without
version control.
- Starting new experiments from scratch instead of building on
previous work.

**Benefits of establishing this best
practice:**

- Enhanced reproducibility of experiments and model training.
- Improved collaboration among data science teams.
- Better visibility into the performance of different model
iterations.
- Faster identification of the best performing models.
- Ability to roll back to previous model versions if needed.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Machine learning development involves experimenting with multiple
combinations of data, algorithms, and parameters while observing
how incremental changes impact model accuracy. Without proper
tracking and version control, you risk losing valuable insights
and the ability to reproduce successful experiments.

To address these challenges, you need a systematic approach to
track experiments, version control your code and data processing
techniques, and manage model deployment. AWS SageMaker AI provides
integrated tools for experiment tracking, version control, and
model registry that can streamline your machine learning
operations.

By implementing proper tracking and versioning mechanisms, you can
document your model development journey, track performance metrics
across experiments, and reliability reproduce and deploy your
models. This creates a foundation for continuous improvement of
your machine learning applications.

### Implementation steps

- **Track your ML experiments with
SageMaker AI Experiments**. Use Amazon SageMaker AI
Experiments to you create, manage, analyze, and compare your
machine learning experiments. SageMaker AI Experiments
automatically tracks inputs, parameters, configurations, and
results of your iterations as runs. You can assign, group,
and organize these runs into experiments. SageMaker AI
Experiments integrates with Amazon SageMaker AI Studio,
providing a visual interface to browse active and past
experiments, compare runs on key performance metrics, and
identify the best-performing models.
- **Process data with SageMaker AI
Processing**. For analyzing data, documenting
processing, and evaluating ML models, use
[Amazon SageMaker AI Processing](https://docs.aws.amazon.com/sagemaker/latest/dg/processing-job.html). This capability can be used for
feature engineering, data validation, model evaluation, and
model interpretation. SageMaker AI Processing provides a
standardized way to run your data processing workloads,
fostering consistency and reproducibility.
- **Use SageMaker AI Unified Studio for
enhanced collaboration**. Use
[Amazon SageMaker AI Unified Studio](https://aws.amazon.com/sagemaker/unified-studio/) with enhanced collaborative
features and team sharing capabilities for integrated data
and AI workflows. The unified solution provides improved
debugging and monitoring capabilities, VS Code server
integration, and enhanced project sharing. This approach
keeps your data processing code and documentation accessible
while facilitating better collaboration and version tracking
across teams.
- **Use SageMaker AI Model
Registry**. Catalog, manage, and deploy models
using SageMaker AI Model Registry. Create a model group and,
for each run of your ML pipeline, create a model version
that you register in the model group. The Model Registry
provides a centralized repository for model versions, making
it more straightforward to track model lineage, compare
model performance, and promote models to production.
- **Implement CI/CD for model
deployment**. Automate your model deployment
process using CI/CD pipelines for consistent and reliable
deployments. SageMaker AI Pipelines can be used to create
end-to-end workflows that include model building,
evaluation, and deployment steps. Implement CI/CD for model
deployment to thoroughly test your models before they are
deployed to production, reducing the risk of
deployment-related issues.
- **Integrate data version
control**. Use tools like Data Version Control
(DVC) in conjunction with SageMaker AI Experiments to track
both your model code and the datasets used for training and
evaluation. With these tools, you can completely reproduce
your machine learning experiments.
- **Create model cards for
documentation**. For each model version in your
registry, create comprehensive
[SageMaker AI
Model Cards](https://docs.aws.amazon.com/sagemaker/latest/dg/model-cards.html) with enhanced documentation and
governance capabilities that document the model's purpose,
training data, performance metrics, limitations, and usage
guidelines. This documentation helps users understand when
and how to use specific model versions and supports improved
model governance.

## Resources

**Related documents:**

- [Amazon SageMaker AI Experiments in Studio Classic](https://docs.aws.amazon.com/sagemaker/latest/dg/experiments.html)
- [Accelerate
generative AI development using managed MLflow on Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/mlflow.html)
- [Git
repositories with SageMaker AI Notebook Instances](https://docs.aws.amazon.com/sagemaker/latest/dg/nbi-git-repo.html)
- [MLOps
Automation With SageMaker AI Projects](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-projects.html)
- [Amazon SageMaker AI Model Cards](https://docs.aws.amazon.com/sagemaker/latest/dg/model-cards.html)
- [Model
Registration Deployment with Model Registry](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry.html)
- [Data
transformation workloads with SageMaker AI Processing](https://docs.aws.amazon.com/sagemaker/latest/dg/processing-job.html)
- [Pipelines](https://docs.aws.amazon.com/sagemaker/latest/dg/pipelines.html)

**Related examples:**

- [SageMaker AI
Experiment Examples](https://github.com/aws/amazon-sagemaker-examples/tree/main/sagemaker-experiments)
- [SageMaker AI
Model Registry Examples](https://github.com/aws/amazon-sagemaker-examples/tree/main/sagemaker-pipelines)
- [Amazon SageMaker AI processing](https://sagemaker.readthedocs.io/en/stable/amazon_sagemaker_processing.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlops03-bp02.html*

---

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

# MLOPS05 — Deployment

**Pillar**: Operational Excellence  
**Best Practices**: 1

---

# MLOPS05-BP01 Establish deployment environment metrics

Establish comprehensive monitoring of machine learning operations to
gain visibility into your deployed ML environments. By measuring
metrics such as memory, CPU/GPU usage, disk utilization, endpoint
invocations, and latency, you can provide optimal performance and
improve the reliability of your ML systems.

**Desired outcome:** You gain
real-time visibility into your ML deployment environments through
systematic collection and analysis of performance metrics. You
establish robust monitoring dashboards, alerting systems, and
automated responses to potential issues. This enables you to
proactively address performance bottlenecks, optimize resource
utilization, and maintain reliable ML services while managing costs
effectively.

**Common anti-patterns:**

- Implementing monitoring only after experiencing production
issues.
- Focusing only on basic system metrics while ignoring ML-specific
performance indicators.
- Creating monitoring dashboards without establishing
corresponding alerts.
- Setting static thresholds that don't account for typical usage
patterns.
- Collecting metrics without regular review or actionable response
plans.

**Benefits of establishing this best
practice:**

- Early detection of performance issues before they impact end
users.
- Improved resource optimization and cost efficiency.
- Enhanced ability to scale ML services based on actual usage
patterns.
- Faster troubleshooting and reduced mean time to resolution.
- Data-driven capacity planning and infrastructure decisions.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Establishing effective deployment environment metrics requires a
systematic approach to monitoring both infrastructure and
application-specific ML metrics. You need to focus on both
system-level metrics like CPU, memory, and disk usage, as well as
ML-specific metrics such as inference latency, throughput, and
model accuracy. By using AWS services like Amazon CloudWatch, you
can centralize your monitoring approach and gain comprehensive
visibility into your ML operations.

Start by identifying the key performance indicators that matter
most for your specific ML workloads. For inference endpoints,
these typically include latency, throughput, and resource
utilization. For batch processing jobs, focus on processing time,
error rates, and resource efficiency. With these KPIs established,
you can implement automated monitoring and alerting to quickly
identify when your systems deviate from expected performance.

Regular review of your metrics can identify trends and potential
areas for optimization. For example, you might discover that
certain models require more memory than originally allocated, or
that specific types of inference requests consistently take longer
to process. This information guides your infrastructure decisions
and prioritizes optimization efforts.

### Implementation steps

- **Record performance-related
metrics.** Use a monitoring and observability
service like Amazon CloudWatch to record performance-related
metrics. These metrics can include database transactions,
slow queries, I/O latency, HTTP request throughput, service
latency, and other key data. For SageMaker AI endpoints,
collect metrics such as CPUUtilization, MemoryUtilization,
DiskUtilization, and model-specific metrics like
ModelLatency and InvocationsPerInstance.
- **Analyze metrics when events or
incidents occur.** Use monitoring dashboards and
reports to understand and diagnose the impact of an event or
incident. Amazon CloudWatch Dashboards provide insight into
what portions of the workload are not performing as
expected. Correlate metrics, logs, and traces to quickly
identify root causes when issues arise.
- **Establish key performance indicators
(KPIs) to measure workload performance.** Identify
the KPIs that indicate whether the workload is performing as
intended. An API-based ML endpoint might use overall
response latency as an indication of overall performance,
while a batch processing job might track throughput metrics.
For generative AI applications, monitor additional metrics
like token usage, cost per request, prompt engineering
effectiveness, and use
[SageMaker AI
Training Plans](https://aws.amazon.com/sagemaker/pricing/) for cost optimization of large-scale
AI training workloads.
- **Use monitoring to generate
alarm-based notifications.** Monitor metrics for
the defined KPIs and generate alarms automatically when the
measurements are outside expected boundaries. Configure
Amazon CloudWatch Alarms to send notifications using Amazon SNS when thresholds are breached, which provides for timely
responses to potential issues.
- **Review metrics at regular
intervals.** As routine maintenance, or in response
to events or incidents, review what metrics are collected
and identify the metrics that were key in addressing issues.
Identify additional metrics that can identify, address, or
avoid issues. Schedule periodic reviews to keep your
monitoring strategy effective as your ML applications
evolve.
- **Monitor and alarm
proactively.** Use KPIs, combined with monitoring
and alerting systems, to proactively address
performance-related issues. Configure CloudWatch to initiate
automated actions to remediate issues where possible.
Escalate the alarm to those able to respond if an automated
response is not possible. Use anomaly detection to predict
expected KPI values, and generate alerts and automatically
halt or roll back deployments if KPIs are outside of the
expected values.
- **Use Amazon CloudWatch for
comprehensive monitoring.** Use Amazon CloudWatch
metrics for SageMaker AI endpoints to determine the memory,
CPU usage, and disk utilization. Set up CloudWatch
Dashboards to visualize the environment metrics and
establish CloudWatch alarms to initiate a notification
through Amazon SNS (email, SMS, or webHook) to notify on
events occurring in the runtime environment. For model
performance monitoring, implement Amazon SageMaker AI Model
Monitor to detect data drift and quality issues.
- **Use Amazon EventBridge for automated
workflows.** Define an automated workflow using
Amazon EventBridge to respond automatically to events. These
events can include training job status changes, endpoint
status changes, and increasing the compute environment
capacity after it crosses a defined threshold (such as CPU
or disk utilization). Create event rules that run Lambda
functions to scale resources, update configurations, or
notify specific teams based on the event type.
- **Use AWS Application Cost Profiler
for cost allocation.** Implement AWS Application Cost Profiler to report the cost per tenant (model or user).
This assists you in tracking resource usage at a granular
level and enables accurate cost attribution across different
ML models, teams, or business units. Use
[SageMaker AI
Training Plans](https://aws.amazon.com/sagemaker/pricing/) for compute reservation and better
resource planning of high-demand GPU resources. Use these
insights to optimize resource allocation and identify
opportunities for cost savings.
- **Implement SageMaker AI Model Monitor
for data drift detection.** Configure SageMaker AI
Model Monitor to continuously monitor the quality of your
machine learning models in production. Set up automated
quality checks to detect data drift, model drift, and bias
drift in your production workloads. This enables you to
maintain high quality standards and take corrective actions
when models start to deviate from expected behavior.
- **Use AWS X-Ray for distributed
tracing.** Implement AWS X-Ray to trace requests
through your ML application components. This provides
visibility into request flows, latency bottlenecks, and
error points in distributed systems. X-Ray provides an
understanding of the dependencies between components so you
can optimize end-to-end performance of your ML applications.
- **Implement Amazon SageMaker AI Clarify
for bias monitoring.** Use SageMaker AI Clarify to
detect bias in your deployed models. Set up regular
monitoring jobs to track bias metrics and alert when they
exceed acceptable thresholds so that your ML systems
continue to make fair and unbiased predictions in
production.

## Resources

**Related documents:**

- [Data
and model quality monitoring with Amazon SageMaker AI Model
Monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html)
- [Metrics
in Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/working_with_metrics.html)
- [Using
Amzon CloudWatch dashboards](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html)
- [DevOps
and AWS](https://aws.amazon.com/devops/?ref=wellarchitected-wp)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlops05-bp01.html*

---

# MLOPS06 — Monitoring

**Pillar**: Operational Excellence  
**Best Practices**: 2

---

# MLOPS06-BP01 Synchronize architecture and configuration, and check for skew across environments

Synchronize your systems and configurations across development and
deployment phases for consistent machine learning model inference
results. By maintaining identical environments, you can avoid
discrepancies that arise from architectural differences, leading to
more reliable and predictable model performance.

**Desired outcome:** You have
established a systematic approach to foster architectural and
configuration consistency across development, staging, and
production environments for machine learning models. This includes
automated infrastructure deployment, continuous model quality
monitoring, and proactive detection of environmental skew. Your
machine learning systems deliver the same range of accuracy
regardless of which environment they run in, and you can quickly
identify and address deviations.

**Common anti-patterns:**

- Manually configuring each environment, leading to
inconsistencies.
- Neglecting to validate model performance across different
environments.
- Assuming model behavior will be identical across environments
without verification.
- Using different hardware specifications or software versions
between environments.
- Making changes only when needed to production environments
without documenting or replicating them in other environments.

**Benefits of establishing this best
practice:**

- Consistent model performance across environments.
- Reduced debugging time for environment-specific issues.
- Improved reliability of machine learning applications.
- Straightforward identification of the root causes of performance
deviations.
- Streamlined promotion process from development to production.
- Enhanced confidence in deployed models.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Synchronizing your machine learning environments is critical for
checking that a model trained in one environment behaves the same
way when deployed in another. Differences in system architectures,
software dependencies, or configuration settings can cause
unexpected variations in model performance, leading to inaccurate
predictions or even system failures.

By treating your infrastructure as code and implementing automated
monitoring, you can maintain consistency across environments and
quickly detect deviations. This approach allows you to focus on
improving your models rather than debugging environment-specific
issues. It also provides a reliable foundation for continuous
delivery of machine learning solutions.

Environmental skew can occur in various ways, such as through
differences in hardware capabilities, software versions, or system
configurations. For example, a model trained on a development
environment with specific CPU architecture might behave
differently when deployed to a production environment with
different specifications. Similarly, differences in underlying
libraries or dependencies can lead to subtle variations in model
behavior.

Regular validation of model performance across environments should
be part of your standard promotion process. This includes
comparing not only the accuracy metrics but also the distribution
of predictions and the model's behavior for edge cases.

### Implementation steps

- **Define infrastructure as code using
AWS CloudFormation**. Create CloudFormation
templates that define resources, configurations, and
dependencies for your machine learning environments. With
this strategy, each environment is provisioned consistently
and can be recreated identically when needed. Include
compute resources, networking configurations, security
settings, and machine learning-specific components.
- **Implement version control for
infrastructure templates**. Store your
CloudFormation templates in a version control system like
AWS CodeCommit or GitHub. This allows you to track changes
over time, roll back to previous configurations if needed,
and verify that your environments are using the same version
of the infrastructure definition.
- **Set up CI/CD pipelines for
infrastructure deployment**. Use AWS CodePipeline
or AWS CodeBuild to automate the deployment of your
infrastructure changes across environments. This reduces
manual intervention and the potential for human error when
updating environments.
- **Configure Amazon SageMaker AI Model
Monitor for continuous quality evaluation**. Set up
Model Monitor to automatically track the quality of your
models in production and compare the results with the
baseline established during training. This can identify when
model performance starts to drift due to environmental
factors or data changes.
- **Implement data quality
monitoring**. Use SageMaker AI Model Monitor's data
quality monitoring capability to detect changes in the
statistical properties of your input data across
environments. This capability provides similar input
distributions to your models regardless of environment.
- **Set up model quality
monitoring**. Configure SageMaker AI Model Monitor to
track model quality metrics such as accuracy, precision, and
recall over time. Compare these metrics between your
development, staging, and production environments to detect
inconsistencies.
- **Enable bias drift
monitoring**. Use SageMaker AI Model Monitor's bias
drift monitoring to detect if your models exhibit different
biases in different environments, which could indicate
environment-specific issues.
- **Configure alerts for
deviations**. Set up Amazon CloudWatch alarms to
notify you when SageMaker AI Model Monitor detects significant
deviations in model performance or data characteristics
across environments. This allows for proactive intervention
before small issues become major problems.
- **Establish a promotion
checklist**. Create a formal checklist that
includes verifying model performance consistency across
environments before promoting a model to the next stage.
Document the acceptable thresholds for performance
differences between environments.
- **Implement regular cross-environment
validation**. Schedule periodic validation of model
performance across your environments, even when no changes
are being made. Use this validation to catch gradual drift
that might occur due to external factors.
- **Create environment comparison
dashboards**. Use
[Quick with GenBI capabilities](https://aws.amazon.com/quicksight/generative-bi/) to automatically
generate visualizations and dashboards for model performance
metrics across different environments, making it more
straightforward to spot discrepancies and track trends over
time.
- **Utilize foundation models for
anomaly detection**. Implement
[Amazon
Bedrock](https://aws.amazon.com/bedrock/knowledge-bases/) or
[SageMaker AI
JumpStart](https://aws.amazon.com/sagemaker/jumpstart/) with expanded library of foundation models
to analyze performance patterns and identify anomalous
behavior that might indicate environmental inconsistencies,
especially for complex ML systems where traditional
monitoring might miss subtle differences.

## Resources

**Related documents:**

- [Data
and model quality monitoring with Amazon SageMaker AI Model
Monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html)
- [What
is AWS CloudFormation?](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html)
- [What
is AWS Config?](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html)
- [Detect
unmanaged configuration changes to stacks and resources with
drift detection](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html)
- [AWS Systems Manager Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html)
- [Amazon SageMaker AI best practices](https://docs.aws.amazon.com/sagemaker/latest/dg/best-practices.html)

**Related examples:**

- [Introduction
to Amazon SageMaker AI Model Monitor](https://sagemaker-examples.readthedocs.io/en/latest/sagemaker_model_monitor/introduction/SageMaker AI-ModelMonitoring.html)
- [Model
Monitor Visualization](https://sagemaker-examples.readthedocs.io/en/latest/sagemaker_model_monitor/visualization/SageMaker AI-Model-Monitor-Visualize.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlops06-bp01.html*

---

# MLOPS06-BP02 Enable model observability and tracking

Establish model monitoring mechanisms to identify and proactively
avoid inference issues. ML models can degrade in performance over
time due to drifts. Monitor metrics that are attributed to your
model's performance. For real time inference endpoints, measure the
operational health of the underlying compute resources hosting the
endpoint and the health of endpoint responses. Establish lineage to
trace hosted models back to versioned inputs and model artifacts for
analysis.

**Desired outcome:** You can
continuously monitor your machine learning models in production to
detect and avoid performance degradation over time. You have
mechanisms in place to track model lineage, identify various types
of drift, and receive alerts when models deviate from expected
behavior. Your monitoring solution provides clear visibility into
both the technical health of model endpoints and the business
performance of the models themselves, enabling you to maintain
high-quality predictions and make informed decisions about model
updates.

**Common anti-patterns:**

- Deploying models without monitoring capabilities.
- Failing to establish model lineage tracking for audit and
governance.
- Not monitoring for data drift or concept drift in production
models.
- Ignoring model bias and fairness considerations after
deployment.
- Lacking documentation of model information and performance
metrics.

**Benefits of establishing this best
practice:**

- Early detection of model performance degradation.
- Improved model governance and adherence through comprehensive
documentation.
- Enhanced ability to explain model predictions and address bias
concerns.
- Reduced operational risk through proactive monitoring of model
health.
- Streamlined model updates and improvements based on real-world
performance data.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Model observability is critical for maintaining the reliability,
fairness, and performance of machine learning systems in
production. Without proper monitoring mechanisms, ML models can
silently degrade over time as the data they process begins to
differ from the data they were trained on, a phenomenon known as
drift.

You need to implement comprehensive monitoring across several
dimensions: data quality to check that inputs remain consistent
with training data, model quality to track performance metrics,
bias detection to verify fairness, and explainability to
understand model decisions. Additionally, model lineage tracking
can trace issues back to specific model versions, training
datasets, and hyperparameters.

Amazon SageMaker AI provides integrated tools that make implementing
these monitoring capabilities straightforward. SageMaker AI Model
Monitor can automatically detect deviations in your model's data
and performance characteristics, while SageMaker AI Clarify
identifies bias and explains predictions. By setting up proper
alerts, you can be notified when issues arise and take corrective
action before they impact your business.

Documentation is equally important for model governance. SageMaker AI
Model Cards provide a centralized location to store important
model information, including performance metrics, intended use
cases, and potential limitations.

### Implementation steps

- **Set up Amazon SageMaker AI Model
Monitor**. Configure
[Amazon SageMaker AI Model Monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html) to automatically monitor the
quality of your ML models in production. Create baseline
statistics and constraints during model training, then
monitor for deviations in production data. Set up the
following types of monitoring:

Data quality monitoring to detect changes in data
distributions
- Model quality monitoring to track accuracy and other
performance metrics
- Bias drift monitoring to detect changes in model
fairness
- Feature attribution drift monitoring to track changes in
feature importance

- **Integrate with Amazon CloudWatch**. SageMaker AI Model Monitor automatically
sends metrics to
[Amazon CloudWatch](https://aws.amazon.com/cloudwatch/), allowing you to track usage statistics
for your ML models. Set up CloudWatch dashboards to
visualize key metrics and create alarms that go off when
metrics exceed predefined thresholds. Configure
notifications through Amazon SNS to alert relevant teams
when issues are detected.
- **Implement SageMaker AI Model
Dashboard**. Use the
[SageMaker AI
Model Dashboard](https://docs.aws.amazon.com/sagemaker/latest/dg/model-dashboard.html) to gain a centralized view of your
models. From the SageMaker AI console, you can search, view,
and explore your models in one place. Set up monitors to
track the performance of models deployed on real-time
inference endpoints and identify models that violate
thresholds for data quality, model quality, bias, and
explainability.
- **Enable bias detection with SageMaker AI
Clarify**. Deploy
[SageMaker AI
Clarify](https://aws.amazon.com/sagemaker/clarify/) to identify various types of bias that can
emerge during model training or when the model is in
production. Configure both pre-training and post-training
bias metrics to understand how your model's predictions
affect different segments of your user base. Use Clarify's
monitoring capabilities to detect bias drift in production
models.
- **Implement model
explainability**. Configure SageMaker AI Clarify's
feature attribution capabilities to explain how your models
make predictions. This builds trust with stakeholders and
can identify potential issues with model logic. Set up
monitoring to detect when feature attribution patterns drift
from baseline, which could indicate underlying problems with
the model.
- **Establish ML lineage
tracking**. Implement
[SageMaker AI
ML Lineage Tracking](https://sagemaker.readthedocs.io/en/v2.77.0/workflows/lineage/) to create and store information
about each step in your machine learning workflow, from data
preparation to model deployment. This creates a running
history of your ML experiments and establishes model
governance by tracking model lineage artifacts for auditing
and adherence verification.
- **Create Model Cards for
documentation**. Use
[Amazon SageMaker AI Model Cards](https://docs.aws.amazon.com/sagemaker/latest/dg/model-cards.html) with enhanced documentation and
governance capabilities to document critical information
about your models in a single location. Include business
requirements, key decisions, observations during
development, performance goals, risk ratings, and evaluation
results. This streamlines documentation throughout a model's
lifecycle and supports approval workflows, registration, and
audits.
- **Implement shadow testing for model
validation**. Before deploying new model versions
to production, use
[Amazon SageMaker AI Shadow Testing](https://docs.aws.amazon.com/sagemaker/latest/dg/shadow-tests.html) to compare the performance
of new models against production models using real-world
inference request data. Configure SageMaker AI to route copies
of production inference requests to the new model variant
and generate dashboards displaying performance differences
across key metrics in real-time.

## Resources

**Related documents:**

- [Data
and model quality monitoring with Amazon SageMaker AI Model
Monitor](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html)
- [Amazon SageMaker AI Model Dashboard](https://docs.aws.amazon.com/sagemaker/latest/dg/model-dashboard.html)
- [Shadow
tests](https://docs.aws.amazon.com/sagemaker/latest/dg/shadow-tests.html)
- [Lineage
Tracking Entities](https://docs.aws.amazon.com/sagemaker/latest/dg/lineage-tracking-entities.html)
- [Using
CloudWatch outlier detection](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.html)
- [Monitoring
Amazon ML with Amazon CloudWatch Metrics](https://docs.aws.amazon.com/machine-learning/latest/dg/cw-doc.html)
- [New
for Amazon SageMaker AI – Perform Shadow Tests to Compare
Inference Performance Between ML Model Variants](https://aws.amazon.com/blogs/aws/new-for-amazon-sagemaker-perform-shadow-tests-to-compare-inference-performance-between-ml-model-variants/)
- [Integrate
Amazon SageMaker AI Model Cards with the model registr](https://aws.amazon.com/blogs/machine-learning/integrate-amazon-sagemaker-model-cards-with-the-model-registry/)
- [Improve
governance of your machine learning models with Amazon SageMaker AI](https://aws.amazon.com/blogs/machine-learning/improve-governance-of-your-machine-learning-models-with-amazon-sagemaker/)

**Related examples:**

- [Monitoring
bias drift and feature attribution drift with Amazon SageMaker AI
Clarify](https://sagemaker-examples.readthedocs.io/en/latest/sagemaker_model_monitor/fairness_and_explainability/SageMaker AI-Model-Monitor-Fairness-and-Explainability.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlops06-bp02.html*

---

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
