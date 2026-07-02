**Saga**: Development lifecycle
**Capability**: DL.ADS — Advanced deployment strategies

---

# [DL.ADS.6] Use cell-based architectures for granular deployment and release

**Category:** OPTIONAL

A cell-based architecture segments a larger system into isolated, independently
functioning replicas, or *cells*. These cells are smaller components of
the system that contain all application logic and storage. They have their own monitoring
and alerting systems, are automated for creation and update, and can be managed and scaled
individually. This approach offers advantages including scalability, fault isolation,
testing, and operational resilience.

A cell-based architecture is a natural fit for DevOps as it
enables small, frequent changes, reduces the risk from
problematic deployments, and enables rapid recovery. It allows
teams to deliver incremental updates to individual cells
without risking the entire system's stability.

Start by defining your cells, each of which should be a
complete, independently deployable unit of your system. You
should limit the maximum size of a cell and maintain this
consistency across different regions or installations. You
then need to establish a routing layer that redirects client
requests to the appropriate cell. You can store the routing
information, such as user-to-cell mapping, in a low-latency
database. Every cell should have its own monitoring and
alerting system.

You will need to automate the lifecycle of your cells, including initial deployment
and subsequent updates. A *canary cell* can be helpful in initial
deployment of updates and assessing their impact. Ensure that you implement a central
dashboard to provide an aggregated view of the state of your cells, enabling easy
system-wide monitoring. Stream changes to a central data lake for centralized querying and
analysis of changes across all cells. Finally, implement an operational tool to move users
between cells and create new cells as needed. This step optimizes load distribution across
cells by updating the user-to-cell assignment.

Cell-based architectures are optional. While beneficial for
complex systems, smaller systems might not require such
architectural complexity.

**Related information:**

- [AWS Well-Architected Reliability Pillar: REL10-BP04 Use
bulkhead architectures to limit scope of impact](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_fault_isolation_use_bulkhead.html)
- [Guidance
for Cell-based Architecture on AWS](https://aws.amazon.com/solutions/guidance/cell-based-architecture-on-aws/)
- [Minimizing
correlated failures in distributed systems](https://aws.amazon.com/builders-library/minimizing-correlated-failures-in-distributed-systems#Noninfrastructure_causes_of_correlated_failures)
- [Journey
to cell-based microservices architecture on AWS for
hyperscale](https://www.youtube.com/watch?v=ReRrhU-yRjg)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.ads.6-utilize-cell-based-architectures-for-granular-deployment-and-release.html*
