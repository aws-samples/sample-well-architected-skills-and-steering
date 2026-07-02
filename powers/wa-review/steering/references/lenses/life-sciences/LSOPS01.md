# LSOPS01 — Organization

**Pillar**: Operational Excellence  
**Best Practices**: 1

---

# LSOPS01-BP01 Regularly identify and classify applicable regulatory frameworks

Conduct a systematic assessment to identify applicable regulatory
frameworks based on product type assessment, geographic analysis,
data classification, development phase mapping, and risk-based
classification for comprehensive regulatory coverage for your life
sciences workloads. Repeat this process as the project and its
requirements evolve over time.

**Desired outcome:** A comprehensive
regulatory framework map that clearly identifies applicable
regulations, their specific requirements, and how they impact
different aspects of your life sciences project. This enables
informed decision-making and verifies that you don't overlook
regulatory requirements.

**Common anti-patterns:**

- You assume a one-size-fits-all approach to auditing without
accounting for specific regional or other requirements.
- You identify applicable regulatory frameworks as a one-time
activity and assume adherence even as the project evolves.
- You assume the applicable regulatory frameworks have been
identified without regular review to verify.

**Benefits of establishing this best
practice:**

- Provides clear guidance for project stakeholders on regulatory
expectations.
- Identifies required regulatory submissions and approvals.
- Reduces risk of becoming non-compliant over time.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

GxP refers to the regulations and guidelines applicable to life
sciences organizations that make food and medical products such as
drugs, medical devices, and medical software applications.
Depending on the location of research and development, governing
bodies may include U.S. Food & Drug Administration
([FDA](https://www.fda.gov/)), European
Medicines Agency
([EMA](https://www.ema.europa.eu/en/homepage)),
or International Council for Harmonisation (ICH) Good Clinical
Practice guideline
([ICH-GCP](https://ich.org/)). In the US,
handling of Personal Health Information (PHI) is governed by
[HIPAA](https://www.hhs.gov/hipaa/for-professionals/privacy/laws-regulations/index.html),
in the EU, General Data Protection Regulation
([GDPR](https://gdpr.eu/)). If you are
manufacturing a product, you need to align with Good Manufacturing
Practices
([GMP](https://www.who.int/teams/health-product-policy-and-standards/standards-and-specifications/norms-and-standards/gmp)).

Review regulations related to your project location and industry.
Consider what type of data you will be handling in your
application, where it is collected, and where it is stored.
Consider if there are data sovereignty or residency requirements
that would determine the Region in which data can be stored or
processed.

### Implementation steps

- Identify relevant regulatory frameworks based on the type of
project and how data is managed, collected, and stored.
- Document the frameworks that apply to your project
and region. Review the resources available from
[AWS Compliance Programs](https://aws.amazon.com/compliance/programs/) to find AWS resources for common
regulatory frameworks.
- Identify requirements that are common across frameworks to
identify necessary checks to satisfy applicable controls.

## Resources

**Related documents:**

- [Don't
Blame Regulators: How Software Excellence Satisfies
Compliance](https://aws.amazon.com/blogs/enterprise-strategy/stop-blaming-regulations-how-software-excellence-satisfies-compliance/)
- [Life
Sciences Compliance in the Cloud](https://aws.amazon.com/health/life-sciences-compliance/)
- [GxP](https://aws.amazon.com/compliance/gxp-part-11-annex-11/)
- [GxP
Systems on AWS](https://d0.awsstatic.com/whitepapers/compliance/Using_AWS_in_GxP_Systems.pdf)

**Related tools:**

- [AWS Audit Manager](https://aws.amazon.com/audit-manager/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsops01-bp01.html*

---
