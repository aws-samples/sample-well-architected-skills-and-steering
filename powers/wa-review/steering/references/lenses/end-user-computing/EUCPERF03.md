# EUCPERF03 — Architecture selection

**Pillar**: Performance Efficiency  
**Best Practices**: 1

---

# EUCPERF03-BP01 Consider modernization of backend services to use managed services from AWS for best performance

By using AWS EUC services, you are already taking advantage of the reduced
infrastructure and management overheads of maintaining your own environment. Taking the same
approach to other backend services which support the EUC deployment can further increase
operational efficiency.

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

Review the backend services required for your AWS EUC deployment, and determine if
transitioning to managed service equivalents from AWS might improve performance,
simplify cost modelling, and reduce the administrative and support overheads of delivering
these in-house. Examples include:

- **Amazon FSx for Windows File Server**: Resilient, high performance file
shares, user data storage and profile management.
- **Amazon RDS**: A range of high-performance managed SQL
services.
- **Amazon CloudWatch**: Insight into operational metrics and
alerting to maintain performance and efficiency.
- **AWS CloudTrail**: Records logs that provide insight into
activities undertaken within an AWS account.

Reduce the overhead of managing your own infrastructure, and invest the time saved to
perform continual service improvement, increasing the performance efficiency of your EUC
deployment.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucperf03-bp01.html*

---
