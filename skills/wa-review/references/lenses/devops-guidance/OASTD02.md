**Saga**: Organizational adoption
**Capability**: OA.STD — Supportive team dynamics

---

# [OA.STD.2] Tailor operating models to business needs and team preferences

**Category:** FOUNDATIONAL

Adopt operating models that align with the needs of the business goals, while considering the
capabilities and preferences of individual teams. The AWS Well-Architected Framework
Operational Excellence Pillar provides a detailed [2 by 2 representations of operating model implementations](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/operating-model-2-by-2-representations.html) that can be reviewed
to gain insights into potential combinations. Selecting the right operating model involves
evaluating the organization's requirements, such as decision-making processes, communication
channels, and resource allocation. Keep in mind that multiple
operating models can be used concurrently, catering to different use cases, levels of
organizational maturity, and individual team and product needs.

Not all operating models support a DevOps culture, and DevOps might not be suitable
for every system. In some cases, especially in large and diverse organizations,
it might be necessary to support stringent compliance requirements. Additionally, mass migration
to a new way of working for all teams may not be feasible due to time, complexity
of the system, or skill requirements. For these use cases, a [fully separated](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/fully-separated-operating-model.html)
operating model or introducing an Internal MSP and Consulting Partner
might be needed for those systems that must stay *as is* with
more traditional ways of working.

When choosing a Well-Architected operating model for systems that can support DevOps, first determine if centralized or decentralized control of governance is
necessary. A centralized governance model grants platform teams within an organization the
ability to control *how* and *what* other
teams are able to deploy, at the cost of restricting those teams' ability to innovate and
make changes quickly. Conversely, a fully decentralized model offers teams more flexibility and autonomy, requiring
less intensive collaboration between teams through reliance on guardrails and automated
governance over strict control.

**Related information:**

- [AWS Well-Architected Operational Excellence Pillar: Operating
model 2 by 2 representations](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/operating-model-2-by-2-representations.html)
- [Building
your Cloud Operating Model: Organize for Success](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-cloud-operating-model/implement-roadmap.html#organize)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/oa.std.2-tailor-operating-models-to-business-needs-and-team-preferences.html*
