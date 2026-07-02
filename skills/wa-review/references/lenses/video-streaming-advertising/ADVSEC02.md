# ADVSEC02 — Data protection

**Pillar**: Security  
**Best Practices**: 1

---

# ADVSEC02-BP01 Encrypt DSP to SSP communication in transit using TLS

Protect data in transit by using encrypted communication channel
at the network communication level.

## Implementation guidance

Protecting data that is transmitted from network to network
remains a top security priority. Data confidentiality,
integrity, and authenticity of the supported workloads are
crucial for securing sensitive information, preventing
unauthorized access, and enabling reliable operations within the
workload.

Use [AWS PrivateLink](https://aws.amazon.com/privatelink/) to establish connectivity between Amazon VPCs
and other services without exposing the data to the public
internet. If you have on-premises resources, consider using
[AWS Direct Connect](https://aws.amazon.com/directconnect/). Direct Connect can make it easy to
establish private connectivity between an AWS datacenter and
your internal network. Implementing MACsec security on your
Direct Connect connection provides point-to-point encryption for
your traffic.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advsec02-bp01.html*

---
