# Sustainability

**Pages**: 8

---

# Definition

Optimize workload placement, and optimize your architecture for
user, software, data, hardware, and development and deployment
patterns to increase energy efficiency. Each of these areas
represents opportunities to employ best practices to reduce the
sustainability impact of your cloud workload by maximizing
utilization, and minimizing waste and the total resources
deployed and powered to support your workload.

- Region selection
- User behavior patterns
- Software and architecture patterns
- Data patterns
- Hardware patterns
- Development and deployment patterns

*Source: https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/sus-definition.html*

---

# Region selection

There are no sustainability practices unique to SaaS applications.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/region-selection.html*

---

# User behavior patterns

SaaS SUS 3: Do you have a tenant off-boarding plan for inactive tenants? How
do you decommission tenant resources that are not being used to limit or prevent
waste?

Each tenant in the SaaS solution has a footprint that includes infrastructure resources
such as compute, storage, and relevant data. When a tenant decides to off-board (stop using
the SaaS solution), the respective tenant’s footprint should be decommissioned when there is
no expectation that the tenant is likely to be re-activated. The faster unused resources can
be decommissioned (such as by automating the
process), the lower the impact, as decommissioned resources equate to energy saved. Since
this process involves data archiving or deletion, it should be described as part of the service level
agreement (SLA).

- **Best Practice–01:** Keep an updated list of
infrastructure resources allocated per tenant.
- **Best Practice–02:** Maintain a runbook with a list of
steps required to off-board a tenant, and periodically test it in non-production
environment to help ensure it’s current.
- **Best Practice–03:** Use automation tools to run
decommissioning steps to avoid human errors, and speed up the run time.
This process should not affect the performance of active tenants.
- **Best Practice–04:** Before decommissioning, the SaaS
provider should ensure, if required, that a copy of the data is created to meet any
audit or compliance requirements, and to restore or reactivate the tenant in the future.
- **Best Practice–05:** Start automated decommissioning
processes as part of a process approval system, such as a ServiceNow-approved workflow.
- **Best Practice–06:** Use auto-scaling to remove capacity
as demand change.

**AWS services recommendation:**

