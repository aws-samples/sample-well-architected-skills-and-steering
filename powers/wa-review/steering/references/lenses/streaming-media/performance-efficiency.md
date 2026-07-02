# Performance efficiency

**Pages**: 4

---

# Selection

SM_PERF1: How do you optimize media delivery through media origination and
processing?

**SM_PBP1 – Select an appropriate origin technology for
your workload**

There are two origin approaches that can be used to optimize
performance of your workload — pass-through and dynamic.
Pass-through origin servers are high-performance HTTP servers
that are adequately scaled to respond to requests for content
segments from viewers or CDNs. Encoders PUT pre-encoded,
pre-packaged, and pre-encrypted content to the origin server.
Pass-through origin servers, like AWS Elemental MediaStore or
Amazon S3, offer limited media processing functionality like
repackaging, but offer high performance and low cost.

When using a pass-through origin, the media processing layer is
responsible for the media codec and transport protocol
formatting. For example, the encoder configuration for HLS
segment size will directly impact the end-to-end latency of a
live stream. To support multi-protocol environments like MPEG
DASH and Apple HLS with a single set of processed media on a
passthrough origin, the industry is moving toward the Common
Media Application Format (CMAF). We encourage you to use this
format if you are planning to use a pass-through origin (if your
player devices support it) as it reduces storage costs, improves
CDN cache efficiency, and can decrease latency through
chunked-transfer-encoding.

*Comparing pass-through origin to dynamic
origin*

With a dynamic origin, content is PUT to the origin by an
encoder in a single format and dynamically formatted as
requested by viewers. This process, often referred to as
just-in-time packaging (JITP), provides additional flexibility
as content endpoints can be customized to support business
objectives without modifying the content produced by the
encoder. This is especially powerful for multi-protocol or
multi-DRM workflows that address a fractured device ecosystem
with variable requirements. Additional features enabled by
dynamic origin services like AWS Elemental MediaPackage include
look-back, start-over, and live-to-VOD recording. Note that
because dynamic origins require an internal buffer to process
content just-in-time, you will trade off live stream latency
when compared to pass-through origins.

Dynamic origins provide you with the flexibility to customize
endpoints to support your target devices. For example, you can
create an endpoint optimized for connected television
experiences that accounts for in-home network connections and
large screens by creating a rendition set with high-resolution
content and large segment sizes. Alternatively, using the same
content, you could create an endpoint optimized for mobile
networks, screens, and interactivity with shorter segment sizes
and additional low-resolution options.

The decision to use a pass-through origin or a dynamic origin
depends on your unique business requirements. In general, use a
pass-through origin if you have a limited number of client
compatibility requirements, a desire for the lowest possible
live latency, and value simplicity over flexibility. If you have
a diverse client ecosystem and require advanced origin features
like live-to-VOD recording, you should use a dynamic origin.

SM_PERF2: Hw do you approach media source contribution?

**SM_PBP2 – Begin with the highest-quality sources that you
can reasonably acquire**

**SM_PBP3 – Use specialized media transport and
acceleration protocols**

**SM_PBP4 – Use private network connectivity between your
content provider and media ingest**

There are two ingest patterns for video applications,
*real-time*
and *file-based*. Real-time workloads often
include a business requirement for reliability and low latency,
while file-based transfers for mezzanine files or archive
workloads generally prioritize efficiency of data movement.

**Real-time contribution**

It’s difficult to consistently deliver live video content to
large audiences quickly, reliably, and cost-effectively. Getting
a live source from an event site, often called a
*contribution feed*, is the first inflection
point when deciding trade-offs that will eventually impact end
users. In all cases, use of an efficient codec (for example,
HEVC) for signal contribution allows for optimum bandwidth
utilization and improved quality at lower cost.

