# network-algorithmics-8-5-pathfinder-factoring-out-common-checks (chunk 000004)

8.6 Dynamic packet filter: compilers to the rescue                205

Although Pathfinder has been described so far as a tree, the data structure can be generalized to
a directed acyclic graph (DAG). A DAG allows two different filters to initially follow different paths
through the Pathfinder graph and yet come together to share a common path suffix. This can be useful,
for instance, when providing a filter for TCP packets for destination port 80 that can be fragmented
or unfragmented. While one needs a separate path of cells to specify fragmented and unfragmented IP
packets, the two paths can point to a common set of TCP cells.
    Finally, Pathfinder also allows the use of OR links that lead from a cell. The idea is that each of the
OR links specify a value, and each of the OR links is checked to find a value that matches and then that
link is followed.
    In order to prioritize packets during periods of congestion, as in Chapter 6, the demultiplexing
routine must complete in the minimum time it takes to receive a packet. Software implementations of
Pathfinder are fast but are typically unable to keep up with line speeds. Fortunately, the Pathfinder state
machine can be implemented in hardware to run at line speeds. This is analogous to the way IP lookups
using tries can be made to work at line speeds (Chapter 11).
    The hardware prototype described in Bailey et al. (1994) trades functionality for speed. It works
in 16-bit chunks and implements only the most basic cell functions; it does, however, implement frag-
mentation in hardware. The limited functionality implies that the Pathfinder hardware can only be used
as a cache to speed up Pathfinder software that handles the less common cases. A prototype design
running at 100 MHz was projected to take 200 nanoseconds to process a 40-byte TCP message, which
is sufficient for 1.5 Gbps. The design can be scaled to higher wire speeds using faster clock rates, faster
memories, and a pipelined traversal of the state machine.
