# Systems Performance — Ch.9 §9.6.11 bpftrace (disk I/O latency + errors)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch9-scout-p482-560.txt` (extends prior `…-p460-520.txt` window)
- Scope: **§9.6.11** conclusion — **Disk I/O Latency** + **Disk I/O Errors** (**completes** fragments in `…-bpftrace-issue-insert-attribution-9-6-11c`)

## Processed artifacts

- `processed/code/systems-performance-disks-ch9-observability-bpftrace-latency-errors-9-6-11d.md`
- Chunks: `*-chunk-000001.md`

## Extracted ideas

- **Latency pairing:** disk completions **interrupt arbitrary threads**—so **`(dev,sector)` keys** replace **TID keys** used for **VFS** latency (**[[measurement-validity]]** **scope/semantics** vs §8 bpftrace patterns).
- **Error slice:** **`block_rq_complete`** **error≠0** path is the **USE “E”** signal at **block completion** granularity (**[[throughput-latency-metrics]]**, **[[event-tracing]]**, **[[extended-bpf]]**).

## Decision clarity

**Decision:** choose **`(dev, sector)` map keys** over **thread-ID maps** when **measuring strictly below the filesystem** where **completion isn’t paired with the submitting thread**.

## Concepts reused / refined / created

- Reused: [[measurement-validity]], [[latency-analysis]], [[extended-bpf]], [[event-tracing]], [[throughput-latency-metrics]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[measurement-validity]], [[latency-analysis]], [[extended-bpf]], [[event-tracing]], [[throughput-latency-metrics]], [[systems-performance]]
