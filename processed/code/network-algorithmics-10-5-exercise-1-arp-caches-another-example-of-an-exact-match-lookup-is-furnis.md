# Network Algorithmics — 10.5 Exercise 1. ARP Caches: Another example of an exact-match lookup is furnished by ARP (address resolution (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 274
- Slice: from `10.5 Exercise 1. ARP Caches: Another example of an exact-match lookup is furnished by ARP (address resolution` up to next detected section heading

---

10.5 Exercise
1. ARP Caches: Another example of an exact-match lookup is furnished by ARP (address resolution
   protocol) caches in a router or endnode. In an Internet router when a packet first arrives at a des-
   tination, the router must store the packet and send an ARP request to the Ethernet containing the
   packet. The ARP request is broadcast to all endnodes on the Ethernet and contains the IP address of
   the destination. When the destination responds with an ARP reply containing the Ethernet address
   of the destination, the router stores the mapping in an ARP table and sends the stored data packet,
   with the destination Ethernet address filled in.
   • What lookup algorithms can be used for ARP caches?
   • Why might the task of storing data packets awaiting data translation result in packet reordering?

248     Chapter 10 Exact-match lookups



   • Some router implementations get around the reordering problem by dropping all data packets
     that arrive to find that the destination address is not in the ARP table (however, the ARP request
     is sent out). Explain the pros and cons of such a scheme.
2. Using CAM to Absorb Overflows From a Hash Table: Suppose 1 million nodes are hashed into
   a hash table that contains 1 million buckets. On average, what is the total number of overflows if
   each bucket can hold at most 4 nodes (say in a memory line)? Calculating this number will help
   us determine the right size for the CAM. Here, you may assume that the hash function is strictly
   uniform (across the 1 million indices/buckets). You may also approximate the Binomial random
   variable you will encounter in this case by a Poisson random variable (since 1 million is a large
   enough number).

                                                                                           CHAPTER


Prefix-match lookups
                                                                                    11
                                                                                        You can look it up.
                                                                                             —Traditional


Consider a flight database in London that lists flights to a thousand US cities. One alternative would
be to keep a record specifying the path to each of the 1000 cities. Suppose, however, that most flights
to America hub through Boston, except flights to California, which hub through Los Angeles. This
observation can be exploited to reduce the flight database from a thousand entries to two prefix entries
(USA* → Boston; USA.CA.* → LA).
    A problem with this reduction is that a destination city like USA.CA.Fresno will now match both the
USA* and USA.CA.* prefixes; the database must return the longest match (USA.CA.*). Thus prefixes
have been used to compress a large database but at the cost of a more complex longest-matching-prefix
lookup.
    As described in Chapter 2 the Internet uses the same idea. In the year 2022 core routers stored only
around 900,000 prefixes instead of potentially billions of entries for each possible Internet address. For
example, to a core router, all the computers within a university, such as UCLA (University of California,
Los Angeles), will probably be reachable by the same next hop. If all the computers within UCLA are
given the same initial set of bits (the network number or prefix), then the router can store one entry for
UCLA instead of thousands of entries for each computer in UCLA.
    The world has changed significantly since the first edition as follows.
• Prefix Growth: Since the first edition, the core routing table has grown from around 150,000 in 2004
  to around 900,000 prefixes in 2022.
• IP v6: When the first edition was written, 128-bit IPv6 was being talked about but did not penetrate
  significantly because of the prevalence of Network Address Translation (NAT) boxes. However, the
  popularity of mobile and Internet of Things (IoT) devices have led to rapid deployment of IPv6,
  with IPv6 availability of Google users at over 30% (Google, 2022).
• DRAM versus SRAM: Many router hardware lookups find it cheaper to use a small amount of on-
  chip memory and large low-latency external DRAM instead of SRAM.
• Programmable Chips with TCAM: Chips, such as Intel’s Tofino-3 (Intel Corporation, 2022), have
  emerged that have a fairly large amount of TCAM and are programmable. While IP lookups can be
  done using TCAM, new data structures can use TCAM to scale to larger databases. Further, they
  can be programmed to do different IP lookup schemes using a new higher level language for router
  programming called P4 (P4 Open Source Programming Language, 2022).
• Software Defined Networks (SDN): The SDN movement allows the control plane (and with pro-
  grammable chips, even the data plane) to be changed by a centralized controller. Each router simply
Network Algorithmics. https://doi.org/10.1016/B978-0-12-809927-8.00018-X
Copyright © 2022 Elsevier Inc. All rights reserved.
                                                                                                     249

250      Chapter 11 Prefix-match lookups



  allows a set of match-action rules that can be used to implement bridge lookups, MPLS lookups, IP
  lookups, or other forms of lookup by simply changing the definition of a match.
• Multicore Processors: Processors have become faster and multicore. Thus software implementations
  of IP lookups at Gigabit speeds are feasible today.
• Network Function Virtualization (NFV): There is a growing trend among mobile carriers to replace
  complex middleboxes (that performed network functions such as longest matching prefix, firewalls,
  parental controls etc.) with flexible software realizations, a trend called Network Function Virtual-
  ization (NFV, 2022).
    Despite these changes, the underlying algorithmic ideas have remained except for small variations
that we will point out including fast software implementations such as DXR (2022) and algorithms
optimized for large amounts of DRAM and small on-chip SRAM such as SAIL (Yang et al., 2014).
    The entire chapter is organized as follows. Section 11.1 provides an introduction to prefix lookups.
Section 11.2 describes attempts to finesse the need for IP lookups. Section 11.3 presents non-
algorithmic techniques for lookup based on caching and parallel hardware. Section 11.4 describes the
simplest technique based on unibit tries.
    The chapter then transitions to describe seven more sophisticated schemes: multibit tries (Sec-
tion 11.5), level-compressed tries (Section 11.6), Lulea-compressed tries (Section 11.7), Tree bitmap
(Section 11.8), binary search on prefix ranges (Section 11.9) (with a modern manifestation called DXR),
binary search on prefix lengths (Section 11.11), and linear search on prefix lengths (Section 11.12).
    The chapter ends with Section 11.13 on memory allocation issues, Section 11.14 on fixed function
lookup chips, and Section 11.15 on programmable chips, and the P4 language to program them. The
techniques described in this chapter (and the corresponding principles) are summarized in Table 11.1.

  Quick reference guide
  The most important lookup algorithms in our opinion for an implementor today are as follows. At speeds up to 100 Gbps
  in hardware or software using DRAM technology, the simplest and most effective scheme is based on binary search on
  prefix ranges (DXR) (Section 11.9) and is unencumbered by patents. At faster speeds, especially using more expensive
  SRAM technology, the most effective algorithm described in this chapter is Tree bitmap (Section 11.8). On the other
  hand, a simple scheme using small on-chip SRAM and external DRAM is SAIL (Section 11.12). Finally, Section 11.15
  describes the P4 language, and potential IP lookup implementations in programmable router chips like Tofino-3 (Intel
  Corporation, 2022) that leverage both CAM and RAM.
