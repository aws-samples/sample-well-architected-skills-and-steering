# ADVSUS05 — Data management

**Pillar**: Sustainability  
**Best Practices**: 1

---

# ADVSUS05-BP01 Identify and remove redundant data across storage

Participants in the real-time advertising supply chain can accrue
large volumes of data. Consider how you use data and data
preservation as outlined in ADPERF04-BP01. Don't keep data that
has no purpose, can easily be recreated, and expedite the removal
of low value or short-lived data. Remove unwanted advertisement
video, images, files, and any other associated data that is no
longer needed.

## Implementation guidance

- Optimize data handling needs based on workload requirements,
and verify that it reflects the nature of the business and
short-lived advertising content (delete or archive based on
data class).
- Consider if duplicate ad files or versions of ad files are
be being saved that can be easily recreated.
- Use
[Amazon S3 storage lifecycle](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html) rules to automate the expiration
(and deletion) of draft ad content versions. For content
that should be preserved for historical purposes, use Amazon S3 storage lifecycles to transition content to another
storage class, such as Amazon Glacier.
- [Amazon S3 Storage Lens](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-lens-optimize-storage.html) can identify incomplete multipart
uploads, buckets that have numerous noncurrent versions, and
if lifecycle rules are not present. Storage Lens can also
provide activity metrics to identify ad objects or even
prefixes that are infrequently used.
- [AWS Config](https://aws.amazon.com/config/) can also identify if you have unused
resources, such as
[EBS
volumes](https://aws.amazon.com/ebs/).
- Use
[Amazon ECR lifecycle policies](https://docs.aws.amazon.com/AmazonECR/latest/userguide/LifecyclePolicies.html) to expire old images used for
real-time bidding containers.
- Evaluate how users are using data to eliminate use cases,
dimensions, and queries that no longer provide value.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advsus05-bp01.html*

---
