# Network Algorithmics — 5.6 Broadening beyond data manipulations (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 164
- Slice: from `5.6 Broadening beyond data manipulations` up to next detected section heading

---

5.6 Broadening beyond data manipulations
So far this chapter has concentrated on reducing the memory (and bus) bandwidth caused by data-
manipulation operations. First, we concentrated on removing redundant data copying between the
network and the application. Second, we addressed redundant copying between the file system, the
application, and the network. Third, we looked at removing redundant memory reads and writes using
integrated layer processing when several data-manipulation operations operate over the same packet.
What is common to all these techniques is an attempt to reduce pressure on the memory and the I/O
bus by avoiding redundant reads and writes.
    But once this is done, there are still other sources of pressure that appear within an endnode archi-
tecture as shown in Fig. 5.1. This is alluded to in the following excerpt from e-mail sent after the alpha
release of a fast user-level Linux Web server (Riccardi, 2001):

   With zero-copy sendfile, data movement is not an issue anymore, asynchronous network IO allows
   for really inexpensive thread scheduling, and system call invocation adds a very negligible overhead
   in Linux. What we are left with now is purely wait cycles, the CPUs and the NICs are contending for
   memory and bus bandwidth.
   In essence once the first-order effects (such as eliminating copies) are taken care of, performance
can be improved only by paying attention to what might be thought of as second-order effects. The next
two subsections discuss two such architectural effects that greatly impact the use of bus and memory
bandwidth: the effective use of caches and the choice of DMA versus PIO.
