# network-algorithmics-6-6-radical-restructuring-of-operating-systems (chunk 000001)

# Network Algorithmics — 6.6 Radical Restructuring of Operating Systems (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 198
- Slice: from `6.6 Radical Restructuring of Operating Systems` up to next detected section heading

---

6.6 Radical Restructuring of Operating Systems
While we have already surveyed techniques like kernel bypass and the use of epoll() in Linux, these in-
volve fairly local restructuring of the operating system to lubricate the flow of packets. DPDK, for
instance, simply provides an interface for applications to safely bypass the kernel and epoll() is a
new Linux API for scalable event notification. Another local restructuring proposal is Megapipe (Han
et al., 2012) which suggests replacing the classic socket-based networking API with what they call
lightweight sockets that remove the file related overheads of the classic socket interface. The API also
allows for more aggressive batching to reduce (but not completely avoid) the cost of system calls.
     In this section, we briefly survey several proposals for more radical restructuring of operating sys-
tems even beyond Arrakis (Peter et al., 2015), that seeks to reduce overhead for all I/O. None of these
proposals except Google’s Snap (Marty et al., 2019) is, as far as we know, deployed widely, but the
ideas are stimulating. At the very least, they are helpful to understand the general issues, and may pro-
voke further thought even among implementors constrained by current Operating Systems. At the very
best, such operating systems may be needed in the immediate future as commodity operating systems
like Linux are already hard pressed to reach 100 Gbps per core (Cai et al., 2021), and certainly find it
hard to reduce say the 99-percentile latency of network operations to microseconds (Ousterhout, 2021)
for warehouse scale computing (Barroso et al., 2017).
     At the outset, it is worth clarifying what we hope to gain by radically restructuring operating systems
for better networking performance besides higher raw throughput. These are well articulated in Belay et
al. (2016). Besides throughput and protection which are already partly addressed by library OS methods
such as DPDK (2018), three additional goals for warehouse scale computing (Barroso et al., 2017) are
as follows. They seek to reduce the tail (often measure by 99th percentile) latency to microseconds,
strive for good utilization in the face of varying data center load, and enable rapid deployment of new
features.
     All three of these additional goals are motivated by warehouse style “scale out” computing described
in the chapter introduction, where multiple cheap commodity servers are used to serve a user request.
Since the request cannot complete until the slowest response is received, this explains the sensitivity
to tail latency. Further, as we have seen, the metric to improve is computation per dollar (Barroso et

172      Chapter 6 Transferring control
