# RAISP04 — Choosing a system configuration

**Best Practices**: 1

---

# RAISP04-BP01 Use paired tests to choose from candidate designs

Test different candidate configurations of your system, including
different versions of your components or models during development
using validation sets to determine which performs best. Different
versions can come from different component choices,
hyperparameters, training settings, or model architectures. Set up
controlled comparisons between versions on the same validation
data, then use paired statistical tests to determine if one
version is statistically better than the other based on your
release criteria. Keep your evaluation sets separate from
component selection because using them would bias your final
performance measurements and make your release decisions
unreliable.

**Level of risk exposed if this best
practice is not established:** Medium

## Implementation considerations

- Use validation datasets exclusively for choosing between
candidate versions, keeping them separate from your final
evaluation data. This separation blocks you from accidentally
tuning your choices to the test set, which may make your final
performance estimates unreliable.
- Run head-to-head comparisons where each candidate version
processes identical validation inputs under the same
conditions. Measure their performance on metrics that matter
for your release criteria so you can see which version
delivers better results.
- Apply paired statistical tests to determine whether
performance differences between candidates are real
improvements or just random noise. Calculate confidence
intervals and effect sizes to understand not just whether one
version is better, but by how much.

## Resources

**Related documents**

- [ISO/IEC
42001:2023 A.6.2.4 AI system verification and
validation](https://www.iso.org/standard/42001)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raisp04-bp01.html*

---
