# network-algorithmics-5-3-2-modern-day-incarnations-of-rdma (chunk 000003)

adaptor implements the transport protocol in hardware. There are two common solutions, iWarp and
RoCE, with the latter popular in data centers.
    iWarp: In the Internet world the transport protocol is TCP. Thus adaptors must implement TCP in
hardware. This is not too hard, and chips that perform TCP offload are available.
    The harder parts are as follows. First, as we saw in Case Study 1 of Chapter 2, TCP is a streaming
protocol. The application writes bytes to a queue, and these bytes are arbitrarily segmented into packets.
The RDMA idea, on the other hand, is based on messages, each of which has a named buffer field.
Second, RDMA over TCP requires a header to hold named buffers.
    The iWarp (RDMA Consortium, 2001) proposal solves both these problems by logically layering
three protocols over TCP. The first protocol, MPA, adds a header that defines message boundaries in the
byte stream. The second and third protocols implement the RDMA header fields but are separated as
follows. Notice that when a packet carries data, all that is needed is a buffer name and offset. Thus this
header is abstracted out into a so-called DDA (for direct data access) header together with a command
verb (such as READ or WRITE).
    The iWarp RDMA protocol that is layered over DDA adds a header with a few more fields. For
example, for an RDMA remote READ, the initial request must specify the remote buffer name (to be
read) and the local name (to be written to). One of these two buffer names can be placed in the DDA
header, but the other must be placed in the RDMA header. Thus, except for control messages such as
initiating a READ, all data carries only a DDA header and not an RDMA header.
    During the evolution from VAX Clusters to the RDMA proposal, one interesting generalization was
to replace a named buffer with an anonymous buffer. In this case the DDA header contains a queue
name, and the packet is placed in a buffer corresponding to the buffer at the head of the free queue at
the receiver.
    RoCE: In response to the perceived complexity of iWarp, RoCE or RDMA over Converged Eth-
ernet (Guo et al., 2016) was introduced. Recall that RDMA in Infiniband runs over networks that use
credit-based flow control to make the network lossless. Because packet drops are rare in such clusters,
the RDMA Infiniband transport (as implemented on the NIC) was not designed to efficiently recover
from packet losses. When the receiver receives an out-of-order packet, it discards it and sends a NACK;
this causes the sender to retransmits all packets in the window.
    The central idea in RoCE is to run over UDP, not TCP, but to use a crude form of flow control at
switches called PFC (for Priority Flow Control) to prevent packet drops due to congestion, believed
to be the most common cause of loss in the network. The idea is that when a downstream switch is
congested it sends a signal to the upstream switch to make it “pause” before the downstream switch has
to drop packets. This crude form of flow control (compared to credit based flow control in Infiniband)
is easy to implement, but has many potential disadvantages: unfairness cause by head-of-line blocking,
and extreme failure modes such as “pause spreading” and network deadlocks (Guo et al., 2016).
    Despite these disadvantages of RoCE, its perceived simplicity, latency and cost has made RoCE very
popular in data centers. A paper (Mittal et al., 2018) comparing RoCE and iWarp for example suggests
that at the time of comparison, iWarp had a latency that was three times worse, and a throughput
that was four times lower, than RoCE. To be fair, the same paper (Mittal et al., 2018) argues that the
cost-performance disadvantages of iWarp are not fundamental and can be mitigated with a cleverer
implementation, but these ideas have not penetrated to the market to the best of our knowledge.
