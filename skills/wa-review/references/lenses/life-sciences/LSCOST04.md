# LSCOST04 — Optimize over time

**Pillar**: Cost Optimization  
**Best Practices**: 2

---

# LSCOST04-BP01 Implement tiered storage strategies aligned with data access patterns and retention requirements

Design and implement a tiered storage architecture that matches
storage costs to data value and access patterns while verifying
adherence to retention requirements. Classify research data based on
access frequency, regulatory requirements, and business value to
determine appropriate storage tiers. Move infrequently accessed data
to lower-cost storage while maintaining required accessibility and
integrity controls.

**Desired outcome:** Tiered storage
architecture that optimizes data lifecycle costs through strategic
placement of research data across storage tiers based on access
patterns and requirements, verifying regulatory adherence while
minimizing storage expenses and maintaining seamless data
accessibility throughout the research lifecycle.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Tiered storage strategies optimize costs while maintaining
adherence in life sciences data management. Categorize research
data based on access patterns, regulatory requirements, and
business value to determine appropriate storage tiers. Match
storage solutions to data requirements, from frequently accessed
data needing high performance to archival data requiring long-term
retention. Consider regulations (GxP, HIPAA, GDPR) when designing
storage tiers. Implement necessary controls for security,
encryption, and audit trails. Automate data movement between tiers
based on defined policies while verifying that data remains
accessible and protected throughout its lifecycle.

### Implementation steps

- Conduct a comprehensive inventory of research data. Classify
each dataset based on its type, access frequency, value, and
regulatory requirements.
- Evaluate available storage options and create 3-4 tiers
based on performance needs and cost considerations. Document
clear policies for each tier, including what type of data
belongs in each.
- Create policies for moving data between tiers, and define
triggers for these transitions. Verify that each policy
complies with relevant regulatory requirements.
- Configure storage classes in your cloud environment and set
up appropriate access controls and encryption. Implement
automated lifecycle policies to manage data movement between
tiers.
- Create procedures for initial data classification and
storage. Establish processes for data retrieval and define
clear roles and responsibilities for managing the tiered
storage system.
- Thoroughly test data movement between tiers and validate
that access controls and encryption are working as intended.
Perform mock audits to check adherence to regulatory
requirements.
- Train researchers and IT staff on the new storage strategy.
Create comprehensive documentation of the tiered storage
architecture, policies, and user guides for accessing data
in different tiers.
- Implement monitoring for storage usage and costs. Regularly
review access patterns and adjust tiering policies as needed
to optimize performance and cost-efficiency.
- Perform quarterly reviews of storage usage and costs.
Annually reassess the overall tiered storage strategy and
update policies based on changing research needs and
regulatory requirements.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lscost04-bp01.html*

---

# LSCOST04-BP02 Implement data retention and deletion policies aligned with regulatory requirements

Develop and enforce comprehensive data retention and deletion
policies that comply with industry regulations while minimizing
unnecessary storage costs. These policies should clearly define how
long different types of research data must be retained, how it
should be stored, and when it can be safely deleted or archived.

**Desired outcome:** A comprehensive,
automated data retention and deletion framework that improves
regulatory adherence while minimizing storage costs through
intelligent lifecycle management, enabling safe data disposal when
appropriate and maintaining complete audit trails for data lifecycle
decisions across research phases.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Organizations should first analyze their data usage patterns and
regulatory requirements across different research stages.
Implement automated tools for monitoring data access patterns and
costs. Develop clear policies for data classification and
retention requirements. Create automated workflows for moving data
between storage tiers based on age and usage while maintaining
audit trails. Regularly review and optimize storage costs while
verifying that regulatory requirements are met.

### Implementation steps

- Analyze current data storage costs and usage patterns across
research phases.

Document regulatory requirements for different data
types and research stages.
- Define metrics for measuring storage optimization
success and establish baseline costs.
- Create data classification policies that balance
research needs with cost optimization opportunities.

- Create comprehensive data lifecycle policies that define
storage tiers, retention periods, and movement criteria.

Develop automation rules for data movement between
storage tiers based on age and access patterns.
- Establish regulatory documentation requirements for data
lifecycle changes.
- Define processes for data retrieval and restoration when
needed.

- Deploy automated tools for monitoring data usage and
implementing lifecycle policies.

Configure storage tiering based on defined policies and
regulatory requirements.
- Implement automated documentation and audit trail
creation for each data movement.
- Set up cost monitoring and optimization tools with
appropriate alerting.

- Regularly review storage costs and usage patterns to
identify optimization opportunities.

Adjust automation rules based on changing research needs
and cost patterns.
- Conduct periodic audits to verify that requirements are
met.
- Update policies and procedures based on new regulatory
requirements or research needs.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lscost04-bp02.html*

---
