# IOTREL01 — Reliability

**Pillar**: Reliability  
**Best Practices**: 2

---

## IOTREL01-BP01 Use NTP to maintain time synchronization on devices

IoT devices need to have a client to keep track of time—either
using Real Time Clock (RTC) or Network Time Protocol (NTP) to
set the RTC on boot. Failure to provide accurate time to an IoT
device could help prevent it from being able to connect to the
cloud.

**Level of risk exposed if this best
practice is not established:** Medium

**Prescriptive guidance
IOTREL01-BP01-01** *Prefer NTP to RTC when NTP
synchronization is available.*

Many computers have an RTC peripheral that helps in keeping
time. Consider that RTC is prone to clock drift of about 1
second a day, which can result in the device going offline
because of certificate invalidity.

**Prescriptive guidance
IOTREL01-BP01-02** *Use Network Time Protocol
for connected applications.*

- Select a safe, reliable NTP pool to use, and a one that
addresses your security design
- Many operating systems include an NTP client to sync with an
NTP server
- If the IoT device is using GNU/Linux, it is likely to
include the NTPD daemon
- You can import an NTP client to your system if using
FreeRTOS
- The device's software needs to include an NTP client and
should wait until it has synchronized with an NTP server
before attempting a connection with AWS IoT Core
- The system should provide a way for a user to set the
device's time so that subsequent connections can succeed
- Use NTP to synchronize RTC on the device to help prevent the
device from deviating from UTC
- Consider the following
[The
NTP Pool for vendors](https://www.pool.ntp.org/en/vendors.html)
- [Chrony](https://chrony.tuxfamily.org/)
is a different implementation of NTP than what NTPD uses and
it is able to synchronize the system clock faster and with
better accuracy than NTPD. Chrony can be set up as a client
and server.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/foundations.html*

---

## IOTREL01-BP02 Provide devices access to NTP servers

An NTP server should be available for clients to use for local
time. NTP servers are required by NTP clients to synchronize
device time and function properly.

**Level of risk exposed if this best
practice is not established:** Low

**Prescriptive guidance
IOTREL01-BP02-01** *Provide access to NTP
services.*

- ntp.org can be used to synchronize your computer clocks.

- [Amazon
Time Sync Service](https://aws.amazon.com/about-aws/whats-new/2017/11/introducing-the-amazon-time-sync-service/): a time synchronization service
delivered over NTP, which uses a fleet of redundant
satellite-connected and atomic clocks in each Region to
deliver a highly accurate reference clock. This is natively
accessible from Amazon EC2 instances and this can be pushed
to edge devices.
- [Chrony](https://chrony.tuxfamily.org/)
is a different implementation of NTP than what NTPD uses and
it is able to synchronize the system clock faster and with
better accuracy than NTPD. Chrony can be set up as a server
and client.

IOTREL02: How do you manage service
quotas and limits for peaks in your IoT workload?

AWS IoT provides a set of soft and hard limits for different
dimensions of usage. AWS IoT outlines the data plane limits on
the IoT limits, see
[AWS service quotas](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html#limits_iot). Data plane operations (for example, MQTT
Connect, MQTT Publish, and MQTT Subscribe) are the primary
driver of your device connectivity. Therefore, it's important to
review the IoT limits and make sure that your application
adheres to any soft limits related to the data plane, while not
exceeding any hard limits that are imposed by the data plane.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/foundations.html*

---
