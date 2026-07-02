# Cost optimization

**Pages**: 8

---

# Design principles

In addition to the general Well-Architected cost optimization design principles, there are some design principles specific for cost optimization for connected mobility:

**Manage cost and business value tradeoffs:** Managing tradeoffs
between cost and other factors in connected mobility requires a careful balance between
short-term costs, such as installation, setup and subscription fees, and long-term costs, such
as data storage, management and infrastructure upgrades cost, cost-benefit analysis, and risk
management. For example, if you want to optimize for speed to market with low cost?

Choosing a solution solely based on cost without considering its business value can result
in increased operational cost overtime. Factors such as functionality, scalability, security,
speed of innovation, and going to market should be carefully evaluated along with cost to
select the right services/solutions. For example, a logistics company wants to implement a
connected mobility solution to track packages and optimize delivery routes. Implementing a
flexible architecture that can scale to accommodate growth and demand may come with an
increased short-term cost, however, it also comes with an increased business value creation
which will result in cost savings in long-term.

**Design the system to filter relevant data:** Connected mobility
applications could generate 10 exabytes of data per month. That's why it is important to
identify the data to be collected throughout your vehicle's fleets based on the corresponding
business use-case or security/compliance requirements. Identify opportunities to stop
collecting unnecessary data and consider collecting data targeted on business case and moving
to event-based collection instead of interval whenever possible.

**Evaluate where to process data:** Data transfer between vehicle
and cloud backend incur cost. Evaluation based on the use case through several
dimensions:

- The network cost private or public may have different cost implications. In the
context of connected vehicles, a private network refers to a dedicated and secure
communication network established specifically for the vehicles and related systems within
a closed environment. This network is isolated from public networks and is designed to
provide a controlled and reliable communication infrastructure for connected vehicle
operations.
For example, imagine a fleet of autonomous delivery vehicles operated by a logistics
company. To ensure seamless and secure communication between these vehicles, as well as
with the central control system, the company sets up a private network. This network could
consist of dedicated cellular connections, Wi-Fi hotspots, or even a custom-built
communication infrastructure.
- The latency requirements to process the data. Latency refers to the delay between
when data is generated or transmitted and when it is received and processed by the
relevant systems. Here are two examples of latency requirements for processing data in
connected vehicles:

**Emergency collision avoidance:**

Data source: Sensors on a vehicle detect an imminent collision with another vehicle.

Processing needs: The data from these sensors must be processed immediately to assess
the risk and decide on an appropriate action (for example, applying brakes, or changing
lanes).

Latency tolerance: In this scenario, extremely low latency is critical. A delay of
even a few milliseconds could be the difference between a successful collision avoidance and
an accident.

**Traffic signal optimization:**

Data source: The connected vehicle is equipped with technology to communicate with
traffic signals in real-time.

Processing needs: The vehicle's system sends data to the traffic signal control
system to request a green light or to adjust the signal timing for optimal traffic flow.

Latency tolerance: While not as critical as collision avoidance, low latency is still
important. Delays should be minimized to ensure smooth traffic flow and reduce unnecessary
stops.

In both cases, low latency is essential for the effective
operation of connected vehicle systems. It allows for timely
decision-making and actions, enhancing safety and efficiency
on the road.

- The compute capacity requirements where processing the data makes more sense, at edge
in the vehicle or in the AWS Cloud. In this scenario, edge processing (in-vehicle) is
critical for immediate decision-making and ensuring passenger safety. It allows each
vehicle to operate autonomously, reacting swiftly to its environment.

On the other hand, cloud processing is beneficial for
higher-level, aggregate analysis. It can be used to optimize
routes across the entire fleet, predict traffic patterns, and
perform long-term planning. Overall, a combination of edge and
cloud processing can offer the best of both worlds, allowing
for real-time decision-making at the vehicle level while also
leveraging the cloud's computational power for broader fleet
optimization and analytics.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/connected-mobility-lens/design-principles-cost.html*

---

# Cost-effective resources

CMCOST_1: How do you optimize your raw vehicle data storage?

Managing raw vehicle data is important because it allows
organizations to leverage the data to drive innovation,
improve their business processes and is the original source of
analytics. Vehicle data can provide valuable insights into
driving patterns, vehicle performance, and other areas that
can be used to optimize operations, improve safety, and
enhance the customer experience, however the amount of data
generated can also be a big driver for cost. Vehicular data is
a key source of information that can be used to drive
automotive transformation, but it can be a challenge to manage
due to the volume, velocity, and variety of the data. By
effectively managing the raw vehicular data, organizations can
unlock the value of the data and use it to drive innovation
and improve business processes.

