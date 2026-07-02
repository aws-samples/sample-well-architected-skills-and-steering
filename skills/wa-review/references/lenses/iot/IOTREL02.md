# IOTREL02 — Reliability

**Pillar**: Reliability  
**Best Practices**: 1

---

## IOTREL02-BP01 Manage service quotas and constraints

For cloud-based workload architectures, there are service quotas (which are also referred to as service limits). These quotas exist to help prevent accidentally provisioning more resources than you need and to limit request rates on API operations so as to protect services from abuse.

**Level of risk exposed if this best
practice is not established:** High

**Prescriptive guidance
IOTREL02-BP01-01** *Follow the Reliability
Foundations Best Practices defined in the AWS Well-Architected
Framework.*

The most important part of your IoT scaling approach is to make sure that you architect around any hard limits because exceeding limits that are not adjustable results in application errors, such as throttling and client errors. Hard limits are related to throughput on a single IoT connection. Consider restructuring your MQTT topics, or implementing cloud-side logic to aggregate or filter messages before delivering the messages to the interested devices.

Soft limits in AWS IoT traditionally correlate to account-level limits that are independent of a single device. For any account-level limits, you should calculate your IoT usage for a single device and then multiply that usage by the number of devices to determine the base IoT limits that your application will require for your initial product launch. AWS recommends that you have a ramp-up period where your limit increases align closely to your current production peak usage with an additional buffer. To make sure that the IoT application is not under provisioned:

- Consult published AWS IoT CloudWatch metrics for all limits:
[AWS IoT metrics and dimensions](https://docs.aws.amazon.com/iot/latest/developerguide/metrics_dimensions.html)
- Monitor CloudWatch metrics in AWS IoT Core:
[Logging
and Monitoring](https://docs.aws.amazon.com/iot/latest/developerguide/security-logging.html)
- Alert on CloudWatch throttle metrics, which would signal if
you need a limit increase.
- Set alarms for all thresholds in IoT, including MQTT
connect, publish, subscribe, receive, and rule engine
actions.
- Monitoring AWS IoT MQTT Traffic and Automating Quota and
Throttling Notifications
- [Monitoring
your IoT Fleet using CloudWatch](https://aws.amazon.com/blogs/iot/monitoring-your-iot-fleet-using-cloudwatch/)
- Make sure that you request a limit increase in a timely
fashion, before reaching 100% capacity. See the AWS
documentation on Requesting a quota increase:
[Requesting
a quota increase](https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html)

In addition to data plane limits, the AWS IoT service has a
control plane for administrative APIs. The control plane manages
the process of creating and storing IoT policies and principals,
creating the thing in the registry, and associating IoT
principals including certificates and Amazon Cognito federated
identities. Because bootstrapping and device registration is
critical to the overall process, it's important to plan control
plane operations and limits. Control plane API calls are based
on throughput measured in requests per second. Control plane
calls are normally in the order of magnitude of tens of requests
per second. It is important for you to work backward from peak
expected registration usage to determine if any limit increases
for control plane operations are needed. Plan for sustained
ramp-up periods for onboarding devices so that the IoT limit
increases align with regular day-to-day data plane usage.

To protect against a burst in control plane requests, your
architecture should limit the access to these APIs to only
authorized users or internal applications. Implement back-off
and retry logic, and queue inbound requests to control data
rates to these APIs.

IOTREL03: How do you design workloads to
operate efficiently within network bandwidth and storage
constraints?

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/foundations.html*

---
