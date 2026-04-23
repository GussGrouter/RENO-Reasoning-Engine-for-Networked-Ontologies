<!-- Extracted from systems-performance-ch4-scout-p171-220.txt (book PDF region ~171–220) -->
The return from user functions and their return value can be traced using uretprobes (short for
user-level return probes), which are similar to uprobes. When paired with uprobes and a tracer
that records timestamps, the duration of a user-level function can be measured. Be aware that
the overhead of uretprobes can significantly skew such measurements of fast functions.

uprobes Interface and Overhead
The uprobes interface is similar to kprobes. There is a way to instrument them via /sys files and
also (preferably) via the perf_event_open(2) syscall.

4.3 Observability Sources

uprobes currently work by trapping into the kernel. This costs much higher CPU overheads than
kprobes or tracepoints. For a particular system I measured, the minimum uprobe cost 1,287
nanoseconds, and the minimum uretprobe cost 1,931 nanoseconds [Gregg 19]. The uretprobe
overhead is higher because it is a uprobe plus a trampoline function.

uprobe Documentation
uprobes are documented in the Linux source under Documentation/trace/uprobetracer.rst.
I summarized advanced uprobe topics in BPF Performance Tools, Chapter 2 [Gregg 19]: how
they work at the instruction level. The user functions they instrument are typically not documented outside of the application source (since most are unlikely to be an API, they don’t need
to be). For documented user-space tracing, use USDT.

4.3.8

USDT

User-level statically-defined tracing (USDT) is the user-space version of tracepoints. USDT is to
uprobes as tracepoints is to kprobes. Some applications and libraries have added USDT probes
to their code, providing a stable (and documented) API for tracing application-level events. For
example, there are USDT probes in the Java JDK, in the PostgreSQL database, and in libc. The
following lists OpenJDK USDT probes using bpftrace:
# bpftrace -lv 'usdt:/usr/lib/jvm/openjdk/libjvm.so:*'
usdt:/usr/lib/jvm/openjdk/libjvm.so:hotspot:class__loaded
usdt:/usr/lib/jvm/openjdk/libjvm.so:hotspot:class__unloaded
usdt:/usr/lib/jvm/openjdk/libjvm.so:hotspot:method__compile__begin
usdt:/usr/lib/jvm/openjdk/libjvm.so:hotspot:method__compile__end
usdt:/usr/lib/jvm/openjdk/libjvm.so:hotspot:gc__begin
usdt:/usr/lib/jvm/openjdk/libjvm.so:hotspot:gc__end
[...]

This lists USDT probes for Java class loading and unloading, method compilation, and garbage
collection. Many more were truncated: the full listing shows 524 USDT probes for this JDK version.
Many applications already have custom event logs that can be enabled and configured, and are
useful for performance analysis. What makes USDT probes different is that they can be used
from various tracers that can combine application context with kernel events such as disk and
network I/O. An application-level logger may tell you that a database query was slow due to file
system I/O, but a tracer can reveal more information: e.g., the query was slow due to lock contention in the file system, and not disk I/O as you might have assumed.
Some applications contain USDT probes, but they are not currently enabled in the packaged
version of the application (this is the case with OpenJDK). Using them requires rebuilding
the application from source with the appropriate config option. That option may be called
--enable-dtrace-probes after the DTrace tracer, which drove adoption of USDT in applications.
USDT probes must be compiled into the executable they instrument. This is not possible for
