# RAIGT01 — Guiding

**Best Practices**: 5

---

# RAIGT01-BP01 Develop a transparency strategy

For each identified stakeholder group, choose a transparency
strategy (for example, blog post, user guide, FAQs, system
documentation, service card) and identify appropriate distribution
channels to provide downstream stakeholders information to make
informed decisions about the AI system.

**Level of risk exposed if this best
practice is not established:** High

## Implementation considerations

- Build a transparency format selection process that matches
each stakeholder group's needs and technical capabilities with
appropriate communication methods like secure portals, public
documentation, or interactive guides. Test different formats
with sample stakeholders to see which ones are effective in
assisting them to make better decisions about using your AI
system.
- Identify how to reach each stakeholder group effectively,
whether through existing professional networks, reporting
systems, or direct user interfaces. Set up pilot channels to
test delivery effectiveness before rolling out to
stakeholders.
- Create content development workflows that produce
stakeholder-specific information covering system capabilities,
limitations, risks, and decision-making guidance tailored to
each group's expertise level. Build templates and review
processes to keep information consistent while allowing
customization for different audiences.
- Build automated update systems that track when your AI system
changes and trigger content revisions across different
distribution channels to keep stakeholder information current.
Set up monitoring to catch when outdated information is still
circulating and create processes to quickly correct or
redirect stakeholders to updated materials.
- Engage your organization's leadership to determine public
disclosure requirements by identifying information appropriate
for public sharing versus proprietary details restricted to
internal audiences. Implement a structured publication review
and approval process for AI system documentation. This
mechanism safeguards sensitive AI design and performance
information while maintaining appropriate transparency to
different stakeholder groups.

## Resources

**Related documents:**

