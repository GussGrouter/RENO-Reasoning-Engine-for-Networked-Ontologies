# Systems Performance — Main memory utilization and saturation (7.2.7) (PDF 321–360 extract)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 7, **§7.2.7** — **DRAM utilization** (cache reclaimable), **saturation** (paging / OOM / swap activity), **virtual capacity** limits vs **overcommit**

## Processed artifacts

- Converted slice: `processed/code/systems-performance-memory-concepts-utilization-saturation-7-2-7.md`
- Chunks:
  - `processed/code/systems-performance-memory-concepts-utilization-saturation-7-2-7-chunk-000001.md`

## Extracted ideas (with classification)

- (structure) **Memory saturation** is signaled by **reclaim/paging/OOM**, not only **bytes used**—the same chapter explicitly excludes **reclaimable cache** from the “used vs pressure” panic ([[utilization-and-saturation]], [[caching]]).
- (measurement) **“Available swap” naming** for virtual headroom is a **semantics trap**—do not map it to **disk swap device idle** without tool definitions ([[measurement-validity]], [[virtual-memory-abstraction]]).

## Application validation

- **SLO breach + high used RAM**: check **scan rate / PSI / swap-in** before scaling **DRAM**—you may be saturating **reclaim throughput**, not lacking **bytes**.

## Decision clarity

- **Decision**: choose **saturation-side signals (reclaim, swap-in, OOM, PSI)** over **used/total DRAM alone** when deciding whether memory is the **bottleneck** class for **tail latency**.

## Concepts reused / refined / created

- Reused (structure): [[utilization-and-saturation]]
- Reused (mechanism): [[caching]]
- Reused (abstraction): [[measurement-validity]]
- Reused (abstraction): [[virtual-memory-abstraction]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[utilization-and-saturation]]
  - [[caching]]
  - [[measurement-validity]]
  - [[virtual-memory-abstraction]]
  - [[systems-performance]]
- Related sources:
  - [[systems-performance-memory-concepts-filesystem-cache-usage-7-2-6]]
  - [[systems-performance-memory-concepts-overcommit-7-2-4]]
