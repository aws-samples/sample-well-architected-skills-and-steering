# Reliability

**Pages**: 5

---

# Foundations

See the AWS Well-Architected Framework whitepaper for best
practices in the **Foundations**
area for Reliability within streaming media applications.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/streaming-media-lens/foundations.html*

---

# Workload architecture

SM_REL1: How does your streaming infrastructure withstand failures in ingest,
processing, origination, or delivery components?

**SM_RBP1 – Document all workload dependencies and expected
viewer experience in the event of component failure**

**SM_RBP2 – Design live streaming ingest architecture to
withstand source failure by ingesting redundant video signals that take diverse
network paths to AWS**

**SM_RBP3 – Design live streaming workflow to withstand
individual processing and origination failures by implementing redundant video
pipelines**

Closely examine both hard and soft service dependencies to ensure that failure
conditions are well understood. Engage directly with service partners to understand failure
conditions *before* issues arise. If problems do occur, notify the end
user and protect their experience by offering alternate content. Use postmortems to learn
from experiences and develop action plans.

Examples of hard dependencies in a streaming media workload include:

- Signal contribution path (Live)
- Media processing (Live)
- Media origin
- Digital rights management (DRM) and authentication

Examples of soft dependencies in a streaming media workload
include:

- Content management systems
- Ad insertion and splicing
- Analytics
- Content Delivery Network (load dependent)

For example, if your ad-insertion platform experiences an
availability outage, systems should fall back to an underlying
origin source or have a process in place to remove ad insertion.
This might decrease the revenue earned in the short term, but
would retain service up-time and your audience satisfaction.

Every business will have to trade off the cost of reliably
streaming content with any failure conditions that arise. We
recommend reviewing the
[Well-Architected
Reliability Pillar whitepaper](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html) to help you calculate your
reliability target and the hard and soft dependencies of your
workload.

**Live resilient design**

To achieve a highly available media streaming workflow, it is
important to design for redundancy in every component of the
chain. Let’s consider the components in a live workflow and the
network paths between them:

*End-to-end redundant Live workflow*

A failure in either the video signal or the network path that it
takes to reach AWS Cloud impacts the entire workload and
subsequently the end customer experience. Design your live video
ingest architecture to withstand individual source failure by
ingesting redundant video signals that take diverse network
paths to AWS.

For example, in the preceding architecture, Source A and Source
B are redundant input mezzanine sources. The contribution
encoder is designed to fail over between the redundant sources
in case of signal loss. To protect against failure of the
contribution encoders, ensure that there are redundant
contribution encoders in different physical on-premises
locations. Each contribution encoder outputs two sets of
contribution feeds, each with a binary identical SMPTE 2022-7
compliant network packet streams (represented by the same color
arrow lines). This allows for transmission over separate network
routes so if packets from one route are lost, the data can be
reconstructed using packets from the second stream (as depicted
by the Network Packet Failover component).

**AWS Direct Connect** can be
used to provide dedicated network paths and
**AWS Elemental MediaConnect**
Flows can be used to reliably transport the feeds and provide
failover at the network packet level compliant to SMPTE 2022-7
specifications. This design provides for full ingest redundancy
across source signals and network paths.

Distribution encoding can be impacted by infrastructure issues,
degradation of a dependent source, or by factors locally within
the component. To achieve distribution encoder pipeline
redundancy, ensure that the input source is being processed in
at least two redundant locations within a Region. In the
preceding architecture diagram, a distribution encoder in each
Region is receiving two redundant input sources and processing
them in separate AZs. Consider replicating the processing
pipeline into an additional Region if your reliability targets
warrant it.

With **AWS Elemental MediaLive**,
a standard channel creates two redundant encoding pipelines (one
in each AZ) with the option to provide redundant input sources
with configurable failure scenarios. This allows you to
architect a workload that can seamlessly fail between inputs
while maintaining the integrity of the stream being published to
the origin. By providing embedded timecode in your sources, you
can prevent input failures from impacting the viewer experience
through the MediaLive pipeline locking feature. If the input to
MediaLive does not have valid timecode, the channel still
remains highly available but without seamless failover.

