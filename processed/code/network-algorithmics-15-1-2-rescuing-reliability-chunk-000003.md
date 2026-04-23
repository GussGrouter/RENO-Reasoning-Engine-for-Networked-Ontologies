# network-algorithmics-15-1-2-rescuing-reliability (chunk 000003)

434       Chapter 15 Routers as distributed systems

FIGURE 15.2
Three steps to a marker algorithm.

In particular, the marker protocol makes the credit-update protocol self-stabilizing, i.e., it can re-
cover from arbitrary errors, including link errors, and also hardware errors that corrupt registers. This
is an extreme form of fault tolerance that can greatly improve the reliability of subsystems without
sacrificing performance.
    In summary, the general technique for a two-node system is to write down the protocol invariants and
then to design a periodic snapshot to verify and, if necessary, correct the invariants. Further techniques
for protocols that work on more than two nodes are described in Awerbuch et al. (1991); they are
based on decomposing, when possible, multinode protocols into two-node subsystems and repeating
the snapshot idea.

15.2 Internal Link Striping          435

An alternative technique for making a two-node credit protocol fault tolerant is the FCVC idea of
Kung et al. (1994), which is explored in the exercises. The main idea is to use absolute packet numbers
instead of incremental updates; with this modification, the protocol can be made robust by the technique
of periodically resending the control state on the two links without the use of a snapshot.
