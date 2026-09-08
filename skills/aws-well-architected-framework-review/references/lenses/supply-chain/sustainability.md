# Sustainability

**Pillar**: Sustainability  
**Questions**: 10

---

# SCSUS01 — Region selection

**Pillar**: Sustainability  
**Best Practices**: 1

---

# SCSUS01-BP01 Optimize your visibility over the entire supply chain network

Verify consistent visibility of your supply chain workloads across
the entire supply chain network. The goal is to collect
information on where workloads are running and how much resources
they require to fulfill business needs. Reaching this level of
visibility enables organizations to look for optimal AWS Regions,
from both business efficiency and sustainability needs standpoint,
where workloads can or should run to match service levels and
sustainability targets.

**Desired outcome:** Achieve
comprehensive visibility into your supply chain network, to help
make sure that workloads are running within the optimal setup to
meet business needs while minimizing emissions. This includes
mapping critical workloads, highlighting self-managed areas versus
partner areas and continuously adapting to the evolving business
requirements and external conditions.

**Benefits of establishing this best
practice:** This practice enables informed
decision-making, optimal resource usage, and alignment of
technology to sustainability targets. It promotes transparency
across supply chain networks, which enhances accountability and
performance efficiency.

**Level of risk exposed if this best
practice is not established:** High

## Implementation guidance

Evaluate and map your supply chains technology-related
workloads, focusing especially on the most critical scenarios,
with your supply chain network. This creates a comprehensive
view of where you run the most intensive workloads, where you
have the biggest facilities or most relevant supply chain
infrastructures, and how they connect to each other through the
network.

Highlight the areas of your network which are directly managed
by you and which ones from your trading partners, while
considering calculating the footprint of the workloads running
on-premises and in the cloud.

### Implementation steps

- Map supply chain technology workloads and identify the
most critical scenarios across your network
infrastructure.
- Evaluate current workload placement and calculate
emissions footprint for both on-premises and cloud-based
operations.
- Assess optimal AWS Regions based onProximity to renewable
energy projects in the regions, lowest carbon footprint,
latency requirements, and service availability.
- Analyze cost implications and Sovereignty constraints when
selecting AWS Regions for workload placement.
- Develop a migration plan for workloads that should be
moved to more sustainable AWS Regions while maintaining
operational requirements.
- Establish ongoing monitoring and optimization processes to
adapt AWS Region selection as business needs and
sustainability goals evolve.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/supply-chain-lens/scsus01-bp01.html*

---

# SCSUS02 — Region selection

**Pillar**: Sustainability  
**Best Practices**: 1

---

# SCSUS02-BP01 Use the available AWS infrastructure to implement your distributed architecture

Consider optimizing where you run your workloads using the
extensive AWS infrastructure and a distributed architecture to
enable your trading partners to rely on services based on their
predominant areas of operation.

**Desired outcome:** Enable
seamless execution of supply chain operations by optimizing
workload distribution across appropriate AWS Regions, matching
partners needs and aligning with sustainability and operational
goals.

**Benefits of establishing this best
practice:** Optimizes the emissions while supporting
global scalability, latency and performance. It serves also as a
practice to align sustainability targets with trading partners'
operations, facilitating also the dynamic, on-demand resource
scaling to reach optimal cost and performance ratio.

**Level of risk exposed if this best
practice is not established:** Medium

## Implementation guidance

Evaluate a distributed architecture to support your supply chain
operations, using the extensive AWS infrastructure. Consider
mapping the optimal AWS Regions, correlating from where your
trading partners could benefit the execution from, while using
the scaling capabilities of the AWS infrastructure to replicate
services where needed and adopt an on-demand approach with
related automations to scale, turn on and off services based on
target areas of execution.

### Implementation steps

- Map trading partner locations and their predominant areas
of supply chain execution to identify optimal region
placement.
- Evaluate distributed architecture options that use AWS
infrastructure to support global supply chain operations.
- Implement AWS region-specific service deployments that
align with partner operational areas and sustainability
goals.
- Configure automated scaling and on-demand resource
provisioning based on regional demand patterns.
- Establish monitoring and optimization processes to
facilitate efficient resource utilization across
distributed AWS Regions.
- Regularly review and adjust regional deployments based on
changing partner needs and sustainability targets.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/supply-chain-lens/scsus02-bp01.html*

---

# SCSUS03 — Alignment to demand

