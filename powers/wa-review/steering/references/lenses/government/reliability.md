# Reliability

**Pages**: 1

---

# Reliability pillar

The reliability pillar encompasses the ability of a service to
perform its intended function correctly and consistently when it’s
expected to. This includes the ability to operate and test the
service through its total lifecycle and includes a high level of
planning around service continuity and perceived reliability by
the public.

The following questions and best practices are designed to
complement the best practices in the
[Reliability
Pillar whitepaper](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html).

GL-REL-01: How do you test the
service and demonstrate resilience?

- **Establish and document test-driven design and implementation,
including scenario testing and mitigation planning:** Establish system and
process test environments, including scaled functional testing, user testing with the
public, war gaming for procedural and scenario testing, and the potential for regulatory
sandboxes for policy testing.

**Improvement plan** – Consider running regular AWS
Well-Architected *game days* in the lead up to
launching a new product to identify areas for improvement and end to end
system/service reliability. Encourage the organization to consider persistent team
structures that span policy and delivery in their forward planning for the service,
design and run scenarios and mitigation planning sessions with the customer and scaled
test processes and planning.

- **Seek peer review of reliability planning:** Run and
document feedback and recommendations from peer review sessions for the service and
reliability planning.

**Improvement plan** – Support the customer to engage
with relevant peers to review, share, and help assure the best possible reliability of
the service.

GL-REL-02: How do you plan for
service continuity?

Continuity of service is one of the highest priorities for government services. Many
government services are not optional for people. These services are relied upon when we are at
our most vulnerable. Business continuity is especially important to verify that end users are
not put at risk from a lack of access to critical government services and systems.

- **Assess the impact of downtime and service deadlines:** Test
and document the assumptions about the likely impacts of service downtime, especially on
vulnerable people and communities, and around anticipated deadlines such as elections,
seasonal emergencies (such as fire season), and waiting times at medical care facilities.
Capture these assumptions in user journey maps and document remediations and strategies in
the concept of operations document.

**Improvement plan** – Analyze and document the full
impacts of downtime on end users, stakeholders, and others who depend on the service,
using a variety of relevant planned and unplanned scenarios.

- **Plan for a graceful degradation of service, with appropriate
fail-overs and alternative service pathways:** Verify that the service has
appropriate fail-over strategies proportionate to the risk, and that users can identify
alternative pathways to the service, including offline and phone-based user journeys.
Verify that alternative service pathways are quickly discoverable by end users, even if
the digital services are down. Have a stakeholder list, FAQs, and a communications plan
prepared.

**Improvement plan** – Use scenario planning, user
journey maps, and support the organization to resource and plan for service
degradation, failovers, and alternative pathways for the service.

- **Verify and document the processes and public reporting of
post-incident reviews:** Government departments often have specific
requirements to report incidents publicly, and even when there isn't a requirement, it is
often good practice to help maintain high public trust and confidence in the public
institution. Identifying any requirements and ensuring the processes and expectations are
clear and documented can assist in future incident management.

**Improvement plan** – Work with the organization to
document any specific or legislative requirements to report incidents publicly, and
document relevant processes.

## Resources

- [Protect critical services with new Continuity of Government IT on AWS solution
guide](https://aws.amazon.com/blogs/publicsector/protect-critical-services-new-continuity-government-it-solution-aws/)
- [Leverage
the latest cloud technologies to build a resilient organization](https://aws.amazon.com/government-education/building-resilience/)
- [Modernizing government for the new normal: Advice for building resilience](https://aws.amazon.com/blogs/publicsector/modernizing-government-new-normal-advice-for-building-resiliency/)
- [AWS
Well-Architected game days](https://wa.aws.amazon.com/wat.concept.gameday.en.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/government-lens/reliability-pillar.html*

---
