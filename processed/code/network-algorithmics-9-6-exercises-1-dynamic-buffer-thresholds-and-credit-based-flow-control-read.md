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

This page intentionally left blank

                                                                                                          CHAPTER


Exact-match lookups
                                                                                                  10
                           “Challenge-and-response” is a formula describing the free play of forces that provokes new
                       departures in individual and social life. An effective challenge stimulates men to creative action.
                                                                                                       —Arnold Toynbee


In Part 3, for simplicity of terminology, we will generically refer to interconnect devices as routers.
Each chapter in Part 3 addresses the efficient implementation of a key function for such routers. In
the simplest model of a router forwarding path the destination address of a packet is first looked up to
determine a destination port; the packet is then switched to the destination port; finally, the packet is
scheduled at the destination port to provide QoS (Quality of Service) guarantees. In addition, modern
high-performance routers also subject packets to internal striping (to gain throughput) and to internal
credit-based flow control (to prevent loss on chip-to-chip links). The chapters are arranged to follow
the same order, from lookups to switching to QoS.
    Thus the first three chapters concentrate on the surprisingly difficult problem of state lookup in
routers. The story begins with the simplest exact match lookups in this chapter, progresses to longest-
prefix lookups in Chapter 11, and culminates with the most complex classification lookups in Chap-
ter 12.
    What is an exact-match lookup? Exact-match lookups represent the simplest form of database query.
Assume a database with a set of tuples; each tuple consists of a unique fixed-length key together with
some state information. A query specifies a key K. The goal is to return the state information associated
with the tuple whose key is K.
    Now, exact-match queries are easily implemented using well-studied techniques, such as binary
search and hash tables (Cormen et al., 1990). However, they are still worth studying in this book for
two reasons. First, in the networking context the models and metrics for lookups are different from
the usual algorithmic setting. Such differences include the fact that lookups must complete in the time
to receive a packet, the use of memory references rather than processing as a measure of speed, and
the potential use of hardware speedups. Exact-match lookups offer the simplest opportunity to explore
these differences. A second reason to study exact-match lookups is that they are crucial for an important
networking function, called bridging,1 that is often integrated within a router.
    We are grateful to Michael Mitzenmacher for proofreading Section 10.3.3 that describes the d-left
scheme.
    This chapter is organized around a description of the history of bridges. This is done for one chapter
in the book, in the hope of introducing the reader to the process of algorithmics at work in a real


1 A device commonly known as a LAN switch typically implements bridge functionality.

Network Algorithmics. https://doi.org/10.1016/B978-0-12-809927-8.00017-8
Copyright © 2022 Elsevier Inc. All rights reserved.
                                                                                                                    235

236       Chapter 10 Exact-match lookups



                    Table 10.1 Principles used in the various exact-match lookup
                    techniques discussed in this chapter.
                    Number                           Principle                        Used in
                    P15        Use efficient data structures: binary search table First bridge
                    P5         Hardware FPGA for lookup only
                    P15        Use efficient data structure: perfect hashing      Gigaswitch
                    P2a        Precompute hash function with bounded collisions FDDI bridge
                    P5         Pipeline binary search



product that changed the face of networking. This chapter also describes some of the stimuli that lead
to innovation and introduces some of the people responsible for it.
    Arnold Toynbee (Toynbee and Caplan, 1972) describes history using a challenge–response theory,
in which civilizations either grow or fail in response to a series of challenges. Similarly, the history of
bridges can be described as a series of three challenges, which are described in the three sections of
this chapter: Ethernets Under Fire (Section 10.1), Wire Speed Forwarding (Section 10.2), and Scaling
Lookups to Higher Speeds (Section 10.3). The responses to these challenges led to what is now known
as 802.1 spanning tree bridges (IEEE Media, 1997).
    The techniques described in this chapter (and the corresponding principles) are summarized in Ta-
ble 10.1.

   Quick reference guide
   The implementor interested in fast exact-match schemes should consider either parallel hashing techniques inspired by
   perfect hashing (Section 10.3.1) or d-left (Section 10.3.3), or pipelined binary search (Section 10.3.2).
