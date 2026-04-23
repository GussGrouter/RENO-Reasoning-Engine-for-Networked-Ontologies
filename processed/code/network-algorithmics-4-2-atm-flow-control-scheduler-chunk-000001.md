# network-algorithmics-4-2-atm-flow-control-scheduler (chunk 000001)

# Network Algorithmics — ATM flow control scheduler (4.2) (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Extraction: pdftotext -f 104 -l 119 -layout
- Slice: from `4.2 Scheduler for asynchronous transfer mode flow control` up to (excluding) `4.3`

---

4.2 Scheduler for asynchronous transfer mode flow control
In asynchronous transfer mode (ATM), an ATM adaptor may have hundreds of simultaneous virtual
circuits (VCs) that can send data (called cells). Each VC is often flow controlled in some way to limit
the rate at which it can send. For example, in rate-based flow control, a VC may receive credits to send
cells at fixed time intervals. On the other hand, in credit-based flow control (Kung et al., 1994; Ozveren
et al., 1994), credits may be sent by the next node in the path when buffers free up.
    Thus in Fig. 4.3 the adaptor has a table that holds the VC state. There are four VCs that have been
set up (1, 3, 5, 7). Of these, only VCs 1, 5, and 7 have some cells to send. Finally, only VCs 1 and
7 have credits to send cells. Thus the next cell to be sent by the adaptor should be from either one of
the eligible VCs: 1 or 7. The selection from the eligible VCs should be done fairly, for example, in
round-robin fashion. If the adaptor chooses to send a cell from VC 7, the adaptor would decrement the
credits of VC 7 to 1. Since there are no more cells to be sent, VC 7 now becomes ineligible. Choosing
the next eligible VC leads to the following problem.

Problem
A naive scheduler may cycle through the VC array looking for a VC that is eligible. If many of the VCs
are ineligible, this can be quite inefficient, for the scheduler may have to step through several VCs that
are ineligible to send one cell from an eligible VC. How can this inefficiency be avoided?
Hint: Consider invoking P12 to add some extra state to speed up the scheduler main loop. What
state can you add to avoid stepping through ineligible VCs? How would you maintain this state
efficiently?

FIGURE 4.3
An ATM VC is eligible to send data if it is active (has some outstanding cells to send in the queue shown below the
VC) and has credits (shown by gray dots above the VC). The problem is to select the next eligible VC in some fair
manner without stepping through VCs that are ineligible.

---

## PDF page 106
