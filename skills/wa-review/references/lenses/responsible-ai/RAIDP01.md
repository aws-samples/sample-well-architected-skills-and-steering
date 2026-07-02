# RAIDP01 — Identify datasets

**Best Practices**: 4

---

# RAIDP01-BP01 Identify evaluation datasets needed to measure system performance against release criteria

Work backwards from your release criteria to identify the specific
evaluation datasets needed to test each one. Validate that each
dataset has the right characteristics for its purpose (for example,
demographic labels for fairness testing, harmful content examples
for safety testing, and sufficient sample sizes for statistical
confidence). Track mappings between datasets and criteria so you can
verify complete coverage and maintain traceability between your
release criteria and testing approach.

**Level of risk exposed if this best practice
is not established:** High

## Implementation considerations

- For each release criterion, develop a dataset design that
specifies the required data sources and data labels. Use your
analysis of intrinsic and confounding variations to clarify
the specifications. For example, safety testing may require
harmful content examples and fairness testing may require
demographic labels across groups.
- Calculate required dataset sizes using statistical power
analyses based upon the desired confidence level and interval
for the criterion. Verify that the subgroup representation and
sample sizes are adequate to test your release criteria with
the required confidence you have set.
- Consider whether one dataset can be used for multiple
criteria. If so, verify that the statistical power offered by
the dataset meets the needs of the most stringent release
criterion.
- Consider whether one criterion requires evaluation using
multiple datasets. If your understanding of intrinsic and
confounding variations is limited by known or unknown issues,
your evaluation may benefit from using several independently
sourced datasets.

## Resources

**Related documents:**

