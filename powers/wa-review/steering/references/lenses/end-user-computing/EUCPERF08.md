# EUCPERF08 — Process and culture

**Pillar**: Performance Efficiency  
**Best Practices**: 4

---

# EUCPERF08-BP01 Establish and monitor service metrics and KPIs

When using an AWS EUC service to deliver a service to your users, it's important to
consider the service metrics that are key to the delivery of the service for your
organization to verify that the service is operating at the required service levels.

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

Determine service metrics and KPIs for your service. Some examples of key measures to
consider are:

- Service availability
- Mean time to repair (MTTR)
- First call resolution (FCR)
- SLA breach rate
- User and customer satisfaction (CSAT)
- Cost per contact
- Net promoter score
- Incident volume
- Problem resolution time

Consider how metrics available within the AWS EUC services outlined in the
following sections can be used to support or determine your service metrics.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucperf08-bp01.html*

---

# EUCPERF08-BP02 Monitor Amazon WorkSpaces Applications CloudWatch metrics

Use Amazon CloudWatch to establish and monitor your WorkSpaces Applications workload's performance against
the KPIs established for your service. [Use the Automatic
dashboard](https://docs.aws.amazon.com/workspaces/latest/adminguide/cloudwatch-dashboard.html) in Amazon CloudWatch to monitor your fleet capacity over time or consider
creating a custom dashboard tailored to your environment.

**Level of risk exposed if this best practice is not
established:** Low

## Implementation guidance

Measure your workload's performance across [Amazon AppStream
2.0 fleets and fleet instances](https://docs.aws.amazon.com/appstream2/latest/developerguide/monitoring-with-cloudwatch.html).

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucperf08-bp02.html*

---

# EUCPERF08-BP03 Monitor Amazon WorkSpaces Personal CloudWatch metrics

Use CloudWatch to establish and monitor your Amazon WorkSpaces workload's performance against these
KPIs and requirements.

**Level of risk exposed if this best practice is not
established:** Low

## Implementation guidance

Monitor the Amazon WorkSpaces service and instances using Amazon CloudWatch. Use the guidance provided
in the following articles to measure your workload's performance.

- [Monitor your WorkSpaces using CloudWatch metrics](https://docs.aws.amazon.com/workspaces/latest/adminguide/cloudwatch-metrics.html)
- [Creating custom Amazon CloudWatch dashboards and widgets for Amazon WorkSpaces](https://aws.amazon.com/blogs/desktop-and-application-streaming/creating-custom-amazon-cloudwatch-dashboards-and-widgets-for-amazon-workspaces/)
- [Monitor your WorkSpaces health using the CloudWatch automatic dashboard](https://docs.aws.amazon.com/workspaces/latest/adminguide/cloudwatch-dashboard.html)
- [Utilizing CloudWatch Internet Monitor with Amazon WorkSpaces](https://aws.amazon.com/blogs/desktop-and-application-streaming/utilizing-cloudwatch-internet-monitor-with-amazon-workspaces-personal/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucperf08-bp03.html*

---

# EUCPERF08-BP04 Monitor operating system metrics

Operating systems can add significant variations in performance to your Workload
depending on the compute, storage, and memory resources required. Test with all operating
systems that are intended to be supported by your deployment.

**Level of risk exposed if this best practice is not
established:** Low

## Implementation guidance

Monitor the performance of instances delivering end user services.

- Use operating system metrics such as Windows Performance Counters for detailed
insight into instance performance.
- [Use
the EUC Toolkit to manage Amazon WorkSpaces Applications and Amazon WorkSpaces](https://aws.amazon.com/blogs/desktop-and-application-streaming/euc-toolkit/).
- For ongoing monitoring and analysis, consider using the [Amazon Kinesis Agent for Windows](https://docs.aws.amazon.com/kinesis-agent-windows/latest/userguide/what-is-kinesis-agent-windows.html) to monitor Windows Performance Counters for
performance trend analysis of key system metrics.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucperf08-bp04.html*

---
