# IOTOPS03 — Operational excellence

**Pillar**: Operational Excellence  
**Best Practices**: 2

---

## IOTOPS03-BP01 Use static and dynamic device hierarchies to support fleet operations

Using a software registry, devices can be categorized into
static groups based on their fixed attributes (such as version
or manufacturer) and into dynamic groups based on their
changing attributes (such as battery percentage or firmware
version). Operationalizing devices in groups can help you
manage, control, and search for devices more efficiently.

**Level of risk exposed if this best
practice is not established:** High

**Prescriptive guidance
IOTOPS03-BP01-01** *Manage several devices at
once by categorizing them into static groups and hierarchy of
groups.*

- Build a hierarchy of static groups for efficient
categorization and indexing of your devices.
- Use provisioning templates to assign devices to static
groups as they are provisioned for the first time.
- For example, categorize all sensors of a car under a car
group and all the cars under a vehicle group. Child groups
inherit policies and permissions attached to their
respective parent groups.

**Prescriptive guidance
IOTOPS03-BP01-02** *Build a device index to
efficiently search for devices, and aggregate registry data,
runtime data, and device connectivity data.*

- Use a fleet indexing service from AWS IoT Core to index
device and group data.
- Use a device index to search registry metadata, stateful
metadata, and device connectivity status metadata.
- Use a group index to search for groups based on group name,
description, attributes, and all parent group names.
- For example, if you want to send over-the-air (OTA) updates
only to devices that are sufficiently charged, then define a
dynamic group for devices with more than 90% battery.
Devices will dynamically be added to or removed from the
group as their battery percentage crosses the threshold.
Send OTA updates to all things under this dynamic group

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/prepare.html*

---

## IOTOPS03-BP02 Use index and search services to enable rapid identification of target devices

A large IoT deployment can have millions of sensors sending
data to the cloud. A separate indexing and search service can
make it straightforward to index and organize the device data,
and search for devices by attributes. Ingesting device data to
a search service, for example, Amazon OpenSearch Service, makes it straightforward to use powerful
search, visualization, and analytics capabilities of OpenSearch Service
to organize and search for devices. You can ingest your device
data and the state to OpenSearch Service seamlessly.

**Level of risk exposed if this best
practice is not established:** Medium

**Prescriptive guidance
IOTOPS03-BP02-01** *Use an indexed data store to
get, update, or delete device state.*

- Use messaging topics to enable applications and things to
get, update, or delete the state information for a Thing
(Thing Shadow).
- Ingest the shadow data to Firehose through the
AWS IoT Core rules engine.
- Ingest the data from Firehose to Amazon OpenSearch Service through built-in
destination options for OpenSearch Service.
- Configure search and visualizations on the data directly or
through the OpenSearch Dashboards console.
- In AWS, you can create an AWS IoT thing for each physical
device in the device registry of AWS IoT Core. By creating a
thing in the registry, you can associate metadata to
devices, group devices, and configure security permissions
for devices. An AWS IoT thing should be used to store static
data in the thing registry while storing dynamic device data
in the thing's associated device shadow. A device's shadow
is a JSON document that is used to store and retrieve state
information for a device.

### Resources

- [AWS IoT Core - Fleet indexing serviceAWS IoT Core - Fleet
indexing](https://docs.aws.amazon.com/iot/latest/developerguide/iot-indexing.html)
- [AWS IoT Core - AWS IoT Device Shadow service](https://docs.aws.amazon.com/iot/latest/developerguide/iot-device-shadows.html)
- [Amazon OpenSearch Service](https://aws.amazon.com/opensearch-service/)
- [The
Internet of Things on AWS – Official Blog: Archive AWS IoT Device Shadow services in Amazon OpenSearch Service](https://aws.amazon.com/blogs/iot/archive-aws-iot-device-shadows-in-amazon-elasticsearch-service/)
- [Analyze
device-generated data with AWS IoT and Amazon OpenSearch Service](https://aws.amazon.com/blogs/mobile/analyze-device-generated-data-with-aws-iot-and-amazon-elasticsearch-service/)

IOTOPS04: How do you verify that newly
provisioned devices have the required operational prerequisites?

Logical security for IoT and data centers is similar in that
both involve predominantly machine-to-machine authentication.
However, they differ in that IoT devices are frequently
deployed to environments that cannot be assumed to be
physically secure. IoT applications also commonly require
sensitive data to traverse the internet. Due to these
considerations, it is vital for you to have an architecture
that determines how devices will securely gain an identity,
continuously prove their identity, be seeded with the
appropriate level of metadata, be organized and categorized
for monitoring, and enabled with the right set of permissions.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/prepare.html*

---
