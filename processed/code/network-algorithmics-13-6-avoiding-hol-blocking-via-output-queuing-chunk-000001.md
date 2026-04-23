# network-algorithmics-13-6-avoiding-hol-blocking-via-output-queuing (chunk 000001)

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
