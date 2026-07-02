# Performance efficiency

**Pages**: 7

---

# Design principles

Core capabilities

- Vehicle provisioning
- Command and control functions
- Telemetry
- Over-the-air updates (OTA)
- Mobile applications – Remote operations (for example, remote start)

**Edge processing and vehicle shadow service architecture:** The
fundamental idea behind this principal is that the automotive industry is transforming itself
to provide a more software centric mobility experience to their customer through applications
and services for both safety and non-safety critical features. This ranges from safety
features in AV/ADAS space as well non-safety critical features like personalization, content
recommendation, trips, navigation, and more. This pushes the need to have more on-board
vehicle compute and storage with high performance CPUs and GPUs. While this is good, there
will never be enough storage and compute on-board vehicles to meet growing industry needs to
provide these experiences and match them with the necessary safety standards. Therefore, the
need exists to have more hybrid architecture and services in place to offload portions of
non-safety critical workloads to edge locations closer to the vehicles to meet latency
requirements.

**Design for failover:** Failures in connected mobility systems
are inevitable especially when vehicles are traversing in suburbs and terrains where
connectivity is spotty and is critically impacted. Working through all possible "what-if"
scenarios during design phase and also having test cases to validate possible scenarios is a
critical aspect of building these systems. Apart from connectivity, it's also important to
build resilient and highly-available cloud systems with a fallback system in place for worst
case scenarios.

**Auto scaling everywhere:** Running and maintaining a connected
mobility application can be expensive, especially when adhering to specific SLAs and KPIs that
cannot be compromised. By using the appropriate services on AWS and applying best practices
and recommendations, customers can handle variable vehicle-cloud data volume spikes and high
vehicle density in specific geographies. This ensures that systems are automatically scalable
on a needed basis and are not running at full capacity at all times, especially during
low-usage periods.

**Multiple connectivity channels:** Vehicle-cloud connectivity is
an integral part of providing a good connected mobility experience. Relying on a single
connectivity channel is error prone due issues like coverage, quality of service (QoS) and
bandwidth capacity and availability. Therefore, it is recommended to explore more than one
connectivity channel not only as a fallback mechanism in case of fail-over, but also as a
means to use different channels for different workload needs. Options can vary, but could
include using secure Wi-Fi for large OTA upgrades to save data costs, using 5G for high
bandwidth, low latency connectivity needs for edge computer-vision or AI/ML workloads, or
using satellite for vehicle-cloud connectivity for high bandwidth needs where latency is not
critical and 5G connectivity is unreliable.

**Every workload is different:** Connected mobility workloads
have their own set of challenges ranging from collecting data when the vehicle is in motion,
processing them and offloading them. It includes latency and bandwidth requirements for data
transfer, and its own SLAs and KPIs that must be met to function optimally.  This is
especially important for safety critical features which cannot be offloaded to edge locations
but still rely on cloud connectivity for some operations. So rather using a modular
architecture approach for all use cases, using these as guiding principles to design what
would be the optimal location for workload execution (edge or region) and tradeoffs can be
made keeping the user safety in mind.

**Measuring and improving with growth:** Having mechanisms in
place where critical workloads are monitored for specific KPI's for performance and ensuring
that it meets the desired SLAs is critical. Even with features like auto-scalable systems, as
more and more vehicles are on-boarded to connected mobility systems it's inevitable that
feature level and overall system performance will degrade over time. Therefore, understanding
tradeoffs in latency and cost in order to support continuously evolving systems, architectures
and mechanisms are needed in order to support critical workloads wherever the vehicle is
operating.

**Regulatory compliance tradeoffs:** Adhering to local laws and
regulatory compliance is mandatory. Care must be taken to assess and consider any impact on
performance while adhering to them. Based on data processing compliance requirements design
your workload architecture to process the data closer to the edge whenever possible can offset
some of the performance concerns.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/connected-mobility-lens/design-principles-perf.html*

---

# Selection

CMPERF_1: Have you identified the critical components of the architecture,
performance data collection to determine the best performing architecture?

The connected mobility ecosystem falls under multiple areas based on the type of use
cases. Architecture needs to account for vehicle, cloud, and communication between the
vehicle and cloud. Break down your application into smaller, independent microservices that
can be managed and scaled independently as needed.  By treating data as a product, package
it at the device (vehicle) by categorizing the data, before sending it to the cloud.
Classify the data based on frequency (for example, every 60 seconds), events, on-demand (for
example, during a failure event, send diagnostic logs). Architect your data processing
platform by decoupling the data collection from processing and offloading to cloud. In cloud
similar architecture approach needs to be in place to process data, before sending them to
downstream application consumption.

