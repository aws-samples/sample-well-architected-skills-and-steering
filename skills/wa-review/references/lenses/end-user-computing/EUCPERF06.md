# EUCPERF06 — Networking and content delivery

**Pillar**: Performance Efficiency  
**Best Practices**: 3

---

# EUCPERF06-BP01 Minimize latency between end users and EUC services

Like many other vendors, AWS EUC solutions deliver their services using a remote
display protocol to stream the pixel information to the endpoint device, which is highly
efficient and capable of tolerating a variety of network conditions. Low latency, low packet
loss, and jitter are key to delivering the best service for end users.

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

Minimize latency between end user devices (like desktops, laptops, and thin clients)
and the AWS EUC service endpoints by avoiding proxies, inspection appliances, and VPNs.

Determine whether there are any conditions which might introduce latency between your
end users and the AWS EUC service endpoints. Test connectivity under various conditions
to identify the maximum latency that can be tolerated by the application set being
deployed, and verify that your network can scale to reliably deliver the number of users
being deployed.

If end users will be working from home, try to establish a minimum level of network
connectivity that should provide a good user experience. Most home broadband connections
are more than capable of delivering low latency for home working, but problems with home
networks can be difficult to diagnose.

Verify that endpoint devices can run the local client application (WorkSpaces or AppStream
Client) that processes and displays the encrypted pixel stream which flows between the end
user and the AWS EUC service connection points (streaming gateways). If the workload
delivers collaboration tools such as Microsoft TEAMs, Zoom, or Webex, optimization
capabilities will try to offload processing to the local endpoint device, which must be
capable of handling this additional load.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucperf06-bp01.html*

---

# EUCPERF06-BP02 Minimize latency between EUC instances and dependent services

In most cases, EUC users require connections to resources outside their EUC instances.
Common dependencies include web or application servers, database servers, and storage
services.

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

When possible, deploy these dependencies in the same AWS Region and ideally the same
Availability Zone. If the system of record must reside elsewhere, consider deploying
caches or replicas. For example, if your Active Directory domain controllers are on your
on-premises network, deploy replicas on Amazon EC2.

When connecting to Amazon S3, use gateway VPC endpoints. For more information on
configuring gateway endpoints, see [Gateway endpoints for
Amazon S3](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-s3.html).

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucperf06-bp02.html*

---

# EUCPERF06-BP03 Make sure that EUC network configurations don't interfere with service management connections

WorkSpaces Applications instances use a dedicated management network interface (eth0) for
streaming and service management connections.

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

Do not configure applications or the operating system to interfere with the
connections listed in [Amazon WorkSpaces Applications Connections to Your VPC](https://docs.aws.amazon.com/appstream2/latest/developerguide/appstream2-port-requirements-appstream2.html#management_ports). If private network connectivity
from WorkSpaces Applications instances to resources outside your VPC is required, use a VPC-level
solution such as AWS Site-to-Site VPN or AWS Transit Gateway. Do not use a client VPN on the WorkSpaces Applications
instance, as this is complex and error-prone to configure properly.

WorkSpaces instances use a dedicated management network interface (eth0) for streaming and
service management connections.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucperf06-bp03.html*

---
