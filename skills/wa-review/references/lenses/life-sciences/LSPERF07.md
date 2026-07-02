# LSPERF07 — Compute and hardware

**Pillar**: Performance Efficiency  
**Best Practices**: 3

---

# LSPERF07-BP01 Use a risk-based validation framework

Use risk-based validation with full validation (Installation,
Operation, and Performance Qualification) for high-risk systems
affecting patient safety, streamlined methods for lower-risk
environments. Focus resources where critical and use automated
testing to maintain regulatory adherence without slowing innovation.
Revalidate based on risk assessment, not after every change.

**Desired outcome:** Achieve
regulatory adherence while optimizing resource allocation through a
balanced validation approach that maintains patient safety in
critical systems yet maintains operational efficiency. Enable
innovation in research environments through appropriate validation
levels, resulting in fewer bottlenecks and greater productivity
without compromising quality or standards.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Develop a framework for classifying computational systems based on
GxP impact and patient safety considerations. Risk-based
stratification maintains an appropriate level of validation
intensity and blocks over-validation of research systems.

Design validation approaches proportional to the established risk
categories. Tiered protocols verify that critical systems receive
comprehensive validation while avoiding unnecessary documentation
burden for research-focused systems.

Implement ongoing verification practices integrated with
development and operational workflows. Continuous validation
approaches maintain regulatory adherence while supporting agility
and innovation in computational environments.

Establish criteria for when systems require revalidation based on
change impact rather than arbitrary rules. Intelligent triggers
block unnecessary revalidation while providing proper scrutiny of
significant changes.

Maintain regulatory adherence while preserving computational
agility for research innovation. A balanced approach blocks
validation processes from becoming bottlenecks while maintaining
patient safety and data integrity in regulated contexts.

### Implementation steps

- Create risk classification framework with documented
regulatory justification.
- Develop validation strategies appropriate to system risk
levels.
- Deploy automated testing integrated with development
pipelines.
- Create change assessment framework with risk-based review
process.
- Optimize validation efficiency while maintaining regulatory
adherence.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsperf07-bp01.html*

---

# LSPERF07-BP02 Design a compliant-by-design infrastructure

Design a computing architecture that addresses both performance and
regulatory requirements through technical controls built directly
into the infrastructure. Implement segregated computing environments
with appropriate data controls between GxP and non-GxP workloads,
deploy immutable infrastructure techniques that enhance both
security and compliance, and use containerization with validated
base images to accelerate deployment while maintaining regulatory
integrity. Establish infrastructure templates with pre-validated
components, automated audit trail generation, and built-in data
integrity mechanisms that minimize the performance overhead
typically associated with compliance retrofitting, while verifying
that computational workloads execute in appropriately validated
environments based on their regulatory classification.

**Desired outcome:** Create a
computing infrastructure that balances performance and adherence
through built-in controls, proper isolation, and automated
validation, enabling efficient scientific work without regulatory
burden.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Design distinct computing environments with appropriate boundaries
for different regulatory contexts. Isolation allows tailored
controls while avoiding regulatory requirements from limiting
innovation in research-focused areas.

Use infrastructure as code and immutable deployment patterns that
enhance both security and regulatory adherence. Immutable
approaches block configuration drift while creating inherently
more auditable and consistent environments.

Create a library of pre-validated infrastructure components and
patterns. Pre-validated components accelerate deployment while
maintaining compliance-aligned assurance through already-verified
building blocks.

Integrate mechanisms directly into the infrastructure rather than
as external processes. Embedded controls reduce overhead while
blocking continuous compliance-aligned assurance without manual
intervention.

Design infrastructure that maintains computational efficiency
while meeting regulatory requirements. Performance-preserving
approaches stop regulatory controls from becoming computational
bottlenecks.

### Implementation steps

- Design segregated domains with controlled data transfer
between boundaries.
- Implement immutable deployment with versioned infrastructure
processes.
- Build validated component library with pre-approved
templates.
- Deploy automated built-in audit trails and verification.
- Optimize balance between controls and performance
requirements.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsperf07-bp02.html*

---

# LSPERF07-BP03 Develop an agile change management process

Develop a specialized change management process that enables rapid
iteration for scientific computing while maintaining GxP adherence
through a combination of procedural and technical safeguards.
Implement digital solutions for documentation-as-code that creates
machine-readable artifacts alongside software development, establish
predefined patterns for common computational workflows, and deploy
automated monitoring tools that provide real-time verification
without manual intervention. Create cross-functional teams combining
computational scientists, IT specialists and experts who
collaboratively define fit-for-purpose validation approaches that
protect data integrity and regulatory requirements while enabling
the performance optimization and innovation velocity required by
modern life sciences research.

**Desired outcome:** Establish
efficient change management that enables fast scientific progress
while maintaining adherence through automated documentation,
predefined patterns, and cross-functional collaboration.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Design change processes specifically optimized for computational
science workflows. Specialized frameworks balance requirements
with the need for scientific agility and rapid iteration.

Integrate documentation directly into development workflows using
automated approaches. Documentation-as-code creates
machine-readable artifacts that evolve alongside computational
systems.

Create standardized approaches for common scientific computing
challenges. Pre-defined patterns accelerate implementation while
improving the consistency of regulatory and GxP approaches across
research platforms.

Implement automated monitoring that continuously validates the
state of systems. Real-time verification replaces periodic manual
audits with constant assurance of compliant operations.

Establish collaborative teams that combine scientific, technical,
and compliance-aligned expertise. Integrated teams develop
balanced approaches that satisfy stakeholders while optimizing for
research outcomes.

### Implementation steps

- Create streamlined change management tailored for research
computing needs.
- Deploy automated documentation with version-controlled
artifacts.
- Develop reusable patterns for common computational
processes.
- Implement monitoring tools with alerts for potential issues.
- Create collaborative governance between scientists, IT, and
auditing teams.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsperf07-bp03.html*

---
