# IOTSEC12 — Security

**Pillar**: Security  
**Best Practices**: 3

---

## IOTSEC12-BP01 Manage IoT device and gateway source code using source code management tools

All source code which implements applications in devices and
gateways should be maintained in a version management system.
Version management enables an orderly progression of changes to
source code along with the ability to understand what updates to
code were made when, by whom, and for what reasons. Version
management also enables parallel feature development as well as
a path for backing out or reverting changes that are found to be
incorrect or unwanted.

**Level of risk exposed if this best
practice is not established:** High

**Prescriptive guidance
IOTSEC12-BP01-01** *Use a code management tool
for managing source code.*

Many code management tools are available for use. Choose a tool
which allows for your team to collaborate on application source
code development, build, deployment, and testing.

**Prescriptive guidance
IOTSEC12-BP01-02** *Use a problem management
tool for prioritizing updates and changes made to source
code.*

Many problems and ticket management tools are available for use.
Choose a tool which allows for your team to collaborate in
problems, bugs or tickets as well as features to be developed.
The problem management tool should enable linking between
application source code updates and the problems or features
which document the reasons for making the source code updates.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/application-security.html*

---

## IOTSEC12-BP02 Use static code analysis tools and code scanning to check IoT application code

Source code scanning enables teams to identify potential issues
in application code long before any build, deployment, and
testing is performed. This can greatly reduce the time and
effort needed to identify problems. Fixing issues earlier in the
development or deployment cycle is generally much more efficient
and cost-effective than fixing problems which are found in
already-deployed software.

**Level of risk exposed if this best
practice is not established:** Low

**Prescriptive guidance
IOTSEC12-BP02-01** *Configure code scanning to
run in multiple points during the development
workflow.*

Source code scanning should be performed at multiple points in
the development workflow. Code scans using workstation-based or
integrated development environment (IDE) based plug-ins help
developers identify and fix findings as they are writing the
code. Code scans run before commit to version management provide
another opportunity to identify issues early. Code scans run on
workstations are typically optional or under the control of a
developer for their configuration. Code scans run on code as it
is pushed to central repositories and also when code is being
built or prepared for deployment is a means of scanning code
which has been merged from several developers' separate updates.
Periodic code scanning as background processing jobs allows for
scanning source code even when updates to that code have not
been submitted. Periodic scanning helps find latent issues which
might have been discovered since the code was developed or find
issues which have been recently added as items to be checked or
updated in source code.

**Prescriptive guidance
IOTSEC12-BP02-02** *Feed the results of code
scanning tools to problem management systems.*

Provide feedback to the owners of the source code in the most
appropriate format for them to be able to take action. If
running in IDEs, provide feedback within the IDE. If code
scanning is run in build automation, provide feedback in build
logs as well as by using notification mechanisms to the
developers responsible for that code. This may include creating
problem reports or tickets in problem management systems and
assigning them to the appropriate owner to resolve.

**Prescriptive guidance
IOTSEC12-BP02-03** *Establish a process for
fixing issues identified from code scans.*

Once problems are identified, use the preferred problem
management and backlog management tools for the team to
prioritize and work on fixes that are indicated by the issues
found. Backlog refinement should take care to not always
de-prioritize fixing security-related code scan findings. Use an
aging factor for security-related findings which boosts the
priority of fixing the finding over time.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/application-security.html*

---

## IOTSEC12-BP03 Deploy IoT applications using IaC, CI/CD pipelines, and build and deploy automation

Application security problems often arise from faulty or
inconsistent deployment when humans are responsible for some set
of the steps required to perform the build, test, and deployment
of the application. By using build, test, deploy, and
staged-roll-out mechanisms, human involvement can be used for
verification and approval processing, with the specific steps
required to deploy the application codified into automation
scripts and processing. These processing steps can be logged and
monitored.

**Level of risk exposed if this best
practice is not established:** Medium

**Prescriptive guidance
IOTSEC12-BP03-01** *Use build automation
pipelines to build, test, and stage updates for
deployment.*

Build automation tools allow human involvement to be focused on
verification and approval processing, with the specific steps
required to deploy the application codified into automation
scripts and processing. Consider using services such as
[AWS CodePipeline](https://aws.amazon.com/codepipeline/) and
[AWS CodeDeploy](https://aws.amazon.com/codedeploy/) for automating build, test, and staging of
updates for deployment.

**Prescriptive guidance
IOTSEC12-BP03-**02 *Use deployment automation
to deploy updated to IoT application code*

Deployment automation tools enable a staged roll-out of updates
to large fleets of devices. By rolling out in stages, issues
found in rolling out the updated application can be limited in
scope. Deployment automation tools provide information on the
progress of deployments for those responsible for the roll-outs
to monitor and take appropriate action if necessary. Consider
using services such as
[AWS IoT Greengrass](https://aws.amazon.com/greengrass/) deployments,

[IoT
Fleet Management](https://aws.amazon.com/solutions/iot/fleet-management/), and

[AWS IoT Core](https://aws.amazon.com/iot-core/) Jobs for automating deployments of updated IoT
application code.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/application-security.html*

---
