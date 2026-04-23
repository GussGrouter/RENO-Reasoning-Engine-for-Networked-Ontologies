For comparison, an example two-processor non-uniform memory access (NUMA) system is shown
in Figure 7.4, which uses a CPU interconnect that becomes part of the memory architecture. For
this architecture, the access time for main memory varies based on its location relative to the CPU.

Figure 7.4 Example NUMA main memory architecture, two-processor
CPU 1 can perform I/O to DRAM A directly, via its memory bus. This is referred to as local memory.
CPU 1 performs I/O to DRAM B via CPU 2 and the CPU interconnect (two hops). This is referred
to as remote memory and has a higher access latency.
The banks of memory connected to each CPU are referred to as memory nodes, or just nodes. The
operating system may be aware of the memory node topology based on information provided
by the processor. This then allows it to assign memory and schedule threads based on memory
locality, favoring local memory as much as possible to improve performance.

Buses
How main memory is physically connected to the system depends on the main memory architecture, as previously pictured. The actual implementation may involve additional controllers
and buses between the CPUs and memory. Main memory may be accessed in one of the following ways:
■

Shared system bus: Single or multiprocessor, via a shared system bus, a memory bridge
controller, and finally a memory bus. This was pictured as the UMA example, Figure 7.3,
and as the Intel front-side bus example, Figure 6.9 in Chapter 6, CPUs. The memory controller in that example was a Northbridge.

7.3

■

■

Architecture

Direct: Single processor with directly attached memory via a memory bus.
Interconnect: Multiprocessor, each with directly attached memory via a memory bus,
and processors connected via a CPU interconnect. This was pictured earlier as the NUMA
example in Figure 7.4; CPU interconnects are discussed in Chapter 6, CPUs.

If you suspect your system is none of the above, find a system functional diagram and follow the
data path between CPUs and memory, noting all components along the way.