Additional aspects to take into account on data:

- Timeliness of the data by minimizing latency (for example, 200 milliseconds or
less).
- Data as current as possible (close to real time).

Primary goal – To support internal applications (for example, last location
of vehicle, and fuel information.)
- Vehicle state service – Last known values per vehicle

- Business intelligence data

Primary goal – To support the business for understanding the features use
(for example, infotainment, driver usage patterns, and environmental data)

When developing a connected mobility platform on AWS focusing on performance efficiency,
there are essential architectural components and methods for performance data collection
that should be identified and optimized. Let's break this down:

**[CMPERF_BP1.1] Confirm critical components of the connected vehicle
platform**

The critical components of a connected vehicle platform into the simplified structure
of data plane, control plane, and consuming applications:

- **Data plane:** This is concerned with the movement of data
throughout the system.

**In-vehicle data plane:**

**Data ingestion:** The vehicle collects real-time
data from its sensors and systems.
- **Edge processing:** The vehicle's onboard systems
process this data locally, especially vital in areas with spotty connectivity.
This can involve analyzing sensor data, determining the current vehicle status,
or even making immediate decisions like automatic braking in emergencies.

- **Cloud data plane:**

**Data ingestion:** This is where real-time data
from vehicles is received, ingested, and stored in the cloud for further
processing or analysis.

- **Control plane:** This component manages and coordinates
the operations of the system, including ensuring the system's proper function and
orchestrating event-driven processes.

**In-vehicle control plane:**

Directly interacts with the vehicle's hardware and
systems. It takes action based on the processed
data, such as adjusting vehicle settings or
activating certain features.

- **Cloud control plane:**

**Compute:** This involves running code in response
to specific triggers, like changes in data or custom events. With a serverless
architecture, this can be event-driven, scaling automatically based on demand.

- **Consuming applications:** These are interfaces and
applications that end users (drivers, passengers, or vehicle owners) interact with.

**Mobile applications:** Drivers and users can access
mobile apps to control and monitor their vehicles remotely. This includes functions
like starting the vehicle remotely, locking/unlocking doors, checking oil levels,
and scheduling starts to pre-warm or cool the vehicle.

**[CMPERF_BP1.2] Enforce performance data collection**

To determine the best performing architecture, it's vital to
continuously collect, monitor, and analyze performance data.

- Collects and tracks metrics, collects and monitors log
files, and sets alarms. It can be used to collect and
track custom metrics.
- Get insights into the behavior of your applications,
helping to understand how they are performing and where
bottlenecks are occurring.
- Use cloud-native tools to review the resources health, performance, and
optimizations recommendations.

Note
To derive cost per vehicle = Total cloud cost / Number of vehicles connecting to the
platform.

CMPERF_2: Have you conducted performance tests for vehicle-to-connected
mobility platform communication across various connectivity methods, including LTE,
Wi-Fi, satellite, and scenarios with no connection?

The performance of vehicle-to-connected mobility platform communication across different
connectivity methods is crucial for the seamless functioning of connected vehicles.

**Steps to test performance across various connectivity methods:**

**[CMPERF_BP2.1] Define key metrics**

Decide what you'll measure, including latency, bandwidth, data consistency, and uptime,
across different connectivity methods.

Simulate environments:

- **LTE:** Mimic a mobile LTE connection with varying signal
strengths.
- **Wi-Fi:** Test under various conditions, for example,
stable home networks, and public Wi-Fi with many connected devices.
- **Satellite:** If possible, conduct tests in environments
where only satellite connectivity is available, such as remote or maritime areas.
- **No connection:** Simulate scenarios where a vehicle loses
connection. Monitor how much data is stored locally and then synced when connectivity is
restored.
CautionThere will be storage limitations on the vehicle side and it is critical to
implement logic to persist critical data versus non-critical data.

**[CMPERF_BP2.2] Check data consistency**

Ensure that data is consistent across various connection states, especially when
transitioning between them.

**[CMPERF_BP2.3] Evaluate fail-over and redundancy. If one connection
method fails, does the system seamlessly switch to another available method?**

A successful connected vehicle platform not only requires
solid performance under various connectivity conditions but
also robust security, redundancy, and fail-over mechanisms.

CMPERF_3: Have you evaluated the performance of the connected mobility platform
to ensure it can accommodate future vehicle demand projections?

