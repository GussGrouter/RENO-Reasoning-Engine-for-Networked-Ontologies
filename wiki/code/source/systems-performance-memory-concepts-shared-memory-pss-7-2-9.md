# Systems Performance — Shared memory accounting and PSS (7.2.9) (PDF 321–360 extract)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 7, **§7.2.9** — **shared mappings** (e.g. text), **per-process RSS ambiguity**, **PSS** as proportional attribution (forward reference to tools)

## Processed artifacts

- Converted slice: `processed/code/systems-performance-memory-concepts-shared-memory-pss-7-2-9.md`
- Chunks:
  - `processed/code/systems-performance-memory-concepts-shared-memory-pss-7-2-9-chunk-000001.md`

## Extracted ideas (with classification)

- (measurement) **RSS sums “double count” shared pages**—fleet **chargeback**, **cgroup limits**, and **noisy-neighbor** stories need a declared **attribution rule** (private vs shared vs PSS) ([[measurement-validity]], [[process-abstraction]]).
- (abstraction) **PSS** is a **representation compromise**: better for **fair accounting**, still not a **latency** model ([[throughput-latency-metrics]]).

## Application validation

- **“Top memory consumers” for billing**: if processes share huge read-only mappings, **RSS ranking lies**—rerank with **PSS or private dirty** depending on **finance semantics**.

## Decision clarity

- **Decision**: choose **PSS (or explicit private/dirty split)** over **raw RSS** when **allocating DRAM cost** across tenants that **share identical text/data mappings**.

## Concepts reused / refined / created

- Reused (abstraction): [[measurement-validity]]
- Reused (abstraction): [[process-abstraction]]
- Reused (structure): [[throughput-latency-metrics]]
- Reused: [[systems-performance]]

## Links

- Concepts:
  - [[measurement-validity]]
  - [[process-abstraction]]
  - [[throughput-latency-metrics]]
  - [[systems-performance]]
- Related sources:
  - [[systems-performance-memory-terminology-7-1]]
  - [[systems-performance-memory-concepts-allocators-7-2-8]]
