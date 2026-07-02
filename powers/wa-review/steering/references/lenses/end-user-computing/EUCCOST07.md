# EUCCOST07 — Manage demand and supply resources

**Pillar**: Cost Optimization  
**Best Practices**: 1

---

# EUCCOST07-BP01 Use the available cost optimizers for Amazon WorkSpaces and Amazon WorkSpaces Applications

Leverage available tools from AWS and partners to support you
with cost monitoring and optimization.

**Level of risk exposed if this best
practice is not established:** High

## Implementation guidance

Amazon WorkSpaces Applications uses app block and image builders that are charged hourly or in one second
increments with a 15-minute minimum if you keep them running. You must explicitly stop
them to stop the billing. The [Cost Optimizer
for Amazon WorkSpaces Applications](https://github.com/aws-samples/cost-optimizer-for-amazon-appstream2) can monitor your WorkSpaces Applications app block and image builders and notify
you or stop them when they are active for longer than specified thresholds.

Third-party tools like the [AppStream
Optimizer by Cambrian Technologies](https://www.cambriantechnologies.com/solutions/appstream-optimiser/) use machine learning to optimize your WorkSpaces Applications
Fleets and achieve a better utilization. This helps reduce your cost by reducing idle
capacity.

Deploy the
[Cost
Optimizer for Amazon WorkSpaces](https://aws.amazon.com/solutions/implementations/cost-optimizer-for-amazon-workspaces/) to receive reports with
recommendations on which running mode to select for your
WorkSpaces and automatically convert your WorkSpaces to the
most cost-effective running mode.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/euccost07-bp01.html*

---
