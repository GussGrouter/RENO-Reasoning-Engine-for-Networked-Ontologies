# Systems Performance — Ch.10 §10.4.3 Software: drivers/NAPI/coalescing (scout PDF 520–640)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch10-scout-p520-640.txt` (lines **1737–1931**; file rebuilt 2026-04-20)
- Scope: batching tradeoffs and driver-queue bottlenecks

## Processed artifacts

- `processed/code/systems-performance-network-ch10-architecture-software-device-drivers-napi-coalescing-10-4-3f.md`

## Extracted ideas

- Coalescing is a throughput/latency knob: batch interrupts for throughput; reduce batching for latency-sensitive workloads ([[throughput-latency-metrics]], [[queueing-theory]]).
- Driver queues are queueing points; use backlog reasoning before attributing “network latency” to the WAN path ([[queueing-theory]]).

## Decision clarity

**Decision:** choose **reduce coalescing / use low-latency receive mode** over “add CPU” when latency sensitivity dominates and evidence suggests batching delay rather than saturation ([[throughput-latency-metrics]]).

## Concepts reused / refined / created

- Reused: [[throughput-latency-metrics]], [[queueing-theory]], [[utilization-and-saturation]], [[systems-performance]]
- Refined: none
- **Created:** none

## Links

- Concepts: [[throughput-latency-metrics]], [[queueing-theory]], [[utilization-and-saturation]], [[systems-performance]]

