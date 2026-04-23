# network-algorithmics-14-4-token-bucket-policing (chunk 000001)

# Network Algorithmics — 14.4 Token bucket policing (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 417
- Slice: from `14.4 Token bucket policing` up to next detected section heading

---

14.4 Token bucket policing
So far with RED, we assumed that all packets are placed in a single output queue; the RED drop
decision is taken at the input of this queue. Can we add any form of bandwidth guarantees for flows
that are placed in a common queue without segregation? For example, many customers require limiting
the rate of traffic for a flow. More specifically, an ISP may want to limit NEWS traffic in its network
to no more than 1 Mbps. A second example is where UDP traffic is flowing from the router to a slow
remote line. Since UDP sources currently do not react to congestion, congestion downstream can be
avoided by having a manager limit the UDP traffic to be smaller than the remote line speed. Fortunately,
these examples of bandwidth limiting can easily be accomplished by a technique called token bucket
policing, which uses only a single queue and a counter per flow.
    Token bucket policing is a simple derivative of another idea, called token bucket shaping. Token
bucket shaping (Turner, 1986) is a simple way to limit the burstiness of a flow by limiting its average
rate and also its maximum burst size. For example, a flow could be limited to sending at a long-term
average of 100 Kbps but could be allowed to send 4 KB as fast as it wants. Since most applications
are bursty, it helps to allow some burstiness. Downstream nodes are helped by leaky bucket shaping
because bursts contribute directly to short-term congestion and packet loss. The implementation is
shown conceptually in Fig. 14.5.
    Imagine that one has a bucket per flow that fills with “tokens” at the specified average rate of R
per second. The bucket size, however, is limited to the specified burst size of B tokens. Thus when the
bucket is full, all incoming tokens are dropped. When packets arrive for a flow, they are allowed out
only if the bucket contains a number of tokens equal to the size of packet in bits. If not, the packet is
queued until sufficient tokens arrive. Since there can be at most B tokens, a burst is limited to at most
B bits, followed by a more steady rate of R bits per second. This can easily be implemented using a
counter and a timer per flow; the timer is used to increment the counter, and the counter is limited never
to grow beyond B. When packets are sent out, the counter is decremented.
    Unfortunately, token bucket shaping would require different queues for each flow because some
flows may have temporarily run out of tokens and have to wait, while other, later-arriving packets may
belong to flows that have accumulated tokens. If one wishes to limit oneself to a single queue, a simpler
technique is to limit oneself (P3, relax system requirements) to a token bucket policer. The idea would
be simply to drop any packet that arrives to find the token bucket empty. In other words, a policer is

14.5 Multiple outbound queues and priority                391

FIGURE 14.5
Conceptual picture of token bucket shaping and policing.

a shaper without the buffer shown in Fig. 14.5. A policer needs only a counter and a timer per flow,
which is simple to implement at high speeds using the efficient timer implementations of Chapter 7.