It’s a best practice to deploy redundant origin services in
Multi-AZ or multi-Region and in case of an origin failure,
reroute affected traffic. You can monitor origin health metrics
and make real-time traffic routing decisions through DNS-based
failover or CDN health checks. Alternatively, you can present
all origin options to the player within the ABR manifest and
implement client conditions for switching. In addition to the
full outage failures, it is also important to protect against
transient failures like high request latencies or timeouts.

For availability, performance, and geographic coverage reasons,
it is common to deliver content using multiple CDNs. Doing so
helps in distributing the traffic based on geolocation and
available capacity. It also protects against failure or
over-subscription in one or more CDN PoPs. It is recommended to
collect near-real time QoS data (error rates, buffer rates,
latency, etc.) from CDNs to determine the best delivery path for
your customers and award traffic to best performing CDN. You may
also load balance across CDNs based on other business
considerations like cost.

**VOD resilient design**

As described in the scenarios section, VOD processing typically
uses a serverless state machine comprised of event sources,
messaging services, and subscribers to perform various
operations. These operations should always be idempotent and
designed so that when operations receive messages more than once
or run multiple times, they do not negatively impact the state
of the workload. Dead-letter queues and distributed tracing
services like AWS X-Ray can help you identify problematic
messages or functions in your workflows as you scale.

The non-real-time nature of VOD provides you with the
flexibility to decouple the batch Ingest and Processing
components from Delivery and Playback. Thus, there are two
approaches for reliable VOD design:

**VOD origin reliability** — In
this scenario, your business objectives require that viewers can
play content in the event of a workload failure, but allow for
an interruption in the ability to publish new content to your
platform. This is typical for platforms that publish a
relatively small amount of new content on a daily or weekly
basis. After content is ingested and processed, it’s published
and redundantly copied to multiple origin services. Technologies
such as **Amazon S3 Cross-Region
Replication (CRR)** can automate this function.

Once content is securely stored in multiple delivery endpoints,
the CDN or client device can attempt playback from an alternate
origin if playback from the primary endpoint fails. This
architecture necessitates that the key delivery, authentication,
content management, and other application layer services be
reachable in the event of a failure.

**VOD processing and origin
reliability** — In this scenario, the full application
functionality must remain available in the event of an
interruption. This includes the ability to ingest and process
new content. This is achieved through a multi-Region design
where the streaming architecture is replicated across two AWS Regions and CDNs, client logic, and DNS is used to route
requests between Regions. In this scenario, care must be taken
when designing the underlying storage and persistence layers
(for example, databases and caching) to ensure consistency
between Regions.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/streaming-media-lens/workload-architecture.html*

---

# Change management

In a traditional streaming media environment, major changes are
performed infrequently during maintenance windows with manual
processes. This is high-risk as the people, processes, and tools
used to update infrastructure are infrequently used. This can
lead to drift in documentation and institutional knowledge of
the workload.

We encourage you to automate deployments, testing, and rollbacks
using services like AWS CloudFormation. This enables teams to
make small, frequent changes on a regular basis and ensure that
the infrastructure state is represented in code, managed in
version control, and that your processes used for change
management are well tested. To make troubleshooting issues
easier, we also recommend creating a consistent naming
convention for the components that make up the workflow, for
instance, name the component with identifiers for asset, service
Region, and AZ.

SM_REL2: How does your streaming media workload adapt to viewer demand?

**SM_RBP4 – Use a CDN and plan capacity with your
providers**

**SM_RBP5 – Design your origin service to automatically
scale to meet viewer demand**

The relationship between the client requests, delivery caching,
and origin scaling is the most important area to examine when
scaling your streaming media workload. Ingest and Processing
components are scaled out in advance or run in batch before
being made available for viewers and demand has no impact on
these components.

A Content Delivery Network (CDN) is necessary to scale
infrastructure for streaming media. CDNs provide multiple
benefits by reducing the load on backend origination services,
improving end-user performance, and lowering cost. By caching
requests at the edge and within the CDN network, viewers are
served directly from caches nearest them and requests to your
origin server are dramatically reduced.

