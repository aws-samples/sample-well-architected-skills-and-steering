# LSPERF12 — Network and content delivery

**Pillar**: Performance Efficiency  
**Best Practices**: 3

---

# LSPERF12-BP01 Implement network segmentation with defense-in-depth controls

Design the network with clearly defined security zones separated by
firewalls, with sensitive data repositories isolated from general
network traffic. Employ a layered security approach (defense in
depth) with multiple security controls at each boundary. Use VLANs,
subnets, and micro-segmentation to isolate data flows based on
security levels and functional requirements. This architecture
limits potential attack surface and contains breaches should they
occur while maintaining efficient routing paths for authorized large
data transfers.

**Desired outcome:** You have a
segmented network architecture that provides multiple layers of
security controls, supports regulatory requirements, and enables
secure collaboration across research teams. This approach protects
sensitive life sciences data while maintaining operational
efficiency and regulatory alignment.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Network segmentation is fundamental for life sciences
organizations handling sensitive data like clinical trials,
genomic data, or patient information. By implementing multiple
security layers, you create isolation between different data
sensitivity levels and reduce the potential attack surface.

This approach aligns with key regulatory requirements including
HIPAA, GxP, and GDPR. Segmentation enables clear audit boundaries
and demonstrates regulatory adherence by maintaining separate
environments for development, validation, and production systems.

Defense in depth controls allow for granular access management and
simplified auditing. This architecture supports the isolation of
regulated workloads while enabling secure collaboration between
research teams, clinical partners, and third-party vendors.

### Implementation steps

- Create separate VPCs for production, development, and test
environments with tiered subnets.
- Deploy AWS Transit Gateway for centralized connectivity
between environments.
- Implement AWS Network Firewall and AWS PrivateLink for
secure service access.
- Configure security groups and Network ACLs following
least-privilege principles.
- Deploy AWS WAF and AWS Shield for application security and
DDoS protection.
- Enable VPC Flow Logs and AWS GuardDuty for comprehensive
security monitoring.
- Establish AWS Security Hub CSPM for centralized audit and
security posture management.
- Configure AWS Site-to-Site VPN for secure remote
connectivity to on-premises resources.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsperf12-bp01.html*

---

# LSPERF12-BP02 Deploy accelerated encryption technologies with hardware offloading

Implement high-performance encryption solutions that don't
compromise throughput when securing large datasets in transit. Use
hardware-accelerated encryption (specialized NICs, encryption
accelerator cards) and efficient protocols like TLS 1.3 with
optimized cipher suites. Consider authenticated encryption with
associated data (AEAD) ciphers for simultaneous confidentiality and
integrity validation. For extremely large datasets, evaluate
selective encryption approaches that prioritize sensitive components
while optimizing overall transfer speeds.

**Desired outcome:** You have a
hardware-accelerated encryption system that provides data security
while maintaining high performance for life sciences workflows. This
enables efficient processing of sensitive research data with
automated scaling, regulatory adherence, and consistent performance
during peak workloads.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Hardware-accelerated encryption is critical for life sciences
workflows involving large-scale data processing, such as genomic
sequencing or medical imaging. This approach improves security
without creating bottlenecks in research pipelines.

Encryption technologies must meet specific regulatory standards
for data protection while supporting high-throughput operations.
Hardware offloading enables consistent performance for encrypted
data transfers while maintaining regulatory adherence.

The solution scales automatically with workload demands, providing
consistent performance during peak processing periods such as
batch analysis or multi-site clinical trials. This maintains
security without compromising research timelines.

### Implementation steps

- Deploy EC2 instances with NVIDIA T4 or AWS Inferentia chips
for hardware-accelerated encryption.
- Configure TLS 1.3 with AES-GCM cipher suites and AWS CloudHSM for key management.
- Implement AWS Nitro Enclaves for instance-level encryption
offloading.
- Enable AWS Global Accelerator for optimized encrypted data
routing.
- Set up AWS Certificate Manager for automated TLS certificate
lifecycle management.
- Configure enhanced networking with Elastic Network Adapters
for encryption performance.
- Establish Amazon CloudWatch dashboards to monitor encryption
performance metrics.
- Implement automated key rotation and comprehensive
encryption audit logging.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsperf12-bp02.html*

---

# LSPERF12-BP03 Optimize data transfer with intelligent traffic management and compression

Implement quality of service (QoS) mechanisms to prioritize critical
data transfers while avoiding bandwidth saturation. Deploy WAN
optimizers and SD-WAN solutions that can intelligently route traffic
across multiple paths based on real-time conditions. Use lossless
compression algorithms appropriate to your data types before
transmission to reduce bandwidth requirements. Implement enhanced
TCP congestion control algorithms (like bottleneck bandwidth and
round-trip propagation time (BBR)) and parallel data transfer
technologies to maximize throughput across high-latency networks
without overwhelming network resources.

**Desired outcome:** You have an
optimized network infrastructure that intelligently prioritizes
research traffic, efficiently routes data across global sites, and
uses advanced compression techniques. This enables faster and more
reliable data transfers while maintaining the integrity of sensitive
life sciences workloads.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Implement QoS mechanisms to provide bandwidth priority to critical
research data and time-sensitive clinical trial information. This
avoids network congestion while maintaining performance for
essential workflows and regulatory adherence requirements.

Deploy SD-WAN solutions with real-time path selection capabilities
to optimize data movement across global research sites. WAN
optimization improves network resource utilization efficiency
while maintaining data integrity for sensitive life sciences
workloads.

Use lossless compression algorithms specifically designed for life
sciences data types. This improves data integrity for genomic
sequences, clinical trials, and medical imaging while reducing
bandwidth consumption and transfer times.

Implement advanced TCP congestion control with BBR to maximize
network efficiency. Configure parallel data transfer capabilities
to optimize throughput for large-scale research data sets across
high-latency global networks.

Balance network resources through intelligent traffic shaping and
bandwidth allocation. Monitor network utilization patterns to
avoid saturation while providing consistent performance for
critical research operations.

### Implementation steps

- Deploy AWS Global Accelerator for optimized global routing
and traffic management.
- Configure Amazon Route 53 with health checks and failover
routing policies for high availability.
- Implement Amazon CloudFront with optimized cache behaviors
for life sciences content distribution.
- Enable Amazon S3 Transfer Acceleration for expedited large
genomic dataset transfers.
- Configure QoS policies with traffic prioritization for
different data types (like genomic, clinical, and imaging).
- Deploy Application Load Balancers with content-based routing
for distributed data transfers.
- Implement data-specific compression algorithms for genomic,
clinical trial, and medical imaging data.
- Establish compression verification checks and performance
monitoring dashboards.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/life-sciences-lens/lsperf12-bp03.html*

---
