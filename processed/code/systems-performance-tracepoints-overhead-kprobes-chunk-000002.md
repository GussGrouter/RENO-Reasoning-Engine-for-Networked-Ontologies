# systems-performance-tracepoints-overhead-kprobes (chunk 000002)

Tracepoint Documentation
      The tracepoints technology is documented in the kernel source under Documentation/trace/
      tracepoints.rst. The tracepoints themselves are (sometimes) documented in the header files that
      define them, found in the Linux source under include/trace/events. I summarized advanced
                                                                                    4.3 Observability Sources      151

tracepoint topics in BPF Performance Tools, Chapter 2 [Gregg 19]: how they are added to kernel
code, and how they work at the instruction level.

Sometimes you may wish to trace software execution for which there are no tracepoints: for that
you can try the unstable kprobes interface.

4.3.6         kprobes
kprobes (short for kernel probes) is a Linux kernel event source for tracers based on dynamic
instrumentation, a term introduced in Chapter 1, Introduction, Section 1.7.3, Tracing. kprobes
can trace any kernel function or instruction, and were made available in Linux 2.6.9, released in
2004. They are considered an unstable API because they expose raw kernel functions and argu-
ments that may change between kernel versions.

kprobes can work in different ways internally. The standard method is to modify the instruction
text of running kernel code to insert instrumentation where needed. When instrumenting the
entry of functions, an optimization may be used where kprobes make use of existing Ftrace
function tracing, as it has lower overhead.7

kprobes are important because they are a last-resort8 source of virtually unlimited information
about kernel behavior in production, which can be crucial for observing performance issues that
are invisible to other tools. They can be used by the tracers introduced in Section 4.5, Tracing
Tools, and are covered in depth in Chapters 13 to 15.

kprobes and tracepoints are compared in Table 4.3.

Table 4.3        kprobes to tracepoints comparison
Detail                                   kprobes             Tracepoints
Type                                     Dynamic             Static
Rough Number of Events                   50,000+             1,000+
Kernel Maintenance                       None                Required
Disabled Overhead                        None                Tiny (NOPs + metadata)
Stable API                               No                  Yes

kprobes can trace the entry to functions as well as instruction offsets within functions. The
use of kprobes creates kprobe events (a kprobe-based trace event). These kprobe events only exist
when a tracer creates them: by default, the kernel code runs unmodified.

7
    It can also be enabled/disabled via the debug.kprobes-optimization sysctl(8).
8
 Without kprobes, the last resort option would be to modify the kernel code to add instrumentation where needed,
recompile, and redeploy.
152   Chapter 4 Observability Tools

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

When paired with kprobes and a tracer that records timestamps, the duration of a kernel func-
      tion can be measured. For example, measuring the duration of do_nanosleep() using bpftrace:

# bpftrace -e 'kprobe:do_nanosleep { @ts[tid] = nsecs; }
           kretprobe:do_nanosleep /@ts[tid]/ {
           @sleep_ms = hist((nsecs - @ts[tid]) / 1000000); delete(@ts[tid]); }
           END { clear(@ts); }'
      Attaching 3 probes...
                                                                     4.3 Observability Sources       153

^C

@sleep_ms:
[0]                    1280 |@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@|
[1]                       1 |                                                             |
[2, 4)                    1 |                                                             |
[4, 8)                    0 |                                                             |
[8, 16)                   0 |                                                             |
[16, 32)                  0 |                                                             |
[32, 64)                  0 |                                                             |
[64, 128)                 0 |                                                             |
[128, 256)                0 |                                                             |
[256, 512)                0 |                                                             |
[512, 1K)                 2 |                                                             |

The output shows that do_nanosleep() was usually a fast function, returning in zero milliseconds
(rounded down) 1,280 times. Two occurrences reached the 512 to 1024 millisecond range.

bpftrace syntax is explained in Chapter 15, BPF, which includes a similar example for timing
vfs_read().

kprobes Interface and Overhead
The kprobes interface is similar to tracepoints. There is a way to instrument them via /sys files,
via the perf_event_open(2) syscall (which is preferred), and also via the register_kprobe() kernel
API. The overhead is similar to that of tracepoints when the entries to functions are traced
(Ftrace method, if available), and higher when function offsets are traced (breakpoint method)
or when kretprobes are used (trampoline method). For a particular system I measured the min-
imum kprobe CPU cost to be 76 nanoseconds, and the minimum kretprobe CPU cost to be 212
nanoseconds [Gregg 19].

kprobes Documentation
kprobes are documented in the Linux source under Documentation/kprobes.txt. The kernel
functions they instrument are typically not documented outside of the kernel source (since most
are not an API, they don’t need to be). I summarized advanced kprobe topics in BPF Performance
Tools, Chapter 2 [Gregg 19]: how they work at the instruction level.

4.3.7      uprobes
uprobes (user-space probes) are similar to kprobes, but for user-space. They can dynamically
instrument functions in applications and libraries, and provide an unstable API for diving deep
into software internals beyond the scope of other tools. uprobes were made available in Linux 3.5,
released in 2012.

uprobes can be used by the tracers introduced in Section 4.5, Tracing Tools, and covered in
depth in Chapters 13 to 15.
154   Chapter 4 Observability Tools

uprobes Example
      As an example of uprobes, the following bpftrace command lists possible uprobe function entry
      locations in the bash(1) shell:

# bpftrace -l 'uprobe:/bin/bash:*'
      uprobe:/bin/bash:rl_old_menu_complete
      uprobe:/bin/bash:maybe_make_export_env
      uprobe:/bin/bash:initialize_shell_builtins
      uprobe:/bin/bash:extglob_pattern_p
      uprobe:/bin/bash:dispose_cond_node
      uprobe:/bin/bash:decode_prompt_string
      [..]

The full output showed 1,507 possible uprobes. uprobes instrument code and create uprobe events
      when needed (a uprobe-based trace event): the user-space code runs unmodified by default. This
      is similar to using a debugger to add a breakpoint to a function: before the breakpoint is added,
      the function is running unmodified.

uprobes Arguments
      Arguments to user functions are made available by uprobes. As an example, the following uses
      bpftrace to instrument the decode_prompt_string() bash function and print the first argument
      as a string:

# bpftrace -e 'uprobe:/bin/bash:decode_prompt_string { printf("%s\n", str(arg0)); }'
      Attaching 1 probe...
      \[\e[31;1m\]\u@\h:\w>\[\e[0m\]
      \[\e[31;1m\]\u@\h:\w>\[\e[0m\]
      ^C

The output shows the bash(1) prompt string on this system. The uprobe for decode_prompt_
      string() is created when the bpftrace program begins running, and is removed when bpftrace
      terminates (Ctrl-C).

uretprobes
      The return from user functions and their return value can be traced using uretprobes (short for
      user-level return probes), which are similar to uprobes. When paired with uprobes and a tracer
      that records timestamps, the duration of a user-level function can be measured. Be aware that
      the overhead of uretprobes can significantly skew such measurements of fast functions.

uprobes Interface and Overhead
      The uprobes interface is similar to kprobes. There is a way to instrument them via /sys files and
      also (preferably) via the perf_event_open(2) syscall.
                                                                      4.3 Observability Sources      155
