# network-algorithmics-10-5-exercise-1-arp-caches-another-example-of-an-exact-match-lookup-is-furnis (chunk 000001)

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
