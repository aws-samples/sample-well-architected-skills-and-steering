# IOTPERF08 — Performance efficiency

**Pillar**: Performance Efficiency  
**Best Practices**: 2

---

## IOTPERF08-BP01 Load test your IoT applications

Applications can be complex and have multiple dependencies.
Testing the application under load helps identify problems
before going into production. Load testing your IoT applications
verifies that you understand the cloud-side performance
characteristics and failure modes of your IoT architecture.
Testing helps you understand how your application architecture
operates under load, identify performance bottlenecks, and apply
mitigating strategies prior to releasing changes to your
production systems.

**Prescriptive guidance
IOTPERF08-BP01-01**
*Simulate the real device
behavior.*

- A device simulator should implement the device behavior as
closely as possible. Test not only message publishing, but
also connections, reconnections, subscriptions, enrollment,
and other contextual events such as constrained network
bandwidth. Start testing at a lower load, and progressively
increase to 100%. Additionally, consider exercising the
workload beyond the traditional expected load by performing
stress tests.

Start the load test at a low percent of your estimated
total device fleet (for example, 10%).
- Evaluate the performance of your application using
operational dashboards created to measure end-to-end
delivery of device telemetry data and automated device
commands.
- Make any necessary changes to the application
architecture to achieve desired performance goals.
- Iterate these steps increasing the load until you get to
100%.
- For further workload development, consider performing
stress tests beyond usual load expected

### Resources

- [IoT
Device Simulator](https://aws.amazon.com/solutions/implementations/iot-device-simulator/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/process-and-culture.html*

---

## IOTPERF08-BP02 Monitor and manage your IoT service quotas using available tools and metrics

Be aware of the adjustable and unadjustable quotas of the AWS
service, and continuously monitor the key performance indicators
so that you can anticipate when actions must be taken to request
increases in the service quotas and re-evaluate your
architecture. Verify that your application operates within the
quotas of the services that you are building on to provide the
optimal performance to your users.

Monitoring keeps you aware of which service quotas you might be
reaching so that you can change your application to cope with
the unadjustable quotas or to request the increase of an
adjustable quota with sufficient lead time.

**Level of risk exposed if this best
practice is not established:** High

**Prescriptive guidance
IOTPERF08-BP02-01**
*Be aware of the service
quotas of the different IoT services.*

- Pay attention to which limits are adjustable quotas and
which are unadjustable quotas as they require different
approaches. For example:

An unadjustable *quota*, such a
control plane request rate, requires changes in the
application behavior to avoid the event repeating too
often. Workarounds for unadjustable quotas might require
different design decisions, such as using multiple
accounts. It's good to know the unadjustable and
adjustable quotas in advance so that you can make these
design decisions as early as possible in the development
process.
- *Adjustable quotas* should be
monitored to anticipate the need for additional capacity
and provide sufficient notice so that a request for a
limit increase can be made well ahead of time. For
example:

For AWS IoT Core, alert on `RulesMessageThrottles`,
`Connect.ClientIDThrottle`, `Connect.Throttle`,
`PublishIn.Throttle`, `Subscribe.Throttle`,
`Unsubscribe.Throttle`.
- For AWS IoT Device Management, monitor active
continuous jobs, and active snapshot jobs in Service Quotas

### Resources

- [AWS IoT Core endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/iot-core.html)
- [AWS IoT Device Defender endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/iot_device_defender.html)
- [AWS IoT Device Management endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/iot_device_management.html)
- [AWS IoT Greengrass V2 endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/greengrassv2.html)
- [AWS IoT SiteWise endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/iot-sitewise.html)

IOTPERF09: How do you maintain
visibility over the distributed infrastructure
deployed?

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/process-and-culture.html*

---
