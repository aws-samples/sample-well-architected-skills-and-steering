# Operational excellence

**Pages**: 3

---

# Reshape the operating model

As governments seek to digitally transform, technology expertise and experience is
essential to achieving strategic policy outcomes. To verify that digital delivery of mission
objectives can consistently evolve and be delivered successfully, organizational structures
must be reshaped and be inclusive of both business and technology experts.

Many government departments have functionally segmented structures that create a
challenge for modern delivery of portfolio objectives. These departments often have
technology in a corporate silo or have outsourced their technology entirely. This structure
has left many governments with an operational divide between their business and technology
staff that slows or prevents the realization of new strategic intent. Meanwhile, in the
context of a rapidly changing world, many government organizations are actively seeking
solution and service agility.

GL-OPS-01: How do you adjust
the organizational structure to better realize strategic policy
outcomes?

- **Support the establishment of persistent and multi-disciplinary
team structures:** When services are developed as projects, and teams
assembled for the project are disbanded at the end of the project, the service is left
without persistent product management. Establish team structures and governance models
that can persist beyond the end of project.

**Improvement plan** – Encourage the organization
to consider persistent team structures that span policy and delivery in their
forward planning for the service. Consider running a Cloud Adoption Framework
assessment to support operational assessment and planning.

- **Enable team structures and appropriate governance to delegate
delivery decision making:** Delivery and innovation happen at the speed of
trust. Service and product owners require a reasonable amount of decision-making
autonomy to realize continuous improvement and operational reform in a timely manner.
This autonomy has the benefit of streamlining escalation, unblocking slow and laborious
go-live protocols, and minimizing decision gaps between business owners and technology
people, and can be complemented by oversight mechanisms without slowing or impeding good
service delivery.

**Improvement plan** – Encourage the organization
to consider delegation of two-door decision making, including continuous improvement
and operational reforms in their forward planning for the service.

- **Support the creation of a Concept of Operations for the
service:** Create a *Concept of Operations
document* that explicitly describes how the service will continually improve
over time, with supported and authorized product management and team. Its contents might
include delegated decision-making mechanisms, product management in government, outcomes
or product-based funding, and how to bring multi-disciplinary teams together to manage
aspects of the service.

**Improvement plan** – If the organization does not
have a Concept of Operations document, or equivalent documentation, encourage the
organization to consider it in their forward planning for the service.

- **Consider all relevant feedback loops:** Consider what
additional feedback loops might complement the [feedback loops defined in the Operational Excellence Pillar](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_evolve_ops_feedback_loops.html) in the special
context of the department and jurisdiction. For example, how might staff or the public
report legal or impact concerns.

**Improvement plan** – Identify and document
additional feedback loops, and build these into the service architecture, escalation
mechanisms and operating model as appropriate.

- **Consider a minimum viable product (MVP) deployment model where
viable:** Many government projects take a *big bang*
deployment model approach, attempting to develop all features and then launch a fully
formed product. This approach can create substantial risk, which can be minimized
through iterative and MVP-based deployment. An MVP deployment model identifies the
minimum features needed for a functional product to launch, often initially to a subset
of end users, and then scales and adds features in a test-driven way. This method
accelerates early identification of and validation of product goals, while minimizing
risk, delivering early value, and ensuring that all product features are tested for
effectiveness with end users.

**Improvement plan** – If the organization does not
want to adopt an MVP-based deployment model, advise on the risk and encourage the
organization to consider it in their forward planning for the service. Provide use
cases where appropriate.

- **Document and engage with cultural context:** Understand
the cultural context, including indigenous or First Nations needs. Ensure culturally
diverse needs are included in user research, user testing, and other service
engagements, and where possible diverse representation in product teams and governance
can be applied.

**Improvement plan** – Encourage the organization
to consider cultural context in their forward planning for the service.

GL-OPS-02: How do you verify that digital experiences remain operational and
relevant over time?

Some government departments can only fund changes to a service through a new funding
application, which can make change slow and expensive. This funding model can lead to a
great product becoming less than great over time.

- **Ensure that government and other staff are well supported to
operate the service:** The more empowered public servants are to understand,
manage, and improve their services, the more they are positioned to be proactive and
effective in delivering great services, both directly and with vendors.

**Improvement plan** – Provide information and
access to relevant AWS skills and capabilities training for the service, and
support the organization to identify gaps throughout the process, with AWS digital
transformation guides, whitepapers, and case studies.

- **Embed continuous improvement into the operating model:**
Continuous improvement helps make sure that public-facing government digital experiences
don’t deteriorate over time. Investment must be made to maintain the continuous
evolution and maintenance of the service to match the expectations and feedback of
consumers. If you have a fixed or scheduled approach to improvement, support the best
practices possible.

**Improvement plan** – Run change scenarios with
the organization, including small and significant changes to the service, to
identify and document how continuous improvements will be enabled, and with what
oversight and decision making.

- **Implement a design-led agile development and funding
framework:** Ensure that the operating and funding model supports a
design-led agile approach that incorporates:

