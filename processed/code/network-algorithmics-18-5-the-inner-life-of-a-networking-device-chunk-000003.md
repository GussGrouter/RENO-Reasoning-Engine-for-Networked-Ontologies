# network-algorithmics-18-5-the-inner-life-of-a-networking-device (chunk 000003)

sequence number of the first byte in a segment is carried explicitly; the sequence numbers of the other
bytes are implicit, based on their offset.
    When the 20-byte GET message arrives at the receiver, the receiving TCP delivers it to the receiving
Web application. The Web server at D may respond with a Web page of (say) 1900 bytes that it writes
to the receiver TCP input queue along with an HTTP header of 100 bytes, making a total of 2000 bytes.
TCP can choose to break up the 2000-byte data arbitrarily into segments; the example of Fig. A.1 uses
two segments of 1500 and 500 bytes.
    Assume for variety that the second segment of 500 bytes is lost in the network; this is shown in a
time–space picture by a message arrow that does not reach the other end. Since the receiver does not
receive an ACK, the receiver retransmits the second segment after a timer expires. Note that ACKs
are cumulative: A single ACK acknowledges the byte specified and all previous bytes. Finally, if the
sender is done, the sender begins closing the connection with a FIN message that is also asked (if all
goes well), and the receiver does the same.
    Once the connection is closed with FIN messages, the receiver TCP keeps no sequence number in-
formation about the sender application that terminated. But networks can also cause duplicates (because
of retransmissions, say) of SYN and DATA segments that appear later and confuse the receiver. This is
why the receiver in Fig. A.1 does not believe any data that is in a SYN message until it is validated by
receiving a third message containing the unused number Y the receiver picked. If Y is echoed back in a
third message, then the initial message is not a delayed duplicate, since Y was not used recently. Note
that if the SYN is a retransmission of a previously closed connection, the sender will not echo back Y ,
because the connection is closed.
    This preliminary dance featuring a SYN and a SYN-ACK is called TCP’s three-way handshake. It
allows TCP to forget about past communication, at the cost of increased latency to send new data. In
practice, the validation numbers X and Y do double duty as the initial sequence numbers of the data
segments in each direction. This works because sequence numbers need not start at 0 or 1 as long as
both sender and receiver use the same initial value.
    The TCP sequence numbers are carried in a TCP header contained in each segment. The TCP header
contains 16 bits for the destination port (recall that a port is like a telephone extension that helps identify
the receiving application), 16 bits for the sending port (analogous to a sending application extension),
a 32-bit sequence number for any data contained in the segment, and a 32-bit number acknowledging
any data that arrived in the reverse direction. There are also flags that identify segments as being SYN,
FIN, etc. A segment also carries a routing header1 and a link header that changes on every link in the
path.
    If the application is (say) a videoconferencing application that does not want reliability guarantees,
it can choose to use a protocol called UDP (user datagram protocol) instead of TCP. Unlike TCP,
UDP does not need acks or retransmissions, because it does not guarantee reliability. Thus the only
sensible fields in the UDP header corresponding to the TCP header are the destination and source port
numbers. Like ordinary mail versus certified mail, UDP is cheaper in bandwidth and processing but
offers no reliability guarantees. For more information about TCP and UDP, Stevens (1994) is highly
recommended.

1 The routing header is often called the Internet protocol, or IP, header.

532       Detailed models

FIGURE A.2
A sample network topology corresponding to the Internet of Fig. A.1.
