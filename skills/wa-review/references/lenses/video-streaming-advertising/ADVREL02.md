# ADVREL02 — Latency sensitive advertising

**Pillar**: Reliability  
**Best Practices**: 3

---

# ADVREL02-BP01 To allow fast and graceful failure of latency-sensitive services, avoid exponential backing off and retry

With real-time bidding systems, your workload must handle failures
in latency-sensitive services. Traditional exponential backoff and
retry mechanisms should be avoided. Instead, opt for fast-fail
approaches and appropriate rate-limiting techniques to maintain
service responsiveness.

## Implementation guidance

Operating within 100 ms real-time bidding contracts, a single
throttle and retry of five seconds can result in many failed
bids and potentially insurmountable retry queues. Avoid this by
adapting retries to fail fast.  Regulate request rates using
algorithms, such as token buckets, leaky buckets, or fixed
window counters, or use managed service features, like Amazon API Gateway's request throttling. Rate limiting helps prevent
resource exhaustion and fairly distributes resources among
clients or services. Know the trade-offs: while rate limiting
can be an effective way to protect a service from being
overloaded, it can also potentially make the service less
reliable if not implemented carefully. For example, if the rate
limits are set too low, legitimate requests may be rejected or
delayed, leading to reduced availability or responsiveness of
the service.

## Key AWS services

- [Amazon API Gateway](https://aws.amazon.com/api-gateway/) implements the token bucket algorithm to throttle requests according to account and region limits
- [Amazon Simple Queue Service (Amazon SQS)](https://aws.amazon.com/sqs/) and Amazon Kinesis can buffer requests to smooth out the request rate
- [AWS WAF](https://aws.amazon.com/waf/) can also be used to implement rate
limiting and throttle specific API consumers

## Resources

**Related documentation:**

- [Implementing
layers of admission control](https://aws.amazon.com/builders-library/fairness-in-multi-tenant-systems/)
- [API Gateway Request Throttling](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-request-throttling.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advrel02-bp01.html*

---

# ADVREL02-BP02 Implement a caching strategy

Implementing caching strategies enhances system reliability and
performance. Evaluate different caching levels from client-side to
server-side, and explore various caching solutions, including
ElastiCache, third-party databases, and CDNs for optimizing ad
payload delivery and reducing backend load.

## Implementation guidance

Caching can be applied at various levels, such as client-side
caching of user-profiles and server-side caching for bid
enhancement. Distributed caching solutions include Amazon ElastiCache Redis or Memcached. Third-party databases such as
Aerospike, Cassandra, and Scylla Cache are also commonly
deployed for server-side caching. Ad Creative payloads are very
effectively cached by CDNs, such as CloudFront, further reducing
the load on web-servers.

## Key AWS services

- [Amazon ElastiCache](https://aws.amazon.com/elasticache/) is a fully managed in-memory
data store
- [Amazon API Gateway](https://aws.amazon.com/api-gateway/) also provides a built-in
caching layer
- [AWS Lambda](https://aws.amazon.com/lambda/), a serverless compute service, can
be used to implement caching at the application layer

## Resources

**Related documentation:**

- [Amazon ElastiCache (Memcached)](https://aws.amazon.com/elasticache/memcached/index.html)
- [Data Caching Across Microservices in a Serverless Architecture](https://aws.amazon.com/blogs/architecture/data-caching-across-microservices-in-a-serverless-architecture/index.html)
- [Caching for high-volume workloads with Amazon ElastiCache](https://aws.amazon.com/getting-started/hands-on/purpose-built-databases/elasticache/index.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advrel02-bp02.html*

---

# ADVREL02-BP03 Prevent scale mismatch of both internal services and external partners

It's important to implement proportional scaling across all system
components in advertising workloads. Balance service capacities,
particularly in DSP to SSP integrations, and use pub/sub patterns
to reliably distribute load and prevent service overload in
microservices architectures.

## Implementation guidance

Providing reliability is paramount for advertising workloads,
which can be achieved by proportionally scaling all
sub-components. For instance, when you integrate using a
PrivateLink between DSP and SSP, your partner's requests may
overwhelm your API front-end services, leading to throttling. To
mitigate this when using a microservices architecture, the
smaller services should drive larger capacity services,
preventing them from being overwhelmed. The pub/sub pattern
should also be followed wherever possible to enhance reliability
through decoupled communication and load distribution across
multiple subscribers. By implementing these measures,
advertising workloads can maintain high availability and fault
tolerance, providing a seamless and reliable experience for all
stakeholders.

## Key AWS services

- [Amazon API Gateway](https://aws.amazon.com/api-gateway/)
- [Amazon SQS](https://aws.amazon.com/sqs/)
- [Amazon Kinesis](https://aws.amazon.com/kinesis/)
- [AWS Lambda](https://aws.amazon.com/lambda/)

## Resources

- [Avoiding overload in distributed systems by putting smaller service in control](https://aws.amazon.com/builders-library/avoiding-overload-in-distributed-systems-by-putting-the-smaller-service-in-control/)
- [Pub/sub
pattern](https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-integrating-microservices/pub-sub.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advrel02-bp03.html*

---