When designing a connected mobility platform, especially for performance efficiency,
it's crucial to evaluate its performance to ensure it can accommodate future vehicle demand
projections. When you are testing the performance and scalability of the platform, keep the
current capacity as 70% utilized, and 30% of capacity available for future needs (for new
vehicles load including data). Based on your vehicle demand projections, forecast 30% of the
infrastructure capacity is available with your vendors (cloud, marketplace, licensing) for
your workloads

**[CMPERF_BP3.1] Evaluate performance and
scalability**

- **Assess current performance:** Determine the platform's
current performance metrics, including throughput, latency, error rates, and capacity.
- **Load, stress, and scalability testing:** Simulate
the expected number of vehicles and users to test how the system behaves under
anticipated loads. This will help identify any bottlenecks or performance issues. Push
the system beyond its expected limits. This helps to understand the system's breaking
point and ensures that it fails gracefully. Determine if the system can scale out (add
more instances) or scale up (add more resources to an instance) to meet increased
demand. This is crucial for accommodating future growth.
- **Performance monitoring:**Continuously monitor system
performance in real-time to identify and address issues before they impact users.
- **Future demand projections:** Use data analytics to
project future vehicle demands based on current trends, market research, and other
relevant factors.
- **Infrastructure evaluation:** Ensure that the underlying
infrastructure (servers, databases, networks) can support the projected increase in
demand.
- **Database optimization:** As the number of vehicles and
data points increase, database performance becomes critical. Regularly optimize queries,
indexes, and storage solutions.
- **Geographical distribution:** If the platform serves a
global audience, consider distributing data centers geographically to reduce latency and
improve performance for users worldwide.
- **Redundancy and failover:** Ensure that there are backup
systems in place to take over if the primary system fails. This is crucial for
maintaining uptime during unexpected events.
- **Feedback loop:** Regularly gather feedback from users and
stakeholders to understand any performance-related issues they face and address them
proactively.
- **Threshold limits:** In addition to load test,
scalability, performance it is critical to understand the limits on the cloud side
especially on compute resources, load balancer limits, data transfer across regions /
3rd party providers. It's good practice to keep an eye on service limits to make sure
monitoring is in place to alert and take proactive action.

CMPERF_4: Have you assessed the performance of the connected mobility platform
when integrated with third-party vendor solutions?

Connected mobility platforms when integrated with third-party vendor solutions
evaluate and select a high-performing architecture that aligns with your organization's
goals for efficiency.

**[CMPERF_BP4.1] Implement steps for performance
assessment**

- Map integration: Identify data flows, dependencies, and potential bottlenecks.
- Baseline metrics: Establish key performance metrics like latency, throughput,
response time and error rates.
- Testing: Perform load and stress tests to simulate
real-world traffic.
- Dependency checks: Assess software and hardware dependencies.
- Data integrity: Ensure data consistency and integrity between integrated systems.
- Security and compliance: Evaluate security protocols and ensure legal compliance.

**[CMPERF_BP4.2] Collect key performance
metrics**

- Scalability: Can the system handle growth efficiently?
- Latency and throughput: Assess speed and capacity under different loads.
- Resilience: Evaluate fault tolerance and fail-over
capabilities.
- Resource utilization: Monitor CPU, memory, and bandwidth usage.
- Interoperability: Assess ease of integration with other
systems.
- Monitoring: Use analytics to identify bottlenecks or
inefficiencies.
- Cost: Evaluate total cost of ownership (TCO).

When assessing the performance of third-party integrations on a platform like the
connected mobility platform, it's essential to employ a mix of monitoring, testing, and
optimization tools. AWS offers a robust suite of services that can be leveraged for these
purposes.

CMPERF_5: Have you considered irregular data traffic patterns during the day or
within Regions and can the system handle sporadic traffic without impacting the
overall Service Level Agreement (SLA) and user or vehicle experience?

**[CMPERF_BP5.1] Address irregular data traffic patterns and ensure
that the system handles sporadic traffic efficiently.**

These steps are crucial for a connected mobility platform or any large-scale system. AWS
offers various solutions and services that can help in managing these unpredictable
workloads without impacting the SLA, user, or vehicle experience.

**[CMPERF_BP5.2] Take into account that mobility patterns can vary
significantly.**

When selecting an architecture, some factors to consider are peak commuting hours,
weekends, holidays, climatic conditions (summer versus winter), or even unexpected events
such as accidents and natural disasters.

