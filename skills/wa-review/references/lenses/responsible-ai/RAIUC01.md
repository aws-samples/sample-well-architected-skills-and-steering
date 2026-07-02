# RAIUC01 — Define your specific problem

**Best Practices**: 2

---

# RAIUC01-BP01 Clarify the business problem

Describe the specific problem or business challenge. Assess how
frequently the challenge occurs, where it occurs, and its concrete
impacts. Describe the specific benefit of solving the challenge for
the primary user for your use case.

**Level of risk exposed if this best practice
is not established:** High

## Implementation considerations

- Collect quantitative and qualitative data on the problem's
frequency, impact, and specific scenarios from primary users
and other sources.
- Define clear boundaries for the problem scope, including
domain, geographic, and user segment limitations.
- Evaluate the urgency by quantifying inaction costs and
quantifying potential benefits of solving the problem.
- Draft a structured problem statement using a format such as
"Enable to
given input when every
with ".
- Validate the problem statement with key stakeholders, confirm
its current relevance, and refine based on feedback.

## Resources

**Related documents:**

- [ISO/IEC 42001:2023](https://www.iso.org/standard/42001) A.9.3 Objectives for responsible use of AI
system
- [ISO/IEC 42001:2023](https://www.iso.org/standard/42001) A.6.2.2 AI system requirements and
specification
- [NIST Artificial Intelligence Risk Management Framework (NIST AI
100-1)](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf): MAP1.1, MAP1.3, MAP1.4

*Source: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raiuc01-bp01.html*

---

# RAIUC01-BP02 Verify that AI is required to solve the problem

Before committing to using AI, evaluate whether traditional software
approaches or even manual processes could meet your requirements.
Choose AI if it provides clear, substantial benefits over competing
solutions, and not simply because it is technically possible to
apply AI to the problem.

**Level of risk exposed if this best practice
is not established:** High

## Implementation considerations

- Consider whether you can solve the problem by writing down a
clear and compact set of rules. It is generally infeasible,
for example, to write down a compact set of pixel-comparison
rules to decide if two arbitrary face images represent the
same person. However, it is feasible to write down a brief set
of rules to decide if two images are identical. If yes, you
may be able to use a solution other than machine learning, and
you may not need this best practice guidance.
- Consider whether you can access reliable sources of training,
fine-tuning, and test examples. If it is difficult to
access such examples, you may not have the data necessary to
develop or evaluate an AI, and may need to consider either
reframing the use case or alternate solutions.
- Consider alternative reformulations of the use case that might
be solved by rule-based systems, traditional information
retrieval systems, or other software solutions.

## Resources

**Related documents:**

- [Responsible
AI Practices](https://aws.amazon.com/machine-learning/responsible-ai/)
- [ISO/IEC
42001:2023](https://www.iso.org/standard/42001) A.9.2 Process for responsible use of AI
systems
- [NIST
Artificial Intelligence Risk Management Framework (NIST AI
100-1)](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf): MAP1.1, MAP1.6, MAP2.1

*Source: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raiuc01-bp02.html*

---
