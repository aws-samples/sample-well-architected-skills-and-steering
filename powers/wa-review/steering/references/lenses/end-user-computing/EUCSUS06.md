# EUCSUS06 — Software and architecture

**Pillar**: Sustainability  
**Best Practices**: 2

---

# EUCSUS06-BP01 Stop image builders and app block builders when not in use

In WorkSpaces Applications, image builders and app block builders are two instances used only when
creating your baseline image or application package. There is no requirement to keep them
running.

**Level of risk exposed if this best
practice is not established:** Medium

## Implementation guidance

The [Cost Optimizer for Amazon WorkSpaces Applications](https://aws.amazon.com/blogs/desktop-and-application-streaming/cost-optimizer-for-amazon-appstream-2-0-on-the-solutionist/) monitors your WorkSpaces Applications image builders, notifying
you and halting them when they are active for longer than specified thresholds.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucsus06-bp01.html*

---

# EUCSUS06-BP02 Implement the Cost Optimizer for Amazon WorkSpaces

The
[Cost
Optimizer for Amazon WorkSpaces](https://aws.amazon.com/solutions/implementations/cost-optimizer-for-amazon-workspaces/) analyzes your Amazon WorkSpaces usage data and automatically converts the WorkSpace
to the most cost-effective billing option (hourly or monthly),
depending on your individual usage.

**Level of risk exposed if this best
practice is not established:** Low

## Implementation guidance

This solution analyzes your Amazon WorkSpaces usage data and
automatically converts WorkSpaces to the most cost-effective
billing option (hourly or monthly). This verifies that the
lowest carbon footprint and cost is associated with each
individual WorkSpace instance based on the unique usage
pattern for each user. This data provides the opportunity to
identify usage of WorkSpaces and delete unused WorkSpaces
through the definition of a rule.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucsus06-bp02.html*

---
