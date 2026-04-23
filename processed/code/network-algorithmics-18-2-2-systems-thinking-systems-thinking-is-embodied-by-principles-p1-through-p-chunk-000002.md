# network-algorithmics-18-2-2-systems-thinking-systems-thinking-is-embodied-by-principles-p1-through-p (chunk 000002)

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
