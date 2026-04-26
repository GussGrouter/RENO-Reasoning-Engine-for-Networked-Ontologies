# Network Algorithmics — 18.5 The inner life of a networking device (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 555
- Slice: from `18.5 The inner life of a networking device` up to next detected section heading

---

18.5 The inner life of a networking device
We have tried to summarize in this chapter the major themes of this book in terms of the techniques
described and the principles used. We have also tried to argue that network algorithmics is used in
real products and is likely to find further application in the future because of new abstractions, new
connecting disciplines, and new requirements. While the specific techniques and problems may change,
we hope the principles involved remain useful.
    Besides the fact that network algorithmics is useful in building better and faster network devices,
we hope this book makes the case that network algorithmics is also intellectually stimulating. While it
may lack the depth of hard problems in theoretical computer science or physics, perhaps what can be
most stimulating is the breadth, in terms of the disciplines it encompasses.
    An endnode, for instance, may appear as a simple processing state machine at the highest level of
abstraction. A more detailed inspection would see a Web request packet arriving at a server interface,
the interrupt firing, and the protocol code being scheduled via a software interrupt. Even within the
protocol code, each line of code has to be fetched, hopefully from the I-cache, and each data item has
to go through the VM system (via the TLB hopefully) and the data cache. Finally, the application must
get involved via a returned system call and a process-scheduling operation. The request may trigger file
system activity and disk activity.
    A router similarly has an interesting inner life. Reflecting the macrocosmos of the Internet outside
the router is a microcosmos within the router consisting of major subsystems, such as line cards and the
switch fabric, together with striping and flow control across chip-to-chip links.
    Network algorithmics seeks to understand these hidden subsystems of the Internet to make the In-
ternet faster. This book is a first attempt to begin understanding, in Feynman’s phrase, this “tremendous
world of interconnected hierarchies” within routers and endnodes. In furthering this process of under-
standing and streamlining these hierarchies, there are still home runs to be hit and touchdowns to be
scored as the game against networking bottlenecks continues to be played.

                                                                                            APPENDIX


Detailed models
                                                                                           A
This appendix contains further models and information that can be useful for some readers of this
book. For example, the protocols section may be useful for hardware designers who wish to work
in networking but need a quick self-contained overview of protocols such as TCP and IP to orient
themselves. On the other hand, the hardware section provides insights that may be useful for software
designers without requiring a great deal of reading. The switch section provides some more details
about switching theory.



A.1 TCP and IP
To be self-contained, Section A.1.1 provides a very brief sketch of how transmission control protocol
(TCP) operates, and Section A.1.2 briefly describes how IP routing operates.


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

A.1.2 Routing protocols
Fig. A.2 shows a more detailed view of a plausible network topology between Web client S and Web
server D of Fig. A.1. The source is attached to a local area network such as an Ethernet, to which is
also connected a router, R1. Routers are the automated post offices of the Internet, which consult the
destination address in an Internet message (often called a packet) to decide on which output link to
forward the message.
    In the figure source S belongs to an administrative unit (say, a small company) called a domain. In
this simple example, the domain of S consists only of an Ethernet and a router, R1, that connects to an
Internet service provider (ISP) through router R2. Our Internet service provider is also a small outfit,
and it consists only of three routers, R2, R3, and R4, connected by fiber-optic communication links.
Finally, R4 is connected to router R5 in D’s domain, which leads to the destination, D.
    Internet routing is broken into two conceptual parts, called forwarding and routing. First consider
forwarding, which explains how packets move from S to D through intermediate routers.
    When S sends a TCP packet to D, it first places the IP address of D in the routing header of the
packet and sends it to the neighboring router, R1. Forwarding at endnodes such as S and D is kept
simple and consists of sending the packet to an adjoining router. R1 realizes it has no information
about D and so passes it to ISP router R2. When it gets to R2, R2 must choose to send the packet to
either R3 or R4. R2 makes its choice based on a forwarding table at R2 that specifies (say) that packets
to D should be sent to R4. Similarly, R4 will have a forwarding entry for traffic to D that points to R5.
A description of how forwarding entries are compressed using prefixes can be found in Section 2.3.2. In
summary, an Internet packet is forwarded to a destination by following forwarding information about
the destination at each router. Each router need not know the complete path to D, but only the next hop
to get to D.
    While forwarding must be done at extremely high speeds, the forwarding tables at each router must
be built by a routing protocol. For example, if the link from R2 to R4 fails, the routing protocol within
the ISP domain should change the forwarding table at R2 to forward packets to D to R3. Typically,
each domain uses its own routing protocol to calculate shortest-path routes within the domain. Two
main approaches to routing within a domain are distance vector and link state.
    In the distance vector approach exemplified by the protocol RIP (Perlman, 1992), the neighbors of
each router periodically exchange distance estimates for each destination network. Thus in Fig. A.2
R2 may get a distance estimate of 2 to D’s network from R3 and a distance estimate of 1 from R4.
Thus R2 picks the shorter-distance neighbor, R4, to reach D. If the link from R2 to R4 fails, R2 will

                                                                             Detailed models        533



time-out this link, set its estimate of distance to D through R4 to infinity, and then choose the route
through R3. Unfortunately, distance vector takes a long time to converge when destinations become
unreachable (Perlman, 1992).
    Link state routing (Perlman, 1992) avoids the convergence problems of distance vector by having
each router construct a link state packet (LSP) listing its neighbors. In Fig. A.2 for instance, R3’s
LSP will list its links to R2 and R4. Each router then broadcasts its LSP to all other routers in the
domain using a primitive flooding mechanism; LSP sequence numbers are used to prevent LSPs from
circulating forever. When all routers have each other’s LSP, every router has a map of the network and
can use Dijkstra’s algorithm (Perlman, 1992) to calculate shortest-path routes to all destinations. The
most common routing protocol used within ISP domains is a link state routing protocol called open
shortest path first (OSPF) (Perlman, 1992).
    While shortest-path routing works well within domains, the situation is more complex for routing
between domains. Imagine that Fig. A.2 is modified so that the ISP in the middle, say, ISP A, does not
have a direct route to D’s domain but instead is connected to ISPs C and E, each of which has a path
to D’s domain. Should ISP A send a packet addressed to D to ISP C or E? Shortest-path routing no
longer makes sense because ISPs want to route based on other metrics (e.g., dollar cost) or on policy
(e.g., always send data through a major competitor, as in so-called “hot potato” routing).
    Thus interdomain routing is a more messy kettle of fish than routing within a domain. The most
commonly used interdomain protocol today is called the border gateway protocol (BGP) (Stevens,
1998), which uses a gossip mechanism akin to distance vector, except that each route is augmented
with the path of domains instead of just the distance. The path ostensibly makes convergence faster
than the distance vector and provides information for policy decisions.
    To go beyond this brief sketch of routing protocols, the reader is directed to Interconnections by
Radia Perlman (1992) for insight into routing in general and to BGP-4 by John Stewart (1999) as the
best published textbook on the arcana of BGP.



A.2 Hardware models
For completeness, this section contains some details of hardware models that were skipped in Chapter 2
for the sake of brevity. These detailed models are included in this section to provide a somewhat deeper
understanding for software designers.

A.2.1 From transistors to logic gates
The fundamental building block of the most complex network processor is a transistor (Fig. A.3).
A transistor is a voltage-controlled switch. More precisely, a transistor is a device with three external
attachments (Fig. A.3): a gate, a source, and a drain. When an input voltage I is applied to the gate, the
source-drain path conducts electricity; when the input voltage is turned off, the source-drain path does
not conduct. The output O voltage occurs at the drain. Transistors are physically synthesized on a chip
by having a polysilicon path (gate) cross a diffusion path (source-drain) at points governed by a mask.
    The simplest logic gate is an inverter (also known as a NOT gate). This gate is formed (Fig. A.3)
by connecting the drain to a power supply and the source to ground (0 volts). The circuit functions as
an inverter because when I is a high voltage (i.e., I = 1), the transistor turns on, “pulling down” the
output to ground (i.e., O = 0). On the other hand, when I = 0, the transistor turns off, “pulling up” the

534        Detailed models




FIGURE A.3
A transistor is a voltage-controlled switch allowing the source-to-drain path to conduct current when the gate voltage
is high. An inverter is a transistor whose source is connected to ground and whose drain is connected to a power
supply.


output to the power supply (i.e., O = 1). Thus an inverter output flips the input bit, implementing the
NOT operation. Although omitted in our pictures, real gates also add a resistance in the path to avoid
“shorting” the power supply when I = 1, by connecting it directly to ground.
    The inverter generalizes to a NAND gate (Fig. A.4) of two inputs, I1 and I2, using two transistors
whose source-drain paths are connected in series. The output O is pulled down to ground if and only
if both transistors are on, which happens if and only if both I 1 and I 2 are 1. Similarly, a NOR gate is
formed by placing two transistors in parallel.

A.2.2 Timing delays
Fig. A.3 assumes that the output changed instantaneously when the input changed. In practice, when
I is turned from 0 to 1, it takes time for the gate to accumulate enough charge to allow the source-
drain path to conduct. This is modeled by thinking of the gate input as charging a gate capacitor (C) in
series with a resistor (R). If you don’t remember what capacitance and resistance are, think of charge
as water, voltage as water pressure, capacitance as the size of a container that must be filled with water,
and resistance as a form of friction impeding water flow. The larger the container capacity and the larger
the friction, the longer the time to fill the container. Formally, the voltage at time t after the input I is
set to V is V (1 − e−t/RC ). The product RC is the charging time constant; within one time constant, the
output reaches 1 − 1/e = 63.2% of its final value.
    In Fig. A.3 notice also that if I is turned off, output O pulls up to the power supply voltage. But to
do so, the output must charge one or more gates to which it is connected, each of which is a resistance
and a capacitance (the sum of which is called the output load). For instance, in a typical 0.18-micron
process,2 the delay through a single inverter driving an output load of four identical inverters is 60
picoseconds.


2 Semiconductor processes are graded by the smallest gate lengths they can produce. Shrinking process width decreases capaci-
tances and resistances and so increases speed.

                                                                            Detailed models        535




FIGURE A.4
Using two transistors in series to create a NAND gate.



    Charging one input can cause further outputs to charge further inputs, and so on. Thus for a combi-
natorial function, the delay is the sum of the charging and discharging delays over the worst-case path
of transistors. Such path delays must fit within a minimum packet arrival time. Logic designs are sim-
ulated to see if they meet timing using approximate analysis as well as accurate circuit models, such as
Spice. Good designers have intuition that allows them to create designs that meet timing. A formaliza-
tion of such intuition is the method of logical effort (Sutherland et al., 1999), which allows a designer
to make quick timing estimates. Besides the time to charge capacitors, another source of delay is wire
delay.


A.2.3 Hardware design building blocks
This section describes some standard terminology for higher-level building blocks used by hardware
designers that can be useful to know.

Programmable logic arrays and programmable array logics
A programmable logic array (PLA) has the generality of a software lookup table but is more compact.
Any binary function can be written as the OR of a set of product terms, each of which is the AND of a
subset of (possibly complemented) inputs. The PLA thus has all the inputs pass through an AND plane,
where the desired product terms are produced by making the appropriate connections. The products are
then routed to an OR plane. A designer produces specific functions by making connections within the
PLA. A more restrictive but simpler form of PLA is a PAL (programmable array logic).

536       Detailed models




FIGURE A.5
To store the output of an inverter indefinitely in the absence of writes, the output is fed back to the input after a
second inversion. Two further transistors are used to allow writes and to block the feedback refresh.


Standard cells
Just as software designers reuse code, so also do hardware designers reuse a repertoire of commonly
occurring functions, such as multiplexers and adders.
    The functional approach to design is generally embodied in standard cell libraries and gate array
technologies, in which a designer must map his or her specific problem to a set of building blocks
offered by the technology. At even higher abstraction levels, designers use synthesis tools to write
higher-level language code in Verilog or VHDL for the function they wish to implement. The VHDL
code is then synthesized into hardware by commercial tools. The trade-off is reduced design time, at
some cost in performance. Since a large fraction of the design is not on the critical path, synthesis can
greatly reduce time to market. This section ends with a networking example of the use of reduction for
a critical path function.


A.2.4 Memories: the inside scoop
This section briefly describes implementation models for registers, static random access memories
(SRAMs), and dynamic RAMs (DRAMs).

Registers
How can a bit be stored such that in the absence of writes and power failures, the bit stays indefinitely?
Storing a bit as the output of the inverter shown in Fig. A.3 will not work, because, left to itself, the
output will discharge from a high to a low voltage via “parasitic” capacitances. A simple solution is to
use feedback: in the absence of a write the inverter output can be fed back to the input and “refresh” the
output. Of course, an inverter flips the input bit, and so the output must be inverted a second time in the
feedback path to get the polarity right, as shown in Fig. A.5. Rather than show the complete inverter
(Fig. A.3), a standard triangular icon is used to represent an inverter.
   Input to the first transistor must be supplied by the write input when a write is enabled and by the
feedback output when a write is disabled. This is accomplished by two more “pass” transistors. The

                                                                                    Detailed models          537




FIGURE A.6
A DRAM cell stores a bit using charge on a capacitor that leaks away slowly and must be refreshed periodically.


pass transistor whose gate is labeled “Refresh Enable” is set to high when a write is disabled, while the
pass transistor whose gate is labeled “Write Enable” is set to high when a write is enabled. In practice,
refreshes and writes are done only at the periodic pulses of a systemwide signal called a clock. Fig. A.5
is called a flip-flop.
    A register is an ordered collection of flip-flops. For example, most modern processors (e.g., the Pen-
tium series) have a collection of 32- or 64-bit on-chip registers. A 32-bit register contains 32 flip-flops,
each storing a bit. Access from logic to a register on the same chip is extremely fast, say, 0.5–1 nanosec-
ond. Access to a register off-chip is slightly slower because of the delay to drive larger off-chip loads.

Static RAM
A SRAM contains N registers addressed by log N address bits A. SRAM is so named because the
underlying flip-flops refresh themselves and so are “static.” Besides flip-flops, an SRAM needs a de-
coder that decodes A into a unary value used to select the right register. Accessing an SRAM on-chip
is only slightly slower than accessing a register because of the added decode delay. At the time of
writing, it was possible to obtain on-chip SRAMs with 0.5 nanoseconds access times. Access times of
1–2 nanoseconds for on-chip SRAM and 5–10 nanoseconds for off-chip SRAM are common. On-chip
SRAM is limited to around 64 Mbits today.

Dynamic RAM
The SRAM bit cell of Fig. A.5 requires at least five transistors. Thus SRAM is always less dense or
more expensive than memory technology based on DRAM. In Fig. A.6 a DRAM cell uses only a single
transistor connected to an output capacitance. The transistor is only used to connect the write input to
the output when the write enable signal on the gate is high. The output voltage is stored on the output
capacitance, which is significantly larger than the gate capacitance; thus the charge leaks, but slowly.
Loss due to leakage is fixed by refreshing the DRAM cell externally within a few milliseconds.
    To obtain high densities, DRAMs use “pseudo-three-dimensional trench or stacked capacitors”
(Fromm et al., 1997); together with the factor of 5–6 reduction in the number of transistors, a DRAM
cell is roughly 16 times smaller than an SRAM cell (Fromm et al., 1997).
    The compact design of a DRAM cell has another important side effect: a DRAM cell requires
higher latency to read or write than the SRAM cell of Fig. A.5. Intuitively, if the SRAM cell of Fig. A.5

538      Detailed models



