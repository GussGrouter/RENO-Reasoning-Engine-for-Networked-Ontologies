# Network Algorithmics — 13.4 The take-a-ticket crossbar scheduler (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 364
- Slice: from `13.4 The take-a-ticket crossbar scheduler` up to next detected section heading

---

13.4 The take-a-ticket crossbar scheduler
The simplest crossbar is an array of N input buses and N output buses, as shown in Fig. 13.3. Thus
if line card R wishes to send data to line card S, input bus R must be connected to output bus S. The
simplest way to make this connection is via a “pass” transistor, as shown in Fig. 13.4. For every pair
of input and output buses, such as R and S, there is a transistor that when turned on connects the two
buses. Such a connection is known as a crosspoint. Notice that a crossbar with N inputs and N outputs
has N 2 crosspoints, each of which needs a control line from the scheduler to turn it on or off.
     While N 2 crosspoints seem large, easy VLSI implementation via transistors makes pin counts, card
connector technologies, etc., still more limiting factors in building large switches. Thus most routers
and switches built before 2002 use simple crossbar-switch backplanes to support 16–32 ports. Notice
that multicast is trivially achieved by connecting input bus R to all the output buses that wish to receive
from R. However, scheduling multicast is tricky.
     In practice, only older crossbar designs use pass transistors. This is because the overall capacitance
(Chapter 2) grows very large as the number of ports increases. This in turn increases the delay to send a
signal, which becomes an issue at higher speeds. Modern implementations often use large multiplexer
trees per output or tristate buffers (Alleyne, 2002; Turner, 2002). Higher-performance systems even
pipeline the data flowing through the crossbar using some memory (i.e., a gate) at the crosspoints.
     Thus the design of a modern crossbar switch is actually quite tricky and requires careful attention to
physical-layer considerations. However, crossbar-design issues will be ignored in this chapter to con-
centrate on the algorithmic issues related to switch scheduling. But, what should scheduling guarantee?
     For correctness, the control logic must ensure that every output bus is connected to at most one
input bus (to prevent inputs from mixing). However, for performance, the logic must also maximize the
number of line-card pairs that communicate in parallel. While the ideal parallelism is achieved if all
N output buses are busy at the same time, in practice parallelism is limited by two factors. First, there
may be no data for certain output line cards. Second, two or more input line cards may wish to send
data to the same output line card. Since only one input can win at a time, this limits data throughput if
the other “losing” input cannot send data.

338       Chapter 13 Switching




FIGURE 13.4
Connecting input from Line Card R to Line Card S by turning the pass transistor connecting the two buses. Modern
crossbars replace this simplistic design by multiplexer trees to reduce capacitance.


     Thus despite extensive parallelism, the major contention occurs at the output port. How can con-
tention for output ports be resolved while maximizing parallelism? A simple and elegant scheduling
scheme for this purpose was first invented and used in DEC’s GigaSwitch. An example of the operation
of the so-called “take-a-ticket” algorithm (Souza et al., 1994) used there is given in Fig. 13.5.
     The basic idea is that each output line card S essentially maintains a distributed queue for all input
line cards R waiting to send to S. The queue for S is actually stored at the input line card itself (instead
of being at S) using a simple ticket number mechanism like that at some deli counters. If line card
R wants to send a packet to line card S, it first makes a request over a separate control bus to S; S
then provides a queue number back to R over the control bus. The queue number is the number of R’s
position in the output queue for S.
     R then monitors the control bus; whenever S finishes accepting a new packet, S sends the current
queue number it is serving on the control bus. When R notices that its number is being “served,” R
places its packet on the input data bus for R. At the same time, S ensures that the R–S crosspoint is
turned on.
     To see this algorithm in action, consider Fig. 13.5, where, on the top frame, input line card A has
three packets destined to outputs 1, 2, and 3, respectively. B has three similar packets destined for the
same outputs, while C has packets destined for outputs 1, 3, and 4. Assume the packets have the same
size in this example (though this is not necessary for the take-a-ticket algorithm to work).
     Each input port works only on the packet at the head of its queue. Thus the algorithm begins with
each input sending a request, via a control bus, to the output port for which the packet at the head of its
input queue is destined. Thus in the example each input sends a request to output port 1 for permission
to send a packet.
     In general, a ticket number is a small integer that wraps around and is given out in order of arrival,
as in a deli. In this case assume that A’s request arrived first on the serial control bus, followed by
B, followed by C, though the top left diagram makes it appear that the requests are sent concurrently.
Since output port 1 can service only one packet at a time, it serializes the requests, returning T 1 to A,
T 2 to B, and T 3 to C.
     Thus in the middle diagram of the top row, output port 1 also broadcasts the current ticket number
