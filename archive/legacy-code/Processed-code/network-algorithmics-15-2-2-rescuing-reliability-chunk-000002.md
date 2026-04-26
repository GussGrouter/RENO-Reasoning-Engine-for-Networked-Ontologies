# network-algorithmics-15-2-2-rescuing-reliability (chunk 000002)

channels have not been visited in the first round-robin scan at the receiver. When the round-robin pointer
increments to a channel at the sender or receiver, the corresponding round number is incremented.
    Effectively, round numbers can be considered to be implicit per-channel sequence numbers. Thus A
can be considered to have sequence number R1, the next cell, D, sent on Channel 1 can be considered
to have sequence number R2, etc.
    Thus in Scene 2 of Fig. 15.3 the sender has marched on to send D on Channel 1 and E on Channel 2.
The receiver is still waiting for a cell on Channel 1, which it finally receives. At this point, the play
shifts to Scene 3, where the receiver outputs D and B (in that order) and moves to Channel 3, where it
eventually receives cell C.
    Basically, the misordering problem in Scene 2 is caused by the receiver’s dequeuing a cell sent in
Round R2 (i.e., D) in Round R1 at the receiver. This suggests a simple strategy to synchronize the round
numbers in channels: periodically, the sender should send its current round number on each channel to
the receiver. To reduce overhead, such a marker cell should be sent after hundreds of data cells are sent,
at the cost of having potentially hundreds of cells misordered after a loss.
    Because brevity is the soul of wit, the play in Fig. 15.3 assumes a marker is sent after D on Chan-
nel 1; the sending of markers on other channels is not shown. Thus in Scene 3 notice that a marker is
sent on Channel 1 with the current round number, R2, at the sender.
    In Scene 4 the receiver has output D, B, and C, in that order, and is now waiting for Channel 1 again.
At this point, the marker containing R2 arrives.
    A marker is processed at the receiver only when the marker is at the head of the buffer and the
round-robin pointer is at the corresponding channel. Processing is done by the following four rules.
(1) If the round number in the marker is strictly greater than the current receiver round number, the
marker has arrived too early; the round-robin pointer is incremented; (2) if the round numbers are equal,
any subsequent cells will have higher round numbers; thus the round-robin pointer is incremented, and
the marker is also removed (but not sent to the output).
    (3) If the round number in the marker is 1 less than the current channel round number, this is the
normal error-free case; the subsequent cell will have the right round number. In this case the marker
is removed, but the round-robin pointer at the receiver is not incremented. And last, (4) if the round
number in the marker is k > 1 less than the current channel round number, a serious error (other than
cell loss) has occurred and the sender and receiver should reinitialize.
    Thus in Scene 4 Rule 2 applies: the marker is destroyed and the round-robin pointer incremented.
At this point, it is easy to see that the sender and receiver are now in perfect synchronization because,
for each channel at the receiver, the round number when that channel is reached is equal to the round
number of the next cell. Thus the play ends with E’s being (correctly) dequeued in Scene 4, then F in
Scene 5, and finally G in Scene 6. Order is restored; morality is vindicated.
    Thus the augmented load-balancing algorithm recovers from errors very quickly (time between
sending the marker plus a one-way propagation delay). The general technique underlying the method
of Fig. 15.3 is to detect state inconsistency on each channel by periodically sending a marker one way.
    One-way sending of periodic state (unlike, say, Fig. 15.2) suffices for load balancing and also for the
FCVC protocol (see Exercises) because the invariants of the protocol are one-way. A one-way invariant
is an invariant that involves only variables at the two nodes and one link. By contrast, the flow control
protocol of Fig. 15.1 has an invariant that uses variables on both links.
    Periodic sending of state has been advocated as a technique for building reliable Internet protocols,
together with timing out state that has not been refreshed for a specified period (Clark, 1988). While
