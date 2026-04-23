# Systems Performance — Ch.10 §10.7.6 tc / netem (scout PDF 520–640)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch10-scout-p520-640.txt`
- Scope: **intentional loss** as a controlled queueing experiment (lab), not a prod “fix”

## Processed artifacts

- `processed/code/systems-performance-network-ch10-experimentation-tc-netem-loss-lab-10-7-6.md`

## Extracted ideas

- Injected loss increases **retransmits and tail latency** as **queueing consequences** on the shaped path—useful to validate **timeout/retry behavior** and **app sensitivity** under controlled conditions ([[queueing-theory]]).
- **`tc -s` drops are cumulative counters** for that qdisc lifetime—compute **rates** via deltas or time windows ([[counters-statistics-metrics]]).
- This is explicitly **perturbation** of production traffic if applied on real interfaces—treat as [[instrumentation-overhead-and-perturbation]] / lab-only unless you fully isolate blast radius.

## Decision clarity

**Decision:** choose **netem in a dedicated test netns/VM** over **netem on a shared prod NIC** when you need loss injection without creating uncontrolled cross-team outages ([[instrumentation-overhead-and-perturbation]]).

## Application validation

- **Chaos testing:** validate circuit breakers by injecting **1% loss** and watch whether **p99** explodes due to **retry storms** (queueing feedback), not just mean error rate ([[throughput-latency-metrics]]).

## Concepts reused / refined / created

- Reused: [[queueing-theory]], [[counters-statistics-metrics]], [[instrumentation-overhead-and-perturbation]], [[throughput-latency-metrics]], [[observability-vs-experimentation]], [[systems-performance]]
- Refined: none
- **Created:** none

## Links

- Concepts: [[queueing-theory]], [[counters-statistics-metrics]], [[instrumentation-overhead-and-perturbation]], [[throughput-latency-metrics]], [[observability-vs-experimentation]], [[systems-performance]]
