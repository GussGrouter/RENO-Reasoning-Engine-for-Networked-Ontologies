8.6.8 fatrace
fatrace(1) is a specialized tracer that uses the Linux fanotify API (file access notify).

(Omitted in this processed extract: multi-line sample — see PDF.)

Each line shows the process name, PID, type of event, full path, and optional status. The type of
event can be opens (O), reads (R), writes (W), and closes (C). fatrace(1) can be used for workload
characterization: understanding the files accessed, and looking for unnecessary work that could
be eliminated.
However, for a busy file system workload, fatrace(1) can produce tens of thousands of lines of
output every second, and can cost significant CPU resources. This may be alleviated somewhat
by filtering to one type of event. BPF-based tracing tools, including opensnoop(8) (Section 8.6.10),
also greatly reduce overhead.

8.6.9 LatencyTOP
LatencyTOP is a tool for reporting sources of latency, aggregated system-wide and per process.
File system latency is reported by LatencyTOP.

(Omitted in this processed extract: ASCII example table — see PDF.)

The upper section is the system-wide summary, and the bottom is for a single gzip(1) process,
which is compressing a file. Most of the latency for gzip(1) is due to Reading from file at
70.2%, with 27.2% in synchronous write as the new compressed file is written.
LatencyTOP was developed by Intel, but it has not been updated in a while, and its website is
no longer online. It also requires kernel options that are not commonly enabled. You may find
it easier to measure file system latency using BPF tracing tools instead: see Sections 8.6.13 to
8.6.15.
