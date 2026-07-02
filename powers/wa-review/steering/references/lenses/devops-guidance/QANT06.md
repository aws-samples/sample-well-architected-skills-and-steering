**Saga**: Quality assurance
**Capability**: QA.NT — Non-functional testing

---

# [QA.NT.6] Experiment with failure using resilience testing to build recovery preparedness

**Category:** RECOMMENDED

Resilience testing deliberately introduces controlled failures
into a system to gauge its ability to withstand failure and
recover during disruptive scenarios. Simulating failures in
different parts of the system provides insight into how
failures propagate and affect other components. This helps
identify bottlenecks or single points of failure in the
system.

Before initiating any resilience tests, especially in
production, understand the potential impact on the system,
dependent systems, and the operating environment. Start small
with less invasive tests and gradually expand the scope and
frequency of these tests. This iterative approach allows you
to understand the ramifications of a particular failure and
ensures that you don't accidentally cause a significant
disruption.

There are various types of resilience testing:

- **Chaos engineering:** Resilience tests using fault
injection to introduce controlled failures into the system. This can include
simulating service failures, region outages, single node failures, network outages, or
complete failovers of connected systems. Controlled failures enable teams to identify
system vulnerabilities, ensuring weaknesses introduced by deployments and
infrastructure changes are mitigated. Fault injection tools, such as [AWS Fault Injection Service](https://aws.amazon.com/fis/) and [AWS Resilience Hub](https://aws.amazon.com/resilience-hub/), can assist in conducting these experiments.
Embed the use of these tools into automated pipelines to run fault injection tests
after deployment.
- **Data recovery testing:** Resilience tests that verify
that specific datasets can be restored from backups. Data recovery tests ensure that
the backup mechanism is effective and that the restore process is reliable and
performant. Schedule data recovery tests periodically, such as monthly, quarterly, or
after major data changes or migrations. Initiate these tests through deployment
pipelines. For example, after a database schema deployment, run a test to ensure that
the new schema doesn't compromise backup integrity.
- **Disaster recovery testing:** Resilience tests that help
ensure the entire system can be restored and made operational after large scale
events, such as data center outages. This includes activities such as restoring
systems from backups, switching to redundant systems, or transitioning traffic to a
disaster recovery environment. These tests are extensive and therefore run less
frequently, such as semi-annually or annually. When running in production
environments, these tests are usually performed during maintenance windows or off-peak
hours, and stakeholders are informed well in advance. Use disaster recovery tools,
such as [AWS Elastic Disaster
Recovery](https://aws.amazon.com/disaster-recovery/) and [AWS Resilience Hub](https://aws.amazon.com/resilience-hub/), to assist with planning, coordinating, and performing recovery
actions. While integrating these tests fully into deployment pipelines is rare, it is
possible to automate sub-tasks or preliminary checks. For example, after significant
infrastructure changes, a test might check the functionality of failover mechanisms to
ensure they still operate as expected. It can often be more effective to trigger these
tests based on events or manual triggers, especially earlier on in your DevOps
adoption journey.

Before running resilience tests in either test or production environments, consider
the use case, the benefits of the test, and the system's readiness. Regardless of the
target environment, always inform all stakeholders of the system before executing
significant resilience tests. Have a pre-prepared, comprehensive communication plan in the
event of unforeseen challenges or downtime. We recommend initially running resilience
tests in a test environment to get an understanding of their effects, refine the testing
process, and train the team.

After gaining confidence in the testing process and building the necessary
observability and rollback mechanisms to run them safely, consider running controlled
tests in production to gain the most accurate representation of recovery scenarios in
real-world settings. When executing in production, limit the impact of your tests. For
example, if you are testing the resilience of a multi-Region application, don't bring down
all Regions at once. A better approach would be to start with one Region, observe its
behavior, and learn from the results. After running resilience tests, conduct a
retrospective to understand what went well, any unexpected behaviors, improvements that
can be made, and to plan work to enhance both the system's resilience and the testing
process itself.

**Related information:**

- [AWS Well-Architected Reliability Pillar: REL09-BP04 Perform
periodic recovery of the data to verify backup integrity and processes](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_backing_up_data_periodic_recovery_testing_data.html)
- [AWS Well-Architected Reliability Pillar: REL12-BP05 Test
resiliency using chaos engineering](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_testing_resiliency_failure_injection_resiliency.html)
- [AWS Well-Architected Reliability Pillar: REL13-BP03 Test
disaster recovery implementation to validate the implementation](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_planning_for_recovery_dr_tested.html)
- [AWS Fault Isolation Boundaries](https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/abstract-and-introduction.html)
- [Well-Architected
Lab - Testing for Resiliency](https://wellarchitectedlabs.com/reliability/300_labs/300_testing_for_resiliency_of_ec2_rds_and_s3/)
- [Fault
testing on Amazon EBS](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-fis.html)
- [Chaos
experiments on Amazon RDS using AWS Fault Injection Service](https://aws.amazon.com/blogs/devops/chaos-experiments-on-amazon-rds-using-aws-fault-injection-simulator/)
- [Chaos
Testing with AWS Fault Injection Service and AWS CodePipeline](https://aws.amazon.com/blogs/architecture/chaos-testing-with-aws-fault-injection-simulator-and-aws-codepipeline/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/qa.nt.6-experiment-with-failure-using-resilience-testing-to-build-recovery-preparedness.html*
