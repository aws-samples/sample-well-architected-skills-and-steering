# MSFTCOST04 — Databases

**Pillar**: Cost Optimization  
**Best Practices**: 3

---

# MSFTCOST04-BP01 Use caching to enhance SQL Server workloads

Caching in .NET applications reduces costs and improves performance
by storing frequently accessed data, lowering the load on backend
databases like SQL Server. While especially useful for read-heavy
operations, choose a caching method that fits your needs,
considering that local caching has scalability limitations. Evaluate
the trade-off between performance gains and caching costs when
implementing your strategy.

**Desired outcome:** Implement an
effective caching strategy for our .NET applications with SQL Server
backends to reduce database load, cut costs, and improve
performance. This tailored approach will optimize workloads and
initiate our application modernization efforts, balancing
performance gains with implementation costs.

**Common anti-patterns:**

- Over-Caching: Caching all data indiscriminately without
considering data volatility or access patterns. This leads to
stale data issues, increased memory consumption, and potentially
higher costs than direct database queries would incur.
- Local Cache Sprawl: Implementing isolated local caches across
multiple application instances without a coherent invalidation
strategy, resulting in data inconsistencies, increased
maintenance overhead, and poor scalability in distributed
environments.

**Benefits of establishing this best
practice:**

- Reduced load on SQL Server instances leads to lower database
sizing requirements and decreased infrastructure costs, as fewer
resources are needed to handle the same workload volume.
- Faster application response times through immediate access to
cached data, eliminating repetitive database queries and
reducing network latency for frequently accessed information.

**Level of risk exposed if this best practice
is not established:** Low

## Implementation guidance

Identify frequently accessed, static data for caching. Use
distributed caching solutions like Redis for scalability.
Implement robust cache invalidation to maintain data freshness.
Apply cache-aside pattern for seamless database fallback.
Regularly monitor cache hit rates and performance metrics to
optimize your strategy as your application evolves.

### Implementation steps

- Configure a distributed cache service (like Redis) and
integrate it with your .NET application using appropriate
client libraries and connection strings
- Implement cache-aside pattern in your data access layer,
wrapping database calls with cache checks and updates using
appropriate timeouts and invalidation logic
- Set up monitoring for cache performance metrics (hit rates,
memory usage, latency) using Application Insights or similar
tools to validate and optimize caching effectiveness

## Resources

**Related documents:**