is selected, the power supply quickly drives the output bit line to the appropriate threshold. On the
other hand, the capacitor in Fig. A.6 has to drive an output line of higher capacitance. The resulting
small voltage swing of a DRAM bit line takes longer to sense reliably. In addition, DRAMs need extra
delay for two-stage decoding and for refresh. DRAM refreshes are done automatically by the DRAM
controller’s periodically enabling RAS for each row R, thereby refreshing all the bits in R.


A.2.5 Chip design
Finally, it may be useful for networking readers to understand how chips for networking functions are
designed.
    After partitioning functions between chips, the box architect creates a design team for each chip and
works with the team to create chip specification. For each block within a chip, logic designers write
software register transfer level (RTL) descriptions using a hardware design language such as Verilog or
VHDL. Block sizes are estimated and a crude floor plan of the chip is done in preparation for circuit
design.
    At this stage, there is a fork in the road. In synthesized design the designer applies synthesis tools to
the RTL code to generate hardware circuits. Synthesis speeds the design process but generally produces
slower circuits than custom-designed circuits. If the synthesized circuit does not meet timing (e.g.,
8 nsec for OC-768 routers), the designer redoes the synthesis after adding constraints and tweaking
parameters. In custom design, on the other hand, the designer can design individual gates or drag-
and-drop cells from a standard library. If the chip does not meet timing, the designer must change the
design (Sutherland et al., 1999). Finally, the chip “tapes out” and is manufactured, and the first yield is
inspected.
    Even at the highest level, it helps to understand the chip design process. For example, systemwide
problems can be solved by repartitioning functions between chips. This is easy when the chip is being
specified, is an irritant after RTL is written, and causes blood feuds after the chip has taped out. A second
“spin” of a chip is something that any engineering manager would rather work around.

Interconnects, power, and packaging
Chips are connected using either point-to-high connections known as high-speed serial links, shared
links known as buses, or parallel arrays of buses known as crossbar switches. Instead of using N 2
point-to-point links to connect N chips, it is cheaper to use a shared bus. A bus is similar to any shared
media network, such as an Ethernet, and requires an arbitration protocol often implemented (unlike an
Ethernet) using a centralized arbiter. Once a sender has been selected in a time slot, other potential
senders must not send any signals. Electrically, this is done by having transmitters use a tristate output
device that can output a0 or a1 or be in a high-impedance state. In a high-impedance state there is no
path through the device to either the power supply or ground. Thus the selected transmitter sends 0’s or
1’s, while the nonselected transmitters stay in a high-impedance state.
    Buses are limited today to around 20 Gb/sec. Thus many routers today use parallel buses in the form
of crossbar switches (Chapter 13). A router can be built with a small number of chips, such as a link
interface chip, a packet-forwarding chip, memory chips to store lookup state, a crossbar switch, and a
queuing chip with associated DRAM memory for packet buffers.

                                                                                            Detailed models             539




A.3 Switching theory
This section provides some more details about matching algorithms for Clos networks and the dazzling
variety of interconnection networks.


A.3.1 Matching algorithms for Clos networks with k = n
A Clos network can be proved to be rearrangably nonblocking for k = n. The proof uses Hall’s theorem
and the notion of perfect matchings. A bipartite graph is a special graph with two sets of nodes I and
O; edges are only between a node in I and a node in O. A perfect matching is a subset E of edges in
this graph such that every node in I is the endpoint of exactly one edge in E, and every node in O is
also the endpoint of exactly one edge in E. A perfect match marries every man in I to every woman
in O while respecting monogamy. Hall’s theorem states that a necessary and sufficient condition for a
perfect matching to exist is that every subset X of I of size d has at least d edges going to d distinct
nodes in O.
    To apply Hall’s theorem to prove the Clos network is nonblocking, we show that any arrangement
of N inputs that wish to go to N different outputs can be connected via the Clos network. Use the
following iterative algorithm. In each iteration match input switches (set I ) to output switches (set O)
after ignoring the middle switches. Draw an edge between an input switch i and an output switch o if
there is at least one input of i that wishes to send to an output directly reachable through o.
    Using this definition of an edge, here is Claim 1: every subset X of d input switches in I has edges
to at least d output switches in O. Suppose Claim 1 were false. Then the total number of outputs desired
by all inputs in X would be strictly less than nd (because each edge to an output switch can correspond
to at most n outputs). But this cannot be so, because d input switches with n inputs each must require
exactly nd outputs.
    Claim 1 and Hall’s theorem can be used to conclude that there is a perfect matching between input
switches and output switches. Hence the algorithm is to perform this matching after placing back exactly
one middle switch M. This is possible because every middle switch has a link to every input switch and
a link to every output switch. This allows routing one input link in every input switch to one output link
in every switch. It also makes unavailable all the n links from each input switch to the middle switch
M and all output links from M.
    Thus the problem has been reduced from having to route n inputs on each input switch using n
middle switches to having to route n − 1 inputs per input switch using n − 1 middle switches. Thus n
iterations are sufficient to route all inputs to all outputs without causing resource conflicts that lead to
blocking.
    Thus a simple version of this algorithm would take n perfect matches; using the best existing al-
gorithm for perfect matching (Hopcroft and Karp, 1973) takes O(N 2.5 /n1.5 ) time. A faster approach
is via edge coloring; each middle switch is assigned a color, and we color the edges of the demand
multigraph between input switches and output switches so that no two edges coming out of a node have
the same color.3 However, edge coloring can be done directly (without n iterations as before) in around
O(N log N ) time (Cole and Hopcroft, 1982).


3 Intuitively, each set of edges colored with a single color corresponds to one matching and one middle switch, as in our first
algorithm.

540      Detailed models




A.4 The interconnection network Zoo
There is a dazzling variety of (log N )-depth interconnection networks, all based on the same idea of
using bits in the output address to steer to the appropriate portion, starting with the most significant
bit. For example, one can construct the famous Butterfly network in a very similar way to the recursive
construction of the Delta network of Fig. 13.13. In the Delta network all the inputs to the top (N/2)-size
Delta network come from the 0 outputs of the first stage in order. Thus the 0 output of the first first-stage
switch is the first input, the 0 output of the second switch is the second input, etc.
     By contrast, in a Butterfly the second input of the upper N/2 switch is the 0 output of the middle
switch of the first stage (rather than the second switch of the first stage). The 0 output of the second
switch is then the third input, while the 0 output of the switch following the middle switch gets the
fourth input, etc. Thus the two halves are interleaved in the Butterfly but not in the Delta, forming a
classic bowtie or butterfly pattern. However, even with this change, it is still easy to see that the same
principle is operative: outputs with MSB 0 go to the top half, while outputs with MSB 1 go to the
bottom.
     Because the Butterfly can be created from the Delta by renumbering inputs and outputs, the two
networks are said to be isomorphic. Butterflies were extremely popular in parallel computing (Culler et
al., 1999), gaining fame in the BBN Butterfly, though they seem to have lost ground to low-dimensional
meshes (see Section 13.19) in recent machines.
     There is also a small variant of the Butterfly, called the Banyan, that involves pairing the inputs
even in the first stage in a more shuffled fashion (the first input pairs with the middle input, etc.) before
following Butterfly connections to the second stage. Banyans enjoyed a brief resurgence in the network
community when it was noticed that if the outputs for each input are in sorted order, then the Banyan
can route without internal blocking. An important such switch was the Sunshine switch (Giacopelli
et al., 1991). Since sorting can be achieved using Batcher sorting networks (Cormen et al., 1990),
these were called Batcher-Banyan networks. Perhaps because much the same effect can be obtained
by randomization in a Benes or Clos network without the complexity of sorting, this approach has not
found a niche commercially.
     Finally, there is another popular network called the hypercube. The networks described so far use
d-by-d building block switches, where d is a constant such as 2, independent of the size of N . By
contrast, hypercubes use switches with log N links per switch. Each switch is assigned a binary address
from 1 to N and is connected to all other switches that differ from it in exactly one bit. Thus in a very
similar fashion to traversing a Delta or a Butterfly one can travel from an input switch to an output
switch by successively correcting the bits that are different between output and input addresses, in any
order. Unfortunately, the log N link requirement is onerous for large N and can lead to an “impractical
number of links per line card” (Semeria, 2002).

References

A Retrospective on SEDA, 2010. http://matt-welsh.blogspot.com/2010/07/retrospective-on-seda.html.
A reworked TCP zero-copy receive API, 2018. https://lwn.net/Articles/754681/.
Adel’son-Vel’skii, G.M., Landis, E.M., 1962. An algorithm for organization of information. Doklady Akademii
  Nauk 146, 263–266.
Adisheshu, H., 1998. Services for next generation routers. PhD thesis. Washington University Computer Science
  Department.
Aggarwal, G., Motwani, R., Shah, D., Zhu, A., 2003. Switch scheduling via randomized edge coloring. In: Pro-
  ceedings of the IEEE FOCS, pp. 502–512.
Agrawal, R., Imielinski, T., Swami, A., 1993. Mining association rules between sets of items in large databases.
  In: Proceedings of ACM SIGMOD, pp. 207–216.
Aho, A., Corasick, M., 1975. Efficient string matching: an aid to bibliographic search. Communications of the
  ACM 18 (6), 333–343.
Ahuja, R., Magnanti, T., Orlin, J., 1993. Network Flows. Prentice-Hall.
Albertengo, G., Riccardo, S., 1990. Parallel CRC generation. In: IEEE Micro.
Alleyne, B., 2002. Personal communication.
Alon, N., Matias, Y., Szegedy, M., 1999a. The space complexity of approximating the frequency moments. Journal
  of Computer and System Sciences 58 (1), 137–143.
Alon, N., Gibbons, P.B., Matias, Y., Szegedy, M., 1999b. Tracking join and self-join sizes in limited storage. In:
  Proceedings of the ACM SIGACT-SIGMOD-SIGART Symposium on Principles of Database Systems.
AMD, 2007. Software optimization guide for AMD family 10h processors. Available at http://www.amd.com/us-
  en/assets/content_type/white_papers_and_tech_docs/40546.pdf.
Anderson, T., Owicki, S., Saxe, J., Thacker, C., 1993. High speed switch scheduling for local area networks. ACM
  Transactions on Computer Systems 11 (4), 319–352.
Arista Corporation, Flex Route Engine White Paper, 2010. https://www.arista.com/assets/data/pdf/Whitepapers/
  FlexRoute-WP.pdf.
Aron, M., Druschel, P., 1999. Soft timers: efficient microsecond timer support for network processing. In: Proceed-
  ings of the 17th Symposium on Operating System Principles (SOSP).
Asai, H., Ohara, Y., 2015. Poptrie: a compressed trie with population count for fast and scalable software IP routing
  table lookup. In: Proceedings of the 2015 ACM Conference on Special Interest Group on Data Communication.
  Association for Computing Machinery, pp. 57–70.
Awerbuch, B., Patt-Shamir, B., Varghese, G., 1991. Self-stabilization by local checking and correction. In: Pro-
  ceedings of the 32nd Annual Symposium of Foundations of Computer Science (FOCS).
Baboescu, F., Varghese, G., 2001. Scalable packet classification. In: Proceedings of ACM SIGCOMM.
Bailey, M., Gopal, B., Pagels, M., Peterson, L., Sarkar, P., 1994. PATHFINDER: a pattern-based packet clas-
  sifier. In: Proceedings of the First Symposium on Operating Systems Design and Implementation (OSDI),
  pp. 115–123.
Banga, G., Mogul, J., 1998. Scalable kernel performance for Internet servers under realistic loads. In: Proceedings
  of the 1998 USENIX Annual Technical Conference. New Orleans, LA.
Banga, G., Mogul, J., Druschel, P., 1999. A scalable and explicit event delivery mechanism for UNIX. In: USENIX
  Annual Technical Conference, pp. 253–265.
Banks, D., Prudence, M., 1993. A high-performance network architecture for a PA-RISC workstation. IEEE Jour-
  nal on Selected Areas in Communications.
Barile, I., 2004. I/O multiplexing and scalable socket servers. Dr. Dobbs Journal.
                                                                                                               541

542         References



Barroso, L., Marty, M., Patterson, D., Ranganathan, P., 2017. Attack of the killer microseconds. Communications
   of the ACM 60 (4), 48–54. https://doi.org/10.1145/3015146.
Belazzougui, D., Botelho, F.C., Dietzfelbinger, M., 2009. Hash, displace, and compress. In: Fiat, A., Sanders, P.
   (Eds.), Algorithms – ESA 2009. Springer Berlin Heidelberg, pp. 682–693.
Belay, A., Prekas, G., Primorac, M., Klimovic, A., Grossman, S., Kozyrakis, C., Bugnion, E., 2016. The IX Operat-
   ing System: combining low latency, high throughput, and efficiency in a protected dataplane. ACM Transactions
   on Computer Systems 34 (4), 11. https://doi.org/10.1145/2997641.
Bell, E.T., 1986. Men of Mathematics, reissue edition. Touchstone Books.
Benner, A., 1995. Fibre Channel: Gigabit Communications and I/O for Computer Networks. McGraw-Hill.
Bennett, B.T., Kruskal, V.J., 1975. LRU stack processing. IBM Journal of Research and Development 19 (4),
   353–357.
Bennett, J., Zhang, H., 1996a. Hierarchical packet fair queuing algorithms. SIGCOMM Computer Communication
   Review 26 (4), 143–156. https://doi.org/10.1145/248157.248170.
Bennett, J., Zhang, H., 1996b. wf 2 q: worst-case fair weighted fair queuing. In: IEEE INFOCOM’96.
Bennett, J., Zhang, H., 1997. Hierarchical packet fair queuing algorithms. IEEE/ACM Transactions on Network-
   ing 5, 675–689.
Bentley, J.L., 1982. Writing Efficient Programs. Prentice Hall.
Bhagwan, R., Lin, W., 2000. Fast and scalable priority queue architecture for high-speed network switches. In:
   IEEE INFOCOM, pp. 538–547.
Bhattacharyya, S., Diot, C., Jetcheva, J., Taft, N., 2001. Pop-level and access-link traffic dynamics in a tier-1 pop.
   In: SIGCOMM Internet Measurement Workshop.
Birell, A., et al., 1982. Grapevine: an exercise in distributed computing. Communications of the ACM 25 (4),
   202–208.
Blackwell, T., 1996. Speeding up protocols for small messages. In: Proceedings of ACM SIGCOMM.
Blake, S., et al., 1998. An architecture for differentiated services. https://datatracker.ietf.org/doc/html/rfc2475.
Bloom, B.H., 1970. Space/time trade-offs in hash coding with allowable errors. Communications of the ACM 13
   (7), 422–426. https://doi.org/10.1145/362686.362692.
Boecking, S., Seidel, V., Vindeby, P., 1995. Channels—a run-time system for multimedia protocols. In: ICCCN.
Boggs, D.R., Mogul, J.C., Kent, C.A., 1988. Measured capacity of an Ethernet: myths and reality. Proceedings
   ACM SIGCOMM 18, 222–234.
Bosshart, P.W., Gibb, G., Kim, H.-S., Varghese, G., McKeown, N., Izzard, M., Mujica, F.A., Horowitz, M., 2013.
   Forwarding metamorphosis: fast programmable match-action processing in hardware for SDN. In: Proceedings
   of the ACM SIGCOMM 2013 Conference on SIGCOMM.
Boyer, R.S., Moore, J.S., 1977. A fast string searching algorithm. Communications of the ACM 20 (10), 762–772.
Boyle, J., 1997. Internet draft: RSVP extensions for CIDR aggregated data flows. In: Internic.
Brakmo, L., Malley, S.O., Peterson, L., 1994. TCP Vegas: New techniques for congestion detection and avoidance.
   In: Proceedings of ACM SIGCOMM.
