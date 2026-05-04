one in every ten thousands requests. This is sufficient to analyze the performance of the bulk
of the requests, but it may make the analysis of intermittent errors or outliers difficult due to
limited data. Some distributed tracers are tail-based, where all events are first captured and then
a decision is made as to what to keep, perhaps based on latency and errors.
Once a problematic service has been identified, it can be analyzed in more detail using other
methodologies and tools.

5.5

Observability Tools

This section introduces application performance observability tools for Linux-based operating
systems. See the previous section for strategies to follow when using them.
The tools in this section are listed in Table 5.3 along with a description of how these tools are
used in this chapter.

199


200

Chapter 5 Applications

Table 5.3

Linux application observability tools

Section

Tool

Description

5.5.1

perf

CPU profiling, CPU flame graphs, syscall tracing

5.5.2

profile

CPU profiling using timed sampling

5.5.3

offcputime

Off-CPU profiling using scheduler tracing

5.5.4

strace

Syscall tracing

5.5.5

execsnoop

New process tracing

5.5.6

syscount

Syscall counting

5.5.7

bpftrace

Signal tracing, I/O profiling, lock analysis


