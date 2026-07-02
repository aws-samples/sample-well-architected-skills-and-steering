# GAMESEC10 — Threat modeling

**Pillar**: Security  
**Best Practices**: 1

---

# GAMESEC10-BP01 Determine when and how to complete threat modeling exercises throughout your application development lifecycle

There is no one single best way to approach threat modeling. Details for when and how to do this will vary based on the unique needs of your game studio. For example, depending on the size of your studio, you may have team members who are involved in one or multiple aspects of the threat modeling process.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

The [AWS Security Blog](https://aws.amazon.com/blogs/security/how-to-approach-threat-modeling/) provides an overview for considerations to keep in mind when devising your strategy for threat modeling, such as:

- Which of your team members and personas should be involved in
threat modeling
- How to determine the appropriate workflow tools to use
- How to determine ownership of various aspects of threat
modeling
- How to identify and evaluate security controls to be used
within your workload design

**Customer example**

AnyCompany Games begins by cataloging valuable assets such as
player data, game code and algorithms, in-game currencies,
user-generated content, and intellectual property like unreleased
content or proprietary engines. They consider different types of
potential bad actors such cheaters seeking unfair advantages, bad
actors attempting to steal personal or financial data, and
malicious users trying to disrupt gameplay.

Throughout the development process, AnyCompany Games uses threat
models to guide secure coding practices and influence testing
strategies to focus on high-risk areas. Before a game launch, they
conduct comprehensive threat modeling reviews to assess readiness
for anticipated player loads and unauthorized access attempts, and
to prepare incident response procedures.

### Implementation steps

- Implement guardrails at every stage of your CI/CD pipeline.
- Use automation and tools to improve the efficiency of your
application security reviews.
- Use threat modeling as a process for improving the security
of your applications.

### Resources

- [AWS Security Blog: How to approach threat modeling](https://aws.amazon.com/blogs/security/how-to-approach-threat-modeling/)
- [NIST:
Guide to Data-Centric System Threat Modeling](https://csrc.nist.gov/pubs/sp/800/154/ipd)
- [Threat
modeling the right way for builders – AWS Skill Builder
virtual self-paced training](https://explore.skillbuilder.aws/learn/course/external/view/elearning/13274/threat-modeling-the-right-way-for-builders-workshop)
- [Threat
modeling for builders – AWS Workshop](https://catalog.workshops.aws/threatmodel)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/gamesec10-bp01.html*

---
