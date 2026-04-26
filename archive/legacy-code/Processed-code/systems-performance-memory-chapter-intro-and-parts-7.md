Chapter 7
Memory

System main memory stores application and kernel instructions, their working data, and file
system caches. The secondary storage for this data is typically the storage devices—the disks—
which operate orders of magnitude more slowly. Once main memory has filled, the system may
begin switching data between main memory and the storage devices. This is a slow process that
will often become a system bottleneck, dramatically decreasing performance. The system may
also terminate the largest memory-consuming process, causing application outages.
Other performance factors to consider include the CPU expense of allocating and freeing memory, copying memory, and managing memory address space mappings. On multisocket architectures, memory locality can become a factor, as memory attached to local sockets has lower access
latency than remote sockets.
The learning objectives of this chapter are:
■

Understand memory concepts.

■

Become familiar with memory hardware internals.

■

Become familiar with kernel and user allocator internals.

■

Have a working knowledge of the MMU and TLB.

■

Follow different methodologies for memory analysis.

■

Characterize system-wide and per-process memory usage.

■

Identify issues caused by low available memory.

■

Locate memory usage in a process address space and kernel slabs.

■

Investigate memory usage using profilers, tracers, and flame graphs.

■

Become aware of tunable parameters for memory.

This chapter has five parts, the first three providing the basis for memory analysis, and the last
two showing its practical application to Linux-based systems. The parts are as follows:
■

■

Background introduces memory-related terminology and key memory performance
concepts.
Architecture provides generic descriptions of hardware and software memory
architecture.

304

Chapter 7 Memory

■

Methodology explains performance analysis methodology.

■

Observability Tools describes performance tools for memory analysis.

■

Tuning explains tuning and example tunable parameters.

The on-CPU memory caches (Level 1/2/3, TLB) are covered in Chapter 6, CPUs.