it is serving (T 1) on another control bus. When A sees it has a matching number for input 1, in the
diagram on the top right, A then connects its input bus to the output bus of 1 and sends its packet on

                                                      13.4 The take-a-ticket crossbar scheduler                           339




FIGURE 13.5
In the take-a-ticket scheduling mechanism all input ports have a single input queue that is labeled with the output
port number for which each packet is destined. Thus on the top frame, inputs A, B, and C send requests to output
port 1. Output port 1 (top, middle) gives the first number to A, the second to B, etc., and these numbers are used to
serialize access to output ports.


its input bus. Thus by the end of the topmost row of diagrams, A has sent the packet at the head of its
input queue to output port 1. Unfortunately, all the other input ports, B and C, are stuck waiting to get
a matching ticket number from output port 1.
     The second row in Fig. 13.5 starts with A sending a request for the packet that is now at the head of
its queue to output port 2; A is returned a ticket number, T 1, for port 2.1 In the middle diagram of the
second row port 1 announces that it is ready for T 2, and port 2 announces it is ready for ticket T 1. This
result is in the rightmost diagram of the second row, where A is connected to port 2 and B is connected
to port 1, and the corresponding packets are transferred.
     The third row of diagrams in Fig. 13.5 starts similarly with A and B sending a request for ports 3
and 2, respectively. Note that poor C is still stuck waiting for its ticket number, T 3, which it obtained
two iterations ago, to be announced by output port 1. Thus C makes no more requests until the packet
at the head of its queue is served. A is returned T 1 for port 3, and B is returned T 2 for port 2. Then


1 Although not shown in the pictures, a ticket should really be considered a pair of numbers, a ticket number and the output port
number, so the same ticket number used at different output ports should cause no confusion at input ports.

340      Chapter 13 Switching



port 1 broadcasts T 3 (finally!), port 2 broadcasts T 2, and port 3 broadcasts T 1. This results in the final
diagram of the third row, where the crossbar connects A and 3, B and 2, and C and 1.
     The take-a-ticket scheme scales well in the control state, requiring only two (log2 N )-bit counters
at each output port to store the current ticket number being served and the highest ticket number dis-
pensed. This allowed the implementation in DEC’s GigaSwitch to scale easily to 36 ports (Souza et
al., 1994), even in the early 1990s when on-chip memory was limited. The scheme used a distributed
scheduler, with each output port’s arbitration done by a so-called GPI chip per line card; the GPI chips
communicate via a control bus.
     The GPI chips have to arbitrate for the (serial) control bus so as to present a request to an output line
card and to obtain a queue number. Because the control bus is a broadcast bus, an input port can figure
out when its turn comes by observing the service of those who were before it, and it can then instruct
the crossbar to make a connection.
     Besides the small control state, the take-a-ticket scheme has the advantage of being able to handle
variable-sized packets directly. Output ports can asynchronously broadcast the next ticket number when
they finish receiving the current packet; different output ports can broadcast their current ticket numbers
at arbitrary times. Thus unlike all the other schemes described later, there is no header and control
overhead to break up packets into “cells” and then do the reassembly later. On the other hand, take-a-
ticket has limited parallelism because of HOL blocking, a phenomenon we look at in the next section.
     The take-a-ticket scheme also allows a nice feature called hunt groups. Any set of line cards (not
just physically contiguous line cards) can be aggregated to form an effectively higher-bandwidth link
called a hunt group. Thus three 100-Mbps links can be aggregated to look like a 300-Mbps link.
     The hunt group idea requires only small modifications to the original scheduling algorithm because
each of the GPI chips in the group can observe each other’s messages on the control bus and thus keep
local copies of the (common) ticket number consistent. The next packet destined for the group is served
by the first free output port in the hunt group, much as in a delicatessen with multiple servers. While
basic hunt groups can cause reordering of packets sent to different links, a small modification allows
packets from one input to be sent to only one output port in a hunt group via a simple deterministic
hash. This modification avoids reordering, at the cost of reduced parallelism.
     Since the GigaSwitch was a bridge, it had to handle LAN multicast. Because the take-a-ticket
scheduling mechanism uses distributed scheduling via separate GPI chips per output, it is hard to coor-
dinate all schedulers to ensure that every output port is free. Furthermore, waiting for all ports to have
a free ticket for a multicast packet would result in blocking some ports that were ready to service the
packet early, wasting throughput. Hence, multicast was handled by a central processor in software and
was thus accorded “second-class” status.
