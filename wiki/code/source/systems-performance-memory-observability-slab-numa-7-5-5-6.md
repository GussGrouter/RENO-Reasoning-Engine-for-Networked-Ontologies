# Systems Performance — slabtop + numastat (§7.5.5–§7.5.6) (PDF scout 320–380)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 7, **§7.5.5–§7.5.6** — **slabtop** kernel slab caches + **numastat** NUMA locality

## Processed artifacts

- Scout: `processed/code/systems-performance-ch7-scout-p320-380.txt`
- Converted slice: `processed/code/systems-performance-memory-observability-slab-numa-7-5-5-6.md`
- Chunks: `processed/code/systems-performance-memory-observability-slab-numa-7-5-5-6-chunk-000001.md`

## Extracted ideas (with classification)

- (structure) **Slab growth is kernel-side footprint**, often mistaken for **application heap** when only RSS/top are watched—**attribute layer** before blaming user code ([[resource-vs-implementation-bottleneck]], [[cross-component-interactions]]).
- (measurement) **numa_hit vs miss / foreign**: low hit ratio motivates **topology-aware placement**, not faster DIMMs alone ([[measurement-validity]], caching / locality tie to existing memory architecture sources).

## Application validation

- **Kernel RSS ballooning after a new FS workload:** rank **slab caches** before rewriting app caches—**ext4/dentry** dominance suggests **metadata path**, not malloc.

## Decision clarity

- **Decision:** choose **slab/slabtop + kmem accounting review** over **application heap profiling** when **kernel cache names dominate growth** and **user RSS is flat**.

## Concepts reused / refined / created

- Reused (structure): [[resource-vs-implementation-bottleneck]], [[cross-component-interactions]]
- Reused (measurement): [[measurement-validity]]
- Reused: [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[resource-vs-implementation-bottleneck]], [[cross-component-interactions]], [[measurement-validity]], [[systems-performance]]
- Related sources: [[systems-performance-memory-observability-sar-7-5-4]], [[systems-performance-memory-observability-ps-top-pmap-7-5-7-9]]
