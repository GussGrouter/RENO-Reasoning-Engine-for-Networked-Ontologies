# network-algorithmics-9-6-exercises-1-dynamic-buffer-thresholds-and-credit-based-flow-control-read (chunk 000002)

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