Braun, H.W., 1998. Characterizing traffic workload. www.caida.org.
Broder, A., 1998. On the resemblance and containment of documents. In: Sequences’91.
Broder, A., Mitzenmacher, M., 2001. Using multiple hash functions to improve IP lookups. In: Proceedings IEEE
   Infocom, pp. 1454–1463.
Brustoloni, J., 1999. Interoperation of copy avoidance in network and file I/O. In: Proceedings of IEEE Infocom.
   New York.
Brustoloni, J., Steenkiste, P., 1996. Effects of buffering semantics on I/O performance. In: Proceedings of the 2nd
   USENIX Symposium on Operating Systems Design and Implementation.
Build Ultra High-Performance Storage Applications with the Storage Performance Development Kit, 2022. https://
   spdk.io/.
Buonadonna, P., Geweke, A., Culler, D., 2002. An implementation and analysis of the virtual interface architecture.
   In: SC98: High Performance Networking and Computing Conference.

                                                                                      References          543



Bux, W., Grillo, D., 1985. Flow control in local-area networks of interconnected token rings. IEEE Transactions
  on Communications COM-33 (10), 1058–1066.
Cai, Q., Chaudhary, S., Vuppalapati, M., Hwang, J., Agarwal, R., 2021. Understanding host network stack over-
  heads. In: Proceedings of the 2021 ACM SIGCOMM 2021 Conference, SIGCOMM ’21. Association for
  Computing Machinery, pp. 65–77.
Cao, J., Xia, R., Yang, P., Guo, C., Lu, G., Yuan, L., Zheng, Y., Wu, H., Xiong, Y., Maltz, D., 2013. Per-packet
  load-balanced, low-latency routing for clos-based data center networks. In: Proceedings of the Ninth ACM
  Conference on Emerging Networking Experiments and Technologies, CoNEXT’13. Association for Computing
  Machinery, New York, NY, pp. 49–60.
Cardwell, N., Cheng, Y, Gunn, S.C., Yeganeh, S.H., Van, J., 2017. BBR: congestion-based congestion control.
  Communications of the ACM 60 (2), 58–66. https://doi.org/10.1145/3009824.
Carlton, A., 1996. An explanation of the SPECweb96 benchmark. Standard performance evaluation corporation
  white paper. http://www.specbench.org/.
Casella, G., Berger, R., 2001. Statistical Inference, 2 edition. Duxbury Thomson Learning.
Chandranmenon, G., Varghese, G., 1996. Trading packet headers for packet processing. ACM /IEEE Transactions
  Networking 17 (1).
Chandranmenon, G., Varghese, G., 1998. Reconsidering fragmentation and reassembly. In: Symposium on Princi-
  ples of Distributed Computing, pp. 21–29.
Chandranmenon, G., Varghese, G., 2001. Reducing web latencies using precomputed hints. In: Proceedings of
  IEEE INFOCOM.
Chandy, K.M., Lamport, L., 1985. Distributed snapshots: determining global states of distributed systems. ACM
  Transactions on Computer Systems 3 (1), 63–75.
Chaney, T., Fingerhut, A., Flucke, M., Turner, J., 1997. Design of a gigabit ATM switch. In: Proceedings of IEEE
  INFOCOM, pp. 2–11.
Chang, C.-S., Lee, D.-S., Jou, Y.-S., 2002a. Load balanced Birkhoff–von Neumann switches, part I: one-stage
  buffering. Computer Communications 25 (6), 611–622.
Chang, C.-S., Lee, D.-S., Lien, C.-M., 2002b. Load balanced Birkhoff–von Neumann switches, part II: multi-stage
  buffering. Computer Communications 25 (6), 623–634.
Chankhunthod, A., Danzig, P., et al., 1996. A hierarchical Internet object cache. In: USENIX Annual Technical
  Conference, pp. 153–164.
Chao, H.J., Guo, X., 2001. Quality of Service Control in High-Speed Networks. Wiley.
Charikar, M., Chen, K., Farach-Colton, M., 2002. Finding frequent items in data streams. In: ICALP’02: Pro-
  ceedings of the 29th International Colloquium on Automata, Languages and Programming. Springer-Verlag,
  London, pp. 693–703.
Chazelle, B., 1990a. Lower bounds for orthogonal range searching, I: the reporting case. Journal of the ACM 37.
Chazelle, B., 1990b. Lower bounds for orthogonal range searching, II: the arithmetic model. Journal of the
  ACM 37.
Checconi, F., Rizzo, L., Valente, P., 2013. IEEE/ACM transactions on networking. QFQ: Efficient Packet Schedul-
  ing With Tight Guarantees 21 (3), 802–816. https://doi.org/10.1109/TNET.2012.2215881.
Chelf, B., 2001. Dynamic memory management. Linux magazine readable at http://www.linux-mag.com/2001-06/
  compile_03.html.
Chesson, G., 1989. XTP/PE design considerations. In: IFIP Workshop on Protocols for High Speed Networks.
Cheswick, W., Bellovin, S., 1995. Firewalls and Internet Security. Addison-Wesley.
Chiueh, T., Pradhan, P., 1999. High performance IP routing table lookup using CPU caching. In: Proceedings IEEE
  INFOCOM, pp. 1421–1428.
Choudhury, A., Hahne, E., 1998. Dynamic queue length thresholds for shared-memory packet switches.
  IEEE/ACM Transactions on Networking 6 (2), 130–140.
Chuang, S.-T., Goel, A., McKeown, N., Prabhakar, B., 1999. Matching output queueing with a combined in-
  put/output-queued switch. IEEE Journal on Selected Areas in Communications 17 (6), 1030–1039.

544        References



Chung, F., Graham, R., Varghese, G., 2004. Parallelism versus memory allocation in pipelined router forwarding
  engines. In: Proceedings of the Sixteenth Annual ACM Symposium on Parallelism in Algorithms and Architec-
  tures. Association for Computing Machinery, pp. 103–111.
Cisco express forwarding commands, 2001a. http://www.cisco.com.
Cisco netflow, 2001b. http://www.cisco.com/warp/public/732/Tech/netflow.
Cisco Systems, 2001c. Cisco 12000 series Internet routers. http://www.cisco.com/warp/public/cc/pd/rt/12000/tech/
  index.shtml.
Cisco Systems, Inc., 2017. Intelligent buffer management on Cisco Nexus 9000 Series switches white paper.
  Technical report. Available at https://www.cisco.com/c/en/us/products/collateral/switches/nexus-9000-series-
  switches/white-paper-c11-738488.html. (Accessed November 2020).
Clark, D.D., 1985. Structuring of systems using upcalls. In: Proceedings of the 10th ACM Symposium on Operat-
  ing Systems Principles (SOSP), pp. 171–180.
Clark, D.D., 1988. The design philosophy of the DARPA Internet protocols. In: Proceedings ACM SIGCOMM,
  pp. 106–114.
Clark, D., Tennenhouse, D., 1990. Architectural considerations for a new generation of protocols. In: Proceedings
  of ACM SIGCOMM.
Clark, D.D., Jacobson, V., Romkey, J., Salwen, H., 1989. An analysis of TCP processing overhead. IEEE Commu-
  nications 27 (6), 23–29.
Clark, D., Wroclawski, J., Sollins, K., Braden, R., 2002. Tussle in cyberspace: defining tomorrow’s Internet. In:
  Proceedings ACM SIGCOMM.
Cobb, J., Gouda, M., El Nahas, A., 1996. Time-shift scheduling: fair scheduling of flows in high speed networks.
  In: Proceedings of ICNP.
Cohen, E., 2016. Minhash sketches: a brief survey. http://www.cohenwang.com/edith/Surveys/minhash.pdf. (Ac-
  cessed 27 January 2021).
Coit, C., Staniford, S., McAlerney, J., 2001. Towards faster pattern matching for intrusion detection or exceeding
  the speed of snort. In: Proceedings of the 2nd DARPA Information Survivability Conference and Exposition
  (DISCEX II).
Cole, R., Hopcroft, J., 1982. On edge coloring bipartite graphs. SIAM Journal of Computation 11, 540–546.
Commentz-Walter, B., 1979. A string matching algorithm fast on the average. In: Proceedings 6th International
  Colloquium on Automata, Languages and Programming, vol. 71. Springer.
Compaq, Intel, and Microsoft Corporations, 1997. Virtual interface architecture specification. http://www.viaarch.
  org.
Corbet, J., 2015. Reinventing the timer wheel. https://lwn.net/Articles/646950/.
Components of Linux Traffic Control, 2022. https://tldp.org/HOWTO/Traffic-Control-HOWTO/components.html.
Cormen, T., Leiserson, C., Rivest, R., 1990. Introduction to Algorithms. MIT Press/McGraw-Hill.
Cormen, T.H., Leiserson, C.E., Rivest, R.L., Stein, C., 2009. Introduction to Algorithms, 3rd edition. MIT Press.
Cormode, Graham, Muthukrishnan, S., 2005. An improved data stream summary: the count-min sketch and its
  applications. Journal of Algorithms 55 (1), 58–75.
Costello, A., Varghese, G., 1998. Redesigning the BSD Callout and timeout facilities. In: Software Practice and
  Experience.
Cox, A., 1996. Kernel Korner: network buffers and memory management. Linux Journal. www.linuxjournal.com.
Crovella, M., Carter, R., 1995. Dynamic server selection in the Internet. In: Proceedings of HPCS’95.
Culler, D., Singh, J., Gupta, A., 1999. Parallel Computer Architecture: A Hardware/Software Approach. Morgan
  Kaufman.
Dai, J., Prabhakar, B., 2000. The throughput of data switches with and without speedup. In: Proceedings of the
  IEEE INFOCOM. Tel Aviv, Israel, pp. 556–564.
Dally, W., 2002. Scalable switching fabrics for Internet routers. In: Avici Networks White Paper. http://www.avici.
  com/technology/whitepapers.

                                                                                           References            545



Dally, W., Chao, L., et al., 1987. Architecture of a message-driven processor. In: Proceedings of the International
  Symposium on Computer Architecture (ISCA).
Davison, G., 1989. Calendar p’s and q’s. Communications of the ACM 32 (10), 1241–1242.
Decasper, D., Dittia, Z., Parulkar, G., Plattner, B., 1998. Router plugins: a software architecture for next generation
  routers. In: Proceedings ACM SIGCOMM.
Degermark, M., Brodnik, A., Carlsson, S., Pink, S., 1997. Small forwarding tables for fast routing lookups. In:
  Proceedings ACM SIGCOMM, pp. 3–14.
Demers, A., Keshav, S., Shenker, S., 1989. Analysis and simulation of a fair queueing algorithm. ACM SIGCOMM
  Computer Communication Review 19 (4), 1–12. Proceedings of the Sigcomm’89 Symposium on Communica-
  tions Architectures and Protocols.
Denning, D., 1987. An intrusion-detection model. IEEE Transactions on Software Engineering 13 (2), 222–232.
Dharmapurikar, S., Krishnamurthy, P., Taylor, D.E., 2003. Longest prefix matching using bloom filters. In: Pro-
  ceedings of the 2003 Conference on Applications, Technologies, Architectures, and Protocols for Computer
  Communications. Association for Computing Machinery, pp. 201–212.
Dietzfelbinger, M., Karlin, A., et al., 1988. Dynamic perfect hashing: upper and lower bounds. In: 29th IEEE
  Symposium on Foundations of Computer Science (FOCS).
Ding, W., Xu, J., Dai, J.G., Song, Y., Bill, L., 2014. Sprinklers: A randomized variable-size striping approach
  to reordering-free load-balanced switching. In: ACM CoNext, the 10th International Conference on Emerging
  Networking EXperiments and Technologies. ACM.
Dittia, Z.D., Parulkar, G.M., Cox Jr., J.R., 1997. The APIC approach to high performance network interface design:
  protected DMA and other techniques. In: Proceedings of IEEE INFOCOM.
Draves, R., King, C., Venkatachary, S., Zill, B., 1999. Constructing optimal IP routing tables. In: Proceedings IEEE
  INFOCOM.
Druschel, P., Banga, G., 1996. Lazy receiver processing: a network subsystem architecture for server systems. In:
  Proceedings of the UNIX 2nd OSDI Conference.
Druschel, P., Peterson, L., 1993. Fbufs: A high-bandwidth cross-domain transfer facility. In: Proceedings of the
  Fourteenth ACM Symposium on Operating System Principles, pp. 189–202.
Druschel, P., Davie, B., Peterson, L., 1994. Experiences with a high-speed network adapter: a software perspective.
  In: Proceedings ACM SIGCOMM.
Duan, R., Su, H., 2012. A scaling algorithm for maximum weight matching in bipartite graphs. In: Proceedings of
  the ACM-SIAM SODA, pp. 1413–1424.
Duffield, N., Grossglauser, M., 2000. Trajectory sampling for direct traffic observation. In: Proceedings ACM
  SIGCOMM, pp. 271–282.
Duffield, N., Lund, C., Thorup, M., 2001. Charging from sampled network usage. In: SIGCOMM Internet Mea-
  surement Workshop.
Duffield, N., Lund, C., Thorup, M., 2002. Properties and prediction of flow statistics from sampled packet streams.
  In: Proceedings of ACM SIGCOMM Internet Measurement Workshop.
Duffield, N., Lund, C., Thorup, M., 2003. Estimating flow distributions from sampled flow statistics. In: Proceed-
  ings of ACM SIGCOMM.
DXR: Beyond two billion IPv4 routing lookups per second in software, 2022. http://www.nxlab.fer.hr/dxr/.
Eatherton, W., 1995. Hardware-based Internet protocol prefix lookups. MS thesis. Washington University Electrical
  Engineering Department.
Eatherton, W., Dittia, Z., Varghese, G., 2004. Tree bitmap: hardware software IP lookups with incremental updates.
  ACM Computer Communications Review 34 (2), 97–123.
Elmasri, R., Navathe, S., 2010. Fundamentals of Database Systems, 6th edition. Addison-Wesley Publishing Com-
  pany.
Engler, D., 1996. VCODE: a retargetable, extensible, very fast dynamic code generation system. In: SIGPLAN
  Conference on Programming Language Design and Implementation, pp. 160–170.

546        References



Engler, D., Kaashoek, M.F., 1996. DPF: fast, flexible message demultiplexing using dynamic code generation. In:
   Proceedings ACM SIGCOMM, pp. 53–59.
Engler, D., Kaashoek, F., O’Toole, J., 1995. Exokernel: an operating system architecture for application-level
   resource management. In: Symposium on Operating Systems Principles, pp. 251–266.
epoll(7) – Linux manual page, 2022. https://man7.org/linux/man-pages/man7/epoll.7.html.
Estan, C., Varghese, G., 2002. New directions in traffic measurement and accounting. In: Proceedings of ACM
   SIGCOMM.
Estan, C., Varghese, G., Fisk, M., 2002. Counting the number of active flows on a high speed link. Technical Report
   0705. CSE Department, UCSD.
Estan, C., Savage, S., Varghese, G., 2003. Automatically inferring patterns of resource consumption in network
   traffic. In: Proceedings ACM SIGCOMM.
Fall, K., Pasquale, J., 1993. Exploiting in-kernel data paths to improve I/O throughput and CPU availability. In:
   USENIX Winter, pp. 327–334.
Fang, W., Peterson, L., 1999. Inter-AS traffic patterns and their implications. In: Proceedings of IEEE GLOBE-
   COM.
Feigenbaum, J., Kannan, S., Strauss, M.J., Viswanathan, M., 2003. An approximate l1-difference algorithm for
   massive data streams. SIAM Journal on Computing 32 (1), 131–151.
