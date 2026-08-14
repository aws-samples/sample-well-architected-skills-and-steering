# Sustainability — All Questions & Best Practices

This file contains all 6 WA Framework questions for the sustainability pillar
and their complete best-practice content. Load this ONE file to have the entire
pillar in context at once — no need for 6 separate Read calls.

For a lightweight catalog of every BP ID across all 6 pillars, see
`references/manifest.md`.

---

## Question SUS01

# SUS 1 — How do you select Regions for your workload?

**Pillar**: Sustainability  
**Best Practices**: 1

---

# SUS01-BP01 Choose Region based on both business requirements and sustainability goals

Choose a Region for your workload based on both your business requirements
and sustainability goals to optimize its KPIs, including performance, cost,
and carbon footprint.

**Common anti-patterns:**

- You select the workload’s Region based on your own location.
- You consolidate all workload resources into one geographic location.

**Benefits of establishing this best practice:** Placing a workload
close to Amazon renewable energy projects or Regions with low published carbon intensity can help
to lower the carbon footprint of a cloud workload.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

The AWS Cloud is a constantly expanding network of Regions and points of presence (PoP),
with a global network infrastructure linking them together. The choice of Region for your
workload significantly affects its KPIs, including performance, cost, and carbon footprint.
To effectively improve these KPIs, you should choose Regions for your workload based on
both your business requirements and sustainability goals.

### Implementation steps

- **Shortlist potential Regions:** Follow these steps to assess and shortlist potential Regions for your workload
based on your business requirements, including compliance, available features,
cost, and latency:

