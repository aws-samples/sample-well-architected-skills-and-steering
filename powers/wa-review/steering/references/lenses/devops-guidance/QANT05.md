**Saga**: Quality assurance
**Capability**: QA.NT — Non-functional testing

---

# [QA.NT.5] Automate adherence to compliance standards through conformance testing

**Category:** RECOMMENDED

Conformance testing, often referred to as compliance testing, verifies that a system
meets internal and external compliance requirements. It compares the system's behaviors,
functions, and capabilities with predefined criteria from recognized standards or
specifications.

Conformance testing acts as a safeguard, ensuring that while agility is prioritized,
compliance isn't compromised. There are many regulated industries, such as finance,
healthcare, or aerospace, that have a strict set of compliance requirements which must be
met when delivering software. Historically, balancing fast software delivery with
stringent compliance was a challenge in these industries. Generating the documentation and
proof required to maintain compliance was often a manual, time-intensive step that created
a bottleneck at the end of the development lifecycle.

Conformance testing integrated into deployment pipelines provides a solution to this
problem by automating the creation of compliance attestations and documentation. It can be
used to meet both internal and external compliance requirements. Start by determining both
internal (for example, risk assessment policies, or change management procedures) and
external standards (for example, [GxP](https://aws.amazon.com/compliance/gxp-part-11-annex-11/) for life sciences). Prioritize and
choose the relevant parts of the standards which can be automated (for example, GxP
Installation Qualification report). Ensure that conformance tests remain current by
updating them according to evolving standards.

Use the data at your disposal, including APIs, output from other forms of testing,
and possibly additional data from IT Service Management (ITSM) and Configuration
Management Databases (CMDB). Embed conformance testing scripts into deployment pipelines
to generate real-time compliance attestations and documentation using this data. Consider
using machine-readable markup languages, such as JSON and YAML, to store the compliance
artifacts. If the markup languages are not considered sufficiently human readable by
auditors, then retain the ability to convert these markdown files into another format.
This conversion can then be done when needed, not as a default step, removing the burden
of document management where it is not absolutely necessary.

**Related information:**

- [Wikipedia
- Conformance testing](https://en.wikipedia.org/wiki/Conformance_testing)
- [Qualification
Strategy for Life Science Organizations](https://docs.aws.amazon.com/whitepapers/latest/gxp-systems-on-aws/qualification-strategy-for-life-science-organizations.html)
- [Automating
the Installation Qualification (IQ) Step to Expedite GxP
Compliance](https://aws.amazon.com/blogs/industries/automating-the-installation-qualification-iq-step-to-expedite-gxp-compliance/)
- [Automating
GxP compliance in the cloud: Best practices and
architecture guidelines](https://aws.amazon.com/blogs/industries/automating-gxp-compliance-in-the-cloud-best-practices-and-architecture-guidelines/)
- [Automating
GxP Infrastructure Installation Qualification on AWS with
Chef InSpec](https://aws.amazon.com/blogs/industries/automating-gxp-infrastructure-installation-qualification-on-aws-with-chef-inspec/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/qa.nt.5-automate-adherence-to-compliance-standards-through-conformance-testing.html*
