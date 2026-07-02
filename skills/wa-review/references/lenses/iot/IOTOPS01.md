# IOTOPS01 — Operational excellence

**Pillar**: Operational Excellence  
**Best Practices**: 2

---

## IOTOPS01-BP01 Conduct an OT and IT cybersecurity risk assessment using a common framework

When taking advantage of IT technologies in OT environments, it
is important to conduct a cybersecurity risk assessment using
frameworks to fully understand and proactively manage risks (for
example, ISA/IEC 62443).
Companies with maturing OT and IT convergence display common
patterns.

**Level of risk exposed if this best practice is not established:** Medium

**Prescriptive guidance IOTOPS01-BP01-01:** *Conduct a cyber-security risk assessment so that the risks, gaps and vulnerabilities are fully understood and can be proactively managed. Create and maintain an up-to-date threat model.*

- Proactively managing risks, gaps, and vulnerabilities
between OT and IT
- Up to date threat modeling capabilities for both OT and IT
- Define the system being assessed
- Identify threats, vulnerabilities and consequences of
unintended access or behavior
- Rank the discovered risks
- Develop a risk mitigation strategy

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/organization.html*

---

## IOTOPS01-BP02 Evaluate if OT and IT teams use separate policies and controls to manage cybersecurity risks or if they use the same policy

The ongoing maturity and adoption of cloud within IT and now
within OT creates a more common environment. A comprehensive
enterprise and OT security policy will encompass risks across
the entirety of the business. This allows for OT risks such as
safety to be recognized and addressed within IT. Conversely,
this allows for IT risks such as bots and ransomware to be
addressed within OT. While policies might converge, mitigation
strategies will still differ in many cases.

**Level of risk exposed if this best
practice is not established:** High

**Prescriptive
guidance IOTOPS01-BP02-01**

- OT and IT maintaining separate risk policies.
- The degree of isolation for process control and safety
networks.
- Interconnectedness of OT and IT systems and networks.
- Security risks that were applicable to either IT or OT might
now apply to both.
- Singular security control policy that governs both OT and
IT.
- Different mitigation strategies as appropriate for OT and
for IT. For example, the speed of patching is often
different between OT and IT by design.
- The use of holistic approaches to manage OT and IT risk.

### Resources

- [How
to approach threat modeling](https://aws.amazon.com/blogs/security/how-to-approach-threat-modeling/)
- [AWS Threat Modeling workshop](https://maturitymodel.security.aws.dev/en/3.-efficient/threat-modeling/)
- [Assessing
OT and IIoT cybersecurity risk](https://aws.amazon.com/blogs/iot/assessing-ot-and-iiot-cybersecurity-risk/)
- [Guidance
on using ISA/IEC 62443 for IIoT projects](https://aws.amazon.com/blogs/iot/guidance-on-using-isa-iec-62443-for-iiot-projects/)

IOTOPS02: Is there a central cloud
center of excellence (CCoE) with equivalent representation
from OT and IT in industrial organizations?

Given the historical nature of the separation of IT and OT,
organizations might still operate in silos. An indication of
converging maturity is how well those teams are working across
divisions or have even removed silos altogether. Meaningful
OT/IT convergence requires focused and organized effort, which
a CCoE can facilitate. A CCoE is a multi-disciplinary team of
passionate OT and IT subject matter experts (SMEs) who act as
change agents to accelerate IIoT adoption by standardizing and
evangelizing best practices, developing repeatable patterns to
scale implementation, driving governance, and providing
thought leadership. The CCoE can start small with 3-5 members,
cross-trained in both IT and OT aspects and can scale as
needed. For a CCoE to be successful, it requires executive
sponsorship and ability to act autonomously. The CCoE can
focus on making incremental improvements instead of a big-bang
approach. A prioritization framework is used to identify pilot
use cases starting with low-risk, high value, and low effort
use cases with measurable success metrics. After the pilot use
cases are deployed and business value demonstrated, this
activity continues cyclically to implement the pipeline of
prioritized use cases.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/organization.html*

---