Feldmann, A., Greenberg, A., et al., 2000. Deriving traffic demands for operational IP networks: methodology and
   experience. In: Proceedings ACM SIGCOMM, pp. 257–270.
Firoozshahian, A., Manshadi, V., Goel, A., Prabhakar, B., 2007. Efficient, fully local algorithms for CIOQ
   switches. In: IEEE INFOCOM 2007—26th IEEE International Conference on Computer Communications,
   pp. 2491–2495.
Fisk, M., Varghese, George, 2001. Fast content-based packet handling for intrusion detection. UCSD Technical
   Report CS2001-0670.
Flajolet, P., Martin, G., 1985. Probabilistic counting algorithms for data base applications. Journal of Computer
   and System Sciences 31 (2), 182–209.
Floyd, S., Jacobson, V., 1993. Random early detection gateways for congestion avoidance. In: ACM/IEEE Trans-
   actions Networking.
Floyd, S., Jacobson, V., 1995. Link-sharing and resource management models for packet networks. In: ACM/IEEE
   Transactions Networking.
Floyd, S., Jacobson, V., McCanne, S., Liu, C., Zhang, L., 1995. A reliable multicast framework for light-weight
   sessions and application level framing. In: Proceedings ACM SIGCOMM.
Floyd, S., Mahdavi, J., Mathis, M., Podolsky, M., Romanow, A., 1999. An extension to the selective acknowledge-
   ment (SACK) option for TCP.
Fromm, R., Perissakis, S., Cardwell, N., et al., 1997. The energy efficiency of IRAM architectures. In: International
   Symposium on Computer Architecture (ISCA 97).
Gale, D., Shapley, L.S., 1962. College admissions and the stability of marriage. The American Mathematical
   Monthly 69 (1), 9–15.
Gammo, L., Brecht, T., Shukla, A., Pariag, D., 2004. Comparing and evaluating epoll, select, and poll event mech-
   anisms. In: Proceedings of the 6th Annual Ottawa Linux Symposium.
Ghorbani, S., Yang, Z., Brighten Godfrey, P., Ganjali, Y., Drill, A.F., 2017. Micro load balancing for low-latency
   data center networks. In: Proceedings of the Conference of the ACM Special Interest Group on Data Commu-
   nication, SIGCOMM’17. Association for Computing Machinery, New York, NY, pp. 225–238.
Giaccone, P., Prabhakar, B., Shah, D., 2003. Randomized scheduling algorithms for high-aggregate bandwidth
   switches. IEEE Journal on Selected Areas in Communications 21 (4), 546–559.
Giaccone, P., Leonardi, E., Prabhakar, B., Shah, D., 2004. Delay bounds for combined input-output switches with
   low speedup. Performance Evaluation 55 (1), 113–128. https://doi.org/10.1016/S0166-5316(03)00103-2.
Gleixner, T., Niehaus, D., 2006. Linux HR timers and beyond: transforming the Linux time subsystems. https://
   www.kernel.org/doc/ols/2006/ols2006v1-pages-333-346.pdf.

                                                                                           References            547



Giacopelli, J., et al., 1991. Sunshine: a high performance self-routing packet switch architecture. IEEE Journal on
  Selected Areas in Communication 9 (8).
Global Intrusion Detection and Prevention Systems Market to Record an Impressive Growth of USD 9.04 Billion
  by 2028: Fior Markets. https://www.globenewswire.com/news-release/2022/05/10/2440086/0/en/Global-
  Intrusion-Detection-and-Prevention-Systems-Market-to-Record-an-Impressive-Growth-of-USD-9-04-Billion-
  by-2028-Fior-Markets.html.
Gokhale, A., Schmidt, D., 1998. Principles for optimizing CORBA Internet inter-ORB protocol performance. In:
  Hawaiian International Conference on System Sciences.
Gong, L., Tune, P., Liu, L., Yang, S., Xu, J., 2017. Queue-proportional sampling: a better approach to crossbar
  scheduling for input-queued switches. Proceedings of the ACM SIGMETRICS 1 (1), 3:1–3:33. https://doi.org/
  10.1145/3084440.
Gonnet, Gaston H., 1981. Expected length of the longest probe sequence in hash code searching. Journal of the
  ACM 28 (2), 289–304.
Google, IPv6 statistics. https://www.google.com/intl/en/ipv6/statistics.html.
Griffin, T., Wilfong, G., 2002. On the correctness of IBGP configuration. In: Proceedings ACM SIGCOMM,
  pp. 17–30.
Guo, C., Wu, H., Deng, Z., Soni, G., Ye, J., Padhye, J., Lipshteyn, M., 2016. RDMA over commodity ethernet at
  scale. In: Proceedings of the 2016 ACM SIGCOMM Conference, SIGCOMM ’16. Association for Computing
  Machinery, pp. 202–215.
Gupta, P., McKeown, N., 1999a. Packet classification on multiple fields. In: Proceedings ACM SIGCOMM,
  pp. 147–160.
Gupta, P., McKeown, N., 1999b. Designing and implementing a fast crossbar scheduler. IEEE Micro.
Gupta, P., McKeown, N., 2001. Algorithms for packet classification. IEEE Network 15 (2).
Gupta, P., Lin, S., McKeown, N., 1998. Routing lookups in hardware at memory access speeds. In: IEEE INFO-
  COM.
Han, S., Marshall, S., Chun, B.-G., Ratnasamy, S., 2012. MegaPipe: a new programming interface for scalable net-
  work I/O. In: Proceedings of the 10th USENIX Conference on Operating Systems Design and Implementation,
  OSDI’12. USENIX Association, pp. 135–148.
Hennessey, J., Patterson, D., 1996. Computer Architecture: A Quantitative Approach, 2nd ednition. Morgan Kauf-
  mann.
Hohn, N., Veitch, D., 2003. Inverting sampled traffic. In: Proceedings of ACM SIGCOMM Internet Measurement
  Conference.
Hopcroft, J., Karp, R., 1973. An n5/2 algorithm for maximum matchings in bipartite graphs. SIAM Journal on
  Computation 2, 225–231.
Horowitz, E., Sahni, S., 1978. Fundamentals of Computer Algorithms. Computer Science Press.
Hua, N., Zhao, H., Lin, B., Xu, J., 2008a. Rank-indexed hashing: a compact construction of bloom filters and
  variants. In: Proceedings of IEEE International Conference on Network Protocols (ICNP).
Hua, N., Lin, B., Xu, J., Zhao, H., 2008b. Brick: a novel exact active statistics counter architecture. In: Proceedings
  of ACM/IEEE Symposium on Architectures for Networking and Communications Systems (ANCS). http://
  doi.acm.org/10.1145/1477942.1477956.
Huggahalli, R., Iyer, R., Tetrick, S., 2005. Direct cache access for high bandwidth network I/O. In: Proceedings
  of the 32nd Annual International Symposium on Computer Architecture, ISCA ’05. IEEE Computer Society,
  pp. 50–59.
Hutchinson, N.C., Peterson, L.L., 1991. The x-Kernel: an architecture for implementing network protocols. IEEE
  Transactions on Software Engineering 17 (1), 64–76.
IEEE, 1997. Media access control (mac) bridging of ethernet v2.0 in local area networks. http://standards.ieee.org/
  reading/ieee/std/lanman/802.1H-1997.pdf.
IETF MPLS Charter, 1997. Multiprotocol label switching. http://www.ietf.org/html-charters/mpls-charter.html.

548         References



Indyk, P., Motwani, R., et al., 1997. Locality-preserving hashing in multidimensional spaces. In: Proceedings of
   the 29th ACM Symposium on Theory of Computing, pp. 618–625.
Infiniband Specification, 2000. Infiniband Architecture Specification.
Infiniband Trade Association, 2001. Infiniband architecture. http://www.infinibandta.org/home.
Information about the TCP Chimney Offload, Receive Side Scaling, and Network Direct Memory Access
   features in Windows Server 2008. https://learn.microsoft.com/en-us/troubleshoot/windows-server/networking/
   information-about-tcp-chimney-offload-rss-netdma-feature.
Intel Corporation, Intel Aurora 710 Product datasheet, 2022. https://netbergtw.com/products/aurora-710/.
Intel 64 and IA-32r, 2007. Architectures software developer’s manual, vol. 2B. Available at ftp://download.intel.
   com/technology/architecture/new-instructions-paper.pdf.
Israel, A., Itai, A., 1986. A fast and simple randomized parallel algorithm for maximal matching. Information
   Processing Letters 22 (2), 77–80.
Iyer, S., Zhang, R., McKeown, N., 2002. Routers with a single stage of buffering. SIGCOMM Computer Commu-
   nication Review 32 (4), 251–264. https://doi.org/10.1145/964725.633050.
Jacobson, V., 1988. Congestion avoidance and control. In: Proceedings ACM SIGCOMM.
Jacobson, G., 1989. Space-efficient static trees and graphs. In: 30th FOCS, pp. 549–554.
Jacobson, V., 1993. TCP in 30 instructions. In: Message Sent to Comp.Protocols. TCP Newsgroup.
Jaramillo, J.J., Milan, F., Srikant, R., 2008. Padded frames: a novel algorithm for stable scheduling in load-balanced
   switches. Networking, IEEE/ACM Transactions on Networking 16 (5), 1212–1225.
Kamber, M., Han, J., 2000. Data Management Systems: Data Mining: Concepts and Techniques. Elsevier.
Kanakia, H., 1999. Datapath Switch. In: ATT Bell Labs Internal Memorandum.
Karol, M., Hluchyj, M., Morgan, S., 1987. Input versus output queuing on a space division switch. IEEE Transac-
   tions on Communications, 1347–1356.
Kay, J., Pasquale, J., 1993. The importance of non-data touching processing overheads in TCP/IP. In: Proceedings
   ACM SIGCOMM.
Kent, C.A., Mogul, J.C., 1987. Fragmentation considered harmful. In: Proceedings ACM SIGCOMM.
Keshav, S., 1991. On the efficient implementation of fair queueing. Internetworking: Research and Experience 2,
   157–173.
Keshav, S., 1997. Computer Networks: An Engineering Approach. Addison-Wesley.
Keshav, S., Demers, A., Shenker, S., 1990. Analysis and simulation of a fair queueing algorithm. In: Internetwork-
   ing: Research and Experience, pp. 3–26.
Keslassy, I., 2004. The load-balanced router. PhD thesis. Stanford University.
Knuth, D., 1973. Fundamental Algorithms vol 3: Sorting and Searching. Addison-Wesley.
Kogan, K., Nikolenko, S., Rottenstreich, O., Culhane, W., Eugster, P., 2014. SAX-PAC (scalable and EXpressive
   PAcket classification). In: Proceedings of the 2014 ACM Conference on SIGCOMM. SIGCOMM ’14. Associ-
   ation for Computing Machinery, pp. 15–26.
Kohler, E., Morris, R., et al., 2000. The click modular router. ACM Transactions on Computer Systems.
Krishnamurthy, B., Sen, S., Zhang, Y., Chen, Y., 2003. Sketch-based change detection: methods, evaluation, and
   applications. In: Proceedings of ACM SIGCOMM IMC.
Kronenberg, N., Levy, H., Strecker, W., 1986. Vaxclusters: a closely-coupled distributed system. ACM Transac-
   tions on Computer Systems 4 (2).
Kumar, A., Xu, J., Wang, J., Spatschek, O., Li, L., 2004a. Space-code bloom filter for efficient per-flow traffic
   measurement. In: Proceedings of IEEE INFOCOM.
Kumar, A., Sung, M., Xu, J., Wang, J., 2004b. Data streaming algorithms for efficient and accurate estimation of
   flow size distribution. In: Proceedings of the ACM SIGMETRICS.
Kung, H.T., Chapman, A., Blackwell, T., 1994. The FCVC credit based flow control protocol. In: Proceedings of
   the ACM SIGCOMM.
Kurzweil, R., 2001. What’s creativity and who’s creative. https://www.closertotruth.com/roundtables/whats-
   creativity-and-whos-creative.

                                                                                          References            549



Labovitz, C., Malan, G., Jahanian, F., 1997. Internet routing instability. In: Proceedings of the ACM SIGCOMM.
Lai, K., Baker, M., 1996. A performance comparison of UNIX operating systems on the Pentium. In: Proceedings
   of the 1996 USENIX Conference. San Diego.
Lakshman, T.V., Stidialis, D., 1998. High speed policy-based packet forwarding using efficient multi-dimensional
   range matching. In: Proceedings of the ACM SIGCOMM.
Lampson, B., 1989. Hints for computer system design. In: Proceedings of the 9th ACM Symposium on Operating
   Systems Principles (SOSP) 1989.
Lampson, B., Srinivasan, V., Varghese, G., 1998. IP lookups using multi-way and multicolumn search. In: Pro-
   ceedings of IEEE INFOCOM.
Leslie, G. Valiant, 1982. A scheme for fast parallel communication. SIAM Journal on Computing 11 (2), 350–361.
Leung, J.Y.-T., 1989. A new algorithm for scheduling periodic, real-time tasks. Algorithmica 4 (1), 209–219.
Li, P., Church, K.W., 2007. A sketch algorithm for estimating two-way and multi-way associations. Computational
   Linguistics, p. 2007.
Li, W., Li, X., 2013. HybridCuts: a scheme combining decomposition and cutting for packet classification. In:
   2013 IEEE 21st Annual Symposium on High-Performance Interconnects, pp. 41–48.
Li, J., Sung, M., Xu, J., Li, L., May 2004. Large-scale IP traceback in high-speed internet: practical techniques and
   theoretical foundation. In Proceedings of IEEE Symposium on Security and Privacy.
Li, W., Yang, T., Rottenstreich, O., Li, X., Xie, G., Li, H., Vamanan, B., Li, D., Lin, H., 2020. Tuple space assisted
   packet classification with high performance on both search and update. IEEE Journal on Selected Areas in
   Communications 38 (7), 1555–1569.
Liang, E., Zhu, H., Jin, X., Stoica, I., 2019. Neural packet classification. In: Proceedings of the ACM Special
   Interest Group on Data Communication. SIGCOMM ’19. Association for Computing Machinery, pp. 256–269.
Limasset, A., Rizk, G., Chikhi, R., Peterlongo, P., 2017. Fast and scalable minimal perfect hashing for massive key
   sets. In: 16th International Symposium on Experimental Algorithms, vol. 11, pp. 1–11. hal-01566246.
Lin, B., Keslassy, I., 2010. The concurrent matching switch architecture. IEEE/ACM Transactions on Network-
   ing 18 (4), 1330–1343.
Lin, B., Xu, J. (Jim), Hua, N., Wang, H., Zhao, H. (Chuck), 2009. A randomized interleaved DRAM architecture
   for the maintenance of exact statistics counters. ACM SIGMETRICS Performance Evaluation Review 37 (2),
   53–54.
Loukissas, A., Al-Fares, M., Vahdat, A., 2008. A scalable, commodity data center network architecture. In: Pro-
   ceedings of the ACM SIGCOMM 2008 Conference on Data Communication, SIGCOMM’08. Association for
   Computing Machinery, New York, NY, pp. 63–74.
Lu, Y., Wang, M., Prabhakar, B., Elephanttrap, F.B., 2007. A low cost device for identifying large flows. In: 15th
   IEEE Symposium on High-Performance Interconnects, pp. 99–105.
Ma, Y., Banerjee, S., 2012. A smart pre-classifier to reduce power consumption of TCAMs for multi-dimensional
   packet classification. In: Proceedings of the ACM SIGCOMM 2012 Conference on Applications, Technolo-
   gies, Architectures, and Protocols for Computer Communication. SIGCOMM ’12. Association for Computing
   Machinery, pp. 335–346.
