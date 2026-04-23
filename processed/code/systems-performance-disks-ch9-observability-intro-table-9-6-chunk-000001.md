9.6

Observability Tools

This section introduces disk I/O observability tools for Linux-based operating systems. See the
previous section for strategies to follow when using them.
The tools in this section are listed in Table 9.5.

Table 9.5

Disk observability tools

Section

Tool

Description

9.6.1

iostat

Various per-disk statistics

9.6.2

sar

Historical disk statistics

9.6.3

PSI

Disk pressure stall information

9.6.4

pidstat

Disk I/O usage by process

9.6.5

perf

Record block I/O tracepoints

9.6.6

biolatency

Summarize disk I/O latency as a histogram

9.6.7

biosnoop

Trace disk I/O with PID and latency

9.6.8

iotop, biotop

Top for disks: summarize disk I/O by process

9.6.9

biostacks

Show disk I/O with initialization stacks

9.6.10

blktrace

Disk I/O event tracing

9.6.11

bpftrace

Custom disk tracing

9.6.12

MegaCli

LSI controller statistics

9.6.13

smartctl

Disk controller statistics

9.6 Observability Tools

This is a selection of tools to support Section 9.5, Methodology, beginning with traditional tools
and statistics, then tracing tools, and finally disk controller statistics. Some of the traditional
tools are likely available on other Unix-like operating systems where they originated, including:
iostat(8) and sar(1). Many of the tracing tools are BPF-based, and use BCC and bpftrace frontends
(Chapter 15); they are: biolatency(8), biosnoop(8), biotop(8), and biostacks(8).
See the documentation for each tool, including its man pages, for full references of its features.