- Dynamic scaling: Your system architecture should be able to scale up or down
based on demand to handle irregular data traffic patterns. Cloud-based solutions often
provide auto-scaling features to meet this need.
- Quality of Service (QoS): Implement QoS mechanisms to
prioritize essential or time-sensitive data over less
critical data, ensuring that crucial functions are always
available.
- Caching and data aggregation: Use caching mechanisms to store frequently used
data temporarily. Data aggregation techniques can help in reducing the amount of data
that needs to be transmitted, thus relieving pressure on the system during peak loads.
- Rate limiting: Consider implementing rate limiting for non-essential or batch
operations. This ensures that the system remains available for real-time and
high-priority tasks.
- Redundancy and fail-over: Design the architecture with redundancy in mind to
handle failures without affecting the SLA. Implement failover systems that can take over
in case one part of the system becomes overloaded or fails.
- Traffic analysis: Use real-time monitoring and analytics to identify traffic
patterns. This analysis can help in pre-scaling resources before a predicted
high-traffic event.
- SLA monitoring: Implement tools that continuously monitor the system to ensure
that it meets the agreed-upon SLAs, even during times of sporadic or high traffic.
- Geographical distribution: Consider deploying resources in multiple geographic
locations if you expect irregular traffic patterns across different regions.
- User experience monitoring: Keep track of metrics that directly reflect user or
vehicle experience such as app load times, navigation responsiveness, and real-time
updates.
- Testing: Perform extensive stress and load testing
simulating irregular traffic patterns to validate that the
system can meet SLAs and provide a good user/vehicle
experience under these conditions.

By accounting for these factors in your architecture selection, you can better
prepare the connected mobility platform to handle irregular and sporadic traffic patterns
without adversely affecting performance or user experience.

CMPERF_6: Have you taken into account any data regulatory requirements for
vehicles and tested that might affect performance?

**[CMPERF_BP6.1] Consider data regulatory
requirements**

- Data privacy and protection: Regulations like the General Data Protection
Regulation (GDPR) in the European Union or the California Consumer Privacy Act (CCPA) in
the United States mandate strict controls over personal data. Ensuring compliance can
introduce additional processing steps, like encryption or anonymization, which might
impact performance.
- Data localization: Some regulations require data to be stored in the same country
or region where it's generated. This can affect the architecture of your platform,
potentially introducing latency if data needs to be accessed from distant locations.
- Data retention and access: Regulations might dictate how long you can store data
and who can access it. Implementing these controls can introduce additional database
queries or checks, impacting performance.
- Data transmission: Secure transmission of data, SSL termination and off-loading
especially in real-time applications, is crucial. Implementing robust encryption
protocols (for example, mTLS) can introduce latency, affecting SLAs.
- Audit and logging: To ensure compliance, you might need to maintain detailed logs
of all data accesses and changes. Writing and storing these logs can have performance
implications.
- Data recovery and backups: Regulations might require you to have robust data
recovery solutions in place. While this might not directly impact performance, it can
affect SLAs, especially in terms of data recovery times.
- Third-party integrations: If your platform integrates with third-party services,
you need to ensure they are also compliant with relevant regulations. Their performance
and SLAs can directly impact your platform.
- Continuous monitoring and reporting: To ensure ongoing compliance, continuous
monitoring and reporting mechanisms might be needed. These systems can introduce
additional loads on the platform.

**[CMPERF_BP6.2] Take regulatory requirements into account as you
define SLAs for a connected mobility platform**

These requirements can have a direct impact on performance and the Service Level
Agreements (SLAs) you set. For example, if data encryption introduces a delay, factor that
into your SLA. Similarly, if data localization introduces latency, that should be considered
when setting performance benchmarks.

CMPERF_7: Have you considered a vehicle simulation tool to create artificial
load scenarios for better understanding and analyzing the performance metrics of the
system?

**[CMPERF_7.1] Simulate real-world scenarios to understand how the
system will behave under various conditions**

Using a vehicle simulation tool can be invaluable in this context. Using vehicle
simulation tools is an excellent approach to stress-test a connected mobility platform. By
simulating various load scenarios, you can evaluate how the system performs under different
conditions, anticipate potential bottlenecks, and optimize accordingly.