Maeda, C., Bershad, B., 1993. Protocol service decomposition for high-performance networking. In: Proceedings
   of the 14th ACM Symposium on Operating Systems Principles (SOSP).
Mahalingam, M., et al., 2020. Virtual eXtensible local area network (VXLAN): a framework for overlaying virtu-
   alized layer 2 networks over layer 3 networks. https://datatracker.ietf.org/doc/html/rfc7348.
Malan, G., Jahanian, F., 1998. An extensible probe architecture for network protocol measurement. In: Proceedings
   of the ACM SIGCOMM.
Maltzahn, C., Richardson, K., Grunwald, D., 1997. Performance issues of enterprise level web proxies. In: Mea-
   surement and Modeling of Computer Systems, pp. 13–23.
Manku, G., Motwani, R., 2002. Approximate frequency counts over data streams. In: Proceedings of the 28th
   International Conference on Very Large Data Bases (VLDB).

550         References



Mao, Z., Govindan, R., Varghese, G., Katz, R., 2002. Route flap damping can exacerbate BGP convergence. In:
  Proceedings of the ACM SIGCOMM, pp. 221–234.
Marty, M., de Kruijf, M., Adriaens, J., Alfeld, C., Bauer, S., Contavalli, C., Dalton, M., Dukkipati, N., Evans,
  W.C., Gribble, S., Kidd, N., Kononov, R., Kumar, G., Mauer, C., Musick, E., Olson, L., Rubow, E., Ryan,
  M., Springborn, K., Turner, P., Valancius, V., Wang, X., Vahdat, A., 2019. Snap: a microkernel approach to
  host networking. In: Proceedings of the 27th ACM Symposium on Operating Systems Principles, SOSP ’19.
  Association for Computing Machinery, pp. 399–413.
Max Vision, 2001. Advanced reference archive of current heuristics for network intrusion detection systems (arach-
  NIDS). http://www.whitehats.com/ids/.
McCanne, S., 1992. A distributed whiteboard for network conferencing. In: UC Berkeley CS 268 Computer Net-
  works Term Project.
McCanne, S., Jacobson, V., 1993. The BSD packet filter: a new architecture for user-level packet capture. In:
  USENIX Winter Conference, pp. 259–270.
McKenney, P., 1991. Stochastic fairness queueing. Internetworking: Research and Experience 2, 113–131.
McKeown, N., 1997. A fast switched backplane for a gigabit switched router. Business Communications Review 27
  (12).
McKeown, N., 1999. The iSLIP scheduling algorithm for input-queued switches. IEEE/ACM Transactions on
  Networking 7 (2), 188–201.
McKeown, N., et al., 1997. The tiny tera: a packet switch core. IEEE Micro.
McKeown, N., Mekkittikul, A., Anantharam, V., Walrand, J., 1999. Achieving 100% throughput in an input-queued
  switch. IEEE Transactions on Communications 47 (8), 1260–1267.
McQuillan, J., 1997. Layer 4 switching. In: Data Communications.
Mead, C., Conway, L., 1980. Introduction to VLSI Systems. Addison Wesley.
Medina, A., Taft, N., et al., 2002. Traffic matrix estimation: existing techniques and new directions. In: Proceedings
  of the ACM SIGCOMM.
Meng, J., Gong, L., Xu, J., 2020. Sliding-window GPS (SW-GPS): a perfect parallel iterative switching algorithm
  for input-queued switches. In: Proceedings of IFIP PERFORMANCE. https://dl.acm.org/doi/10.1145/3453953.
  3453969.
Meiners, C.R., Liu, A.X., Torng, E., 2008. Algorithmic approaches to redesigning TCAM-based systems. https://
  www.cse.msu.edu/~alexliu/publications/pipeline/sigmetricabstract.pdf.
Misra, J., Gries, D., 1982. Finding repeated elements. Technical report.
Mittal, R., Agarwal, R., Ratnasamy, S., Shenker, S., 2015. Universal packet scheduling. In: Proceedings of the 14th
  ACM Workshop on Hot Topics in Networks. Association for Computing Machinery.
Mittal, R., Shpiner, A., Panda, A., Zahavi, E., Krishnamurthy, A., Ratnasamy, S., Shenker, S., 2018. Revisiting
  network support for RDMA. In: Proceedings of the 2018 Conference of the ACM Special Interest Group on
  Data Communication, SIGCOMM ’18. Association for Computing Machinery, pp. 313–326.
Mitzenmacher, M.D., 1996. The power of two choices in randomized load balancing. PhD thesis. University of
  California at Berkeley.
Mogul, J., 1995. The case for persistent-connection http. In: Proceedings of the ACM SIGCOMM.
Mogul, J., Ramakrishnan, K.K., 1997. Eliminating receive livelock in an interrupt-driven kernel. In: ACM Trans-
  actions on Computer Systems, pp. 303–313.
Mogul, J., Rashid, R., Accetta, M., 1987. The packet filter: an efficient mechanism for user-level network code. In:
  Proceedings of the 11th ACM Symposium on Operating Systems Principles (SOSP), vol. 21, pp. 39–51.
Molinero-Fernandez, P., McKeown, N., 2002. TCP switching exposing circuits to IP. IEEE Microwave Maga-
  zine 22 (1), 82–89.
Montazeri, Behnam, Li, Yilong, Alizadeh, Mohammad, Ousterhout, John, Homa, 2018. A Receiver-Driven Low-
  Latency Transport Protocol Using Network Priorities. In: Proceedings of the 2018 Conference of the ACM
  Special Interest Group on Data Communication, SIGCOMM ’18. Association for Computing Machinery,
  pp. 221–235.

                                                                                           References            551



Moore, D., 2001. CAIDA analysis of code red. Personal conversation. Also see http://www.caida.org/analysis/
  security/code-red/.
Moore, D., Voelker, G., Savage, S., 2001. Inferring Internet denial-of-service activity. In: Proceedings of the 2001
  USENIX Security Symposium.
Mosberger, D., Peterson, L., 1996. Making paths explicit in the Scout operating system. In: Operating Systems
  Design and Implementation, pp. 153–167.
Mosberger, D., Peterson, L., Bridges, P., O’ Malley, S., 1996. Analysis of techniques to improve protocol latency.
  In: Proceedings of the ACM SIGCOMM.
Motin, A., Italiano, D., 2018. Calloutng: a new infrastructure for for timer facilities in the FreeBSD kernel. https://
  people.freebsd.org/davide/asia/calloutng.pdf.
Muthukrishnan, S., 2005. Data Streams: Algorithms and Applications at Foundations and Trends in Theoretical
  Computer Science. NOW Publisher Inc.
Myhrhaug, B., 2001. Sequencing set efficiency. In: Pub. A9, Norwegian Computing Center.
NEBS, 2002. Network equipment building system (NEBS) requirements. http://www.telecordia.com.
Neely, M.J., Modiano, E., Cheng, Y.S., 2007. Logarithmic delay for N × N packet switches under the crossbar
  constraint. IEEE/ACM Transactions on Networking 15 (3), 657–668.
Newman, P., Minshall, G., Huston, L., 1997. IP switching and Gigabit routers. In: IEEE Communications Maga-
  zine.
Nilsson, S., Karlsson, G., 1998. Fast address lookup for Internet routers. In: Proceedings of IEEE Broadband
  Communications 98.
Network Functions Virtualization (NFV), 2022. https://www.etsi.org/technologies/nfv.
Ousterhout, J., 2021. A Linux Kernel Implementation of the Homa Transport Protocol. In: 2021 USENIX Annual
  Technical Conference (USENIX ATC 21). USENIX Association, pp. 99–115.
Ousterhout, A., Fried, J., Behrens, J., Belay, A., Balakrishnan, H., 2019. Shenango: achieving high CPU efficiency
  for latency-sensitive datacenter workloads. In: NSDI’19. USENIX Association, pp. 361–377.
Ozveren, C., Simcoe, R., Varghese, G., 1994. Reliable and efficient hop-by-hop flow control. In: Proceedings of
  the ACM SIGCOMM.
P4 Open Source Programming Language, 2022. https://p4.org/.
Padhye, J., Floyd, S., 2001. On inferring TCP behavior. In: Proceedings of the ACM SIGCOMM, pp. 271–282.
Pai, V., Druschel, P., Zwaenepoel, W., 1999a. Flash: an efficient and portable Web server. In: Proceedings of the
  USENIX 1999 Annual Technical Conference.
Pai, V., Druschel, P., Zwaenepoel, W., 1999b. I/O-lite: a unified I/O buffering and caching system. In: Proceedings
  of the 3rd USENIX Symposium on Operating Systems Design and Implementation.
Pakin, S., Karamcheti, V., Chien, A.A., 1997. Fast messages: efficient, portable communication for workstation
  clusters and MPPs. In: IEEE Concurrency.
Pan, R., Prabhakar, B., Bonomi, F., Olsen, B., 2008. Approximate fair bandwidth allocation: A method for simple
  and flexible traffic management. In: 2008 46th Annual Allerton Conference on Communication, Control, and
  Computing, pp. 1081–1085.
Parekh, A., Gallager, R., 1993. A generalized processor sharing approach to flow control in integrated services
  networks: the single node case. IEEE/ACM Transactions on Networking 1 (3), 344–357.
Partridge, C., 1993. Gigabit Networking. Addison-Wesley, Reading.
Partridge, C., 1996. Locality and route caches. In: NSF Workshop on Internet Statistics Measurement. San Diego.
Partridge, C., Pink, S., 1993. A faster UDP. IEEE/ACM Transactions on Networking 1 (4).
Partridge, C., Blumenthal, S., Walden, D., 2004. Data networking BBN. In: IEEE Annals of Computing, pp. 56–71.
Parulkar, G., Turner, J., Schmidt, D., 1995. IP over ATM: a new strategy for integrating IP and ATM. In: Proceed-
  ings of the ACM SIGCOMM.
Patterson, H., et al., 1995. Informed prefetching and caching. In: Proceedings of the 15th ACM Symposium of
  Operating Systems Principles (SOSP).

552         References



Perlman, R., 1992. Interconnections: Bridges and Routers. Addison Wesley.
Peter, S., Li, J., Zhang, I., Ports, D.R.K., Woos, D., Krishnamurthy, A., Anderson, T., Roscoe, T., 2015. Arrakis:
   the operating system is the control plane. ACM Transactions on Computer Systems 33 (4), 11. https://doi.org/
   10.1145/2812806.
Peterson, L., Davy, B., 2000. Computer Networking: A Systems Approach, second edition. Morgan-Kaufman.
Pfaff, B., Pettit, J., Koponen, T., Jackson, E.J., Zhou, A., Rajahalme, J., Gross, J., Wang, A., Stringer, J., Shelar, P.,
   Amidon, K., Casado, M., 2015. The design and implementation of open VSwitch. In: Proceedings of the 12th
   USENIX Conference on Networked Systems Design and Implementation. NSDI’15, Oakland, CA. USENIX
   Association, pp. 117–130.
Polya, G., 1957. How to Solve It, 2nd edition. Princeton University Press.
PPCI-SIG Single Root I/O Virtualization, 2018. (SR-IOV) Support in Intel Virtualization Technology for Con-
   nectivity. https://www.intel.com/content/dam/doc/white-paper/pci-sig-single-root-io-virtualization-support-in-
   virtualization-technology-for-connectivity-paper.pdf.
Prabhakar, B., 2009. Scheduling algorithms for CIOQ switches. https://web.stanford.edu/class/ee384m/Handouts/
   handout9.pdf.
Prabhakar, B., McKeown, N., 1997. On the Speedup Required for Combined Input and Output Queued Switching.
   Stanford University.
Prekas, G., Kogias, M., Bugnion, E., 2017. ZygOS: achieving low tail latency for microsecond-scale networked
   tasks. In: Proceedings of the 26th Symposium on Operating Systems Principles, SOSP ’17. Association for
   Computing Machinery, pp. 325–341.
Preparata, F., Shamos, M., 1985. Computational Geometry: An Introduction. Springer-Verlag, New York.
QFQ source code in Linux Kernels. https://github.com/torvalds/linux/blob/master/net/sched/sch_qfq.c.
Qiu, L., Varghese, G., Suri, S., 2001. Fast firewall implementations for software and hardware-based routers. In:
   Proceedings of the 9th International Conference on Network Protocols (ICNP).
Rabin, M.O., 1981. Fingerprinting by random polynomials. Technical report.
Ramabhadran, S., Varghese, G., 2003. Efficient implementation of a statistics counter architecture. In: Proceedings
   ACM SIGMETRICS.
Ramakrishnan, K.K., Jain, R., 1990. A binary feedback scheme for congestion avoidance in computer networks.
   ACM Transactions on Computer Systems.
Rashid, R., Forin, A., Golub, D., Jones, M., Orr, D., Sanzi, R., 1989. Mach: a foundation for open systems (oper-
   ating systems). In: Proceedings of the Second Workshop on Workstation Operating Systems.
Rau, B., 1991. Pseudo-randomly interleaved memory. In: Proceedings International Symposium on Computer
   Architecture (ISCA).
RDMA Consortium, 2001. Architectural specifications for RDMA over TCP/IP. http://www.rdmaconsortium.org/
   home.
Rekhter, Y., Li, T., 1996. An architecture for IP address allocation with CIDR. In: RFC 1518.
Riccardi, F., 2001. Posted note. In: Linux Kernel Archive.
Rijsinghani, A., 1994. Computation of the Internet checksum via incremental update. In: RFC 1624. www.ietf.org/
   rfc/rfc1624.txt.
Rios, V., Varghese, G., 2022. MashUp: scaling TCAM-based IP lookup to larger databases by tiling trees. https://
   arxiv.org/abs/2204.09813.
Rizzo, L., Landi, M., 2011. Netmap: memory mapped access to network devices. In: Proceedings of the ACM
   SIGCOMM 2011 Conference, SIGCOMM ’11. In: Association for Computing Machinery, pp. 422–423.
Robson, J.M., 1974. Bounds for some functions concerning dynamic storage allocation. Journal of the Association
   for Computing Machinery.
Roesch, M., 1999. Snort—lightweight intrusion detection for networks. In: Proceedings of the 13th Systems Ad-
   ministration Conference. USENIX.
Ronad, A., 2019. Troubleshooting QoS on the Nexus9k. Presented at Cisco Live 2019, San Diego, CA. https://
   www.ciscolive.com/c/dam/r/ciscolive/us/docs/2019/pdf/CTHDCN-2301.pdf. (Accessed November 2020).

                                                                                         References           553



Sabnani, K., Netravali, A., 1989. A high speed transport protocol for datagram virtual circuit networks. In: Pro-
   ceedings of the ACM SIGCOMM.
Saeed, A., Dukkipati, N., Valancius, V., The Lam, V., Contavalli, C., Vahdat, A.C., 2017. Carousel: scalable traffic
   shaping at end hosts. In: Proceedings of the Conference of the ACM Special Interest Group on Data Communi-
   cation, SIGCOMM ’17. Association for Computing Machinery, pp. 404–417.
Salim, J.H., Olsson, R., Kuznetsov, A., Softnet, B., 2001. Beyond Softnet. In: Proceedings of the 5th Annual Linux
   Showcase & Conference, vol. 5, ALS ’01. USENIX Association, p. 18.
Sanchez, L., Milliken, W., et al., 2001. Hardware support for hash-based IP traceback. In: Proceedings of the 2nd
   DARPA Information Survivability Conference and Exposition. DISCEX.
