# network-algorithmics-13-7-avoiding-hol-blocking-via-virtual-output-queuing (chunk 000001)

# Network Algorithmics — 13.7 Avoiding HOL blocking via virtual output queuing (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 371
- Slice: from `13.7 Avoiding HOL blocking via virtual output queuing` up to next detected section heading

---

13.7 Avoiding HOL blocking via virtual output queuing
One such solution approach that has sustained the test of time is VOQ (Tamir and Frazier, 1988). In fact,
it was proposed earlier than most of the output queueing solutions described in the previous section.
The VOQ approach is to reconsider input queuing but retrofit it to avoid HOL blocking. It does so by
allowing an input port to schedule not just the head of its input queue but also other cells, which can
make progress when the head is blocked. At first glance, this looks very hard. There could be a hundred
thousand cells in each queue; attempting to maintain even 1 bit of scheduling state for each cell will
take too much memory to store and process.
     However, the first significant observation is that cells in each input port queue can be destined
for only N possible output ports. Suppose cell P 1 is before cell P 2 in input queue X and that both
P 1 and P 2 are destined for the same output queue Y . Then, to preserve FIFO behavior, P 1 must be
scheduled before P 2 anyway. Thus there is no point in attempting to schedule P 2 before P 1 is done.
Thus obvious waste can be avoided (P1) by not scheduling any cells other than the first cell sent to
every distinct output port.
     The idea of the VOQ approach is to exploit a degree of freedom (P13) and to decompose the single
input queue of Fig. 13.5 into a separate input queue per output at each input port in Fig. 13.7. These
are called virtual output queues. Notice that the top left diagram of Fig. 13.7 contains the same input
cells as in Fig. 13.6, except now they are placed in separate VOQs.
     With the concept of VOQ introduced, we face a new computational problem in switching. Whereas
an input port with a single (combined) packet queue should always be paired (if at all) with the output
port for which its HOL packet is destined, an input port with N VOQs has up to N pairing options and
has to decide on one of them. More generally, the switch with N input ports and N output ports has to
decide, out of its N 2 VOQs (N per input port), which N of them (or less) to serve in a time slot.
     As we will explain next, in a crossbar switch, to make such a pairing decision involves computing
a bipartite matching, which has been known since 1970s to be a nontrivial computational problem in
general. Indeed, the general bipartite matching algorithms are too computationally expensive for large
and fast switches (i.e., where N is large and a time slot is short). This is perhaps a reason why the VOQ
approach was not widely adopted until a decade or so after it was first proposed, when computationally
efficient bipartite matching algorithms designed specifically for switching, such as PIM (Anderson et
al., 1993) and iSLIP (McKeown, 1999), were discovered.