Early feedback on requirements from citizens, industry,
and government
- Testing and evolving of non-technical go-live processes
the government might need to conduct
- Consistently and continuously evolve functionality as
the service feedback and requirements mature over time
- Align with the concept of operations document to make sure that expectations
are met during service development.

- **Improvement plan** – Support the need for an
agile development framework, providing use cases where helpful, and AWS digital
transformation guides, whitepapers, and case studies.

GL-OPS-03: How do you verify that the service meets operational transparency
requirements?

- **Document how the service delivers
operational accountability requirements:** Many
governments have strong requirements around operational
accountability through various audit and reporting
mechanisms. In some jurisdictions, there are public
reporting requirements for public facing services.

**Improvement plan** – Include any reporting
requirements in the concept of operations document, along with the chain of those
responsible.

- **Document how citizens and companies will be kept
informed:** To manage expectations and make it simple for consumers to use
the service, create high quality communications (both marketing and transactional),
supporting information, and technical documentation for the service.

**Improvement plan** – Include the public
communications approach in the concept of operations document, including who is
responsible.

GL-OPS-04: How can you improve
solution definition criteria?

Taking time to ensure the right solution is defined from the start can save money, time,
and effort down the line. This best practice encourages ways to validate and likely iterate
the solution definition through policy, problem, and opportunity validation, and testing
with end users.

- **Ensure that multiple concepts are tested with end users prior to
deciding on a solution:** Testing concepts provides the opportunity to
validate assumptions about what might work, and to proceed only with tested policy
interventions. Sometimes the best solution is no solution at all, a regulation, or a
change to an existing service.

**Improvement plan** – Encourage the use of the
AWS Digital Innovation program, including Working Backwards workshops, to explore
and identify the purpose and goals for the service. Leverage service and system
design, as is helpful.

- **Identify patterns in the desired service capabilities and intended
service usage:** Patterns might appear as emergent (such as self-sovereign
digital identity), or common (such as a notification service, or application of
government legislation and rules in a desired service capability). Patterns should have
broad use case applicability with high volumes of reuse and could be candidates for
whole of government reusable capabilities.

**Improvement plan** – Identify and recommend
potential reusable patterns for consideration in the solution architecture.

- **Define foundational reusable
components:** Informed by the previous pattern
identification, look for opportunities to standardize
people, processes, and technology solutions to optimize
delivery, implementation, and operation of one or many
components that support a service capability.

**Improvement plan** – Consider relevant government
architectural frameworks, including from the [Scenarios](./scenarios.html) section of this whitepaper.

GL-OPS-05: How can you improve solution acquisition criteria?

When considering technology acquisition for a service, you’ll need a business or
organization level understanding of the government mission and policy objectives, government
process, standards, and how these map to service capabilities, which then inform solution
requirements. For more information, see [Enabling services outcomes for government](./enabling-services-outcomes-for-government.html).

Not all components have the same business and technical requirements. Consider the
following best practices when designing, evaluating, or acquiring solutions and
technologies:

- **Consider and prioritize reuse where appropriate:**
Leverage modular architecture and use existing design systems, tools, environments, and
open-source government solutions, where feasible, to minimize duplication of systems and
efforts, and to enable future system agility and extendability of the solution. Provide
relevant AWS reference architectures to support modular, virtualized, and utility
based approaches, enabling greatest extendibility and scalability of the service,
ideally with an omni-channel approach if public facing.

**Improvement plan** – Look for relevant existing
tools, solutions, or capabilities available in the jurisdiction or globally, and
consider the AWS open source catalog.

- **Consider build versus buy/acquire strategically:** If an
existing solution can be used with minor modification, you might prefer an off the shelf
(proprietary or open source) tool. If you require system agility, if a solution does not
yet exist, or if you want to integrate multiple systems into a channel, consider the
benefits of building it yourself. The capabilities and strengths of the customer's team
should be considered and planned for to ensure service viability, both technically and
financially.

**Improvement plan** – Consider an AWS Digital
Innovation program to work backwards from the problem and identify the requirements
and capabilities needed for a new solution. Support the customer to take a strategic
approach to designing the architecture and sourcing of the service components. Where
minimal customization is required and the solution is mission-aligned, consider
purchasing a solution to meet a particular need, noting most modern services will
require a blend of solutions.

- **Consider where code, research, and efforts can be
shared:** Reusable foundational components and solutions could be shared back
to the open government community through open-source licensing.

**Improvement plan** – Provide guidance on sharing
and contributing back to projects or to government.

- **Consider a sustainable and delivery focused approach to
sourcing:** Outsourcing might be suitable in the short term if there is a
staffing constraint for design, implementation, and ongoing operations. Customers are
encouraged to develop and maintain a minimum viable internal expertise and delivery
capability, to maintain control over the strategic direction, product management,
continuous improvement, and the selection criteria as above. These competencies can
support and leverage vendors, while maintaining the necessary internal agility for
operational excellence. Explore flexible procurement arrangements, such as sprint or
outcome-based procurement.

