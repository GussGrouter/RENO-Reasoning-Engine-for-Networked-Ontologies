# Systems Performance — Memory tuning: §7.6 opening (PDF scout 381–400)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Author: Brendan Gregg
- Raw: `raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf`
- Batch scope: Chapter 7, **§7.6** — tuning goals **before** knobs (keep workloads **resident**; avoid chronic paging/swap)

## Processed artifacts

- Scout: `processed/code/systems-performance-ch7-scout-p381-400.txt`
- Converted slice: `processed/code/systems-performance-memory-tuning-ch7-intro-7-6.md`
- Chunks: `processed/code/systems-performance-memory-tuning-ch7-intro-7-6-chunk-000001.md`

## Extracted ideas (with classification)

- (heuristic) **Primary “tuning” is often stopping pathological paging**, not sysctl shopping—validate with **§7.4/§7.5** evidence first ([[static-performance-tuning]], [[scientific-method]]).
- (scope) **Kernel version + workload shape** determine which knobs exist and whether they help—**semantics beat defaults copied from blogs** ([[measurement-validity]]).

## Application validation

- **Ticket asks for “vm tuning”:** confirm **PSI/OOM/swap timeline** exists; if not, **instrumentation/methodology** gaps dominate **sysctl** tweaks.

## Decision clarity

- **Decision:** choose **capacity or application working-set fixes** over **kernel tunable sweeps** when **methodology already shows sustained anonymous paging or cgroup limit pressure** as the dominant story.

## Concepts reused / refined / created

- Reused: [[static-performance-tuning]], [[scientific-method]], [[measurement-validity]], [[systems-performance]]
- **Created:** none

## Links

- Concepts: [[static-performance-tuning]], [[scientific-method]], [[measurement-validity]], [[systems-performance]]
- Related sources: [[systems-performance-memory-tuning-sysctl-vm-7-6-1]]
