# network-algorithmics-15-1-2-rescuing-reliability (chunk 000002)

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
