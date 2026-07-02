# MLPERF01 — Business goal identification

**Pillar**: Performance Efficiency  
**Best Practices**: 1

---

# MLPERF01-BP01 Determine key performance indicators

Use guidance from business stakeholders to capture key performance
indicators (KPIs) relevant to the business use case. The KPIs should
be directly linked to business value to guide acceptable model
performance. Consider that machine learning inferences are
probabilistic and will not provide exact results. Identify a minimum
acceptable accuracy and maximum acceptable error in the KPIs. This
enables you to achieve the required business value and manage the
risk of variable results.

**Desired outcome:** By defining
direct, measurable KPIs, ML initiatives deliver quantifiable
business outcomes, such as cost savings, expanded scale, and faster
response times. Clear performance thresholds set realistic
stakeholder expectations and enable risk management based on the
probabilistic nature of ML.

**Common anti-patterns:**

- Implementing ML solutions without defining clear
business-oriented success metrics.
- Focusing solely on technical metrics (like model accuracy)
without connecting them to business outcomes.
- Setting unrealistic expectations for ML performance without
accounting for probabilistic results.
- Failing to define acceptable error thresholds for critical
business processes.
- Neglecting to quantify the actual business value of ML
implementations.

**Benefits of establishing this best
practice:**

- Aligns machine learning (ML) outcomes with business objectives
for measurable value.
- Creates clear expectations about model performance that account
for ML's probabilistic nature.
- Enables objective evaluation of ML solution success based on
business impact.
- Improves prioritization of ML investments based on tangible
results.
- Accelerates decision-making by translating ML insights into
business actions.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Start by identifying business challenges ML aims to solve and how
success translates into specific, quantifiable benefits. Engage
stakeholders throughout KPI selection to verify that business
priorities drive metric design. Use metrics that reflect business
value—such as cost reduction, customer retention rate, or time
savings—rather than technical measures alone.

Regularly review KPIs to stay aligned with strategic shifts.
Feedback from business results informs necessary adjustments to
both models and evaluation metrics. Common pitfalls include
proceeding without clear business KPIs, focusing only on technical
metrics such as accuracy, or establishing unrealistic expectations
that ignore the probabilistic nature of ML results. Failing to set
acceptable error thresholds exposes critical business processes to
unmanaged risk, and overlooking the business value of ML adoption
makes it hard to measure impact or secure stakeholder support.

### Implementation steps

- **Quantify the value of machine
learning for the business**. Consider measures of
how machine learning and automation will impact the
business:

How much will machine learning reduce costs?
- How many more users will be reached by increasing scale?
- How much time will the business save by being able to
respond faster to changes, such as in demand and supply
disruptions?
- How many hours of manual effort will be reduced by
automating with machine learning?
- How much will machine learning be able to change user
behavior, such as reducing churn?

- **Evaluate risks and the tolerance for
error**. Quantify the impact of machine learning on
the business. Rank order the value of impacts to identify
the primary KPIs to optimize with machine learning. Define
the cost of error for automated inferences that will be
performed by ML models in the use case. Determine the
tolerance of the business for error. For example, determine
how far off a cost reduction estimate would have to be to
negatively impact the business goals. Finally, evaluate the
risks of machine learning for the business, and whether the
benefits of ML solutions are of high enough value to
outweigh those risks.
- **Establish baseline
metrics**. Before implementing ML solutions,
document current performance metrics to create a baseline
against which to measure improvements. Collect data on
existing processes, including costs, time requirements,
error rates, and other relevant performance indicators. This
baseline will serve as a reference point for demonstrating
the business value of your ML implementation.
- **Define predictive and prescriptive
KPIs**. Move beyond retrospective metrics to
develop KPIs that offer predictive and prescriptive
insights. Use
[Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) and
[Quick](https://aws.amazon.com/quicksight/) to create dashboards that visualize these
forward-looking KPIs, making them accessible to business
stakeholders.
- **Create a KPI governance
framework**. Develop a structured approach for
monitoring, reviewing, and refining your KPIs over time.
Gather executive alignment on metrics, establish consistent
data collection processes, and define protocols for taking
corrective actions when negative trends emerge. Regularly
analyze trends and periodically refine KPIs to accurately
gauge the business impact of ML implementations.
- **Leverage advanced analytics for
insights**. Enhance KPI discovery and accessibility
by integrating advanced analytics services, such as
[Amazon Q](https://aws.amazon.com/q/). These tools uncover hidden business patterns and
translate complex results into conversational analytics for
non-technical audiences.

## Resources

**Related documents:**

- [Improve
Business Outcomes with Machine Learning](https://aws.amazon.com/machine-learning/ml-use-cases/)
- [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html)
- [Machine
Learning (ML) Governance with Amazon SageMaker AI](https://aws.amazon.com/sagemaker/ai/ml-governance/)
- [Amazon Q for
Business Analytics](https://aws.amazon.com/q/)
- [AI/ML
| AWS Executive Insights](https://aws.amazon.com/executive-insights/generative-ai-ml/)
- [Thought
Leadership | Artificial Intelligence - AWS](https://aws.amazon.com/blogs/machine-learning/category/post-types/thought-leadership/)
- [Keys
to maximizing AI value](https://aws.amazon.com/isv/resources/keys-to-maximizing-generative-ai-value-in-software-companies/)

**Related videos:**

- [How
to Drive Business Value with AI/ML](https://www.youtube.com/watch?v=W4Xd8mPqqKU)
- [Creating
Business Value with AWS AI/ML](https://www.youtube.com/watch?v=A2bIIznG-80)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlperf01-bp01.html*

---