Sarwate, D., 1988. Computation of cyclic redundancy checks by table lookup. Communications of the ACM 31
   (8).
Satran, J., Smith, D., Meth, K., et al., July 2001. ISCSI. In Internet Draft draft-ietf-ips-iSCSI-07.txt.
Savage, S., Wetherall, D., Karlin, A., Anderson, T., 2000. Practical network support for IP traceback. In: Proceed-
   ings of the ACM SIGCOMM, pp. 295–306.
Segmentation Offloads, 2022. https://www.kernel.org/doc/html/latest/networking/segmentation-offloads.html.
sendmsg copy avoidance with MS_ZEROCOPY, 2022. https://legacy.netdevconf.info/2.1/papers/debruijn-
   msgzerocopy-talk.pdf.
Semeria, C., 2002. T-series routing platforms: system and forwarding architecture. In: Juniper Networks White
   Paper, Part Number 200027-001.
Semeria, C., Gredler, J., 2001. Juniper networks solutions for network accounting. In: Juniper White Paper,
   200010-001.
Shah, D., Gupta, P., 2001. Fast updates on Ternary CAMs for packet lookups and classification. IEEE Micro 21
   (1).
Shah, D., Iyer, S., Prabhakar, B., McKeown, N., 2002a. Maintaining statistics counters in router line cards. IEEE
   Micro.
SHARP, 2019. In-Network Scalable Hierarchical Aggregation and Reduction Protocol. http://
   www.hpcadvisorycouncil.com/events/2019/swiss-workshop/pdf/020419/G_Bloch_Mellanox_SHARP_
   02042019.pdf.
Shah, D., Giaccone, P., Prabhakar, B., 2002b. Efficient randomized algorithms for input-queued switch scheduling.
   IEEE Micro 22 (1), 10–18.
Shannon, C., Moore, D., Claffy, K., 2001. Characteristics of fragmented IP traffic on Internet links. In: ACM
   SIGCOMM Internet Measurement Workshop.
Sherwood, T., Varghese, G., Calder, B., 2003. A pipelined memory architecture for high throughput network pro-
   cessors. In: International Symposium on Computer Architecture.
Sikka, S., Varghese, G., 2000. Memory efficient state lookups. In: Proceedings of the ACM SIGCOMM.
Simcoe, R., Pei, T., 1994. Perspectives on ATM switch architecture and the influence of traffic pattern assumptions
   on switch design. In: ACM Computer Communication Review.
Singh, S., Baboescu, F., Varghese, G., 2004a. Packet classification using multidimensional cutting. In: Proceedings
   ACM SIGCOMM.
Singh, S., Estan, C., Varghese, G., Savage, S., 2004b. Automated worm fingerprinting. In: OSDI.
Sivaraman, A., Subramanian, S., Alizadeh, M., Chole, S., Chuang, S.-T., Agrawal, A., Balakrishnan, H., Edsall,
   T., Katti, S., McKeown, N., 2016a. Programmable packet scheduling at line rate. In: Proceedings of the 2016
   ACM SIGCOMM Conference. Association for Computing Machinery, pp. 44–57.
Sivaraman, A., Cheung, A., Budiu, M., Kim, C., Alizadeh, M., Balakrishnan, H., Varghese, G., McKeown, N.,
   Licking, S., 2016b. Packet transactions: high-level programming for line-rate switches. In: SIGCOMM ’16.
   Association for Computing Machinery, pp. 15–28.
Smith, J., Traw, B., 2001. Technical report. Operating systems support for end-to-end Gbps networking.
Snoeren, A., Partridge, C., et al., 2001. Hash-based IP traceback. In: Proceedings of the ACM SIGCOMM,
   pp. 295–306.

554        References



Snort, 2001. The open source network intrusion detection system. http://www.snort.org/.
Souza, R., Krishnakumar, P., Ozveren, C., Simcoe, R., Spinney, B., Thomas, R., Walsh, R., 1994. GIGAswitch: A
   high-performance packet switching platform. Digital Technical Journal 6 (1), 9–22.
Spalink, T., Karlin, S., Peterson, L., 2000. Evaluating network processors in IP forwarding. Computer Science
   Technical Report TR-626-00. Princeton University.
SPEC consortium, 1999. Specweb99 benchmark. http://www.specbench.org/osg/web99/.
Spring, N., Mahajan, R., Wetherall, D., 2002. Measuring ISP topologies using rocketfuel. In: Proceedings of the
   ACM SIGCOMM.
Srinivasan, V., Varghese, G., 1999. Faster IP lookups using controlled prefix expansion. ACM Transactions on
   Computer Systems.
Srinivasan, V., Varghese, G., Suri, S., Waldvogel, M., 1998. Fast and scalable layer four switching. Computer
   Communication Review 28 (4), 191–202.
Srinivasan, V., Suri, S., Varghese, G., 1999. Packet classification using tuple space search. In: Proceedings of the
   ACM SIGCOMM, pp. 135–146.
Stanojevic, R., 2007. Small active counters. In: Proceedings of IEEE Infocom.
Stevens, W.R., 1994. TCP/IP Illustrated, vol. 1. Addison Wesley.
Stevens, W.R., 1998. UNIX Network Programming. Prentice-Hall.
Stewart, J.W., 1999. BGP-4: Interdomain Routing in the Internet. Addison Wesley.
Stiliadis, D., Varma, A., 1996a. Latency-rate servers: a general model for analysis of traffic scheduling algorithms.
   In: Proceedings of Infocom’96.
Stiliadis, D., Varma, A., 1996b. Design and analysis of frame-based fair queuing: a new traffic scheduling algorithm
   for packet switched networks. In: Proceedings of ACM Sigmetrics’96, pp. 104–115.
Sting, S. Savage, 1999. A TCP-based network measurement tool. In: USENIX Symposium on Internet Technolo-
   gies and Systems.
Stoica, I., Abdel-Wahab, H., 1995. Earliest Eligible Virtual Deadline First: A Flexible and Accurate Mechanism
   for Proportional Share Resource Allocation. Old Dominion University.
Stoica, I., Zhang, H., 1998. Exact emulation of an output queueing switch by a combined input output queueing
   switch. In: Sixth IEEE/IFIP International Workshop on Quality of Service, pp. 218–224.
Stoica, I., Shenker, S., Zhang, H., 1998. Core-Stateless Fair Queuing: Achieving approximately fair bandwidth. In:
   Proceedings of ACM SIGCOMM’98, pp. 118–130.
Stone, J., Partridge, C., 2000. When the CRC and TCP checksum disagree. In: Proceedings of the ACM SIG-
   COMM, pp. 309–319.
Sundar, I., 2008. Load balancing and parallelism for the internet. PhD Thesis. Stanford University.
Sundar, I., Kompella, R.R., McKeown, N., 2008. Designing packet buffers for router linecards. IEEE/ACM Trans-
   actions on Networking 16 (3), 705–717. https://doi.org/10.1109/TNET.2008.923720.
Suri, S., Varghese, G., Chandranmenon, G., 1997. Leap forward virtual clock: a new fair queuing scheme with
   guaranteed delays and throughput fairness. In: Proceedings of Infocom 97.
Suri, P., Warkhede, S., Varghese, G., 2001. Multiway range trees: Scalable IP lookup with fast updates. In: Globe-
   com.
Sutherland, I., Sproull, R., Harris, D., 1999. Logical Effort, Designing Fast CMOS Circuits. Morgan Kaufmann.
Tamir, Y., Frazier, G.L., 1988. High-performance multi-queue buffers for VLSI communications switches.
   SIGARCH Computer Architecture News 16 (2), 343–354.
Tanenbaum, A.S., 1981. Computer Networks. Prentice-Hall.
Tanenbaum, A., 1992. Modern Operating Systems. Prentice Hall.
Tassiulas, L., 1998. Linear complexity algorithms for maximum throughput in radio networks and input queued
   switches. In: Proceedings of the IEEE INFOCOM. San Francisco, CA, pp. 533–539.
Tassiulas, L., Ephremides, A., 1992. Stability properties of constrained queueing systems and scheduling poli-
   cies for maximum throughput in multihop radio networks. IEEE Transactions on Automatic Control 37 (12),
   1936–1948.

                                                                                         References            555



Taylor, D.E., Turner, J.S., 2007. ClassBench: a packet classification benchmark. IEEE/ACM Transactions on Net-
  working 15 (3), 499–511.
Thadani, M.N., Khalidi, Y.A., 1995. An efficient zero-copy I/O framework for UNIX. Technical Report SMLI
  TR-95-39. Sun Microsystems Laboratories, Inc.
The Lam, V., Mitzenmacher, M., Varghese, G., 2010. Carousel: scalable logging for intrusion prevention systems.
  In: Proceedings of the 7th USENIX Symposium on Networked Systems Design and Implementation. NSDI
  2010, April 28–30, 2010. USENIX Association, San Jose, CA, pp. 361–376.
The State of Fibre Channel, 2022. https://fibrechannel.org/state-of-fibre-channel/.
Thekkath, C., Nguyen, T., Moy, E., Lazowska, E., 1993. Implementing network protocols at user level. In: Pro-
  ceedings ACM SIGCOMM.
Thomas, R., Varghese, G., Harvey, G., Souza, R., 1992. Method for keeping track of sequence numbers in a large
  space.
Thompson, K., Miller, G., Wilder, R., 1997. Wide-area traffic patterns and characterizations. In: IEEE Network.
Touch, J., Parham, B., 1996. Implementing the Internet checksum in hardware. In: RFC 1936. www.ietf.org/rfc/
  rfc1936.txt.
Toynbee, A., Caplan, J., 1972. A Study of History, Abridged Version. Oxford University Press.
Turner, J.S., 1986. New directions in communications (or which way to the information age?). IEEE Communica-
  tions.
Turner, J., 1997. Design of a gigabit ATM switch. In: Proceedings of IEEE INFOCOM.
Turner, J., 2002. Personal communication.
UNH Inter Operability Lab, 2001. FDDI tutorials. http://www.iol.unh.edu/training/fddi.html.
Userspace Networking with DPDK. https://www.linuxjournal.com/content/userspace-networking-dpdk.
Valente, P.o, 2004. Exact GPS simulation with logarithmic complexity, and its application to an optimally fair
  scheduler. In: Proceedings of the ACM SIGCOMM.
Valiant, L., 1990. A bridging model for parallel computation. Communications of the ACM 33 (8).
Vamanan, B., Vijaykumar, T.N., 2011. TreeCAM: decoupling updates and lookups in packet classification. In:
  Proceedings of the Seventh COnference on Emerging Networking EXperiments and Technologies. Association
  for Computing Machinery.
Vamanan, B., Voskuilen, G., Vijaykumar, T.N., 2010. EffiCuts: Optimizing packet classification for memory and
  throughput. In: Proceedings of the ACM SIGCOMM 2010 Conference. SIGCOMM ’10. Association for Com-
  puting Machinery, pp. 207–218.
Varadhan, K., Govindan, R., Estrin, D., 2000. Persistent route oscillations in inter-domain routing. Computer Net-
  works 32 (1), 1–16.
Varghese, G., Lauck, A., 1987. Hashed and hierarchical timing wheels: data structures for the efficient imple-
  mentation of a timer facility. In: Proceedings of the 11th ACM Symposium on Operating Systems Principles
  (SOSP).
Vaucher, J.G., Duval, P., 1975. A comparison of simulation event list algorithms. In: CACM, vol. 18.
von Eicken, T., Culler, D., et al., 1992a. Active messages: a mechanism for integrated communication and compu-
  tation. In: 19th International Symposium on Computer Architecture, pp. 256–266.
von Eicken, T., Culler, D., Goldstein, S., Schauser, K., 1992b. Active messages: a mechanism for integrated com-
  munication and computation. In: Proceedings of the 19th International Symposium on Computer Architecture
  (ISCA), pp. 256–266.
von Eicken, T., Basu, A., et al., 1995. U-Net: a user-level network interface for parallel and distributed computing.
  In: Proceedings of the 15th ACM Symposium on Operating Systems Principles (SOSP).
Waldvogel, M., Varghese, G., Turner, J., Plattner, B., 1997. Scalable high speed IP routing lookups. In: SIGCOMM.
Wang, J., Huang, C., 2000. A high-speed single-phase-clocked CMOS priority encoder. In: IEEE International
  Symposium on Circuits and Systems.
Wang, H., Zhao, H., Lin, B., Xu, J., 2010. Design and analysis of a robust pipelined memory system. In: 2010
  Proceedings of IEEE INFOCOM, pp. 1541–1549.

556        References



Wang, L., Ye, T., Lee, T., Hu, W., 2018. A parallel complex coloring algorithm for scheduling of input-queued
  switches. IEEE Transactions on Parallel and Distributed Systems 29 (7), 1456–1468.
Warkhede, P., Suri, S., Varghese, G., 2001. Multiway range trees: scalable IP lookups with fast updates. In: IEEE
  Globecom 2001 Internet Symposium.
Web Polygraph Association, 2001. Web polygraph. http://www.web-polygraph.org/.
Welsh, M., Culler, David E., Brewer, Eric A., 2001. SEDA: an architecture for well-conditioned, scalable Internet
  services. In: Proceedings of the 22nd Symposium on Operating Systems Principles (SOSP), pp. 230–243.
Whang, K., Vander-Zanden, B., Taylor, H., 1990. A linear-time probabilistic counting algorithm for database
  applications. ACM Transactions on Database Systems.
Wilson, P., 1992. Uniprocessor garbage collection techniques. Lecture Notes in Computer Science, vol. 637.
  Springer-Verlag.
Wilson, P., Johnstone, M., et al., 1995. Dynamic storage allocation: a survey and critical review. In: Proceedings
  of the International Workshop on Memory Management. Kinross Scotland (UK).
Wilton, S.J.E., Jouppi, N.P., 1996. CACTI: an enhanced cache access and cycle time model. IEEE Journal of
  Solid-State Circuits 31 (5), 677–688.
Woo, T., 2000. A modular approach to packet classification: algorithms and results. In: Proceedings IEEE INFO-
  COM.
Wright, G.R., Stevens, W.R., 1995. TCP/IP Illustrated, vol. 2. Addison-Wesley.
Xu, J., Singhal, M., Degroat, J., 2000. A novel cache architecture to support layer four packet classification at
  memory access speeds. In: Proceedings IEEE INFOCOM, pp. 1445–1454.
Yang, M., Zheng, S.Q., 2003. An efficient scheduling algorithm for CIOQ switches with space-division multi-
  plexing expansion. In: INFOCOM 2003. Twenty-Second Annual Joint Conference of the IEEE Computer and
  Communications, vol. 3. IEEE Societies, pp. 1643–1650.
Yang, T., Xie, G., Li, Y., Fu, Q., Liu, A.X., Li, Q., Mathy, L., 2014. Guarantee IP lookup performance with FIB
  explosion. Computer Communication Review 44 (4), 39–50. https://doi.org/10.1145/2740070.2626297.
Yang, S., Lin, B., Tune, P., Xu, J., 2017a. A simple re-sequencing load-balanced switch based on analytical packet
  reordering bounds. In: The 36th Annual IEEE International Conference on Computer Communications (INFO-
  COM).
Yang, Sen, Lin, Bill, Xu, Jun, 2017b. Safe randomized load-balanced switching by diffusing extra loads. Proceed-
  ings of the ACM on Measurement and Analysis of Computing Systems 1 (2), 29:1–29:37.
Yeh, Y., Hluchyj, M., Acampora, A., 1987. The knockout switch: a simple modular architecture for high-
  performance packet switching. IEEE Journal on Selected Areas in Communications, 1426–1435.
