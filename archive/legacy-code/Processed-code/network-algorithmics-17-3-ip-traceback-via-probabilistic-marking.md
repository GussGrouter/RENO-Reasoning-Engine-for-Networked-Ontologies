# Network Algorithmics — 17.3 IP traceback via probabilistic marking (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 524
- Slice: from `17.3 IP traceback via probabilistic marking` up to next detected section heading

---

17.3 IP traceback via probabilistic marking
This section transitions from the problem of detecting an attack to responding to an attack. Response
could involve a variety of tasks, from determining the source of the attack to stopping the attack by
adding some checks at incoming routers.
    The next two sections concentrate on traceback, an important aspect of response, given the ability
of attackers to use forged IP source addresses. To understand the traceback problem it helps first to
understand a canonical denial-of-service (DOS) attack that motivates the problem.
    In one version of a DOS attack, called SYN flooding, Wily Harry Hacker wakes up one morning
looking for fun and games and decides to attack CNN. To do so, he makes his computer fire off a large
number of TCP connection requests to the CNN server, each with a different forged source address.
The CNN server sends back a response to each request R and places R in a pending connection queue.
    Assuming the source addresses do not exist or are not online, there is no response. This effect
can be ensured by using random source addresses and by periodically resending connection requests.
Eventually the server’s pending-connection queue fills up. This denies service to innocent users like
you who wish to read CNN news because the server can no longer accept connection requests.
    Assume that each such DOS attack has a traffic signature (e.g., too many TCP connection requests)
that can be used to detect the onset of an attack. Given that it is difficult to shut off a public server, one
way to respond to this attack is to trace such a DOS back to the originating source point despite the use
of fake source addresses. This is the IP traceback problem.
    The first and simplest systems approach (P3, relax system requirements) is to finesse the problem
completely using help from routers. Observe that when Harry Hacker sitting in an IP subnetwork with
prefix S sends a packet with fake source address H , the first router on the path can detect this fact if H
does not match S. This would imply that Harry’s packet cannot disguise its subnetworks, and offending
packets can be traced at least to the right subnetwork.
    There are two difficulties with this approach. First, it requires that edge routers do more processing
with the source address. Second, it requires trusting edge routers to do this processing, which may be
difficult to ensure if Harry Hacker has already compromised his ISP. There is little incentive for a local
ISP to slow down performance with extra checks to prevent DOS attacks to a remote ISP.
    A second and cruder systems approach is to have managers that detect an attack call their ISP, say,
A. ISP A monitors traffic for a while and realizes these packets are coming from prior-hop ISP B, who
is then called. B then traces the packets back to the prior-hop provider and so on until the path is traced.
This is the solution used currently.
    A better solution than manual tracing would be automatic tracing of the packet back to the source.
Assume one can modify routers for now. Then packet tracing can be trivially achieved by having each
router in the path of a packet P write its router IP address in sequence into P ’s header. However, given
common route lengths of 10, this would be a large overhead (40 bytes for 10 router IDs), especially for
minimum-size acknowledgments. Besides the overhead, there is the problem of modifying IP headers
to add fields for path tracing. It may be easier to steal a small number of unused message bits.
    This leads to the following problem. Assuming router modifications are possible, find a way to trace
the path of an attack by marking as few bits as possible in a packet’s header.
    For a single-packet attack, this is very difficult in an information theoretic sense. Clearly, it is im-
possible to construct a path of 10 32-bit router IDs from, say, a 2-byte mark in a packet. One can’t make
a silk purse from a sow’s ear.

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
