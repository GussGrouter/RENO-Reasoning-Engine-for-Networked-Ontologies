# Chunk 000003

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Slice: 2.3.1 Endnode architecture
- From: processed/code/network-algorithmics-2-3-1-endnode-architecture.md

---
2.3 Network device architectures                   35




FIGURE 2.9
Using parallel connections within an endnode architecture to allow concurrent processing and network traffic via a
parallel switch.



by issuing multiple instructions concurrently. While these innovations (see, for example, the classic
reference on endnode architecture [Hennessey and Patterson, 1996]) remove computation bottlenecks,
they do little for data-movement bottlenecks. Consider the following speculative architecture instead.

Example 6. Endnode Architecture Using a Crossbar Switch: Fig. 2.9 shows the endnode bus being
replaced by a programmable hardware switch, as is commonly used by routers. The switch internally
contains a number of parallel buses so that any set of disjoint endpoint pairs can be connected in parallel
by the switch. Thus in the figure, the processor is connected to Memory 1, while the network adaptor is
connected to Memory 2. Thus packets from the network can be placed in Memory 2 without interfering
with the processor’s reading from Memory 1. If the processor now wishes to read the incoming packet,
the switch can be reprogrammed to connect the processor to Memory 2 and the adaptor to Memory 1.
This can work well if the queue of empty packet buffers used by the adaptor alternates between the two
memories.
    There are recent proposals for Infiniband switch technology to replace the I/O bus in processors
(Chapter 5). The ultimate message of this example is not that architectures such as Fig. 2.9 are nec-
essarily good but that simple architectural idea to improve network performance, such as Fig. 2.9,
are not hard for even protocol designers to conceive, given simple models of hardware and architec-
ture.
