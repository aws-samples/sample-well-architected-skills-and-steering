# TELCOREL02 — Workload architecture

**Pillar**: Reliability  
**Best Practices**: 5

---

# TELCOREL02-BP01 Deploy user plane functions in a distributed architecture and highly available configuration

Follow a distributed architecture approach to deploy user plane nodes across multiple
geographical locations with built-in redundancy. Such a design maintains service continuity
through redundant instances and geographical distribution, minimizing the impact of localized
failures or outages while optimizing network performance through efficient load distribution.

**Desired outcome:**

- Achieve high availability on critical network functions.
- Minimized impact from localized failures.
- Optimized network performance.
- Reduced exposure to regional outages.

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

Implement a distributed and redundant architecture for the user plane functions that can
withstand regional service degradations or outages. This involves deploying redundant
instances of user plane network functions across multiple geographical locations. Within each
site, utilize strategies such as active-active or active-standby configurations, automated
health monitoring, and failover strategy. Comprehensive monitoring and data visualization
tools provide visibility into the network's performance and availability, enabling
rapid identification and response to potential issues. Geographical distribution of these
functions, based on user demands and regulatory requirements enhance the resilience and
responsiveness of the telecom infrastructure by reducing exposure in case of failure.
Automating failover mechanisms, with thresholds and triggers defined by the network management
systems, verifies that the network can quickly recover from failures without disrupting
service to end users.

### Implementation steps

- Deploy redundant instances across multiple Availability Zones:

Deploy your 5G network architecture across multiple AWS Regions, Availability
Zones, and Outposts where possible.
- Use AWS Auto Scaling and Amazon CloudWatch to monitor and scale your network function
instances based on real-time and projected traffic patterns.

- Implement redundancy patterns:

Deploy your user plane functions as Auto Scaling groups with Amazon EC2 instances in
an active-active or active-standby configuration.
- Use Amazon CloudWatch for automated instance health monitoring and failover.

- Establish monitoring:

Deploy Amazon CloudWatch to capture and analyze performance and availability metrics
across your distributed instances.

- Implement geographical distribution:

Choose AWS Regions and Availability Zones based on user distribution,
regulatory requirements, and disaster recovery needs.
- Evaluate AWS network connectivity options, such as AWS Direct Connect and Site-to-Site VPN,
to optimize inter-region communication.

- Configure automatic failover:

Use Amazon CloudWatch alarms and metrics to define infrastructure and application-level
thresholds for initiating automated failover.
- Integrate with your 5G network management systems to correlate failures and
trigger appropriate responses.

## Resources

**Key AWS services:**

