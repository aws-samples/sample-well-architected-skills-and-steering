# RAISP02 — AI system baking

**Best Practices**: 10

---

# RAISP02-BP01 Design the core AI system to directly address your release criteria

Build your system with your release criteria in mind from the
beginning, choosing components and designing processes that directly
support the performance targets you need to hit. Think of your
release criteria as the blueprint for your system design where every
design decision should move you closer to meeting those specific
goals. Set up regular check-ins during development to see how you
are tracking against your targets and be ready to adjust your
approach if you spot gaps early. Make sure your candidate testing
and validation closely mirror the way you will measure success at
release time, so there are no surprises when it is time to release.
This approach assists you to build exactly what you need to pass
your release criteria, rather than creating a system that performs
well on general metrics but falls short on the specific measures
that matter for your use case.

**Level of risk exposed if this best
practice is not established:** High

## Implementation considerations

- Define alignment goals that support the release criteria.
- Define the architecture of the AI system to enhance alignment
with release criteria (including determining which methods
will be used to address criteria in model training, setting
bounds on free parameters, putting in place uncertainty
estimation and output validation procedures).
- Develop training protocol with safety checkpoints and consider
techniques like fine-tuning and constitutional training.
- Establish a validation framework, including safety-focused
testing, alignment validation, adversarial and stress testing
and integration tests that mirror how the success of the AI
system will be measured once it is released.

## Resources

**Related documents:**

