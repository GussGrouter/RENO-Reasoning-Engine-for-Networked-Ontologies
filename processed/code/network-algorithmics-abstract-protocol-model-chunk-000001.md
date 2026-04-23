# Chunk 000001

- Source: raw/code/pdf/Network.Algorithmics.pdf
- PDF pages: 45–46
- From: processed/code/network-algorithmics-abstract-protocol-model-p45-47.md

---

18       Chapter 2 Network implementation models

2.1 Protocols
Section 2.1.1 describes the transport protocol TCP and the IP routing protocol. These two examples are
used to provide an abstract model of a protocol and its functions in Section 2.1.2. Section 2.1.3 ends
with common network performance assumptions. Readers familiar with TCP/IP may wish to skip to
Section 2.1.2.

2.1.1 Transport and routing protocols
Applications subcontract the job of reliable delivery to a transport protocol such as the Transmission
Control Protocol (TCP). TCP’s job is to provide the sending and receiving applications with the illusion
of two shared data queues in each direction—despite the fact that the sender and receiver machines
are separated by a lossy network. Thus whatever the sender application writes to its local TCP send
queue should magically appear in the same order at the local TCP receive queue at the receiver, and
vice versa. TCP implements this mechanism by breaking the queued application data into segments
and retransmitting each segment until an acknowledgment (ack) has been received. A more detailed
description of TCP operation can be found in Section A.1.1.
    If the application is (say) a videoconferencing application that does not want reliability guarantees,
it can choose to use a protocol called UDP (User Datagram Protocol) instead of TCP. Unlike TCP, UDP
does not need acks or retransmissions because it does not guarantee reliability.
    Transport protocols such as TCP and UDP work by sending segments from a sender node to a
receiver node across the Internet. The actual job of sending a segment is subcontracted to the Internet
routing protocol IP.
    Internet routing is broken into two conceptual parts, called forwarding and routing. Forwarding is
the process by which packets move from source to destination through intermediate routers. A packet
is a TCP segment together with a routing header that contains the destination Internet address.
    While forwarding must be done at extremely high speeds, the forwarding tables at each router must
be built by a routing protocol, especially in the face of topology changes, such as link failures. There are
several commonly used routing protocols, such as distance vector (e.g., RIP), link state (e.g., OSPF),
and policy routing (e.g., BGP). More details and references to other texts can be found in Section A.1.2
in Appendix.

2.1.2 Abstract protocol model
A protocol is a state machine for all nodes participating in the protocol, together with interfaces and
message formats. A model for a protocol state machine is shown in Fig. 2.1. The specification must
describe how the state machine changes state and responds (e.g., by sending messages, setting timers)
to interface calls, received messages, and timer events.
    For instance, when an application makes a connect request, the TCP sender state machine initializes
by picking an unused initial sequence number, goes to the so-called SYN-SENT state, and sends a
SYN message. As a second example, a link-state routing protocol like OSPF has a state machine at
each router; when a link state packet (LSP) arrives at a router with a higher sequence number than the
last LSP from the source, the new LSP should be stored and sent to all neighbors. While the LSP is very
different from TCP, both protocols can be abstracted by the state machine model shown in Fig. 2.1.

---

2.1 Protocols            19

FIGURE 2.1
Abstract model of the state machine implementing a protocol at a node participating in a protocol.

FIGURE 2.2
Common protocol functions. The small shaded black box to the lower left represents the state table used by the
protocol.
