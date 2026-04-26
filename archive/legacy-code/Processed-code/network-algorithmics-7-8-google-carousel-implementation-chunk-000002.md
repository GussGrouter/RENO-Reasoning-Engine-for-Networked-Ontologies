# network-algorithmics-7-8-google-carousel-implementation (chunk 000002)

Qdisc (Components of Linux Traffic Control, 2022) supports various fair queuing disciplines including
HTB (hierarchical token buckets).
    Measurements on Google servers (Saeed et al., 2017) show that the use of existing Qdisc mecha-
nisms in Linux resulting in either imperfect rate control or excessively high CPU overhead. Thus rather
than rely on Linux timers, the Carousel designers (Saeed et al., 2017) use a large hashed timing wheel.
Carousel is not, however, a timing facilty. It is instead a shaper/policer that scales to hundreds of thou-
sands of flows. To avoid the problem in a shaper where the application keeps bursting packets that are
queued in Carousel, the Carousel system also adds a second idea called deferred completions.
    The idea in deferred completions is to not allow the system call to complete until any packets stored
by Carousel are sent to the NIC by Carousel. This provides feedback that slows down an over-zealous
sender. Deferred completions means that completions can arrive out of order—an application paced to
a slow rate may receive a completion later than a faster rate application even though it send its request
earlier. This requires a way to match completions and requests using a hash table (P15) but this added
complexity is worthwhile. Deferred completions are thus a way to change the interface (P9).
    Notice that unlike the traditional use cases where timers are used to trigger retransmission or detect
failure, the Carousel timers always expire (unlike retransmission or failure timers that almost never
expire), and thus some of the optimizations used in the Linux timer facilty (see Corbet, 2015) cannot be
used. Instead, Carousel uses several other implementation tricks. Carousel uses one timing wheel per
CPU to avoid lock contention and can use multiple cores if needed. It also uses pre-allocated buffers
(P2a) to reduce the overhead of buffer allocation.
    The net result is that Carousel shapes traffic 10 times more accurately for Google traffic (Saeed
et al., 2017) while improving overall machine CPU utilization by 10% and reducing memory by two
orders of magnitude when compared to the best earlier techiques for traffic shaping. This shows the
utility of timing wheels when fundamentally integrated into a shaping algorithm (as opposed to being
used solely as a timer facility) combined with innovations such as deferred completions.
