# RAIRC03 — Select metrics

**Best Practices**: 9

---

# RAIRC03-BP01 Measure safety harms and harmful outputs

Create objective definitions of safe and unsafe content for your use
case by considering both direct potential harms and contextual
inappropriateness. Identify harm categories relevant to possible
outputs of your system (for example, toxicity or violence). For
identified harm categories, select metrics and plan tests with both
quantitative (for example,
[model-based
toxicity classifiers](https://aws.amazon.com/blogs/machine-learning/build-a-robust-text-based-toxicity-predictor/)) and qualitative evaluation strategies
(for example, human red-teaming). Supplement your safety evaluation
with popular open-source benchmarks (like
[ToxiGen](https://github.com/microsoft/TOXIGEN)
and
[AdvBench](https://github.com/thunlp/Advbench))
and Resources (like
[Detoxify](https://github.com/unitaryai/detoxify)),
and choose metric types that are appropriate for the risk of your
use case.

**Level of risk exposed if this best practice
is not established:** High

## Implementation considerations

- Write clear and objective definitions of what counts as safe
and unsafe content for your specific use case by creating
measurable criteria and concrete examples of acceptable and
unacceptable outputs. Include both direct harms like violence
or toxicity and contextual problems like inappropriate tone
for your audience, with specific thresholds and boundaries
that evaluators can apply consistently. Objective definitions
reduce subjective interpretation and assist evaluators apply
consistent standards.
- Identify the specific harm categories that your system could
potentially produce, such as toxicity, violence,
misinformation, or inappropriate content for your target
users. Focus on harms that are realistic given your system's
purpose and capabilities rather than trying to cover every
possible risk. This targeted approach assists you to allocate
evaluation resources effectively.
- Choose quantitative metrics like automated toxicity
classifiers or content filtering tools that can measure your
identified harm categories at scale. Test popular tools like
[Detoxify](https://github.com/unitaryai/detoxify)
or [Perspective
API](https://perspectiveapi.com/) on sample outputs to see how well they detect the
types of harmful content your system might produce. Automated
metrics give you consistent measurement across large datasets.
- Plan qualitative evaluation methods like human red-teaming
where experts try to get your system to produce harmful
outputs through adversarial prompting. Have safety experts or
domain specialists review sample outputs for harms that
automated tools might miss. Human evaluation catches nuanced
safety issues that automated systems may overlook.
- Supplement your custom evaluation with open-source benchmarks
like
[ToxiGen](https://github.com/microsoft/TOXIGEN)
or
[AdvBench](https://github.com/thunlp/Advbench)
that test for common safety problems. Run these standard tests
alongside your custom evaluation to compare your system's
performance against known safety baselines. This provides
additional validation and assists to identify blind spots in
your custom evaluation approach.
- Match your evaluation intensity to your system's risk level by
using more thorough testing for higher-risk applications. For
example, consider using basic automated screening for low-risk
creative tools but adding human red-teaming for systems that
might influence important decisions. Appropriate evaluation
depth blocks both over-testing low-risk systems and
under-testing higher-risk ones.

## Resources

**Related documents:**

- [NIST
AI Risk Management Framework](https://www.sailpoint.com/identity-library/nist-risk-management-framework?igaag=157677752325&igaat=&igacm=21058117573&igacr=718115902071&igakw=governance%20risk%20compliance&igamt=p&igant=g&campaignid=21058117573&utm_source=google&utm_network=g&utm_medium=cpc&utm_content=ams-arm&utm_term=governance%20risk%20compliance&utm_id=7012J000001Fba9&gad_source=1&gad_campaignid=21058117573&gbraid=0AAAAADyJpawWDt3k-sX8hDHmVC7XLrvuM&gclid=CjwKCAjwlOrFBhBaEiwAw4bYDbokgnFJpSpMkv1GVD024r23HcapGPC4VyP5GKoBEpNqy2vVD-nydRoCmp0QAvD_BwE)
- [Build
a robust text-based toxicity predictor](https://aws.amazon.com/blogs/machine-learning/build-a-robust-text-based-toxicity-predictor/)
- [ISO/IEC
42001:2023](https://www.iso.org/standard/42001) A.6.2.4 AI system verification and
validation

**Related tools:**

- [Perspective
API](https://perspectiveapi.com/)
- [Detoxify](https://github.com/unitaryai/detoxify)
- [ToxiGen](https://github.com/microsoft/TOXIGEN)
- [AdvBench](https://github.com/thunlp/Advbench)
- [Bedrock
Evaluations](https://aws.amazon.com/bedrock/evaluations/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/rairc03-bp01.html*

---

# RAIRC03-BP02 Measure fairness as unwanted bias across stakeholder groups

Measure variations across relevant stakeholder groups based on your
specific use case and context. This evaluation may include
identifying appropriate fairness metrics that align with your use
case requirements and could examine consistency at both individual
and group levels. Technical approaches for measuring variations in
system performance may include metrics such as demographic parity,
equal outcome rates, equalized odds and equal opportunity to
understand the experience of different groups using the system.
Balance these different fairness metrics based on your use case
context, as optimizing for one type of fairness may sometimes
conflict with others.

**Level of risk exposed if this best practice
is not established:** High

## Implementation considerations

- Measure individual fairness by testing whether similar
individuals get similar treatment regardless of their
demographic characteristics.
- Measure group fairness by comparing your system's performance
across the demographic groups you identified in your risk
assessment (RAIBR02) using metrics like accuracy, precision,
and recall. Calculate performance differences between groups
and compare them to your acceptable thresholds to identify
potential biases. Group-level measurement reveals systemic
unwanted bias that may have larger impacts (like bias across
entire groups).
- Test for representational fairness by analyzing whether your
system's outputs reinforce harmful stereotypes or misrepresent
different groups. Use existing tools like stereotype detection
classifiers or analyze generated content for biased language
patterns. This catches subtle bias that may not show up in
performance metrics but still causes harm.
- Consider testing your system on pairs of similar inputs that
differ only in demographic attributes to see if outputs change
inappropriately. This reveals potential bias where demographic
factors inappropriately influence decisions.
- Consider testing your system on intersectional groups that
combine multiple demographic characteristics, using the same
metrics you applied to single-group analysis. Compare results
across these intersectional groups to identify potential bias
that might be hidden when looking at single demographics
alone.
- Consider experimenting with complementary fairness metrics
like demographic parity, equal opportunity, and equalized odds
to get multiple perspectives on your system's fairness. For
example, measure whether different groups receive similar
positive prediction rates and whether the system correctly
identifies positive cases at similar rates across groups.
Multiple metrics reveal different types of bias since systems
can appear fair on one measure but not on another.
- Identify which fairness metrics conflict with each other for
your system and make explicit decisions about which to
prioritize based on your use case context and stakeholder
values established in your risk characterization (RAIBR02).
Record your reasoning for these trade-offs since optimizing
for one type of fairness often reduces performance on others.
Clear prioritization assists you to make consistent decisions
when fairness measures conflict.

## Resources

**Related documents**

- [NIST
AI Risk Management Framework](https://www.sailpoint.com/identity-library/nist-risk-management-framework?igaag=157677752325&igaat=&igacm=21058117573&igacr=718115902071&igakw=governance%20risk%20compliance&igamt=p&igant=g&campaignid=21058117573&utm_source=google&utm_network=g&utm_medium=cpc&utm_content=ams-arm&utm_term=governance%20risk%20compliance&utm_id=7012J000001Fba9&gad_source=1&gad_campaignid=21058117573&gbraid=0AAAAADyJpawWDt3k-sX8hDHmVC7XLrvuM&gclid=CjwKCAjwlOrFBhBaEiwAw4bYDbokgnFJpSpMkv1GVD024r23HcapGPC4VyP5GKoBEpNqy2vVD-nydRoCmp0QAvD_BwE)
- [ISO/IEC
42001:2023](https://www.iso.org/standard/42001) A.6.2.4 AI system verification and
validation
- [Common
fairness metrics](https://fairlearn.org/main/user_guide/assessment/common_fairness_metrics.html)

**Related tools:**

- [Amazon
Bedrock Evaluations](https://aws.amazon.com/bedrock/evaluations/)
- [Amazon SageMaker AI Clarify](https://aws.amazon.com/sagemaker/ai/clarify/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/rairc03-bp02.html*

---

# RAIRC03-BP03 Measure veracity of outputs

Assess your system's tendency to generate factually accurate
information while avoiding the specific types of hallucinations,
misinformation, or fabricated content your risk assessment
identified as problematic for your use case. Implement automated
fact-checking and human expert evaluations. Measure the specific
aspects of truthfulness your risk assessment prioritized such as
factual accuracy, groundedness to source material, or consistency
across interactions.

**Level of risk exposed if this best practice
is not established:** High

## Implementation considerations

- Identify metrics for potential hallucination, omission, and
misemphasis harms that you identified in your risk assessment
(RAIBR02).
- Plan expert human evaluations where domain specialists review
sample outputs for factual accuracy and appropriateness within
their area of expertise. Have subject matter experts evaluate
claims in their field to catch subtle inaccuracies that
automated tools might miss. Human experts can assess context,
nuance, and domain-specific accuracy that automated systems
often overlook.
- Measure groundedness, i.e. the degree to which your system's
outputs can be traced back to reliable source material when
sources are available. Check if claims in generated content
align with the source documents and whether citations are
accurate and relevant. Groundedness testing blocks your system
from making claims that aren't supported by its reference
materials.
- Measure consistency by asking your system the same questions
multiple times and across different phrasings to see if
answers remain factually consistent. Also test related
questions to see if responses contradict each other across
different interactions. Consistency testing reveals when your
system generates conflicting information about the same
topics.

## Resources

**Related documents**

- [NIST
AI Risk Management Framework](https://www.sailpoint.com/identity-library/nist-risk-management-framework?igaag=157677752325&igaat=&igacm=21058117573&igacr=718115902071&igakw=governance%20risk%20compliance&igamt=p&igant=g&campaignid=21058117573&utm_source=google&utm_network=g&utm_medium=cpc&utm_content=ams-arm&utm_term=governance%20risk%20compliance&utm_id=7012J000001Fba9&gad_source=1&gad_campaignid=21058117573&gbraid=0AAAAADyJpawWDt3k-sX8hDHmVC7XLrvuM&gclid=CjwKCAjwlOrFBhBaEiwAw4bYDbokgnFJpSpMkv1GVD024r23HcapGPC4VyP5GKoBEpNqy2vVD-nydRoCmp0QAvD_BwE)
- [ISO/IEC
42001:2023](https://www.iso.org/standard/42001) A.6.2.4 AI system verification and
validation

**Related tools:**

- [Amazon
Bedrock Evaluations](https://aws.amazon.com/bedrock/evaluations/)
- [Improve
accuracy by adding Automated Reasoning checks in Amazon
Bedrock Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-automated-reasoning-checks.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/rairc03-bp03.html*

---

# RAIRC03-BP04 Measure robustness of outputs to input variation

Measure how consistently your system performs when faced with the
specific input variations and distribution shifts that are relevant
to your use case. Prepare to test performance across the natural
variations your risk assessment determined users might provide (such
as different writing styles, dialects, image qualities, or audio
conditions relevant to your use case).

**Level of risk exposed if this best practice
is not established:** High

## Implementation considerations

- Build controlled robustness tests that vary one input factor
at a time while keeping the content meaning the same, using
the input variations your RAIBR02 risk assessment found most
likely in your deployment environment. Create paired test
cases where you change only one thing, such as converting
formal business language to casual speech or adjusting image
lighting conditions. Controlled variation testing shows you
which specific input factors cause performance drops and by
how much.
- Apply the same metrics you selected in RAIRC02-BP01 to measure
performance across different input variations, comparing how
your system performs on standard inputs versus challenging
variations. Use controlled comparisons where you test the same
content with only one input characteristic changed at a time,
such as measuring accuracy on both formal and casual versions
of the same question. This approach reveals which specific
input factors cause performance drops and by how much.
- Calculate performance variance and degradation across known
input variations to quantify how much your system's
reliability fluctuates under different conditions. Identify
the worst-case performance drops across input types.
- Test combinations of multiple input variations together, such
as processing accented speech with background noise or
analyzing low-quality images with poor lighting, since real
users often provide challenging inputs with several issues
simultaneously. Focus on combinations most likely to occur in
your deployment environment based on your use case analysis.
Combined variation testing catches failure modes that only
emerge when multiple challenging factors interact.

## Resources

**Related documents**

- [NIST
AI Risk Management Framework](https://www.sailpoint.com/identity-library/nist-risk-management-framework?igaag=157677752325&igaat=&igacm=21058117573&igacr=718115902071&igakw=governance%20risk%20compliance&igamt=p&igant=g&campaignid=21058117573&utm_source=google&utm_network=g&utm_medium=cpc&utm_content=ams-arm&utm_term=governance%20risk%20compliance&utm_id=7012J000001Fba9&gad_source=1&gad_campaignid=21058117573&gbraid=0AAAAADyJpawWDt3k-sX8hDHmVC7XLrvuM&gclid=CjwKCAjwlOrFBhBaEiwAw4bYDbokgnFJpSpMkv1GVD024r23HcapGPC4VyP5GKoBEpNqy2vVD-nydRoCmp0QAvD_BwE)
- [ISO/IEC
42001:2023](https://www.iso.org/standard/42001) A.6.2.4 AI system verification and
validation

**Related tools:**

- [Amazon
Bedrock Evaluations](https://aws.amazon.com/bedrock/evaluations/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/rairc03-bp04.html*

---

# RAIRC03-BP05 Measure privacy protection

Measure how well your system protects each type of confidential or
personal information that your risk assessment identified as at
risk. This may include detecting privacy leaks, unauthorized data
access patterns, or inappropriate data retention issues your risk
assessment determined to be most likely or impactful. Assess private
data identification and redaction capabilities for the data types
that your risk assessment prioritized and consult with your legal
team on the specific privacy regulations relevant to your use case.

**Level of risk exposed if this best practice
is not established:** High

## Implementation considerations

- Build privacy attack tests that target the vulnerabilities
your RAIBR02 risk assessment found, using both automated tools
such as
[Promptfoo](https://github.com/promptfoo/promptfoo)
and manual testing to check for membership inference, data
extraction, and prompt injections. Create standard test cases
with clear success measures and document your testing methods
so you can repeat them across different system versions.
- Set up automated detection tests that check your system's
ability to find and remove the types of confidential and
personal information that your risk assessment prioritized.
Build testing pipelines that measure how accurately your
system detects these data types.

## Resources

**Related documents:**

- [NIST
AI Risk Management Framework](https://www.sailpoint.com/identity-library/nist-risk-management-framework?igaag=157677752325&igaat=&igacm=21058117573&igacr=718115902071&igakw=governance%20risk%20compliance&igamt=p&igant=g&campaignid=21058117573&utm_source=google&utm_network=g&utm_medium=cpc&utm_content=ams-arm&utm_term=governance%20risk%20compliance&utm_id=7012J000001Fba9&gad_source=1&gad_campaignid=21058117573&gbraid=0AAAAADyJpawWDt3k-sX8hDHmVC7XLrvuM&gclid=CjwKCAjwlOrFBhBaEiwAw4bYDbokgnFJpSpMkv1GVD024r23HcapGPC4VyP5GKoBEpNqy2vVD-nydRoCmp0QAvD_BwE)
- [NIST
Privacy Engineering Program](https://www.nist.gov/privacy-engineering)
- [ISO/IEC
42001:2023](https://www.iso.org/standard/42001) A.6.2.4 AI system verification and
validation
- [Remove
PII from conversations by using sensitive information
filters](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-sensitive-filters.html)

**Related tools:**

- [Promptfoo](https://github.com/promptfoo/promptfoo)
- [Presidio:
Data Protection and De-identification SDK](https://microsoft.github.io/presidio/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/rairc03-bp05.html*

---

# RAIRC03-BP07 Measure user controllability of system behavior

To verify that users can effectively control your AI system when
they need to override, adjust, or roll back its behavior, develop
quantitative measures that assess how well user controls correlate
with intended system outcomes. Test the range and granularity of
control effectiveness by measuring whether adjustments produce the
expected changes in system behavior. Create metrics that capture
both the responsiveness of controls and their precision. Your
metrics should measure when controls fail to work as intended or
when they produce unexpected side effects.

**Level of risk exposed if this best practice
is not established:** High

## Implementation considerations

- Plan how you'll test user controls before building your system
by deciding which control mechanisms matter most for user
safety based on your RAIBR02 risk assessment findings. Create
simple test scenarios that check if each control works as
intended and build basic measurement tools that show whether
user inputs can change system behavior. This upfront planning
saves time later and assists you to build controls that work
when users need them.
- Design tests that check how well users can fine-tune your
system's behavior, from small adjustments to major changes.
Test both precise control scenarios where users make small
tweaks and broad control scenarios where users need to make
big behavioral shifts. Include tests that push controls to
their breaking points to determine where the system stops
responding to user input, which assists you to fix weak spots.
- Build ways to measure how fast your system reacts when users
try to override, adjust, or roll back its behavior. Track how
long controls take to activate and how quickly the system
settles into new behavior patterns after users make changes.
Fast, reliable control response keeps users in charge of the
system.
- Create tests that catch when controls fail or cause unexpected
problems elsewhere in your system. Test what happens when
users try controls that should fail gracefully and verify that
your system gives clear feedback when controls can't work.
Look for cases where adjusting one thing accidentally breaks
something else, as surprise effects can undermine user trust.

## Resources

**Related documents:**

- [FollowBench](https://aclanthology.org/2024.acl-long.257.pdf)
- [IFEval](https://arxiv.org/pdf/2311.07911)
- [Prompt
Steerability](https://aclanthology.org/2025.naacl-long.400.pdf)
- [Human
Agency Scale](https://www.emergentmind.com/topics/human-agency-scale-has)
- [ISO/IEC
42001:2023](https://www.iso.org/standard/42001) A.6.2.4 AI system verification and
validation

*Source: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/rairc03-bp07.html*

---

# RAIRC03-BP08 Measure explainability of system behavior

Consider metrics for explainability based on user studies that
quantitatively measure stakeholders' ability to understand system
outputs, including their comprehension of confidence scores,
reasoning paths, and limitations, while also tracking the
effectiveness of provided explanations across different user groups
and expertise levels. This can include objective metrics (such as
task completion rates when acting on AI explanations) and subjective
assessments (like user satisfaction scores and trust ratings). Pay
particular attention to whether users can accurately identify when
to rely on or question the system's outputs.

**Level of risk exposed if this best practice
is not established:** High

## Implementation considerations

- Create baseline measurement approaches that check whether
users can correctly interpret what your system is telling them
and why. Include the user groups from your RAIBR02 risk
assessment who need to understand system outputs, and design
simple comprehension tests for confidence scores, reasoning
paths, and system limitations.
- Design objective testing that measures how successfully users
complete tasks when they rely on your system's explanations.
Build tests that track task completion rates, decision
accuracy, and time to completion when users act on AI
explanations and when they work without them. Test across
different expertise levels to see where your explanations
assist users to make better decisions and where they might
mislead people.
- Build subjective assessment tools that capture user
satisfaction, trust levels, and confidence in your system's
explanations. Create simple rating scales and feedback
collection methods that show whether users feel your
explanations are helpful, trustworthy, and simple to
understand. Track how these subjective measures vary across
different user groups so you can spot where your explanations
work well and where they fall short.
- Test whether users can accurately judge when to trust or
question your system's outputs by creating scenarios where the
system should and shouldn't be trusted. Build measurement
approaches that check if users correctly identify high
confidence as compared to low confidence situations and
whether they appropriately rely on or override system
recommendations. This testing assists you to catch cases where
users might over- or under-trust your system.

## Resources

**Related documents:**

- [Advanced
tracing and evaluation of generative AI agents using LangChain
and Amazon SageMaker AI AI MLFlow](https://aws.amazon.com/blogs/machine-learning/advanced-tracing-and-evaluation-of-generative-ai-agents-using-langchain-and-amazon-sagemaker-ai-mlflow/)

**Related tools:**

- [Amazon SageMaker AI Clarify](https://aws.amazon.com/sagemaker/ai/clarify/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
- [AWS Step Functions](https://aws.amazon.com/step-functions/)
- [AWS EventBridge](https://aws.amazon.com/eventbridge/)
- [Amazon Simple Notification Service](https://aws.amazon.com/pm/sns/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/rairc03-bp08.html*

---

# RAIRC03-BP09 Measure security risks and threats

Consider quantitative measurements of security risks to AI systems,
such as measuring adversarial attack success rates. For example,
measure the rate of successful prompt injection attempts, prompt
injection detection rates, jailbreaking success rate, guardrail
bypass rates, and model extraction resistance (measuring how simply
model parameters or behavior can be reverse engineered).

**Level of risk exposed if this best practice
is not established:** High

## Implementation considerations

- Track metrics such as the percentage of prompt injections that
successfully change your system's behavior, how many
jailbreaking attempts bypass your guardrails, and whether
attackers can extract sensitive information about your model's
architecture or training data.
- Measure attack detection accuracy. Determine the correct
balance between blocking suspected attacks and not blocking
legitimate user inputs.
- Test your defenses with advanced attack combinations like
prompt injections embedded within seemingly innocent requests
or multi-turn conversations that gradually escalate toward
harmful content. See if your security holds up when attackers
chain techniques together or adapt their methods based on your
system's responses.
- Include red teaming exercises where security experts attempt
to break your system using creative attack methods you might
not have considered.

## Resources

**Related documents**

- [ISO/IEC
42001:2023](https://www.iso.org/standard/42001) A.6.2.4 AI system verification and
validation

**Related tools**

- [Threat
Composer](https://github.com/awslabs/threat-composer?tab=readme-ov-file)
- [Metrics
in Amazon Cloudwatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/working_with_metrics.html)
- [Amazon
Bedrock Guardrails](https://aws.amazon.com/bedrock/guardrails/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/rairc03-bp09.html*

---

# RAIRC03-BP10 Measure transparency quality

Consider situations where system documentation is insufficient,
users do not understand the probabilistic nature of a system output,
or where users are unaware of AI system presence. Transparency
deficits might conceal or amplify potential harms while evaluating
impacts on different stakeholder groups. The goal is finding the
right transparency level for your situation by balancing enough
openness to build trust and meet requirements without creating new
vulnerabilities or unintended consequences.

**Level of risk exposed if this best practice
is not established:** High

## Implementation considerations

- Plan how you'll test transparency effectiveness before
building your disclosure features by identifying which
stakeholders from your RAIBR02 risk assessment need what level
of transparency about AI system presence, capabilities, and
limitations. Create simple tests that check whether users
understand when they're interacting with AI, grasp the
probabilistic nature of outputs, and recognize potential
biases. This upfront planning assists you to build
transparency features that inform users without overwhelming
them.
- Design tests that measure whether your transparency
disclosures assist users to make better decisions or
accidentally create new problems. Build tests that track
decision quality when users have different levels of system
information and measure whether transparency improves outcomes
or leads to misinterpretation. Test across different user
expertise levels to see where more transparency assists versus
where it might create confusion.
- Build measurement approaches that capture both positive
transparency outcomes like increased trust alongside potential
negative effects like exposure or security risks. Create
simple metrics that track user confidence, stakeholder
satisfaction, and compliance-aligned measures while also
checking for unintended information leakage or misuse. This
balanced approach assists you to spot where transparency
creates value and where it might cause harm.
- Test transparency calibration by creating scenarios where
users need to understand system confidence levels,
limitations, and appropriate use cases for high-stakes
decisions like financial or health recommendations. Build
measurement tools that check whether users correctly interpret
uncertainty indicators and make appropriately cautious
decisions when system confidence is low. This testing catches
cases where transparency gaps might lead to harmful
over-reliance on uncertain outputs.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/rairc03-bp10.html*

---
