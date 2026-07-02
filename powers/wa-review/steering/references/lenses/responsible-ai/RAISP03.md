# RAISP03 — Filtering

**Best Practices**: 4

---

# RAISP03-BP01 Add privacy-preserving filters

Implement filtering mechanisms that automatically detect and remove
unwanted confidential and personal data from both inputs and
outputs. Design input sanitization processes that cleanse user
queries and system data of unwanted information before processing,
using both rule-based and machine learning approaches to identify
personal data. Implement output filtering that blocks the generation
or disclosure of confidential or personal information, including
techniques like anonymization that replace identifying details with
generic placeholders or synthetic alternatives.

**Level of risk exposed if this best
practice is not established:** High

## Implementation considerations

- Create a strategy for Identifying unwanted data including
personal information and domain-specific information that
should not be included in inputs or outputs, then implement
appropriate detection methods using tools like Amazon Bedrock
Guardrails for filtering inputs and outputs.
- Design and implement privacy filters for both inputs and
outputs, using meaningful placeholders for redacted
information and verifying proper encryption for data storage
and transmission.
- Design for unwanted data redaction across data touchpoints
including logs and evaluation reports, not just primary inputs
and outputs.

## Resources

**Related video:**

- [Amazon
Bedrock Guardrails: Implementing Custom Safeguards for
Responsible AI Applications](https://aws.amazon.com/awstv/watch/02103dd95d3/)
- [AWS re:Inforce 2025 - Privacy-first generative AI: Establishing
guardrails for compliance (COM224)](https://www.youtube.com/watch?v=GAjWNoxgkYY)

**Related tools:**

- [Remove
PII from conversations by using sensitive information
filters](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-sensitive-filters.html)

**Related documents:**

- [Differentially
Private Fair Learning](https://arxiv.org/abs/1812.02696)
- [Remove
PII from conversations by using sensitive information
filters](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-sensitive-filters.html)
- [Towards
Efficient Privacy-Preserving Machine Learning: A Systematic
Review from Protocol, Model, and System Perspectives](https://arxiv.org/pdf/2507.14519)
- [Training
curriculum on AI and data protection Fundamentals of Secure AI
Systems with Personal Data](https://www.edpb.europa.eu/system/files/2025-06/spe-training-on-ai-and-data-protection-technical_en.pdf)
- [AI
Privacy Risks & Mitigations - Large Language Models
(LLMs)](https://www.edpb.europa.eu/system/files/2025-04/ai-privacy-risks-and-mitigations-in-llms.pdf)
- [An
overview of implementing security and privacy in federated
learning](https://link.springer.com/article/10.1007/s10462-024-10846-8)
- [Understanding
Users' Security and Privacy Concerns and Attitudes Towards
Conversational AI Platforms](https://arxiv.org/html/2504.06552v1)
- [Clio:
Privacy-Preserving Insights into Real-World AI Use](https://arxiv.org/pdf/2506.07555)
- [Privacy
Preserving Machine Learning Model Personalization through
Federated Personalized Learning](https://arxiv.org/pdf/2505.01788)
- [Privacy-Preserving
AI: Techniques & Frameworks](https://dialzara.com/blog/privacy-preserving-ai-techniques-and-frameworks)
- [Data
Anonymisation Made Simple - 7 Methods & Best
Practices](https://spotintelligence.com/2025/03/06/data-anonymisation/)
- [A
Comprehensive Guide to Differential Privacy: From Theory to
User Expectations](https://arxiv.org/html/2509.03294v1)
- [ISO/IEC
42001:2023 A.6.1.2 Objectives for responsible development of
AI system](https://www.iso.org/standard/42001)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raisp03-bp01.html*

---

# RAISP03-BP02 Add security filters

Implement security safeguards that detect and block threats such as
prompt injections, roleplay jailbreaks, and other adversarial
inputs. Design input validation mechanisms that identify unwanted
prompts and suspicious query patterns before they can manipulate
system behavior or extract sensitive information. Implement
guardrails with content filtering capabilities designed to block the
generation of harmful outputs even when inputs successfully bypass
input protections.

**Level of risk exposed if this best
practice is not established:** High

## Implementation considerations

- Revisit your security analysis in RAIBR02-BP06 to understand
the scope of security issues, including chat interfaces,
knowledge bases, file systems and tools, considering the
entire system architecture and component interactions beyond
just user touchpoints.
- Design multi-layered security using input validation, content
filtering, and rate limiting, utilizing tools like Amazon
Bedrock Guardrails for unwanted prompt detection and Amazon Comprehend for input validation.
- Apply traditional security best practices like least privilege
access using AWS IAM roles and policies, while securing
infrastructure components and monitoring systems.
- Design your AI system with a zero-trust model, where no user
or device is trusted by default and verification is required
for every access attempt.
- Design for providing the right access level to users and
applications invoking AI features and related Resources. For
example, provide role-based access control (RBAC) and
attribute-based access control (ABAC) to assign permissions based on
user roles and context, granting access only to necessary functions
and data. Grant users and agents only the minimum permissions
necessary to perform their tasks.
- Design for encrypting sensitive data used in AI systems both
at rest (in storage) and in transit to block unauthorized
access.
- Design for sanitizing sensitive inputs coming in and going out
of AI system. Validate that system inputs conform to expected
formats.

## Resources

**Related documents:**

- [Detect
and filter harmful content by using Amazon Bedrock
Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html)
- [ISO/IEC
42001:2023 A.6.1.2 Objectives for responsible development of
AI system](https://www.iso.org/standard/42001)

**Related tools:**

- [Amazon
Bedrock Guardrails](https://aws.amazon.com/bedrock/guardrails/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raisp03-bp02.html*

---

# RAISP03-BP03 Implement output filtering to catch unsafe content before it reaches users

Build screening mechanisms that automatically review and filter your
system's outputs to catch potentially harmful content before users
see it, acting as a final safety check regardless of what your
system generates. This means implementing safety classifiers that
can identify toxic, harmful, or inappropriate content in real-time,
content filtering systems that block or modify unsafe outputs based
on your safety definitions, and automated screening processes that
evaluate each response against your safety criteria before delivery.

For example, if your release criteria include safety standards for
blocking harmful outputs, you might implement toxicity detection
models that score each response, build content filters that
automatically block responses containing harmful information, or
create screening systems that flag suspicious outputs for human
review before they reach users.

**Level of risk exposed if this best
practice is not established:** High

## Implementation considerations

- Based upon release criteria, identify types of potentially
harmful content, including adversarial inputs and categories
outside of your system's use case
- Map the types of potentially harmful content to available
content filters, such as those already built-in to safeguard
services. Additional safety concerns may require custom
safeguards, either through system prompting, fine tuning,
exact match word configuration, or non-AI solutions that
control critical access and permissions to resources.
- Configure or customize safety filters that can identify and
block potentially harmful content across multiple categories
such as violence, self-harm, illegal activities, and other
context-specific safety concerns.

## Resources

**Related documents:**

- [Amazon
Bedrock Guardrails enhances generative AI application safety
with new capabilities](https://aws.amazon.com/blogs/aws/amazon-bedrock-guardrails-enhances-generative-ai-application-safety-with-new-capabilities/)
- [Measuring
and Mitigating Toxicity in LLMs](https://github.com/aws-samples/measuring-and-mitigating-toxicity-in-llms?tab=readme-ov-file#measuring-and-mitigating-toxicity-in-llms)
- [Flag
harmful content using Amazon Comprehend toxicity
detection](https://aws.amazon.com/blogs/machine-learning/flag-harmful-content-using-amazon-comprehend-toxicity-detection/)
- [Thorn
and All Tech Is Human Forge Generative AI Principles with AI
Leaders to Enact Strong Child Safety Commitments](https://www.thorn.org/blog/generative-ai-principles/)
- [ISO/IEC
42001:2023 A.6.1.2 Objectives for responsible development of
AI system](https://www.iso.org/standard/42001)

**Related video:**

- [AWS re:Invent 2024 - Responsible AI: From theory to practice with
AWS (AIM210)](https://www.youtube.com/watch?v=SCXw2xuoF6o)
- [AWS re:Invent 2024 - Build an AI gateway for Amazon Bedrock with
AWS AppSync (FWM310)](https://www.youtube.com/watch?v=iW7OWwct-Ww)

**Related tools:**

- [Amazon
Bedrock Guardrails](https://aws.amazon.com/bedrock/guardrails/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raisp03-bp03.html*

---

# RAISP03-BP04 Implement output filtering to detect and block hallucinations

Build filtering mechanisms that automatically detect and block
factually incorrect outputs, hallucinations, and misleading
information before they reach users. These filters act as a final
check to catch inaccuracies that your core AI system might generate.
Use both automated reasoning checks and fact verification systems to
validate outputs against known facts and logical consistency before
delivery.

**Level of risk exposed if this best
practice is not established:** High

## Implementation considerations

- Identify the specific types of veracity issues your system
needs to filter based on your release criteria. Define what
counts as hallucinations, factual errors, and misleading
information for your use case.

For example, determine whether you need to catch mathematical
errors, fabricated citations, invented statistics, or false
historical claims.

- Design your filtering strategy by deciding which verification
methods to use and how they will work together. Plan whether
you need automated reasoning checks, external fact
verification, confidence scoring, or human review processes.
Create a filtering architecture that can handle your expected
output volume and response time requirements.
- Implement your filtering mechanisms starting with automated
reasoning checks that validate logical consistency,
mathematical accuracy, and basic factual relationships. Add
fact checking connections to reliable knowledge sources and
databases. Build hallucination detection systems that can
identify fabricated information patterns your system commonly
generates.
- Test your complete filtering system using known examples of
your system's typical errors and hallucinations. Measure how
effectively your filters catch different types of inaccuracies
without blocking too many accurate outputs. Adjust detection
thresholds and add new filtering rules based on what you
discover during testing.

## Resources

**Related tools:**

- [Improve
accuracy by adding Automated Reasoning checks in Amazon
Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-automated-reasoning-checks.html)
- [Amazon
Bedrock: Knowledge Bases](https://aws.amazon.com/bedrock/knowledge-bases/)
- [Amazon Comprehend Features](https://aws.amazon.com/comprehend/features/)
- [Amazon Kendra](https://aws.amazon.com/kendra/)
- [Amazon
Bedrock Evaluations](https://aws.amazon.com/bedrock/evaluations/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raisp03-bp04.html*

---
