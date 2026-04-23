# network-algorithmics-7-8-google-carousel-implementation (chunk 000001)

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
