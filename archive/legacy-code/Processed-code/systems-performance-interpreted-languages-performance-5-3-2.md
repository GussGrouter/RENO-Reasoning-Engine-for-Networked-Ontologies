<!-- pdftotext -f 182 -l 230 Systems.Performance.Enterprise.and.the.Cloud.pdf -->
5.3.2 Interpreted Languages
Interpreted languages execute a program by translating it into actions during runtime, a
process that adds execution overhead. Interpreted languages are not expected to exhibit high
performance and are used for situations where other factors are more important, such as ease of
programming and debugging. Shell scripting is an example of an interpreted language.
Unless observability tools are provided, performance analysis of interpreted languages can be
difficult. CPU profiling can show the operation of the interpreter—including parsing, translating, and performing actions—but it may not show the original program function names, leaving

6
Depending on the profiler, there may be other solutions available for stack walking, such as using debuginfo,
LBR, BTS, and more. For the perf(1) profiler, ways to use different stack walkers are described in Chapter 13, perf,
Section 13.9, perf record.
7

If you do distribute stripped binaries, consider making debuginfo packages so that the debug information can be
installed when needed.

5.3

Programming Languages

essential program context a mystery. This interpreter analysis may not be totally fruitless, as
there can be performance issues with the interpreter itself, even when the code it is executing
appears to be well designed.
Depending on the interpreter, program context may be available as arguments to interpreter
functions, which can be seen using dynamic instrumentation. Another approach is examine
the process’s memory, given knowledge of program layout (e.g., using the Linux process_vm_
readv(2) syscall).
Often these programs are studied by simply adding print statements and timestamps. More
rigorous performance analysis is uncommon, since interpreted languages are not commonly
selected for high-performance applications in the first place.

