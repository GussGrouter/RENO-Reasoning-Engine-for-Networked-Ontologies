# Network Algorithmics — 5.3.2 Modern-day incarnations of RDMA (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 155
- Slice: from `5.3.2 Modern-day incarnations of RDMA` up to next detected section heading

---

5.3.2 Modern-day incarnations of RDMA
VAX Clusters introduced a very early storage area network. Storage area networks (SANs) are back-
end networks that connect many computers to shared storage, in terms of network-attached disks. There
are several successors to VAX Clusters that provide SAN technology today. These range from the
venerable Fiber Channel (Benner, 1995) technology to modern upstarts such as Infiniband (Infiniband
Trade Association, 2001) and iSCSI (Satran et al., 2001).

Fiber channel
In 1988 the American National Standards Institute (ANSI) Task Group X3T11 began work on a stan-
dard called Fibre Channel (Benner, 1995). One of the goals of Fibre Channel was to take the standard
SCSI (small computer system interface) between a workstation and a local disk and extend it over larger
distances. Thus in many Fibre Channel installations, SCSI is still used as the protocol that runs over
Fiber Channel.
    Fibre Channel goes further than VAX Clusters in the underlying network, using modern network
technology such as point-to-point fiber links connected with switches. This allows speeds of up to 64
Gbps and allows a larger distance span than in the Vax Cluster network. Switches can even be remotely
connected, allowing a trading firm to have backup storage of all trades at a remote site. The use of
switches requires attention to such issues as credit flow control, which is done very carefully to avoid
dropping packets where possible to maintain the illusion of a lossless computer bus over the network.
    Fibre Channel also makes slightly more concession to security than VAX Clusters. In VAX Clusters
any device with the right name can overwrite the memory of any other device. Fiber Channel allows
the network to be virtualized into zones. Nodes in a zone cannot access the memory of nodes in other
zones. Some recent products go even further and propose techniques based on authentication.

                                              5.3 Avoiding copying using remote DMA                129



    However, other than these differences in the underlying technology, the underlying ideas are the
same. RDMA via named buffers is still a key enabling idea. While Fibre Channel has had much recent
competition from Ethernet based RDMA methods such as RoCE (Guo et al., 2016) (see below), it
has still been the mainstay of storage area networks (SANs) for two decades and shows no signs of
disappearing.
    One reason for its continued popularity (The State of Fibre Channel, 2022) may be the popularity of
solid state disks or NVM (Non Volatile Memory) especially over the PCI Express bus (NVMe). Fibre
Channel latencies are particularly low. Thus despite the potential cost advantages of Ethernet solutions,
the performance of Fibre Channel may explain its continued use in SANs.

Infiniband
Infiniband starts with the observation that the internal I/O bus used within many workstations and PCs,
the PCI bus, is showing its age and needs replacement. With a maximum bandwidth of 533 MB/sec, the
PCI bus is being overwhelmed by modern high-speed peripherals, such as Gigabit Ethernet interface
cards. While there are some temporary alternatives, such as the PCI-X bus, the internal computer inter-
connect needs to scale in the same way as the external Internet has scaled from, say, 10-Mbit Ethernet
to Gigabit Ethernet.
    Also, observe that there are three separate networking technologies within a computer: the network
interface (e.g., Ethernet), the disk interface (e.g., SCSI over Fibre Channel), and the PCI bus. Occam’s
razor suggests substituting these three with one network technology. Accordingly, Compaq, Dell, HP,
IBM, and Sun banded together to form the Infiniband Trade Association.
    The Infiniband specifications use many of the ideas in Fibre Channel’s underlying network technol-
ogy. The interconnect is also based on switches and point-to-point links. Infiniband has a few additional
twists. It uses the proposal for 128-bit IP addresses in the next-generation Internet as a basis for ad-
dressing. It allows individual physical links to be virtualized into separate virtual links called lanes.
It has features for quality of service and even multicast. Once again, RDMA is the key technology to
avoid copies.
    While Infiniband has not enjoyed the spurt in popularity of Ethernet based solutions described next
or even that of Fibre Channel in Storage Area Networks, it is still widely used in supercomputing instal-
lations for high performance computing (SHARP, 2019). It is also used for speeding up large machine
learning workloads using abstractions for in-network computing called SHARP that we describe in
Section 5.5. For instance, it is used in two of the world’s largest supercomputers in Oakridge and Los
Alamos, with close to 10,000 Infiniband nodes each (SHARP, 2019).

iSCSI via iWarp and RoCE
Given that IP has invaded various other networking spaces, such as voice, TV, and radio, a natural
consequence is to invade the storage space. This, the argument goes, should drive down prices (while
also opening up new markets for network vendors). Further, Fibre Channel and Infiniband are being
extended to connect remote data centers over the Internet. This involves using transport protocols that
are not necessarily compatible with TCP in terms of reacting to congestion. Why not just adapt TCP
for this purpose instead of trying to modify these other protocols to be TCP friendly?
    For the purposes of this chapter, the most interesting thing about iSCSI is the way it must emulate
RDMA over standard IP protocols. In particular recall that in all RDMA implementations, the host

130      Chapter 5 Copying data



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

                                                            5.4 Broadening to file systems             131
