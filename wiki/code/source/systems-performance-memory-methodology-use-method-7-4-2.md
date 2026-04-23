# Systems Performance — USE method for memory (7.4.2) (PDF ~320–380 extract)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 7, **§7.4.2** — **utilization / saturation / errors** for memory; **cache-inclusive “free”** semantics; **virtual capacity**; **ECC** as error signal; **cgroups vs host RAM**

## Processed artifacts

- Scout: `processed/code/systems-performance-ch7-scout-p320-380.txt`
- Converted slice: `processed/code/systems-performance-memory-methodology-use-method-7-4-2.md`
- Chunks:
  - `processed/code/systems-performance-memory-methodology-use-method-7-4-2-chunk-000001.md`

## Extracted ideas (with classification)

- (structure) **USE for memory** still triangulates **busy vs pressure vs failure**, but **utilization** must declare **cache treatment**—“10 MB free” can coexist with **10 GB reclaimable cache** ([[utilization-and-saturation]], [[measurement-validity]], [[caching]]).
- (structure) **Quota’d guests** break **host-wide free memory** intuition—**saturation** can show while **host DRAM is idle** ([[cross-component-interactions]], [[measurement-validity]]).

## Application validation

- **Cloud VM swapping with “plenty of free” on hypervisor dashboards**: measure **guest limit + PSI inside guest**, not **host pool headroom** alone.

## Decision clarity

- **Decision**: choose **guest-side saturation + limit metrics** over **host free-memory charts** when **software caps** can starve a tenant **before** physical exhaustion.

## Concepts reused / refined / created

- Reused (heuristic): [[use-method]]
- Reused (structure): [[utilization-and-saturation]]
- Reused (abstraction): [[measurement-validity]]
- Reused (mechanism): [[caching]]
- Reused (structure): [[cross-component-interactions]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[use-method]]
  - [[utilization-and-saturation]]
  - [[measurement-validity]]
  - [[caching]]
  - [[cross-component-interactions]]
  - [[systems-performance]]
- Related sources:
  - [[systems-performance-memory-methodology-characterizing-usage-7-4-3a]]
