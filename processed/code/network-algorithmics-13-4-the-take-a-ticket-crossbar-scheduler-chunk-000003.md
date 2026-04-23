# network-algorithmics-13-4-the-take-a-ticket-crossbar-scheduler (chunk 000003)

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