- [Retrieve
Anything To Augment Large Language Models](https://arxiv.org/abs/2310.07554)
- [Constitutional
AI: Harmlessness from AI Feedback](https://arxiv.org/abs/2212.08073)
- [ISO/IEC
42001:2023 Information technology — Artificial intelligence —
Management system](https://www.iso.org/standard/42001)

**Related tools:**

- [Customize
models in Amazon Bedrock with your own data using fine-tuning
and continued pre-training](https://aws.amazon.com/blogs/aws/customize-models-in-amazon-bedrock-with-your-own-data-using-fine-tuning-and-continued-pre-training/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raisp02-bp01.html*

---

# RAISP02-BP02 Privacy: Build privacy-preserving mechanisms into the core AI system

Design your system from the start to protect confidential and
personal data. This may include incorporating techniques like data
encryption, access controls, data minimization, data obfuscation,
and privacy-preserving training methods directly into how your
system works, based on your release criteria.

For example, if your release criteria include keeping certain types
of user information confidential, you might build in automatic data
masking, use techniques that scramble sensitive information while
keeping it useful for training, or set up your system to process
information without storing sensitive details. The specific privacy
mechanisms you choose should align with your release criteria.

**Level of risk exposed if this best
practice is not established:** High

## Implementation considerations

- Implement data protection measures: Establish security
protections around sensitive information. First, identify
essential data requirements through data minimization
analysis. Create a mapping of sensitive fields and implement
anonymization. For example, in a healthcare system, converting
'John Doe, diabetic, 123 Main Street' to 'Patient_2384,
condition_type_2, region_14' maintains analytical value while
protecting individual privacy. Encrypt sensitive data at rest
and in transit. Establish role-based access controls with
documented access levels for sensitive data.
- Apply privacy-preserving training techniques: Consider using
differential privacy techniques to introduce controlled noise
to the training process. For example, when processing customer
transaction data, apply calculated variations to individual
purchases while maintaining accurate aggregate patterns.
Consider using federated learning to enable distributed model
training where data remains at source locations.

For example, with federated learning, healthcare institutions
can improve diagnostic models by sharing only parameter updates
instead of raw patient data. Consider using gradient clipping to
block individual training examples from disproportionately
influencing model learning, maintaining both privacy and model
quality.

## Resources

**Related documents:**

- [Differentially
Private Fair Learning](https://arxiv.org/abs/1812.02696)
- [Remove
PII from conversations by using sensitive information
filters](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-sensitive-filters.html)
- [ISO/IEC
42001:2023 A.6.1.2 Objectives for responsible development of
AI system](https://www.iso.org/standard/42001)

**Related video:**

- [Amazon
Bedrock Guardrails: Implementing Custom Safeguards for
Responsible AI Applications](https://aws.amazon.com/awstv/watch/02103dd95d3/)
- [AWS re:Inforce 2025 - Privacy-first generative AI: Establishing
guardrails for compliance (COM224)](https://www.youtube.com/watch?v=GAjWNoxgkYY)

**Related tools:**

- [Amazon
Bedrock Guardrails and PII removal](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-sensitive-filters.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raisp02-bp02.html*

---

# RAISP02-BP03 Mitigate unwanted bias directly in the core AI system design

Consider incorporating fairness mitigations such as sampling and
optimization methods during training, alignment and calibration
techniques that actively mitigate biased system responses, and
post-processing strategies that review and adjust outputs before
they reach users. The specific fairness strategies you use should
directly support the fairness goals in your release criteria.

**Level of risk exposed if this best
practice is not established:** High

## Implementation considerations

- Use sampling-based methods during training to improve model
performance on underrepresented groups. Apply techniques like
weighted sampling to give more importance to underrepresented
examples, oversampling to create more training instances from
minority groups, or stratified sampling to achieve balanced
representation. Consider error-based weighted sampling where
you identify groups that experience higher error rates on a
validation set and sample datapoints from those groups at
higher rates during training. These methods assist your model
learn better patterns for each group instead of just the
majority.
- Consider using fairness metrics within the model loss function
to guide model training to penalize unfair outputs.
- Consider if demographic features or proxy features factor
significantly into the model predictions by analyzing feature
attributions for indications of a biased model. Consider using
Amazon SageMaker AI Clarify for feature attributions and bias
detection.

## Resources

**Related documents:**

- [Amazon
AI Fairness and Explainability Whitepaper](https://pages.awscloud.com/rs/112-TZM-766/images/Amazon.AI.Fairness.and.Explainability.Whitepaper.pdf)
- [Fairness,
model explainability and bias detection with SageMaker AI
Clarify](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-configure-processing-jobs.html)
- [Transform
responsible AI from theory into practice](https://aws.amazon.com/ai/responsible-ai/)
- [Automate
model retraining with Amazon SageMaker AI Pipelines when drift is
detected](https://aws.amazon.com/blogs/machine-learning/automate-model-retraining-with-amazon-sagemaker-pipelines-when-drift-is-detected/)
- [Accenture
Enterprise AI – Scaling Machine Learning and Deep Learning
Models](https://docs.aws.amazon.com/whitepapers/latest/accenture-ai-scaling-ml-and-deep-learning-models/monitoring-for-performance-and-bias.html)
- [Amazon SageMaker AI AI: Prepare ML Data with Amazon SageMaker AI Data
Wrangler](https://docs.aws.amazon.com/sagemaker/latest/dg/data-wrangler.html)
- [NIST
AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
- [ISO/IEC
42001:2023 Information technology — Artificial intelligence —
Management system](https://www.iso.org/standard/42001)

**Related tools:**

- [Amazon SageMaker AI Clarify](https://aws.amazon.com/sagemaker/ai/clarify/)
- [Fairlearn](https://fairlearn.org/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raisp02-bp03.html*

---

# RAISP02-BP04 Build security protections directly into the core AI system design

Follow "secure by design" and "defense in depth" principles and
build security protections into your system from the beginning to
protect your system and maintain its intended operation. This means
incorporating safeguards like access controls, input validation and
sanitization to defend against prompt injections, and robust
techniques to mitigate attempts at jailbreaking or bypassing your
system's safety guardrails. The specific security measures you
choose should directly address the security requirements in your
release criteria.

**Level of risk exposed if this best
practice is not established:** High

## Implementation considerations

- Build input validation into your model's core processing by
checking inputs for unwanted patterns, prompt injections, and
attempts to manipulate system behavior. Create filters that
detect and block unwanted patterns such as instruction
overrides, data extraction attempts, and jailbreaking prompts
before they reach your model.
- Design access controls directly into your system architecture
by requiring authentications for each interaction, limiting
what different user types can access, and restricting
administrative functions to authorized personnel only. Set up
role-based permissions that block unauthorized users from
accessing sensitive model capabilities or training data.
- Build adversarial robustness into your model by training it to
resist attempts to manipulate its outputs through crafted
inputs. Include adversarial examples in your training data and
design your model architecture to be stable when faced with
inputs designed to cause harmful or unexpected behavior.

## Resources

**Related documents:**

- [Detect
and filter harmful content by using Amazon Bedrock
Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html)
- [ISO/IEC
42001:2023 A.6.1.2 Objectives for responsible development of
AI system](https://www.iso.org/standard/42001)

**Related tools**

- [Amazon
Bedrock Guardrails](https://aws.amazon.com/bedrock/guardrails/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raisp02-bp04.html*

---

# RAISP02-BP05 Embed provenance indicators into core AI system outputs

Address release criteria for transparency by building provenance
indicators directly into your AI system. Providing machine readable
labels for audio and imagery outputs is one of the approaches.

**Level of risk exposed if this best
practice is not established:** High

## Implementation considerations

- Consider the necessity and utility of embedding
machine-readable labels into AI-generated content such as
images, audio, and video that clearly identifies the content
as AI-generated.
- Consider whether to create provenance chains that track the
details such as name of the AI system provider, name of the AI
system, time stamp of synthetic output generation, and unique
identifiers  so that users can trace how content was created
and modified. The level of detail provided should balance
verification value against data costs, security impacts, and
risks of disclosing proprietary system details.
- If your system outputs machine readable labels , provide
capabilities that let users check that content has originated
from your system. For example, Amazon Bedrock provides
customers with the capability to check if an image was
generated by Amazon Nova Canvas or Amazon Titan Image
Generator via a publicly available tool,
[Content
Credentials Verify](https://contentcredentials.org/verify).

## Resources

**Related documents:**

- [Considerations
for addressing the core dimensions of responsible AI for
Amazon Bedrock applications](https://aws.amazon.com/blogs/machine-learning/considerations-for-addressing-the-core-dimensions-of-responsible-ai-for-amazon-bedrock-applications/)
- [Evaluate
models or RAG systems using Amazon Bedrock Evaluations – Now
generally available](https://aws.amazon.com/blogs/machine-learning/evaluate-models-or-rag-systems-using-amazon-bedrock-evaluations-now-generally-available/)
- [Amazon
Titan Image Generator and watermark detection API are now
available in Amazon Bedrock](https://aws.amazon.com/blogs/aws/amazon-titan-image-generator-and-watermark-detection-api-are-now-available-in-amazon-bedrock/)
- [ISO/IEC
42001:2023 A.8.2 System documentation and information for
users](https://www.iso.org/standard/42001)
- [Thorn
and All Tech Is Human Forge Generative AI Principles with AI
Leaders to Enact Strong Child Safety Commitments](https://www.thorn.org/blog/generative-ai-principles/)

**Related videos:**

- [Amazon
Titan Image Generator Demo - Watermark Detection | Amazon Web Services](https://www.youtube.com/watch?v=M5Vqb3UoXtc)

**Related tools:**

- [Watermark
detection for Amazon Titan Image Generator now available in
Amazon Bedrock](https://aws.amazon.com/about-aws/whats-new/2024/04/watermark-detection-amazon-titan-image-generator-bedrock/)
- [Generating
images with Amazon Nova Canvas](https://docs.aws.amazon.com/nova/latest/userguide/image-generation.html)
- [Amazon
Nova – AWS AI Service Card](https://docs.aws.amazon.com/ai/responsible-ai/nova-canvas/overview.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raisp02-bp05.html*

---

# RAISP02-BP06 Enable users to customize core AI system behaviors

Design your system so users can adjust how it works to better fit
their particular requirements and preferences, while keeping those
adjustments within appropriate boundaries for your use case. This
means incorporating features like adjustable output styles, user
preference settings, or options that let users guide how the system
interprets and responds to their requests.

**Level of risk exposed if this best
practice is not established:** High

## Implementation considerations

- When adding guardrails to your system, build adjustable
controls that let users determine how strictly content gets
filtered. Set up multi-level filtering from low to high for
different content types and create user roles where
administrators set baseline policies while end users can
adjust settings within safe limits. Include feedback systems
to track how well these guardrail controls work and improve
them over time.
- Design interfaces for adjusting output content, style and
tone. Allow users to adjust inference parameters like
Temperature, Top P, and Top K for text generation to balance
between creative and focused outputs. These parameters control
the output by influencing the token selection process.
Temperature determines randomness of token selection, with
higher values producing more creative text and lower values
resulting in more focused output. Top P (Nucleus Sampling)
samples tokens whose cumulative probability sums to a given
threshold, dynamically adjusting the option pool. Top K
restricts the model's choice to a fixed number of
highest-probability tokens. Similarly, provide ways to the
user to adjust response length, format options, and output
style.
- Design structured prompting frameworks to enhance user control
over AI system behavior and outputs. Create system-level
prompt templates that allow administrators to define AI
personality, tone, and response boundaries, while enabling end
users to customize task-specific instructions within safe
limits. Build prompt libraries with preset configurations for
common use cases (for example, professional communication,
creative writing, technical analysis) that users can select
and modify. Include prompt validation mechanisms to assist
user-provided prompts align with safety guidelines while
maintaining the desired level of control over AI responses.
Design prompt management interfaces that assist users to
understand prompt effectiveness through clear feedback and
iterative refinement options.
- Design tracking mechanisms for control adjustments, system
responses, user interactions and performance impacts.
- Create feedback mechanisms that enable users to refine AI
behavior over time. This assists to maintain relevance and
reliability of the AI system based on user input and
preferences.
- Develop role-based customization options, allowing different
levels of AI feature access and customization based on user
roles and business requirements.

## Resources

**Related documents:**

- [Prompt
templates and examples for Amazon Bedrock text models](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-templates-and-examples.html)
- [Detect
and filter harmful content by using Amazon Bedrock
Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html)
- [Influence
response generation with inference parameters](https://docs.aws.amazon.com/bedrock/latest/userguide/inference-parameters.html)
- [ISO/IEC
42001:2023 Information technology — Artificial intelligence —
Management system](https://www.iso.org/standard/42001)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raisp02-bp06.html*

---

# RAISP02-BP07 Incorporate explainability mechanisms into the core AI system

Adding explainability to your AI system assists to address
explainability release criteria by verifying stakeholders can
understand and trust how decisions are made for your specific use
case. Include confidence scores with predictions to show how certain
the model is about its outputs, and for generative AI systems, use
techniques such as content attribution, and token probabilities to
explain what influenced the generated content. When explanations are
critical, use interpretable models like decision trees that are
simple to understand and when more complex models are required add
explanation tools (like LIME or SHAP) afterward to interpret their
decisions.

**Level of risk exposed if this best
practice is not established:** High

## Implementation considerations

- Build confidence scoring into your system's output pipeline so
users can see how certain your model is about each prediction.
Test different confidence calculation methods to find ones
that actually correlate with accuracy, since some approaches
give misleading confidence scores that don't assist users to
make better decisions.
- Choose interpretable model architectures, such as decision
trees or linear models when stakeholders need to understand
exactly how decisions are made. Compare the performance
trade-offs between interpretable and complex models for your
specific use case to see if the explanation benefits justify
accuracy costs.
- Add explanation tools like LIME or SHAP to complex models that
you can't make interpretable but still need to explain. Test
these tools with your actual users to make sure the
explanations are helpful rather than confusing, since some
explanation methods work better for different types of models
and use cases.
- For generative AI systems, build in techniques like
chain-of-thought prompting that show the reasoning process,
content attribution that traces outputs back to source
material, and token probability displays that reveal
uncertainty. Test these explanation methods to see which ones
assist users to understand and trust the generated content.
For example, each response from an Amazon Bedrock agent is
accompanied by a trace that details the steps being
orchestrated by the agent. The trace assists to follow the
agent's reasoning process that leads it to the response it
gives at that point in the conversation.
- Build automatic source attribution into your Retrieval
Augmented Generation (RAG) system by linking retrieved
information directly to its origin document with specific
citations, page numbers, and document identifiers. Display
these citations alongside generated content so users can
independently verify where information came from.

Create explanation validation processes that check whether your
explainability mechanisms are effective in assisting users make
better decisions about trusting or acting on your system's
outputs. Regularly test explanations with real users to catch
when explanation methods become misleading or stop being useful
as your system evolves.

## Resources

**Related documents:**

- [ISO/IEC
42001:2023 A.8.2 System documentation and information for
users](https://www.iso.org/standard/42001)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raisp02-bp07.html*

---

# RAISP02-BP08 Consider core AI system designs that improve factual accuracy

Design your system to produce more accurate information by
incorporating techniques that distinguish facts from speculation,
reduce hallucinations, and acknowledge uncertainty. This means
connecting to authoritative knowledge sources through retrieval
methods with source attribution (for example, RAG), employing
alignment approaches like constitutional training and reinforcement
learning from human feedback (RLHF) to block hallucinations, and
incorporating automated reasoning capabilities like chain of thought
reasoning for self-reflection along with uncertainty and confidence
measurements that assist the system to recognize when it is not
confident about information.

**Level of risk exposed if this best
practice is not established:** High

## Implementation considerations

- Design and implement knowledge grounding strategy using RAG
architecture or parametric knowledge, verifying clear version
control of knowledge bases and rigorous source validation
process.
- Create training objectives that explicitly reward factual
accuracy and penalize hallucinations, incorporating
self-critique methods and negative examples while using tools
like Constitutional AI or RLHF.
- Build uncertainty quantification into model behavior through
calibrated confidence scores and explicit knowledge
boundaries, training the system to acknowledge limitations
rather than generate plausible but unverified responses.
- Establish continuous feedback loops to identify and correct
factual errors, implementing regular validation cycles against
authoritative sources and domain-specific accuracy metrics.
- Use output validation to check that your system's responses
are accurate and relevant. This is used to detect when your
system makes up information by comparing responses against
trusted sources and using logical checks to verify facts are
correct. For example, Amazon Bedrock Guardrails provide
capabilities for detecting hallucinations in model responses
using contextual grounding checks. Automated Reasoning checks
in Amazon Bedrock Guardrails assists to block factual errors
from hallucinations using logically accurate and verifiable
reasoning that explains why responses are correct. Automated
Reasoning assists to mitigate hallucinations using sound
mathematical techniques to validate/correct, and logically
explain the information generated leading to outputs that
align with known facts and are not based on fabricated or
inconsistent data.

## Resources

**Related documents:**

- [Minimize
AI hallucinations and deliver up to 99% verification accuracy
with Automated Reasoning checks: Now available](https://aws.amazon.com/blogs/aws/minimize-ai-hallucinations-and-deliver-up-to-99-verification-accuracy-with-automated-reasoning-checks-now-available/)
- Build responsible AI applications with Amazon Bedrock
Guardrails
- [ISO/IEC
42001:2023 A.6.1.2 Objectives for responsible development of
AI system](https://www.iso.org/standard/42001)

**Related tools:**

- [Amazon
Bedrock Guardrails](https://aws.amazon.com/bedrock/guardrails/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raisp02-bp08.html*

---

# RAISP02-BP09 Design your core AI system to handle input variations

Design your system to be more resilient by building in the ability
to handle input variations and edge cases that could cause it to
fail or behave unpredictably. This means incorporating techniques
like data augmentation that creates variations of your training
examples, adversarial training that tests your system against
challenging inputs, and exposure to diverse input formats, styles,
and edge cases during the development process. The robustness
techniques you choose should directly support your release criteria,
assisting your system to perform consistently even when users
interact with it in unexpected ways.

**Level of risk exposed if this best
practice is not established:** High

## Implementation considerations

- Review your release criteria to identify expected input
variations and how your data might change in real use, from
variations like lighting changes in images to text typos or
paraphrasing.
- Create a data augmentation pipeline (automated system to
modify training data) that generates different versions of
your inputs. Use both simple transformations like rotations or
text swaps, and advanced generative methods to create diverse
examples.
- Include robustness techniques during training by adding
controlled noise (small random changes) to your data and using
optimization objectives that assist your model to learn to
ignore minor input differences.
- Design for continuous monitoring and updating to adapt the
system to new data, evolving environments, and unforeseen
issues, verifying its continued robustness.
- Refer to the Dataset Planning focus area for details on data
related best practices for designing robust AI system.

## Resources

**Related documents:**

- [Clarify
Semantic Robustness Evaluation](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-semantic-robustness-evaluation.html)
- [ISO/IEC
42001:2023 A.6.1.2 Objectives for responsible development of
AI system](https://www.iso.org/standard/42001)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raisp02-bp09.html*

---

# RAISP02-BP10 Build safety protections into the core AI system

Follow the safety-by-design principle and design your system from
the start to block harmful outputs and unsafe behaviors through
multiple layers of protection. Start by creating clear, objective
definitions of what constitutes safe versus unsafe behavior for your
specific use case, then incorporate safety training approaches like
model alignment techniques, constitutional training, and
reinforcement learning from human feedback (RLHF) that teach your
system to recognize and avoid harmful content while aligning with
human values and safety preferences, input sanitization techniques
that clean or modify problematic user requests before processing,
output alteration methods that modify or block unsafe responses
before they reach users, and guardrails that enforce safe
interaction boundaries throughout the system.

For example, if your release criteria include safety standards for
blocking harmful content, you might implement alignment methods to
align your model behavior with your safety criteria, use training
approaches that incorporate human feedback to reduce toxic output
generation, build input filtering that neutralizes harmful requests,
use output modification techniques that sanitize responses, or
create interaction limits that block unsafe usage patterns. The
safety techniques you choose should directly support your release
criteria, creating multiple protective layers that work together to
meet safety requirements in your release criteria.

**Level of risk exposed if this best
practice is not established:** High

## Implementation considerations

- Define specific safety boundaries for your use case by
creating clear examples of safe versus unsafe outputs that
match your release criteria. Test these definitions with
stakeholders to make sure your team agrees on what constitutes
harmful behavior, then use these examples to guide your other
safety work.
- Build safety training into your model development process
using techniques like constitutional AI training that teaches
your system to follow safety principles, or RLHF approaches
that incorporate human feedback about harmful content. Compare
different safety training methods to see which ones work best
for addressing the specific release criteria for your use
case.
- Create input sanitization filters that identify and modify
problematic user requests before they reach your model. Build
these filters to catch different types of harmful inputs like
requests for dangerous information, attempts to bypass safety
measures, or prompts designed to generate toxic content.
- Build interaction guardrails that limit how users can interact
with your system, like rate limits to block abuse,
conversation boundaries that redirect harmful discussions, or
session controls that detect and stop unsafe usage patterns.
Test your complete safety system with red teaming exercises to
find weaknesses and improve your protections before launch.

## Resources

**Related documents:**

- [Flag
harmful content using Amazon Comprehend toxicity
detection](https://aws.amazon.com/blogs/machine-learning/flag-harmful-content-using-amazon-comprehend-toxicity-detection/)
- [Thorn
and All Tech Is Human Forge Generative AI Principles with AI
Leaders to Enact Strong Child Safety Commitments](https://www.thorn.org/blog/generative-ai-principles/)
- [ISO/IEC
42001:2023 A.6.1.2 Objectives for responsible development of
AI system](https://www.iso.org/standard/42001)

**Related tools:**

- [Amazon
Bedrock Guardrails](https://aws.amazon.com/bedrock/guardrails/)

**Related videos:**

- [AWS re:Invent 2024 - Build an AI gateway for Amazon Bedrock with
AWS AppSync (FWM310)](https://www.youtube.com/watch?v=iW7OWwct-Ww)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raisp02-bp10.html*

---
