# AGENTCOST02 — Model invocation and token cost optimization

**Pillar**: Cost Optimization  
**Best Practices**: 4

---

# AGENTCOST02-BP01 Architect tiered model selection for cost-performance optimization

Running every agent task on the largest available model inflates
inference cost by an order of magnitude for work that smaller models
handle correctly. Match each task to the cheapest model capable of
acceptable quality, and escalate only when confidence drops.

**Desired outcome:**

- You have agent tasks classified into complexity tiers, with a
documented routing policy mapping each tier to a specific
foundation model.
- You have cascading patterns that escalate to higher-cost models
only when a lower tier's confidence falls below threshold.
- You track cost-per-correct-response across tiers and refresh
routing decisions with the data rather than with intuition.

**Common anti-patterns:**

- Using the largest available model for all agent tasks without
assessing task complexity, inflating inference costs for routine
operations.
- Hard-coding static model assignments without confidence-based
escalation, which either over-provisions routine tasks or
under-provisions complex edge cases.
- Tracking aggregate costs without decomposing agent performance
by model tier, hiding opportunities to shift workloads to
cheaper models.
- Failing to monitor customized model performance after switching
to a smaller tier, allowing cost savings to mask hidden quality
degradation.

**Benefits of establishing this best
practice:**

- Tiered selection reserves expensive models for genuinely complex
reasoning and routes routine tasks to cost-effective
alternatives.
- Model cascading minimizes premium model invocations through
confidence-based escalation.
- Specialized models for domain-specific tasks deliver higher
accuracy at lower cost than general-purpose alternatives.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Task complexity is an important property to measure. At every
agent invocation, the reasoning you need is either lightweight
(classification, format conversion, intent extraction), moderate
(multi-step reasoning, summarization), or genuinely complex
(open-ended analysis, multi-constraint optimization). These three
classes map to different price points across the
[Amazon
Bedrock](https://aws.amazon.com/bedrock/) model catalog, and treating them identically means
you pay the complex-class price for every low-complexity task.
Classifying upfront and routing accordingly is where most of the
cost headroom sits.

A lightweight pre-classifier gives you that routing decision
without invoking the main model first. Rule-based heuristics or a
small model can analyze request characteristics like input length,
structured or unstructured format, constraint count, and reasoning
depth, assigning scores that map to tier thresholds (for example,
below 0.3 for simple, 0.3 to 0.7 for moderate, above 0.7 for
complex). The pre-classifier must cost less than the tier price
differential to produce net savings on first-attempt routing. For
multimodal tasks the principle extends further. Route document
extraction to Amazon Bedrock Data Automation and audio
interactions to Amazon Nova Sonic rather than sending raw images
or audio through expensive general-purpose vision models.

Model cascading is a fallback mechanism when the classifier is
uncertain. Have the lower-tier model return a structured response
with a self-assessed confidence score and escalate to the next
tier only when confidence falls below a threshold. Primary,
secondary, and tertiary fallback chains catch timeouts and
failures by moving up a tier rather than retrying the same one,
improving completion rates without retry waste.
[Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html) is designed to support multiple
frameworks and LLM providers, and
[Amazon
Bedrock AgentCore Policy](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy.html) enforces guardrails that help
prevent expensive model calls when task complexity doesn't justify
the cost.

Pricing tier is independent of model size.
[Amazon
Bedrock capacity, limits, and cost optimization](https://docs.aws.amazon.com/bedrock/latest/userguide/capacity-limits-cost-optimization.html) documents
Flex for development and testing at the lowest per-token cost,
Standard for production, and Priority only for latency-sensitive
user-facing interactions where throttling risk must be minimized.
Batch inference offers up to 50% savings for non-time-sensitive
workloads like report generation, training data preparation, or
offline evaluation. For consistent high-volume traffic, Reserved
Tier commitments provide 30 to 50% savings against on-demand
pricing. With
[Amazon
Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html), you can benchmark multiple
model options against your actual task distribution, measuring
cost-per-correct-response and refreshing the routing policy
quarterly as new models become available.

### Implementation steps

- **Classify agent tasks into complexity
tiers:** Document a model routing policy mapping
each tier (simple, moderate, and complex) to a specific
[Amazon
Bedrock](https://aws.amazon.com/bedrock/) model, and commit the policy as an
architectural decision record so downstream reviewers can
audit the rationale.
- **Select pricing tier per
environment:** Use Flex for development and
testing, Standard for production, and Priority only for
latency-sensitive user-facing agents, and evaluate
[Amazon
Bedrock Reserved Tier](https://docs.aws.amazon.com/bedrock/latest/userguide/capacity-limits-cost-optimization.html) commitments for consistent
high-volume workloads.
- **Insert a task complexity
pre-classifier:** Deploy rule-based heuristics or a
small-model call that scores each request on input length,
structure, constraint count, and reasoning depth before the
main invocation, and make sure the classifier costs less
than the tier price differential.
- **Implement model cascading on
confidence:** Have each lower-tier response include
a self-assessed confidence score, and escalate to the next
tier when confidence falls below the configured threshold
rather than retrying at the same tier.
- **Configure fallback chains per task
category:** Define primary, secondary, and tertiary
model options, with automatic escalation on timeout or
failure instead of retry, so transient failures move up a
tier rather than repeating the same cost.
- **Route non-time-sensitive tasks to
batch inference:** Use
[Amazon
Bedrock batch inference](https://docs.aws.amazon.com/bedrock/latest/userguide/batch-inference.html) for report generation, data
enrichment, and offline evaluation to capture up to 50%
savings over on-demand pricing.
- **Benchmark specialized compared to
general-purpose models:** Run
[Amazon
Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html) on your actual task
distribution, measuring cost-per-correct-response so routing
choices are grounded in outcome data.
- **Review routing policies
quarterly:** Use AWS Cost Explorer and Amazon CloudWatch dashboards to inspect observed escalation rates,
and adjust tier assignments when cascade escalation patterns
indicate mis-tuned thresholds.

## Resources

**Related best practices:**

- [AGENTCOST01-BP01
Use the reflection pattern to design efficient agent reasoning
loops](agentcost01-bp01.html)
- [AGENTCOST01-BP04
Design agent hierarchies and delegation patterns that reduce
coordination overhead](agentcost01-bp04.html)
- [AGENTCOST02-BP02 Cost
optimize token consumption through efficient prompt
engineering](agentcost02-bp02.html)
- [AGENTCOST02-BP04
Implement model customization for long-term cost
reduction](agentcost02-bp04.html)
- [AGENTCOST05-BP01
Establish agent-level reasoning cost tracking and
attribution](agentcost05-bp01.html)

**Related documents:**

- [Amazon
Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html)
- [Effective
cost optimization strategies for Amazon Bedrock](https://aws.amazon.com/blogs/machine-learning/effective-cost-optimization-strategies-for-amazon-bedrock/)
- [Use
Amazon Bedrock Intelligent Prompt Routing for cost and latency
benefits](https://aws.amazon.com/blogs/machine-learning/use-amazon-bedrock-intelligent-prompt-routing-for-cost-and-latency-benefits/)
- [Optimizing
cost for using foundational models with Amazon Bedrock](https://aws.amazon.com/blogs/aws-cloud-financial-management/optimizing-cost-for-using-foundational-models-with-amazon-bedrock/)
- [Economics
for agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-economics/index.html)
- [Guidance
for Cost Analysis and Optimization with Amazon Bedrock
Agents](https://aws.amazon.com/solutions/guidance/cost-analysis-and-optimization-with-amazon-bedrock-agents/)
- [Agentic
AI patterns and workflows on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-patterns/introduction.html)
- [Amazon
Bedrock model pricing](https://aws.amazon.com/bedrock/pricing/)
- [Amazon
Bedrock capacity, limits, and cost optimization](https://docs.aws.amazon.com/bedrock/latest/userguide/capacity-limits-cost-optimization.html)
- [Amazon
Bedrock batch inference](https://docs.aws.amazon.com/bedrock/latest/userguide/batch-inference.html)

**Related videos:**

- [AWS re:Invent 2024 - Balance cost, performance & reliability
for AI at enterprise scale (AIM3304)](https://www.youtube.com/watch?v=Lwvv8Q33eeE)
- [AWS re:Invent 2024 - Mastering model choice: The 3-step Amazon
Bedrock advantage (AIM391)](https://www.youtube.com/watch?v=Vu91YwZxskY)

**Related examples:**

- [GitHub:
awslabs/amazon-bedrock-agentcore-samples - Evaluations
tutorials](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/07-AgentCore-evaluations)

**Related tools:**

- [Strands
Agents Model Providers](https://strandsagents.com/docs/user-guide/concepts/model-providers/)

**Related services:**

- [Amazon
Bedrock](https://aws.amazon.com/bedrock/)
- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
- [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentcost02-bp01.html*

---

# AGENTCOST02-BP02 Cost optimize token consumption through efficient prompt engineering

Every token in a system prompt is paid for on every invocation, so
prompt bloat compounds linearly with traffic. Compressing system
prompts, tool descriptions, and output formats makes the fixed cost
of each agent call proportional to the decision it has to make, not
the verbosity of its instructions.

**Desired outcome:**

- You have agent system prompts compressed to the minimum tokens
needed for accurate task completion.
- You have tool descriptions presented dynamically based on the
current task rather than transmitted in full on every call.
- You constrain output length explicitly so verbose responses
don't compound across multi-turn reasoning.
- You version prompts and track cost-per-task per version so
efficiency changes are measurable over time.

**Common anti-patterns:**

- Writing verbose system prompts with lengthy persona descriptions
and redundant explanations, inflating the fixed token cost on
every invocation.
- Including every tool description in every invocation regardless
of task relevance, which inflates input tokens when only a
subset of tools applies.
- Allowing unconstrained output length without formatting
directives, enabling verbose responses that compound across
multi-turn reasoning cycles.
- Treating prompts as uncontrolled strings rather than versioned
artifacts, so regressions in token efficiency go unnoticed until
a billing review.

**Benefits of establishing this best
practice:**

- Fixed-cost reductions from prompt compression compound across
every agent invocation in high-volume deployments.
- Dynamic tool loading transmits only task-relevant tools,
reducing tool description overhead in proportion to catalog
size.
- Prompt versioning with token tracking makes compression an
ongoing, measurable practice rather than a one-off cleanup.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

The system prompt is the largest fixed cost in every model
invocation, which means every unnecessary sentence is paid for
again each time the agent is called. Start by auditing prompts
with
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) to measure token
footprints, then compress systematically. Replace verbose
instructions with structured directives, tighten role definitions,
and remove redundant explanations.

Tool descriptions behave the same way. If the prompt carries the
full tool catalog even when only three tools are relevant, you are
paying for the rest of the catalog on every call.
[Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) uses MCP-based Semantic Tool
Selection to present only the tools relevant to the current
intent, and
[Amazon
Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) manages conversation state across
multi-turn sessions so you don't pay for manual history
concatenation.

In your context window, allocate tokens across the system prompt
(20 to 30%), user context (30 to 40%), few-shot examples (10 to
20%), and agent scratchpad (20 to 30%), and adjust based on your
agent's reasoning patterns. For few-shot examples in particular,
test whether the model performs well zero-shot before paying for
examples on every call. When examples are needed, identify the
minimum count that maintains task accuracy against the quality
baseline. Two or three examples are typically enough, and dynamic
example selection from a semantic index keeps only the relevant
ones in context.

Output length is the last thing to adjust. Explicit formatting
directives in the system prompt (response structure, maximum
length) directly control output token costs. Treat prompts as
versioned artifacts. Record token count, task success rate, and
cost-per-task for each version using AgentCore Observability
telemetry, and establish a monthly review cadence that tracks
cumulative savings in AWS Cost Explorer.

### Implementation steps

- **Audit and compress system
prompts:** Use
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html) to measure token
footprints for every prompt, then apply compression to
minimize prompt size while maintaining decision accuracy.
- **Present tools dynamically through
Gateway:** Use
[Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html) Semantic Tool Selection to
present only relevant tools per invocation, and compress
tool descriptions to tool name, one-sentence description,
and concise parameter schema.
- **Constrain output length:**
Add explicit output formatting directives to the system
prompt and configure model-specific token limit parameters
to enforce hard caps on response size.
- **Use managed memory for multi-turn
context:** Configure
[Amazon
Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) so conversation state is
maintained automatically instead of re-transmitted as full
history.
- **Reduce few-shot example
overhead:** Evaluate whether each agent task needs
examples at all, then reduce to the minimum effective count
of two to three. Load examples dynamically from an Amazon S3-hosted library using semantic similarity retrieval.
- **Version prompts and track
efficiency:** Record token count and task success
rate per prompt version, and establish a monthly
optimization review cadence that tracks cumulative savings
against cost-per-task targets.

## Resources

**Related best practices:**

- [AGENTCOST01-BP01
Use the reflection pattern to design efficient agent reasoning
loops](agentcost01-bp01.html)
- [AGENTCOST02-BP01
Architect tiered model selection for cost-performance
optimization](agentcost02-bp01.html)
- [AGENTCOST02-BP03 Use
intelligent caching to reduce redundant model
invocations](agentcost02-bp03.html)

**Related documents:**

- [Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html)
- [Amazon
Bedrock AgentCore Gateway](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html)
- [Amazon
Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html)
- [Economics
for agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-economics/index.html)

**Related videos:**

- [AWS re:Invent 2024 - Sustainable and cost-efficient generative AI
with agentic workflows (AIM333)](https://www.youtube.com/watch?v=tFiDkSG2ess)
- [Strands
Tools: Building Custom AI Agents with Python](https://www.youtube.com/watch?v=EGhIZCfOvG4)

**Related examples:**

- [GitHub:
awslabs/amazon-bedrock-agentcore-samples - Runtime
tutorials](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/01-AgentCore-runtime)

**Related tools:**

- [Strands
Agents Custom Tools](https://strandsagents.com/docs/user-guide/concepts/tools/custom-tools/)

**Related services:**

- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentcost02-bp02.html*

---

# AGENTCOST02-BP03 Use intelligent caching to reduce redundant model invocations

Agents repeat work constantly: identical prompts, semantically
equivalent requests, the same planning steps across similar tasks.
Caching at the prompt, semantic, and plan-template layers changes
repetition from a recurring expense into a one-time cost paid on the
first invocation.

**Desired outcome:**

- You have prompt caching enabled for stable system prompts so the
cacheable prefix is reused across invocations at reduced rates.
- You have a semantic cache that serves responses for functionally
equivalent requests above a configurable similarity threshold.
- You have plan templates cached and instantiated for recurring
task patterns rather than regenerated each time.
- You track cache hit rates and cost savings per caching layer.

**Common anti-patterns:**

- Transmitting identical system prompts and tool descriptions on
every invocation at full input token cost rather than cached
prefix rates.
- Using exact-match lookups when functionally equivalent requests
use different wording, causing cache misses on semantically
identical tasks.
- Applying one cache TTL across all task types without
distinguishing static reference data from time-sensitive
information, returning stale responses that degrade quality.
- Deploying customized models without monitoring cache-assisted
performance, missing opportunities to validate that expected
cost reductions actually materialize.

**Benefits of establishing this best
practice:**

- Prompt caching reduces input token costs by reusing cached
system instructions across invocations at reduced rates.
- Semantic caching helps prevent redundant reasoning by serving
cached responses for functionally equivalent tasks.
- Plan template reuse reduces model invocations for the planning
phase of recurring task patterns.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Caching for agents works at three distinct layers, and each layer
has a different failure mode.

[Amazon
Bedrock prompt caching](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-caching.html) is the highest-impact layer for
agents with large stable system prompts. Amazon Bedrock stores the
key-value state of the cached prefix and reuses it at reduced
rates. Design so that the cacheable prefix (system prompt, tool
descriptions) is stable across invocations, because any dynamic
content mixed in invalidates the cache. Refactor to move
user-specific or session-specific content out of the cacheable
prefix.

Semantic caching addresses the idea that two requests that mean
the same thing are rarely identical in wording. Generate an
embedding of each incoming request with a lightweight model and
query
[Amazon OpenSearch Service Serverless](https://aws.amazon.com/opensearch-service/features/serverless/) for similar prior requests above a
configurable threshold such as cosine similarity greater than
0.95. The threshold helps you tune, as higher values reduce false
positives but lower hit rates, and the right value depends on how
much response variance your agent tolerates. Store cache entries
with TTLs calibrated to each task type's freshness requirements,
so reference data cached for hours doesn't pollute tasks that need
up-to-date market or inventory information.

Don't overlook plan template caching. Agent planning outputs are
highly repeatable for recurring task patterns, like an onboarding
checklist, a support triage decomposition, or a reporting workflow
plan. Store these plans keyed by task type and input parameter
signature, and instantiate cached templates with current
parameters rather than regenerating new plans each time.
[Amazon
Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) manages conversation state by
extracting and persisting key information, reducing input token
costs from repeated history transmission.

Cache correctness depends on invalidation. Event-driven
invalidation purges stale entries the moment source data changes,
which is what makes aggressive caching safe for moderately
volatile data. Measure impact with AWS Cost Explorer and Amazon CloudWatch integrated with
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html), and alarm when hit rates
fall below targets.

### Implementation steps

- **Enable prompt caching for stable
prefixes:** Turn on
[Amazon
Bedrock prompt caching](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-caching.html) for agents with system prompts
larger than 1,000 tokens, and refactor the prompt to move
dynamic content out of the cacheable prefix.
- **Deploy a semantic cache
layer:** Stand up an OpenSearch Serverless index
with embedding-based similarity, configure similarity
thresholds per task type, and set per-task TTLs. Accept
quantization only when accuracy loss remains below two
percent on task success rate.
- **Cache plan templates:** Key
plan templates by task type and input parameter signature,
and perform a pre-invocation lookup before generating a new
plan.
- **Use managed memory for session
state:** Configure
[Amazon
Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html) session identifiers so
multi-turn conversation state is maintained without manual
history concatenation.
- **Design event-driven invalidation and
monitor hit rates:** Wire event-driven cache
invalidation to source data changes, and create CloudWatch
dashboards that display hit rates across prompt, semantic,
and plan-template caches with alarms when hit rates fall
below target.

## Resources

**Related best practices:**

- [AGENTCOST02-BP01
Architect tiered model selection for cost-performance
optimization](agentcost02-bp01.html)
- [AGENTCOST02-BP02 Cost
optimize token consumption through efficient prompt
engineering](agentcost02-bp02.html)
- [AGENTCOST03-BP01
Design cost-effective retrieval systems with tiered
memory](agentcost03-bp01.html)

**Related documents:**

- [Amazon
Bedrock Prompt Caching](https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-caching.html)
- [Effectively
use prompt caching on Amazon Bedrock](https://aws.amazon.com/blogs/machine-learning/effectively-use-prompt-caching-on-amazon-bedrock/)
- [Optimize
LLM response costs and latency with effective caching](https://aws.amazon.com/blogs/database/optimize-llm-response-costs-and-latency-with-effective-caching/)
- [Amazon
Bedrock AgentCore Memory](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/memory.html)
- [Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html)
- [Economics
for agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-economics/index.html)

**Related videos:**

- [AWS re:Invent 2024 - Balance cost, performance & reliability
for AI at enterprise scale (AIM3304)](https://www.youtube.com/watch?v=Lwvv8Q33eeE)

**Related examples:**

- [GitHub:
awslabs/amazon-bedrock-agentcore-samples - Memory
tutorials](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/04-AgentCore-memory)

**Related services:**

- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon OpenSearch Service](https://aws.amazon.com/opensearch-service/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentcost02-bp03.html*

---

# AGENTCOST02-BP04 Implement model customization for long-term cost reduction

Customizing smaller models for a high-volume recurring task can
optimize per-invocation costs into a one-time training expense that
amortizes across every future call. The math only works when volume
and task stability are high enough to justify the investment, so the
decision needs to start with a break-even calculation, not an
enthusiasm for fine-tuning.

**Desired outcome:**

- You have specialized models handling high-volume recurring tasks
at materially lower per-invocation cost than general-purpose
foundation models.
- You have a customization pipeline that captures decision
patterns from production and refreshes models on a scheduled
cadence.
- You validate decision quality with A/B testing against
foundation models before routing production traffic to a
customized model.
- You track inference cost savings and decision quality side by
side so positive ROI is provable rather than assumed.

**Common anti-patterns:**

- Fine-tuning on synthetic data that misrepresents production task
distributions, causing underperformance that offsets cost
savings through lower task completion rates.
- Applying customization to low-volume task categories where
training costs exceed projected inference savings, wasting
effort on optimization that doesn't reach positive ROI.
- Treating customization as a one-time project without continuous
adaptation, allowing specialized models to drift as workload
patterns change.
- Routing production traffic to customized models without A/B
testing against foundation models, risking quality degradation
that undermines cost savings.
- Deploying customized models without instrumenting inference
latency, token costs, and quality metrics, reducing the risk of
validation that the expected cost reduction materialized.

**Benefits of establishing this best
practice:**

- Fine-tuned smaller models achieve comparable accuracy at lower
per-invocation cost through reduced token consumption and faster
inference.
- One-time training costs amortize across thousands of
invocations, delivering compounding returns for high-volume
tasks.
- Continuous adaptation pipelines keep specialized models aligned
with evolving workload patterns rather than decaying silently.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Calculate current monthly inference cost for the target task
category using
[Amazon
Bedrock AgentCore Observability](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/observability.html), estimate the reduction
from a smaller customized model, and compare against one-time
customization costs plus ongoing refresh. When monthly inference
costs exceed $500 and task volume exceeds 10,000 invocations per
month, customization typically reaches break-even within 6 to 12
months. Make the break-even explicit: (one-time training cost +
quarterly refresh cost × planning horizon in quarters) divided by
monthly inference savings. For a $5,000 training run that saves
$400 per month, break-even lands at month 13, which is acceptable
for workloads with multi-year lifespans but not for experimental
projects.

[Knowledge
distillation](https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models.html) transfers capability from a large teacher
model to a smaller student model at lower per-invocation cost. The
training data should come from production invocation logs filtered
for high-confidence, successful completions. Parameter-efficient
fine-tuning methods like QLoRA quantize base model weights to
four-bit precision and train only adapter parameters, making
single-GPU fine-tuning viable for smaller teams.
[Amazon
Bedrock model customization](https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models.html) jobs and
[Amazon SageMaker AI AI Training Jobs](https://docs.aws.amazon.com/sagemaker/latest/dg/train-model.html) with QLoRA support fine-tuning
without managing training infrastructure, and
[Amazon
Bedrock Custom Model Import](https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html) brings the results into Amazon
Bedrock for serving.

Validation helps prevent quality regressions that occur from these
cost optimizations. With
[Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html), you can split production traffic
between foundation and customized models during A/B testing, and
[Amazon
Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html) runs LLM-as-a-Judge
assessments against both arms. Accept quantization only when
accuracy loss stays within your acceptable quality threshold on
task success rate. Treat customization as a pipeline: periodically
extract high-quality examples from production logs, schedule
quarterly refresh jobs, and gate promotion on A/B validation so
drift doesn't compound silently between refreshes.

### Implementation steps

- **Conduct a customization cost-benefit
analysis:** Calculate current monthly inference
costs for high-volume task categories, identify where
training costs amortize within your planning horizon, and
compare fine-tuning investment (training compute plus
ongoing maintenance) against projected cumulative inference
savings.
- **Curate training data from production
logs:** Extract high-quality examples from
production invocation logs by filtering for invocations with
low error rates and acceptable latency using AgentCore
Observability metrics. Target 500 to 1,000 examples per task
category. Query Amazon CloudWatch for invocations where
latency falls within the p50 to p90 range and error_type is
absent, review a sample manually to verify quality, and
store the curated dataset in Amazon S3.
- **Run distillation or
fine-tuning:** Use
[Amazon
Bedrock model customization](https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models.html) jobs or
[Amazon SageMaker AI AI Training Jobs](https://docs.aws.amazon.com/sagemaker/latest/dg/train-model.html) with QLoRA, and validate
using
[Amazon
Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html) against a held-out test
set.
- **Import and A/B test customized
models:** Use
[Amazon
Bedrock Custom Model Import](https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html) and deploy through
[Amazon
Bedrock AgentCore Runtime](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/agents-tools-runtime.html), routing a traffic slice to
the customized model before promoting it to handle
production volume.
- **Schedule quarterly refresh
jobs:** Automate training data extraction and
retraining on a quarterly cadence, with A/B validation as
the promotion gate to catch drift at each refresh rather
than at annual review.

## Resources

**Related best practices:**

- [AGENTCOST02-BP01
Architect tiered model selection for cost-performance
optimization](agentcost02-bp01.html)
- [AGENTCOST02-BP02 Cost
optimize token consumption through efficient prompt
engineering](agentcost02-bp02.html)
- [AGENTCOST05-BP01
Establish agent-level reasoning cost tracking and
attribution](agentcost05-bp01.html)

**Related documents:**

- [Model
customization in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models.html)
- [Amazon
Bedrock Custom Model Import](https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html)
- [Amazon
Bedrock AgentCore Evaluations](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations.html)
- [Evaluate
models in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation-judge.html)
- [Economics
for agentic AI on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-economics/index.html)
- [Guidance
for Cost Analysis and Optimization with Amazon Bedrock
Agents](https://aws.amazon.com/solutions/guidance/cost-analysis-and-optimization-with-amazon-bedrock-agents/)

**Related videos:**

- [AWS re:Invent 2024 - Mastering model choice: The 3-step Amazon
Bedrock advantage (AIM391)](https://www.youtube.com/watch?v=Vu91YwZxskY)

**Related examples:**

- [GitHub:
awslabs/amazon-bedrock-agentcore-samples - Evaluations
tutorials](https://github.com/awslabs/amazon-bedrock-agentcore-samples/tree/main/01-tutorials/07-AgentCore-evaluations)

**Related services:**

- [Amazon
Bedrock](https://aws.amazon.com/bedrock/)
- [Amazon
Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/)
- [Amazon SageMaker AI AI](https://aws.amazon.com/sagemaker-ai/)
- [Amazon S3](https://aws.amazon.com/s3/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentcost02-bp04.html*

---
