# HPCSUS01 — Sustainability

**Pillar**: Sustainability  
**Best Practices**: 2

---

## HPCSUS01-BP01 Select target AWS Regions that balance performance and resource availability with your sustainability goals

The AWS Cloud is a constantly expanding network of Regions and points of presence
(PoP), with a global network infrastructure linking them together. The choice of Region for
your workload significantly affects its KPIs, including end user latency, cost, and carbon
footprint. To effectively improve these KPIs, you should choose Regions for your workload
based on both your business requirements and sustainability goals.

Following performance efficiency best practices, you have identified the right Amazon EC2
instances for your HPC workloads. Amazon EC2 provides the ability to deploy instances in multiple
locations, so you need to find which Regions have your preferred instance type. Then, select
the best Region following the other practices in this pillar.

### Implementation guidance

To achieve your sustainability goals, choose Regions that are near Amazon renewable
energy projects and where the grid has a published carbon intensity that is lower than
other locations (or Regions). For more detail on choosing a Region based on your
sustainability guidelines, see [How to select a Region for your workload based on sustainability goals](https://aws.amazon.com/blogs/architecture/how-to-select-a-region-for-your-workload-based-on-sustainability-goals/).

*Source: https://docs.aws.amazon.com/wellarchitected/latest/high-performance-computing-lens/region-selection.html*

---

## HPCSUS01-BP02 Select Regions based on where your users are located

Placing a workload closer to its users provides the lowest
latency while decreasing data movement across the network and
reducing environmental impact.

### Implementation guidance

It may happen that the two best practices described above
cannot be implemented simultaneously (for example, if the
preferred instances are not available in the Region closest to
the end-users). In this case, the HPC cluster administrators
must find the right tradeoff between the business objectives
and the sustainability objectives.

## Key AWS services

- [AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/)

## Resources

- [How
to select a Region for your workload based on sustainability
goals](https://aws.amazon.com/blogs/architecture/how-to-select-a-region-for-your-workload-based-on-sustainability-goals/).

*Source: https://docs.aws.amazon.com/wellarchitected/latest/high-performance-computing-lens/region-selection.html*

---
