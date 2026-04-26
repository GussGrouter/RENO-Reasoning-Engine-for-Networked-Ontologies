# network-algorithmics-14-2-random-early-detection (chunk 000001)

# Network Algorithmics — 14.2 Random early detection (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 413
- Slice: from `14.2 Random early detection` up to next detected section heading

---

14.2 Random early detection
RED is a packet-scheduling algorithm implemented in most modern routers, even at the highest speeds,
that has become a de facto standard. In a nutshell a RED router monitors the average output-queue
length; when this goes beyond a threshold, it randomly drops arriving packets with a certain probability,
even though there may be space to buffer the packet. The dropped packet acts as a signal to the source
to slow down early, preventing a large number of dropped packets later.
    To understand RED, we must review the Internet-congestion-control algorithm. The top of Fig. 14.2
shows a network connecting source S and destination D. Imagine the network had links with a capacity
of 1 Mbps and that a file transfer can occur at 1 Mbps. Now suppose the middle link is replaced by
a faster, 10-Mbps link. Surely it can’t make things worse, can it? Well, in the old days of the Internet
it did. Packets arrived at a 10-Mbps rate at the second router, which could only forward packets at
1 Mbps; this caused a flood of dropped packets, which led to slow retransmissions. This resulted in a
very low throughput for the file transfer.
    Fortunately, the dominant Internet transport protocol, TCP, added a mechanism called TCP conges-
tion control, which is depicted in Fig. 14.2. The source maintains a window of size W , which is the
number of packets the source will send without an acknowledgment. Controlling window size controls
the source rate because the source is limited to a rate of W packets in a trip delay to the destination. As
shown in Fig. 14.2, a TCP source starts W at 1. Assuming no dropped packets, the source increases its

14.2 Random early detection                     387

FIGURE 14.2
An illustration of TCP congestion control as a prelude to RED.
