# Operational excellence

**Pages**: 3

---

# Preparation

Load testing builds confidence in your infrastructure design
before a large event and highlights weaknesses early. When
possible, use historical data to model and test system load. For
example, if you’ve acquired content streaming rights, but a
similar show or event has aired in the past, Nielsen or Comscore
data can provide useful estimates for peak concurrent viewers.
With this model, you can develop accurate load tests that
simulate real-world conditions. Be sure to test both individual
service components *and* the end-to-end
system with load tests that emulate end user clients.

SM_OPS1: How do you prepare for large-scale streaming media events?

**SM_OBP1 – Ensure that your content delivery
infrastructure can scale to the expected demand**

**SM_OBP2 – Evaluate and adjust Service Quotas to match your workload’s needs in
advance**

**SM_OBP3 – Engage with AWS Support programs to assist with events**

For origin services, estimate load in Transactions Per Second
(TPS) or Requests Per Second (RPS). We advise that you estimate
peak TPS the player devices will generate based on the usage
pattern, layers of caching, and unique nature of your audience.

For example, for an HLS stream with 6-second segments and
un-muxed video, audio, and captions, each player will generate
one TPS (= 3*1/6 TPS for video, audio, and caption manifest
requests + 3*1/6 for video, audio, and caption segment requests)
to the CDN. Assuming a 95% cache hit ratio (CHR) for the CDN, it
will result in 0.05 TPS (=1*(1-0.95)) to the origin. To
calculate peak TPS to the origin, multiply the peak number of
player devices expected at any time with 0.05 TPS.

For DASH streams, the TPS depends on how frequently the DASH
player requests the manifest and segments. A common practice is
to request once every segment length. Note, that all DASH
segments are unmuxed, that is, the player will request a video,
audio, and caption segments each time. So, for a 6-second
segment, the TPS would be 0.66 TPS (= 1/6 for manifest + 3*1/6
for video, audio and caption segments). Again, assuming a 95%
cache hit ratio (CHR) for the CDN, that would result in 0.033
TPS (=0.66*(1-0.95)) to the origin. Based on the forecast for
peak concurrent HLS and DASH playback sessions, peak TPS for the
origin can then be calculated.

You can use the following TPS formulas to guide your
estimations, but, when available, always use your own metrics
and data to forecast usage.

**Streaming Protocol**

**TPS Formula**

HLS

Peak audience x (2 x (Number of elementary stream
segments)/(segment length)) x (1-CHR)

DASH

Peak audience x (4/(segment length)) x (1-CHR)

*Estimating transactions per second for common
streaming media protocols*

For HLS, the number of elementary stream segments depends on
whether the video, audio, and caption date is muxed in one
segment or unmuxed in separate segments. In case of muxed
segments, there is only one elementary stream segment whereas in
the case of unmuxed segments, there are three elementary stream
segments.

AWS Cloud can handle very large scale streaming events. However,
services have soft limits in place to protect customers from
inadvertently scaling resources beyond their needs and racking
up unnecessary costs. Service quotas (also referred to as
limits) for all media services are Region-specific unless
otherwise noted in the documentation. For more information about
the quotas for a specific service, refer to its documentation.

You can centrally manage Service Quotas for all services in your
account using
[Service Quotas](https://console.aws.amazon.com/servicequotas) in the **AWS Management Console** where you can view your current quotas and
also request increases. If you don’t find your AWS service in
Service Quotas, contact AWS Support to increase them. Provide
details of the Regions in which your workflow will operate,
usage patterns, and timeframe.

Consider using Infrastructure and Event Management (IEM) and
Media Events Management programs for large-scale live events
that might require immediate support during an event. By
engaging AWS through these programs, you enable AWS experts to
become familiar with your workload, provide architectural and
operational guidance, and real-time support for your planned
event.

In addition to IEM, Enterprise Support customers are eligible
for a Cloud Operations Review and a Well-Architected Framework
Review designed to help identify risks in your cloud operations.
This cross-team engagement helps establish a common
understanding of your workload and helps AWS contribute to your
streaming events. You can always perform your own architecture
review for any workload by using the
[AWS Well-Architected Tool](https://console.aws.amazon.com/wellarchitected) in the AWS Management Console.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/streaming-media-lens/preparation.html*

---

# Operations

AWS enables visibility into your streaming workload at all
layers through log collection and monitoring features. Data on
use of services, resources, application programming interfaces
(APIs), network flow logs, and system traces can be collected
using **Amazon CloudWatch**,
**AWS CloudTrail**,
**VPC Flow Logs**, and
**AWS X-Ray**. Equipped with this
data, you can design automated failure and remediation systems
at each stage in your video application – ingest, processing,
origin, delivery, and client-side.

For live streaming, expressing the component relationships and
tracing the signal path is important for operators who need to
identify and respond to issues that arise. Visual documentation
or interactive dashboards that reflect the real-time status of
the workflow will improve awareness and shorten time to issue
resolution. Consider using or building your own tools like the
[Media
Services Application Mapper](https://aws.amazon.com/solutions/implementations/media-services-application-mapper/) to model your workload and
better inform operations.

One unique property of media streaming is that while every
component in the workload can be operating as expected, the
resulting audio or video might not be the intended content.
Consider placing video decoder probes throughout your live
stream signal path to emit thumbnail images or low bitrate proxy
media to monitoring systems. This will ensure that the correct
content is being transmitted and improve operational
observability for troubleshooting.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/streaming-media-lens/operations.html*

---

# Resources

Refer to the following resources to learn more about AWS best
practices for operational excellence.

## Documents

- [Infrastructure
Event Management](https://aws.amazon.com/premiumsupport/iem/)
- [Load
Testing CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/load-testing.html)
- [Media
Services Application Mapper](https://github.com/awslabs/aws-media-services-application-mapper)
- [Monitoring
AWS Media Services using Amazon CloudWatch Events](https://aws.amazon.com/blogs/media/monitoring-aws-media-services-using-amazon-cloudwatch-events/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/streaming-media-lens/resources-opex.html*

---
