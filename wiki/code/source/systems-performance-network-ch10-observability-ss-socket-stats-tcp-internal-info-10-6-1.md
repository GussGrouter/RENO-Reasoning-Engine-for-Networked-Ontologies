# Systems Performance — Ch.10 §10.6.1 ss (scout PDF 520–640)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch10-scout-p520-640.txt` (lines **2502–2602**; file rebuilt 2026-04-20)
- Scope: socket-level workload facts + TCP “where is time going?” hints (not tool worship)

## Processed artifacts

- `processed/code/systems-performance-network-ch10-observability-ss-socket-stats-tcp-internal-info-10-6-1.md`

## Extracted ideas

- Treat **Recv-Q / Send-Q** as **queue backlog signals**: non-zero sustained queues imply **saturation somewhere** (peer consumption, kernel queues, app reads/writes)—frame as [[queueing-theory]] before naming a moral “root cause.”
- Use **limiter flags** (`app_limited`, `rwnd_limited`, `sndbuf_limited`) as **classification aids**: they describe *which constraint surface* dominated recently (app vs window vs buffer), which drives what you change (code vs tuning vs dependency).
- **Retransmits/rtt variance**: high RTO/retrans behavior is usually a **queueing/loss/congestion consequence** on the path or at endpoints; pair with interface/stack drops from [[use-method]] rather than treating “TCP is unhappy” as the story’s end.
- **Tail latency lens**: compare **minrtt** to smoothed RTT/mdev—large gaps often mean **variable queueing delay** (bad for tails even if means look fine) ([[throughput-latency-metrics]]).
- **Cross-tool correlation**: netlink-backed `ss` vs `/proc/net/*` consumers may disagree subtly on edge cases—when evidence conflicts, invoke [[measurement-validity]] as **scope/semantics** (different kernel interfaces), not drama.
- **Perturbation**: the text’s `strace ss` illustration is a reminder that **observer overhead** exists ([[instrumentation-overhead-and-perturbation]])—don’t leave `strace` on in prod.

## Decision clarity

**Decision:** choose **`ss` extended TCP internals** over deeper capture when you need **per-connection limiter classification** (app vs rwnd vs sndbuf) and queue growth signals without payload capture ([[drill-down-analysis]]).

## Application validation

- **Dependency saturation:** many open ESTAB sockets + growing **Send-Q** to one upstream IP suggests **upstream queueing / slow consumer**; confirm with interface/saturation counters before rewriting clients ([[queueing-theory]]).

## Concepts reused / refined / created

- Reused: [[counters-statistics-metrics]], [[resource-analysis-vs-workload-analysis]], [[queueing-theory]], [[throughput-latency-metrics]], [[use-method]], [[instrumentation-overhead-and-perturbation]], [[measurement-validity]], [[drill-down-analysis]], [[systems-performance]]
- Refined: none
- **Created:** none

## Links

- Concepts: [[counters-statistics-metrics]], [[resource-analysis-vs-workload-analysis]], [[queueing-theory]], [[throughput-latency-metrics]], [[use-method]], [[instrumentation-overhead-and-perturbation]], [[measurement-validity]], [[drill-down-analysis]], [[systems-performance]]