**Pillar**: Sustainability  
**Best Practices**: 1

---

# SCSUS03-BP01 Use the supply chain operations reference (SCOR) to map your supply chain

Consider the adoption of the SCOR model or equivalent standardized
models like Value Reference Model (VRM) and managing for supply
chain performance (M4SC) to map your supply chains and keep
related metrics monitored, to be sure you are aligning planning,
execution and enablement to the actual demand, leading to
emissions optimizations.

**Desired outcome:** Develop a structured, measurable, and adaptable view of your supply chain to align operations with actual demand, help minimize emissions, and optimized resource use.

**Benefits of establishing this best practice:** Provides a standardized framework for monitoring and improving supply chain operations, leading to reduced waste, better alignment with sustainability targets, and increased agility.

**Level of risk exposed if this best
practice is not established:** High

## Implementation guidance

Evaluate the adoption of the SCOR model over the organization to
generate an aggregated view of your operations, the implemented
use cases, and the related technology workloads, considering the
six areas of the model: plan, source, make, deliver, return,
enable. This would allow your organization to rely on a common
model to keep tracking and measuring technology services, use
cases and related operations you run and where (location), your
performance and emissions your operations generate, while using
tags applied to the AWS services in use for straightforward
report, export, and aggregated views.

### Implementation steps

- Adopt the SCOR model or equivalent standardized framework
to map and categorize your supply chain operations.
- Implement comprehensive tagging strategies for AWS
services to enable the tracking by SCOR model areas and
Supply Chain network locations.
- Establish metrics and monitoring systems to track
performance and emissions across all SCOR model areas.
- Create aggregated views that show the percentage of
operations running in cloud versus on-premises for each
supply chain area of the model.
- Identify and plan migration strategies for the services
corresponding to the on-premises percentage that you would
move to the cloud to gain additional sustainability
benefits.
- Regularly review and update the map of your supply chain
to reflect changes you might have applied to your
operations, and to get an updated status of where you are
towards your sustainability targets.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/supply-chain-lens/scsus03-bp01.html*

---

# SCSUS04 — Software and architecture

**Pillar**: Sustainability  
**Best Practices**: 2

---

# SCSUS04-BP01 Optimize your compute workloads for your supply chain sustainability

Consider configuring AWS Compute Optimizer to analyze and
investigate supply chain sustainability related workloads, to
support your analysis on how to optimize the usage of compute
resources to sustain your supply chain workloads.

**Desired outcome:** Optimize the
performance of compute workloads to reduce energy consumption and
emissions while maintaining the reliability of supply chain
operations.

**Benefits of establishing this best
practice:** Enhances the efficiency of compute resource
utilization, reduces operational costs, and aligns sustainability
efforts with performance objectives.

**Level of risk exposed if this best
practice is not established:** Medium

## Implementation guidance

Before proceeding with scenarios simulation over your supply
chains operations, to help you understand why and which set of
operations are requiring more compute and memory resources,
consider to setup and run AWS Compute Optimizer combined with
Amazon CloudWatch metrics to analyze resource utilization
patterns and identify optimization opportunities, leading as a
direct consequence to sustainability's KPIs improvements.

### Implementation steps

- Configure AWS Compute Optimizer to analyze supply chains
workload performance and resource utilization patterns.
- Provision Amazon CloudWatch and configure metrics
collection to gather detailed performance data across all
supply chains compute resources.
- Analyze compute utilization patterns to identify
over-provisioned or under-utilized resources that can be
optimized.
- Right-size compute instances based on actual usage
patterns and performance requirements.
- Implement automated scaling policies to match compute
resources with actual demand patterns.
- Monitor and measure the impact of optimization efforts on
both performance and sustainability metrics.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/supply-chain-lens/scsus04-bp01.html*

---

# SCSUS04-BP02 Build and run optimization models for resources involved in supply chains sustainability

Consider building and run specific optimization models targeting
supply chains sustainability, through scenarios simulation able to
simulate resources usage and collect metrics for supply chains
planning, execution and enablement.

**Desired outcome**: Develop and
use optimization models to identify opportunities for operations
efficiency, resource efficiency, reduce emissions, and align
resource usage with both sustainability and business objectives.

**Benefits of establishing this best
practice:** Facilitates data-driven resource allocation,
helps with optimal performance with minimal environmental impact,
and supports comprehensive scenario planning for supply chain
operations.

