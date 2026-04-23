# Systems Performance — Operations are not equal (§8.3.13) (scout PDF 398–460)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: **§8.3.13** — op mix dominates outcomes; **Table 8.2 omitted** (micro-benchmark latencies)

## Processed artifacts

- Scout: `processed/code/systems-performance-ch8-scout-p398-460.txt`
- Converted slice: `processed/code/systems-performance-filesystems-ch8-ops-not-equal-8-3-13.md`
- Chunks: `processed/code/systems-performance-filesystems-ch8-ops-not-equal-8-3-13-chunk-000001.md`

## Extracted ideas (with classification)

- (measurement) **Ops/sec without op mix is low-validity throughput**—same rate can be cache hits or disk misses ([[counters-statistics-metrics]], [[measurement-validity]], [[throughput-latency-metrics]]).
- (method) **Micro-benchmark op families** to learn **local FS CPU software cost** vs device ([[micro-benchmarking]]).

## Application validation

- **Dashboard: “500 FS ops/s”:** split **`open` vs `read` vs `stat` vs `write`**—metadata-heavy layers need different fixes than streaming reads.

## Decision clarity

- **Decision:** choose **decomposing operation-type counters / latency histograms by syscall** over **raising peak ops/sec targets** when **tail latency is bad but average op rate looks healthy**.

## Concepts reused / refined / created

- Reused: [[counters-statistics-metrics]], [[measurement-validity]], [[throughput-latency-metrics]], [[micro-benchmarking]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[counters-statistics-metrics]], [[measurement-validity]], [[throughput-latency-metrics]], [[micro-benchmarking]], [[systems-performance]]
- Related sources: [[systems-performance-filesystems-ch8-special-timestamps-capacity-8-3-14-16]]
