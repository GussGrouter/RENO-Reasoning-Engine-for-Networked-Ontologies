# Systems Performance — Ch.10 §10.6 Observability tools (intro + Table 10.4) (scout PDF 520–640)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch10-scout-p520-640.txt` (lines **3839–3900**; file rebuilt 2026-04-20)
- Scope: observability sequencing and “what class of evidence am I buying?”

## Processed artifacts

- `processed/code/systems-performance-network-ch10-observability-tools-intro-table-10-6.md`

## Extracted ideas

- Treat the tool list as a **ladder of evidence cost**: start with statistics that answer “how much / how saturated / where queued,” escalate to tracing for **per-connection lifecycle and retransmit attribution**, and reserve capture for when you need payload-adjacent truth ([[observability-vs-experimentation]], [[instrumentation-overhead-and-perturbation]]).
- The chapter explicitly orders tools from **traditional** to **BPF tracing** to **packet capture**—this is an anti-[[streetlight-anti-method]] pattern: pick the family that matches the suspected failure mode, not the tool you know best, and treat the ladder as a [[drill-down-analysis]] sequence (cheap evidence first).
- **Retransmits/drops/latency spikes** belong in the **queueing consequence** bucket until you’ve identified the limiting queue (NIC/driver/OS/policy/path) ([[queueing-theory]]).
- **Measurement-validity:** not forced here; deprecation/status differences are mostly about **feature coverage and maintainership**, not a live metric conflict.

## Decision clarity

**Decision:** choose **socket/stack counters** over **packet capture** when the question is backlog/concurrency/saturation and you still need cheap, low-perturbation signal ([[instrumentation-overhead-and-perturbation]]).

## Application validation

- **Incident triage:** if dashboards show elevated TCP retransmits, treat that as “a queue is hurting” and move left-to-right on the ladder until you can name *which* queue—before capturing full traffic ([[queueing-theory]]).

## Concepts reused / refined / created

- Reused: [[observability-vs-experimentation]], [[instrumentation-overhead-and-perturbation]], [[streetlight-anti-method]], [[queueing-theory]], [[drill-down-analysis]], [[systems-performance]]
- Refined: none
- **Created:** none

## Links

- Concepts: [[observability-vs-experimentation]], [[instrumentation-overhead-and-perturbation]], [[streetlight-anti-method]], [[queueing-theory]], [[drill-down-analysis]], [[systems-performance]]
