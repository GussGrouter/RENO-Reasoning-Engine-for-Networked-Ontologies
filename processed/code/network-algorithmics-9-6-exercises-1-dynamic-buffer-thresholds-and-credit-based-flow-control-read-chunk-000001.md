# network-algorithmics-9-6-exercises-1-dynamic-buffer-thresholds-and-credit-based-flow-control-read (chunk 000001)

# Network Algorithmics — 9.6 Exercises 1. Dynamic Buffer Thresholds and Credit-Based Flow Control: Read the credit-based protocol (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 258
- Slice: from `9.6 Exercises 1. Dynamic Buffer Thresholds and Credit-Based Flow Control: Read the credit-based protocol` up to next detected section heading

---

9.6 Exercises
1. Dynamic Buffer Thresholds and Credit-Based Flow Control: Read the credit-based protocol
   described in Chapter 15. Consider how to modify the buffer-sharing protocol of Chapter 15 to use

232      Chapter 9 Protocol processing

dynamic thresholds. What are some of the possible benefits? This last question is ideally answered
   by a simulation, which would make it a longer-term class project.
2. Incremental Checksum Computation: RFC 1141 states that when an IP header with checksum H
   is modified by changing some 16-bit field value (such as the TTL field) m to a new value m , then the
   new checksum should become H + m + m , where X denotes the 1’s complement of X. While this
   works most of the time, the right equation, described in RFC 1624, is to compute (H + m + m ):
   this is slightly more inefficient but correct. This should show that tinkering with the computation
   can be tricky and requires proofs.
   To see the difference between these two implementations, consider an example given in RFC 1624
   with an IP header in which a 16-bit field m = 0x5555 changes to m = 0x3285. The 1’s-complement
   sum of all the remaining header bytes is 0xCD7A. Compute the checksum both ways and show that
   they produce different results. Given that these two results are really the same in 1’s complement
   notation (different representations of zero), why might it cause trouble at the receiver?
3. Parallel Checksum Computation: Figure out how to modify checksum calculation in hardware so
   as to work on W chunks of the packet in parallel and finally to fold all the results.
4. Hardware Reassembly: Suppose the FIFO assumption is not true and fragments arrive out of or-
   der. In this problem your assignment is to design an efficient hardware reassembly scheme for IP
   fragments subject to the restrictions stated in Chapter 2. One idea you could exploit is to have the
   hardware DMA engine that writes the fragment to a buffer also write a control bit for every word
   written to memory. This only adds a bit for every 32 bits.
   When all the fragments have arrived, all the bits are set. You could determine whether all bits are set
   by using a summary tree, in which all the bits are leaves and each node has 32 children. A node’s
   bit is set if all its children’s bits are set. The summary tree does not require any pointers because all
   node bit positions can be calculated from child bit positions, as in a heap. Describe the algorithms
   to update the summary tree when a new fragment arrives. Consider hardware alternatives in which
   packets are stored in DRAM and bitmaps are stored in SRAM, as well as other creative possibilities.

PART

Playing with routers
                                                                                  3
                                                                   My work is a game, a very serious game.
                                                                                            —M.C. Escher

Part 1 dealt with models and principles and Part 2 dealt with applying these models and principles to
endnodes. The third part of this book deals with router algorithmics. This is the application of network
algorithmics to building fast routers. However, many of the techniques apply to bridges, gateways,
measurement devices, and firewalls. The techniques are applied mostly in a hardware setting, and much
of it has to do with processing packets at wire speeds as links get faster. We study exact lookups, prefix
lookups, packet classification, switching, and quality of service (QoS). We also study some other chores
within a router, such as striping and flow control across chip-to-chip links within a router.
