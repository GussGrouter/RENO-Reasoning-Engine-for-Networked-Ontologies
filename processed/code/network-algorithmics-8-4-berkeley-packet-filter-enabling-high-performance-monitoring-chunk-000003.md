# network-algorithmics-8-4-berkeley-packet-filter-enabling-high-performance-monitoring (chunk 000003)

8.5 Pathfinder: factoring out common checks                     201

FIGURE 8.3
The BPF uses a state machine or CFG as its underlying model, which enables it to avoid redundant comparisons
when compared to Fig. 8.2.

BPF is active, BPF is first called. BPF checks the packet against each currently specified user filter. For
each matching filter, BPF copies as many bytes as are specified by the filter to a per-filter buffer. Notice
that multiple BPF applications can cause multiple copies of the same packet to be buffered. The figure
also shows another common BPF application besides tcpdump, the reverse ARP demon (rarpd).
    There are two small features of BPF that are also important for high performance. First, BPF filters
packets before buffering, which avoids unnecessary waste (P1) when most of the received packets
are not wanted by BPF’s applications. The waste is not just memory for buffers but also for the time
required to do a copy (Chapter 5).
    Second, since packets can arrive very fast and the read() system call is quite slow, BPF allows batch
processing (P2c) and allows multiple packets to be returned to the monitoring application in one call. To
handle this and yet allow packet boundaries to be distinguished, BPF adds a header to each packet that
includes a timestamp and length. Users of tcpdump do not have to use this interface; instead, tcpdump
offers a more user-friendly interface: interface commands are compiled to BPF instructions.
