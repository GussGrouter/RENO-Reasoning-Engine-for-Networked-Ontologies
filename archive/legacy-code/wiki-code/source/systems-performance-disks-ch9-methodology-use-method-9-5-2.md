# Systems Performance — Ch.9 §9.5.2 USE method (disks) (scout PDF 460–520)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch9-scout-p460-520.txt`
- Scope: **USE** on **disks**, **controllers**, **transports**

## Processed artifacts

- `processed/code/systems-performance-disks-ch9-methodology-use-method-9-5-2.md`

## Extracted ideas

- **USE** extends to **non-time util** on controllers; **virtual disk** breaks naive **U** ([[use-method]], [[utilization-and-saturation]], [[cross-component-interactions]]).

## Decision clarity

**Decision:** choose **controller+transport summation / limiting tests** over **per-LUN `iostat` only** when **throughput plateaus** independent of workload mix.

## Concepts reused / refined / created

- Reused: [[use-method]], [[utilization-and-saturation]], [[counters-statistics-metrics]], [[measurement-validity]], [[cross-component-interactions]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[use-method]], [[utilization-and-saturation]], [[counters-statistics-metrics]], [[measurement-validity]], [[cross-component-interactions]], [[systems-performance]]