Yuan, X., Duan, Z., Round-Robin, F., 2009. A low complexity packet schduler with proportional and worst-case
  fairness. IEEE Transactions on Computers 58 (3), 365–379. https://doi.org/10.1109/TC.2008.176.
Zane, F., Narlikar, G., Basu, A., 2003. Coolcams: power-efficient TCAMs for forwarding engines. In: IEEE INFO-
  COM 2003. Twenty-Second Annual Joint Conference of the IEEE Computer and Communications Societies,
  vol. 1, pp. 42–52. (IEEE Cat. No. 03CH37428).
Zec, M., Mikuc, M., 2017. Pushing the envelope: beyond two billion IP routing lookups per second on com-
  modity CPUs. In: 25th International Conference on Software, Telecommunications and Computer Networks
  (SoftCOM), pp. 1–6.
Zec, M., Rizzo, L., Mikuc, M., 2012. DXR: towards a billion routing lookups per second in software. Computer
  Communication Review 42 (5), 29–36. https://doi.org/10.1145/2378956.2378961.
Zhang, L., 1991. Virtual clock: a new traffic control algorithm for packet-switched networks. ACM Transactions
  on Computer Systems.
Zhang, H., Ferrari, D., 1994. Rate-controlled service disciplines. Journal of High Speed Networks 3 (4), 389–412.
Zhang, Y., Roughan, M., Duffield, N., Greenberg, A., 2003. Fast accurate computation of large-scale IP matrices
  from link loads. In: Proceedings of the ACM SIGMETRICS.
Zhang, Y., Singh, S., Sen, S., Duffield, N., Lund, C., 2004. Online identification of hierarchical heavy hitters:
  algorithms, evaluation, and application. In: Proceedings of the ACM Internet Measurement Conference (IMC).

                                                                                         References           557



Zhao, Q., Xu, J., 2004. On the computational complexity of maintaining GPS clock in packet scheduling. In:
  Proceedings of IEEE INFOCOM.
Zhao, Q., Kumar, A., Wang, J., Xu, J., 2005. Data streaming algorithms for accurate and efficient measurement of
  traffic and flow matrices. In: Proceedings of ACM SIGMETRICS.
Zhao, Q., Ge, Z., Wang, J., Xu, J., 2006a. Robust traffic matrix estimation with imperfect information: making use
  of multiple data sources. In: Proceedings of ACM SIGMETRICS.
Zhao, Q., Xu, J., Liu, Z., 2006b. Design of a novel statistics counter architecture with optimal space and time
  efficiency. In: Proceedings of ACM SIGMETRICS.
Zhao, H. (Chuck), Wang, H., Lin, B., Xu, J. (Jim), 2009. Design and performance analysis of a DRAM-based
  statistics counter array architecture. In: Proceedings of the 5th ACM/IEEE Symposium on Architectures for
  Networking and Communications Systems, ANCS’09. ACM, New York, NY, pp. 84–93.
Zhao, H. (Chuck), Lall, A., Ogihara, M., Xu, J., 2010. Global iceberg detection over distributed data streams. In:
  Proceedings of IEEE ICDE.
Zhao, S., Wang, R., Zhou, J., Ong, J., Mogul, J.C., Vahdat, A., 2019. Minimal rewiring: efficient live expansion for
  clos data center networks. In: 16th USENIX Symposium on Networked Systems Design and Implementation
  (NSDI 19). USENIX Association, Boston, MA, pp. 221–234.

This page intentionally left blank

Index

A                                                   Banyan, 540
Acknowledgments (ack), withholding, 99–101          Barrel shifters, 24
Active messages, 168                                Batch allocator, 214, 215
Adaptor memory, 115–117                             Batching, 59, 173
Address lookup, 252                                 Benes networks, 370–375
Address Resolution Protocol (ARP), 38               Berkeley packet filter (BPF), 152, 199–201
Addresses, Internet, 252                            BGP (Border Gateway Protocol), 18, 443, 444
Admission control, 392                              Binary search
Afterburner approach, 116, 117                        of long identifiers, 103–105
Aggregation                                           on prefix lengths, 278–280
                                                      on ranges, 275–277
  edge, 425, 426
                                                      on ranges with initial lookup table, 277, 278
  random, 425
                                                      pipelining, 244, 245
  threshold, 464–466
                                                    Binary trees, balanced, 29
Aho–Corasick algorithm, 490–493
                                                    Binomial bucketing, 95
Algorithms versus algorithmics, 55, 56              Bit slicing, 375, 376
American National Standards Institute (ANSI), 128   Bit vector linear search, 316–318
Anomaly intrusion detection, 489                    Bit-by-bit round-robin, 395
Apache Web server, 155                              Bitmap, tree, 271–274
API                                                 Blockade state, 393
  speeding up select() by changing, 164, 165        Bloom filters, 501, 502
  speeding up select() without changing, 163, 164   Bottlenecks, 3
Appletalk, 38, 237                                    endnode, 4, 5
Application code, 146                                 router, 5–7
Application device channel (ADC), 168               Boyer–Moore algorithm, 493–495
  buffer validation of, 76–78                       BPF (Berkeley packet filter), 152, 199–201
Architecture                                        Bridges/bridging, 82, 83
  endnode, 33–35                                      defined, 235
  router, 35–39                                       Ethernets, 236–238
  virtual interface, 169                              scaling lookups to higher speeds, 242–246
Asynchronous transfer mode (ATM)                      wire speed forwarding, 238–242
  flow control, 78, 79                              BSD UNIX, 41, 42, 173
  video conferencing via, 105–107                     callouts and timers, 189, 190
                                                    Bucket sorting, 80, 95, 96
                                                    Buddy system, 213, 214
B                                                   Buffer(s)
Backtracking, 14, 307, 308                            aggregates, 132
Baker, Fred, 241                                      allocation, 5, 212–215
Bandwidth, 28                                         dynamic buffer limiting, 216
  guarantees, 393–399                                 fast, 119–123
  reduce collection, 469, 470                         management, 212, 217
  scaling, 5                                          overflow, 8
Banks, 28                                             sharing, 215–217, 432
                                                                                                      559

560        Index



  stealing, 215, 216                                    Compaction, frame-based, 284, 285
  validation of application device channel (ADC),       Compaq Computer Inc., virtual interface architecture,
           76–78                                                   169
Buffers, Router, 438–441                                Concentrator, 343
Buses, 29, 34, 335, 336                                 Concurrency, 148, 157, 158
Butterfly network, 540                                  Connection lists, getting rid of TCP open, 96–99
Byte swapping and order, 221, 222                       Content-addressable memory (CAM), 51–55, 244,
                                                                   258, 301, 304
C                                                       Control overhead, 5, 240
Caches (caching), 33, 34, 64, 65, 137–141, 258            context-switching, 153–159
  packet classification and, 302                          fast select, 159–165
Callouts, 189                                             in networking code, 149–153
Cell, 204                                                 interrupts, 172–174
CERN Web proxy, 159                                       reasons for, 147–149
Channel, 435                                              restructuring, 171, 172
Checksums, 5, 37, 217                                     system calls, 166–171
  header, 222, 223                                      Copy-on-write (COW), 59, 117, 118
  Internet, 221–223                                       transient (TCOW), 124, 125
Cheetah Web server, 133                                 Copying, 4
Chesson, Greg, 224                                        Afterburner approach, 116, 117
Chi-square, 15                                            daptor memory, 115–117
                                                          data, 132
Chips
                                                          in a cluster, 127, 128
  design, 538
                                                          loop, 134–136
  scaling and speeds, 32
                                                          methods of, 113–115
Circuit switches, 39
                                                          page remapping, 119–123
Cisco, 256, 332, 399, 452
                                                          reducing, 115–125
  GSR, 525
                                                          remote DMA to avoid, 126–130
  NetFlow, 468
                                                          semantics, transparent emulation, 123–125
Clark, Dave, 149–151
                                                          zero copying in modern systems, 125, 126
Class-based queuing (CBQ), 398, 399
                                                        Counting (counters), 452, 453
Classification, see Packet classification
                                                          per-prefix, 474
Classless Internet Domain Routing (CIDR), 252
                                                          probabilistic, 467
Client                                                    reducing counter height using flow, 466, 467
  structuring processes per client, 154, 155              reducing counter height using threshold aggregation,
  structuring threads per client, 155                              464–466
Clos, Charles, 366                                        reducing counter width using approximate, 464
Clos networks, 366, 367, 539                            Cross-producting
Clouds                                                    equivalenced, 320–323
  traffic shaping, 190, 191                               on demand, 318–320
Clusters                                                Crossbar, 336
  copying in, 127                                       Crossbar switches/scheduler, 6, 337–340
  VAX, 126–128                                          Crosspoint, 337, 338
CMU Stanford packet filter (CSPF), 152, 198, 199, 208   CSPF (CMU Stanford packet filter), 152, 198, 199, 208
Code                                                    Cyclic redundancy check (CRC), 217
  application, 146
  arrangement, 139, 140                                 D
  networking, 149–153                                   Data, copying, see Copying data
Column address strobe (CAS), 28                         Data cache, 33

                                                                                           Index   561



Data link layer, 237                                   dlmalloc(), 214
Data manipulations, 19                                 Doorbells, 169
Data Plane Development Kit (DPDK), 169                 Download times, reducing, 67, 68
Databases, incremental reading of large, 101–103       Duplicates, 442
DCA, 138                                               Dynamic buffer limiting, 216
DEC (Digital Equipment Corporation), 127, 236, 241,    Dynamic packet filter (DPF), 205–208
            242                                        Dynamic random access memory (DRAM), 27–30, 33,
DECbit scheme, 387                                                240, 537
Decision trees, 323–326                                  reducing SRAM width using, backing store,
DECNET, 38, 237                                                   453–455
Decoders, 24
Deficit round-robin (DRR), 395–399                     E
Degrees of freedom, 54, 55, 65                         Encoders
Delay guarantees, 384, 386, 399, 424                     architecture, 35
Delta network, 370–372, 540                              design of priority, 23, 24
Demand paging, 43                                        programmable priority, 24–26
Demultiplexing (demultiplexers), 5, 19, 24, 151, 152     quality of service and priority, 22
  Berkeley packet filter (BPF), 152, 199–201           Encoders, programmable priority, 351
                                                       Endnodes, 3, 4, 514, 515
  challenges of early, 197, 198
                                                         architecture, 33–35
  CMU Stanford packet filter (CSPF), 152, 198, 199,
                                                       Ethernets
            208
                                                         description of, 236–238
  defined, 195
                                                         forwarding packets, 82, 83
  delayered, 197
                                                       Event-driven scheduler, 155
  dynamic packet filter (DPF), 205–208
                                                       Event-driven server, 157
  early, 121, 195–198
                                                       Evil packet example, 8
  in x-kernel, 84, 85
                                                       Exact-match lookups, 5, 29, 235–246
  layered, 195
                                                       ExpiryProcessing, 182
  packet classification and, 303
                                                       Expression tree model, 198, 199
  PathFinder, 152, 201–205
                                                       Extended grid of tries (EGT), 315
Dense wavelength-division multiplexing (DWDM),
            363                                        F
Descriptors, 166–169                                   False negative, 10
Design, implementation principles versus, 66, 67       Fast retransmit, 387
Device driver, 44                                      Fast select, see select()
DiffServ, 297, 304, 383, 425, 426                      fbufs (fast buffers), 119–123
Dijkstra’s algorithm, 79–81                            FDDI, 242, 244
Direct memory access (DMA), 34, 240                    Feynman, Richard, 516
  remote, 126–130                                      Fiber Channel, 21, 128
  versus programmed I/O, 142                           Fibre Channel, 127, 128
Directed acyclic graph (DAG), 205                      File systems
Display-get-data, 150                                     I/O splicing, 134
Distinct keys, 442                                        IO-Lite, 132–134
Distributed systems, routers as                           shared memory, 120, 131
  asynchronous updates, 441–443                        Fine-granularity timers, 191, 192
  distributed memory, 438–441                          Firewalls, 297
  internal flow control, 430–435                       First in, first out (FIFO), 383
  internal striping, 435–438                           Fisk, Mike, 8
Divide-and-conquer, 315–323                            Fixed-stride tries, 262, 263

562        Index



Flash Web server, 157, 524                               Hole filling, 475
Flip-flops, 27                                           Hunt groups, 340
Flow control, internal, 430–435                          Hypercube, 540
Flow counting, reducing counter height using, 466, 467
Flow ID lookups, 29–31                                   I
Flow switching, 256, 257                                 I-caches, 138–140
Forwarding, 18                                           I/O splicing, 134
Forwarding information base (FIB), 36                    IBM, 237
Fractional cascading, 312                                Identifiers, binary search of long, 103–105
Fragmentation, 38                                        Implementation principles
   of link state protocols, 90–92                           caution when using, 69–71
Frame-based compaction, 284, 285                            modularity with efficiency principles, 57, 62–64
                                                            routines, principles for speeding up, 57, 64–66
G                                                           systems principles, 57–62
Generalized Processor Sharing (GPS), 400–407                versus design, 66, 67
  clock tracking, 384, 401, 403, 405, 407, 408           Infiniband, 128, 129
  graph, 401, 413                                        Instruction cache, 33
  virtual finish time, 401, 402                          Integrated layer processing (ILP), 135
Geometric view, of packet classification, 311, 312       Intel
Gigaswitch, 242–244                                         virtual interface architecture, 169
Green, Larry, 224                                           VTune, 21
Grid of tries, 295, 305, 308–310                         Internal flow control, 430–435
  extended, 315                                          Internal striping, 435–438
                                                         Internet Control Message Protocol (ICMP), 38
H                                                        Interrupt(s)
Hardware                                                    handlers, 40, 151
  component-level design, 31                                reducing, 172–174
  design tools, 24–26                                       software, 41, 151, 173, 174
  logic gates, 22                                        Intrusion detection systems (IDSs), 489
  memory, 26–31                                             Aho–Corasick algorithm, 492, 493
  models, 533–538                                           anomaly, 489
  parallelism, 244                                          Boyer–Moore algorithm, 493–495
  parameters, 32, 33                                        logging, 499–504
  transmission speed, 23, 24                                probabilistic marking, 497–499
Hart, John, 241                                             searching for multiple strings in packet payloads,
Harvest Web server, see Squid Web server                              491–495
Hashed wheels, 185, 186                                     signature, 489
Hashing, 29, 77, 242–244                                    speeding up, 68, 69
  locality-sensitive, 495                                   string matching, approximate, 495, 496
Head-of-line blocking, 6, 331, 340–344                      subtasks, 490
Header checksum, 222, 223                                   worms, detecting, 504–506
Header fields, 298                                       IO-Lite, 132–134
Header prediction, 224–226                               IP Lookups, see Prefix-match lookups
Header validation, 37                                    iSCSI, 21, 22, 129
Hewlett-Packard, OpenView, 21                            iSLIP, 347–352
Hierarchical deficit round-robin, 398
Hierarchical wheels, 187, 188                            J
Hints, use of, 63–66                                     Jumbo frames, 173

                                                                                           Index       563



K                                                        mbufs, 122, 212
Kempf, Mark, 237, 241                                    McQuillan, John, 297
Kernels, 44, 169                                         Measuring network traffic
Kingsley, Chris, 213                                      difficulty of, 451–453
Knockout tree, 343                                        reducing collection bandwidth, 469, 470
                                                          reducing counter height using flow counting, 466,
