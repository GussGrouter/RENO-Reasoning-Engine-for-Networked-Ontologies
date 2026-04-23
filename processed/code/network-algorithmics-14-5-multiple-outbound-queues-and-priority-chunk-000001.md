# network-algorithmics-14-5-multiple-outbound-queues-and-priority (chunk 000001)

# Network Algorithmics — 14.5 Multiple outbound queues and priority (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 418
- Slice: from `14.5 Multiple outbound queues and priority` up to next detected section heading

---

14.5 Multiple outbound queues and priority
So far, we have limited ourselves to one single queue for all outbound packets, as shown on the left of
Fig. 14.6. RED or token bucket policing (or both) can be used to decide whether to drop packets before
they are placed on this queue. We now transition to examine scheduling disciplines that are possible
with multiple queues. This is shown on the right of Fig. 14.6.
    First, note that we now need to demultiplex packets based on packet headers to identify which out-
bound queue to place a packet on. This can be done using the packet-classification techniques described
in Chapter 12 or simpler techniques based on inspecting the TOS bits in the IP header. Second, note
that we can still implement RED and token bucket policing by dropping packets before they are placed
on the appropriate outbound queue.
    Third, note that we now have a new problem. If multiple queues have packets to send, we have
to decide which queue to service next, and when. If we limit ourselves to work-conserving schemes2

2 Token bucket shaping is a commonly used example of a scheduling discipline that is not work conserving.

392       Chapter 14 Scheduling packets

FIGURE 14.6
A single outbound queue (left) versus multiple outbound queues (right). Disciplines based on dropping (such as
RED and policing) can be implemented with a single queue, but other possibilities, such as round-robin and priority,
are possible with multiple queues.

that never idle the link, then the only decision is which queue to service next when the current packet
transmission on the output link finishes. In this chapter we will indeed focus on the work-conserving
schemes.
    As the simplest example of a multiple queue-scheduling discipline, consider strict priority. For
example, imagine two outbound queues, one for premium service and one for other packets. Imagine
that packets are demultiplexed to these two queues based on a bit in the IP TOS field. In strict priority,
we will always service a queue with higher priority before one with lower priority as long as there is a
packet in the higher-priority queue.
