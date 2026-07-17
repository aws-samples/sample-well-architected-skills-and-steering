# Sustainability

**Pages**: 7

---

# Best practice 15.1 – Define your organization’s current environmental impact

As an organization, you should track your progress towards your sustainability goals. By determining your current environmental impact, you can track and report improvements as you make changes over time. Without knowing where you are you can’t know how far you’ve come.

**How do you track your analytics
carbon footprint?**

## Suggestion 15.1.1 – Determine the carbon emissions of your workload using the AWS Customer Carbon Footprint Tool

Determining the current carbon emissions of your analytics workloads at the start of your optimization journey is important as it enables you to track your changes and see what efforts have the biggest impact. If you are an AWS user, your
organization can use the AWS Customer Carbon Footprint Tool. The AWS Customer Carbon
Footprint Tool is a data tracking and visualization tool that reports on your AWS accounts carbon usage.

Your organization should maintain an audit trail of the changes that your team
have made, when they were made, and the impact that the changes had on the carbon
footprint of each workload.

For more details, refer to the following information:

- [AWS Customer Carbon Footprint Tool](https://aws.amazon.com/aws-cost-management/aws-customer-carbon-footprint-tool/)
- [AWS Customer Carbon
Footprint Tool Overview](https://www.youtube.com/watch?v=WqhAnLdg3rg)
- [Sustainability Pillar Improvement Process](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/improvement-process.html)
- [Sustainability Pillar Improvement Process](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/improvement-process.html)

## Suggestion 15.1.2 – Define and track your progress using proxy metrics

When something is hard or impractical or very difficult to measure directly, you can instead use a related measurements in its place. This is called a *proxy metric*.

Environmental impact is hard to measure directly, especially when you want fine-grained measurements. However, in the cloud, the environmental impact of a workload is often correlated with efficiency, which is also often correlated with cost. Just like you can apply many of the best practices of the performance efficiency and cost optimization pillars to lower your environmental impact, you can also use performance metrics and cost as proxy metrics to track your progress.

For more details, refer to the following information:

- [Evaluate specific improvements](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/evaluate-specific-improvements.html)
- [Turning Cost and Usage Reports into Efficiency Reports](https://catalog.workshops.aws/well-architected-sustainability/en-US/5-process-and-culture/cur-reports-as-efficiency-reports)
- [Best practice 8.3 – Define and measure the computing performance metrics](https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/best-practice-8.3---define-and-measure-the-computing-performance-metrics..html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/best-practice-15.1-define-organization-current-environmental-impact.html*

---

# Best practice 15.2 – Encourage sustainable thinking

Software architects are often encouraged to apply systems thinking to the problems they tackle. To zoom out and look at the bigger picture and how the different components interact and form a whole. To build sustainable cloud workloads also requires sustainability thinking – including environmental impact as a parameter in design and planning.

Organizations should include sustainability requirements when considering new projects, and continuously evaluate the environmental impact of existing workloads. They should find the balance between business needs and sustainable goals – and creative solutions to achieve both.

Encourage questioning business requirements on sustainability grounds. For example, when considering the update frequency of dashboards, include the impact on things like energy usage in the discussions. Sometimes this leads to insights such as that only some of the KPIs need frequent updates, while the majority of the dashboard contents only need updating once per day. This can result in a reduction in energy usage while still delivering the same business value.

## Suggestion 15.2.1 – Review the update frequency of your reports and dashboards

Running reports and refreshing dashboards can be a compute intensive process. Continuously review the business requirements and question how frequently refreshes are needed. Can some reports be run only on demand because they are accessed infrequently? Can reports that today run on demand instead be run on a schedule to have them always available instead of multiple people running them many times per day? Does every KPI need to be refreshed at the same time?

## Suggestion 15.2.2 – Review your reports, dashboards, and metrics and remove what is no longer needed

As organizations evolve, so does business requirements.. Over time, some reports and dashboards become more important and used, and others less. New metrics become important, and reports and dashboards accumulate elements that are no longer necessary.

Continually evaluate business requirements and remove what is no longer needed. Remove metrics from reports when they are not necessary, and remove whole reports and dashboards when they lose their relevance. Eﬃcient reporting has a positive impact on your sustainability goals. Your organization can also identify similar goals across teams or departments to reduce the number of separate reports and thereby reduce duplication and overlap.

## Suggestion 15.2.3– Review the running frequency of your data pipelines

Data pipelines are the backbone of analytics platforms. They process data and produce new data sets. They are compute-intensive processes that can have a big impact on the overall environmental impact of your analytics platform. The more frequently they run, the higher the impact. Work backwards from your business requirements and decide appropriate running frequencies that balance business value and environmental impact.

Consider splitting pipeline jobs when there is an opportunity to run the majority of its calculations on a lower frequency while still maintaining the overall business goals.

## Suggestion 15.2.4– Be flexible in your job schedules

It’s common to run jobs on regular schedules, like hourly or daily, often at the top of the hour. When using managed and serverless technologies, the service often keeps a warm pool of compute resources to be able to meet demand. The pool needs to be managed to meet peaks in demand, and for job-oriented services this often coincides with the top of the hour. By being flexible in when you run your jobs, and for example avoiding the top of the hour, you can help the service smooth out demand.

This is similar to how you can optimize your own resource usage by implementing buffering and throttling, as described in [SUS02-BP06 Implement buffering or throttling to flatten the demand curve](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_user_a7.html).

*Source: https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/best-practice-15.2-encourage-sustainable-thinking.html*

---

# Best practice 15.3 – Encourage a culture of data minimization

Analytics relies heavily on large volumes of data being stored and processed. Minimizing the amount of data stored and processed can have a positive impact on the environmental impact of your organization’s analytics platform. Encourage architects, data engineers, and other roles that work on the platform to think about ways to minimize the amount of data stored and processed at every point in the system. A just enough data mindset can reduce the overall amount of data processed and therefore reduce the amount of compute power and storage used, and lower the environmental impact.

Look for opportunities to break linear relationships so that datasets don’t need to grow at the same pace as your business. As your user base increases, find ways to avoid datasets growing at the same pace. In many cases it may be unavoidable, but for example, if you store partially aggregated data you can break the linear relationship.

Encouraging a culture of always thinking about ways to minimize data can help ensure your organization does not unintentionally increase its environmental impact again after reductions have been made.
More information on building and implementing an Improvement
process can be found in the
[Sustainability
Pillar whitepaper](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/improvement-process.html).

**How do you minimize the amount of
data that is processed?**

## Suggestion 15.3.1– Minimize the amount of data extracted from your source systems that gets stored in your data warehouse

Data warehousing plays an important role in providing meaningful insights to your reporting layers and analytics. Data warehousing is the ingestion and merging of multiple data sources to create a single data model optimized for the business’ needs. Typically it employs techniques such as denormalization and materialized views of aggregates to provide faster query response times. It is encouraged that your organization applies these principles of building a data warehouse.

It is common that all source data is ingested into a data warehouse. Since data warehouses are good at storing massive amounts of data, and because it’s hard to know in advance what is going to be needed, many organizations store everything. This leads to higher environmental impact because of the added compute and storage requirements.

Work backwards from the business needs, reports, and dashboards when designing ingestion processes and data models for data warehouses. This avoids the overhead of extracting, processing, and storing source data that is not strictly needed.

For more details, refer to the following information:

- [Amazon Redshift development guide: Database Developer Guide](https://docs.amazonaws.cn/en_us/redshift/latest/dg/redshift-dg.pdf)
- [Optimize your modern data architecture for sustainability: Part 1 – data ingestion and data lake](https://aws.amazon.com/blogs/architecture/optimize-your-modern-data-architecture-for-sustainability-part-1-data-ingestion-and-data-lake/)

When designing your source data extraction processes, it is recommended that your organization should only extract data required for the workloads, such as reports and dashboards, that the data warehouse supports. This results in less data being transferred over the network, less data processed, less data being loaded into the data warehouse, less data being stored over time, and less data to remove when applying data retention policies.

When extracting data from your source datastore, your organization should use a date range to extract only data that has been added or updated in the source datastore since the last data extract. This is called delta updates. This approach reduces the environmental impact of reprocessing the same data multiple times.

Designing and building an efficient data model requires
upfront consideration. Your development team should ensure
that the optimal row-level granularity (for example
customer level, address level, or product level) and data
attributes reduces unnecessary deduplication and
filtering further downstream.

Most reporting applications support data editing and data
filtering capabilities. Therefore, your development teams
can develop a subset of data within the business tool
minimizing the amount of data required for a report
refresh.

For more details, refer to the following information:

- [Quick: Creating
datasets](https://docs.aws.amazon.com/quicksight/latest/user/creating-data-sets.html)

## Suggestion 15.3.2 – Use appropriate data types when developing database tables

Databases and data warehouses can store many different types of data, and have optimized storage mechanisms for each type. Choosing the appropriate type for columns can optimize both the storage size of a dataset and the compute resources needed to process it. For example, storing numbers as integers, floats, and so on, instead of strings can save a lot of storage space, and greatly reduce the processing required when performing calculations. Similarly, dates and timestamps should be stored using matching data types. Consider each column and assign the most specific data type possible.

For more details, refer to the following information:

- [Amazon Redshift best practices for designing tables](https://docs.aws.amazon.com/redshift/latest/dg/c_designing-tables-best-practices.html)
- [Data
types in Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/data-types.html)
- [Amazon Redshift data types](https://docs.aws.amazon.com/redshift/latest/dg/c_Supported_data_types.html)
- [Quick: Supported
data types and values](https://docs.aws.amazon.com/quicksight/latest/user/supported-data-types-and-values.html)

## Suggestion 15.3.3 – Review your APIs to understand whether all data must be shared with your streaming applications

APIs play an important role in connecting and sharing data between
applications, databases and other systems. Application developers should consider the size
of an event payload submitted to these systems.

Organizations require the ability to run analytics on
real-time data. To do so, organizations send data to
streaming services. Streaming services, such as Amazon Managed Streaming for Apache Kafka (Amazon MSK) and Amazon Kinesis, allow organizations to run analytics on real-time
streams of information. It is important that the data
being shared with such streaming services is reviewed
through the improvement process, because the more data
provided in the payload will require more resources to
store and process the data. Reducing the network, storage,
and compute resources required to process unnecessary data
can help towards reducing your organization’s analytics
environmental impact.

Review data that is captured by the application and pushed
to the streaming platform to identify data attributes that
can be removed. Also identify opportunities to store
commonly used transforms to create values that can be
computed once. Review your Kafka topic and identify if
it’s duplicated data of whether a single topic is enough
to deliver to multiple dependencies. Through the
Improvement process you should consider data volumes and
the value of your assets, and measure these against your
organization’s proxy metrics.

If it is not possible to reduce data at the point of data
capture, as a developer, you can use AWS Lambda to trim
event payloads of data attributes that are not required
for downstream processing. However, as an organization,
you should balance the trade-off of compute cost of
removing the data versus retaining the original data
values. This is not a binary option but should be measured
over time to determine if it would be worthwhile removing
data.

For more details, refer to the following information:

- AWS Lambda:
[Using
AWS Lambda with Amazon Kinesis](https://docs.aws.amazon.com/lambda/latest/dg/with-kinesis-example.html)

Implement a monitor and alert strategy to get a clear
picture of data growth over time. Take action on any
significant data growth by understanding what additional
attributes have been added to the event payload. Alerts
should be implemented on thresholds, such as 3x data
growth, or create an internal metric that your
organization should expect to increase the overall data
footprint aligned with new customers.

For more details, refer to the following information:

- Amazon Kinesis:
[Monitoring
the Amazon Kinesis Data Streams Service with Amazon CloudWatch](https://docs.aws.amazon.com/streams/latest/dev/monitoring-with-cloudwatch.html)

## Suggestion 15.3.4 – Reduce the amount of data migrated from one environment to another

Migrating data from one environment to another is a common exercise. Your
organization should consider data minimization when migrating from one environment to
another as migration requires additional network, storage, and compute resources for
migrating unwanted information. Your organization should regularly review all
information that is in scope of the migration and determine whether it is necessary
for future workloads, rather than defaulting to a *migrate all*
approach.

If your organization maintains a data catalog, a review of the data assets by a
data owner prior to migrating the data should be performed to understand
whether the data is required by the business.

For more details, refer to the following information:

- AWS Data Migration: [Top 10 Data Migration](https://pages.awscloud.com/rs/112-TZM-766/images/2020_0124-STG_Slide-Deck.pdf)
- AWS Data Migration (video):
[Top 10 Data
Migration Best Practices](https://www.youtube.com/watch?v=i0-pSHQJ7pA)

## Suggestion 15.3.5 – Apply the optimal data model for your data access patterns

Understanding your data access patterns helps you determine which data modeling technique is most suitable. Work backwards from the way you access the data to determine the most suitable data model. There are two broad approaches to data modelling that you can start to consider: normalization and denormalization.

*Normalization* is the method of arranging the data in a data model
to reduce redundant data and improve query efficiency. This method involves designing the tables and setting up relationships between those tables according to certain rules. Each piece of data is only stored once, and is referenced using its ID. Joins are used to reassemble the full data model. Typically, normalized data models are used in online transaction processing (OLTP) and are supported by relational databases that store the database data in rows. Normalized models minimize the amount of data stored, and compute power needed to make updates.

*Denormalization* is almost the opposite of normalization. Instead of referencing data using IDs, data is copied as many times as needed. Denormalized data models are typically used in online analytical processing (OLAP) where the data is stored in column-oriented massively parallel processing (MPP) databases such as Amazon Redshift. OLAP is designed for multidimensional analysis of data in a data warehouse, which contains both transactional and historical data. In MPP architectures data locality is important, and keeping redundant copies of data and avoiding joins can reduce the compute power needed, as well as network overhead. On the flip side, they may take up more storage, and updates require more compute power.

Whether you should choose normalization or denormalization for your data model depends on your data access patterns. Consider the way you query and update the data set first. In analytics, denormalized data models often perform better. The extra storage requirements from data duplication is often balanced by compression. When storing data in columns instead of rows, data encoding and compression becomes more efficient.

To normalize or denormalize is not an either-or proposition, but a scale. You can denormalize some parts of your data model heavily, while keeping other parts more normalized. For example, if you store personal data and have to be able to update and delete it easily, normalization of that part of the model may lead to the least environmental impact overall. Each query may become slightly less efficient, but you ensure you don’t have to rewrite the whole data set to remove multiple copies of a data point.

For more details, refer to the following information:

- Modern data architecture:
[Build a modern data architecture on AWS with Amazon AppFlow, AWS Lake Formation, and Amazon Redshift](https://aws.amazon.com/blogs/big-data/build-a-modern-data-architecture-on-aws-with-amazon-appflow-aws-lake-formation-and-amazon-redshift/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/best-practice-15.3-encourage-culture-of-data-minimization.html*

---

# Best practice 15.4 – Implement data retention processes to remove unnecessary data from your analytics environment

The retention of data should be informed, relevant, and limited to what is
necessary for the purposes for which the data is processed. Storing data indefinitely and
without purpose can cause significant storage and processing overhead that can impact your
organization’s analytics environmental impact. Ensure that the period for which the data
should be stored is limited and reviewed on a regular basis.

**How can you remove unnecessary data from an object
store?**

## Suggestion 15.4.1 – Deﬁne and implement a data lifecycle process for data at rest

Implement a lifecycle management process that will either remove data that is no
longer required, or archive data into less resource-intensive storage.

When removing data from an object store, your organization should consider the
following design points:

- The data retention removal process should run on a regular basis
- The data retention removal process should remove data from all buckets,
sub-directories and prefixes.
- The data retention removal process should take an
audit of what data has been removed, when it was
removed, and who performed the removal process. This
audit data should be tracked in an immutable audit log
for auditing purposes.
- Production, user acceptance test (UAT), and
development (DEV) environments must be included and
adhere to the agreed retention policy across all
environments.
- Consider other locations where data might be stored,
such as SFTP locations.
- Classify your organization’s data by data temperature,
such as *hot* for frequently
accessed, and *cold* for
infrequently accessed. After data has been classified
by temperature, your organization should implement a
strategy to move data into the respective S3 bucket
storage classes. For example, cold data could be moved
to Amazon Glacier storage class. For an
illustration of data temperatures, see
[Optimizing
your AWS Infrastructure for Sustainability, Part II:
Storage](https://aws.amazon.com/blogs/architecture/optimizing-your-aws-infrastructure-for-sustainability-part-ii-storage/).

For more details, refer to the following information:

- Amazon S3 Lifecycle
Management:
[Managing
your storage lifecycle](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html)

**How can you remove unnecessary
data from databases?**

## Suggestion 15.4.2 – Remove unnecessary data from databases

To effectively remove information from a database, your
organization should track when the data was loaded into
the database and when the last customer interaction
occurred, such as a purchase or other activity. This
tracking helps you accurately identify when data should be
removed.

- The data retention removal process should run
frequently, but should not be run excessively, as
excessive deletion can increase compute resources that
could mitigate the benefit of removing the data from
your database.
- The data retention removal process should remove data
from all databases and tables.
- The data retention removal process should retain an
audit of what data has been removed, when it was
removed, and who performed the removal process. This
audit data should be tracked in an immutable audit log
for auditing purposes.
- If your database enforces referral integrity, you
should redact only the data and retain the primary and
foreign keys.

For more details, refer to the following information:

- Amazon Redshift:
[Amazon Redshift Stored Procedures](https://docs.amazonaws.cn/en_us/redshift/latest/dg/stored-procedure-create.html)
- Amazon Redshift:
[DELETE
Statement](https://docs.aws.amazon.com/redshift/latest/dg/r_DELETE.html)
- Amazon Redshift:
[Scheduling
a query on the Amazon Redshift console](https://docs.aws.amazon.com/redshift/latest/mgmt/query-editor-schedule-query.html)

## Suggestion 15.4.3 – Use the shortest possible retention period in streaming applications

The primary use-case of a streaming application is to transfer information from source to target, but they can also retain data for a configured time. This allows replaying the stream to, for example, recover from corruption in a downstream system. At the same time, data stored in a streaming application becomes redundant as soon as it has been stored downstream. Determine the shortest possible retention period that you need to meet your Recovery Point Objective (RPO).

For more details, refer to the following information:

- Amazon Kinesis:
[Changing
the Data Retention Period](https://docs.aws.amazon.com/streams/latest/dev/kinesis-extended-retention.html)
- Amazon Managed Streaming for Apache Kafka:
[Adjust
data retention parameters](https://docs.aws.amazon.com/msk/latest/developerguide/bestpractices.html)

## Suggestion 15.4.4 – Design your application to make it possible to efficiently remove or archive outdated data

Designing a data model that supports efficient deletion of data can be surprisingly hard. In the worst case, the deletion of a single piece of data may require rewriting a large portion of the data set in a data lake. This is inefficient and has an unnecessary environmental impact. When designing an application, also design how you remove or archive data from it once that data is outdated, no longer relevant, or upon request.

Consider, and design for things like:

- How to delete all data belonging to a specific user
- How to delete data older than a specific time
- How to delete personal data

In data lakes and analytics applications it is often hard to delete individual pieces of data. Consider how to organize data to reduce the amount of data that has to be rewritten to delete a single piece of data – but always balance it against the impact to query performance.

It is often good practice to partition a data set in a data lake by time to make it possible to efficiently delete historical data when it is no longer needed. Similarly, in a data warehouse, keeping data sorted by time yields similar efficiencies.

For more details see:

- [Optimize your modern data architecture for sustainability: Part 1 – data ingestion and data lake](https://aws.amazon.com/blogs/architecture/optimize-your-modern-data-architecture-for-sustainability-part-1-data-ingestion-and-data-lake/)
- [AWS Well-Architected Framework: SUS04-BP05 Remove unneeded or redundant data](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_data_a6.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/best-practice-15.4-implement-data-retention-processes-to-remove-redundant-data-from-your-analytics-environment..html*

---

# Best practice 15.5 – Optimize your data modeling and data storage for efficient data retrieval

How your data is organized in a data store, database, or ﬁle system can have an impact on the amount of resources that are required to store, process, and analyze the data. Using encoding, compression, indexes, partitioning, and similar tools we can make this more efficient and reduce the overall environmental impact of our analytics workloads.

**How can your organization reduce the
resources required to store, process, and analyze your
organization’s data in a sustainable manner?**

Reducing data that a database system scans to return a result is an eﬃcient way in reducing your organization’s analytics environmental impact. This approach requires less resources to scan the disk to retrieve the information to service the request, and reduces the amount of provisioned storage required to service the workload. There are diﬀerent methods that database engines use to optimize the amount of information scanned, such as partitioning, bucketing, and sorting.

## Suggestion 15.5.1 – Implement an efficient partitioning strategy for your data lake

Partitioning plays a crucial role when optimizing data sets for
Amazon Athena or Amazon Redshift Spectrum. By partitioning a data set, you can reduce the amount of data scanned by queries dramatically. This reduces the amount of compute power needed, and therefore the environmental impact.

When implementing a partitioning scheme for your data model, work backwards from your queries and identify the properties that would reduce the amount of data scanned the most. For example, it is common to partition data sets by date. Data sets tend to grow over time, and queries tend to look at specific windows of time, such as the last week, or last month.

For more details, refer to the following information:

- Amazon S3 and Amazon Athena:
[Partitioning and bucketing in Athena](https://docs.aws.amazon.com/athena/latest/ug/ctas-partitioning-and-bucketing.html)
- Amazon Athena:
[Partitioning
data in Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/partitions.html)

## Suggestion 15.5.2 – Configure and sort distribution keys on your Amazon Redshift tables

Amazon Redshift sort keys determine the order in which
rows in a table are stored on the disk. When you query a data set in Redshift, it can leverage the sort order of the data to avoid reading blocks that are outside of the range of values you are looking for. By reading fewer blocks of data, this approach can result in a reduction of compute resources required.

For more details, refer to the following information:

- Amazon Redshift:
[Choose
the best sort key](https://docs.aws.amazon.com/redshift/latest/dg/c_best-practices-sort-key.html)

In Amazon Redshift, the distribution key, or distkey, determines how data is distributed between the nodes in a cluster. Choosing the right distribution keys can improve the performance of common analytical operations like joins and aggregations.

For more details, refer to the following information:

- Amazon Redshift:
[Automate
your Amazon Redshift performance tuning with automatic
table optimization](https://aws.amazon.com/blogs/big-data/automate-your-amazon-redshift-performance-tuning-with-automatic-table-optimization/)
- Amazon Redshift:
[Distribution
styles](https://docs.aws.amazon.com/redshift/latest/dg/c_choosing_dist_sort.html)

## Suggestion 15.5.3 – Enable results and query plan caching

Computing the same result over and over again is wasteful. Query engines and data warehouses often support result caching, and/or query plan caching. By enabling these you can reduce the overall amount of compute power needed for your analytics workload by eliminating recomputing results and/or query plans when the data set hasn’t changed. This saves on compute resource and reduce the environmental impact.

For more details, refer to the following information:

- Amazon Redshift:
[Performance
optimization](https://docs.aws.amazon.com/redshift/latest/dg/c_challenges_achieving_high_performance_queries.html)
- Amazon Athena: [Query result reuse](https://docs.aws.amazon.com/athena/latest/ug/reusing-query-results.html)

## Suggestion 15.5.4 – Enable data compression to reduce storage resources

Your organization should consider compressing data in both
object stores, such as Amazon S3, and if supported, in
your organization’s database systems. By compressing data,
your organization is reducing the amount of storage and
networking resources required for the workload. Database
systems can decompress the data at a rate that is almost
unnoticeable to the end user or application. As the data
is compressed and then decompressed, this will also reduce
the retrieval time of the database engine to fetch all the
data from the storage array leading to a potential
reduction in compute resources.

For more details, refer to the following information:

- **Amazon Redshift compression
and encoding:**
[Amazon Redshift Engineering’s Advanced Table Design Playbook:
Compression Encodings](https://aws.amazon.com/blogs/big-data/amazon-redshift-engineerings-advanced-table-design-playbook-compression-encodings/)
- **Amazon Redshift file
compression parameter:**
[File
compression parameters](https://docs.aws.amazon.com/redshift/latest/dg/copy-parameters-file-compression.html)
- Amazon Redshift
Compression:
[Compression
encodings](https://docs.aws.amazon.com/redshift/latest/dg/c_Compression_encodings.html)
- Amazon DynamoDB
Compression:
[Using
data compression](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/EMRforDynamoDB.CopyingData.Compression.html)
- Amazon Athena Compression
Support:
[Amazon Athena compression support](https://docs.aws.amazon.com/athena/latest/ug/compression-formats.html)

## Suggestion 15.5.5– Use file formats that optimize storage and compute needs

There are many diﬀerent file formats that can be used to store data from the ubiquitous CSV format, through structured formats like JSON, and data lake-optimized formats like Parquet – each is designed to overcome speciﬁc technical challenges. There is no file format that meets all needs, and different formats have different uses.

For analytical workloads, columnar file formats like Parquet and ORC often perform better overall. They achieve higher compression rates, and help query engines scan less data. Through reduced storage and compute needs they can help reduce the environmental impact of your workload.

More information on how to choose the right format can be found in [Choose the best-performing file format and partitioning](https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/design-principle-10.html).

## Suggestion 15.5.6– Avoid using unnecessary operations in queries, use approximations where possible, and pre-compute commonly used aggregates and joins

Consider the computational requirements of the operations you use when writing queries. For example, think about how the result gets consumed. For example, avoid adding an ORDER BY clause unless the result strictly needs to be ordered.

Many compute-intensive operations can be replaced by approximations. Modern query engines and data warehouses, like Amazon Athena and Amazon Redshift, have functions that can calculate approximate distinct counts, approximate percentiles, and similar analytical functions. These often require much less compute power to run, which can lower the environmental impact of your analytical workload.

Consider pre-computing operations. When you notice that the complexity of your queries increase, or that many queries include the same joins, aggregates, or other compute intensive operations, this can be a sign that you should pre-compute these. Depending on your platform this can be in the form of adding steps to your data transformation pipeline, or by introducing a materialized view.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/best-practice-15.5-optimize-your-data-modeling-and-data-storage-for-efficient-data-retrieval..html*

---

# Best practice 15.6 – Prevent unnecessary data movement between systems and applications

Moving data around your organization can be very costly as
it requires compute, networking, and storage resources. This
can be particularly costly for analytics workloads as they
generally require large quantities of information. When
businesses move data around their organization, they
increase the risk of creating duplicate data, which can
impact your storage resource.

At the same time, making multiple copies of data can also reduce the overall amount of data transferred from each access to the data. When designing your data platform, consider the overall environmental impact and make informed choices about when and when not to duplicate data.

**How does your organization mitigate
the unnecessary data movement from one part of your
organization to another?**

## Suggestion 15.6.1 – Implement data virtualization techniques to query information where the data resides

In data virtualization, only the data that is required to service the request is copied from the source location into the data virtualization layer and temporarily cached in memory. This data is then used to service the user’s request. By copying the most frequently used parts of the data set closer to the compute instances, overhead associated with data movement is reduced, and the query processing has more efficient access to the data.

For more details, refer to the following information:

- Use Amazon Athena for data
virtualization:
[Amazon Athena](https://aws.amazon.com/athena/?whats-new-cards.sort-by=item.additionalFields.postDateTime&whats-new-cards.sort-order=desc)
- Running Presto and Trino on Amazon EMR:
[Presto
and Trino](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-presto.html)

## Suggestion 15.6.2 – Reduce the ﬂow of data between application and database by implementing predicates pushdown

Filtering data by pushing down predicates as close to the storage as possible reduces the amount of data that upstream systems need to process. Query engines like Amazon Athena have query planners that leverage predicate pushdown where possible. For example, when using columnar file formats like Parquet and ORC, Athena can use metadata stored in the files to determine which sections of the files to read, effectively pushing down some predicates to the storage layer. Similarly, when querying a federated data source, Athena can push down some, but not all, predicates into the source systems. This reduces the amount of data that needs to be transferred from the source system into the query engine itself. Research the query engine you use to determine under which circumstances it is able to perform predicate pushdown, and leverage this in your application.

For more details, refer to the following information:

- Use pushdown predicated with Amazon Athena:
[Top
10 Performance Tuning Tips for Amazon Athena](https://aws.amazon.com/blogs/big-data/top-10-performance-tuning-tips-for-amazon-athena/)
- Optimizing EMR Spark with leveraging pushdown
predicates:
[Optimize
Spark performance](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-spark-performance.html)

## Suggestion 15.6.3 – Prevent data movement by leveraging pre-calculated materialized views

A materialized view can reduce the amount of data shared
between your data warehouse and reporting layers by
pre-computing the results of a pre-defined query.
Materialized views are especially useful for speeding up
queries that are predictable and repeated. Instead of
performing resource-intensive queries against large tables
(such as aggregates or multiple joins), applications can
query a materialized view and retrieve a precomputed
result set, therefore, saving on compute resource and
reducing an organization’s analytics environmental impact.

Where materialized views are not available, you can use operations such as CREATE TABLE AS (CTAS) to create pre-computed versions of queries.

For more details, refer to the following information:

- Amazon Redshift:
[Creating
materialized views in Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/dg/materialized-view-overview.html)
- Amazon Athena: [Creating a table from query results (CTAS)](https://docs.aws.amazon.com/athena/latest/ug/ctas.html)

## Suggestion 15.6.4 – Reduce the flow of data between an operational database and a data warehouse by using federated querying

A federated query allows you to directly
query data stored in external databases without data movement. This allows data
analysts, engineers, and data scientists to perform SQL
queries across data stored in relational, non-relational,
object, and custom data sources.  With federated querying,
you can submit a single SQL query and analyze data from
multiple sources running on premises or hosted in the
cloud, which reduces data latency in reporting. Federated
querying can reduce the amount of information shared
between data stores, however, the sustainability trade-off
is that your organization could transfer the same
information multiple times rather than a once-off single
bulk copy of all information on a daily basis. Your
organization should frequently review your federated
querying patterns to identify whether it’s more
sustainable to use federated query or single bulk copies.
To do this, your organization could review the amount of
data that has been queried in a week, versus calculating
the size of a full extract, and implement the approach
that processes the least amount of data.

For more details, refer to the following information:

- Amazon Redshift:
[Querying
data with federated queries in Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/dg/federated-overview.html)
- Amazon Athena:
[Using
Amazon Athena Federated Query](https://docs.aws.amazon.com/athena/latest/ug/connect-to-a-data-source.html)

## Suggestion 15.6.5 – Decrease the amount of data duplication between Amazon Redshift clusters by using data sharing

Data sharing allows an administrator to share databases, tables, and views from one Amazon Redshift cluster to another cluster without copying the underlying data. The consumer cluster can query live data, meaning changes made on the producer cluster reflect immediately on the consumer cluster. This removes the need to create, store, and keep copies of data sets up-to-date.

For more details, refer to the following information:

- Amazon Redshift:
[Amazon Redshift Data Sharing](https://aws.amazon.com/redshift/features/data-sharing/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/best-practice-15.6-prevent-unnecessary-data-movement-between-systems-and-applications..html*

---

# Best practice 15.7 – Efficiently manage your analytics infrastructure to reduce underutilized resources

Ensuring your organization has the correct amount of resource provisioned for your workload is a diﬃcult and challenging task. The common approach for ensuring your organization has the suﬃcient number of resources available for unpredicted peaks is to overprovision your resources. However, this approach generally leads to underutilization, and energy waste.

When designing your analytics workloads, consider using managed and serverless services. Managed services shift responsibility for maintaining high average utilization, and sustainability optimization of the deployed hardware, to AWS. Use managed services to distribute the sustainability impact of the service across all tenants of the service, reducing your individual contribution.

For a wider understanding of optimizing infrastructure for sustainability, refer to the
following information:

- Well-Architected Sustainability: [Optimizing your AWS Infrastructure for Sustainability, Part I: Compute](https://aws.amazon.com/blogs/architecture/optimizing-your-aws-infrastructure-for-sustainability-part-i-compute/)
- Well-Architected Sustainability: [Optimizing your AWS Infrastructure for Sustainability, Part II: Storage](https://aws.amazon.com/blogs/architecture/optimizing-your-aws-infrastructure-for-sustainability-part-ii-storage/)

**How does your organization ensure efficient infrastructure
usage?**

## Suggestion 15.7.1– Use managed and serverless services

Serverless is ideal when it is diﬃcult to predict compute needs, such as with variable workloads, periodic workloads with idle time, and steady-state workloads with spikes. These kinds of workloads are common in analytics applications. Data processing pipelines, running reports, and as-necessary queries are some examples.

Use serverless services AWS Glue ETL and Amazon EMR Serverless to run your data processing jobs and let AWS manage and optimize the underlying resources efficiently. Similarly, using Amazon Athena and Amazon Redshift Serverless for data lakes and data warehousing ensures that you only use compute resources when needed, and allow these services to optimize resource utilization behind the scenes.

For more details, refer to the following information:

- [Amazon Athena](https://aws.amazon.com/athena/)
- [AWS Glue](https://aws.amazon.com/glue/engines/)
- [Amazon Redshift Serverless](https://aws.amazon.com/redshift/redshift-serverless/)
- [Amazon EMR Serverless](https://aws.amazon.com/emr/serverless/)

## Suggestion 15.7.2– Pause your data warehouse and compute clusters when not in use

Compute resources should only be allocated when needed. If your workload cannot leverage serverless technologies, you should implement a process of stopping your compute clusters if there are periods when they will not be used (for example, during nights and weekends).

If your data warehouse uses Amazon Redshift, you can use the pause and resume feature. This retains the underlying data structures so that you can resume the cluster when needed. You can pause and resume clusters using the console, or the API, or even create a schedule that automatically pauses and resumes the cluster at set times.

Pausing data warehouse and compute clusters when not in use ensures there are fewer underutilized resources and reduces the environmental impact of your analytics workload.

For more details, refer to the following information:

- [Amazon Redshift pause and resume: Lower your costs with the new pause and resume actions on Amazon Redshift](https://aws.amazon.com/blogs/big-data/lower-your-costs-with-the-new-pause-and-resume-actions-on-amazon-redshift/)
- [Amazon Redshift pause and resume: Pausing and resuming clusters](https://docs.aws.amazon.com/redshift/latest/mgmt/managing-cluster-operations.html#rs-mgmt-pause-resume-cluster)
- [AWS Well-Architected Framework Data Analytics: Decouple storage from compute](https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/best-practice-11.1---decouple-storage-from-compute..html)

## Suggestion 15.7.3 – Scale your data warehouses and compute clusters to match demand

Only the necessary amount of compute resources should be allocated at any time. Scaling your data warehouse and compute clusters to match demand helps you maximize resource utilization, and reduce the environmental impact of your analytics workload.

For more details, refer to the following information:

- [AWS Well-Architected Framework: SUS05-BP01 Use the minimum amount of hardware to meet your needs](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_hardware_a2.html)
- AWS Well-Architected Framework Data Analytics: Best practice 11.4 – Use auto scaling where appropriate
- [Scale Amazon Redshift to meet high throughput query requirements](https://aws.amazon.com/blogs/big-data/scale-amazon-redshift-to-meet-high-throughput-query-requirements/)
- [Amazon Redshift: Elastic resize](https://docs.aws.amazon.com/redshift/latest/mgmt/managing-cluster-operations.html#elastic-resize)
- [Amazon Redshift: Working with concurrency scaling](https://docs.aws.amazon.com/redshift/latest/dg/concurrency-scaling.html)

## Suggestion 15.7.4 – Run your analytics workloads on spare capacity in your Amazon EKS environment for optimal application infrastructure usage

If you use Amazon EKS to run your applications, you can use Amazon EMR on Amazon EKS to also run your analytics workloads, such as Apache Spark jobs, on the same infrastructure. This can make it possible to increase the utilization of your existing compute resources.

For more details, refer to the following information:

- [Amazon EMR on Amazon EKS](https://aws.amazon.com/emr/features/eks/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/best-practice-15.7-efficiently-manage-your-analytics-infrastructure-to-reduce-underutilized-resources.html*

---

<!--
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
-->