**Level of risk exposed if this best
practice is not established:** High

## Implementation guidance

Optimization models specifically envisioned for supply chain
sustainability can be designed, built, and configured through
optimization capabilities running on AWS as managed services.

This allows you to optimize your operations and the use of
resources to achieve lower CO2 emissions and energy
optimization, while generating more efficient purpose-built
analysis for sustainability. The integration of these
sustainability measures with existing optimization analysis
enables greater focus on cost efficiency, service-level
performance, and the ability to respond to disruptions or
failures.

### Implementation steps

- Design and develop optimization models specifically
focused on supply chain sustainability using AWS managed
services.
- Integrate sustainability
[Software
and architecture](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/software-and-architecture.html)metrics with existing cost
efficiency and performance optimization models.
- Implement scenario simulation capabilities to test
different resource allocation strategies and their
sustainability impact.
- Configure automated optimization workflows that balance
sustainability goals with operational efficiency and
requirements.
- Establish feedback loops to continuously improve
optimization models based on actual performance and
sustainability outcomes.
- Create reporting and visualization tools to communicate
optimization results and sustainability improvements to
stakeholders.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/supply-chain-lens/scsus04-bp02.html*

---

# SCSUS05 — Data management

**Pillar**: Sustainability  
**Best Practices**: 1

---

# SCSUS05-BP01 Adopt modern data management and governance practices for your supply chain sustainability, and focus on economic, environmental, and social needs

Consider supply chain fine-tuned data lake, analytics, and data
governance practices with specific focus on sustainability to
address economic, environmental and social needs.

**Desired outcome:** Implement
robust data management practices to help with
sustainability-related use cases, providing support for accurate,
secure, and comprehensive datasets.

**Level of risk exposed if this best
practice is not established:** High

## Implementation guidance

Consider the adoption of a managed supply chain fine-tuned data
lake using Amazon S3, and Amazon S3 Tables and table bucket, for
unmatched performance, durability, availability, scalability,
security, compliance and audit capabilities, in combination with
AWS Lake Formation to accelerate the build of secure data lakes.
Build your data inventory considering all the data sources (both
internal and external), your EDI flows, and create your data
catalog with the proper metadata and tags that can help you map
which information is contributing to both the economic,
environmental and social needs perspectives.

### Implementation steps

- Implement a managed supply chain data lake using Amazon S3, Amazon S3 Tables and table buckets, and AWS Lake Formation to centralize sustainability-related data.
- Build a comprehensive data inventory that includes
internal and external data sources, EDI flows, and
sustainability metrics.
- Create detailed data catalogs with metadata and tags that
map data contributions to economic, environmental, and
social sustainability needs.
- Implement data governance policies and access controls to
maintain data quality and security across the
sustainability data environment.
- Establish data integration pipelines that connect AWS Glue
with Amazon DataZone for comprehensive data management
across organizational boundaries.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/supply-chain-lens/scsus05-bp01.html*

---

# SCSUS06 — Data management

**Pillar**: Sustainability  
**Best Practices**: 1

---

# SCSUS06-BP01 Enhance your data strategy and exchange capabilities with your trading partners

Consider enhancing your data strategy and your data exchange
capabilities with external parties and trading partners or
providers to address compliance needs (for example, digital
product passport, battery passport, and CO2 emissions reports) and
to accelerate the path towards your sustainability targets.

**Desired**
**outcome:** Foster collaboration
and compliance across the supply chain by adopting decentralized
data exchange strategies (like data spaces) and enhancing
data-sharing capabilities.

**Benefits of establishing this best
practice:** Accelerates the achievement of sustainability
targets and needs through increased transparency and improved
compliance.

**Level of risk exposed if this best
practice is not established:** High

## Implementation guidance

Strengthen your data strategy for supply chain and
sustainability use cases, and more generally, for the entire
organization. If already not in place, consider allocating time
and resources to the development of your data strategy, while
considering the adoption of decentralized approaches (for
example, data spaces) applied to data exchange, to efficiently
steer towards adhering to regulations to reach higher levels of
compliance and simplify the implementation of use cases that
require complex data exchange over the trading partners network.

### Implementation steps

