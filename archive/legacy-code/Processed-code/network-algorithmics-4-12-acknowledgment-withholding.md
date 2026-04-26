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

Solution
In an application such as file transfer, the sender application knows that there is more data to be sent
(e.g., there will be a block 4 after block 3). The sending application may also be willing to tolerate the
latency due to batching of acks. However, it is the transport module at the receiver that needs to know
this information. This observation leads to a simple proposal.
    The sender application passes a bit to the sender transport (in the application–transport interface)
that is set when the application has more data to send. Assume that the transport protocol can be
modified to carry a withhold bit. The sending transport can use the information passed by the application
to set a withhold bit w in every packet that it sends; w is cleared when the sender wants an immediate
ack. The moral, of course, is that it is better for the sender to telegraph his intentions than for the
receiver to make guesses about the future!
    For example, in Fig. 4.23 the sender transport is informed by the sending file transfer application
that there are four blocks to be sent. Thus the sender transport sets the withhold bit on the first three
packets and clears the bit in the fourth packet. The receiver acts on this information to send one ack
instead of four. On the other hand, an application that is latency sensitive can choose not to pass any
information about data to be sent. Note also that the withhold bit is a hint; the receiver can choose to
ignore this information and send an ack anyway. Despite its apparent cleverness, this solution is a bad
idea in today’s TCP. See the exercises for details.

Exercises

• Another technique for reducing acks is to piggyback acks on data flowing from the receiver to the
  sender. To support this, most transport protocols, such as TCP, have extra fields in data packets to

                                               4.13 Incrementally reading a large database          101




FIGURE 4.23
Telegraphing the sender’s intentions using a withhold bit w.


  convey reverse ack information. However, piggybacking has the same classical trade-off between
  latency and piggybacking efficiency. How long should the receiver transport wait for reverse data?
  On the other hand, there are common applications where the sender application knows this infor-
  mation. How could the solution outlined earlier be extended to support piggybacking as well as ack
  batching?
• Recall that Chapter 3 outlined a set of cautionary questions for evaluating purported improvements.
  For example, Q3 asks whether a change can affect the rest of the system. Why might aggressive
  ack withholding interact with other aspects of the transport protocol, such as flow and congestion
  control (Stevens, 1994)?
