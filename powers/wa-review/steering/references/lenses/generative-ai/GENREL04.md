# GENREL04 — Prompt management

**Pillar**: Reliability  
**Best Practices**: 2

---

# GENREL04-BP01 Implement a prompt catalog

Prompt catalogs store and manage prompts and prompt versions. They
act as a reliable store for prompts for generative AI workloads.

**Desired outcome:** When
implemented, this best practice improves the reliability of your
generative AI workload by creating a central store for prompts that
can be used for generative AI workloads.

**Benefits of establishing this best
practice:**
[Manage
change through automation](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel-dp.html) - Implementing a prompt catalog
helps to automate the process of deploying and rolling back prompt
versions.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Prompt catalogs function as a centralized system for
developing, testing, and managing prompts. Implement a prompt
catalog to maintain different versions of prompts. Prompts
should be released to a live version once passing the
appropriate testing thresholds and benchmarks. In the case
where a prompt results in unexpected or undesirable behavior,
a prompt catalog enables the ability to roll back to the
previous version.

Additionally, maintain versioned information on hyperparameter
ranges for prompts. Prompt behavior can change drastically
when tuning hyperparameters such as temperature, top_p, or
top_k. Value ranges for these hyperparameters should be paired
with and validated against prompt versions as part of the
prompt engineering process.

Prompt catalogs should maintain test results for a prompt
against several model versions. A given foundation model can
have several versions, and prompt test results for each model
version can vary accordingly. Consider developing a catalog
that maintains prompt versions for each of the available
models.

### Implementation steps

- Design catalog structure:

Define prompt metadata schema (like version, author, and purpose)
- Create categorization system for different prompt types
- Establish naming conventions and tagging standards
- Define access control requirements

- Implement version control:

Set up version tracking for prompts
- Create changelog management process
- Define rollback procedures
- Establish backup and recovery processes

- Create testing framework:

Define success criteria for prompts
- Establish validation procedures
- Create test suites for different use cases
- Set up automated testing pipelines

- Configure prompt metadata:

Document hyperparameter ranges
- Track performance metrics
- Record model compatibility
- Maintain usage statistics

- Establish governance processes:

Define approval workflows
- Create audit trails
- Set up review procedures
- Implement quality controls
- Codify in your organizations AI usage or policy document

## Resources

**Related best practices:**

- [REL07-BP01](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_adapt_to_changes_autoscale_adapt.html)
- [REL08-BP02](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_tracking_change_management_functional_testing.html)
- [REL08-BP04](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_tracking_change_management_immutable_infrastructure.html)

**Related documents:**

- [AWS re:Invent 2023
- Prompt Engineering Best Practices for LLMs on Amazon Bedrock
(AIM377)](https://www.youtube.com/watch?v=jlqgGkh1wzY)

**Related examples:**

- [Amazon Bedrock Prompt Management is now Available in GA](https://aws.amazon.com/blogs/machine-learning/amazon-bedrock-prompt-management-is-now-available-in-ga/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/genrel04-bp01.html*

---

# GENREL04-BP02 Implement a model catalog

Model catalogs store and manage model versions. They act as a
reliable store for models which may need to be deployed or rolled
back at any time. They also facilitate decoupled deployment
automation.

**Desired outcome:** When
implemented, this best practice improves the reliability of your
generative AI workload by helping to make sure the deployed model is
the appropriate model for the given use case.

**Benefits of establishing this best
practice:**
[Manage
change through automation](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel-dp.html) - Implementing a model catalog
helps to automate the process of deploying and rolling back model
versions.

**Level of risk exposed if this best practice
is not established:** Low

## Implementation guidance

Model catalogs provide a centralized location to review
models, model versions, and model cards. Traditionally, model
catalogs are meant to store model artifacts developed by
customers. Foundation models are rarely developed from
scratch, and as a result, foundation model catalogs should
maintain first-party models, third-party models, and custom
models developed from third-party models.

Consider implementing a model catalog for foundation models
that records and tracks model access, model versions, and
model card information. Maintain a model catalog in your
environment to track available models. Model catalogs should
provide a central location for model management, particularly
if there is a need to roll back to a particular model or model
version.

AI policy documents should provide clear details regarding the
usage, maintenance, and updating of the model catalog. The AI
policy document is intended to be the central authority for
operational questions pertaining to AI workloads and
supporting infrastructure. Keep this document up to date with
the appropriate materials necessary to scale the usage of the
model catalog throughout the organization.

### Implementation steps

- Set up catalog structure:

Create model classification system (by type, purpose, and provider)
- Define model metadata schema
- Establish versioning conventions
- Design access control framework

- Configure model tracking:

Record model lineage and dependencies
- Track model versions and updates
- Document model customizations
- Maintain performance benchmarks

- Implement model cards:

Define required model information
- Document model capabilities and limitations
- Record training data characteristics
- Specify intended use cases and constraints
- Include ethical considerations and biases

- Establish model governance:

Create model approval workflows
- Define deployment procedures
- Set up model monitoring
- Implement security controls
- Track model usage and access

- Create maintenance procedures:

Define model update process
- Establish deprecation policies
- Create archival procedures
- Set up backup and recovery

- Implement validation framework:

Create model testing procedures
- Define acceptance criteria
- Set up performance benchmarking
- Establish quality gates

## Resources

**Related best practices:**

- [REL04-BP02](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_prevent_interaction_failure_loosely_coupled_system.html)
- [REL07-BP01](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_adapt_to_changes_autoscale_adapt.html)

**Related documents:**

- [Amazon Bedrock API Reference](https://docs.aws.amazon.com/bedrock/latest/APIReference/welcome.html)
- [Amazon Bedrock Marketplace](https://docs.aws.amazon.com/bedrock/latest/userguide/amazon-bedrock-marketplace.html)
- [Find
serverless models with the Amazon Bedrock model catalog](https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/model-catalog.html)
- [Bring
your own endpoint](https://docs.aws.amazon.com/bedrock/latest/userguide/bedrock-marketplace-bring-your-own-endpoint.html)

**Related examples:**

- [Amazon Bedrock Marketplace: Access over 100 foundation models in one
place](https://aws.amazon.com/blogs/aws/amazon-bedrock-marketplace-access-over-100-foundation-models-in-one-place/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/genrel04-bp02.html*

---
