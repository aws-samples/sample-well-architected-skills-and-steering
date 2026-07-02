# Cost optimization

**Pages**: 3

---

# Cost-effective resources

Object storage is a key part of origin services or media
archives. The 11 9’s of durability and near-infinite scale
reduce operational overhead and storage costs for media
applications. As media assets can easily reach hundreds of
gigabytes in size, you should develop a storage strategy that
takes into account the access patterns of the content.

SM_COST1: What is your strategy for optimizing object storage and data transfer
costs?

**SM_CBP2 –Trace and limit data transfer between services,
Availability Zones, Regions, and clients**

We recommend that you prioritize a strategy for storage
lifecycle and data transfer, as these often have the largest
savings potential when compared to requests, management
functions, and object replication.

With media archive or batch transcoding workloads, you should
analyze and define access patterns. Once understood, represent
these patterns in **Amazon S3 Lifecycle
Policies**, which automate the continual movement of
assets to the most effective storage. This achieves the lowest
storage costs, while meeting the business accessibility
requirements.

For applications with non-deterministic access patterns, such as
video recordings, user-generated-content, or a large
back-catalog, it's a challenge to design lifecycle policies or
select outright the most cost-effective
**Amazon S3** storage tier for
your content. To optimize storage costs, asset access patterns
need to be actively monitored and managed. This can be done
manually through content management solutions or with features
like **Amazon S3** Analytics
Storage Class Analysis and S3 Intelligent-Tiering.

Real-time media streams are measured in megabytes per second and
source files can easily reach into the hundreds of gigabytes per
file. To control data transfer and outbound costs, be aware of
the data transfer costs associated with transmitting the data
throughout the cloud and to users. To control costs associated
with inter-AZ or inter-Region transfer, you should ingest
content into the Region and Availability Zone in which it will
be processed. For outbound data cost control between the origin
and client, consider the use **Amazon CloudFront** to reduce costs while improving
performance for viewers. When content does need to span
Availability Zones, Regions, or incur outbound costs, use the
most efficient compression possible to minimize cost.

SM_COST2: What is your strategy for optimizing content processing
costs?

**SM_CBP3 – Baseline resources and throughput for media
processing tasks**

**SM_CBP4 – Run media processing tasks in parallel**

Consumer demand for more content choices at higher quality
(resolution, color-depth, frame rate) puts pressure on
processing components. As media processing needs increase for
tasks like quality control (QC), transcoding, and packaging, so
do the costs associated with these tasks.

To manage costs, baseline the time and infrastructure resources
necessary for your most common processing tasks. One way to
understand processing speed and resource density is to calculate
the real-time factor (RTF) by taking task execution time divided
by source duration. An RTF lower than one indicates that content
is processing faster than real-time, greater than one is slower
than real time. For example, a video transcoding task that takes
an EC2 instance 45 minutes to process a one-hour video has an
RTF of 0.75. RTF and the resources required can be used to
understand and communicate how changes to the task or
infrastructure will impact business priorities.

One way to reduce RTF while accessing cost effective resources
is to split jobs into smaller subtasks and run them in parallel.
With video content, you can split tasks on I-frame boundaries,
process those segments, and then stitch them together when all
subtasks are complete. Split-and-stitch and parallelization
techniques create granular tasks that can easily be placed
across a processing fleet, leading to more efficient use of
compute resource. Splitting processor intensive tasks also
reduces dependency on vertical scaling and enables access the
most cost effective compute resource available through
heterogeneous **Amazon EC2 Spot**
clusters.

When using **AWS Elemental Media
Services**, many pricing options are available to make
workloads more cost effective. For example, for live streaming
workloads where redundancy is not required,
**AWS Elemental MediaLive**
offers channels that run in *single-pipeline*
mode for a significant discount over the standard channel rates.
Similarly, for long-running and 24x7 channels, channel
reservations offer significant discounts in exchange for term
commitments. For file-based workloads,
**AWS Elemental MediaConvert**
offers *basic tier* functionality where lower
rates are available in exchange for avoiding certain
computationally intensive or licensed features. When a large
volume of steady-state file-based transcoding is required,
reserved transcoding slots can also be purchased to provide
steady-state transcoding capacity for a fixed monthly cost
rather than the standard billing model of per output minute.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/streaming-media-lens/cost-effective-resources.html*

---

# Optimizing over time

Content delivery is the largest cost-optimization area for
organizations streaming content to large audiences. You should
*always* be evaluating the perceptual quality
of content and striving to lower video data rates while
maintaining, or ideally improving quality through encoder
optimization.

SM_COST3: How do you minimize distribution costs while maintaining visual
quality?

**SM_CBP5 – Use objective and subjective measurement
techniques to benchmark and improve video compression
efficiency**

To optimize quality while balancing delivery costs, you should
focus on media processing and compression. The codec you use
will be dependent on your content complexity, encoder
capabilities, and client interoperability. Most codecs provide
many controls that can be tuned. Use a combination of objective
and subjective measurement to understand and improve your
compression efficiency over time.

Though not always an accurate representation of human visual
perception, objective measurement tools, like Peak
Signal-to-Noise-Ratio (PSNR), Structural Similarity (SSIM), and
Video Multi-Method Assessment Fusion (VMAF) are readily
available tools to help analyze your compression performance.
Given a source, varied encoding job settings, and resulting
outputs, compare these metrics to tune for your unique content.
In general, though there are many options to consider while
tuning video compression settings, high motion content will
require a higher data rate than low motion to retain the same
perceptual quality.

Subjective measurement techniques will uncover practical issues
with your video compression that might not be identified by
objective scoring. For subjective testing with human eyes and
real network conditions outside of a production environment,
consider user feedback mechanisms that enable willing users to
provide information on their viewing experience. For a simulated
environment, **Amazon Mechanical
Turk** can give you access to humans willing to watch
your content and provide feedback. For a small fee,
*Turkers* around the world can provide you
with valuable insights on their playback experience, which can
be used to improve your workload.

Use this combination of subjective, objective, and
real-user-metrics to tune encoding settings and ABR protocol
configuration.  It is recommended that you familiarize yourself
with the codec and encoder you use for delivery so that you can
identify optimizations that could save you delivery costs. For
example, context-aware or quality-based encoding, available as a
QVBR setting for **AWS Elemental
MediaLive** and **AWS Elemental MediaConvert**, can analyze the complexity of the
content and optimize processing on your behalf.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/streaming-media-lens/optimizing-over-time.html*

---

# Resources

Refer to the following resources to learn more about AWS best practices for cost
optimization.

## Documents

- [Netflix VMAF Project](https://github.com/Netflix/vmaf)

## Videos

- [Containerizing Video: The Next
Generation Video Transcoding Pipeline](https://www.youtube.com/watch?v=tfoFilopvR0)
- [Leverage the Power of the Crowd
To Work with Amazon Mechanical Turk](https://www.youtube.com/watch?v=r7xR9kLHCHc)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/streaming-media-lens/resources-cost.html*

---
