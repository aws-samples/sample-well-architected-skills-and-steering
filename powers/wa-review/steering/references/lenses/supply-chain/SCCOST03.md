# SCCOST03 — Automate and streamline operations

**Pillar**: Cost Optimization  
**Best Practices**: 3

---

# SCCOST03-BP01 Compress and aggregate data whenever possible to reduce the amount of data that needs to be transmitted over the network

Maximizing processing and sanitation of data reduces the
amount of data to be sent and processed in the cloud, leading to
significant cost savings and improved performance.

**Desired outcome:** A well-defined
strategy on where data gets processed and transmitted to reduce
unnecessary load on the network and cloud

**Benefits of establishing this best
practice:** Reduced cost, optimized performance, and
better customer satisfaction

**Level of risk exposed if this best
practice is not established:** Medium

## Implementation guidance

Maximize processing and sanitation of the data in-situ, to
reduce the amount of data to be sent and processed in the cloud.
AWS IoT Greengrass v2 can help with processing and summarization
of data at the edge, while implementing data filtering and
aggregation at the edge using AWS IoT Core rules engine or AWS IoT Greengrass v2 components to send only relevant, summarized
data to the cloud.

### Implementation steps

- Identify data processing opportunities at the edge to
reduce the volume of data transmitted to the cloud.
- Deploy AWS IoT Greengrass v2 for local data processing,
filtering, and aggregation at manufacturing facilities.
- Implement data compression techniques and Combine multiple
measurements into single messages to reduce transmission
costs.
- Configure AWS IoT Core rules engine to filter and route
only relevant data to cloud storage and processing
systems.
- Establish data summarization processes that aggregate
detailed operational data into meaningful insights before
cloud transmission.
- Monitor network usage and data transmission costs to
continuously optimize edge processing strategies.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/supply-chain-lens/sccost03-bp01.html*

---

# SCCOST03-BP02 Adjust collection frequency depending on the context

Optimize data collection frequency based on business needs and
context using event-based triggers and thresholds to reduce costs
while maintaining performance and efficiency.

**Desired outcome:** A well-defined
collection strategy which meets the business and functional
requirements.

**Benefits of establishing this best
practice:** Reduced cost, optimized performance, and
better customer satisfaction

**Level of risk exposed if this best
practice is not established:** Medium

## Implementation guidance

Optimize data collection frequency based on functional and
business needs to minimize unnecessary transmission and improve
efficiency in supply chain systems.

Implement event-based or context-dependent collection schemes
using tools like AWS IoT Greengrass components to dynamically
adapt data gathering, while defining threshold values and
triggers for specific events or parameters to determine when to
adjust collection frequency.

### Implementation steps

- Analyze business requirements to determine optimal data
collection frequencies for different types of supply chain
data.
- Implement event-based data collection that triggers only
when significant changes or thresholds are reached.
- Configure dynamic collection frequency adjustment based on
operational context and business priorities.
- Deploy AWS IoT Greengrass components to enable
intelligent, context-aware data collection at edge
locations.
- Establish threshold-based triggers that automatically
adjust collection frequency based on operational
conditions.
- Monitor data collection costs and effectiveness to
continuously optimize collection strategies.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/supply-chain-lens/sccost03-bp02.html*

---

# SCCOST03-BP03 Choose the right communication service and configuration depending on the use case

Tailor your communication service selection and setup to match
specific supply chain scenarios and requirements.

**Desired outcome:** A well-defined
formatting/transmission strategy which meets the functional
requirements of downstream applications and the entire SCM
environment.

**Benefits of establishing this best
practice:** Reduced cost, optimized performance, and
better customer satisfaction

**Level of risk exposed if this best
practice is not established:** High

## Implementation guidance

Use AWS B2B Data Interchange to automatically convert Electronic
Data Interchange (EDI) documents into JSON and XML formats, while
utilizing MQTT 5 protocol for lightweight communication between
sensors and AWS IoT Core. Implement AWS IoT Core device shadow to
store and synchronize device states, reducing the need for
constant communication, and employ caching mechanisms to store
frequently accessed data locally.

### Implementation steps

- Assess communication requirements for different supply chain
use cases and select appropriate protocols and services.
- Implement AWS B2B Data Interchange for efficient EDI
document processing and format conversion.
- Deploy MQTT 5 protocol for lightweight, efficient
communication between IoT devices and cloud services.
- Configure AWS IoT Core device shadow for state
synchronization and reduced communication overhead.
- Implement local caching mechanisms to minimize cloud
requests and reduce bandwidth consumption.
- Optimize Quality of Service (QoS) levels and routing paths
to balance reliability with cost efficiency.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/supply-chain-lens/sccost03-bp03.html*

---