- [AWS Systems Manager
Inventory](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-inventory.html) provides visibility into your AWS computing environment.
- [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html) provides a detailed view of the configuration of AWS resources in
your AWS account. This includes how the resources are related to one another and how
they were configured in the past so that you can see how the configurations and
relationships change over time.
- [AWS Cost and
Usage Report](https://docs.aws.amazon.com/cur/latest/userguide/what-is-cur.html) (CUR) with [resource tags](https://docs.aws.amazon.com/cur/latest/userguide/resource-tags-columns.html)— You can
use the resource columns in AWS Cost and Usage Reports to find information about the
specific resources covered by a line item. These columns include user-defined cost
allocation tags.
- [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-guide.html) templates describe your desired resources and their dependencies so
that you can launch and configure them together as a stack. You can use a template to
create, update, and delete an entire stack as a single unit, as often as you need to,
instead of managing resources individually.
- [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html) provides serverless orchestration for modern applications.
Orchestration centrally manages a workflow by breaking it into multiple steps, adding
flow logic, and tracking the inputs and outputs between the steps.
- [Amazon S3
Inventory](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-inventory.html) provides comma-separated values (CSV), Apache optimized row columnar
(ORC), or Apache Parquet output files that list your objects and their corresponding
metadata on a daily or weekly basis for an S3 bucket or a shared prefix (that is,
objects that have names that begin with a common string).
- [Amazon S3 storage classes](https://aws.amazon.com/s3/storage-classes/) (and the
Amazon Glacier classes in particular) can be used to store or archive a tenant’s data for
long-term retention and with reduced energy consumption.
- [Amazon EC2 Auto Scaling](https://aws.amazon.com/ec2/autoscaling/) and  [Application Auto Scaling](https://docs.aws.amazon.com/autoscaling/application/userguide/what-is-application-auto-scaling.html) can help you make smart scaling decisions.
- [Quick](https://aws.amazon.com/quicksight/features/) provides you with data
driven analysis and visualization.

SaaS SUS 4: How do you provide per-tenant footprint visibility (such as
resource utilization and carbon emission data) in your SaaS environment?

Reflecting the consumption level per tenant creates awareness, visibility into the SaaS
solutions’ customers sustainability footprint, and improvement process.

- **Best Practice–01:** Instrument your SaaS application to
collect metrics at a per-tenant level. The goal is to accurately capture all the
activities and consumption patterns of each tenant in your system.
- **Best Practice–02:** Use application and system monitoring
tools to identify infrastructure usage patterns on a per-tenant basis. This data must
contain information that ties it back to the tenant.
- **Best Practice–03:** Provide detailed dashboards and
visualizations of per-tenant operational data across the different layers of the SaaS
solution. This data includes total compute required, such as CPU and memory usage, total
data transfer and network costs, and total data and storage costs. The goal is to create
a unified view of the per-tenant footprint, which provides useful operational insights
in to your SaaS environment.

**AWS services recommendation:**

- AWS SaaS Lens guidance on [Tenant-aware
Operations](https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/tenant-aware-operations.html)— SaaS providers need to be able to view system activity and health
through the lens of individual tenants and tenant tiers. This is essential to diagnosing
and evaluating the trends and patterns of activity and consumption for individual
tenants.
- AWS SaaS guidance on [Tenant
Activity and Consumption](https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/tenant-activity-and-consumption.html)—Provide visibility into how tenants are using your
application and imposing load on your system’s architecture.
- [Amazon Cloudwatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/working_with_metrics.html) and tools from AWS Partners such as DataDog or New Relic
can be used to capture and surface per-tenant metrics and consumption data.
- [AWS Systems Manager
Inventory](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-inventory.html) provides visibility into your AWS compute environment.
- [AWS Cost and
Usage Reports](https://docs.aws.amazon.com/cur/latest/userguide/what-is-cur.html) (AWS CUR) with [resource tags](https://docs.aws.amazon.com/cur/latest/userguide/resource-tags-columns.html)— You can
use the resource columns in AWS CUR to find information about the specific resources
covered by a line item. These columns include user-defined cost allocation tags.
- Tracking SaaS resource and consumption—[This presentation](https://www.slideshare.net/AmazonWebServices/gpstec309saas-monitoring-creating-a-unified-view-of-multitenant-health-featuring-new-relic) goes through the best practices for capturing and surfacing
tenant level consumption patterns using an AWS partner solution.
- Use the [AWS Customer Carbon
Footprint Tool](https://aws.amazon.com/aws-cost-management/aws-customer-carbon-footprint-tool/)to track, measure, review, and forecast the carbon emissions
generated from your AWS usage.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/user-behavior-patterns.html*

---

# Software and architecture patterns

SaaS SUS 1: How do you use deployment models (silo, bridge, pool)
to align tenant consumption with resource utilization?

- **Best Practice–01:** Have a good understanding of the key
value and principles behind the silo, pool, and bridge models, including awareness how silo
and pool strategies can be applied more granularly across the layers and services of your solution.
- **Best Practice–02:** Understand the operational tradeoffs
of each model. Build a unified onboarding, operations, and analytics experience spanning
any of these models.
- **Best Practice–03:** Have a complete end-to-end automated
tenant onboarding process that maps the tenancy models to the resources that are
provisioned at each architecture layer or component. Also have detailed insights into
the footprint and consumption costs and tradeoffs associated with each of these models

SaaS applications can be built using a variety of different architectural models.
Regulatory, competitive, strategic, cost efficiency, and market considerations all influence
the shape of your SaaS architecture. At the same time, there are strategies and patterns
that can be applied when defining the footprint of the components within a SaaS application.
These patterns—silo, bridge, and pool—can be applied in combinations to enable the most
efficient consumption of infrastructure resources.

**AWS services recommendation:**

- AWS WA SaaS Lens guidance on [Architectural
model](https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/silo-pool-and-bridge-models.html)
- [SaaS Tenant Isolation Strategies whitepaper](https://docs.aws.amazon.com/whitepapers/latest/saas-tenant-isolation-strategies/saas-tenant-isolation-strategies.html)
- Amazon EKS SaaS reference solution [https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/amazon-eks-saas.html](https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/amazon-eks-saas.html)
- Serverless SaaS reference solution [https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/serverless-saas.html](https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/serverless-saas.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/software-and-architecture-patterns.html*

---

# Data patterns

There are no sustainability practices unique to SaaS
applications.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/data-patterns.html*

---

# Hardware patterns

SaaS SUS 2: How do you maximize the value from the resources that the SaaS
environment consumes?

SaaS, by its nature, tries to promote the sharing of infrastructure across tenants to maximize
efficiency and economies of scale. SaaS providers should continually evaluate their opportunities
to maximize infrastructure sharing to promote reduced energy consumption. SaaS providers should
have an iterative improvement process that allows them to identify opportunities to limit
excess resource consumption.

- **Best Practice–01:** Use managed services to shift the
responsibility for maintaining optimal utilization of the deployed hardware to AWS.
- **Best Practice–02:** Right-size compute resources based on
your architecture and iteratively optimize by tracking utilization, and use auto-scaling
to handle peak system load.
- **Best Practice–03:** Use serverless computing and other
managed services to automatically scale resources as needed, eliminates tasks for
infrastructure provisioning and management, and resources utilization is optimized.

**AWS services recommendation:**

- [AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/index.html) analyzes
the configuration and utilization metrics of your AWS resources. It reports whether
your resources are optimal, and generates optimization recommendations.
- [Amazon CloudWatch metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/working_with_metrics.html) provide data about the performance of your system, for
example, CPU utilization.
- [Auto Scaling](https://docs.aws.amazon.com/autoscaling/index.html)—AWS
provides multiple services that you can use to scale your application.
- Examples of AWS managed services:

[Amazon Relational Database Service (Amazon RDS)](https://aws.amazon.com/rds/)
- [AWS Fargate](https://aws.amazon.com/fargate/)
- [Amazon Redshift](https://aws.amazon.com/redshift/)
- [Amazon Managed Streaming for Apache Kafka (Amazon MSK)](https://aws.amazon.com/msk/)
- [Amazon DynamoDB](https://aws.amazon.com/dynamodb/)
- [Amazon Elastic Kubernetes Service (Amazon EKS)](https://aws.amazon.com/eks/)

- [Lab—Rightsizing Recommendations](https://wellarchitectedlabs.com/cost/100_labs/100_aws_resource_optimization/)
- [Serverless on AWS](https://aws.amazon.com/serverless/) helps you build
and run applications without thinking about servers, capacity sizing and provisioning,
and maintenance.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/hardware-patterns.html*

---

# Development and deployment patterns

There are no sustainability practices unique to SaaS
applications.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/development-and-deployment-patterns.html*

---

# Resources

Refer to the following resources to learn more about AWS best practices for sustainability.

**Documentation and blogs**

- [Building Sustainable, Efficient, and Cost-Optimized Applications on AWS](https://aws.amazon.com/blogs/compute/building-sustainable-efficient-and-cost-optimized-applications-on-aws/)
- [Optimize your AWS Infrastructure for Sustainability](https://aws.amazon.com/blogs/architecture/optimizing-your-aws-infrastructure-for-sustainability-part-i-compute/) (a three-part blog
series)
- [Best Practices from IBM and AWS for Optimizing SaaS Solutions for
Sustainability](https://aws.amazon.com/blogs/apn/best-practices-from-ibm-and-aws-for-optimizing-saas-solutions-for-sustainability/)
- [Let’s Architect! Architecting for sustainability](https://aws.amazon.com/blogs/architecture/lets-architect-architecting-for-sustainability/)
- [How to select a Region for your workload based on sustainability goals](https://aws.amazon.com/blogs/architecture/how-to-select-a-region-for-your-workload-based-on-sustainability-goals/)

**Labs**

- [AWS Well-Architected Labs
for Sustainability Pillar](https://wellarchitectedlabs.com/sustainability/)
- [AWS
Well-Architected Labs – Cloud Intelligence Dashboards](https://wellarchitectedlabs.com/cost/200_labs/200_cloud_intelligence/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/saas-lens/sus-resources.html*

---

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
