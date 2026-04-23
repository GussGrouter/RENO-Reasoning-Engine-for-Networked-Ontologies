# Memory technology tradeoff

- Tag: tradeoff

## Definition

The **memory technology tradeoff** characterizes a recurring memory-technology boundary: SRAM is typically faster (lower access latency) but more area/cost per bit, while DRAM is typically denser/cheaper per bit but slower and operationally more complex.

## Scope note

This concept is about *choosing where state lives* in an implementation (fast/small vs slow/large), not about any particular device or networking context.

## Relation

- Constrains feasible designs when “memory access time dominates logic time”.
- A concrete instance of [[time-space-tradeoff]].
- Supports [[network-algorithmics]] by making memory technology a first-class implementation constraint.

## Links

- Source: [[network-algorithmics-2-2-4-memories-registers-sram-dram]]
- Source: [[systems-performance-memory-architecture-intro-dram-latency-7-3-1a]]
- Source: [[systems-performance-memory-architecture-ddr-multichannel-7-3-1c]]
- Related concepts:
  - [[time-space-tradeoff]]
  - [[network-algorithmics]]
  - [[throughput-latency-metrics]]