- Predicting system behavior: By simulating different vehicle behaviors and traffic
scenarios, you can predict how the system will respond under different conditions. This
can help in identifying potential bottlenecks or performance issues before they occur in
a real-world scenario.
- Scalability testing: Connected mobility platforms need to handle a large number
of vehicles, especially in urban environments. Using a simulation tool, you can
artificially increase the number of vehicles to test the system's scalability.
- Real-time data processing: Many connected vehicle applications require real-time
data processing, such as collision avoidance or traffic rerouting. By simulating these
scenarios, you can ensure that the system can handle real-time data processing
efficiently.
- Network load testing: Connected vehicles will continuously send and receive data.
Simulating this can help in understanding the network load and ensuring that the
infrastructure can handle it.
- Understanding edge cases: While typical scenarios are essential, it's also
crucial to understand how the system behaves under edge cases. For instance, what
happens if a large number of vehicles suddenly go offline? Or if there's a sudden surge
in data transmission?
- Improving SLAs: By understanding the system's behavior
under various scenarios, you can set more accurate Service
Level Agreements (SLAs) and ensure that they are met.
- Cost optimization: Running simulations can also help in understanding the cost
implications. For instance, if you're using cloud services, understanding the data
transmission rates can help in predicting costs and optimizing them.

**[CMPERF_BP7.2] Build your vehicle simulation tool to be compatible
with AWS**

When selecting a vehicle simulation tool, ensure its compatible with AWS, or consider
building a custom simulation environment that uses the full power of AWS services.

Whatever your choice, AWS provides a robust suite of tools and services that can be
harnessed to understand and optimize the performance metrics of the connected mobility
platform under various simulated load scenarios.

CMPERF_8: Have you considered an edge inference simulation solution to
continuously test infer or predict based on the past data?

Edge inference is a crucial concept, especially for applications where real-time data processing is essential, such as autonomous vehicles, industrial IoT, and smart cities. By running inference at the edge (closer to where data is generated), you can reduce latency, save bandwidth, and respond quickly to local changes. Continuously testing the ability of edge devices to infer or predict based on past data is essential to maintain system reliability and performance.

**[CMPERF_BP8.1] Edge inference and simulation play a pivotal role in
the realm of connected mobility platforms**

This is especially important when focusing on performance efficiency. Edge computing allows
data processing to occur closer to the data source, such as a vehicle, rather than sending
it to a centralized cloud server. This approach can significantly enhance the performance
and responsiveness of the system.

- Latency reduction: One of the primary benefits of edge inference is the drastic
reduction in latency. By processing data on the edge (for example, onboard a vehicle or
a nearby edge server), the need to transmit data to a central server and wait for a
response is eliminated. This is crucial for real-time applications like autonomous
driving or collision avoidance.
- Bandwidth efficiency: Transmitting large volumes of raw data from vehicles to
central servers can be bandwidth-intensive. Edge inference allows for initial processing
and filtering of data, sending only essential information to the central server, thus
saving bandwidth.
- Continuous testing and learning: An edge inference simulation solution can
continuously test and adapt based on past data. This iterative process can help in
refining algorithms and improving prediction accuracy over time.
- Real-world scenarios: Edge simulation tools can recreate real-world driving
scenarios, allowing the system to test and infer based on historical data. This can be
invaluable in understanding how the system would react in specific situations.
- Data privacy and regulatory compliance: Processing data on the edge can also
address data privacy concerns. By analyzing and making decisions locally, sensitive data
might not need to be transmitted or stored centrally, aiding in compliance with data
protection regulations.
- Scalability: As the number of connected vehicles grows,
central servers might become overwhelmed with data. Edge
computing distributes the processing load, ensuring that
the system remains scalable.
- Resilience and reliability: Edge inference provides a decentralized approach,
ensuring that even if there's a failure in one part of the system, other parts can
continue to operate independently.
- Integration with other systems: Edge devices can integrate with other local
systems, such as traffic light controllers or local weather stations, to make more
informed decisions.

**[CMPERF_BP8.2] Your edge inference simulation solution should
provide a versatile approach to address many variables.**

When considering an edge inference simulation solution for a connected mobility
platform, it's essential to select a solution that can:

- Simulate various real-world scenarios.
- Continuously learn and adapt based on past data.
- Integrate seamlessly with the vehicle's onboard systems
and other edge devices.
- Ensure data security and privacy.
- Simulate the expected volume and variety of data at the
edge.
- Test the machine learning models' accuracy and speed under
various conditions.
- Measure the latency and reliability of communication
between edge devices and the central cloud or data
centers.

