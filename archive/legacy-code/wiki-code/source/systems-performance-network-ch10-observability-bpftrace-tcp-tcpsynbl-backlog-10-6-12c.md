# Systems Performance — Ch.10 §10.6.12 bpftrace — TCP + SYN backlog (scout PDF 520–640)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch10-scout-p520-640.txt` (lines **3325–3735**; file rebuilt 2026-04-20)
- Scope: backlog queues → SYN drops → tail latency via handshake retries

## Processed artifacts

- `processed/code/systems-performance-network-ch10-observability-bpftrace-tcp-tcpsynbl-backlog-10-6-12c.md`

## Extracted ideas

- **SYN drops are queueing failures** at the listener: growing backlog histograms predict **timeout/retry storms** that inflate **tail connect latency** for clients ([[queueing-theory]], [[throughput-latency-metrics]]).
- Prefer **TCP tracepoints** over wholesale `k:tcp_*` blanket probes when stability + overhead matter ([[event-tracing]] vs brute-force kprobes).
- Histogram presentation affects decisions: **log buckets distort “how close to limit” intuition**—switch representations when answering capacity questions ([[measurement-validity]] **representation**).

## Decision clarity

**Decision:** choose **backlog histogram tooling** over **aggregate SYN retransmit counters alone** when you must know **how close the listen queue operates to its limit** before drops spike ([[queueing-theory]]).

## Application validation

- **Rolling deploy causing connect spikes:** if backlog buckets pile into top ranges, expect **SYN retransmits** as clients retry—fix accept throughput / backlog sizing / upstream protection, not random TCP sysctl tweaks ([[queueing-theory]]).

## Concepts reused / refined / created

- Reused: [[queueing-theory]], [[throughput-latency-metrics]], [[event-tracing]], [[measurement-validity]], [[extended-bpf]], [[instrumentation-overhead-and-perturbation]], [[systems-performance]]
- Refined: none
- **Created:** none

## Links

- Concepts: [[queueing-theory]], [[throughput-latency-metrics]], [[event-tracing]], [[measurement-validity]], [[extended-bpf]], [[instrumentation-overhead-and-perturbation]], [[systems-performance]]
