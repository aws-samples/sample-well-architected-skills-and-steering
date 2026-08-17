# Sustainability

**Pillar**: Sustainability  
**Questions**: 18

---

# FSISUS01: How do you select the most sustainable Regions in your area?

The choice of Region for your workload significantly affects its KPIs, including
performance, cost, and carbon footprint. To effectively improve these KPIs, you should
choose Regions for your workloads based on both business requirements and sustainability
goals.

## FSISUS01-BP01 Select a Region with lower environmental impact that meets your business and compliance considerations

### Prescriptive guidance

The following guidance is provided to aid your selection of most sustainable
Regions in your area:

- Shortlist potential Regions based on the following topics:

Data security and privacy issues
- Regulatory compliance requirements
- The operational efficiency of your workloads
- Local data sovereignty concerns (see FSISUS02)
- A number of services and features that optimize sustainability

- Select Regions by market-based or location-based methods in line with your
financial services industry's internal relevant sustainability guidelines that are
used to track and to compare your organization's year-to-year emissions.
- Wherever possible, choose a Region that provides better than 95% renewable
energy, using the market-based method and low grid carbon intensity, as well as
using a typical location-based method.

**Generative AI considerations**

- Select Regions with lower carbon intensity for generative AI model training and
inference workloads.
- Consider AWS Regions that offer specialized generative AI instances with
improved performance per watt.
- Evaluate Region-specific availability of managed generative AI services like
Amazon Bedrock to reduce infrastructure overhead.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsisus01.html*

---

# FSISUS02: How do you address data sovereignty regulations for location of sustainable Region?

While selection of low-carbon Regions is generally recommended for processing of
financial data, sometimes data residency requirements stipulate the use of higher carbon
storage.

## FSISUS02-BP01 Run workloads and store restricted data in required country and unrestricted in sustainable Region selected by following SUS01 guidance

### Prescriptive guidance

The following guidance provides insights into data sovereignty regulations.

- Review data sovereignty regulations and identify workloads and data that can be
run in sustainable Regions. You may need to separate your data and processing to
take advantage of data and processes using lower carbon resources where data
residency is not required, while accessing higher carbon resources when data
residency is a requirement.
- Choose a sustainable Region following the guidance provided in FSISUS01.
- Run your workloads and store data whenever you are not restricted to specific
locations using more sustainable Regions.

- Balance data residency requirements with sustainable generative AI
infrastructure placement.
- Verify that generative AI training data and model artifacts adhere to regional
data sovereignty while optimizing for carbon footprint.
- Consider federated learning approaches for generative AI models when data
cannot cross jurisdictional boundaries.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsisus02.html*

---

# FSISUS03: How do you select a Region to optimize financial services workloads for sustainability?

Financial institutions must focus on sustainability within their cloud operating model
to reduce their impact on the environment and to encourage sustainable practices. Focusing
on these areas helps financial institutions adapt their workloads to financial services
industry sustainability best practices, to adopt new environmentally friendly technology
trends, and to plan for the business impacts of potential future regulatory requirements.
The selection of the best Region might be driven by taking into account a variety of
reasons.

## FSISUS03-BP01 Choose Regions with services and hardware required for financial service organizations that maximize carbon footprint reductions

### Prescriptive guidance

Recommended guidance for customer architecture includes:

- Develop a list of all services required by financial services workloads.
- Select a Region using guidance from FSISUS01-BP01.
- Develop a cross-reference of sustainable Regions chosen according to the [services that are offered within each Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/) as well as the variety and
types of sustainable hardware offered in the Region.
- Prioritize Regions offering energy-efficient generative AI services and
sustainable hardware for financial services AI workloads.
- Select Regions with renewable energy sources for computationally intensive
generative AI model training.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsisus03.html*

---

# FSISUS04: How do you prioritize business critical functions over non-critical functions?

