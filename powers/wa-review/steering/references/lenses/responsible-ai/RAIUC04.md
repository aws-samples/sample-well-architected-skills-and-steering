# RAIUC04 — AI workflow impact

**Best Practices**: 3

---

# RAIUC04-BP01 Map the user journey to identify AI interaction requirements

Map the user journey to identify interaction requirements and risks.
During pre-interaction, assist users in learning about the system's
capabilities and limitations.

During the initial interaction, consider the different accessibility
needs of users, and the different sources for key system inputs.

During processing, maintain transparency about AI decision-making
and provide appropriate progress indicators. Post-interaction,
enable users to understand, challenge, and provide feedback on AI
outputs, which keeps the system accountable and improvable.

Consider how different user groups might be affected differently at
each stage and implement appropriate safeguards and support
mechanisms. If the AI system will be embedded in an existing
human-powered workflow, consider what purposes the workflow might
address that the AI system does not, and consider the variety of
ways in which users might modify system inputs and outputs for other
purposes.

**Level of risk exposed if this best practice
is not established:** High

## Implementation considerations

- Identify the expectations users may have and the information
they need before engaging with the proposed AI system.
- Sketch the initial interaction phase. Identify the first
touchpoints where users provide input and the guidance they
need for effective interaction. Consider how users might alter
inputs to influence outputs.
- Sketch the AI processing phase. Consider how long processing
takes, what users see during processing, and what information
assists users to understand system activity and confidence
levels.
- Sketch the post-interaction phase. Plan how users receive,
interpret, and act on AI outputs, including confidence
indicators, explanation features, and guidance for appropriate
use of results. Consider the purposes which the outputs might
serve.
- Identify transparency touch points. Mark specific moments in
each phase where guidance is most valuable.

## Resources

**Related documents:**

- [ISO/IEC
42001:2023](https://www.iso.org/standard/42001) - User interaction lifecycle implementation
- [ISO/IEC
42001:2023](https://www.iso.org/standard/42001) A.5.4 Assessing AI system impact on
individuals or groups of individuals
- [NIST
Artificial Intelligence Risk Management Framework: Generative
Artificial Intelligence Profile (NIST AI 600-1)](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf):
- [NIST
Artificial Intelligence Risk Management Framework (NIST AI
100-1)](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf): MAP2.1, MAP2.2, MAP2.3

*Source: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raiuc04-bp01.html*

---

# RAIUC04-BP02 Identify human oversight opportunities

Place human review at points where the quality of system inputs or
outputs can be harder to judge. Consider moments where human
expertise adds unique value or assists with consequential decisions.

**Level of risk exposed if this best practice
is not established:** High

## Implementation considerations

- Review the user journey to find moments where errors could
have significant consequences, or where human expertise is
uniquely valuable. Create user interface elements and
workflows that make human oversight natural and efficient,
providing the right information at the right time for
effective decision-making.
- Identify requirements to assist human reviewers, such as
system output explanations and contributing factors,
confidence scores, similar case examples, and other
information needed for informed oversight decisions.

## Resources

**Related documents:**

- [ISO/IEC
42001:2023](https://www.iso.org/standard/42001) A.6.2.6 AI system operation and monitoring

*Source: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raiuc04-bp02.html*

---

# RAIUC04-BP03 Identify accessibility requirements for different user groups

Identifying accessibility points assists to generate requirements
for people with different capabilities and disabilities to use the
proposed AI system effectively.

**Level of risk exposed if this best practice
is not established:** High

## Implementation considerations

- Conduct accessibility needs assessment. Research the specific
accessibility challenges faced when interacting with AI
systems, including cognitive, visual, auditory, speech,
sensory, and motor accessibility needs. You may explore
research published in the
[ACM
CHI: Conference on Human Factors in Computing Systems](https://dl.acm.org/doi/proceedings/10.1145/3706598),
or consider reading more from articles published from Amazon:
[Use
AWS AI and ML services to foster accessibility and inclusion
of people with a visual or communication disability](https://aws.amazon.com/blogs/machine-learning/use-aws-ai-and-ml-services-to-foster-accessibility-and-inclusion-of-people-with-a-visual-or-communication-disability/) or
[12
ways Amazon is making products more accessible for customers
with disabilities](https://www.aboutamazon.com/news/devices/amazon-accessibility-features).
- Map out multimodal interactions. Provide multiple ways for
users to input information and receive AI outputs, including
voice, text, visual, and tactile options as appropriate for
your system.
- Consider if AI explanations, confidence indicators, and system
status information would be available in formats accessible to
users with different abilities (screen reader compatible, high
contrast, simplified language options). You may read more from
[AWS Accessibility](https://aws.amazon.com/accessibility/) or
[12
ways Amazon is making products more accessible for customers
with disabilities](https://www.aboutamazon.com/news/devices/amazon-accessibility-features).

## Resources

**Related documents:**

- [AWS Accessibility](https://aws.amazon.com/accessibility/)
- [Use
AWS AI and ML services to foster accessibility and inclusion
of people with a visual or communication disability](https://aws.amazon.com/blogs/machine-learning/use-aws-ai-and-ml-services-to-foster-accessibility-and-inclusion-of-people-with-a-visual-or-communication-disability/)
- [Exploring
accessible audio descriptions with Amazon Nova |
Artificial...](https://aws.amazon.com/blogs/machine-learning/exploring-accessible-audio-descriptions-with-amazon-nova/)
- [12
ways Amazon is making products more accessible for customers
with disabilities](https://www.aboutamazon.com/news/devices/amazon-accessibility-features)
- [ISO/IEC
42001:2023](https://www.iso.org/standard/42001) A.8.2 System documentation and information
for users
- [Sign-Speak
builds with AI on AWS to create accessible experiences](https://aws.amazon.com/blogs/startups/sign-speak-builds-with-ai-on-aws-to-create-accessible-experiences/)
- [Accessible
Rich Internet Applications (ARIA)](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raiuc04-bp03.html*

---
