**Saga**: Observability
**Capability**: O.SI — Strategic instrumentation

---

# [O.SI.4] Build health checks into every service

**Category:** RECOMMENDED

Each service within a system should be configured to include a health check endpoint
which provides real-time insight into how the system and its dependencies are performing.
Usually manifested as a secure and private HTTP health endpoint (for example,
`/actuator/health`), this feature serves as a critical component in
monitoring the health status of the overall system, generally including information such
as operating status, versions of software running, database response time, and memory
consumption. By offering lightweight and fast-responding feedback, they enable sustaining
system reliability and availability, two attributes that directly impact customer
experience and service credibility.

Observability, governance, and testing tools can invoke these
health check endpoints periodically, ensuring the continuous
evaluation of system health. However, implementing them should
be done with precautionary measures like rate-limiting,
thresholding, and circuit breakers to avoid overwhelming the
system and to involve human intervention when required.

Integrating health check endpoints is highly recommended for
larger, more complex systems or any environment where system
availability and rapid issue resolution need to be
prioritized. In systems with high interoperability, such as
microservices architecture, the presence of health check
endpoints in every service becomes even more critical as they
help identify issues related to specific services in the
system. This can significantly reduce the debugging time and
enhance the efficiency of the development process.

For mission critical workloads it may be beneficial to explore
additional mitigation strategies to prevent widespread failure
due to faulty deployments. These strategies could include
alerting mechanisms when overall fleet size, load, latency, or
error rate are abnormal, and phased deployments to ensure
thorough testing before full-scale implementation. These
preventive deployment measures complement health check
endpoints and can prevent a potentially flawed deployment from
propagating throughout the entire system.

**Related information:**

- [Implementing
health checks](https://aws.amazon.com/builders-library/implementing-health-checks/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/o.si.4-build-health-checks-into-every-service.html*
