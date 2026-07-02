# GENPERF04 — Vector store optimization

**Pillar**: Performance Efficiency  
**Best Practices**: 2

---

# GENPERF04-BP01 Test vector embeddings for latency and relevant performance

Optimizing a data retrieval system for generative AI may have
more to do with data architecture and meta-data than the
foundation model selected. This best practice encourages high
data quality and data architecture to accelerate data-driven
generative AI workloads.

**Desired outcome:** When
implemented, this best practice facilitates expedient data
storage and access, with accurate and relevant data retrieval.

**Benefits of establishing this best
practice:**
[Consider
mechanical sympathy](https://docs.aws.amazon.com/wellarchitected/latest/framework/perf-dp.html) - Optimizing a data storage system
for a generative AI workload can be as simple as changing vector
indexes or modifying the chunking strategy. Familiarize yourself
with how the system performs data storage and retrieval to best
optimize the database.

**Level of risk exposed if this best
practice is not established:** Medium

## Implementation guidance

Optimizing vector store features for generative AI requires a
holistic approach to search architecture. Begin with effective
chunking and embedding strategies, as these have greater
effects on performance and can only be addressed before data
enters the data store. There are several popular chunking
strategies to select from, including fixed-size, hierarchical,
or semantic. Some vector base solutions like Amazon Bedrock
allow for custom chunking strategies that can be defined with
an AWS Lambda function. There are several factors to consider
when selecting a chunking strategy, including the data being
chunked and how that data is to be retrieved. Evaluate the
available options when configuring a vector store, testing
document retrieval performance against each chunking strategy.

Search algorithms form the backbone of how vectors are
retrieved from vector stores. When selecting an approximate
nearest neighbor (ANN) algorithm, consider the trade-offs
between accuracy, speed, memory usage, and scalability. Common
options include locality-sensitive hashing (LSH) for fast
indexing, hierarchical navigable small world (HNSW) for high
accuracy, inverted file index (IVF) for balance, and product
quantization (PQ) for compact storage. Benchmark multiple
algorithms with your specific dataset to find the optimal
balance based on your prioritized performance metrics.

Organize indices hierarchically, with top-level indices for
general information and lower-level indices for detailed data.
This approach generally outperforms single indices.

For search optimization in AI-driven queries, focus on
machine-to-machine interactions. Implement query expansion
using AI-generated context, and shift fuzzy matching towards
semantic similarity. Leverage hybrid search approaches that
combine semantic understanding with traditional retrieval
techniques to enhance result relevance.

Continually monitor performance across all system components,
including embedding generation, index construction, query
processing, and result retrieval. Track latency, throughput,
and resource utilization. Prepare for scenarios where
performance bottlenecks may shift between layers as your
system scales and usage patterns change. You may have to
re-architect elements of your data storage solution based on
shifting usage patterns. Develop operational runbooks to
facilitate such changes.

Maintain data quality through regular assessments of
freshness, accuracy, and representativeness. Monitor for data
drift and implement processes for continuous data ingestion
and periodic re-embedding. Use automated checks, human review,
and AI output analysis to maintain data quality. Establish
clear governance policies, and maintain version control of
your vector store.

Remember that optimizations in one area can affect the entire
system. Stay adaptable to new techniques and algorithms to
maintain a high-performing, efficient knowledge retrieval
system that delivers accurate, contextually relevant
information for your generative AI application.

### Implementation steps

- Identify the most important performance KPI for this
workload (for example, accuracy, speed, memory usage, or
scalability). Consider implementing a custom search
algorithm that supports this KPI.
- Organize indices based on a hierarchy, where more detail
is introduced towards the bottom of the hierarchy.
- Establish query latency monitoring on the data retrieval
system to verify the database latency is consistently
monitored and alerted upon.
- Perform regular data quality checks, verifying that data
is assessed for quality before being placed into a
database.
- Develop an operational runbook to facilitate rapid
architecture changes to accommodate shifting usage
patterns.
- Develop an operational runbook to facilitate rapid
architecture changes to accommodate shifting usage
patterns.

## Resources

**Related best practices:**

- [PERF05-BP02](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_process_culture_use_monitoring_solutions.html)
- [PERF05-BP03](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_process_culture_workload_performance.html)

**Related documents:**

- [Working
with vector search collections](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-vector-search.html)
- [Vector
search features and limits](https://docs.aws.amazon.com/memorydb/latest/devguide/vector-search-limits.html)

**Related examples:**

- [Accelerate
performance using a custom chunking mechanism with Amazon Bedrock](https://aws.amazon.com/blogs/machine-learning/accelerate-performance-using-a-custom-chunking-mechanism-with-amazon-bedrock/)
- [Amazon Bedrock Knowledge Bases now supports advanced parsing, chunking, and query reformulation giving greater control of accuracy in RAG based applications](https://aws.amazon.com/blogs/machine-learning/amazon-bedrock-knowledge-bases-now-supports-advanced-parsing-chunking-and-query-reformulation-giving-greater-control-of-accuracy-in-rag-based-applications/)
- [Amazon OpenSearch Service's vector database capabilities
explained](https://aws.amazon.com/blogs/big-data/amazon-opensearch-services-vector-database-capabilities-explained/)
- [Building
scalable, secure, and reliable RAG applications using Amazon Bedrock Knowledge Bases](https://aws.amazon.com/blogs/machine-learning/building-scalable-secure-and-reliable-rag-applications-using-amazon-bedrock-knowledge-bases/)
- [Dive
deep into vector data stores using Amazon Bedrock Knowledge
Bases](https://aws.amazon.com/blogs/machine-learning/dive-deep-into-vector-data-stores-using-amazon-bedrock-knowledge-bases/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/genperf04-bp01.html*

---

# GENPERF04-BP02 Optimize vector sizes for your use case

Embedding models may offer support for different sizes of vectors
when embedding data. Optimizing the vector size for an embedding may
introduce long-term performance gains.

**Desired outcome:** When
implemented, this best practice helps verify that vector sizes are
optimized for a specific use case, which can lead to improved
performance over time.

**Benefits of establishing this best
practice:**
[Consider
mechanical sympathy](https://docs.aws.amazon.com/wellarchitected/latest/framework/perf-dp.html) - Optimizing vector sizes for supported
vector embedding models may improve performance of your application.
Familiarize yourself with how your selected embedding model performs
embeddings and retrievals when optimizing.

**Level of risk exposed if this best practice
is not established:** Low

## Implementation guidance

When embedding unstructured data into a vector database, it's
important to test multiple embedding models with various
vector sizes to optimize data retrieval and identify
performance trade-offs. While there's a general relationship
between vector size and accuracy within a model family, this
correlation isn't universal across all embedding models. The
performance of your embeddings depends on several factors: the
specific data you're encoding, the chosen embedding model, and
the vector size used within that model. Consider checking
popular leaderboards like
[HuggingFace's
Massive Text Embedding Benchmark (MTEB) Leaderboard](https://huggingface.co/mteb/leaderboard)
when selecting an embedding model.

Start with a more compact encoding, and increase the vector
size if warranted by your use cases to improve accuracy or
minimize loss. Consider the nature of your dataset and how
focused the topics or language are. The more narrow and deep
the content, the more likely fine-tuning is to improve
accuracy while potentially reducing vector size.

For use cases where higher latency is acceptable, larger
vector sizes within a given model may offer more accuracy and
response nuance. Conversely, for low-latency requirements,
smaller vector sizes typically result in faster retrieval.
However, it's crucial to note that a well-tuned model with
smaller dimensions (like 256) can sometimes outperform a more
generic model with larger dimensions (1024 or greater) in both
accuracy and speed.

Keep in mind that some models offer a limited range of
permissible vector dimensions. This is particularly true for
managed embedding model access through Amazon Bedrock. A wider
variety of embedding models can be incorporated into a
generative AI workflow using Amazon SageMaker AI model endpoints
or SageMaker AI JumpStart. Always test and evaluate the
performance of different models and vector sizes with your
specific dataset to find the optimal balance between accuracy
and latency for your use case.

### Implementation steps

- Identify the most important performance KPI for this
workload (like accuracy, speed, memory usage, or
scalability).
- Determine the number of vector options supported by your
selected embedding model and design experiments meant to
test each option.

Experiment on a variety of data to get a clear
determination of which embedding size is best for this
workload.
- Consider self-hosting an open-source embedding model
using Amazon SageMaker AI model endpoints if available
embedding options are not sufficient.

- Run the experiment and determine the most performant
embedding model for this scenario.

## Resources

**Related best practices:**

- [PERF03-BP01](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_data_use_purpose_built_data_store.html)
- [PERF03-BP02](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_data_evaluate_configuration_options_data_store.html)
- [PERF03-BP03](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_data_collect_record_data_store_performance_metrics.html)
- [PERF03-BP04](https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_data_implement_strategies_to_improve_query_performance.html)

**Related documents:**

- [Customizing
your knowledge base](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-how-customization.html)
- [Working
with vector search collections](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-vector-search.html)
- [Vector
search features and limits](https://docs.aws.amazon.com/memorydb/latest/devguide/vector-search-limits.html)

**Related examples:**

- [Amazon OpenSearch Service's vector database capabilities
explained](https://aws.amazon.com/blogs/big-data/amazon-opensearch-services-vector-database-capabilities-explained/)
- [Building
scalable, secure, and reliable RAG applications using Amazon Bedrock Knowledge Bases](https://aws.amazon.com/blogs/machine-learning/building-scalable-secure-and-reliable-rag-applications-using-amazon-bedrock-knowledge-bases/)
- [Dive
deep into vector data stores using Amazon Bedrock Knowledge
Bases](https://aws.amazon.com/blogs/machine-learning/dive-deep-into-vector-data-stores-using-amazon-bedrock-knowledge-bases/)

**Related tools:**

- [HuggingFace's
MTEB Leaderboard](https://huggingface.co/spaces/mteb/leaderboard)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/genperf04-bp02.html*

---
