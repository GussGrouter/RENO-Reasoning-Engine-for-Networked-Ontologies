5.4.1 CPU Profiling
CPU profiling is an essential activity for application performance analysis and is explained in
Chapter 6, CPUs, beginning with Section 6.5.4, Profiling. This section summarizes CPU profiling and CPU flame graphs, and describes how CPU profiling can be used for some off-CPU
analysis.
There are many CPU profilers for Linux, including perf(1) and profile(8), summarized in
Section 5.5, Observability Tools, both of which used timed sampling. These profilers run in
kernel mode and can capture both the kernel and user stacks, producing a mixed-mode profile.
This provides (almost) complete visibility for CPU usage.
Applications and runtimes sometimes provide their own profiler that runs in user mode, which
cannot show kernel CPU usage. These user-based profilers may have a skewed notion of CPU
time as they may be unaware of when the kernel has descheduled the application, and do not
account for it. I always start with kernel-based profilers (perf(1) and profile(8)) and use userbased ones as a last resort.
