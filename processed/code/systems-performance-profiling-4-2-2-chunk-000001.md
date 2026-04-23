4.2.2

Profiling

Profiling characterizes the target by collecting a set of samples or snapshots of its behavior. CPU
usage is a common target of profiling, where timer-based samples are taken of the instruction
pointer or stack trace to characterize CPU-consuming code paths. These samples are usually
collected at a fixed rate, such as 100 Hz (cycles per second) across all CPUs, and for a short duration such as one minute. Profiling tools, or profilers, often use 99 Hz instead of 100 Hz to avoid
sampling in lockstep with target activity, which could lead to over- or undercounting.
Profiling can also be based on untimed hardware events, such as CPU hardware cache misses or
bus activity. It can show which code paths are responsible, information that can especially help
developers optimize their code for memory usage.
Unlike fixed counters, profiling (and tracing) are typically only enabled on an as-needed basis,
since they can cost some CPU overhead to collect, and storage overhead to store. The magnitudes
of these overheads depend on the tool and the rate of events it instruments. Timer-based profilers are generally safer: the event rate is known, so its overhead can be predicted, and the event
rate can be selected to have negligible overhead.

System-Wide
System-wide Linux profilers include:
■

■

■

perf(1): The standard Linux profiler, which includes profiling subcommands.
profile(8): A BPF-based CPU profiler from the BCC repository (covered in Chapter 15, BPF)
that frequency counts stack traces in kernel context.
Intel VTune Amplifier XE: Linux and Windows profiling, with a graphical interface
including source browsing.

These can also be used to target a single process.

Per-Process
Process-oriented profilers include:
■

■

■

gprof(1): The GNU profiling tool, which analyzes profiling information added by compilers (e.g., gcc -pg).
cachegrind: A tool from the valgrind toolkit, can profile hardware cache usage (and more)
and visualize profiles using kcachegrind.
Java Flight Recorder (JFR): Programming languages often have their own special-purpose
profilers that can inspect language context. For example, JFR for Java.

See Chapter 6, CPUs, and Chapter 13, perf, for more about profiling tools.

135

136

Chapter 4 Observability Tools

