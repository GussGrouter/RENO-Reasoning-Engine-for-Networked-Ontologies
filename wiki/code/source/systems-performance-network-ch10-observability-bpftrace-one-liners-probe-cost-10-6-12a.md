# Systems Performance — Ch.10 §10.6.12 bpftrace — one-liners + cost (scout PDF 520–640)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch10-scout-p520-640.txt` (lines **3325–3735**; file rebuilt 2026-04-20)
- Scope: purposeful tracing (avoid “measure everything TCP” traps)

## Processed artifacts

- `processed/code/systems-performance-network-ch10-observability-bpftrace-one-liners-probe-cost-10-6-12a.md`

## Extracted ideas

- **Probe fan-out = overhead + skew risk**: wildly broad attachments can dominate CPU and distort latency—prefer stable tracepoints/targeted probes when hypotheses exist ([[instrumentation-overhead-and-perturbation]], **perturbation**).
- **Attribution warnings**: deep send/recv kprobes may attribute work to **wrong PID/comm** relative to connection owner → [[measurement-validity]] **representation** risk when blaming processes from those counters alone.
- Pattern: start from **syscall/socket layer** when you need reliable process identity ([[extended-bpf]], [[event-tracing]]).

## Decision clarity

**Decision:** choose **syscall/tracepoint-targeted bpftrace** over **`k:*sendmsg/*recvmsg` hot kprobes** when you primarily need **which application** opened/moved traffic ([[measurement-validity]]).

## Application validation

- **Blame-game incident:** if bpftrace maps implicate an unrelated daemon, widen scope—likely **wrong execution context**, not malicious traffic ([[measurement-validity]]).

## Concepts reused / refined / created

- Reused: [[extended-bpf]], [[event-tracing]], [[instrumentation-overhead-and-perturbation]], [[measurement-validity]], [[systems-performance]]
- Refined: none
- **Created:** none

## Links

- Concepts: [[extended-bpf]], [[event-tracing]], [[instrumentation-overhead-and-perturbation]], [[measurement-validity]], [[systems-performance]]
