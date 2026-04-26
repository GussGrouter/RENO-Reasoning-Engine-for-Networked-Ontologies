# network-algorithmics-15-5-conclusions-the-routing-protocol-bgp-border-gateway-protocol-controls-th (chunk 000001)

# Network Algorithmics — 15.5 Conclusions The routing protocol BGP (Border Gateway Protocol) controls the backbone of the Internet. In the last (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 470
- Slice: from `15.5 Conclusions The routing protocol BGP (Border Gateway Protocol) controls the backbone of the Internet. In the last` up to next detected section heading

---

15.5 Conclusions
The routing protocol BGP (Border Gateway Protocol) controls the backbone of the Internet. In the last
few years careful scrutiny of BGP has uncovered several subtle flaws. Incompatible policies can lead
to routing loops (Varadhan et al., 2000), and attempts to make Internal BGP scale using route reflectors

444      Chapter 15 Routers as distributed systems

also lead to loops (Griffin and Wilfong, 2002). Finally, mechanisms to thwart instability by damping
flapping routes can lead to penalizing innocent routes for up to an hour (Mao et al., 2002).
    While credit must go to the BGP designers for designing a protocol that deals with great diversity
while making the Internet work most of the time, there is surely some discomfort at these findings. It
is often asserted that such bugs rarely manifest themselves inoperational networks. But there may be a
Three Mile Island incident waiting for us, as in the crash of the old ARPANET (Perlman, 1992), where
a single unlikely corner case capsized the network for a few days.
    Even worse, there may be a slow, insidious erosion of reliability that gets masked by transparent
recovery mechanisms. Routers restart, TCPs retransmit, and applications retry. Thus failures in proto-
cols and router implementations may only manifest themselves in terms of slow response times, frozen
screens, and rebooting computers.
    Jeff Raskin said: “Imagine if every Thursday your shoes exploded if you tied them the usual way.
This happens to us all of the time with computers, and nobody thinks of complaining.” Given our
tolerance for pain when dealing with networks and computers, a lack of reliability ultimately translates
into a decline in user productivity.
    The examples in this chapter fit this thesis. In each case incorrect distributed algorithm design leads
to productivity erosion, not Titanic failures. Flow control deadlocks can be masked by router reboots,
and cell loss can be masked by TCP retransmits. Failure to preserve ordering within an internal striping
algorithm leads to TCP performance degradation, but not to loss. Failure to consider all cases in DRAM
striping can lead to adversarial access patterns where queues are starved and packets are lost, though
such packets can be retransmitted. Finally, incorrect binary search table updates lead only to increased
packet flooding. But together, the nickels and dimes of every reboot, retransmission, performance loss,
and unnecessary flood can add up to significant losses.
    Thus this chapter is a plea for care in the design of protocols between routers and also within routers.
In the quest for performance that has characterized the rest of the book this chapter is a lonely plea for
rigor. While full proofs may be infeasible, even sketching key invariants and using informal arguments
can help find obscure failure modes. Perhaps, if we reason together, routers can become as comfortable
and free of surprises as an ordinary pair of shoes.
