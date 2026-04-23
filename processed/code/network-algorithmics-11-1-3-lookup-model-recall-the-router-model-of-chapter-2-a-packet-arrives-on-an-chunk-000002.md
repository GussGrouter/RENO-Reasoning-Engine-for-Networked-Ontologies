# network-algorithmics-11-1-3-lookup-model-recall-the-router-model-of-chapter-2-a-packet-arrives-on-an (chunk 000002)

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
