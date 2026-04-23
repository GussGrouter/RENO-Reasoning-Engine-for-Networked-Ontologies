# Network Algorithmics — 18.2.2 Systems thinking Systems thinking is embodied by Principles P1 through P10. Principles P1 through P5 were described (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 547
- Slice: from `18.2.2 Systems thinking Systems thinking is embodied by Principles P1 through P10. Principles P1 through P5 were described` up to next detected section heading

---

18.2.2 Systems thinking
Systems thinking is embodied by Principles P1 through P10. Principles P1 through P5 were described
earlier as systems principles. Systems unfold in space and time: in space, through various components
(e.g., kernel, application), and in time, through certain key time points (e.g., application initialization
time, packet arrival time). Principles P1 through P5 ask that a designer expand his or her vision to see
the entire system and then to consider moving functions in space and time to gain efficiency.
    For example, Principle P1, avoiding obvious waste, is a cliché by itself. However, our understanding
of systems, in terms of separable and modular hierarchies, often precludes the synoptic eye required to
see waste across system hierarchies. For example, the number of wasted copies is apparent only when
one broadens one’s view to that of a Web server (see I/O-Lite in Chapter 5). Similarly, the opportunities
for dynamic code generation in going from Pathfinder to DPF (see Chapter 8) are apparent only when
one considers the code required to implement a generic classifier.
    Similarly, Principle P4 asks the designer to be aware of existing system components that can be
leveraged. Fbufs (Chapter 5) leverage off the virtual memory subsystem, while timing wheels (Chap-
ter 7) leverage off the existing time-of-day computation to amortize the overhead of stepping through
empty buckets. Principle P4 also asks the designer to be especially aware of the underlying hardware,
whether to exploit local access costs (e.g., DRAM pages, cache lines), to trade memory for speed (ei-
ther by compression, if the underlying memory is SRAM, or by expansion, if memory is DRAM), or to
exploit other hardware features (e.g., replacing multiplies by shifts in RED calculations in Chapter 14).
    Principle P5 asks the designer to be even bolder and to consider adding new hardware to the system;
this is especially useful in a router context. While this is somewhat vague, Principles 5a (parallelism via
memory interleaving), P5b (parallelism via wide words), and P5c (combining DRAM and SRAM to
improve overall speed and cost) appear to underlie many clever hardware designs to implement router
functions. Thus memory interleaving and pipelining can be used to speed up IP lookups (Chapter 11),
wide words are used to improve the speed of the Lucent classification scheme (Chapter 12), and DRAM
and SRAM can be combined to construct an efficient counter scheme (Chapter 16).
    Once the designer sees the system and identifies wasted sequences of operations together with possi-
ble components to leverage, the next step is to consider moving functions in time (P2) and space (P3c).
Fig. 18.4 shows examples of endnode algorithmic techniques that move functions between components.
Fig. 18.5 shows similar examples for router algorithmics.
    Besides moving functions in space, moving functions in time is a key enabler for efficient algo-
rithms. Besides the more conventional approaches of precomputation (P2a), lazy evaluation (P2b), and
batch processing (P2c), there are subtler examples of moving functions to different times at which
the system is instantiated. For example, in fbufs (Chapter 5), common VM mappings between the ap-
plication and kernel are calculated when the application first starts up. Application device channels
(Chapter 6) have the kernel authorize buffers (on behalf of an application) to the adaptor when the
application starts up. Dynamic packet filter (DPF) (Chapter 8) specializes code when a classifier is up-
dated. Tag switching (Chapter 11) moves the work of computing labels from packet-forwarding time to
route-computation time.

                                                  18.2 What network algorithmics is about         521




FIGURE 18.4
Endnode algorithmics: examples of moving functions in space.




FIGURE 18.5
Router algorithmics: examples of moving functions in space.



    Finally, Principles P6 through P10 concern the use of alternative system structuring techniques to
remove inefficiencies. P6 suggests considering specialized routines or alternative interfaces; for ex-
ample, Chapter 6 suggests that event-driven APIs may be more efficient than the state-based interface
of the select() call. P7 suggests designing interfaces to avoid unnecessary generality; for example, in
Chapter 5 fbufs map the fbuf pages into the same locations in all processes, avoiding the need for a
further mapping when moving between processes. P8 suggests avoiding being unduly influenced by
reference implementations; for example, in Chapter 9 naive reference implementations of checksums
have poor performance.
    Principles P9 and P10 suggest keeping existing interfaces but adding extra information to interfaces
(P9) or packet headers (P10). For example, efficiently reimplementing the select() call (Chapter 6)
requires passing information between the protocol module and the select module. Passing information
in packet headers, on the other hand, has a huge array of examples, including RDMA (Chapter 5),
MPLS (Chapter 11), DiffServ, and core stateless fair queuing (Chapter 14).

522      Chapter 18 Conclusions
