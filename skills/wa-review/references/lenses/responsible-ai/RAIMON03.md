# RAIMON03 — Decomissioning

**Best Practices**: 1

---

# RAIMON03-BP01 Establish mechanisms for honoring stakeholder obligations

Consider how to honor obligations you many have to upstream
stakeholders (such as people who contributed content to an
evaluation or training dataset) and downstream stakeholders (such as
workflows that have taken dependencies on your AI system).

**Level of risk exposed if this best
practice is not established:** High

## Implementation considerations

- Review your dataset registry to decide the correct way to
handle each dataset, for example should it be kept for re-use,
kept as a required record, or deleted.
- Review logs and customer agreements to identify potential
downstream dependents and determine a decommissioning strategy
that provides appropriate notice.

## Resources

**Related tools:**

- [Overview
of the decommissioning process](https://docs.aws.amazon.com/controltower/latest/userguide/decommissioning-process-overview.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raimon03-bp01.html*

---
