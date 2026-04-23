# Network Algorithmics — 15.1.2 Rescuing reliability (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 459
- Slice: from `15.1.2 Rescuing reliability` up to next detected section heading

---

15.1.2 Rescuing reliability
The protocol sketched in the last subsection uses limited receiver SRAM buffers very efficiently but
is not robust to failures. Before understanding how to make the more elaborate flow control protocol
robust against failures, it is wiser to start with the simpler credit protocol portrayed in Fig. 15.1.
    Intuitively, the protocol in Fig. 15.1 is like transferring money between two banks: the “banks” are
the sender and the receiver, and both credits and cells count as “money.” It is easy to see that, in the
absence of errors, the total “money” in the system is conserved. More formally, let CR be the credit
register, M the number of cells in transit from sender to receiver, C the number of credits in transit in
the other direction, and Q the number of cell buffers that are occupied at the receiver.
    Then, it is easy to see that (assuming proper initialization and that no cells or credits are lost on the
link), the protocol maintains the following property at any instant: CR + M + Q + C = B, where B is
the total buffer space at the receiver. The relationship is called an invariant because it holds at all times
when the protocol works correctly. It is the job of protocol initialization to establish the invariant and
the job of fault tolerance mechanisms to maintain the invariant.

                                                                   15.1 Internal flow control          433



     If this invariant is maintained at all times, then the system will never drop cells because the number
of cells in transit plus the number of stored cells is never more than the number of buffers allocated.
     There are two potential problems with a simple hop-by-hop flow control scheme. First, if initial-
ization is not done correctly, then the sender can have too many credits, which can lead to cells being
dropped. Second, credits or cells for a class can be lost due to link errors. Even chip-to-chip links are
not immune from infrequent bit errors; at high link speeds, such errors can occur several times an hour.
This second problem can lead to a slowdown or deadlock.
     Many implementors can be incorrectly persuaded that these problems can be fixed by simple mecha-
nisms. One immediate response is to argue that these cases won’t happen or will happen rarely. Second,
one can attempt to fix the second problem by using a timer to detect possible deadlock. Unfortunately,
it is difficult to distinguish deadlock from the receiver’s removing cells very slowly. What is worse,
the entire link can slow down to a crawl, causing router performance to fall; the result will be hard to
debug.
     The problems can probably be cured by a router reset, but this is a Draconian solution. Instead,
consider the following resynchronization scheme. For clarity, the scheme is presented using a series of
refinements depicted in Fig. 15.2.
     In the simplest synchronization scheme (Scheme 1, Fig. 15.2) assume that the protocol periodically
sends a specially marked cell called a marker. Until the marker returns, the sender stops sending data
cells. At the receiver, the marker flows through the buffer before being sent back to the upstream node.
It is easy to see that after the marker returns, it has “flushed” the pipe of all cells and credits. Thus at
the point the marker returns, the protocol can set the CR to the maximum value (B). Scheme 1 is simple
but requires the sender to be idled periodically to do resynchronization.
     So, Scheme 2 (Fig. 15.2) augments Scheme 1 by allowing the sender to send cells after the marker
has been sent; however, the sender keeps track of the cells sent since the marker was launched in
a register, say, CSM (for “cells sent since marker”). When the marker returns, the sender adjusts the
correction to take into account the cells sent since the marker was launched and so sets CR = B − CSM.
     The major flaw in Scheme 2 is the inability to bound the delay that it takes the marker to go through
the queue at the receiver. This causes two problems. First, it makes it hard to bound how long the scheme
takes to correct itself. Second, to make the marker scheme itself reliable, the sender must periodically
retransmit the marker. Without a bound on the marker round-trip delay, the sender could retransmit too
early, making it hard to match a marker response to a marker request without additional complexity in
terms of sequence numbers.
     To bound the marker round-trip delay, Scheme 3 (Fig. 15.2) lets the marker bypass the receiver
queue and “reflect back” immediately. However, this requires the marker to return with the number of
free cell buffers F in the receiver at the instant the marker was received. Then, when the marker returns,
the sender sets the credit register CR = F − CSM.
     The marker scheme is a special instance of a classical distributed systems technique called a snap-
shot. Informally, a snapshot is a distributed audit that produces a consistent state of a distributed system.
Our marker-based snapshot is slightly different from the classical snapshot described in Chandy and
Lamport (1985). The important point, however, is that snapshots can be used to detect incorrect states
of any distributed algorithm and can be efficiently implemented in a two-node subsystem to make any
such protocol robust. In particular, the same technique can be used (Ozveren et al., 1994) to make the
fancier flow control of Section 15.1.1 equally robust.

434       Chapter 15 Routers as distributed systems




FIGURE 15.2
Three steps to a marker algorithm.

    In particular, the marker protocol makes the credit-update protocol self-stabilizing, i.e., it can re-
cover from arbitrary errors, including link errors, and also hardware errors that corrupt registers. This
is an extreme form of fault tolerance that can greatly improve the reliability of subsystems without
sacrificing performance.
    In summary, the general technique for a two-node system is to write down the protocol invariants and
then to design a periodic snapshot to verify and, if necessary, correct the invariants. Further techniques
for protocols that work on more than two nodes are described in Awerbuch et al. (1991); they are
based on decomposing, when possible, multinode protocols into two-node subsystems and repeating
the snapshot idea.

                                                                 15.2 Internal Link Striping          435



    An alternative technique for making a two-node credit protocol fault tolerant is the FCVC idea of
Kung et al. (1994), which is explored in the exercises. The main idea is to use absolute packet numbers
instead of incremental updates; with this modification, the protocol can be made robust by the technique
of periodically resending the control state on the two links without the use of a snapshot.
