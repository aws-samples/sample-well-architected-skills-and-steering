# ADVSUS06 — Hardware and services

**Pillar**: Sustainability  
**Best Practices**: 2

---

# ADVSUS06-BP01 Shut down resources when not in use, and implement energy-efficient machine learning models

Resources for machine learning may have real-time demands that
fluctuate or not be needed at certain times, such as when data can
be processed as a batch. Set machine learning workloads to respond
to demand in real-time, including turning off or shutting down
resources when not needed. Use available tools to optimize the
compute resources and models used for machine learning workloads.

## Implementation guidance

- Organizations can use machine learning to draw insights on
correlation and causation from data sets in order to
optimize advertising activities. However, resources for data
preparation, identity resolution, data collaboration, and
creation of machine learning models do not need to run 24/7.
Optimize and shut down these resources when not in use to
reduce carbon emissions.
- When using
[Amazon SageMaker AI](https://aws.amazon.com/sagemaker/), customers can take multiple steps to
optimize their compute usage:

Use Graviton-based instances when possible.
- [Amazon SageMaker AI Inference Recommender](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-recommender.html) can specify the
most performant instance type.
- [Inference
optimization techniques](https://docs.aws.amazon.com/sagemaker/latest/dg/model-optimize.html) can be applied to
SageMaker AI models.
- SageMaker AI can dynamically adjust the number of instances
provisioned for a model in response to changes in your
workload by
using [scaling
policies](https://docs.aws.amazon.com/sagemaker/latest/dg/endpoint-auto-scaling.html).

- Use AI chips that provide the highest performance for
training and inference, such as
[AWS Tranium](https://aws.amazon.com/ai/machine-learning/trainium/) and
[AWS Inferentia](https://aws.amazon.com/ai/machine-learning/inferentia/).

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advsus06-bp01.html*

---

# ADVSUS06-BP02 Continuously monitor and right-size your AWS resources, and use the minimum resources required to meet your workload needs

Monitoring workloads allows you to optimize and elastically scale
your workloads to meet demand. Using serverless offerings can also
help you automatically scale to reduce resource usage and improve
the ability to meet sustainability targets. Consider how your
requirements change based on advertising campaigns, and take
advantage of the elasticity and agility of cloud to optimize your
resource usage.

## Implementation guidance

- Advertising SSPs and DSPs should use [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) dashboards for visibility into active connections and bytes process
per endpoint to drive resource usage.
- Use [AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/) to identify
the optimal resources for workloads. For example, when using [Amazon EMR](https://aws.amazon.com/emr/) to analyze ad impression and click-through data, Compute Optimizer can
recommend the optimal EC2 instance types based on utilization data.
- Monitor boot time for improvements, such as pre-installing dependent libraries in
container images for bidder processing.
- For downstream analytics and reporting of bidder transactions, use [Amazon Kinesis](https://aws.amazon.com/pm/kinesis/) Data Streams and Amazon Data Firehose to send
data to Amazon S3. The use of a data stream enables faster responses and allows independent
scaling for components of the real-time bidding architecture.
- Ad servers and click-through servers should be in [Auto Scaling
groups](https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html) to automatically scale in when load is reduced.

## Key AWS services

- [AWS Lambda](https://aws.amazon.com/lambda/)
- [Amazon DynamoDB](https://aws.amazon.com/dynamodb/)
- [Karpenter](https://aws.amazon.com/blogs/aws/introducing-karpenter-an-open-source-high-performance-kubernetes-cluster-autoscaler/) (Open-Source Kubernetes cluster autoscaler built with AWS)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advsus06-bp02.html*

---
