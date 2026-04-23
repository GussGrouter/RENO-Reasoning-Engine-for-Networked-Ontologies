# Network Algorithmics — 9.3 Generic protocol processing (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 251
- Slice: from `9.3 Generic protocol processing` up to next detected section heading

---

9.3 Generic protocol processing
Section 9.1 described techniques for buffering a packet, and Section 9.2 described techniques to effi-
ciently compute packet checksums. The stage is now set to actually process such a packet. The reader
unfamiliar with TCP may wish first to consult the models in Chapter 2.
   Since TCP accounts for 90% of traffic (Braun, 1998) in most sites, it is crucial to efficiently process
TCP packets at close to wire speeds. Unfortunately, a first glance at TCP code is daunting. While the
TCP sender code is relatively simple, Stevens (1994) says:
   TCP input processing is the largest piece of code that we examine in this text. The function tcp_input
   is about 1100 lines of code. The processing of incoming segments is not complicated, just long and
   detailed.
    Since TCP appears to be complex, Greg Chesson and Larry Green formed Protocol Engines, Inc., in
1987, which proposed an alternative protocol called XTP (Chesson, 1989). XTP was carefully designed
with packet headers that were easy to parse and streamlined processing paths. With XTP threatening
to replace TCP, Van Jacobson riposted with a carefully tuned implementation of TCP in BSD UNIX
that is well described in Stevens (1994). This implementation was able to keep up with even 100-Mbps
links. As a result, while XTP is still used (Chesson, 1989), TCP proved to be a runaway success.
    Central to Jacobson’s optimized implementation is a mechanism called header prediction (Jacob-
son, 1993). Much of the complexity of the 1100 lines of TCP receive processing comes when handling
rare cases. Header prediction provides a fast path through the thicket of exceptions by optimizing the
expected case (P11).

TCP header prediction
The first operation on receiving a TCP packet is to find the protocol control block (PCB) that contains
the state (e.g., receive and sent sequence numbers) for the connection of which the packet is a part.
Assuming the connection is set up and that most workstations have only a few concurrent connections,
the few active connection blocks can be cached. The BSD UNIX code (Stevens, 1994) maintains a
one-behind cache containing the PCB of the last segment received; this works well in practice for
workstation implementations.
    After locating the PCB, the TCP header must be processed. A good way to motivate header pre-
diction, found in Partridge (1993), comes from looking at the fields in the TCP header, as shown in
Fig. 9.7.
    After a connection is set up, the destination and source ports are fixed. Since IP networks work
hard to send packets in order, the sequence number is likely to be the next in sequence after the last
packet received. The control bits, often called flag bits, are typically off, with the exception of the ack
bit, which is always set after the initial packet is sent. Finally, most of the time, the receiver does not
change its window size, and the urgent pointer is irrelevant. Thus the only two fields whose information
content is high are the ack number and checksum fields.
    Motivated by this observation, header prediction identifies the expected case as one of two possibil-
ities: receiving a pure acknowledgment (i.e., the received segment contains no data) or receiving a pure
data packet (i.e., the received segment contains an ack field that conveys no new information). In addi-
tion, the packet should also reflect business as usual in the following precise sense: no unexpected TCP
flags should be set, and the flow control window advertised in the packet should be no different from
what the receiver had previously advertised. In pseudocode (simplified from Ref. Jacobson, 1993):

                                                                9.3 Generic protocol processing                  225




FIGURE 9.7
TCP header fields: the fields most likely to change are the checksum and the ack fields. The other fields carry very
little information and can often be predicted from past values.


IF (No unexpected flags) AND (Window in packet is as before)
AND (Packet sequence number is the next expected) THEN
    IF (Packet contains only headers and no data)
    Do Ack Processing
/* Release acked bytes, stop timers, awaken process */
ELSE IF (Packet does not ack anything new) /* pure data */
    Copy data to user buffer while checksumming;
    Update next sequence number expected;
    Send Acks if needed and release buffer;
ENDIF
ELSE /* header prediction failed -\/- take long path */
...

Clearly, this code is considerably shorter than the complete TCP receive processing code. However,
some of the checks can be made more efficient by leveraging off the fact that most machines can do
efficient comparisons in units of a machine word size (P4a, exploit locality).
     For example, consider the TCP flags contained in the control bits of Fig. 9.7. There are six flags,
each encoded as a bit: SYN, FIN, RESET, PUSH, URG, ACK. If it is business as usual, all the flags
must be clear, with the exception of ACK, which must be set, and PUSH, which is irrelevant. Checking
for each of these conditions individually would require several instructions to extract and compare each
bit.
     Instead, observe that the flags field is the fourth word of the TCP header and that the window size is
contained in the last 16 bits. In the header prediction code the sender precomputes (P2a) the expected
value of this word by filling in all the expected values of the flag and using the last advertised value of
the window size.
     The expected value of the fourth TCP header word is stored in the PCB entry for the connection.
Given this setup, the first two checks in the pseudocode shown earlier can be accomplished in one
stroke by comparing the fourth word of the TCP header in the incoming packet with the expected value
stored in the PCB. If all goes well, and tests indicate they often do, the expected value of the fourth
field is computed only at the start of the connection. It is this test that explains the origin of the name
header prediction: a portion of the header is being predicted and checked against an incoming segment.

226      Chapter 9 Protocol processing



    The pseudocode described earlier is abstracted from the implementation by Jacobson in a research
kernel (Jacobson, 1993) that claims to do TCP receiving processing in 30 Sun SPARC instructions! The
BSD UNIX code given in Stevens (1994) is slightly more complicated, having to deal with mbufs and
with the need to eliminate other possibilities, such as the PAWS (TCP Sequence number wrapping) test
(Stevens, 1994).
    The discussion so far has been limited to TCP receive processing because it is more complex than
sending a TCP segment. However, a dual of header prediction exists for the sender side. If only a few
fields change between segments, the sender may benefit from keeping a template TCP (and IP) header
in the connection block. When sending a segment, the sender need only fill in the few fields that change
into the template. This is more efficient if copying the TCP header is more efficient than filling in each
field. Caching of sending packet headers is implemented in the Linux kernel.
    Before finishing this topic, it is worth recalling Caveat Q8 and examining how sensitive this opti-
mization is to the system environment. Originally, header prediction was targeted at workstations. The
underlying assumption (that the next segment is for the same connection and is one higher in sequence
number than the last received segment) works well in this case.
    Clearly, the assumption that the next segment is for the same connection works poorly in a server en-
vironment. This was noted as early as Jacobson (1993), who suggested using a hash of the port numbers
to quickly locate the PCB. McKenney and Dove confirmed this by showing that using hashing to locate
the PCB can speed up receive processing by an order of magnitude in an OLTP (online transaction
processing) environment.
    The FIFO (first in, first out) assumption is much harder to work around. While some clever schemes
can be used to do sequence number processing for out-of-order packets, there are some more funda-
mental protocol mechanisms in TCP that build on the FIFO assumption. For example, if packets can
be routinely misordered, TCP receivers will send duplicate acknowledgments. In TCP’s fast retrans-
mit algorithm (Stevens, 1994) TCP senders use three duplicate acknowledgments to infer a loss (see
Chapter 14).
    Thus lack of FIFO behavior can cause spurious retransmissions, which will lower performance
more drastically as compared to the failure of header prediction. However, as TCP receivers evolve to
do selective acknowledgment (Floyd et al., 1999), this could allow fast TCP processing of out-of-order
segments in the future.
