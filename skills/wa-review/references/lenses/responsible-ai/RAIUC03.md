# RAIUC03 — Refine your use case

**Best Practices**: 3

---

# RAIUC03-BP01 Identify the expected input and outputs for the AI system

Imagine the AI system solving the use case as a box containing an
unknown mechanism. Describe the inputs to the AI system. Stay at a
high level, focusing, for example, on whether inputs might contain
spoken English text and images, but not on the specific audio or
image filetypes. Consider what information is present in the input
signal, and whether that information is enough to infer the desired
outputs. Consider whether the inputs and outputs differ from how the
use case is currently solved.

**Level of risk exposed if this best practice
is not established:** High

## Implementation considerations

- Define your AI system's inputs at a high level by describing
the types of information that will flow into your system, such
as text in multiple languages, images, audio recordings, or
structured data like user preferences or transaction
histories. Focus on the content and meaning rather than
technical formats. For example, you could define inputs as
*customer support conversations* rather
than *MP3 audio files*.
- Specify what your AI system should produce as outputs,
describing the type of information it will generate. This
might include text responses, classification labels,
recommendations, generated content, or structured data that
downstream systems can use to take actions.
- Analyze whether your inputs contain enough information to
reliably produce your desired outputs by thinking through the
logical connection between what you're giving the system and
what you expect it to produce. If you want your system to
diagnose medical conditions but only provide it with basic
symptoms, consider whether that's sufficient or if you need
additional input like medical history or test results.
- Compare your AI system's inputs and outputs to how the problem
is solved today without AI, identifying what's different and
what stays the same. For example, if human customer service
agents currently handle inquiries using phone calls and
internal knowledge bases, but your AI will work with chat
messages and documentation, note these differences and
consider their implications.

## Resources

**Related documents:**

- [ISO/IEC
42001:2023](https://www.iso.org/standard/42001) A.6.2.2 AI system requirements and
specification
- [NIST
Artificial Intelligence Risk Management Framework (NIST AI
100-1)](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf): MAP2.1, MAP2.2

**Related tools:**

- [Improve
accuracy by adding Automated Reasoning checks in Amazon
Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-automated-reasoning-checks.html)
- [Use
contextual grounding check to filter hallucinations in
responses](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-contextual-grounding-check.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raiuc03-bp01.html*

---

# RAIUC03-BP02 Identify how your expected inputs could vary in their content

Identify the ways in which inputs to the AI system might
systematically vary under real-world conditions. For example, the
inputs to system that transcribes speech in audio recordings might
vary by background noise, physical characteristics of the voices, or
the sensitivity of the microphone. Or, inputs to chatbot could vary
by language, use of slang or jargon, or word spellings ("analyze" vs
"analyse"). Decide whether each type of variation is something the
AI system should attend to, or ignore.

**Level of risk exposed if this best practice
is not established:** High

## Implementation considerations

- Review examples of potential real-world inputs to identify the
types of intrinsic and confounding variations. Consider how
inputs are sourced (for example, sensor types, environmental
conditions, and potentially pre-processed). Consider
variations across different user segments, geographic regions,
and time periods.

*Intrinsic variation* refers to
differences in input data to which AI system should attend
to succeed.
- *Confounding variation* refers to
differences in input data that an AI system should ignore
to succeed.
- For example, when comparing two images of faces to
determine if the images are of the same person, an AI
system must look at differences in pixel intensities that
are due to facial geometry (like the width of the nose)
and skin albedo (including scars, tattoos, and natural
skin coloration), but not pixel differences due to camera
angle, facial expression, or scene lighting. The first
variations are intrinsic and the second are confounding.

- Consider whether data capturing intrinsic or confounding
variations can be synthesized.
- Identify edge cases and other out-of-distribution scenarios
that might affect system reliability.

## Resources:

**Related documents:**

- [Responsible
AI Practices](https://aws.amazon.com/machine-learning/responsible-ai/)
- [ISO/IEC
42001:2023](https://www.iso.org/standard/42001) A.7.4 Quality of data for AI systems
- [NIST
Artificial Intelligence Risk Management Framework (NIST AI
100-1)](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf): MAP2.1, MAP2.2, MAP2.3

*Source: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raiuc03-bp02.html*

---

# RAIUC03-BP03 Identify the type of AI required by your AI use case

Selecting the appropriate type of AI solution is a critical decision
that fundamentally shapes your project's success and risk profile.
Your choice of traditional ML, generative AI, or agentic AI must
align with your specific use case requirements, data availability,
and desired outcomes. The decision impacts everything from
development complexity and resource requirements to explainability
and risk management needs. A misaligned choice can lead to project
failure, increased costs, or unmanageable risks, while the right
selection creates a foundation for successful AI implementation that
meets business objectives while maintaining appropriate controls.

**Level of risk exposed if this best practice
is not established:** High

## Implementation considerations

- Determine if your use case primarily involves recognizing
patterns in complex but pre-defined input data. If so, you may
need traditional ML. Examples include fraud detection, demand
forecasting, or quality control systems where patterns exist
but are too complex for explicit rules.
- Determine if your use case requires understanding widely
varying inputs, including natural language, and creating
new content or providing human-like responses. If so, you may
need Generative AI. Examples include media creation, code
generation, and advanced customer chatbots.
- Determine if your use case requires breaking down high-level
user objectives into workflows, and potentially reconfiguring
the workflows depending on the results of intermediate tasks,
as opposed to just responding to queries or making
predictions. The use of a **natural
language interface** for users to communicate these
complex, high-level intents and receive updates is one of the
primary characteristics of this approach. If so, you may need
agentic AI. Examples include research and travel assistants.

## Resources

**Related documents:**

- [AWS AI Services](https://aws.amazon.com/machine-learning/ai-services/)
- [AWS Responsible AI](https://aws.amazon.com/machine-learning/responsible-ai/)
- [ISO/IEC
42001:2023](https://www.iso.org/standard/42001) A.6.2.2 AI system requirements and
specification
- [NIST
Artificial Intelligence Risk Management Framework (NIST AI
100-1)](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf): MAP2.1, MAP2.2, MAP2.3

*Source: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raiuc03-bp03.html*

---
