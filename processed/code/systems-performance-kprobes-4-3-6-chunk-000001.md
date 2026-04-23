for making them available. A disabled tracepoint becomes a small number of instructions: for
x86_64 it is a 5-byte no-operation (nop) instruction. There is also a tracepoint handler added
to the end of the function, which increases its text size a little. While these overheads are very
small, they are something you should analyze and understand when adding tracepoints to the
kernel.

Tracepoint Documentation
The tracepoints technology is documented in the kernel source under Documentation/trace/
tracepoints.rst. The tracepoints themselves are (sometimes) documented in the header files that
define them, found in the Linux source under include/trace/events. I summarized advanced

4.3 Observability Sources

tracepoint topics in BPF Performance Tools, Chapter 2 [Gregg 19]: how they are added to kernel
code, and how they work at the instruction level.
Sometimes you may wish to trace software execution for which there are no tracepoints: for that
you can try the unstable kprobes interface.

4.3.6

kprobes

kprobes (short for kernel probes) is a Linux kernel event source for tracers based on dynamic
instrumentation, a term introduced in Chapter 1, Introduction, Section 1.7.3, Tracing. kprobes
can trace any kernel function or instruction, and were made available in Linux 2.6.9, released in
2004. They are considered an unstable API because they expose raw kernel functions and arguments that may change between kernel versions.
kprobes can work in different ways internally. The standard method is to modify the instruction
text of running kernel code to insert instrumentation where needed. When instrumenting the
entry of functions, an optimization may be used where kprobes make use of existing Ftrace
function tracing, as it has lower overhead.7
kprobes are important because they are a last-resort8 source of virtually unlimited information
about kernel behavior in production, which can be crucial for observing performance issues that
are invisible to other tools. They can be used by the tracers introduced in Section 4.5, Tracing
Tools, and are covered in depth in Chapters 13 to 15.
kprobes and tracepoints are compared in Table 4.3.

Table 4.3

kprobes to tracepoints comparison

Detail

kprobes

Tracepoints

Type

Dynamic

Static

Rough Number of Events

50,000+

1,000+

Kernel Maintenance

None

Required

Disabled Overhead

None

Tiny (NOPs + metadata)

Stable API

No

Yes

kprobes can trace the entry to functions as well as instruction offsets within functions. The
use of kprobes creates kprobe events (a kprobe-based trace event). These kprobe events only exist
when a tracer creates them: by default, the kernel code runs unmodified.

7
8

It can also be enabled/disabled via the debug.kprobes-optimization sysctl(8).

Without kprobes, the last resort option would be to modify the kernel code to add instrumentation where needed,
recompile, and redeploy.

151

152

Chapter 4 Observability Tools

kprobes Example
As an example of using kprobes, the following bpftrace command instruments the
do_ nanosleep() kernel function and prints the on-CPU process:
# bpftrace -e 'kprobe:do_nanosleep { printf("sleep by: %s\n", comm); }'
Attaching 1 probe...
sleep by: mysqld
sleep by: mysqld
sleep by: sleep
^C
#

The output shows a couple of sleeps by a process named “mysqld”, and one by “sleep” (likely
/bin/sleep). The kprobe event for do_nanosleep() is created when the bpftrace program begins
running and is removed when bpftrace terminates (Ctrl-C).

kprobes Arguments
As kprobes can trace kernel function calls, it is often desirable to inspect the arguments to the
function for more context. Each tracing tool exposes them in its own way and is covered in later
sections. For example, using bpftrace to print the second argument to do_nanosleep(), which is
the hrtimer_mode:
# bpftrace -e 'kprobe:do_nanosleep { printf("mode: %d\n", arg1); }'
Attaching 1 probe...
mode: 1
mode: 1
mode: 1
[...]

Function arguments are available in bpftrace using the arg0..argN built-in variable.

kretprobes
The return from kernel functions and their return value can be traced using kretprobes (short for
kernel return probes), which are similar to kprobes. kretprobes are implemented using a kprobe
for the function entry, which inserts a trampoline function to instrument the return.
When paired with kprobes and a tracer that records timestamps, the duration of a kernel function can be measured. For example, measuring the duration of do_nanosleep() using bpftrace:
# bpftrace -e 'kprobe:do_nanosleep { @ts[tid] = nsecs; }
kretprobe:do_nanosleep /@ts[tid]/ {
@sleep_ms = hist((nsecs - @ts[tid]) / 1000000); delete(@ts[tid]); }
END { clear(@ts); }'
Attaching 3 probes...

4.3 Observability Sources

^C
@sleep_ms:
[0]

1280 |@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@|

[1]

1 |

|

[2, 4)

1 |

|

[4, 8)

0 |

|

[8, 16)

0 |

|

[16, 32)

0 |

|

[32, 64)

0 |

|

[64, 128)

0 |

|

[128, 256)

0 |

|

[256, 512)

0 |

|

[512, 1K)

2 |

