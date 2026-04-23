# Network Algorithmics — 6.7 Reducing interrupts We have worked our way down the hierarchy of control overheads from process scheduling to select (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 199
- Slice: from `6.7 Reducing interrupts We have worked our way down the hierarchy of control overheads from process scheduling to select` up to next detected section heading

---

6.7 Reducing interrupts
We have worked our way down the hierarchy of control overheads from process scheduling to select
call implementations to system calls. At the bottom of the list is interrupt overhead. While involving
less overhead than process scheduling or system calls, interrupt overhead can be substantial. Each time
a packet arrives, fielding the corresponding interrupt from the device disrupts processor pipelines and
requires some context switching to service the interrupt. There is no way to avoid interrupts completely.
However, one can reduce interrupt overhead using the following tricks.
• Interrupt only for significant events: For example, in the ADC solution, the adaptor does not
  need to interrupt the processor on every packet reception but only for the first packet received in a
  stream of packets (we can assume the application will check for more packets received) and when
  the queue of free buffer descriptors becomes empty. This can reduce interrupt overhead to 1 in N

                                                                   6.7 Reducing interrupts           173



  packets received, if N packets are received in a burst. This is just an application of batching or
  expense sharing (P2c).
  Batching is very commonly used in operating systems today not just to reduce the overhead of
  interrupts but also to reduce system call overhead using such mechanisms as jumbo frames (large
  packet sizes), and sender and receiver offloads. More details of various batching/offload mechanisms
  used in Linux can be found in (Segmentation Offloads, 2022). These include mechanisms such
  as TSO (TCP segmentation offload), GSO (Generic Sender Offload) on the send side, and GRO
  (Generic Receiver Offload) on the receive side (Segmentation Offloads).
• Polling: The idea here is that the processor (CPU) keeps checking to see if packets have arrived
  and the adaptor never interrupts. This can be more overhead than interrupt-driven processing if the
  number of packets received is low, but it can become more efficient for high throughput data streams.
  Another variation is clocked interrupts (Smith and Traw, 2001): The CPU periodically polls when a
  timer fires.
• Application controlled: An even more radical idea, once proposed by Dave Clark, is that the sender
  be able to control when the receiver interrupts by passing a bit in the packet header. For example, a
  sending FTP could set the interrupt bit only for the last data packet in a file transfer. This is another
  example of P10, passing hints in protocol headers. It is probably too radical for use. However, a
  more recent paper (Dittia et al., 1997) proposes implementing a refinement of this idea in an ATM
  chip that was indeed fabricated.
    In general, the use of batching works quite well in practice. However, in some implementations, such
as the first bridge implementation (described in Chapter 10), the use of polling is also very effective.
Thus more radical ideas, such as clocked or application-controlled interrupts, have become less useful.
Note that the RDMA (remote direct memory access) ideas described in Chapter 5 also have the great
potential advantage of removing the need for both per-packet system calls and per-packet interrupts for
a large data transfer.
