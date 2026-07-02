# IOTSEC14 — Security

**Pillar**: Security  
**Best Practices**: 3

---

## IOTSEC14-BP01 Establish a security governance team for your IoT applications or extend the security governance team for the organization

A security governance team will evaluate IoT applications
against a risk management framework. By establishing the
potential risks that each IoT application poses, teams can then
identify mitigations for those risks and update or remediate IoT
applications appropriately. Security governance applies to
people, processes, and tools used by the organization to
establish, evaluate, and update the security posture of
applications.

**Level of risk exposed if this best
practice is not established:** Low

**Prescriptive guidance
IOTSEC14-BP01-01** *Coordinate activities
between security governance teams.*

If there are multiple security governance teams throughout the
organization, coordinate the activities across these teams so
that decisions made by one team are consistent and carried out
by other parts of the organization which might be affected by
those decisions.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/security-governance.html*

---

## IOTSEC14-BP02 Define security policy so that it can be written into verifiable checks using policy as code techniques

Security policies for an organization generally begin from
existing standards such as
[NIST
800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final),

[ISO/IEC
27001](https://www.iso.org/isoiec-27001-information-security.html),

[ISA/IEC
62443](https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards), and

[CIS](https://www.cisecurity.org/). Using
the controls identified in those standards along with the
specific architecture and implementation of applications,
verifiable checks of the configuration of the application can be
created which result in the controls being expressed in code.
These codified checks can then be automated so that compliance
can be evaluated on a repeated and ongoing basis. Reports
provide feedback on the compliance status of applications and
logs of the automated checks provide evidence of ongoing
evaluation of the environment.

**Level of risk exposed if this best
practice is not established:** Medium

**Prescriptive guidance
IOTSEC14-BP02-01** *Codify security policy
into verifiable checks.*

Use tools such as
[AWS Config](https://aws.amazon.com/config/) and the rules development kit (RDK) to codify
security policies into verifiable checks. Additional services
including
[AWS Security Hub CSPM](https://aws.amazon.com/security-hub/),

[AWS IoT Device Defender](https://aws.amazon.com/iot-device-defender/), and

[Amazon
Security Lake](https://aws.amazon.com/security-lake/) help to log compliance checks and provide
reports on the compliance status of applications.

**Prescriptive guidance
IOTSEC14-BP02-02** *Implement security policy
checks as part of the develop, build, test, and deploy workflow
and automation.*

Security policy checks can also be implemented through source
code scanning as well as policy checking during deployment
processing. Use build automation and code scanning tools to
check for security configuration and report findings into
services such as
[Amazon
Security Lake](https://aws.amazon.com/security-lake/). Use

[AWS CloudFormation Hooks](https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/what-is-cloudformation-hooks.html), a feature of

[AWS CloudFormation](https://aws.amazon.com/cloudformation/), to add compliance checks into the
deployment processing of applications to check for and report
issues with the configuration of infrastructure which supports
applications.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/security-governance.html*

---

## IOTSEC14-BP03 Implement a risk assessment and risk management process

A risk management process includes procedures for identify,
assess, and monitor risks as well as implementing mitigations
for those risks. The
[NIST
Risk Management Framework](https://csrc.nist.gov/Projects/risk-management) provides an example process
which can be worked from if your organization does not already
have a process to follow. If your organization has an existing
risk management process, evaluate the process for any potential
adjustments which are specific to IoT applications. Consider the
environmental and human safety risks that may be applicable in
IoT application environments.

**Level of risk exposed if this best
practice is not established:** Low

**Prescriptive guidance
IOTSEC14-BP03-01** *Integrate risk assessment
and risk management with other problem management tools that are
used by the development and operations teams.*

Any work items or tasks which are generated from risk assessment
and risk management activities as well as findings from
automated compliance scanning performed during development,
build, and deployment of applications should be reflected back
into the problem management tools used by the application and
infrastructure development teams. Depending on the tools used to
perform compliance checks, this integration can be built into
the environment by using services such as
[Amazon EventBridge](https://aws.amazon.com/eventbridge/) coupled with

[Amazon Simple Queue Service (SQS)](https://aws.amazon.com/pm/sqs/) and

[AWS Lambda](https://aws.amazon.com/pm/lambda/).

**Prescriptive guidance
IOTSEC14-BP03-02** *Identify what
environmental and human safety concerns are applicable to the
IoT application.*

IoT applications often have direct interaction with humans
and the environment. Pay particular attention to the risks
related to environmental and human safety caused by the
decisions, processing and actions taken by the IoT application.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/security-governance.html*

---