- [ISO/IEC
42001:2023 A.8.2 System documentation and information for
users](https://www.iso.org/standard/42001)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raigt01-bp01.html*

---

# RAIGT01-BP02 Create a system card that communicates intended usage and limitations

AI system cards are a form of responsible AI documentation that
provide stakeholders with a single place to find information on the
intended use cases and limitations, responsible AI design choices,
and deployment and performance optimization best practices. System
cards do not provide guidance on expected performance of the AI
system on the specific inputs the deployer may provide; that testing
is the responsibility of the deployer.

**Level of risk exposed if this best
practice is not established:** High

## Implementation considerations

- Identify intended use case(s) to illustrate how users should
plan to interact with your system. The use case section gives
the reader a tangible example, describing the steps and
workflow required end-to-end while calling out limitations in
the technology.
- Plan a specific set of evaluations for the AI service card. As
appropriate, disclose the datasets chosen for the evaluations
and how they meet the criteria to support the testing of each
Responsible AI dimension. For example, datasets should have
appropriate demographic labels for fairness testing, a
representative sample of examples from known safety
categories, and common as well as uncommon variations in the
input examples for robustness testing.
- Include performance metrics and success criteria for each use
case, with real-world examples demonstrating proper
implementation.
- Detail system limitations and constraints. Consider financial
risk assessment AI where specific market conditions or
transaction types might fall outside system capabilities.
Document scenarios where system performance may degrade or
become unreliable, including environmental factors affecting
behavior.
- Outline potential failure modes and implementation strategies
when appropriate. As an example, describe how a recommendation
system might fail during high-traffic periods or with novel
user patterns, and provide recommended responses. Include
warning signs and blocking strategies for each failure mode.

## Resources

**Related documents:**

- [Introducing
AWS AI Service Cards: A new resource to enhance transparency
and advance responsible AI](https://aws.amazon.com/blogs/machine-learning/introducing-aws-ai-service-cards-a-new-resource-to-enhance-transparency-and-advance-responsible-ai/)
- [Resources
that promote AI transparency](https://aws.amazon.com/ai/responsible-ai/resources/)
- [Amazon SageMaker AI model cards](https://docs.aws.amazon.com/sagemaker/latest/dg/model-cards.html)
- [Model
cards for model reporting](https://arxiv.org/abs/1810.03993)
- [Model
Registration Deployment with Model Registry](https://docs.aws.amazon.com/sagemaker/latest/dg/model-registry.html)
- [Transform
responsible AI from theory into practice](https://aws.amazon.com/ai/responsible-ai/)
- [Securing
generative AI: data, compliance, and privacy
considerations](https://aws.amazon.com/blogs/security/securing-generative-ai-data-compliance-and-privacy-considerations/)
- [Thorn
and All Tech Is Human Forge Generative AI Principles with AI
Leaders to Enact Strong Child Safety Commitments](https://www.thorn.org/blog/generative-ai-principles/)
- [ISO/IEC
42001:2023 A.8.2 System documentation and information for
users](https://www.iso.org/standard/42001)
- [ISO/IEC
42001:2023 A.8.3 External Reporting](https://www.iso.org/standard/42001)
- [ISO/IEC
42001:2023 A.8.5 Information for interested parties](https://www.iso.org/standard/42001)

**Related tools:**

- [Amazon SageMaker AI Model Cards](https://docs.aws.amazon.com/sagemaker/latest/dg/model-cards.html)
- [Amazon SageMaker AI AI](https://docs.aws.amazon.com/sagemaker/latest/dg/model-cards-create.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raigt01-bp02.html*

---

# RAIGT01-BP03 Create a plan for publishing and updating documentation

Identify which documents require updates based on stakeholder
feedback, new use-cases, new system releases, and industry best
practice developments. Dedicate an owner to facilitate the change
management process which supports plans for review cycles, document
and system versioning and approval chains.

**Level of risk exposed if this best
practice is not established:** Medium

## Implementation considerations

- Establish documentation management infrastructure. Define the
criteria for mandatory updates and create automated triggers
(AWS EventBridge, Amazon SNS) based on system updates and
stakeholder feedback. Assign ownership and responsibility for
making the updates. Maintain document version history.
- Establish and follow a review process. Set up an approval
chain and create approval workflows. Check the contents for
completeness, clarity, and technical accuracy.
- Publish the updates and make them accessible to the
stakeholders. Have a communication plan. Optionally set up an
automated system to notify stakeholders of document updates.

## Resources

**Related documents:**

- [ISO/IEC
42001:2023](https://www.iso.org/standard/42001) A.8.2 System documentation and information
for users

**Related tools:**

- [AWS Step Functions](https://aws.amazon.com/step-functions/)
- [AWS EventBridge](https://aws.amazon.com/eventbridge/)
- [Amazon Simple Notification Service](https://aws.amazon.com/sns/)
- [Serverless
Computing - AWS Lambda](https://aws.amazon.com/pm/lambda/)
- [Cloud
Object Storage - Amazon S3](https://aws.amazon.com/pm/serv-s3/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raigt01-bp03.html*

---

# RAIGT01-BP04 Guide users on how to understand system outputs

Provide accessible guidance on how a user should interpret system
outputs. Provide guidance on features the user can use to better
understand why a particular input might have produced a specific
output. This includes features such as confidence scores, feature
importance indicators, decision paths, or chains of thought. Tailor
the complexity and format of the guidance to match user expertise
levels, providing both high-level summaries and detailed technical
information as appropriate. Assist users to identify when to trust
system outputs, when to seek additional verification, and when to
override or ignore system recommendations based on their domain
knowledge.

**Level of risk exposed if this best
practice is not established:** Medium

## Implementation considerations

- Provide guidance on assisting users to understand how the
decisions were made for predicting certain outcome. This
includes showing which factors were most influential (feature
importance) and how certain the system is about its decision
(confidence scores). For traditional ML models, Amazon SageMaker AI Canvas provides visual explanations showing these
key factors and confidence levels. For example, a loan
approval system would display the main factors affecting the
decision with their relative importance, how confident the
system is in its prediction (expressed as a percentage),
historical patterns that influenced the decision and data
quality indicators supporting the prediction.
- For generative AI systems and agents, consider looking at
chain of thought techniques that provide the step-by-step
thinking process, use observability features like from Amazon
Bedrock Cloud Watch integrations to understand traces
collected from agents execution that provides visibility to
how tools for the agent was selected to be invoked that
allowed agents to act. Amazon Bedrock Agents and AgentCore
provide detailed traces showing how the system reached its
conclusion. For example, a customer service agent would show
the sequence of steps taken to resolve a query, which
knowledge sources or tools were consulted, why specific
approaches were chosen and what alternative options that were
considered
- When possible, provide ways to the users of AI system to
understand when to rely on system outputs and when to seek
additional verification. Implement monitoring, for example,
use AWS AgentCore observability features to trace reliability.
For instance, an AI-powered diagnostic system would set clear
thresholds for automatic approval versus human review based
upon tool invoked and other criteria's, show confidence levels
with simple-to-understand indicators, provide specific
criteria for when to seek expert verification

## Resources

**Related documents:**

- [ISO/IEC
42001:2023 A.8.2 System documentation and information for
users](https://www.iso.org/standard/42001)

**Related tools:**

- [Amazon SageMaker AI Clarify](https://aws.amazon.com/sagemaker/ai/clarify/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
- [AWS Step Functions](https://aws.amazon.com/step-functions/)
- [AWS EventBridge](https://aws.amazon.com/eventbridge/)
- [Amazon Simple Notification Service](https://aws.amazon.com/pm/sns/)
- [Observe
your agent applications on Amazon Bedrock AgentCore
Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raigt01-bp04.html*

---

# RAIGT01-BP06 Guide users on how to responsibly change system behavior

Provide guidance that informs users how to effectively alter system
behaviors and interpret results. Include user interface elements
that guide users toward productive interactions while steering them
away from approaches likely to produce poor or harmful results.
Explain response mechanisms that provide real-time feedback on input
quality and suggest improvements when user inputs are unclear,
inappropriate, or likely to produce unsatisfactory results. Direct
users to available education resources that assists users to
understand system capabilities and limitations, enabling them to
leverage the system effectively while maintaining realistic
expectations about its performance.

**Level of risk exposed if this best
practice is not established:** Medium

## Implementation considerations

- Create clear guidance materials that explain how users can
adjust system settings or modify their inputs to get different
types of outputs from your AI system. Test these instructions
with real users to see if they can follow them and achieve the
results they want without accidentally causing problems.
- Build educational resources that assist users to understand
what your system can and can't do, including interactive
tutorials, capability demonstrations, and examples of common
mistakes for control modifications. Test these materials with
different user groups to make sure people walk away with
realistic expectations about system performance and clear
ideas about how to use it effectively.
- Create feedback collection systems that let users report when
the guidance isn't working or when they discover better
approaches than what you've documented. Use this input to
continuously improve your user guidance and update your
educational materials based on what real users need to know.
For example, feedback may indicate commonly used parameter
combinations, or unsafe parameter settings that users may be
trying, you can use this information to improve the
educational material for these topics to guide users on
effective controllability of the AI system.

## Resources

**Related documents:**

- [ISO/IEC
42001:2023 A.8.2 System documentation and information for
users](https://www.iso.org/standard/42001)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raigt01-bp06.html*

---
