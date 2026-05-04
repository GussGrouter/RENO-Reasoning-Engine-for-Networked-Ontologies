# Network Algorithmics — 16.12 A concerted approach to accounting (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 497
- Slice: from `16.12 A concerted approach to accounting` up to next detected section heading

---

16.12 A concerted approach to accounting
In moving from efficient counter schemes to trajectory sampling, we moved from schemes that required
only local support at each router to a scheme (i.e., trajectory sampling) that enlists the cooperation of
multiple routers to extract more useful information. We now take this theme a step further by showing
the power of concerted schemes that can involve all aspects of the network system (e.g., protocols,


2 The picture is courtesy of Duffield and Grossglauser (2000).

                                                16.12 A concerted approach to accounting                       471




FIGURE 16.12
Trajectory sampling ensures that all routers sample a packet, or do not, by using the same hash function (as opposed
to a random coin) to decide when to sample a packet.


routers) at various time scales (e.g., route computation, forwarding). We provide two examples: an
accounting example based on a scheme proposed by Juniper networks (described in this section) and
the problem of traffic matrices (described in the next section).
    The specific problem being addressed in this section is that of an ISP wishing to collect traffic
statistics on traffic sent by a customer to charge the customer based on the type of traffic and the
destination of the traffic. Refer to Fig. 16.13, which depicts a small ISP, Z, for the discussion that
follows.
    In the figure assume that ISP Z wishes to bill Customer A at one rate for all traffic that exits via ISP
X and at a different rate for all traffic that exits via ISP Y . One way to do this would be for router R1 to
keep a separate counter for each prefix that represents traffic sent to that prefix. In the figure R1 would
have to keep at least 30,000 prefix counters. Not only does this make implementation more complex,
but it is also unaligned with the user’s need, which will eventually aggregate the 30,000 prefixes into
two tariff classes. Further, if routes change rapidly, the prefixes advertised by each ISP may change
rapidly, requiring constant updating of this mapping by the tool.
    Instead, the Juniper DCU solution (Semeria and Gredler, 2001) has two components.
1. Class Counters: Each forwarding table entry has a 16-bit class ID. Each bit in the class ID repre-
   sents one of 16 classes. Thus if a packet matches prefix P with associated class ID C and C has
   bits set in bits 3, 6, and 9, then the counters corresponding to all three set bits are incremented.
   Thus, there are only 16 classes supported, but a single packet can cause multiple class counters to
   be incremented. The solution aligns with hardware design realities because 16 counters per link is

472        Chapter 16 Measuring network traffic




FIGURE 16.13
Example of an ISP with customer and peer links to other ISPs, X and Y .


   not much harder than one counter, and incrementing in parallel is easily feasible if the 16 counters
   are maintained on-chip in a forwarding ASIC. The solution also aligns with real user needs because
   it cheaply supports the use of up to 16 destination-sensitive3 counters.
2. Routing Support: To attack the problem of changing prefix routes (which would result in the tool’s
   having to constantly map each prefix into a different class), the DCU solution enlists the help of
   the routing protocol. The idea is that all prefixes advertised by ISP X are given a color (which
   can be controlled using a simple route policy filter), and prefixes advertised by ISP Y are given a
   different color. Thus, when a router such as R1 gets a route advertisement for prefix P with color c,
   it automatically assigns prefix P to class c. This small change in the routing protocol greatly reduces
   the work of the tool.
    Juniper also has other schemes (Semeria and Gredler, 2001), including counters based on packet
classifiers and counters based on MPLS tunnels. These are slightly more flexible than DCU accounting
because they can take into account the source address of a packet in determining its class. But these
other schemes do not have the administrative scalability of DCU accounting because they lack routing
support.
    The DCU accounting scheme is an example of P4, leveraging existing system components, and P3,
relaxing system requirements (e.g., only a small number of aggregate classes).
