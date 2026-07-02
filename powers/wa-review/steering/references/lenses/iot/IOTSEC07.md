# IOTSEC07 — Security

**Pillar**: Security  
**Best Practices**: 3

---

## IOTSEC07-BP01 Configure cloud infrastructure to have secure communications

Limit the communications paths and protocols used by the
solution to only those which are necessary for the applications.
For example, consider using only MQTT publish or subscribe
communications when communicating with IoT devices. In addition,
if possible, IoT devices should only connect out-bound to
trusted and verified and authenticated service endpoints and not
set up processes which listen for connections.

When it is necessary for IoT devices to listen for connection
requests, the sources of these connections should be strictly
limited. Any connecting client which is connecting to the device
must be authenticated before the device communicates with that
client. This applies whether or not the device itself is acting
as a proxy for clients which connect to it. Authentication
processing at the device is a device-specific design decision
and brings additional complications such as how to authenticate,
using what identity provider, and so on. This further supports
the recommendation for devices to avoid listening for connection
requests.

**Level of risk exposed if this best
practice is not established:** High

**Prescriptive guidance
IOTSEC07-BP01-01** *Use only MQTT
publish/subscribe in IoT devices when possible.*

Configure devices to use MQTT communications and use the IoT
Device Client or other MQTT client software to enable this
communication.

**Prescriptive guidance
IOTSEC07-BP01-02** *Design IoT devices and
solutions so that devices only connect and do not listen for
connections.*

Refrain from creating server-type applications running on IoT
devices. If necessary for handling local administration or
configuration types of activities, consider only enabling such
activities based on being placed into a maintenance mode and
then stopping these applications during normal operation.

**Prescriptive guidance
IOTSEC07-BP01-03** *When listening for
connections in IoT devices, authenticate connecting
clients.*

Require authentication by any connecting entity which connects
to the device. Be sure that there are no default credentials
(passwords, keys, or tokens) which could become compromised and
then used to access other devices. Authentication processing at
the device is a device-specific design decision and brings
additional complications such as how to authenticate, using what
identity provider, and so on. This further supports the
recommendation for devices to avoid listening for connection
requests. To enable local administration, initial installation
or provisioning should not rely on default credentials.

For example, local initial installation or provisioning on first
start or after factory reset may require a local administrator
to create a set of credentials or authenticate with a separate
identity provider.

**Prescriptive guidance
IOTSEC07-BP01-04** *For sizeable data
transfers like large file transfer, use encrypted HTTPS or SFTP
communications with an IoT device as the connecting client.*

Use TCP protocols which are set up for handling bulk or
large data transfers for performing those tasks. Connect from
the IoT device to the remote system in order to put to or pull
from files from that remote system. Verify the contents of those
files using digital signatures or file hashes retrieved through
a separate channel.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/infrastructure-protection.html*

---

## IOTSEC07-BP02 Define networking configuration which restricts communications to only those ports and protocols which are required

Restrict the possible communications protocols, paths, and ports
on which IoT devices can communicate. Also, configure network
communications so that there are separate network zones, with
only the allowed protocols, ports, and connection initiation
paths defined between these zones.

**Level of risk exposed if this best
practice is not established:** Medium

**Prescriptive guidance
IOTSEC07-BP02-01** *Use a minimum number of
protocols for device communication.*

If only MQTT communications is required, restrict communications
to only the IP port used for those communications. Consider
using a protocol-aware firewall to restrict traffic to only that
type of protocol. If HTTPS communications is also necessary,
enable only the two protocols/ports.

**Prescriptive guidance
IOTSEC07-BP02-02** *Configure network zones
which have strict protection for inbound/outbound communications
and connection initiation.*

Configure network zoning using virtual or physical network
connections. Use virtual network connection configuration to
restrict connection initiation direction., Allow only outbound
connections from IoT devices and restrict inbound
connections from outside the local network.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/infrastructure-protection.html*

---

## IOTSEC07-BP03 Log and monitor network configuration changes and network communication

The ability to monitor and log communications assists in
verifying that only the expected communications is taking place
in the infrastructure. Also, having network logs allows for
forensic analysis and problem determination if and when a
problem is suspected or identified.

**Level of risk exposed if this best
practice is not established:** Low

**Prescriptive guidance
IOTSEC07-BP03-01** *Set up network logging at
network zone connection points*

Use network routers or switches and firewalls between network
zones. Set up network logging on those devices and appliances.

**Prescriptive guidance
IOTSEC07-BP03-02** *Send logs to a centralized
logging infrastructure to enable remote problem determination
and forensic analysis.*

Centralize logs to offload the logs from the remote devices and
appliances. This also allows for network communications analysis
across the overall solution in addition to looking at individual
network zone activity. Centralized logging solutions are
available on AWS. For example,
[Amazon OpenSearch Service Centralized Logging with OpenSearch](https://aws.amazon.com/solutions/implementations/centralized-logging-with-opensearch/) is a
centralized log management solution. Also,
[Amazon
Security Lake](https://aws.amazon.com/security-lake/) can be used to understand, review, and act
on security-related events in your computing environment.

IOTSEC08: How is the infrastructure into
which your IoT devices are deployed managed and
maintained?

After initial installation and configuration of an IoT solution,
including the IoT devices, the solution components, networking
configuration, and IoT devices themselves will still require
ongoing maintenance and management. IoT devices should have a
defined method for managing and maintaining their firmware,
software, and configuration. This also includes maintaining or
updating the identity of the devices, Also, the devices must be
able to authenticate on connection start up as well as verify
the identity of the endpoints which they connect to and
communicate with.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/infrastructure-protection.html*

---
