# Network Algorithmics — 7.8 Google Carousel implementation (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 217
- Slice: from `7.8 Google Carousel implementation` up to next detected section heading

---

7.8 Google Carousel implementation
Many years after the Costello implementation, Google built a scalable traffic shaping sytem called
Carousel (Saeed et al., 2017) whose underlying data structure is a timing wheel that can handle hun-
dreds of thousands of concurrent fine-grained timers. Because the speeds and scale are so much higher
than the Costello implementation, we briefly review the new use cases that motivated this design.
    The first use case is the use of fine grained pacing in rate-based congestion control algorithms like
BBR (Cardwell et al., 2017). Recall that the TCP congestion control algorithm is based on reducing
the window size (number of outstanding bytes that have not yet been acked) based on congestion
signals like congestion-encountered bits set by congested routers and dropped packets. The problem
with TCP’s congestion control algorithm is that when a cumulative acknowledgement arrives for a large
number of bytes, the sender can release a burst of traffic into the network, which can cause packets to be
dropped in routers. Rate based congestion algorithms like BBR, by contrast, control the rate of packet
sending based on congestion signals. The rate in turn is enforced by fine grained timers that control
the time between sending of packets. The use of BBR is reported to greatly improve round trip delays
around the world and Youtube Quality of Experience measures (Cardwell et al., 2017)
    The second use case is Virtual Machine (VM) isolation in severs that hosts thousands of VMS each
of which can communicate with hundreds of other VMs. Without iimits on the bandwidth used by each
VM either in isolation or aggregate, if one VM misbehaves by sending at too high a rate, other VMs
may be adversely affected because they share the same physical outgoing link. The third use case is
similar in terms of the Incast problem (Saeed et al., 2017) in warehouse computing, where a request
receives hundreds of responses from other servers that causes dropped packets in routers. Incast can be
mitigated by having a busy receiver rate control the acks it sends back using fine grained pacing.
    The second and third use cases are traditionally done by token bucket schemes which we will de-
scribe in the chapter on router QoS, Chapter 14. Briefly the idea is that each user is given a certain
number of tokens to send bytes every timer tick. When the user has sent more bytes than it has to-
kens, the user’s traffic is either dropped (in which case it is called a policer) or placed in a queue till
more tokens arrive (in which case it is called a shaper). While such schemes have traditionally been
implemented in routers, the three use cases above require token buckets in hosts. For example, Linux’s

                                                   7.9 Obtaining finer granularity timers            191



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