Determine what is defined as a business-critical process and workload, and protect and
prioritize it. Model and prioritize individual functions and workloads by recording relevant
metadata, such as interdependencies, SLAs for particular flows, and nuances of user access.

## FSISUS04-BP01 Actively manage each business function and the allocation and configuration of resources

**Prescriptive guidance**

- Use [Amazon ECS Spot](https://aws.amazon.com/ec2/spot/) compute for
non-critical workloads such as end-of-month reconciliations.
- Use [Amazon EC2 Dedicated
Hosts](https://aws.amazon.com/ec2/dedicated-hosts/) queues for priority jobs such as order initiation.
- Use [Amazon ECR Lifecycle
Policies](https://docs.aws.amazon.com/AmazonECR/latest/userguide/LifecyclePolicies.html) for ephemeral ETL data such as ingestion ledgers.
- Develop architecture strategies that use built-in queueing and buffering to
offload non-critical tasks.

## FSISUS04-BP02 FSI workloads serve the highest common denominator of application demands

Systems in financial services are built to serve the highest level of performance for
retention, availability, and integrity. This leads to workloads that often exceed
performance expectations or might not be respectful of ancillary or critical jobs and
workflows. Breaking down a system into its component parts allows for a more fine-grained
view of resource consumption and the trade-offs possible to balance SLAs against your
sustainability goals.

### Prescriptive guidance

Provide prioritization advice to customers on the following topics:

- **Prioritize at the organizational level:** Determine
what is defined as a business-critical process and workload and protect and
prioritize it.
- **Prioritize at the SCP or OU level:** Restrict AWS
usage-based metrics on your Organizational Units' (OU) profiles and requirements.
Batch-running processes that have extended SLAs can have dedicated accounts and
permissions to restrict and reduce their carbon impact; for

example, select serverless preferences, choose specific instance types, or operate
during specific processing hours. Development and test instances should have enforced
central guardrails to limit Amazon EBS attachments or automatically pause and resume
resources as needed.

- **Prioritize at the account level:** Model and
prioritize individual functions and workloads by recording relevant metadata, such
as interdependencies, SLAs for particular flows, and nuances of user access. For
example, investigations and warm access commonly take longer at a bank than its
typical 35-day retention period.
- **Prioritize at the resource or tag level:** Use tags
to group and aggregate the management and reporting of resources. You may only have
one critical flow but you likely monitor dozens of processes and receive millions of
Event Notifications. Create a prioritization schema to determine which process
matter most to your workload operations.
- **Prioritize at the job or object level:** Not all jobs
are born equal. Use mechanisms such as graceful termination of non-critical jobs and
active workload management to help you prioritize at the job and object levels.
- **Prioritize resource allocation for critical generative AI
applications in financial services:** Implement right-sized generative AI
models for different business criticality levels - use smaller, efficient models for
non-critical functions. Evaluate if generative AI is necessary or if simpler
approaches can achieve the same outcome. FSISUS05: How do you define, review, and
optimize network access patterns for sustainability?

Assess and optimize network access patterns for sustainability. Pay attention to
redundant layers and redirects or patterns generating excessive and unnecessary data
movement.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsisus04.html*

---

# FSISUS05: How do you define, review, and optimize network access patterns for sustainability?

Assess and optimize network access patterns for sustainability. Pay attention to
redundant layers and redirects or patterns generating excessive and unnecessary data
movement.

## FSISUS05-BP01 Analyze network access patterns to identify the places that your customers are connecting from

**Prescriptive guidance**

Remove redundant layers and redirects, use pagination and local caching mechanisms to
reduce data movement, and consider separating workloads that serve different users.

## FSISUS05-BP02 Avoid common architectural misconfigurations

In financial services organizations, it's common to hairpin large amounts of traffic
through on- premises networks, have largely redundant layers of control using trusted
private networks, and sometimes include untrusted public traffic.

A simple example of this is using [AWS Direct Connect](https://docs.aws.amazon.com/directconnect/) where performance is often degraded as FSI organizations insist
that all inbound and outbound traffic originates from their network.

Another common mistake is to serve both OLAP and OLTP workloads from the same
database or cluster, which normally span two or more completely different geographic
locations. Both patterns generate excessive and unnecessary data movement.

### Prescriptive guidance

Identify poor architectural choices and risky configurations as good candidates for
remediation.

Assess your workflows from the perspective of varying demand over time, so select
scalable AWS services over fixed ones.

Do not underestimate your network requirements, especially for peak loads. Provide
sufficient failover resources to support your operations in case of partial outages.

Optimize generative AI inference patterns to minimize data transfer and network
overhead.

Implement edge inference for generative AI models where appropriate to reduce
network traffic.

Use efficient prompt engineering to reduce token lengths and network utilization.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsisus05.html*

---

# FSISUS06: How do you monitor and minimize resource usage for financial services workloads?

Monitor and analyze your financial services' usage patterns to minimize resource usage.
Identify services that are not required to be operational at all times or that can be scaled
up and down based on user access patterns.

## FSISUS06-BP01 Actively monitor your FSI resource usage

- Monitor and analyze your financial services' usage patterns to minimize resource
usage.
- Identify services that are not required to always be operational, or that can be
scaled up and down based on user access patterns.
- For example, many consumer-based services can be scaled down or turned off during
off-peak hours.

### Prescriptive guidance

- Remove underutilized software modules and combine these functions into other
software services.
- Minimize the average resource demand required per unit-of-work using automatic
scaling services, serverless transaction processing, or shutting down your resources
when usage patterns permit.
- Use queue-driven architectures, pipeline management, and On-Demand Instance
workers to maximize your utilization for batch processing.
- Implement comprehensive monitoring of generative AI resource consumption using
Amazon CloudWatch.
- Track token lengths of prompts and model responses to measure generative AI
utilization.
- Identify idle time periods to scale down or suspend generative AI inference
endpoints.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsisus06.html*

---

# FSISUS07: How do you optimize batch processing components for sustainability?

Because batch processing is often found within many workloads across financial systems,
verify that the minimum number of resources are consumed by batching transactions together
while meeting your customer SLA and system requirements.

## FSISUS07-BP01 Optimize your batch processing systems

Because batch processing is often found within many workloads across financial
systems, verify that the minimum number of resources are consumed by batching transactions
together while meeting your customer SLA and system requirements.

### Prescriptive guidance

- Queue up several requests together that don't require immediate processing.
- Increase serialization to flatten utilization across your pipeline.
- Modify the capacity of individual components to prevent idling resources
waiting for input.
- Create buffers and establish rate limiting to smooth the consumption of
external services.
- Use the most efficient available hardware and services to optimize your
software.
- If possible, schedule jobs during times of day where carbon intensity for power
is lowest.
- Use managed spot training for generative AI model training to utilize spare EC2
capacity efficiently.
- Implement parameter-efficient fine-tuning (PEFT) techniques like LoRA to reduce
computational requirements.
- Optimize generative AI batch inference jobs using serverless architectures.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsisus07.html*

---

# FSISUS08: How do you optimize your resource usage?

Review and optimize your resource usage by implementing either a pub/sub or pull
mechanism instead of relying on a polling approach.

## FSISUS08-BP01 Use event-driven architecture

Implement either a pub/sub or pull mechanism instead of using a polling approach.

### Prescriptive guidance

- Implement event-driven architecture where possible to avoid idling of resources
running and waiting for state changes.
- If event-driven architecture is not possible, modify the capacity of individual
components to prevent idling downstream resources waiting for input.
- Avoid polling APIs or queues, instead have components and services subscribe to
events or be notified of changes to reduce the idling of resources.
- Implement auto scaling and serverless architectures for generative AI
workloads.
- Use managed generative AI services like Amazon Bedrock to optimize resource
utilization.
- Apply model optimization techniques like quantization and pruning.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsisus08.html*

---

# FSISUS09: How do you optimize areas of your code that use the most resources?

Analyze and optimize your code's efficiency to improve resource utilization.

## FSISUS09-BP01 Monitor and optimize areas of code that are the most compute resource-intensive

### Prescriptive guidance

- Use [CodeGuru](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/welcome.html) and [Amazon Q Developer](https://aws.amazon.com/q/developer/) to optimize your code's efficiency.
- If possible, choose the most efficient OS and programming languages to run your
code.
- Remove unnecessary code such as modules that perform sorting or formatting.
- Optimize generative AI model inference code using efficient model
architectures.
- Implement model distillation to create smaller, task-specific generative AI
models.
- Use specialized instances like EC2 Inferentia for generative AI workloads.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsisus09.html*

---

# FSISUS10: Have you selected the storage class with the lowest carbon footprint?

Data is at the heart of strategic innovations for the financial services industry. This
can have many use cases ranging from providing hyperpersonalised experiences for customers,
training machine learning models to better understand risk and fraud detection. Each use
case requires different levels of data availability, processing, and storage and therefore
varies in storage technologies from transactional databases, to data lakes and data
warehouses. These come with various considerations from a sustainability perspective.

## FSISUS10-BP01 Balance your data performance requirements against its carbon footprint

### Prescriptive guidance

To balance data performance requirements against its carbon footprint:

- Define proxy metrics to monitor the business outcome of the data-involved
service in relation to their environmental impact. An example proxy metric could be
efficiency of the AI/ML service to help detect fraud faster (with the associated
cost saving) and the carbon footprint of training and storing the data. These proxy
metrics then become the vehicle to balance your performance requirements against its
carbon footprint. Proxy metrics can be collected by importing AWS Cost and Usage
Report as well as Amazon CloudWatch metrics into Amazon S3 and monitored using Amazon Athena and Quick.
- Use the right storage class for Amazon S3 Storage Classes based on the data
performance requirements. The storage class impacts the environmental impact of the
dataset through its access patterns and its architecture. For example, in [Amazon S3
One Zone-IA](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html), energy and server capacity are reduced because data is stored
only within one Availability Zone. Amazon

S3 Storage Classes can be configured at the object level and a single bucket can
contain objects stored across all of the storage classes.

- Learn more about [Amazon S3 Storage
Classes](https://aws.amazon.com/s3/storage-classes/) and their use cases.
- You can also use Amazon S3 lifecycle policies to transition objects automatically
between storage classes without application changes. In general, you must make a
trade-off between resource efficiency, access latency, and reliability when
considering these storage mechanisms.
- For storage systems that are a fixed size, such as Amazon EBS or Amazon FSx, monitor
the available storage space and automate storage allocation on reaching a threshold.
You can use Amazon CloudWatch to collect and analyze different metrics for [Amazon EBS](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using_cloudwatch_ebs.html) and [Amazon FSx](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/monitoring-cloudwatch.html).
- Avoiding the backup of unnecessary data can help lower cost and reduce the
storage resources used by the workload. Only back up data that has business value or
is needed to satisfy compliance requirements. Use [AWS Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html) for Amazon EFS or
Amazon Glacier Storage options for backup of infrequently accessed data.

Data types may include the following:

- Real-time analytics for financial services, including banking, payments,
insurance, and markets.
- Unstructured data such as biometrics, facial images, and documents.
- Structured data like fund movements or, transaction attempts.

## FSISUS10-BP02 Separate data into hot, warm, and cold storage

### Prescriptive guidance

- Implement a data classification policy to understand its criticality to
business outcomes and choose the right energy-efficient storage tier. Determine
criticality, confidentiality, integrity, and availability of data based on risk to
the organization.

Evaluate your data characteristics and access pattern to collect the key
characteristics of your storage needs. Key characteristics to consider include:

**Data type:** Structured, semistructured,
unstructured
- **Data growth:** Bounded, unbounded
- **Data durability:** Persistent, ephemeral,
transient
- **Access patterns:** Reads or writes,
frequency, spiky, or consistent

- Use these requirements to group data into one of the data classification tiers
that you adopt. For more detail on data classification categories, see the [Data
Classification whitepaper](https://docs.aws.amazon.com/whitepapers/latest/data-classification/data-classification.html).
- [AWSAWS Glue Data Catalog](https://docs.aws.amazon.com/glue/latest/dg/components-overview.html#data-catalog-intro) lets you store, annotate, and share metadata in the AWS
cloud while providing comprehensive audit and governance capabilities, to
periodically audit your environment for untagged and unclassified data and tag the
data appropriately.
- Optimize storage for generative AI training data and model artifacts using
appropriate storage classes.
- Implement data purification filters to reduce unnecessary generative AI
training data storage.
- Use columnar formats and compression for generative AI datasets.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsisus10.html*

---

# FSISUS11: Do you store processed data or raw data?

## FSISUS11-BP01 Use processed data to reduce your storage footprint

Often raw data from your data sources may include a large number of observations from
streaming data sources that continually produce data or include large amounts of redundant
data from a variety of sources. You can reduce your storage requirements by first
processing the raw data, then storing only the results. Unless you have a raw data
retention compliance policy or requirement, you can purge the raw data automatically
shortly after processing to reduce your data storage requirements.

Store processed generative AI training data rather than raw data when compliance
allows. Implement efficient vector storage strategies for generative AI applications.
Optimize vector lengths for embedded tokens in generative AI systems.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsisus11.html*

---

# FSISUS12: What is your process for benchmarking instances for existing workloads?

Maximizing your instance utilization is an effective and quantifiable practice that
helps you meet your sustainability goals. But reaching an ideal utilization state is a
process — it's uncommon for customers to achieve optimal instance utilization on their first
attempt. Define a process to monitor resource utilization over time so you can benchmark
performance and make the necessary adjustments to your workloads.

## FSISUS12-BP01 Set appropriate instance usage goals that reflect your sustainability requirements

**Prescriptive guidance**

- Instance utilization goals differ for every company, but you can use common
metrics that are broadly applied regardless of company size, age, industry, or domain
like carbon emissions and energy consumption.
- You can use these metrics to set goals like an ideal utilization percentage, or a
maximum idle instance threshold.
- It's important to set measurable instance utilization goals that apply within the
context of your business to see and iterate over time.
- Setting appropriate goals provides guidance and justification for every decision
that your organization makes as it collectively works toward a sustainable usage
state.

## FSISUS12-BP02 Track your overall process in achieving your goals

**Prescriptive guidance**

- It's harder to achieve goals if you are not aware of your progress and if you
don't know where you are, you're unable to pivot to make the right changes in reaching
your goal.
- Do this by setting a regular cadence with the appropriate stakeholders to
identify the current state and creating action plans to iterate, if necessary.
- AWS provides tools to help your track your overall progress such as the [AWS
Customer Carbon Footprint Tool](https://aws.amazon.com/aws-cost-management/aws-customer-carbon-footprint-tool/) to report on emissions from your AWS usage,
and specifically Amazon EC2, which follows Greenhouse Gas (GHG) Protocol standards.
- You can analyze the changes in your emissions over time and forecast how your
emissions change across your sustainability journey.

## FSISUS12-BP03 Monitor your individual instance performance metrics

### Prescriptive guidance

- Establish a process to monitor individual instances to help you to use two
major optimization approaches:

Using only what you need
- Right-sizing what you do need

- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) provides a unified view
of metrics that you can use to benchmark instance performance. Use both the default
and custom metrics to gather the data you need to make informed decisions.
- For example, you can use the IsIdle default metric for Amazon EMR to identify
clusters for termination. This process helps your organization adopt more optimal
instances types since newer generation instances typically have better
energy-to-performance ratios.
- Run performance tests specific to the processor to better understand your
workloads' needs to help lower your workload's instance count by evaluating whether
workloads are properly fitted to an instance family by performance metrics other
than CPU and reduce unnecessary instances.
- Establish a process to also track supply to demand with [Amazon EC2 Auto Scaling](https://aws.amazon.com/ec2/autoscaling/). This helps keep your scaling policies
dynamic and relevant to changes to your workload.
- **Implementation guidance:** Hpc 7g instance may be the
obvious contender for a grid computing workload, but network constraints could cause
the need for more instances. Consider switching to C7gn. Do not go after cores, as
memory bandwidth, faster I/O, and higher clock speeds may be more beneficial for
highly intensive financial simulations. For example, on AWS Graviton, since each
vCPU is its own physical core, verify that workloads are running instances beyond
60% CPU to breakage to best assess threshold and limit over provisioning instances.
- **Service recommendations:** Use the following services
to achieve these goals:

[AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/)
- [Amazon CloudWatch
metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/working_with_metrics.html)
- [AWS Graviton Performance Runbook](https://github.com/aws/aws-graviton-getting-started/blob/main/perfrunbook/graviton_perfrunbook.md)

### Generative AI considerations

- Use SageMaker AI AI Inference Recommender to benchmark optimal instance types for
generative AI models.
- Benchmark AWS Trainium instances for energy-efficient generative AI model
training.
- Evaluate EC2 Inferentia instances for sustainable generative AI inference.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsisus12.html*

---

# FSISUS13: Can you complete workloads over more time while not violating your maximum SLA?

How do you avoid load spikes to reduce the provisioned capacity required for your
workload?

Flattening the workload demand curve can help you to reduce the provisioned capacity
for a workload and reduce its environmental impact. In other words, if you can afford to
spread out the load over a longer period of time, rather than having a higher peak in a
shorter span of time, then you lower the overall resource demand for the workload. By doing
so, you lower the overall amount of provisioned capacity, and thus lower overall energy
consumption to meet the workload's demand.

## FSISUS13-BP01 Do not complete a customer transaction in the shortest time when not required by end users

**Prescriptive guidance**

If your workload does not have time-sensitive requirements, consider running them
during times when public demand is lower. This distributes energy consumption to flatten
the resource demand curve. Evaluate your workload requirements to assess if you are able
to make this adjustment.

## FSISUS13-BP02 Introduce jitter to your scheduled tasks

### Prescriptive guidance

- Assess if your scheduled tasks can be distributed to run at random times during
an hour or throughout the day. This minimizes the highs of peak demand load and
spreads it across the day instead. Avoid using the same start minute of scheduled
tasks. Doing so creates high demand for resources at a specific time, which
introduces stress on energy consumption. Staggering job start times avoids load
spikes and creates time-flexible workloads.
- Evaluate whether highly intensive computational workloads such as financial
simulation can be spread over time and run fewer instances to maximize renewable
energy availability. If a grid computing workload is using a third-party scheduler,
prioritize workloads that need to provide calculations for regulators and trading
desks that need information prior to markets opening, so workloads that are not
urgent can be pushed off and worked on at a consistent rate to maximize renewable
energy availability. Additionally, verify that a proper fault tolerance framework is
implemented, as restarting a launch can increase launch time and energy consumption.
- Use [Amazon Simple Queue Service (Amazon SQS)](https://aws.amazon.com/sqs/) achieve your
goal.
- Balance generative AI model response time requirements with energy efficiency.
- Implement cost-aware prompting strategies that may take slightly longer but use
fewer resources.
- Use distributed generative AI inference when time permits to optimize resource
utilization.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsisus13.html*

---

# FSISUS14: Do you have multi-architecture images for grid computing systems?

Multi-architecture image support for a particular workload makes it easier for you to
build different images and thus different architectures and operating systems from the same
source and refer to them all by the same abstract manifest. The manifest specifies the
layers of system content that make up the image as well as its runtime characteristics and
configuration. Having a multi-architecture image increases the flexibility of the workload
thus increases the opportunity to use hardware that may be more sustainable.

## FSISUS14-BP01 Use instances with higher energy efficiency

**Prescriptive guidance**

- [AWS Graviton-based instances](https://docs.aws.amazon.com/whitepapers/latest/aws-graviton-performance-testing/what-is-aws-graviton.html) use up to 60% less energy than comparable
EC2 instances.

## FSISUS14-BP02 Design applications that can use different Amazon EC2 instance types

**Prescriptive guidance**

- This is what we would call a flexible workload. In contrast, inflexible workloads
rely only on a few instance types. These instances types may be less energy efficient
than others.
- Flexible workloads are ideal for Spot Instances. Running workloads on Spot
Instances is generally considered more energy efficient than On-Demand Instances
because Spot is overhead required for the Amazon EC2 On-Demand service to run.
- Use Amazon EC2's spare capacity with Spot Instances to extract the same value, which
increases the total value generated from the Amazon EC2 environment as a whole.

## FSISUS14-BP03 Adopt a serverless, event-driven architecture

### Prescriptive guidance

- Consider using a serverless, event-driven architecture to maximize overall
resource utilization. Serverless architecture removes the requirement to run and
maintain physical servers since AWS handles this on your behalf.
- The cost of serverless architectures generally correlates with the level of
usage, thus increases your workload's cost efficiency.
- **Implementation guidance:** Maximize energy efficiency
as well as availability by building multi- architecture workloads that can run on a
variety of Spot Instances. It is important to account for error precision when
expanding compiler options on varying processors.
- **Service recommendations:** Use the following services
to achieve your goal:

[Amazon Simple Queue Service and Amazon EC2 Spot Instances](https://aws.amazon.com/blogs/compute/running-cost-effective-queue-workers-with-amazon-sqs-and-amazon-ec2-spot-instances/)
- [AWS CodeBuild](https://aws.amazon.com/blogs/devops/creating-multi-architecture-docker-images-to-support-graviton2-using-aws-codebuild-and-aws-codepipeline/)
- [AWS Batch](https://aws.amazon.com/batch/)
- [AWS Parallel
Cluster](https://aws.amazon.com/hpc/parallelcluster/)

- Determine which of your workloads is suitable for use of floating-point
accuracy, performance, and efficiency. Consider testing with a cluster of instances
to see how well it performs at scale.
- For intensive financial simulations and calculations, test the number of bits
that are required to achieve your floating point precision and consider reducing
number of bits by selecting different floating-point formats, including bfloat16,
that's supported by AWS Graviton.
- Develop multi-architecture generative AI model containers for different
instance types.
- Support both GPU and AWS Trainium instances for generative AI workloads.
- Optimize generative AI models for different hardware architectures (like x86,
ARM, or Graviton).

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsisus14.html*

---

# FSISUS15: What is your testing process for workloads that require floating point precision?

## FSISUS15-BP01 Minimize the bit count while maintaining precision

### Prescriptive guidance

Floating point precision is a way to represent real numbers in a finite binary
format. It stores a number in a fixed-width field with the intent to reduce the memory
bandwidth and storage requirements compared to double-precision arithmetic results.
Although double-precision can sometimes lead to more accurate results, single-precision
calculations can be faster and thus

reduce overall energy consumption for particular workloads. Determine which of your
workloads is suitable for use of floating-point accuracy, performance, and efficiency.
Consider testing with a cluster of instances to see how well it performs at scale.

### Implementation guidance:

- For intensive financial simulations and calculations, test the number of bits
that are required to achieve your floating point precision and consider reducing
number of bits by selecting different floating-point formats, including bfloat16,
that's supported by AWS Graviton.
- Using floating point [Quantization](https://aws.amazon.com/blogs/machine-learning/reduce-ml-inference-costs-on-amazon-sagemaker-with-hardware-and-software-acceleration/), you can represent numbers using lower bit-count integers or
floating point numbers without incurring a significant loss in accuracy.
Specifically, you can reduce resource usage by replacing the parameters in your
workload with (1) half-precision (16 bit), (2) bfloat16 (16 bit, but the same
dynamic range as 32 bit), or 8-bit integers instead of the usual single-precision
floating-point (32 bit) values.
- **Service recommendations:** Use the following services
to achieve your goal.

[AWS Batch](https://aws.amazon.com/batch/)
- [AWS Parallel
Cluster](https://aws.amazon.com/hpc/parallelcluster/)
- [Graviton3](https://aws.amazon.com/about-aws/whats-new/2022/05/amazon-ec2-c7g-instances-powered-aws-graviton3-processors/)

- Test generative AI models with reduced precision (quantization) to maintain
accuracy while reducing resource consumption.
- Validate generative AI model performance with different floating-point
precisions.
- Use mixed-precision training for generative AI models to optimize resource
usage.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsisus15.html*

---

# FSISUS16: Do you achieve a judicious use of development resources?

## FSISUS16-BP01 Verify that all development resources are dedicated to an active project or team

Often, project test environments and resources are set up in anticipation of an
upcoming project. If that project is cancelled or never commences, some development
resources could be orphaned from their original projects. To mitigate this, establish a
regular review of all test resources to reduce these missing projects.

Dedicate generative AI development resources to active projects. Implement regular
reviews of generative AI model training and development environments. Foster a culture of
sustainable generative AI practices through team education.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsisus16.html*

---

# FSISUS17: How do you minimize your test, staging, sandbox instances?

## FSISUS17-BP01 Use infrastructure as code (IaC) code base to snapshot your environment allowing you to decommission test infrastructure

### Prescriptive guidance

Reducing the number, frequency, and use of test and staging environments can reduce
your environmental impact. If you use [infrastructure as code (IaC)](https://docs.aws.amazon.com/whitepapers/latest/introduction-devops-aws/infrastructure-as-code.html) with AWS Event Engine or Workshop Studio to
snapshot your environments, you can break down the infrastructure once your testing is
complete. This allows you to reduce the unneeded resources. If the test environment is
required later, you can use IaC to restore it when needed.

Instead of creating separate instances to test several environments, use snapshots
to test only the required workload using the same instance. You can queue your testing
based on development priorities to reduce the use of test and staging instances.

Use infrastructure as code (IaC) to snapshot generative AI development
environments. Implement shared generative AI model testing environments rather than
individual instances. Schedule automatic shutdown of unused generative AI development
instances.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsisus17.html*

---

# FSISUS18: How do you define the minimum requirement in response time for customers in order to maximize your green SLA?

## FSISUS18-BP01 Use a green SLA

### Prescriptive guidance

The Institute of Electronics and Electrical Engineers standards body has created a
set of recommendations known as the *green SLA* that offsets the
responsiveness of system to meet customer requirements against the need to reduce
environmental impacts. For more information, see [Providing green SLAs in High
Performance Computing clouds](https://ieeexplore.ieee.org/document/6604503).

- Implement green SLAs that balance generative AI response time with
environmental impact.
- Define acceptable generative AI model response times that optimize for
sustainability.
- Use timeout mechanisms on generative AI agent workflows to prevent excessive
resource consumption.
- These considerations integrate the sustainability best practices from the
Generative AI Lens with each existing FSI sustainability pillar, verifying that
generative AI implementations in financial services maintain both regulatory
adherence and environmental responsibility.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsisus18.html*

---

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
