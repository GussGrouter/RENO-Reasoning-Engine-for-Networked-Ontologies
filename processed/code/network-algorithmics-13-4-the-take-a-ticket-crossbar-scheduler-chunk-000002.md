# network-algorithmics-13-4-the-take-a-ticket-crossbar-scheduler (chunk 000002)

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
