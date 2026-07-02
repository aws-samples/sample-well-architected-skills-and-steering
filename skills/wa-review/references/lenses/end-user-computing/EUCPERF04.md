# EUCPERF04 — Compute and hardware

**Pillar**: Performance Efficiency  
**Best Practices**: 3

---

# EUCPERF04-BP01 Evaluate available instance types (AppStream) and hardware bundles (WorkSpaces)

WorkSpaces Applications groups instances into families, such as General Purpose (stream.standard).
Within each family, there are different instance sizes, such as stream.standard.medium and
stream.standard.large. Each size has a different number of vCPUs and memory. Graphics
optimized families include instances with one or more GPUs. For more information on the
Graphics G4 (stream.graphics.g4dn), Graphics G5 (stream.graphics.g5), and Memory Optimized
(stream.memory.z1d) families, see [Amazon EC2
Instance Types](https://aws.amazon.com/ec2/instance-types/).

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

WorkSpaces bundle selection begins with determining if your workload requires a GPU. If it
does, evaluate the Graphics G4 and Graphics G5 families. If it does not require a GPU,
evaluate the General Purpose, Compute Optimized, and Memory Optimized families. In
addition to large amounts of memory, stream.memory.z1d instances offer the highest CPU
clock rates of the WorkSpaces Applications instance family.

WorkSpaces provides hardware bundles with different amounts of vCPUs and memory.
Graphics.G4dn and GraphicsPro.G4dn bundles include GPUs.

For specifications and recommended uses cases, see [Amazon WorkSpaces](https://aws.amazon.com/workspaces-family/workspaces/pricing/).

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucperf04-bp01.html*

---

# EUCPERF04-BP02 Identify all user types, and deploy required fleet types and instance types as needed

Not all end users necessarily require the same level of performance. Users who perform
routine tasks such as data entry, document review, or customer service may need a low level
of performance, while content or video editors, investment and securities traders, or
graphics users may require performant desktops. Other users may require moderate levels of
performance as their workloads may be unpredictable.

It's important to have a high degree of familiarity with the applications that need to
be delivered using Amazon WorkSpaces Applications in terms of their compute resource requirements. By
understanding core compute requirements such as the amount of memory, CPU, network
bandwidth, latency, and disk space that applications require, you can determine the optimum
fleet type and instance sizes required for the workload.

**Level of risk exposed if this best practice is not
established:** Medium

## Implementation guidance

Determine the compute requirements for your applications.

- Assess your users' applications and tasks, and deploy a sufficient level of fleet
types and instance types as are needed.
- Monitor the resulting user feedback to verify that performance meets their needs
without overprovisioning their instance types.
- If performance or productivity suffers for various users, increase the
performance of their instances. This can be achieved by using larger instances with
more CPU or in the case of WorkSpaces Applications using a different instance family that
provides higher clock speed for CPU cores.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucperf04-bp02.html*

---

# EUCPERF04-BP03 Determine the running mode and size of hardware bundles needed to support each user type's applications

It's important to have a high degree of familiarity with the applications that need to
be delivered using Amazon WorkSpaces Personal in terms of their compute resource requirements and
their usage pattern. By understanding core compute requirements such as the amount of
memory, CPU, network bandwidth, latency, and disk space that applications require, you can
more effectively determine the optimum WorkSpaces Personal bundle type. The optimal running mode
required to support the workload is determined by understanding the pattern of usage of the
application.

## Implementation guidance

Determine the compute requirements for your applications.

- Assess your users' applications and tasks and deploy a sufficient level of
performance as is needed.
- Monitor the resulting user feedback to verify that performance meets their needs
without overprovisioning their hardware types.
- If performance or productivity suffers for various users, increase the size of
their instances.
- For Personal WorkSpaces, establish the current or required pattern of usage of the
applications or desktops being delivered. Select an Always-On running mode for user
environments that are broadly used throughout each month (> 80 hours), select the
Auto-Stop running mode where usage will be

*Source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucperf04-bp03.html*

---
