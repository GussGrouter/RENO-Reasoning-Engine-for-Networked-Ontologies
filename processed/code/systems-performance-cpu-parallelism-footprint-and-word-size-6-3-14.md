<!-- pdftotext -f 231 -l 285 Systems.Performance.Enterprise.and.the.Cloud.pdf (Chapter 6 CPUs continues) -->

6.4

Architecture

Whichever technique is used, it is important that enough processes or threads be created to
span the desired number of CPUs—which, for maximum performance, may be all of the CPUs
available. Some applications may perform better when running on fewer CPUs, when the cost
of thread synchronization and reduced memory locality (NUMA) outweighs the benefit of running across more CPUs.
Parallel architectures are also discussed in Chapter 5, Applications, Section 5.2.5, Concurrency
and Parallelism, which also summarizes co-routines.

6.3.14

Word Size

Processors are designed around a maximum word size—32-bit or 64-bit—which is the integer size
and register size. Word size is also commonly used, depending on the processor, for the address
space size and data path width (where it is sometimes called the bit width).
Larger sizes can mean better performance, although it’s not as simple as it sounds. Larger
sizes may cause memory overheads for unused bits in some data types. The data footprint also
increases when the size of pointers (word size) increases, which can require more memory I/O.
For the x86 64-bit architecture, these overheads are compensated by an increase in registers and
a more efficient register calling convention, so 64-bit applications will likely be faster than their
32-bit versions.
Processors and operating systems can support multiple word sizes and can run applications compiled for different word sizes simultaneously. If software has been compiled for the smaller word
size, it may execute successfully but perform relatively poorly.

