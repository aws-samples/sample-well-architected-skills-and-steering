**Pillar**: Reliability

# FSIREL04: Does the resilience and the architecture of your workload reflect the business requirements and resilience tier?

Understanding how AWS services can impact your workload's availability is an
important step in determining the resilience of your architecture.

## FSIREL04-BP01 Use best practices to implement highly resilient critical workloads

Financial services institutions must be compliant with regulatory frameworks that
define policies towards the resilience and operational excellence of their mission
critical or core workloads. Workloads designated by regulators and financial
institutions as critical are therefore subject to greater scrutiny from regulators
because financial services institutions must demonstrate that they can recover
operations within reasonable recovery times and with little or no data loss.

To achieve these targets, you must mitigate scenarios that may disrupt your system
by anticipating the scenarios, being able to monitor for their occurrence, and having
pre-arranged responses in place. Adopting processes like ORRs, predictive monitoring
with leading indicators, and consistent deployments are just some of the best
practices that can be used to mitigate common scenarios. Additional workload design
patterns for resilient systems can be found in the [The Amazon Builders' Library](https://aws.amazon.com/builders-library/?cards-body.sort-by=item.additionalFields.sortDate&cards-body.sort-order=desc&awsf.filter-content-category=*all&awsf.filter-content-type=*all&awsf.filter-content-level=*all).

## FSIREL04-BP02 Provide external dependency accessibility from failover environments

FSI workloads often rely on many external service integrations with partner firms
or online services from other departments in the same firm. While your workload may be
able to resume service in a different failover environment, confirm that the system is
able to operate with its dependencies from the failover environment. Make your
dependencies accessible from the failover environment, and verify that the workload is
able to function despite any changes in network attributes, such as latency.

Tightly coupled dependencies may need to be failed over in advance of your
workload's failover. This slows down the recovery of your workload as it waits for its
dependencies to become available. Coordinate your disaster recovery failover to
expedite this process and bring down the recovery time to within acceptable
ranges.

## FSIREL04-BP03 Decouple your dependencies

Design your workload so that it is able to function despite impairment to dependencies, like external
service integrations with partner firms, as well as services from other departments in the
same firm. Decouple your workload from its
dependencies so that it has static stability and continues functioning, or at least
fails gracefully, even when its dependencies are impaired. Workload code should be
reviewed and tested with the consideration that any API call to an external dependency
may time out with no response, or return an unexpected error. Use chaos engineering to
perform experiments where the workload's functionality is observed during simulation
dependency disruption.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsirel04.html*
