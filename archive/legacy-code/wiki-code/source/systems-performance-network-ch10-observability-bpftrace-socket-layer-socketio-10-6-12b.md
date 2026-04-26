# Systems Performance — Ch.10 §10.6.12 bpftrace — socket layer (scout PDF 520–640)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch10-scout-p520-640.txt` (lines **3325–3735**; file rebuilt 2026-04-20)
- Scope: queues at socket boundary + trustworthy attribution patterns

## Processed artifacts

- `processed/code/systems-performance-network-ch10-observability-bpftrace-socket-layer-socketio-10-6-12b.md`

## Extracted ideas

- **`sock_rcvqueue_full` / `sock_exceed_buf_limit`** are explicit **socket-buffer queue saturation** signals—drops here propagate as **retransmits/tails** downstream ([[queueing-theory]]).
- **State-change tracepoints** underpin tools like `tcplife`—same abstract lesson: prefer **lower-rate state events** when possible ([[event-tracing]]).
- Struct parsing adds **brittleness** across kernels/architectures (endianness): treat as [[measurement-validity]] **representation** risk when scripts hardcode layouts.

## Decision clarity

**Decision:** choose **syscall + `sock:*` tracepoints** over **deep TCP kprobes** when the question is **which app fills buffers / accepts slowly** ([[drill-down-analysis]]).

## Application validation

- **Growing receive-side latency:** if `sock_rcvqueue_full` fires for a DB port, you’re usually in **consumer/read speed vs buffer** territory—tails worsen when queues stay near full ([[queueing-theory]]).

## Concepts reused / refined / created

- Reused: [[queueing-theory]], [[event-tracing]], [[drill-down-analysis]], [[measurement-validity]], [[extended-bpf]], [[systems-performance]]
- Refined: none
- **Created:** none

## Links

- Concepts: [[queueing-theory]], [[event-tracing]], [[drill-down-analysis]], [[measurement-validity]], [[extended-bpf]], [[systems-performance]]
