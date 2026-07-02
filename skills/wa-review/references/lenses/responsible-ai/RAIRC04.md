# RAIRC04 — Release criteria thresholds

**Best Practices**: 3

---

# RAIRC04-BP01 Identify baseline performance targets

Set specific performance goals for your AI system before you build
it. These goals become the pass or fail criteria that determine
whether your system is ready to release. Good targets are based on
real data, not guesswork, and assist you to make clear decisions
about when your system is working well enough to release.

**Level of risk exposed if this best practice
is not established:** High

## Implementation considerations

- Research existing performance benchmarks in your domain by
collecting data on how current solutions perform and what
users need from your system. Look at industry standards,
competitor performance, and user satisfaction data to
understand the performance bar for your specific use case.
- Collect baseline data from existing systems, user studies, or
pilot tests that show what performance levels are achievable
and what users will accept for each of your metrics. Real
baseline data assists you to set targets that are challenging
but realistic instead of impossible or too simple.
- Set specific performance targets for your metrics by deciding
what performance levels are acceptable for each measurement.
This approach transforms your measurement capabilities into
clear pass or fail criteria that guide your development and
deployment decisions.
- Plan how you'll track and update your performance targets as
you learn more about your system and users by building
feedback loops that capture real-world performance data after
deployment. Create processes for adjusting targets when you
discover your initial goals were too high, too low, or missed
important performance dimensions. Flexible target management
assists you to improve your system over time while maintaining
the discipline of clear performance goals.

## Resources

**Related documents:**

- [ISO/IEC
42001:2023](https://www.iso.org/standard/42001) A.6.2.4 AI system verification and
validation
- [ISO/IEC
42001:2023](https://www.iso.org/standard/42001) A.9.3 Objectives for responsible use of AI
system

*Source: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/rairc04-bp01.html*

---

# RAIRC04-BP02 Consider trade-offs between release criteria

Consider trade-offs where meeting your criteria thresholds for one
potential harm may reduce your ability to meet the criteria for
another harm (for example, privacy as opposed to transparency).
Consider harm and benefit trade-offs where meeting the criteria for
your potential harms may also reduce your ability to meet the
criteria for your benefits. Reconsider your threshold choices to
appropriately balance the trade-offs given your use case priorities
and document trade-off decisions.

**Level of risk exposed if this best practice
is not established:** High

## Implementation considerations

- Map competing metric relationships and potential conflicts.
For example, create a matrix showing how stricter privacy
requirements might limit model explainability, or how higher
accuracy targets could impact latency performance.
- In the context of the metric relationships you identified,
consider the limits you would set on each competing metric.
For example, when user privacy and model accuracy compete, you
may opt for privacy requirements even if it means accepting
lower accuracy within acceptable bounds.
- Document threshold decisions and rationale. For example,
record final thresholds, identified conflicts, and
justification for trade-off decisions in release documentation
for future reference and auditing.

## Resources

**Related documents:**

- [ISO/IEC
42001:2023](https://www.iso.org/standard/42001) A.6.2.4 AI system verification and
validation
- [ISO/IEC
42001:2023](https://www.iso.org/standard/42001) A.9.3 Objectives for responsible use of AI
system

*Source: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/rairc04-bp02.html*

---

# RAIRC04-BP03 Set confidence requirements for your quantitative release criteria

Decide how certain you need to be that your system meets each
performance threshold before each release criterion question can be
answered. For example, if you were to divide use cases into higher,
moderate, and lower risk, you might set corresponding confidence
requirements to 99%, 95%, and 90% respectively. Consider what level
of confidence your stakeholders might expect.

**Level of risk exposed if this best practice
is not established:** High

## Implementation considerations

- Group your release criteria by risk level to understand which
performance decisions need higher confidence as opposed to
those where you can accept more uncertainty. Create simple
risk categories like high, medium, and low based on how much
harm could result if you're wrong about whether your system
meets each performance limit. This grouping assists you to
focus your most rigorous testing on the decisions that matter
most while avoiding over-testing low-risk areas.
- Check what confidence levels your key stakeholders expect by
talking with users, business leaders, and other groups who
depend on your system working correctly. Compare their
expectations with your planned confidence levels and adjust
where there are mismatches between what you're planning and
what they need. Stakeholder alignment assists you to avoid
surprise rejection of your system because your confidence
levels don't match their risk tolerance.
- Set specific confidence levels for each risk category by
deciding how certain you need to be before you can confidently
say your system meets each performance limit. Assign
confidence percentages like 99% for high-risk decisions, 95%
for medium-risk, and 90% for lower-risk areas based on what
level of uncertainty and risk tolerance your organization and
stakeholders can accept.
- For each release criteria, transform your question from
"Does our system produce accurate outputs?" into
confidence, threshold, and metric-based questions like
"Are we at least 95% confident that our system achieves
at least 85% accuracy on our LLM-as-a-judge metric for
correctness?" This allows for clear, objective and
measurable criteria that leads to binary yes or no responses
that account for measurement uncertainty.

## Resources

**Related documents:**

- [ISO/IEC
42001:2023](https://www.iso.org/standard/42001) A.6.2.4 AI system verification and
validation
- [ISO/IEC
42001:2023](https://www.iso.org/standard/42001) A.9.3 Objectives for responsible use of AI
system

*Source: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/rairc04-bp03.html*

---
