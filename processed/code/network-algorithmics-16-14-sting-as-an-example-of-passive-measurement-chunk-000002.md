# network-algorithmics-16-14-sting-as-an-example-of-passive-measurement (chunk 000002)

16.14 Sting as an example of passive measurement
So far, this chapter has dealt exclusively with router measurement problems that involve changes to
router implementations and to other subsystems, such as routing protocols. While such changes can be
achieved with the cooperation of a few dominant router vendors, they do face the difficulty of incre-
mental deployment. By contrast to the schemes already described, passive measurement focuses on the
ability to trick a network into providing useful measurement data without changing network internals.
The basic idea is to get around the lack of measurement support provided by the Internet protocol suite.
    Imagine you are no longer an ISP but a network manager at the Acme Widget Company. An upstart
ISP is claiming to provide better service than your existing ISP. You would like to conduct a test to see
whether this is true. To do so, you want to determine end-to-end performance measurements from your
site to various Web servers across the country, using both ISPs in turn.
    The standard solution is to use tools, such as Ping and Traceroute, that are based on sending ICMP
messages. The difficulty with these tools is that ISPs regularly filter or rate-limit such messages because
of their use by hackers.
    An idea that gets around this limitation was introduced by Sting (1999) tool, invented by Stefan
Savage. The main idea is to send measurement packets in the clothing of TCP packets; ISPs and Web
servers cannot drop or rate-limit such packets without penalizing good clients. Then every protocol
mechanism of TCP becomes a degree of freedom (P13) for the measurement tool.
    Consider the problem of determining the loss probability between a source and a distant Web server.
This may be useful to know if most of the traffic is sent in only one direction, as in a video broadcast.
Even if Ping were not rate-limited, Ping only provides the combined loss probability in both directions.
    The Sting idea to find the loss probability from the source to the server is as follows. The algorithm
starts by making a normal TCP connection to the server and sending N data packets to the server in
sequence. Acknowledgments are ignored: After all, it’s measurements we are after, not data transfer.
    After the data-seeding stage, the algorithm moves into a second stage, called hole filling. Hole filling
starts with sending a single data packet with sequence number 1 greater than the last packet sent in the
first phase. If an acknowledgment is received, all is well; no data packets were lost.
    If not, after sufficient retransmission, the receiver will respond with the highest number, X, received
in sequence. The sender tool now sends only the segment corresponding to X + 1. Eventually, an up-
dated acknowledgment arrives with the next highest received in sequence. The receiver fills in this next
hole and marches along until all “holes” are filled. At the end of the second phase, the sender knows
exactly which data packets were lost in the first phase and can compute the loss rate.
    It is more of a challenge to compute the reverse loss rate because the receiver TCP may batch
acknowledgments. However, once it is grasped that the tool is not limited to behaving like a normal
TCP connection, all the stops can be loosed. By sending packets out of order in the first phase and a
series of bizarre ploys, the receiver is conned into providing the required information.
    At this point, the theoretician may shake his head sadly and say, “It’s a bunch of tricks. I always
knew these network researchers were not quite the thing.” Indeed, Sting employs a collection of tricks
to compute its particular metrics. But the idea of using TCP’s venerable protocol mechanisms as a
palette for measurement is perhaps an eye-opener. It has influenced later measurement tools, such as
TBIT (Padhye and Floyd, 2001) that used the same general idea to measure the extent to which new
TCP features were deployed.
    Of course, the idea is not limited to TCP but applies to any protocol. Any protocol, including BGP,
can be subverted for the purposes of measurement. Philosophically, this is, however, dangerous ground
