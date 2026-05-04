# Network Algorithmics — 2.1.1 Transport and routing protocols (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 45
- Slice: from `2.1.1 Transport and routing protocols` up to next detected section heading

---

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
