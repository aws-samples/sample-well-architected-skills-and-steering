**Saga**: Quality assurance
**Capability**: QA.ST — Security testing

---

# [QA.ST.3] Use application risk assessments for secure software design

**Category:** FOUNDATIONAL

Application risk assessments integrate security considerations
directly into the software development lifecycle. At the
earliest stages of the development lifecycle, design reviews
focus on the planned architecture, features, and flow of the
application. During these reviews, security experts should
assist with making design choices to prevent introducing weak
points that could introduce vulnerabilities. The primary goal
is to make security-centric design decisions, eliminating
vulnerabilities before they're developed.

After the design phase, threat modeling dives deeper into
potential security threats that the finalized design might
face. This results in a list of possible attack vectors,
identifying how an attacker might exploit vulnerabilities. An
inverse approach to threat modeling is attack modeling, which
identifies specific attacks or vulnerabilities and examines
how they can be exploited. Both methods offer insights into
possible vulnerabilities and guide developing protective
measures.

Once vulnerabilities are identified through design reviews and
potential threats through modeling, these insights should
directly inform the software's security requirements. As
applications evolve or as new threats emerge, periodically
revisit and update both functional and non-functional
requirements. Functional requirements involves measures like
input validation, session management, or error handling.
Non-functional requirements includes making changes that
impact to performance, scalability, and reliability under
security threats.

Translate identified risks into actionable user stories that detail potential abuse
or misuse scenarios. Add these stories into the backlog for the team to address during
development. Attach a test case to each story to validate its effective resolution,
establishing a clear *definition of done* for developers to adhere to.

**Related information:**

- [Threat
Composer](https://awslabs.github.io/threat-composer)
- [Threat
modeling for builders](https://catalog.workshops.aws/threatmodel/)
- [AWS Security Maturity Model - Threat Modeling](https://maturitymodel.security.aws.dev/en/3.-efficient/threat-modeling/)
- [How
to approach threat modeling](https://aws.amazon.com/blogs/security/how-to-approach-threat-modeling/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/qa.st.3-use-application-risk-assessments-for-secure-software-design.html*
