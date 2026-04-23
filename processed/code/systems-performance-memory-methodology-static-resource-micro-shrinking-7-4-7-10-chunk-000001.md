7.4.7 Static Performance Tuning
Static performance tuning focuses on issues of the configured environment. For memory
performance, examine the following aspects of the static configuration:
■

How much main memory is there in total?

■

How much memory are applications configured to use (their own config)?

■

Which memory allocators do the applications use?

■

What is the speed of main memory? Is it the fastest type available (DDR5)?

■

Has main memory ever been fully tested (e.g., using Linux memtester)?

■

What is the system architecture? NUMA, UMA?

■

Is the operating system NUMA-aware? Does it provide NUMA tunables?

■

Is memory attached to the same socket, or split across sockets?

■

How many memory buses are present?

■

What are the number and size of the CPU caches? TLB?

■

What are the BIOS settings?

■

Are large pages configured and used?

■

Is overcommit available and configured?

■

What other system memory tunables are in use?

■

Are there software-imposed memory limits (resource controls)?

Answering these questions may reveal configuration choices that have been overlooked.

7.4.8

Resource Controls

The operating system may provide fine-grained controls for the allocation of memory to processes
or groups of processes. These controls may include fixed limits for main memory and virtual
memory usage. How they work is implementation-specific and is discussed in Section 7.6,
Tuning, and Chapter 11, Cloud Computing.

7.4.9 Micro-Benchmarking
Micro-benchmarking may be used to determine the speed of main memory and characteristics
such as CPU cache and cache line sizes. It may be helpful when analyzing differences between
systems, as the speed of memory access may have a greater effect on performance than CPU
clock speed, depending on the application and workload.
In Chapter 6, CPUs, the Latency section under CPU Caches (in Section 6.4.1, Hardware) shows
the result of micro-benchmarking memory access latency to determine characteristics of the
CPU caches.

7.4.10

Memory Shrinking

This is a working set size (WSS) estimation method that uses a negative experiment, requiring
swap devices to be configured to perform the experiment. Available main memory for an application is progressively reduced while measuring performance and swapping: the point where
performance sharply degrades and swapping greatly increases shows when the WSS no longer
fits into the available memory.
While worth mentioning as an example negative experiment, this is not recommended for
production use as it deliberately harms performance. For other WSS estimation techniques, see the
experimental wss(8) tool in Section 7.5.12, wss, and my website on WSS estimation [Gregg 18c].
