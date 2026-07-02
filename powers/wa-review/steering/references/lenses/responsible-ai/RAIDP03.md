# RAIDP03 — Dataset issues

**Best Practices**: 5

---

# RAIDP03-BP01 Address data that may be unsafe or inappropriate for your use case

To perpetuate dataset safety throughout the AI system lifecycle,
establish definitions of safe and unsafe content for your use case.
Create specific criteria for content exclusion across training,
evaluation, and auxiliary datasets, considering both direct harms
and contextual inappropriateness. Implement automated and human
review filtering processes, with protective measures for reviewers.
Document safety definitions and filtering decisions and regularly
audit datasets to verify effective removal of unsafe content while
maintaining necessary testing scenarios.

**Level of risk exposed if this best practice
is not established:** High

## Implementation considerations

- Define what unsafe content looks like for your specific use
case by creating objective definitions that align with your
release criteria.
- Consider implementing filters and other mechanisms to filter
out potentially unsafe or inappropriate content. There may be
scenarios where human review is appropriate and helpful in
identifying problematic content that models might miss or
misclassify. Depending on your use case, seek legal guidance
about whether and how to build in processes to filter training
data for illegal content such as known child sexual abuse
material (CSAM) or adopt additional measures to mitigate risks
related to CSAM and exploitative content.
- Implement protection systems for dataset labelers. For
example, set content warnings, exposure limits, and support
Resources. Create rotation schedules and anonymous reporting
channels for reviewer wellbeing.
- Measure filtering effectiveness regularly. For example, track
removal rates of unsafe content while verifying preservation
of necessary test scenarios.
- Document safety decisions you make to create an audit trail of
what content gets filtered out and why, so you can explain
your choices and improve your process over time.

## Resources

**Related documents:**

