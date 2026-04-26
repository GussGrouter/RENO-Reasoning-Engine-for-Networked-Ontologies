# network-algorithmics-9-3-generic-protocol-processing (chunk 000003)

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
