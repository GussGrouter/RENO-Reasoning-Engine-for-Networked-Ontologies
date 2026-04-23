# Systems Performance — strace syscall latency + observer skew vs BPF (§8.6.7) (scout PDF 398–460)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: **§8.6.7 strace** — ptrace overhead + `-tt`/`-T` latency reading + FD→FS attribution

## Processed artifacts

- Scout: `processed/code/systems-performance-ch8-scout-p398-460.txt`
- Converted slice: `processed/code/systems-performance-filesystems-ch8-strace-syscall-latency-8-6-7.md`
- Chunks: `processed/code/systems-performance-filesystems-ch8-strace-syscall-latency-8-6-7-chunk-000001.md`

## Extracted ideas (with classification)

- (perturbation) **ptrace-based strace** can dominate latency—measurements may describe **the instrumented process under strace**, not production timing ([[instrumentation-overhead-and-perturbation]]).
- (representation) **Syscall latency** still targets the **syscall layer** from §8.5.2—must verify FD maps to **file**, not socket/pipe (`open` context, `/proc/.../fd`).
- (upgrade path) **BPF buffered tracers** (`ext4slower` cited) aim for **lower skew** at similar abstraction layer ([[extended-bpf]]).

## Application validation

- **Microsecond spread under strace vs BPF:** treat strace as **upper-bound pessimism** or **lab-only** unless rates are trivial.

## Decision clarity

- **Decision:** choose **BPF FS latency tools** over **long-running production strace** when **millisecond accuracy** must match **live traffic intensity**.

## Concepts reused / refined / created

- Reused: [[instrumentation-overhead-and-perturbation]], [[measurement-validity]], [[extended-bpf]], [[latency-analysis]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[instrumentation-overhead-and-perturbation]], [[measurement-validity]], [[extended-bpf]], [[latency-analysis]], [[event-tracing]], [[systems-performance]]
- Related sources: [[systems-performance-filesystems-ch8-slabtop-fs-caches-8-6-6]], [[systems-performance-filesystems-ch8-fatrace-latencytop-8-6-8-9]]
