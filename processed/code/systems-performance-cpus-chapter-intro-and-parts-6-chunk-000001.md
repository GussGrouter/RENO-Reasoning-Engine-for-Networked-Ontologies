[Rudolph 18] Rudolph, J., “perf-map-agent,” https://github.com/jvm-profiling-tools/
perf-map-agent, last updated 2018.
[Schwartz 18] Schwartz, E., “Dynamic Optimizations for SBCL Garbage Collection,”
11th European Lisp Symposium, https://european-lisp-symposium.org/static/proceedings/
2018.pdf, 2018.
[Axboe 19] Axboe, J., “Efficient IO with io_uring,” https://kernel.dk/io_uring.pdf, 2019.
[Gregg 19] Gregg, B., BPF Performance Tools: Linux System and Application Observability,
Addison-Wesley, 2019.
[Apdex 20] Apdex Alliance, “Apdex,” https://www.apdex.org, accessed 2020.
[Golang 20] “Why goroutines instead of threads?” Golang documentation, https://golang.org/
doc/faq#goroutines, accessed 2020.
[Gregg 20b] Gregg, B., “BPF Performance Tools,” https://github.com/brendangregg/
bpf-perf-tools-book, last updated 2020.
[Gregg 20c] Gregg, B., “jmaps,” https://github.com/brendangregg/FlameGraph/blob/master/
jmaps, last updated 2020.
[Linux 20e] “RCU Concepts,” Linux documentation, https://www.kernel.org/doc/html/
latest/RCU/rcu.html, accessed 2020.
[Microsoft 20] “Procmon Is a Linux Reimagining of the Classic Procmon Tool from the
Sysinternals Suite of Tools for Windows,” https://github.com/microsoft/ProcMon-for-Linux,
last updated 2020.
[Molnar 20] Molnar, I., and Bueso, D., “Generic Mutex Subsystem,” Linux documentation,
https://www.kernel.org/doc/Documentation/locking/mutex-design.rst, accessed 2020.
[Node.js 20] “Node.js,” http://nodejs.org, accessed 2020.
[Pangin 20] Pangin, A., “async-profiler,” https://github.com/jvm-profiling-tools/
async-profiler, last updated 2020.


Chapter 6
CPUs

CPUs drive all software and are often the first target for systems performance analysis. This
chapter explains CPU hardware and software, and shows how CPU usage can be examined in
detail to look for performance improvements.
At a high level, system-wide CPU utilization can be monitored, and usage by process or thread
can be examined. At a lower level, the code paths within applications and the kernel can be
profiled and studied, as well as CPU usage by interrupts. At the lowest level, CPU instruction
execution and cycle behavior can be analyzed. Other behaviors can also be investigated, including scheduler latency as tasks wait their turn on CPUs, which degrades performance.
The learning objectives of this chapter are:
■

Understand CPU models and concepts.

■

Become familiar with CPU hardware internals.

■

Become familiar with CPU scheduler internals.

■

Follow different methodologies for CPU analysis.

■

Interpret load averages and PSI.

■

Characterize system-wide and per-CPU utilization.

■

Identify and quantify issues of scheduler latency.

■

Perform CPU cycle analysis to identify inefficiencies.

■

Investigate CPU usage using profilers and CPU flame graphs.

■

Identify soft and hard IRQ CPU consumers.

■

Interpret CPU flame graphs and other CPU visualizations.

■

Become aware of CPU tunable parameters.

This chapter has six parts. The first three provide the basis for CPU analysis, and the last three
show its practical application to Linux-based systems. The parts are:
■

Background introduces CPU-related terminology, basic models of CPUs, and key CPU
performance concepts.


