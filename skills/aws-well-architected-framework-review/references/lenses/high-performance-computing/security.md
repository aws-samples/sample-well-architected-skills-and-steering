# Security

**Pillar**: Security  
**Questions**: 2

---

# HPCSEC01 — Security

**Pillar**: Security  
**Best Practices**: 2

---

## HPCSEC01-BP01 Separate HPC cluster components in different network layers

When architecting for
[SEC05-BP01](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_network_protection_create_layers.html),
you create network layers and separate components into different
layers. In HPC clusters, you can separate different cluster
components, such as head node, login nodes, and compute
resources. For example, with AWS ParallelCluster, the cluster
head node can be separated from the compute resources. The head
node could be running in a public subnet with the compute fleet
running in a private subnet. Additionally, you could further
isolate your cluster by running in private subnets with private
connectivity to the cluster.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/high-performance-computing-lens/infrastructure-protection.html*

---

## HPCSEC01-BP02 Control traffic flow within your HPC cluster

According to
[SEC05-BP02](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_network_protection_layered.html),
you control traffic flow within your network layers. You permit
only the network flows necessary for the components of your
workloads to communicate. When running tightly coupled HPC
workloads with Elastic Fabric Adapter (EFA), EFA requires being
a member of a security group allowing all inbound and outbound
traffic to and from itself. Each cluster member will allow all
traffic between members when processing the same EFA-based job.

Clusters are commonly used with multiple running jobs and a
single security group would be used for all EFA traffic without
separation by job. If your environment requires further security
separation by job, consider an alternative design, such as
multiple clusters or a more advanced security group mapping,
rather than having one security group for all traffic between
members.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/high-performance-computing-lens/infrastructure-protection.html*

---

# HPCSEC02 — Security

**Pillar**: Security  
**Best Practices**: 2

---

## HPCSEC02-BP01 Enforce encryption at rest in your HPC environment

With
[SEC08-BP01](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_protect_data_rest_key_mgmt.html),
you securely manage encryption keys to protect data at rest. You
also tightly control access through the use of
[key
policies](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html) and IAM policies. AWS HPC products, such as AWS ParallelCluster, configure IAM permissions on different
components, such as cluster, queues, and login nodes. Therefore,
cluster users can unencrypt data at rest by IAM permissions
associated with the cluster or component. If your HPC
environment needs further isolation, such as by project or group
separation, consider an architecture with multiple clusters for
data separation by encryption key.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/high-performance-computing-lens/data-protection.html*

---

## HPCSEC02-BP02 Enforce encryption in transit in your HPC environment

When implementing
[SEC09-BP02](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_protect_data_transit_encrypt.html),
you enforce encryption in transit. Tightly coupled HPC
applications using EFA bypass the operating system kernel and
directly communicate with the EFA device rather than traditional
TCP/IP networking. This provides low-latency, reliable
communication between cluster instances but introduces
additional considerations when enforcing encryption in transit
compared to traditional TCP/IP approaches.

AWS provides secure and private connectivity between EC2
instances of all types. In addition, some instance types use the
offload capabilities of the underlying Nitro System hardware to
automatically encrypt in-transit traffic between instances. This
encryption uses Authenticated Encryption with Associated Data
(AEAD) algorithms with 256-bit encryption, which also helps
implement
[SEC09-BP03](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_protect_data_transit_authentication.html).
There is no impact on network performance.

Therefore, your EFA traffic is automatically encrypted between
cluster members with no impact to performance. This automatic
encryption is also used with
[FSx for Lustre](https://docs.aws.amazon.com/fsx/latest/LustreGuide/encryption-in-transit-fsxl.html) and enforcing encryption in transit between
cluster members and an FSx for Lustre filesystem. See
[Encryption
in transit](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/data-protection.html#encryption-transit) for additional details.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/high-performance-computing-lens/data-protection.html*

---

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
