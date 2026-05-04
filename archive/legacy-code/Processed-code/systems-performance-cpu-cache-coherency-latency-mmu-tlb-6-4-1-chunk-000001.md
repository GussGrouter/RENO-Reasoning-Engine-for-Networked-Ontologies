<!-- pdftotext -f 231 -l 285 Systems.Performance.Enterprise.and.the.Cloud.pdf (Chapter 6 CPUs continues) -->

For multicore and multithreading processors, some caches may be shared between cores and
threads. For the examples in Table 6.3, all processors since the Intel Xeon 7460 (2008) have
multiple Level 1 and Level 2 caches, typically one for each core (the sizes in the table refer to the
per-core cache, not the total size).
Apart from the increasing number and sizes of CPU caches, there is also a trend toward providing these on-chip, where access latency can be minimized, instead of providing them externally
to the processor.

Latency
Multiple levels of cache are used to deliver the optimum configuration of size and latency. The
access time for the Level 1 cache is typically a few CPU clock cycles, and for the larger Level 2
cache around a dozen clock cycles. Main memory access can take around 60 ns (around 240
cycles for a 4 GHz processor), and address translation by the MMU also adds latency.
The CPU cache latency characteristics for your processor can be determined experimentally
using micro-benchmarking [Ruggiero 08]. Figure 6.7 shows the result of this, plotting memory
access latency for an Intel Xeon E5620 2.4 GHz tested over increasing ranges of memory using
LMbench [McVoy 12].
Both axes are logarithmic. The steps in the graphs show when a cache level was exceeded, and
access latency becomes a result of the next (slower) cache level.

233

234

Chapter 6 CPUs

Figure 6.7 Memory access latency testing

Associativity
Associativity is a cache characteristic describing a constraint for locating new entries in the
cache. Types are:
■

■

■

Fully associative: The cache can locate new entries anywhere. For example, a least
recently used (LRU) algorithm could be used for eviction across the entire cache.
Direct mapped: Each entry has only one valid location in the cache, for example, a hash
of the memory address, using a subset of the address bits to form an address in the cache.
Set associative: A subset of the cache is identified by mapping (e.g., hashing) from within
which another algorithm (e.g., LRU) may be performed. It is described in terms of the subset size; for example, four-way set associative maps an address to four possible locations, and
then picks the best from those four (e.g., the least recently used location).

CPU caches often use set associativity as a balance between fully associative (which is expensive
to perform) and direct mapped (which has poor hit rates).

Cache Line
Another characteristic of CPU caches is their cache line size. This is a range of bytes that are
stored and transferred as a unit, improving memory throughput. A typical cache line size for
x86 processors is 64 bytes. Compilers take this into account when optimizing for performance.
Programmers sometimes do as well; see Hash Tables in Chapter 5, Applications, Section 5.2.5,
Concurrency and Parallelism.

Cache Coherency
Memory may be cached in multiple CPU caches on different processors at the same time. When
one CPU modifies memory, all caches need to be aware that their cached copy is now stale and

6.4

Architecture

should be discarded, so that any future reads will retrieve the newly modified copy. This process,
called cache coherency, ensures that CPUs are always accessing the correct state of memory.
One of the effects of cache coherency is LLC access penalties. The following examples are provided as a rough guide (these are from [Levinthal 09]):
■

LLC hit, line unshared: ~40 CPU cycles

■

LLC hit, line shared in another core: ~65 CPU cycles

■

LLC hit, line modified in another core: ~75 CPU cycles

Cache coherency is one of the greatest challenges in designing scalable multiprocessor systems,
as memory can be modified rapidly.

MMU
The memory management unit (MMU) is responsible for virtual-to-physical address translation.

Figure 6.8 Memory management unit and CPU caches
A generic MMU is pictured in Figure 6.8, along with CPU cache types. This MMU uses an
on-chip translation lookaside buffer (TLB) to cache address translations. Cache misses are satisfied by translation tables in main memory (DRAM), called page tables, which are read directly by
the MMU (hardware) and maintained by the kernel.
These factors are processor-dependent. Some (older) processors handle TLB misses using kernel
software to walk the page tables, and then populate the TLB with the requested mappings. Such
software may maintain its own, larger, in-memory cache of translations, called the translation
storage buffer (TSB). Newer processors can service TLB misses in hardware, greatly reducing
their cost.
