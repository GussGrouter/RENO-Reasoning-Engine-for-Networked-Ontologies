7.3

7.3

Architecture

Architecture

This section introduces memory architecture, both hardware and software, including processor
and operating system specifics.
These topics have been summarized as background for performance analysis and tuning. For
more details, see the vendor processor manuals and texts on operating system internals listed at
the end of this chapter.

7.3.1

Hardware

Memory hardware includes main memory, buses, CPU caches, and the MMU.

Main Memory
The common type of main memory in use today is dynamic random-access memory (DRAM).
This is a type of volatile memory—its contents are lost when power is lost. DRAM provides
high-density storage, as each bit is implemented using only two logical components: a capacitor
and a transistor. The capacitor requires a periodic refresh to maintain charge.
Enterprise servers are configured with different amounts of DRAM depending on their purpose,
typically ranging from one Gbyte to one Tbyte and larger. Cloud computing instances are typically smaller, ranging between 512 Mbytes and 256 Gbytes each.3 However, cloud computing
is designed to spread load over a pool of instances, so they can collectively bring much more
DRAM online for a distributed application, although at a much higher coherency cost.

Latency
The access time of main memory can be measured as the column address strobe (CAS) latency:
the time between sending a memory module the desired address (column) and when the data
is available to be read. This varies depending on the type of memory (for DDR4 it is around
10 to 20ns [Crucial 18]). For memory I/O transfers, this latency may occur multiple times for
a memory bus (e.g., 64 bits wide) to transfer a cache line (e.g., at 64 bytes wide). There are also
other latencies involved with the CPU and MMU for then reading the newly available data. Read
instructions avoid these latencies when they return from a CPU cache; write instructions may
avoid them as well, if the processor supports write-back caching (e.g., Intel processors).

Main Memory Architecture
An example main memory architecture for a generic two-processor uniform memory access
(UMA) system is shown in Figure 7.3.
Each CPU has uniform access latency to all of memory, via a shared system bus. When managed
by a single operating system kernel instance that runs uniformly across all processors, this is
also a symmetric multiprocessing (SMP) architecture.
