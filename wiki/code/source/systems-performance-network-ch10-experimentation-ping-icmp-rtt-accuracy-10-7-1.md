# Systems Performance — Ch.10 §10.7.1 ping (scout PDF 520–640)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch10-scout-p520-640.txt`
- Scope: **ICMP RTT as an experimental signal**, not a TCP SLO substitute

## Processed artifacts

- `processed/code/systems-performance-network-ch10-experimentation-ping-icmp-rtt-accuracy-10-7-1.md`

## Extracted ideas

- **Per-sample RTTs + mdev** hint **tail risk** beyond the average—watch max/mdev when diagnosing **latency spikes** ([[throughput-latency-metrics]]).
- **Measurement-validity** applies when using ping as a stand-in for app latency: **representation** (ICMP treatment) + historical **representation** (user-space timestamp inflation) ([[measurement-validity]]).
- **Packet loss %** in the summary is **for the probe stream**—still often a **queueing/congestion consequence** on shared paths, not an app-layer root label ([[queueing-theory]]).

## Decision clarity

**Decision:** choose **TCP/TLS-layer probes or app-level checks** over **raw ICMP ping** when policy/QoS treats ICMP differently than customer traffic ([[measurement-validity]]).

## Application validation

- **“Ping is fine but app is slow”:** don’t dismiss the network—ICMP may be **de-prioritized**, hiding congestion that hurts TCP queues ([[queueing-theory]]).

## Concepts reused / refined / created

- Reused: [[throughput-latency-metrics]], [[measurement-validity]], [[queueing-theory]], [[observability-vs-experimentation]], [[systems-performance]]
- Refined: none
- **Created:** none

## Links

- Concepts: [[throughput-latency-metrics]], [[measurement-validity]], [[queueing-theory]], [[observability-vs-experimentation]], [[systems-performance]]
