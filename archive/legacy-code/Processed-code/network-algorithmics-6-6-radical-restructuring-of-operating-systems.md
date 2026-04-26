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



al., 2017); thus it is important to keep resources and cores fully utilized. Finally, most cloud vendors
employ an army of programmers to work on different networking features; hence, it is important to
create an environment in which new code can be rapidly debugged and deployed.
     Of the approaches we survey, perhaps the least radical is Google’s Snap (Marty et al., 2019). How-
ever, it is the most widely used as it is deployed widely in a large fraction of Google’s fleet of servers.
Snap advocates a microkernel approach like Mach (Rashid et al., 1989) where the networking code is
pulled into a separate user level thread as opposed to a library called by the application thread. This
approach, which was deprecated earlier, is now becoming much more feasible because of the avail-
ability of multiple cores and cheap inter-thread communication. In return for potential inter-thread IPC
overhead, Snap decouples the release of networking code from application code, which are intertwined
in library OS methods like DPDK. It also decouples networking code from kernel updates which are
interwoven in classical network stacks like Linux (Cai et al., 2021). Further, Snap provides more cen-
tral allocation of networking resources (as in a classical operating system like Linux) compared to
library OS methods like DPDK; this helps improve core utilization. Snap allows several scheduling
modes (Marty et al., 2019) including one that can dedicate cores for achieving better latency (as in
DPDK), and also modes where load is balanced among cores to improve CPU utilization. Snap, how-
ever, is not optimal in reducing tail latency.
     Next, ZygOS (Prekas et al., 2017) observes like Snap that data plane operating systems like Ar-
rakis (Peter et al., 2015) and IX (Belay et al., 2016) reduce latency by avoiding shared processing
of flows, but cannot handle load imbalances across cores. ZygOS addresses work imbalance by work
stealing in which idle cores steal work from overloaded cores. On the other hand, Shenango (Ouster-
hout et al., 2019) uses a dedicated core to detect core congestion at microsecond time scales to do more
fine grained core rebalancing across applications, as opposed to the balancing of load within an appli-
cation across cores done in ZygOS. Finally, even more radical are proposals like Homa (Montazeri et
al., 2018) that advocate completely changing the transport to reduce tail latency even further by even
tackling network congestion at the edge. This is done by having the receiving transport protocol control
priority queues (P10) in the network. The jury is still out, in terms of impact, on each of these proposals,
with the exception of Snap which is widely deployed in Google (Marty et al., 2019).
