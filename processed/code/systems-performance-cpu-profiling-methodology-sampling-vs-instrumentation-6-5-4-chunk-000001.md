<!-- pdftotext -f 286 -l 320 Systems.Performance.Enterprise.and.the.Cloud.pdf (Chapter 6 CPUs §6.5 continued) -->

6.5.4 Profiling
Profiling builds a picture of the target for study. CPU profiling can be performed in different
ways, typically either:
■

Timer-based sampling: Collecting timer-based samples of the currently running
function or stack trace. A typical rate used is 99 Hertz (samples per second) per CPU. This
provides a coarse view of CPU usage, with enough detail for large and small issues. 99 is
used to avoid lock-step sampling that may occur at 100 Hertz, which would produce a
skewed profile. If needed, the timer rate can be lowered and the time span enlarged until
the overhead is negligible and suitable for production use.

247

248

Chapter 6 CPUs

■

Function tracing: Instrumenting all or some function calls to measure their duration.
This provides a fine-level view, but the overhead can be prohibitive for production use,
often 10% or more, because function tracing adds instrumentation to every function call.

Most profilers used in production, and those in this book, use timer-based sampling. This is pictured in Figure 6.14, where an application calls function A(), which calls function B(), and so on,
while stack trace samples are collected. See Chapter 3, Operating Systems, Section 3.2.7, Stacks,
for an explanation of stack traces and how to read them.

Figure 6.14 Sample-based CPU profiling
Figure 6.14 shows how samples are only collected when the process is on-CPU: two samples
show function A() on-CPU, and two samples show function B() on-CPU called by A(). The time
off-CPU during a syscall was not sampled. Also, the short-lived function C() was entirely missed
by sampling.
Kernels typically maintain two stack traces for processes: a user-level stack and a kernel stack
when in kernel context (e.g., syscalls). For a complete CPU profile, the profiler must record both
stacks when available.
Apart from sampling stack traces, profilers can also record just the instruction pointer, which
shows the on-CPU function and instruction offset. Sometimes this is sufficient for solving
issues, without the extra overhead of collecting stack traces.

Sample Processing
As described in Chapter 5, a typical CPU profile at Netflix collects user and kernel stack traces
at 49 Hertz across (around) 32 CPUs for 30 seconds: this produces a total of 47,040 samples, and
presents two challenges:
1. Storage I/O: Profilers typically write samples to a profile file, which can then be read and
examined in different ways. However, writing so many samples to the file system can
generate storage I/O that perturbs the performance of the production application. The

6.5 Methodology

BPF-based profile(8) tool solves the storage I/O problem by summarizing the samples in
kernel memory, and only emitting the summary. No intermediate profile file is used.
2. Comprehension: It is impractical to read 47,040 multi-line stack traces one by one:
summaries and visualizations must be used to make sense of the profile. A commonly
used stack trace visualization is flame graphs, some examples of which are shown in earlier
chapters (1 and 5); and there are more examples in this chapter.
Figure 6.15 shows the overall steps to generate CPU flame graphs from perf(1) and profile, solving the comprehension problem. It also shows how the storage I/O problem is solved: profile(8)
does not use an intermediate file, saving overhead. The exact commands used are listed in
Section 6.6.13, perf.

Figure 6.15 CPU flame graph generation
While the BPF-based approach has lower overhead, the perf(1) approach saves the raw samples (with timestamps), which can be reprocessed using different tools, including FlameScope
(Section 6.7.4).

Profile Interpretation
Once you have collected and summarized or visualized a CPU profile, your next task is to
understand it and search for performance problems. A CPU flame graph excerpt is shown
in Figure 6.16, and the instructions for reading this visualization are in Section 6.7.3, Flame
Graphs. How would you summarize the profile?

249

250

Chapter 6 CPUs

Figure 6.16 CPU flame graph excerpt
My method for finding performance wins in a CPU flame graphs is as follows:
1. Look top-down (leaf to root) for large “plateaus.” These show that a single function is
on-CPU during many samples, and can lead to some quick wins. In Figure 6.16, there are
two plateaus on the right, in unmap_page_range() and page_remove_rmap(), both related
to memory pages. Perhaps a quick win is to switch the application to use large pages.
2. Look bottom-up to understand the code hierarchy. In this example, the bash(1) shell was
calling the execve(2) syscall, which eventually called the page functions. Perhaps an even
bigger win is to avoid execve(2) somehow, such as by using bash builtins instead of external processes, or switching to another language.
3. Look more carefully top-down for scattered but common CPU usage. Perhaps there
are many small frames related to the same problem, such as lock contention. Inverting
the merge order of flame graphs so that they are merged from leaf to root and become
icicle graphs can help reveal these cases.
Another example of interpreting a CPU flame graph is provided in Chapter 5, Applications,
Section 5.4.1, CPU Profiling.

Further Information
The commands for CPU profiling and flame graphs are provided in Section 6.6, Observability
Tools. Also see Section 5.4.1 on CPU analysis of applications, and Section 5.6, Gotchas, which
describes common profiling problems with missing stack traces and symbols.
For the usage of specific CPU resources, such as caches and interconnects, profiling can use
PMC-based event triggers instead of timed intervals. This is described in the next section.

