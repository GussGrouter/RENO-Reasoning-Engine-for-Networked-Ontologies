# Systems Performance — Ch.10 §10.6.12 bpftrace — event-source ladder (scout PDF 520–640)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch10-scout-p520-640.txt` (lines **3325–3735**; file rebuilt 2026-04-20)
- Scope: pick the **lowest-cost stable observation layer** that matches the hypothesis (table absorbed as workflow, not taxonomy-as-concepts)

## Processed artifacts

- `processed/code/systems-performance-network-ch10-observability-bpftrace-event-sources-table-10-6-12d.md`

## Extracted ideas

- **Layer choice is a decision primitive**: application symptoms may need uprobes; queue saturation may need qdisc/net/device probes—don’t default to packets ([[drill-down-analysis]], [[streetlight-anti-method]]).
- **Tracepoint-first** reduces brittleness across kernel versions vs wide kprobe regexes ([[event-tracing]], [[measurement-validity]] **scope/semantics** when comparing runs across kernels).

## Decision clarity

**Decision:** choose **sock/TCP tracepoints** over **skb packet hooks** when the suspected issue is **connection setup / buffer pressure**, not wire-level corruption ([[drill-down-analysis]]).

## Application validation

- **Bufferbloat at qdisc:** if stacks look fine but tails explode, move instrumentation toward **queue/discipline layers** rather than drowning in TCP payload histograms ([[queueing-theory]]).

## Concepts reused / refined / created

- Reused: [[drill-down-analysis]], [[streetlight-anti-method]], [[event-tracing]], [[measurement-validity]], [[queueing-theory]], [[extended-bpf]], [[systems-performance]]
- Refined: none
- **Created:** none

## Links

- Concepts: [[drill-down-analysis]], [[streetlight-anti-method]], [[event-tracing]], [[measurement-validity]], [[queueing-theory]], [[extended-bpf]], [[systems-performance]]
