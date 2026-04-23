■

■

■

■

■

perf(1): The official Linux profiler. It is excellent for CPU profiling (sampling of stack
traces) and PMC analysis, and can instrument other events, typically recording to an
output file for post-processing.
Ftrace: The official Linux tracer, it is a multi-tool composed of different tracing utilities. It
is suited for kernel code path analysis and resource-constrained systems, as it can be used
without dependencies.
BPF (BCC, bpftrace): Extended BPF was introduced in Chapter 3, Operating Systems,
Section 3.4.4, Extended BPF. It powers advanced tracing tools, the main ones being BCC
and bpftrace. BCC provides powerful tools, and bpftrace provides a high-level language
for custom one-liners and short programs.
SystemTap: A high-level language and tracer with many tapsets (libraries) for tracing
different targets [Eigler 05][Sourceware 20]. It has recently been developing a BPF backend,
which I recommend (see the stapbpf(8) man page).
LTTng: A tracer optimized for black-box recording: optimally recording many events for
later analysis [LTTng 20].

The first three tracers are covered in Chapter 13, perf; Chapter 14, Ftrace; and Chapter 15, BPF. The
chapters that now follow (5 to 12) include various uses of these tracers, showing the commands
to type and how to interpret the output. This ordering is deliberate, focusing on uses and performance wins first, and then covering the tracers in more detail later if and as needed.
At Netflix, I use perf(1) for CPU analysis, Ftrace for kernel code digging, and BCC/bpftrace for
everything else (memory, file systems, disks, networking, and application tracing).

4.6 Observing Observability

4.6

Observing Observability

Observability tools and the statistics upon which they are built are implemented in software,
and all software has the potential for bugs. The same is true for the documentation that describes
the software. Regard with a healthy skepticism any statistics that are new to you, questioning
what they really mean and whether they are really correct.
Metrics may be subject to any of the following problems:
■

Tools and measurements are sometimes wrong.

■

Man pages are not always right.

■

Available metrics may be incomplete.

■

Available metrics may be poorly designed and confusing.

■

Metric collectors (e.g., that parse tool output) can have bugs.13

■

Metric processing (algorithms/spreadsheets) can also introduce errors.

When multiple observability tools have overlapping coverage, you can use them to cross-check
