# Incident Investigation Patterns

## Triage Decision Tree

```
New Incident
│
├── Is it during a maintenance window?
│   ├── YES + Severity LOW/MEDIUM → Skip (expected disruption)
│   └── YES + Severity HIGH/CRITICAL → Investigate (unexpected impact)
│
├── Is it a known recurring issue with auto-remediation?
│   ├── YES + Auto-remediation triggered → Monitor for resolution
│   └── YES + Auto-remediation failed → Escalate immediately
│
├── Is customer impact confirmed?
│   ├── YES → Severity HIGH minimum, begin RCA
│   └── NO → Assess blast radius, monitor for 5 minutes
│
└── Is the root cause obvious from alarm context?
    ├── YES → Proceed to mitigation
    └── NO → Begin systematic investigation (RCA skill)
```

## Root Cause Analysis Framework

### Step 1: Timeline reconstruction

Build a timeline correlating:
- Deployment events (CodeDeploy, CloudFormation)
- Configuration changes (Config, Parameter Store)
- Scaling events (Auto Scaling, ECS)
- Alarm state changes (CloudWatch)
- Error rate changes (ALB, API Gateway)

### Step 2: Blast radius assessment

Determine scope:
- Single resource vs. fleet-wide?
- Single AZ vs. multi-AZ?
- Single service vs. cascading?
- Single customer vs. all traffic?

### Step 3: Hypothesis-driven investigation

For each hypothesis:
1. State the hypothesis clearly
2. Identify the evidence that would confirm/deny it
3. Gather the evidence (metrics, logs, traces)
4. Evaluate: confirmed, denied, or inconclusive
5. If inconclusive, refine hypothesis

### Step 4: Common root cause patterns

| Pattern | Indicators | Investigation Path |
|---------|------------|-------------------|
| Deployment failure | Error spike correlates with deploy time | Check CodeDeploy events, compare with canary metrics |
| Capacity exhaustion | Gradual degradation, quota errors | Check CPU/memory/connections, service quotas |
| Dependency failure | Elevated latency/errors to downstream | Check dependency health, circuit breaker state |
| Configuration change | Sudden behavior change, no deploy | Check Config history, Parameter Store changes |
| Data issue | Specific operations failing | Check data integrity, recent migrations |
| Network issue | Intermittent connectivity, AZ-specific | Check VPC Flow Logs, NLB health, DNS |
| Certificate/secret expiry | Authentication failures, TLS errors | Check ACM, Secrets Manager rotation dates |

## Mitigation Playbooks

### Playbook: Rollback deployment

**When to use:** Error rate or latency increased after deployment  
**Risk:** LOW — reverting to known-good state

1. Confirm deployment correlation (errors started within deployment window)
2. Check if rollback is safe (no database migrations that prevent rollback)
3. Trigger rollback via CodeDeploy or ECS task definition revert
4. Monitor error rate for 5 minutes post-rollback
5. Verify: error rate returns to pre-deploy baseline

### Playbook: Scale up capacity

**When to use:** Resource utilization above 85%, scaling events failing  
**Risk:** LOW — adding capacity

1. Confirm capacity is the bottleneck (CPU, memory, or connections near limit)
2. Check if Auto Scaling is blocked (quota, launch template, AZ capacity)
3. Manually increase desired count or instance size
4. Monitor utilization decrease
5. Verify: latency and error rate recover

### Playbook: Failover to secondary

**When to use:** Primary resource unhealthy, secondary available  
**Risk:** MEDIUM — traffic shift may have side effects

1. Confirm primary is truly unhealthy (not a false alarm)
2. Verify secondary is healthy and has capacity
3. Initiate failover (Route 53 health check, RDS failover, Aurora failover)
4. Monitor secondary for increased load
5. Verify: customer-facing metrics recover
6. Plan: investigate and recover primary

### Playbook: Circuit breaker activation

**When to use:** Downstream dependency failing, causing cascade  
**Risk:** MEDIUM — degraded experience for affected features

1. Confirm downstream is the source (elevated latency/errors to dependency)
2. Verify circuit breaker configuration exists
3. Force-open circuit breaker if not triggering automatically
4. Serve fallback/cached response where possible
5. Monitor: upstream error rate should stabilize
6. Plan: close circuit breaker when dependency recovers

### Playbook: Traffic shift away from AZ

**When to use:** AZ-localized failures  
**Risk:** MEDIUM — remaining AZs must handle full load

1. Confirm issue is AZ-specific (cross-reference with AWS Health events)
2. Verify remaining AZs have capacity for full load
3. Remove unhealthy AZ from ALB target group or adjust Route 53 weights
4. Monitor remaining AZs for overload
5. Verify: overall error rate and latency recover
6. Plan: re-add AZ when issue resolves

## Post-Incident Review Template

```markdown
## Incident Summary
- **Date/Time**: {UTC start} — {UTC end}
- **Duration**: {total time}
- **Severity**: {SEV level}
- **Impact**: {customer-facing impact description}

## Timeline
| Time (UTC) | Event |
|------------|-------|
| {time} | {what happened} |

## Root Cause
{Clear, specific explanation of what failed and why}

## Detection
- **How detected**: {alarm, customer report, automated check}
- **Time to detect (MTTD)**: {duration}
- **Could we have detected faster?**: {yes/no + how}

## Mitigation
- **Actions taken**: {what was done to restore service}
- **Time to mitigate (MTTM)**: {duration}
- **Could we have mitigated faster?**: {yes/no + how}

## Action Items
| Action | Owner | Priority | Due Date |
|--------|-------|----------|----------|
| {preventive action} | {team/person} | {P1/P2/P3} | {date} |

## Lessons Learned
- {What went well}
- {What didn't go well}
- {What was lucky}
```
