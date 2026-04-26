# network-algorithmics-17-3-ip-traceback-via-probabilistic-marking (chunk 000003)

498       Chapter 17 Network security

FIGURE 17.4
Reconstructing an attack path by having each router stamp its ID independently, with probability p, into a single
node ID field. The receiver reconstructs order by sorting, assuming that closer routers will produce more samples.

However, in the systems context one can optimize the expected case (P11), since most interesting
attacks consist of hundreds of packets at least. Assuming they are all coming from the same physical
source, the victim can shift the path computation over time (P2) by making each mark contribute a
piece of the path information.
    Let’s start by assuming a single 32-bit field in a packet that can hold a single router ID. How are the
routers on the path to synchronize access the field so that each router ID gets a chance, over a stream of
packets, to place its ID in the field?
    A naive solution is shown in Fig. 17.4. The basic idea is that each router independently writes its ID
into a single node ID field in the packet with probability p, possibly overwriting a previous router’s ID.
Thus in Fig. 17.4 the packet already has R1 in it and can be overwritten by R3 to R1 with probability p.
    The hope, however, is that over a large sequence of packets from the attacker to the victim, every
router ID in the path will get a chance to place its ID without being overwritten. Finally, the victim can
sort the received IDs by the number of samples. Intuitively, the nodes closer to the victim should have
more samples, but one has to allow for random variation.
    The two problems with this naive approach are that too many samples (i.e., attack packets) are
needed to deal with random variation in inferring order. Also, the attacker, knowing this scheme, can
place malicious marks in the packet to fool the reconstruction scheme into believing that fictitious nodes
are close to the victim because they receive extra marks.
    To foil this threat, p must be large, say, 0.51. But in this case the number of packets required to
receive the router IDs far away from the victim becomes very large. For example, with p = 0.5 and a
path of length L = 15, the number of packets required is the reciprocal of the probability that the router
furthest from the victim sends a mark that survives. This is p(1 − p)L−1 = 2−15 , because it requires
the furthest router to put a mark and the remaining L − 1 routers not to. Thus the average number of
                                 1
packets for this to happen is 2−15   = 32 000. Attacks have a number of packets, but not necessarily this
many.
    The straightforward lesson from the naive solution is that randomization is good for synchronization
(to allow routers to independently synchronize access to the single node ID field) but not to reconstruct
order. The simplest solution to this problem is to use a hop count (the attacker can initialize each packet
with a different TTL (time-to-live), making the TTL hard to use) as well as a node ID. But a hop count
by itself can be confusing if there are multiple attacks going on. Clearly a mark of node X with hop
count 2 may correspond to a different attack path from a mark of node Y with hop count 1.

17.4 IP traceback via logging              499

FIGURE 17.5
Edge sampling improves on node sampling by sampling edges and not nodes. This allows trivial order reconstruc-
tion based on edge distance and not sample frequency.
