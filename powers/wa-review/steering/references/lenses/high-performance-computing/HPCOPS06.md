# HPCOPS06 — Operational excellence

**Pillar**: Operational Excellence  
**Best Practices**: 1

---

## HPCOPS06-BP01 Test and observe job-level performance for every change

Before moving users to a new cluster environment, you should run
a set of representative HPC job benchmarks to confirm that your
system is performing as expected. To verify that this
performance is maintained, consider periodically rerunning these
benchmarks or a subset so that any unexpected changes can be
localized and investigated early.

As the projects of your users evolve, the requirements and usage
of your HPC environment will also change from the initial set of
jobs on which your representative set of testcases were built.
To verify that the performance tests are relevant, you could
periodically update your testcases, or you can consider
alternative methods such as monitoring the jobs that your users
are running. For example, by monitoring job logs or percent
usage by department or user, you may proactively detect
anomalies. You can then investigate whether these anomalies were
caused by a known change in usage patterns, or an unexplained
performance regression. Set alerts and automated responses where
appropriate.

Performance regressions can go undetected as they may not throw
any errors, but can result in longer running jobs and increased
cost per job. Consider adding operational mechanisms to track
metrics of your jobs and building them into a cohesive
dashboard. You can use these collected metrics to tune your
environment based on real usage, such as rightsizing the tier of
throughput and capacity of your file systems, or adding new
compute options similar to hardware configurations that are
currently oversubscribed.

### Implementation guidance

Log job-level statistics, track anomalies and integrate your
environment logging into a dashboard.

There are a number of options for tracking the operational
performance of your HPC environment which vary in the level of
granularity the offer and operational overhead required to run
them. Most HPC schedulers have their own tools to track job
level metrics, and these can be the easiest place to start as
they natively integrate with the scheduler.

If using AWS ParallelCluster with Slurm, leverage
[Slurm
accounting with AWS ParallelCluster](https://docs.aws.amazon.com/parallelcluster/latest/ug/slurm-accounting-v3.html) to log job-level
statistics in an external database. You can then add a method
to visualize these metrics so you can easily gain a view
across your environment. The
[ParallelCluster
Monitoring dashboard](https://github.com/aws-samples/parallelcluster-monitoring-dashboard) repository is an example of how
you can construct a dashboard to track job data. If using AWS Batch, a similar tool is the
[AWS Batch Runtime Monitoring Dashboards Solution](https://github.com/aws-samples/aws-batch-runtime-monitoring).

Higher level alternative or complementary tracking methods
such as tagging cloud resources by project and using them to
drill down into cost reports using AWS cost allocation tags to
detect anomalies can offer a similar effect with lower
operational overhead but reduced granularity. For more
information, see
[Organizing
and tracking costs using AWS cost allocation tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html). Many
tools such as
[AWS ParallelCluster resources and tagging](https://docs.aws.amazon.com/parallelcluster/latest/ug/resources-tags-v3.html) and AWS Batch
resource tagging:
[Tag
your AWS Batch](https://docs.aws.amazon.com/batch/latest/userguide/using-tags.html) resources integrate with this mechanism
natively to simplify automated tagging.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/high-performance-computing-lens/operate.html*

---
