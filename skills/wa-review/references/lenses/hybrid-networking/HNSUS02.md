# HNSUS02 — Alignment to demand

**Pillar**: Sustainability  
**Best Practices**: 2

---

# HNSUS02-BP01 Prioritize critical components

Break down your workload into individual components (for example,
microservices, databases, and APIs). Use metrics like CPU
utilization, request rates, and business impact to classify them as
critical or non-critical.

**Desired outcome:** Resource
allocation aligned with business value, minimizing waste in
low-impact areas.

**Level of risk exposed if this best practice
is not established:** Medium

**Benefits of establishing this best
practice:**

- Focuses optimization efforts on high-impact components
- Reduces energy consumption
- Maintains performance for mission-critical workloads

## Implementation guidance

- Map component dependencies and usage. For example, you can
achieve this using AWS X-Ray.
- Apply tags to categorize components (for example,
business-critical, dev-test).
- Right-size your resources during off-peak hours. For example,
you can achieve this using AWS Auto Scaling.

## Resources

- [AWS X-Ray: Service Map Analysis](https://docs.aws.amazon.com/xray/latest/devguide/xray-concepts.html)
- [Best
Practices for Tagging AWS Resources](https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/what-are-tags.html)
- [AWS Auto Scaling - application scaling](https://aws.amazon.com/autoscaling/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnsus02-bp01.html*

---

# HNSUS02-BP02 Perform lifecycle assessments for sustainability trade-offs

Evaluate the environmental impact of architectural decisions (for
example, regional placement, instance types, storage classes).
Compare trade-offs between performance, cost, and sustainability.

**Desired outcome:** Informed
decisions that balance business needs with environmental
responsibility.

**Level of risk exposed if this best practice
is not established:** Low

**Benefits of establishing this best
practice:**

- Identifies opportunities to reduce carbon footprint without
compromising functionality
- Supports ESG reporting and transparency

## Implementation guidance

- Use tools, such as the
[AWS Customer Carbon Footprint Tool](https://aws.amazon.com/blogs/aws/new-customer-carbon-footprint-tool/), to measure emissions
- Prefer regions powered by renewable energy
- Consider more efficient resources, such as Graviton-based
instances

## Resources

-
- [AWS Customer Carbon Footprint
Tool](https://aws.amazon.com/sustainability/tools/aws-customer-carbon-footprint-tool/)[AWS Graviton Processor](https://aws.amazon.com/pm/ec2-graviton/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnsus02-bp02.html*

---