When considering which CDN to use, use the CDN’s network
infrastructure presence in the geographical areas where your
viewers are located. While most CDNs offer coverage for viewers
in the US and Europe, platforms with large number of viewers in
Asia, Africa, or Latin America should be especially cognizant of
the points of presence and network capacity of their CDN in
those Regions and even consider a multi-CDN approach.

To achieve petabyte delivery scale, improve performance, or
respond to intermittent delivery network issues, streaming media
architectures might consider a multi-CDN delivery strategy. With
multiple CDNs, you award or weight traffic to specific
distribution networks based on current performance for a
specific user or geographic Region – providing optimal viewing
experience. Before you take this approach, consider the
following trade-offs when compared to a single CDN approach:

- **Increased Origin Load** —
With multiple CDNs, you will have more caches to populate
with content. This will result in a lower Cache-Hit-Ratio
and increase the****load
to origination services. Some of this load can be offset
through an origin shield component.
- **Increased Cost** — Many
CDNs offer tiered pricing based on utilization. By using
multiple CDNs, you might not have access to lower pricing
tiers.
- **Operational Overhead** —
Deployment, testing, and the operation of multiple CDNs
adds operational overhead.
- **Lack of Feature Parity**
— Implementation might be hindered by the lack of feature
parity across CDNs. This situation could introduce new
requirements for your infrastructure and even reduce
performance.

One approach to multi-CDN uses DNS resolution to apply a
weighted round-robin distribution across CDNs. This is common
for organizations looking to distribute load to meet capacity
requirements, to meet cost commitments, or to minimize blast
radius of CDN outages. This can be accomplished using
**Amazon Route 53** by defining
multiple record sets with a “Weighted” routing policy and the
desired weight.

A DNS-based configuration is easy to implement and can be
changed periodically to reflect network conditions, but DNS
changes don’t propagate quickly and some systems do not honor
TTL values. For live events, where client playback buffers are
small and network degradation can cause immediate impact, we
recommend a dynamic HTTP-based approach that specifies a CDN
during initialization of a playback session.

Adaptive Bitrate (ABR) protocols function by serving a manifest
with pointers to media segments representing the elementary
streams of audio and video data. With HTTP-based evaluation and
routing, client content requests are served playback manifests
that reference objects hosted by one or more CDNs. By serving
customized manifests, you can target specific devices,
geographies, or ISPs with prescriptive CDN. You can maintain CDN
redundancy by providing alternative content URIs within the
manifest, weighting them, and implementing failover logic within
the player.

Regardless of approach, using multiple CDNs will increase load
on origin services because each CDN will have its own caching
network and requests to satisfy. To minimize the number of
requests hitting origin services directly, you should optimize
the content TTL, enable each layer of caching available, and use
an origin shield service that can collapse requests from
multiple CDNs into a single request to your origin layer.

As client requests come through the CDN, the origin layer must
elastically respond to meet viewership demand. Implement your
origin service within Auto Scaling groups, across multiple
Availability Zones, and behind Application Load Balancers to
ensure high availability. To determine the additional demand
back to the origin, refer to the Performance Pillar in this
paper to estimate load and inform scaling needs.

For best practices in change management, refer to the
[Reliability
Pillar](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html) whitepaper.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/streaming-media-lens/change-management.html*

---

# Failure management

SM_REL3: How does your streaming infrastructure respond to or heal from
failures in origination or delivery components?

**SM_RBP6 – Design your streaming media workflow to
automatically distribute traffic to redundant origins**

**SM_RBP7 – Monitor live streaming manifests for expected
segment update patterns and to alert on staleness**

The origin component exposes content endpoints and is at the
heart of the streaming media workload. Managing failure must
start with an evaluation of the failure scenarios that can be
introduced at the origin component. An origin can fail to serve
content due to issues with upstream dependencies or due to
internal service failure cases. The most effective way of
managing upstream failures is to introduce component-level
redundancy so that upstream failures do not impact the health of
the origin. Internal service failures should be managed by
routing traffic to alternate origin resources through manifest
re-writes, CDN origin traffic redirection, or client-side
heuristics.

