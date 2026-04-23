# Systems Performance — Section 3.6 Kernel Comparisons (kernel-comparisons-3-6) (PDF pages 118–170)

- Source: raw/code/pdf/Systems.Performance.Enterprise.and.the.Cloud.pdf
- Extraction base: processed/code/systems-performance-ch3-background-p118-170.txt

---

3.6 Kernel Comparisons
Which kernel is fastest? This will depend partly on the OS configuration and workload and how
much the kernel is involved. In general, I expect that Linux will outperform other kernels due to
its extensive work on performance improvements, application and driver support, and widespread
use and the large community who discover and report performance issues. The top 500 supercomputers, as tracked by the TOP500 list since 1993, became 100% Linux in 2017 [TOP500 17]. There
will be some exceptions; for example, Netflix uses Linux on the cloud and FreeBSD for its CDN.16
Kernel performance is commonly compared using micro-benchmarks, and this is error-prone.
Such benchmarks may discover that one kernel is much faster at a particular syscall, but that
syscall is not used in the production workload. (Or it is used, but with certain flags not tested by
the microbenchmark, which greatly affect performance.) Comparing kernel performance accurately is a task for a senior performance engineer—a task that can take weeks. See Chapter 12,
Benchmarking, Section 12.3.2, Active Benchmarking, as a methodology to follow.
In the first edition of this book, I concluded this section by noting that Linux did not have a
mature dynamic tracer, without which you might miss out on large performance wins. Since
that first edition, I have moved to a full-time Linux performance role, and I helped develop the
dynamic tracers that Linux was missing: BCC and bpftrace, based on extended BPF. These are
covered in Chapter 15 and in my previous book [Gregg 19].
Section 3.4.1, Linux Kernel Developments, lists many other Linux performance developments
that have occurred in the time between the first edition and this edition, spanning kernel versions 3.1 and 5.8. A major development not listed earlier is that OpenZFS now supports Linux as
its primary kernel, providing a high-performance and mature file system option on Linux.
With all this Linux development, however, comes complexity. There are so many performance
features and tunables on Linux that it has become laborious to configure and tune them for each
workload. I have seen many deployments running untuned. Bear this in mind when comparing
kernel performance: has each kernel been tuned? Later chapters of this book, and their tuning
sections, can help you remedy this.