Confirm that these Regions are compliant, based on your required local regulations (for example, data sovereignty).
- Use the [AWS Regional Services Lists](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/) to check if the Regions have the services and features you need to run your workload.
- Calculate the cost of the workload on each Region using the [AWS Pricing Calculator](https://calculator.aws/).
- Test the network latency between your end user locations and each AWS Region.

- **Choose Regions:** Choose Regions near Amazon renewable energy projects and Regions where the grid has a
published carbon intensity that is lower than other locations (or Regions).

Identify your relevant sustainability guidelines to track and compare year-to-year
carbon emissions based on [Greenhouse Gas Protocol](https://ghgprotocol.org/) (market-based and location based methods).
- Choose region based on method you use to track carbon emissions. For more detail
on choosing a Region based on your sustainability guidelines, see
[How to select a Region for your workload based on sustainability goals](https://aws.amazon.com/blogs/architecture/how-to-select-a-region-for-your-workload-based-on-sustainability-goals/).

## Resources

**Related documents:**

- [Understanding your carbon emission estimations](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/ccft-estimation.html)
- [Amazon
Around the Globe](https://sustainability.aboutamazon.com/about/around-the-globe?energyType=true)
- [Renewable
Energy Methodology](https://sustainability.aboutamazon.com/amazon-renewable-energy-methodology)
- [What
to Consider when Selecting a Region for your Workloads](https://aws.amazon.com/blogs/architecture/what-to-consider-when-selecting-a-region-for-your-workloads/)

**Related videos:**

- [AWS re:Invent 2023 - Sustainability innovation in AWS Global Infrastructure](https://www.youtube.com/watch?v=0EkcwLKeOQA)
- [AWS re:Invent 2023 - Sustainable architecture: Past, present, and future](https://www.youtube.com/watch?v=2xpUQ-Q4QcM)
- [AWS re:Invent 2022 - Delivering sustainable, high-performing architectures](https://www.youtube.com/watch?v=FBc9hXQfat0)
- [AWS re:Invent 2022 - Architecting sustainably and reducing your AWS carbon footprint](https://www.youtube.com/watch?v=jsbamOLpCr8)
- [AWS re:Invent 2022 - Sustainability in AWS global infrastructure](https://www.youtube.com/watch?v=NgMa8R9-Ywk)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_region_a2.html*

---

---

## Question SUS02

# SUS 2 — How do you align cloud resources to your demand?

**Pillar**: Sustainability  
**Best Practices**: 6

---

# SUS02-BP01 Scale workload infrastructure dynamically

Use elasticity of the cloud and scale your infrastructure dynamically to match supply of cloud
resources to demand and avoid overprovisioned capacity in your workload.

**Common anti-patterns:**

- You do not scale your infrastructure with user load.
- You manually scale your infrastructure all the time.
- You leave increased capacity after a scaling event instead of scaling back down.

**Benefits of establishing this best practice:** Configuring and testing
workload elasticity help to efficiently match supply of cloud resources to demand and avoid overprovisioned
capacity. You can take advantage of elasticity in the cloud to automatically scale capacity during and
after demand spikes to make sure you are only using the right number of resources needed to meet your
business requirements.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

The cloud provides the flexibility to expand or reduce your resources dynamically through a variety of
mechanisms to meet changes in demand. Optimally matching supply to demand delivers the lowest environmental
impact for a workload.

Demand can be fixed or variable, requiring metrics and automation to make sure that management does
not become burdensome. Applications can scale vertically (up or down) by modifying the instance size,
horizontally (in or out) by modifying the number of instances, or a combination of both.

You can use a number of different approaches to match supply of resources with demand.

- **Target-tracking approach:** Monitor your scaling metric and
automatically increase or decrease capacity as you need it.
- **Predictive scaling:** Scale in anticipation of daily and weekly trends.
- **Schedule-based approach:** Set your own scaling schedule according to
predictable load changes.
- **Service scaling:** Pick services (like serverless) that are natively
scaling by design or provide auto scaling as a feature.

Identify periods of low or no utilization and scale resources to remove excess capacity and improve efficiency.

## Implementation steps

- Elasticity matches the supply of resources you have against the demand for those resources.
Instances, containers, and functions provide mechanisms for elasticity, either in combination with
automatic scaling or as a feature of the service. AWS provides a range of auto scaling mechanisms
to ensure that workloads can scale down quickly and easily during periods of low user load. Here
are some examples of auto scaling mechanisms:

Auto scaling mechanism
Where to use

[Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html)

Use to verify you have the correct number of Amazon EC2 instances available to
handle the user load for your application.

[Application Auto Scaling](https://docs.aws.amazon.com/autoscaling/application/userguide/what-is-application-auto-scaling.html)

Use to automatically scale the resources for individual AWS services beyond Amazon EC2,
such as Lambda functions or Amazon Elastic Container Service (Amazon ECS) services.

[Kubernetes Cluster Autoscaler](https://aws.amazon.com/blogs/aws/introducing-karpenter-an-open-source-high-performance-kubernetes-cluster-autoscaler/)

Use to automatically scale Kubernetes clusters on AWS.
- Scaling is often discussed related to compute services like Amazon EC2 instances or AWS Lambda
functions. Consider the configuration of non-compute services like [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) read and write
capacity units or [Amazon Kinesis Data Streams](https://aws.amazon.com/kinesis/data-streams/) shards to match the demand.
- Verify that the metrics for scaling up or down are validated against the type of workload being deployed.
If you are deploying a video transcoding application, 100% CPU utilization is expected and should not be your primary metric.
You can use a [customized metric](https://aws.amazon.com/blogs/mt/create-amazon-ec2-auto-scaling-policy-memory-utilization-metric-linux/) (such as memory utilization) for your
scaling policy if required. To choose the right metrics, consider the following guidance for Amazon EC2:

The metric should be a valid utilization metric and describe how busy an instance is.
- The metric value must increase or decrease proportionally to the number of instances in the Auto Scaling group.

- Use [dynamic scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scale-based-on-demand.html) instead of
[manual scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-manual-scaling.html) for your Auto Scaling group.
We also recommend that you use [target
tracking scaling policies](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-target-tracking.html) in your dynamic scaling.
- Verify that workload deployments can handle both scale-out and scale-in events. Create test scenarios for scale-in events to verify that the workload behaves as expected
and does not affect the user experience (like losing sticky sessions). You can use
[Activity history](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-verify-scaling-activity.html) to verify a scaling activity for an Auto Scaling group.
- Evaluate your workload for predictable patterns and proactively scale as you anticipate predicted and planned changes in demand. With predictive scaling, you can eliminate the need to overprovision capacity. For more detail, see
[Predictive Scaling with Amazon EC2 Auto Scaling](https://aws.amazon.com/blogs/compute/introducing-native-support-for-predictive-scaling-with-amazon-ec2-auto-scaling/).

## Resources

**Related documents:**

- [Getting
Started with Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/GettingStartedTutorial.html)
- [Predictive
Scaling for EC2, Powered by Machine Learning](https://aws.amazon.com/blogs/aws/new-predictive-scaling-for-ec2-powered-by-machine-learning/)
- [Analyze
user behavior using Amazon OpenSearch Service, Amazon Data Firehose and Kibana](https://aws.amazon.com/blogs/database/analyze-user-behavior-using-amazon-elasticsearch-service-amazon-kinesis-data-firehose-and-kibana/)
- [What
is Amazon CloudWatch?](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html)
- [Monitoring
DB load with Performance Insights on Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.html)
- [Introducing Native Support for Predictive Scaling with Amazon EC2 Auto Scaling](https://aws.amazon.com/blogs/compute/introducing-native-support-for-predictive-scaling-with-amazon-ec2-auto-scaling/)
- [Introducing Karpenter - An Open-Source, High-Performance Kubernetes Cluster Autoscaler](https://aws.amazon.com/blogs/aws/introducing-karpenter-an-open-source-high-performance-kubernetes-cluster-autoscaler/)
- [Deep Dive on Amazon ECS Cluster Auto Scaling](https://aws.amazon.com/blogs/containers/deep-dive-on-amazon-ecs-cluster-auto-scaling/)

**Related videos:**

- [AWS re:Invent 2023 - Scaling on AWS for the first 10 million users](https://www.youtube.com/watch?v=JzuNJ8OUht0)
- [AWS re:Invent 2023 - Sustainable architecture: Past, present, and future](https://www.youtube.com/watch?v=2xpUQ-Q4QcM)
- [AWS re:Invent 2022 - Build a cost-, energy-, and resource-efficient
compute environment](https://www.youtube.com/watch?v=8zsC5e1eLCg)
- [AWS re:Invent 2022 - Scaling containers from one user to millions](https://www.youtube.com/watch?v=hItHqzKoBk0)
- [AWS re:Invent 2023 - Scaling FM inference to hundreds of models with Amazon SageMaker AI](https://www.youtube.com/watch?v=6xENDvgnMCs)
- [AWS re:Invent 2023 - Harness the power of Karpenter to scale, optimize & upgrade Kubernetes](https://www.youtube.com/watch?v=lkg_9ETHeks)

**Related examples:**

- [Autoscaling](https://www.eksworkshop.com/docs/autoscaling/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_user_a2.html*

---

# SUS02-BP02 Align SLAs with sustainability goals

Review and optimize workload service-level agreements
(SLA) based on your sustainability goals to minimize the
resources required to support your workload while continuing
to meet business needs.

**Common anti-patterns:**

- Workload SLAs are unknown or ambiguous.
- You define your SLA just for availability and performance.
- You use the same design pattern (like Multi-AZ architecture) for all your workloads.

**Benefits of establishing this best practice:** Aligning
SLAs with sustainability goals leads to optimal resource usage while meeting business
needs.

**Level of risk exposed if this best practice
is not established:** Low

## Implementation guidance

SLAs define the level of service expected from a cloud workload,
such as response time, availability, and data retention. They
influence the architecture, resource usage, and environmental
impact of a cloud workload. At a regular cadence, review SLAs
and make trade-offs that significantly reduce resource usage
in exchange for acceptable decreases in service levels.

### Implementation steps

- **Understand sustainability goals:** Identify sustainability goals in your organization, such as carbon reduction or improving resource utilization.
- **Review SLAs:** Evaluate your SLAs to assess if they support your business requirements. If you are exceeding SLAs, perform further review.
- **Understand trade-offs:** Understand the trade-offs across your workload’s complexity (like high volume of concurrent users), performance (like latency), and sustainability impact (like required resources). Typically, prioritizing two of the factors comes at the expense of the third.
- **Adjust SLAs:** Adjust your SLAs by making trade-offs that significantly reduce sustainability impacts in exchange for acceptable decreases in service levels.

**Sustainability and reliability:** Highly available workloads tend to consume more resources.
- **Sustainability and performance:** Using more resources to boost performance could have a higher environmental impact.
- **Sustainability and security:** Overly secure workloads could have a higher environmental impact.

- **Define sustainability SLAs if possible:** Include sustainability SLAs for your workload. For example, define a minimum utilization level as a sustainability SLA for your compute instances.
- **Use efficient design patterns:** Use design patterns such as microservices on AWS that prioritize business-critical functions and allow lower service levels (such as response time or recovery time objectives) for non-critical functions.
- **Communicate and establish accountability:** Share the SLAs with all relevant stakeholders, including your development team and your customers. Use reporting to track and monitor the SLAs. Assign accountability to meet the sustainability targets for your SLAs.
- **Use incentives and rewards:** Use incentives and rewards to achieve or exceed SLAs aligned with sustainability goals.
- **Review and iterate:** Regularly review and adjust your SLAs to make sure they are aligned with evolving sustainability and performance goals.

## Resources

**Related documents:**

- [Understand resiliency patterns and trade-offs to architect efficiently in the cloud](https://aws.amazon.com/blogs/architecture/understand-resiliency-patterns-and-trade-offs-to-architect-efficiently-in-the-cloud/)
- [Importance
of Service Level Agreement for SaaS Providers](https://aws.amazon.com/blogs/apn/importance-of-service-level-agreement-for-saas-providers/)

**Related videos:**

- [AWS re:Invent 2023 - Capacity, availability, cost efficiency: Pick three](https://www.youtube.com/watch?v=E0dYLPXrX_w)
- [AWS re:Invent 2023 - Sustainable architecture: Past, present, and future](https://www.youtube.com/watch?v=2xpUQ-Q4QcM)
- [AWS re:Invent 2023 - Advanced integration patterns & trade-offs for loosely coupled systems](https://www.youtube.com/watch?v=FGKGdUiZKto)
- [AWS re:Invent 2022 - Delivering sustainable, high-performing architectures](https://www.youtube.com/watch?v=FBc9hXQfat0)
- [AWS re:Invent 2022 - Build a cost-, energy-, and resource-efficient compute environment](https://www.youtube.com/watch?v=8zsC5e1eLCg)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_user_a3.html*

---

# SUS02-BP03 Stop the creation and maintenance of unused assets

Decommission unused assets in your workload to reduce
the number of cloud resources required to support your
demand and minimize waste.

**Common anti-patterns:**

- You do not analyze your application for assets that are redundant or no longer required.
- You do not remove assets that are redundant or no longer required.

**Benefits of establishing this best practice:** Removing
unused assets frees resources and improves the overall efficiency of the workload.

**Level of risk exposed if this best practice
is not established:** Low

## Implementation guidance

Unused assets consume cloud resources like storage space and compute power. By identifying and eliminating these assets, you can free up these resources, resulting in a more efficient cloud architecture. Perform regular analysis on application assets such as pre-compiled reports, datasets, static images, and asset access patterns to identify redundancy, underutilization, and potential decommission targets. Remove those redundant assets to reduce the resource waste in your workload.

### Implementation steps

- **Conduct an inventory:** Conduct a comprehensive inventory to identify all assets within your workload.
- **Analyze usage:** Use continuous monitoring to identify static assets that are no longer required.
- **Remove unused assets:** Develop a plan to remove assets that are no longer required.

Before removing any asset, evaluate the impact of removing it on the architecture.
- Consolidate overlapping generated assets to remove redundant processing.
- Update your applications to no longer produce and store assets that are not required.

- **Communicate with third parties:** Instruct third parties to stop producing and storing assets managed on your behalf that are no longer required. Ask to consolidate redundant assets.
- **Use lifecycle policies:** Use lifecycle policies to automatically delete unused assets.

You can use [Amazon S3 Lifecycle](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html) to manage your objects throughout their lifecycle.
- You can use [Amazon Data Lifecycle Manager](https://docs.aws.amazon.com/ebs/latest/userguide/snapshot-lifecycle.html) to automate the creation, retention, and deletion of Amazon EBS snapshots and Amazon EBS-backed AMIs.

- **Review and optimize:** Regularly review your workload to identify and remove any unused assets.

## Resources

**Related documents:**

- [Optimizing
your AWS Infrastructure for Sustainability, Part II:
Storage](https://aws.amazon.com/blogs/architecture/optimizing-your-aws-infrastructure-for-sustainability-part-ii-storage/)
- [How do I terminate active resources that I no longer need on my AWS account?](https://aws.amazon.com/premiumsupport/knowledge-center/terminate-resources-account-closure/)

**Related videos:**

- [AWS re:Invent 2023 - Sustainable architecture: Past, present, and future](https://www.youtube.com/watch?v=2xpUQ-Q4QcM)
- [AWS re:Invent 2022 - Preserving and maximizing the value of digital media assets using Amazon S3](https://www.youtube.com/watch?v=8OI0Uu-YvD8)
- [AWS re:Invent 2023 - Optimize costs in your multi-account environments](https://www.youtube.com/watch?v=ie_Mqb-eC4A)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_user_a4.html*

---

# SUS02-BP04 Optimize geographic placement of workloads based on their networking requirements

Select cloud location and services for your workload that reduce the distance network
traffic must travel and decrease the total network resources required to support your workload.

**Common anti-patterns:**

- You select the workload's Region based on your own location.
- You consolidate all workload resources into one geographic location.
- All traffic flows through your existing data centers.

**Benefits of establishing this best practice:** Placing a workload close
to its users provides the lowest latency while decreasing data movement across
the network and reducing environmental impact.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

The AWS Cloud infrastructure is built around location options such as Regions, Availability Zones,
placement groups, and edge locations such as [AWS Outposts](https://docs.aws.amazon.com/outposts/latest/userguide/what-is-outposts.html) and [AWS Local Zones](https://aws.amazon.com/about-aws/global-infrastructure/localzones/). These location options
are responsible for maintaining connectivity between application components, cloud services, edge networks and on-premises data centers.

Analyze the network access patterns in your workload to identify how to use these cloud location options and reduce the distance network traffic must travel.

## Implementation steps

- Analyze network access patterns in your workload to identify how users use your application.

Use monitoring tools, such as [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) and [AWS CloudTrail](https://aws.amazon.com/cloudtrail/), to gather data on network activities.
- Analyze the data to identify the network access pattern.

- Select the Regions for your workload deployment based on the following key elements:

**Your Sustainability goal:** as explained in [Region selection](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/region-selection.html).
- **Where your data is located:** For data-heavy applications (such as big data and machine learning),
application code should run as close to the data as possible.
- **Where your users are located:** For user-facing
applications, choose a Region (or Regions) close to your workload’s users.
- **Other constraints:** Consider constraints such as
cost and compliance as explained in [What to Consider when Selecting a Region for your Workloads](https://aws.amazon.com/blogs/architecture/what-to-consider-when-selecting-a-region-for-your-workloads/).

- Use local caching or [AWS
Caching Solutions](https://aws.amazon.com/caching/aws-caching/) for frequently used assets to improve performance, reduce
data movement, and lower environmental impact.

Service
When to use

[Amazon CloudFront](https://aws.amazon.com/cloudfront/)

Use to cache static content such as images, scripts, and videos, as well as dynamic content
such as API responses or web applications.

[Amazon ElastiCache](https://aws.amazon.com/elasticache/)

Use to cache content for web applications.

[DynamoDB Accelerator](https://aws.amazon.com/dynamodb/dax/)

Use to add in-memory acceleration to your DynamoDB tables.
- Use services that can help you run code closer to users of your workload:

Service
When to use

[Lambda@Edge](https://aws.amazon.com/lambda/edge/)

Use for
compute-heavy operations that are initiated when objects are not in the cache.

[Amazon CloudFront Functions](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-functions.html)

Use for simple use cases like HTTP(s) request or response manipulations
that can be initiated by short-lived functions.

[AWS IoT Greengrass](https://aws.amazon.com/greengrass/)

Use to run local compute, messaging, and data caching for connected devices.
- Use connection pooling to allow for connection reuse and reduce required
resources.
- Use distributed data stores that don’t rely on persistent connections and synchronous updates for consistency to serve regional populations.
- Replace pre-provisioned static network capacity with shared dynamic capacity, and share the sustainability impact of network capacity with other subscribers.

## Resources

**Related documents:**

- [Optimizing
your AWS Infrastructure for Sustainability, Part III:
Networking](https://aws.amazon.com/blogs/architecture/optimizing-your-aws-infrastructure-for-sustainability-part-iii-networking/)
- [Amazon ElastiCache Documentation](https://docs.aws.amazon.com/elasticache/index.html)
- [What
is Amazon CloudFront?](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html)
- [Amazon CloudFront Key Features](https://aws.amazon.com/cloudfront/features/)
- [AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/)
- [AWS Local Zones and AWS Outposts, choosing the right technology for your edge workload](https://aws.amazon.com/blogs/compute/aws-local-zones-and-aws-outposts-choosing-the-right-technology-for-your-edge-workload/)
- [Placement groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html)
- [AWS Local Zones](https://aws.amazon.com/about-aws/global-infrastructure/localzones/)
- [AWS Outposts](https://aws.amazon.com/outposts/)

**Related videos:**

- [Demystifying data transfer on AWS](https://www.youtube.com/watch?v=-MqXgzw1IGA)
- [Scaling network performance on next-gen Amazon EC2 instances](https://www.youtube.com/watch?v=jNYpWa7gf1A)
- [AWS Local Zones Explainer Video](https://www.youtube.com/watch?v=JHt-D4_zh7w)
- [AWS Outposts: Overview and How it Works](https://www.youtube.com/watch?v=ppG2FFB0mMQ)
- [AWS re:Invent 2023 - A migration strategy for edge and on-premises workloads](https://www.youtube.com/watch?v=4wUXzYNLvTw)
- [AWS re:Invent 2021 - AWS Outposts: Bringing the AWS experience on premises](https://www.youtube.com/watch?v=FxVF6A22498)
- [AWS re:Invent 2020 - AWS Wavelength: Run apps with ultra-low latency at 5G edge](https://www.youtube.com/watch?v=AQ-GbAFDvpM)
- [AWS re:Invent 2022 - AWS Local Zones: Building applications for a distributed edge](https://www.youtube.com/watch?v=bDnh_d-slhw)
- [AWS re:Invent 2021 - Building low-latency websites with Amazon CloudFront](https://www.youtube.com/watch?v=9npcOZ1PP_c)
- [AWS re:Invent 2022 - Improve performance and availability with AWS Global Accelerator](https://www.youtube.com/watch?v=s5sjsdDC0Lg)
- [AWS re:Invent 2022 - Build your global wide area network using AWS](https://www.youtube.com/watch?v=flBieylTwvI)
- [AWS re:Invent 2020: Global traffic management with Amazon Route 53](https://www.youtube.com/watch?v=E33dA6n9O7I)

**Related examples:**

- [AWS Networking
Workshops](https://catalog.workshops.aws/networking/en-US)
- [Architecting for sustainability - Minimize data movement across networks](https://catalog.us-east-1.prod.workshops.aws/workshops/7c4f8394-8081-4737-aa1b-6ae811d46e0a/en-US)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_user_a5.html*

---

# SUS02-BP05 Optimize team member resources for activities performed

Optimize resources provided to team members to minimize the
environmental sustainability impact while supporting their needs.

**Common anti-patterns:**

- You ignore the impact of devices used by your team members on the overall efficiency of your cloud application.
- You manually manage and update resources used by team members.

**Benefits of establishing this best practice:** Optimizing
team member resources improves the overall efficiency of cloud-enabled applications.

**Level of risk exposed if this best practice
is not established:** Low

## Implementation guidance

Understand the resources your team members use to consume your services, their expected lifecycle, and the financial and sustainability impact. Implement strategies to optimize these resources. For example, perform complex operations, such as rendering and compilation, on highly utilized scalable infrastructure instead of on underutilized high-powered single-user systems.

### Implementation steps

- **Use energy-efficient workstations:** Provide team members with energy-efficient workstations and peripherals. Use efficient power management features (like low power mode) in these devices to reduce their energy usage
- **use virtualization:** Use virtual desktops and application streaming to limit upgrade and device requirements.
- **Encourage remote collaboration:** Encourage team members to use remote collaboration tools such as [Amazon Chime](https://aws.amazon.com/chime/) or [AWS Wickr](https://aws.amazon.com/wickr/) to reduce the need for travel and associated carbon emissions.
- **Use energy-efficient software:** Provide team members with energy-efficient software by removing or turning off unnecessary features and processes.
- **Manage lifecycles:** Evaluate the impact of processes and systems on your device lifecycle, and select solutions that minimize the requirement for device replacement while satisfying business requirements. Regularly maintain and update workstations or software to maintain and improve efficiency.
- **Remote device management:** Implement remote management for devices to reduce required business travel.

[AWS Systems Manager Fleet Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/fleet.html) is a unified user interface (UI) experience that helps you remotely manage your nodes running on AWS or on premises.

## Resources

**Related documents:**

- [What
is Amazon WorkSpaces?](https://docs.aws.amazon.com/workspaces/latest/adminguide/amazon-workspaces.html)
- [Cost Optimizer for Amazon WorkSpaces](https://docs.aws.amazon.com/solutions/latest/cost-optimizer-for-workspaces/overview.html)
- [Amazon
AppStream 2.0 Documentation](https://docs.aws.amazon.com/appstream2/)
- [NICE
DCV](https://docs.aws.amazon.com/dcv/)

**Related videos:**

- [Managing cost for Amazon WorkSpaces on AWS](https://www.youtube.com/watch?v=0MoY31hZQuE)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_user_a6.html*

---

# SUS02-BP06 Implement buffering or throttling to flatten the demand curve

Buffering and throttling flatten the demand curve and reduce the provisioned capacity required for your workload.

**Common anti-patterns:**

- You process the client requests immediately while it is not needed.
- You do not analyze the requirements for client requests.

**Benefits of establishing this best practice:** Flattening the demand curve reduce the required provisioned capacity for the workload. Reducing the provisioned capacity means less energy consumption and less environmental impact.

**Level of risk exposed if this best practice
is not established:** Low

## Implementation guidance

Flattening the workload demand curve can help you to reduce the provisioned capacity for a workload and reduce its environmental impact. Assume a workload with the demand curve shown in below figure. This workload has two peaks, and to handle those peaks, the resource capacity as shown by orange line is provisioned. The resources and energy used for this workload is not indicated by the area under the demand curve, but the area under the provisioned capacity line, as provisioned capacity is needed to handle those two peaks.

*Demand curve with two distinct peaks that require high provisioned capacity.*

You can use buffering or throttling to modify the demand curve and smooth out the peaks, which means less provisioned capacity and less energy consumed. Implement throttling when your clients can perform retries. Implement buffering to store the request and defer processing until a later time.

*Throttling's effect on the demand curve and provisioned capacity.*

**Implementation steps**

- Analyze the client requests to determine how to respond to them. Questions to consider include:

Can this request be processed asynchronously?
- Does the client have retry capability?

- If the client has retry capability, then you can implement throttling, which tells the source that if it cannot service the request at the current time, it should try again later.

You can use [Amazon API Gateway](https://aws.amazon.com/api-gateway/) to implement throttling.

- For clients that cannot perform retries, a buffer needs to be implemented to flatten the demand curve. A buffer defers request processing, allowing applications that run at different rates to communicate effectively. A buffer-based approach uses a queue or a stream to accept messages from producers. Messages are read by consumers and processed, allowing the messages to run at the rate that meets the consumers’ business requirements.

[Amazon Simple Queue Service (Amazon SQS)](https://aws.amazon.com/sqs/) is a managed service that provides queues that allow a single consumer to read individual messages.
- [Amazon Kinesis](https://aws.amazon.com/kinesis/) provides a stream that allows many consumers to read the same messages.

- Analyze the overall demand, rate of change, and required response time to right size the throttle or buffer required.

## Resources

**Related documents:**

- [Getting started with Amazon SQS](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-getting-started.html)
- [Application integration Using Queues and Messages](https://aws.amazon.com/blogs/architecture/application-integration-using-queues-and-messages/)
- [Managing and monitoring API throttling in your workloads](https://aws.amazon.com/blogs/mt/managing-monitoring-api-throttling-in-workloads/)
- [Throttling a tiered, multi-tenant REST API at scale using API Gateway](https://aws.amazon.com/blogs/architecture/throttling-a-tiered-multi-tenant-rest-api-at-scale-using-api-gateway-part-1/)
- [Application integration Using Queues and Messages](https://aws.amazon.com/blogs/architecture/application-integration-using-queues-and-messages/)

**Related videos:**

- [AWS re:Invent 2022 - Application integration patterns for microservices](https://www.youtube.com/watch?v=GoBOivyE7PY)
- [AWS re:Invent 2023 - Smart savings: Amazon EC2 cost-optimization strategies](https://www.youtube.com/watch?v=_AHPbxzIGV0)
- [AWS re:Invent 2023 - Advanced integration patterns & trade-offs for loosely coupled systems](https://www.youtube.com/watch?v=FGKGdUiZKto)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_user_a7.html*

---

---

## Question SUS03

# SUS 3 — How do you take advantage of software and architecture patterns to support your sustainability goals?

**Pillar**: Sustainability  
**Best Practices**: 5

---

# SUS03-BP01 Optimize software and architecture for asynchronous and scheduled jobs

Use efficient software and architecture patterns such as queue-driven to
maintain consistent high utilization of deployed resources.

**Common anti-patterns:**

- You overprovision the resources in your cloud workload to meet unforeseen spikes in demand.
- Your architecture does not decouple senders and receivers of asynchronous messages by a messaging component.

**Benefits of establishing this best practice:**

- Efficient software and architecture patterns minimize the unused resources in your workload and improve the overall efficiency.
- You can scale the processing independently of the receiving of asynchronous messages.
- Through a messaging component, you have relaxed availability requirements that you can meet with fewer resources.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Use efficient architecture patterns such as [event-driven architecture](https://aws.amazon.com/event-driven-architecture/) that result in
even utilization of components and minimize overprovisioning in your workload. Using
efficient architecture patterns minimizes idle resources from lack of use due to changes
in demand over time.

Understand the requirements of your workload components and adopt architecture patterns
that increase overall utilization of resources. Retire components that are no longer required.

### Implementation steps

- Analyze the demand for your workload to determine how to respond to those.
- For requests or jobs that don’t require synchronous responses, use queue-driven
architectures and auto scaling workers to maximize utilization. Here are some
examples of when you might consider queue-driven architecture:

Queuing mechanism
Description

[AWS Batch job queues](https://docs.aws.amazon.com/batch/latest/userguide/job_queues.html)

AWS Batch jobs are submitted to a job queue where
they reside until they can be scheduled to run in a
compute environment.

[Amazon Simple Queue Service and Amazon EC2 Spot Instances](https://aws.amazon.com/blogs/compute/running-cost-effective-queue-workers-with-amazon-sqs-and-amazon-ec2-spot-instances/)

Pairing Amazon SQS and Spot Instances to build fault tolerant and efficient architecture.
- For requests or jobs that can be processed anytime, use scheduling mechanisms
to process jobs in batch for more efficiency. Here are some examples of scheduling
mechanisms on AWS:

Scheduling mechanism
Description

[Amazon EventBridge Scheduler](https://aws.amazon.com/blogs/compute/introducing-amazon-eventbridge-scheduler/)

A capability from [Amazon EventBridge](https://aws.amazon.com/eventbridge/) that allows you to create, run, and manage scheduled tasks at scale.

[AWS Glue time-based schedule](https://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html)

Define a time-based schedule for your crawlers and jobs in AWS Glue.

[Amazon Elastic Container Service (Amazon ECS) scheduled tasks](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/scheduled_tasks.html)

Amazon ECS supports creating scheduled tasks. Scheduled tasks use Amazon EventBridge rules to run tasks either on a schedule or in a response to an EventBridge event.

[Instance Scheduler](https://aws.amazon.com/solutions/implementations/instance-scheduler-on-aws/)

Configure start and stop schedules for your Amazon EC2 and Amazon Relational Database Service instances.
- If you use polling and webhooks mechanisms in your architecture, replace those with events.
Use [event-driven architectures](https://docs.aws.amazon.com/lambda/latest/operatorguide/event-driven-architectures.html) to build highly efficient workloads.
- Leverage [serverless on AWS](https://aws.amazon.com/serverless/) to eliminate over-provisioned infrastructure.
- Right size individual components of your architecture to prevent idling resources waiting for input.

You can use the [Rightsizing Recommendations in AWS Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-rightsizing.html) or [AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/) to identify rightsizing opportunities.
- For more detail, see [Right Sizing: Provisioning Instances to Match Workloads](https://docs.aws.amazon.com/whitepapers/latest/cost-optimization-right-sizing/cost-optimization-right-sizing.html).

## Resources

**Related documents:**

- [What
is Amazon Simple Queue Service?](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html)
- [What
is Amazon MQ?](https://docs.aws.amazon.com/amazon-mq/latest/developer-guide/welcome.html)
- [Scaling
based on Amazon SQS](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-using-sqs-queue.html)
- [What
is AWS Step Functions?](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html)
- [What
is AWS Lambda?](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)
- [Using
AWS Lambda with Amazon SQS](https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html)
- [What
is Amazon EventBridge?](https://docs.aws.amazon.com/eventbridge/latest/userguide/what-is-amazon-eventbridge.html)
- [Managing Asynchronous Workflows with a REST API](https://aws.amazon.com/blogs/architecture/managing-asynchronous-workflows-with-a-rest-api/)

**Related videos:**

- [AWS re:Invent 2023 - Navigating the journey to serverless event-driven architecture](https://www.youtube.com/watch?v=hvGuqHp051c)
- [AWS re:Invent 2023 - Using serverless for event-driven architecture & domain-driven design](https://www.youtube.com/watch?v=3foMZJSPMI4)
- [AWS re:Invent 2023 - Advanced event-driven patterns with Amazon EventBridge](https://www.youtube.com/watch?v=6X4lSPkn4ps)
- [AWS re:Invent 2023 - Sustainable architecture: Past, present, and future](https://www.youtube.com/watch?v=2xpUQ-Q4QcM)
- [Asynchronous Message Patterns | AWS Events](https://www.youtube.com/watch?v=-yJqBuwouZ4)

**Related examples:**

- [Event-driven architecture with AWS Graviton Processors and Amazon EC2 Spot Instances](https://catalog.workshops.aws/well-architected-sustainability/en-US/2-software-and-architecture/event-driven-architecture-with-graviton-spot)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_software_a2.html*

---

# SUS03-BP02 Remove or refactor workload components with low or no use

Remove components that are unused and no longer required, and refactor
components with little utilization to minimize waste in your workload.

**Common anti-patterns:**

- You do not regularly check the utilization level of individual components of your workload.
- You do not check and analyze recommendations from AWS rightsizing tools such as [AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/).

**Benefits of establishing this best practice:** Removing unused components
minimizes waste and improves the overall efficiency of your cloud workload.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Unused or underutilized components in a cloud workload consume unnecessary compute, storage or network resources. Remove or refactor these components to directly reduce waste and improve the overall efficiency of a cloud workload. This is an iterative improvement process which can be initiated by changes in demand or the release of a new cloud service. For example, a significant drop in [AWS Lambda](https://docs.aws.amazon.com/lambda/) function run time can be indicate a need to lower the memory size. Also, as AWS releases new services and features, the optimal services and architecture for your workload may change.

Continually monitor workload activity and look for opportunities to improve the utilization level of individual components. By removing idle components and performing rightsizing activities, you meet your business requirements with the fewest cloud resources.

### Implementation steps

- **Inventory your AWS resourceds:** Create an inventory of your AWS resources. In AWS, you can turn on [AWS Resource Explorer](https://docs.aws.amazon.com/resource-explorer/latest/userguide/welcome.html) to explore and organize your AWS resources. For more details, see [AWS re:Invent 2022 - How to manage resources and applications at scale on AWS](https://www.youtube.com/watch?v=bbgUnKq6PAU).
- **Monitor utilization:** Monitor and capture the utilization metrics for critical components of your workload (like CPU utilization, memory utilization, or network throughput in [Amazon CloudWatch metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/working_with_metrics.html)).
- **Identify unused components:**Identify unused or under-utilized components in your architecture.

For stable workloads, check AWS rightsizing tools such as [AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/) at regular intervals to identify idle, unused, or underutilized components.
- For ephemeral workloads, evaluate utilization metrics to identify idle, unused, or underutilized components.

- **Remove unused components:** Retire components and associated assets (like Amazon ECR images) that are no longer needed.

[Automated Cleanup of Unused Images in Amazon ECR](https://aws.amazon.com/blogs/compute/automated-cleanup-of-unused-images-in-amazon-ecr/)
- [Delete unused Amazon Elastic Block Store (Amazon EBS) volumes by using AWS Config and AWS Systems Manager](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/delete-unused-amazon-elastic-block-store-amazon-ebs-volumes-by-using-aws-config-and-aws-systems-manager.html)

- **Refactor underutilized components:** Refactor or consolidate underutilized components with other resources to improve utilization efficiency. For example, you can provision multiple small databases on a single [Amazon RDS](https://aws.amazon.com/rds/) database instance instead of running databases on individual underutilized instances.
- **Evaluate improvements:** Understand the [resources provisioned by your workload to complete a unit of work](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/evaluate-specific-improvements.html). Use this information to evaluate improvements achieved by removing or refactoring components.

[Measure and track cloud efficiency with sustainability proxy metrics, Part I: What are proxy metrics?](https://aws.amazon.com/blogs/aws-cloud-financial-management/measure-and-track-cloud-efficiency-with-sustainability-proxy-metrics-part-i-what-are-proxy-metrics/)
- [Measure and track cloud efficiency with sustainability proxy metrics, Part II: Establish a metrics pipeline](https://aws.amazon.com/blogs/aws-cloud-financial-management/measure-and-track-cloud-efficiency-with-sustainability-proxy-metrics-part-ii-establish-a-metrics-pipeline/)

## Resources

**Related documents:**

- [AWS Trusted Advisor](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/)
- [What
is Amazon CloudWatch?](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html)
- [Right Sizing: Provisioning Instances to Match Workloads](https://docs.aws.amazon.com/whitepapers/latest/cost-optimization-right-sizing/cost-optimization-right-sizing.html)
- [Optimizing your cost with Rightsizing Recommendations](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-rightsizing.html)

**Related videos:**

- [AWS re:Invent 2023 - Capacity, availability, cost efficiency: Pick three](https://www.youtube.com/watch?v=E0dYLPXrX_w)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_software_a3.html*

---

# SUS03-BP03 Optimize areas of code that consume the most time or resources

Optimize your code that runs within different components of your
architecture to minimize resource usage while maximizing performance.

**Common anti-patterns:**

- You ignore optimizing your code for resource usage.
- You usually respond to performance issues by increasing the resources.
- Your code review and development process does not track performance changes.

**Benefits of establishing this best practice:** Using
efficient code minimizes resource usage and improves performance.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

It is crucial to examine every functional area, including the code for a cloud architected application, to optimize its resource usage and performance. Continually monitor your workload’s performance in build environments and production and identify opportunities to improve code snippets that have particularly high resource usage. Adopt a regular review process to identify bugs or anti-patterns within your code that use resources inefficiently. Leverage simple and efficient algorithms that produce the same results for your use case.

## Implementation steps

- **Use efficient programming language:**
Use an efficient operating system and programming language for the workload. For details on energy efficient programming languages (including Rust), see [Sustainability with Rust](https://aws.amazon.com/blogs/opensource/sustainability-with-rust/).
- **Use an AI coding companion:** Consider using an AI coding companion such as [Amazon Q Developer](https://aws.amazon.com/q/developer/) to efficiently write code.
- **Automate code reviews:**
While developing your workloads, adopt an automated code review process to improve quality and identify bugs and anti-patterns.

[Automate code reviews with Amazon CodeGuru Reviewer](https://aws.amazon.com/blogs/devops/automate-code-reviews-with-amazon-codeguru-reviewer/)
- [Detecting concurrency bugs with Amazon CodeGuru](https://aws.amazon.com/blogs/devops/detecting-concurrency-bugs-with-amazon-codeguru/)
- [Raising code quality for Python applications using Amazon CodeGuru](https://aws.amazon.com/blogs/devops/raising-code-quality-for-python-applications-using-amazon-codeguru/)

- **Use a code profiler:**
Use a code profiler to identify the areas of code that use the most time or resources as targets for optimization.

[Reducing your organization's carbon footprint with Amazon CodeGuru Profiler](https://aws.amazon.com/blogs/devops/reducing-your-organizations-carbon-footprint-with-codeguru-profiler/)
- [Understanding memory usage in your Java application with Amazon CodeGuru Profiler](https://aws.amazon.com/blogs/devops/understanding-memory-usage-in-your-java-application-with-amazon-codeguru-profiler/)
- [Improving customer experience and reducing cost with Amazon CodeGuru Profiler](https://aws.amazon.com/blogs/devops/improving-customer-experience-and-reducing-cost-with-codeguru-profiler/)

- **Monitor and optimize:** Use continuous monitoring resources to identify components with high resource requirements or suboptimal configuration.

Replace computationally intensive algorithms with simpler and more efficient version that produce the same result.
- Remove unnecessary code such as sorting and formatting.

- **Use code refactoring or transformation:** Explore the possibility of [Amazon Q code transformation](https://aws.amazon.com/q/aws/code-transformation/) for application maintenance and upgrades.

[Upgrade language versions with Amazon Q Code Transformation](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/code-transformation.html)
- [AWS re:Invent 2023 - Automate app upgrades & maintenance using Amazon Q Code Transformation](https://www.youtube.com/watch?v=LY76tak6Z1E)

## Resources

**Related documents:**

- [What
is Amazon CodeGuru Profiler?](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/what-is-codeguru-profiler.html)
- [FPGA
instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/fpga-getting-started.html)
- [The AWS SDKs
on Tools to Build on AWS](https://aws.amazon.com/tools/)

**Related videos:**

- [Improve Code Efficiency Using Amazon CodeGuru Profiler](https://www.youtube.com/watch?v=1pU4VddsBRw)
- [Automate Code Reviews and Application Performance Recommendations with Amazon CodeGuru](https://www.youtube.com/watch?v=OD8H63C0E0I)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_software_a4.html*

---

# SUS03-BP04 Optimize impact on devices and equipment

Understand the devices and equipment used in your architecture and use strategies to reduce their usage. This can minimize the overall environmental impact of your cloud workload.

**Common anti-patterns:**

- You ignore the environmental impact of devices used by your customers.
- You manually manage and update resources used by customers.

**Benefits of establishing this best practice:** Implementing software patterns and features that are optimized for customer device can reduce the overall environmental impact of cloud workload.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Implementing software patterns and features that are optimized for customer devices can reduce the environmental impact in several ways:

- Implementing new features that are backward compatible can reduce the number of hardware replacements.
- Optimizing an application to run efficiently on devices can help to reduce their energy consumption and extend their battery life (if they are powered by battery).
- Optimizing an application for devices can also reduce the data transfer over the network.

Understand the devices and equipment used in your architecture, their expected lifecycle, and the impact of replacing those components. Implement software patterns and features that can help to minimize the device energy consumption, the need for customers to replace the device and also upgrade it manually.

### Implementation steps

- **Conduct an inventory:**
Inventory the devices used in your architecture. Devices can be mobile, tablet, IOT devices, smart light, or even smart devices in a factory.
- **Use energy-efficient devices:** Consider using energy-efficient devices in your architecture. Use power management configurations on devices to enter low power mode when not in use.
- **Run efficient applications:**
Optimize the application running on the devices:

Use strategies such as running tasks in the background to reduce their energy consumption.
- Account for network bandwidth and latency when building payloads, and implement capabilities that help your applications work well on low bandwidth, high latency links.
- Convert payloads and files into optimized formats required by devices. For example, you can use [Amazon Elastic Transcoder](https://docs.aws.amazon.com/elastic-transcoder/) or [AWS Elemental MediaConvert](https://aws.amazon.com/mediaconvert/) to convert large, high quality digital media files into formats that users can play back on mobile devices, tablets, web browsers, and connected televisions.
- Perform computationally intense activities server-side (such as image rendering), or use application streaming to improve the user experience on older devices.
- Segment and paginate output, especially for interactive sessions, to manage payloads and limit local storage requirements.

- **Engage suppliers:**
Work with device suppliers who use sustainable materials and provide transparency in their supply chains and environmental certifications.
- **Use over-the-air (OTA) updates:**
Use automated over-the-air (OTA) mechanism to deploy updates to one or more devices.

You can use a [CI/CD pipeline](https://aws.amazon.com/blogs/mobile/build-a-cicd-pipeline-for-your-android-app-with-aws-services/) to update mobile applications.
- You can use [AWS IoT Device Management](https://aws.amazon.com/iot-device-management/) to remotely manage connected devices at scale.

- **Use managed device farms:**
To test new features and updates, use managed device farms with representative sets of hardware and iterate development to maximize the devices supported. For more details, see [SUS06-BP05 Use managed device farms for testing](./sus_sus_dev_a5.html).
- **Continue to monitor and improve:**
Track the energy usage of devices to identify areas for improvement. Use new technologies or best practices to enhance environmental impacts of these devices.

## Resources

**Related documents:**

- [What
is AWS Device Farm?](https://docs.aws.amazon.com/devicefarm/latest/developerguide/welcome.html)
- [WorkSpaces Applications Documentation](https://docs.aws.amazon.com/appstream2/)
- [NICE
DCV](https://docs.aws.amazon.com/dcv/)
- [OTA tutorial for updating firmware on devices running FreeRTOS](https://docs.aws.amazon.com/freertos/latest/userguide/dev-guide-ota-workflow.html)
- [Optimizing Your IoT Devices for Environmental Sustainability](https://aws.amazon.com/blogs/architecture/optimizing-your-iot-devices-for-environmental-sustainability/)

**Related videos:**

- [AWS re:Invent 2023 - Improve your mobile and web app quality using AWS Device Farm](https://www.youtube.com/watch?v=__93Tm0YCRg)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_software_a5.html*

---

# SUS03-BP05 Use software patterns and architectures that best support data access and storage patterns

Understand how data is used within your workload, consumed by your users, transferred, and stored.
Use software patterns and architectures that best support data access and storage to minimize the compute,
networking, and storage resources required to support the workload.

**Common anti-patterns:**

- You assume that all workloads have similar data storage and access patterns.
- You only use one tier of storage, assuming all workloads fit within that tier.
- You assume that data access patterns will stay consistent over time.
- Your architecture supports a potential high data access burst, which results in the resources remaining idle most of the time.

**Benefits of establishing this best practice:** Selecting and optimizing your architecture based on data access and storage patterns will help decrease development complexity and increase overall utilization. Understanding when to use global tables, data partitioning, and caching will help you decrease operational overhead and scale based on your workload needs.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

To improve long-term workload sustainability, use architecture patterns that support data access and storage characteristics for your workload. These patterns help you efficiently retrieve and process data. For example, you can use [modern data architecture on AWS](https://aws.amazon.com/big-data/datalakes-and-analytics/modern-data-architecture/) with purpose-built services optimized for your unique analytics use cases. These architecture patterns allow for efficient data processing and reduce the resource usage.

### Implementation steps

- **Understand data characteristics:** Analyze your data characteristics and access patterns to identify the correct configuration for your cloud resources. Key characteristics to consider include:

**Data type:** structured, semi-structured, unstructured
- **Data growth:** bounded, unbounded
- **Data durability:** persistent, ephemeral, transient
- **Access patterns** reads or writes, update frequency, spiky, or consistent

- **Use optimal architecture patterns:** Use architecture patterns that best support data access and storage patterns.

[Patterns for enabling data persistence](https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-data-persistence/enabling-patterns.html)
- [Let’s Architect! Modern data architectures](https://aws.amazon.com/blogs/architecture/lets-architect-modern-data-architectures/)
- [Databases on AWS: The Right Tool for the Right Job](https://www.youtube.com/watch?v=-pb-DkD6cWg)

- **Use purpose-built services:** Use technologies that are fit-for-purpose.

Use technologies that work natively with compressed data.

[Athena Compression Support file formats](https://docs.aws.amazon.com/athena/latest/ug/compression-formats.html)
- [Format Options for ETL Inputs and Outputs in AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-format.html)
- [Loading compressed data files from Amazon S3 with Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/dg/t_loading-gzip-compressed-data-files-from-S3.html)

- Use purpose-built [analytics services](https://aws.amazon.com/big-data/datalakes-and-analytics/?nc2=h_ql_prod_an_a) for data processing in your architecture. For detail on AWS purpose-built analytics services, see [AWS re:Invent 2022 - Building modern data architectures on AWS](https://www.youtube.com/watch?v=Uk2CqEt5f0o).
- Use the database engine that best supports your dominant query pattern. Manage your database indexes for efficient querying. For further details, see [AWS Databases](https://aws.amazon.com/products/databases/) and [AWS re:Invent 2022 - Modernize apps with purpose-built databases](https://www.youtube.com/watch?v=V-DiplATdi0).

- **Minimize data transfer:** Select network protocols that reduce the amount of network capacity consumed in your architecture.

## Resources

**Related documents:**

- [COPY
from columnar data formats with Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/dg/copy-usage_notes-copy-from-columnar.html)
- [Converting
Your Input Record Format in Firehose](https://docs.aws.amazon.com/firehose/latest/dev/record-format-conversion.html)
- [Improve
query performance on Amazon Athena by Converting to Columnar
Formats](https://docs.aws.amazon.com/athena/latest/ug/convert-to-columnar.html)
- [Monitoring
DB load with Performance Insights on Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_PerfInsights.html)
- [Monitoring
DB load with Performance Insights on Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_PerfInsights.html)
- [Amazon S3 Intelligent-Tiering storage class](https://aws.amazon.com/s3/storage-classes/intelligent-tiering/)
- [Build a CQRS event store with Amazon DynamoDB](https://aws.amazon.com/blogs/database/build-a-cqrs-event-store-with-amazon-dynamodb/)

**Related videos:**

- [AWS re:Invent 2022 - Building data mesh architectures on AWS](https://www.youtube.com/watch?v=nGRvlobeM_U)
- [AWS re:Invent 2023 - Deep dive into Amazon Aurora and its innovations](https://www.youtube.com/watch?v=je6GCOZ22lI)
- [AWS re:Invent 2023 - Improve Amazon EBS efficiency and be more cost-efficient](https://www.youtube.com/watch?v=7-CB02rqiuw)
- [AWS re:Invent 2023 - Optimizing storage price and performance with Amazon S3](https://www.youtube.com/watch?v=RxgYNrXPOLw)
- [AWS re:Invent 2023 - Building and optimizing a data lake on Amazon S3](https://www.youtube.com/watch?v=mpQa_Zm1xW8)
- [AWS re:Invent 2023 - Advanced event-driven patterns with Amazon EventBridge](https://www.youtube.com/watch?v=6X4lSPkn4ps)

**Related examples:**

- [AWS Purpose Built Databases Workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/93f64257-52be-4c12-a95b-c0a1ff3b7e2b/en-US)
- [AWS Modern Data Architecture Immersion Day](https://catalog.us-east-1.prod.workshops.aws/workshops/32f3e732-d67d-4c63-b967-c8c5eabd9ebf/en-US)
- [Build a Data Mesh on AWS](https://catalog.us-east-1.prod.workshops.aws/workshops/23e6326b-58ee-4ab0-9bc7-3c8d730eb851/en-US)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_software_a6.html*

---

---

## Question SUS04

# SUS 4 — How do you take advantage of data management policies and patterns?

**Pillar**: Sustainability  
**Best Practices**: 8

---

# SUS04-BP01 Implement a data classification policy

Classify data to understand its criticality to business
outcomes and choose the right energy-efficient storage tier
to store the data.

**Common anti-patterns:**

- You do not identify data assets with similar characteristics
(such as sensitivity, business criticality, or regulatory
requirements) that are being processed or stored.
- You have not implemented a data catalog to inventory your data assets.

**Benefits of establishing this best practice:** Implementing
a data classification policy allows you to determine the most energy-efficient storage
tier for data.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Data classification involves identifying the types of data
that are being processed and stored in an information system
owned or operated by an organization. It also involves making
a determination on the criticality of the data and the likely
impact of a data compromise, loss, or misuse.

Implement data classification policy by working backwards
from the contextual use of the data and creating a categorization
scheme that takes into account the level of criticality of a
given dataset to an organization’s operations.

### Implementation steps

- **Perform data inventory:**
Conduct an inventory of the various data types that exist for your workload.
- **Group data:**
Determine criticality, confidentiality, integrity, and
availability of data based on risk to the organization.
Use these requirements to group data into one of the data
classification tiers that you adopt. As an example, see [Four simple steps to classify your data and
secure your startup](https://aws.amazon.com/blogs/startups/four-simple-steps-to-classify-your-data-and-secure-your-startup/).
- **Define data classification levels and policies:**
For each data group, define data classification level (for example, public or confidential) and handling policies. Tag data accordingly. For more detail on data classification categories, see Data Classification whitepaper.
- **Periodically review:**
Periodically review and audit your environment for untagged and
unclassified data. Use automation to identify this data, and classify and tag the data
appropriately. As an example, see [Data Catalog and crawlers in AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/catalog-and-crawler.html).
- **Establish a data catalog:**
Establish a data catalog that provides
audit and governance capabilities.
- **Documentation:**
Document data classification policies and handling procedures
for each data class.

## Resources

**Related documents:**

- [Leveraging
AWS Cloud to Support Data Classification](https://docs.aws.amazon.com/whitepapers/latest/data-classification/leveraging-aws-cloud-to-support-data-classification.html)
- [Tag
policies from AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_tag-policies.html)

**Related videos:**

- [AWS re:Invent 2022 - Enabling agility with data governance on AWS](https://www.youtube.com/watch?v=vznDgJkoH7k)
- [AWS re:Invent 2023 - Data protection and resilience with AWS storage](https://www.youtube.com/watch?v=rdG8JV3Fhk4)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_data_a2.html*

---

# SUS04-BP02 Use technologies that support data access and storage patterns

Use storage technologies that best support how your
data is accessed and stored to minimize the resources
provisioned while supporting your workload.

**Common anti-patterns:**

- You assume that all workloads have similar data storage and access patterns.
- You only use one tier of storage, assuming all workloads fit within that tier.
- You assume that data access patterns will stay consistent over time.

**Benefits of establishing this best practice:** Selecting
and optimizing your storage technologies based on data access and storage patterns will
help you reduce the required cloud resources to meet your business needs and improve
the overall efficiency of cloud workload.

**Level of risk exposed if this best practice
is not established:** Low

## Implementation guidance

Select the storage solution that aligns best to your access
patterns, or consider changing your access patterns to align
with the storage solution to maximize performance efficiency.

### Implementation steps

- **Evaluate data and access characteristics:**
Evaluate your data characteristics and access pattern to
collect the key characteristics of your storage needs.
Key characteristics to consider include:

**Data type:** structured, semi-structured,
unstructured
- **Data growth:** bounded, unbounded
- **Data durability:** persistent, ephemeral,
transient
- **Access patterns:** reads or writes,
frequency, spiky, or consistent

- **Choose the right storage technology:**
Migrate data to the appropriate storage technology that supports
your data characteristics and access pattern. Here are some
examples of AWS storage technologies and their
key characteristics:

Type
Technology
Key characteristics

Object storage

[Amazon S3](https://aws.amazon.com/s3/)

An object storage service with unlimited scalability,
high availability, and multiple options for accessibility.
Transferring and accessing objects in and out of Amazon S3
can use a service, such as
[Transfer Acceleration](https://aws.amazon.com/s3/transfer-acceleration/)
or [Access
Points](https://aws.amazon.com/s3/features/access-points/), to support your location, security needs, and access
patterns.

Archiving storage

[Amazon Glacier](https://aws.amazon.com/s3/storage-classes/glacier/)

Storage class of Amazon S3 built for data-archiving.

Shared file system

[Amazon Elastic File System (Amazon EFS)](https://aws.amazon.com/efs/)

Mountable file system that can be accessed by multiple
types of compute solutions. Amazon EFS automatically
grows and shrinks storage and is performance-optimized
to deliver consistent low latencies.

Shared file system

[Amazon FSx](https://aws.amazon.com/fsx/)

Built on the latest AWS compute solutions to support
four commonly used file systems: NetApp ONTAP, OpenZFS,
Windows File Server, and Lustre. Amazon FSx
[latency,
throughput, and IOPS](https://aws.amazon.com/fsx/when-to-choose-fsx/) vary per file system and should be
considered when selecting the right file system for your
workload needs.

Block storage

[Amazon Elastic Block Store (Amazon EBS)](https://aws.amazon.com/ebs/)

Scalable, high-performance block-storage service
designed for Amazon Elastic Compute Cloud (Amazon EC2).
Amazon EBS includes SSD-backed storage for transactional,
IOPS-intensive workloads and HDD-backed storage for
throughput-intensive workloads.

Relational database

[Amazon Aurora](https://aws.amazon.com/rds/aurora/), [Amazon RDS](https://aws.amazon.com/rds/), [Amazon Redshift](https://aws.amazon.com/redshift/)

Designed to support ACID (atomicity, consistency, isolation, durability) transactions and maintain referential integrity and strong data consistency. Many traditional applications, enterprise resource planning (ERP), customer relationship management (CRM), and ecommerce systems use relational databases to store their data.

Key-value database

[Amazon DynamoDB](https://aws.amazon.com/dynamodb/)

Optimized for common access patterns, typically to store and retrieve large volumes of data. High-traffic web apps, ecommerce systems, and gaming applications are typical use-cases for key-value databases.
- **Automate storage allocation:**
For storage systems that are a fixed size, such as
Amazon EBS or Amazon FSx, monitor the available
storage space and automate storage allocation on
reaching a threshold. You can leverage Amazon CloudWatch
to collect and analyze different metrics for
[Amazon EBS](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using_cloudwatch_ebs.html) and
[Amazon FSx](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/monitoring-cloudwatch.html).
- **Choose the right storage class:**
Choose the appropriate storage class for your data.

Amazon S3 storage classes can be configured at the object
level. A single bucket can contain objects stored
across all of the storage classes.
- You can use
[Amazon S3 Lifecycle policies](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html) to automatically transition objects
between storage classes or remove data without any application changes.
In general, you have to make a trade-off between resource
efficiency, access latency, and reliability when considering
these storage mechanisms.

## Resources

**Related documents:**

- [Amazon EBS volume types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volume-types.html)
- [Amazon EC2 instance store](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html)
- [Amazon S3 Intelligent-Tiering](https://docs.aws.amazon.com/AmazonS3/latest/userguide/intelligent-tiering.html)
- [Amazon EBS I/O Characteristics](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/ebs-io-characteristics.html)
- [Using Amazon S3 storage classes](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html)
- [What
is Amazon Glacier?](https://docs.aws.amazon.com/amazonglacier/latest/dev/introduction.html)

**Related videos:**

- [AWS re:Invent 2023 - Improve Amazon EBS efficiency and be more cost-efficient](https://www.youtube.com/watch?v=7-CB02rqiuw)
- [AWS re:Invent 2023 - Optimizing storage price and performance with Amazon S3](https://www.youtube.com/watch?v=RxgYNrXPOLw)
- [AWS re:Invent 2023 - Building and optimizing a data lake on Amazon S3](https://www.youtube.com/watch?v=mpQa_Zm1xW8)
- [AWS re:Invent 2022 - Building modern data architectures on AWS](https://www.youtube.com/watch?v=Uk2CqEt5f0o)
- [AWS re:Invent 2022 - Modernize apps with purpose-built databases](https://www.youtube.com/watch?v=V-DiplATdi0)
- [AWS re:Invent 2022 - Building data mesh architectures on AWS](https://www.youtube.com/watch?v=nGRvlobeM_U)
- [AWS re:Invent 2023 - Deep dive into Amazon Aurora and its innovations](https://www.youtube.com/watch?v=je6GCOZ22lI)
- [AWS re:Invent 2023 - Advanced data modeling with Amazon DynamoDB](https://www.youtube.com/watch?v=PVUofrFiS_A)

**Related examples:**

- [Amazon S3 Examples](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/s3-examples.html)
- [AWS Purpose Built Databases Workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/93f64257-52be-4c12-a95b-c0a1ff3b7e2b/en-US)
- [Databases for Developers](https://catalog.workshops.aws/db4devs/en-US)
- [AWS Modern Data Architecture Immersion Day](https://catalog.us-east-1.prod.workshops.aws/workshops/32f3e732-d67d-4c63-b967-c8c5eabd9ebf/en-US)
- [Build a Data Mesh on AWS](https://catalog.us-east-1.prod.workshops.aws/workshops/23e6326b-58ee-4ab0-9bc7-3c8d730eb851/en-US)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_data_a3.html*

---

# SUS04-BP03 Use policies to manage the lifecycle of your datasets

Manage the lifecycle of all of your data and automatically enforce
deletion to minimize the total storage required for your workload.

**Common anti-patterns:**

- You manually delete data.
- You do not delete any of your workload data.
- You do not move data to more energy-efficient storage tiers based on its retention and access requirements.

**Benefits of establishing this best practice:** Using data lifecycle policies ensures efficient data access and retention in a workload.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Datasets usually have different retention and access requirements during their lifecycle.
For example, your application may need frequent access to some datasets for a limited
period of time. After that, those datasets are infrequently accessed. To improve the efficiency of data storage and computation over time, implement lifecycle policies, which are rules that define how data is handled over time.

With lifecycle configuration rules, you can tell the specific storage service to transition a dataset to more energy-efficient storage tiers, archive it, or delete it. This practice minimizes active data storage and retrieval, which leads to lower energy consumption. In addition, practices such as archiving or deleting obsolete data support regulatory compliance and data governance.

### Implementation steps

- **Use data classification:** [Classify datasets in your workload.](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_data_a2.html)
- **Define handling rules:** Define handling procedures for each data class.
- **Enable automation:** Set automated lifecycle policies to enforce lifecycle rules.
Here are some examples of how to set up automated lifecycle policies
for different AWS storage services:

Storage service
How to set automated lifecycle policies

[Amazon S3](https://aws.amazon.com/s3/index.html)

You can use [Amazon S3 Lifecycle](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html) to manage your objects throughout their lifecycle.
If your access patterns are unknown, changing, or unpredictable, you can use [Amazon S3
Intelligent-Tiering](https://docs.aws.amazon.com/AmazonS3/latest/userguide/intelligent-tiering.html), which monitors access patterns and automatically moves objects that
have not been accessed to lower-cost access tiers. You can leverage [Amazon S3 Storage Lens](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage_lens.html)
metrics to identify optimization opportunities and gaps in lifecycle management.

[Amazon Elastic Block Store](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AmazonEBS.html)

You can use [Amazon Data Lifecycle Manager](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/snapshot-lifecycle.html) to automate the creation,
retention, and deletion of Amazon EBS snapshots and Amazon EBS-backed AMIs.

[Amazon Elastic File System](https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html)

[Amazon EFS lifecycle management](https://docs.aws.amazon.com/efs/latest/ug/lifecycle-management-efs.html) automatically manages file storage for your file systems.

[Amazon Elastic Container Registry](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html)

[Amazon ECR lifecycle policies](https://docs.aws.amazon.com/AmazonECR/latest/userguide/LifecyclePolicies.html) automate the cleanup of your
container images by expiring images based on age or count.

[AWS Elemental MediaStore](https://docs.aws.amazon.com/mediastore/latest/ug/what-is.html)

You can use an [object lifecycle policy](https://docs.aws.amazon.com/mediastore/latest/ug/policies-object-lifecycle.html) that governs how long objects should be stored in the MediaStore container.
- **Delete unused assets:** Delete unused volumes, snapshots, and data that is out of its retention period.
Use native service features like [Amazon DynamoDB Time To Live](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/TTL.html) or [Amazon CloudWatch
log retention](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html#SettingLogRetention) for deletion.
- **Aggregate and compress:** Aggregate and compress data where applicable based on lifecycle rules.

## Resources

**Related documents:**

- [Optimize your Amazon S3 Lifecycle rules with Amazon S3 Storage Class Analysis](https://docs.aws.amazon.com/AmazonS3/latest/userguide/analytics-storage-class.html)
- [Evaluating
Resources with AWS Config Rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config.html)

**Related videos:**

- [AWS re:Invent 2021 - Amazon S3 Lifecycle best practices to optimize your storage spend](https://www.youtube.com/watch?v=yGNXn7jOytA)
- [AWS re:Invent 2023 - Optimizing storage price and performance with Amazon S3](https://www.youtube.com/watch?v=RxgYNrXPOLw)
- [Simplify Your Data Lifecycle and Optimize Storage Costs With Amazon S3 Lifecycle](https://www.youtube.com/watch?v=53eHNSpaMJI)
- [Reduce Your Storage Costs Using Amazon S3 Storage Lens](https://www.youtube.com/watch?v=A8qOBLM6ITY)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_data_a4.html*

---

# SUS04-BP04 Use elasticity and automation to expand block storage or file system

Use elasticity and automation to expand block storage or file system as data grows to minimize the total provisioned storage.

**Common anti-patterns:**

- You procure large block storage or file system for future need.
- You overprovision the input and output operations per second (IOPS) of your file system.
- You do not monitor the utilization of your data volumes.

**Benefits of establishing this best practice:** Minimizing over-provisioning for storage system reduces the idle resources and improves the overall efficiency of your workload.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Create block storage and file systems with size allocation, throughput, and latency that are appropriate for your workload. Use elasticity and automation to expand block storage or file system as data grows without having to over-provision these storage services.

### Implementation steps

- For fixed size storage like [Amazon EBS](https://aws.amazon.com/ebs/), verify that you are monitoring the amount of storage used versus the overall storage size and create automation, if possible, to increase the storage size when reaching a threshold.
- Use elastic volumes and managed block data services to automate allocation of additional storage as your persistent data grows. As an example, you can use [Amazon EBS Elastic Volumes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-modify-volume.html) to change volume size, volume type, or adjust the performance of your Amazon EBS volumes.
- Choose the right storage class, performance mode, and throughput mode for your file system to address your business need, not exceeding that.

[Amazon EFS performance](https://docs.aws.amazon.com/efs/latest/ug/performance.html)
- [Amazon EBS volume performance on Linux instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSPerformance.html)

- Set target levels of utilization for your data volumes, and resize volumes outside of expected ranges.
- Right size read-only volumes to fit the data.
- Migrate data to object stores to avoid provisioning the excess capacity from fixed volume sizes on block storage.
- Regularly review elastic volumes and file systems to terminate idle volumes and shrink over-provisioned resources to fit the current data size.

## Resources

**Related documents:**

- [Extend the file system after resizing an EBS volume](https://docs.aws.amazon.com/ebs/latest/userguide/recognize-expanded-volume-linux.html)
- [Modify a volume using Amazon EBS Elastic Volumes](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-modify-volume.html)
- [Amazon FSx Documentation](https://docs.aws.amazon.com/fsx/index.html)
- [What
is Amazon Elastic File System?](https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html)

**Related videos:**

- [Deep Dive on Amazon EBS Elastic Volumes](https://www.youtube.com/watch?v=Vi_1Or7QuOg)
- [Amazon EBS and Snapshot Optimization Strategies for Better Performance and Cost Savings](https://www.youtube.com/watch?v=h1hzRCsJefs)
- [Optimizing Amazon EFS for cost and performance, using best practices](https://www.youtube.com/watch?v=9kfeh6_uZY8)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_data_a5.html*

---

# SUS04-BP05 Remove unneeded or redundant data

Remove unneeded or redundant data to minimize the storage resources required to store your
datasets.

**Common anti-patterns:**

- You duplicate data that can be easily obtained or recreated.
- You back up all data without considering its criticality.
- You only delete data irregularly, on operational events, or not at all.
- You store data redundantly irrespective of the storage service's durability.
- You turn on Amazon S3 versioning without any business justification.

**Benefits of establishing this best practice:** Removing unneeded
data reduces the storage size required for your workload and the workload environmental impact.

**Level of risk exposed if this best practice is not established:**
Medium

## Implementation guidance

When you remove unneeded and redundant datasets, you can reduce storage cost and environmental footprint. This practice may also make computing more efficient, as compute resources only process important data instead of unneeded data. Automate the deletion of unneeded data. Use technologies that deduplicate data at the file and block level. Use service features for native data replication and redundancy.

### Implementation steps

- **Evaluate public datasets:** Evaluate if you can avoid storing data by using existing publicly available datasets
in [AWS Data Exchange](https://aws.amazon.com/data-exchange/) and [Open Data on AWS](https://registry.opendata.aws/).
- **De-deplicate data:** Use mechanisms that can deduplicate data at the block and object level. Here are some
examples of how to deduplicate data on AWS:

Storage service
Deduplication mechanism

[Amazon S3](https://aws.amazon.com/s3/)

Use [AWS Lake Formation FindMatches](https://aws.amazon.com/blogs/big-data/integrate-and-deduplicate-datasets-using-aws-lake-formation-findmatches/) to find matching records across a dataset
(including ones without identifiers) by using the new FindMatches ML
Transform.

[Amazon FSx](https://aws.amazon.com/fsx/)

Use [data deduplication](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/using-data-dedup.html)
on Amazon FSx for Windows.

[Amazon Elastic Block Store snapshots](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSSnapshots.html)

Snapshots are incremental backups, which means that only the blocks on the
device that have changed after your most recent snapshot are saved.
- **Use lifecycle policies:** Use lifecycle policies to automate unneeded data deletion. Use native service features like [Amazon DynamoDB Time To Live](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/TTL.html),
[Amazon S3 Lifecycle](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html), or [Amazon CloudWatch log
retention](https://docs.aws.amazon.com/managedservices/latest/userguide/log-customize-retention.html) for deletion.
- **Use data virtualization:** Use data virtualization capabilities on AWS to maintain data at its source and
avoid data duplication.

[Cloud Native Data
Virtualization on AWS](https://www.youtube.com/watch?v=BM6sMreBzoA)
- [Optimize Data Pattern Using Amazon Redshift Data Sharing](https://catalog.workshops.aws/well-architected-sustainability/en-US/3-data/optimize-data-pattern-using-redshift-data-sharing)

- **Use incremental backup:** Use backup technology that can make incremental backups.
- **Use native durability:** Leverage the durability of [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/DataDurability.html) and [replication of
Amazon EBS](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volumes.html) to meet your durability goals instead of self-managed technologies (such
as a redundant array of independent disks (RAID)).
- **Use efficient logging:** Centralize log and trace data, deduplicate identical log entries, and establish
mechanisms to tune verbosity when needed.
- **Use efficient caching:** Pre-populate caches only where justified.
- Establish cache monitoring and automation to resize the cache accordingly.
- **Remove old version assets:** Remove out-of-date deployments and assets from object stores and edge caches when
pushing new versions of your workload.

## Resources

**Related documents:**

- [Change log data retention in CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html#SettingLogRetention)
- [Data
deduplication on Amazon FSx for Windows File Server](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/using-data-dedup.html)
- [Features of
Amazon FSx for ONTAP including data deduplication](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/what-is-fsx-ontap.html#features-overview)
- [Invalidating Files on Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Invalidation.html)
- [Using AWS Backup to back up
and restore Amazon EFS file systems](https://docs.aws.amazon.com/efs/latest/ug/awsbackup.html)
- [What is
Amazon CloudWatch Logs?](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html)
- [Working with
backups on Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.html)
- [Integrate and deduplicate datasets using AWS Lake Formation](https://aws.amazon.com/blogs/big-data/integrate-and-deduplicate-datasets-using-aws-lake-formation-findmatches/)

**Related videos:**

- [Amazon Redshift Data Sharing Use
Cases](https://www.youtube.com/watch?v=sIoTB8B5nn4)

**Related examples:**

- [How do
I analyze my Amazon S3 server access logs using Amazon Athena?](https://aws.amazon.com/premiumsupport/knowledge-center/analyze-logs-athena/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_data_a6.html*

---

# SUS04-BP06 Use shared file systems or storage to access common data

Adopt shared file systems or storage to avoid data duplication and allow for more efficient
infrastructure for your workload.

**Common anti-patterns:**

- You provision storage for each individual client.
- You do not detach data volume from inactive clients.
- You do not provide access to storage across platforms and systems.

**Benefits of establishing this best practice:** Using shared file
systems or storage allows for sharing data to one or more consumers without having to copy the
data. This helps to reduce the storage resources required for the workload.

**Level of risk exposed if this best practice is not established:**
Medium

## Implementation guidance

If you have multiple users or applications accessing the same datasets, using shared
storage technology is crucial to use efficient infrastructure for your workload. Shared
storage technology provides a central location to store and manage datasets and avoid data
duplication. It also enforces consistency of the data across different systems. Moreover,
shared storage technology allows for more efficient use of compute power, as multiple compute
resources can access and process data at the same time in parallel.

Fetch data from these shared storage services only as needed and detach unused volumes to
free up resources.

### Implementation steps

- **Use shared storage:** Migrate data to shared storage when the data has multiple consumers. Here are some
examples of shared storage technology on AWS:

Storage option
When to use

[Amazon EBS
Multi-Attach](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volumes-multi.html)

Amazon EBS Multi-Attach allows you to attach a single Provisioned IOPS SSD (io1
or io2) volume to multiple instances that are in the same Availability
Zone.

[Amazon EFS](https://aws.amazon.com/efs/)

See [When to Choose
Amazon EFS](https://aws.amazon.com/efs/when-to-choose-efs/).

[Amazon FSx](https://aws.amazon.com/fsx/)

See [Choosing an Amazon FSx
File System](https://aws.amazon.com/fsx/when-to-choose-fsx/).

[Amazon S3](https://aws.amazon.com/s3/)

Applications that do not require a file system structure and are designed to
work with object storage can use Amazon S3 as a massively scalable, durable, low-cost
object storage solution.
- **Fetch data as needed:** Copy data to or fetch data from shared file systems only as needed. As an example, you
can create an [Amazon FSx for Lustre file system backed by Amazon S3](https://aws.amazon.com/blogs/storage/new-enhancements-for-moving-data-between-amazon-fsx-for-lustre-and-amazon-s3/) and only load the subset of data
required for processing jobs to Amazon FSx.
- **Delete unneeded data:** Delete data as appropriate for your usage patterns as outlined in [SUS04-BP03 Use policies to manage the lifecycle of your datasets](./sus_sus_data_a4.html).
- **Detach inactive clients:** Detach volumes from clients that are not actively using them.

## Resources

**Related documents:**

- [Linking your file system
to an Amazon S3 bucket](https://docs.aws.amazon.com/fsx/latest/LustreGuide/create-dra-linked-data-repo.html)
- [Using Amazon EFS for AWS Lambda in your serverless applications](https://aws.amazon.com/blogs/compute/using-amazon-efs-for-aws-lambda-in-your-serverless-applications/)
- [Amazon EFS Intelligent-Tiering Optimizes Costs for Workloads with Changing Access Patterns](https://aws.amazon.com/blogs/aws/new-amazon-efs-intelligent-tiering-optimizes-costs-for-workloads-with-changing-access-patterns/)
- [Using
Amazon FSx with your on-premises data repository](https://docs.aws.amazon.com/fsx/latest/LustreGuide/fsx-on-premises.html)

**related videos:**

- [Storage cost optimization
with Amazon EFS](https://www.youtube.com/watch?v=0nYAwPsYvBo)
- [AWS re:Invent 2023 - What's
new with AWS file storage](https://www.youtube.com/watch?v=yXIeIKlTFV0)
- [AWS re:Invent 2023 - File
storage for builders and data scientists on Amazon Elastic File System](https://www.youtube.com/watch?v=g0f6lrmEyRM)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_data_a7.html*

---

# SUS04-BP07 Minimize data movement across networks

Use shared file systems or object storage to access common data and minimize the total
networking resources required to support data movement for your workload.

**Common anti-patterns:**

- You store all data in the same AWS Region independent of where the data users are.
- You do not optimize data size and format before moving it over the network.

**Benefits of establishing this best practice:** Optimizing data
movement across the network reduces the total networking resources required for the workload and
lowers its environmental impact.

**Level of risk exposed if this best practice is not established:**
Medium

## Implementation guidance

Moving data around your organization requires compute, networking, and storage resources.
Use techniques to minimize data movement and improve the overall efficiency of your workload.

## Implementation steps

- **Use proximity:** Consider proximity to the data or users as a decision factor when [selecting a Region for your workload](https://aws.amazon.com/blogs/architecture/how-to-select-a-region-for-your-workload-based-on-sustainability-goals/).
- **Partition services:** Partition Regionally-consumed services so that their Region-specific data is stored
within the Region where it is consumed.
- **Use efficient file formats:** Use efficient file formats (such as Parquet or ORC) and compress data before you move
it over the network.
- **Minimize data movement:** Don't move unused data. Some examples that can help you avoid moving unused data:

Reduce API responses to only relevant data.
- Aggregate data where detailed (record-level information is not required).
- See [Well-Architected Lab - Optimize Data Pattern Using Amazon Redshift Data Sharing](https://catalog.workshops.aws/well-architected-sustainability/en-US/3-data/optimize-data-pattern-using-redshift-data-sharing).
- Consider [Cross-account data
sharing in AWS Lake Formation](https://docs.aws.amazon.com/lake-formation/latest/dg/cross-account-permissions.html).

- **Use edge services:** Use services that can help you run code closer to users of your workload.

Service
When to use

[Lambda@Edge](https://aws.amazon.com/lambda/edge/)

Use for compute-heavy operations that are run when objects are not in the
cache.

[CloudFront
Functions](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-functions.html)

Use for simple use cases such as HTTP(s) request/response manipulations that
can be initiated by short-lived functions.

[AWS IoT Greengrass](https://aws.amazon.com/greengrass/)

Run local compute, messaging, and data caching for connected devices.

## Resources

**Related documents:**

- [Optimizing your AWS Infrastructure for Sustainability, Part III: Networking](https://aws.amazon.com/blogs/architecture/optimizing-your-aws-infrastructure-for-sustainability-part-iii-networking/)
- [AWS Global
Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/)
- [Amazon CloudFront Key Features including the
CloudFront Global Edge Network](https://aws.amazon.com/cloudfront/features/)
- [Compressing HTTP requests in Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/gzip.html)
- [Intermediate data compression with Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-output-compression.html#HadoopIntermediateDataCompression)
- [Loading
compressed data files from Amazon S3 into Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/dg/t_loading-gzip-compressed-data-files-from-S3.html)
- [Serving compressed
files with Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/ServingCompressedFiles.html)

**Related videos:**

- [Demystifying data transfer
on AWS](https://www.youtube.com/watch?v=-MqXgzw1IGA)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_data_a8.html*

---

# SUS04-BP08 Back up data only when difficult to recreate

Avoid backing up data that has no business value to minimize storage resources requirements
for your workload.

**Common anti-patterns:**

- You do not have a backup strategy for your data.
- You back up data that can be easily recreated.

**Benefits of establishing this best practice:** Avoiding back-up
of non-critical data reduces the required storage resources for the workload and lowers its
environmental impact.

**Level of risk exposed if this best practice is not established:**
Medium

## Implementation guidance

Avoiding the back up of unnecessary data can help lower cost and reduce the storage
resources used by the workload. Only back up data that has business value or is needed to
satisfy compliance requirements. Examine backup policies and exclude ephemeral storage that
doesn’t provide value in a recovery scenario.

### Implementation steps

- **Classify data:** Implement data classification policy as outlined in [SUS04-BP01 Implement a data classification policy](./sus_sus_data_a2.html).
- **Design a backup strategy:** Use the criticality of your data classification and design backup strategy based on
your [recovery time objective (RTO) and recovery point objective (RPO](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_planning_for_recovery_objective_defined_recovery.html)). Avoid backing
up non-critical data.

Exclude data that can be easily recreated.
- Exclude ephemeral data from your backups.
- Exclude local copies of data, unless the time required to restore that data from
a common location exceeds your service-level agreements (SLAs).

- **Use automated backup:** Use an automated solution or managed service to back up business-critical data.

[AWS Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html) is a fully-managed service that makes it easy to centralize and
automate data protection across AWS services, in the cloud, and on premises. For
hands-on guidance on how to create automated backups using AWS Backup, see [Well-Architected Labs - Testing Backup and Restore of Data](https://catalog.workshops.aws/well-architected-reliability/en-US/4-failure-management/1-backup/30-testing-backup-and-restore-of-data).
- [Automate backups and optimize backup costs for Amazon EFS using AWS Backup](https://aws.amazon.com/blogs/storage/automating-backups-and-optimizing-backup-costs-for-amazon-efs-using-aws-backup/).

## Resources

**Related best practices:**

- [REL09-BP01 Identify and back up all data that needs to be backed up, or reproduce the
data from sources](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_backing_up_data_identified_backups_data.html)
- [REL09-BP03 Perform data backup automatically](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_backing_up_data_automated_backups_data.html)
- [REL13-BP02 Use defined recovery strategies to meet the recovery
objectives](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_planning_for_recovery_disaster_recovery.html)

**Related documents:**

- [Using AWS Backup to back up
and restore Amazon EFS file systems](https://docs.aws.amazon.com/efs/latest/ug/awsbackup.html)
- [Amazon EBS
snapshots](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSSnapshots.html)
- [Working with
backups on Amazon Relational Database Service](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.html)
- [APN
Partner: partners that can help with backup](https://partners.amazonaws.com/search/partners?keyword=Backup)
- [AWS Marketplace: products that can be used for backup](https://aws.amazon.com/marketplace/search/results?searchTerms=Backup)
- [Backing Up
Amazon EFS](https://docs.aws.amazon.com/efs/latest/ug/efs-backup-solutions.html)
- [Backing
Up Amazon FSx for Windows File Server](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/using-backups.html)
- [Backup
and Restore for Amazon ElastiCache (Redis OSS)](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/backups.html)

**Related videos:**

- [AWS re:Invent 2023 -
Backup and disaster recovery strategies for increased resilience](https://www.youtube.com/watch?v=E073XISxrSU)
- [AWS re:Invent 2023 - What's
new with AWS Backup](https://www.youtube.com/watch?v=QIffkOyTf7I)
- [AWS re:Invent 2021 -
Backup, disaster recovery, and ransomware protection with AWS](https://www.youtube.com/watch?v=Ru4jxh9qazc)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_data_a9.html*

---

---

## Question SUS05

# SUS 5 — How do you select and use cloud hardware and services to support your sustainability goals?

**Pillar**: Sustainability  
**Best Practices**: 4

---

# SUS05-BP01 Use the minimum amount of hardware to meet your needs

Use the minimum amount of hardware for your workload to efficiently meet your business
needs.

**Common anti-patterns:**

- You do not monitor resource utilization.
- You have resources with a low utilization level in your architecture.
- You do not review the utilization of static hardware to determine if it should be
resized.
- You do not set hardware utilization goals for your compute infrastructure based on
business KPIs.

**Benefits of establishing this best practice:** Rightsizing your
cloud resources helps to reduce a workload’s environmental impact, save money, and maintain
performance benchmarks.

**Level of risk exposed if this best practice is not established:**
Medium

## Implementation guidance

Optimally select the total number of hardware required for your workload to improve its
overall efficiency. The AWS Cloud provides the flexibility to expand or reduce the number of
resources dynamically through a variety of mechanisms, such as [AWS Auto Scaling](https://aws.amazon.com/autoscaling/), and meet changes in demand. It also provides [APIs and SDKs](https://aws.amazon.com/developer/tools/) that allow resources to be
modified with minimal effort. Use these capabilities to make frequent changes to your workload
implementations. Additionally, use rightsizing guidelines from AWS tools to efficiently
operate your cloud resource and meet your business needs.

**Implementation steps**

- **Choose the instances type:** Choose the right instances
type to best fit your needs. To learn about how to choose Amazon Elastic Compute Cloud instances and use
mechanisms such as attribute-based instance selection, see the following:

[How do
I choose the appropriate Amazon EC2 instance type for my workload?](https://aws.amazon.com/premiumsupport/knowledge-center/ec2-instance-choose-type-for-workload/)
- [Attribute-based instance type selection for Amazon EC2 Fleet.](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-fleet-attribute-based-instance-type-selection.html)
- [Create
an Auto Scaling group using attribute-based instance type selection.](https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-asg-instance-type-requirements.html)

- **Scale:** Use small increments to scale variable
workloads.
- **Use multiple compute purchase options:** Balance
instance flexibility, scalability, and cost savings with multiple compute purchase
options.

[Amazon EC2 On-Demand Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-on-demand-instances.html) are best suited for new, stateful, and spiky
workloads which can’t be instance type, location, or time flexible.
- [Amazon EC2 Spot Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html) are a great way to supplement the other options for
applications that are fault tolerant and flexible.
- Leverage [Compute
Savings Plans](https://aws.amazon.com/savingsplans/compute-pricing/) for steady state workloads that allow flexibility if your
needs (like AZ, Region, instance families, or instance types) change.

- **Use instance and Availability Zone diversity:** Maximize
application availability and take advantage of excess capacity by diversifying your
instances and Availability Zones.
- **Rightsize instances:** Use the rightsizing
recommendations from AWS tools to make adjustments on your workload. For more
information, see [Optimizing your cost with Rightsizing Recommendations](https://docs.aws.amazon.com/latest/userguide/ce-rightsizing.html) and [Right
Sizing: Provisioning Instances to Match Workloads](https://docs.aws.amazon.com/latest/cost-optimization-right-sizing/cost-optimization-right-sizing.html)

Use rightsizing recommendations in AWS Cost Explorer or [AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/) to identify rightsizing
opportunities.

- **Negotiate service-level agreements (SLAs):** Negotiate
SLAs that permit temporarily reducing capacity while automation deploys replacement
resources.

## Resources

**Related documents:**

- [Optimizing your AWS Infrastructure for Sustainability, Part I: Compute](https://aws.amazon.com/blogs/architecture/optimizing-your-aws-infrastructure-for-sustainability-part-i-compute/)
- [Attirbute based Instance Type Selection for Auto Scaling for Amazon EC2 Fleet](https://aws.amazon.com/blogs/aws/new-attribute-based-instance-type-selection-for-ec2-auto-scaling-and-ec2-fleet/)
- [AWS Compute Optimizer Documentation](https://docs.aws.amazon.com/compute-optimizer/index.html)
- [Operating Lambda:
Performance optimization](https://aws.amazon.com/blogs/compute/operating-lambda-performance-optimization-part-2/)
- [Auto Scaling
Documentation](https://docs.aws.amazon.com/autoscaling/index.html)

**Related videos:**

- [AWS re:Invent 2023 - What's
new with Amazon EC2](https://www.youtube.com/watch?v=mjHw_wgJJ5g)
- [AWS re:Invent 2023 - Smart
savings: Amazon Elastic Compute Cloud cost-optimization strategies](https://www.youtube.com/watch?v=_AHPbxzIGV0)
- [AWS re:Invent 2022 -
Optimizing Amazon Elastic Kubernetes Service for performance and cost on AWS](https://www.youtube.com/watch?v=5B4-s_ivn1o)
- [AWS re:Invent 2023 -
Sustainable compute: reducing costs and carbon emissions with AWS](https://www.youtube.com/watch?v=0Bl1SDU2HxI)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_hardware_a2.html*

---

# SUS05-BP02 Use instance types with the least impact

Continually monitor and use new instance types to take advantage of energy efficiency
improvements.

**Common anti-patterns:**

- You are only using one family of instances.
- You are only using x86 instances.
- You specify one instance type in your Amazon EC2 Auto Scaling configuration.
- You use AWS instances in a manner that they were not designed for (for example, you
use compute-optimized instances for a memory-intensive workload).
- You do not evaluate new instance types regularly.
- You do not check recommendations from AWS rightsizing tools such as [AWS Compute Optimizer.](https://aws.amazon.com/compute-optimizer/)

**Benefits of establishing this best practice:** By using
energy-efficient and right-sized instances, you are able to greatly reduce the environmental
impact and cost of your workload.

**Level of risk exposed if this best practice is not established:**
Medium

## Implementation guidance

Using efficient instances in cloud workload is crucial for lower resource usage and
cost-effectiveness. Continually monitor the release of new instance types and take advantage
of energy efficiency improvements, including those instance types designed to support specific
workloads such as machine learning training and inference, and video transcoding.

## Implementation steps

- **Learn and explore instance types:** Find instance types
that can lower your workload's environmental impact.

Subscribe to [What's New with AWS](https://aws.amazon.com/new/) to
stay up-to-date with the latest AWS technologies and instances.
- Learn about different AWS instance types.
- Learn about AWS Graviton-based instances which offer the best performance per
watt of energy use in Amazon EC2 by watching [re:Invent 2020 - Deep dive on
AWS Graviton2 processor-powered Amazon EC2 instances](https://www.youtube.com/watch?v=NLysl0QvqXU) and [Deep dive
into AWS Graviton3 and Amazon EC2 C7g instances](https://www.youtube.com/watch?v=WDKwwFQKfSI&ab_channel=AWSEvents).

- **Use instance types with the least impact:** Plan and
transition your workload to instance types with the least impact.

Define a process to evaluate new features or instances for your workload. Take
advantage of agility in the cloud to quickly test how new instance types can improve
your workload environmental sustainability. Use proxy metrics to measure how many
resources it takes you to complete a unit of work.
- If possible, modify your workload to work with different numbers of vCPUs and
different amounts of memory to maximize your choice of instance type.
- Consider transitioning your workload to Graviton-based instances to improve the
performance efficiency of your workload. For more information on moving workloads to
AWS Graviton, see [AWS
Graviton Fast Start](https://aws.amazon.com/ec2/graviton/fast-start/) and [Considerations when transitioning workloads to AWS Graviton-based Amazon Elastic Compute Cloud
instances](https://github.com/aws/aws-graviton-getting-started/blob/main/transition-guide.md).
- Consider selecting the AWS Graviton option in your usage of [AWS managed services.](https://github.com/aws/aws-graviton-getting-started/blob/main/managed_services.md)
- Migrate your workload to Regions that offer instances with the least
sustainability impact and still meet your business requirements.
- For machine learning workloads, take advantage of purpose-built hardware that is
specific to your workload such as [AWS Trainium](https://aws.amazon.com/machine-learning/trainium/), [AWS Inferentia](https://aws.amazon.com/machine-learning/inferentia/), and [Amazon EC2 DL1.](https://aws.amazon.com/ec2/instance-types/dl1/) AWS Inferentia
instances such as Inf2 instances offer up to 50% better performance per watt over
comparable Amazon EC2 instances.
- Use [Amazon SageMaker AI Inference
Recommender](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-recommender.html) to right size ML inference endpoint.
- For spiky workloads (workloads with infrequent requirements for additional
capacity), use [burstable
performance instances.](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/burstable-performance-instances.html)
- For stateless and fault-tolerant workloads, use [Amazon EC2 Spot Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html)
to increase overall utilization of the cloud, and reduce the sustainability impact of
unused resources.

- **Operate and optimize:** Operate and optimize your
workload instance.

For ephemeral workloads, evaluate [instance Amazon CloudWatch metrics](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/viewing_metrics_with_cloudwatch.html#ec2-cloudwatch-metrics) such as `CPUUtilization` to identify
if the instance is idle or under-utilized.
- For stable workloads, check AWS rightsizing tools such as [AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/) at regular intervals to
identify opportunities to optimize and right-size the instances. For further examples and recommendations, see the following labs:

[Well-Architected Lab - Rightsizing Recommendations](https://catalog.workshops.aws/well-architected-cost-optimization/en-US/3-cost-effective-resources/40-rightsizing-recommendations-100)
- [Well-Architected Lab - Rightsizing with Compute Optimizer](https://catalog.workshops.aws/well-architected-cost-optimization/en-US/3-cost-effective-resources/50-rightsizing-recommendations-200)
- [Well-Architected Lab - Optimize Hardware Patterns and Observice Sustainability
KPIs](https://catalog.workshops.aws/well-architected-sustainability/en-US/4-hardware-and-services/optimize-hardware-patterns-observe-sustainability-kpis)

## Resources

**Related documents:**

- [Optimizing your AWS Infrastructure for Sustainability, Part I: Compute](https://aws.amazon.com/blogs/architecture/optimizing-your-aws-infrastructure-for-sustainability-part-i-compute/)
- [AWS Graviton](https://aws.amazon.com/ec2/graviton/)
- [Amazon EC2 DL1](https://aws.amazon.com/ec2/instance-types/dl1/)
- [Amazon EC2 Capacity
Reservation Fleets](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/cr-fleets.html)
- [Amazon EC2 Spot
Fleet](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-fleet.html)
- [Functions: Lambda
Function Configuration](https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html#function-configuration)
- [Attribute-based instance type selection for Amazon EC2 Fleet](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-fleet-attribute-based-instance-type-selection.html)
- [Building Sustainable, Efficient, and Cost-Optimized Applications on
AWS](https://aws.amazon.com/blogs/compute/building-sustainable-efficient-and-cost-optimized-applications-on-aws/)
- [How the Contino Sustainability Dashboard Helps Customers Optimize Their Carbon
Footprint](https://aws.amazon.com/blogs/apn/how-the-contino-sustainability-dashboard-helps-customers-optimize-their-carbon-footprint/)

**Related videos:**

- [AWS re:Invent 2023 - AWS
Graviton: The best price performance for your AWS workloads](https://www.youtube.com/watch?v=T_hMIjKtSr4)
- [AWS re:Invent 2023 - New
Amazon Elastic Compute Cloud generative AI capabilities in AWS Management Console](https://www.youtube.com/watch?v=sSpJ8tWCEiA)
- [AWS re:Invent 2023 = What's new
with Amazon Elastic Compute Cloud](https://www.youtube.com/watch?v=mjHw_wgJJ5g)
- [AWS re:Invent 2023 - Smart
savings: Amazon Elastic Compute Cloud cost-optimization strategies](https://www.youtube.com/watch?v=_AHPbxzIGV0)
- [AWS
re:Invent 2021 - Deep dive into AWS Graviton3 and Amazon EC2 C7g instances](https://www.youtube.com/watch?v=WDKwwFQKfSI&ab_channel=AWSEvents)
- [AWS re:Invent 2022 - Build
a cost-, energy-, and resource-efficient compute environment](https://www.youtube.com/watch?v=8zsC5e1eLCg)

**Related examples:**

- [Solution: Guidance for Optimizing Deep Learning Workloads for Sustainability on AWS](https://aws.amazon.com/solutions/guidance/optimizing-deep-learning-workloads-for-sustainability-on-aws/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_hardware_a3.html*

---

# SUS05-BP03 Use managed services

Use managed services to operate more efficiently in the cloud.

**Common anti-patterns:**

- You use Amazon EC2 instances with low utilization to run your applications.
- Your in-house team only manages the workload, without time to focus on innovation or
simplifications.
- You deploy and maintain technologies for tasks that can run more efficiently on managed
services.

**Benefits of establishing this best practice:**

- Using managed services shifts the responsibility to AWS, which has insights across
millions of customers that can help drive new innovations and efficiencies.
- Managed service distributes the environmental impact of the service across many users
because of the multi-tenet control planes.

**Level of risk exposed if this best practice is not established:**
Medium

## Implementation guidance

Managed services shift responsibility to AWS for maintaining high utilization and
sustainability optimization of the deployed hardware. Managed services also remove the
operational and administrative burden of maintaining a service, which allows your team to have
more time and focus on innovation.

Review your workload to identify the components that can be replaced by AWS managed
services. For example, [Amazon RDS](https://aws.amazon.com/rds/), [Amazon Redshift](https://aws.amazon.com/redshift/), and [Amazon ElastiCache](https://aws.amazon.com/elasticache/) provide a managed database service. [Amazon Athena](https://aws.amazon.com/athena/), [Amazon EMR](https://aws.amazon.com/emr/), and [Amazon OpenSearch Service](https://aws.amazon.com/opensearch-service/)
provide a managed analytics service.

**Implementation steps**

- **Inventory your workload:** Inventory your workload for
services and components.
- **Identify candidates:** Assess and identify components
that can be replaced by managed services. Here are some examples of when you might
consider using a managed service:

Task
What to use on AWS

Hosting a database

Use managed [Amazon Relational Database Service (Amazon RDS)](https://aws.amazon.com/rds/)
instances instead of maintaining your own Amazon RDS instances on [Amazon Elastic Compute Cloud (Amazon EC2)](https://aws.amazon.com/ec2/).

Hosting a container workload

Use [AWS Fargate](https://aws.amazon.com/fargate/), instead of
implementing your own container infrastructure.

Hosting web apps

Use [AWS Amplify
Hosting](https://aws.amazon.com/amplify/hosting/) as fully managed CI/CD and hosting service for static websites
and server-side rendered web apps.
- **Create a migration plan:** Identify dependencies and
create a migrations plan. Update runbooks and playbooks accordingly.

The [AWS Application Discovery Service](https://aws.amazon.com/application-discovery/)
automatically collects and presents detailed information about application
dependencies and utilization to help you make more informed decisions as you plan your
migration

- **Perform tests** Test the service before migrating to
the managed service.
- **Replace self-hosted services:** Use your migration plan
to replace self-hosted services with managed service.
- **Monitor and adjust:** Continually monitor the service
after the migration is complete to make adjustments as required and optimize the service.

## Resources

**Related documents:**

- [AWS Cloud Products](https://aws.amazon.com/products/)
- [AWS Total Cost of Ownership (TCO) Calculator](https://calculator.aws/#/)
- [Amazon DocumentDB](https://aws.amazon.com/documentdb/)
- [Amazon Elastic Kubernetes Service (EKS)](https://aws.amazon.com/eks/)
- [Amazon Managed Streaming for Apache Kafka (Amazon MSK)](https://aws.amazon.com/msk/)

**Related videos:**

- [AWS re:Invent 2021 - Cloud
operations at scale with AWS Managed Services](https://www.youtube.com/watch?v=OCK8GCImWZw)
- [AWS re:Invent 2023 - Best
practices for operating on AWS](https://www.youtube.com/watch?v=XBKq2JXWsS4)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_hardware_a4.html*

---

# SUS05-BP04 Optimize your use of hardware-based compute accelerators

Optimize your use of accelerated computing instances to reduce the physical infrastructure
demands of your workload.

**Common anti-patterns:**

- You are not monitoring GPU usage.
- You are using a general-purpose instance for workload while a purpose-built instance
can deliver higher performance, lower cost, and better performance per watt.
- You are using hardware-based compute accelerators for tasks where they’re more
efficient using CPU-based alternatives.

**Benefits of establishing this best practice:** By optimizing the
use of hardware-based accelerators, you can reduce the physical-infrastructure demands of your
workload.

**Level of risk exposed if this best practice is not established:**
Medium

## Implementation guidance

If you require high processing capability, you can benefit from using accelerated
computing instances, which provide access to hardware-based compute accelerators such as
graphics processing units (GPUs) and field programmable gate arrays (FPGAs). These hardware
accelerators perform certain functions like graphic processing or data pattern matching more
efficiently than CPU-based alternatives. Many accelerated workloads, such as rendering,
transcoding, and machine learning, are highly variable in terms of resource usage. Only run
this hardware for the time needed, and decommission them with automation when not required to
minimize resources consumed.

## Implementation steps

- **Explore compute accelerators:** Identify which [accelerated computing
instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/accelerated-computing-instances.html) can address your requirements.
- **Use purpose-built hardware:** For machine learning workloads, take advantage of purpose-built hardware that is
specific to your workload, such as [AWS Trainium](https://aws.amazon.com/machine-learning/trainium/), [AWS Inferentia](https://aws.amazon.com/machine-learning/inferentia/), and [Amazon EC2 DL1](https://aws.amazon.com/ec2/instance-types/dl1/). AWS Inferentia instances such as Inf2
instances offer up to [50%
better performance per watt over comparable Amazon EC2 instances](https://aws.amazon.com/machine-learning/inferentia/).
- **Monitor usage metrics:** Collect usage metric for your accelerated computing instances. For example, you can
use CloudWatch agent to collect metrics such as `utilization_gpu` and
`utilization_memory` for your GPUs as shown in [Collect NVIDIA
GPU metrics with Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Agent-NVIDIA-GPU.html).
- **Rightsize:** Optimize the code, network operation, and settings of hardware accelerators to make
sure that underlying hardware is fully utilized.

[Optimize
GPU settings](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/optimize_gpu.html)
- [GPU
Monitoring and Optimization in the Deep Learning AMI](https://docs.aws.amazon.com/dlami/latest/devguide/tutorial-gpu.html)
- [Optimizing I/O for GPU performance tuning of deep learning training in
Amazon SageMaker AI](https://aws.amazon.com/blogs/machine-learning/optimizing-i-o-for-gpu-performance-tuning-of-deep-learning-training-in-amazon-sagemaker/)

- **Keep up to date:** Use the latest high performant libraries and GPU drivers.
- **Release unneeded instances:** Use automation to release GPU instances when not in use.

## Resources

**Related documents:**

- [Accelerated
Computing](https://aws.amazon.com/ec2/instance-types/#Accelerated_Computing)
- [Let's Architect!
Architecting with custom chips and accelerators](https://aws.amazon.com/blogs/architecture/lets-architect-custom-chips-and-accelerators/)
- [How do I
choose the appropriate Amazon EC2 instance type for my workload?](https://aws.amazon.com/premiumsupport/knowledge-center/ec2-instance-choose-type-for-workload/)
- [Amazon EC2 VT1 Instances](https://aws.amazon.com/ec2/instance-types/vt1/)
- [Choose the best AI accelerator and model compilation for computer vision inference
with Amazon SageMaker AI](https://aws.amazon.com/blogs/machine-learning/choose-the-best-ai-accelerator-and-model-compilation-for-computer-vision-inference-with-amazon-sagemaker/)

**Related videos:**

- [AWS re:Invent 2021 - How
to select Amazon EC2 GPU instances for deep learning](https://www.youtube.com/watch?v=4bVrIbgGWEA)
- [AWS Online Tech Talks -
Deploying Cost-Effective Deep Learning Inference](https://www.youtube.com/watch?v=WiCougIDRsw)
- [AWS re:Invent 2023 -
Cutting-edge AI with AWS and NVIDIA](https://www.youtube.com/watch?v=ud4-z_sb_ps)
- [AWS re:Invent 2022 - [NEW
LAUNCH!] Introducing AWS Inferentia2-based Amazon EC2 Inf2 instances](https://www.youtube.com/watch?v=jpqiG02Y2H4)
- [AWS re:Invent 2022 -
Accelerate deep learning and innovate faster with AWS Trainium](https://www.youtube.com/watch?v=YRqvfNwqUIA)
- [AWS re:Invent 2022 - Deep
learning on AWS with NVIDIA: From training to deployment](https://www.youtube.com/watch?v=l8AFfaCkp0E)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_hardware_a5.html*

---

---

## Question SUS06

# SUS 6 — How do your organizational processes support your sustainability goals?

**Pillar**: Sustainability  
**Best Practices**: 5

---

# SUS06-BP01 Communicate and cascade your sustainability goals

Technology is a key enabler of sustainability. IT teams play a
crucial role in driving meaningful change towards your
organization's sustainability goals. These teams should clearly
understand the company's sustainability targets and work to
communicate and cascade those priorities across its operations.

**Common anti-patterns:**

- You don't know your organization's sustainability goals and how
they apply to your team.
- You have insufficient awareness and training about the
environmental impact of cloud workloads.
- You are unsure about the specific areas to prioritize.
- You do not involve your employees and customers in your
sustainability initiatives.

**Benefits of establishing this best
practice:** From optimization of infrastructure and systems
to use of innovative technologies, IT teams can reduce the
organization's carbon emissions and minimize resource consumption.
Communication of sustainability goals can provide the ability for IT
teams continuously improve and adapt to evolving sustainability
challenges. Additionally, these sustainable optimizations often
translate to cost savings as well, which strengthens the business
case.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

The primary sustainability goals for IT teams should be to
optimize systems and solutions to increase resource efficiency and
minimize the organization's carbon footprint and overall
environmental impact. Shared services and initiatives like
training programs and operational dashboards can support
organizations as they optimize IT operations and build solutions
that can help significantly reduce the carbon footprint. The cloud
presents an opportunity not only to move physical infrastructure
and energy procurement responsibilities to the shared
responsibility of the cloud provider but also to continuously
optimize the resource efficiency of cloud-based services.

When teams use the cloud's inherent efficiency and shared
responsibility model, they can drive meaningful reductions in the
organization's environmental impact. This, in turn, can contribute
to the organization's overall sustainability goals and demonstrate
the value of these teams as strategic partners in the journey
towards a more sustainable future.

### Implementation steps

- **Define goals and
objectives:** Establish well-defined goals for your IT program. This involves getting input from
responsible stakeholders from different departments such as
IT, sustainability, and finance. These teams should define
measurable goals that align with your organization's
sustainability goals, including areas such carbon reduction
and resource optimization.
- **Understand the carbon accounting
boundaries of your business:** Understand how
carbon accounting methods like the Greenhouse Gas (GHG)
Protocol relate to your workloads in the cloud
(for more detail, see [Cloud
sustainability](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/cloud-sustainability.html)).
- **Use cloud solutions for carbon
accounting:** Use cloud solutions such as
[carbon
accounting solutions on AWS](https://aws.amazon.com/solutions/sustainability/carbon-accounting/) to track scope one, two,
and three for GHG emissions across your operations,
portfolios, and value chains. With these solutions,
organizations can streamline GHG emission data acquisition,
simplify reporting, and derive insights to inform their
climate strategies.
- **Monitor the carbon footprint of your
IT portfolio:** Track and report carbon emissions
of your IT systems. Use the
[AWS Customer Carbon Footprint Tool](https://aws.amazon.com/aws-cost-management/aws-customer-carbon-footprint-tool/) to track, measure,
review, and forecast the carbon emissions generated from
your AWS usage.
- **Communicate resource usage through
proxy metrics to your teams:** Track and report on
your
[resource
usage through proxy metrics](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/evaluate-specific-improvements.html). In the on-demand pricing
models of the cloud, resource usage is related to cost,
which is a generally-understandable metric. At a minimum,
use cost as a proxy metric to communicate the resource usage
and improvements by each team.

**Enable hourly granularity in
your Cost Explorer and create a
[Cost
and Usage Report (CUR)](https://aws.amazon.com/aws-cost-management/aws-cost-and-usage-reporting/):** The CUR
provides daily or hourly usage granularity, rates,
costs, and usage attributes for all AWS services. Use
[the
Cloud Intelligence Dashboards](https://catalog.workshops.aws/awscid/) and its
Sustainability Proxy Metrics Dashboard as a starting
point for the processing and visualization of cost and
usage based data. For more detail, see the following:
- [Measure
and track cloud efficiency with sustainability proxy
metrics, Part I: What are proxy metrics?](https://aws.amazon.com/blogs/aws-cloud-financial-management/measure-and-track-cloud-efficiency-with-sustainability-proxy-metrics-part-i-what-are-proxy-metrics/)
- [Measure
and track cloud efficiency with sustainability proxy
metrics, Part II: Establish a metrics pipeline](https://aws.amazon.com/blogs/aws-cloud-financial-management/measure-and-track-cloud-efficiency-with-sustainability-proxy-metrics-part-ii-establish-a-metrics-pipeline/)

- **Continuously optimize and
evaluate:** Use an
[improvement
process](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/improvement-process.html) to continuously optimize your IT systems,
including cloud workload for efficiency and sustainability.
Monitor carbon footprint before and after implementation of
optimization strategy. Use the reduction in carbon footprint
to assess the effectiveness.
- **Foster a sustainability
culture:** Use training programs (like
[AWS Skill Builder](https://explore.skillbuilder.aws/learn/external-ecommerce;view=none;redirectURL=?ctldoc-catalog-0=se-sustainability)) to educate your employees about
sustainability. Engage them in sustainability initiatives.
Share and celebrate their success stories. Use incentives to
award them if they achieve sustainability targets.

## Resources

**Related documents:**

- [Understanding
your carbon emission estimations](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/ccft-estimation.html)

**Related videos:**

- [AWS re:Invent 2023 - Accelerate data-driven circular economy
initiatives with AWS](https://www.youtube.com/watch?v=ivTJorpUTo0)
- [AWS re:Invent 2023 - Sustainability innovation in AWS Global
Infrastructure](https://www.youtube.com/watch?v=0EkcwLKeOQA)
- [AWS re:Invent 2023 - Sustainable architecture: Past, present, and
future](https://www.youtube.com/watch?v=2xpUQ-Q4QcM)
- [AWS re:Invent 2022 - Delivering sustainable, high-performing
architectures](https://www.youtube.com/watch?v=FBc9hXQfat0)
- [AWS re:Invent 2022 - Architecting sustainably and reducing your
AWS carbon footprint](https://www.youtube.com/watch?v=jsbamOLpCr8)
- [AWS re:Invent 2022 - Sustainability in AWS global
infrastructure](https://www.youtube.com/watch?v=NgMa8R9-Ywk)

**Related examples:**

- [Well-Architected
Lab - Turning cost & usage reports into efficiency
reports](https://catalog.workshops.aws/well-architected-sustainability/en-US/5-process-and-culture/cur-reports-as-efficiency-reports)

**Related trainings:**

- [Sustainability
Transformation on AWS](https://explore.skillbuilder.aws/learn/course/internal/view/elearning/15981/sustainability-transformation-with-aws?trk=f5740d24-133a-44e7-bdca-e6669e296419&sc_channel=el)
- [SimuLearn
- Sustainability Reporting](https://explore.skillbuilder.aws/learn/course/internal/view/elearning/20240/aws-simulearn-sustainability-reporting)
- [Decarbonization
with AWS](https://explore.skillbuilder.aws/learn/course/internal/view/elearning/19030/decarbonization-with-aws-introduction)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_dev_a1.html*

---

# SUS06-BP02 Adopt methods that can rapidly introduce sustainability improvements

Adopt methods and processes to validate potential improvements,
minimize testing costs, and deliver small improvements.

**Common anti-patterns:**

- Reviewing your application for sustainability is a task done
only once at the beginning of a project.
- Your workload has become stale, as the release process is too
cumbersome to introduce minor changes for resource efficiency.
- You do not have mechanisms to improve your workload for
sustainability.

**Benefits of establishing this best
practice:** By establishing a process to introduce and
track sustainability improvements, you will be able to continually
adopt new features and capabilities, remove issues, and improve
workload efficiency.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Test and validate potential sustainability improvements before
deploying them to production. Account for the cost of testing when
calculating potential future benefit of an improvement. Develop
low cost testing methods to deliver small improvements.

### Implementation steps

- **Understand and communicate your
organizational sustainability goals:** Understand
your organizational sustainability goals, such carbon
reduction or water stewardship. Translate these goals into
sustainability requirements for your cloud workloads.
Communicate these requirements to key stakeholders.
- **Add sustainability requirements to
your backlog:** Add requirements for sustainability
improvement to your development backlog.
- **Iterate and improve:** Use an
[iterative
improvement process](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/improvement-process.html) to identify, evaluate, prioritize,
test, and deploy these improvements.
- **Test using minimum viable product
(MVP):** Develop and test potential improvements
using the minimum viable representative components to reduce
the cost and environmental impact of testing.
- **Streamline the process:**
Continually improve and streamline your development processes.
As an example, Automate your software delivery process using
continuous integration and delivery (CI/CD) pipelines to test
and deploy potential improvements to reduce the level of
effort and limit errors caused by manual processes.
- **Training and awareness:** Run
training programs for your team members to educate them about
sustainability and how their activities impact your
organizational sustainability goals.
- **Assess and adjust:**
Continually assess the impact of improvements and make
adjustments as needed.

## Resources

**Related documents:**

- [AWS enables sustainability solutions](https://aws.amazon.com/sustainability/)

**Related videos:**

- [AWS re:Invent 2023 - Sustainable architecture: Past, present, and
future](https://www.youtube.com/watch?v=2xpUQ-Q4QcM)
- [AWS re:Invent 2022 - Delivering sustainable, high-performing
architectures](https://www.youtube.com/watch?v=FBc9hXQfat0)
- [AWS re:Invent 2022 - Architecting sustainably and reducing your
AWS carbon footprint](https://www.youtube.com/watch?v=jsbamOLpCr8)
- [AWS re:Invent 2022 - Sustainability in AWS global
infrastructure](https://www.youtube.com/watch?v=NgMa8R9-Ywk)
- [AWS re:Invent 2023 - What's new with AWS observability and
operations](https://www.youtube.com/watch?v=E8qQBMDJjso)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_dev_a2.html*

---

# SUS06-BP03 Keep your workload up-to-date

Keep your workload up-to-date to adopt efficient features, remove
issues, and improve the overall efficiency of your workload.

**Common anti-patterns:**

- You assume your current architecture is static and will not be
updated over time.
- You do not have any systems or a regular cadence to evaluate if
updated software and packages are compatible with your workload.

**Benefits of establishing this best
practice:** By establishing a process to keep your workload
up to date, you can adopt new features and capabilities, resolve
issues, and improve workload efficiency.

**Level of risk exposed if this best practice
is not established:** Low

## Implementation guidance

Up to date operating systems, runtimes, middlewares, libraries,
and applications can improve workload efficiency and make it
easier to adopt more efficient technologies. Up to date software
might also include features to measure the sustainability impact
of your workload more accurately, as vendors deliver features to
meet their own sustainability goals. Adopt a regular cadence to
keep your workload up to date with the latest features and
releases.

### Implementation steps

- **Define a process:** Use a
process and schedule to evaluate new features or instances for
your workload. Take advantage of agility in the cloud to
quickly test how new features can improve your workload to:

Reduce sustainability impacts.
- Gain performance efficiencies.
- Remove barriers for a planned improvement.
- Improve your ability to measure and manage sustainability
impacts.

- **Conduct an inventory:**
Inventory your workload software and architecture and identify
components that need to be updated.

You can use
[AWS Systems Manager Inventory](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-inventory.html) to collect operating
system (OS), application, and instance metadata from your
Amazon EC2 instances and quickly understand which
instances are running the software and configurations
required by your software policy and which instances need
to be updated.

- **Learn the update procedure:**
Understand how to update the components of your workload.

Workload component

How to update

Machine images

Use
[EC2 Image Builder](https://aws.amazon.com/image-builder/) to manage updates to
[Amazon
Machine Images (AMIs)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html) for Linux or Windows server
images.

Container images

Use
[Amazon Elastic Container Registry (Amazon ECR)](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html) with your
existing pipeline to
[manage
Amazon Elastic Container Service (Amazon ECS)
images](https://docs.aws.amazon.com/AmazonECR/latest/userguide/ECR_on_ECS.html).

AWS Lambda

AWS Lambda includes
[version
management features.](https://docs.aws.amazon.com/lambda/latest/dg/configuration-versions.html)

- **Use automation:** Automate
updates to reduce the level of effort to deploy new features
and limit errors caused by manual processes.

You can use
[CI/CD](https://aws.amazon.com/blogs/devops/complete-ci-cd-with-aws-codecommit-aws-codebuild-aws-codedeploy-and-aws-codepipeline/)
to automatically update AMIs, container images, and other
artifacts related to your cloud application.
- You can use tools such as
[AWS Systems Manager Patch Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-patch.html) to automate the
process of system updates, and schedule the activity using
[AWS Systems Manager Maintenance Windows](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-maintenance.html).

## Resources

**Related documents:**

- [AWS Architecture Center](https://aws.amazon.com/architecture)
- [What's
New with AWS](https://aws.amazon.com/new/?ref=wellarchitected&ref=wellarchitected)
- [AWS Developer Tools](https://aws.amazon.com/products/developer-tools/)

**Related videos:**

- [AWS re:Invent 2022 - Optimize your AWS workloads with
best-practice guidance](https://www.youtube.com/watch?v=t8yl1TrnuIk)
- [All
Things Patch: AWS Systems Manager](https://www.youtube.com/watch?v=PhIiVsCEBu8)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_dev_a3.html*

---

# SUS06-BP04 Increase utilization of build environments

Increase the utilization of resources to develop, test, and build
your workloads.

**Common anti-patterns:**

- You manually provision or terminate your build environments.
- You keep your build environments running independent of test,
build, or release activities (for example, running an
environment outside of the working hours of your development
team members).
- You over-provision resources for your build environments.

**Benefits of establishing this best
practice:** By increasing the utilization of build
environments, you can improve the overall efficiency of your cloud
workload while allocating the resources to builders to develop,
test, and build efficiently.

**Level of risk exposed if this best practice
is not established:** Low

## Implementation guidance

Use automation and infrastructure-as-code to bring build
environments up when needed and take them down when not used. A
common pattern is to schedule periods of availability that
coincide with the working hours of your development team members.
Your test environments should closely resemble the production
configuration. However, look for opportunities to use instance
types with burst capacity, Amazon EC2 Spot Instances, automatic
scaling database services, containers, and serverless technologies
to align development and test capacity with use. Limit data volume
to just meet the test requirements. If using production data in
test, explore possibilities of sharing data from production and
not moving data across.

**Implementation steps**

- **Use infrastructure as code:**
Use infrastructure as code to provision your build
environments.
- **Use automation:** Use
automation to manage the lifecycle of your development and
test environments and maximize the efficiency of your build
resources.
- **Maximize utilization**: Use
strategies to maximize the utilization of development and test
environments.

Use minimum viable representative environments to develop
and test potential improvements.
- Use serverless technologies if possible.
- Use On-Demand Instances to supplement your developer
devices.
- Use instance types with burst capacity, Spot Instances,
and other technologies to align build capacity with use.
- Adopt native cloud services for secure instance shell
access rather than deploying fleets of bastion hosts.
- Automatically scale your build resources depending on your
build jobs.

## Resources

**Related documents:**

- [AWS Systems Manager Session Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager.html)
- [Amazon EC2 Burstable performance instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/burstable-performance-instances.html)
- [What
is AWS CloudFormation?](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html)
- [What
is AWS CodeBuild?](https://docs.aws.amazon.com/codebuild/latest/userguide/welcome.html)
- [Instance
Scheduler on AWS](https://aws.amazon.com/solutions/implementations/instance-scheduler-on-aws/)

**Related videos:**

- [AWS re:Invent 2023 - Continuous integration and delivery for
AWS](https://www.youtube.com/watch?v=25w9uJPt0SA)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_dev_a4.html*

---

# SUS06-BP05 Use managed device farms for testing

Use managed device farms to efficiently test a new feature on a
representative set of hardware.

**Common anti-patterns:**

- You manually test and deploy your application on individual
physical devices.
- You do not use app testing service to test and interact with
your apps (for example, Android, iOS, and web apps) on real,
physical devices.

**Benefits of establishing this best
practice:** Using managed device farms for testing
cloud-enabled applications provides a number of benefits:

- They include more efficient features to test application on wide
range of devices.
- They eliminate the need for in-house infrastructure for testing.
- They offer diverse device types, including older and less
popular hardware, which eliminates the need for unnecessary
device upgrades.

**Level of risk exposed if this best practice
is not established:** Low

## Implementation guidance

Using Managed device farms can help you to streamline the testing
process for new features on a representative set of hardware.
Managed device farms offer diverse device types including older,
less popular hardware, and avoid customer sustainability impact
from unnecessary device upgrades.

### Implementation steps

- **Define testing
requirements**: Define your testing requirements and
plan (like test type, operating systems, and test schedule).

You can use
[Amazon CloudWatch RUM](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM.html) to collect and analyze client-side
data and shape your testing plan.

- **Select a managed device
farm:** Select a managed device farm that can support
your testing requirements. For example, you can use
[AWS Device Farm](https://docs.aws.amazon.com/devicefarm/latest/developerguide/welcome.html) to test and understand the impact of your
changes on a representative set of hardware.
- **Use automation:** Use
automation and continuous integration/continuous deployment
(CI/CD) to schedule and run your tests.

[Integrating
AWS Device Farm with your CI/CD pipeline to run
cross-browser Selenium tests](https://aws.amazon.com/blogs/devops/integrating-aws-device-farm-with-ci-cd-pipeline-to-run-cross-browser-selenium-tests/)
- [Building
and testing iOS and iPadOS apps with AWS DevOps and mobile
services](https://aws.amazon.com/blogs/devops/building-and-testing-ios-and-ipados-apps-with-aws-devops-and-mobile-services/)

- **Review and adjust:**
Continually review your testing results and make necessary
improvements.

## Resources

**Related documents:**

- [AWS Device Farm
device list](https://awsdevicefarm.info/)
- [Viewing
the CloudWatch RUM dashboard](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-view-data.html)

**Related videos:**

- [AWS re:Invent 2023 - Improve your mobile and web app quality using
AWS Device Farm](https://www.youtube.com/watch?v=__93Tm0YCRg)
- [AWS re:Invent 2021 - Optimize applications through end user
insights with Amazon CloudWatch RUM](https://www.youtube.com/watch?v=NMaeujY9A9Y)

**Related examples:**

- [AWS Device Farm Sample App for Android](https://github.com/aws-samples/aws-device-farm-sample-app-for-android)
- [AWS Device Farm Sample App for iOS](https://github.com/aws-samples/aws-device-farm-sample-app-for-ios)
- [Appium
Web tests for AWS Device Farm](https://github.com/aws-samples/aws-device-farm-sample-web-app-using-appium-python)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_dev_a5.html*

---

---

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
