# RAIUC02 — Identify use case stakeholders

**Best Practices**: 2

---

# RAIUC02-BP01 Identify downstream stakeholders

Identify a person, group, or entity involved in or affected by the
operation of the proposed AI system. Consider different stakeholder
categories, like primary users, secondary users, and indirect
stakeholders. Consider whether vulnerable populations could be
stakeholders. Seek out individuals with different perspectives from
those of the builder team, including potential stakeholder groups
and different organizational functions, to identify possible
stakeholders.

**Level of risk exposed if this best practice
is not established:** High

## Implementation considerations

- Organize workshops with potential end users, buyers, builders,
and operators to brainstorm potential stakeholders. Include
people with different backgrounds and expertise.
- Categorize identified stakeholders into primary users (for
example, those providing inputs and receiving outputs),
secondary users (for example, those whose data may used as
input), and indirect stakeholders (for example, those affected
by system operations). Include vulnerable populations across
categories.
- Analyze each stakeholder group's relationship to the AI system
by documenting their expected interactions, potential impacts,
and specific needs or concerns. Break down larger stakeholder
groups into relevant subgroups for detailed analysis.
- Review and validate the stakeholder list periodically
throughout system development to capture emerging stakeholder
groups and changing relationships. Consider how system
modifications might affect different stakeholder groups.

## Resources

**Related documents:**

- [NIST
Artificial Intelligence Risk Management Framework (NIST AI
100-1)](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf): MAP1.1, MAP5.1, GOVERN5.1

*Source: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raiuc02-bp01.html*

---

# RAIUC02-BP02 Identify contributing and other upstream stakeholders

Identify the full set of people involved in designing, developing,
deploying, operating, funding, supplying, and approving an AI system
built by your team. The set may include product managers, engineers,
data scientists, AI oversight functions (compliance, assurance,
risk), domain experts on topics such as security, privacy, existing
AI systems, or the use case itself, as well as other contributors or
users.

**Level of risk exposed if this best practice
is not established:** High

## Implementation considerations

- Map out the roles involved in your AI system's lifecycle from
initial concept to ongoing operations. Consider product,
engineering, data science, legal, security, infrastructure,
and other company functions that provide input on requirements
or constraints.
- Identify external stakeholders who contribute to or influence
your system even though they are not part of your direct team.
This includes vendors who supply data or model components and
upstream teams whose decisions affect your system's design or
operation.
- Document the specific ways each stakeholder group contributes
to or influences your system, rather than just listing names
and titles. For example, note that your security team reviews
threat models and sets deployment constraints, while your
legal team provides guidance on data use and compliance
obligations, and your infrastructure team manages the
computing Resources your system runs on.
- Include oversight and governance stakeholders who may not be
involved in day-to-day development but have authority over key
decisions about your system. This covers compliance officers
who approve deployments, risk management teams who set
acceptable use policies, and executive sponsors who control
funding and strategic direction.
- Create a stakeholder contact list with clear points of contact
for each group, including backup contacts and escalation paths
for important decisions. Keep this list updated as team
structures change and make sure everyone on your team knows
who to reach out to for different types of questions or
approvals throughout the system's development and operation.

## Resources

**Related documents:**

- [ISO/IEC
42001:2023](https://www.iso.org/standard/42001) A.3.2 AI roles and responsibilities
- [NIST
Artificial Intelligence Risk Management Framework (NIST AI
100-1)](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf): MAP1.1, MAP1.2, GOVERN5.1

*Source: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/raiuc02-bp02.html*

---
