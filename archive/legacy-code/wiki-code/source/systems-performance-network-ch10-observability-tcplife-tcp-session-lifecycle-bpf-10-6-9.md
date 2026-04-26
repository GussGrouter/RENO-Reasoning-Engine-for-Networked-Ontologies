# Systems Performance — Ch.10 §10.6.9 tcplife (scout PDF 520–640)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch10-scout-p520-640.txt` (lines **3186–3239**; file rebuilt 2026-04-20)
- Scope: connection-centric observability at **event rates far below packet rates**

## Processed artifacts

- `processed/code/systems-performance-network-ch10-observability-tcplife-tcp-session-lifecycle-bpf-10-6-9.md`

## Extracted ideas

- **Flow duration + bytes** separates **chatty short flows** from **bulk long flows**—a workload-shape input for capacity and tail-risk planning ([[resource-analysis-vs-workload-analysis]]).
- **State-change tracing vs packet capture** trades wire fidelity for **cost**: fewer events usually means less **perturbation** risk than full capture ([[instrumentation-overhead-and-perturbation]], [[observability-vs-experimentation]]).
- Long-lived flows with tiny bytes vs huge bytes both inform **queueing**: bulk transfers stress **persistent queues**; micro flows stress **handshake/churn** resources ([[queueing-theory]]).

## Decision clarity

**Decision:** choose **session lifecycle summaries** over **packet capture** when you need **who connects where, how long, how much transferred** without reconstructing packets ([[extended-bpf]]).

## Application validation

- **Dependency hunt:** filter `tcplife` to a service port to see whether tail latency correlates with **a few huge peer flows** vs **many tiny calls**—that changes whether you optimize batching or connection churn ([[cross-component-interactions]]).

## Concepts reused / refined / created

- Reused: [[extended-bpf]], [[resource-analysis-vs-workload-analysis]], [[instrumentation-overhead-and-perturbation]], [[observability-vs-experimentation]], [[queueing-theory]], [[cross-component-interactions]], [[systems-performance]]
- Refined: none
- **Created:** none

## Links

- Concepts: [[extended-bpf]], [[resource-analysis-vs-workload-analysis]], [[instrumentation-overhead-and-perturbation]], [[observability-vs-experimentation]], [[queueing-theory]], [[cross-component-interactions]], [[systems-performance]]
