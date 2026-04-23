# network-algorithmics-17-3-ip-traceback-via-probabilistic-marking (chunk 000002)

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
