4.2.3 Tracing
Tracing instruments every occurrence of an event, and can store event-based details for later
analysis or produce a summary. This is similar to profiling, but the intent is to collect or inspect
all events, not just a sample. Tracing can incur higher CPU and storage overheads than profiling,
which can slow the target of tracing. This should be taken into consideration, as it may negatively affect the production workload, and measured timestamps may also be skewed by the
tracer. As with profiling, tracing is typically only used as needed.
Logging, where infrequent events such as errors and warnings are written to a log file for later
reading, can be thought of as low-frequency tracing that is enabled by default. Logs include the
system log.
The following are examples of system-wide and per-process tracing tools.

System-Wide
These tracing tools examine system-wide activity in the context of system software or hardware
resources, using kernel tracing facilities. Linux tools include:
■

tcpdump(8): Network packet tracing (uses libpcap)

■

biosnoop(8): Block I/O tracing (uses BCC or bpftrace)

■

execsnoop(8): New processes tracing (uses BCC or bpftrace)

■

perf(1): The standard Linux profiler, can also trace events

■

perf trace: A special perf subcommand that traces system calls system-wide

■

Ftrace: The Linux built-in tracer

■

BCC: A BPF-based tracing library and toolkit

■

bpftrace: A BPF-based tracer (bpftrace(8)) and toolkit

perf(1), Ftrace, BCC, and bpftrace are introduced in Section 4.5, Tracing Tools, and covered
in detail in Chapters 13 to 15. There are over one hundred tracing tools built using BCC and
bpftrace, including biosnoop(8) and execsnoop(8) from this list. More examples are provided
throughout this book.

Per-Process
These tracing tools are process-oriented, as are the operating system frameworks on which they
are based. Linux tools include:
■

strace(1): System call tracing

■

gdb(1): A source-level debugger

The debuggers can examine per-event data, but they must do so by stopping and starting the
execution of the target. This can come with an enormous overhead cost, making them unsuitable for production use.
System-wide tracing tools such as perf(1) and bpftrace support filters for examining a single
process and can operate with much lower overhead, making them preferred where available.

4.2 Tool Types