**Improvement plan** – Provide guidance, support,
and training materials to support capability uplift.

- **Consider the suitability of solution licensing:**
Licensing conditions can sometimes constrain the effectiveness or financial viability of
a service in several ways, such as:

If a user-based license model is used for a government service with significant
citizen uptake.
- License terms that are bound by hardware configurations can have an impact on
service agility with financial consequences to scaling the government service as
demand evolves.
- Creating a preferential technology ecosystem that inhibits the government’s use
of other technologies can limit the ability to innovate and scale.

- **Improvement plan** – Organizations will have
their own capabilities for this domain.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/government-lens/reshape-the-operating-model.html*

---

# Organizational risk

Every service should have a risk management plan to assess and manage risk. Risk
management should be comprehensive to consider all hazards, including how the cloud service
supports risk mitigation by design. This assessment is essential to make informed design
decisions. Service risk must be contextualized as part of the broader organization risk
strategy.

GL-OPS-6: Do you have adequate
people and process risk management systems in place covering a
broad risk spectrum?

- **Take an all-hazards approach:** Include consideration of
personnel, supply chain, cyber security, information security, and natural risks.

Have a strong understanding of controls that can be inherited from the cloud
service provider, for example, the physical security of data centers.
- Consider sovereign resilience requirements, which can aid in the survival of
government in extreme circumstances.

- **Improvement plan** – Document the preceding items
into the relevant security documentation or concept of operations document.

- **Develop a risk management plan:** Have a plan that
supports ongoing risk assessment and treatment, and verifies that the service risk is
contextualized as part of the organization’s risk profile.

Decide what matters most to your organization, and to
your service. Considerations include social, cultural,
political or regional issues, economic and technology
trends, policy and law, and your organizations aims,
policies and strategies.
- Identify, analyze, and evaluate risks to help make sure
that adequate treatments are identified so that your
service is resilient.
- When considering the risk of a service, consider whether
the risk is acceptable for the associated service
outcome it achieves.

- **Improvement plan** – Document these items into
the relevant security documentation or concept of operations document.

- **Align with required compliance frameworks:** When
implementing compliance frameworks such as [CSA](https://cloudsecurityalliance.org/), [NIST](https://www.nist.gov/cybersecurity), [CISPE](https://aws.amazon.com/compliance/cispe/), [ISM](https://aws.amazon.com/blogs/publicsector/how-australian-government-agencies-can-navigate-ism-essential-8-compliance-aws/), and [ISO](https://aws.amazon.com/compliance/iso-certified/), verify that the framework is appropriate for the risks requiring
mitigation and that it is considered as part of the broader organizations risk strategy
and risk appetite statement.

**Improvement plan** – Document the preceding items
into the relevant security documentation or concept of operations document, and
provide relevant AWS certifications and risk management guides and case
studies.

- **Determine the necessary conditions of
engagement:** Consider the Business Impact Level (BIL) of the service to
determine personnel requirements, such as security clearances, vetting, data handling,
and risk training.

**Improvement plan** – Document the preceding items
into the relevant security documentation or concept of operations document, and
provide the AWS certification programs as required.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/government-lens/organizational-risk.html*

---

# Resources

- [AWS Compliance Programs](https://aws.amazon.com/compliance/programs/)
- [Open source at AWS](https://aws.amazon.com/opensource/)
- [The AWS Cloud Adoption
Framework (AWS CAF)](https://aws.amazon.com/cloud-adoption-framework/)

[AWS Cloud Adoption Framework whitepaper](https://docs.aws.amazon.com/whitepapers/latest/overview-aws-cloud-adoption-framework/welcome.html)
- [Risk
Management in the AWS Cloud Adoption Framework](https://docs.aws.amazon.com/whitepapers/latest/aws-caf-governance-perspective/risk-management.html)
- [AWS risk and compliance program](https://docs.aws.amazon.com/whitepapers/latest/aws-risk-and-compliance/aws-risk-and-compliance-program.html)

- [Building your Cloud Operating Model](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-cloud-operating-model/welcome.html)
- [How
governments can transform services securely in the cloud](https://aws.amazon.com/blogs/publicsector/how-governments-can-transform-services-securely-cloud/)
- AWS digital and operational transformation guidance

[Digital Transformation: The Why, Who, How, and What – Part 1, “The Why”](https://aws.amazon.com/blogs/enterprise-strategy/digital-transformation-the-why-who-how-and-what-part-1-the-why/)
- [Digital Transformation: The Why, Who, How, and What – Part 2, “The Who”](https://aws.amazon.com/blogs/enterprise-strategy/digital-transformation-the-why-who-how-and-what-part-2-the-who/)
- [Four Steps Toward Digital Government](https://aws.amazon.com/blogs/enterprise-strategy/four-steps-toward-digital-government/)

- AWS digital and data controls

[AWS
Digital Sovereignty Pledge: Control without compromise](https://aws.amazon.com/blogs/security/aws-digital-sovereignty-pledge-control-without-compromise/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/government-lens/resources.html*

---
