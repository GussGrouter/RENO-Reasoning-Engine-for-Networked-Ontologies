# Systems Performance — Ch.10 §10.8.1 system-wide tuning — discovery + example (scout PDF 520–640)

## Source

- Title: *Systems Performance: Enterprise and the Cloud* (Second Edition)
- Scout: `processed/code/systems-performance-ch10-scout-p520-640.txt` (lines **4510–4568**; file rebuilt 2026-04-20)
- Scope: **how to find knobs** + why **fleet examples aren’t recipes**

## Processed artifacts

- `processed/code/systems-performance-network-ch10-tuning-sysctl-system-wide-discovery-example-10-8-1a.md`

## Extracted ideas

- **Discovery-first** reduces blind copying: map what your kernel actually exposes before “tuning by blog post” ([[static-performance-tuning]]).
- A **14-line profile** can still be wrong elsewhere: treat as **hypothesis**, validate with **workload + regression gates** ([[resource-analysis-vs-workload-analysis]]).
- **Footnote-driven revisions** are a reminder that even experts iterate—sysctl tuning is **contextual**, not canonical ([[measurement-validity]] **scope/semantics** across fleets/kernels).

## Decision clarity

**Decision:** choose **measured A/B on canaries** over **bulk rolling Netflix-style sysctl blocks** when your kernel generation, NIC driver, and workload differ materially ([[measurement-validity]]).

## Application validation

- **Image refresh:** if a sysctl block is inherited from years ago, re-run discovery (`sysctl -a`) and compare to **current defaults** before assuming you’re still optimizing ([[static-performance-tuning]]).

## Concepts reused / refined / created

- Reused: [[static-performance-tuning]], [[resource-analysis-vs-workload-analysis]], [[measurement-validity]], [[systems-performance]]
- Refined: none
- **Created:** none

## Links

- Concepts: [[static-performance-tuning]], [[resource-analysis-vs-workload-analysis]], [[measurement-validity]], [[systems-performance]]
