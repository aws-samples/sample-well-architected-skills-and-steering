# SCPERF02 — Compute selection

**Pillar**: Performance Efficiency  
**Best Practices**: 3

---

# SCPERF02-BP01 Use serverless compute to run tasks

Choosing the correct compute power for the workload provides
smooth performance of the application, not only for the end users
also for the solution developer community to maintain the software
stacks across various infrastructures.

**Desired outcome:** Smooth
performance that elastic in nature with low upkeep.

**Benefits of establishing this best
practice:** Improved user experience, maintenance of
software stack, and scalability.

**Level of risk exposed if this best
practice is not established:** High

## Implementation guidance

Some supply chain services computing workloads, like supplier
data visibility, are typically loosely coupled and can benefit
from event-driven architectures using the scaling capacity of
AWS serverless compute options like AWS Lambda and AWS Fargate,
combined with messaging services including Amazon SQS and Amazon EventBridge to decouple components. These serverless solutions
minimize the overhead of capacity management, automatically
scaling in or out to meet demands. Where scale is the primary
factor, AWS serverless container compute engine AWS Fargate, can
be used with both Amazon Elastic Container Service (Amazon ECS)
and Amazon Elastic Kubernetes Service (Amazon EKS), removing the
overhead of managing and provisioning compute resources.

### Implementation steps

- Identify supply chain workloads that are suitable for
serverless architectures, focusing on event-driven and
loosely coupled processes.
- Implement AWS Lambda functions for lightweight,
short-duration tasks such as data processing and API
integrations.
- Deploy AWS Fargate for containerized workloads that
require more control over the runtime environment while
maintaining serverless benefits.
- Integrate messaging services like Amazon SQS and Amazon EventBridge to decouple components and enable asynchronous
processing.
- Configure auto-scaling policies to automatically adjust
compute resources based on demand patterns and workload
requirements.
- Monitor performance metrics and optimize function
configurations to facilitate efficient resource
utilization and cost-effectiveness.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/supply-chain-lens/scperf02-bp01.html*

---

# SCPERF02-BP02 Use machine learning capabilities for supply chain applications

AWS Supply Chain unifies data and provides machine
learning--powered actionable insights, built-in contextual
collaboration, and demand planning.

**Desired**
**outcome:** High requirement
workloads can be made easier using machine learning capabilities.
Certain pre-built algorithms can reused to fit your workflow which
can save time for building the right solutions.

**Benefits of establishing this best
practice:** Agility, performance, and re-usability.

**Level of risk exposed if this best
practice is not established:** Medium

## Implementation guidance

Use
[AWS Supply Chain](https://aws.amazon.com/aws-supply-chain/) to reduce the heavy lifting of the
workloads, which involves deep machine learning skills and
time-consuming algorithm development activities.

### Implementation steps

- Evaluate existing supply chain processes to identify
opportunities where machine learning can provide value and
improve efficiency.
- Implement AWS Supply Chain to use pre-built machine
learning models for demand forecasting and supply
planning.
- Integrate machine learning capabilities with existing
supply chain systems to enhance decision-making and
automation.
- Train teams on machine learning tools and best practices
to maximize the value of AI-powered supply chain
solutions.
- Monitor machine learning model performance and
continuously refine algorithms based on actual business
outcomes.
- Expand machine learning usage to additional supply chain
use cases as capabilities and confidence grow.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/supply-chain-lens/scperf02-bp02.html*

---

# SCPERF02-BP03 Use edge compute capabilities for supply chain applications

AWS offers a robust suite of edge computing solutions that extend
cloud capabilities closer to end users, devices, and on-premises
locations. At the core of AWS's edge computing strategy are two
main services: AWS Outposts and AWS Local Zones.

**Desired**
**outcome:** These edge compute
capabilities enable a single-digit millisecond latency for
applications like supply chain which needs real-time edge data to
perform machine learning inferences and action autonomously
without pushing the decision making at the cloud.

**Benefits of establishing this best
practice:** Agility, performance, and low latency.

**Level of risk exposed if this best
practice is not established:** High

## Implementation guidance

AWS offers a robust suite of edge computing solutions that
extend cloud capabilities closer to end users, devices, and
on-premises locations. At the core of AWS's edge computing
strategy are two main services: AWS Outposts and AWS Local
Zones. AWS Outposts brings native AWS services, infrastructure,
and operating models to virtually any datacenter or on-premises
facility. It's ideal for workloads requiring low latency access
to on-premises systems, local data processing, or data residency
requirements. AWS Local Zones are infrastructure deployments
that place compute, storage, database, and other AWS services
closer to large population and industry centers. Local Zones act
as an extension of an AWS Region, connected through
high-bandwidth, secure connections.

### Implementation steps

- Assess supply chain operations to identify use cases that
require low-latency processing or local data residency.
- Deploy AWS Outposts for on-premises workloads that need
AWS services with local data processing capabilities.
- Implement AWS Local Zones for applications requiring
ultra-low latency access to end users or manufacturing
facilities.
- Configure AWS IoT Greengrass for edge devices to enable
local data processing and autonomous decision-making
capabilities.
- Establish secure connectivity between edge locations and
central cloud infrastructure to maintain data
synchronization.
- Monitor edge computing performance and optimize resource
allocation to facilitate efficient operation across
distributed locations.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/supply-chain-lens/scperf02-bp03.html*

---
