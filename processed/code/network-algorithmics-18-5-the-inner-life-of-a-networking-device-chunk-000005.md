# network-algorithmics-18-5-the-inner-life-of-a-networking-device (chunk 000005)

time-out this link, set its estimate of distance to D through R4 to infinity, and then choose the route
through R3. Unfortunately, distance vector takes a long time to converge when destinations become
unreachable (Perlman, 1992).
    Link state routing (Perlman, 1992) avoids the convergence problems of distance vector by having
each router construct a link state packet (LSP) listing its neighbors. In Fig. A.2 for instance, R3’s
LSP will list its links to R2 and R4. Each router then broadcasts its LSP to all other routers in the
domain using a primitive flooding mechanism; LSP sequence numbers are used to prevent LSPs from
circulating forever. When all routers have each other’s LSP, every router has a map of the network and
can use Dijkstra’s algorithm (Perlman, 1992) to calculate shortest-path routes to all destinations. The
most common routing protocol used within ISP domains is a link state routing protocol called open
shortest path first (OSPF) (Perlman, 1992).
    While shortest-path routing works well within domains, the situation is more complex for routing
between domains. Imagine that Fig. A.2 is modified so that the ISP in the middle, say, ISP A, does not
have a direct route to D’s domain but instead is connected to ISPs C and E, each of which has a path
to D’s domain. Should ISP A send a packet addressed to D to ISP C or E? Shortest-path routing no
longer makes sense because ISPs want to route based on other metrics (e.g., dollar cost) or on policy
(e.g., always send data through a major competitor, as in so-called “hot potato” routing).
    Thus interdomain routing is a more messy kettle of fish than routing within a domain. The most
commonly used interdomain protocol today is called the border gateway protocol (BGP) (Stevens,
1998), which uses a gossip mechanism akin to distance vector, except that each route is augmented
with the path of domains instead of just the distance. The path ostensibly makes convergence faster
than the distance vector and provides information for policy decisions.
    To go beyond this brief sketch of routing protocols, the reader is directed to Interconnections by
Radia Perlman (1992) for insight into routing in general and to BGP-4 by John Stewart (1999) as the
best published textbook on the arcana of BGP.

A.2 Hardware models
For completeness, this section contains some details of hardware models that were skipped in Chapter 2
for the sake of brevity. These detailed models are included in this section to provide a somewhat deeper
understanding for software designers.

A.2.1 From transistors to logic gates
The fundamental building block of the most complex network processor is a transistor (Fig. A.3).
A transistor is a voltage-controlled switch. More precisely, a transistor is a device with three external
attachments (Fig. A.3): a gate, a source, and a drain. When an input voltage I is applied to the gate, the
source-drain path conducts electricity; when the input voltage is turned off, the source-drain path does
not conduct. The output O voltage occurs at the drain. Transistors are physically synthesized on a chip
by having a polysilicon path (gate) cross a diffusion path (source-drain) at points governed by a mask.
    The simplest logic gate is an inverter (also known as a NOT gate). This gate is formed (Fig. A.3)
by connecting the drain to a power supply and the source to ground (0 volts). The circuit functions as
an inverter because when I is a high voltage (i.e., I = 1), the transistor turns on, “pulling down” the
output to ground (i.e., O = 0). On the other hand, when I = 0, the transistor turns off, “pulling up” the

534        Detailed models
