# MLPERF05 — Deployment

**Pillar**: Performance Efficiency  
**Best Practices**: 2

---

# MLPERF05-BP01 Evaluate cloud versus edge options for machine learning deployment

Evaluate machine learning deployment options to determine if your
application requires near-instantaneous inference results or needs
to operate without network connectivity. When the lowest possible
latency is essential, deploying inference directly on edge devices
avoids costly roundtrips to cloud API endpoints. Edge deployments
are particularly valuable for use cases like predictive maintenance
in factories, where immediate local responses are critical.

**Desired outcome:** You can make
informed decisions about where to deploy your machine learning
models based on your business requirements. You understand when to
use cloud resources for training and when to deploy optimized models
to edge devices for low-latency inference. Your edge deployments can
operate autonomously when needed while maintaining security,
performance, and the ability to update models as new data becomes
available.

**Common anti-patterns:**

- Defaulting to cloud-based inference without evaluating latency
requirements.
- Deploying models to edge devices without proper optimization,
resulting in poor performance.
- Neglecting to establish a strategy for model updates and
monitoring on edge devices.
- Overlooking security considerations for models deployed at the
edge.
- Failing to evaluate hardware constraints of edge devices before
deployment.

**Benefits of establishing this best
practice:**

- Dramatically reduced inference latency for time-sensitive
applications.
- Ability to operate ML models in environments with limited or no
connectivity.
- Lower operational costs by reducing network traffic and cloud
compute usage.
- Enhanced privacy by keeping sensitive data local to edge
devices.
- Improved resilience against network outages.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Machine learning deployments require careful consideration of
where inference should take place based on your use case
requirements. While training complex models is computationally
intensive and best suited for the cloud, inference operations
require less computing power and can often be performed directly
on edge devices.

Avoid defaulting to cloud-based inference without evaluating
latency requirements. Many organizations deploy models to edge
devices without proper optimization, resulting in poor
performance, neglect to establish a strategy for model updates and
monitoring on edge devices, overlook security considerations for
models deployed at the edge, and fail to evaluate hardware
constraints of edge devices before deployment.

When evaluating cloud versus edge deployment, consider factors
like latency requirements, connectivity constraints, data privacy
needs, and the computational capabilities of your edge devices.
For applications requiring real-time responses, such as autonomous
vehicles, industrial equipment monitoring, or smart security
systems, edge deployment reduces network latency and provides
continuous operation even during connectivity disruptions.

AWS provides comprehensive tools to optimize models for edge
deployment while maintaining the ability to train and manage those
models in the cloud. This hybrid approach gives you the best of
both worlds: powerful cloud resources for development and
optimization, with efficient edge deployment for operational
performance.

### Implementation steps

