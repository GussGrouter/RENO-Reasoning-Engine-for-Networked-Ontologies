# Systems Performance — Ch.8 §8.8.1 Application calls (fadvise, madvise) (scout PDF 398–460)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: **§8.8.1** — **fsync** batching pointer; **posix_fadvise** / **madvise** (Tables 8.8–8.9 summarized in processed text)

## Processed artifacts

- Scout: `processed/code/systems-performance-ch8-scout-p398-460.txt`
- Converted slice: `processed/code/systems-performance-filesystems-ch8-application-calls-fadvise-madvise-8-8-1.md`
- Chunks: `processed/code/systems-performance-filesystems-ch8-application-calls-fadvise-madvise-8-8-1-chunk-000001.md`

## Extracted ideas (with classification)

- **Hints, not contracts:** **posix_fadvise** and **madvise** are **advice** for **prefetch and cache eligibility**; the kernel may ignore or mis-apply if workload changes ([[performance-hints]], [[caching]]).
- **Two surfaces:** file descriptor range vs **mmap** region—pick the API that matches how data is actually accessed.

## Application validation

- **Random read benchmark but SEQUENTIAL hint:** you may see **pathological prefetch** or **cache thrash**; pair hints with **page cache / device** metrics, not just app timing.

## Decision clarity

- **Decision:** choose **explicit fadvise/madvise** over **default kernel heuristics** when **access order is stable and known** (e.g. long sequential scans or “read once” cold paths) and **wrong caching is measurably expensive**.

## Concepts reused / refined / created

- Reused: [[performance-hints]], [[caching]], [[static-performance-tuning]], [[cache-tuning]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[performance-hints]], [[caching]], [[static-performance-tuning]], [[cache-tuning]], [[systems-performance]]
- Related sources: [[systems-performance-filesystems-ch8-tuning-intro-8-8]], [[systems-performance-filesystems-ch8-concept-caching-8-3-2]]
