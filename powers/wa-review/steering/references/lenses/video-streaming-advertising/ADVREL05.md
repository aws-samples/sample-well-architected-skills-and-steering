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
