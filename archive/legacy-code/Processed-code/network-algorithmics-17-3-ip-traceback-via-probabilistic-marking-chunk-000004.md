# network-algorithmics-17-3-ip-traceback-via-probabilistic-marking (chunk 000004)

The solution provided in the seminal paper (Savage et al., 2000) avoids the aliasing due to hop
counts by conceptually starting with a pair of consecutive node IDs and a hop count to form a triple
(R, S, h), as shown in Fig. 17.5.
     When a router R receives a packet with triple (X, Y, h), R generates a random number between 0
and 1. If the number is less than the sampling probability p, router R writes its own ID into the mark
triple, rewriting it as (R, −, 0), where the “−” character indicates that the next router in the path has
still to be determined. If the random number is greater than p, then R must maintain the integrity of the
previously written mark. If h = 0, R writes R to the second field because R is the next router after the
writer of the mark. Finally, if the random number is greater than p, R increments h.
     It should be clear that by assuming that every edge gets sampled once, the victim can reconstruct
the path. Note also that the attacker can only add fictitious nodes to the start of the path. But how many
packets are required to find all edges? Given that ordering is explicit, one can use arbitrary values of p.
     In particular, if p is approximately 1/L, where L is the path length to the furthest router, the
probability we computed before of the furthest router sending an edge mark that survives becomes
p(1 − p)L−1 ≈ p/(1 − p)e, where e is the base of natural logarithms. For example, for p = 1/25, this
is roughly 1/70, which is fairly large compared to the earlier attempt.
     What is even nicer is that if we choose p = 1/50 based on the largest path lengths encountered in
practice on the Internet (say, 50), the probability does not grow much smaller, even for much smaller
path lengths. This makes it easy to reconstruct the path with hundreds of packets as opposed to thou-
sands.
     Finally, one can get rid of obvious waste (P1) and avoid the need for two node IDs by storing only
the Exclusive-OR of the two fields in a single field. Working backward from the last router ID known
to the victim, one can Exclusive-OR with the previous edge mark to get the next router in the path, and
so on. Finally, by viewing each node as consisting of a sequence of a number of “pseudonodes,” each
with a small fragment (say, 8 bits) of the node’s ID, one can reduce the mark length to around 16 bits
total.