- [Amazon EKS](https://aws.amazon.com/pm/eks/)
- [Amazon ECS](https://aws.amazon.com/ecs/)
- [AWS Auto Scaling](https://aws.amazon.com/autoscaling/)
- [AWS Local
Zones](https://aws.amazon.com/about-aws/global-infrastructure/localzones/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/telco-lens/telcorel02-bp01.html*

---

# TELCOREL02-BP02 Implement full mesh between control plane and user plane functions

Implement a resilient architecture design where each control plane node can manage user
plane functions in a mesh configuration. For each user plane function, one control plane node
will be active at a time. The control plane node should be designed to have enough capacity to
control the user plane nodes, when needed. This verifies that if one or multiple control plane
nodes fail, the remaining nodes can manage user plane functions without service interruption.
The design incorporates high-capacity centralized control components with distributed user plane
functions.

**Desired outcome:**

- Enhanced system resilience through redundant connectivity.
- Remove single points of failure in control plane.
- Seamless failover during node failures.
- Maintained service continuity.

**Level of risk exposed if this best practice is not established:**
Low

## Implementation guidance

A full mesh connectivity design between the control plane and user plane components is
recommended for a highly available Telcom network. Implementing diverse routing paths and
continuously monitoring the status of these connectivity routes are key steps. Defining clear
failover triggers and thresholds, along with automated recovery procedures, allows the network
to quickly respond to and recover from failures. Thorough documentation of these processes,
including integration with incident management and troubleshooting guides, further enhances
the reliability of the overall system. Comprehensive monitoring and observability solutions
provide the necessary visibility into the network's performance and health, enabling proactive
identification and mitigation of potential issues.

### Implementation steps

- Design mesh topology:

Use AWS Transit Gateway to enable connectivity between your control and user plane
network functions in a star topology, enabling each control plane node to be able to
manage the user plane node, when needed.
- Verify capacity planning and failure domain considerations using Amazon CloudWatch and
AWS Auto Scaling.

- Implement connectivity paths:

Deploy control plane and user plane instances across multiple AWS
Availability Zones and Regions where possible.
- Configure diverse routing paths using AWS VPC routing tables and AWS Transit Gateway
routing policies.
- Leverage AWS Direct Connect for physical path separation and high-performance
connectivity with the on-premises systems including Access Network (RAN) functions.

- Configure routing policies:

Implement routing policies using AWS Transit Gateway route tables and AWS Lambda-based
custom routing logic to recover services in case of a control plane node failure.

- Define failover triggers:

Use Amazon CloudWatch alarms and metrics to define the conditions and thresholds for
triggering automated failover processes.
- Provide manual override capabilities through AWS Lambda functions or Amazon API Gateway.

- Document procedures:

Store the detailed failover and recovery procedures in AWS Systems Manager for secure
access and versioning.
- Integrate the documentation with your incident management processes and provide
troubleshooting guides and escalation procedures.

## Resources

**Key AWS services:**

- [AWS Transit Gateway](https://aws.amazon.com/transit-gateway/)
- [Amazon VPC](https://aws.amazon.com/vpc/)
- [AWS Lambda](https://aws.amazon.com/lambda/)
- [AWS Direct Connect](https://aws.amazon.com/directconnect/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/telco-lens/telcorel02-bp02.html*

---

# TELCOREL02-BP03 Implement a flexible network function (NF) design to leverage available infrastructure resources for autoscaling

Designing a flexible network function design enables the telecom network to dynamically
scale its resources based on the availability of suitable instance types in the deployment
region. This approach avoids issues like `Insufficient Capacity Error` that can occur when
the required instance type is not available, by using alternative instance types that
can be provisioned. The architecture should be able to automatically adapt to the most
suitable instance types that are present, allowing the network to scale up or down as needed
without being constrained by the availability of a specific instance configuration.

**Desired outcome:**

- Improving the probability of a successful on-demand scale-out in case of traffic surge
or failover trigger.
- Network functions can scale seamlessly by utilizing the most suitable instance types
that are available in the deployment region.
- Remove the risk of scaling failures due to `Insufficient Capacity Error` when
the preferred instance type is not available.
- Verifies continued service availability and responsiveness by maintaining the ability
to scale the network functions as needed.

**Level of risk exposed if this best practice is not established:**
Medium

## Implementation guidance

To build a flexible and scalable telecom network architecture, a modular and
containerized approach to network functions is recommended. This involves decomposing network
functions into independently scalable components, packaged as container images, and
orchestrating them on a Kubernetes-based solution. Dynamic scaling and efficient resource
utilization are enabled using a Kubernetes cluster autoscaler, which provisions appropriate
instance types based on component requirements. Flexible scaling policies, comprehensive
monitoring, failover mechanisms, and thorough documentation verify the network can adapt to
changing demands, optimize resource utilization, and maintain overall resilience and
reliability.

### Implementation steps

- Design a modular and containerized network function architecture:

Use a microservices-based approach to decompose network functions into smaller,
independently scalable components.
- Package each network function component as a container image to enable
flexibility in deployment and scaling.

- Implement Kubernetes-based orchestration for network functions:

Deploy the network function components on Amazon EKS.
- Integrate the Karpenter open-source Kubernetes cluster autoscaler with your EKS
cluster.
- Configure Karpenter to automatically provision the appropriate instance types
based on the resource requirements of the network function components.

- Monitor resource utilization and scaling events:

Use Amazon CloudWatch to monitor the performance and resource utilization of the network
function components.
- Analyze scaling events, instance provisioning, and capacity fluctuations to
optimize the scaling policies and Karpenter configurations.

- Implement failover and self-healing mechanisms:

Configure Kubernetes health checks and readiness probes to detect and replace
unhealthy network function instances.

- Document scaling procedures and best practices:

Maintain comprehensive documentation on the flexible network function
architecture, scaling policies, and Karpenter configuration.
- Establish guidelines for updating the scaling policies and Karpenter
configurations as the instance type availability changes over time.

## Resources

**Key AWS services:**

- [Amazon EKS (Elastic Kubernetes Service)](https://aws.amazon.com/pm/eks/)
- [Karpenter
(open-source Kubernetes cluster autoscaler)](https://docs.aws.amazon.com/eks/latest/userguide/autoscaling.html)
- [Amazon CloudWatch for monitoring and
observability](https://aws.amazon.com/cloudwatch/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/telco-lens/telcorel02-bp03.html*

---

# TELCOREL02-BP04 Introduce an SCTP load balancer designed for control-plane network functions, carrier-grade performance, and high availability

The major public cloud services providers lack native support for load balancing of the
Telecom services that rely on control-plane signaling protocols like SCTP (Stream Control
Transmission Protocol). It is recommended to introduce a cloud-based SCTP Load Balancer for
control plane network functions, designed specifically for telco workloads in the public cloud.
Such a solution will provide SCTP protocol awareness, including support for multi-homing and
association management, along with carrier-grade performance. The load balancer should also
deliver high availability through failover and health checks, maintaining reliable and scalable
operation of critical telecommunications components deployed in the public cloud.

**Desired outcome:**

- Provide a cloud-based SCTP load balancing solution specifically designed for telco
control plane workloads.
- Offer built-in support for the SCTP protocol in the network functions, including
features like multi-homing, stream multiplexing, and association management.
- Verify high availability through redundancy, failover capabilities, and health
monitoring.

**Level of risk exposed if this best practice is not established:**
High

## Implementation guidance

To enhance the reliability of telecom networks, an SCTP load balancing solution should be
onboarded and deployed. This load balancer should incorporate SCTP-specific features, verify
high throughput and low latency, and be implemented with high availability and fault tolerance
through redundant deployments and automated failover. Integrate the load balancer with
Kubernetes-based network functions, optimize for carrier-grade performance, and implement
comprehensive monitoring and automation practices to deliver a reliable and responsive telecom
infrastructure.

### Implementation steps

- Select an SCTP load balancer:

Research and evaluate available SCTP load balancer solutions that offer the
required features, such as multi-homing, stream management, and association
tracking. Verify the selected product can scale to handle the throughput and latency
requirements of telco control plane workloads.

- Implement high availability and fault tolerance:

Deploy the SCTP load balancer across multiple AWS Availability Zones for
redundancy.
- Configure health checks and automated failover mechanisms to verify continuous
service availability.
- Use AWS Auto Scaling to dynamically scale the load balancer instances based on
traffic patterns.

- Optimize for carrier-grade performance:

Configure the SCTP load balancer to optimize for the specific requirements of
telco control plane workloads.

- Implement comprehensive monitoring and observability:

Use Amazon CloudWatch to monitor the SCTP load balancer's performance, availability,
and error metrics.
- Configure Amazon CloudWatch alarms and Amazon SNS notifications for proactive alerting and
incident management.

## Resources

**Key AWS services:**

- [AWS Auto Scaling](https://aws.amazon.com/autoscaling/)
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
- [Amazon SNS](https://aws.amazon.com/sns/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/telco-lens/telcorel02-bp04.html*

---

# TELCOREL02-BP05 Optimize failure recovery timers for the shared tenancy and potential for transient network issues in cloud environments

Many telecom network function vendors implement health monitoring thresholds based on
on-premises architectural assumptions, where redundant network interfaces and multiple physical
network paths may exist between components. However, when these telecom network functions are
deployed in cloud environments, the underlying network is a shared resource with a single
connection. This can lead to frequent connection alarms and service disruptions due to transient
network issues or single point of failure events, even though the network function itself may
remain functional. It is recommended to proactively engage with telecom ISVs and Network
Function developers to optimize the timers and behaviors used for health monitoring and failure
recovery. This includes designing network architecture to be resilient to packet losses or
higher latencies over the underlying network.

**Desired outcome:**

- Verify the network functions can effectively detect, react, and recover from network
issues and failures.
- Optimize the health monitoring and failure recovery timers to strike the right balance
between prompt failure detection and resilience against false positives.
- Use cloud capabilities to supplement vendor-provided failure detection and
recovery mechanisms.
- Maintain high availability and service continuity for critical telco network functions
despite the dynamic and shared nature of the cloud infrastructure.

**Level of risk exposed if this best practice is not established:**
Medium

## Implementation guidance

Work closely with network function vendors to optimize health monitoring and failure
recovery mechanisms for cloud-based deployments. Implement multi-layered monitoring,
dynamically adjust failure detection timers, and integrate vendor-provided recovery procedures
with cloud-based automation. Validate and test the failure recovery processes, then
continuously monitor performance and collaborate with vendors to further refine the
configurations over time.

### Implementation steps

- Collaborate with network function vendors:

Engage with the network function vendors to understand their default health
monitoring and failure recovery mechanisms.
- Work with the vendors to customize and optimize the monitoring and recovery
timers based on the cloud solutions and NF failure modes.

- Implement multi-layered health monitoring:

Leverage Amazon CloudWatch to set up comprehensive monitoring of the network function
instances, including resource utilization, network performance, and
application-level metrics.
- Configure Amazon CloudWatch alarms to detect anomalies and potential failure conditions,
with customized thresholds and rules.
- Implement AWS Lambda-based health check functions to perform more advanced
application-level checks, accounting for the specific requirements of the telco
network functions.

- Optimize failure detection timers:

Work with the network function vendors to fine-tune the health check intervals,
failure detection thresholds, and recovery timeouts.
- Balance the need for prompt failure detection with resilience against transient
issues that can trigger false positives.
- Use Amazon CloudWatch and AWS Lambda to implement dynamic timer adjustments based on
observed patterns and cloud infrastructure conditions.

- Enhance failure recovery mechanisms:

Integrate the network function vendor-provided recovery procedures with
AWS-native capabilities, such as Amazon EC2 Auto Scaling, Amazon EKS, and AWS Lambda.
- Develop automated recovery workflows using AWS Step Functions or AWS Lambda to handle
different types of failures and verify consistent, reliable recovery.
- Implement rollback and self-healing mechanisms to verify that the network
functions can recover to a known good state.

- Validate and test the failure recovery:

Use AWS Fault Injection Service to inject various types of failures and network issues into
the environment.
- Monitor the health monitoring and failure recovery mechanisms, and fine-tune
the timers and thresholds based on the observed behavior.
- Document the optimized health monitoring and recovery configurations, including
vendor-specific customizations.

## Resources

**Key AWS services:**

- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
- [AWS Lambda](https://aws.amazon.com/lambda/)
- [AWS Step Functions](https://aws.amazon.com/step-functions/)
- [AWS Auto Scaling](https://aws.amazon.com/autoscaling/)
- [Amazon EKS](https://aws.amazon.com/pm/eks/)
- [AWS Fault Injection Service](https://aws.amazon.com/fis/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/telco-lens/telcorel02-bp05.html*

---
