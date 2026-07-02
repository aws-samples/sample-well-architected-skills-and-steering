# RAIDP02 — Dataset quality

**Best Practices**: 4

---

# RAIDP02-BP01 Validate the representativeness of datasets for the use case

Consider whether your datasets accurately reflect the real-world
conditions where your system will be used. Gather examples that
represent your users while filtering out data from contexts that
don't match your use case. This is especially relevant for
fine-tuning, alignment, and calibration sets, and for evaluation
sets since testing on unrepresentative data can make it seem that
your system works better (or worse) than it really does. Ask
yourself: "Does this dataset reflect how my system will be used
and exclude scenarios that are not part of my use case?"
Document what you've included and excluded so you know where your
results might not be sufficient.

**Level of risk exposed if this best practice
is not established:** High

## Implementation considerations

- Determine who will consistently use your system and how
they'll use it by thinking through your real deployment
scenario. Consider how users typically interact with systems
like yours and what kinds of inputs they'll give you. This
assists you to understand the representative data for your
actual use case.
- Check whether your datasets match real user inputs by
comparing what's in your datasets against what you've
documented about your use case context. Look for gaps where
you're missing certain user groups, missing typical
interaction styles, or including data from scenarios that
don't match how your system could be used.
- Clean up your datasets by removing examples that don't match
your use case and adding examples that fill important gaps.
Focus on your fine-tuning, alignment, calibration, and
evaluation datasets since these directly affect how your
system behaves and how accurately you can measure its
performance.
- Record what you included and excluded from your datasets, so
the limitations are known. Keep track of which user groups or
scenarios might not be well-covered so you understand your
evaluation limitations.

## Resources

**Related documents:**

