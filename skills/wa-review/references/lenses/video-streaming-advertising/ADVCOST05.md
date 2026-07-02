# ADVCOST05 — Privacy-enhanced collaboration

**Pillar**: Cost Optimization  
**Best Practices**: 1

---

# ADVCOST05-BP01 Use cost efficient data types and configurations for collaborative data environments

Use efficient storage formats and streamlined query configurations to reduce unnecessary data scanning, duplication, and transfer costs in collaborative analytics environments.

## Implementation guidance

- Use parquet or columnar formats with partitioning and compress datasets.
- Use standard SQL for lightweight or well-partitioned datasets.
- Avoid unnecessary cross-joins or full table scans.
- Use same-Region AWS Clean Rooms collaborations to minimize inter-Region transfer costs.

## Key AWS services

- AWS Clean Rooms

## Resources

- [Data
formats for AWS Clean Rooms](https://docs.aws.amazon.com/clean-rooms/latest/userguide/data-formats.html)
- [Data Analytics Lens](https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/best-practice-10.4---partition-your-data-to-avoid-unnecessary-file-reads.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advcost05-bp01.html*

---
