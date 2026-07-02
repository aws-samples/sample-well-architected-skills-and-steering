**Pillar**: Performance Efficiency

# FSIPERF05: How do you select and optimize generative AI components for your workload?

Selecting and optimizing generative AI components requires
defining your use case requirements—including accuracy
thresholds, latency constraints, and compliance needs—then
evaluating foundation models using automated benchmarks and
task-specific criteria before optimizing through prompt
engineering or fine-tuning. This enables you to build
generative AI systems that deliver reliable business value
while meeting the rigorous standards required for production
deployment, particularly in regulated industries like
financial services.

## FSIPERF05-BP01 Define a ground truth data set of prompts and responses for financial services use cases

For financial services applications using generative AI,
develop a ground truth dataset that captures domain-specific
prompts and expected responses. This dataset should include
scenarios relevant to financial applications such as
regulatory adherence queries, transaction anomaly detection,
risk assessment, and customer service interactions common in
financial institutions.

**Implementation steps:**

- Define a series of prompts and expected responses specific
to financial services use cases.
- Create a structured dataset that organizes these
prompt-response pairs by business domain (like banking,
trading, and risk management).
- Store this dataset in a secure object storage or database
with appropriate access controls given the sensitive
nature of financial data.
- Develop a testing harness that can evaluate model
performance against these financial services scenarios.

## FSIPERF05-BP02 Select and customize models appropriate for financial services use cases

When implementing generative AI models in financial services
workloads, evaluate model performance against
domain-specific requirements including regulatory adherence,
accuracy in financial terminology, and consistency in risk
assessment. Consider model customization through fine-tuning
or continuous pre-training to improve performance on
financial domain knowledge and financial
institution-specific scenarios.

**Implementation steps:**

- Test multiple models against your financial services
ground truth dataset.
- Consider customizing models using techniques like
fine-tuning to improve performance on financial tasks.
- Evaluate model response consistency and accuracy,
particularly for regulated processes.
- Consider model distillation techniques for deploying
smaller, more efficient models in production that maintain
accuracy for specific financial tasks.

## FSIPERF05-BP03 Optimize vector stores for financial data retrieval

Financial services applications often require high-precision
data retrieval from large datasets of financial information,
regulatory documents, or transaction histories. Optimize
vector databases to enhance the retrieval accuracy and speed
when used in conjunction with generative AI models.

**Implementation steps:**

- Test different chunking strategies for financial
documents, considering their specialized structure.
- Select appropriate approximate nearest neighbor (ANN)
algorithms based on the precision and recall requirements
for financial use cases.
- Optimize vector dimensions based on the complexity and
specificity of financial information.
- Implement hierarchical indices that allow efficient
navigation from general financial concepts to specific
details.
- Regularly test and monitor performance metrics including
latency, throughput, and accuracy.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsiperf05.html*
