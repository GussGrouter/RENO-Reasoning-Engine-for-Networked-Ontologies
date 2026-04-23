# Network Algorithmics — 6.7.1 Avoiding receiver livelock (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 200
- Slice: from `6.7.1 Avoiding receiver livelock` up to next detected section heading

---

6.7.1 Avoiding receiver livelock
Besides inefficiencies due to the cost of handling interrupts, interrupts can interact with operating sys-
tem scheduling to drive end-system throughput to zero, a phenomenon known as receiver livelock.
Recall that in Example 8 of Chapter 2 we showed that in BSD UNIX the arrival of a packet generates
an interrupt. The processor then jumps to the interrupt handler code, bypassing the scheduler, for speed.
The interrupt handler copies the packet to a kernel queue of IP packets waiting to be consumed, makes
a request for an operating system thread (called a software interrupt), and exits.
    Recall also that under high network load, the computer can enter what is called receiver livelock
(Mogul and Ramakrishnan, 1997), in which the computer spends all its time processing incoming
packets, only to discard them later because the applications never run. If there is a series of back-to-
back packet arrivals, only the highest-priority interrupt handler will run, possibly leaving no time for
the software interrupt and certainly none for the browser process. Thus either the IP or socket queues
will fill up, causing packets to be dropped after resources have been invested in their processing.
    Many of these ideas are now part of the Linux NAPI processing framework (Salim et al., 2001).
When the network adaptor or NIC receives a packet, it generates an Interrupt Request (IRQ) to the
driver and selects a CPU core to process the new data using a packet steering mechanism that either
distributes load using a hash of the TCP 4-tuple (Receive Packet Steering or RPS), or sends the packet

174        Chapter 6 Transferring control



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
