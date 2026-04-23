<!-- pdftotext -f 286 -l 320 Systems.Performance.Enterprise.and.the.Cloud.pdf (Chapter 6 CPUs §6.5 continued) -->

6.5.11 Micro-Benchmarking
Tools for CPU micro-benchmarking typically measure the time taken to perform a simple operation many times. The operation may be based on:
■

■

■

CPU instructions: Integer arithmetic, floating-point operations, memory loads and
stores, branch and other instructions
Memory access: To investigate latency of different CPU caches and main memory
throughput
Higher-level languages: Similar to CPU instruction testing, but written in a higher-level
interpreted or compiled language

8
Linux has a solution since 2.6.25 for this problem: RLIMIT_RTTIME, which sets a limit in microseconds of CPU time
a real-time thread may consume before making a blocking syscall.

253

254

Chapter 6 CPUs

■

Operating system operations: Testing system library and system call functions that are
CPU-bound, such as getpid(2) and process creation

An early example of a CPU benchmark is Whetstone by the National Physical Laboratory, written
in 1972 in Algol 60 and intended to simulate a scientific workload. The Dhrystone benchmark
was developed in 1984 to simulate integer workloads of the time, and became a popular means
to compare CPU performance. These, and various Unix benchmarks including process creation
and pipe throughput, were included in a collection called UnixBench, originally from Monash
University and published by BYTE magazine [Hinnant 84]. More recent CPU benchmarks have
been created to test compression speeds, prime number calculation, encryption, and encoding.
Whichever benchmark you use, when comparing results between systems, it’s important that
you understand what is really being tested. Benchmarks like those listed earlier often end
up testing differences in compiler optimizations between compiler versions, rather than the
benchmark code or CPU speed. Many benchmarks execute single-threaded, and their results
lose meaning in systems with multiple CPUs. (A four-CPU system may benchmark slightly faster
than an eight-CPU system, but the latter is likely to deliver much greater throughput when given
enough parallel runnable threads.)
For more on benchmarking, see Chapter 12, Benchmarking.