- [Flag
harmful content using Amazon Comprehend toxicity
detection](https://aws.amazon.com/blogs/machine-learning/flag-harmful-content-using-amazon-comprehend-toxicity-detection/)
- [Trust
and safety](https://docs.aws.amazon.com/comprehend/latest/dg/trust-safety.html)
- [Automate
media content filtering with AWS](https://aws.amazon.com/blogs/media/automate-media-content-filtering-with-aws/)
- [Data-Centric
Safety and Ethical Measures for Data and AI Governance](https://arxiv.org/pdf/2506.10217)
- [AEGIS2.0:
A Diverse AI Safety Dataset and Risks Taxonomy for Alignment
of LLM Guardrails](https://openreview.net/pdf?id=0MvGCv35wi)
- [BEAVERTAILS:
Towards Improved Safety Alignment of LLM via a
Human-Preference Dataset](https://papers.nips.cc/paper_files/paper/2023/file/4dbb61cb68671edc4ca3712d70083b9f-Paper-Datasets_and_Benchmarks.pdf)
- [CISA
AI Data Security Guidelines - Best Practices for Securing Data
Used to Train & Operate AI Systems](https://media.defense.gov/2025/May/22/2003720601/-1/-1/0/CSI_AI_DATA_SECURITY.PDF)
- [Training
curriculum on AI and data protection Fundamentals of Secure AI
Systems with Personal Data](https://www.edpb.europa.eu/system/files/2025-06/spe-training-on-ai-and-data-protection-technical_en.pdf)
- [AI
Privacy Risks & Mitigations - Large Language Models
(LLMs)](https://www.edpb.europa.eu/system/files/2025-04/ai-privacy-risks-and-mitigations-in-llms.pdf)
- [Thorn
Generative AI Child Safety Commitments](https://www.thorn.org/blog/generative-ai-principles/)
- [ISO/IEC
42001:2023](https://www.iso.org/standard/42001)A.7.2 Data for development and enhancement of
AI system
- [ISO/IEC
42001:2023](https://www.iso.org/standard/42001) A.7.4 Quality of data for AI systems

*Source: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raidp03-bp01.html*

---

# RAIDP03-BP02 Minimize unwanted bias in your datasets

When assessing the quality of a dataset, determine whether it
appropriately represents the demographics of the expected range of
system users. Consider datasets that include self-reported
demographic labels. Calculate if datasets contain sufficient
representation across demographic groups to enable statistically
valid fairness assessments or fairness outcomes.

**Level of risk exposed if this best practice
is not established:** High

## Implementation considerations

- Analyze the demographic composition of your datasets to
identify which groups may be over- or under-represented for
your use case.
- Consider using self-reported demographic labels. For example,
consider using survey responses or user-provided information
rather than algorithmic or human predictions of demographic
information.
- Calculate statistical power for each demographic group in your
evaluation datasets by working backwards from your release
criteria. For instance, determine whether you have enough
examples per group to answer each release criteria question
with the required statistical confidence.
- Address representation gaps by collecting additional data from
underrepresented groups or using techniques like stratified
sampling, where a population is divided into subgroups, or
"strata," based on shared characteristics, and then
a random sample is taken from each subgroup to verify
representation.
- Validate that your bias mitigation efforts don't introduce new
fairness concerns. For example, check if balancing one
demographic dimension inadvertently creates imbalances across
intersectional groups.

## Resources

**Related documents:**

- [Metrics
for Dataset Demographic Bias: A Case Study on Facial
Expression Recognition](https://arxiv.org/html/2303.15889v2)
- [Responsible
AI question bank: A comprehensive tool for AI risk
assessment](https://arxiv.org/pdf/2408.11820)
- [A Review
of Machine Learning Techniques in Imbalanced Data and Future
Trends](https://arxiv.org/pdf/2310.07917)
- [A survey
on learning from imbalanced data streams: taxonomy, challenges, empirical study, and reproducible experimental
framework](https://arxiv.org/pdf/2204.03719)
- [A Survey
on Small Sample Imbalance Problem: Metrics, Feature Analysis,
and Solutions](https://arxiv.org/pdf/2504.14800)
- [Amazon SageMaker AI Clarify: Machine Learning Bias Detection and
Explainability in the Cloud](https://arxiv.org/pdf/2109.03285)
- [Fairness,
model explainability and bias detection with SageMaker AI
Clarify](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-configure-processing-jobs.html)
- [Data
Curation Practices to Minimize Bias in Medical AI.](https://towardsdatascience.com/data-curation-practices-to-minimize-bias-in-medical-ai-379bf6983de2/)
- [DSAP:
Analyzing bias through demographic comparison of
datasets](https://www.sciencedirect.com/science/article/pii/S1566253524005384)
- [Mitigating
Bias in Training Data with Synthetic Data](https://keymakr.com/blog/mitigating-bias-in-training-data-with-synthetic-data/)
- [A
framework to mitigate bias and improve outcomes in the new age
of AI](https://aws.amazon.com/blogs/publicsector/framework-mitigate-bias-improve-outcomes-new-age-ai/)
- [Balance
your data for machine learning with Amazon SageMaker AI Data
Wrangler](https://aws.amazon.com/blogs/machine-learning/balance-your-data-for-machine-learning-with-amazon-sagemaker-data-wrangler/)
- [How
Clarify helps machine learning developers detect unintended
bias](https://www.amazon.science/latest-news/how-clarify-helps-machine-learning-developers-detect-unintended-bias)
- [Generate
Reports for Bias in Pre-training Data in SageMaker AI
Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-data-bias-reports-ui.html)
- [Get
Insights On Data and Data Quality](https://docs.aws.amazon.com/sagemaker/latest/dg/data-wrangler-data-insights.html)
- [Build
an enterprise synthetic data strategy using Amazon
Bedrock](https://aws.amazon.com/blogs/machine-learning/build-an-enterprise-synthetic-data-strategy-using-amazon-bedrock/)
- [ISO/IEC
42001:2023](https://www.iso.org/standard/42001) A.7.2 Data for development and enhancement
of AI system
- [ISO/IEC
42001:2023](https://www.iso.org/standard/42001) A.7.4 Quality of data for AI systems

*Source: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raidp03-bp02.html*

---

# RAIDP03-BP03 Protect the privacy of individuals represented in your datasets

Translate the guidance of your legal counsel on what constitutes
personal information into technical definitions appropriate to your
use case. Implement processes to identify and limit personal
information in training, evaluation, and auxiliary datasets, using
both automated filtering, data obfuscation, and manual review
approaches. Validate the effectiveness of your privacy protection
mechanisms against your taxonomy of personal information types.
Maintain detailed documentation of privacy protection measures and
regularly audit datasets so that personal information removal
doesn't compromise your ability to measure important system
behaviors.

**Level of risk exposed if this best practice
is not established:** High

## Implementation considerations

- Translate the guidance of your legal counsel into a taxonomy
of personal data types. For example, define the string
patterns for direct identifiers (like names and addresses),
quasi-identifiers (like age and zip code), and other
attributes (like health conditions and financial status)
relevant to your domain.
- Implement multi-layered privacy filtering processes combining
automated detection, data obfuscation, and manual review. For
instance, use regex patterns and named entity recognition to
flag potential personal information, and then apply techniques
like tokenization, masking, or synthetic data replacement.
- Create test datasets with deliberately inserted personal
information to evaluate privacy criteria while preserving data
utility.
- Balance privacy protection with system and evaluation needs by
verifying that your privacy measures don't compromise your
system's ability to address your use case or your ability to
test release criteria. For instance, verify that anonymization
techniques maintain demographic diversity needed for fairness
assessments.
- Document privacy protection decisions and create audit trails
of what information gets filtered, obfuscated, or retained.

## Resources

**Related documents:**

- [Towards
Efficient Privacy-Preserving Machine Learning: A Systematic
Review from Protocol, Model, and System Perspectives](https://arxiv.org/pdf/2507.14519)
- [Training
curriculum on AI and data protection Fundamentals of Secure AI
Systems with Personal Data](https://www.edpb.europa.eu/system/files/2025-06/spe-training-on-ai-and-data-protection-technical_en.pdf)
- [AI
Privacy Risks & Mitigations - Large Language Models
(LLMs)](https://www.edpb.europa.eu/system/files/2025-04/ai-privacy-risks-and-mitigations-in-llms.pdf)
- [An
overview of implementing security and privacy in federated
learning](https://link.springer.com/article/10.1007/s10462-024-10846-8)
- [Understanding
Users' Security and Privacy Concerns and Attitudes Towards
Conversational AI Platforms](https://arxiv.org/html/2504.06552v1)
- [Clio:
Privacy-Preserving Insights into Real-World AI Use](https://arxiv.org/pdf/2506.07555)
- [Privacy
Preserving Machine Learning Model Personalization through
Federated Personalized Learning](https://arxiv.org/pdf/2505.01788)
- [Privacy-Preserving
AI: Techniques & Frameworks](https://dialzara.com/blog/privacy-preserving-ai-techniques-and-frameworks)
- [Data
Anonymisation Made Simple - 7 Methods & Best
Practices](https://spotintelligence.com/2025/03/06/data-anonymisation/)
- [A
Comprehensive Guide to Differential Privacy: From Theory to
User Expectations](https://arxiv.org/html/2509.03294v1)
- [Data
protection in AWS Glue DataBrew](https://docs.aws.amazon.com/databrew/latest/dg/data-protection.html)
- [Identifying
and handling personally identifiable information (PII)](https://docs.aws.amazon.com/databrew/latest/dg/personal-information-protection.html)
- [Introducing
PII data identification and handling using AWS Glue DataBrew](https://aws.amazon.com/blogs/big-data/introducing-pii-data-identification-and-handling-using-aws-glue-databrew/)
- [Machine
learning with decentralized training data using federated
learning on Amazon SageMaker AI](https://aws.amazon.com/blogs/machine-learning/machine-learning-with-decentralized-training-data-using-federated-learning-on-amazon-sagemaker/)
- [ISO/IEC
42001:2023](https://www.iso.org/standard/42001) A.7.2 Data for development and enhancement
of AI system
- [ISO/IEC
42001:2023](https://www.iso.org/standard/42001) A.7.4 Quality of data for AI systems

*Source: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raidp03-bp03.html*

---

# RAIDP03-BP04 Include both intrinsic and confounding variations in your datasets

Revisit your release criteria and use case description to confirm
that your definitions of intrinsic and confounding input variations
(respectively, variations the system should attend to, and
variations it should ignore). Include coverage of relevant
variations for your use case in your datasets. If you have
robustness release criteria, label what type of variation is present
in each example in your evaluation set so you can measure how well
your system handles different kinds of variations.

**Level of risk exposed if this best practice
is not established:** High

## Implementation considerations

- Update your lists of intrinsic and confounding input
variations (respectively, variations the system should attend
to and variations it should ignore) based on your release
criteria.
- Determine ways to get examples of intrinsic variations.
Consider whether your samples cover the full distribution of
values possible (for example, the full range of nose
geometries) if designing a system to recognize dogs.
- Determine ways to get examples of confounding variations.
Consider whether your samples cover the full distribution of
values possible (for example, the full range of head poses) if
designing a system to recognize dogs.
- Label variation types in your evaluation datasets to enable
robustness measurements against your release criteria. For
instance, tag each example with metadata indicating whether it
contains lighting variations, formatting changes, or
background differences.

## Resources

**Related documents:**

- [What
is Data Augmentation?](https://aws.amazon.com/what-is/data-augmentation/)
- [ISO/IEC
42001:2023](https://www.iso.org/standard/42001) A.7.2 Data for development and enhancement
of AI system
- [ISO/IEC
42001:2023](https://www.iso.org/standard/42001) A.7.4 Quality of data for AI systems

**Related videos:**

- [Augmenting
Datasets using Generative AI and Amazon Sagemaker for
Autonomous Driving Use Cases on AWS](https://aws.amazon.com/blogs/industries/augmenting-datasets-using-generative-ai-and-amazon-sagemaker-for-autonomous-driving-use-cases-on-aws/)

**Related tools:**

- [Amazon
Bedrock](https://aws.amazon.com/bedrock/)
- [Data
transformation workloads with SageMaker AI Processing](https://docs.aws.amazon.com/sagemaker/latest/dg/processing-job.html)
- [Transform
data with SageMaker AI Data Wrangler](https://docs.aws.amazon.com/sagemaker/latest/dg/data-wrangler-transform.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raidp03-bp04.html*

---

# RAIDP03-BP05 Review the correctness of the content of your datasets

Create regular review processes for ground-truth labels and factual
content across your datasets. Implement fact-checking procedures
using human reviewers or comparison against authoritative sources to
identify and correct inaccuracies. Datasets used for veracity
evaluation may require high accuracy standards to provide reliable
measurements. Document the review process and track accuracy metrics
over time, updating datasets when new information becomes available
or when errors are discovered.

**Level of risk exposed if this best practice
is not established:** High

## Implementation considerations

- Design your datasets with built-in accuracy validation by
enabling multiple sources to confirm factual claims before
including them.
- Create fact-checking workflows that combine domain experts
with authoritative source verification during dataset
creation. Have subject matter experts review content and flag
potential inaccuracies before data gets finalized.
- Apply stricter standards to datasets that will be used for
evaluation, since these provide the ground truth for measuring
release criteria. Engage multiple reviewers to validate each
claim and achieve high agreement before accepting labels.
- Schedule periodic reviews of your dataset content to catch
errors that may have emerged over time or due to changing
information. Plan regular audits where you re-examine your
data to verify labels and factual claims are still accurate.
- Build correction processes for when you discover errors or
when new information becomes available that affects your
dataset accuracy. Create clear workflows for updating factual
content and maintaining dataset integrity over time.

## Resources

**Related documents:**

- [Visualize
data quality scores and metrics generated by AWS Glue Data
Quality](https://aws.amazon.com/blogs/big-data/visualize-data-quality-scores-and-metrics-generated-by-aws-glue-data-quality/)
- [Build
a data quality score card using AWS Glue DataBrew, Amazon Athena, and Quick](https://aws.amazon.com/blogs/big-data/build-a-data-quality-score-card-using-aws-glue-databrew-amazon-athena-and-amazon-quicksight/)
- [Ground
truth generation and review best practices for evaluating
generative AI question-answering with FMEval](https://aws.amazon.com/blogs/machine-learning/ground-truth-generation-and-review-best-practices-for-evaluating-generative-ai-question-answering-with-fmeval/)
- [Inspect
your data labels with a visual, no code tool to create
high-quality training datasets with Amazon SageMaker Ground Truth Plus](https://aws.amazon.com/blogs/machine-learning/inspect-your-data-labels-with-a-visual-no-code-tool-to-create-high-quality-training-datasets-with-amazon-sagemaker-ground-truth-plus/)
- [ISO/IEC
42001:2023](https://www.iso.org/standard/42001)A.7.2 Data for development and enhancement of
AI system
- [ISO/IEC
42001:2023](https://www.iso.org/standard/42001) A.7.4 Quality of data for AI systems

**Related tools:**

- [Amazon
Bedrock Guardrails : Use contextual grounding check to filter
hallucinations in responses](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-contextual-grounding-check.html)
- [The
Effects of Data Quality on Machine Learning Performance on
Tabular Data](https://arxiv.org/abs/2207.14529)
- [A Survey
on Data Quality Dimensions and Tools for Machine
Learning](https://arxiv.org/abs/2406.19614)
- [BoundingDocs:
a Unified Dataset for Document Question Answering with Spatial
Annotations](https://arxiv.org/pdf/2501.03403v1)
- [CodeUltraFeedback:
An LLM-as-a-Judge Dataset for Aligning Large Language Models
to Coding Preferences](https://arxiv.org/pdf/2403.09032v3)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raidp03-bp05.html*

---
