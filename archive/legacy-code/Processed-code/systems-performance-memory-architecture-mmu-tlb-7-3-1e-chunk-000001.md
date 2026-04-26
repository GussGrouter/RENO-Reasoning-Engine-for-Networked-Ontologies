MMU
The MMU (memory management unit) is responsible for virtual-to-physical address translations.
These are performed per page, and offsets within a page are mapped directly. The MMU was
introduced in Chapter 6, CPUs, in the context of nearby CPU caches.
A generic MMU is pictured in Figure 7.5, with levels of CPU caches and main memory.

Figure 7.5 Memory management unit

Multiple Page Sizes
Modern processors support multiple page sizes, which allow different page sizes (e.g., 4 Kbytes,
2 Mbytes, 1 Gbyte) to be used by the operating system and the MMU. The Linux huge pages feature supports larger page sizes, such as 2 Mbytes or 1 Gbyte.

TLB
The MMU pictured in Figure 7.5 uses a TLB (translation lookaside buffer) as the first level of
address translation cache, followed by the page tables in main memory. The TLB may be divided
into separate caches for instruction and data pages.

Because the TLB has a limited number of entries for mappings, the use of larger page sizes
increases the range of memory that can be translated from its cache (its reach), which reduces
TLB misses and improves system performance. The TLB may be further divided into separate
caches for each of these page sizes, improving the probability of retaining larger mappings
in cache.
As an example of TLB sizes, a typical Intel Core i7 processor provides the four TLBs shown in
Table 7.2 [Intel 19a].

[Processed extract: Table 7.2 vendor TLB entry grid omitted — see PDF.]

This processor has one level of data TLB. The Intel Core microarchitecture supports two levels,
similar to the way CPUs provide multiple levels of main memory cache.
The exact makeup of the TLB is specific to the processor type. Refer to the vendor processor
manuals for details on the TLBs in your processor and further information on their operation.
