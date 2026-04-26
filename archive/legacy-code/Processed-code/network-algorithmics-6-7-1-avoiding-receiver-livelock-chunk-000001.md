# network-algorithmics-6-7-1-avoiding-receiver-livelock (chunk 000001)

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
