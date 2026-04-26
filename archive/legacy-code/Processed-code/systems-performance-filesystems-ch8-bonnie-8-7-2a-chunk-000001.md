8.7.2

Micro-Benchmark Tools

There are many file system benchmark tools available, including Bonnie, Bonnie++, iozone,
tiobench, SysBench, fio, and FileBench. A few are discussed here, in order of increasing complexity. Also see Chapter 12, Benchmarking. My personal recommendation is to use fio.

Bonnie, Bonnie++
The Bonnie tool is a simple C program to test several workloads on a single file, from a single
thread. It was originally written by Tim Bray in 1989 [Bray 90]. Usage is straightforward, not
requiring arguments (defaults will be used):

(Omitted in this processed extract: full Bonnie ASCII report — see PDF.)

The output includes the CPU time during each test, which at 100% is an indicator that Bonnie
never blocked on disk I/O, instead always hitting from cache and staying on-CPU. The reason
is that the target file size is 100 Mbytes, which is entirely cached on this system. You can change
the file size using -s size.
There is a 64-bit version called Bonnie-64, which allows larger files to be tested. There is also a
rewrite in C++ called Bonnie++ by Russell Coker [Coker 01].
Unfortunately, file system benchmark tools like Bonnie can be misleading, unless you clearly
understand what is being tested. The first result, a putc(3) test, can vary based on the system
library implementation, which then becomes the target of the test rather than the file system.
See the example in Chapter 12, Benchmarking, Section 12.3.2, Active Benchmarking.