In conclusion, edge inference simulation is a forward-thinking approach that can
significantly enhance the performance efficiency of a connected mobility platform. It allows
for real-time processing, continuous learning, and adaptation, ensuring that the platform
remains responsive, accurate, and efficient.

CMPERF_9: Have you identified an appropriate communication protocol based on
use case?

**[CMPERF_BP9.1] For vehicle-cloud communications, different
protocols must address your specific use case.**

- Pub-Sub protocols such as MQTT and AMQP can be used to exchange telemetry
messages, command-control functions.
- HTTP or gRPC based protocol can be used to deliver over the air (OTA) updates.
- WebRTC protocol (RTMP) can be used to deliver video stream with real-time
latency.
- SMS can be used for device wake-up, and run simple commands.
The appropriate communication protocol often depends on the specific requirements of the use case. Here's a brief overview of common communication protocols and the typical use cases they serve:
- HTTP/HTTPS:

Use cases: Web applications, mobile applications, and many modern
internet-based applications.
- Advantages: Well-known, widely used, and supported.
Secure version (HTTPS) available.

- MQTT (Message Queuing Telemetry Transport):

Use cases: Internet of Things (IoT) devices, real-time analytics, mobile
applications, and communication in unreliable networks.
- Advantages: Lightweight protocol with low bandwidth
requirements. Supports QoS (Quality of Service)
levels.

- WebSocket:

Use cases: Real-time web applications, gaming, chat applications, live sports
updates.
- Advantages: Provides full-duplex communication
channels over a single TCP connection. More efficient
than repeatedly opening new HTTP connections.

- AMQP (Advanced Message Queuing Protocol):

Use cases: Message-oriented middleware, cloud services, and brokered
messaging.
- Advantages: Supports message orientation, queuing, and
routing.

- Payload efficiency

For optimal payload efficiency in a Connected Vehicle
Platform, adopt compact data formats like Google
Protocol Buffers (GPB) or MessagePack, which provide
efficient serialization.
- Send only changed or relevant data, employing
compression algorithms like gzip for textual data, and
utilizing delta encoding can minimize the data's size.

- Consider the trade-offs between data freshness and
bandwidth utilization, tailoring strategies to the
specific application's needs.

Note
Refer to [Resources](./resources-perf.html) for links to
the mentioned protocols

**[CMPERF_BP9.2] Choose a protocol based on the factors that apply
to your use case**

When choosing a communication protocol, it's important to assess the specific needs of
the use case and test the chosen protocol in realistic scenarios to ensure it meets the
requirements.

The choice of protocol will typically depend on:

- Data volume and frequency.
- Power and bandwidth constraints.
- Required communication range.
- Latency and real-time requirements.
- Security and privacy needs.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/connected-mobility-lens/selection.html*

---

# Review

CMPERF_10: Have you considered the implementation of scalable, cost-effective,
and low-maintenance managed services for high-performance computing workloads to
process diverse data types (such as high and low fidelity data, logs, and commands)
collected from vehicles?

**[CMPERF_BP10.1] Build a cost-effective solution that is scalable
and yet easy to manage as more vehicles connect to the cloud.**

We need to think about use cases that are critical in order to bring a good user
experience to end consumers. For example, vehicle state services play a key role for
consumers to know the state of vehicle, for example, door locked, or window down. In this
case, data caching solutions (Redis Cache or MemoryDB) are important to quickly access last
available data with low latency (200 milliseconds or less) interval. Any new data will move
classify earlier as historical data, this can be stored in either No SQL database such as
DynamoDB or data lake for further processing. Training can be done to improve machine learning
models and later it can be deployed for prediction based on the type of use case (for
example, recommend cabin temperature based on historical data in vehicle)

Recommendation - Telemetry data strategy

- Top 50 Properties – In memory cache (open standard numbers)
- Next 500 Properties – Microsecond interval
- 5000+ Properties – Seconds or higher interval

CMPERF_11: Have you tested the ability of your platform to seamlessly adopt,
replace, or upgrade various compute solutions, including standalone systems,
container-based architectures, and serverless technologies?

Ensuring that your platform can seamlessly adopt, replace, or
upgrade various compute solutions is crucial for scalability,
adaptability, and resilience.

When considering AWS services, here's how you can ensure flexibility across
different compute solutions:

**[CMPERF_BP11.1] Self-managed systems (Amazon EC2)**

- Compute: Virtual servers in the cloud where you can run
applications.
- Load balancing: Distributes incoming application traffic across multiple targets,
such as EC2 instances.
- Auto scaling: Ensures that you have the right number of EC2 instances available
to handle the load for your application.
- Seamless adoption and upgrades: Use Amazon Machine Images (AMIs) to create and
save configurations, making it easier to scale, replace, or upgrade.

