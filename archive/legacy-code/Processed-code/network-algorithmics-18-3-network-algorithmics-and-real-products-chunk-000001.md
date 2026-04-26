# network-algorithmics-18-3-network-algorithmics-and-real-products (chunk 000001)

# Network Algorithmics — 18.3 Network algorithmics and real products (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 551
- Slice: from `18.3 Network algorithmics and real products` up to next detected section heading

---

18.3 Network algorithmics and real products
Many of the algorithms used in this book are found in real products. The following is a quick survey.
  Endnode Algorithmics: Zero-copy implementations of network stacks are now quite common (sendmsg,
2022), as are implementations of memory-mapped files; however, more drastic changes, such as
IO-Lite are still not in commodity operating systems. The RDMA specification has developed con-
siderably since the first edition. For instance, RDMA is now implemented over commodity Ethernet
in ROCE (Guo et al., 2016). Event-driven Web servers are quite common, and many operating sys-
tems other than UNIX (such as Windows NT) have fast implementations of select() equivalents. The
DPDK standard (DPDK, 2018) avoids system calls and copies using ideas similar to ADCs. Google’s
Carousel (Saeed et al., 2017) uses timing wheels to schedule packets.
Most commercial systems for early demultiplexing still rely on BPF (Berkeley packet filter) (Engler
and Kaashoek, 1996), but that is because few systems require so many classifiers that they need the
scalability of a Pathfinder or a DPF (dynamic packet filter). Some operating systems use timing wheels,
notably Linux and FreeBSD. Linux uses fast buffer-manipulation operations on linear buffers. Fast IP
checksum algorithms are common, and so are multibit CRC algorithms in hardware.
  Router Algorithmics: Binary search lookup algorithms for bridges were common in products, as were
hashing schemes (e.g., Gigaswitch). Multibit trie algorithms for IP lookups are very common; recently,
compressed versions, such as the tree bitmap algorithm, have become popular in Cisco’s latest CRS-1
router. Classification is often done by CAMs, but Virtual Switches like Open vSwitch (Pfaff et al., 2015)
use tuple search and Hypercuts was used in the Cisco CRS-1 router Chapter 12. Distributed memory
ideas (Sundar et al., 2008) that combine SRAM and DRAM cleverly to build router buffers are used in
Cisco routers.
In some chapters, such as the chapter on switching (Chapter 13), we provided a real product exam-
ple for every switching scheme (see Table 13.1, for example) described in the first edition. In the
second edition, we have added a few switching schemes that are of pedagogical importance, such as
Sample-and-compare (Section 13.12), SERENA (Section 13.13), QPS (Section 13.14), and SW-QPS
(Section 13.16.3); among them SW-QPS has been patented and may find adoption in future router
products due to its simple design and low complexities. In fair queuing DRR, RED, AFD and token
buckets are commonly implemented. General weighted fair queuing (WFQ), WF2 Q, virtual clock, and
core stateless fair queuing are hardly ever used except for an approximation called Quick Fair Queuing
(QFQ) that provides better delay bounds and is available in Linux. However, for pedagogical purpose,
we have added the materials describing how WFQ and WF2 Q can be implemented (in Sections 14.12
and 14.13) so that their time complexities are strictly O(log n) (still considered impractically high) in
the worse case.
   It is useful to see many of these ideas come together in a complete system. While it is hard to find
details of such systems (because of commercial secrecy), the following two large systems pull together
ideas in endnode and router algorithmics.

System Example 1: Flash Web server
The Flash (Pai et al., 1999a) Web server was designed at Rice University and undoubtedly served as
the inspiration (and initial code base) for a company called iMimic. A version of Flash called Flash-lite
uses the following ideas from endnode algorithmics.

18.4 Network algorithmics: back to the future             525
