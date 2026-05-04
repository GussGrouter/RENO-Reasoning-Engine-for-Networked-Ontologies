# network-algorithmics-6-6-radical-restructuring-of-operating-systems (chunk 000002)

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
