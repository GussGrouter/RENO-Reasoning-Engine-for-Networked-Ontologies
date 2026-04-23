# network-algorithmics-8-4-berkeley-packet-filter-enabling-high-performance-monitoring (chunk 000001)

# Network Algorithmics — 8.4 Berkeley packet filter: enabling high-performance monitoring (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 226
- Slice: from `8.4 Berkeley packet filter: enabling high-performance monitoring` up to next detected section heading

---

8.4 Berkeley packet filter: enabling high-performance monitoring
CSPF guarantees security by using instructions of limited power and by doing run-time bounds check-
ing on memory accesses. However, CSPF is not composable and has problems with speed. The next
mutation in the design of packet filters occurred with the introduction of the BPF (McCanne and Jacob-
son, 1993).
   The BPF designers were particularly interested in using BPF as a basis for high-performance
network-monitoring tools such as tcpdump, for which speed was crucial. They noted two speed prob-
lems with the use of even a single CSPF expression tree of the kind shown in Fig. 8.2.

200      Chapter 8 Demultiplexing
