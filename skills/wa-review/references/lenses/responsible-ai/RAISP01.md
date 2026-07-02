# RAISP01 — AI system architecture design

**Best Practices**: 2

---

# RAISP01-BP01 Detail your core AI system design in a system registry

Detail how your AI system works, including the components and the
data flows between them. When issues come up, you need to know
exactly where problems might creep in, which components could fail,
and how problems in one part affect the whole system. Include
details about component versions and dependencies so you can track
which specific versions might be causing issues and understand how
updates could affect your system behavior.

**Level of risk exposed if this best practice
is not established:** High

## Implementation considerations

- Create System Architecture Diagrams: Create system
architecture diagrams including preprocessing steps, model
architectures, deployment configurations, and integration
points. Show end-to-end data flow and component relationships
in architecture diagrams.
- Define Component Specifications and Interactions: Detail each
component's functionality, input/output specifications, and
dependencies. Document data transformations, model parameters,
and performance requirements. Include API specifications,
security controls, and integration requirements. Map how
components communicate and share data across the system.
- Establish Documentation Management System: Set up a
centralized registry for system documentation, including
design decisions and component versions. Implement version
control for document updates, create clear update and approval
process, and establish review cycles. Include both technical
details and business context for each component.

## Resources

**Related documents:**

- [ISO/IEC
42001:2023 A.6.2.3 Documentation of AI system design and
development](https://www.iso.org/standard/42001)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raisp01-bp01.html*

---

# RAISP01-BP03 Check if design choices have introduced new risks

Review how design decisions affect the risk profile, determining
whether additional assessment criteria must be incorporated into the
testing framework.

For example, choosing to use a third-party component instead of
building your own solution might introduce new risk considerations.
When you identify new risks or changes in risk likelihood, decide if
you need to update your release criteria to properly test for these
issues before release.

**Level of risk exposed if this best practice
is not established:** High

## Implementation considerations

- Review the AI system document, design decisions and tradeoffs
for each component.
- Determine if the design decisions result in new risks or
updates to already identified risks in terms of severity and
likelihood.
- Update the risk assessment accordingly.
- Review the release criteria and determine if the release
criteria sufficiently covers the identified risks.
- Update the release criteria accordingly.

## Resources

**Related documents:**

- [ISO/IEC
42001:2023 A.6.2.3 Documentation of AI system design and
development](https://www.iso.org/standard/42001)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raisp01-bp03.html*

---
