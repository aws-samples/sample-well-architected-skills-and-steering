# RAIBR03 — Assess risks

**Best Practices**: 4

---

# RAIBR03-BP01 Identify the likelihood of each potential harm

Establish a risk rating methodology that considers the likelihood of
the event occurring. The risk likelihood indicates the probability
of a harmful event occurring when the system is deployed for the use
case.

**Level of risk exposed if this best practice
is not established:** High

## Implementation considerations

- Create a standardized likelihood scale with clear definitions.
For example, establish ranges from *almost
certain* (95%+ probability) to *highly
unlikely* (less than 5% probability). Include
specific frequency ranges for each category to maintain
consistent evaluation.
- Document likelihood assessments with supporting evidence. For
example, consider a content moderation system where historical
data shows harmful content detection failures occur in 15% of
edge cases, placing this risk in the
*unlikely* category. Include rationale for
each assessment.

## Resources

**Related documents:**

- [Learn
how to assess the risk of AI systems](https://aws.amazon.com/blogs/machine-learning/learn-how-to-assess-risk-of-ai-systems/)
- [NIST
Risk Management Framework](https://csrc.nist.gov/projects/risk-management/about-rmf)
- [Responsible
AI in the generative era](https://www.amazon.science/blog/responsible-ai-in-the-generative-era)
- [ISO/IEC
42001:2023](https://www.iso.org/standard/42001) A.5.2 AI system impact assessment process

*Source: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raibr03-bp01.html*

---

# RAIBR03-BP02 Identify the severity of each potential harm

Risk severity estimates the magnitude of the negative on affected
stakeholder groups if it were to occur. Severity also considers the
reversibility of harm, recognizing that some types of harm may be
permanent or difficult to remedy.

**Level of risk exposed if this best practice
is not established:** High

## Implementation considerations

- Create standardized severity scale with clear impact levels.
For example, establish a range from *low*
(minimal, reversible impact) to *extreme*
(substantial, long-lasting impact). Include specific criteria
for each level to enable consistent evaluation.
- Evaluate harm severity considering multiple factors. As an
example, in medical AI systems, incorrect diagnoses might have
*major* severity due to potential health
impacts and difficulty in reversing treatment decisions.
Consider immediate effects, long-term consequences and
reversibility.
- Document severity assessments with supporting evidence. For
example, consider financial AI where incorrect investment
advice might have a moderate or major severity estimate for
impacted users, depending on the context. Include analysis of
varying stakeholder impacts.

## Resources

**Related documents:**

- [Learn
how to assess the risk of AI systems](https://aws.amazon.com/blogs/machine-learning/learn-how-to-assess-risk-of-ai-systems/)
- [NIST
Risk Management Framework](https://csrc.nist.gov/projects/risk-management/about-rmf)
- [ISO/IEC
42001:2023](https://www.iso.org/standard/42001) A.5.2 AI system impact assessment process

*Source: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raibr03-bp02.html*

---

# RAIBR03-BP03 Assign an overall risk level to each potential harm

Risk ratings are typically determined by using a risk matrix that
combines the likelihood (probability of occurrence) and severity
(degree of consequences) of the potential harmful events.

**Level of risk exposed if this best practice
is not established:** High

## Implementation considerations

- Create a consistent risk matrix or scoring system that
combines likelihood and severity ratings to produce overall
risk levels for each potential harm you've identified. Your
matrix should define clear categories for both dimensions. For
example, use a one to five scale for likelihood (unlikely to
likely) and severity (minimal to extreme impact), then
combining these to create overall risk ratings like low,
medium, high, or critical.
- Evaluate the likelihood of each potential harm by considering
factors like how often similar issues have occurred in
comparable systems, how robust your current mitigations are,
and what conditions would need to align for the harm to occur.
Be realistic about probabilities rather than assuming your
system will work perfectly, and consider both technical
failures and misuse scenarios.
- Assess the severity of each potential harm by thinking through
the full scope of consequences if it were to occur, including
immediate impacts on affected individuals, broader effects on
communities or society, and long-term damage to trust in AI
systems. Consider both direct harms and cascading effects that
might result.
- Apply your risk matrix consistently across the identified
harms to generate comparable risk ratings, and use the same
criteria and standards for each assessment. Document your
reasoning for each rating so others can understand and review
your risk evaluations and consider having multiple people
independently assess potential harms that you haven't
considered.
- Prioritize your risk mitigation efforts based on these overall
risk ratings, focusing first on the highest-risk harms while
also considering factors like mitigation cost and feasibility.
Use these risk levels to guide decisions about which harms
need immediate attention, which can be addressed in future
iterations, and what level of mitigation investment is
appropriate for each type of harm.

## Resources

**Related documents:**

- [Learn
how to assess the risk of AI systems](https://aws.amazon.com/blogs/machine-learning/learn-how-to-assess-risk-of-ai-systems/)
- [NIST
Risk Management Framework](https://csrc.nist.gov/projects/risk-management/about-rmf)
- [Responsible
AI in the generative era](https://www.amazon.science/blog/responsible-ai-in-the-generative-era)
- [ISO/IEC
42001:2023](https://www.iso.org/standard/42001) A.5.2 AI system impact assessment process

*Source: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raibr03-bp03.html*

---

# RAIBR03-BP04 Use a risk registry to track and calibrate potential harms and risks

Establish a risk registry to track and calibrate categories of risks
across your ML lifecycle and other use cases your team or
organization may be tackling. The registry includes information
about each identified risk, including the associated use case,
examples of harmful input and output pairs, affected stakeholders,
likelihood, severity, risk level, and high-level mitigation
approaches. Risk registry maintenance includes processes for keeping
risk information current and accurate as use cases and systems
evolve, new threats emerge, and responsible AI understanding
deepens.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation considerations

- Use a secure mechanism to capture each risk, with fields for
the associated use case, examples of harmful input and output
pairs, affected stakeholders, likelihood, severity, risk
level, and high-level mitigation approaches.
- Create workflows that link each risk in the registry to
development artifacts such as release criteria and technical
mitigation specifications, and track whether those fixes
worked. Record baseline measurements before mitigation,
implementation details, and follow-up measurements to see
which approaches work best for different risks.
- Periodically review registered risks to check if mitigations
are working and risk assessments were accurate. Compare actual
outcomes against predictions and update risk ratings when you
have new evidence about likelihood or severity.
- When starting a new use case, consult the risk registry to
speed and calibrate your risk assessments.

## Resources

**Related documents:**

- [ISO/IEC
42001:2023](https://www.iso.org/standard/42001) A.5.3 Documentation of AI system impact
assessments

*Source: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raibr03-bp04.html*

---
