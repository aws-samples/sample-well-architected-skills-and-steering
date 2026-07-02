# RAIRC01 — Define release criteria

**Best Practices**: 1

---

# RAIRC01-BP01 Turn your expected benefits and potential harms into testable release criteria

Turn your identified potential harms and expected benefits into
clear yes or no questions that determine if your system is ready for
deployment. Each question should address either a specific harm you
want to block or a benefit you want your system to deliver. These
questions form the basis of your release criteria that should be
passed before your system is considered ready for release. Track
which stakeholders bear the impact of a failed criterion. You may
need multiple criteria for complex harms and benefits. This approach
yields a consistent, data-driven approach for determining when your
system is ready for release.

**Level of risk exposed if this best practice
is not established:** High

## Implementation considerations

- Take each potential harm and expected benefit you identified
and write it as a yes or no question about prevention or
delivery. For example, change "users might get biased
recommendations" to "Does the system mitigate
unwanted bias for each user group?" and "improved
response time" to "Does the system improve the
response time for user queries?" This assists you to
define exactly what success looks like for harm prevention and
measure whether your system delivers the expected value.
- Check that every question can only be answered yes or no based
on measurable data, not opinions or interpretations. This
reduces ambiguity during evaluation and makes release
decisions clear and objective.
- For each criterion, document the stakeholders who would be
impacted if the system failed to meet the release criterion.
This assists you to prioritize which criteria are most
critical and creates accountability for release decisions.

## Resources

**Related documents:**

- [ISO/IEC
42001:2023](https://www.iso.org/standard/42001) A.6.2.4 AI system verification and
validation

*Source: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/rairc01-bp01.html*

---
