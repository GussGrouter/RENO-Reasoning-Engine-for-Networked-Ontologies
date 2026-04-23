# Systems Performance — ps + top + pmap (§7.5.7–§7.5.9) (PDF scout 320–380)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 7, **§7.5.7–§7.5.9** — **RSS vs VSZ**, summing RSS pitfalls, **pmap** mappings + **PSS** semantics

## Processed artifacts

- Scout: `processed/code/systems-performance-ch7-scout-p320-380.txt`
- Converted slice: `processed/code/systems-performance-memory-observability-ps-top-pmap-7-5-7-9.md`
- Chunks: `processed/code/systems-performance-memory-observability-ps-top-pmap-7-5-7-9-chunk-000001.md`

## Extracted ideas (with classification)

- (measurement) **RSS column sums can exceed physical RAM** because of **shared mappings**—**PSS / pmap** answer “who pays” for shared libs ([[measurement-validity]], [[throughput-latency-metrics]], [[resource-analysis-vs-workload-analysis]]).
- (representation) **Extended pmap modes** change **which kernel fields appear**—**kernel-version dependent** claims need **label discipline** ([[measurement-validity]]).

## Application validation

- **Capacity plan from summing ps RSS:** replace with **PSS-aware view** or **cgroups memory.stat**—otherwise you **over-provision** for duplicated text mappings.

## Decision clarity

- **Decision:** choose **PSS-aware attribution (pmap -X/-XX or cgroup memory breakdown)** over **summing RSS across processes** when **shared libraries/mmap’d segments** dominate and **capacity math must be finance-grade**.

## Concepts reused / refined / created

- Reused (measurement): [[measurement-validity]], [[throughput-latency-metrics]]
- Reused (abstraction): [[resource-analysis-vs-workload-analysis]]
- Reused: [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[measurement-validity]], [[throughput-latency-metrics]], [[resource-analysis-vs-workload-analysis]], [[systems-performance]]
- Related sources: [[systems-performance-memory-concepts-shared-memory-pss-7-2-9]], [[systems-performance-memory-observability-perf-7-5-10]]
