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



• Architectural Mismatch: The CSPF stack model was invented for the PDP-11 and hence is a poor
  match to modern RISC architectures. First, the stack must be simulated at the price of an extra
  memory reference for each Boolean operation to update the stack pointer. Second, RISC architec-
  tures gain efficiency from storing variables in fast registers and doing computation directly from
  registers. Thus to gain efficiency in a RISC architecture, as many computations as possible should
  take place using a register value before it is reused. For instance, in Fig. 8.2, the CSPF model will
  result in two separate loads from memory for each reference to the Ethernet type field (to check
  equality with ARP and IP). On modern machines, it would be better to reduce memory references
  by storing the type field in a register and finishing all comparisons with the type field in one fell
  swoop.
• Inefficient Model: Even ignoring the extra memory references required by CSPF, the expression tree
  model often results in more operations than are strictly required. For example, in Fig. 8.2, notice
  that the CSPF expression takes four comparisons to evaluate all the leaves. However, notice that
  once we know that the Ethernet type is equal to ARP (if we are evaluating from left to right), then
  the extra check for whether the IP source address is equal to X is redundant (Principle P1, seek to
  avoid waste). The main problem is that in the expression tree model there is no way to “remember”
  packet parse state as the computation progresses. This can be fixed by a new model that builds a
  state machine.
    CSPF had two other minor problems. It could only parse fields at fixed offsets within packet head-
ers; thus it could not be used to access a TCP header encapsulated within an IP header because this
requires first parsing the IP header-length field. CSPF also processes headers using only 16-bit fields;
this doubles the number of operations required for 32-bit fields such as IP addresses.
    The BPF fixes these problems as follows. First, it replaces the stack-based language with a register-
based language, with an indirection operator that can help parse TCP headers. Fields at specified
packet offsets are loaded into registers using a command such as “LOAD [12],” which loads the
Ethernet type field, which happens to start at an offset of 12 bytes from the start of an Ethernet
packet.
    BPF can then do comparisons and jumps such as “JUMP_IF_EQUAL ETHERTYPE_IP, TAR-
GET1, TARGET2.” This instruction compares the accumulator register to the IP Ethernet type field; if
the comparison is true, the program jumps to line number TARGET1; otherwise, it jumps to TARGET2.
BPF allows working in 8-, 16-, and 32-bit chunks.
    More fundamentally, BPF uses a control flow graph (CFG) model of computation, as illustrated in
Fig. 8.3. This is basically a state machine starting with a root, whose state is updated at each node,
following which it transitions to other node states, shown as arcs to other nodes. The state machine
starts off by checking whether the Ethernet type field is that of IP; if true, it need only check whether
the IP source field is X to return true. If false, it needs to check whether the Ethernet type field is
ARP and whether the ARP source is X. Notice that in the left branch of the state machine we do not
check whether the IP source address is X. Thus the worst-case number of comparisons is 3 in Fig. 8.3,
compared to 4 in Fig. 8.2.
    The BPF is used as a basis for a number of tools, including the well-known tcpdump tool by which
users can obtain a readable transcript of TCP packets flowing on a link. BPF is embedded into the BSD
kernel as shown in Fig. 8.4.
    When a packet arrives on a network link, such as an Ethernet, the packet is processed by the appro-
priate link-level driver and is normally passed to the TCP/IP protocol stack for processing. However, if

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
