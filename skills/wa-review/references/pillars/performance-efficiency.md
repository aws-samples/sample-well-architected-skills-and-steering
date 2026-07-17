# Performance Efficiency — All Questions & Best Practices

This file contains all 5 WA Framework questions for the performance-efficiency pillar
and their complete best-practice content. Load this ONE file to have the entire
pillar in context at once — no need for 5 separate Read calls.

For a lightweight catalog of every BP ID across all 6 pillars, see
`references/manifest.md`.

---

## Question PERF01

# PERF 1 — How do you select appropriate cloud resources and architecture patterns?

**Pillar**: Performance Efficiency  
**Best Practices**: 7

---

# PERF01-BP01 Learn about and understand available cloud services and features

Continually learn about and discover available services and configurations that help you
make better architectural decisions and improve performance efficiency in your workload
architecture.

**Common anti-patterns:**

- You use the cloud as a collocated data center.
- You do not modernize your application after migration to the cloud.
- You only use one storage type for all things that need to be persisted.
- You use instance types that are closest matched to your current standards, but are
larger where needed.
- You deploy and manage technologies that are available as managed services.

**Benefits of establishing this best practice:** By considering new
services and configurations, you may be able to greatly improve performance, reduce cost, and
optimize the effort required to maintain your workload. It can also help you accelerate the
time-to-value for cloud-enabled products.

**Level of risk exposed if this best practice is not established:**
High

## Implementation guidance

AWS continually releases new services and features that can improve performance and
reduce the cost of cloud workloads. Staying up-to-date with these new services and features is
crucial for maintaining performance efficacy in the cloud. Modernizing your workload
architecture also helps you accelerate productivity, drive innovation, and unlock more growth
opportunities.

### Implementation steps

- Inventory your workload software and architecture for related services. Decide
which category of products to learn more about.
- Explore AWS offerings to identify and learn about the relevant services and
configuration options that can help you improve performance and reduce cost and
operational complexity.