**[CMREF_BP11.2] Container-based architectures**

- Containerization: A highly scalable, high-performance
container orchestration service that supports Docker
containers.

Serverless compute for containers. You don't need to
provision, configure, or scale clusters of virtual
machines to run containers.

- Seamless adoption and upgrades: Use container orchestration to manage the
lifecycle of containers, ensuring that services can be updated or rolled back without
downtime.

**[CMPERF_BP11.3] Serverless technologies**

- Run code without provisioning or managing servers. You pay
only for the compute time that you consume.
- API Gateway: For creating, deploying, and managing APIs
along with serverless function to create serverless
applications.
- Seamless adoption and upgrades: With serverless, deployments can be versioned,
allowing for easy rollbacks.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/connected-mobility-lens/review.html*

---

# Monitoring

CMPERF_12: Have you implemented end-to-end monitoring and logging (between
edge, vehicle, and cloud) of your system along with notifications?

**[CMPERF_BP12.1] Monitoring, logging, and setting up notifications
are critical for maintaining the health, performance, and security of a system.**

AWS offers a comprehensive suite of tools to help with these tasks:

- Ensure that all services, applications, and resources report their metrics and
logs.
- Regularly review and adjust your monitoring strategy to adapt to changes in your
environment and application.
- Ensure that you're not just collecting data but also deriving actionable insights
from it.

**[CMPERF_BP12.2] Implement device monitoring at the edge device
(vehicle), data transmission monitoring, monitor cloud services, and log monitoring.**

As a general practice, establish alerts to monitor different workloads, applications,
database services, load balancers, and network monitoring. Notify site reliability
engineering (SRE) team once a certain threshold level is breached. These actions will help
to define KPIs such as round-trip time, and network latency between vehicle-cloud and
internal applications.

CMPERF_13: Have you built the right dashboards and widgets for your prioritized
actionable insights?

Building an effective dashboard involves focusing on the key
performance indicators (KPIs) that matter most to your
organization and displaying them in an easily understandable
and visually appealing way.

**[CMPERF_BP13.1] Follow best practices when creating
dashboards**

User-centric design:

- Tailor the dashboard to the needs of its primary users.
Consider who will be using the dashboard and why.
- Use a clear, organized layout and meaningful naming
conventions.

Prioritize key metrics:

- Show the most important data points prominently, ensuring
they are easily accessible and visible.
- Avoid cluttering the dashboard with non-essential metrics.

Use appropriate visualizations:

- Choose the right type of graph or visualization based on
the nature of the data. For instance, time-series data is
best viewed with line charts.

Interactive elements:

- Add interactive filters, drill-down capabilities, or
time-span selectors to allow users to explore the data
more deeply.

Consistent refresh rates:

- Determine how frequently the dashboard needs updating.
Some metrics might require real-time updates, while others
might be daily or weekly.

Alerting:

- Integrate alert mechanisms, using services like Amazon SNS, to notify stakeholders of important events or
thresholds.

Feedback loop:

- Regularly gather feedback from users and iterate on the
dashboard design and widgets.

Tools such as dashboards, container insights, serverless insights, along with
external tools such as Datadog can be used to build custom dashboards that can provide
better insights. When you are running applications in containers or using serverless
architectures, visibility into your workloads becomes paramount for optimizing performance,
troubleshooting issues, and ensuring security.

**[CMPERF_BP13.2] Use tools and best practices to gain
insights**

- End-to-end visibility: Ensure that you're tracking the complete lifecycle of a
request or a transaction across all components of your application.
- Alerts and alarms: Set up meaningful alerts and alarms based on the metrics and
traces collected.
- Anomaly detection: Anomaly detection to create alarms that watch for anomalies in
your metrics.
- Regularly review metrics and logs: Periodically review the metrics and logs, even
if there's no issue, to understand the standard behavior of your applications.
- Security: Always monitor for security threats, especially
in serverless applications where the application's
perimeter might not be as defined.
- Cost optimization: Especially for serverless architectures, where you're billed
for what you use, monitoring can also help in understanding the cost patterns and
optimize.

Remember, while AWS provides the tools to monitor and gain
insights, it's the combination of these tools with best
practices that will give you the most valuable insights into
your container and serverless environments.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/connected-mobility-lens/monitoring.html*

---

