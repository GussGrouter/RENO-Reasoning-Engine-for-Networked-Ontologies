# Systems Performance — opensnoop (§8.6.10) (scout PDF 398–460)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: **§8.6.10** — trace **`open`/`openat`** only (sample output trimmed in processed extract)

## Processed artifacts

- Scout: `processed/code/systems-performance-ch8-scout-p398-460.txt`
- Converted slice: `processed/code/systems-performance-filesystems-ch8-opensnoop-8-6-10.md`
- Chunks: `processed/code/systems-performance-filesystems-ch8-opensnoop-8-6-10-chunk-000001.md`

## Extracted ideas (with classification)

- **Discoverability:** enumerate config/log/data paths during startup or incidents—useful when docs drift ([[event-tracing]] as workload-discovery).
- **Rate assumption:** opens are usually sparse → expected **low tracing tax** versus syscall-wide taps ([[extended-bpf]]).

## Application validation

- **“Where does MySQL read `my.cnf` from on *this* build?”**—`opensnoop` answers with live paths; use **failed-open** mode when hunting missing files in deploys.

## Decision clarity

- **Decision:** choose **opens open-syscall tracing** over **read(2) volume counts** when **the risk is wrong path / missing file / open storm**, not byte throughput.

## Concepts reused / refined / created

- Reused: [[event-tracing]], [[extended-bpf]], [[drill-down-analysis]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[event-tracing]], [[extended-bpf]], [[drill-down-analysis]], [[systems-performance]]
- Related sources: [[systems-performance-filesystems-ch8-fatrace-latencytop-8-6-8-9]], [[systems-performance-filesystems-ch8-filetop-8-6-11]]
