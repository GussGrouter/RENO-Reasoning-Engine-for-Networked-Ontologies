# network-algorithmics-13-8-input-queued-switching-as-a-bipartite-matching-problem (chunk 000001)

# Network Algorithmics — 13.8 Input-queued switching as a bipartite matching problem (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 371
- Slice: from `13.8 Input-queued switching as a bipartite matching problem` up to next detected section heading

---

13.8 Input-queued switching as a bipartite matching problem
We can formulate the problem of scheduling a crossbar as a bipartite matching problem as follows. An
N × N input-queued crossbar can be modeled as a weighted complete bipartite graph, of which the two
disjoint vertex sets are the N input ports and the N output ports, respectively. In this bipartite graph
there is an edge between any input port i and any output port j , which corresponds to the VOQ at input
port i that buffers packets destined for output port j . The weight of this edge is defined as the length
of (i.e., the number of cells buffered at) this VOQ. A set of such edges constitutes a valid crossbar
schedule, or a matching, if any two of them do not share a common vertex. The weight of a matching
is the total weight of all the edges belonging to it (i.e., the total length of all corresponding VOQs).

13.8 Input-queued switching as a bipartite matching problem                             345

FIGURE 13.7
The parallel iterative matching (PIM) scheme works by having all inputs send requests in parallel to all outputs they
wish to reach. PIM then uses randomization to do fair matching such that outputs that receive multiple requests pick
a random input, and inputs that receive multiple grants randomly pick an output to send to. This three-round process
can then be iterated to improve the size of the matching.

Three types of matchings play important roles in crossbar scheduling problems: (1) maximal match-
ings; (2) maximum matchings; and (3) maximum weighted matchings (MWMs). A matching S is called
a maximal matching if it is no longer a matching when any edge that has nonzero weight and is
not in S is added to it. A matching with the largest possible number of edges of nonzero weights is
called a maximum matching or maximum cardinality matching. Neither maximal matchings nor maxi-
mum matchings take into account the weights of edges, whereas maximum weighted matchings do. A
maximum weighted matching is one that has the largest total weight among all matchings. In the switch-
ing context (where all edge weights are nonnegative) any maximum matching or maximum weighted
matching is also a maximal matching, but neither converse is generally true.
    Although crossbar scheduling using MWM (for every time slot) can provably guarantee 100%
throughput under all traffic patterns (McKeown et al., 1999; Tassiulas and Ephremides, 1992), and
empirically achieve very low queueing delays (McKeown et al., 1999), the state-of-the-art serial MWM
algorithm has a very high computational complexity of O(N 2.5 log W ) (Duan and Su, 2012), where W
is the maximum possible weight (length) of an edge (VOQ). By the same measure, maximum match-
ing is an even “rawer deal”: it has a slightly lower time complexity of O(N 2.5 ) (Hopcroft and Karp,

346      Chapter 13 Switching
