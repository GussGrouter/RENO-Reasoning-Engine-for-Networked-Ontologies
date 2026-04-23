# network-algorithmics-8-2-goals-if-early-demultiplexing-is-a-good-idea-is-it-easy-to-implement-ear (chunk 000001)

# Network Algorithmics — 8.2 Goals If early demultiplexing is a good idea, is it easy to implement? Early demultiplexing is particularly (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 225
- Slice: from `8.2 Goals If early demultiplexing is a good idea, is it easy to implement? Early demultiplexing is particularly` up to next detected section heading

---

8.2 Goals
If early demultiplexing is a good idea, is it easy to implement? Early demultiplexing is particularly
easy to implement if each packet carries some information in the outermost (e.g., data link or network)
header, which identifies the final endpoint. This is an example of P14, passing information in layer
headers. For example, if the network protocol is a virtual circuit protocol such as ATM, the ATM
virtual circuit identifier (VCI) can directly identify the final recipient of the packet.
    However, protocols such as IP do not offer such a convenience. MPLS (multi-protocol label switch-
ing) does offer this convenience, but MPLS is generally used only between routers, as described in
Chapter 11. Even using a protocol such as ATM, the number of available VCIs may be limited. In lieu
of a single demultiplexing field more complex data structures are needed that we call packet filters or
packet classifiers. Of course, as we have pointed out at the start, doing this just for TCP connections is
easy using a hash of the TCP 4-tuple but the more general solutions require better data structures.
    Such data structures take a complete packet header as input and map the input to an endpoint or
path. Intuitively, the endpoint of a packet represents the receiving application process, while the path
represents the sequence of protocols that need to be invoked in processing the packet prior to con-
sumption by the endpoint. Before describing how packet filters are built, here are the goals of a good
early-demultiplexing algorithm.
• Safety: Many early-demultiplexing algorithms are implemented in the kernel based on input from
  user-level programs. Each user program P specifies the packets it wishes to receive. As with Java
  programs, designers must ensure that incorrect or malicious users cannot affect other users. This is
  particularly important even today for traffic monitoring.
• Speed: Since demultiplexing is done in real time, the early-demultiplexing code should run quickly,
  particularly in the case where there is only a single filter specified.
• Composability: If N user programs specify packet filters that describe the packets they expect to
  receive, the implementation should ideally compose these N individual packet filters into a single
  composite packet filter. The composite filter should have the property that it is faster to search
  through the composite filter than to search each of the N filters individually, especially for large N .
   This chapter takes a mildly biological view, describing a series of packet filter species, with each
successive adaptation achieving more of the goals than the previous one. Not surprisingly, the earliest
species is nearly extinct, though it is noteworthy for its simplicity and historical interest.