- Develop a comprehensive data strategy that encompasses
supply chain sustainability use cases and organizational
requirements.
- Evaluate and implement decentralized data exchange
approaches (data spaces) to facilitate trading partner
data sharing.
- Establish secure data sharing protocols that support
compliance requirements, such as digital product passport
and battery passport.
- Configure automated CO2 emissions reporting capabilities
that integrate with trading partner systems.
- Implement data governance frameworks that maintain
compliance with sustainability regulations across partner
networks.
- Create monitoring and auditing capabilities to track data
exchange effectiveness and compliance adherence.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/supply-chain-lens/scsus06-bp01.html*

---

# SCSUS07 — Hardware and services

**Pillar**: Sustainability  
**Best Practices**: 1

---

# SCSUS07-BP01 Plan and design for automation for supply chain sustainability

Consider optimizing your supply chain sustainability through
automation, planning, and designing for automation. Plan for
designing completely or partially, where applicable, all the
time-consuming tasks to reduce the usage time of a required AWS
resource, to collect data for peaks and valleys analysis to feed
them into ML models or advanced analysis to enable automatic
scalability based on demand.

Provision the AWS Cloud services you need to support your
operations based on your business needs.

**Desired outcome:**
Streamline supply
chain operations through automation, reducing manual processes,
and optimizing resource utilization to align with sustainability
goals.

**Benefits of establishing this best
practice:** Enhances operational efficiency, reduces
costs, and improves responsiveness to changing business needs.

**Level of risk exposed if this best
practice is not established:** Medium

## Implementation guidance

Automate the provisioning of the AWS services you need to
support your operations to keep the technology infrastructure
quickly adjustable in case your business needs change.
Automation is a best practice in the context of supply chain and
sustainability, as well as implementing predictive horizontal
and vertical scaling of compute resources, turning on and off
resources based on usage and demand, and forecasting the demand,
business peaks and valleys due to seasonality, and promotions
for direct and indirect emissions optimization.

### Implementation steps

- Implement infrastructure as code (IaC) approaches to
automate the provisioning and management of AWS services
supporting supply chain operations.
- Configure predictive scaling policies for compute
resources based on historical demand patterns and
seasonality analysis.
- Establish automated resource scheduling to turn resources
on/off based on actual usage patterns and business demand.
- Deploy machine learning models to forecast demand patterns
and optimize resource allocation for sustainability.
- Implement automated monitoring and alerting systems to
track resource utilization and sustainability metrics.
- Create continuous improvement processes to refine
automation strategies based on performance and
sustainability outcomes.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/supply-chain-lens/scsus07-bp01.html*

---

# SCSUS08 — Hardware and services

**Pillar**: Sustainability  
**Best Practices**: 1

---

# SCSUS08-BP01 Collect usage data to feed advanced analysis and ML models to better predict future resources needs

Consider improving your ability to predict AWS Cloud resources
required for your supply chain and sustainability-related
workloads to prefer on-demand over always-on. Base this data on
forecasts, seasonality, and peaks and valleys analysis to
efficiently turn resources on and off accordingly or scaling
resources up and down and horizontally.

**Desired outcome**: Achieve
dynamic scalability and resource efficiency by using historical
usage data to predict and optimize resource needs.

**Benefits of establishing this best
practice:** Improves operational agility, reduces
downtime, and minimizes unnecessary resource usage.

**Level of risk exposed if this best
practice is not established:** Medium

## Implementation guidance

Consider collecting data about resource usage over the past
years to design and prefer on-demand over always-on, with the
main goal of optimizing resources scaling, uptime and downtime,
availability, and replication based on your business needs.

