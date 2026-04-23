# Systems Performance — Ch.10 §10.6.13 tcpdump (scout PDF 520–640)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch10-scout-p520-640.txt` (lines **3736–3786**; file rebuilt 2026-04-20)
- Scope: capture as a **high-cost evidence layer** + how to read capture **totals vs deltas**

## Processed artifacts

- `processed/code/systems-performance-network-ch10-observability-tcpdump-capture-filters-overhead-10-6-13.md`

## Extracted ideas

- **Kernel drops during capture** mean the **capture queue/path saturated** under offered load—treat as [[queueing-theory]] at the capture/instrumentation boundary; they can also **coexist with** (and hide) production drops elsewhere if capture perturbs timing ([[instrumentation-overhead-and-perturbation]], **perturbation** when evidence suggests it).
- **Per-packet timestamps are not throughput**: they are **event times**; delta modes help **tail/spacing** diagnosis (micro-bursts, stalls), but you still convert to rates explicitly if needed ([[throughput-latency-metrics]]).
- **Checksum “incorrect”** alongside offloads is often a **representation mismatch** between what wire capture sees vs NIC offload behavior—apply [[measurement-validity]] **representation**, not “the network flipped bits” by default.
- Prefer **short captures + BPF filters** over “run tcpdump forever” when the goal is performance work, not forensic completeness ([[observability-vs-experimentation]]).

## Decision clarity

**Decision:** choose **bounded file capture + strict BPF filter** over **unfiltered live tcpdump** when rates are high but you still need wire proof for a narrow hypothesis ([[instrumentation-overhead-and-perturbation]]).

## Application validation

- **Incidents:** if “drops by kernel” climbs while prod latency spikes, first decide whether you’re measuring **capture saturation** vs **NIC saturation** using independent interface counters—don’t merge the stories without evidence ([[use-method]]).

## Concepts reused / refined / created

- Reused: [[queueing-theory]], [[instrumentation-overhead-and-perturbation]], [[throughput-latency-metrics]], [[measurement-validity]], [[observability-vs-experimentation]], [[use-method]], [[systems-performance]]
- Refined: none
- **Created:** none

## Links

- Concepts: [[queueing-theory]], [[instrumentation-overhead-and-perturbation]], [[throughput-latency-metrics]], [[measurement-validity]], [[observability-vs-experimentation]], [[use-method]], [[systems-performance]]
