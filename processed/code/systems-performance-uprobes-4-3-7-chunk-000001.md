|

The output shows that do_nanosleep() was usually a fast function, returning in zero milliseconds
(rounded down) 1,280 times. Two occurrences reached the 512 to 1024 millisecond range.
bpftrace syntax is explained in Chapter 15, BPF, which includes a similar example for timing
vfs_read().

kprobes Interface and Overhead
The kprobes interface is similar to tracepoints. There is a way to instrument them via /sys files,
via the perf_event_open(2) syscall (which is preferred), and also via the register_kprobe() kernel
API. The overhead is similar to that of tracepoints when the entries to functions are traced
(Ftrace method, if available), and higher when function offsets are traced (breakpoint method)
or when kretprobes are used (trampoline method). For a particular system I measured the minimum kprobe CPU cost to be 76 nanoseconds, and the minimum kretprobe CPU cost to be 212
nanoseconds [Gregg 19].

kprobes Documentation
kprobes are documented in the Linux source under Documentation/kprobes.txt. The kernel
functions they instrument are typically not documented outside of the kernel source (since most
are not an API, they don’t need to be). I summarized advanced kprobe topics in BPF Performance
Tools, Chapter 2 [Gregg 19]: how they work at the instruction level.

4.3.7

uprobes

uprobes (user-space probes) are similar to kprobes, but for user-space. They can dynamically
instrument functions in applications and libraries, and provide an unstable API for diving deep
into software internals beyond the scope of other tools. uprobes were made available in Linux 3.5,
released in 2012.
uprobes can be used by the tracers introduced in Section 4.5, Tracing Tools, and covered in
depth in Chapters 13 to 15.

153

154

Chapter 4 Observability Tools

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
