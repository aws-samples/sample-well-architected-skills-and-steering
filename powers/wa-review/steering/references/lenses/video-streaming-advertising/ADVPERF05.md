# ADVPERF05 — Networking and content delivery

**Pillar**: Performance Efficiency  
**Best Practices**: 4

---

# ADVPERF05-BP01 Establish private connections between your VPC and AWS services to improve performance

A private network not only enhances the overall stability and
security of your system, but it also improves the latency and user experience
for advertising customers.

## Implementation guidance

Use [AWS PrivateLink](https://aws.amazon.com/privatelink/) to establish private connections between your
VPC and AWS services, such as Amazon S3, Amazon DynamoDB, or
Amazon ElastiCache. This approach enhances security by avoiding
the public internet and improves performance by reducing network
hops and latency.

## Resources

- [Access
AWS services through AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/privatelink-access-aws-services.html)
- [Simplify
private connectivity to Amazon DynamoDB with AWS PrivateLink](https://aws.amazon.com/blogs/database/simplify-private-connectivity-to-amazon-dynamodb-with-aws-privatelink/)
- [AWS PrivateLink for Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/privatelink-interface-endpoints.html)
- [AWS services that integrate with AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/aws-services-privatelink-support.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advperf05-bp01.html*

---

# ADVPERF05-BP02 Use edge services for static content caching and dynamic request acceleration to reduce latency and improve user experience

Edge services can accelerate requests for static content as well
as improve the response time for dynamic requests. By using the
advantages of the cloud backbone network, it can maximize the
efficiency and stability of access after requests enter the cloud.

## Implementation guidance

If your advertising workload involves serving static content,
such as images or videos, use
[Amazon CloudFront](https://aws.amazon.com/cloudfront/) to cache and deliver your content from edge
locations around the world. Amazon CloudFront reduces latency
and improves user experience for your global audience by serving
content from the nearest edge location.

## Key AWS services

- [Amazon CloudFront](https://aws.amazon.com/cloudfront/) Regional Edge Caches (RECs)
- [Amazon CloudFront](https://aws.amazon.com/cloudfront/) Points of Presence (POPs)
- [AWS Lambda@Edge](https://aws.amazon.com/lambda/edge/)

## Resources

- [Use
an Amazon CloudFront distribution to serve a static website](https://docs.aws.amazon.com/Route%C2%A053/latest/DeveloperGuide/getting-started-cloudfront-overview.html)
- [Ways
to use CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/IntroductionUseCases.html)
- [CloudFront
configuration best practices](https://docs.aws.amazon.com/whitepapers/latest/amazon-cloudfront-media/cloudfront-configuration-best-practices.html)
- [Speeding
up your website with Amazon CloudFront](https://docs.aws.amazon.com/AmazonS3/latest/userguide/website-hosting-cloudfront-walkthrough.html)
- [Customize
at the edge with Lambda@Edge](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-at-the-edge.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advperf05-bp02.html*

---

# ADVPERF05-BP03 Use load balancers to improve high availability and load distribution in your workload

Use the load balancing service provided by AWS to enhance the high
availability of applications. In the event of disruptions that cause targets to become unhealthy, load balancers can automatically exclude unhealthy targets from traffic routing.

## Implementation guidance

Elastic Load Balancing (ELB) employs various load balancing
algorithms, such as round-robin, least outstanding requests, or
IP hash, to distribute traffic evenly across healthy targets,
which optimizes resource utilization and prevents overloading of
individual targets. It supports content-based routing, which
routes traffic based on the content of the request, such as the
URL path or headers, efficiently handling different types of
requests. ELB can offload SSL/TLS decryption and encryption from
your targets, reducing the computational overhead on your
application servers and improving overall performance.

## Key AWS services

- [Amazon Elastic
Load balancer (ELB)](https://aws.amazon.com/elasticloadbalancing/)
- [Amazon Elastic Compute Cloud (EC2)](https://aws.amazon.com/ec2/)

## Resources

- [What's
the Difference Between Application, Network, and Gateway Load Balancing?](https://aws.amazon.com/compare/the-difference-between-the-difference-between-application-network-and-gateway-load-balancing/)
- [Monitor
your Application Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-monitoring.html)
- [ELB
Best Practices Guides](https://aws.github.io/aws-elb-best-practices/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advperf05-bp03.html*

---

# ADVPERF05-BP04 Provide dedicated network connection between your on-premises environment and AWS to offer high bandwidth and low latency

Use dedicated network connections to provide stable and high-speed
data communication between the on-premises data center and the AWS Cloud. This model is also applicable for connections between
multiple Regions, providing efficient and secure data
communication while effectively avoiding public network noise.

## Implementation guidance

For workloads that require high throughput or have strict
compliance requirements, consider implementing
[AWS Direct Connect](https://aws.amazon.com/directconnect/). AWS Direct Connect provides a dedicated
network connection between your on-premises environment and AWS,
offering high bandwidth, low latency, and enhanced security by
bypassing the public internet.

## Key AWS services

- [AWS PrivateLink](https://aws.amazon.com/privatelink/)

## Resources

- [AWS Direct Connect Resiliency Recommendations](https://aws.amazon.com/directconnect/resiliency-recommendation/)
- [Compliance
validation for AWS Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/DirectConnect-compliance.html)
- [Using
the AWS Direct Connect Resiliency Toolkit to get started](https://docs.aws.amazon.com/directconnect/latest/UserGuide/resiliency_toolkit.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advperf05-bp04.html*

---
