# network-algorithmics-6-7-1-avoiding-receiver-livelock (chunk 000002)

to the core the application is running on (Receive Flow Steering or RFS). Receive Flow Steering helps
improve data cache hit rate by steering received packets to the CPU that the application thread (that will
consume the packet) is running on. Both steering mechanisms can be accelerated using NIC hardware
(P5); the hardware version of RPS is called RSS, and the hardware version of RFS is called aRFS (Cai
et al., 2021).
    The driver then triggers NAPI polling (Salim et al., 2001) where the core polls until a certain number
of frames are received or a timer expires. For example, the default parameters described in Cai et al.
(2021) are 300 (frame limit) and 2 msec (timer). The originators of the NAPI framework explicitly
cite (Salim et al., 2001) the early ideas of Mogul and Ramakrishnan (1997)
    Another technique (Mogul and Ramakrishnan, 1997) is to turn off interrupts for a certain number
of clock ticks so that some fraction of the CPU time is reserved for non-interrupt processing. This can
be done by keeping track of how much time is spent in interrupt routines for a device and masking off
that device if the fraction spent exceeds a specified percentage of total time. However, merely doing so
can drop all packets that arrive during overload, including well-behaved and important packet flows.
    A very nice solution to this problem is described by Druschel and Banga (1996),10 who suggest
combating this problem via two mechanisms. First, they suggest using a separate queue per destination
socket instead of a single shared queue. When a packet arrives, early demultiplexing (Chapter 8) is used
to place the packet in the appropriate per-socket queue. Thus if a single socket’s queues fill up because
its application is not reading packets, other sockets can still make progress.
    The second mechanism is to implement the protocol processing at the priority of the receiving pro-
cess and as part of the context of the received process (and not a separate software interrupt). First, this
removes the unfair practice of charging protocol processing for application X to the application, Y , that
was running when the packet for X arrives. Second, it means that if an application is running slowly, its
per-socket queue fills up and its particular packets will be dropped, allowing others to progress. Third,
and most importantly, since protocol processing is done at a lower priority (application processing), it
greatly alleviates the livelock problem caused by the partial processing (i.e., protocol processing only)
of many packets without the corresponding application processing required to remove these packets
from the socket queue.
    This mechanism, called lazy receiver processing (LRP), essentially uses lazy evaluation (P2b), not
so much for efficiency but for fairness and to avoid livelock. Solutions that require less drastic changes
are described in Mogul and Ramakrishnan (1997).
