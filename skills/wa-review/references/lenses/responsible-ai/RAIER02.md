# RAIER02 — Aggregate results

**Best Practices**: 2

---

# RAIER02-BP01 Add statistical confidence to your release decision

Move beyond simple averages and point estimates to understand how
confident you can be that your system will meet its release
criteria when deployed. Instead of just asking did we hit our
target threshold, ask how confident are we that we'll consistently
hit this threshold given the uncertainty in our test results? Use
appropriate statistical methods to account for the limited data
you have and the variation you expect to see in real-world
performance. When you have multiple release criteria, adjust your
analysis to account for the fact that meeting the criteria
simultaneously is harder than meeting each one individually. This
approach may provide a clear, data-driven answer to whether you're
ready to release, rather than making that decision based on
potentially misleading averages that don't account for
uncertainty.

**Level of risk exposed if this best
practice is not established:** High

## Implementation considerations

- Choose appropriate statistical methods to make inferences
about your target population based on your sample. For
example, use a t or normal distribution for continuous
metrics. For ordinal metrics (for example, LLM as a Judge),
use non-parametric approaches.
- To calculate the confidence of meeting a minimum threshold,
you can use a Cumulative Distribution Function (CDF), while
for a maximum threshold, you would use the Survival Function
(SF). For ordinal data, non-parametric approaches like
bootstrapping can be used to empirically derive these values
by repeatedly resampling from your observed data to create a
full distribution of a summary statistic, such as the median.
From this empirical distribution, you can directly calculate
the proportion of outcomes that fall below or above a specific
threshold.
- Adjust confidence thresholds when evaluating multiple criteria
together. Apply corrections like Bonferroni to address
compounding uncertainty from multiple criteria. Document
methodology and provide clear pass/fail decisions.

## Resources

**Related documents**

- [ISO/IEC
42001:2023 A.6.2.4 AI system verification and
validation](https://www.iso.org/standard/42001)

**Related tools:**

- [Python
SciPy Stats](https://docs.scipy.org/doc/scipy/reference/stats.html)
- [Python
Numpy](https://numpy.org/doc/stable/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raier02-bp01.html*

---

# RAIER02-BP02 Summarize critical information and review with appropriate internal stakeholders

Organize evidence from your use case, risk assessments, release
criteria testing, datasets, and system design evidence into a single
document/source of truth that contains the information needed to
make a release decision. Include verification that appropriate
mitigations are in place for risks across relevant responsible AI
dimensions. Update the system registry with the go/no-go decision.

**Level of risk exposed if this best
practice is not established:** High

## Implementation considerations

- Pull together your release documentation into one package that
includes your use case definition, risk assessment results,
how you did on your release criteria tests, dataset quality
reports, and system design details. Organize everything into a
single source of truth that gives decision-makers the
information they need to make an informed choice about
releasing your system.
- Check that you've addressed risks across responsible AI areas
including safety, fairness, privacy, security, robustness,
veracity, explainability, transparency, controllability, and
governance. Document what mitigations you put in place and
make sure they tackle the specific risks you identified
earlier in your process.
- Calculate a single readiness score that combines your
confidence in meeting the release criteria. Start with your
statistical confidence that the quantitative criteria will
pass (using methods from PG-SC03-BP03). This gives you one
clear number that shows overall system readiness for release.
- Write an executive summary that hits the highlights including
your key findings, whether you passed or failed each release
criterion, what risks are still left after your mitigations,
and a clear recommendation about whether you should go ahead
with the release. Back up your recommendation with reasoning
that stakeholders can understand.
- Set up review meetings with internal teams like your legal
experts, technical leads, risk management teams,
compliance-aligned teams and business owners. Walk them
through your findings and get their input on whether you're
ready to release, since they might catch issues you missed or
have concerns you have not considered.
- Write down your final release decision and update your system
registry with whether it's a go or no-go, why you made that
decision, who signed off on it, and conditions or monitoring
requirements you'll need to follow after release.

## Resources

**Related documents**

- [Machine
Learning Lens for the AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/welcome.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raier02-bp02.html*

---
