# network-algorithmics-13-18-2-a-divide-and-conquer-approach-to-building-large-switches (chunk 000001)

# Network Algorithmics — 13.18.2 A divide-and-conquer approach to building large switches (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 392
- Slice: from `13.18.2 A divide-and-conquer approach to building large switches` up to next detected section heading

---

13.18.2 A divide-and-conquer approach to building large switches
The divide-and-conquer approach is to build a large switch as an interconnection network of smaller
switches. As a result, the time complexity of matching computations in each smaller switch becomes
small enough to handle at line rates, and, as we will elaborate next, the number of crosspoints is also
significantly reduced due to its O(N 2 ) scaling. In the following subsections we describe one such
divide-and-conquer solution and briefly mention another that were actually adopted in real network
products in the dot.com era (the end of the 1990s to the early 2000s). The first solution was inspired by,
and based on, the Clos networks proposed originally for the circuit switching in a telephone network.
The second solution was adapted from a classical solution for interconnection networks, for parallel
processing.
    Here, we highlight an important fact about these two solutions that was not mentioned in the first
edition of the book. The original ideas of both solutions solve a different problem than that of switching
in our definition so far. In both original applications, namely circuit switching (in a telephone network)
and interconnection network for parallel processors, which “input port” should be paired with which
“output port” at any moment is never in doubt and requires no computation. In a telephone network
the established phone sessions uniquely define the matchings between inputs and outputs; in an in-
terconnection network this pairing (of communicating processors at any moment) is dictated by the
parallel algorithm running on it. In both solutions the computation problem is, given a desired pairing
between the inputs and the outputs in the giant (virtual) switch, to arrive at the configurations of the
small (physical) switches that realize such a matching.
    This computation problem is clearly different from the crossbar scheduling problem we have so far
formulated, which is precisely to compute such a pairing. This computation problem, however, is not
necessarily in the strict sense a simpler one because of the more stringent constraints that go with it
in the original applications. For example, one such constraint is that all these small switches have no
buffer, and as a result, the two paths taken by any two distinct input-output port pairs have to be disjoint
(i.e., cannot share an intermediate node or link) or, equivalently, the large switch has to be nonblocking
(to be defined in Section 13.18.3). In contrast, in the packet switching problem, the input ports are
assumed to have adequate amounts of buffers and do not impose such a constraint.

366      Chapter 13 Switching

FIGURE 13.16
Three-stage Clos network.

In Sections 13.18.3 and 13.18.4 we will explain both solutions in terms of how they facilitate a
known matching between the input and the output ports of the large crossbar, just like in the first edition
of the book. In Section 13.18.3 we will describe how to adapt one of them, namely the Clos network,
for the packet switching problem. More specifically, we will describe a possible way of constructing a
large packet switch using a Clos network of small packet switches with buffers.
