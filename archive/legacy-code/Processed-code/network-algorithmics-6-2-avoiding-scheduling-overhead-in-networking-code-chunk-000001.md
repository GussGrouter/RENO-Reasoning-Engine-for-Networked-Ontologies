# network-algorithmics-6-2-avoiding-scheduling-overhead-in-networking-code (chunk 000001)

# Network Algorithmics — 6.2 Avoiding scheduling overhead in networking code (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 176
- Slice: from `6.2 Avoiding scheduling overhead in networking code` up to next detected section heading

---

6.2 Avoiding scheduling overhead in networking code
One of the major difficulties with implementing a protocol is to balance modularity (so you implement
a big system in pieces and get each piece right, independent of the others) and performance (so you
can get the overall system to perform well). As a simple example, consider how one might implement a
networking stack. The “obvious modularity” would be to implement the transport protocol (e.g., TCP)
as a process, the routing protocol (e.g., IP) as a process, and the applications as a separate process. If
that were the case, however, every received packet would take at least two process-context switches,
which are expensive. There are, however, a number of creative alternatives that allow modularity as
well as efficiency. These were first pointed out by Dave Clark in a series of papers.
    Fig. 6.2 provides an example that Clark (1985) used to illustrate his ideas. It consists of a simple
application that reads data from a keyboard and sends it to the network using a reliable transport proto-
col. When the data is received by some receiver on the network, the data is displayed on the screen. The
vertical slices show the various protocol layers, with the topmost slice (routines such as display-get-data
and display-receive) being the application protocol, the second slice (routines such as transport-receive
and transport-send) being the transport protocol, and the bottom slice (routines such as net-receive and
net-dispatch) being the network protocol. The naive way to implement this protocol would be to have a
process per slice, which would involve three processes and two full-scale context switches per received
or sent packet.
    Instead, Clark suggests using only two processes, each at the sender and two processes at the re-
ceiver (shown as boxed vertical sections), to implement the network protocol stack. In Fig. 6.2 the
leftmost two sections correspond to receiver processes and the rightmost two sections correspond to
sender processes. Thus the sender has a Keyboard Handler process that gathers data coming in from the
keyboard and calls transport-arm-to-send when it has got some data. Notice that transport-arm-to-send
is a transport-layer function that is exported to the Keyboard Handler process and is executed by the
Keyboard Handler process. At this point the Keyboard Handler can suspend itself (a context switch).
Transport-arm-to-send only tells the transport protocol that this connection wishes to send data; it does
not transfer data.

150       Chapter 6 Transferring control

FIGURE 6.2
Implementing a protocol using upcalls.
