# MLSUS02 — ML problem framing

**Pillar**: Sustainability  
**Best Practices**: 2

---

# MLSUS02-BP01 Consider AI services and pre-trained models

Using AI services and pre-trained models can significantly reduce
the resources needed for machine learning workloads, enabling you to
quickly implement AI capabilities without developing custom models
from scratch.

**Desired outcome:** You identify
opportunities to use managed AI services or pre-trained models
instead of building custom models, reducing the environmental impact
of training and deploying ML solutions while accelerating time to
market. By using existing capabilities through APIs or fine-tuning
pre-trained models, you minimize computational resources required
for data preparation, model training, and deployment.

**Common anti-patterns:**

- Building custom models from scratch when suitable managed
services already exist.
- Collecting and processing large datasets unnecessarily when
pre-trained models could be utilized.
- Ignoring transfer learning opportunities that could reduce
training time and computational resources.
- Overlooking model optimization techniques that could reduce
inference resource requirements.

**Benefits of establishing this best
practice:**

- Reduced environmental impact through decreased computational
resource usage.
- Lower operational costs for ML development and deployment.
- Faster time-to-market for ML-powered solutions.
- Access to state-of-the-art models without specialized ML
expertise.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

When developing machine learning solutions, evaluate whether you
truly need to build a custom model or if existing services and
pre-trained models can meet your requirements. Many common use
cases like image recognition, natural language processing, or
recommendation systems can use pre-built capabilities available
through APIs. These managed services handle the underlying
infrastructure, data processing, and model maintenance, reducing
both environmental impact and operational overhead.

If fully managed services don't meet your specific requirements,
consider starting with pre-trained models that you can fine-tune
with your data. This approach, known as transfer learning, allows
you to benefit from models that have already undergone
resource-intensive training on large datasets. By fine-tuning, you
can achieve similar or better performance than training from
scratch while using significantly fewer computational resources.

For example, instead of training a computer vision model from
scratch, you could use a pre-trained image recognition model from
Amazon Rekognition or fine-tune a model available through
SageMaker AI JumpStart with your specific images. This approach
reduces the carbon footprint associated with extensive model
training while delivering high-quality results.

### Implementation steps

