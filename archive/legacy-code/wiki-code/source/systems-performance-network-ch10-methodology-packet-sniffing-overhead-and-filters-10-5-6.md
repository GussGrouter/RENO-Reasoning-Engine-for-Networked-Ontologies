# Systems Performance — Ch.10 §10.5.6 Packet sniffing (scout PDF 520–640)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch10-scout-p520-640.txt` (lines **2279–2328**; file rebuilt 2026-04-20)
- Scope: packet capture as high-fidelity, high-cost evidence

## Processed artifacts

- `processed/code/systems-performance-network-ch10-methodology-packet-sniffing-overhead-and-filters-10-5-6.md`

## Extracted ideas

- Packet capture is observational but can impose significant overhead; treat it as a constrained experiment on production, and interpret drops as part of the evidence ([[observability-vs-experimentation]], [[instrumentation-overhead-and-perturbation]]).

## Decision clarity

**Decision:** choose **short, filtered capture** over “capture everything” when you need protocol truth but must minimize overhead and storage risk ([[instrumentation-overhead-and-perturbation]]).

## Concepts reused / refined / created

- Reused: [[observability-vs-experimentation]], [[instrumentation-overhead-and-perturbation]], [[extended-bpf]], [[systems-performance]]
- Refined: none
- **Created:** none

## Links

- Concepts: [[observability-vs-experimentation]], [[instrumentation-overhead-and-perturbation]], [[extended-bpf]], [[systems-performance]]

