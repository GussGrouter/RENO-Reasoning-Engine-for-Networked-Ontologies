# network-algorithmics-18-5-the-inner-life-of-a-networking-device (chunk 000002)

A.1.1 Transport protocols
When you point your Web browser to www.cs.ucsd.edu, your browser first converts the destination host
name (i.e., cs.ucsd.edu) into a 32-bit Internet address, such as 132.239.51.18, by making a request to a
local DNS name server (Perlman, 1992); this is akin to dialing directory assistance to find a telephone
number. A 32-bit IP address is written in dotted decimal form for convenience; each of the four numbers
between dots (e.g., 132) represents the decimal value of a byte. Domain names such as cs.ucsd.edu
appear only in user interfaces; the Internet transport and routing protocols deal only with 32-bit Internet
addresses.
    Networks lose and reorder messages. If a network application cares that all its messages are received
in sequence, the application can subcontract the job of reliable delivery to a transport protocol such
as TCP. It is the job of TCP to provide the sending and receiving applications with the illusion of
two shared data queues in each direction, despite the fact that the sender and receiver machines are
separated by a lossy network. Thus whatever the sender application writes to its local TCP send queue
should magically appear in the same order at the local TCP receive queue at the receiver, and vice versa.
    Since Web browsers care about reliability, the Web browser at sender S (Fig. A.1) first contacts
its local TCP with a request to set up a connection to the destination application. The destination
application is identified by a well-known port number (such as 80 for Web traffic) at the destination
IP address. If IP addresses are thought of as telephone numbers, port numbers can be thought of as
extension numbers. A connection is the shared state information, such as sequence numbers and timers,
at the sender and receiver TCP programs that facilitate reliable delivery.
                                                                                                     529

530      Detailed models

FIGURE A.1
Time–space figure of a possible scenario for a conversation between Web client S and Web server D as mediated
by the reliable transport protocol TCP. Assume that the ack to the SYN-ACK is piggybacked on the 20-byte GET
message.

Fig. A.1 is an example of a time–space figure, with time flowing downward and space represented
horizontally. A line from S to D that slopes downward represents the sending of a message from S to
D, which arrives at a later time.
    To set up a connection, the sending TCP (Fig. A.1) sends out a request to start the connection, called
a SYN message, with a number X the sender has not used recently. If all goes well, the destination will
send back a SYN-ACK to signify acceptance, along with a number Y that the destination has not used
before. Only after the SYN-ACK is the first data message sent.
    The messages sent between TCPs are called TCP segments. Thus to be precise, the following models
will refer to TCP segments and to IP packets (often called datagrams in IP terminology).
    In Fig. A.1 the sender is a Web client, whose first message is a small (say) 20-byte HTTP GET
message for the Web page (e.g., index.html) at the destination. To ensure message delivery, TCP will
retransmit all segments until it gets an acknowledgment. To ensure that data is delivered in order and
to correlate acks with data, each byte of data in a segment carries a sequence number. In TCP only the

Detailed models          531
