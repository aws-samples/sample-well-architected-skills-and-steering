# RAIMON02 — Responding to feedback

**Best Practices**: 1

---

# RAIMON02-BP01 Create feedback loops to apply monitoring results to system improvement

Translate monitoring results, incident patterns, and performance
trends into actionable system improvements and risk mitigation
enhancements. Implement regular review cycles that analyze
monitoring data across multiple time horizons, identifying both
immediate optimization opportunities and longer-term improvement
strategies based on usage patterns and performance drift. Update
system components based on monitoring insights, including refining
guardrails, adjusting model parameters, updating training data, and
modifying deployment strategies. Track the effectiveness of
monitoring-driven improvements by validating that changes address
identified issues without introducing new problems or degrading
system performance in other areas.

**Level of risk exposed if this best
practice is not established:** Medium

## Implementation considerations

- Establish regular monitoring review cycles: daily checks for
immediate issues, weekly trend analysis, and monthly pattern
reviews. Example: Review ML model accuracy daily, analyze
feature drift patterns weekly, evaluate system performance
trends monthly.
- Create an improvement action framework to categorize
monitoring insights into quick fixes, medium-term adjustments,
and long-term enhancements.
- Build an automated alert-to-action pipeline that connects
monitoring alerts to specific improvement workflows. Example:
Configure Amazon SageMaker AI Model Monitor to capture incoming
data and detect changes in model feature distributions or
prediction patterns. Set up Amazon EventBridge to
automatically initiate SageMaker AI Pipeline for model retraining
when Model Monitor detects data drift beyond defined
thresholds.
- Implement validation checks to measure improvement
effectiveness. Example: Compare model metrics pre and
post-retraining, monitor downstream impacts, and validate that
automated improvements maintain model quality standards.

## Resources

**Related documents:**

- [Automate
model retraining with Amazon SageMaker AI Pipelines when drift is
detected](https://aws.amazon.com/blogs/machine-learning/automate-model-retraining-with-amazon-sagemaker-pipelines-when-drift-is-detected/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raimon02-bp01.html*

---