**[CMCOST_BP1.1] Store raw data in a scalable and cost-effective
way**

Efficient data storage can help you avoid high costs
associated with storing large amounts of data. Object storage
is recommended for large amounts of unstructured data,
especially when durability, unlimited storage, scalability,
and complex metadata management are relevant factors for
overall performance.

Use object storage and evaluate the appropriate storage classes.

Raw vehicle data typically includes large volumes of data that
require different levels of access speed and frequency. To
optimize storage costs, you can use appropriate storage
classes based on the access speed and frequency of the data.
For example, you can use Amazon S3 Standard for frequently
accessed data and Amazon Glacier for archived data.
[Amazon S3 Intelligent-Tiering](https://aws.amazon.com/s3/storage-classes/intelligent-tiering/) can also automatically move data
between storage classes based on changing access patterns.

Avoid costs by using a schema-on-read service, such as
[Amazon Athena](https://aws.amazon.com/athena/), to query the data in its native form. Using
Athena can help reduce the need for large-scale storage arrays
or always-on databases to read raw archival data.

To optimize storage costs, you can also use data lifecycle policies to automatically
move data between different storage classes based on the stage of the data. For example, you
can use [Amazon S3 lifecycle policies](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html)
to move data from S3 Standard to Amazon Glacier for archiving after a certain period of time.

Amazon DynamoDB Accelerator (DAX) or Amazon Timestream for time-series: If you are using Amazon DynamoDB
for real-time data storage, DAX can help improve read performance by caching frequently
accessed data. It reduces the need to retrieve data from the database directly, thus
optimizing data access. Alternatively, you can use Amazon Timestream as a fast, scalable, and
serverless time-series purpose-built database for short-lived real-time time series data.

**[CMCOST_BP1.2] Use data partitioning for optimize performance and
scalability**

Raw vehicle data can be partitioned based on time, geography, or other factors to optimize
storage and retrieval costs. For example, you can partition data by time to store data
generated in different time intervals in separate Amazon S3 prefixes. This allows you to scan
only the relevant data during query operations, reducing the amount of data scanned and the
cost of querying.

Implementing data partitioning offers several significant
advantages, making it an essential approach for handling
substantial volumes of data efficiently and effectively:

Splitting the raw data into smaller partitions based on relevant attributes (e.g.,
time, vehicle ID) can improve data retrieval and reduce costs. Additionally, compressing the
data before storage can significantly reduce storage costs and improve data transfer speed.
[AWS Glue](https://aws.amazon.com/glue/) or [Amazon Redshift](https://aws.amazon.com/redshift/) can be used for data partitioning, while Amazon S3 provides
built-in data compression options.

**[CMCOST_BP1.3] Choose the right services by evaluating storage
characteristics and requirements for your use case.**

Vehicles generate a massive amount of data, which needs to be stored for various reasons,
including compliance, regulatory requirements, and future analysis. As the volume of data
grows, so does the cost of storing and managing it. Cold storage, such as Amazon Glacier, is a
popular option for storing data that is infrequently accessed but needs to be retained for
the long term. However, due to factors like cost of retrieving the data from cold storage,
the overall data retention cost can be high. Effectively managing this data is crucial for
enhancing vehicle performance, improving user experiences, and enabling data-driven
decision-making.

Evaluate velocity, the volume of data coming and data retention/transfer cost from vehicles
when selecting storage services.

In this scenario, using a general-purpose database might be
inefficient and costly. It would require constant maintenance
to handle the high volume of incoming data and manage the
expiration of outdated information.

- For vehicle's short living time series data consider purpose-built database
service, [Amazon Timestream](https://aws.amazon.com/timestream/). Imagine a fleet
management system for a ride-sharing company. This system tracks the GPS coordinates,
speed, and passenger information of each vehicle in real-time. However, this data is
highly time-sensitive and loses its relevance after a short period, typically a few
days.
- Here's where Amazon Timestream comes into play. It is optimized for precisely this type
of data. It's designed to handle large volumes of time series data efficiently,
automatically managing the retention of old data and ensuring high availability for
querying recent information. By employing Amazon Timestream, the ride-sharing company can
effectively manage their vehicle data without the overhead of handling it in a
traditional database. This not only leads to cost savings but also allows for smoother
and more efficient operations.
- Your vehicle data use case may experience varying data
loads over time. Consider services like Amazon Aurora or
Amazon Redshift for scalable and flexible database
solutions that can adapt to changing demands without
compromising performance.
- For data at lower scale of time, devices, or other
characteristics—Consider Amazon DynamoDB or Amazon Aurora
for short-term historical data. Use your data lifecycle
policies to optimize what is kept in the short-term
storage.
- Amazon DynamoDB is a fully managed NoSQL database service
that is designed to handle low-scale to high-scale
workloads. It provides fast and predictable performance
with seamless scalability.

**[CMCOST_BP1.4] Sanitize your data and ensure that only essential
and accurate data is transferred to the cloud.**

Collecting only the necessary data is important for several
reasons because it helps to reduce the amount of irrelevant
data that can accumulate over time, which can clutter the
system and make it more difficult to extract useful insights.
Data sanitizing is a critical step in ensuring that only
essential and accurate information is transferred to the
cloud. This process involves identifying, cleansing, and
validating data before it's sent for storage or processing in
the cloud.

For example, outliers in GPS coordinates that are far from regular routes might be
flagged for further validation or omitted. Additionally, sensitive information like vehicle
identification numbers or proprietary algorithms may be anonymized or encrypted to protect
intellectual property and user privacy.

By sanitizing the data before integration with the cloud, the
connected vehicle system optimizes bandwidth usage, reduces
storage costs, and ensures that the information stored in the
cloud is of the highest quality and security. This practice is
fundamental in building a robust and efficient connected
vehicle ecosystem.

Process data at edge as much as possible:

- Edge analytics and decision making: Use edge computing platforms to perform
analytics and real-time decision-making directly in the vehicle. Implement AWS Lambda
functions on the edge to process data locally, enabling immediate actions without
incurring cloud round-trip latency.
- Prioritize critical or high-priority data for immediate
transmission to the cloud, while less time-sensitive data
can be sent during periods of lower network activity. This
strategy optimizes data transfer efficiency and reduces
cloud processing costs.
- Priority data (high sensitivity):

Scenario: A vehicle detects an imminent collision with
an obstacle or another vehicle.
- Response: This data is considered critical and
requires immediate transmission to the cloud. The
system prioritizes it for real-time analysis and
action, ensuring the safety of the vehicle and its
surroundings.

- Routine telemetry (lower sensitivity):

Scenario: The vehicle's telemetry data, including GPS
location, fuel levels, and tire pressure, is collected
for regular maintenance and analysis.
- Response: This data, while important, isn't as
time-sensitive. It can be queued for transmission
during periods of lower network activity, such as
during off-peak hours or when the vehicle is in a
low-traffic area.

Data filtering and pre-processing:

- Implement data filtering and pre-processing directly in
the vehicle's onboard systems. Use edge computing
solutions to analyze and filter out irrelevant or
redundant data at the source. This reduces the data volume
that needs to be sent to the cloud, leading to cost
savings on data transfer fees.
- Aggregate data locally in the vehicle to reduce the number
of individual data packets sent to the cloud. Apply data
compression techniques to further optimize data transfer,
minimizing data transmission costs.

Use [cost calculators](https://calculator.aws/#/) to model
different approaches for message size and count.

- The [AWS Pricing Calculator](https://calculator.aws/#/)can estimate costs for specific
message sizes, traffic, and operations.

CMCOST_2: How do you optimize your network consumption and interactions between
vehicles and cloud?

With an expansive amount of data collected from vehicles,
optimizing network consumption and payload size is essential
in to ensure efficient and effective data communication
between vehicles and the cloud. With limited bandwidth and the
need for real-time data processing, optimizing network
consumption reduces data usage and reduces costs. Lightweight
and efficient protocols such MQTT, data filtering,
compression, caching, quality of service, and optimized
routing is some of the best practices that can be employed.

- MQTT (Message Queuing Telemetry Transport): MQTT is a
lightweight and efficient messaging protocol designed for
devices with limited processing power or bandwidth. It's
based on a publish-subscribe model, allowing efficient
communication between devices and the server.

For example, in a connected vehicle system, if various sensors need to send data to
the cloud, MQTT can be employed. It minimizes overhead and ensures reliable communication.

- Data filtering: Data filtering involves the process of selectively extracting
relevant information from a larger dataset based on predefined criteria. This reduces
the volume of data that needs to be transmitted.
For example, in a fleet of vehicles, not all sensor data may be equally important.
Filtering out non-critical data ensures that only essential information is transmitted,
saving bandwidth.
- Compression: Compression reduces the size of data before transmission, decreasing
the amount of bandwidth required. This is particularly useful for transmitting large
datasets efficiently.
For example, in connected vehicles, images or video feeds from cameras can be
compressed before sending them to the cloud, reducing the amount of data that needs to
be transmitted.
- Caching: Caching involves storing frequently accessed data locally on the device or
in a nearby server. This minimizes the need for repeated requests to the cloud, reducing
latency and bandwidth usage.
For example, in a connected vehicle, frequently requested map data or software
updates can be cached locally, reducing the need for continual downloads.
- Quality of Service (QoS): QoS defines the level of service reliability and delivery
assurance during data transmission. It ensures that data is delivered accurately and
reliably.
For example, in a connected vehicle scenario, a high QoS level might be assigned to
safety-critical data like collision warnings, while less critical telemetry data might
have a lower QoS requirement.
- Optimized routing: Optimized routing involves selecting the most efficient path for
data transmission to minimize delays and reduce congestion on the network.
For example, in a fleet of vehicles, data can be routed through the most stable and
low-latency network connections available, ensuring timely delivery.

By implementing these practices, connected vehicle solutions
can operate seamlessly and effectively, improving overall
efficiency.

**[CMCOST_BP2.1] Compress and aggregate data whenever possible to reduce
the amount of data that needs to be transmitted over the network.**

Data filtering and aggregation:

- Implement data filtering and aggregation logic at the edge to send only relevant
and summarized data to the cloud. Use AWS IoT Core rules engine to perform data
transformations and filtering before transmitting data to the target systems for storage
or consumption by microservice.
- A common way to achieve better data transmission
efficiency is by combining a series of measurements into a
single message enabling also more efficient compression as
the volume of the message increases. You can leverage
[AWS IoT GreenGrass v2 components](https://aws.amazon.com/blogs/iot/5-tips-to-build-aws-iot-greengrass-v2-components/) to implement your
aggregation function at edge.

Compress data whenever possible to reduce size of data transmitted.

- Techniques such as `gzip` compression can reduce significantly the
size of data being sent. You can use [AWS IoT GreenGrass
v2 components](https://aws.amazon.com/blogs/iot/5-tips-to-build-aws-iot-greengrass-v2-components/) to implement your compression function at edge.
- You can also use Protocol Buffers (protobuf – binary format) that provides an
efficient structured compressing mechanism. You can use [AWS IoT Core and AWS Lambda](https://aws.amazon.com/blogs/iot/protobuf_with_aws_iot/) to ingest and
process Protobuf for consumption.
- If using AWS IoT FleetWise for data collection you can [configure your
campaign](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_CreateCampaign.html) to compress signals before transmitting data using
`SNAPPY`.

**[CMCOST_BP2.2] Adjust collection frequency depending on the
context.**

Evaluate and adjust the frequency of data collection depending
on functional and business need. By adjusting the collection
frequency of data from a connected vehicle based on the
context, you can minimize unnecessary data transmission and
optimize cloud resources. This approach helps to ensure that
the most relevant and critical data is delivered to the AWS Cloud while reducing data transfer costs and improving overall
data efficiency.

- Adjust frequency as needed based on events or context in
the vehicle such as increased frequency telemetry when
operating in autonomous mode. You can configure
[Rules-based
collection campaign](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/campaigns.html) in AWS IoT FleetWise or develop
an
[AWS IoT GreenGrass v2 component](https://aws.amazon.com/blogs/iot/5-tips-to-build-aws-iot-greengrass-v2-components/) that dynamically adapt
collection frequency depending on an event in the vehicle.
Similarly, you can leverage same event-based collection
schemes to send to the cloud telemetry only if an event
happens or a rule is matched such collecting weather
telemetry only if engine overheat.
- Define threshold values for each event or context
parameter that determine when the data collection
frequency should be adjusted. Set triggers to respond to
changes in the context, such as exceeding a certain speed
limit or encountering specific driving conditions.

**[CMCOST_BP2.3] Choose the right communication service and
configuration depending on the use case.**

Use MQTT 5 protocol properties to optimize bandwidth.

- MQTT Protocol for Lightweight Communication: Use the
lightweight MQTT (Message Queuing Telemetry Transport)
protocol for communication between vehicles and AWS IoT Core. MQTT is efficient in terms of bandwidth and is
well-suited for IoT applications.
- You can use MQTT 5 properties to further optimize the bandwidth between vehicle
and backend. You can set "Message Expiry Interval" to not hold messages indefinitely on
the client when client disconnects, this should be done in particular for messages that
have a performance expectations like Remote Operations that should be very short lived.
- AWS IoT Core device shadow: Use the AWS IoT Core device shadow to store and synchronize
the current state of vehicles with the cloud (fleet management systems or user mobile
devices). This enables vehicles to retrieve the latest desired state from the cloud
without continual communication, reducing network consumption.

Optimize routing and use caching mechanisms:

- **Caching:** Caching involves storing frequently accessed
data locally on the device or in a nearby server. This minimizes the need for repeated
requests to the cloud, reducing latency and bandwidth usage. Example: In a connected
vehicle, frequently requested map data or software updates can be cached locally,
reducing the need for continual downloads.
- **Quality of Service (QoS):** QoS defines the level of
service reliability and delivery assurance during data transmission. It ensures that
data is delivered accurately and reliably. Example: In a connected vehicle scenario, a
high QoS level might be assigned to safety- critical data like collision warnings, while
less critical telemetry data might have a lower QoS requirement.
- **Optimized routing:** Optimized routing involves selecting
the most efficient path for data transmission to minimize delays and reduce congestion
on the network. Example: In a fleet of vehicles, data can be routed through the most
stable and low-latency network connections available, ensuring timely delivery.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/connected-mobility-lens/cost-effective-resources.html*

---

# Expenditure and usage awareness

CMCOST_3: How do you select the compute and storage solution for your vehicle
data?

The right storage and compute solution for vehicular data depends on a variety of factors including the volume of data being generated, the speed at which it needs to be processed, its computation requirements, the security requirements, and the budget available for infrastructure. These factors are essential to ensure that the solution chosen can handle the amount of data generated by vehicular systems, process the data in real-time, store the data securely, and deliver insights that can be used to optimize vehicular operations.

**[CMCOST_BP3.1] Analyze the data volume and evaluate the processing
needs to save on computation costs**

Improve the ROI by using serverless architecture.

- Implement serverless computing to minimize infrastructure costs and focus on
developing innovative services. With AWS Lambda, you can run code without the need to
manage servers, which makes it ideal for processing data from connected vehicles.
Serverless architecture can improve return on investment (ROI) when it comes to
vehicular data by reducing infrastructure costs, optimizing resource utilization, and
enabling faster application development.
- Serverless function for real-time aggregation: Use AWS Lambda or a similar
serverless function to aggregate trip data in real-time. This function should collect
and process data from multiple sensors and sources during a trip.
- Stream processing for efficiency: Use Amazon Kinesis or similar stream processing
services to handle data streams efficiently. This ensures that data is processed as it
arrives, reducing latency and improving responsiveness.
- Data validation and error handling: Implement data validation checks within the
serverless function to ensure the integrity of aggregated trip data. Handle any errors
or exceptions gracefully.
- Real-time score calculation: Implement a serverless function that calculates
driver scores based on aggregated trip data. This function should factor in various
parameters like speed, acceleration, braking, and adherence to traffic rules.
- By implementing these strategies, you can harness the
power of serverless architecture to efficiently aggregate
trip data and calculate driver scores. This not only
improves the overall efficiency of the system but also
contributes to increased ROI by promoting safer and more
cost-effective driving behaviors. Velocity
- Cost efficiency: Evaluate the cost of the compute and storage services in
relation to your budget and expected data workload. Consider services with pay-as-you-go
pricing and cost optimization features like AWS Cost Explorer.
- Implement storage lifecycle policies to optimize cost and utilize Amazon S3
Intelligent-Tiering.
- Define data archiving and lifecycle policies to automatically move less frequently
accessed data to cost-effective storage tiers like Amazon Glacier or Amazon S3 Intelligent-Tiering.

**[CMCOST_BP3.2] Use data analytics to analyze vehicular data and
develop new services with minimum investment.**

Assess the volume of data generated by your vehicles and the
velocity at which the data is produced. High-velocity data
might require solutions with low latency and high throughput,
while large volumes of data might demand scalable storage
options.

Data volume and velocity:

- Analyze the data from connected vehicles to gain insights
and develop new services. Analyzing vehicular data can
help in identifying patterns and trends that can be used
to improve existing services and prevent the need for
reinventing the wheel.
- Data filtering and prioritization:

Guidance: Implement filters at the edge to capture
only essential data, prioritizing critical information
for immediate transmission.
- Example: In a connected vehicle, prioritize
safety-critical events like collision alerts over less
critical data like routine diagnostics.

- Optimize data transmission protocols (for example, MQTT):

Guidance: Choose lightweight, efficient protocols like
MQTT for communication. It minimizes overhead and is
ideal for low-bandwidth environments.
- Example: Use MQTT to transmit aggregated sensor data
from a vehicle to the cloud with minimal packet
overhead.

- Use of data compression techniques:

Guidance: Implement data compression algorithms to
reduce the size of transmitted data.
- Example: Compress image or video data from vehicle
cameras before transmission, reducing the bandwidth
required.

- Optimize frequency of telemetry updates:

Guidance: Adjust the frequency of telemetry updates
based on need. Reduce update rates for less
time-sensitive data.
- Example: Decrease the update frequency for components
with stable readings, like tire pressure, to conserve
bandwidth.

- Implement data retention policies:

Guidance: Define policies for data retention. Store
only relevant data and set expiration rules to manage
storage costs.
- Example: Store high-resolution telemetry data for a
limited period and transition to lower-resolution data
for historical analysis.

- By implementing these strategies, you can efficiently
manage the volume and velocity of connected vehicle data,
ensuring that only relevant, timely information is
transmitted to the cloud. This not only optimizes costs
but also enhances the overall performance of the IoT
application.

**[CMCOST_BP3.3] Integrating with existing infrastructure cost
efficiently.**

- Cost efficiency: Evaluate the cost of the compute and storage solutions in
relation to your budget and expected data workload. Consider services that provide
pay-as-you-go pricing and allow you to optimize costs based on actual usage.
- Use existing APIs and protocols:

Guidance: Use standard APIs and protocols for integration with existing
systems. This minimizes the need for custom development.
- Example: Integrate connected vehicle data using RESTful APIs, MQTT, or OPC
UA, depending on compatibility with existing infrastructure.

- Implement edge computing for local processing:

Guidance: Use edge computing to process data locally
before integration with existing systems. This reduces
the load on centralized servers.
- Example: Employ edge devices like IoT gateways to
pre-process data from connected vehicles before
sending it to the central system.

- Implement data transformation layers:

Guidance: Introduce data transformation layers to
convert data formats between connected vehicle systems
and existing infrastructure.
- Example: Use AWS Lambda functions to transform and map
incoming data from vehicles to match the format
expected by the existing systems.

- Leverage message brokers for integration:

Guidance: Implement message brokers such as Apache Kafka or Amazon Managed Streaming for Apache Kafka for
seamless integration with existing systems.
- Example: Use Apache Kafka to buffer and process data streams from connected
vehicles before ingestion into on-premises databases.

- Use standard data formats (for example, JSON or XML):

Guidance: Ensure that data exchanged between connected vehicles and existing
infrastructure uses standard formats to ease integration. For example, convert
vehicle telemetry data to JSON format before passing it to legacy systems that
understand this format.

By following these strategies, you can efficiently integrate connected vehicles with
existing infrastructure, ensuring seamless data flow while optimizing costs associated with
integration efforts.

This involves fine-tuning resource allocation, enhancing scalability, and
capitalizing on managed services to steer clear of over-provisioning.

- Managed services: Use AWS managed services like AWS IoT Core for device
management, AWS DynamoDB for NoSQL database needs, and Amazon S3 for scalable and
cost-effective object storage. These services reduce the overhead of managing
infrastructure and are often more cost-efficient than self-managed solutions.
- Implement automatic scaling for compute resources like EC2 instances to
dynamically adjust capacity based on demand: Automatic scaling helps ensure that you
have the right number of resources at any given time, optimizing costs by only paying
for what you use.
- Reserved Instances or Savings Plans: If you have predictable workloads, consider
purchasing AWS Reserved Instances or Savings Plans. These offer upfront cost savings and
discounted pricing compared to On-Demand Instances.
- AWS cost management tools: Set up AWS Budgets and cost alarms to receive notifications
when your spending exceeds predefined thresholds, helping you maintain better control
over costs.**

*Source: https://docs.aws.amazon.com/wellarchitected/latest/connected-mobility-lens/expenditure-and-usage-awareness.html*

---

# Matching supply and demand

CMCOST_4: How do you optimize cost by matching backend resources with demand?

Connected vehicle solutions generate a massive amount of data and events, which can
quickly become overwhelming for traditional, request-response-based architectures.
Event-driven architectures allow for a more scalable solution, as events are processed
asynchronously, allowing for faster and more efficient handling of large volumes of events
and consume resources only when and if events occur.

**[CMCOST_BP4.1] Implement event driven architectures for your backend
systems.**

- Use AWS managed services such [Amazon EventBridge](https://aws.amazon.com/eventbridge/) or [Amazon Managed Streaming for Apache Kafka (MSK)](https://aws.amazon.com/msk/) for
event bus, [AWS Lambda](https://aws.amazon.com/lambda/) or [AWS Fargate](https://aws.amazon.com/fargate/) for event processing, and [AWS Step Functions](https://aws.amazon.com/step-functions/) for orchestrating the
business. The combination of event driven architectures and AWS managed services helps
you consume resources only when an event occurs and for the time processing the event
while decoupling the different components of the system.
- You can leverage event-driven architecture to process events from vehicle as
illustrated in this blog [Building event-driven architectures with IoT sensor data](https://aws.amazon.com/blogs/architecture/building-event-driven-architectures-with-iot-sensor-data/). You can also expand
the event-driven pattern to other business applications as illustrated for [Building an Interactive Sales Portal for Automotive Using AWS Microservice
Architecture](https://aws.amazon.com/blogs/apn/building-an-interactive-sales-portal-for-automotive-using-aws-microservice-architecture/)

Evaluate and select your compute type depending on events
processed by your backend systems.

- Consider using AWS Lambda for events that can be processed asynchronously with one
or a cascade of processing steps short lived time (up to 15 minutes) that can be
orchestrated with AWS Step Functions. As an example, Lambda are suitable for an API based service
such subscription management for a service. Use AWS Step Functions to coordinate serverless
workflows. It helps manage and control the execution order of your Lambda functions and
other services, reducing the time and resources needed for complex tasks.
- Consider using containers through Amazon Elastic Kubernetes Service (Amazon EKS) or Amazon Elastic Container Service (Amazon ECS) when you
need near real time event processing of large-scale number of events or require more
processing time. Both Amazon EKS and Amazon ECS offer AWS Fargate that run your containers
serverless without any underlying infrastructure to maintain.
- As an example, containers are suitable for large number of
MQTT messaging based events that needs near real time
processing such vehicle diagnose data collection and
processing after a defect being detected.
- Amazon EC2 Spot Instances: For non-critical workloads,
consider using EC2 Spot Instances. Spot Instances are
available at significantly lower prices compared to
On-Demand instances but can be interrupted with short
notice when the Spot price exceeds your bid. Use Spot
Instances to handle non-time-sensitive tasks and save
costs.
- AWS Cost Explorer and AWS Budgets: Utilize AWS Cost Explorer and AWS Budgets to monitor and analyze your AWS
costs. These tools provide insights into spending patterns
and can help you identify opportunities for optimization.
- Finally, for large batch processing [AWS Batch](https://docs.aws.amazon.com/batch/latest/userguide/what-is-batch.html)
that helps you to run batch computing workloads on the AWS Cloud.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/connected-mobility-lens/matching-supply-and-demand.html*

---

# Cloud Financial Management

CMCOST_5: Have you defined a tagging strategy for your connected mobility
workloads?

Resource classification allows you to categorize resources, providing clarity on
usage and enabling you to allocate costs accurately to different departments or projects.
Targeted Cost Allocation with tags, you can pinpoint specific resources and their costs,
allowing for precise billing and enabling you to identify areas where cost-saving measures
can be implemented effectively.

**[CMCOST_BP5.1] Define and implement an organizational tagging
strategy, and require key tags.**

- Engage with relevant stakeholders across line which could include line of business
teams, financial and governance teams, cloud operations teams, and other stakeholders.
Define the use cases needed for tagging, define required versus optional tags, discuss
ways to enforce tagging, and who will own the tagging of resources. As an example, you
might want to define a tag to track resources used for a specific OEM to allow you to
allocate costs appropriately.
- Publish a common and consistent naming schema. This should
include naming and value conventions, publishing required
and optional tags, and define and publish the process for
adding new tags, or modifying existing tags.
- Implement your tagging strategy:

For manually managed resources you can use AWS Config
which can be used to look for required tags, and if
missing, apply them to resources using Lambda.
- When using infrastructure as code (IaC), use the CloudFormation resources tag
property to define tags to add required tags on resource creation. This action helps
ensure that required tags are configured before resource creation. Use AWS CloudFormation
Hooks to check before resource creation, and warn or prevent resource creation when
missing key tags.

- Enforcing your tagging can be done using tagging policies and service control
policies (SCP) in combination.

Tagging policies allow you to define and standardize your tag keys, including
capitalization, and what values are allowed to be used within the specific tag.
- Service control policies allow you to block resource creation when required
tags are missing.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/connected-mobility-lens/cloud-financial-management.html*

---

# Optimize over time

CMCOST_6: How do you optimize the payload size to reduce cost in evolving
generations of connected vehicles?

**[CMCOST_BP6.1] Dynamically adjust the payload capacity to accommodate
changing conditions or demands**

Implement dynamic payload adjustment based on network conditions and available
bandwidth. For example, adaptively vary payload size based on real-time network conditions
to optimize for cost and performance.

Prioritize critical data: Ensure that critical or safety-related data is prioritized
in the payload, while less time-sensitive data can be sent during off-peak times or in
batches. Example: In a connected vehicle, prioritize alerts for collision warnings over
routine diagnostics.

CMCOST_7: How do you optimize the cost of storing the state of connected
mobility application over time?

**[CMCOST_BP7.1] Implement a monitoring strategy.**

Continually monitor and analyze usage patterns, network traffic, and associated costs.

- Define key cost metrics: Identify critical cost metrics relevant to connected
mobility, such as data transmission costs, edge processing expenses, and cloud storage
charges. For example, monitor data usage per vehicle, edge processing costs, and cloud
storage fees to understand cost drivers.
- Set budgets and alarms: Establish budget thresholds for each cost metric and
configure alarms to notify when thresholds are approaching or exceeded. Example: Set a
budget for monthly data transmission costs and configure an alert to notify when 80% of
the budget is reached.
- Regularly review cost reports: Conduct regular reviews of cost reports to
identify anomalies, trends, or cost spikes that may require investigation or
optimization. Example: Review weekly cost reports to spot any unexpected increases in
data transmission costs.
- Optimize resource usage with AWS Trusted Advisor: AWS Trusted Advisor to receive
recommendations for optimizing resource usage and reducing costs. Example: Act on
recommendations to modify resource configurations for improved efficiency and cost
savings.
- Implement cost-effective data management practices: Apply data retention
policies, archival, and deletion strategies to minimize storage costs without
sacrificing critical data availability. Example: Archive historical telemetry data to
lower-cost storage solutions after a specified time period.
- Track and optimize data transmission costs: Monitor data transmission costs from
vehicles to the cloud and consider techniques like data aggregation, compression, and
prioritization to reduce expenses. Example: Implement payload optimization techniques to
minimize the amount of data transmitted, thereby reducing costs.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/connected-mobility-lens/optimize-over-time.html*

---

# Key AWS services

The following services and features are important in the five areas of cost
optimization previous covered in this document:

- **Cost-effective resources:** Amazon S3, Amazon Athena, Amazon DynamoDB
Accelerator, AWS IoT Greengrass, AWS IoT Core, AWS IoT Greengrass, AWS IoT FleetWise, API Gateway, CloudFront are AWS services that
enable you to optimize storage of raw data, optimize network consumption to improve the
cost effectiveness of compute resources.
- **Expenditure and usage awareness:** AWS Cost Explorer, AWS
Budgets, Anomaly Detector, AWS Cost and Usage Reports are AWS services that enable you
to view and analyze your costs and usage.
- **Matching supply and demand:** Analyzing the demands of
workloads over time can help in matching the supply. Quick, and AWS Cost and Usage
Reports, are two services that can help you perform a visual analysis of workload demand.
- **Cloud Financial Management:** AWS Config, AWS CloudFormation resource
tags, service control policies, AWS tags are AWS services that can help enable a
cost-conscious culture that drives accountability across all teams and functions.
- **Optimize over time:** In AWS, you optimize over time by
reviewing new services and implementing them in your workload. The [AWS What's New with Cost Optimization](https://aws.amazon.com/about-aws/whats-new/cloud-financial-management/?whats-new-content.sort-by=item.additionalFields.postDateTime&whats-new-content.sort-order=desc&awsf.whats-new-products=*all) page is a resource for learning about
what is newly launched as part of AWS's Cost Optimization Pillar.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/connected-mobility-lens/key-aws-services-cost.html*

---

# Resources

**Documentation and blogs:**

- [Connected Mobility
Solutions](https://aws.amazon.com/automotive/connected-mobility/)
- [Monitoring Tools
in AWS](https://docs.aws.amazon.com/apigateway/latest/developerguide/monitoring_automated_manual.html)
- [Trends Dashboard with AWS Cost and Usage Reports, Amazon Athena and Quick](https://aws.amazon.com/blogs/aws-cloud-financial-management/trends-dashboard-with-aws-cost-and-usage-reports-amazon-athena-and-amazon-quicksight/)
- [AWS Resource
Tagging](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html)
- [AWS Cloud Financial
Management Blogs](https://aws.amazon.com/blogs/aws-cloud-financial-management/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/connected-mobility-lens/resources-cost.html*

---
