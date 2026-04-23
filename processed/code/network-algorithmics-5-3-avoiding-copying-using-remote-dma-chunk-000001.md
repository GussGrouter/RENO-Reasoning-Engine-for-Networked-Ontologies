# network-algorithmics-5-3-avoiding-copying-using-remote-dma (chunk 000001)

# Network Algorithmics — 5.3 Avoiding copying using remote DMA (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 153
- Slice: from `5.3 Avoiding copying using remote DMA` up to next detected section heading

---

5.3 Avoiding copying using remote DMA
While fbufs provide a reasonable solution to the problem of avoiding redundant application-to-kernel
copies, there is a more direct solution that also removes an enormous amount of control overhead.
Normally, if a 1-MB file is transferred between two workstations on an Ethernet, the file is chopped up
into 1460-byte pieces. The CPU is involved in processing each of these 1460-byte pieces to do TCP
processing and copying each packet (possibly via a zero-copy interface such as fbufs) to application
memory.
    On the other hand, recall from Chapter 2 how a CPU orchestrates a DMA operation between, say,
disk and memory for, say, a 1-MB transfer. The CPU sets up the DMA, tells the disk the range of
addresses into which the data must be written, and goes about its business. One megabyte of data later,
the disk interrupts the CPU to essentially say, “Master, your job is done.” Note that the CPU does
not micromanage every piece of this transfer, unlike in the earlier case of the corresponding network
transfer.
    This analogy suggests the vision of doing DMA across the network, or RDMA as it is sometimes
called. In fact, it is hardly surprising that this networking feature was first proposed in VAX Clusters
by a group of computer architects (Kronenberg et al., 1986). It is said that breakthroughs often come
via outsiders to an area. There is an apocryphal story about how one of the inventors of VAX Clusters
came to the networking people at DEC and asked to learn about networking. They laughed at him and

5.3 Avoiding copying using remote DMA                  127

gave him a copy of the standard undergraduate text at that time. He came back 6 months later with the
RDMA design.
    The intent is that data should be transferred between two memories in two computers across the
network without per-packet mediation by the two CPUs. Instead, the two adaptors conspire to read from
one memory and to write to the other: DMA across the network. To realize this vision two problems
must be solved: (1) how the receiving adaptor knows where to place the data—it cannot ask the host
for help without defeating the intent; (2) how security is maintained. The possibility of rogue packets
coming over the network and overwriting key pieces of memory should make one pause.
    This section starts by describing this very early idea and then moves on to describe modern incar-
nations of this idea in the Fibre Channel, Infiniband and iSCSI proposals.