- [Use
caching to reduce database demand](https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/net-caching.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftcost04-bp01.html*

---

# MSFTCOST04-BP02 Consider Babelfish for Amazon Aurora PostgreSQL

Babelfish is an Amazon Aurora PostgreSQL feature that allows SQL
Server client applications to connect directly to PostgreSQL
databases. It works by understanding SQL Server's TDS protocol and
common SQL statements, providing a dedicated endpoint for SQL Server
connections. This functionality enables organizations to migrate
from SQL Server to PostgreSQL while maintaining application
compatibility and minimizing the need for code modifications.

**Desired outcome:** By implementing
Babelfish for Amazon Aurora PostgreSQL, we aim to efficiently
migrate our SQL Server-based applications while minimizing
development effort, reducing migration costs, and maintaining
application compatibility. This will enable a smoother transition to
PostgreSQL without extensive code refactoring.

**Common anti-patterns:**

- Complete rewrite approach: Unnecessarily rewriting entire
applications to migrate from SQL Server to PostgreSQL, instead
of leveraging Babelfish's compatibility features. This approach
often leads to extended project timelines, increased costs, and
potential introduction of new bugs.
- Ignoring dialect differences: Assuming full SQL Server
compatibility and neglecting to test and adjust for specific
T-SQL features not supported by Babelfish. This can result in
unexpected behavior or errors in production after migration.

**Benefits of establishing this best
practice:**

- Reduces costs and complexity by minimizing code changes when
transitioning from SQL Server to PostgreSQL, accelerating the
migration process.
- Enables quick transition to Amazon Aurora PostgreSQL while
maintaining application compatibility, allowing organizations to
leverage cloud benefits with minimal disruption.

**Level of risk exposed if this best practice
is not established:** Low

## Implementation guidance

Begin by identifying SQL Server applications suitable for
Babelfish migration and assess their T-SQL compatibility using the
Babelfish Compass tool. Create a test environment to validate
application functionality with Babelfish-enabled Amazon Aurora
PostgreSQL cluster, focusing on critical database operations and
stored procedures. Implement the migration in phases, starting
with non-critical applications, and maintain detailed
documentation of any required code adjustments or workarounds for
unsupported features.

### Implementation steps

- Assess application compatibility using the Babelfish Compass
tool or the AWS Schema Convertion Tool.
- Set up a Babelfish-enabled Amazon Aurora PostgreSQL cluster
and configure the TDS listener port.
- Modify application connection strings to point to the
Babelfish endpoint instead of the SQL Server instance.
- Test thoroughly, focusing on critical database operations,
stored procedures, and application functionality before
migrating production workloads.

## Resources

**Related documents:**

- [Using
Babelfish for Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish.html)
- [Migrating
a SQL Server database to Babelfish for Aurora
PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/babelfish-migration.html)
- [Prepare
for Babelfish migration with the AWS SCT assessment
report](https://aws.amazon.com/blogs/database/prepare-for-babelfish-migration-with-the-aws-sct-assessment-report/)

**Related tools:**

- [Babelfish
Compass](https://github.com/babelfish-for-postgresql/babelfish_compass)
- [What
is the AWS Schema Conversion Tool?](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Welcome.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftcost04-bp02.html*

---

# MSFTCOST04-BP03 Consider purpose-built databases

Purpose-built databases are gaining traction among businesses
adopting modern architectures like microservices, as they can
precisely accommodate specific data access patterns. These
databases, whether SQL or NoSQL, offer application teams benefits
like reduced costs, enhanced scalability, and improved resilience.
By selecting the right database for each specific use case, teams
can optimize their data management while leveraging cloud advantages
for more efficient solutions.

**Desired outcome:** By adopting
purpose-built databases tailored to specific workload requirements,
application teams will optimize data management, reduce costs, and
enhance scalability and resilience. This approach will lead to more
efficient cloud-based solutions, whether using SQL or NoSQL
databases, and minimize undifferentiated heavy lifting in database
operations.

**Common anti-patterns:**

- Using a single database technology for all applications and
workloads, regardless of their specific data access patterns or
requirements. This can lead to suboptimal performance,
scalability issues, and increased costs.
- Adopting multiple specialized databases for every minor
variation in data needs, resulting in a fragmented and overly
complex data architecture that increases management overhead and
potentially negates cost savings.

**Benefits of establishing this best
practice:**

- Purpose-built databases are designed to handle specific data
access patterns, resulting in improved query performance and
overall system efficiency tailored to each application's unique
needs.
- By choosing databases that align closely with workload
requirements, organizations can avoid over-provisioning
resources and reduce unnecessary licensing costs associated with
general-purpose database solutions.
- Purpose-built databases often come with built-in features for
horizontal scaling and high availability, making it easier for
applications to handle growth in data volume and user traffic
while maintaining robust performance and reliability.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Begin by analyzing your application's data access patterns, query
requirements, and scalability needs. Identify distinct workload
characteristics across your application portfolio and map them to
appropriate purpose-built database solutions. For new
applications, design the data architecture with these specific
requirements in mind from the start. For existing applications,
consider a phased migration approach, starting with the components
that would benefit most from purpose-built databases. Evaluate AWS
purpose-built database options such as Amazon DynamoDB for
high-performance NoSQL needs, Amazon RDS for traditional
relational workloads, or Amazon Redshift for data warehousing,
ensuring each choice aligns with both technical requirements and
cost optimization goals.

### Implementation steps

- Analyze current data access patterns and requirements across
your application portfolio
- Identify suitable purpose-built database solutions for each
distinct workload
- Develop a migration strategy, prioritizing components that
will benefit most from the change
- Implement and test the new database solutions in a staging
environment
- Gradually migrate production workloads, monitoring
performance and costs throughout the process

## Resources

**Related documents:**

- [Consider
purpose-built databases](https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/net-purpose.html)

**Related tools:**

- [What
is the AWS Schema Conversion Tool?](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Welcome.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftcost04-bp03.html*

---
