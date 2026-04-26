# Systems Performance — Ch.10 §10.8.3 configuration tuning — MTU, aggregation, traffic class (scout PDF 520–640)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch10-scout-p520-640.txt` (lines **4492–4502**; file rebuilt 2026-04-20)
- Scope: configuration-level levers beyond sysctl/setsockopt

## Processed artifacts

- `processed/code/systems-performance-network-ch10-tuning-configuration-jumbo-lacp-firewall-dscp-10-8-3.md`

## Extracted ideas

- **Jumbo frames** are an end-to-end **compatibility constraint**: you only benefit if the whole path supports it. Treat failures as **scope/semantics** problems (“my host MTU ≠ network MTU”) rather than performance mysteries ([[measurement-validity]] **scope/semantics**).
- **Link aggregation** changes the capacity model: it’s a way to add bandwidth without changing per-link latency characteristics; it’s a “capacity intervention,” not a tail-latency fix ([[throughput-latency-metrics]]).
- **DSCP/ToS marking** is a policy handle for shared networks: it’s how you align **queueing priority** with business priority when traffic competes ([[queueing-theory]], [[resource-limits-method]]).

## Decision clarity

**Decision:** choose **DSCP/priority marking** over **blind bandwidth upgrades** when multiple traffic classes share the same links and you need predictable latency for a subset (production RPCs vs backups) ([[queueing-theory]]).

## Application validation

- If a service has stable throughput but bursty p99 during backup windows, test whether traffic-class marking + queue discipline reduces tail delays before scaling NIC bandwidth ([[queueing-theory]]).

## Concepts reused / refined / created

- Reused: [[measurement-validity]], [[throughput-latency-metrics]], [[queueing-theory]], [[resource-limits-method]], [[systems-performance]]
- Refined: none
- **Created:** none

## Links

- Concepts: [[measurement-validity]], [[throughput-latency-metrics]], [[queueing-theory]], [[resource-limits-method]], [[systems-performance]]
