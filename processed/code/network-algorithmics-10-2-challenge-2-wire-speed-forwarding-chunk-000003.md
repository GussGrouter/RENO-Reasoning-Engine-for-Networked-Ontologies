# network-algorithmics-10-2-challenge-2-wire-speed-forwarding (chunk 000003)

of DRAM memory accesses. As the first product aimed for a table size of 8000,4 this required
    log2 8000 memory accesses of 100-nanosecond each, yielding a lookup time of 1.3 microsecond.
    Given that the processor does useful work during the lookup, two lookups for source and destination
    easily fit within a 25.6 microsecond budget (Q4).
    To answer Q5 in Chapter 3 as to whether custom hardware is worthwhile, Mark found that the
lookup chip could be cheaply and quickly implemented using a PAL (programmable array logic; see
Chapter 2). To answer Q7, his initial prototype met wire speed tests constructed using logic analyzers.
Finally, Q8, which asks about the sensitivity to environment changes, was not relevant to a strictly
worst-case design like this.
    The 68000 software, written by Bob Shelley, also had to be carefully constructed to maximize
parallelism. After the prototype was built, Tony Lauck, then head of DECNET, was worried that bridges
would not work correctly if they were placed in cyclic topologies. For example, if two bridges are placed
between the same pair of Ethernets, messages sent on one Ethernet will be forwarded at wire speed in
the loop between bridges. In response, Radia Perlman, then the DEC routing architect, invented her
celebrated spanning tree algorithm. The algorithm ensures that bridges compute a loop-free topology
by having redundant bridges turn off appropriate bridge ports.
    While you can read up on the design of the spanning tree algorithm in Perlman’s book (Perlman,
1992), it is interesting to note that there was initial resistance to implementing her algorithm, which ap-
peared to be “complex” when compared to simple, fast bridge data forwarding. However, the spanning
tree algorithm used control messages, called Hellos, that are not processed in real time.
    A simple back-of-the-envelope calculation by Tony Lauck related the number of instructions used to
process a hello (at most 1000), the rate of hello generation (specified at that time to be once every sec-
ond), and the number of instructions per second of the Motorola 68000 (around 1 million). Lauck’s vi-
sion and analysis carried the day, and the spanning tree algorithm was implemented in the final product.
    Manufactured at a cost of $1000, the first bridge was initially sold at a markup of around eight,
ensuring a handsome profit for DEC when sales initially climbed. In 1986 Mark Kempf was awarded
US Patent 4,597,078, titled “Bridge circuit for interconnecting networks.” DEC made no money from
patent licensing, choosing instead to promote the IEEE 802.1 bridge interconnection standards process.
    Together with the idea of self-learning bridges, the spanning tree algorithm has passed into history.
Ironically, one of the first customers complained that the bridge did not work correctly; field service
later determined that the customer had connected two bridge ports to the same Ethernet, and the span-
ning tree had (rightly) turned the bridge off! While features like autoconfigurability and provable fault
tolerance have only recently been added to Internet protocols, they were part of the bridge protocols in
the 1980s.
    The success of Ethernet bridges led to proposals for several other types of bridges connecting other
local area networks and even wide area bridges. The author even remembers working with John Hart
(who went on to become CTO of 3Com) and Fred Baker (who went on to become a Cisco Fellow)
on building satellite bridges that could link geographically distributed sites. While some of the initital
enthusiasm to extend bridges to supplant routers was somewhat extreme, bridges found their most
successful niche in cheaply interconnecting similar local area networks at wire speeds.

4 This allows a bridged Ethernet to have only 8000 stations. While this is probably sufficient for most customer sites, later bridge
implementations raised this figure to 16K and even 64K.

242      Chapter 10 Exact-match lookups
