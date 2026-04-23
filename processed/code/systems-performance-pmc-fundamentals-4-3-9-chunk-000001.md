JIT-compiled languages such as Java, which usually compiles on the fly. A solution to this is

155

156

Chapter 4 Observability Tools

dynamic USDT, which precompiles probes as a shared library, and provides an interface to call
them from the JIT-compiled language. Dynamic USDT libraries exist for Java, Node.js, and other
languages. Interpreted languages have a similar problem and need for dynamic USDT.
USDT probes are implemented in Linux using uprobes: see the previous section for a description
of uprobes and their overhead. In addition to the enabled overhead, USDT probes place nop
instructions in the code, as do tracepoints.
USDT probes can be used by the tracers introduced in Section 4.5, Tracing Tools, covered in
depth in Chapters 13 to 15 (although using USDT with Ftrace requires some extra work).

USDT Documentation
If an application makes USDT probes available, they should be documented in the application’s
documentation. I summarized advanced USDT topics in BPF Performance Tools, Chapter 2 [Gregg
19]: how USDT probes can be added to application code, how they work internally, and dynamic
USDT.

4.3.9

Hardware Counters (PMCs)

The processor and other devices commonly support hardware counters for observing activity.
The main source are the processors, where they are commonly called performance monitoring
counters (PMCs). They are known by other names as well: CPU performance counters (CPCs),
performance instrumentation counters (PICs), and performance monitoring unit events (PMU events).
These all refer to the same thing: programmable hardware registers on the processor that provide low-level performance information at the CPU cycle level.
PMCs are a vital resource for performance analysis. Only through PMCs can you measure the
efficiency of CPU instructions, the hit ratios of CPU caches, the utilization of memory and device
buses, interconnect utilization, stall cycles, and so on. Using these to analyze performance can
lead to various performance optimizations.

PMC Examples
While there are many PMCs, Intel have selected seven as an “architectural set,” which provide
a high-level overview of some core functions [Intel 16]. The presence of these architectural set
PMCs can be checked using the cpuid instruction. Table 4.4 shows this set, which serves as an
example set of useful PMCs.

Table 4.4

Intel architectural PMCs

Event Name

UMask

Event
Select

Example Event Mask Mnemonic

UnHalted Core Cycles

00H

3CH

CPU_CLK_UNHALTED.THREAD_P

Instruction Retired

00H

C0H

INST_RETIRED.ANY_P

UnHalted Reference Cycles

01H

3CH

CPU_CLK_THREAD_UNHALTED.REF_XCLK

LLC References

4FH

2EH

LONGEST_LAT_CACHE.REFERENCE

4.3 Observability Sources

Event Name

UMask

Event
Select

Example Event Mask Mnemonic

LLC Misses

41H

2EH

LONGEST_LAT_CACHE.MISS

Branch Instruction Retired

00H

C4H

BR_INST_RETIRED.ALL_BRANCHES

Branch Misses Retired

00H

C5H

BR_MISP_RETIRED.ALL_BRANCHES

As an example of PMCs, if you run the perf stat command without specifying events (no -e),
it defaults to instrumenting the architectural PMCs. For example, the following runs perf stat
on the gzip(1) command:
# perf stat gzip words
Performance counter stats for 'gzip words':
156.927428

task-clock (msec)

#

0.987 CPUs utilized

1

context-switches

#

0.006 K/sec

0

cpu-migrations

#

0.000 K/sec

page-faults

#

0.835 K/sec

209,911,358

cycles

#

1.338 GHz

288,321,441

instructions

#

66,240,624

branches

#

1,382,627

branch-misses

#

131

1.37

insn per cycle

422.110 M/sec
2.09% of all branches

0.159065542 seconds time elapsed

The raw counts are the first column; after a hash are some statistics, including an important
