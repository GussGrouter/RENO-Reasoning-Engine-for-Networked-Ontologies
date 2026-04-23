# Systems Performance — Ch.10 §10.7.2 traceroute (scout PDF 520–640)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch10-scout-p520-640.txt`
- Scope: path discovery + **what missing hops do/don’t mean**

## Processed artifacts

- `processed/code/systems-performance-network-ch10-experimentation-traceroute-ttl-path-dynamics-firewalls-10-7-2.md`

## Extracted ideas

- **Hop RTTs are samples, not SLOs**: each value is an **experimental RTT measurement** for that probe class—compare distributions (three samples) rather than treating one number as truth ([[throughput-latency-metrics]]).
- **Firewall / ICMP policy** creates **scope/semantics** risk: missing hops are often “**no signal**,” not “infinite latency” ([[measurement-validity]] **scope/semantics**).
- **Path churn** explains sudden performance shifts without app releases—tie traceroute evidence into [[static-performance-tuning]] / routing regression checks ([[cross-component-interactions]]).

## Decision clarity

**Decision:** choose **TCP-based traceroute variants** over **ICMP traceroute** when middleboxes consistently **blackhole ICMP time-exceeded** but allow application-like probes ([[measurement-validity]]).

## Application validation

- **Post-incident “route changed”:** if hop 7 alternates between two IPs mid-run, correlate with **latency tail changes** and **retransmit bursts** as **queueing-on-different-path** symptoms ([[queueing-theory]]).

## Concepts reused / refined / created

- Reused: [[throughput-latency-metrics]], [[measurement-validity]], [[static-performance-tuning]], [[cross-component-interactions]], [[queueing-theory]], [[observability-vs-experimentation]], [[systems-performance]]
- Refined: none
- **Created:** none

## Links

- Concepts: [[throughput-latency-metrics]], [[measurement-validity]], [[static-performance-tuning]], [[cross-component-interactions]], [[queueing-theory]], [[observability-vs-experimentation]], [[systems-performance]]
