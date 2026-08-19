# Reliability

**Pillar**: Reliability  
**Questions**: 9

---

# ADVREL01 — Design for reliability

**Pillar**: Reliability  
**Best Practices**: 4

---

# ADVREL01-BP01 Use loosely-coupled architectures to enable graceful recovery from failures

Use architecture patterns like service-oriented architecture
(SOA), microservices, and event-driven architecture (EDA) to
recover quickly and efficiently from failure. These architectural
patterns enable robust failure recovery through loosely coupled
designs and enhance system resilience and component self-sufficiency.

## Implementation guidance

Highly scalable and reliable workloads necessitate reusable
software components that are accessible through service
interfaces like APIs. Microservices take this a step further by
breaking down components into smaller, simpler units. EDAs build
upon and enhance microservices with an event broker, fostering
greater efficiency.

Implement EDAs using services like
[Amazon EventBridge](https://aws.amazon.com/eventbridge/) and

[Amazon Simple Notification Service (SNS)](https://aws.amazon.com/sns/) to decouple components and
enable asynchronous communication. This can improve resilience
by reducing hard coded dependencies and enabling retries and
error handling.

Make sure that the data pipelines of the advertising system
operate reliably despite unexpected failures, packet loss, or
high latency. Design interactions between components in your
distributed advertising system in such way that their failure
makes minimal impact.

## Key AWS services

- [Amazon Simple Queue Service (SQS)](https://aws.amazon.com/sqs/)
- [AWS Step Functions](https://aws.amazon.com/step-functions/)

## Resources

- [What is EDA? - Event Driven Architecture Explained - AWS](https://aws.amazon.com/what-is/eda/index.html)
- [Avoiding insurmountable queue backlogs](https://aws.amazon.com/builders-library/avoiding-insurmountable-queue-backlogs/)
- [How can I prevent an increasing backlog of messages in my Amazon SQS queue?](https://repost.aws/knowledge-center/sqs-message-backlog)
- [Amazon Simple Notification Service (SNS) | AWS News Blog](https://aws.amazon.com/blogs/aws/category/messaging/amazon-simple-notification-service-sns/index.html)
- [Increasing
MTBF - Availability and Beyond: Understanding and Improving the Resilience of Distributed Systems on AWS](https://docs.aws.amazon.com/whitepapers/latest/availability-and-beyond-improving-resilience/increasing-mtbf.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advrel01-bp01.html*

---

# ADVREL01-BP02 Architect your system with appropriate recovery objectives

Avoid over- or under-architecting your services by
[working
backwards](https://www.aboutamazon.com/news/workplace/an-insider-look-at-amazons-culture-and-processes) from your services' recovery objectives, striking
a balance with adjacent pillars such as cost optimization and
operational excellence. KPIs established in the operational
excellence pillar should inform approaches to reliability.

## Implementation guidance

Identify critical parts of the architecture and individually
confirm their reliability and recovery point and time objectives
(RPO and RTO). For example, with real-time bidding (RTB),
delivery services have increased RPO and RTO requirements as
compared to creative services. On close inspection, certain
architectures also have variable availability and recovery
requirements, operating on a spectrum from multiple layers of
redundancy to entirely non-redundant. Advertising customers
accept ranges from milliseconds to hours as appropriate
recovery. For example, enrichment and auction layers often have
the most stringent requirements, while analytics or as necessary
reporting can see reduced requirements.

## Key AWS services

- [AWS Resilience Hub](https://aws.amazon.com/resilience-hub/)

## Resources

- [Establishing
RPO and RTO Targets for Cloud Applications](https:\aws.amazon.com\blogs\mt\establishing-rpo-and-rto-targets-for-cloud-applications)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advrel01-bp02.html*

---

# ADVREL01-BP03 Architect for variable demand

Architect to elastically launch resources for variable demand,
including the most challenging peak events, like flash crowds or
thundering herds.

## Implementation guidance

Depending on the advertising channel, such as retail stores,
video streaming, or audio apps, loads will peak at different
times in different locations. Know your historical load
statistics, and adjust load testing scenarios based on
historical peaks to determine how the workload performs in
unexpected situations and peak demand. With
[Amazon CloudWatch Real-User Monitoring (RUM)](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM.html), you can collect
and view client-side data about your web application performance
from actual user sessions in near real-time.
[CloudWatch](https://aws.amazon.com/cloudwatch/)
Synthetics are configurable scripts that run on a schedule to
monitor your endpoints and APIs.

If this a new workload without historical data, load testing is
part of this process. Until enough historical data is obtained,
use [Auto
Scaling](https://aws.amazon.com/autoscaling/) groups and Elastic Load Balancers (ELB) to meet
compute demands and send requests to healthy hosts. Networking
demands must also be considered and capacity planned to prevent
congestion. For critical workloads, consider private AWS Direct Connect networking to connect to partners or on-premise
infrastructure to provide sufficient capacity and more stable
latency.

## Resources

- [Predictive
scaling for Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-predictive-scaling.html)
- [Guidance
for AdTech Private Network on AWS](https://aws.amazon.com/solutions/guidance/adtech-private-network-on-aws/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advrel01-bp03.html*

---

# ADVREL01-BP04 Implement chaos engineering practices

Accept that "everything fails, all the time," (Dr. Werner Vogels,
Amazon CTO), and safely disrupt things on your terms to discover
faults and fragility so that you can later improve services.

## Implementation guidance

Advertising systems have components that are sensitive to
disconnects, latency, and bandwidth changes. Use tools like
[AWS Fault
Injection Service (FIS)](https://aws.amazon.com/fis/) or open-source tools like
[Chaos
Monkey](https://netflix.github.io/chaosmonkey/) to inject failures into your workload which
simulate network disruptions or resource unavailability. Based
on the results, update responses to failure scenarios, how you
monitor, and what you alert on, then adapt runbooks and
playbooks before practicing failure response with relevant
teams.

## Key AWS services

- [AWS Resilience Hub](https://aws.amazon.com/resilience-hub/)

## Resources

**Related documentation:**

- [AWS chaos engineering blogs](https://aws.amazon.com/blogs/architecture/tag/chaos-engineering/)
- [Continuous
integration and continuous delivery](https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-caf-platform-perspective/ci-cd.html)
- [Leverage
AWS Resilience Lifecycle Framework to assess and improve the resilience of application using AWS Resilience Hub](https://aws.amazon.com/blogs/mt/leverage-aws-resilience-lifecycle-framework-to-assess-and-improve-the-resilience-of-application-using-aws-resilience-hub/index.html)
- [[QA.NT.6]
Experiment with failure using resilience testing to build recovery preparedness](https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/qa.nt.6-experiment-with-failure-using-resilience-testing-to-build-recovery-preparedness.html)

**Related
videos:**

- [AWS re:Invent 2020 - Developer Keynote with Dr. Werner Vogels](https://www.youtube.com/watch?v=jt-gV1YwmnI)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advrel01-bp04.html*

---

# ADVREL02 — Latency sensitive advertising

**Pillar**: Reliability  
**Best Practices**: 3

---

# ADVREL02-BP01 To allow fast and graceful failure of latency-sensitive services, avoid exponential backing off and retry

With real-time bidding systems, your workload must handle failures
in latency-sensitive services. Traditional exponential backoff and
retry mechanisms should be avoided. Instead, opt for fast-fail
approaches and appropriate rate-limiting techniques to maintain
service responsiveness.

## Implementation guidance

Operating within 100 ms real-time bidding contracts, a single
throttle and retry of five seconds can result in many failed
bids and potentially insurmountable retry queues. Avoid this by
adapting retries to fail fast.  Regulate request rates using
algorithms, such as token buckets, leaky buckets, or fixed
window counters, or use managed service features, like Amazon API Gateway's request throttling. Rate limiting helps prevent
resource exhaustion and fairly distributes resources among
clients or services. Know the trade-offs: while rate limiting
can be an effective way to protect a service from being
overloaded, it can also potentially make the service less
reliable if not implemented carefully. For example, if the rate
limits are set too low, legitimate requests may be rejected or
delayed, leading to reduced availability or responsiveness of
the service.

## Key AWS services

- [Amazon API Gateway](https://aws.amazon.com/api-gateway/) implements the token bucket algorithm to throttle requests according to account and region limits
- [Amazon Simple Queue Service (Amazon SQS)](https://aws.amazon.com/sqs/) and Amazon Kinesis can buffer requests to smooth out the request rate
- [AWS WAF](https://aws.amazon.com/waf/) can also be used to implement rate
limiting and throttle specific API consumers

## Resources

**Related documentation:**

- [Implementing
layers of admission control](https://aws.amazon.com/builders-library/fairness-in-multi-tenant-systems/)
- [API Gateway Request Throttling](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-request-throttling.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advrel02-bp01.html*

---

# ADVREL02-BP02 Implement a caching strategy

Implementing caching strategies enhances system reliability and
performance. Evaluate different caching levels from client-side to
server-side, and explore various caching solutions, including
ElastiCache, third-party databases, and CDNs for optimizing ad
payload delivery and reducing backend load.

## Implementation guidance

Caching can be applied at various levels, such as client-side
caching of user-profiles and server-side caching for bid
enhancement. Distributed caching solutions include Amazon ElastiCache Redis or Memcached. Third-party databases such as
Aerospike, Cassandra, and Scylla Cache are also commonly
deployed for server-side caching. Ad Creative payloads are very
effectively cached by CDNs, such as CloudFront, further reducing
the load on web-servers.

## Key AWS services

- [Amazon ElastiCache](https://aws.amazon.com/elasticache/) is a fully managed in-memory
data store
- [Amazon API Gateway](https://aws.amazon.com/api-gateway/) also provides a built-in
caching layer
- [AWS Lambda](https://aws.amazon.com/lambda/), a serverless compute service, can
be used to implement caching at the application layer

## Resources

**Related documentation:**

- [Amazon ElastiCache (Memcached)](https://aws.amazon.com/elasticache/memcached/index.html)
- [Data Caching Across Microservices in a Serverless Architecture](https://aws.amazon.com/blogs/architecture/data-caching-across-microservices-in-a-serverless-architecture/index.html)
- [Caching for high-volume workloads with Amazon ElastiCache](https://aws.amazon.com/getting-started/hands-on/purpose-built-databases/elasticache/index.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advrel02-bp02.html*

---

# ADVREL02-BP03 Prevent scale mismatch of both internal services and external partners

It's important to implement proportional scaling across all system
components in advertising workloads. Balance service capacities,
particularly in DSP to SSP integrations, and use pub/sub patterns
to reliably distribute load and prevent service overload in
microservices architectures.

## Implementation guidance

Providing reliability is paramount for advertising workloads,
which can be achieved by proportionally scaling all
sub-components. For instance, when you integrate using a
PrivateLink between DSP and SSP, your partner's requests may
overwhelm your API front-end services, leading to throttling. To
mitigate this when using a microservices architecture, the
smaller services should drive larger capacity services,
preventing them from being overwhelmed. The pub/sub pattern
should also be followed wherever possible to enhance reliability
through decoupled communication and load distribution across
multiple subscribers. By implementing these measures,
advertising workloads can maintain high availability and fault
tolerance, providing a seamless and reliable experience for all
stakeholders.

## Key AWS services

- [Amazon API Gateway](https://aws.amazon.com/api-gateway/)
- [Amazon SQS](https://aws.amazon.com/sqs/)
- [Amazon Kinesis](https://aws.amazon.com/kinesis/)
- [AWS Lambda](https://aws.amazon.com/lambda/)

## Resources

- [Avoiding overload in distributed systems by putting smaller service in control](https://aws.amazon.com/builders-library/avoiding-overload-in-distributed-systems-by-putting-the-smaller-service-in-control/)
- [Pub/sub
pattern](https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-integrating-microservices/pub-sub.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advrel02-bp03.html*

---

# ADVREL03 — Design for single- and Multi-Region deployments

**Pillar**: Reliability  
**Best Practices**: 4

---

# ADVREL03-BP01 Use a full Regional deployment for compute resources through Auto Scaling groups and compute container orchestrators

Deploy compute resources across multiple Availability Zones (AZs) and
Regions to enhance application resilience. Implement zone-aware
architectures to optimize performance and manage costs, and focus
on intra-AZ communication and load balancing configurations.

## Implementation guidance

Increase resiliency of real-time advertising applications by
distributing resources across multiple Availability Zones or
Regions, but maintain awareness of cross-AZ and cross-Region
data transfer costs. When you use a full Regional deployment,
implement zone-aware architectures within each Region to
optimize performance and costs. When distributing resources
across multiple Availability Zones for resilience, implement
logic to prefer intra-AZ communication, when possible, and use
features like AZ-aware load balancing to minimize cross-AZ
traffic. By being zone-aware, companies can reduce costs and
improve performance even when they need to operate in multiple
Regions.

## Key AWS services

- [Amazon EC2 Auto Scaling](https://aws.amazon.com/autoscaling/) groups can be configured
to span multiple AZs
- [Amazon Elastic Kubernetes Service (EKS)](https://aws.amazon.com/eks/) clusters
can also be deployed across multiple AZs

## Resources

- [Regions
and Availability Zones](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/)
- [Distribute
instances across Availability Zones](https://docs.aws.amazon.com/autoscaling/ec2/userguide/auto-scaling-benefits.html#arch-AutoScalingMultiAZ)
- [EC2
Instance Meta-Data Retrieval](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instancedata-data-retrieval.html)
- [Creating
Kubernetes Auto Scaling Groups for Multiple Availability Zones | Containers](https://aws.amazon.com/blogs/containers/amazon-eks-cluster-multi-zone-auto-scaling-groups/index.html)
- [Add
an Availability Zone - Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-add-az-console.html)
- [Simplify
node lifecycle with managed node groups - Amazon EKS](https://docs.aws.amazon.com/eks/latest/userguide/managed-node-groups.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advrel03-bp01.html*

---

# ADVREL03-BP02 Choose AWS Regions that meet your legal and disaster recovery requirements

Select AWS Regions based on compliance and disaster recovery
needs. It emphasizes the importance of understanding data
jurisdiction requirements, particularly for advertising systems,
and explains how regional choices impact both regulatory
compliance (like GDPR) and system redundancy.

## Implementation guidance

Depending on the resiliency design of your advertising system,
some components may reside in a different Region for redundancy
purposes. Consider compliance needs for your in-transit and at-rest data.

## Key AWS services

- [AWS Control Tower](https://aws.amazon.com/controltower/) provides Region-deny
capabilities
- [AWS Managed Microsoft AD](https://aws.amazon.com/directoryservice/) supports multi-Region
deployment, allowing AD-aware applications and AWS services
to connect to the local instances of the global directory
- [AWS KMS](https://aws.amazon.com/kms/) allows you to replicate multi-Region
keys into other Regions
- AWS services like
[Amazon S3](https://aws.amazon.com/s3/) and

[Amazon RDS](https://aws.amazon.com/rds/) are designed to be resilient by
spreading requests and data across multiple

[Availability
Zones within a Region](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/). However, for
additional redundancy, you can deploy these services across
multiple Regions to achieve isolation and avoid correlated
failures

## Resources

- [Accelerate
your multi-region strategy with Amazon DynamoDB: Part 1](https://aws.amazon.com/blogs/database/part-1-accelerate-your-multi-region-strategy-with-amazon-dynamodb/)
- [AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/)
- [Understand
resiliency patterns and trade-offs to architect efficiently in the cloud](https://aws.amazon.com/blogs/architecture/understand-resiliency-patterns-and-trade-offs-to-architect-efficiently-in-the-cloud/)
- [Deny
services and operations for AWS Regions of your choice with AWS Control Tower](https://aws.amazon.com/about-aws/whats-new/2021/11/deny-services-operations-aws-regions-control-tower/index.html)
- [Design
consideration for AWS Managed Microsoft Active Directory - Active Directory Domain Services on AWS](https://docs.aws.amazon.com/whitepapers/latest/active-directory-domain-services/design-consideration-for-aws-managed-microsoft-active-directory.html)
- [Creating
multi-Region replica keys - AWS Key Management Service](https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-replicate.html)
- [Regional
services - AWS Fault Isolation Boundaries](https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/regional-services.html)
- [Navigating
GDPR Compliance on AWS](https://docs.aws.amazon.com/whitepapers/latest/navigating-gdpr-compliance/welcome.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advrel03-bp02.html*

---

# ADVREL03-BP03 Configure databases to span across multiple Availability Zones

Explore database configuration strategies for reliability and
disaster recovery, such as periodic snapshots to warm standby
solutions. Evaluate trade-offs between single-AZ and multi-AZ
deployments, costs considerations, and specific recovery time
objectives (RTO).

## Implementation guidance

Carefully consider the trade-offs between disaster recovery
strategies when configuring databases in multi-AZ and single-AZ
deployments. While multi-AZ deployments offer high availability,
they can incur significant cross-AZ data transfer costs.

For cost-sensitive workloads, consider implementing a single-AZ
database cluster with the following resilience strategies:

- **Periodic snapshots:**
Implement frequent automated snapshots of your database.
This approach provides point-in-time recovery capabilities
with a relatively low RTO, typically in the range of 15-60
minutes, depending on the database size and recovery
process.
- **Read replicas:** Deploy
read replicas in a different Availability Zone. While this
incurs some cross-AZ data transfer costs, it's generally
less expensive than a full multi-AZ deployment. In case of a
primary Availability Zone failure, promote the read replica
to become the new primary. This can reduce RTO to between
five and 15 minutes.
- **Cold standby:** Maintain a
stopped database instance in another Availability Zone, and
periodically update it with snapshots. This approach
balances cost and recovery time, with an RTO of
approximately 10-30 minutes.

For mission-critical applications, where minimal downtime is
essential, consider:

- **Warm standby:** Keep an
active, scaled-down secondary database in another
Availability Zone continuously updated using asynchronous
replication. This approach offers a lower RTO (between one
and five minutes), but at a higher cost than cold standby.

Choose the strategy that best aligns with your specific RTO
requirements and budget constraints. Implement and regularly
test your chosen disaster recovery process to verify that it
meets your RTO targets.

For AdTech customers who require multi-region deployment for
global resilience, use services like Amazon Aurora Global
Database or Amazon DynamoDB global tables. These services
provide Region-wide resilience with minimal impact on
performance and manageable costs.

Regularly review and optimize your database architecture as your
workload and requirements evolve. Always weigh the costs of
potential downtime against the ongoing expenses of more
resilient configurations.

## Key AWS services

- [Amazon Relational Database Service (Amazon RDS)](https://aws.amazon.com/rds/)
provides a Multi-AZ deployment option
- [Amazon DynamoDB](https://aws.amazon.com/dynamodb/)
- [Amazon Aurora](https://aws.amazon.com/rds/aurora/)
- [Amazon ElastiCache](https://aws.amazon.com/elasticache/)

## Resources

- [Amazon RDS Multi-AZ](https://aws.amazon.com/rds/features/multi-az/)
- [Protect
critical workload with Pod Disruption Budgets](https://docs.aws.amazon.com/eks/latest/best-practices/application.html#_recommendations_3)
- [Using
Amazon Aurora Global Database](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database.html)
- [Amazon DynamoDB global tables](https://aws.amazon.com/dynamodb/global-tables/)
- [What
is Amazon Relational Database Service (Amazon RDS)?](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html)
- [Multi-AZ
DB instance deployments for Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZSingleStandby.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advrel03-bp03.html*

---

# ADVREL03-BP04 Reserve appropriate capacity of services in the supported Regions

Manage service capacity across multiple Regions. Perform regular
load testing at five times your baseline RTB traffic levels to
validate capacity requirements. Validate that appropriate
reservations are made to handle normal operations, peak loads, and
potential disruptions.

## Implementation guidance

If your application is designed to scale out over multiple
Regions, service could be disrupted by temporary resource
constraints or other issues impacting a single Availability Zone
or Region. Regularly perform load tests with at least five times
the baseline of RTB traffic expectations to validate that
allocated capacity meets low water mark, mean, and peak capacity
projections. Based on the results of your load tests, make
capacity reservation.

## Key AWS services

- [Amazon Route 53](https://aws.amazon.com/route53/)
- [Amazon DynamoDB global tables](https://aws.amazon.com/dynamodb/)
- [Amazon S3](https://aws.amazon.com/s3/)

## Resources

- [AWS service quotas](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html)
- [Quotas
and constraints for Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Limits.html)
- [What
to Consider when Selecting a Region for your Workloads](https://aws.amazon.com/blogs/architecture/what-to-consider-when-selecting-a-region-for-your-workloads/)
- [Creating
a Multi-Region Application with AWS Services – Part 1, Compute, Networking, and Security](https://aws.amazon.com/blogs/architecture/creating-a-multi-region-application-with-aws-services-part-1-compute-and-security/index.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advrel03-bp04.html*

---

# ADVREL04 — Change management

**Pillar**: Reliability  
**Best Practices**: 2

---

# ADVREL04-BP01 Through your CI/CD pipeline, employ end-to-end regression, performance, and canary testing

Integrate comprehensive testing methodologies into CI/CD pipelines
for advertising workloads. Monitor key metrics like 5xx errors and
latency, especially in RTB systems, and respond quickly to issues
through immediate engagement and fast rollbacks.

## Implementation guidance

For RTB at scale, the primary reliability metrics for
availability are 5xx internal errors and elevated latency. If
these metrics are breached, do not wait for impacts to ad
effectiveness. Instead, fail fast and revert changes until the
root cause of the issue can be identified and addressed.

## Key AWS services

- [AWS CodePipeline](https://aws.amazon.com/codepipeline/) is a fully-managed continuous
delivery service
- [AWS Fault Injection Service](https://aws.amazon.com/fis/) is a
fully-managed service that simulates real-world failures
- [AWS Step Functions](https://aws.amazon.com/step-functions/)

## Resources

- [Deployment
strategies](https://docs.aws.amazon.com/whitepapers/latest/introduction-devops-aws/deployment-strategies.html)
- [Canary
deployments](https://docs.aws.amazon.com/whitepapers/latest/overview-deployment-options/canary-deployments.html)
- [Use
CloudWatch Synthetics to Monitor Sites, API Endpoints, Web Workflows, and More](https://aws.amazon.com/blogs/aws/new-use-cloudwatch-synthetics-to-monitor-sites-api-endpoints-web-workflows-and-more/)
- [Performing
canary deployments and metrics-driven rollback with Amazon managed Service for Prometheus and Flagger](https://aws.amazon.com/blogs/opensource/performing-canary-deployments-and-metrics-driven-rollback-with-amazon-managed-service-for-prometheus-and-flagger/index.html)
- [Testing
and creating CI/CD pipelines for AWS Step Functions](https://aws.amazon.com/blogs/devops/testing-and-creating-ci-cd-pipelines-for-aws-step-functions-using-aws-codepipeline-and-aws-codebuild/index.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advrel04-bp01.html*

---

# ADVREL04-BP02 Deploy new code or resources in staggered phases, separated by sufficient time, to verify that the changes are successful

Implement gradual, phased deployments to minimize risks and
service impacts when updating systems.

## Implementation guidance

When deploying new code or resources, it is possible for
unintended results to occur. Various deployment strategies can
be used to reduce frequency and service impact.

By making changes through a blue/green deployment methodology,
you can significantly reduce the impact of any potential issues
and avoid downtime.

When a blue/green deployment isn't possible, a rolling
deployment methodology should be used to reduce the number of
resources being modified simultaneously. With a rolling
deployment, changes are made in small batches, with a
pre-determined amount of buffer time between batches. If an
issue occurs with the deployment, the unchanged resources can
continue handling traffic, avoiding downtime.

## Key AWS services

- [AWS CloudFormation](https://aws.amazon.com/cloudformation/)
- [Amazon Elastic Container Service (ECS)](https://aws.amazon.com/ecs/)

## Resources

- [Blue/Green
Deployments on AWS](https://docs.aws.amazon.com/whitepapers/latest/blue-green-deployments/welcome.html)
- [Rolling
deployments](https://docs.aws.amazon.com/whitepapers/latest/overview-deployment-options/rolling-deployments.html)
- [Deployment
methods](Users/jblatch/Downloads/%E2%80%A2%20https:/docs.aws.amazon.com/whitepapers/latest/practicing-continuous-integration-continuous-delivery/deployment-methods.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advrel04-bp02.html*

---

# ADVREL05 — Failure management

**Pillar**: Reliability  
**Best Practices**: 2

---

# ADVREL05-BP01 Perform routine evaluation of your workload's fault tolerance capabilities

Resiliency evaluations should not be considered a one-time effort,
but a continuous part of any workload's lifecycle.

## Implementation guidance

Your workload, as well as the environment (both regulatory and
partner) in which it operates, is constantly changing. Make
resilience a regular part of your feature delivery and
operational cadence throughout a workload's lifetime. Create a
living document to track evolving processes, expectations, and
improvements. Use AWS Gamedays, Well-Architected Framework
Reviews, and Support Countdown engagements to improve
reliability of advertising workloads. Coordinate with your
various advertising partners and stakeholders to perform
successful failover testing.

## Key AWS services

- [AWS Well-Architected Tool](https://aws.amazon.com/well-architected-tool/)
- [Fault
Tolerance Analyzer Tool](https://github.com/aws-samples/fault-tolerance-analyser) is an open-source
tool that focuses specifically on identifying potential
fault tolerance issues across different AWS services
- [AWS Gamedays](https://aws.amazon.com/gameday/)
- [Support Countdowns](https://aws.amazon.com/premiumsupport/aws-countdown/)

## Resources

- [AWS Countdown](https://aws.amazon.com/premiumsupport/aws-countdown/)
- [Build
Your Own Game Day to Support Operational Resilience](https://aws.amazon.com/blogs/architecture/build-your-own-game-day-to-support-operational-resilience/)
- [Best practices for handling EC2 Spot Instance interruptions](https://aws.amazon.com/blogs/compute/best-practices-for-handling-ec2-spot-instance-interruptions/index.html)
- [Using
the Fault Tolerance Analyzer Tool to Identify Potential Issues](https://aws.amazon.com/blogs/mt/using-the-fault-tolerance-analyser-tool-to-identify-potential-issues/index.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advrel05-bp01.html*

---

# ADVREL05-BP02 Create disaster recovery (DR) runbooks, and regularly test documented backup and restoration processes

Processes for backup, restoration, and failover of data should be
documented and regularly tested to validate efficacy and
understanding.

## Implementation guidance

Advertising workloads are designed for low latency when
accessing information. An unsuccessful or slow data restoration
could result in negative impact to the workload. To mitigate the
impact from data unavailability during a disaster, implement
data backup mechanisms which can quickly make necessary data
available. By documenting processes, incident response teams can
address impactful events, while validation ensures that the
processes will work when needed, and that team members are
comfortable, and confident, in performing disaster response
activities quickly.

## Key AWS services

- [AWS Elastic Disaster Recovery (DRS)](https://aws.amazon.com/disaster-recovery/) is a
service that can help design a DR solution, map applications
and networks, and build and test a DR runbook
- [AWS Config](https://aws.amazon.com/config/) can be used to continuously monitor
and record resource configurations
- [AWS CloudFormation](https://aws.amazon.com/cloudformation/) can detect drift in stacks
that have been deployed

## Resources

- [Disaster
recovery options in the cloud](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html)
- [Orchestrate
disaster recovery automation using Amazon Application Recovery Controller (ARC) and AWS Step Functions](https://aws.amazon.com/blogs/networking-and-content-delivery/orchestrate-disaster-recovery-automation-using-amazon-route-53-arc-and-aws-step-functions/)
- [Testing
disaster recovery](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/testing-disaster-recovery.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advrel05-bp02.html*

---

# ADVREL06 — Architecture capacity

**Pillar**: Reliability  
**Best Practices**: 1

---

# ADVREL06-BP01 Architect defensively against failures

Acknowledge that systems and services occasionally fail, and some
failures will come from external partners and dependencies outside
of your control.

## Implementation guidance

Most advertising systems exist in hybrid configurations, with
services and applications spanning across cloud and on-premise
infrastructure. They use mechanisms across multiple Regions or
data centers to provide high availability, scalability, and
performance.

Understand the characteristics of your application components
and how each component in a hybrid environment may impact your
system as a whole. Be familiar with the complexity of deployment
and operations across different types of environments and how
that complexity can impact overall resilience.

Instead of using internet-based connections, use AWS Direct Connect where possible to provide a consistent network
experience for critical workload networking requirements.
Implement circuit breakers, retries, and fallbacks to gracefully
handle failures from external dependencies, and prevent
cascading failures within your system. Adopt a distributed
architecture with loose coupling and asynchronous communication
patterns to isolate failures and prevent them from propagating
across the entire system.

To validate your resilience strategies and identify potential
weaknesses, regularly conduct chaos engineering experiments by
intentionally injecting controlled failures into your system.

## Key AWS services

- [Amazon Simple Queue Service (Amazon SQS)](https://aws.amazon.com/sqs/)
- [Amazon DynamoDB](https://aws.amazon.com/dynamodb/)
- [Amazon ElastiCache](https://aws.amazon.com/elasticache/)
- [AWS Lambda](https://aws.amazon.com/lambda/)
- [Amazon API Gateway](https://aws.amazon.com/api-gateway/)
- [AWS Auto Scaling](https://aws.amazon.com/autoscaling/)
- [AWS Availability Zones and Regions](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/)
- [AWS Elastic Load Balancing](https://aws.amazon.com/elasticloadbalancing/)
- [Monitoring
and alerting](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html)

## Resources

- [Architecting
for Reliability on AWS](https://aws.amazon.com/blogs/architecture/architecting-for-reliability-on-aws/)
- [Implementing
Microservices on AWS](https://docs.aws.amazon.com/whitepapers/latest/microservices-on-aws/microservices-on-aws.html)
- [Disaster
Recovery of Workloads on AWS: Recovery in the Cloud](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-workloads-on-aws.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advrel06-bp01.html*

---

# ADVREL07 — Failure and recovery

**Pillar**: Reliability  
**Best Practices**: 3

---

# ADVREL07-BP01 Design your workloads to withstand failures of individual components, such as compute instances, queues, databases, and caches

Build building resilient advertising systems by identifying
critical components, and implement fault tolerance through
cell-based architectures and distributed resources across
Availability Zones.

## Implementation guidance

Determine which components of your workload are in a critical
path to maintain operations for real-time bidding, ad serving,
and other crucial functions. Identify AWS services that provide
built-in fault tolerance mechanisms which are within your
workload's response time, RTO, and RPO targets. Use cell-based
architectures, with resources spread across multiple
availability zones, to reduce the scope of a disruptive event.
Where consistent communications are necessary, implement static
stability mechanisms to reduce the dependency on control plane
actions.

## Key AWS services

- [Amazon Simple Queue Service (Amazon SQS)](https://aws.amazon.com/sqs/)
- [Amazon DynamoDB](https://aws.amazon.com/dynamodb/)
- [Amazon ElastiCache](https://aws.amazon.com/elasticache/)
- [AWS Lambda](https://aws.amazon.com/lambda/)
- [Amazon API Gateway](https://aws.amazon.com/api-gateway/)
- [AWS Auto Scaling](https://aws.amazon.com/autoscaling/)
- [AWS Availability Zones and Regions](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/)
- [AWS Elastic Load Balancing](https://aws.amazon.com/elasticloadbalancing/)
- [Monitoring
and Alerting](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html)

## Resources

- [Reducing
the Scope of Impact with Cell-Based Architecture](https://docs.aws.amazon.com/wellarchitected/latest/reducing-scope-of-impact-with-cell-based-architecture/reducing-scope-of-impact-with-cell-based-architecture.html)
- [Static
stability using Availability Zones](https://aws.amazon.com/builders-library/static-stability-using-availability-zones/)
- [Control
planes and data planes](https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/control-planes-and-data-planes.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advrel07-bp01.html*

---

# ADVREL07-BP02 Implement a backup strategy which would meet RTO and RPO objectives

Develop comprehensive backup strategies, focusing on data
classification and meeting Recovery Time Objective (RTO) and
Recovery Point Objective (RPO) requirements through appropriate
service selection.

## Implementation guidance

Review the data related to your workload and classify the data
according to usage, retention, and availability needs. Example
classifications might be user profile info, campaign data,
reporting data. Consider how those different data classes are
used within your workload and how the availability of that data
can impact your workload's operation. Use those classifications
to determine the RPO and RTO requirements for your workload.
Identify the AWS services that can meet your requirements, and
deploy resources to the Regions or Availability Zones that can
achieve your RTO and RPO targets. Test the backup and
restoration process to verify that your backup and recovery
strategies will work during a disruptive event.

## Key AWS services

- [AWS Backup](https://aws.amazon.com/backup/)
- [Amazon EBS](https://aws.amazon.com/ebs/)
- [Amazon EC2](https://aws.amazon.com/ec2/)
- [Amazon Relational Database Service](https://aws.amazon.com/rds/)
- [Amazon Elastic File System](https://aws.amazon.com/efs/)

## Resources

- [Disaster
Recovery (DR) Architecture on AWS, Part II: Backup and Restore with Rapid Recovery](https://aws.amazon.com/blogs/architecture/disaster-recovery-dr-architecture-on-aws-part-ii-backup-and-restore-with-rapid-recovery/index.html)
- Establishing
RPO and RTO Targets for Cloud Applications

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advrel07-bp02.html*

---

# ADVREL07-BP03 Back up data in multiple locations with consideration for your regulatory or legal requirements

Back up data in multiple locations, and consider how consumer privacy laws may impact your data replication and storage plans.

## Implementation guidance

Select AWS Regions for backup locations that satisfy your legal
and business requirements. Consider how consumer privacy laws may impact your ability to replicate data which
could contain personal data. Be
aware of how countries where your workload operates regulate
advertising and related data, and seek legal consultation when
you are unsure of how regulations might apply to your workload.
Use your understanding of those regulations to select AWS
services and Regions. Seek legal counsel when in doubt.

## Key AWS services

- [AWS Backup](https://aws.amazon.com/backup/)
- [AWS Key Management Service (KMS)](https://aws.amazon.com/kms/)

## Resources

- [Cloud
security guidance](https://www.ncsc.gov.uk/collection/cloud)
- [Protecting
your data with backups](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/using-backups.html)
- [Amazon DynamoDB now helps you meet regulatory compliance and business continuity requirements through enhanced backup features in AWS Backup](https://aws.amazon.com/about-aws/whats-new/2021/11/amazon-dynamodb-requirements-aws-backup/index.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advrel07-bp03.html*

---

# ADVREL08 — Privacy

**Pillar**: Reliability  
**Best Practices**: 3

---

# ADVREL08-BP01 Design resilient architectures with privacy-preserving fault tolerance

Build resilient architectures that maintain data privacy in multi-party collaborations, focusing on fault-tolerant AWS Clean Rooms deployment, encrypted failover mechanisms, and privacy-preserving disaster recovery procedures.

## Implementation guidance

- Deploy AWS Clean Rooms across multiple Regions with
replicated privacy policies, differential privacy budgets,
and encrypted collaboration configurations to facilitate
continuous privacy-protected analytics during regional
outages.
- Configure automatic failover for AWS Clean Rooms and Nitro
Enclaves with cross-Region KMS key access, synchronized
IAM roles, and validated privacy control restoration to
maintain cryptographic isolation and data protection
during service transitions.
- Implement privacy-aware error handling for data matching
with encrypted retry queues, failed operation logging that
preserves anonymity, and automatic termination of
computations that cannot maintain privacy guarantees
during processing errors.
- Deploy circuit breakers with privacy validation that
fail-closed when privacy controls cannot be verified,
monitor differential privacy budget exhaustion, and halt
operations when cryptographic attestation fails in
dependent services.
- Monitor AWS Clean Rooms privacy metrics including query
result threshold compliance, privacy budget consumption
rates, unauthorized access attempts, and cryptographic
operation health with automated alerts for privacy policy
violations.
- Use encrypted dead-letter queues for failed matching
operations with privacy context preservation, secure
purging policies for expired operations, and manual review
processes that maintain data anonymization during failure
analysis.
- Automate backup of privacy-protected datasets with
cross-Region encrypted replication, privacy policy version
control, differential privacy state preservation, and
recovery procedures that validate privacy controls before
data restoration.

## Key AWS services:

- AWS Clean Rooms
- Amazon Route 53
- AWS Auto Scaling
- Amazon EventBridge

## Resources

- [Reliablity Design principles](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/design-principles.html)
- [Disaster recovery best practices](https://docs.aws.amazon.com/clean-rooms/latest/userguide/disaster-recovery-resiliency.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advrel08-bp01.html*

---

# ADVREL08-BP02 Maintain data consistency and availability across collaboration workflows

Data consistency and availability is critical when working with multiple stakeholders or workflows. Implement tools like versioning, logging, and health checks to verify that data remains consistent and available.

## Implementation guidance

- Implement versioning for collaborative datasets and
schemas.
- Use transaction logs for tracking privacy computation
state.
- Configure cross-Region replication for critical data
stores.
- Implement idempotency for matching operations.
- Set up health checks for collaboration service endpoints.
- Use read replicas for high-availability data access.
- Configure automated rollback procedures for failed
operations.

## Key AWS services

- Amazon DynamoDB
- Amazon S3
- AWS Lambda
- Amazon CloudWatch

## Resources

- [Guidance for Maximum Data Availability Architecture on AWS](https://aws.amazon.com/solutions/guidance/maximum-data-availability-architecture-on-aws/)
- [CAP theorem](https://docs.aws.amazon.com/whitepapers/latest/availability-and-beyond-improving-resilience/cap-theorem.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advrel08-bp02.html*

---

# ADVREL08-BP03 Implement secure and privacy-preserving recovery mechanisms for collaboration workloads

Ad data requires security and preservation of privacy. Implement tooling and systems that preserve secure data and avoid privacy breaches when collaborating with first and third parties, and verify that you have disaster recovery and automated backup mechanisms in place.

## Implementation guidance

- Design recovery procedures that maintain data encryption
throughout the process.
- Implement point-in-time recovery for privacy-protected
datasets.
- Configure automated backup verification with privacy
controls intact.
- Set up secure backup encryption key rotation policies.
- Establish recovery time objectives (RTOs) aligned with
privacy requirements. This is because privacy requirements
can significantly extend RTOs by adding mandatory
verification and security steps.
- Implement secure state management for interrupted privacy
computations. For example, if encryption fails during
recovery, then halt the process rather than expose data;
if privacy controls can't be verified then deny access
until controls are restored; If secure state can't be
maintained then terminate the computation safely
- Create automated disaster recovery testing procedures.

## Key AWS services

- AWS Backup
- AWS KMS
- AWS Secrets Manager
- Amazon S3

## Resources

- [Data protection](https://docs.aws.amazon.com/whitepapers/latest/aws-caf-security-perspective/data-protection.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advrel08-bp03.html*

---

# ADVREL09 — Ad measurement and verification

**Pillar**: Reliability  
**Best Practices**: 2

---

# ADVREL09-BP01 Implement redundant ad-verification systems with automated failover mechanisms

Implement redundant ad-verification systems with automated failover capabilities. Use multiple verification providers and automated monitoring for continuous, reliable advertising measurement and validation.

## Implementation guidance

- Deploy multiple third-party verification providers for
cross-validation
- Implement automated failover mechanisms for measurement
systems
- Use data quality checks and anomaly detection
- Maintain backup measurement methodologies
- Configure automated retry mechanisms for failed
measurements
- Implement circuit breakers for degraded third-party
services
- Set up monitoring and alerting for measurement system
health

## Key AWS services

- Amazon CloudWatch
- AWS Lambda
- Amazon EventBridge
- AWS Step Functions
- Amazon DynamoDB

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advrel09-bp01.html*

---

# ADVREL09-BP02 Establish robust data collection and validation pipelines for measurement accuracy

Build reliable data collection and validation pipelines, emphasizing real-time monitoring, automated reconciliation, and recovery procedures to maintain measurement accuracy in advertising systems.

## Implementation guidance

- Implement data validation at collection points
- Set up real-time data quality monitoring
- Create automated data reconciliation processes
- Configure dead letter queues for failed events
- Implement idempotent processing for measurement events
- Establish clear data freshness SLAs
- Deploy automated data recovery procedures

## Key AWS services

- Amazon Kinesis
- Amazon SQS
- Amazon S3
- AWS Glue
- Amazon EMR

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advrel09-bp02.html*

---

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