- [Statistical
Power Analysis for the Behavioral Sciences](https://utstat.utoronto.ca/~brunner/oldclass/378f16/readings/CohenPower.pdf)
- [Bedrock
Model Evaluation](https://aws.amazon.com/bedrock/evaluations/)
- [NIST
AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
- [Datasheets
for Datasets methodology](https://arxiv.org/abs/1803.09010)
- [ISO/IEC
42001:2023](https://www.iso.org/standard/42001) A.4.3 Data Resources

*Source: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raidp01-bp01.html*

---

# RAIDP01-BP02 Identify the datasets needed for training and customizing your system

Identify and plan datasets needed to train your AI system to meet
your release criteria. Determine which dataset types (training,
fine-tuning, validation, calibration, and alignment) you need based
on your training approach, assess existing data to identify gaps,
then acquire or build the missing datasets through external sources,
your own collection, crowdsourcing, or synthetic generation.
Finally, plan how to combine and allocate your datasets while
keeping them separate from evaluation data and maintaining proper
representation across user groups.

**Level of risk exposed if this best practice
is not established:** High

## Implementation considerations

- Map release criteria to training data requirements by listing
specific capabilities, behaviors, and knowledge areas your
system should demonstrate. Identify what types of training
examples you need for each criterion, like domain-specific
terminology for accuracy or diverse interactions for fairness.
- Assess existing training data and identify gaps by checking
which model capabilities your current datasets support. Look
for missing edge cases, underrepresented languages, or
insufficient examples for specific behaviors your system needs
to learn.
- Choose between building custom datasets and using existing
ones by weighing control against cost for each gap. Custom
datasets provide precise control but require more Resources,
while existing datasets are faster but may not perfectly match
your needs.
- Plan data combination and allocation across training phases
including pre-training, fine-tuning, validation, calibration,
and alignment while maintaining complete separation from
evaluation datasets. Design systems that block
training-evaluation overlap to protect measurement integrity.

## Resources

**Related documents:**

- [Generative
AI lifecycle](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/generative-ai-lifecycle.html)
- [Responsible
AI Best Practices: Promoting Responsible and Trustworthy AI
Systems](https://aws.amazon.com/blogs/enterprise-strategy/responsible-ai-best-practices-promoting-responsible-and-trustworthy-ai-systems/)
- [AWS Generative AI Best Practices Framework v2](https://docs.aws.amazon.com/audit-manager/latest/userguide/aws-generative-ai-best-practices.html)
- [ISO/IEC
42001:2023](https://www.iso.org/standard/42001) A.4.3 Data Resources

*Source: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raidp01-bp02.html*

---

# RAIDP01-BP03 Identify auxiliary datasets needed to operate your system

Auxiliary data covers additional data that affects your system
behavior beyond the training, validation, and evaluation datasets,
such as knowledge bases used at inference time by RAG systems.
Identify auxiliary data sources that affect system behavior during
operation. Determine whether auxiliary datasets should be identical
between evaluation and deployment environments or if differences are
acceptable based on your use case requirements.

**Level of risk exposed if this best practice
is not established:** High

## Implementation considerations

- Map auxiliary data sources your system uses during operation,
like knowledge bases for retrieval, reference databases for
fact checking, or real-time feeds for updates. Look at your
system architecture to determine where additional data is
pulled in and affects behavior. This assists you to see the
complete data picture beyond just training datasets.
- Find gaps where auxiliary data could fill coverage holes by
analyzing what your training and evaluation data is missing.
Check for underrepresented groups, missing domain knowledge,
or outdated information. For example, if training data lacks
recent events, you might need auxiliary news feeds.
- Source auxiliary data that complements rather than duplicates
your existing datasets by exploring databases, APIs, sensor
feeds, and knowledge bases. Verify that auxiliary sources
bring new perspectives or fill specific gaps instead of
repeating patterns you already captured.
- Plan to run tests on whether auxiliary datasets improve system
capabilities using experiments comparing performance with and
without the auxiliary data. Build simple tests showing whether
auxiliary information assists with edge cases, accuracy, or
underrepresented user groups.
- Plan auxiliary data management by deciding which data should
stay identical between testing and deployment versus which can
differ. Build processes for updating auxiliary data when it
becomes stale and create checks that verify datasets still
match operational needs.

## Resources

**Related documents:**

- [An
introduction to preparing your own dataset for LLM
training](https://aws.amazon.com/blogs/machine-learning/an-introduction-to-preparing-your-own-dataset-for-llm-training/)
- [Prepare
ML Data with Amazon SageMaker AI Data Wrangler](https://docs.aws.amazon.com/sagemaker/latest/dg/data-wrangler.html)
- [What
is RAG (Retrieval-Augmented Generation)?](https://aws.amazon.com/what-is/retrieval-augmented-generation/)
- [Build
verifiable explainability into financial services workflows with Automated Reasoning checks for Amazon Bedrock Guardrails](https://aws.amazon.com/blogs/machine-learning/build-verifiable-explainability-into-financial-services-workflows-with-automated-reasoning-checks-for-amazon-bedrock-guardrails/)
- [Revisiting
the Auxiliary Data in Backdoor Purification](https://arxiv.org/html/2502.07231v1)
- [Learning
to Group Auxiliary Datasets for Molecule](https://arxiv.org/pdf/2307.04052)
- [Unanswerability
Evaluation for Retrieval Augmented Generation](https://arxiv.org/html/2412.12300v1)
- [Training a
Helpful and Harmless Assistant with Reinforcement Learning
from Human Feedback](https://arxiv.org/abs/2204.05862)
- [AI
Benchmarks and Datasets for LLM Evaluation](https://arxiv.org/html/2412.01020v1#S4)
- [ISO/IEC
42001:2023](https://www.iso.org/standard/42001) A.4.3 Data Resources

*Source: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raidp01-bp03.html*

---

# RAIDP01-BP04 Identify potential overlaps between datasets

Check for unintended data overlap between your training, evaluation,
and auxiliary datasets. Ideally, evaluation datasets will contain
entirely new examples that your system has never encountered during
training, as testing on previously seen data can result in
overconfidence in your system capabilities due to overfitting or
memorization. Verify that you do not include public benchmarks used
for evaluation in training data, particularly when using foundation
models where training data provenance may be unclear. Document
unavoidable overlaps and assess their potential impact on evaluation
validity.

**Level of risk exposed if this best practice
is not established:** High

## Implementation considerations

- Define what it means for the content of training and
evaluation datasets to be too similar. For example, if you are
building a bird classifier, you may not want the evaluation
dataset to contain an image of a flock of birds and the
training dataset to contain a sub-image from the flock image,
even if the sub-image is contrast enhanced.
- Define what risk there might be, if any, of having auxiliary
and evaluation datasets overlap. For example, you may not want
a RAG system to be tested using queries that exactly match the
text of FAQs in the RAG document library.
- Using your definitions of similarity, scan for unwanted
similarities between your training, evaluation, and auxiliary
data, and estimate the degree of overlap between each dataset.
- If there are overlaps you cannot remove, estimate the impact
on release criteria, adjusting release criteria as necessary.
- Track changes in overlaps as your datasets evolve by setting
up automated systems to flag similarities when you add or
update data.

## Resources

**Related documents:**

- [Duplicate
Detection with GenAI](https://arxiv.org/abs/2406.15483)
- [Prepare ML Data with Amazon SageMaker AI Data Wrangler](https://docs.aws.amazon.com/sagemaker/latest/dg/data-wrangler.html)
- [An Analysis of Dataset Overlap on Winograd-Style Tasks](https://arxiv.org/pdf/2011.04767)
- [A Large-scale Comprehensive Dataset and Copy-overlap Aware Evaluation Protocol for Segment-level Video Copy Detection](https://arxiv.org/pdf/2203.02654)
- [Data Augmentation for Conflict and Duplicate Detection in Software
Engineering Sentence Pairs](https://arxiv.org/pdf/2305.09608)
- [Towards Scalable Generation of Realistic Test Data for Duplicate
Detection](https://arxiv.org/pdf/2312.17324)
- [What
is Overfitting?](https://aws.amazon.com/what-is/overfitting/)
- [ISO/IEC
42001:2023](https://www.iso.org/standard/42001) A.4.3 Data Resources

*Source: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raidp01-bp04.html*

---
