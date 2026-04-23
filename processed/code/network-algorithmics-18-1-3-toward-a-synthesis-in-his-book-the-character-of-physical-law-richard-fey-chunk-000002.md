# network-algorithmics-18-1-3-toward-a-synthesis-in-his-book-the-character-of-physical-law-richard-fey (chunk 000002)

by contrast, have fairly primitive operating systems (e.g., Cisco IOS) that bear some resemblance to a
real-time operating system. Most endnodes’ protocol functions are implemented (today) in software,
while the critical performance functions in a router are implemented in hardware. Endnodes compute,
routers communicate. Thus routers have no file system and no complex process scheduling.
    But there are similarities as well between endnode and router algorithmics.
• Copying in endnodes is analogous to the data movement orchestrated by switching in routers.
• Demultiplexing in endnodes is analogous to classification in routers.
• Scheduling in endnodes is analogous to fair queuing in routers.
    Other than packet classification, where the analogy is more exact, it may seem that the other cor-
respondences are a little stretched. However, these analogies suggest the following potentially fruitful
directions.
   1. Switch-based endnode architectures: The analogy between copying and switching, and the clean
separation between I/O and computation in a router, suggests that this may also be a good idea for
endnodes. More precisely, most routers have a crossbar switch that allows parallel data transfers using
dedicated ASICs or processors; packets meant for internal computation are routed to a separate set
of processors. While we considered this briefly in Chapter 2, we did not consider very deeply the
implications for endnode operating systems.
By dedicating memory bandwidth and processing to I/O streams, the main computational processors
can compute without interruptions, system calls, or kernel thread because I/O is essentially serviced and
placed in clean form by a set of I/O processors (using separate memory bandwidth that does not interfere
with the main processors) for use by the computational processors when they switch computational
tasks. With switch-based bus replacements such as Infiniband, and the increasing use of protocol offload
engines such as TCP chips, this vision is already realizable. However, while the hardware elements are
present, a fundamental restructuring of operating systems is needed to fully realize the potential of this
vision as for example in Arrakis (Peter et al., 2015) described in Chapter 6.
   2. Generalized endnode packet classification: Although there seems to be a direct correspondence
between packet classification in endnodes (Chapter 8) and packet classification in routers (Chapter 12),
the endnode problem is simpler because it works only for a constrained set of classifiers, where all
the wildcards are at the end. Router classifiers, on the other hand, allow arbitrary classifiers, requiring
more complicated algorithmic machineries or CAMs. To be fair, in recent years the packet classifiers
in Linux and other operating systems have come closer to the power of routers and in some cases have
gone beyond because of their ability to do application level filtering.
   3. Fair queuing in endnodes: Fair queuing in routers was originally invented to provide more dis-
criminating treatment to flows in times of overload and (later) to provide quality of service to flows in
terms of, say, latency. Both these issues resonate in the endnode environment. For example, the problem
of receiver livelock (Chapter 6) requires discriminating between flows during times of overload. The
use of early demultiplexing and separate IP queues per flow in lazy receiver processing seems like a
first crude step toward fair queuing. Similarly, many endnodes do real-time processing, such as running
MPEG players, just as routers have to deal with the real-time constraints of, say, voice-over-IP packets.
Thus a reasonable question is whether the work on fair schedulers in the networking community can
be useful in an operating system environment. When a sending TCP is scheduling between multiple
concurrent connections, could it use a scheduling algorithm such as DRR for better fairness? At a

518       Chapter 18 Conclusions
