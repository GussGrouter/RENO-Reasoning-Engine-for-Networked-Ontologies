# Network Algorithmics — 13.5 Head-of-line blocking (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 367
- Slice: from `13.5 Head-of-line blocking` up to next detected section heading

---

13.5 Head-of-line blocking
Forgetting about the internal mechanics of Fig. 13.5, observe that there were nine potential transmission
opportunities in three iterations (three input ports and three iterations), but, after the connection depicted
in the diagram at the bottom right, there is one packet in B’s queue and two in C’s queue. Thus only
six of potentially nine packets have been sent, thereby taking limited advantage of parallelism.
    This focus on only input–output behavior is sketched in Fig. 13.6. The figure shows the packets sent
in each packet time at each output port. Each output port has an associated timeline labeled with the

                                                                      13.5 Head-of-line blocking                341




FIGURE 13.6
Example of HOL blocking caused by schemes like take-a-ticket. For each output port, a horizontal time scale is
drawn labeled with the input port that sent a packet to that output port during the corresponding time period or a
blank mark if there is none. Note the large number of blanks, showing potentially wasted opportunities that limit
parallelism.


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



    But, are uniform-traffic distributions realistic? Clearly, the analysis is very dependent on the traffic
distribution because no switch can do well if all traffic is destined for one server port. Simple analyses
show that the effect of HOL blocking can be reduced by using hunt groups, by using speedup in the
crossbar fabric compared to the links, and by assuming more realistic distributions in which a number
of clients send traffic to a few servers.
    However, it should be clear that there do exist distributions where HOL blocking can cause great
damage to throughput. Imagine that every input link has B packets to port 1, followed by B packets to
port 2, and so on, and finally B packets to port N . The same distribution of input packets is present in
all input ports. Thus, clearly, when scheduling the group of initial packets to port 1, essentially HOL
blocking will limit the switch to sending only one packet per input each time. Thus the switch reduces
to 1/N of its possible throughput if B is large enough. On the other hand, we will see that switches that
use VOQs (defined later in this chapter) can, in the same situations, achieve nearly 100% throughput.
This is because in such schemes, each block of B packets stays in separate queues at each input.
