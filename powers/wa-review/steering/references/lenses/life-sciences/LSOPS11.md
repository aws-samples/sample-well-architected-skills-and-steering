# LSOPS11 — Operate

**Pillar**: Operational Excellence  
**Best Practices**: 1

---

# LSOPS11-BP01 Identify clear dataset owners and access history

If you are receiving a dataset, identify who is responsible for data
accuracy and governance and who manages the data lineage during
collection. Depending on the storage method, who is responsible for
securing the data in its different stages?

**Desired outcome:** Have an
automated method of auditing shared data between partners.

**Benefits of establishing this best
practice:** Data can be limited to just what is agreed on.
Secure data can be automatically filtered.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Design a collaborative governance framework. Establish unified
governance architecture spanning organizational boundaries. This
foundation enables consistent data policies while respecting each
organization's requirements.

### Implementation steps

- Configure collaborative workflows:

Implement data exchange protocols specific to
organizational relationships.
- Establish shared metadata repositories with
organization-specific views.
- Deploy cross-organizational audit mechanisms.

- Use AWS Clean Rooms to enable granular control and data
sharing without moving data or exposing sensitive
information.

## Resources

**Related documents:**

- [AWS Clean Rooms: Privacy-enhanced collaboration use cases](https://aws.amazon.com/blogs/industries/aws-clean-rooms-privacy-enhanced-collaboration-use-cases/)

**Related examples:**

- [Enable
data collaboration among public health agencies with AWS Clean Rooms – Part 1](https://aws.amazon.com/blogs/big-data/part-1-enable-data-collaboration-among-public-health-agencies-with-aws-clean-rooms/)
- [Automate
AWS Clean Rooms querying and dashboard publishing using AWS Step Functions and Quick – Part 2](https://aws.amazon.com/blogs/big-data/automate-aws-clean-rooms-querying-and-dashboard-publishing-using-aws-step-functions-and-amazon-quicksight-part-2/)

**Related tools:**

- [AWS Clean Rooms](https://aws.amazon.com/clean-rooms/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsops11-bp01.html*

---
