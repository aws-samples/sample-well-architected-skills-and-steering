---
name: "wa-review"
displayName: "AWS Well-Architected Review"
description: "Perform AWS Well-Architected Framework reviews against your codebase — evaluates all 6 pillars with best-practice-level detail, produces evidence-backed findings, and generates prioritized remediation plans. Supports full reviews, quick scans, pillar-scoped assessments, and lens-specific evaluations (Serverless, GenAI, Agentic AI, Migration, and more)."
keywords: ["well-architected", "wa review", "architecture review", "security review", "reliability", "cost optimization", "performance", "sustainability", "operational excellence", "pillar", "best practices", "aws architecture", "infrastructure review", "cloud review", "WAF", "wa-review"]
author: "AWS"
---

## Onboarding

This power provides AWS Well-Architected Framework review capabilities. No external tools or credentials are required — everything runs locally by analyzing your codebase.

1. **Verify you have IaC or application code** in your project (CDK, CloudFormation, Terraform, SAM, or application code with AWS SDK usage). The review works best with infrastructure-as-code but can also assess architectures described verbally.

2. **Available review modes:**
   - Say "WA review" or "architecture review" for a full 6-pillar assessment
   - Say "review security only" or "check reliability" for a pillar-scoped review
   - Say "quick review" for a high-level scan without deep BP-level analysis
   - Mention a workload type (serverless, GenAI, migration) and the relevant lens will be applied automatically

## Steering

This power uses multiple steering files for different workflows. Kiro loads only the relevant file based on what you're doing:

| Activity | Steering file | When it activates |
|----------|--------------|-------------------|
| Full or pillar-scoped WA review | `steering/wa-review.md` | User asks for a review, assessment, or architecture health check |
| Always-on WA principles | `steering/well-architected.md` | Any architecture or design discussion — provides routing, pillars, and design principles |

## Reference Material

The power includes detailed best-practice reference files that are loaded progressively during a review (one question at a time to manage context):

- `steering/references/questions/` — 57 files, one per WA Framework question, containing all best practices with implementation guidance
- `steering/references/lenses/` — Additional lens-specific best practices (serverless, generative-ai, agentic-ai, responsible-ai, hybrid-networking, migration, devops-guidance, machine-learning, data-analytics, games-industry, saas, financial-services, life-sciences, end-user-computing, supply-chain, video-streaming-advertising, telco, sap, modern-industrial-data-technology, microsoft-workloads, connected-mobility, healthcare-industry, container-build, high-performance-computing, streaming-media, iot, government)

The agent loads these on demand — you don't need to do anything. During a full review, it works through questions sequentially: quick-scan first, then deep-dives only on questions where gaps are found.

## License and support

This power is licensed under MIT-0.

- [Privacy Policy](https://aws.amazon.com/privacy/)
- [Support](https://github.com/aws-samples/skills-and-steering-docs/issues)
