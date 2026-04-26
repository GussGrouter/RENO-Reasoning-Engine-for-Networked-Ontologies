# Systems Performance — Ch.10 §10.6 Table 10.4 (BPF tracing tools) (scout PDF 520–640)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch10-scout-p520-640.txt` (lines **3839–3900**; file rebuilt 2026-04-20)
- Scope: when tracing is the right “next step” after USE + counters

## Processed artifacts

- `processed/code/systems-performance-network-ch10-observability-bpf-tracing-tools-table-10-6-b.md`

## Extracted ideas

- BPF-era tracing is the middle rung: it targets **connection-centric** questions (lifespan, top talkers, retransmits with state) and **stack internals** (drops/latency) without immediately jumping to full packet capture ([[extended-bpf]], [[event-tracing]]).
- **Retransmit traces** are best read as **evidence of loss/shaping/congestion-induced queueing**—they narrow *where* retransmissions cluster, but they do not by themselves prove *root cause* without a limiter story ([[queueing-theory]]).
- Tracing trades **lower volume than pcaps** for **higher coupling to kernel/BPF plumbing**—still a perturbation/coverage decision, just a different cost model ([[instrumentation-overhead-and-perturbation]]).
- **Measurement-validity:** not invoked by default here; use it only if you suspect the tracepoint path misrepresents the user-visible phenomenon (representation/scope risk), not because “BPF is fancy.”

## Decision clarity

**Decision:** choose **BPF TCP lifecycle/retransmit tracing** over **tcpdump** when you need retransmit correlation and connection attribution without hauling payloads ([[extended-bpf]]).

## Application validation

- **Blame isolation:** if aggregate counters show retransmits, trace-backed breakdowns help decide whether it’s **a few bad peers**, **a single dependency**, or **widespread path loss**—still a queueing story, now with better locality ([[queueing-theory]]).

## Concepts reused / refined / created

- Reused: [[extended-bpf]], [[event-tracing]], [[queueing-theory]], [[instrumentation-overhead-and-perturbation]], [[observability-vs-experimentation]], [[systems-performance]]
- Refined: none
- **Created:** none

## Links

- Concepts: [[extended-bpf]], [[event-tracing]], [[queueing-theory]], [[instrumentation-overhead-and-perturbation]], [[observability-vs-experimentation]], [[systems-performance]]
