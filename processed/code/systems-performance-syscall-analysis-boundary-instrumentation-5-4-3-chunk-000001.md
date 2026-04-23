5.4.3 Syscall Analysis
System calls (syscalls) can be instrumented for the study of resource-based performance issues.
The intent is to find out where syscall time is spent, including the type of syscall and the reason
it is called.
Targets for syscall analysis include:
■

■

■

New process tracing: By tracing the execve(2) syscall you can log new process execution,
and analyze issues of short-lived processes. See the execsnoop(8) tool in Section 5.5.5,
execsnoop.
I/O profiling: Tracing read(2)/write(2)/send(2)/recv(2) and their variants, and studying
their I/O sizes, flags, and code paths, will help you identify issues of suboptimal I/O, such
as a large number of small I/O. See the bpftrace tool in Section 5.5.7, bpftrace.
Kernel time analysis: When systems show a high amount of kernel CPU time, often
reported as “%sys,” instrumenting syscalls can locate the cause. See the syscount(8) tool in
Section 5.5.6, syscount. Syscalls explain most but not all of kernel CPU time; exceptions
include page faults, asynchronous kernel threads, and interrupts.

Syscalls are a well-documented API (man pages), making them an easy event source to study.
They are also called synchronously with the application, which means that collecting stack
traces from syscalls will show the application code path responsible. Such stack traces can be
visualized as a flame graph.
