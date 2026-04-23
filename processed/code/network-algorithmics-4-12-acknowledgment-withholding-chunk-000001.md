# network-algorithmics-4-12-acknowledgment-withholding (chunk 000001)

# Network Algorithmics — 4.12 Acknowledgment withholding (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 126
- Slice: from `4.12 Acknowledgment withholding` up to next detected section heading

---

4.12 Acknowledgment withholding
Transport protocols such as TCP ensure that data is delivered to the destination by requiring that the
destination send an acknowledgment (ack) for every piece of received data. This is analogous to certi-
fied mail. Packets and acks are numbered. Acks are often cumulative; an ack for a packet numbered N
implicitly acknowledges all packets with numbers less than or equal to N .
    Cumulative acks allow the receiver the flexibility of not sending an ack for every received packet.
Instead, acks can be batched (P2c). For example, in Fig. 4.22 a file transfer program is sending file
blocks, one in every packet. Blocks 1 and 2 are individually acknowledged, but blocks 3 and 4 are
acknowledged with a single ack for block 4.
    Reducing acks is a good thing for the sender and receiver. Although acks are small, they contain
headers that must be processed by every router and the source and the destination. Further, each received
packet, however small, can cause an interrupt at the destination computer, and interrupts are expensive.
Thus, ideally, a receiver should batch as many acks as possible. But what should the receiver batching
policy be? This leads to the following problem.

Problem
Ack withholding is difficult at a receiver that is not clairvoyant. In Fig. 4.22, for example, if block 3
arrives first and is processed quickly, how long should the receiver wait for block 4 before sending the
ack for block 3? If block 4 never arrives (because the sender has no more data to send), then withholding
the ack for block 3 would cause incorrect behavior. The classical solution is to set an ack-withholding
timer; when the timer expires, a cumulative ack is sent. This limits the time that an ack can be withheld.
    However, the withholding timer also causes problems. Some applications are sensitive to latency.
Adding an ack-withholding timer can increase latency in cases where the sender has no more data to
send. If the transport protocol could be modified, what information could be added to avoid unnecessary
latency and yet allow acks to be effectively batched?

100       Chapter 4 Principles in action

FIGURE 4.22
The use of cumulative acks allows the receiver to acknowledge several packets with one ack (e.g., blocks 3 and 4)
but introduces the problem of determining a good receiver ackpolicy.

Hint: In an application such as FTP, which software module knows that there is more data to be
sent? For ack withholding, which software module would ideally like to know that there is more data
to be sent? Now consider using P9 and P10.
