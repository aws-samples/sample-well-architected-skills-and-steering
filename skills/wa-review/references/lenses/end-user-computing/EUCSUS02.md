# EUCSUS02 — Alignment to demand

**Pillar**: Sustainability  
**Best Practices**: 1

---

# EUCSUS02-BP01 Select the instance type or bundle to match software requirement and user personas

Consider the performance needs, cost implications, and any
specific workload characteristics (for example, GPU
requirements). Benchmark and test different instance types to
find the best fit for your workload. Regularly review and adjust
your instance type selection as your application's demands
change over time.

**Level of risk exposed if this best
practice is not established:** High

## Implementation guidance

WorkSpaces Applications offers eight [instance families](https://docs.aws.amazon.com/appstream2/latest/developerguide/instance-types.html) and
a set of instance types per family. Explore these instance families and types to identify
the appropriate requirement for each use case. For graphics workloads, use Graphics G4dn
and Graphics G5. Once you have defined the instance family, you can benchmark at least two
instances type to identify the best choice.

Amazon WorkSpaces offers
[nine
bundles](https://docs.aws.amazon.com/workspaces/latest/adminguide/bundle-options.html), from value to GraphicsPro.g4dn. Once you have
selected applications and usage for each use case, identify
the requirement in term of CPU, memory, and GPU for each of
them.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucsus02-bp01.html*

---
