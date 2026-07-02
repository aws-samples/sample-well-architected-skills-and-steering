# ADVPERF06 — Process and culture

**Pillar**: Performance Efficiency  
**Best Practices**: 2

---

# ADVPERF06-BP01 Adopt a chipset-agnostic workload design for best availability of cloud resources and cost

Implement an x86 chip-agnostic design for workloads to optimize
the compute price of your advertising workload.

## Implementation guidance

Adtech customers that use Amazon EC2 Spot Instances may have found that Spot Instance costs
have swung between a preference towards AMD and Intel. As a result, implement a
chipset-agnostic design, and make your design configuration-based for seamless adoption and
to get the best compute price.

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advperf06-bp01.html*

---

# ADVPERF06-BP02 Optimize your intake request format (like HTTP/2 or HTTP/3) for faster processing

Use optimization in next generation networking protocols to
address low latency needs for advertising workloads.

## Implementation guidance

Implement HTTP/2 protocol, which offers features like
multiplexing (multiple requests and responses are sent over the
same TCP connection), header compression, and binary protocol.
These features improve latency and throughput.

AWS services do support HTTP/2 and HTTP/3 protocols for gains in
performance efficiency.

## Key AWS services

- [Amazon CloudFront](https://aws.amazon.com/cloudfront/)
- [Elastic Load Balancing](https://aws.amazon.com/elasticloadbalancing/)

## Resources

- [New
– HTTP/3 Support for Amazon CloudFront](https://aws.amazon.com/blogs/aws/new-http-3-support-for-amazon-cloudfront/)
- [Application Load Balancers enables gRPC workloads with end to end HTTP/2 support](https://aws.amazon.com/about-aws/whats-new/2020/10/application-load-balancers-enable-grpc-workloads-end-to-end-http-2-support/)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advperf06-bp02.html*

---
