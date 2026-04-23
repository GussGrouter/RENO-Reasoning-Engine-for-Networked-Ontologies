# network-algorithmics-14-1-motivation-for-quality-of-service (chunk 000001)

# Network Algorithmics — 14.1 Motivation for quality of service (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 412
- Slice: from `14.1 Motivation for quality of service` up to next detected section heading

---

14.1 Motivation for quality of service
We will be assigning packets flows to queues and sometimes trying to give guarantees to flows. Though
we have used the term earlier, we repeat the definition of a packet flow. A flow is a stream of packets
that traverses the same route from the source to the destination and that requires the same grade of
service at each router or gateway in the path. In addition, a flow must be identifiable using fields in a
packet header; these fields are typically drawn from the transport, routing, and data link headers only.
    The notion of a flow is general and applies to datagram networks (e.g., IP, OSI) and virtual circuit
networks (e.g., X.25, ATM). For example, in a virtual circuit network a flow could be identified by a
virtual circuit identifier, or VCI. On the other hand, on the Internet a flow could be identified by all
packets (1) with a destination address that matches subnet A, (2) with a source address that matches
subnet B, and (3) that contain mail traffic, where mail traffic is identified by having either source or

386      Chapter 14 Scheduling packets

destination port numbers equal to 25. We assume that packet classification (Chapter 12) can be used to
efficiently identify flows.
    Why create complexity in going beyond FIFO with tail-drop? The following needs are arranged
roughly in order of importance:
• Router Support for Congestion: With link speeds barely catching up with exponentially increasing
  demand, it is often possible to have congestion on the Internet. Most traffic is based on TCP, which
  has mechanisms to react to congestion. However, with router support, it is possible to improve the
  reaction of TCP sources to congestion, improving the overall throughput of sources.
• Fair Sharing of Links Among Competing Flows: With tail-drop routers, customers have noticed
  that during a period of a backup across the network, important Telnet and e-mail connections freeze.
  This is because the backup packets grab all the buffers at an output in some router, locking out the
  other flows at that output link.
• Providing QoS Guarantees to Flows: A more precise form of fair sharing is to guarantee band-
  widths to a flow. For example, an ISP may wish to guarantee a customer 10 Mbps of bandwidth as
  part of a virtual private network connecting customer sites. A more difficult task is to guarantee the
  delay through a router for a flow such as a video flow. Live video will not work well if the network
  delay is not bounded.
   None of these needs should be surprising when one looks at a time-sharing operating system (OS),
such as UNIX or Windows NT. Clearly, in times of overload the OS must decide which load to shed; the
OS often time-shares among a group of competing jobs for fairness; finally, some OSs provide delay
guarantees for the scheduling of certain real-time jobs, such as playing a movie.
