# Systems Performance — mount flags + free cache accounting (§8.6.1–§8.6.2) (scout PDF 398–460)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: **§8.6.1 mount** + **§8.6.2 free** (**ASCII tables trimmed** in processed extract)

## Processed artifacts

- Scout: `processed/code/systems-performance-ch8-scout-p398-460.txt`
- Converted slice: `processed/code/systems-performance-filesystems-ch8-mount-free-8-6-1-2.md`
- Chunks: `processed/code/systems-performance-filesystems-ch8-mount-free-8-6-1-2-chunk-000001.md`

## Extracted ideas (with classification)

- (static signal) **`mount`** exposes **mount-time behavior knobs** (example **relatime**)—metadata write amplification tradeoffs visible without workload replay ([[static-performance-tuning]]).
- (representation) **`free`** separates **buffers vs page cache** in wide mode and surfaces **MemAvailable** semantics—counts answer **“RAM usable without swap pressure,”** not “unused pages” ([[measurement-validity]], [[caching]]).

## Application validation

- **Unexpected `atime` traffic:** confirm **`relatime`/`noatime`** vs workload assumptions before blaming SSD firmware—often a **mount-flag** fix.

## Decision clarity

- **Decision:** choose **inspecting `mount` + `MemAvailable` / meminfo** over **raw “used memory”** when **FS cache pressure and reclaim** feed into **app OOM or throttling** questions.

## Concepts reused / refined / created

- Reused: [[static-performance-tuning]], [[caching]], [[measurement-validity]], [[counters-statistics-metrics]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[static-performance-tuning]], [[caching]], [[measurement-validity]], [[counters-statistics-metrics]], [[use-method]], [[systems-performance]]
- Related sources: [[systems-performance-filesystems-ch8-obs-tools-intro-8-6]], [[systems-performance-filesystems-ch8-top-vmstat-8-6-3-4]]
