# ADVSEC03 — Infrastructure protection

**Pillar**: Security  
**Best Practices**: 1

---

# ADVSEC03-BP01 Use distributed denial of service (DDoS) protection service to maintain platform availability

Deploying DDoS protection helps create strategies for robust
system reliability against potential threats.

## Implementation guidance

AWS Shield Standard protects against most DDoS attacks by
protecting your AWS resources. AWS Shield Standard is
automatically enabled to all AWS customer accounts by default.
AWS Shield defends against common volumetric and exhaustion
attacks and can help protect advertising endpoints such as API's
and websites. AWS Shield can protect advertisement servers or
DSPs APIs that may be accessed by advertisers and publishers
globally.

To additional features to help you protect against DDoS attacks, consider implementing
[AWS Shield Advanced](https://aws.amazon.com/shield/) to provide additional DDoS protection. Shield Advanced includes continual proactive support and increased
bandwidth to protect from DDoS attacks. Shield Advanced can
provide advanced monitoring and protection to Amazon CloudFront
distributions, Route 53 hosted zones, and Amazon ELBs.

Additionally, [AWS WAF](https://aws.amazon.com/waf/) can help protect login and provider sign-in pages
against credential stuffing or creation of fake accounts. By
deploying AWS WAF rules, companies can implement protection
against commonly deployed web-based attacks. These attacks
include bad bots and SQLi. AWS WAF helps prevent those web
requests from hitting your CloudFront edge distributions. You
can use AWS WAF to implement bad actor deny lists, which can
help prevent certain denial of service (DOS) or bad actors
trying to implement malicious ad injection.

## Resources

- [AWS Shield Advanced overview](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-advanced-summary.html)

*Source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advsec03-bp01.html*

---