# Tradeoffs

CMPERF_14: What criteria have you identified where tradeoffs can be
made?

**[CMPERF_BP14.1] Develop criteria where trade-offs can be made
based on the type of functionality.**

For example, infotainment functionality brings higher customer satisfaction where
certain tradeoffs are acceptable (for example, retry actions are configurable to avoid
draining battery). But when it comes to vehicle safety critical OTA updates are not
inhibited by tradeoffs. Additional criteria can be applied:

- Ensure data collection concerning predictive maintenance are not being hindered
- Develop a revision process on actionable insights received from monitoring

**[CMPERF_BP14.2] Architecture design and
trade-offs**

The following options have benefits which bring scalability, higher performance, faster
response but the tradeoff is cost. With volume of vehicles that connect to a connected
vehicle platform increases the cost to maintain them is critical in the long run. In
addition, the amount of data that gets offloaded from vehicle continues to grow.

- Self-managed option
- AWS Managed Service option
- Serverless option

It is critical to identify and categorize the functions, vehicle signals and states,
software updates that are needed to support the connected vehicle platform by processing and
storing them.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/connected-mobility-lens/tradeoffs.html*

---

# Key AWS services

- [AWS Lambda](https://aws.amazon.com/lambda/?nc2=type_a) - serverless provides scalable processing
- [AWS IoT Core](https://aws.amazon.com/iot-core/) - Connect, manage, and scale your edge device
fleets easily and reliably without provisioning or managing
servers.
- [Amazon Data Firehose](https://aws.amazon.com/kinesis/data-firehose/)
- [Amazon CloudWatch](https://aws.amazon.com/pm/cloudwatch/?trk=2dfe7cfe-88b0-4c42-844b-24167b0dc800&sc_channel=ps&ef_id=Cj0KCQjwvL-oBhCxARIsAHkOiu3Fzt_AD3visGTXImdauzHLsK5vC1v16Jzo9FQBFJmrN30r7GgN0tIaAuYEEALw_wcB:G:s&s_kwcid=AL!4422!3!658520966135!!!g!!!19852661915!149878722660)
- [AWS Systems Manager](https://aws.amazon.com/systems-manager/)
- [Amazon Elastic Kubernetes Service](https://aws.amazon.com/eks/)
- [Amazon DynamoDB](https://aws.amazon.com/dynamodb/)
- [Amazon
Elastic Load Balancing](https://aws.amazon.com/elasticloadbalancing/)
- [AWS IoT FleetWise](https://aws.amazon.com/iot-fleetwise/)
- [Amazon Managed Streaming for Apache Kafka (Amazon MSK)](https://aws.amazon.com/msk/)

In summary, AWS provides a comprehensive suite of services that can be tailored to
the specific needs of a connected mobility platform. It's essential to continuously evaluate
and adapt the architecture based on real-world performance data and changing requirements.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/connected-mobility-lens/key-aws-services-perf.html*

---

# Resources

**Documentation and blogs:**

- [AWS Connected Vehicle Reference Architecture](https://docs.aws.amazon.com/architecture-diagrams/latest/aws-connected-vehicle/aws-connected-vehicle.html)
- [Device
Communication Protocols](https://docs.aws.amazon.com/iot/latest/developerguide/protocols.html)
- [gRPC
Framework](https://grpc.io/)
- [WebSocket
Protocol](https://datatracker.ietf.org/doc/html/rfc6455)
- [AWS IoT Core](https://aws.amazon.com/iot-core/)
- [AWS IoT FleetWise](https://aws.amazon.com/iot-fleetwise/)

**Whitepapers:**

- [Designing
Next Generation Vehicle Communication with AWS IoT Core
and MQTT](https://docs.aws.amazon.com/whitepapers/latest/designing-next-generation-vehicle-communication-aws-iot/designing-next-generation-vehicle-communication-aws-iot.html)

**AWS Partner solutions:**

- [Commoditize
connected mobility with WirelessCar on AWS](https://aws.amazon.com/solutions/case-studies/wirelesscar-case-study/)

**Training Materials:**

- [Building
Connected Vehicle platforms with AWS IoT](https://pages.awscloud.com/GLOBAL-other-DL-Connected-vehicle-ebook-2023-learn.html)

**Videos:**

- [Building
Connected Vehicle and Mobility Platforms with
AWS](https://www.youtube.com/watch?v=Oaw_cpLBpoI&themeRefresh=1)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/connected-mobility-lens/resources-perf.html*

---
