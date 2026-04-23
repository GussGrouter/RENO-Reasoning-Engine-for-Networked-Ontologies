# Chunk 000001

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Slice: 2.3.1 Endnode architecture
- From: processed/code/network-algorithmics-2-3-1-endnode-architecture.md

---
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