L                                                                    467
Labels, passing, 303                                      reducing counter width using approximate counting,
Latency, 20                                                          464
Lauck, Tony, 241                                          reducing counters using threshold aggregation,
Layer 4 switching, see Packet classification                         464–466
Layer processing, locality-driven, 140, 141               reducing processing using sampled NetFlow, 468
Lazy evaluation, 13, 59, 98, 117, 174, 222                reducing reporting using sampled charging, 469, 470
Lazy receiver processing (LRP), 174                       reducing SRAM width using DRAM backing store,
Lea, Doug, 214                                                       453–455
Leaf pushing, 269                                         Sting, 475, 476
                                                          traffic matrices, 472–474
Least-cost matching rule, 295, 298–300
                                                          trajectory sampling to correlate, 470
Level-compressed tries, 267, 268
                                                         Memory, 26–31
Linear feedback shift register (LFSR), 220
                                                          adaptor, 115–117
Linear search, 301
                                                          allocation in compressed schemes, 283–285
  bit vector, 316–318
                                                          backtracking, 307
  on prefix lengths, 280–283
                                                          content-addressable memory (CAM), 51–55, 244,
Link state packet (LSP), 18, 79, 90–92
                                                                     258, 301, 304
Link state protocols, avoiding fragmentation of, 90–92
                                                          direct memory access (DMA), 34, 240
Linux allocator, 214
                                                          dynamic random access memory (DRAM), 27–30,
Logging, 499–504
                                                                     33, 240, 537
Logic gates, 22, 533, 534
                                                          main, 31
Logical reception, 435
                                                          mapped, 34
Lookups
                                                          registered, 169
  chip model, 285, 286
                                                          scaling, 377, 378
  exact-match, 5, 29, 235–246
                                                          shared, 120, 131, 334
  flow ID, 29–31                                          static random access memory (SRAM), 27, 33, 242,
  IP lookups using P4, 288, 289                                      453, 454, 536
  prefix-match, 5, 36                                     virtual, 42, 43, 117–119
  programmable processor model, 286–288                  Memory management unit (MMU), 43
Lookups using P4                                         MERGE procedure, 353–355
  Tree of CAMs, MashUp, 288, 289                         Microsoft Inc., virtual interface architecture, 169
Lulea-compressed tries, 268–271                          Minimum bandwidth, 398
                                                         Modified deficit round-robin, 399
M                                                        Modularity with efficiency principles, 57
malloc(), 213                                             generality, avoiding, 63
Markers, 433, 434, 437                                    hints, use of, 63–66
Masking, 221                                              over referencing, avoiding, 63
Matchmaking, 154, 155                                     replace inefficient routines, 62, 63
Maximal matching, 345                                    Multi-protocol-label switching (MPLS), 38, 256–258,
Maximum matching, 345                                                303
Maximum weighted matching (MWM), 345, 352, 353           Multibit tries, 262–267

564        Index



Multicast, 337, 340, 351                              passing labels, 303
Multichassis routers, 363, 364, 366–370               reasons for, 296–298
Multiplexers, 24                                      requirements and metrics, 301
Multithreading, 39                                    role of, 295
                                                      routers, 295
N                                                     Tuple Space Search (TSS), 301
Net-dispatch, 150                                     two dimensional, 304–310, 313–315
NetFlow, 468, 469                                   Packet filters
Network address translation (NAT), 252, 297           Berkeley (BPF), 152, 199–201
Network algorithmics                                  CMU Stanford (CSPF), 152, 198, 199, 208
  algorithms versus, 55, 56                           dynamic, 205–208
  characteristics of, 13–15                         Packet steering, 173
  defined, 14, 519–523                              Packetized generalized processor sharing (PGPS), 400
  future, 525–527                                   Packets, 18
  real products and, 524, 525                         filtering in routers, 87–90
  techniques, 7–15                                    flow, 385
Network processors, 36, 38, 39                        header validation and checksums, 37
Networking code, avoiding scheduling overhead in,     logs, 453, 468
           149–153                                    repeater, 237, 238
Node compression, tries and, 85–87                    scheduling, 383–427
  1D torus, 376                                     Page mode, 28, 240
                                                    Page remapping, 119–123
                                                    Pages, 43
O
                                                    Parallel iterative matching (PIM), 344–347
Offload Mechanisms, 173
                                                    Parallelism, hardware, 244
Operating systems
                                                    Pareto optimality, 215
  system calls and simple, 44
                                                    Path MTU, 228
  uninterrupted computation, 40–42
                                                    PathFinder, 152, 201–205, 303
  virtual memory, 42, 43                            Patricia trie, 14, 261
OSPF, 18, 37, 79                                    pbufs, 213
Output queuing, 342, 343                            Per-prefix counters, 474
Output scheduling, 37                               Perfect hashing, 243
                                                    Performance, improving, 431, 432, 435, 436, 439, 442
P                                                   Performance measures, 21
P4 Language                                           for timers, 181
  model, functionality, applications, 287, 288        select() and server performance problem, 159, 160
Packet classification, 6, 37, 197, 295              Perlman, Radia, 241
  caching, 302                                      PerTickBookkeeping, 181, 182
  content-addressable memory, 304                   Physical reception, 435
  cross-producting, 318–320                         Piggybacking, 101
  cross-producting, equivalenced, 320–323           Ping, 475
  decision trees, 323–326                           Pipelining, 29, 30, 244, 245
  demultiplexing, 303                               Polling, 173, 175
  divide-and-conquer, 315–323                       Population scaling, 5
  extended grid of tries, 313                       Prefix-match lookups, 5, 36
  geometric view, 311, 312                            binary search, on ranges, 275–277
  grid of tries, 308–310                              binary search, on ranges, with initial lookup table,
  linear search, 301                                             277, 278
  linear search, bit vector, 316–318                  binary search, prefix lengths, 278–280

                                                                                        Index        565



  flow switching, 256, 257                             R
  linear search, prefix lengths, 280–283               Random early detection (RED), 386, 388
  memory allocation, 283–285                           Randomization
  model, 252–254                                         avoiding, 347–352
  model, lookup-chip, 285, 286                           memory scaling using, 377, 378
  model, programmable processors, P4, 286, 287         Rate sharing, 432
  multi-protocol label switching, 38, 256–258, 303     Rational, Quantify, 21
  nonalgorithmic techniques for, 258, 259              Reading large databases, incremental, 101–103
  notation, 250, 251                                   Rearrangeably nonblocking, 368
  threaded indices and tag switching, 14, 255–257      Reassembly, 20, 227–230
  tree bitmaps, 271–274                                Receive Flow Steering, 173
                                                       Receive Packet Steering, 173
  tries, level-compressed, 267, 268
                                                       Receiver livelock, 41, 42
  tries, Lulea-compressed, 268–271
                                                         avoiding, 173, 174
  tries, multibit, 262–267
                                                       Reception
  tries, unibit, 259, 262
                                                         logical, 435
  variable-length, reasons for, 252
                                                         physical, 435
Priorities, 348, 349, 351, 391                         Recursive flow classification (RFC), 296, 320, 323,
Priority encoder (PE), 24                                          329
Probabilistic counting, 467                            Redirects, 38
Probabilistic marking, 497–499                         Reentrant, 152
Programmable logic array (PLA), 535                    Registered memory, 169
Programmable priority encoder (PPE), 24–26, 351, 359   Registers, 27, 536
Protocol control block (PCB), 224–226                  Reliability, 432–434, 436–439, 443
Protocol Engines, Inc., 224                            Remote direct memory access (RDMA), 112, 126–130
Protocol processing                                    Repeaters
  buffer management, 212–217                             filtering, 238
  checksums and cyclic redundancy checks, 217–223        packet, 237
  generic, 224–227                                     Resemblance, 496
  reassembly, 227–230                                  Reservation protocols, 392, 393
Protocols, 18–20, 37, 38                               Resource Reservation Protocol (RSVP), 393
  reservation, 392                                     Resources, identifying, 94–96
Pushout, 216                                           Restructuring
                                                         OS, 171, 172
                                                       RIP, 18, 37
Q
                                                       Round-robin
Quality of service (QOS), 22, 383, 392
                                                         deficit (bit-by-bit), 395–398
  reasons for, 385, 386
                                                         slice-by-slice, 393–395
Queue-Proportional Sampling (QPS), 332                 Routers, 3, 5–7, 429, see also Distributed systems,
  algorithm, 357                                                   routers as
  behavior, 357                                          architecture, 35–39
  data structure, 356–358                                fragmentation, redirects and ARPs, 38, 39
  implementation, 357                                    history of, 335, 336
  strategy, 356                                          lookup, 36, 37
Queuing, 37                                              multichassis, 363, 364, 366–370
  class-based, 398, 399                                  packet classification, 295
  multiple outbound, 391, 392                            packet filtering in, 87–90
  output, 342, 343                                       pin-count for buffers, 31, 32
  scalable fair, 424–426                                 processing, 37, 38

566        Index



  queuing, 37                                             Short links, 376, 377
  switching, 37                                           Signature intrusion detection, 489
  telephone switches versus, 333, 334                     Simcoe, Bob, 242
Routines, principles for speeding up, 57, 64, 66          Simple Network Management Protocol (SNMP), 38,
Routing, 18                                                            452, 473, 526
  computation using Dijkstra’s algorithm, 79–81           Single Root I/O Virtualization (SRIOV), 170
Row address strobe (RAS), 27                              Sliding-Window Queue-Proportional Sampling
                                                                       (SW-QPS), 332, 359
S                                                         Small-Batch Queue-Proportional Sampling (SB-QPS),
Sampled charging, 469, 470                                             359
Savage, Stefan, 475                                       SNA, 38, 237
Scalable fair queuing, 424–426                            Snapshot, 433
Scale                                                     Snort, 466, 489–492, 494
   bandwidth, 5                                           SNS, 237
   endnode, 4                                             Socket queue, 42
   population, 5                                          Software interrupt, 41, 151, 173, 174
   router, 5                                              Spanning tree algorithm, 241
                                                          SPECweb, 115, 134
Scaling
                                                          Spinney, Barry, 242, 244
   chip, 32
                                                          Squid Web server, 157, 159, 160
   memory, 32, 377, 378
                                                          Staircase query problem, 410
   population, 515
                                                          StartTimer, 181, 182
   speed, 515
                                                          State machine implementation, 31
   to faster switches, 363
                                                          Static random access memory (SRAM), 27, 33, 242,
   to larger switches, 363
                                                                       536
   via hashing, 242–244
                                                             reducing, using DRAM backing store, 453–455
Schedule clients, 20
                                                          Sting, 452, 475, 476
Scheduling                                                StopTimer, 181, 183
   crossbar, 24–26, 337–340                               Storage area network (SAN), 21, 22, 128
   event-driven, 155                                      Strict priority, 392
   output, 37                                             String matching, approximate, 495, 496
   packets, 383–427                                       Strings in packet payloads, searching for, 491–495
SCSI (small computer system interface), 21, 22, 128,      Structure, 4
             129                                          Substitution error, 495
Security forensics problem, 55, 56                        Switch pointers, 309, 310
Security issues, see Intrusion detection systems (IDSs)   Switching (switches), 37
select(), 521                                                Benes networks, 370–375
   analysis of, 162, 163                                     bit slicing, 375, 376
   server performance problem, 159, 160                      Clos networks, 365, 366
   speeding up by changing API, 164, 165                     costs, 332
   speeding up without changing API, 163, 164                crossbar scheduler, 337–340
   use and implementation of, 160–162                        flow, 256, 257
SERENA, 353, 354, 356                                        head-of-line blocking, 340–342
Server, event-driven, 157                                    iSLIP, 347–352
Service differentiation, 6                                   memory scaling, 377, 378
Set-pruning tries, 305–307                                   multi-protocol-label, 38, 257, 258, 303
Shape data structure, 409                                    optical, 39
Shared memory, 120, 131, 334                                 output queuing, 342, 343
Shelley, Bob, 241                                            parallel iterative matching (PIM), 344–347

                                                                                            Index        567



  router, 335, 336                                       Timing Wheels, see Timers, wheels
  router versus telephone, 333, 334                      Token bucket shaping and policing, 390, 391
  scaling, 363–365                                       Tomography, 473
  shared-memory, 334                                     Traceback
  short links, 375–377                                     logging, 499–504
  theory, 539                                              probabilistic marking, 497–499
  threaded indices and tag, 14, 255–257                  Traceroute, 475
System calls, 44, 147, 148                               Tracking of GPS clock, 401
  avoiding, 166–171                                      Trading memory for processing, 13
Systems principles                                       Traffic matrices, 472–474
  leverage off system components, 60, 61                 Traffic patterns, monitoring, 92–94, see also
  performance improved by hardware, 61, 62                           Measuring network traffic
  relaxing requirements, 59, 60                          Trajectory sampling, 470
  time and space computation, 58, 59                     Transistors, 533–535
  waste, avoiding, 58                                    Translation look-aside buffer (TLB), 43, 118, 119
                                                         Transmission Control Protocol (TCP), 18
T                                                        Transmission speed, 23, 24
Tag switching, 14, 255–257                               Transport-arm-to-send, 149
Take-a-ticket scheme, 337–340                            Transport-get-port, 150
Task-based structuring, 158, 159                         Tree bitmaps, 271–274
TCP congestion control, 386                              Tries, 492
TCP/IP (Transmission Control Protocol/Internet             defined, 204
           Protocol), 18, 21, 113, 120, 121, 148, 152,     extended grid of, 315
           200                                             fixed-stride, 262, 263
tcpdump, 21                                                grid of, 295, 305, 308, 310
Teardrop attack, 499                                       level-compressed, 267, 268
Telephone switches                                         Lulea-compressed, 268–271
  Clos networks, 367                                       multibit, 262–267
  router versus, 333, 334                                  node compression and, 85–87
Thomas, Bob, 242                                           Patricia, 14, 261
Threads, 41                                                set-pruning, 305–307
  indices and tag switching, 255–257                       unibit, 259–262
  per client, 155                                          variable-stride, 263–266
Threshold aggregation, 464–466                           Tuple space search (TSS), 296, 301
Throughput, 20
  memory, 28                                             U
Timers, 5, 18, 20                                        UDP (User Datagram Protocol), 18, 226, 227
  BSD UNIX implementation, 189, 190                      ufalloc(), 160, 176
  delays, 534                                            Unibit tries, 259–262
  fine granularity, 191, 192                             UNIX mbufs, 122, 212, see also BSD UNIX
  Google Carousel implementation, 190, 191               Upcalls, 150, 151
  hashed wheels, 185, 186                                Updates, asynchronous, 441–443
  hierarchical wheels, 187, 188                          User processes, 41
  reasons for, 180, 181                                  User-level implementation, 151–153
  routines and performance of, 181
  simple, 182, 183                                       V
  wheels, 183–185                                        Valid crossbar schedule, 344

568        Index



Variable-stride tries, 263–266                         task-based structuring, 158, 159
VAX cluster, 126–128                                   thread per client, 155
Video conferencing, asynchronous transfer mode and,   Weighted fair queuing (WFQ), 400–402, 405, 407,
            105–107                                             408, 418
Virtual circuit (VC), 78, 79, 105, 125                Wheels, see Timers
Virtual interface architecture (VIA), 169             Wire-speed forwarding, 14, 238–242
Virtual memory, 42, 43, 117–119                       Work-conserving schemes, 391
Virtual output queue (VOQ), 331, 344, 345             Worms, detecting, 504–506
                                                      Worst-case fair weighed fair queueing, 408
W
WAN (wide area network), 160                          X
Waters, Greg, 245                                     x-kernel, demultiplexing in, 84, 85
Web servers                                           Xerox, 237
  context-switching control overhead, 153–159         XTP protocol, 224
  event-driven scheduler, 155
  event-driven server, 157                            Z
  process per client, 154, 155                        Zeus server, 157
