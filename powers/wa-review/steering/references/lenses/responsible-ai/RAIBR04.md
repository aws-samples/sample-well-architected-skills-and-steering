# RAIBR04 — Mitigate risks

**Best Practices**: 3

---

# RAIBR04-BP01 Narrow the use case

Identify the minimum viable use case that still delivers meaningful
business value while reducing complexity and associated risks.
Narrow the use case to a specific domain, industry vertical,
geography, or user segment rather than attempting to solve broad,
general problems. Restrict the types of inputs your system accepts
and the formats of outputs it generates.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation considerations

- Evaluate current scope and identify risk reduction
opportunities. For example, an AI medical diagnosis system
might focus on a specific condition type rather than general
diagnostics or limit analysis to structured lab results rather
than free-text notes.
- Define specific boundaries for system application. As an
example, a financial AI advisor might serve only retail
investors within certain portfolio sizes, using standardized
investment products rather than complex instruments. Consider
expertise requirements.
- Document input and output restrictions to control risk
exposure. Consider a customer service AI that accepts only
structured inputs rather than free-text queries, which
improves response reliability. Include clear guidance on
system limitations and context for appropriate use.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raibr04-bp01.html*

---

# RAIBR04-BP02 Weigh trade-offs across competing use case objectives

Evaluate and balance trade-offs between benefits and risks. If not
already available from your organization, develop explicit trade-off
criteria (like tenets) that reflect organizational policies and
stakeholder needs.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation considerations

- Review objectives, benefits, and risks across relevant
responsible AI dimensions and stakeholders to identify
potential conflicts.
- Analyze conflicts between different to prioritize their
importance. For example, a diagnostic health care use case
might trade off overall accuracy against full coverage of
disease types, or a financial fraud detection use case might
trade off a higher false positive rate against a faster
response time.

## Resources

**Related documents:**

- [Responsible
AI: From Principles to Production](https://aws.amazon.com/blogs/enterprise-strategy/responsible-ai-from-principles-to-production/)
- [Resolving
Ethics Trade-offs in Implementing Responsible AI](https://arxiv.org/html/2401.08103v3)

**Related videos**

- [AWS re:Invent 2024 - Responsible AI: From theory to practice with
AWS (AIM210)](https://www.youtube.com/watch?v=SCXw2xuoF6o)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raibr04-bp02.html*

---

# RAIBR04-BP03 Assign your potential harm mitigations to implementation strategies

As input to your system design, consider whether potential harms can
be addressed through technical features or stakeholder guidance.

**Level of risk exposed if this best practice
is not established:** High

## Implementation considerations

- Categorize your mitigations into implementation strategies
that are either built into the system (a part of the core AI
system or resolved with filtering of inputs and outputs) or
addressed through guidance. For example, a healthcare chatbot
might reduce the risk of incorrectly responding to requests
for legal advice by either customizing the underlying model or
guardrails, or by warning users not to request legal advice,
or both.

## Resources

**Related documents:**

- [Learn
how to assess the risk of AI systems](https://aws.amazon.com/blogs/machine-learning/learn-how-to-assess-risk-of-ai-systems/)
- [Responsible
AI in the generative era](https://www.amazon.science/blog/responsible-ai-in-the-generative-era)
- [NIST
Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raibr04-bp03.html*

---