Gain visibility of required resources through ML-based
predictions, using built-in features of AWS System Manager,
Instance Scheduler on AWS, and signals from Amazon CloudWatch,
while using managed databases like Amazon RDS, and
[containers
orchestration](https://aws.amazon.com/containers/) running on AWS towards serverless
architectures.

### Implementation steps

- Collect and analyze historical resource usage data to
identify patterns and optimization opportunities for
on-demand resource allocation.
- Implement machine learning-based prediction models to
forecast future resource needs based on business patterns
and seasonality.
- Deploy AWS Systems Manager and Instance Scheduler to
automate resource scheduling based on predicted demand
patterns.
- Configure Amazon CloudWatch monitoring to provide
real-time signals for dynamic resource scaling decisions.
- Migrate appropriate workloads to managed databases and
serverless architectures to optimize resource utilization.
- Establish continuous monitoring and optimization processes
to refine on-demand resource strategies over time.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/supply-chain-lens/scsus08-bp01.html*

---

# SCSUS09 — Process and culture

**Pillar**: Sustainability  
**Best Practices**: 1

---

# SCSUS09-BP01 Align your supply chain sustainability goals and metrics with the broader set of company-wise sustainability goals

Align supply chain workloads and the technology-related emissions
to the wider organization's sustainability strategy and goals to
monitor how their impact evolves over the time and contributes to
your organization's sustainability targets.

**Desired outcome:** Supply chain
sustainability initiatives contribute effectively to the overall
sustainability goals of the organization.

**Benefits of establishing this best
practice:** Creates a unified approach to sustainability,
enhances organizational impact, and helps with consistent progress
toward long-term goals.

**Level of risk exposed if this best
practice is not established:** High

## Implementation guidance

Supply chains are almost always responsible for most of the
emissions produced by an organization, but this is true
considering all the supply chains involved to plan, source,
make, deliver and, eventually, return a product or component.
Technology-related workloads are responsible of only a portion
of the total emissions, but depending on how much your
organization is digitized, the percentage can vary and emit a
larger portion compared to overall emissions. The adoption of
the cloud to run all or partially your operations eases the
tracking and measuring carbon emissions with regards to your
AWS-related workloads through the
[Customer
Carbon Footprint](https://aws.amazon.com/aws-cost-management/aws-customer-carbon-footprint-tool/) tool.

### Implementation steps

- Establish clear alignment between supply chain
sustainability metrics and company-wide sustainability
goals and targets.
- Implement the Customer Carbon Footprint tool to track and
measure carbon emissions from AWS-related supply chain
workloads.
- Create regular reporting mechanisms that show how supply
chain sustainability initiatives contribute to overall
organizational goals.
- Establish governance processes to make sure supply chain
sustainability efforts are coordinated with broader
organizational sustainability strategies.
- Monitor and measure the percentage impact of
technology-related emissions within the overall
organizational carbon footprint.
- Develop continuous improvement processes to enhance the
contribution of supply chain sustainability to
company-wide goals.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/supply-chain-lens/scsus09-bp01.html*

---

# SCSUS10 — Process and culture

**Pillar**: Sustainability  
**Best Practices**: 1

---

# SCSUS10-BP01 Use document digitization as an ESG goal

Explore opportunities to digitize any physical documentation
used for supply chain operations within the company but also
in operations involving partners and external entities.
Digitization of physical documentation leads to a positive
ripple effect over sustainability-related use cases,
simplifying data sharing across companies and supply chains,
data transparency, and solutions required to solve
compliance-related needs.

**Desired outcome:** Avoid or
significantly reduce the use of physical documentation in
supply chain operations, leading to measurable reductions in
paper waste, improved data accessibility, and alignment with
sustainability goals.

**Benefits of establishing this best
practice:**

- **Environmental benefits:**
Reduces paper waste, lowering the organization's carbon
footprint and aligning with ESG objectives.
- **Operational benefits:**
Improves document accessibility, reduces processing time,
and enhances data-driven decision-making.
- **Compliance benefits:**
Enables better tracking, management, and storage of
sensitive supply chain data in secure, auditable digital
formats.

**Level of risk exposed if this best
practice is not established:** Medium

**Implementation guidance**

Supply chain operations often generate significant volumes of
physical documents, including supplier contracts, freight
airway bills (AWBs), and invoices. Transition to a
digital-first approach by using AI-powered document
digitization tools, such as Amazon Textract and AWS
Comprehend, to extract, organize, and analyze data from
physical documents. Integrate these tools into your supply
chain workflows to minimize paper dependency, while evaluating
the environmental impact of physical documentation and
quantifying the reductions achieved through digitization
initiatives.

## Implementation steps

- Identify all physical documentation used in supply chain
operations and assess opportunities for digitization.
- Implement AI-powered document digitization tools such as
Amazon Textract and AWS Comprehend to automate document
processing.
- Create digital repositories for centralized document
management using secure AWS storage services.
- Establish Secure and compliance-aligned document storage
using AWS tools like Amazon S3 and AWS KMS.
- Automate document processing workflows to improve
operational efficiency and minimize paper dependency.
- Measure and report on environmental impact reductions
achieved through digitization initiatives to support ESG
goals.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/supply-chain-lens/scsus10-bp01.html*

---

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
