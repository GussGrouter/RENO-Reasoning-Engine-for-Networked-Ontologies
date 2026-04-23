# network-algorithmics-11-1-3-lookup-model-recall-the-router-model-of-chapter-2-a-packet-arrives-on-an (chunk 000001)

# Network Algorithmics — 11.1.3 Lookup model Recall the router model of Chapter 2. A packet arrives on an input link. Each packet carries a 32-bit (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 279
- Slice: from `11.1.3 Lookup model Recall the router model of Chapter 2. A packet arrives on an input link. Each packet carries a 32-bit` up to next detected section heading

---

11.1.3 Lookup model
Recall the router model of Chapter 2. A packet arrives on an input link. Each packet carries a 32-bit
Internet (IP) address.2
    The processor consults a forwarding table to determine the output link for the packet. The forward-
ing table contains a set of prefixes with their corresponding output links. The packet is matched to the
longest prefix that matches the destination address in the packet, and the packet is forwarded to the
corresponding output link. The task of determining the output link, called address lookup, is the subject
of this chapter, which surveys lookup algorithms and shows that lookup can be implemented at gigabit
and terabit speeds.
    Before searching for IP lookup solutions, it is important to be familiar with some basic observations
about traffic distributions, memory trends, and database sizes, which are shown in Table 11.2. These in
turn will motivate the requirements for a lookup scheme.

2 While most users deal with domain names, recall again that these names are translated to IP addresses by a directory service
called DNS before packets are sent.

11.1 Introduction to prefix lookups           253

Table 11.2 Some current data about the lookup problem
                     and the corresponding implications for lookup solutions.
                                 Observation                      Inference
                     1. 250,000 concurrent flows in Caching works poorly in backbone
                     backbone                        routers
                     2. 50% are TCP acks             Wire speed lookup needed for 40-
                                                     byte packets
                     3. Lookup dominated by memory Lookup speed measured by num-
                     accesses                        ber of memory accesses
                     4. Prefix lengths from 8 to 32  Naive schemes take 24 memory
                                                     accesses
                     5. 1 million prefixes today and With growth, require 500,000–1
                     multicast and host routes       million prefixes
                     6. Unstable BGP, multicast      Updates in milliseconds to sec-
                                                     onds
                     7. Higher speeds need SRAM      Worth minimizing memory
                     8. IPv6, multicast delays       Both 32-bit and 128-bit lookups
                                                     crucial today
