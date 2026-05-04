# network-algorithmics-13-20-conclusions-this-chapter-has-surveyed-techniques-for-building-switches-f (chunk 000002)

Compared to PIM and iSLIP, SW-QPS is a mind-blowing result. Its per-port time complexity is
strictly O(1) without using any hardware support. Its per-port communication complexity is also O(1),
as compared to O(N ) in the cases of PIM and iSLIP. Yet, it delivers overall better throughput and delay
performance than iSLIP. It achieves all these by exploiting all relevant algorithmics techniques to the
fullest extent: randomization, hardware parallelism, and extreme pipelining (which the sliding-window
technique can arguably be viewed as).
    Larger port counts can also be handled by algorithmic techniques based on the divide-and-conquer
approach. An understanding of the actual costs of switching shows that even a simple three-stage Clos
switch works well for port sizes up to 256. However, for larger switch sizes, the Benes network, with
its combination of (2log N ) depth Delta networks, is better suited for the job. The main issue in both
these scalable fabrics is scheduling. And, in both cases, as in PIM, a complex deterministic algorithm
is finessed using simple randomization. In both the Clos and Benes networks the essential similarity
of structure allows the use of an initial randomized load-balancing step followed by deterministic path
selection from the randomized intermediate destination.
    Similar ideas are also used to reduce memory needs by either picking a random intermediate line
card or a random choice of DRAM bank to send a given packet (cell) to. The knockout switch uses
trees of randomized 2-by-2 concentrators to provide k-out-of-N fairness. Thus randomization is a sur-
prisingly important idea in switch implementations.
    It is interesting to note that almost every new switch idea described in this chapter has led to the
creation of a company. For example, Kanakia worked on shared-memory switches at Bell Labs and
then left to found Torrent. Juniper seems to have been started with Sindhu’s idea for a new fabric
based, perhaps, on the use of staging via a random intermediate line card. McKeown founded Abrizio
after the success of iSLIP. Growth Networks was started by Turner, Parulkar, and Cox to commercialize
Turner’s Benes switch idea, and it was later sold to Cisco. Dally took his ideas for deadlock-free routing
on low-dimensional meshes and moved them successfully from Cray Computers to Avici’s TSR.
    Thus, if you, dear reader, have an idea for a new folded Banyan or an inverted Clos, you, too, may be
the founder of the next great thing in networking. Perhaps some venture capitalist will soon be meeting
you in a coffee shop in Silicon Valley to make you an offer you cannot refuse.
    In conclusion for a router designer it’s better to switch than to fight, with the difficulties of designing
a high-speed bus.
