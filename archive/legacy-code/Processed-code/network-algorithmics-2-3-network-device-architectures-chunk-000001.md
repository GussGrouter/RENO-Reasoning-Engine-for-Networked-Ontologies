# network-algorithmics-2-3-network-device-architectures (chunk 000001)

# Network Algorithmics — 2.3 Network device architectures (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 60
- Slice: from `2.3 Network device architectures` up to next detected section heading

---

2.3 Network device architectures
Optimizing network performance requires optimizing the path of data through the internals of the
source node, the sink node, and every router. Thus it is important to understand the internal archi-
tecture of endnodes and routers. The earlier part of this chapter argued that logic and memory can
be combined to form state machines. In essence, both routers and endnodes are state machines. How-
ever, their architectures are optimized for different purposes: endnode architectures (Section 2.3.1) for
general computation and router architectures (Section 2.3.2) for Internet communication.
