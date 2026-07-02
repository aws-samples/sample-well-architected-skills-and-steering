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