- **Assess your ML use case
requirements**. Before developing an ML solution,
clearly define your requirements and success criteria.
Understand the specific problem you're trying to solve, the
data you have available, and the performance metrics that
matter for your application.
- **Explore AWS AI services**.
[AWS AI services](https://aws.amazon.com/machine-learning/ai-services/) provide ready-to-use capabilities through
APIs for common ML tasks. These services include
[Amazon Rekognition](https://aws.amazon.com/rekognition/) for image and video analysis,
[Amazon Comprehend](https://aws.amazon.com/comprehend/) for natural language processing,
[Amazon
Forecast](https://aws.amazon.com/forecast/) for time-series forecasting, and
[Amazon Personalize](https://aws.amazon.com/personalize/) for personalization and recommendations.
- **Evaluate foundation models in Amazon
Bedrock**.
[Amazon
Bedrock](https://aws.amazon.com/bedrock/) provides serverless access to leading
foundation models from AI companies like Anthropic, Cohere,
AI21 Labs, and Amazon's own Nova models through a single
API. These models can handle tasks like text generation,
summarization, chatbots, and content creation without
requiring model training.
- **Explore pre-trained models from AWS Marketplace**.
[AWS Marketplace](https://aws.amazon.com/marketplace/b/c3714653-8485-4e34-b35b-82c2203e81c1) offers over 1,400 ML-related assets that
you can subscribe to, including pre-trained models for
various industry-specific use cases that can be deployed
with minimal configuration.
- **Leverage SageMaker AI
JumpStart**.
[SageMaker AI
JumpStart](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-jumpstart.html) provides pre-trained, open-source models
for a wide range of problem types to get started with
machine learning. You can incrementally train and fine-tune
these models before deployment, reducing the computational
resources needed compared to training from scratch.
- **Consider Hugging Face
models**.
[Hugging
Face with Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/hugging-face.html) enables you to use
thousands of pre-trained transformer models for NLP,
computer vision, and audio tasks. These models can be
fine-tuned with your specific data to achieve high-quality
results with minimal training.
- **Implement efficient fine-tuning
techniques**. When customizing pre-trained models,
use efficient fine-tuning methods like parameter-efficient
fine-tuning (PEFT), low-rank adaptation (LoRA), or
quantization to minimize computational resources while
maintaining performance.
- **Monitor resource usage and
optimize**. After deploying your solution,
continuously monitor its resource consumption and
performance. Look for opportunities to optimize through
model compression, quantization, or pruning to further
reduce computational requirements.
- **Leverage expanded pre-trained model
libraries**. Use the expanded
[SageMaker AI
JumpStart](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-jumpstart.html) catalog which now includes broader
selection of pre-trained models and industry-specific
solutions, reducing the need for custom model development
and associated computational resources.
- **For generative AI workloads,
implement retrieval-augmented generation (RAG)**.
For generative AI applications requiring domain-specific
knowledge, consider using
[retrieval-augmented
generation](https://aws.amazon.com/what-is/retrieval-augmented-generation/) with SageMaker AI JumpStart foundation models
instead of fine-tuning large models, which can significantly
reduce computational resources while improving accuracy.

## Resources

**Related documents:**

- [AWS AI Services](https://aws.amazon.com/machine-learning/ai-services/)
- [SageMaker AI
JumpStart pretrained models](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-jumpstart.html)
- [Choose
the best data source for your Amazon SageMaker AI training
job](https://aws.amazon.com/blogs/machine-learning/choose-the-best-data-source-for-your-amazon-sagemaker-training-job/)
- [Pre-trained
machine learning models available in AWS Marketplace](https://aws.amazon.com/marketplace/solutions/machine-learning/pre-trained-models)
- [Resources
for using Hugging Face with Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/hugging-face.html)
- [Optimize
AI/ML workloads for sustainability: Part 2, model
development](https://aws.amazon.com/blogs/architecture/optimize-ai-ml-workloads-for-sustainability-part-2-model-development/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlsus02-bp01.html*

---

# MLSUS02-BP02 Select sustainable Regions

Choose the Regions where you implement your workloads based on both
your business requirements and sustainability goals.

**Desired outcome:** You select AWS Regions that align with your organizational sustainability
objectives while meeting your business requirements. By choosing
Regions with renewable energy sources and lower carbon intensity,
you reduce the environmental impact of your machine learning
workloads while maintaining optimal performance for your business
needs.

**Common anti-patterns:**

- Selecting Regions based solely on proximity without considering
environmental impact.
- Ignoring renewable energy availability when deploying machine
learning workloads.
- Deploying workloads across multiple Regions without considering
their carbon footprints.

**Benefits of establishing this best
practice:**

- Alignment with organizational sustainability goals and ESG
initiatives.
- Enhanced reputation as an environmentally responsible
organization.
- Potential cost savings through efficient Region selection.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

When deploying your machine learning workloads, Region selection
plays a crucial role in meeting both your operational requirements
and sustainability goals. While factors such as latency, data
residency, and service availability remain important,
incorporating sustainability considerations into your Region
selection process can minimize your environmental impact. AWS is
continuously expanding its renewable energy projects globally,
making it increasingly possible to host your workloads in Regions
powered by sustainable energy sources.

The cloud offers significant sustainability advantages compared to
on-premises deployments due to higher utilization rates, more
energy-efficient infrastructure, and AWS' commitment to renewable
energy. By selecting Regions thoughtfully, you can further enhance
these sustainability benefits while still meeting your business
needs.

### Implementation steps

- **Understand your business
requirements first**. Identify the non-negotiable
requirements for your workload, including data sovereignty
regulations, compliance-aligned needs, latency requirements,
and service availability in specific Regions. Create a
shortlist of Regions that meet these baseline requirements.
- **Research AWS renewable energy
projects**. Use the
[Amazon
Around the Globe](https://sustainability.aboutamazon.com/about/around-the-globe?energyType=true) resource to identify Regions that
are near Amazon renewable energy projects. AWS achieved
powering its operations with
[100%
renewable energy](https://www.aboutamazon.com/news/sustainability/amazon-renewable-energy-goal) in 2023, seven years ahead of their
original 2030 commitment.
- **Consider the grid's carbon
intensity**. Look for Regions where the electrical
grid has lower published carbon intensity. This information
may be available through regional utility reports or
sustainability documentation. Lower carbon intensity means
reduced emissions even for non-renewable energy sources.
- **Evaluate the trade-offs**.
When selecting Regions, consider potential trade-offs
between sustainability goals and business requirements such
as latency or availability. In some cases, minor performance
trade-offs may be acceptable to achieve significant
sustainability improvements.
- **Monitor sustainability
metrics**. After deployment, track relevant
sustainability metrics to verify that your Region selection
is delivering the expected environmental benefits. Consider
implementing dashboards with key performance indicators
(KPIs) for sustainability tracking.
- **Review and adjust
periodically**. As AWS adds more renewable energy
projects and as your business requirements evolve,
periodically reassess your Region selections to continually
align with your sustainability goals.

## Resources

**Related documents:**

- [AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/)
- [Delivering
on net-zero carbon by 2040](https://sustainability.aboutamazon.com/about/around-the-globe)
- [Climate
solutions](https://sustainability.aboutamazon.com/about/the-climate-pledge)
- [AWS Well-Architected Framework - Sustainability Pillar](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)
- [How
to select a Region for your workload based on sustainability
goals](https://aws.amazon.com/blogs/architecture/how-to-select-a-region-for-your-workload-based-on-sustainability-goals/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/mlsus02-bp02.html*

---
