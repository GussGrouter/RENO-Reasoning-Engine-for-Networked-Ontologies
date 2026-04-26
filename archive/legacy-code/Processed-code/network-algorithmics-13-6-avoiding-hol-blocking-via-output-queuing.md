# Network Algorithmics — 13.6 Avoiding HOL blocking via output queuing (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 369
- Slice: from `13.6 Avoiding HOL blocking via output queuing` up to next detected section heading

---

13.6 Avoiding HOL blocking via output queuing
When HOL blocking was discovered, there was a slew of papers that proposed output queuing in place
of input queuing to avoid HOL blocking. Suppose that packets can somehow be sent to an output port
without any queuing at the input. Then, it is impossible for packet P destined for a busy output port
to block another packet behind it. This is because packet P is sent off to the queue at the output port,
where it can only block packets sent to the same output port.
     The simplest way to do this would be to run the fabric N times faster than the input links. Then, even
if all N inputs send to the same output in a given time slot, all N cells can be sent through the fabric to
be queued at the output. Thus pure output queuing requires an N -fold speedup within the fabric. This
can be expensive or infeasible.
     A practical implementation of output queuing was provided by the knockout-switch design (Yeh et
al., 1987). Suppose that receiving N cells to the same destination in any time slot is rare and that the
expected number is k, which is much smaller than N . Then, the expected case can be optimized (P11)
by designing the fabric links to run k times as fast as an input link, instead of N . This is a big savings
within the fabric. It can be realized with hardware parallelism (P5) by using k parallel buses.
     Unlike the take-a-ticket scheme, all the remaining schemes in this chapter, including the knockout
scheme, rely on breaking up packets into fixed-sized cells. For the rest of the chapter, cells will be used
in place of packets, always understanding that there must be an initial stage where packets are broken
into cells and then reassembled at the output port.
     Besides a faster switch, the knockout scheme needs an output queue that accepts cells k times faster
than the speed of the output link. A naive design that uses this simple specification can be built using
a fast FIFO but would be expensive. Also, the faster FIFO is overkill because clearly the buffer cannot
sustain a long-term imbalance between its input and output speeds. Thus the buffer specification can
be relaxed (P3) to allow it to handle only short periods, in which cells arrive k times as fast as they are
being taken out. This can be handled by memory interleaving and k parallel memories. A distributor
(that does run k times as fast) sprays arriving cells into k memories in round-robin order, and departing
cells are read out in the same order.

                                      13.6 Avoiding HOL blocking via output queuing                 343



    Finally, the design has to fairly handle the case where the expected case is violated and N > k cells
get sent to the same output at the same time. The easiest way to understand the general solution is first
to understand three simpler cases.

   Two contenders, one winner: In the simplest case of k = 1 and N = 2 the arbiter must choose one
cell fairly from two choices. This can be done by building a primitive 2-by-2 switching element, called
a concentrator, that randomly picks a winner and a loser. The winner output is the cell that is chosen.
The loser output is useful for the general case, in which several primitive 2-by-2 concentrators are
combined.
   Many contenders, one winner: Now, consider when k = 1 (only one cell can be accepted) and N > 2
(there are more than two cells that the arbiter must choose fairly from). A simple strategy uses divide-
and-conquer (P15, efficient data structures) to create a knockout tree of 2-by-2 concentrators. As in
the first round of a tennis tournament, the cells are paired up using N/2 copies of the basic 2-by-2
concentrator, each representing a tennis match. This forms the bottom level of the tree. The winners
of the first round are sent to a second round of N/4 concentrators, and so on. The “tournament” ends
with a final, in which the root concentrator chooses a winner. Notice that the loser outputs of each
concentrator are still ignored.
   Many contenders, more than one winner: Finally, consider the general case where k cells must be
chosen from N possible cells for arbitrary values of k and N . A simple idea is to create k separate
knockout trees to calculate the first k winners. However, to be fair, the losers of knockout trees for
earlier trees have to be sent to the knockout trees for the subsequent places. This is why the basic 2-by-
2 knockout concentrator has two outputs, one for the winner and one for the loser, and not just one for
the winner. Loser outputs are routed to the trees for later positions.

    Notice that, if one had to choose four cells from among eight choices, the simplest design would
assign the eight choices (in pairs) to four 2-by-2 knockout concentrators. This logic will pick four win-
ners, the desired quantity. While this logic is certainly much simpler than using four separate knockout
trees, it can be very unfair. For example, suppose two very heavy traffic sources, S1 and S2, happen to
be paired up, while another heavy source, S3, is paired up with a light source. In this case S1 and S2
would get roughly half the traffic that S3 obtains. It is to avoid these devious examples of unfairness
that the knockout logic uses k separate trees, one for each position.
    The naive way to implement the trees is to begin running the logic for the Position j tree strictly
after all the logic for the Position j − 1 tree has been completed. This ensures that all eligible losers
have been collected. A faster implementation trick is explored in the exercises. It is to be hoped that
this design should convince you that fairness is hard to implement correctly. This is a theme that will
be explored again in the discussion of iSLIP.
    While the knockout switch is important to understand because of the techniques it introduced, it is
complex to implement and makes assumptions about traffic distributions. These assumptions are untrue
for real topologies in which more than k clients frequently gang up to concurrently send to a popular
server. More importantly, researchers devised relatively simple ways to combat HOL blocking without
going to output queuing.

344      Chapter 13 Switching
