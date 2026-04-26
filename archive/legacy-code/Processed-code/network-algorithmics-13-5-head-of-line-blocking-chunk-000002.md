# network-algorithmics-13-5-head-of-line-blocking (chunk 000002)

input port that sent a packet during the corresponding time period, with a blank if there is none. Note
also that this picture continues the example started in Fig. 13.5 for three more iterations, until all input
queues are empty.
     It is easy to see from the righthand diagram in Fig. 13.6 that only roughly half of the transmission
opportunities (more precisely, 9 out of 24) are used. Now, of course, no algorithm can do better for
certain scenarios. However, other algorithms, such as iSLIP (see Fig. 13.10 in Section 13.10) can extract
more parallel opportunities and finish the same nine packets in four iterations instead of six.
     In the first iteration of Fig. 13.6 all inputs have packets waiting for output 1. Since only one (i.e., A)
can send a packet to output 1 at a time, the entire queue at B (and C) is stuck waiting for A to complete.
Since the entire queue is held hostage by the progress of the head of the queue, or line, this is called
head-of-line blocking. iSLIP and PIM get around this limitation by allowing packets behind a blocked
packet to make progress (for example, the packet destined for output port 2 in the input queue at B can
be sent to output port 2 in iteration 1 of Fig. 13.6) at the cost of a more complex scheduling algorithm.
     The loss of throughput caused by HOL blocking can be analytically captured using a simple
uniform-traffic model. Assume that the head of each input queue has a packet destined for each of
N outputs with probability 1/N . Thus if two or more input ports send to the same output port, all but
one input are blocked. The entire throughput of the other inputs is “lost” due to HOL blocking.
     More precisely, assume equal-sized packets and one initial trial where a random process draws a
destination port at each input port uniformly from 1 to N . Instead of focusing on input ports, let us focus
on the probability that an output port O is idle. This is simply the probability that none of the N input
ports chooses O. Since each input port does not choose O with probability 1 − 1/N, the probability
that all N of them will not choose O is (1 − 1/N )N . This expression rapidly converges to 1/e. Thus
the probability that O is busy is 1 − 1/e, which is 0.63. Thus the throughput of the switch is not N ∗ B,
which is what it could be ideally if all N output links are busy operating at B bits per second. Instead,
it is 63% of this maximum value because 37% of the links are idle.
     This analysis is simplistic and (incorrectly) assumes that each iteration is independent. In reality
packets picked in one iteration that are not sent must be attempted in the next iteration (without another
random coin toss to select the destination). A classic analysis (Karol et al., 1987) that removes the
independent-trials assumption shows that the actual utilization is slightly worse and is closer to 58.6%.

342      Chapter 13 Switching
