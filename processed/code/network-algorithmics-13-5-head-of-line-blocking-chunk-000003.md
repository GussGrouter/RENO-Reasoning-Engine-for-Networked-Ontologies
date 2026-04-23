# network-algorithmics-13-5-head-of-line-blocking (chunk 000003)

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
