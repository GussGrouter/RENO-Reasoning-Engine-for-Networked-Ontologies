# Systems Performance — Ch.10 §10.6 Table 10.4 (packet capture tools) (scout PDF 520–640)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch10-scout-p520-640.txt` (lines **3839–3900**; file rebuilt 2026-04-20)
- Scope: when capture is worth its operational cost

## Processed artifacts

- `processed/code/systems-performance-network-ch10-observability-packet-capture-tools-table-10-6-c.md`

## Extracted ideas

- Capture is the “microscope” step: use it when the hypothesis requires **exact protocol behavior** (handshake anomalies, option negotiation, fragmentation behavior) that cannot be resolved from counters/traces alone ([[observability-vs-experimentation]]).
- Capture is also the easiest way to create **self-inflicted queueing**: high capture volume can perturb latency and drop behavior—treat new drops/delays during capture as **measurement-induced queueing consequences** until proven otherwise ([[instrumentation-overhead-and-perturbation]]).
- Symptom discipline still applies: **retransmits/delays on the wire** are evidence of loss/shaping/congestion dynamics; your decision is whether to **relieve a queue**, **change pacing**, or **fix negotiation**—not “tcpdump found retransmits” as the final story ([[queueing-theory]]).
- **Measurement-validity (conditional):** apply **perturbation** class reasoning when capture volume/load changes the system under study; do not default-expand into “validity essays” without a concrete conflict.

## Decision clarity

**Decision:** choose **packet capture** over **BPF summaries** when you must prove a specific wire-level behavior (options/handshake/framing) that summary tools cannot falsify ([[observability-vs-experimentation]]).

## Application validation

- **Negotiation fights:** if you suspect MTU/black-hole or odd TCP option behavior, capture becomes the fastest falsifier—after you’ve bounded interfaces with static checks so you don’t chase ghosts ([[static-performance-tuning]]).

## Concepts reused / refined / created

- Reused: [[observability-vs-experimentation]], [[instrumentation-overhead-and-perturbation]], [[queueing-theory]], [[static-performance-tuning]], [[systems-performance]]
- Refined: none
- **Created:** none

## Links

- Concepts: [[observability-vs-experimentation]], [[instrumentation-overhead-and-perturbation]], [[queueing-theory]], [[static-performance-tuning]], [[systems-performance]]
