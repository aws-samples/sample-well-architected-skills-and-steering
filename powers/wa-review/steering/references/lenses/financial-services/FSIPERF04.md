**Pillar**: Performance Efficiency

# FSIPERF04: How do you select your network architecture?

Use performance requirements to drive the selection of network components and
architecture.

## FSIPERF04-BP01 Use AWS services to optimize your network routes

Proximity to data sources, both internal and external, and the distance between
components can be a key factor for financial services workloads, like high-frequency
automated trading systems, so make use of AWS services to sit your solution as close as
possible to dependencies. Where this location is outside of an AWS Region, make use of
AWS edge location solutions such as AWS Outposts and AWS Local Zones to deploy workloads
in the most suitable location, making the trade-off that not all AWS services may be
compatible with these. For example Low Latency Trading has strict latency service level
agreements (SLAs), where a millisecond can make the difference between completing a
transaction or missing an opportunity, and due to these low latency requirements, brokers'
low latency trading systems must be in close proximity to the exchanges.

Use AWS Direct Connect to provide the shortest and most reliable path to AWS resources
for components hosted outside of AWS. Use Amazon CloudFront to cache static content closer to use
cases, and AWS Global Accelerator to route connections to the closest possible source, leveraging the
AWS backbone network and bringing your solutions closer to markets, users, and data.
When using multiple AWS Regions, use Route 53 latency-based routing to serve requests from
the AWS Region with the lowest latency.

## FSIPERF04-BP02 Use Amazon EC2 instances and features to optimize your networking

Consider network performance when selecting Amazon EC2 instances, with specific network
optimized variants indicated by the n-suffix, and bare metal instances offering direct
access to the underlying host, further optimizing the networking stack.

Within an Amazon VPC, when inter-process communication latency, throughput, and consistency
is a consideration, use Amazon EC2 Placement Groups to have greater control over the location
of your virtual instances and optimize network communication, resulting in improved
network performance reduction in latency and increased packet processing rates. The use of
cluster placement groups is covered in greater detail in the[Crypto market-making latency and Amazon EC2 shared placement groups](https://aws.amazon.com/blogs/industries/crypto-market-making-latency-and-amazon-ec2-shared-placement-groups/) blog post
on optimizing market-making systems.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsiperf04.html*
