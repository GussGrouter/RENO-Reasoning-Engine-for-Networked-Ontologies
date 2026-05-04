# Network Algorithmics — 6.5.1 The virtual interface architecture proposal (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 196
- Slice: from `6.5.1 The virtual interface architecture proposal` up to next detected section heading

---

6.5.1 The virtual interface architecture proposal
VIA (Compaq, Intel, and Microsoft Corporations, 1997) was a commercial standard that advocated the
ideas in ADCs. The term virtual interface makes sense because one can think of an ADC as providing
each application with its own virtual interface that it can manipulate without kernel intervention. The
virtual interfaces are, of course, multiplexed on a single physical interface. VIA was proposed by an
industry consortium that includes Microsoft, Compaq, and Intel.
    VIA uses the following terminology that can easily be understood based on the earlier discussion.
• Registered Memory: These are regions of memory that the application uses to send and receive
  data. These regions are authorized for the application to read and write from; they are also pinned
  down to avoid paging.
• Descriptor: To send or receive a packet, the application uses a user-level library (libvia) to con-
  struct a descriptor that is just a data structure with information about the buffer, such as a pointer.
  VIA allows a descriptor to refer to multiple buffers in registered memory (for scatter–gather) and
  allows different memory protection tags. Descriptors can be added to a descriptor queue.
• Doorbells: These represent an unspecified method to communicate descriptors to the network inter-
  face. This can be done via writing part of the interface card’s memory or by triggering an interrupt
  on the card; it varies from implementation to implementation. Doorbells are pointers to descriptors,
  thus leading to a second level of indirection.
