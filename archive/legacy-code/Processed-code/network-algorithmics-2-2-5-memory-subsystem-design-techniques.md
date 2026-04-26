# Network Algorithmics — 2.2.5 Memory subsystem design techniques (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 57
- Slice: from `2.2.5 Memory subsystem design techniques` up to next detected section heading

---

2.2.5 Memory subsystem design techniques
The flow ID lookup problem illustrates three major design techniques commonly used in memory
subsystem designs for networking chips.
• Memory Interleaving and Pipelining: Similar techniques are used in IP lookup, classification, and
  in scheduling algorithms that implement QoS. The multiple banks can be implemented using several
  external memories, a single external memory like a RAMBUS, or on-chip SRAM within a chip that
  also contains processing logic.

                                                                                          2.2 Hardware               31



• Wide Word Parallelism: A common theme in many networking designs, such as the Lucent bit
  vector scheme (Chapter 12), is to use wide memory words that can be processed in parallel. This
  can be implemented using DRAM and exploiting page mode or by using SRAM and making each
  memory word wider.
• Combining DRAM and SRAM: Given that SRAM is expensive and fast and that DRAM is cheap
  and slow, it makes sense to combine the two technologies to attempt to obtain the best of both
  worlds. While the use of SRAM as a cache for DRAM databases is classical, there are many more
  creative applications of the idea of a memory hierarchy. For instance, the exercises explore the effect
  of a small amount of SRAM on the design of the flow ID lookup chip. Chapter 16 describes a more
  unusual application of this technique to implement a large number of counters, where the low-order
  bits of each counter are stored in SRAM.
It is more important for a novice designer to understand these design techniques (than to know memory
implementation details) in order to produce creative hardware implementations of networking func-
tions.
