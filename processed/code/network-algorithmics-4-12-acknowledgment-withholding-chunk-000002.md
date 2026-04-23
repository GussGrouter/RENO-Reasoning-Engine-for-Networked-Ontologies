# network-algorithmics-4-12-acknowledgment-withholding (chunk 000002)

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
