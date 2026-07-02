# IOTOPS04 — Operational excellence

**Pillar**: Operational Excellence  
**Best Practices**: 1

---

## IOTOPS04-BP01 The device management processes should be automated, data-driven, and based on previous, current, and expected device behavior

**Level of risk exposed if this best
practice is not established:** High

**Prescriptive guidance
IOTOPS04-BP01-01** *Defining how devices are
provisioned must include how the devices are manufactured and
how they are registered for both greenfield and brownfield fleet
of devices.*

- In AWS IoT, you can use multiple features to provision your
individual device identities signed by your CA to the cloud.
This path involves provisioning devices with identities and
then using just-in-time-provisioning (JITP),
just-in-time-registration (JITR), fleet provisioning or
Multi-Account Registration to securely register your device
certificates to the cloud. Using AWS services including
Route 53, Amazon API Gateway, Lambda, and DynamoDB, will
create a simple API interface to extend the provisioning
process with device bootstrapping.
- IoT applications must support incremental rollout and
rollback strategies. By having this as part of the
operational efficiency plan, you will be equipped to launch
a fault-tolerant, efficient IoT application.

### Resources

- [Device
Manufacturing and Provisioning with X.509 Certificates in AWS IoT Core](https://docs.aws.amazon.com/pdfs/whitepapers/latest/device-manufacturing-provisioning/device-manufacturing-provisioning.pdf#device-manufacturing-provisioning)
- [How
to automate onboarding of IoT devices to AWS IoT Core at scale with Fleet Provisioning](https://aws.amazon.com/blogs/iot/how-to-automate-onboarding-of-iot-devices-to-aws-iot-core-at-scale-with-fleet-provisioning/)

IOTOPS05: How do you govern device fleet
provisioning process?

IoT solutions can scale to millions of devices and this requires
device fleets to be well planned from the perspectives of
provisioning processes and metadata organization. Maintain a
full chain of security controls over who or what processes can
trigger device provisioning to decrease the likelihood of
inviting unintended (or rogue) devices into your fleet.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/prepare.html*

---