- **Assess your deployment
requirements**. Begin by clearly defining your
application's latency, connectivity, and privacy
requirements. Determine if your use case needs
millisecond-level response times, must function in
environments with unreliable connectivity, or needs to
process sensitive data locally. These factors will guide
your decision between cloud and edge deployment options.
- **Optimize models for edge
deployment**. Training and optimizing machine
learning models require massive computing resources, making
cloud environments ideal for this phase.
[Amazon SageMaker AI](https://aws.amazon.com/sagemaker/) provides powerful tools for building and
training models that can later be optimized for edge
deployment. Consider the computational constraints of your
target edge devices and select model architectures that
balance accuracy with efficiency.
- **Deploy with Amazon SageMaker AI Neo for
cross-solution compatibility**.
[Amazon SageMaker AI Neo](https://aws.amazon.com/sagemaker/neo/) enables ML models to be trained once
and run anywhere in the cloud or at the edge. The Neo
compiler reads models exported from various frameworks,
converts them to framework-agnostic representations, and
generates optimized binary code for target hardware. This
process makes your models run faster without accuracy loss.
- **Implement edge ML with AWS IoT Greengrass**.
[AWS IoT Greengrass](https://aws.amazon.com/greengrass/ml/) provides a robust solution for running
ML inferences on edge devices using cloud-trained models.
These models can be built using Amazon SageMaker AI,
[AWS Deep Learning AMIss](https://aws.amazon.com/machine-learning/amis/), or
[AWS Deep Learning Containers](https://aws.amazon.com/machine-learning/containers/). Models are stored in
[Amazon S3](https://aws.amazon.com/s3/) before deployment to edge devices.

## Resources

**Related documents:**

- [AWS IoT Greengrass](https://aws.amazon.com/greengrass/ml/)
- [Set
up Neo on Edge Devices](https://docs.aws.amazon.com/sagemaker/latest/dg/neo-getting-started-edge.html)
- [AWS Internet of
Things](https://aws.amazon.com/iot/)
- [Optimize
image classification on AWS IoT Greengrass using ONNX
Runtime](https://aws.amazon.com/blogs/iot/optimize-image-classification-on-aws-iot-greengrass-using-onnx-runtime/)

**Related videos:**

- [Machine
Learning at the Edge](https://www.youtube.com/watch?v=EAz-qAL5z2U)
- [Getting
Started Using Machine Learning at the Edge](https://pages.awscloud.com/Getting-Started-Using-Machine-Learning-at-the-Edge_2020_0202-IOT_OD.html)
- [AWS IoT Greengrass and Machine Learning at the Edge](https://www.youtube.com/watch?v=keaq6sy46ek)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlperf05-bp01.html*

---

# MLPERF05-BP02 Choose an optimal deployment option in the cloud

When deploying machine learning models in the cloud, selecting the
right deployment option is crucial for performance efficiency. By
matching your deployment method to your use case requirements for
request frequency, latency, and runtime, you can optimize both
performance and cost.

**Desired outcome:** You can deploy
your machine learning models in a way that meets your application's
needs for throughput, response time, and cost efficiency. The
selected deployment option provides the optimal balance between
performance and resource utilization while accommodating your
workload patterns.

**Common anti-patterns:**

- Deploying models on persistent endpoints regardless of traffic
patterns or workload spikes.
- Overlooking payload size and processing time requirements when
selecting deployment options.
- Using real-time inference for batch processing use cases that
don't require immediate responses.
- Failing to consider cost implications of different deployment
options.
- Not monitoring and optimizing deployment configurations after
initial setup.

**Benefits of establishing this best
practice:**

- Improved cost efficiency by matching resources to actual usage
patterns.
- Enhanced performance through selection of appropriate deployment
methods.
- Better scalability to handle varying workloads.
- Reduced operational overhead with managed deployment options.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Selecting the optimal deployment option for your machine learning
models involves understanding your use case requirements and
matching them to the capabilities of different AWS SageMaker AI
deployment services. Consider factors such as request frequency,
payload size, processing time, and response latency needs.

Avoid deploying models on persistent endpoints regardless of
traffic patterns or workload spikes. Many organizations overlook
payload size and processing time requirements when selecting a
deployment option, use real-time inference for batch processing
use cases that don't require immediate responses, and fail to
consider cost implications of different deployment options.

For time-sensitive applications requiring immediate responses,
real-time inference provides persistent endpoints, while workloads
with inconsistent traffic patterns might benefit from serverless
options that scale automatically. For larger payloads or longer
processing times, asynchronous inference is appropriate, and for
non-time-sensitive bulk processing, batch transformation offers an
efficient option.

Your deployment choice should align with your application's
operational patterns to balance performance and cost efficiency. A
chatbot requiring immediate responses would benefit from real-time
inference, while overnight batch processing of transactions might
use batch transform.

### Implementation steps

- **Evaluate your model deployment
requirements**. Begin by clearly defining your
application's requirements for inference frequency, latency
needs, payload sizes, and budget constraints. Consider how
often model predictions will be requested, how quickly
responses must be delivered, and what resource constraints
you may have.
- **Implement Amazon SageMaker AI Real-time
Inference for continuous, low-latency needs**.
Deploy models that require near-instantaneous responses and
consistent availability using
[SageMaker AI
real-time endpoints](https://docs.aws.amazon.com/sagemaker/latest/dg/realtime-endpoints.html). These fully managed endpoints
support auto-scaling and are ideal for applications like
real-time recommendation engines, chatbots, or fraud
detection systems where immediate response is critical.
- **Implement Amazon SageMaker AI
Serverless Inference for variable traffic
patterns**. For workloads with inconsistent request
patterns or idle periods between traffic spikes, use
[SageMaker AI
Serverless Inference](https://docs.aws.amazon.com/sagemaker/latest/dg/serverless-endpoints.html). This option automatically
provisions and scales compute resources based on traffic,
avoiding the need to manage server infrastructure while
optimizing costs during periods of low utilization.
- **Implement Amazon SageMaker AI
Asynchronous Inference for large payloads or long
processing**. For use cases involving large input
files (up to 1GB) or models requiring extended processing
time (up to 15 minutes), deploy using
[SageMaker AI
Asynchronous Inference](https://docs.aws.amazon.com/sagemaker/latest/dg/async-inference.html). This option queues incoming
requests and processes them when resources are available,
making it ideal for tasks like video processing, large
document analysis, or complex NLP tasks.
- **Implement Amazon SageMaker AI Batch
Transform for scheduled bulk processing**. For
non-time-sensitive workloads where predictions can be
processed in batches, such as overnight processing of
transactions or weekly sentiment analysis of customer
feedback, use
[SageMaker AI
Batch Transform](https://docs.aws.amazon.com/sagemaker/latest/dg/batch-transform.html). This option automatically
distributes workloads across compute instances and shuts
down resources when processing is complete.
- **Monitor and optimize your
deployment**. Once deployed, continuously monitor
your model's performance, resource utilization, and costs.
Use Amazon CloudWatch metrics to track invocation metrics,
errors, latency, and resource utilization. Adjust
auto-scaling configurations or switch deployment options if
your usage patterns change over time.
- **Implement security and
governance**. Incorporate proper security controls
in your model deployments, including IAM roles with least
privilege access, network isolation where appropriate, and
encryption of data in transit and at rest. Use
[Amazon SageMaker AI Role Manager](https://docs.aws.amazon.com/sagemaker/latest/dg/role-manager.html) to create persona-based IAM
roles for different ML user types (data scientists, MLOps
engineers, business analysts) with preconfigured templates
that follow least-privilege principles. For regulated
industries, implement model governance practices to track
model versions, approvals, and changes.

## Resources

**Related documents:**

- [Real-time
inference](https://docs.aws.amazon.com/sagemaker/latest/dg/realtime-endpoints.html)
- [Deploy
models with Amazon SageMaker AI Serverless Inference](https://docs.aws.amazon.com/sagemaker/latest/dg/serverless-endpoints.html)
- [Asynchronous
inference](https://docs.aws.amazon.com/sagemaker/latest/dg/async-inference.html)
- [Batch
transform for inference with Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/batch-transform.html)
- [Amazon SageMaker AI Role Manager](https://docs.aws.amazon.com/sagemaker/latest/dg/role-manager.html)
- [Deploy
models with Amazon SageMaker AI](https://sagemaker-examples.readthedocs.io/en/latest/inference/index.html)
- [Deploying
ML models using SageMaker AI Serverless Inference](https://aws.amazon.com/blogs/machine-learning/deploying-ml-models-using-sagemaker-serverless-inference-preview/)
- [Optimize
deployment cost of Amazon SageMaker AI JumpStart foundation
models with Amazon SageMaker AI asynchronous endpoints](https://aws.amazon.com/blogs/machine-learning/optimize-deployment-cost-of-amazon-sagemaker-jumpstart-foundation-models-with-amazon-sagemaker-asynchronous-endpoints/)
- [Announcing
managed inference for Hugging Face models in Amazon SageMaker AI](https://aws.amazon.com/blogs/machine-learning/announcing-managed-inference-for-hugging-face-models-in-amazon-sagemaker/)
- [Run
computer vision inference on large videos with Amazon SageMaker AI asynchronous endpoints](https://aws.amazon.com/blogs/machine-learning/run-computer-vision-inference-on-large-videos-with-amazon-sagemaker-asynchronous-endpoints/)

**Related videos:**

- [Achieve high
performance and cost-effective model deployment](https://youtu.be/gWuO0gNKlm8)
- [Amazon SageMaker AI serverless inference](https://youtu.be/KB6vLQGixjA)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlperf05-bp02.html*

---
