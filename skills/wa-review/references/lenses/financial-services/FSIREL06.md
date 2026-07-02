**Pillar**: Reliability

# FSIREL06: To mitigate operational risks, can your workload owners detect, locate, and recover from gray failures?

Failures, such as loss of network connectivity, is often considered in a binary
nature where the connectivity is functioning normally or not functioning at all. However
there are non-binary failures called *gray failures*, which are
defined by the characteristic of differential observability, meaning that different
entities observe the failure differently. Gray failures can be subtle and difficult to
detect. An example of a gray failure with network connectivity is a 40% packet loss of
all TCP packets over a network link. Another example is intermittent failure on one or
more servers behind a load balancer where some requests fail, but not enough to initiate
the load balancer's health check. Overall service health metrics may be based on
aggregate metrics, such as average response time from the load balancer, which may
obscure localized failures.

## FSIREL06-BP01 Monitor indicators aside from system metrics that can signal client impairment

Capture data that measures the experience of your workload's clients to understand
when anomalies are affecting the customer experience with a workload function. Such
measures are often collected as percentiles to prevent outliers when trying to
understand the impact over time and how it's spread across your workload's clients.
Examples of such metrics may be the 99th percentile of latency from the load balancer,
a deviation in the number of requests being received over time, or the number of
unsuccessful responses returned to the client. Highly visible workload owners should
also have a means to monitor sudden increases in inbound customer support requests,
and complaints on social media channels. Have a way for users to send feedback
directly from within the service, or adjacent channels that can be monitored by
service owners in near real-time.

## FSIREL06-BP02 Have a way to find outliers hiding in aggregate metrics

Wherever system dashboards and monitors are reporting on aggregate results across
a fleet of resources, be sure that system operators can also break out metrics and
find outliers. Use tools like [Amazon CloudWatch Contributor
Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContributorInsights.html) and [CloudWatch RUM](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM.html) to be able to ask
questions like: "Who are the top 10 clients with high error rates?" And: "Do those top
10 clients share a common root cause?"

## FSIREL06-BP03 Use anomaly detection to detect unusual changes in user engagement metrics

FSI workload owners should monitor for anomalies in metric data such as the
number of user requests that receive a timely and successful response, and user
session dropout rates (the number of users that began a multi-step process, such as a
payment flow, but didn't finish). With Amazon CloudWatch you can enable anomaly detection on
various metrics, which continually analyzes the metrics, determines normal baselines, and
surfaces anomalies that can in turn be used to initiate a CloudWatch alarm.

## FSIREL06-BP04 Have a way to manually route away during failure

There may be a need to fail away from a primary system to its secondary, either
because a system that depends on your workload needs to failover, or due to an
unexpected, undetected impact to your primary system. In such cases you may need to
manually override the status of health checks and route traffic away from the sources
of a gray failure. You can use services such as [Route 53 Application Recovery
Controller](https://aws.amazon.com/route53/application-recovery-controller/) and its feature [zonal shift](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.html) with routing
controls. Also consider having a way to manually control and override the responses
from each health check target, providing you with full control when a workload is
considered unhealthy and initiated to route around the faulty resources.

## FSIREL06-BP05 Establish baselines for expected network traffic

To understand conditions of high or unexpected network traffic, you must
establish a steady state of metrics for the expected data flows between your workload
and its users as well as between the components within your workload. This baseline
should initiate an operational response when a workload is suddenly seeing abnormal
traffic throughput that exceeds the expected steady state ranges. Understanding the
steady state is key in creating the knowledge of normal communication patterns between
and within the workload components. Knowing which network communications patterns are
outside of normal ranges helps operations teams troubleshoot and isolate impacted
components.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsirel06.html*
