# network-algorithmics-18-5-the-inner-life-of-a-networking-device (chunk 000010)

A.3.1 Matching algorithms for Clos networks with k = n
A Clos network can be proved to be rearrangably nonblocking for k = n. The proof uses Hall’s theorem
and the notion of perfect matchings. A bipartite graph is a special graph with two sets of nodes I and
O; edges are only between a node in I and a node in O. A perfect matching is a subset E of edges in
this graph such that every node in I is the endpoint of exactly one edge in E, and every node in O is
also the endpoint of exactly one edge in E. A perfect match marries every man in I to every woman
in O while respecting monogamy. Hall’s theorem states that a necessary and sufficient condition for a
perfect matching to exist is that every subset X of I of size d has at least d edges going to d distinct
nodes in O.
    To apply Hall’s theorem to prove the Clos network is nonblocking, we show that any arrangement
of N inputs that wish to go to N different outputs can be connected via the Clos network. Use the
following iterative algorithm. In each iteration match input switches (set I ) to output switches (set O)
after ignoring the middle switches. Draw an edge between an input switch i and an output switch o if
there is at least one input of i that wishes to send to an output directly reachable through o.
    Using this definition of an edge, here is Claim 1: every subset X of d input switches in I has edges
to at least d output switches in O. Suppose Claim 1 were false. Then the total number of outputs desired
by all inputs in X would be strictly less than nd (because each edge to an output switch can correspond
to at most n outputs). But this cannot be so, because d input switches with n inputs each must require
exactly nd outputs.
    Claim 1 and Hall’s theorem can be used to conclude that there is a perfect matching between input
switches and output switches. Hence the algorithm is to perform this matching after placing back exactly
one middle switch M. This is possible because every middle switch has a link to every input switch and
a link to every output switch. This allows routing one input link in every input switch to one output link
in every switch. It also makes unavailable all the n links from each input switch to the middle switch
M and all output links from M.
    Thus the problem has been reduced from having to route n inputs on each input switch using n
middle switches to having to route n − 1 inputs per input switch using n − 1 middle switches. Thus n
iterations are sufficient to route all inputs to all outputs without causing resource conflicts that lead to
blocking.
    Thus a simple version of this algorithm would take n perfect matches; using the best existing al-
gorithm for perfect matching (Hopcroft and Karp, 1973) takes O(N 2.5 /n1.5 ) time. A faster approach
is via edge coloring; each middle switch is assigned a color, and we color the edges of the demand
multigraph between input switches and output switches so that no two edges coming out of a node have
the same color.3 However, edge coloring can be done directly (without n iterations as before) in around
O(N log N ) time (Cole and Hopcroft, 1982).

3 Intuitively, each set of edges colored with a single color corresponds to one matching and one middle switch, as in our first
algorithm.

540      Detailed models
