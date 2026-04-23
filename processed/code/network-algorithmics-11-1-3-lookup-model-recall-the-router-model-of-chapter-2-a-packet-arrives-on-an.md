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



    First, a study of backbone traffic (Thompson et al., 1997) as far back as 1997 showed around 250,000
concurrent flows of short duration, using a fairly conservative measurement of flows. Measurement data
shows that this number is only increasing to easily over a million concurrent TCP flows. This large
number of flows means caching solutions do not work well.
    Second, the same study (Thompson et al., 1997) showed that roughly half the packets received by
a router are minimum-size TCP acknowledgments. Thus it is possible for a router to receive a stream
of minimum-size packets. Hence, being able to prefix lookups in the time to forward a minimum-size
packet can finesse the need for an input link queue, which simplifies system design. A second reason is
simple marketing: Many vendors claim wire speed forwarding, and these claims can be tested. Assum-
ing wire speed forwarding, forwarding a 40-byte packet should take no more than 32 nanoseconds at
10 Gbps (OC-192 speeds), and 8 nanoseconds at 40 Gbps (OC-768).
    Clearly, the most crucial metric for a lookup scheme is lookup speed. The third observation states
that because the cost of computation today is dominated by memory accesses, the simplest measure
of lookup speed is the worst-case number of memory accesses. The fourth observation shows that
backbone databases have all prefix lengths from 8 to 32, and so naive schemes will require 24 memory
accesses in the worst case to try all possible prefix lengths.
    The fifth observation states that while current databases are around 900,000 prefixes, the possible
use of host routes (full 32-bit addresses) and multicast routes means that future backbone routers will
have prefix databases of over 1 million prefixes.
    The sixth observation refers to the speed of updates to the lookup data structure, for example, to add
or delete a prefix. Unstable routing-protocol implementations can lead to requirements for updates on
the order of milliseconds. Note that whether seconds or milliseconds, this is several orders of magnitude
below the lookup requirements, allowing implementations the luxury of precomputing (P2a) informa-
tion in data structures to speed up lookup, at the cost of longer update times.

254      Chapter 11 Prefix-match lookups



    The seventh observation comes from Chapter 2. While standard (DRAM) memory is cheap, DRAM
access times are currently around 20–40 nanoseconds, and so higher-speed memory (e.g., off- or on-
chip SRAM, 1–5 nanoseconds) may be needed at higher speeds. While DRAM memory is essentially
unlimited, SRAM and on-chip memory are limited by expense or unavailability. Thus a third metric is
memory usage, where memory can be expensive fast memory (cache in software, SRAM in hardware)
as well as cheaper, slow memory (e.g., DRAM, SDRAM).
    Note that a lookup scheme that does not do incremental updates will require two copies of the
lookup database so that search can proceed in one copy while lookups proceed on the other copy. Thus
it may be worth doing incremental updates simply to reduce high-speed memory by a factor of 2!
    The eighth observation concerns prefix lengths. IPv6 requires 128-bit prefixes. Multicast lookups
require 64-bit lookups because the full group address and a source address can be concatenated to make
a 64-bit prefix. However, the full deployment of both IPv6 and multicast is still proceeding. Thus at the
time of writing, it is important to be able to support both 32-bit and 128-bit IP lookups.
    In summary, the interesting metrics, in order of importance, are lookup speed, memory, and update
time. As a concrete example, a good on-chip design using 16 Mbits of on-chip memory may support
any set of 1,000,000 prefixes, do a lookup in 8 nanoseconds to provide wire speed forwarding at terabit
speeds, and allow prefix updates in 1 millisecond.
    The following notations is used consistently in reporting the theoretical performance of IP lookup
algorithms. N denotes the number of prefixes (e.g., 900,000 for large databases in 2022), and W denotes
the length of an address (e.g., 32 for IPv4).
    Finally, two additional observations can be exploited to optimize the expected case.
O1: Almost all prefixes are 24 bits or less, with the majority being 24-bit prefixes and the next largest
    spike being at 16 bits. Some vendors use this to show worst-case lookup times only for 24-bit
    prefixes; however, the future may lead to databases with a large number of host routes (32-bit
    addresses) and integration of ARP caches.
O2: It is fairly rare to have prefixes that are prefixes of other prefixes, such as the prefixes 00* and
    0001*. In fact, the maximum number of prefixes of a given prefix in current databases is seven.
   While the ideal is a scheme that meets worst-case lookup time requirements, it is desirable to have
schemes that also utilize these observations to improve average storage performance.
