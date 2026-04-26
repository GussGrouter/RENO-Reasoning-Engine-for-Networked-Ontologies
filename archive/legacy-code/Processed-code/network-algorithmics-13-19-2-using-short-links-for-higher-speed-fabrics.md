# Network Algorithmics — 13.19.2 Using short links for higher-speed fabrics (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 403
- Slice: from `13.19.2 Using short links for higher-speed fabrics` up to next detected section heading

---

13.19.2 Using short links for higher-speed fabrics
One feature of interconnection networks ignored so far is the physical length of the links used between
stages. Links come in various forms, from serial links between chips to backplane traces, to cable
connections between different line cards. Intuitively, the length matters because long wires increase
delay and decrease bit rate, unless compensated for using more expensive signaling technology, such
as optical signaling.
    A look at the Delta and Clos networks shows that these networks use at least a few long wires
between stages, whose length scales as O(N ). There are, however, interconnect networks that can be
packaged with uniformly short wires. These are the so-called low-dimensional mesh networks. Such
mesh networks have a checkered history in parallel computing, being used by Cray and Intel supercom-
puters.
    The simplest low-dimensional mesh is the 1D torus, which is basically a line of nodes in which the
last node is also connected to the first node to form a logical ring (Fig. 13.22). A 2D torus is basically a
two-dimensional grid of nodes where the last node in each row or column is also connected to the first
node in the same row or column. A 3D torus is the same idea extended to a three-dimensional grid.
    Even a 1D torus, which is logically a ring, appears to have one long wire that connects the first and
last nodes (Fig. 13.22). However, a clever way to amortize this long line length across all nodes is to
use a simple degree of freedom (P13) and to lay out the first half of the nodes on the forward path of the
ring (Fig. 13.22) and the second half on the reverse path. While the length of the A-to-B wire may have
doubled, there are no long wires. The same idea can be extended for 2D and 3D toruses by repeating
this idea across rows and columns.
    Like a Butterfly or Delta network, the problem with a 1D torus, however, is that it suffers from
congestion because there are only two paths between two inputs. It also suffers from high latency
because some pairs of nodes have to travel O(N/2) hops. The congestion and latency problems are
relieved by using a 3D torus. For example, in a 3D torus that is 8-by-8-by-8, an average message can
choose (Dally, 2002) between 90 paths of six hops each.
    The Avici TSR Router (Dally, 2002) is an example of a router built using a 3D torus. It can handle
up to 560 line cards, and the use of short wires allows it to be packaged very neatly. A 260-line-
card configuration can be packaged without any cables by connecting only adjacent backplanes using

                                                         13.19 Scaling to faster link speeds         377




FIGURE 13.22
How a 1D torus can be packaged physically using short wires.




jumpers. The 560-line-card version uses one set of short cables between two rows of racks (Dally,
2002).
   Besides the use of short links, the 3D mesh offers a large number of alternate paths for fault tolerance
and the ability to be incrementally upgraded with minimal extra cost. By contrast, some interconnection
networks tend to require scaling in powers of two.
