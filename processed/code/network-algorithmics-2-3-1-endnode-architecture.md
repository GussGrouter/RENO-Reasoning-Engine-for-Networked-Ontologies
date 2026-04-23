# Network Algorithmics — endnode architecture (2.3.1) (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Extraction: pdftotext -f 60 -l 70 -layout
- Slice: from `2.3.1 Endnode architecture` up to (excluding) `2.3.2 Router architecture`

---

## PDF page 60

2.3.1 Endnode architecture
A processor such as a Pentium is a state machine that takes a sequence of instructions and data as
input and writes output to I/O devices, such as printers and terminals. To allow programs that have a
large state space, the bulk of the processor state is stored externally in cheap DRAM. In PCs, this is
referred to as main memory and is often implemented using 1 GB or more of interleaved DRAM, such
as SDRAM. However, recall that DRAM access times are large, say, 60 nsec. If the processor state
were stored only in DRAM, an instruction would take 60 nsec to read or write to memory.
    Processors gain speed using caches, which are comparatively small chunks of SRAM that can store
commonly used pieces of state for faster access. Some SRAM (i.e., the L1 cache) is placed on the
processor chip, and some more SRAM (i.e., the L2 cache) is placed external to the processor. A cache
is a hash table that maps between memory address locations and contents. CPU caches use a simple
hash function: They extract some bits from the address to index into an array and then search in parallel
for all the addresses that map into the array element.9 When a memory location has to be read from
DRAM, it is placed in the cache, and an existing cache element may be evicted. Commonly used data
is stored in a data cache, and commonly used instructions in an instruction cache.
    Caching works well if the instructions and data exhibit temporal locality (i.e., the corresponding
location is reused frequently in a small time period) or spatial locality (i.e., accessing a location is
followed by access to a nearby location). Spatial locality is taken advantage of as follows. Recall that
accessing a DRAM location involves accessing a row R and then a column within the row. Thus reading
words within row R are cheaper after R is accessed. A Pentium takes advantage of this observation by
prefetching 128 (cache line size) contiguous bits into the cache whenever 32 bits of data are accessed.
Access to the adjoining 96 bits will not incur a cache miss penalty.


8 Of course, there are ways to work around these limits, for instance, by using multiple chips, but such implementations often
do badly in terms of cost, complexity, and power consumption.
9 The number of elements that can be searched in parallel in a hash bucket is called the associativity of the cache. While
router designers rightly consider bit extraction to be a poor hash function, the addition of associativity improves overall hashing
performance, especially on computing workloads.

---

## PDF page 61

34       Chapter 2 Network implementation models




FIGURE 2.8
Model of a workstation.


    Many computing benchmarks exhibit temporal and spatial locality; however, a stream of packets
probably exhibits only spatial locality. Thus improving endnode protocol implementations often re-
quires paying attention to cache effects.
    The foregoing discussion should set the stage for the endnode architecture model shown in Fig. 2.8.
The processor, or CPU—e.g., a Pentium or an Alpha—sits on a bus. A bus can be thought of as a
network like an Ethernet, but optimized for the fact that the devices on the bus are close to each other.
The processor interacts with other components by sending messages across the bus.
    The input–output (I/O) devices are typically memory mapped. In other words, even I/O devices like
the network adaptor and the disk look like pieces of memory. For example, the adaptor memory may
be mapped to 100–200 in the memory address space. This allows uniform communication between
the CPU and any device by using the same conventions used to interact with memory. In terms of
networking, a Read (or Write) can be thought of as a message sent on the bus addressed to the memory
location. Thus a Read 100 is sent on the bus, and the device that owns memory location 100 (e.g., the
adaptor) will receive the message and reply with the contents of location 100.
    Modern machines allow direct memory access (DMA), where devices such as the disk or the net-
work adaptor send Reads and Writes directly to the memory via the bus without processor intervention.
However, only one entity can use the bus at a time. Thus the adaptor has to contend for the bus; any
device that gets hold of the bus “steals cycles” from the processor. This is because the processor is
forced to wait to access memory while a device is sending messages across the bus.
    In Fig. 2.8, also notice that the adaptor actually sits on a different bus (system bus or memory bus)
from the bus on which the network adaptor and other peripherals (I/O bus) sit. The memory bus is
designed for speed and is redesigned for every new processor; the I/O bus is a standard bus (e.g., a PCI
bus) chosen to stay compatible with older I/O devices. Thus the I/O bus is typically slower than the
memory bus.
    A big lesson for networking in Fig. 2.8 is that the throughput of a networking application is crucially
limited by the speed of the slowest bus, typically the I/O bus. Worse, the need for extra copies to
preserve operating system structure causes every packet received or sent by a workstation to traverse
the bus multiple times. Techniques to avoid redundant bus traversals are described in Chapter 5.
    Modern processors are heavily pipelined with instruction fetch, instruction decode, data reads, and
data writes split into separate stages. Superscalar and multithreaded machines go beyond pipelining

---

## PDF page 62

2.3 Network device architectures                   35




FIGURE 2.9
Using parallel connections within an endnode architecture to allow concurrent processing and network traffic via a
parallel switch.



by issuing multiple instructions concurrently. While these innovations (see, for example, the classic
reference on endnode architecture [Hennessey and Patterson, 1996]) remove computation bottlenecks,
they do little for data-movement bottlenecks. Consider the following speculative architecture instead.

Example 6. Endnode Architecture Using a Crossbar Switch: Fig. 2.9 shows the endnode bus being
replaced by a programmable hardware switch, as is commonly used by routers. The switch internally
contains a number of parallel buses so that any set of disjoint endpoint pairs can be connected in parallel
by the switch. Thus in the figure, the processor is connected to Memory 1, while the network adaptor is
connected to Memory 2. Thus packets from the network can be placed in Memory 2 without interfering
with the processor’s reading from Memory 1. If the processor now wishes to read the incoming packet,
the switch can be reprogrammed to connect the processor to Memory 2 and the adaptor to Memory 1.
This can work well if the queue of empty packet buffers used by the adaptor alternates between the two
memories.
    There are recent proposals for Infiniband switch technology to replace the I/O bus in processors
(Chapter 5). The ultimate message of this example is not that architectures such as Fig. 2.9 are nec-
essarily good but that simple architectural idea to improve network performance, such as Fig. 2.9,
are not hard for even protocol designers to conceive, given simple models of hardware and architec-
ture.
