# GENREL05 — Distributed availability

**Pillar**: Reliability  
**Best Practices**: 3

---

# GENREL05-BP01 Load-balance inference requests across all regions of availability

Inference to a foundation model may be available over a local or
large area of availability. Verify that you have resources
available across that area to service inference requests
reliably regardless of where they are coming from.

**Desired outcome:** When
implemented, this best practice improves the reliability of your
generative AI workload by creating a highly available
environment for serving inference requests.

**Benefits of establishing this best
practice:**
[Scale
horizontally to increase aggregate workload availability](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel-dp.html)
- Load-balanced inference requests across horizontally scaled
infrastructure enable inference requests to be serviced evenly
across a region of availability.

**Level of risk exposed if this best
practice is not established:** Medium

## Implementation guidance

Use load balancing and multi-Region deployment strategies to
distribute inference requests across multiple AWS Regions and
Availability Zones. This helps maintain consistent performance
and availability in the face of regional disruptions or
network issues. Consider using Amazon Bedrock's cross-Region
inference profiles to route requests to the nearest available
endpoint. For self-hosted models on Amazon SageMaker AI,
implement a multi-AZ deployment with an Amazon SageMaker AI
Inference Endpoint configured for auto-scaling to
automatically distribute and scale traffic across Regions.

This strategy provides improved reliability, reduced risk of
single points of failure, and better geographic coverage for
global users. Potential trade-offs include increased network
latency and operational complexity.

### Implementation steps

- Configure Amazon Bedrock cross-Region inference profiles
or deploy self-hosted models on Amazon SageMaker AI
Inference Endpoints across multiple Availability Zones.
- Set up an Amazon SageMaker AI Inference Endpoint with
auto-scaling enabled to distribute traffic based on
health and latency.
- Implement health checks and automated failover to
maintain availability.
- Monitor performance metrics like latency, error rates,
and throughput across Regions.

## Resources

**Related best practices:**

- [REL04-BP01](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_prevent_interaction_failure_identify.html)
- [REL10-BP01](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_fault_isolation_multiaz_region_system.html)

**Related documents:**

- [Supported Regions and models for inference profiles](https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles-support.html)

**Related examples:**

