# IOTSEC13 — Security

**Pillar**: Security  
**Best Practices**: 3

---

## IOTSEC13-BP01 Use code and package scanning tools during development to identify potential risks during development

Vulnerability scanning enables teams to identify potential
issues in device firmware and application. Updates to remediate
the risks may require code changes, package version changes, or
operating system version updates. Known vulnerability databases
are updated regularly. New risks may be discovered in existing
firmware and software even when that software has not changed.

**Level of risk exposed if this best
practice is not established:** Medium

**Prescriptive guidance
IOTSEC13-BP01-01** *Scan code and packages
during every build of the application.*

Perform vulnerability scanning on every build and package of the
application. This will provide an early check in the deployment
lifecycle so that these findings can be addressed before the
application code is deployed into any active environments.

**Prescriptive guidance
IOTSEC13-BP01-02** *Update depended-upon
package versions regularly to pick up fixes for known issues
that have been identified.*

Most software now depends on many open-source or third-party
packages. Issues, risks, and bugs may be discovered in these
packages. Any updates to these packages must then be applied to
the applications which are using those packages and the updated
applications then deployed to devices where that code is used.
Plan to regularly re-build, package, and deploy updates to
applications even if no additional features of application
source code updates have been added.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/vulnerability-management.html*

---

## IOTSEC13-BP02 Deploy updates to IoT device firmware or software to address identified issues

Use deployment automation to deploy updates which contain fixes
for issues which have been discovered and identified. The same
automation which is used to deploy firmware or application
updates should be used to deploy updates for remediating risks.

**Level of risk exposed if this best
practice is not established:** High

**Prescriptive guidance
IOTSEC13-BP02-01** *Use an automated,
controlled, and staged roll-out of updates to firmware or
software.*

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

**Prescriptive guidance
IOTSEC13-BP02-02** *Implement a mechanism for
canceling a roll-out and rolling back an update which has been
found to contain issues.*

The deployment automation mechanism should include a method for
canceling or rolling back a set of updates which have been
scheduled to be deployed to a set of devices. Deployment
automation tools provide information on the progress of
deployments for those responsible for the roll-outs to monitor
and take appropriate action if necessary. Consider using
services such as
[AWS IoT Greengrass](https://aws.amazon.com/greengrass/) deployments,

[IoT
Fleet Management](https://aws.amazon.com/solutions/iot/fleet-management/), and

[AWS IoT Core](https://aws.amazon.com/iot-core/) Jobs for automating deployments of updated IoT
application code.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/vulnerability-management.html*

---

## IOTSEC13-BP03 Identify IoT devices which require updates and schedule updates to those devices

An accurate device inventory is needed in order to determine
which IoT devices may be affected by a issue or risk which has
been identified. Once a fix is available for the identified
risk, the identified devices can be targeted to be updated.

**Level of risk exposed if this best
practice is not established:** Medium

**Prescriptive guidance
IOTSEC13-BP03-01** *Use an accurate device
inventory which includes firmware or software version
information to help identify IoT devices which require
updates.*

Maintain an accurate inventory of IoT devices and the SBOM for
firmware and applications deployed to those devices. Use the
inventory to understand which devices are affected by issues
which are identified in the firmware of packages in the SBOM.
This enables targeted updates to be deployed to those devices
which are found to contain the issue.

**Prescriptive guidance
IOTSEC13-BP03-02** *Consider implementing
on-device endpoint detection and response (EDR) technologies to
identify risks and request updates to the device firmware or
software.*

For device operating systems which enable endpoint detection and
response (EDR) technologies, consider using endpoint-based
detection in order to identify vulnerabilities in those devices.
Be sure to stage the roll-out of updates to devices so that if
issues are found with an update the roll-out can be cancelled or
rolled back.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/vulnerability-management.html*

---
