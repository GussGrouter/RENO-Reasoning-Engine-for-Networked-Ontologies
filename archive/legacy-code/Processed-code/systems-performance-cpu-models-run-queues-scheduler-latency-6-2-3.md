<!-- pdftotext -f 231 -l 285 Systems.Performance.Enterprise.and.the.Cloud.pdf (Chapter 6 CPUs begins in this extract) -->

Figure 6.1 CPU architecture
Each hardware thread is addressable as a logical CPU, so this processor appears as eight CPUs. The
operating system may have some additional knowledge of topology to improve its scheduling
decisions, such as which CPUs are on the same core and how CPU caches are shared.

6.2.2

CPU Memory Caches

Processors provide various hardware caches for improving memory I/O performance. Figure 6.2
shows the relationship of cache sizes, which become smaller and faster (a trade-off) the closer
they are to the CPU.
The caches that are present, and whether they are on the processor (integrated) or external to the
processor, depends on the processor type. Earlier processors provided fewer levels of integrated
cache.

2
There is a tool for Linux, lstopo(1), that can generate diagrams similar to this figure for the current system, an
example is in Section 6.6.21, Other Tools.

221