[Amazon Web Services Cloud](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/amazon-web-services-cloud-platform.html)
- [AWS Academy](https://aws.amazon.com/training/awsacademy/)
- [What’s New with AWS?](https://aws.amazon.com/new/)
- [AWS Blog](https://aws.amazon.com/blogs/)
- [AWS Skill Builder](https://skillbuilder.aws/)
- [AWS Events and Webinars](https://aws.amazon.com/events/)
- [AWS Training and Certifications](https://www.aws.training/)
- [AWS Youtube
Channel](https://www.youtube.com/channel/UCd6MoB9NC6uYN2grvUNT-Zg)
- [AWS Workshops](https://workshops.aws/)
- [AWS
Communities](https://aws.amazon.com/events/asean/community-and-events/)

- Use [Amazon Q](https://aws.amazon.com/q/) to get relevant information and advice about services.
- Use sandbox (non-production) environments to learn and experiment with new services
without incurring extra cost.
- Continually learn about new cloud services and features.

## Resources

**Related documents:**

- [Overview of Amazon Web Services](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/introduction.html)
- [Amazon EC2 features](https://aws.amazon.com/ec2/features/)
- [Learn
step-by-step with an AWS Partner Learning Plan](https://aws.amazon.com/partners/training/aws-partner-learning-plans/)
- [AWS Training and Certification](https://aws.amazon.com/training/)
- [My learning path to become an AWS solutions architect](https://aws.amazon.com/blogs/training-and-certification/my-learning-path-to-become-an-aws-solutions-architect/)
- [AWS Architecture Center](https://aws.amazon.com/architecture/)
- [AWS Partner Network](https://aws.amazon.com/partners/)
- [AWS Solutions Library](https://aws.amazon.com/solutions/)
- [AWS Knowledge
Center](https://aws.amazon.com/premiumsupport/knowledge-center/)
- [Build modern applications on AWS](https://aws.amazon.com/modern-apps/)

**Related videos:**

- [AWS re:Invent 2023 -
What’s new with Amazon EC2](https://www.youtube.com/watch?v=mjHw_wgJJ5g)
- [AWS re:Invent 2022 -
Reduce your operational and infrastructure costs with Amazon ECS](https://www.youtube.com/watch?v=vwf0rcdXdVE)
- [AWS re:Invent 2023 - Build
with the efficiency, agility & innovation of the cloud with AWS](https://www.youtube.com/watch?v=AMrXMfYYVXs)
- [AWS re:Invent 2022 -
Deploy ML models for inference at high performance and low cost](https://www.youtube.com/watch?v=4FqHt5bmS2o)
- [This is my
Architecture](https://aws.amazon.com/architecture/this-is-my-architecture/)

**Related examples:**

- [AWS Samples](https://github.com/aws-samples)
- [AWS SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_architecture_understand_cloud_services_and_features.html*

---

# PERF01-BP02 Use guidance from your cloud provider or an appropriate partner to learn about architecture patterns and best practices

Use cloud company resources such as documentation, solutions
architects, professional services, or appropriate partners to guide
your architectural decisions. These resources help you review and
improve your architecture for optimal performance.

**Common anti-patterns:**

- You use AWS as a common cloud provider.
- You use AWS services in a manner that they were not designed
for.
- You follow all guidance without considering your business
context.

**Benefits of establishing this best
practice:** Using guidance from a cloud provider or an
appropriate partner can help you to make the right architectural
choices for your workload and give you confidence in your decisions.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

AWS offers a wide range of guidance, documentation, and resources
that can help you build and manage efficient cloud workloads. AWS
documentation provides code samples, tutorials, and detailed
service explanations. In addition to documentation, AWS provides
training and certification programs, solutions architects, and
professional services that can help customers explore different
aspects of cloud services and implement efficient cloud
architecture on AWS.

Leverage these resources to gain insights into valuable knowledge
and best practices, save time, and achieve better outcomes in the
AWS Cloud.

### Implementation steps

- Review AWS documentation and guidance and follow the best
practices. These resources can help you effectively choose
and configure services and achieve better performance.

[AWS documentation](https://docs.aws.amazon.com/) (like user guides and whitepapers)
- [AWS Blog](https://aws.amazon.com/blogs/)
- [AWS Training and Certifications](https://www.aws.training/)
- [AWS Youtube Channel](https://www.youtube.com/channel/UCd6MoB9NC6uYN2grvUNT-Zg)

- Join AWS partner events (like AWS Global Summits, AWS
re:Invent, user groups, and workshops) to learn from AWS
experts about best practices for using AWS services.

[Learn step-by-step with an AWS Partner Learning Plan](https://aws.amazon.com/partners/training/aws-partner-learning-plans/)
- [AWS Events and Webinars](https://aws.amazon.com/events/)
- [AWS Workshops](https://workshops.aws/)
- [AWS Communities](https://aws.amazon.com/events/asean/community-and-events/)

- Reach out to AWS for assistance when you need additional
guidance or product information. AWS Solutions Architects
and [AWS Professional Services](https://aws.amazon.com/professional-services/) provide guidance for solution
implementation.
[AWS Partners](https://aws.amazon.com/partners/) provide AWS expertise to help you unlock
agility and innovation for your business.
- Use
[Support](https://aws.amazon.com/contact-us/) if you need technical support to use a
service effectively.
[Our
Support plans](https://aws.amazon.com/premiumsupport/plans/) are designed to give you the right mix
of tools and access to expertise so that you can be
successful with AWS while optimizing performance, managing
risk, and keeping costs under control.

## Resources

**Related documents:**

- [AWS Architecture Center](https://aws.amazon.com/architecture/)
- [AWS Partner Network](https://aws.amazon.com/partners/)
- [AWS Solutions Library](https://aws.amazon.com/solutions/)
- [AWS Knowledge Center](https://aws.amazon.com/premiumsupport/knowledge-center/)
- [AWS Enterprise Support](https://aws.amazon.com/premiumsupport/plans/enterprise/)

**Related videos:**

- [This
is my Architecture](https://aws.amazon.com/architecture/this-is-my-architecture/)
- [AWS re:Invent 2023 - Advanced event-driven patterns with Amazon EventBridge](https://www.youtube.com/watch?v=6X4lSPkn4ps)
- [AWS re:Invent 2023 - Implementing distributed design patterns on AWS](https://www.youtube.com/watch?v=pfAlmkzyaJQ)
- [AWS re:Invent 2023 - Application architecture as code](https://www.youtube.com/watch?v=vasvpFRPx9c)

**Related examples:**

- [AWS Samples](https://github.com/aws-samples)
- [AWS SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples)
- [AWS Analytics Reference Architecture](https://github.com/aws-samples/aws-analytics-reference-architecture)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_architecture_guidance_architecture_patterns_best_practices.html*

---

# PERF01-BP03 Factor cost into architectural decisions

Factor cost into your architectural decisions to improve resource
utilization and performance efficiency of your cloud workload. When
you are aware of the cost implications of your cloud workload, you
are more likely to leverage efficient resources and reduce wasteful
practices.

**Common anti-patterns:**

- You only use one family of instances.
- You do not evaluate licensed solutions against open-source
solutions.
- You do not define storage lifecycle policies.
- You do not review new services and features of the AWS Cloud.
- You only use block storage.

**Benefits of establishing this best
practice:** Factoring cost into your decision making allows
you to use more efficient resources and explore other investments.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Optimizing workloads for cost can improve resource utilization
and avoid waste in a cloud workload. Factoring cost into
architectural decisions usually includes right-sizing workload
components and enabling elasticity, which results in improved
cloud workload performance efficiency.

### Implementation steps

- Establish cost objectives like budget limits for your cloud
workload.
- Identify the key components (like instances and storage)
that drive cost of your workload. You can use
[AWS Pricing Calculator](https://calculator.aws/#/) and
[AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/) to identify key cost drivers in your
workload.
- Understand [pricing models](https://aws.amazon.com/pricing/) in the cloud, such as On-Demand, Reserved Instances, Savings Plans, and Spot Instances.
- Use
[Well-Architected
cost optimization best practices](https://docs.aws.amazon.com/wellarchitected/latest/cost-optimization-pillar/welcome.html) to optimize these
key components for cost.
- Continually monitor and analyze cost to identify cost
optimization opportunities in your workload.

Use
[AWS Budgets](https://aws.amazon.com/aws-cost-management/aws-budgets/) to get alerts for unacceptable costs.
- Use
[AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/) or
[AWS Trusted Advisor](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/) to get cost optimization
recommendations.
- Use
[AWS Cost Anomaly Detection](https://aws.amazon.com/aws-cost-management/aws-cost-anomaly-detection/) to get automated cost
anomaly detection and root cause analysis.

## Resources

**Related documents:**

- [What is AWS Billing and Cost Management?](https://docs.aws.amazon.com/cost-management/latest/userguide/what-is-costmanagement.html)
- [Cost Optimization with AWS](https://aws.amazon.com/aws-cost-management/cost-optimization/)
- [Choosing an AWS cost management strategy](https://aws.amazon.com/getting-started/decision-guides/cost-management-on-aws-how-to-choose/)
- [A Beginner’s Guide to AWS Cost Management](https://aws.amazon.com/blogs/aws-cloud-financial-management/beginners-guide-to-aws-cost-management/)
- [A
Detailed Overview of the Cost Intelligence Dashboard](https://aws.amazon.com/blogs/aws-cloud-financial-management/a-detailed-overview-of-the-cost-intelligence-dashboard/)
- [AWS Architecture Center](https://aws.amazon.com/architecture/)
- [AWS Solutions Library](https://aws.amazon.com/solutions/)
- [AWS Knowledge Center](https://aws.amazon.com/premiumsupport/knowledge-center/)

**Related videos:**

- [This
is my Architecture](https://aws.amazon.com/architecture/this-is-my-architecture/)
- [AWS re:Invent 2023 - What’s new with AWS cost optimization](https://www.youtube.com/watch?v=EOUTf2Dxo0Y)
- [AWS re:Invent 2023 - Optimize cost and performance and track progress toward mitigation](https://www.youtube.com/watch?v=keAfy8f84E0)
- [AWS re:Invent 2023 - AWS storage cost-optimization best practices](https://www.youtube.com/watch?v=8LVKNHcA6RY)
- [AWS re:Invent 2023 - Optimize costs in your multi-account environments](https://www.youtube.com/watch?v=ie_Mqb-eC4A)

**Related examples:**

- [AWS Compute Optimizer Demo code](https://github.com/awslabs/ec2-spot-labs/tree/master/aws-compute-optimizer)
- [Cost Optimization Workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/11959269-3506-4bcb-aa2a-f257709cb8ca/en-US)
- [Cloud Financial Management Technical Implementation Playbooks](https://catalog.workshops.aws/awscff/en-US)
- [Startup optimization: Tuning application performance for maximum efficiency](https://catalog.workshops.aws/performance-tuning/en-US)
- [Serverless Optimization Workshop (Performance and Cost)](https://catalog.us-east-1.prod.workshops.aws/workshops/2d960419-7d15-44e7-b540-fd3ebeb7ce2e/en-US)
- [Scaling cost effective architectures](https://catalog.us-east-1.prod.workshops.aws/workshops/f238037c-8f0b-446e-9c15-ebcc4908901a/en-US)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_architecture_factor_cost_into_architectural_decisions.html*

---

# PERF01-BP04 Evaluate how trade-offs impact customers and architecture efficiency

When evaluating performance-related improvements, determine which
choices impact your customers and workload efficiency. For example,
if using a key-value data store increases system performance, it is
important to evaluate how the eventually consistent nature of this
change will impact customers.

**Common anti-patterns:**

- You assume that all performance gains should be implemented,
even if there are tradeoffs for implementation.
- You only evaluate changes to workloads when a performance issue
has reached a critical point.

**Benefits of establishing this best
practice:** When you are evaluating potential
performance-related improvements, you must decide if the tradeoffs
for the changes are acceptable with the workload requirements. In
some cases, you may have to implement additional controls to
compensate for the tradeoffs.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Identify critical areas in your architecture in terms of
performance and customer impact. Determine how you can make
improvements, what trade-offs those improvements bring, and how
they impact the system and the user experience. For example,
implementing caching data can help dramatically improve
performance but requires a clear strategy for how and when to
update or invalidate cached data to prevent incorrect system
behavior.

### Implementation steps

- Understand your workload requirements and SLAs.
- Clearly define evaluation factors. Factors may relate to
cost, reliability, security, and performance of your workload.
- Select architecture and services that can address your
requirements.
- Conduct experimentation and proof of concepts (POCs) to
evaluate trade-off factors and impact on customers and
architecture efficiency. Usually, highly-available,
performant, and secure workloads consume more cloud
resources while providing better customer experience. Understand the trade-offs across your workload’s complexity, performance, and cost.
Typically, prioritizing two of the factors comes at the expense of the third.

## Resources

**Related documents:**

- [Amazon
Builders’ Library](https://aws.amazon.com/builders-library)
- [Quick KPIs](https://docs.aws.amazon.com/quicksight/latest/user/kpi.html)
- [Amazon CloudWatch RUM](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM.html)
- [X-Ray
Documentation](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html)
- [Understand resiliency patterns and trade-offs to architect efficiently in the cloud](https://aws.amazon.com/blogs/architecture/understand-resiliency-patterns-and-trade-offs-to-architect-efficiently-in-the-cloud/)

**Related videos:**

- [Optimize
applications through Amazon CloudWatch RUM](https://www.youtube.com/watch?v=NMaeujY9A9Y)
- [AWS re:Invent 2023 - Capacity, availability, cost efficiency: Pick three](https://www.youtube.com/watch?v=E0dYLPXrX_w)
- [AWS re:Invent 2023 - Advanced integration patterns & trade-offs for loosely coupled systems](https://www.youtube.com/watch?v=FGKGdUiZKto)

**Related examples:**

- [Measure
page load time with Amazon CloudWatch Synthetics](https://github.com/aws-samples/amazon-cloudwatch-synthetics-page-performance)
- [Amazon CloudWatch RUM Web Client](https://github.com/aws-observability/aws-rum-web)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_architecture_evaluate_trade_offs.html*

---

# PERF01-BP05 Use policies and reference architectures

Use internal policies and existing reference architectures when
selecting services and configurations to be more efficient when
designing and implementing your workload.

**Common anti-patterns:**

- You allow a wide variety of technology that may impact the
management overhead of your company.

**Benefits of establishing this best
practice:** Establishing a policy for architecture,
technology, and vendor choices allows decisions to be made quickly.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Having internal policies in selecting resources and architecture
provides standards and guidelines to follow when making
architectural choices. Those guidelines streamline the decision-making
process when choosing the right cloud service and can help improve
performance efficiency. Deploy your workload using policies or
reference architectures. Integrate the services into your cloud
deployment, then use your performance tests to verify that you can
continue to meet your performance requirements.

### Implementation steps

- Clearly understand the requirements of your cloud workload.
- Review internal and external policies to identify the
most relevant ones.
- Use the appropriate reference architectures provided by AWS
or your industry best practices.
- Create a continuum consisting of policies, standards,
reference architectures, and prescriptive guidelines for
common situations. Doing so allows your teams to move
faster. Tailor the assets for your vertical if applicable.
- Validate these policies and reference architectures for your
workload in sandbox environments.
- Stay up-to-date with industry standards and AWS updates to
make sure your policies and reference architectures help
optimize your cloud workload.

## Resources

**Related documents:**

- [AWS Architecture Center](https://aws.amazon.com/architecture/)
- [AWS Partner Network](https://aws.amazon.com/partners/)
- [AWS Solutions Library](https://aws.amazon.com/solutions/)
- [AWS Knowledge Center](https://aws.amazon.com/premiumsupport/knowledge-center/)
- [AWS Architecture Blog](https://aws.amazon.com/blogs/architecture/category/events/reinvent/)

**Related videos:**

- [This
is my Architecture](https://aws.amazon.com/architecture/this-is-my-architecture/)
- [AWS re:Invent 2022 - Accelerate value for your business with SAP & AWS reference architecture](https://www.youtube.com/watch?v=-u3oyOy-HxU)

**Related examples:**

- [AWS Samples](https://github.com/aws-samples)
- [AWS SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_architecture_use_policies_and_reference_architectures.html*

---

# PERF01-BP06 Use benchmarking to drive architectural decisions

Benchmark the performance of an existing workload to understand how it performs on the
cloud and drive architectural decisions based on that data.

**Common anti-patterns:**

- You rely on common benchmarks that are not indicative of your workload’s
characteristics.
- You rely on customer feedback and perceptions as your only benchmark.

**Benefits of establishing this best practice:** Benchmarking your
current implementation allows you to measure performance improvements.

**Level of risk exposed if this best practice is not established:**
Medium

## Implementation guidance

Use benchmarking with synthetic tests to assess how your workload’s components perform.
Benchmarking is generally quicker to set up than load testing and is used to evaluate the
technology for a particular component. Benchmarking is often used at the start of a new
project, when you lack a full solution to load test.

You can either build your own custom benchmark tests or use an industry standard test,
such as [TPC-DS](http://www.tpc.org/tpcds/), to benchmark your workloads.
Industry benchmarks are helpful when comparing environments. Custom benchmarks are useful for
targeting specific types of operations that you expect to make in your architecture.

When benchmarking, it is important to pre-warm your test environment to get valid
results. Run the same benchmark multiple times to verify that you’ve captured any variance
over time.

Because benchmarks are generally faster to run than load tests, they can be used earlier
in the deployment pipeline and provide faster feedback on performance deviations. When you
evaluate a significant change in a component or service, a benchmark can be a quick way to see
if you can justify the effort to make the change. Using benchmarking in conjunction with load
testing is important because load testing informs you about how your workload performs in
production.

### Implementation steps

- Plan and define:

Define the objectives, baseline, testing scenarios, metrics (like CPU
utilization, latency, or throughput), and KPIs for your benchmark.
- Focus on user requirements in terms of user experience and factors such as
response time and accessibility.
- Identify a benchmarking tool that is suitable for your workload. You can use
AWS services like [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) or a third-party tool that is compatible with your workload.

- Configure and instrument:

Set up your environment and configure your resources.
- Implement monitoring and logging to capture testing results.

- Benchmark and monitor:

Perform your benchmark tests and monitor the metrics during the test.

- Analyze and document:

Document your benchmarking process and findings.
- Analyze the results to identify bottlenecks, trends, and areas of improvement.
- Use test results to make architectural decisions and adjust your workload. This
may include changing services or adopting new features.

- Optimize and repeat:

Adjust resource configurations and allocations based on your benchmarks.
- Retest your workload after the adjustment to validate your improvements.
- Document your learnings, and repeat the process to identify other areas of
improvement.

## Resources

**Related documents:**

- [AWS Architecture Center](https://aws.amazon.com/architecture/)
- [AWS Partner Network](https://aws.amazon.com/partners/)
- [AWS Solutions Library](https://aws.amazon.com/solutions/)
- [AWS Knowledge
Center](https://aws.amazon.com/premiumsupport/knowledge-center/)
- [Amazon CloudWatch
RUM](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM.html)
- [Amazon CloudWatch
Synthetics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.html)
- [Genomics workflows, Part 5: automated benchmarking](https://aws.amazon.com/blogs/architecture/genomics-workflows-part-5-automated-benchmarking/)
- [Benchmark and optimize endpoint deployment in Amazon SageMaker AI JumpStart](https://aws.amazon.com/blogs/machine-learning/benchmark-and-optimize-endpoint-deployment-in-amazon-sagemaker-jumpstart/)

**Related videos:**

- [AWS re:Invent 2023 - Benchmarking AWS Lambda cold starts](https://www.youtube.com/watch?v=bGMEPI-va-Q&ab_channel=AWSEvents)
- [Benchmarking stateful services in the cloud](https://www.youtube.com/watch?v=rtW4a4DvcWU&ab_channel=AWSEvents)
- [This is my
Architecture](https://aws.amazon.com/architecture/this-is-my-architecture/)
- [Optimize applications through
Amazon CloudWatch RUM](https://www.youtube.com/watch?v=NMaeujY9A9Y)
- [Demo of Amazon CloudWatch
Synthetics](https://www.youtube.com/watch?v=hF3NM9j-u7I)

**Related examples:**

- [AWS Samples](https://github.com/aws-samples)
- [AWS SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples)
- [Distributed Load Tests](https://aws.amazon.com/solutions/implementations/distributed-load-testing-on-aws/)
- [Measure page load time with Amazon CloudWatch Synthetics](https://github.com/aws-samples/amazon-cloudwatch-synthetics-page-performance)
- [Amazon CloudWatch RUM Web
Client](https://github.com/aws-observability/aws-rum-web)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_architecture_use_benchmarking.html*

---

# PERF01-BP07 Use a data-driven approach for architectural choices

Define a clear, data-driven approach for architectural choices to
verify that the right cloud services and configurations are used to
meet your specific business needs.

**Common anti-patterns:**

- You assume your current architecture is static and should not be
updated over time.
- Your architectural choices are based upon guesses and
assumptions.
- You introduce architecture changes over time without
justification.

**Benefits of establishing this best
practice:** By having a well-defined approach for making
architectural choices, you use data to influence your workload
design and make informed decisions over time.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Use internal experience and knowledge of the cloud or external
resources such as published use cases or whitepapers to choose
resources and services in your architecture. You should have a
well-defined process that encourages experimentation and
benchmarking with the services that could be used in your
workload.

Backlogs for critical workloads should consist of not just user
stories which deliver functionality relevant to business and
users, but also technical stories which form an architecture
runway for the workload. This runway is informed by new
advancements in technology and new services and adopts them based
on data and proper justification. This verifies that the
architecture remains future-proof and does not stagnate.

### Implementation steps

- Engage with key stakeholders to define workload
requirements, including performance, availability, and cost
considerations. Consider factors such as the number of
users and usage pattern for your workload.
- Create an architecture runway or a technology backlog which
is prioritized along with the functional backlog.
- Evaluate and assess different cloud services (for more
detail, see [PERF01-BP01 Learn about and understand available cloud services and features](./perf_architecture_understand_cloud_services_and_features.html)).
- Explore different architectural patterns, like microservices
or serverless, that meet your performance requirements (for
more detail, see [PERF01-BP02 Use guidance from your cloud provider or an appropriate partner to learn about architecture patterns and best practices](./perf_architecture_guidance_architecture_patterns_best_practices.html)).

- Consult other teams, architecture diagrams, and resources,
such as AWS Solution Architects,
[AWS Architecture Center](https://aws.amazon.com/architecture/), and
[AWS Partner Network](https://aws.amazon.com/partners/), to help you choose the right
architecture for your workload.

- Define performance metrics like throughput and response time
that can help you evaluate the performance of your workload.
- Experiment and use defined metrics to validate the
performance of the selected architecture.
- Continually monitor and make adjustments as needed to
maintain the optimal performance of your architecture.
- Document your selected architecture and decisions as a
reference for future updates and learnings.
- Continually review and update the architecture selection
approach based on learnings, new technologies, and metrics
that indicate a needed change or problem in the current
approach.

## Resources

**Related documents:**

- [AWS Solutions Library](https://aws.amazon.com/solutions/)
- [AWS Knowledge Center](https://aws.amazon.com/premiumsupport/knowledge-center/)
- [Architectural Patterns to Build End-to-End Data Driven Applications on AWS](https://docs.aws.amazon.com/whitepapers/latest/build-e2e-data-driven-applications/build-e2e-data-driven-applications.html)

**Related videos:**

- [This
is my Architecture](https://aws.amazon.com/architecture/this-is-my-architecture/)
- [AWS re:Invent 2021 - Data-driven enterprise: Going from vision to value](https://www.youtube.com/watch?v=_D0PF2N2AfA)
- [AWS re:Invent 2022 - Delivering sustainable, high-performing architectures](https://www.youtube.com/watch?v=FBc9hXQfat0)
- [AWS re:Invent 2023 - Optimize cost and performance and track progress toward mitigation](https://www.youtube.com/watch?v=keAfy8f84E0)
- [AWS re:Invent 2022 - AWS optimization: Actionable steps for immediate results](https://www.youtube.com/watch?v=0ifvNf2Tx3w)

**Related examples:**

- [AWS Samples](https://github.com/aws-samples)
- [AWS SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_architecture_use_data_driven_approach.html*

---

---

## Question PERF02

# PERF 2 — How do you select and use compute resources?

**Pillar**: Performance Efficiency  
**Best Practices**: 6

---

# PERF02-BP01 Select the best compute options for your workload

Selecting the most appropriate compute option for your workload
allows you to improve performance, reduce unnecessary infrastructure
costs, and lower the operational efforts required to maintain your
workload.

**Common anti-patterns:**

- You use the same compute option that was used on
premises.
- You lack awareness of the cloud compute options, features, and
solutions, and how those solutions might improve your compute
performance.
- You over-provision an existing compute option to meet scaling or
performance requirements when an alternative compute option
would align to your workload characteristics more precisely.

**Benefits of establishing this best
practice:** By identifying the compute requirements and
evaluating against the options available, you can make your workload
more resource efficient.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

To optimize your cloud workloads for performance efficiency, it is
important to select the most appropriate compute options for your
use case and performance requirements. AWS provides a variety of
compute options that cater to different workloads in the cloud.
For instance, you can use [Amazon EC2](https://docs.aws.amazon.com/ec2/) to launch and manage virtual
servers, [AWS Lambda](https://docs.aws.amazon.com/lambda/?icmpid=docs_homepage_featuredsvcs) to run code without having to provision or
manage servers, [Amazon ECS](https://aws.amazon.com/ecs/) or [Amazon EKS](https://aws.amazon.com/eks/) to run and manage containers, or
[AWS Batch](https://aws.amazon.com/batch/) to process large volumes of data in parallel. Based on
your scale and compute needs, you should choose and configure the
optimal compute solution for your situation. You can also consider
using multiple types of compute solutions in a single workload, as
each one has its own advantages and drawbacks.

The following steps guide you through selecting the right compute
options to match your workload characteristics and performance
requirements.

## Implementation steps

- Understand your workload compute requirements. Key
requirements to consider include processing needs, traffic
patterns, data access patterns, scaling needs, and latency
requirements.
- Learn about different [AWS compute services](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/compute-services.html) for your
workload. For more information, see [PERF01-BP01 Learn about and understand available cloud services and features](./perf_architecture_understand_cloud_services_and_features.html). Here are some key
AWS compute options, their characteristics, and common
use cases:

AWS service

Key characteristics

Common use cases

[Amazon Elastic Compute Cloud (Amazon EC2)](https://aws.amazon.com/ec2/)

Has dedicated option for hardware, license requirements,
large selection of different instance families, processor
types and compute accelerators

Lift and shift migrations, monolithic application, hybrid
environments, enterprise applications

[Amazon Elastic Container Service (Amazon ECS)](https://aws.amazon.com/ecs/), [Amazon Elastic Kubernetes Service (Amazon EKS)](https://aws.amazon.com/eks/)

Easy deployment, consistent environments, scalable

Microservices, hybrid environments

[AWS Lambda](https://aws.amazon.com/lambda/)

[Serverless
compute](https://aws.amazon.com/serverless/) service that runs code in response to
events and automatically manages the underlying compute
resources.

Microservices, event-driven applications

[AWS Batch](https://aws.amazon.com/batch/)

Efficiently and dynamically provisions and
scales [Amazon Elastic Container Service (Amazon ECS)](https://aws.amazon.com/ecs/), [Amazon Elastic Kubernetes Service (Amazon EKS)](https://aws.amazon.com/eks/),
and [AWS Fargate](https://aws.amazon.com/fargate/) compute resources, with an option to use
On-Demand or Spot Instances based on your job requirements

HPC, train ML models

[Amazon Lightsail](https://aws.amazon.com/lightsail/)

Preconfigured Linux and Windows application for running
small workloads

Simple web applications, custom website
- Evaluate cost (like hourly charge or data transfer) and
management overhead (like patching and scaling) associated to
each compute option.
- Perform experiments and benchmarking in a non-production
environment to identify which compute option can best address
your workload requirements.
- Once you have experimented and identified your new compute
solution, plan your migration and validate your performance
metrics.
- Use AWS monitoring tools like [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) and
optimization services like [AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/) to
continually optimize your compute resources based on real-world usage
patterns.

## Resources

**Related documents:**

- [Cloud
Compute with AWS](https://aws.amazon.com/products/compute/?ref=wellarchitected)
- [Amazon EC2
Instance Types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html?ref=wellarchitected)
- [Amazon EKS
Containers: Amazon EKS Worker Nodes](https://docs.aws.amazon.com/eks/latest/userguide/worker.html?ref=wellarchitected)
- [Amazon ECS Containers: Amazon ECS Container
Instances](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ECS_instances.html?ref=wellarchitected)
- [Functions:
Lambda Function Configuration](https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html?ref=wellarchitected#function-configuration)
- [Prescriptive Guidance for Containers](https://aws.amazon.com/prescriptive-guidance/?apg-all-cards.sort-by=item.additionalFields.sortText&apg-all-cards.sort-order=desc&awsf.apg-new-filter=*all&awsf.apg-content-type-filter=*all&awsf.apg-code-filter=*all&awsf.apg-category-filter=categories%23containers&awsf.apg-rtype-filter=*all&awsf.apg-isv-filter=*all&awsf.apg-product-filter=*all&awsf.apg-env-filter=*all)
- [Prescriptive
Guidance for Serverless](https://aws.amazon.com/prescriptive-guidance/?apg-all-cards.sort-by=item.additionalFields.sortText&apg-all-cards.sort-order=desc&awsf.apg-new-filter=*all&awsf.apg-content-type-filter=*all&awsf.apg-code-filter=*all&awsf.apg-category-filter=categories%23serverless&awsf.apg-rtype-filter=*all&awsf.apg-isv-filter=*all&awsf.apg-product-filter=*all&awsf.apg-env-filter=*all)

**Related videos:**

- [AWS
re:Invent 2023 - AWS Graviton: The best price performance for your AWS
workloads](https://www.youtube.com/watch?v=T_hMIjKtSr4&ab_channel=AWSEvents)
- [AWS
re:Invent 2023 - New Amazon Elastic Compute Cloud generative AI capabilities in AMS](https://www.youtube.com/watch?v=sSpJ8tWCEiA)
- [AWS
re:Invent 2023 - What’s new with Amazon Elastic Compute Cloud](https://www.youtube.com/watch?v=mjHw_wgJJ5g)
- [AWS
re:Invent 2023 - Smart savings: Amazon Elastic Compute Cloud cost-optimization strategies](https://www.youtube.com/watch?v=_AHPbxzIGV0)
- [AWS
re:Invent 2021 - Powering next-gen Amazon Elastic Compute Cloud: Deep dive on the Nitro System](https://www.youtube.com/watch?v=2uc1vaEsPXU)
- [AWS re:Invent 2019 - Optimize
performance and cost for your AWS compute](https://www.youtube.com/watch?v=zt6jYJLK8sg)
- [AWS
re:Invent 2019 - Amazon Elastic Compute Cloud foundations](https://www.youtube.com/watch?v=kMMybKqC2Y0)
- [AWS re:Invent 2022 - Deploy ML
models for inference at high performance and low cost](https://www.youtube.com/watch?v=4FqHt5bmS2o)
- [AWS re:Invent 2019 - Optimize
performance and cost for your AWS compute](https://www.youtube.com/watch?v=zt6jYJLK8sg)
- [Amazon EC2
foundations](https://www.youtube.com/watch?v=kMMybKqC2Y0)
- [Deploy ML models for inference at
high performance and low cost](https://www.youtube.com/watch?v=4FqHt5bmS2o)

**Related examples:**

- [Migrating
the Web application to containers](https://application-migration-with-aws.workshop.aws/en/container-migration.html)
- [Run
a Serverless Hello World](https://aws.amazon.com/getting-started/hands-on/run-serverless-code/)
- [Amazon EKS Workshop](https://www.eksworkshop.com/)
- [Amazon EC2 Workshop](https://ec2spotworkshops.com/)
- [Efficient and Resilient Workloads with Amazon Elastic Compute Cloud Auto Scaling](https://catalog.us-east-1.prod.workshops.aws/workshops/20c57d32-162e-4ad5-86a6-dff1f8de4b3c/en-US)
- [Migrating to AWS Graviton with Container Services](https://catalog.us-east-1.prod.workshops.aws/workshops/dcab7555-32fc-42d2-97e5-2b7a35cd008f/en-US/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_compute_hardware_select_best_compute_options.html*

---

# PERF02-BP02 Understand the available compute configuration and features

Understand the available configuration options and features for your
compute service to help you provision the right amount of resources
and improve performance efficiency.

**Common anti-patterns:**

- You do not evaluate compute options or available instance
families against workload characteristics.
- You over-provision compute resources to meet peak-demand
requirements.

**Benefits of establishing this best practice:** Be familiar with AWS compute features and configurations so that you can use a compute solution optimized to meet your workload characteristics and needs.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Each compute solution has unique configurations and features
available to support different workload characteristics and
requirements. Learn how these options complement your workload,
and determine which configuration options are best for your
application. Examples of these options include instance family,
sizes, features (GPU, I/O), bursting, time-outs, function sizes,
container instances, and concurrency. If your workload has been
using the same compute option for more than four weeks and you
anticipate that the characteristics will remain the same in the
future, you can
use [AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/)  to find out if your current compute option is
suitable for the workloads from CPU and memory perspective.

## Implementation steps

- Understand workload requirements (like CPU need, memory, and
latency).
- Review AWS documentation and best practices to learn about
recommended configuration options that can help improve compute performance. Here are some key configuration
options to consider:

Configuration option

Examples

Instance type

[Compute-optimized](https://aws.amazon.com/ec2/instance-types/?trk=36c6da98-7b20-48fa-8225-4784bced9843&sc_channel=ps&sc_campaign=acquisition&sc_medium=ACQ-P|PS-GO|Brand|Desktop|SU|Compute|EC2|US|EN|Text&s_kwcid=AL!4422!3!536392622533!e!!g!!ec2%20instance%20types&ef_id=CjwKCAjwiuuRBhBvEiwAFXKaNNRXM5FrnFg5H8RGQ4bQKuUuK1rYWmU2iH-5H3VZPqEheB-pEm-GNBoCdD0QAvD_BwE:G:s&s_kwcid=AL!4422!3!536392622533!e!!g!!ec2%20instance%20types#Compute_Optimized) instances
are ideal for the workloads that require high higher
vCPU to memory ratio.
- [Memory-optimized](https://aws.amazon.com/ec2/instance-types/?trk=36c6da98-7b20-48fa-8225-4784bced9843&sc_channel=ps&sc_campaign=acquisition&sc_medium=ACQ-P|PS-GO|Brand|Desktop|SU|Compute|EC2|US|EN|Text&s_kwcid=AL!4422!3!536392622533!e!!g!!ec2%20instance%20types&ef_id=CjwKCAjwiuuRBhBvEiwAFXKaNNRXM5FrnFg5H8RGQ4bQKuUuK1rYWmU2iH-5H3VZPqEheB-pEm-GNBoCdD0QAvD_BwE:G:s&s_kwcid=AL!4422!3!536392622533!e!!g!!ec2%20instance%20types#Memory_Optimized) instances
deliver large amounts of memory to support memory
intensive workloads.
- [Storage-optimized](https://aws.amazon.com/ec2/instance-types/?trk=36c6da98-7b20-48fa-8225-4784bced9843&sc_channel=ps&sc_campaign=acquisition&sc_medium=ACQ-P|PS-GO|Brand|Desktop|SU|Compute|EC2|US|EN|Text&s_kwcid=AL!4422!3!536392622533!e!!g!!ec2%20instance%20types&ef_id=CjwKCAjwiuuRBhBvEiwAFXKaNNRXM5FrnFg5H8RGQ4bQKuUuK1rYWmU2iH-5H3VZPqEheB-pEm-GNBoCdD0QAvD_BwE:G:s&s_kwcid=AL!4422!3!536392622533!e!!g!!ec2%20instance%20types#Storage_Optimized) instances
are designed for workloads that require high,
sequential read and write access (IOPS) to local
storage.

Pricing model

- [On-Demand
Instances](https://aws.amazon.com/ec2/pricing/on-demand/) let you use the compute capacity by
the hour or second with no long-term commitment.
These instances are good for bursting above
performance baseline needs.
- [Savings Plans](https://aws.amazon.com/savingsplans/) offer significant savings over
On-Demand Instances in exchange for a commitment to
use a specific amount of compute power for a one or
three-year period.
- [Spot
Instances](https://aws.amazon.com/ec2/spot/) let you take advantage of unused
instance capacity at a discount for your stateless,
fault-tolerant workloads.

Auto Scaling

Use
[Auto Scaling](https://docs.aws.amazon.com/AmazonECS/latest/bestpracticesguide/capacity-autoscaling.html) configuration to match compute resources to
traffic patterns.

Sizing

- Use [Compute Optimizer](https://aws.amazon.com/compute-optimizer/) to get a machine-learning powered
recommendations on which compute configuration best
matches your compute characteristics.
- Use
[AWS Lambda Power Tuning](https://docs.aws.amazon.com/lambda/latest/operatorguide/profile-functions.html) to select the best
configuration for your Lambda function.

Hardware-based compute accelerators

- [Accelerated
computing instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/accelerated-computing-instances.html) perform functions like
graphics processing or data pattern matching more
efficiently than CPU-based alternatives.
- For machine learning workloads, take advantage of
purpose-built hardware that is specific to your
workload, such
as [AWS Trainium](https://aws.amazon.com/machine-learning/trainium/), [AWS Inferentia](https://aws.amazon.com/machine-learning/inferentia/),
and [Amazon EC2 DL1](https://aws.amazon.com/ec2/instance-types/dl1/)

## Resources

**Related documents:**

- [Cloud
Compute with AWS](https://aws.amazon.com/products/compute/?ref=wellarchitected)
- [Amazon EC2
Instance Types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html?ref=wellarchitected)
- [Processor
State Control for Your Amazon EC2 Instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/processor_state_control.html?ref=wellarchitected)
- [Amazon EKS
Containers: Amazon EKS Worker Nodes](https://docs.aws.amazon.com/eks/latest/userguide/worker.html?ref=wellarchitected)
- [Amazon ECS Containers: Amazon ECS Container Instances](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ECS_instances.html?ref=wellarchitected)
- [Functions:
Lambda Function Configuration](https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html?ref=wellarchitected#function-configuration)

**Related videos:**

- [AWS re:Invent 2023 – AWS Graviton: The best price performance for your AWS workloads](https://www.youtube.com/watch?v=T_hMIjKtSr4)
- [AWS re:Invent 2023 – New Amazon EC2 generative AI capabilities in AWS Management Console](https://www.youtube.com/watch?v=sSpJ8tWCEiA)
- [AWS re:Invent 2023 – What's new with Amazon EC2](https://www.youtube.com/watch?v=mjHw_wgJJ5g)
- [AWS re:Invent 2023 – Smart savings: Amazon EC2 cost-optimization strategies](https://www.youtube.com/watch?v=_AHPbxzIGV0)
- [AWS re:Invent 2021 – Powering next-gen Amazon EC2: Deep dive on the Nitro System](https://www.youtube.com/watch?v=2uc1vaEsPXU)
- [AWS re:Invent 2019 – Amazon EC2 foundations](https://www.youtube.com/watch?v=kMMybKqC2Y0)
- [AWS re:Invent 2022 – Optimizing Amazon EKS for performance and cost on AWS](https://www.youtube.com/watch?v=5B4-s_ivn1o)

**Related examples:**

- [Compute Optimizer demo code](https://github.com/awslabs/ec2-spot-labs/tree/master/aws-compute-optimizer)
- [Amazon EC2 spot instances workshop](https://ec2spotworkshops.com/)
- [Efficient and Resilient Workloads with Amazon EC2 AWS Auto Scaling](https://catalog.us-east-1.prod.workshops.aws/workshops/20c57d32-162e-4ad5-86a6-dff1f8de4b3c/en-US)
- [Graviton developer workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/dcab7555-32fc-42d2-97e5-2b7a35cd008f/en-US/)
- [AWS for Microsoft workloads immersion day](https://catalog.us-east-1.prod.workshops.aws/workshops/d6c7ecdc-c75f-4ad1-910f-fdd994cc4aed/en-US)
- [AWS for Linux workloads immersion day](https://catalog.us-east-1.prod.workshops.aws/workshops/a8e9c6a6-0ba9-48a7-a90d-378a440ab8ba/en-US)
- [AWS Compute Optimizer Demo code](https://github.com/awslabs/ec2-spot-labs/tree/master/aws-compute-optimizer)
- [Amazon EKS workshop](https://www.eksworkshop.com/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_compute_hardware_understand_compute_configuration_features.html*

---

# PERF02-BP03 Collect compute-related metrics

Record and track compute-related metrics to better understand how
your compute resources are performing and improve their performance
and their utilization.

**Common anti-patterns:**

- You only use manual log file searching for metrics.
- You only use the default metrics recorded by your monitoring
software.
- You only review metrics when there is an issue.

**Benefits of establishing this best
practice:** Collecting performance-related metrics will
help you align application performance with business requirements to
ensure that you are meeting your workload needs. It can also help
you continually improve the resource performance and utilization in
your workload.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Cloud workloads can generate large volumes of data such as
metrics, logs, and events. In the AWS Cloud, collecting metrics is
a crucial step to improve security, cost efficiency, performance,
and sustainability. AWS provides a wide range of
performance-related metrics using monitoring services such as
[Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) to provide you with valuable insights. Metrics
such as CPU utilization, memory utilization, disk I/O, and network
inbound and outbound can provide insight into utilization levels
or performance bottlenecks. Use these metrics as part of a
data-driven approach to actively tune and optimize your workload's
resources.  In an ideal case, you should collect all metrics
related to your compute resources in a single platform with
retention policies implemented to support cost and operational
goals.

## Implementation steps

- Identify which performance-related metrics are relevant to
your workload. You should collect metrics around resource
utilization and the way your cloud workload is operating (like
response time and throughput).

[Amazon EC2
default metrics](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/viewing_metrics_with_cloudwatch.html)
- [Amazon ECS default metrics](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cloudwatch-metrics.html)
- [Amazon EKS
default metrics](https://docs.aws.amazon.com/prescriptive-guidance/latest/implementing-logging-monitoring-cloudwatch/kubernetes-eks-metrics.html)
- [Lambda
default metrics](https://docs.aws.amazon.com/lambda/latest/dg/monitoring-functions-access-metrics.html)
- [Amazon EC2
memory and disk metrics](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/mon-scripts.html)

- Choose and set up the right logging and monitoring solution
for your workload.

[AWS native Observability](https://catalog.workshops.aws/observability/en-US/aws-native)
- [AWS Distro
for OpenTelemetry](https://aws.amazon.com/otel/)
- [Amazon Managed Service for Prometheus](https://docs.aws.amazon.com/grafana/latest/userguide/prometheus-data-source.html)

- Define the required filter and aggregation for the metrics
based on your workload requirements.

[Quantify
custom application metrics with Amazon CloudWatch Logs and
metric filters](https://aws.amazon.com/blogs/mt/quantify-custom-application-metrics-with-amazon-cloudwatch-logs-and-metric-filters/)
- [Collect
custom metrics with Amazon CloudWatch strategic
tagging](https://aws.amazon.com/blogs/infrastructure-and-automation/collect-custom-metrics-with-amazon-cloudwatch-strategic-tagging/)

- Configure data retention policies for your metrics to match
your security and operational goals.

[Default
data retention for CloudWatch metrics](https://aws.amazon.com/cloudwatch/faqs/#AWS_resource_.26_custom_metrics_monitoring)
- [Default
data retention for CloudWatch Logs](https://aws.amazon.com/cloudwatch/faqs/#Log_management)

- If required, create alarms and notifications for your metrics
to help you proactively respond to performance-related issues.

[Create
alarms for custom metrics using Amazon CloudWatch anomaly
detection](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/create-alarms-for-custom-metrics-using-amazon-cloudwatch-anomaly-detection.html)
- [Create
metrics and alarms for specific web pages with Amazon CloudWatch RUM](https://aws.amazon.com/blogs/mt/create-metrics-and-alarms-for-specific-web-pages-amazon-cloudwatch-rum/)

- Use automation to deploy your metric and log aggregation
agents.

[AWS Systems Manager automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html?ref=wellarchitected)
- [OpenTelemetry
Collector](https://aws-otel.github.io/docs/getting-started/collector)

## Resources

**Related documents:**

- [Monitoring and observability](https://aws.amazon.com/cloudops/monitoring-and-observability/)
- [Best practices: implementing observability with AWS](https://aws.amazon.com/blogs/mt/best-practices-implementing-observability-with-aws/)
- [Amazon CloudWatch documentation](https://docs.aws.amazon.com/cloudwatch/index.html?ref=wellarchitected)
- [Collect
metrics and logs from Amazon EC2 instances and on-premises
servers with the CloudWatch Agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.html?ref=wellarchitected)
- [Accessing
Amazon CloudWatch Logs for AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/monitoring-functions-logs.html?ref=wellarchitected)
- [Using
CloudWatch Logs with container instances](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using_cloudwatch_logs.html?ref=wellarchitected)
- [Publish
custom metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html?ref=wellarchitected)
- [AWS Answers: Centralized Logging](https://aws.amazon.com/answers/logging/centralized-logging/?ref=wellarchitected)
- [AWS Services That Publish CloudWatch Metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CW_Support_For_AWS.html?ref=wellarchitected)
- [Monitoring
Amazon EKS on AWS Fargate](https://aws.amazon.com/blogs/containers/monitoring-amazon-eks-on-aws-fargate-using-prometheus-and-grafana/)

**Related videos:**

- [AWS re:Invent 2023 – [LAUNCH] Application monitoring for modern workloads](https://www.youtube.com/watch?v=T2TovTLje8w)
- [AWS re:Invent 2023 – Implementing application observability](https://www.youtube.com/watch?v=IcTcwUSwIs4)
- [AWS re:Invent 2023 – Building an effective observability strategy](https://www.youtube.com/watch?v=7PQv9eYCJW8)
- [AWS re:Invent 2023 – Seamless observability with AWS Distro for OpenTelemetry](https://www.youtube.com/watch?v=S4GfA2R0N_A)
- [Application
Performance Management on AWS](https://www.youtube.com/watch?v=5T4stR-HFas&ref=wellarchitected)

**Related examples:**

- [AWS for Linux Workloads Immersion Day- Amazon CloudWatch](https://catalog.us-east-1.prod.workshops.aws/workshops/a8e9c6a6-0ba9-48a7-a90d-378a440ab8ba/en-US/300-cloudwatch)
- [Monitoring Amazon ECS clusters and containers](https://ecsworkshop.com/monitoring/)
- [Monitoring with Amazon CloudWatch dashboards](https://catalog.workshops.aws/well-architected-performance-efficiency/en-US/3-monitoring/monitoring-with-cloudwatch-dashboards)
- [Amazon EKS workshop](https://www.eksworkshop.com/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_compute_hardware_collect_compute_related_metrics.html*

---

# PERF02-BP04 Configure and right-size compute resources

Configure and right-size compute resources to match your workload’s
performance requirements and avoid under- or over-utilized
resources.

**Common anti-patterns:**

- You ignore your workload performance requirements resulting in
over-provisioned or under-provisioned compute resources.
- You only choose the largest or smallest instance available for
all workloads.
- You only use one instance family for ease of management.
- You ignore recommendations from AWS Cost Explorer or Compute Optimizer for right-sizing.
- You do not re-evaluate the workload for suitability of new
instance types.
- You certify only a small number of instance configurations for
your organization.

**Benefits of establishing this best
practice:**
Right-sizing compute resources ensures optimal operation in the
cloud by avoiding over-provisioning and under-provisioning
resources. Properly sizing compute resources typically results in
better performance and enhanced customer experience, while also
lowering cost.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Right-sizing allows organizations to operate their cloud
infrastructure in an efficient and cost-effective manner while
addressing their business needs. Over-provisioning cloud resources
can lead to extra costs, while under-provisioning can result in
poor performance and a negative customer experience. AWS provides
tools such as
[AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/) and
[AWS Trusted Advisor](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/) that use historical data to provide
recommendations to right-size your compute resources.

### Implementation steps

- Choose an instance type to best fit your needs:

[How
do I choose the appropriate Amazon EC2 instance type for
my workload?](https://aws.amazon.com/premiumsupport/knowledge-center/ec2-instance-choose-type-for-workload/)
- [Attribute-based
instance type selection for Amazon EC2 Fleet](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-fleet-attribute-based-instance-type-selection.html)
- [Create
an Auto Scaling group using attribute-based instance
type selection](https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-asg-instance-type-requirements.html)
- [Optimizing
your Kubernetes compute costs with Karpenter
consolidation](https://aws.amazon.com/blogs/containers/optimizing-your-kubernetes-compute-costs-with-karpenter-consolidation/)

- Analyze the various performance characteristics of your
workload and how these characteristics relate to memory,
network, and CPU usage. Use this data to choose resources
that best match your workload's profile and performance
goals.
- Monitor your resource usage using AWS monitoring tools such
as Amazon CloudWatch.
- Select the right configuration for compute resources.

For ephemeral workloads,
evaluate [instance
Amazon CloudWatch metrics](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/viewing_metrics_with_cloudwatch.html) such
as `CPUUtilization` to identify if the instance is
under-utilized or over-utilized.
- For stable workloads, check AWS rightsizing tools such
as AWS Compute Optimizer and AWS Trusted Advisor at
regular intervals to identify opportunities to optimize
and right-size the compute resource.

- Test configuration changes in a non-production environment
before implementing in a live environment.
- Continually re-evaluate new compute offerings and compare
against your workload’s needs.

## Resources

**Related documents:**

- [Cloud
Compute with AWS](https://aws.amazon.com/products/compute/)
- [Amazon EC2
Instance Types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html)
- [Amazon ECS
Containers: Amazon ECS Container Instances](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ECS_instances.html)
- [Amazon EKS
Containers: Amazon EKS Worker Nodes](https://docs.aws.amazon.com/eks/latest/userguide/worker.html)
- [Functions:
Lambda Function Configuration](https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html#function-configuration)
- [Processor
State Control for Your Amazon EC2 Instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/processor_state_control.html)

**Related videos:**

- [Amazon EC2 foundations](https://www.youtube.com/watch?v=kMMybKqC2Y0)
- [AWS re:Invent 2023 – AWS Graviton: The best price performance for your AWS workloads](https://www.youtube.com/watch?v=T_hMIjKtSr4)
- [AWS re:Invent 2023 – New Amazon EC2 generative AI capabilities in AWS Management Console](https://www.youtube.com/watch?v=sSpJ8tWCEiA)
- [AWS re:Invent 2023 – What’s new with Amazon EC2](https://www.youtube.com/watch?v=mjHw_wgJJ5g)
- [AWS re:Invent 2023 – Smart savings: Amazon EC2 cost-optimization strategies](https://www.youtube.com/watch?v=_AHPbxzIGV0)
- [AWS re:Invent 2021 – Powering next-gen Amazon EC2: Deep dive on the Nitro System](https://www.youtube.com/watch?v=2uc1vaEsPXU)
- [AWS re:Invent 2019 – Amazon EC2 foundations](https://www.youtube.com/watch?v=kMMybKqC2Y0)

**Related examples:**

- [AWS Compute Optimizer Demo code](https://github.com/awslabs/ec2-spot-labs/tree/master/aws-compute-optimizer)
- [Amazon EKS workshop](https://www.eksworkshop.com/)
- [Right-sizing recommendations](https://catalog.workshops.aws/well-architected-cost-optimization/en-US/3-cost-effective-resources/40-rightsizing-recommendations-100)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_compute_hardware_configure_and_right_size_compute_resources.html*

---

# PERF02-BP05 Scale your compute resources dynamically

Use the elasticity of the cloud to scale your compute resources up
or down dynamically to match your needs and avoid over- or
under-provisioning capacity for your workload.

**Common anti-patterns:**

- You react to alarms by manually increasing capacity.
- You use the same sizing guidelines (generally static
infrastructure) as in on-premises.
- You leave increased capacity after a scaling event instead of
scaling back down.

**Benefits of establishing this best
practice:** Configuring and testing the elasticity of
compute resources can help you save money, maintain performance
benchmarks, and improve reliability as traffic changes.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

AWS provides the flexibility to scale your resources up or down
dynamically through a variety of scaling mechanisms in order to
meet changes in demand. Combined with compute-related metrics, a
dynamic scaling allows workloads to automatically respond to
changes and use the optimal set of compute resources to achieve
its goal.

You can use a number of different approaches to match supply of
resources with demand.

- **Target-tracking approach**: Monitor your scaling metric and
automatically increase or decrease capacity as you need it.
- **Predictive scaling**: Scale in anticipation of daily and
weekly trends.
- **Schedule-based approach**: Set your own scaling schedule
according to predictable load changes.
- **Service scaling**: Choose services (like serverless) that
that automatically scale by design.

You must ensure that workload deployments can handle both scale-up
and scale-down events.

### Implementation steps

- Compute instances, containers, and functions provide
mechanisms for elasticity, either in combination with
autoscaling or as a feature of the service. Here are some
examples of automatic scaling mechanisms:

Autoscaling Mechanism

Where to use

[Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html)

To ensure you have the correct number of
[Amazon EC2](https://aws.amazon.com/ec2/) instances available to handle the user load
for your application.

[Application Auto Scaling](https://docs.aws.amazon.com/autoscaling/application/userguide/what-is-application-auto-scaling.html)

To automatically scale the resources for individual AWS
services beyond Amazon EC2 such as
[AWS Lambda](https://aws.amazon.com/lambda/) functions or
[Amazon Elastic Container Service (Amazon ECS)](https://aws.amazon.com/ecs/) services.

[Kubernetes
Cluster Autoscaler/Karpenter](https://aws.amazon.com/blogs/aws/introducing-karpenter-an-open-source-high-performance-kubernetes-cluster-autoscaler/)

To automatically scale Kubernetes clusters.
- Scaling is often discussed related to compute services like
Amazon EC2 Instances or AWS Lambda functions. Be sure to
also consider the configuration of non-compute services like
[AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/auto-scaling.html) to match the demand.
- Verify that the metrics for scaling match the
characteristics of the workload being deployed. If you are
deploying a video transcoding application, 100% CPU
utilization is expected and should not be your primary
metric. Use the depth of the transcoding job queue instead.
You can use a
[customized
metric](https://aws.amazon.com/blogs/mt/create-amazon-ec2-auto-scaling-policy-memory-utilization-metric-linux/) for your scaling policy if required. To choose
the right metrics, consider the following guidance for Amazon EC2:

The metric should be a valid utilization metric and
describe how busy an instance is.
- The metric value must increase or decrease
proportionally to the number of instances in the Auto Scaling group.

- Make sure that you use
[dynamic
scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scale-based-on-demand.html) instead of
[manual
scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-manual-scaling.html) for your Auto Scaling group. We also
recommend that you use
[target
tracking scaling policies](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-target-tracking.html) in your dynamic scaling.
- Verify that workload deployments can handle both scaling
events (up and down). As an example, you can use
[Activity
history](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-verify-scaling-activity.html) to verify a scaling activity for an Auto Scaling group.
- Evaluate your workload for predictable patterns and
proactively scale as you anticipate predicted and planned
changes in demand. With predictive scaling, you can
eliminate the need to overprovision capacity. For more detail,
see [Predictive
Scaling with Amazon EC2 Auto Scaling](https://aws.amazon.com/blogs/compute/introducing-native-support-for-predictive-scaling-with-amazon-ec2-auto-scaling/).

## Resources

**Related documents:**

- [Cloud
Compute with AWS](https://aws.amazon.com/products/compute/)
- [Amazon EC2
Instance Types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html)
- [Amazon ECS
Containers: Amazon ECS Container Instances](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ECS_instances.html)
- [Amazon EKS
Containers: Amazon EKS Worker Nodes](https://docs.aws.amazon.com/eks/latest/userguide/worker.html)
- [Functions:
Lambda Function Configuration](https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html#function-configuration)
- [Processor
State Control for Your Amazon EC2 Instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/processor_state_control.html)
- [Deep
Dive on Amazon ECS Cluster Auto Scaling](https://aws.amazon.com/blogs/containers/deep-dive-on-amazon-ecs-cluster-auto-scaling/)
- [Introducing
Karpenter – An Open-Source High-Performance Kubernetes Cluster
Autoscaler](https://aws.amazon.com/blogs/aws/introducing-karpenter-an-open-source-high-performance-kubernetes-cluster-autoscaler/)

**Related videos:**

- [AWS re:Invent 2023 – AWS Graviton: The best price performance for your AWS workloads](https://www.youtube.com/watch?v=T_hMIjKtSr4)
- [AWS re:Invent 2023 – New Amazon EC2 generative AI capabilities in AWS Management Console](https://www.youtube.com/watch?v=sSpJ8tWCEiA)
- [AWS re:Invent 2023 – What’s new with Amazon EC2](https://www.youtube.com/watch?v=mjHw_wgJJ5g)
- [AWS re:Invent 2023 – Smart savings: Amazon EC2 cost-optimization strategies](https://www.youtube.com/watch?v=_AHPbxzIGV0)
- [AWS re:Invent 2021 – Powering next-gen Amazon EC2: Deep dive on the Nitro System](https://www.youtube.com/watch?v=2uc1vaEsPXU)
- [AWS re:Invent 2019 – Amazon EC2 foundations](https://www.youtube.com/watch?v=kMMybKqC2Y0)

**Related examples:**

- [Amazon EC2 Auto Scaling Group Examples](https://github.com/aws-samples/amazon-ec2-auto-scaling-group-examples)
- [Amazon EKS Workshop](https://www.eksworkshop.com/)
- [Scale your Amazon EKS workloads by running on IPv6](https://catalog.us-east-1.prod.workshops.aws/workshops/3b06259f-8e17-4f2f-811a-75c9b06a2807/en-US)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_compute_hardware_scale_compute_resources_dynamically.html*

---

# PERF02-BP06 Use optimized hardware-based compute accelerators

Use hardware accelerators to perform certain functions more efficiently than CPU-based
alternatives.

**Common anti-patterns:**

- In your workload, you haven't benchmarked a general-purpose instance against a
purpose-built instance that can deliver higher performance and lower cost.
- You are using hardware-based compute accelerators for tasks that can be more efficient
using CPU-based alternatives.
- You are not monitoring GPU usage.

**Benefits of establishing this best practice:** By using
hardware-based accelerators, such as graphics processing units (GPUs) and field programmable
gate arrays (FPGAs), you can perform certain processing functions more efficiently.

**Level of risk exposed if this best practice is not established:**
Medium

## Implementation guidance

Accelerated computing instances provide access to hardware-based compute accelerators
such as GPUs and FPGAs. These hardware accelerators perform certain functions like graphic
processing or data pattern matching more efficiently than CPU-based alternatives. Many
accelerated workloads, such as rendering, transcoding, and machine learning, are highly
variable in terms of resource usage. Only run this hardware for the time needed, and
decommission them with automation when not required to improve overall performance efficiency.

### Implementation steps

- Identify which [accelerated
computing instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/accelerated-computing-instances.html) can address your requirements.
- For machine learning workloads, take advantage of purpose-built hardware that is
specific to your workload, such as [AWS Trainium](https://aws.amazon.com/machine-learning/trainium/), [AWS Inferentia](https://aws.amazon.com/machine-learning/inferentia/), and [Amazon EC2 DL1](https://aws.amazon.com/ec2/instance-types/dl1/). AWS Inferentia
instances such as Inf2 instances [offer up to 50% better performance/watt over
comparable Amazon EC2 instances](https://aws.amazon.com/machine-learning/inferentia/).
- Collect usage metrics for your accelerated computing instances. For example, you
can use CloudWatch agent to collect metrics such as `utilization_gpu` and
`utilization_memory` for your GPUs as shown in [Collect NVIDIA GPU
metrics with Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Agent-NVIDIA-GPU.html).
- Optimize the code, network operation, and settings of hardware accelerators to make
sure that underlying hardware is fully utilized.

[Optimize
GPU settings](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/optimize_gpu.html)
- [GPU
Monitoring and Optimization in the Deep Learning AMI](https://docs.aws.amazon.com/dlami/latest/devguide/tutorial-gpu.html)
- [Optimizing I/O for GPU performance tuning of deep learning training in
Amazon SageMaker AI](https://aws.amazon.com/blogs/machine-learning/optimizing-i-o-for-gpu-performance-tuning-of-deep-learning-training-in-amazon-sagemaker/)

- Use the latest high performant libraries and GPU drivers.
- Use automation to release GPU instances when not in use.

## Resources

**Related documents:**

- [Working
with GPUs on Amazon Elastic Container Service](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-gpu.html)
- [GPU
instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/accelerated-computing-instances.html#gpu-instances)
- [Instances with AWS Trainium](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/accelerated-computing-instances.html#aws-trainium-instances)
- [Instances with AWS Inferentia](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/accelerated-computing-instances.html#aws-inferentia-instances)
- [Let’s Architect!
Architecting with custom chips and accelerators](https://aws.amazon.com/blogs/architecture/lets-architect-custom-chips-and-accelerators/)

- [Accelerated
Computing](https://aws.amazon.com/ec2/instance-types/#Accelerated_Computing)
- [Amazon EC2 VT1 Instances](https://aws.amazon.com/ec2/instance-types/vt1/)
- [How do I
choose the appropriate Amazon EC2 instance type for my workload?](https://aws.amazon.com/premiumsupport/knowledge-center/ec2-instance-choose-type-for-workload/)
- [Choose the best AI accelerator and model compilation for computer vision inference with
Amazon SageMaker AI](https://aws.amazon.com/blogs/machine-learning/choose-the-best-ai-accelerator-and-model-compilation-for-computer-vision-inference-with-amazon-sagemaker/)

**Related videos:**

- AWS re:Invent 2021 - [How to select
Amazon Elastic Compute Cloud GPU instances for deep learning](https://www.youtube.com/watch?v=4bVrIbgGWEA&ab_channel=AWSEvents)
- [AWS
re:Invent 2022 - [NEW LAUNCH!] Introducing AWS Inferentia2-based Amazon EC2 Inf2
instances](https://www.youtube.com/watch?v=jpqiG02Y2H4&ab_channel=AWSEvents)
- [AWS
re:Invent 2022 - Accelerate deep learning and innovate faster with AWS
Trainium](https://www.youtube.com/watch?v=YRqvfNwqUIA&ab_channel=AWSEvents)
- [AWS
re:Invent 2022 - Deep learning on AWS with NVIDIA: From training to deployment](https://www.youtube.com/watch?v=l8AFfaCkp0E&ab_channel=AWSEvents)

**Related examples:**

- [Amazon SageMaker AI
and NVIDIA GPU Cloud (NGC)](https://github.com/aws-samples/amazon-sagemaker-nvidia-ngc-examples)
- [Use SageMaker AI with
Trainium and Inferentia for optimized deep learning training and inferencing
workloads](https://github.com/aws-samples/sagemaker-trainium-inferentia)
- [Optimizing
NLP models with Amazon Elastic Compute Cloud Inf1 instances in Amazon SageMaker AI](https://github.com/aws-samples/aws-inferentia-huggingface-workshop)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_compute_hardware_compute_accelerators.html*

---

---

## Question PERF03

# PERF 3 — How do you store, manage, and access data?

**Pillar**: Performance Efficiency  
**Best Practices**: 5

---

# PERF03-BP01 Use a purpose-built data store that best supports your data access and storage requirements

Understand data characteristics (like shareable, size, cache size, access patterns,
latency, throughput, and persistence of data) to select the right purpose-built data stores
(storage or database) for your workload.

**Common anti-patterns:**

- You stick to one data store because there is internal experience and knowledge of one
particular type of database solution.
- You assume that all workloads have similar data storage and access requirements.
- You have not implemented a data catalog to inventory your data assets.

**Benefits of establishing this best practice:** Understanding data
characteristics and requirements allows you to determine the most efficient and performant
storage technology appropriate for your workload needs.

**Level of risk exposed if this best practice is not established:**
High

## Implementation guidance

When selecting and implementing data storage, make sure that the querying, scaling, and
storage characteristics support the workload data requirements. AWS provides numerous data
storage and database technologies including block storage, object storage, streaming storage,
file system, relational, key-value, document, in-memory, graph, time series, and ledger
databases. Each data management solution has options and configurations available to you to
support your use-cases and data models. By understanding data characteristics and
requirements, you can break away from monolithic storage technology and restrictive,
one-size-fits-all approaches to focus on managing data appropriately.

### Implementation steps

- Conduct an inventory of the various data types that exist in your workload.
- Understand and document data characteristics and requirements, including:

Data type (unstructured, semi-structured, relational)
- Data volume and growth
- Data durability: persistent, ephemeral, transient
- ACID (atomicity, consistency, isolation, durability) requirements
- Data access patterns (read-heavy or write-heavy)
- Latency
- Throughput
- IOPS (input/output operations per second)
- Data retention period

- Learn about different data stores ([storage](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/storage-services.html) and [database](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/database.html) services) available for
your workload on AWS that can meet your data characteristics, as outlined in [PERF01-BP01 Learn about and understand available cloud services and features](./perf_architecture_understand_cloud_services_and_features.html). Some examples of
AWS storage technologies and their key characteristics include:

**Type**

**AWS Services**

**Key characteristics**

Object storage

[Amazon S3](https://aws.amazon.com/s3/)

Unlimited scalability, high availability, and multiple options for
accessibility. Transferring and accessing objects in and out of Amazon S3 can use a
service, such as [Transfer Acceleration](https://aws.amazon.com/s3/transfer-acceleration/) or [Access Points](https://aws.amazon.com/s3/features/access-points/), to support your
location, security needs, and access patterns.

Archiving storage

[Amazon Glacier](https://aws.amazon.com/s3/storage-classes/glacier/)

Built for data archiving.

Streaming storage

[Amazon Kinesis](https://aws.amazon.com/kinesis/)

[Amazon Managed Streaming for Apache Kafka (Amazon MSK)](https://aws.amazon.com/msk/)

Efficient ingestion and storage of streaming data.

Shared file system

[Amazon Elastic File System (Amazon EFS)](https://aws.amazon.com/efs/)

Mountable file system that can be accessed by multiple types of
compute solutions.

Shared file system

[Amazon FSx](https://aws.amazon.com/fsx/)

Built on the latest AWS compute solutions to support four commonly used
file systems: NetApp ONTAP, OpenZFS, Windows File Server, and Lustre.
Amazon FSx [latency,
throughput, and IOPS](https://aws.amazon.com/fsx/when-to-choose-fsx/) vary per file system and should be considered
when selecting the right file system for your workload needs.

Block storage

[Amazon Elastic Block Store (Amazon EBS)](https://aws.amazon.com/ebs/)

Scalable, high-performance block-storage service designed for Amazon Elastic Compute Cloud
(Amazon EC2). Amazon EBS includes SSD-backed storage for transactional, IOPS-intensive
workloads and HDD-backed storage for throughput-intensive workloads.

Relational database

[Amazon Aurora](https://aws.amazon.com/rds/aurora), [Amazon RDS](https://aws.amazon.com/rds), [Amazon Redshift](https://aws.amazon.com/redshift).
Designed to support ACID (atomicity, consistency, isolation, durability)
transactions, and maintain referential integrity and strong data consistency.
Many traditional applications, enterprise resource planning (ERP), customer
relationship management (CRM), and ecommerce use relational databases to store
their data.

Key-value database

[Amazon DynamoDB](https://aws.amazon.com/dynamodb/)

Optimized for common access patterns, typically to store and retrieve
large volumes of data. High-traffic web apps, ecommerce systems, and gaming
applications are typical use-cases for key-value databases.

Document database

[Amazon DocumentDB](https://aws.amazon.com/documentdb/)

Designed to store semi-structured data as JSON-like documents. These
databases help developers build and update applications such as content
management, catalogs, and user profiles quickly.

In-memory database

[Amazon ElastiCache](https://aws.amazon.com/elasticache/) , [Amazon MemoryDB for Redis](https://aws.amazon.com/memorydb/)

Used for applications that require real-time access to data, lowest
latency and highest throughput. You may use in-memory databases for application
caching, session management, gaming leaderboards, low latency ML feature store,
microservices messaging system, and a high-throughput streaming mechanism

Graph database

[Amazon Neptune](https://aws.amazon.com/neptune/)

Used for applications that must navigate and query millions of
relationships between highly connected graph datasets with millisecond latency
at large scale. Many companies use graph databases for fraud detection, social
networking, and recommendation engines.

Time Series database

[Amazon Timestream](https://aws.amazon.com/timestream/)

Used to efficiently collect, synthesize, and derive insights from data
that changes over time. IoT applications, DevOps, and industrial telemetry can
utilize time-series databases.

Wide column

[Amazon Keyspaces (for Apache
Cassandra)](https://aws.amazon.com/mcs/)

Uses tables, rows, and columns, but unlike a relational database, the
names and format of the columns can vary from row to row in the same table. You
typically see a wide column store in high scale industrial apps for equipment
maintenance, fleet management, and route optimization.

Ledger

[Amazon Quantum Ledger Database (Amazon
QLDB)](https://aws.amazon.com/qldb/)

Provides a centralized and trusted authority to maintain a scalable,
immutable, and cryptographically verifiable record of transactions for every
application. We see ledger databases used for systems of record, supply chain,
registrations, and even banking transactions.
- If you are building a data platform, leverage [modern data
architecture](https://aws.amazon.com/big-data/datalakes-and-analytics/modern-data-architecture/) on AWS to integrate your data lake, data warehouse, and
purpose-built data stores.
- The key questions that you need to consider when choosing a data store for your
workload are as follows:

Question
Things to consider

How is the data structured?

If the data is unstructured, consider an object-store such as [Amazon S3](https://aws.amazon.com/products/storage/data-lake-storage/)
or a NoSQL database such as [Amazon DocumentDB](https://aws.amazon.com/documentdb/)
- For key-value data, consider [DynamoDB](https://aws.amazon.com/documentdb/), [Amazon ElastiCache (Redis OSS)](https://aws.amazon.com/elasticache/redis/) or [Amazon MemoryDB](https://aws.amazon.com/memorydb/)

What level of referential integrity is required?

- For foreign key constraints, relational databases such as [Amazon RDS](https://aws.amazon.com/rds/) and [Aurora](https://aws.amazon.com/rds/aurora/) can provide this level of integrity.
- Typically, within a NoSQL data-model, you would de-normalize your
data into a single document or collection of documents to be retrieved in
a single request rather than joining across documents or tables.

Is ACID (atomicity, consistency, isolation, durability) compliance
required?

- If the ACID properties associated with relational databases are
required, consider a relational database such as [Amazon RDS](https://aws.amazon.com/rds/) and [Aurora](https://aws.amazon.com/rds/aurora/).
- If strong consistency is required for [NoSQL database](https://aws.amazon.com/nosql/), you can use strongly consistent
reads with [DynamoDB](https://aws.amazon.com/documentdb/).

How will the storage requirements change over time? How does this impact
scalability?

- Serverless databases such as [DynamoDB](https://aws.amazon.com/documentdb/) and [Amazon Quantum Ledger Database (Amazon QLDB)](https://aws.amazon.com/qldb/) will scale dynamically.
- Relational databases have upper bounds on provisioned storage, and
often must be horizontally partitioned using mechanisms such as sharding
once they reach these limits.

What is the proportion of read queries in relation to write queries? Would
caching be likely to improve performance?

- Read-heavy workloads can benefit from a caching layer, like [ElastiCache](https://aws.amazon.com/elasticache/) or [DAX](https://aws.amazon.com/dynamodb/dax/) if the database is
DynamoDB.
- Reads can also be offloaded to read replicas with relational
databases such as [Amazon RDS](https://aws.amazon.com/rds/).

Does storage and modification (OLTP - Online Transaction Processing) or
retrieval and reporting (OLAP - Online Analytical Processing) have a higher
priority?

- For high-throughput read as-is transactional processing, consider a
NoSQL database such as DynamoDB.
- For high-throughput and complex read patterns (like join) with
consistency use Amazon RDS.
- For analytical queries, consider a columnar database such as [Amazon Redshift](https://aws.amazon.com/redshift/) or exporting the data
to Amazon S3 and performing analytics using [Athena](https://aws.amazon.com/athena/) or [Amazon Quick](https://aws.amazon.com/quicksight/).

What level of durability does the data require?

- Aurora automatically replicates your data across three Availability
Zones within a Region, meaning your data is highly durable with less
chance of data loss.
- DynamoDB is automatically replicated across multiple Availability Zones,
providing high availability and data durability.
- Amazon S3 provides 11 nines of durability. Many database services, such as
Amazon RDS and DynamoDB, support exporting data to Amazon S3 for long-term retention
and archival.

Is there a desire to move away from commercial database engines or
licensing costs?

- Consider open-source engines such as PostgreSQL and MySQL on Amazon RDS or
Aurora.
- Leverage [AWS Database Migration Service](https://aws.amazon.com/dms/) and
[AWS Schema Conversion Tool](https://aws.amazon.com/dms/schema-conversion-tool/) to perform migrations from commercial database
engines to open-source

What is the operational expectation for the database? Is moving to managed
services a primary concern?

- Leveraging Amazon RDS instead of Amazon EC2, and DynamoDB or Amazon DocumentDB instead of
self-hosting a NoSQL database can reduce operational overhead.

How is the database currently accessed? Is it only application access, or
are there business intelligence (BI) users and other connected off-the-shelf
applications?

- If you have dependencies on external tooling then you may have to
maintain compatibility with the databases they support. Amazon RDS is fully
compatible with the difference engine versions that it supports including
Microsoft SQL Server, Oracle, MySQL, and PostgreSQL.

- Perform experiments and benchmarking in a non-production environment to identify
which data store can address your workload requirements.

## Resources

**Related documents:**

- [Amazon EBS Volume
Types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html)
- [Amazon EC2
Storage](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Storage.html)
- [Amazon EFS: Amazon EFS
Performance](https://docs.aws.amazon.com/efs/latest/ug/performance.html)
- [Amazon FSx for Lustre
Performance](https://docs.aws.amazon.com/fsx/latest/LustreGuide/performance.html)
- [Amazon FSx for Windows File Server Performance](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/performance.html)
- [Amazon Glacier:
Amazon Glacier Documentation](https://docs.aws.amazon.com/amazonglacier/latest/dev/introduction.html)
- [Amazon S3: Request Rate and
Performance Considerations](https://docs.aws.amazon.com/AmazonS3/latest/dev/request-rate-perf-considerations.html)
- [Cloud Storage with AWS](https://aws.amazon.com/products/storage/)
- [Amazon EBS I/O Characteristics](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/ebs-io-characteristics.html)
- [Cloud Databases with
AWS](https://aws.amazon.com/products/databases/?ref=wellarchitected)
- [AWS Database
Caching](https://aws.amazon.com/caching/database-caching/?ref=wellarchitected)
- [DynamoDB Accelerator](https://aws.amazon.com/dynamodb/dax/?ref=wellarchitected)
- [Amazon Aurora
best practices](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Aurora.BestPractices.html?ref=wellarchitected)
- [Amazon Redshift performance](https://docs.aws.amazon.com/redshift/latest/dg/c_challenges_achieving_high_performance_queries.html?ref=wellarchitected)
- [Amazon Athena top 10 performance tips](https://aws.amazon.com/blogs/big-data/top-10-performance-tuning-tips-for-amazon-athena/?ref=wellarchitected)
- [Amazon Redshift Spectrum best practices](https://aws.amazon.com/blogs/big-data/10-best-practices-for-amazon-redshift-spectrum/?ref=wellarchitected)
- [Amazon DynamoDB best practices](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/BestPractices.html?ref=wellarchitected)
- [Choose between
Amazon EC2 and Amazon RDS](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-sql-server/comparison.html)
- [Best Practices for Implementing Amazon ElastiCache](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/BestPractices.html)

**Related videos:**

- [AWS re:Invent 2023: Improve
Amazon Elastic Block Store efficiency and be more cost-efficient](https://www.youtube.com/watch?v=7-CB02rqiuw)
- [AWS re:Invent 2023: Optimizing
storage price and performance with Amazon Simple Storage Service](https://www.youtube.com/watch?v=RxgYNrXPOLw)
- [AWS re:Invent 2023: Building
and optimizing a data lake on Amazon Simple Storage Service](https://www.youtube.com/watch?v=mpQa_Zm1xW8)
- [AWS re:Invent 2022: Building
modern data architectures on AWS](https://www.youtube.com/watch?v=Uk2CqEt5f0o)
- [AWS re:Invent 2022: Building
data mesh architectures on AWS](https://www.youtube.com/watch?v=nGRvlobeM_U)
- [AWS re:Invent 2023: Deep dive
into Amazon Aurora and its innovations](https://www.youtube.com/watch?v=je6GCOZ22lI)
- [AWS re:Invent 2023: Advanced
data modeling with Amazon DynamoDB](https://www.youtube.com/watch?v=PVUofrFiS_A)
- [AWS re:Invent 2022:
Modernize apps with purpose-built databases](https://www.youtube.com/watch?v=V-DiplATdi0)
- [Amazon DynamoDB deep dive:
Advanced design patterns](https://www.youtube.com/watch?v=6yqfmXiZTlM)

**Related examples:**

- [AWS Purpose Built Databases Workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/93f64257-52be-4c12-a95b-c0a1ff3b7e2b/en-US)
- [Databases for Developers](https://catalog.workshops.aws/db4devs/en-US)
- [AWS Modern Data Architecture Immersion Day](https://catalog.us-east-1.prod.workshops.aws/workshops/32f3e732-d67d-4c63-b967-c8c5eabd9ebf/en-US)
- [Build a Data Mesh on AWS](https://catalog.us-east-1.prod.workshops.aws/workshops/23e6326b-58ee-4ab0-9bc7-3c8d730eb851/en-US)
- [Amazon S3 Examples](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/s3-examples.html)
- [Optimize Data Pattern using Amazon Redshift Data Sharing](https://wellarchitectedlabs.com/sustainability/300_labs/300_optimize_data_pattern_using_redshift_data_sharing/)
- [Database
Migrations](https://github.com/aws-samples/aws-database-migration-samples)
- [MS SQL Server - AWS Database Migration Service
(AWS DMS) Replication Demo](https://github.com/aws-samples/aws-dms-sql-server)
- [Database
Modernization Hands On Workshop](https://github.com/aws-samples/amazon-rds-purpose-built-workshop)
- [Amazon Neptune
Samples](https://github.com/aws-samples/amazon-neptune-samples)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_data_use_purpose_built_data_store.html*

---

# PERF03-BP02 Evaluate available configuration options for data store

Understand and evaluate the various features and configuration options available for your
data stores to optimize storage space and performance for your workload.

**Common anti-patterns:**

- You only use one storage type, such as Amazon EBS, for all workloads.
- You use provisioned IOPS for all workloads without real-world testing against all
storage tiers.
- You are not aware of the configuration options of your chosen data management solution.
- You rely solely on increasing instance size without looking at other available
configuration options.
- You are not testing the scaling characteristics of your data store.

**Benefits of establishing this best practice:** By exploring and
experimenting with the data store configurations, you may be able to reduce the cost of
infrastructure, improve performance, and lower the effort required to maintain your workloads.

**Level of risk exposed if this best practice is not established:**
Medium

## Implementation guidance

A workload could have one or more data stores used based on data storage and access
requirements. To optimize your performance efficiency and cost, you must evaluate data access
patterns to determine the appropriate data store configurations. While you explore data store
options, take into consideration various aspects such as the storage options, memory, compute,
read replica, consistency requirements, connection pooling, and caching options. Experiment
with these various configuration options to improve performance efficiency metrics.

### Implementation steps

- Understand the current configurations (like instance type, storage size, or
database engine version) of your data store.
- Review AWS documentation and best practices to learn about recommended
configuration options that can help improve the performance of your data store. Key data
store options to consider are the following:

Configuration option
Examples

Offloading reads (like read replicas and caching)

For DynamoDB tables, you can offload reads using DAX for caching.
- You can create an Amazon ElastiCache (Redis OSS) cluster and configure your application
to read from the cache first, falling back to the database if the
requested item is not present.
- Relational databases such as Amazon RDS and Aurora, and provisioned NoSQL
databases such as Neptune and Amazon DocumentDB all support adding read replicas
to offload the read portions of the workload.
- Serverless databases such as DynamoDB will scale automatically. Ensure
that you have enough read capacity units (RCU) provisioned to handle the
workload.

Scaling writes (like partition key sharding or introducing a queue)

- For relational databases, you can increase the size of the instance
to accommodate an increased workload or increase the provisioned IOPs to
allow for an increased throughput to the underlying storage.
- You can also introduce a queue in front of your database rather than
writing directly to the database. This pattern allows you to decouple the
ingestion from the database and control the flow-rate so the database does
not get overwhelmed.
- Batching your write requests rather than creating many short-lived
transactions can help improve throughput in high-write volume relational
databases.
- Serverless databases like DynamoDB can scale the write throughput
automatically or by adjusting the provisioned write capacity units (WCU)
depending on the capacity mode.
- You can still run into issues with hot partitions when you reach the
throughput limits for a given partition key. This can be mitigated by
choosing a more evenly distributed partition key or by write-sharding the
partition key.

Policies to manage the lifecycle of your datasets

- You can use [Amazon S3
Lifecycle](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html) to manage your objects throughout their lifecycle. If
your access patterns are unknown, changing, or unpredictable, you can
use [Amazon S3
Intelligent-Tiering](https://docs.aws.amazon.com/AmazonS3/latest/userguide/intelligent-tiering.html), which monitors access patterns and
automatically moves objects that have not been accessed to lower-cost
access tiers. You can leverage [Amazon S3 Storage
Lens](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage_lens.html) metrics to identify optimization opportunities and gaps in
lifecycle management.
- [Amazon EFS lifecycle
management](https://docs.aws.amazon.com/efs/latest/ug/lifecycle-management-efs.html) automatically manages file storage for your file
systems.

Connection management and pooling

- Amazon RDS Proxy can be used with Amazon RDS and Aurora to manage connections to
the database.
- Serverless databases such as DynamoDB do not have connections associated
with them, but consider the provisioned capacity and automatic scaling
policies to deal with spikes in load.

- Perform experiments and benchmarking in non-production environment to identify
which configuration option can address your workload requirements.
- Once you have experimented, plan your migration and validate your performance
metrics.
- Use AWS monitoring (like [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)) and optimization (like [Amazon S3 Storage Lens](https://aws.amazon.com/s3/storage-lens/)) tools to continuously optimize your
data store using real-world usage pattern.

## Resources

**Related documents:**

- [Cloud Storage with
AWS](https://aws.amazon.com/products/storage/?ref=wellarchitected)
- [Amazon EBS Volume
Types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html)
- [Amazon EC2
Storage](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Storage.html)
- [Amazon EFS: Amazon EFS
Performance](https://docs.aws.amazon.com/efs/latest/ug/performance.html)
- [Amazon FSx for Lustre
Performance](https://docs.aws.amazon.com/fsx/latest/LustreGuide/performance.html)
- [Amazon FSx for Windows File Server Performance](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/performance.html)
- [Amazon Glacier:
Amazon Glacier Documentation](https://docs.aws.amazon.com/amazonglacier/latest/dev/introduction.html)
- [Amazon S3: Request Rate and
Performance Considerations](https://docs.aws.amazon.com/AmazonS3/latest/dev/request-rate-perf-considerations.html)
- [Amazon EBS I/O Characteristics](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/ebs-io-characteristics.html)
- [Cloud Databases with
AWS](https://aws.amazon.com/products/databases/?ref=wellarchitected)
- [AWS Database
Caching](https://aws.amazon.com/caching/database-caching/?ref=wellarchitected)
- [DynamoDB Accelerator](https://aws.amazon.com/dynamodb/dax/?ref=wellarchitected)
- [Amazon Aurora
best practices](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Aurora.BestPractices.html?ref=wellarchitected)
- [Amazon Redshift performance](https://docs.aws.amazon.com/redshift/latest/dg/c_challenges_achieving_high_performance_queries.html?ref=wellarchitected)
- [Amazon Athena top 10 performance tips](https://aws.amazon.com/blogs/big-data/top-10-performance-tuning-tips-for-amazon-athena/?ref=wellarchitected)
- [Amazon Redshift Spectrum best practices](https://aws.amazon.com/blogs/big-data/10-best-practices-for-amazon-redshift-spectrum/?ref=wellarchitected)
- [Amazon DynamoDB best practices](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/BestPractices.html?ref=wellarchitected)

**Related videos:**

- [AWS
re:Invent 2023: Improve Amazon Elastic Block Store efficiency and be more cost-efficient](https://www.youtube.com/watch?v=7-CB02rqiuw)
- [AWS
re:Invent 2023: Optimize storage price and performance with Amazon Simple Storage Service](https://www.youtube.com/watch?v=RxgYNrXPOLw)
- [AWS
re:Invent 2023: Building and optimizing a data lake on Amazon Simple Storage Service](https://www.youtube.com/watch?v=mpQa_Zm1xW8)
- [AWS
re:Invent 2023: What's new with AWS file storage](https://www.youtube.com/watch?v=yXIeIKlTFV0)
- [AWS
re:Invent 2023: Dive deep into Amazon DynamoDB](https://www.youtube.com/watch?v=ld-xoehkJuU)

**Related examples:**

- [AWS Purpose Built Databases Workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/93f64257-52be-4c12-a95b-c0a1ff3b7e2b/en-US)
- [Databases for Developers](https://catalog.workshops.aws/db4devs/en-US)
- [AWS Modern Data Architecture Immersion Day](https://catalog.us-east-1.prod.workshops.aws/workshops/32f3e732-d67d-4c63-b967-c8c5eabd9ebf/en-US)
- [Amazon EBS Autoscale](https://github.com/awslabs/amazon-ebs-autoscale)
- [Amazon S3 Examples](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/s3-examples.html)
- [Amazon DynamoDB
Examples](https://github.com/aws-samples/aws-dynamodb-examples)
- [AWS Database
migration samples](https://github.com/aws-samples/aws-database-migration-samples)
- [Database
Modernization Workshop](https://github.com/aws-samples/amazon-rds-purpose-built-workshop)
- [Working with parameters on your Amazon RDS for Postgress DB](https://github.com/awsdocs/amazon-rds-user-guide/blob/main/doc_source/Appendix.PostgreSQL.CommonDBATasks.Parameters.md)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_data_evaluate_configuration_options_data_store.html*

---

# PERF03-BP03 Collect and record data store performance metrics

Track and record relevant performance metrics for your data store to
understand how your data management solutions are performing. These
metrics can help you optimize your data store, verify that your
workload requirements are met, and provide a clear overview on how
the workload performs.

**Common anti-patterns:**

- You only use manual log file searching for metrics.
- You only publish metrics to internal tools used by your team and
don’t have a comprehensive picture of your workload.
- You only use the default metrics recorded by your selected
monitoring software.
- You only review metrics when there is an issue.
- You only monitor system-level metrics and do not capture data
access or usage metrics.

**Benefits of establishing this best
practice:** Establishing a performance baseline helps you
understand the normal behavior and requirements of workloads.
Abnormal patterns can be identified and debugged faster, improving
the performance and reliability of the data store.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

To monitor the performance of your data stores, you must record
multiple performance metrics over a period of time. This allows
you to detect anomalies, as well as measure performance against
business metrics to verify you are meeting your workload needs.

Metrics should include both the underlying system that is
supporting the data store and the database metrics. The underlying
system metrics might include CPU utilization, memory, available
disk storage, disk I/O, cache hit ratio, and network inbound and
outbound metrics, while the data store metrics might include
transactions per second, top queries, average queries rates,
response times, index usage, table locks, query timeouts, and
number of connections open. This data is crucial to understand how
the workload is performing and how the data management solution is
used. Use these metrics as part of a data-driven approach to tune
and optimize your workload's resources.

Use tools, libraries, and systems that record performance
measurements related to database performance.

## Implementation steps

- Identify the key performance metrics for your data store to
track.

[Amazon S3 Metrics and dimensions](https://docs.aws.amazon.com/AmazonS3/latest/userguide/metrics-dimensions.html)
- [Monitoring
metrics for in an Amazon RDS instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Monitoring.html)
- [Monitoring DB load with Performance Insights on Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.html)
- [Overview of Enhanced
Monitoring](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring.OS.overview.html)
- [DynamoDB
Metrics and dimensions](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/metrics-dimensions.html)
- [Monitoring
DynamoDB Accelerator](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.Monitoring.html)
- [Monitoring
Amazon MemoryDB with Amazon CloudWatch](https://docs.aws.amazon.com/memorydb/latest/devguide/monitoring-cloudwatch.html)
- [Which Metrics Should I Monitor?](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/CacheMetrics.WhichShouldIMonitor.html)
- [Monitoring
Amazon Redshift cluster performance](https://docs.aws.amazon.com/redshift/latest/mgmt/metrics.html)
- [Timestream
metrics and dimensions](https://docs.aws.amazon.com/timestream/latest/developerguide/metrics-dimensions.html)
- [Amazon CloudWatch metrics for Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraMonitoring.Metrics.html)
- [Logging and monitoring in Amazon Keyspaces (for Apache Cassandra)](https://docs.aws.amazon.com/keyspaces/latest/devguide/monitoring.html)
- [Monitoring
Amazon Neptune Resources](https://docs.aws.amazon.com/neptune/latest/userguide/monitoring.html)

- Use an approved logging and monitoring solution to collect
these metrics.
[Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) can collect metrics across the resources in
your architecture. You can also collect and publish custom
metrics to surface business or derived metrics. Use CloudWatch
or third-party solutions to set alarms that indicate when
thresholds are breached.
- Check if data store monitoring can benefit from a machine
learning solution that detects performance anomalies.

[Amazon DevOps Guru for Amazon RDS](https://docs.aws.amazon.com/devops-guru/latest/userguide/working-with-rds.overview.how-it-works.html) provides visibility into
performance issues and makes recommendations for
corrective actions.

- Configure data retention in your monitoring and logging
solution to match your security and operational goals.

[Default
data retention for CloudWatch metrics](https://aws.amazon.com/cloudwatch/faqs/#AWS_resource_.26_custom_metrics_monitoring)
- [Default
data retention for CloudWatch Logs](https://aws.amazon.com/cloudwatch/faqs/#Log_management)

## Resources

**Related documents:**

- [AWS Database Caching](https://aws.amazon.com/caching/database-caching/)
- [Amazon Athena top 10 performance tips](https://aws.amazon.com/blogs/big-data/top-10-performance-tuning-tips-for-amazon-athena/)
- [Amazon Aurora best practices](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Aurora.BestPractices.html)
- [DynamoDB Accelerator](https://aws.amazon.com/dynamodb/dax/)
- [Amazon DynamoDB best practices](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/BestPractices.html)
- [Amazon Redshift Spectrum best practices](https://aws.amazon.com/blogs/big-data/10-best-practices-for-amazon-redshift-spectrum/)
- [Amazon Redshift performance](https://docs.aws.amazon.com/redshift/latest/dg/c_challenges_achieving_high_performance_queries.html)
- [Cloud
Databases with AWS](https://aws.amazon.com/products/databases/)
- [Amazon RDS Performance Insights](https://aws.amazon.com/rds/performance-insights/)

**Related videos:**

- [AWS re:Invent 2022 - Performance monitoring with Amazon RDS and Aurora, featuring Autodesk](https://www.youtube.com/watch?v=wokRbwK4YLo)
- [Database Performance Monitoring and Tuning with Amazon DevOps Guru for Amazon RDS](https://www.youtube.com/watch?v=cHKuVH7YGBE)
- [AWS re:Invent 2023 - What’s new with AWS file storage](https://www.youtube.com/watch?v=yXIeIKlTFV0)
- [AWS re:Invent 2023 - Dive deep into Amazon DynamoDB](https://www.youtube.com/watch?v=ld-xoehkJuU)
- [AWS re:Invent 2023 - Building and optimizing a data lake on Amazon S3](https://www.youtube.com/watch?v=mpQa_Zm1xW8)
- [AWS re:Invent 2023 - What’s new with AWS file storage](https://www.youtube.com/watch?v=yXIeIKlTFV0)
- [AWS re:Invent 2023 - Dive deep into Amazon DynamoDB](https://www.youtube.com/watch?v=ld-xoehkJuU)
- [Best
Practices for Monitoring Redis Workloads on Amazon ElastiCache](https://www.youtube.com/watch?v=c-hTMLN35BY&ab_channel=AWSOnlineTechTalks)

**Related examples:**

- [AWS Dataset Ingestion Metrics Collection Framework](https://github.com/awslabs/aws-dataset-ingestion-metrics-collection-framework)
- [Amazon RDS Monitoring Workshop](https://www.workshops.aws/?tag=Enhanced%20Monitoring)
- [AWS Purpose Built Databases Workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/93f64257-52be-4c12-a95b-c0a1ff3b7e2b/en-US)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_data_collect_record_data_store_performance_metrics.html*

---

# PERF03-BP04 Implement strategies to improve query performance in data store

Implement strategies to optimize data and improve data query to
enable more scalability and efficient performance for your workload.

**Common anti-patterns:**

- You do not partition data in your data store.
- You store data in only one file format in your data store.
- You do not use indexes in your data store.

**Benefits of establishing this best
practice:** Optimizing data and query performance
results in more efficiency, lower cost, and improved user
experience.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Data optimization and query tuning are critical aspects of performance efficiency in a data store, as they impact the performance and responsiveness of the entire cloud workload. Unoptimized queries can result in greater resource usage and bottlenecks, which reduce the overall efficiency of a data store.

Data optimization includes several techniques to ensure efficient data storage and access. This also help to improve the query performance in a data store. Key strategies include data partitioning, data compression, and data denormalization, which help data to be optimized for both storage and access.

### Implementation steps

- Understand and analyze the critical data queries which are
performed in your data store.
- Identify the slow-running queries in your data store and use query
plans to understand their current state.

[Analyzing
the query plan in Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/dg/c-analyzing-the-query-plan.html)
- [Using
EXPLAIN and EXPLAIN ANALYZE in Athena](https://docs.aws.amazon.com/athena/latest/ug/athena-explain-statement.html)

- Implement strategies to improve the query performance. Some
of the key strategies include:

Using a [columnar file format](https://docs.aws.amazon.com/athena/latest/ug/columnar-storage.html) (like Parquet or ORC).
- Compressing data in the data store to reduce storage space and I/O operation.
- Data partitioning to split data into smaller parts and
reduce data scanning time.

[Partitioning data in Athena](https://docs.aws.amazon.com/athena/latest/ug/partitions.html)
- [Partitions and data distribution](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.Partitions.html)

- Data indexing on the common columns in the query.
- Use materialized views for frequent queries.

[Understanding materialized views](https://docs.aws.amazon.com/prescriptive-guidance/latest/materialized-views-redshift/understanding-materialized-views.html)
- [Creating materialized views in Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/dg/materialized-view-overview.html)

- Choose the right join operation for the query. When you join two tables, specify the larger table on the left side of join and the smaller table on the right side of the join.
- Distributed caching solution to improve latency and reduce
the number of database I/O operation.
- Regular maintenance such as [vacuuming](https://docs.aws.amazon.com/prescriptive-guidance/latest/postgresql-maintenance-rds-aurora/autovacuum.html), reindexing, and [running statistics](https://docs.aws.amazon.com/redshift/latest/dg/t_Analyzing_tables.html).

- Experiment and test strategies in a non-production
environment.

## Resources

**Related documents:**

- [Amazon Aurora best practices](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Aurora.BestPractices.html?ref=wellarchitected)
- [Amazon Redshift performance](https://docs.aws.amazon.com/redshift/latest/dg/c_challenges_achieving_high_performance_queries.html?ref=wellarchitected)
- [Amazon Athena top 10 performance tips](https://aws.amazon.com/blogs/big-data/top-10-performance-tuning-tips-for-amazon-athena/?ref=wellarchitected)
- [AWS Database Caching](https://aws.amazon.com/caching/database-caching/?ref=wellarchitected)
- [Best
Practices for Implementing Amazon ElastiCache](https://docs.aws.amazon.com/AmazonElastiCache/latest/UserGuide/BestPractices.html)
- [Partitioning
data in Athena](https://docs.aws.amazon.com/athena/latest/ug/partitions.html)

**Related videos:**

- [AWS re:Invent 2023 - AWS storage cost-optimization best practices](https://www.youtube.com/watch?v=8LVKNHcA6RY)
- [AWS re:Invent 2022 - Performance monitoring with Amazon RDS and Aurora, featuring Autodesk](https://www.youtube.com/watch?v=wokRbwK4YLo)
- [Optimize
Amazon Athena Queries with New Query Analysis Tools](https://www.youtube.com/watch?v=7JUyTqglmNU&ab_channel=AmazonWebServices)

**Related examples:**

- [AWS Purpose Built Databases Workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/93f64257-52be-4c12-a95b-c0a1ff3b7e2b/en-US)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_data_implement_strategies_to_improve_query_performance.html*

---

# PERF03-BP05 Implement data access patterns that utilize caching

Implement access patterns that can benefit from caching data for
fast retrieval of frequently accessed data.

**Common anti-patterns:**

- You cache data that changes frequently.
- You rely on cached data as if it is durably stored and always
available.
- You don't consider the consistency of your cached data.
- You don't monitor the efficiency of your caching implementation.

**Benefits of establishing this best
practice:** Storing data in a cache can improve read
latency, read throughput, user experience, and overall efficiency,
as well as reduce costs.

**Level of risk exposed if this best practice
is not established**: Medium

## Implementation guidance

A cache is a software or hardware component aimed at storing data
so that future requests for the same data can be served faster or
more efficiently. The data stored in a cache can be reconstructed
if lost by repeating an earlier calculation or fetching it from
another data store.

Data caching can be one of the most effective strategies to
improve your overall application performance and reduce burden on
your underlying primary data sources. Data can be cached at
multiple levels in the application, such as within the application
making remote calls, known as *client-side
caching*, or by using a fast secondary service for
storing the data, known as *remote caching*.

**Client-side caching**

With client-side caching, each client (an application or service
that queries the backend datastore) can store the results of their
unique queries locally for a specified amount of time. This can
reduce the number of requests across the network to a datastore by
checking the local client cache first. If the results are not
present, the application can then query the datastore and store
those results locally. This pattern allows each client to store
data in the closest location possible (the client itself),
resulting in the lowest possible latency. Clients can also
continue to serve some queries when the backend datastore is
unavailable, increasing the availability of the overall system.

One disadvantage of this approach is that when multiple clients are involved, they may store the same cached data locally. This results in both duplicate storage usage and data inconsistency between those clients. One client might cache the results of a query, and one minute later another client can run the same query and get a different result.

**Remote caching**

To solve the issue of duplicate data between clients, a fast
external service, or *remote cache*, can be
used to store the queried data. Instead of checking a local data
store, each client will check the remote cache before querying the
backend datastore. This strategy allows for more consistent
responses between clients, better efficiency in stored data, and a
higher volume of cached data because the storage space scales
independently of clients.

The disadvantage of a remote cache is that the overall system may
see a higher latency, as an additional network hop is required to
check the remote cache. Client-side caching can be used alongside
remote caching for multi-level caching to improve the latency.

### Implementation steps

- Identify databases, APIs and network services that could
benefit from caching. Services that have heavy read
workloads, have a high read-to-write ratio, or are expensive
to scale are candidates for caching.

[Database
Caching](https://aws.amazon.com/caching/database-caching/)
- [Enabling
API caching to enhance responsiveness](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-caching.html)

- Identify the appropriate type of caching strategy that best
fits your access pattern.

[Caching
strategies](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/Strategies.html)
- [AWS Caching Solutions](https://aws.amazon.com/caching/aws-caching/)

- Follow
[Caching
Best Practices](https://aws.amazon.com/caching/best-practices/) for your data store.
- Configure a cache invalidation strategy, such as a
time-to-live (TTL), for all data that balances freshness of
data and reducing pressure on backend datastore.
- Enable features such as automatic connection retries,
exponential backoff, client-side timeouts, and connection
pooling in the client, if available, as they can improve
performance and reliability.

[Best
practices: Redis clients and Amazon ElastiCache (Redis OSS)](https://aws.amazon.com/blogs/database/best-practices-redis-clients-and-amazon-elasticache-for-redis/)

- Monitor cache hit rate with a goal of 80% or higher. Lower
values may indicate insufficient cache size or an access
pattern that does not benefit from caching.

[Which
metrics should I monitor?](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/CacheMetrics.WhichShouldIMonitor.html)
- [Best
practices for monitoring Redis workloads on Amazon ElastiCache](https://www.youtube.com/watch?v=c-hTMLN35BY)
- [Monitoring
best practices with Amazon ElastiCache (Redis OSS) using
Amazon CloudWatch](https://aws.amazon.com/blogs/database/monitoring-best-practices-with-amazon-elasticache-for-redis-using-amazon-cloudwatch/)

- Implement
[data
replication](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/Replication.Redis.Groups.html) to offload reads to multiple instances
and improve data read performance and availability.

## Resources

**Related documents:**

- [Using
the Amazon ElastiCache Well-Architected Lens](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/WellArchitechtedLens.html)
- [Monitoring
best practices with Amazon ElastiCache (Redis OSS) using Amazon CloudWatch](https://aws.amazon.com/blogs/database/monitoring-best-practices-with-amazon-elasticache-for-redis-using-amazon-cloudwatch/)
- [Which
Metrics Should I Monitor?](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/CacheMetrics.WhichShouldIMonitor.html)
- [Performance
at Scale with Amazon ElastiCache whitepaper](https://docs.aws.amazon.com/whitepapers/latest/scale-performance-elasticache/scale-performance-elasticache.html)
- [Caching
challenges and strategies](https://aws.amazon.com/builders-library/caching-challenges-and-strategies/)

**Related videos:**

- [Amazon ElastiCache Learning Path](https://pages.awscloud.com/GLB-WBNR-AWS-OTT-2021_LP_0003-DAT_AmazonElastiCache.html)
- [Design for
success with Amazon ElastiCache best practices](https://youtu.be/_4SkEy6r-C4)
- [AWS re:Invent 2020 - Design for success with Amazon ElastiCache best practices](https://www.youtube.com/watch?v=_4SkEy6r-C4)
- [AWS re:Invent 2023 - [LAUNCH] Introducing Amazon ElastiCache Serverless](https://www.youtube.com/watch?v=YYStP97pbXo)
- [AWS re:Invent 2022 - 5 great ways to reimagine your data layer with Redis](https://www.youtube.com/watch?v=CD1kvauvKII)
- [AWS re:Invent 2021 - Deep dive on Amazon ElastiCache (Redis OSS)](https://www.youtube.com/watch?v=QEKDpToureQ)

**Related examples:**

- [Boosting
MySQL database performance with Amazon ElastiCache (Redis OSS)](https://aws.amazon.com/getting-started/hands-on/boosting-mysql-database-performance-with-amazon-elasticache-for-redis/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_data_access_patterns_caching.html*

---

---

## Question PERF04

# PERF 4 — How do you select and configure networking resources?

**Pillar**: Performance Efficiency  
**Best Practices**: 7

---

# PERF04-BP01 Understand how networking impacts performance

Analyze and understand how network-related decisions impact your
workload to provide efficient performance and improved user
experience.

**Common anti-patterns:**

- All traffic flows through your existing data centers.
- You route all traffic through central firewalls instead of using
cloud-native network security tools.
- You provision AWS Direct Connect connections without understanding
actual usage requirements.
- You don’t consider workload characteristics and encryption
overhead when defining your networking solutions.
- You use on-premises concepts and strategies for networking
solutions in the cloud.

**Benefits of establishing this best
practice:** Understanding how networking impacts workload
performance helps you identify potential bottlenecks, improve user
experience, increase reliability, and lower operational maintenance
as the workload changes.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

The network is responsible for the connectivity between
application components, cloud services, edge networks, and
on-premises data, and therefore it can heavily impact workload
performance. In addition to workload performance, user experience
can be also impacted by network latency, bandwidth, protocols,
location, network congestion, jitter, throughput, and routing
rules.

Have a documented list of networking requirements from the
workload including latency, packet size, routing rules, protocols,
and supporting traffic patterns. Review the available networking
solutions and identify which service meets your workload
networking characteristics. Cloud-based networks can be quickly
rebuilt, so evolving your network architecture over time is
necessary to improve performance efficiency.

### Implementation steps:

- Define and document networking performance requirements,
including metrics such as network latency, bandwidth,
protocols, locations, traffic patterns (spikes and
frequency), throughput, encryption, inspection, and routing
rules.
- Learn about key AWS networking services like [VPCs](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html), [AWS Direct Connect](https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/aws-direct-connect.html), [Elastic Load Balancing (ELB)](https://aws.amazon.com/elasticloadbalancing/), and [Amazon Route 53](https://aws.amazon.com/route53/).
- Capture the following key networking characteristics:

Characteristics

Tools and metrics

Foundational networking characteristics

[VPC
Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html)
- [AWS Transit Gateway Flow Logs](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-flow-logs.html)
- [AWS Transit Gateway metrics](https://docs.aws.amazon.com/vpc/latest/tgw/transit-gateway-cloudwatch-metrics.html)
- [AWS PrivateLink metrics](https://docs.aws.amazon.com/vpc/latest/privatelink/privatelink-cloudwatch-metrics.html)

Application networking characteristics

- [Elastic
Fabric Adapter](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/monitoring-network-performance-ena.html)
- [AWS App Mesh metrics](https://docs.aws.amazon.com/app-mesh/latest/userguide/envoy-metrics.html)
- [Amazon API Gateway metrics](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-metrics-and-dimensions.html)

Edge networking characteristics

- [Amazon CloudFront metrics](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/viewing-cloudfront-metrics.html)
- [Amazon Route 53 metrics](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/monitoring-cloudwatch.html)
- [AWS Global Accelerator metrics](https://docs.aws.amazon.com/global-accelerator/latest/dg/cloudwatch-monitoring.html)

Hybrid networking characteristics

- [Direct Connect metrics](https://docs.aws.amazon.com/directconnect/latest/UserGuide/monitoring-cloudwatch.html)
- [AWS Site-to-Site VPN metrics](https://docs.aws.amazon.com/vpn/latest/s2svpn/monitoring-cloudwatch-vpn.html)
- [AWS Client VPN metrics](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/monitoring-cloudwatch.html)
- [AWS Cloud WAN metrics](https://docs.aws.amazon.com/vpc/latest/cloudwan/cloudwan-cloudwatch-metrics.html)

Security networking characteristics

- [AWS Shield, AWS WAF, and AWS Network Firewall metrics](https://docs.aws.amazon.com/waf/latest/developerguide/monitoring-cloudwatch.html)

Tracing characteristics

- [AWS X-Ray](https://aws.amazon.com/xray/)
- [VPC
Reachability Analyzer](https://docs.aws.amazon.com/vpc/latest/reachability/what-is-reachability-analyzer.html)
- [Network Access Analyzer](https://docs.aws.amazon.com/vpc/latest/network-access-analyzer/what-is-network-access-analyzer.html)
- [Amazon Inspector](https://docs.aws.amazon.com/inspector/latest/user/what-is-inspector.html)
- [Amazon CloudWatch RUM](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM.html)

- Benchmark and test network performance:

[Benchmark](https://aws.amazon.com/premiumsupport/knowledge-center/network-throughput-benchmark-linux-ec2/) network
throughput, as some factors can affect Amazon EC2 network
performance when instances are in the same VPC. Measure
the network bandwidth between Amazon EC2 Linux instances in the
same VPC.
- Perform [load
tests](https://aws.amazon.com/solutions/implementations/distributed-load-testing-on-aws/) to experiment with networking solutions and
options.

## Resources

**Related documents:**

- [Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html)
- [EC2
Enhanced Networking on Linux](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/enhanced-networking.html)
- [EC2
Enhanced Networking on Windows](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/enhanced-networking.html)
- [EC2
Placement Groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html)
- [Enabling
Enhanced Networking with the Elastic Network Adapter (ENA) on
Linux Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/enhanced-networking-ena.html)
- [Network Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html)
- [Networking
Products with AWS](https://aws.amazon.com/products/networking/)
- [Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw)
- [Transitioning
to latency-based routing in Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/TutorialTransitionToLBR.html)
- [VPC
Endpoints](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints.html)

**Related videos:**

- [AWS re:Invent 2023 - AWS networking foundations](https://www.youtube.com/watch?v=8nNurTFy-h4)
- [AWS re:Invent 2023 - What can networking do for your application?](https://www.youtube.com/watch?v=tUh26i8uY9Q)
- [AWS re:Invent 2023 - Advanced VPC designs and new capabilities](https://www.youtube.com/watch?v=cRdDCkbE4es)
- [AWS re:Invent 2023 - A developer’s guide to cloud networking](https://www.youtube.com/watch?v=i77D556lrgY)
- [AWS re:Invent 2019 - Connectivity
to AWS and hybrid AWS network architectures](https://www.youtube.com/watch?v=eqW6CPb58gs)
- [AWS re:Invent 2019 - Optimizing
Network Performance for Amazon EC2 Instances](https://www.youtube.com/watch?v=DWiwuYtIgu0)
- [AWS Summit Online - Improve Global
Network Performance for Applications](https://youtu.be/vNIALfLTW9M)
- [AWS re:Invent 2020 - Networking
best practices and tips with the Well-Architected
Framework](https://youtu.be/wOMNpG49BeM)
- [AWS re:Invent 2020 - AWS networking
best practices in large-scale migrations](https://youtu.be/qCQvwLBjcbs)

**Related examples:**

- [AWS Transit Gateway and Scalable Security Solutions](https://github.com/aws-samples/aws-transit-gateway-and-scalable-security-solutions)
- [AWS Networking Workshops](https://networking.workshop.aws/)
- [Hands-on Network Firewall Workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/d071f444-e854-4f3f-98c8-025fa0d1de2f/en-US)
- [Observing and Diagnosing your Network on AWS](https://catalog.us-east-1.prod.workshops.aws/workshops/cf2ecaa4-e4be-4f40-b93f-e9fe3b1c1f64/en-US)
- [Finding and addressing Network Misconfigurations on AWS](https://validating-network-reachability.awssecworkshops.com/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_networking_understand_how_networking_impacts_performance.html*

---

# PERF04-BP02 Evaluate available networking features

Evaluate networking features in the cloud that may increase performance. Measure the impact of these features through testing, metrics, and analysis. For example, take advantage of network-level features that are available to reduce latency, network distance, or jitter.

**Common anti-patterns:**

- You stay within one Region because that is where your headquarters is physically located.
- You use firewalls instead of security groups for filtering traffic.
- You break TLS for traffic inspection rather than relying on security groups, endpoint policies, and other cloud-native functionality.
- You only use subnet-based segmentation instead of security groups.

**Benefits of establishing this best
practice:** Evaluating all service features and options can increase your workload performance, reduce the cost of infrastructure, decrease the effort required to maintain your workload, and increase your overall security posture. You can use the global AWS backbone to provide the optimal networking experience for your customers.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

AWS offers services like [AWS Global Accelerator](https://aws.amazon.com/global-accelerator/) and [Amazon CloudFront](https://aws.amazon.com/cloudfront/) that can help improve network performance, while most AWS services have product features (such as the [Amazon S3 Transfer Acceleration](https://aws.amazon.com/s3/transfer-acceleration/) feature) to optimize network traffic.

Review which network-related configuration options are available to you and how they could impact your workload. Performance optimization depends on understanding how these options interact with your architecture and the impact that they will have on both measured performance and user experience.

### Implementation steps

- Create a list of workload components.

Consider using [AWS Cloud WAN](https://aws.amazon.com/cloud-wan/) to build, manage and monitor your organization's network when building a unified global network.
- Monitor your global and core networks with [Amazon CloudWatch Logs metrics](https://docs.aws.amazon.com/network-manager/latest/tgwnm/monitoring-cloudwatch-metrics.html). Leverage [Amazon CloudWatch RUM](https://aws.amazon.com/about-aws/whats-new/2021/11/amazon-cloudwatch-rum-applications-client-side-performance/), which provides insights to help to identify, understand, and enhance users’ digital experience.
- View aggregate network latency between AWS Regions and Availability Zones, as well as within each Availability Zone, using [AWS Network Manager](https://aws.amazon.com/transit-gateway/network-manager/) to gain insight into how your application performance relates to the performance of the underlying AWS network.
- Use an existing configuration management database (CMDB) tool or a service such as [AWS Config](https://aws.amazon.com/config/) to create an inventory of your workload and how it’s configured.

- If this is an existing workload, identify and document the benchmark for your performance metrics, focusing on the bottlenecks and areas to improve. Performance-related networking metrics will differ per workload based on business requirements and workload characteristics. As a start, these metrics might be important to review for your workload: bandwidth, latency, packet loss, jitter, and retransmits.
- If this is a new workload, perform [load tests](https://aws.amazon.com/solutions/implementations/distributed-load-testing-on-aws/) to identify performance bottlenecks.
- For the performance bottlenecks you identify, review the configuration options for your solutions to identify performance improvement opportunities. Check out the following key networking options and features:

Improvement opportunity
Solution

Network path or routes

Use [Network Access Analyzer](https://docs.aws.amazon.com/vpc/latest/network-access-analyzer/what-is-network-access-analyzer.html) to identify paths or routes.

Network protocols

See [PERF04-BP05 Choose network protocols to improve performance](./perf_networking_choose_network_protocols_improve_performance.html)

Network topology

Evaluate your operational and performance tradeoffs between [VPC Peering](https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html) and [AWS Transit Gateway](https://aws.amazon.com/transit-gateway/) when connecting multiple accounts. AWS Transit Gateway simplifies how you interconnect all of your VPCs, which can span across thousands of AWS accounts and into on-premises networks. Share your AWS Transit Gateway between multiple accounts using [AWS Resource Access Manager](https://aws.amazon.com/ram/).

See [PERF04-BP03 Choose appropriate dedicated connectivity or VPN for your workload](./perf_networking_choose_appropriate_dedicated_connectivity_or_vpn.html)

Network services

[AWS Global Accelerator](https://aws.amazon.com/global-accelerator/) is a networking service that improves the performance of your users’ traffic by up to 60% using the AWS global network infrastructure.

[Amazon CloudFront](https://aws.amazon.com/cloudfront/) can improve the performance of your workload content delivery and latency globally.

Use [Lambda@edge](https://aws.amazon.com/lambda/edge/) to run functions that customize the content that CloudFront delivers closer to the users, reduce latency, and improve performance.

Amazon Route 53 offers [latency-based routing](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-latency.html), [geolocation routing](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-geo.html), [geoproximity routing](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-geoproximity.html), and [IP-based routing](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-ipbased.html) options to help you improve your workload’s performance for a global audience. Identify which routing option would optimize your workload performance by reviewing your workload traffic and user location when your workload is distributed globally.

Storage resource features

[Amazon S3 Transfer Acceleration](https://aws.amazon.com/s3/transfer-acceleration/) is a feature that lets external users benefit from the networking optimizations of CloudFront to upload data to Amazon S3. This improves the ability to transfer large amounts of data from remote locations that don’t have dedicated connectivity to the AWS Cloud.

[Amazon S3 Multi-Region Access Points](https://docs.aws.amazon.com/AmazonS3/latest/userguide/MultiRegionAccessPoints.html) replicates content to multiple Regions and simplifies the workload by providing one access point. When a Multi-Region Access Point is used, you can request or write data to Amazon S3 with the service identifying the lowest latency bucket.

Compute resource features

[Elastic Network Interfaces (ENI)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html) used by Amazon EC2 instances, containers, and Lambda functions are limited on a per-flow basis. Review your placement groups to optimize your [EC2 networking throughput](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-network-bandwidth.html). To avoid a bottleneck on a per flow-basis, design your application to use multiple flows. To monitor and get visibility into your compute related networking metrics, use CloudWatch Metrics and [ethtool](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/monitoring-network-performance-ena.html). The `ethtool` command is included in the ENA driver and exposes additional network-related metrics that can be published as a [custom metric](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html) to CloudWatch.

[Amazon Elastic Network Adapters (ENA)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/enhanced-networking-ena.html) provide further optimization by delivering better throughput for your instances within a [cluster placement group](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html#placement-groups-cluster%23placement-groups-limitations-cluster).

[Elastic Fabric Adapter (EFA)](https://aws.amazon.com/hpc/efa/) is a network interface for Amazon EC2 instances that allows you to run workloads requiring high levels of internode communications at scale on AWS.

[Amazon EBS-optimized instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-optimized.html) use an optimized configuration stack and provide additional, dedicated capacity to increase the Amazon EBS I/O.

## Resources

**Related documents:**

- [Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html)
- [EC2 Enhanced Networking on Linux](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/enhanced-networking.html)
- [EC2 Enhanced Networking on Windows](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/enhanced-networking.html)
- [EC2 Placement Groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html)
- [Enabling Enhanced Networking with the Elastic Network Adapter (ENA) on Linux Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/enhanced-networking-ena.html)
- [Network Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html)
- [Networking Products with AWS](https://aws.amazon.com/products/networking/)
- [Transitioning to Latency-Based Routing in Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/TutorialTransitionToLBR.html)
- [VPC Endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/concepts.html)
- [VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html)

**Related videos:**

- [AWS re:Invent 2023 – Ready for what's next? Designing networks for growth and flexibility](https://www.youtube.com/watch?v=FkWOhTZSfdA)
- [AWS re:Invent 2023 – Advanced VPC designs and new capabilities](https://www.youtube.com/watch?v=cRdDCkbE4es)
- [AWS re:Invent 2023 – A developer's guide to cloud networking](https://www.youtube.com/watch?v=i77D556lrgY)
- [AWS re:Invent 2022 – Dive deep on AWS networking infrastructure](https://www.youtube.com/watch?v=HJNR_dX8g8c)
- [AWS re:Invent 2019 – Connectivity to AWS and hybrid AWS network architectures](https://www.youtube.com/watch?v=eqW6CPb58gs)
- [AWS re:Invent 2018 – Optimizing Network Performance for Amazon EC2 Instances](https://www.youtube.com/watch?v=DWiwuYtIgu0)
- [AWS Global Accelerator](https://www.youtube.com/watch?v=Docl4julOQw)

**Related examples:**

- [AWS Transit Gateway and Scalable Security Solutions](https://github.com/aws-samples/aws-transit-gateway-and-scalable-security-solutions)
- [AWS Networking Workshops](https://catalog.workshops.aws/networking/en-US)
- [Observing and diagnosing your network](https://catalog.us-east-1.prod.workshops.aws/workshops/cf2ecaa4-e4be-4f40-b93f-e9fe3b1c1f64/en-US)
- [Finding and addressing network misconfigurations on AWS](https://validating-network-reachability.awssecworkshops.com/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_networking_evaluate_networking_features.html*

---

# PERF04-BP03 Choose appropriate dedicated connectivity or VPN for your workload

When hybrid connectivity is required to connect on-premises and
cloud resources, provision adequate bandwidth to meet your
performance requirements. Estimate the bandwidth and latency
requirements for your hybrid workload. These numbers will drive your
sizing requirements.

**Common anti-patterns:**

- You only evaluate VPN solutions for your network encryption
requirements.
- You do not evaluate backup or redundant connectivity options.
- You do not identify all workload requirements (encryption,
protocol, bandwidth, and traffic needs).

**Benefits of establishing this best
practice:** Selecting and configuring appropriate
connectivity solutions will increase the reliability of your
workload and maximize performance. By identifying workload
requirements, planning ahead, and evaluating hybrid solutions, you
can minimize expensive physical network changes and operational
overhead while increasing your time-to-value.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Develop a hybrid networking architecture based on your bandwidth
requirements. [Direct Connect](https://aws.amazon.com/directconnect/) allows you to connect your
on-premises network privately with AWS. It is suitable when you
need high-bandwidth and low-latency while achieving consistent
performance. A VPN connection establishes secure connection over
the internet. It is used when only a temporary connection is
required, when cost is a factor, or as a contingency while waiting
for resilient physical network connectivity to be established when using Direct Connect.

If your bandwidth requirements are high, you might consider
multiple Direct Connect or VPN services. Traffic can be load
balanced across services, although we don't recommend load
balancing between Direct Connect and VPN because of the latency
and bandwidth differences.

### Implementation steps

- Estimate the bandwidth and latency requirements of your
existing applications.

For existing workloads that are moving to AWS, leverage the
data from your internal network monitoring systems.
- For new or existing workloads for which you don’t have
monitoring data, consult with the product owners to
determine adequate performance metrics and provide a good
user experience.

- Select dedicated connection or VPN as your connectivity
option. Based on all workload requirements (encryption,
bandwidth, and traffic needs), you can either choose AWS Direct Connect or [Site-to-Site VPN](https://aws.amazon.com/vpn/) (or both). The
following diagram can help you choose the appropriate
connection type.

[AWS Direct Connect](https://aws.amazon.com/directconnect/) provides dedicated connectivity to the
AWS environment, from 50 Mbps up to 100 Gbps, using either
dedicated connections or hosted connections. This gives you
managed and controlled latency and provisioned bandwidth so
your workload can connect efficiently to other environments.
Using AWS Direct Connect partners, you can have end-to-end
connectivity from multiple environments, providing an
extended network with consistent performance. AWS offers
scaling direct connect connection bandwidth using either
native 100 Gbps, link aggregation group (LAG), or BGP
equal-cost multipath (ECMP).
- The AWS [Site-to-Site VPN](https://aws.amazon.com/vpn/) provides a managed VPN service supporting internet protocol security (IPsec). When a VPN connection is created, each VPN connection includes two tunnels for high availability.

- Follow AWS documentation to choose an appropriate
connectivity option:

If you decide to use Direct Connect, select the
appropriate bandwidth for your connectivity.
- If you are using an AWS Site-to-Site VPN across multiple
locations to connect to an AWS Region, use
an [accelerated
Site-to-Site VPN connection](https://docs.aws.amazon.com/vpn/latest/s2svpn/accelerated-vpn.html) for the opportunity
to improve network performance.
- If your network design consists of IPSec VPN connection
over [AWS Direct Connect](https://aws.amazon.com/directconnect/), consider using Private IP VPN to
improve security and achieve
segmentation. [AWS Site-to-Site Private IP VPN](https://aws.amazon.com/blogs/networking-and-content-delivery/introducing-aws-site-to-site-vpn-private-ip-vpns/) is deployed on top of
transit virtual interface (VIF).
- [AWS Direct Connect SiteLink](https://aws.amazon.com/blogs/aws/new-site-to-site-connectivity-with-aws-direct-connect-sitelink/) allows creating
low-latency and redundant connections between your data
centers worldwide by sending data over the fastest path
between [AWS Direct Connect locations](https://aws.amazon.com/directconnect/locations/), bypassing AWS Regions.

- Validate your connectivity setup before deploying to
production. Perform security and performance testing to
assure it meets your bandwidth, reliability, latency, and
compliance requirements.
- Regularly monitor your connectivity performance and usage
and optimize if required.

*Deterministic performance flowchart*

## Resources

**Related documents:**

- [Networking Products with AWS](https://aws.amazon.com/products/networking/)
- [AWS Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html)
- [VPC Endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/concepts.html)
- [Building
a Scalable and Secure Multi-VPC AWS Network
Infrastructure](https://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/welcome.html)
- [Client
VPN](https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/what-is.html)

**Related videos:**

- [AWS re:Invent 2023 – Building hybrid network connectivity with AWS](https://www.youtube.com/watch?v=Fi4me2vPwrQ)
- [AWS re:Invent 2023 – Secure remote connectivity to AWS](https://www.youtube.com/watch?v=yHEhrkGdnj0)
- [AWS re:Invent 2022 – Optimizing performance with Amazon CloudFront](https://www.youtube.com/watch?v=LkyifXYEtrg)
- [AWS re:Invent 2019 – Connectivity to AWS and hybrid AWS network architectures](https://www.youtube.com/watch?v=eqW6CPb58gs)
- [AWS re:Invent 2020 – AWS Transit Gateway Connect](https://www.youtube.com/watch?v=_MPY_LHSKtM&t=491s)

**Related examples:**

- [AWS Transit Gateway and Scalable Security Solutions](https://github.com/aws-samples/aws-transit-gateway-and-scalable-security-solutions)
- [AWS Networking Workshops](https://networking.workshop.aws/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_networking_choose_appropriate_dedicated_connectivity_or_vpn.html*

---

# PERF04-BP04 Use load balancing to distribute traffic across multiple resources

Distribute traffic across multiple resources or services to allow your workload to take
advantage of the elasticity that the cloud provides. You can also use load balancing for
offloading encryption termination to improve performance, reliability and manage and route
traffic effectively.

**Common anti-patterns:**

- You don’t consider your workload requirements when choosing the load balancer type.
- You don’t leverage the load balancer features for performance optimization.
- The workload is exposed directly to the internet without a load balancer.
- You route all internet traffic through existing load balancers.
- You use generic TCP load balancing and making each compute node handle SSL encryption.

**Benefits of establishing this best practice:** A load balancer
handles the varying load of your application traffic in a single Availability Zone or across
multiple Availability Zones and enables high availability, automatic scaling, and better
utilization for your workload.

**Level of risk exposed if this best practice is not established:**
High

## Implementation guidance

Load balancers act as the entry point for your workload, from which point they distribute
the traffic to your backend targets, such as compute instances or containers, to improve
utilization.

Choosing the right load balancer type is the first step to optimize your architecture.
Start by listing your workload characteristics, such as protocol (like TCP, HTTP, TLS, or
WebSockets), target type (like instances, containers, or serverless), application requirements
(like long running connections, user authentication, or stickiness), and placement (like
Region, Local Zone, Outpost, or zonal isolation).

AWS provides multiple models for your applications to use load balancing. [Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html) is best suited for load balancing of HTTP and HTTPS traffic and provides
advanced request routing targeted at the delivery of modern application architectures,
including microservices and containers.

[Network Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html) is best suited for load balancing of TCP traffic where extreme performance is
required. It is capable of handling millions of requests per second while maintaining
ultra-low latencies, and it is optimized to handle sudden and volatile traffic patterns.

[Elastic Load Balancing](https://aws.amazon.com/elasticloadbalancing/) provides integrated
certificate management and SSL/TLS decryption, allowing you the flexibility to centrally
manage the SSL settings of the load balancer and offload CPU intensive work from your
workload.

After choosing the right load balancer, you can start leveraging its features to reduce
the amount of effort your backend has to do to serve the traffic.

For example, using both Application Load Balancer (ALB) and Network Load Balancer (NLB), you can perform SSL/TLS encryption
offloading, which is an opportunity to avoid the CPU-intensive TLS handshake from being
completed by your targets and also to improve certificate management.

When you configure SSL/TLS offloading in your load balancer, it becomes responsible for
the encryption of the traffic from and to clients while delivering the traffic unencrypted to
your backends, freeing up your backend resources and improving the response time for the
clients.

Application Load Balancer can also serve HTTP/2 traffic without needing to support it on your targets. This
simple decision can improve your application response time, as HTTP/2 uses TCP connections
more efficiently.

Your workload latency requirements should be considered when defining the architecture.
As an example, if you have a latency-sensitive application, you may decide to use Network Load Balancer, which
offers extremely low latencies. Alternatively, you may decide to bring your workload closer to
your customers by leveraging Application Load Balancer in [AWS Local Zones](https://aws.amazon.com/about-aws/global-infrastructure/localzones/) or even [AWS Outposts](https://aws.amazon.com/outposts/rack/).

Another consideration for latency-sensitive workloads is cross-zone load balancing. With
cross-zone load balancing, each load balancer node distributes traffic across the registered
targets in all allowed Availability Zones.

Use Auto Scaling integrated with your load balancer. One of the key aspects of a performance
efficient system has to do with right-sizing your backend resources. To do this, you can
leverage load balancer integrations for backend target resources. Using the load balancer
integration with Auto Scaling groups, targets will be added or removed from the load balancer as
required in response to incoming traffic. Load balancers can also integrate with [Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-load-balancing.html) and [Amazon EKS](https://docs.aws.amazon.com/eks/latest/userguide/alb-ingress.html) for containerized workloads.

- [Amazon ECS - Service load
balancing](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-load-balancing.html)
- [Application load
balancing on Amazon EKS](https://docs.aws.amazon.com/eks/latest/userguide/alb-ingress.html)
- [Network
load balancing on Amazon EKS](https://docs.aws.amazon.com/eks/latest/userguide/network-load-balancing.html)

### Implementation steps

- Define your load balancing requirements including traffic volume, availability and
application scalability.
- Choose the right load balancer type for your application.

Use Application Load Balancer for HTTP/HTTPS workloads.
- Use Network Load Balancer for non-HTTP workloads that run on TCP or UDP.
- Use a combination of both ([ALB as a target of NLB](https://aws.amazon.com/blogs/networking-and-content-delivery/application-load-balancer-type-target-group-for-network-load-balancer/)) if you want to leverage features of both
products. For example, you can do this if you want to use the static IPs of NLB
together with HTTP header based routing from ALB, or if you want to expose your HTTP
workload to an [AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/privatelink-share-your-services.html).
- For a full comparison of load balancers, see [ELB product comparison](https://aws.amazon.com/elasticloadbalancing/features/).

- Use SSL/TLS offloading if possible.

Configure HTTPS/TLS listeners with both [Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-https-listener.html) and [Network Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/create-tls-listener.html) integrated with [AWS Certificate Manager](https://aws.amazon.com/certificate-manager/).
- Note that some workloads may require end-to-end encryption for compliance
reasons. In this case, it is a requirement to allow encryption at the targets.
- For security best practices, see [SEC09-BP02 Enforce encryption in transit](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_protect_data_transit_encrypt.html).

- Select the right routing algorithm (only ALB).

The routing algorithm can make a difference in how well-used your backend
targets are and therefore how they impact performance. For example, ALB
provides [two options for routing algorithms](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-target-groups.html#modify-routing-algorithm):
- **Least outstanding requests:** Use to achieve a better
load distribution to your backend targets for cases when the requests for your
application vary in complexity or your targets vary in processing capability.
- **Round robin:** Use when the requests and targets are
similar, or if you need to distribute requests equally among targets.

- Consider cross-zone or zonal isolation.

Use cross-zone turned off (zonal isolation) for latency improvements and zonal
failure domains. It is turned off by default in NLB and in [ALB you can
turn it off per target group](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/disable-cross-zone.html).
- Use cross-zone turned on for increased availability and flexibility. By
default, cross-zone is turned on for ALB and in [NLB you can
turn it on per target group](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/target-group-cross-zone.html).

- Turn on HTTP keep-alives for your HTTP workloads (only ALB). With this feature, the
load balancer can reuse backend connections until the keep-alive timeout expires,
improving your HTTP request and response time and also reducing resource utilization on
your backend targets. For detail on how to do this for Apache and Nginx, see [What are
the optimal settings for using Apache or NGINX as a backend server for ELB?](https://aws.amazon.com/premiumsupport/knowledge-center/apache-backend-elb/)
- Turn on monitoring for your load balancer.

Turn on access logs for your [Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/enable-access-logging.html) and [Network Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-access-logs.html).
- The main fields to consider for ALB
are `request_processing_time`, `request_processing_time`,
and `response_processing_time`.
- The main fields to consider for NLB
are `connection_time` and `tls_handshake_time`.
- Be ready to query the logs when you need them. You can use Amazon Athena to query
both [ALB
logs](https://docs.aws.amazon.com/athena/latest/ug/application-load-balancer-logs.html) and [NLB logs](https://docs.aws.amazon.com/athena/latest/ug/networkloadbalancer-classic-logs.html).
- Create alarms for performance related metrics such as [TargetResponseTime for ALB](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-cloudwatch-metrics.html).

## Resources

**Related documents:**

- [ELB product
comparison](https://aws.amazon.com/elasticloadbalancing/features/)
- [AWS Global
Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/)
- [Improving Performance and Reducing Cost Using Availability Zone Affinity](https://aws.amazon.com/blogs/architecture/improving-performance-and-reducing-cost-using-availability-zone-affinity/)
- [Step by step for Log Analysis with Amazon Athena](https://github.com/aws/elastic-load-balancing-tools/tree/master/amazon-athena-for-elb)
- [Querying Application Load Balancer logs](https://docs.aws.amazon.com/athena/latest/ug/application-load-balancer-logs.html)
- [Monitor your
Application Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-monitoring.html)
- [Monitor your
Network Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-monitoring.html)
- [Use Elastic Load Balancing to distribute traffic across the instances in your Auto Scaling group](https://docs.aws.amazon.com/autoscaling/ec2/userguide/autoscaling-load-balancer.html)

**Related videos:**

- [AWS re:Invent 2023: What can
networking do for your application?](https://www.youtube.com/watch?v=tUh26i8uY9Q)
- [AWS re:Inforce 20: How to use
Elastic Load Balancing to enhance your security posture at scale](https://www.youtube.com/watch?v=YhNc5VSzOGQ)
- [AWS re:Invent 2018: Elastic Load Balancing: Deep
Dive and Best Practices](https://www.youtube.com/watch?v=VIgAT7vjol8)
- [AWS re:Invent 2021 - How to
choose the right load balancer for your AWS workloads](https://www.youtube.com/watch?v=p0YZBF03r5A)
- [AWS re:Invent 2019: Get the
most from Elastic Load Balancing for different workloads](https://www.youtube.com/watch?v=HKh54BkaOK0)

**Related examples:**

- [Gateway Load Balancer](https://catalog.workshops.aws/gwlb-networking/en-US)
- [CDK and CloudFormation samples for Log Analysis with Amazon Athena](https://github.com/aws/elastic-load-balancing-tools/tree/master/log-analysis-elb-cdk-cf-template)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_networking_load_balancing_distribute_traffic.html*

---

# PERF04-BP05 Choose network protocols to improve performance

Make decisions about protocols for communication between systems and
networks based on the impact to the workload’s performance.

There is a relationship between latency and bandwidth to achieve
throughput. If your file transfer is using Transmission Control
Protocol (TCP), higher latencies will most likely reduce overall
throughput. There are approaches to fix this with TCP tuning and
optimized transfer protocols, but one solution is to use User
Datagram Protocol (UDP).

**Common anti-patterns:**

- You use TCP for all workloads regardless of performance
requirements.

**Benefits of establishing this best
practice:** Verifying that an appropriate protocol is used for communication
between users and workload components helps improve overall user
experience for your applications. For instance, connection-less UDP
allows for high speed, but it doesn't offer retransmission or high
reliability. TCP is a full featured protocol, but it requires
greater overhead for processing the packets.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

If you have the ability to choose different protocols for your
application and you have expertise in this area, optimize your
application and end-user experience by using a different protocol.
Note that this approach comes with significant difficulty and
should only be attempted if you have optimized your application in
other ways first.

A primary consideration for improving your workload’s performance
is to understand the latency and throughput requirements, and then
choose network protocols that optimize performance.

**When to consider using TCP**

TCP provides reliable data delivery, and can be used for
communication between workload components where reliability and
guaranteed delivery of data is important. Many web-based
applications rely on TCP-based protocols, such as HTTP and HTTPS,
to open TCP sockets for communication between application
components. Email and file data transfer are common applications
that also make use of TCP, as it is a simple and reliable transfer
mechanism between application components. Using TLS with TCP can
add some overhead to the communication, which can result in
increased latency and reduced throughput, but it comes with the
advantage of security. The overhead comes mainly from the added
overhead of the handshake process, which can take several
round-trips to complete. Once the handshake is complete, the
overhead of encrypting and decrypting data is relatively small.

**When to consider using UDP**

UDP is a connection-less-oriented protocol and is therefore
suitable for applications that need fast, efficient transmission,
such as log, monitoring, and VoIP data. Also, consider using UDP
if you have workload components that respond to small queries from
large numbers of clients to ensure optimal performance of the
workload. Datagram Transport Layer Security (DTLS) is the UDP
equivalent of Transport Layer Security (TLS). When using DTLS with
UDP, the overhead comes from encrypting and decrypting the data,
as the handshake process is simplified. DTLS also adds a small
amount of overhead to the UDP packets, as it includes additional
fields to indicate the security parameters and to detect
tampering.

**When to consider using SRD**

Scalable reliable datagram (SRD) is a network transport protocol
optimized for high-throughput workloads due to its ability to
load-balancer traffic across multiple paths and quickly recover
from packet drops or link failures. SRD is therefore best used for
high performance computing (HPC) workloads that require high
throughput and low latency communication between compute nodes.
This might include parallel processing tasks such as simulation,
modeling, and data analysis that involve a large amount of data
transfer between nodes.

### Implementation steps

- Use
the [AWS Global Accelerator](https://aws.amazon.com/global-accelerator/) and [AWS Transfer Family](https://aws.amazon.com/aws-transfer-family/) services to improve the throughput of
your online file transfer applications. The AWS Global Accelerator service helps you achieve lower latency between
your client devices and your workload on AWS. With AWS Transfer Family, you can use TCP-based protocols such as
Secure Shell File Transfer Protocol (SFTP) and File Transfer
Protocol over SSL (FTPS) to securely scale and manage your
file transfers to AWS storage services.
- Use network latency to determine if TCP is appropriate for
communication between workload components. If the network
latency between your client application and server is high,
then the TCP three-way handshake can take some time, thereby
impacting on the responsiveness of your application. Metrics
such as time to first byte (TTFB) and round-trip time (RTT)
can be used to measure network latency. If your workload
serves dynamic content to users, consider
using [Amazon CloudFront](https://aws.amazon.com/cloudfront/), which establishes a persistent connection
to each origin for dynamic content to remove the connection
setup time that would otherwise slow down each client
request.
- Using TLS with TCP or UDP can result in increased latency
and reduced throughput for your workload due to the impact
of encryption and decryption. For such workloads, consider
SSL/TLS offloading
on [Elastic Load Balancing](https://aws.amazon.com/elasticloadbalancing/) to improve workload performance by
allowing the load balancer to handle SSL/TLS encryption and
decryption process instead of having backend instances do
it. This can help reduce the CPU utilization on the backend
instances, which can improve performance and increase
capacity.
- Use
the [Network Load Balancer (NLB)](https://aws.amazon.com/elasticloadbalancing/network-load-balancer/) to deploy services that rely on
the UDP protocol, such as authentication and authorization,
logging, DNS, IoT, and streaming media, to improve the
performance and reliability of your workload. The NLB
distributes incoming UDP traffic across multiple targets,
allowing you to scale your workload horizontally, increase
capacity, and reduce the overhead of a single target.
- For your High Performance Computing (HPC) workloads,
consider using
the [Elastic
Network Adapter (ENA) Express](https://aws.amazon.com/about-aws/whats-new/2022/11/elastic-network-adapter-ena-express-amazon-ec2-instances/) functionality that uses
the SRD protocol to improve network performance by providing
a higher single flow bandwidth (25 Gbps) and lower tail
latency (99.9 percentile) for network traffic between EC2
instances.
- Use
the [Application Load Balancer (ALB)](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html) to route and load balance your
gRPC (Remote Procedure Calls) traffic between workload
components or between gRPC clients and services. gRPC uses
the TCP-based HTTP/2 protocol for transport and it provides
performance benefits such as lighter network footprint,
compression, efficient binary serialization, support for
numerous languages, and bi-directional streaming.

## Resources

**Related documents:**

- [How to route UDP traffic into Kubernetes](https://aws.amazon.com/blogs/containers/how-to-route-udp-traffic-into-kubernetes/)
- [Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html)
- [EC2
Enhanced Networking on Linux](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/enhanced-networking.html)
- [EC2
Enhanced Networking on Windows](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/enhanced-networking.html)
- [EC2
Placement Groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html)
- [Enabling
Enhanced Networking with the Elastic Network Adapter (ENA) on
Linux Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/enhanced-networking-ena.html)
- [Network Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html)
- [Networking
Products with AWS](https://aws.amazon.com/products/networking/)
- [Transitioning
to Latency-Based Routing in Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/TutorialTransitionToLBR.html)
- [VPC
Endpoints](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints.html)

**Related videos:**

- [AWS re:Invent 2022 – Scaling network performance on next-gen Amazon Elastic Compute Cloud instances](https://www.youtube.com/watch?v=jNYpWa7gf1A)
- [AWS re:Invent 2022 – Application networking foundations](https://www.youtube.com/watch?v=WcZwWuq6FTk)

**Related examples:**

- [AWS Transit Gateway and Scalable Security Solutions](https://github.com/aws-samples/aws-transit-gateway-and-scalable-security-solutions)
- [AWS Networking Workshops](https://networking.workshop.aws/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_networking_choose_network_protocols_improve_performance.html*

---

# PERF04-BP06 Choose your workload's location based on network requirements

Evaluate options for resource placement to reduce network latency and improve throughput, providing an optimal user experience by reducing page load and data transfer times.

**Common anti-patterns:**

- You consolidate all workload resources into one geographic location.
- You chose the closest Region to your location but not to the workload end user.

**Benefits of establishing this best
practice:** User experience is greatly affected by the latency between the user and your application. By using appropriate AWS Regions and the AWS private global network, you can reduce latency and deliver a better experience to remote users.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Resources, such as Amazon EC2 instances, are placed into Availability Zones within [AWS Regions](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/), [AWS Local Zones](https://aws.amazon.com/about-aws/global-infrastructure/localzones/), [AWS Outposts](https://aws.amazon.com/outposts/), or [AWS Wavelength](https://aws.amazon.com/wavelength/) zones. Selection of this location influences network latency and throughput from a given user location. Edge services like [Amazon CloudFront](https://aws.amazon.com/cloudfront/) and [AWS Global Accelerator](https://aws.amazon.com/global-accelerator/) can also be used to improve network performance by either caching content at edge locations or providing users with an optimal path to the workload through the AWS global network.

Amazon EC2 provides placement groups for networking. A placement group is a logical grouping of instances to decrease latency. Using placement groups with supported instance types and an Elastic Network Adapter (ENA) enables workloads to participate in a low-latency, reduced jitter 25 Gbps network. Placement groups are recommended for workloads that benefit from low network latency, high network throughput, or both.

Latency-sensitive services are delivered at edge locations using AWS global network, such as [Amazon CloudFront](https://aws.amazon.com/cloudfront/). These edge locations commonly provide services like content delivery network (CDN) and domain name system (DNS). By having these services at the edge, workloads can respond with low latency to requests for content or DNS resolution. These services also provide geographic services, such as geotargeting of content (providing different content based on the end users’ location) or latency-based routing to direct end users to the nearest Region (minimum latency).

Use edge services to reduce latency and to enable content caching. Configure cache control correctly for both DNS and HTTP/HTTPS to gain the most benefit from these approaches.

### Implementation steps

- Capture information about the IP traffic going to and from network interfaces.

[Logging IP traffic using VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html)
- [How the client IP address is preserved in AWS Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/preserve-client-ip-address.headers.html)

- Analyze network access patterns in your workload to identify how users use your application.

Use monitoring tools, such as [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) and [AWS CloudTrail](https://aws.amazon.com/cloudtrail/), to gather data on network activities.
- Analyze the data to identify the network access pattern.

- Select Regions for your workload deployment based on the following key elements:

**Where your data is located:** For data-heavy
applications (such as big data and machine learning), application code should run as
close to the data as possible.
- **Where your users are located**: For user-facing
applications, choose a Region (or Regions) close to your workload’s users.
- **Other constraints**: Consider constraints such as
cost and compliance as explained in [What to Consider when Selecting a Region for
your Workloads.](https://aws.amazon.com/blogs/architecture/what-to-consider-when-selecting-a-region-for-your-workloads/)

- Use [AWS Local Zones](https://aws.amazon.com/about-aws/global-infrastructure/localzones/) to run workloads like video rendering. Local Zones allow you to benefit from having compute and storage resources closer to end users.
- Use [AWS Outposts](https://aws.amazon.com/outposts/) for workloads that need to remain on-premises and where you want that workload to run seamlessly with the rest of your other workloads in AWS.
- Applications like high-resolution live video streaming, high-fidelity audio, and augmented reality or virtual reality (AR/VR) require ultra-low-latency for 5G devices. For such applications, consider [AWS Wavelength](https://aws.amazon.com/wavelength/). AWS Wavelength embeds AWS compute and storage services within 5G networks, providing mobile edge computing infrastructure for developing, deploying, and scaling ultra-low-latency applications.
- Use local caching or [AWS Caching Solutions](https://aws.amazon.com/caching/aws-caching/) for frequently used assets to improve performance, reduce data movement, and lower environmental impact.

Service
When to use

[Amazon CloudFront](https://aws.amazon.com/cloudfront/)

Use to cache static content such as images, scripts, and videos, as well as dynamic content such as API responses or web applications.

[Amazon ElastiCache](https://aws.amazon.com/elasticache/)

Use to cache content for web applications.

[DynamoDB Accelerator](https://aws.amazon.com/dynamodb/dax/)

Use to add in-memory acceleration to your DynamoDB tables.
- Use services that can help you run code closer to users of your workload like the following:

Service
When to use

[Lambda@edge](https://aws.amazon.com/lambda/edge/)

Use for compute-heavy operations that are initiated when objects are not in the cache.

[Amazon CloudFront Functions](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-functions.html)

Use for simple use cases like HTTP(s) requests or response manipulations that can be initiated by short-lived functions.

[AWS IoT Greengrass](https://aws.amazon.com/greengrass/)

Use to run local compute, messaging, and data caching for connected devices.
- Some applications require fixed entry points or higher performance by reducing first byte latency and jitter, and increasing throughput. These applications can benefit from networking services that provide static anycast IP addresses and TCP termination at edge locations. [AWS Global Accelerator](https://aws.amazon.com/global-accelerator/) can improve performance for your applications by up to 60% and provide quick failover for multi-region architectures. AWS Global Accelerator provides you with static anycast IP addresses that serve as a fixed entry point for your applications hosted in one or more AWS Regions. These IP addresses permit traffic to ingress onto the AWS global network as close to your users as possible. AWS Global Accelerator reduces the initial connection setup time by establishing a TCP connection between the client and the AWS edge location closest to the client. Review the use of AWS Global Accelerator to improve the performance of your TCP/UDP workloads and provide quick failover for multi-Region architectures.

## Resources

**Related best practices:**

- [COST07-BP02 Implement Regions based on cost](https://docs.aws.amazon.com/wellarchitected/latest/framework/cost_pricing_model_region_cost.html)
- [COST08-BP03 Implement services to reduce data transfer costs](https://docs.aws.amazon.com/wellarchitected/latest/framework/cost_data_transfer_implement_services.html)
- [REL10-BP01 Deploy the workload to multiple locations](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel_fault_isolation_multiaz_region_system.html)
- [REL10-BP02 Select the appropriate locations for your multi-location deployment](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel_fault_isolation_select_location.html)
- [SUS01-BP01 Choose Region based on both business requirements and sustainability goals](https://docs.aws.amazon.com/wellarchitected/latest/framework/sus_sus_region_a2.html)
- [SUS02-BP04 Optimize geographic placement of workloads based on their networking requirements](https://docs.aws.amazon.com/wellarchitected/latest/framework/sus_sus_user_a5.html)
- [SUS04-BP07 Minimize data movement across networks](https://docs.aws.amazon.com/wellarchitected/latest/framework/sus_sus_data_a8.html)

**Related documents:**

- [AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/)
- [AWS Local Zones and AWS Outposts, choosing the right technology for your edge workload](https://aws.amazon.com/blogs/compute/aws-local-zones-and-aws-outposts-choosing-the-right-technology-for-your-edge-workload/)
- [Placement groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html)
- [AWS Local Zones](https://aws.amazon.com/about-aws/global-infrastructure/localzones/)
- [AWS Outposts](https://aws.amazon.com/outposts/)
- [AWS Wavelength](https://aws.amazon.com/wavelength/)
- [Amazon CloudFront](https://aws.amazon.com/cloudfront/)
- [AWS Global Accelerator](https://aws.amazon.com/global-accelerator/)
- [AWS Direct Connect](https://aws.amazon.com/directconnect/)
- [AWS Site-to-Site VPN](https://aws.amazon.com/vpn/site-to-site-vpn/)
- [Amazon Route 53](https://aws.amazon.com/route53/)

**Related videos:**

- [AWS Local Zones Explainer Video](https://www.youtube.com/watch?v=JHt-D4_zh7w)
- [AWS Outposts: Overview and How it Works](https://www.youtube.com/watch?v=ppG2FFB0mMQ)
- [AWS re:Invent 2023 - A migration strategy for edge and on-premises workloads](https://www.youtube.com/watch?v=4wUXzYNLvTw)
- [AWS re:Invent 2021 - AWS Outposts: Bringing the AWS experience on premises](https://www.youtube.com/watch?v=FxVF6A22498)
- [AWS re:Invent 2020: AWS Wavelength: Run apps with ultra-low latency at 5G edge](https://www.youtube.com/watch?v=AQ-GbAFDvpM)
- [AWS re:Invent 2022 - AWS Local Zones: Building applications for a distributed edge](https://www.youtube.com/watch?v=bDnh_d-slhw)
- [AWS re:Invent 2021 - Building low-latency websites with Amazon CloudFront](https://www.youtube.com/watch?v=9npcOZ1PP_c)
- [AWS re:Invent 2022 - Improve performance and availability with AWS Global Accelerator](https://www.youtube.com/watch?v=s5sjsdDC0Lg)
- [AWS re:Invent 2022 - Build your global wide area network using AWS](https://www.youtube.com/watch?v=flBieylTwvI)
- [AWS re:Invent 2020: Global traffic management with Amazon Route 53](https://www.youtube.com/watch?v=E33dA6n9O7I)

**Related examples:**

- [AWS Global Accelerator Custom Routing Workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/ac213084-3f4a-4b01-9835-5052d6096b5b/en-US)
- [Handling Rewrites and Redirects using Edge Functions](https://catalog.us-east-1.prod.workshops.aws/workshops/814dcdac-c2ad-4386-98d5-27d37bb77766/en-US)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_networking_choose_workload_location_network_requirements.html*

---

# PERF04-BP07 Optimize network configuration based on metrics

Use collected and analyzed data to make informed decisions about
optimizing your network configuration.

**Common anti-patterns:**

- You assume that all performance-related issues are
application-related.
- You only test your network performance from a location close to
where you have deployed the workload.
- You use default configurations for all network services.
- You overprovision the network resource to provide sufficient
capacity.

**Benefits of establishing this best
practice:** Collecting necessary metrics of your AWS
network and implementing network monitoring tools allows you to
understand network performance and optimize network configurations.

**Level of risk exposed if this best practice
is not established:** Low

## Implementation guidance

Monitoring traffic to and from VPCs, subnets, or network
interfaces is crucial to understand how to utilize AWS network
resources and optimize network configurations. By using the
following AWS networking tools, you can further inspect
information about the traffic usage, network access and logs.

### Implementation steps

- Identify the key performance metrics such as latency or packet
loss to collect. AWS provides several tools that can
help you to collect these metrics. By using the following
tools, you can further inspect information about the traffic
usage, network access, and logs:

AWS tool

Where to use

[Amazon VPC IP Address Manager](https://docs.aws.amazon.com/vpc/latest/ipam/what-it-is-ipam.html).

Use IPAM to plan, track, and monitor IP addresses for
your AWS and on-premises workloads. This is a best
practice to optimize IP address usage and allocation.

[VPC
Flow logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html)

Use VPC Flow Logs to capture detailed information about
traffic to and from network interfaces in your VPCs.
With VPC Flow Logs, you can diagnose overly restrictive
or permissive security group rules and determine the
direction of the traffic to and from the network
interfaces.

[AWS Transit Gateway Flow Logs](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-flow-logs.html)

Use AWS Transit Gateway Flow Logs to capture information
about the IP traffic going to and from your transit
gateways.

[DNS
query logging](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/query-logs.html)

Log information about public or private DNS queries
Route 53 receives. With DNS logs, you can optimize DNS
configurations by understanding the domain or subdomain
that was requested or Route 53 EDGE locations that
responded to DNS queries.

[Reachability Analyzer](https://docs.aws.amazon.com/vpc/latest/reachability/what-is-reachability-analyzer.html)

Reachability Analyzer helps you analyze and debug
network reachability. Reachability Analyzer is a
configuration analysis tool that allows you to perform
connectivity testing between a source resource and a
destination resource in your VPCs. This tool helps you
verify that your network configuration matches your
intended connectivity.

[Network Access Analyzer](https://docs.aws.amazon.com/vpc/latest/network-access-analyzer/what-is-network-access-analyzer.html)

Network Access Analyzer helps you understand network
access to your resources. You can use Network Access Analyzer to specify your network access requirements and
identify potential network paths that do not meet your
specified requirements. By optimizing your corresponding
network configuration, you can understand and verify the
state of your network and demonstrate if your network on
AWS meets your compliance requirements.

[Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html)

Use [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) and turn on the appropriate metrics
for network options. Make sure to choose the right
network metric for your workload. For example, you can
turn on metrics for VPC Network Address Usage, VPC NAT
Gateway, AWS Transit Gateway, VPN tunnel, AWS Network Firewall, Elastic Load Balancing, and AWS Direct Connect. Continually monitoring metrics is a good
practice to observe and understand your network status
and usage, which helps you optimize network
configuration based on your observations.

[AWS Network Manager](https://aws.amazon.com/about-aws/whats-new/2022/11/network-manager-real-time-performance-monitoring-aws-global-network/)

Using AWS Network Manager, you can monitor the real-time
and historical performance of
the [AWS Global Network](https://aws.amazon.com/about-aws/global-infrastructure/global_network/) for operational and planning
purposes. Network Manager provides aggregate network
latency between AWS Regions and Availability Zones and
within each Availability Zone, allowing you to better
understand how your application performance relates to
the performance of the underlying AWS network.

[Amazon CloudWatch RUM](https://aws.amazon.com/blogs/aws/cloudwatch-rum/)

Use Amazon CloudWatch RUM to collect the metrics that
give you the insights that help you identify,
understand, and improve user experience.
- Identify top talkers and application traffic patterns using
VPC and AWS Transit Gateway Flow Logs.
- Assess and optimize your current network architecture
including VPCs, subnets, and routing. As an example, you can
evaluate how different VPC peering or AWS Transit Gateway
can help you improve the networking in your architecture.
- Assess the routing paths in your network to verify that the
shortest path between destinations is always used. Network Access Analyzer can help you do this.

## Resources

**Related documents:**

- [Public
DNS query logging](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/query-logs.html)
- [What
is IPAM?](https://docs.aws.amazon.com/vpc/latest/ipam/what-it-is-ipam.html)
- [What
is Reachability Analyzer?](https://docs.aws.amazon.com/vpc/latest/reachability/what-is-reachability-analyzer.html)
- [What
is Network Access Analyzer?](https://docs.aws.amazon.com/vpc/latest/network-access-analyzer/what-is-network-access-analyzer.html)
- [CloudWatch
metrics for your VPCs](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-cloudwatch.html)
- [Optimize
performance and reduce costs for network analytics with VPC
Flow Logs in Apache Parquet format](https://aws.amazon.com/blogs/big-data/optimize-performance-and-reduce-costs-for-network-analytics-with-vpc-flow-logs-in-apache-parquet-format/)
- [Monitoring
your global and core networks with Amazon CloudWatch
metrics](https://docs.aws.amazon.com/vpc/latest/tgwnm/monitoring-cloudwatch-metrics.html)
- [Continuously
monitor network traffic and resources](https://docs.aws.amazon.com/whitepapers/latest/security-best-practices-for-manufacturing-ot/continuously-monitor-network-traffic-and-resources.html)

**Related videos:**

- [AWS re:Invent 2023 – A developer's guide to cloud networking](https://www.youtube.com/watch?v=i77D556lrgY)
- [AWS re:Invent 2023 – Ready for what’s next? Designing networks for growth and flexibility](https://www.youtube.com/watch?v=FkWOhTZSfdA)
- [AWS re:Invent 2023 – Advanced VPC designs and new capabilities](https://www.youtube.com/watch?v=cRdDCkbE4es)
- [AWS re:Invent 2022 – Dive deep on AWS networking infrastructure](https://www.youtube.com/watch?v=HJNR_dX8g8c)
- [AWS re:Invent 2020 – Networking
best practices and tips with the AWS Well-Architected
Framework](https://www.youtube.com/watch?v=wOMNpG49BeM)
- [AWS re:Invent 2020 – Monitoring
and troubleshooting network traffic](https://www.youtube.com/watch?v=Ed09ReWRQXc)

**Related examples:**

- [AWS Networking Workshops](https://networking.workshop.aws/)
- [AWS Network Monitoring](https://github.com/aws-samples/monitor-vpc-network-patterns)
- [Observing and diagnosing your network on AWS](https://catalog.us-east-1.prod.workshops.aws/workshops/cf2ecaa4-e4be-4f40-b93f-e9fe3b1c1f64/en-US)
- [Finding and addressing network misconfigurations on AWS](https://validating-network-reachability.awssecworkshops.com/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_networking_optimize_network_configuration_based_on_metrics.html*

---

---

## Question PERF05

# PERF 5 — What process do you use to support more performance efficiency?

**Pillar**: Performance Efficiency  
**Best Practices**: 7

---

# PERF05-BP01 Establish key performance indicators (KPIs) to measure workload health and performance

Identify the KPIs that quantitatively and qualitatively measure
workload performance. KPIs help you measure the health and
performance of a workload related to a business goal.

**Common anti-patterns:**

- You only monitor system-level metrics to gain insight into your
workload and don’t understand business impacts to those metrics.
- You assume that your KPIs are already being published and shared
as standard metric data.
- You do not define a quantitative, measurable KPI.
- You do not align KPIs with business goals or strategies.

**Benefits of establishing this best
practice:** Identifying specific KPIs that represent
workload health and performance helps align teams on their
priorities and define successful business outcomes. Sharing those
metrics with all departments provides visibility and alignment on
thresholds, expectations, and business impact.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

KPIs allow business and engineering teams to align on the
measurement of goals and strategies and how these factors combine
to produce business outcomes. For example, a website workload
might use page load time as an indication of overall performance.
This metric would be one of multiple data points that measures user experience. In addition to identifying the page load time
thresholds, you should document the expected outcome or business
risk if ideal performance is not met. A long page load time
affects your end users directly, decreases their user experience
rating, and can lead to a loss of customers. When you define your
KPI thresholds, combine both industry benchmarks and your end user
expectations. For example, if the current industry benchmark is a
webpage loading within a two-second time period, but your end
users expect a webpage to load within a one-second time period,
then you should take both of these data points into consideration
when establishing the KPI.

Your team must evaluate your workload KPIs using real-time
granular data and historical data for reference and create
dashboards that perform metric math on your KPI data to derive
operational and utilization insights. KPIs should be documented
and include thresholds that support business goals and strategies,
and should be mapped to metrics being monitored. KPIs should be
revisited when business goals, strategies, or end user
requirements change.

## Implementation steps

- **Identify stakeholders:** Identify and document key business stakeholders, including development and operation teams.
- **Define objectives:**
Work with these stakeholders to define and document objectives
of your workload. Consider the critical performance aspects of your workloads, such as throughput, response time, and cost, as well as business goals, such as user satisfaction.
- **Review industry best practices:**
Review industry best practices to identify relevant KPIs
aligned with your workload objectives.
- **Identify metrics:** Identify metrics that are aligned with your workload objectives and can help you measure performance and business goals. Establish KPIs based on these metrics. Example metrics are measurements like average response time or number of concurrent users.
- **Define and document KPIs:**
Use industry best practices and your workload objectives to
set targets for your workload KPI. Use this information to set
KPI thresholds for severity or alarm level. Identify and document the risk and impact of a KPI is not met.
- **Implement monitoring:**
Use monitoring tools such as
[Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) or
[AWS Config](https://aws.amazon.com/config/) to collect metrics and measure KPIs.
- **Visually communicate KPIs:**
Use dashboard tools like [Amazon Quick](https://aws.amazon.com/pm/quicksight/) to visualize and communicate KPIs with
stakeholders.
- **Analyze and optimize:**
Regularly review and analyze KPIs to identify areas of your
workload that need to be improved. Work with stakeholders to implement these improvements.
- **Revisit and refine:**
Regularly review metrics and KPIs to assess their effectiveness, especially when business goals or workload performance change.

## Resources

**Related documents:**

- [CloudWatch
documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html)
- [Monitoring,
Logging, and Performance AWS Partners](https://aws.amazon.com/devops/partner-solutions/#_Monitoring.2C_Logging.2C_and_Performance)
- [AWS observability tools](https://docs.aws.amazon.com/wellarchitected/latest/management-and-governance-guide/aws-observability-tools.html)
- [The Importance of Key Performance Indicators (KPIs) for Large-Scale Cloud Migrations](https://aws.amazon.com/blogs/mt/the-importance-of-key-performance-indicators-kpis-for-large-scale-cloud-migrations/)
- [How to track your cost optimization KPIs with the KPI Dashboard](https://aws.amazon.com/blogs/aws-cloud-financial-management/how-to-track-your-cost-optimization-kpis-with-the-kpi-dashboard/)
- [X-Ray
Documentation](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html)
- [Using
Amazon CloudWatch dashboards](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html?ref=wellarchitected)
- [Quick KPIs](https://docs.aws.amazon.com/quicksight/latest/user/kpi.html)

**Related videos:**

- [AWS re:Invent 2023 - Optimize cost and performance and track progress toward mitigation](https://www.youtube.com/watch?v=keAfy8f84E0)
- [AWS re:Invent 2023 - Manage resource lifecycle events at scale with AWS Health](https://www.youtube.com/watch?v=VoLLNL5j9NA)
- [AWS re:Invent 2023 - Performance & efficiency at Pinterest: Optimizing the latest instances](https://www.youtube.com/watch?v=QSudpowE_Hs)
- [AWS re:Invent 2022 - AWS optimization: Actionable steps for immediate results](https://www.youtube.com/watch?v=0ifvNf2Tx3w)
- [AWS re:Invent 2023 - Building an effective observability strategy](https://www.youtube.com/watch?v=7PQv9eYCJW8)
- [AWS Summit SF 2022 - Full-stack observability and application monitoring with AWS](https://www.youtube.com/watch?v=or7uFFyHIX0)
- [AWS re:Invent 2023 - Scaling on AWS for the first 10 million users](https://www.youtube.com/watch?v=JzuNJ8OUht0)
- [AWS re:Invent 2022 - How Amazon uses better metrics for improved website performance](https://www.youtube.com/watch?v=_uaaCiyJCFA)
- [Creating an Effective Metrics Strategy for Your Business | AWS Events](https://www.youtube.com/watch?v=zBO-K4RvbtM)

**Related examples:**

- [Creating
a dashboard with Quick](https://github.com/aws-samples/amazon-quicksight-sdk-proserve)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_process_culture_establish_key_performance_indicators.html*

---

# PERF05-BP02 Use monitoring solutions to understand the areas where performance is most critical

Understand and identify areas where increasing the performance of
your workload will have a positive impact on efficiency or customer
experience. For example, a website that has a large amount of
customer interaction can benefit from using edge services to move
content delivery closer to customers.

**Common anti-patterns:**

- You assume that standard compute metrics such as CPU utilization
or memory pressure are enough to catch performance issues.
- You only use the default metrics recorded by your selected
monitoring software.
- You only review metrics when there is an issue.

**Benefits of establishing this best
practice:** Understanding critical areas of performance
helps workload owners monitor KPIs and prioritize high-impact
improvements.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Set up end-to-end tracing to identify traffic patterns, latency,
and critical performance areas. Monitor your data access patterns
for slow queries or poorly fragmented and partitioned data.
Identify the constrained areas of the workload using load testing
or monitoring.

Increase performance efficiency by understanding your
architecture, traffic patterns, and data access patterns, and
identify your latency and processing times. Identify the potential
bottlenecks that might affect the customer experience as the
workload grows. After investigating these areas, look at which
solution you could deploy to remove those performance concerns.

### Implementation steps

- Set up end-to-end monitoring to capture all workload
components and metrics. Here are examples of monitoring
solutions on AWS.

Service

Where to use

[Amazon CloudWatch Real-User Monitoring (RUM)](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM.html)

To capture application performance metrics from real
user client-side and frontend sessions.

[AWS X-Ray](https://aws.amazon.com/xray/)

To trace traffic through the application layers and
identify latency between components and dependencies.
Use X-Ray service maps to see relationships and latency
between workload components.

[Amazon Relational Database Service Performance Insights](https://aws.amazon.com/rds/performance-insights/)

To view database performance metrics and identify
performance improvements.

[Amazon RDS Enhanced Monitoring](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring.OS.html)

To view database OS performance metrics.

[Amazon
DevOps Guru](https://aws.amazon.com/devops-guru/)

To detect abnormal operating patterns so you can
identify operational issues before they impact your
customers.
- Perform tests to generate metrics, identify traffic
patterns, bottlenecks, and critical performance areas. Here
are some examples of how to perform testing:

Set
up [CloudWatch
Synthetic Canaries](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.html) to mimic browser-based user
activities programmatically using Linux cron jobs or
rate expressions to generate consistent metrics over
time.
- Use the [AWS Distributed Load Testing](https://aws.amazon.com/solutions/implementations/distributed-load-testing-on-aws/) solution to generate
peak traffic or test the workload at the expected growth
rate.

- Evaluate the metrics and telemetry to identify your critical
performance areas. Review these areas with your team to
discuss monitoring and solutions to avoid bottlenecks.
- Experiment with performance improvements and measure those
changes with data. As an example, you can
use [CloudWatch
Evidently](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Evidently.html) to test new improvements and performance
impacts to your workload.

## Resources

**Related documents:**

- [What's new in AWS Observability at re:Invent 2023](https://aws.amazon.com/blogs/mt/whats-new-in-aws-observability-at-reinvent-2023/)
- [Amazon
Builders’ Library](https://aws.amazon.com/builders-library)
- [X-Ray
Documentation](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html)
- [Amazon CloudWatch RUM](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM.html)
- [Amazon DevOps Guru](https://aws.amazon.com/devops-guru/)

**Related videos:**

- [AWS re:Invent 2023 - [LAUNCH] Application monitoring for modern workloads](https://www.youtube.com/watch?v=T2TovTLje8w)
- [AWS re:Invent 2023 - Implementing application observability](https://www.youtube.com/watch?v=IcTcwUSwIs4)
- [AWS re:Invent 2023 - Building an effective observability strategy](https://www.youtube.com/watch?v=7PQv9eYCJW8)
- [AWS Summit SF 2022 - Full-stack observability and application monitoring with AWS](https://www.youtube.com/watch?v=or7uFFyHIX0)
- [AWS re:Invent 2022 - AWS optimization: Actionable steps for immediate results](https://www.youtube.com/watch?v=0ifvNf2Tx3w)
- [AWS re:Invent 2022 - The
Amazon Builders’ Library: 25 years of Amazon operational
excellence](https://www.youtube.com/watch?v=DSRhgBd_gtw)
- [AWS re:Invent 2022 - How Amazon uses better metrics for improved website performance](https://www.youtube.com/watch?v=_uaaCiyJCFA)
- [Visual
Monitoring of Applications with Amazon CloudWatch
Synthetics](https://www.youtube.com/watch?v=_PCs-ucZz7E)

**Related examples:**

- [Measure
page load time with Amazon CloudWatch Synthetics](https://github.com/aws-samples/amazon-cloudwatch-synthetics-page-performance)
- [Amazon CloudWatch RUM Web Client](https://github.com/aws-observability/aws-rum-web)
- [X-Ray
SDK for Python](https://github.com/aws/aws-xray-sdk-python)
- [Distributed
Load Testing on AWS](https://aws.amazon.com/solutions/implementations/distributed-load-testing-on-aws/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_process_culture_use_monitoring_solutions.html*

---

# PERF05-BP03 Define a process to improve workload performance

Define a process to evaluate new services, design patterns, resource
types, and configurations as they become available. For example, run
existing performance tests on new instance offerings to determine
their potential to improve your workload.

**Common anti-patterns:**

- You assume your current architecture is static and won’t be
updated over time.
- You introduce architecture changes over time with no metric
justification.

**Benefits of establishing this best
practice:** By defining your process for making
architectural changes, you can use gathered data to influence your
workload design over time.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Your workload's performance has a few key constraints. Document
these so that you know what kinds of innovation might improve the
performance of your workload. Use this information when learning
about new services or technology as it becomes available to
identify ways to alleviate constraints or bottlenecks.

Identify the key performance constraints for your workload.
Document your workload’s performance constraints so that you know
what kinds of innovation might improve the performance of your
workload.

### Implementation steps

- **Identify KPIs:**
Identify your workload performance KPIs as outlined in [PERF05-BP01 Establish key performance indicators (KPIs) to measure workload health and performance](./perf_process_culture_establish_key_performance_indicators.html) to
baseline your workload.
- **Implement monitoring:**
Use
[AWS observability tools](https://docs.aws.amazon.com/wellarchitected/latest/management-and-governance-guide/aws-observability-tools.html) to collect performance metrics
and measure KPIs.
- **Conduct analysis:**
Conduct in-depth analysis to identify the areas (like
configuration and application code) in your workload that is
under-performing as outlined in
[PERF05-BP02 Use monitoring solutions to understand the areas where performance is most critical](./perf_process_culture_use_monitoring_solutions.html). Use your analysis and performance tools to identify the performance improvement strategies.
- **Validate improvements:**
Use sandbox or pre-production environments to validate the
effectiveness of improvement strategies.
- **Implement changes:**
Implement the changes in production and continually monitor
the workload’s performance. Document the improvements, and communicate the changes to stakeholders.
- **Revisit and refine:** Regularly review your performance improvement process to identify areas for enhancement.

## Resources

**Related documents:**

- [AWS Blog](https://aws.amazon.com/blogs/)
- [What's
New with AWS](https://aws.amazon.com/new/?ref=wellarchitected)
- [AWS Skill Builder](https://explore.skillbuilder.aws/learn)

**Related videos:**

- [AWS re:Invent 2022 - Delivering sustainable, high-performing architectures](https://www.youtube.com/watch?v=FBc9hXQfat0)
- [AWS re:Invent 2023 - Optimize cost and performance and track progress toward mitigation](https://www.youtube.com/watch?v=keAfy8f84E0)
- [AWS re:Invent 2022 - AWS optimization: Actionable steps for immediate results](https://www.youtube.com/watch?v=0ifvNf2Tx3w)
- [AWS re:Invent 2022 - Optimize your AWS workloads with best-practice guidance](https://www.youtube.com/watch?v=t8yl1TrnuIk)

**Related examples:**

- [AWS Github](https://github.com/aws)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_process_culture_workload_performance.html*

---

# PERF05-BP04 Load test your workload

Load test your workload to verify it can handle production load and
identify any performance bottleneck.

**Common anti-patterns:**

- You load test individual parts of your workload but not your
entire workload.
- You load test on infrastructure that is not the same as your
production environment.
- You only conduct load testing to your expected load and not
beyond, to help foresee where you may have future problems.
- You perform load testing without consulting the [Amazon EC2 Testing Policy](https://aws.amazon.com/ec2/testing/) and submitting a Simulated Event Submissions Form. This results in your test failing to run, as it looks like a denial-of-service event.

**Benefits of establishing this best
practice:** Measuring your performance under a load test
will show you where you will be impacted as load increases. This can
provide you with the capability of anticipating needed changes
before they impact your workload.

**Level of risk exposed if this best practice
is not established:** Low

## Implementation guidance

Load testing in the cloud is a process to measure the performance
of cloud workload under realistic conditions with expected user
load. This process involves provisioning a production-like cloud
environment, using load testing tools to generate load, and
analyzing metrics to assess the ability of your workload handling
a realistic load. Load tests must be run using synthetic or
sanitized versions of production data (remove sensitive or
identifying information). Automatically carry out load tests as
part of your delivery pipeline, and compare the results against
pre-defined KPIs and thresholds. This process helps you continue
to achieve required performance.

### Implementation steps

- **Define your testing objectives:** Identify the performance aspects of your workload that you want to evaluate, such as throughput and response time.
- **Select a testing tool:** Choose and configure the load testing tool that suits your workload.
- **Set up your environment:**
Set up the test environment based on your production
environment. You can use AWS services to run
production-scale environments to test your architecture.
- **Implement monitoring:** Use monitoring tools such as [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) to collect metrics across the resources in your architecture. You can also collect and publish custom metrics.
- **Define scenarios:**
Define the load testing scenarios and parameters (like test
duration and number of users).
- **Conduct load testing:**
Perform test scenarios at scale. Take advantage of the AWS Cloud to test your workload to discover where it fails to
scale, or if it scales in a non-linear way. For example, use
Spot Instances to generate loads at low cost and discover
bottlenecks before they are experienced in production.
- **Analyze test results:**
Analyze the results to identify performance bottlenecks and
areas for improvements.
- **Document and share findings:**
Document and report on findings and recommendations. Share this information with stakeholders to help them make informed decision regarding performance optimization strategies.
- **Continually iterate:** Load testing should be performed at regular cadence, especially after a system change of update.

## Resources

**Related documents:**

- [Amazon CloudWatch RUM](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM.html)
- [Amazon CloudWatch Synthetics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.html)
- [Distributed
Load Testing on AWS](https://docs.aws.amazon.com/solutions/latest/distributed-load-testing-on-aws/welcome.html)

**Related videos:**

- [AWS Summit ANZ 2023: Accelerate with confidence through AWS Distributed Load Testing](https://www.youtube.com/watch?v=4J6lVqa6Yh8)
- [AWS re:Invent 2022 - Scaling on AWS for your first 10 million users](https://www.youtube.com/watch?v=yrP3M4_13QM)
- [Solving
with AWS Solutions: Distributed Load Testing](https://www.youtube.com/watch?v=Y-2rk0sSyOM)

- [AWS re:Invent 2021 - Optimize applications through end user insights with Amazon CloudWatch RUM](https://www.youtube.com/watch?v=NMaeujY9A9Y)
- [Demo
of Amazon CloudWatch Synthetics](https://www.youtube.com/watch?v=hF3NM9j-u7I)

**Related examples:**

- [Distributed
Load Testing on AWS](https://aws.amazon.com/solutions/implementations/distributed-load-testing-on-aws/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_process_culture_load_test.html*

---

# PERF05-BP05 Use automation to proactively remediate performance-related issues

Use key performance indicators (KPIs), combined with monitoring and
alerting systems, to proactively address performance-related issues.

**Common anti-patterns:**

- You only allow operations staff the ability to make operational
changes to the workload.
- You let all alarms filter to the operations team with no
proactive remediation.

**Benefits of establishing this best
practice:** Proactive remediation of alarm actions allows
support staff to concentrate on those items that are not
automatically actionable. This helps operations staff handle all
alarms without being overwhelmed and instead focus only on critical
alarms.

**Level of risk exposed if this best practice
is not established:** Low

## Implementation guidance

Use alarms to trigger automated actions to remediate issues where
possible. Escalate the alarm to those able to respond if automated
response is not possible. For example, you may have a system that
can predict expected key performance indicator (KPI) values and
alarm when they breach certain thresholds, or a tool that can
automatically halt or roll back deployments if KPIs are outside of
expected values.

Implement processes that provide visibility into performance as
your workload is running. Build monitoring dashboards and
establish baseline norms for performance expectations to determine
if the workload is performing optimally.

### Implementation steps

- **Identify remediation workflow:**
Identify and understand the performance issue that can be
remediated automatically. Use AWS monitoring solutions such
as
[Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) or AWS X-Ray to help you better understand
the root cause of the issue.
- **Define the automation process:**
Create a step-by-step remediation process that can
be used to automatically fix the issue.
- **Configure the initiation event:**
Configure the event to automatically initiate the
remediation process. For example, you can define a trigger
to automatically restart an instance when it reaches a
certain threshold of CPU utilization.
- **Automate the remediation:**
Use AWS services and technologies to automate the
remediation process. For example,
[AWS Systems Manager Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html) provides a secure and
scalable way to automate the remediation process. Make sure to use self-healing logic to revert changes if they do not successfully resolve the issue.
- **Test the workflow**
Test the automated remediation process in a pre-production
environment.
- **Implement the workflow:** Implement the automated remediation in the production environment.
- **Develop a playbook:** Develop and document a playbook that outlines the steps for the remediation plan, including the initiation events, remediation logic, and actions taken. Make sure to train stakeholders to help them effectively respond to automated remediation events.
- **Review and refine:** Regularly assess the effectiveness of the automated remediation workflow. Adjust initiation events and remediation logic if necessary.

## Resources

**Related documents:**

- [CloudWatch
Documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html)
- [Monitoring,
Logging, and Performance AWS Partner Network Partners](https://aws.amazon.com/devops/partner-solutions/#_Monitoring.2C_Logging.2C_and_Performance)
- [X-Ray
Documentation](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html)
- [Using
Alarms and Alarm Actions in CloudWatch](https://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/cw-example-using-alarm-actions.html)
- [Build a Cloud Automation Practice for Operational Excellence: Best Practices from AWS Managed Services](https://aws.amazon.com/blogs/mt/build-a-cloud-automation-practice-for-operational-excellence-best-practices-from-aws-managed-services/)
- [Automate your Amazon Redshift performance tuning with automatic table optimization](https://aws.amazon.com/blogs/big-data/automate-your-amazon-redshift-performance-tuning-with-automatic-table-optimization/)

**Related videos:**

- [AWS re:Invent 2023 - Strategies for automated scaling, remediation, and smart self-healing](https://www.youtube.com/watch?v=nlGyIa3UQYU)
- [AWS re:Invent 2023 - [LAUNCH] Application monitoring for modern workloads](https://www.youtube.com/watch?v=T2TovTLje8w)
- [AWS re:Invent 2023 - Implementing application observability](https://www.youtube.com/watch?v=IcTcwUSwIs4)
- [AWS re:Invent 2021 - Intelligently
automating cloud operations](https://www.youtube.com/watch?v=m0S8eAF0l54)
- [AWS re:Invent 2022 - Setting
up controls at scale in your AWS environment](https://www.youtube.com/watch?v=NkE9_okfPG8)
- [AWS re:Invent 2022 - Automating
patch management and compliance using AWS](https://www.youtube.com/watch?v=gL3baXQJvc0)
- [AWS re:Invent 2022 - How
Amazon uses better metrics for improved website
performance](https://www.youtube.com/watch?v=_uaaCiyJCFA&ab_channel=AWSEvents)
- [AWS re:Invent 2023 - Take a load off: Diagnose & resolve performance issues with Amazon RDS](https://www.youtube.com/watch?v=Ulj88e5Aqzg)
- [AWS re:Invent 2021 -{New Launch} Automatically detect and resolve issues with Amazon DevOps Guru](https://www.youtube.com/watch?v=iwQNQHwoXfk)
- [AWS re:Invent 2023 - Centralize your operations](https://www.youtube.com/watch?v=9-RBjmhDdaM)

**Related examples:**

- [CloudWatch Logs Customize Alarms](https://github.com/awslabs/cloudwatch-logs-customize-alarms)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_process_culture_automation_remediate_issues.html*

---

# PERF05-BP06 Keep your workload and services up-to-date

Stay up-to-date on new cloud services and features to adopt
efficient features, remove issues, and improve the overall
performance efficiency of your workload.

**Common anti-patterns:**

- You assume your current architecture is static and will not be
updated over time.
- You do not have any systems or a regular cadence to evaluate if
updated software and packages are compatible with your workload.

**Benefits of establishing this best
practice:** By establishing a process to stay up-to-date on
new services and offerings, you can adopt new features and
capabilities, resolve issues, and improve workload performance.

**Level of risk exposed if this best practice
is not established:** Low

## Implementation guidance

Evaluate ways to improve performance as new services, design
patterns, and product features become available. Determine which
of these could improve performance or increase the efficiency of
the workload through evaluation, internal discussion, or external
analysis. Define a process to evaluate updates, new features, and
services relevant to your workload. For example, build a proof of
concept that uses new technologies or consult with an internal
group. When trying new ideas or services, run performance tests to
measure the impact that they have on the performance of the
workload.

## Implementation steps

- **Inventory your workload:**
Inventory your workload software and architecture and identify
components that need to be updated.
- **Identify update sources:**
Identify news and update sources related to your workload
components. As an example, you can subscribe to
the [What’s New
at AWS blog](https://aws.amazon.com/new/) for the products that match your workload
component. You can subscribe to the RSS feed or manage
your [email
subscriptions](https://pages.awscloud.com/communication-preferences.html).
- **Define an update schedule:**
Define a schedule to evaluate new services and features for
your workload.

You can
use [AWS Systems Manager Inventory](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-inventory.html) to collect operating
system (OS), application, and instance metadata from your
Amazon EC2 instances and quickly understand which
instances are running the software and configurations
required by your software policy and which instances need
to be updated.

- **Assess the new update:**
Understand how to update the components of your workload. Take
advantage of agility in the cloud to quickly test how new
features can improve your workload to gain performance
efficiency.
- **Use automation:**
Use automation for the update process to reduce the level of
effort to deploy new features and limit errors caused by
manual processes.

You can
use [CI/CD](https://aws.amazon.com/blogs/devops/complete-ci-cd-with-aws-codecommit-aws-codebuild-aws-codedeploy-and-aws-codepipeline/) to
automatically update AMIs, container images, and other
artifacts related to your cloud application.
- You can use tools such
as [AWS Systems Manager Patch Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-patch.html) to automate the
process of system updates, and schedule the activity
using [AWS Systems Manager Maintenance Windows](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-maintenance.html).

- **Document the process:**
Document your process for evaluating updates and new services.
Provide your owners the time and space needed to research,
test, experiment, and validate updates and new services. Refer
back to the documented business requirements and KPIs to help
prioritize which update will make a positive business impact.

## Resources

**Related documents:**

- [AWS Blog](https://aws.amazon.com/blogs/)
- [What's
New with AWS](https://aws.amazon.com/new/?ref=wellarchitected)
- [Implementing up-to-date images with automated EC2 Image Builder pipelines](https://aws.amazon.com/blogs/compute/implementing-up-to-date-images-with-automated-ec2-image-builder-pipelines/)

**Related videos:**

- [AWS re:Inforce 2022 - Automating patch management and compliance using AWS](https://www.youtube.com/watch?v=gL3baXQJvc0)
- [All Things Patch: AWS Systems Manager | AWS Events](https://www.youtube.com/watch?v=PhIiVsCEBu8)

**Related examples:**

- [Inventory and Patch Management](https://mng.workshop.aws/ssm/use-case-labs/inventory_patch_management.html)
- [One Observability Workshop](https://catalog.workshops.aws/observability/en-US)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_process_culture_keep_workload_and_services_up_to_date.html*

---

# PERF05-BP07 Review metrics at regular intervals

As part of routine maintenance or in response to events or
incidents, review which metrics are collected. Use these reviews to
identify which metrics were essential in addressing issues and which
additional metrics, if they were being tracked, could help identify,
address, or prevent issues.

**Common anti-patterns:**

- You allow metrics to stay in an alarm state for an extended
period of time.
- You create alarms that are not actionable by an automation
system.

**Benefits of establishing this best
practice:** Continually review metrics that are being
collected to verify that they properly identify, address, or prevent
issues. Metrics can also become stale if you let them stay in an
alarm state for an extended period of time.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Constantly improve metric collection and monitoring. As part of
responding to incidents or events, evaluate which metrics were
helpful in addressing the issue and which metrics could have
helped that are not currently being tracked. Use this method to
improve the quality of metrics you collect so that you can prevent,
or more quickly resolve future incidents.

As part of responding to incidents or events, evaluate which
metrics were helpful in addressing the issue and which metrics
could have helped that are not currently being tracked. Use this
to improve the quality of metrics you collect so that you can
prevent or more quickly resolve future incidents.

### Implementation steps

- **Define metrics:** Define critical performance metrics to monitor that are aligned to your workload
objective, including metrics such as response time and resource utilization.
- **Establish baselines:** Set a baseline and desirable value for each metric. The baseline should provide reference points to identify deviation or anomalies.
- **Set up a cadence:** Set a cadence (like weekly or monthly) to review critical metrics.
- **Identify performance issues:** During each review, assess trends and deviation from the baseline values. Look for
any performance bottlenecks or anomalies. For identified issues, conduct in-depth root cause analysis to understand the main
reason behind the issue.
- **Identify corrective actions:** Use your analysis to identify corrective actions. This may include parameter tuning, fixing bugs, and scaling resources.
- **Document findings:** Document your findings, including identified issues, root causes, and corrective actions.
- **Iterate and improve:** Continually assess and improve the metrics review process. Use the lesson learned from previous review to enhance the process over time.

## Resources

**Related documents:**

- [CloudWatch
Documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html)
- [Collect
metrics and logs from Amazon EC2 Instances and on-premises
servers with the CloudWatch Agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Install-CloudWatch-Agent.html?ref=wellarchitected)
- [Query your metrics with CloudWatch Metrics Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/query_with_cloudwatch-metrics-insights.html)
- [Monitoring,
Logging, and Performance AWS Partner Network Partners](https://aws.amazon.com/devops/partner-solutions/#_Monitoring.2C_Logging.2C_and_Performance)
- [X-Ray
Documentation](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html)

**Related videos:**

- [AWS re:Invent 2022 - Setting
up controls at scale in your AWS environment](https://www.youtube.com/watch?v=NkE9_okfPG8)
- [AWS re:Invent 2022 - How
Amazon uses better metrics for improved website
performance](https://www.youtube.com/watch?v=_uaaCiyJCFA&ab_channel=AWSEvents)
- [AWS re:Invent 2023 - Building an effective observability strategy](https://www.youtube.com/watch?v=7PQv9eYCJW8)
- [AWS Summit SF 2022 - Full-stack observability and application monitoring with AWS](https://www.youtube.com/watch?v=or7uFFyHIX0)
- [AWS re:Invent 2023 - Take a load off: Diagnose & resolve performance issues with Amazon RDS](https://www.youtube.com/watch?v=Ulj88e5Aqzg)

**Related examples:**

- [Creating
a dashboard with Quick](https://github.com/aws-samples/amazon-quicksight-sdk-proserve)
- [CloudWatch Dashboards](https://catalog.us-east-1.prod.workshops.aws/workshops/a8e9c6a6-0ba9-48a7-a90d-378a440ab8ba/en-US/300-cloudwatch/340-cloudwatch-dashboards)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/perf_process_culture_review_metrics.html*

---

---

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
