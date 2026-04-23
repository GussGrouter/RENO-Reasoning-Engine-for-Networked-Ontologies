# Network Algorithmics — 10.4 Summary This chapter on exact-match lookups is written as a story, the story of bridging. Three morals can be (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 274
- Slice: from `10.4 Summary This chapter on exact-match lookups is written as a story, the story of bridging. Three morals can be` up to next detected section heading

---

10.4 Summary
This chapter on exact-match lookups is written as a story, the story of bridging. Three morals can be
drawn from this story.
    First, bridging was a direct response to the challenge of efficiently extending Ethernets without using
routers or repeaters; wire speed forwarding was a direct response to the problem of potentially losing
important packets in a flood of less important packets. At the risk of sounding like a self-help book,
I hold that challenges are best regarded as opportunities and not as annoyances. The mathematician
Felix Klein (Bell, 1986) used to say, “You must always have a problem; you may not find what you
were looking for but you will find something interesting on the way.” For example, it is clear that the
main reason bridges were invented, that is, the lack of high-performance multiprotocol routers, is not
the reason bridges are still useful today.
    This brings us to the second moral. Today it is clear that bridges will never displace routers because
of their lack of scalability using flat Ethernet addresses, lack of shortest-cost routing, etc. However,
they remain interesting today because bridges are interconnect devices with better cost for performance
and higher flexibility than routers for interconnecting a small number of similar local area networks.
Thus bridges still abound in the marketplace, often referred to as switches. What many network vendors
refer to as a switch is a crossbar switch, such as the Gigaswitch, that is capable of bridging on every
interface. A few new features, notably virtual LANs (VLANs) (Perlman, 1992), have been added. But
the core idea remains the same.
    Third, the techniques introduced by the first bridge have deeply influenced the next generation of
interconnect devices, from core routers to Web switches. Recall that Roger Bannister, who first broke
the 4-minute-mile barrier, was followed in a few months by several others. In the same way, the first
Ethernet bridge was quickly followed by many other wire speed bridges. Soon the idea began to flow to
routers as well. Other important concepts introduced by bridges include the use of memory references
as a metric, the notion of trading update time for faster lookups, and the use of minimal hardware
speedups. All these ideas carry over into the study of router lookups in the next chapter.
    In conclusion, the challenge of building the first bridge stimulated creative actions that went far
beyond the first bridge. While wire speed router designs are fairly commonplace today, it is perhaps
surprising that there are products still being announced that claim gigabit wire speed processing rates
for such abstruse networking tasks as encryption and even XML transformations.