When managing an origin failure event during a live stream, you
either introduce a discontinuity in the stream or design for
seamless failover. In either case, the goal is to continue
playback with minimal impact to the viewer. To achieve seamless
playback, redundant packagers (encoder or origin) must serve
content that is segment aligned. This means that all streams
must present content that is aligned across segment boundaries,
sequencing, and media properties (PTS). This is possible when
redundant packagers are time synchronized. If this is not
supported by your packager or you are unable to synchronize the
packagers, segments won’t contain the same content and the
player might need to reset the decoder to continue playback
during failover. Some players can handle this gracefully without
input from the user, while others require a player reset in
order to continue. Failure logic implemented in the player
should always strive to continue playback in the event of a
discontinuity without interaction from the user.

There are many ways to implement failover depending on your
architecture and business requirements. One common approach,
often used for video-on-demand assets and other static assets,
is to use origin failover logic provided by a CDN. Origin health
check implementations are transparent to the client, easy to set
up, and typically work by redirecting traffic to alternate
origins when requests from primary origin respond with failure
codes or take too long.

CDN origin failover heuristics may not be sufficient for live
streaming because frequent manifest updates are made as the
stream progresses and we also need to monitor and trigger
failovers based on the health of these updates.  If a live
stream manifest returned back from the origin does not advance
in the expected real-time cadence players will re-buffer or halt
playback completely, compromising playback experience. In
addition to 4xx, 5xx errors, and high response latencies, you
should design origin monitoring to alert on stale live
manifests. The heuristics used to detect manifest staleness will
depend on the configuration of your stream segment size and the
client playback buffer size. For example, you might consider
rerouting requests to healthy origins if the manifest remains
unchanged for 2x – 5x segment size (4 – 10 seconds for a
2-second segment). When using **AWS Elemental MediaStore** as your live streaming origin,
you can configure a Transient Data Policy on your container via
the Object Lifecycle Policy API. This feature will remove an HLS
manifest from the origin if it has not been recently updated
enabling players to automatically switch from a primary origin
to a backup origin.

When a stale manifest is detected, use client-side or edge logic
to introduce origin failover. Many players allow for the
configuration of alternate playback sources by explicitly
providing multiple endpoints or by providing a manifest with
alternate renditions. Always work closely with your player
provider to determine the appropriate architecture for
client-side failover implementation and incorporate test cases
that simulate the common failure cases. If additional logic is
required to route requests dynamically in response to failures,
Lambda@Edge can be used to manipulate manifest responses to the
player.

When failover does occur, consider the implications of sticky or
non-sticky playback session handling. With sticky failover
clients are pinned to the new origin endpoint during failover
and only switch again if there is an additional failure. With
non-sticky failover clients access content from the primary
origin anytime it becomes available. You should always use a
sticky design when implementing a non-seamless failover design
to prevent origin switches that could adversely impact clients.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/streaming-media-lens/failure-management.html*

---

# Resources

Refer to the following resources to learn more about our best
practices related to reliability.

## Documents

- [Blog
Series: Resilient End-to-End Live Workflow Using AWS
Elemental Services](https://aws.amazon.com/blogs/media/part1-how-to-set-up-a-resilient-end-to-end-live-workflow/)
- [Amazon CloudFront for Media](https://docs.aws.amazon.com/whitepapers/latest/amazon-cloudfront-media/amazon-cloudfront-media.html)
- [Using
Amazon CloudFront Origin Shield in a Multi-CDN
Architecture](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/origin-shield.html#os-use-cases-multi-cdn)
- [Seamless
regional failover capabilities with Clustered Video Streams
Reference Architecture](https://github.com/awslabs/aws-clustered-video-streams)

## Videos

- [Raising
the Bar on Video Streaming Quality Using AWS](https://www.youtube.com/watch?v=IGXrnQviFLc)
- [Designing
for Live Stream Failure with Seamless Switching](https://www.youtube.com/watch?v=gkhRBxIElH0)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/streaming-media-lens/resources-rel.html*

---