Any impact to the network during the live contribution of media
can quickly degrade and disrupt video distribution to end
users**. AWS Direct Connect**, in
a
[maximum
resiliency configuration](https://aws.amazon.com/directconnect/resiliency-recommendation/), is recommended for services
requiring a dedicated, sustained connection to AWS (that is,
high visibility live events) as it provides a consistent network
experience when compared to internet transport. For first-mile
connectivity at remote live events that are subject to unmanaged
networks for delivering live media, we strongly recommend using
a combination of mediums, such as bonded-cellular, satellite
uplink, and multiple ISPs connecting to the AWS network.

Many applications use TCP-based protocols like RTMP to deliver
contribution feeds, but these protocols are inefficient and can
introduce unnecessary latency. We recommend a UDP-based reliable
transport protocol like RTP, Reliable Internet Stream Transport
(RIST), or Secure Reliable Transport (SRT) for real-time
contribution. These protocols are optimized for low-latency,
efficient video transport, and include tunable error correction
schemes like Automatic Repeat Request (ARQ) and Forward Error
Correction (FEC). In general, ARQ-based protocols are preferred
for unmanaged, public networks where loss is non-deterministic
and FEC is useful for semi-managed networks where loss is
deterministic.

**File-based contribution**

Asset management, archive, video-on-demand, and many other media
workloads manage large file transfers. AWS provides
a portfolio of services designed for these specific needs. These
are our general recommendations:

- As with live workloads, sustained file upload
architectures should use AWS Direct Connect.
- Always use **Amazon S3 Multipart
Upload** when uploading content to
**Amazon S3**.
- When uploading content from a location geographically
distant from an AWS Region, use
**Amazon S3 Transfer
Acceleration** to leverage CloudFront edge PoPs
for connectivity into AWS.
- When upload duration is expected to exceed more than one
week, use **AWS Snowball Edge.**
- For hybrid architectures where on-premises infrastructure
requires **Amazon S3**
access as NFS mounts or a virtual tape library interface
to Amazon Glacier, use **AWS Storage Gateway** and **AWS File Gateway.**

Due to the large file sizes of mezzanine quality media assets,
video workloads should employ tiered storage balancing
performance and cost. S3 Lifecycle policies can be used to
programmatically move infrequently accessed S3 assets to Amazon S3 IA or Amazon Glacier, however, this applies only to object
storage and is a one-way function. Consider designing an
intelligent filer service to restore source assets into the
appropriate storage service (block, file, or object) when
required by a processing job. If asset references exist use
these manifests to optimize restores.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/streaming-media-lens/selection.html*

---

# Review and monitoring

SM_PERF3: How do you use caching to improve content delivery
performance?

**SM_PBP5 – Use a content delivery network and monitor your
cache-hit-ratio**

**SM_PBP6 – Ensure that cache-control headers for your
content are optimized**

**SM_PBP7 – Have a cache invalidation
runbook**

**SM_PBP8 – Minimize negative (error)
caching**

A Content Delivery Network (CDN) scales video delivery by serving content from local
caches nearest the user and providing optimized routes to origination services. Caching
improves time-to-first-byte for clients and reduces the load on origin services. CDNs use a
multi-tier architecture with two or three tiers of cache hierarchy before requests make it
back to the origin server. These tiers are usually referred to as the edge tier and mid-tier
caches. The edge tier is first to receive a request from client and responds fastest in the
case of a cache match. The mid-tier has a larger cache depth, but is located only in select
locations. Cache misses to the edge tier come back to the mid-tier for another chance at a
cache match.

A Cache Hit Ratio (CHR) is the ratio of requests served from
cache (matches) to the total requests (misses and matches) over
a period of time. Cache matches improve the client experience
and cache misses result in a request directly to your origin
layer that increases response latency and costs. Monitoring CHR
will help you to improve delivery and origin layer performance
over time. You can enable CHR, origin latency, and HTTP error
rate metrics from your Amazon CloudFront monitoring settings.

CDNs typically employ a last recently used (LRU) caching
strategy on each tier. This means that data will be maintained
in caches based on the amount of traffic an object receives and
the available cache size. Though you can’t guarantee caches will
hold content for the next request, you can set Cache-Control
headers on the origin to indicate the preferred duration for an
object to be kept in a CDN cache. Your CDN should be configured
to respect caching headers from your origin server to ensure
that live content and manifests are only cached for the
appropriate amount of time.

Live streaming manifests are frequently updated to represent the
next media object in the stream and should not be cached for
longer than half of your segment duration. Caching longer than
the segment duration could result in the serving of stale
manifests, a delay for clients to retrieve the next media
segment, and client buffer exhaustion, which will negatively
impact user experience. Live media segments and VOD content
(both segments and manifests) should be cached for as long as
possible to retain them in delivery caches for the maximum
amount of time.

**Scenario**

**Segment Size**

**Manifest Update
Frequency**

**Segment Cache-Control Header or
Cache Behavior**

**Manifest Cache-Control Header or
Cache Behavior**

**Live**

10 seconds

10 seconds

21,600 seconds or max DVR window

5 seconds or less

**VOD**

10 seconds

Static

86,400 seconds or longest possible

86,400 seconds or longest possible

*Recommended cache behaviors for live and
Video-on-Demand (VOD) scenarios*

There are often times when cached content needs to be modified
or invalidated. Have a cache invalidation runbook in place so
that you can modify cached objects and invalidate the previous
content. This can be achieved by invalidating content with a CDN
feature, using variable file names, or using query string
parameters to “break” the cache when content is changed.

Caching of error responses from the origin, also known
as *negative caching*, should be minimized as
some streaming clients might proactively request future segments
before they are published to minimize latency. For live
streaming, it should be disabled completely for manifest and
segment files. At a minimum, the negative caching duration
should not exceed one segment length. Amazon CloudFront caches
origin errors for five minutes by default, but you
can [configure
it to suit your needs](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/custom-error-pages-expiration.html).

SM_PERF4: How do you monitor viewer experience?

**SM_PBP9 – Collect and analyze real user logs and
metrics**

**SM_PBP10 – Recognize and respond to playback
anomalies**

Infrastructure logging and monitoring only provides you with
part of the picture. We recommend that you design a client that
sends real-user data directly to monitoring and logging systems.
This allows you to benchmark normal behavior, identify
anomalies, and correlate events with content delivery systems.
For example, session initialization information, like playback
URL, user-agent, and network connection status could help you
identify issues with a specific origin, client device type, or
network environment.

For streaming media, it’s especially important to monitor the
health of the video decoder to determine how changes in network
topology, video encoding settings, or mobile operating systems
impact the end user experience. For example, capturing video
buffering events, which directly impact customer satisfaction,
should be a key indicator of streaming health.

We recommend that you capture client metrics from streaming
sessions with services like **Amazon Kinesis** and monitor for anomalies with
**Amazon CloudWatch**. Equipped
with this data, you can uncover patterns from real users, create
alerting systems, and automate remediation tasks. The
**AWS Partner Network** provides
another avenue for video-specific monitoring tools that can give
you actionable data from playback sessions.

Amazon Prime Video, a streaming media service by Amazon, has
many ways of monitoring customer experience. One key metric,
*Zero-Impact-Rate*, measures the rate of
streaming sessions that have had any buffers or errors. This is
used to baseline customer experience and alert when there are
deviations from normal behavior. Here are other client metrics
that provide valuable insights into viewer playback experience:

**Metric**

**Description**

**Time-to-First-Frame**

Time between client request for content and first frame
being displayed on client

**Playback Frames Per
Second**

Client displayed frame rate

**Session Resolution**

Client displayed resolution

**Session Duration**

Duration the client spent watching content

**Buffering Events**

Client buffering events

**Zero-Buffer-Rate**

Number of sessions that had zero buffer events

**Client Errors Events**

Client HTTP or application errors

**Zero-Error-Rate**

Percentage of total sessions that had zero error events

**Zero-Impact-Rate**

Percentage of total sessions that had zero Buffers or
Errors

*Suggested metrics for measuring quality of
service*

*Source: https://docs.aws.amazon.com/wellarchitected/latest/streaming-media-lens/review-and-monitoring.html*

---

# Tradeoffs

SM_PERF5: What tradeoffs have you made in media processing to improve client
experience and lower bandwidth costs?

**SM_PBP11 – Optimize the number of adaptive bitrate
renditions for your workload**

**SM_PBP12 – Select appropriate encoding settings for your
content type and quality targets**

**SM_PBP13 – Trade higher content processing cost for lower
delivery costs for popular content**

For media delivery applications, protocol selection and
configuration have a dramatic impact on client performance.
Progressive file downloads or RTMP streaming, can be slow to
download, costly to scale, or inflexible. Instead, use
HTTP-based Adaptive-Bitrate protocols, like Apple HLS, combined
with web caching mechanisms to improve distribution efficiency.
These protocols also enable clients to select the optimal
rendition for playback based on network connection, display
resolution, and other client-side characteristics, greatly
improving viewer experience.

The *ABR ladder*, or number of logical
renditions available to an individual client, should be tuned to
meet the needs of the specific application, taking into account:

- Playback quality
- Client and display ecosystem
- User geography and network connectivity

Providing too many renditions can increase encoding costs and
cause clients to fluctuate frequently between renditions,
reducing perceived quality. Not providing enough renditions
might leave usable bandwidth underutilized and, thus, also
reduce quality. Our general recommendation is to determine the
maximum bitrate first, then divide by 1.5–2 for each step down.
This step in the ladder allows clients to make significant jumps
in quality, but not so many that frequent changes could be
perceived by end users. If your application is delivering to
Apple devices, refer to Apple TN2224 for additional guidance on
creating adaptive bitrate content. If you are using AWS Elemental MediaConvert, the *Auto ABR*
capability can automatically determine an optimal ABR ladder for
you based on the specific characteristics of the content.

SM_PERF6: What tradeoffs have you made to lower live glass-to-glass
latency?

**SM_PBP14 – Optimize processing, origination, delivery,
and client for low latency**

**SM_PBP15 – Remove unnecessary processing
stages**

Latency is inherent in any broadcasting or streaming platform.
Over-the-air live broadcast glass-to-glass latency ranges
between 3 – 12 seconds, with an average of 6 seconds often seen
in practice. This means that it could take up to an average of 6
seconds before the event that is captured in the camera is
displayed on the playback device. For streaming platforms, this
latency can vary anywhere from 3 to 90 seconds, depending on
various design choices. Typically, achieving low latency in a
streaming platform may be a tradeoff with other critical aspects
of the streaming experience, such as, video quality,
re-buffering rate, error rates and other quality-of-service
indicators.

With HTTP-based streaming, latency mainly depends on the media
segment length. For instance, the Apple HLS specification
recommends at least three segments of buffer for best
performance. This directly influences the latency. Other factors
in the media delivery pipeline that influence latency include
the video encoding operations, the duration of ingest and
packaging operations, network propagation delays, and the CDN.
In most cases, the player buffer carries the largest share of
the overall latency.

There are several tradeoffs to consider with low latency media
streaming design. Shorter media segment lengths will result in
increased traffic on the caching servers and then to the origin.
This is fairly manageable by a CDN, especially if it supports
HTTP 2.0 at the edge and HTTP 1.1 origins. As previously
mentioned, encoding parameters have an impact on latency and
optimizations for latency typically impact the video quality.
For example, setting an
encoder *lookahead* size to a low value will
improve latency, but reduces output quality for demanding scene
changes. If your content does not have dramatic scene changes,
keeping this value low will not have a noticeable impact video
quality.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/streaming-media-lens/tradeoffs.html*

---

# Resources

Refer to the following resources to learn more about our best
practices related to performance efficiency.

## Documents

- [HLS
Authoring Specification for Apple Devices](https://developer.apple.com/documentation/http_live_streaming/hls_authoring_specification_for_apple_devices)
- [How
to Compete with Broadcast Latency Using Current Adaptive
Bitrate Technologies](https://aws.amazon.com/blogs/media/how-to-compete-with-broadcast-latency-using-current-adaptive-bitrate-technologies-part-1/)
- [Managing
How Long Content Stays in an Edge Cache](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Expiration.html)
- [Increasing
the Proportion of Requests that Are Served from CloudFront
Edge Caches (Cache Hit Ratio)](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cache-hit-ratio.html)
- [Delivering
Live Streaming Video with CloudFront and AWS Media
Services](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/live-streaming.html)
- [Streaming
Media Analytics Solution](https://github.com/awslabs/aws-streaming-media-analytics)

## Videos

- [Architecting
a 24x7 Live Linear Broadcast for 100% availability on
AWS](https://youtu.be/mZenLM-E4k4)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/streaming-media-lens/resources-perf.html*

---