- [Getting Started with cross-Region inference in Amazon Bedrock](https://aws.amazon.com/blogs/machine-learning/getting-started-with-cross-region-inference-in-amazon-bedrock/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/genrel05-bp01.html*

---

# GENREL05-BP02 Replicate embedding data across all regions of availability

Inference to a foundation model may be available over a local availability region, or could
be a large region of availability. Make sure your data is available across all regions of
availability to adequately service inference requests.

**Desired outcome:** When implemented, this best practice improves
the reliability of your generative AI workload by validating that models have access to the
appropriate data to service inference requests across an entire Region of availability.

**Benefits of establishing this best
practice:**
[Scale
horizontally to increase aggregate workload availability](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel-dp.html) -
Data replication across a region of availability enables horizontal
scaling of the data access infrastructure and supports consistent
serving of inference requests.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Replicate the data required for generative AI workloads, such
as embeddings and knowledge bases, and make that data readily
available across all designated Regions. This helps prevent
data access from becoming a bottleneck and maintains
consistent performance for users regardless of their location.
Use solutions like Amazon S3 cross-Region replication, Amazon OpenSearch Service cross-cluster replication, and AWS Glue
data pipelines to distribute data efficiently.

Consider data sovereignty requirements and regulatory
restrictions that may limit your ability to freely replicate
data, including embeddings, across all Regions. Carefully
review the data residency and compliance needs for your
specific use case and workload. Implement data distribution
strategies that respect these constraints, such as keeping
embeddings within a defined geographic area or using
Region-specific data stores.

Replicating data across Regions can incur additional storage
and data transfer costs. Optimize data partitioning and
compression to minimize the overall storage footprint. Use
Amazon S3 Intelligent Tiering to automatically move less
frequently accessed data to more cost-effective storage
classes. Replicating data provides improved data availability
and reduced latency for users. If done properly, this practice
helps you maintain compliance with data sovereignty
regulations. Trade-offs may include increased costs and
potential consistency challenges within the allowed Regions.

### Implementation steps

- Assess data sovereignty requirements and regulatory
constraints for your generative AI workload, including
the distribution of embeddings.
- Identify the Regions where you can freely replicate
embeddings and other data based on your compliance
needs.
- Set up cross-Region replication for embedding data
stores like Amazon S3 and Amazon OpenSearch Service
within the allowed Regions.
- Implement data ingestion pipelines using AWS Glue to
keep the allowed Regions synchronized for embeddings and
other data.
- Configure monitoring and alerting to detect data
replication issues and compliance violations.
- Optimize data partitioning, compression, and storage
tiering to minimize the cost of cross-Region data
replication.

## Resources

**Related best practices:**

- [REL04-BP01](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_prevent_interaction_failure_identify.html)
- [REL07-BP01](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_adapt_to_changes_autoscale_adapt.html)
- [REL10-BP01](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_fault_isolation_multiaz_region_system.html)

**Related documents:**

- [Supported
Regions and Models for inference profiles](https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles-support.html)

**Related examples:**

- [Ensure
availability of your data using cross-cluster replication with
Amazon OpenSearch Service](https://aws.amazon.com/blogs/big-data/ensure-availability-of-your-data-using-cross-cluster-replication-with-amazon-opensearch-service/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/genrel05-bp02.html*

---

# GENREL05-BP03 Verify that agent capabilities are available across all regions of availability

Agents require supporting infrastructure to service requests from
foundation models. Using agents across a region of availability
requires the supporting infrastructure to be available in that
region.

**Desired outcome:** When
implemented, this best practice improves the reliability of your
generative AI workload by verifying that agents have access to the
appropriate supporting infrastructure such as APIs or functions, so
they may service a wider region of availability.

**Benefits of establishing this best
practice:**
[Scale
horizontally to increase aggregate workload availability](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel-dp.html) -
Data replication across a region of availability horizontally scales
data access infrastructure, enabling foundation models to
consistently service inference requests across a region of
availability.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Agents for Amazon Bedrock can be made available across
regions, so long as the models and supporting infrastructure
exist in the desired regions. Amazon Bedrock Agents make API
calls on behalf of a user. Once deployed to a new region,
these agents must have access to the same or
regionally-equivalent API. Consider deploying your APIs across
multiple regions behind a CloudFront distribution with
latency-based routing. When possible, leverage Amazon Route 53
with latency-based routing to direct traffic within your VPC
(and on the Amazon backbone) rather than taking private
traffic public to route to an internal service. If your agent
is not making calls to a foundation model using a cross-region
inference profile, be sure to configure model access in all
required regions.

When using agents in your generative AI architecture, make the
supporting infrastructure, such as APIs and functions,
available across all Regions where your agents are deployed.
This involves replicating the necessary components and
configuring appropriate routing mechanisms to maintain
consistent agent functionality regardless of user location.

### Implementation steps

- Deploy supporting agent infrastructure (APIs, functions)
in primary and secondary Regions.
- Implement latency-based routing or similar mechanisms to
distribute agent requests.
- Verify that agents can access the required resources in
all Regions.
- Monitor agent performance and resource utilization
across Regions.

## Resources

**Related best practices:**

- [REL04-BP01](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_prevent_interaction_failure_identify.html)
- [REL07-BP01](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_adapt_to_changes_autoscale_adapt.html)
- [REL10-BP01](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_fault_isolation_multiaz_region_system.html)

**Related documents:**

- [Latency-based
routing](https://docs.aws.amazon.com/Route%C2%A053/latest/DeveloperGuide/routing-policy-latency.html)

**Related examples:**

- [Using
latency-based routing with Amazon CloudFront for a
multi-Region active-active architecture](https://aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-latency.html/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/genrel05-bp03.html*

---
