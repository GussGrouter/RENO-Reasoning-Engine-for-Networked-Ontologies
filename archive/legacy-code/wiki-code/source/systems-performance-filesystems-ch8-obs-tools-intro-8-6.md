# Systems Performance — File system observability tools intro (§8.6) (scout PDF 398–460)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: **§8.6** opening — **Table 8.6 omitted** (tool index); **traditional vs BPF** toolchain split

## Processed artifacts

- Scout: `processed/code/systems-performance-ch8-scout-p398-460.txt`
- Converted slice: `processed/code/systems-performance-filesystems-ch8-obs-tools-intro-8-6.md`
- Chunks: `processed/code/systems-performance-filesystems-ch8-obs-tools-intro-8-6-chunk-000001.md`

## Extracted ideas (with classification)

- (method ladder) Same methodology chapter as §8.5—tools are **servants** of the investigation order; mixing **counter-era** utilities with **BPF-era** tracers is normal if validity is tracked ([[drill-down-analysis]], [[measurement-validity]]).
- (architecture) **BCC/bpftrace front ends** name several FS-focused probes—signals **extended BPF** as the low-overhead path vs classic ptrace tracing ([[extended-bpf]]).

## Application validation

- When choosing instrumentation for FS latency, prefer the stack’s **documented low-overhead hooks** over whatever happens to be installed—tool familiarity ([[streetlight-anti-method]]) should not override **perturbation class**.

## Decision clarity

- **Decision:** choose **BPF-based FS latency tools** over **ptrace strace as primary evidence** when **production-like rates** matter and **observer skew** would falsify milliseconds claims.

## Concepts reused / refined / created

- Reused: [[extended-bpf]], [[instrumentation-overhead-and-perturbation]], [[drill-down-analysis]], [[streetlight-anti-method]], [[measurement-validity]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[extended-bpf]], [[instrumentation-overhead-and-perturbation]], [[drill-down-analysis]], [[measurement-validity]], [[systems-performance]]
- Related sources: [[systems-performance-filesystems-ch8-table-8-5-expectations]], [[systems-performance-filesystems-ch8-mount-free-8-6-1-2]]