- [Training
data labeling using humans with Amazon SageMaker Ground Truth](https://docs.aws.amazon.com/sagemaker/latest/dg/sms.html)
- [Using
Amazon Augmented AI for Human Review](https://docs.aws.amazon.com/sagemaker/latest/dg/a2i-use-augmented-ai-a2i-human-review-loops.html)
- [Data
lineage in Amazon DataZone](https://docs.aws.amazon.com/datazone/latest/userguide/datazone-data-lineage.html)
- [Dataset
Representativeness and Downstream Task Fairness](https://arxiv.org/abs/2407.00170)
- [NIST
Towards a Standard for Identifying and Managing Bias in
Artificial Intelligence](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.1270.pdf)
- [Policy
advice and best practices on bias and fairness in AI](https://link.springer.com/article/10.1007/s10676-024-09746-w)
- [ISO/IEC
42001:2023](https://www.iso.org/standard/42001) A.7.4 Quality of data for AI systems

*Source: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raidp02-bp01.html*

---

# RAIDP02-BP02 Set dataset quality requirements based on your release criteria

Work backwards from your release criteria to define the quality
standards for each dataset, then select metrics and thresholds to
measure when your data meets those standards. Think of this as
creating data readiness criteria just like your system release
criteria. Data quality means different things depending on how
you'll use the data and what your release criteria need. For
example, it could mean label accuracy, representation across user
groups, diversity of examples, or completeness of coverage.

For each dataset, pick specific quality metrics that align with your
release criteria and set minimum thresholds that should be met
before using that data. Different datasets need different quality
bars. For example, evaluation sets require higher quality standards
than training sets.

**Level of risk exposed if this best practice
is not established:** High

## Implementation considerations

- Work backwards from each release criterion to determine the
quality standards means for your datasets by asking,
"What quality level does my data need to reach for me to
trust this measurement?" Define what quality means for
each use case, whether that's label accuracy for fairness
testing, completeness for harm detection, or consistency for
robustness evaluation.
- Pick specific quality metrics that align with how you'll use
each dataset by choosing measurements like missing value
rates, label agreement scores, noise levels, or coverage
percentages. Make sure your metrics connect to your release
criteria instead of just measuring generic data health that
might not matter for your specific goals.
- Set minimum quality thresholds that must be met before you can
use each dataset by deciding on specific numbers like label
accuracy above 95%, missing values below 2%, or representation
coverage across demographic groups. Document these thresholds
as clear pass or fail criteria that your team can check
against.
- Set high quality standards for your evaluation data since
evaluation quality directly affects your confidence in release
decisions and noise in this data could lead to inaccurate test
results.
- Build data readiness checks that validate your quality
thresholds before using a dataset by setting up both automated
validation for quantitative metrics and manual reviews for
qualitative standards. Treat these like deployment gates that
block you from using data that doesn't meet your quality
criteria.

## Resources

**Related documents:**

- [Amazon
Responsible AI Best Practices](https://aws.amazon.com/machine-learning/responsible-ai/)
- [Data
Quality Assessment Guidelines](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-data-quality.html)
- [ISO/IEC
42001:2023](https://www.iso.org/standard/42001) A.7.4 Quality of data for AI systems

*Source: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raidp02-bp02.html*

---

# RAIDP02-BP03 Validate the quality of human and generated labels and features in your dataset

Implement quality control mechanisms for human annotators including
training processes, unwanted bias identification, and inter-rater
agreement measurements. Assess potential sources of unwanted human
bias and establish procedures to minimize their impact on label
quality. When using synthetic or model-generated labels, validate
their accuracy against human judgment and document known limitations
that affect reliability. Track annotator performance over time and
implement feedback mechanisms to maintain consistent labeling
standards across your datasets.

**Level of risk exposed if this best practice
is not established:** High

## Implementation considerations

- Set up quality control for human annotators by creating
training processes that teach consistent labeling, measuring
how well different annotators agree with each other, and
checking for unwanted biases in their work. Build simple tests
using examples with known correct answers to catch annotators
who aren't following guidelines or who might be introducing
their own biases into the labels.
- Hunt for sources of human bias in your labeling process by
looking at whether certain annotators consistently label some
groups differently than others, whether the annotation
guidelines accidentally encourage biased decisions, or whether
the examples themselves push annotators toward unfair
judgments.
- Check synthetic and model-generated labels against human
judgment by reviewing a sample of machine-generated labels to
see how often they're wrong or misleading. Test whether your
synthetic labels work well for underrepresented groups and
edge cases where automated systems may fail, and document the
specific limitations you discover.
- Track how your annotators perform over time by measuring their
consistency, accuracy, and agreement with other annotators
across different batches of work. Set up alerts that flag when
someone's quality drops or when they start showing new bias
patterns, so you can provide additional training or feedback
before it affects too much data.
- Build feedback loops that maintain consistent labeling
standards by giving annotators regular updates on their
performance, sharing examples of good and bad labels, and
updating your guidelines when you discover new edge cases or
bias sources. Create processes for fixing labels that don't
meet your quality standards to block similar problems in
future annotation work.

## Resources

**Related documents:**

- [Amazon
Sagemaker Ground Truth](https://docs.aws.amazon.com/sagemaker/latest/dg/sms.html)
- [Amazon
Sagemaker AI Augmented AI](file:///Users/chadhrac/Downloads/Users/chadhrac/Downloads/-%20%20https:/docs.aws.amazon.com/sagemaker/latest/dg/a2i-use-augmented-ai-a2i-human-review-loops.html)
- [Amazon
Responsible AI Best Practices](https://aws.amazon.com/machine-learning/responsible-ai/)
- [Data
Quality Assessment Guidelines](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor-data-quality.html)
- [ISO/IEC
42001:2023](https://www.iso.org/standard/42001) A.7.4 Quality of data for AI systems

*Source: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raidp02-bp03.html*

---

# RAIDP02-BP04 Validate the quality and reliability of augmented or synthetic datasets

Assess the quality of model-generated labels and synthetic examples
against human evaluation standards. Identify potential sources of
unwanted bias in synthetic data generation. Validate that synthetic
data maintains the statistical properties needed for your specific
datasets and doesn't exclude important edge cases. Document the
limitations of synthetic approaches and verify that synthetic
examples can effectively substitute for real data in representing
the phenomena you care about.

**Level of risk exposed if this best practice
is not established:** High

## Implementation considerations

- Test your synthetic data quality against human standards by
reviewing samples of your generated examples and labels to see
how realistic and accurate they are. Check whether humans can
tell the difference between your synthetic data and real data,
and measure how often your synthetic examples contain errors
or unrealistic patterns that could mislead your model
training.
- Search for bias in your synthetic data generation by checking
whether your generation process consistently produces unfair
or skewed examples for certain groups. Look at whether your
synthetic data overrepresents some demographics while
underrepresenting others, and test whether the generation
process amplifies existing biases from your source data or
introduces new ones.
- Verify that your synthetic data keeps the statistical
properties you need by comparing distributions, correlations,
and patterns between your synthetic and real data. Make sure
your synthetic examples don't accidentally exclude important
edge cases or rare scenarios that your model needs to handle,
and check that key relationships in the data are preserved.
- Test whether synthetic examples can substitute for real data
by having domain experts evaluate whether your synthetic
examples capture the key phenomena and scenarios you need to
represent, or by training discriminator models to predict
whether examples are real or synthetic. If your synthetic data
is high quality, the model should struggle to tell the
difference. Check if your synthetic data covers the same range
of situations, edge cases, and user behaviors as your real
data, and verify that it includes the specific patterns and
relationships that matter for your use case.
- Document the limitations and failure modes that you discover
in your synthetic data so downstream users know where it might
be unreliable. Write down what types of examples your
synthetic data handles well versus poorly, what biases it
contains, and when it should versus shouldn't be used as a
substitute for real data.

## Resources

**Related documents:**

- [AWS Well-Architected Machine Learning Lens](https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/welcome.html)
- [Responsible
AI Best Practices for Synthetic Data](https://aws.amazon.com/machine-learning/responsible-ai/)
- [NIST
AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
- [Partnership on
AI Synthetic Media Framework](https://partnershiponai.org/)
- [ISO/IEC
42001:2023](https://www.iso.org/standard/42001)A.7.4 Quality of data for AI systems

*Source: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raidp02-bp04.html*

---
