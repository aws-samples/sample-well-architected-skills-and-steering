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
