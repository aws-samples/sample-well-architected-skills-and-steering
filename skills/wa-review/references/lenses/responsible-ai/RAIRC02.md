# RAIRC02 — Measure test properties

**Best Practices**: 3

---

# RAIRC02-BP01 Select metrics to measure the properties tested by the release criteria

For each release criterion you defined, choose specific metrics that
can reliably measure the information needed to answer the question.
A single criterion may require multiple metrics to properly measure
it. Consider both automated metrics (like accuracy scores and
toxicity detection) and human evaluation methods (like expert
reviews and user feedback) depending on what you're measuring and
explore open-source libraries as well as proprietary services that
provide pre-built metrics. Document which metrics map to which
criteria so you have a clear measurement plan for every release
question you need to answer.

**Level of risk exposed if this best practice
is not established:** High

## Implementation considerations

- Take each yes or no release criterion and identify what
specific measurements you need to answer that question. For
example, if your criterion is "Does the system respond to
queries quickly?", you need response time metrics, or if
it's "Does the system block toxic content?", you
need toxicity detection scores. Break down abstract criteria
into concrete, measurable criteria.
- Look for existing automated metrics that can measure what you
need, such as accuracy scores, response time tracking, or
toxicity detection tools. Check open source options like
[scikit-learn](https://scikit-learn.org/stable/modules/model_evaluation.html)
or [Hugging
Face](https://huggingface.co/) libraries as well as paid services such as
[Amazon
Bedrock Evaluations](https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation.html). Automated metrics save time and
provide consistent measurements you can run repeatedly.
- Consider using
[LLM-as-a-judge](https://aws.amazon.com/blogs/machine-learning/llm-as-a-judge-on-amazon-bedrock-model-evaluation/)
for criteria that require understanding context, quality, or
appropriateness. For example, you can prompt an LLM to
evaluate whether responses are helpful, coherent, or follow
specific guidelines by giving it examples and scoring rubrics.
LLM judges work well for subjective assessments that are too
complex for simple automated metrics and are more scalable
than human review.
- Identify which criteria need human evaluation because neither
automated metrics nor LLM judges can capture what you're
trying to measure. For example, measuring whether user
interface designs are intuitive may require actual users to
test the interface to better capture the real user experience
and preferences. Human evaluation catches the most nuanced
issues and is more representative of your user experience but
is slower and more expensive.
- If you find yourself needing multiple different metrics to
test one criterion because the criterion itself is complex,
consider splitting the criterion into separate yes or no
questions. For example, change "Does the system provide a
good user experience?" into "Does the system respond
quickly?", "Does the system give accurate
results?", and "Does the system have an intuitive
interface?" This makes each criterion simple to measure
definitively.
- Track which metric you'll use for each release criterion. This
gives you a clear testing plan and creates a mapping from your
measurements to your release criteria.

## Resources

**Related documents:**

[Amazon SageMaker AI AI : Metrics and Validation](https://docs.aws.amazon.com/sagemaker/latest/dg/autopilot-metrics-validation.html)

[Amazon SageMaker AI Canvas : Metrics reference](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-metrics.html)

[Evaluating
your SageMaker AI AI-trained model](https://docs.aws.amazon.com/sagemaker/latest/dg/nova-model-evaluation.html#nova-model-evaluation-benchmark)

[Evaluation
metrics and statistical tests for machine learning](https://www.nature.com/articles/s41598-024-56706-x)

[ISO/IEC
42001:2023](https://www.iso.org/standard/42001) A.6.2.4 AI system verification and validation

**Related tools:**

[Metrics
and scoring: quantifying the quality of predictions](https://scikit-learn.org/stable/modules/model_evaluation.html)

[LLM-as-a-judge
on Amazon Bedrock Model Evaluation](https://aws.amazon.com/blogs/machine-learning/llm-as-a-judge-on-amazon-bedrock-model-evaluation/)

[Hugging Face](https://huggingface.co/)

[Amazon
Bedrock Evaluations](https://aws.amazon.com/bedrock/evaluations/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/rairc02-bp01.html*

---

# RAIRC02-BP02 Consider strength and limitation trade-offs when choosing metrics

Before selecting a metric to measure a release criterion, assess its
strengths and weaknesses. Validate model-derived metrics (such as
LLM-as-a-judge or -jury) through correlation with human assessors,
and document limitations that affect reproducibility (for example,
random seed or model version used in LLM-as-a-judge). Evaluate
metrics derived from human assessors and annotators for unwanted
bias, assessor variance, and consistency. Consider trade-offs
between automated metrics, which are generally consistent but may
miss context, compared to human evaluation, which may be more
nuanced but subjective and harder to scale.

**Level of risk exposed if this best practice
is not established:** High

## Implementation considerations

- Track what each potential metric does well and what it might
miss before you choose it. For example, automated accuracy
scores are consistent and fast, but might not catch responses
that are technically correct but unhelpful to users.
Understanding these trade-offs upfront assists you to pick the
right combination of metrics.
- Test LLM-based or model-derived metrics against human
evaluators to see how well they agree. Run a set of examples
through both your LLM judge and human reviewers, then
calculate correlation scores to see if the LLM is measuring
what you think it is. This validation catches cases where LLMs
might have different responses than humans.
- Check your human evaluators for bias and consistency by having
multiple people evaluate the same examples and comparing their
scores. Look for patterns where certain evaluators
consistently rate things higher or lower or where people
disagree a lot on similar examples. This assists you to spot
when human judgment might be unreliable or a task is too
subjective.
- Balance the trade-offs between automated metrics that are
consistent but might miss nuance and human evaluation that may
be more representative of your users but increases costs and
time. Use automated metrics for things you can measure
objectively and human evaluation when human feedback is vital.
- Document your final metric choices and why you picked them,
including what limitations you're accepting. This assists
future team members understand your reasoning and alerts them
to potential blind spots in your measurements.

## Resources

**Related documents:**

- [Evaluate
the performance of Amazon Bedrock Resources](https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation.html)
- [Review
metrics for an automated model evaluation job in Amazon
Bedrock (console)](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-report-programmatic.html)
- [Create
a model evaluation job with Amazon Bedrock](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/model-evaluation-jobs-management-create.html)
- [ISO/IEC
42001:2023](https://www.iso.org/standard/42001) A.6.2.4 AI system verification and
validation

*Source: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/rairc02-bp02.html*

---

# RAIRC02-BP03 Design a custom metric if no suitable metric exists

When creating custom metrics for benefits or potential harmful
events, define what you need to measure and its key characteristics.
Break complex concepts into quantifiable components that directly
relate to stakeholder impacts. Design metrics with definitions and
examples of positive and negative results, including edge cases.
Validate your custom metric against known examples, choose
appropriate measurement scales (like binary, categorical, or
continuous), and document the methodology. Plan for refinement based
on testing, being cautious of metrics that may not generalize well
beyond initial testing.

**Level of risk exposed if this best practice
is not established:** High

## Implementation considerations

- Clearly define what you're trying to measure and write down
its key characteristics, focusing on how it directly impacts
your stakeholders. For example, if you need to measure how
natural a conversation is, define what makes a conversation
feel natural or robotic to your specific users. This
foundation assists to build an accurate metric.
- Break complex concepts down into smaller pieces that you can
count or score. For example, split user satisfaction into task
completion rate, time to complete, and user survey scores, as
you can measure each of these objectively. This makes abstract
concepts concrete and measurable.
- Identify what good and bad results look like, including edge
cases that might confuse your metric. Define that a helpful
response should be accurate, relevant, and actionable. Clear
examples reduce confusion during measurement.
- Test your custom metric on examples where you already know
what the right answer should be. Run your metric on obviously
good and obviously bad examples to see if it gives the results
you expect. This catches major problems with your metric
design before you use it on real data.
- Choose the types of scores your measurement needs. Continuous
scores give you more nuanced information and let you track
gradual improvements, while categorical ratings are simpler
for humans and LLM judge models to assign consistently and
binary scores simplify the metric but can hide performance
nuance.
- Document exactly how to calculate your metric, including
step-by-step instructions that someone else could follow to
get the same results. This blocks inconsistency when different
team members apply your metric and assists you to spot
problems in your methodology
- Plan to refine your metric based on real testing since custom
metrics often need adjustment after you see how they perform.
Start with small tests and be ready to modify the metric if it
doesn't work well in practice or gives misleading results on
new types of data.

## Resources

**Related documents:**

[Use
custom metrics to evaluate your generative AI application with
Amazon Bedrock](https://aws.amazon.com/blogs/machine-learning/use-custom-metrics-to-evaluate-your-generative-ai-application-with-amazon-bedrock/)

[ISO/IEC
42001:2023](https://www.iso.org/standard/42001) A.6.2.4 AI system verification and validation

**Related tools:**

[scikit
learn : make_scorer](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.make_scorer.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/rairc02-bp03.html*

---
