# Systems Performance — Ch.10 §10.4.3 Software: NIC DMA + descriptor limits (scout PDF 520–640)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch10-scout-p520-640.txt` (lines **1737–1931**; file rebuilt 2026-04-20)
- Scope: device-level saturation signals (descriptor limits)

## Processed artifacts

- `processed/code/systems-performance-network-ch10-architecture-software-nic-dma-descriptors-softirq-10-4-3g.md`

## Extracted ideas

- Descriptor exhaustion is a saturation-like limiter at the NIC/driver boundary; treat it as a queueing/bottleneck point rather than “mysterious network slow” ([[utilization-and-saturation]], [[queueing-theory]]).

## Decision clarity

**Decision:** choose **driver/NIC queue investigation** over “optimize application” when transmission pauses align with descriptor limits (device can’t drain fast enough) ([[utilization-and-saturation]]).

## Concepts reused / refined / created

- Reused: [[utilization-and-saturation]], [[queueing-theory]], [[systems-performance]]
- Refined: none
- **Created:** none

## Links

- Concepts: [[utilization-and-saturation]], [[queueing-theory]], [[systems-performance]]

