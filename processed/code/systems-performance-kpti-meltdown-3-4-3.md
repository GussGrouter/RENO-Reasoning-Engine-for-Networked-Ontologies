# Systems Performance — Section 3.4.3 KPTI (Meltdown) (kpti-meltdown-3-4-3) (PDF pages 118–170)

- Source: raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf
- Extraction base: processed/code/systems-performance-ch3-background-p118-170.txt

---

3.4.3 KPTI (Meltdown)
The kernel page table isolation (KPTI) patches added to Linux 4.14 in 2018 are a mitigation for
the Intel processor vulnerability called “meltdown.” Older Linux kernel versions had KAISER
patches for a similar purpose, and other kernels have employed mitigations as well. While these
work around the security issue, they also reduce processor performance due to extra CPU cycles
and additional TLB flushing on context switches and syscalls. Linux added process-context ID
(PCID) support in the same release, which allows some TLB flushes to be avoided, provided the
processor supports pcid.
I evaluated the performance impact of KPTI as between 0.1% and 6% for Netflix cloud production workloads, depending on the workload’s syscall rate (higher costs more) [Gregg 18a].
Additional tuning will further reduce the cost: the use of huge pages so that a flushed TLB
warms up faster, and using tracing tools to examine syscalls to identify ways to reduce their rate.
A number of such tracing tools are implemented using extended BPF.

