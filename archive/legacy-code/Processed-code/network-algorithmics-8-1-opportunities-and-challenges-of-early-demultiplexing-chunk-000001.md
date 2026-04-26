# network-algorithmics-8-1-opportunities-and-challenges-of-early-demultiplexing (chunk 000001)

# Network Algorithmics — 8.1 Opportunities and challenges of early demultiplexing (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 224
- Slice: from `8.1 Opportunities and challenges of early demultiplexing` up to next detected section heading

---

8.1 Opportunities and challenges of early demultiplexing
Why is early demultiplexing a good idea? The following basic motivations were discussed in Chapter 6.
• Flexible User-Level Implementations: The original reason for early demultiplexing was to allow
  flexible user-level implementation of protocols without excessive context switching.
• Efficient User-Level Implementations: As time went on, implementors realized that early demulti-
  plexing could also allow efficient user-level implementations by minimizing the number of context
  switches. The main additional trick was to structure the protocol implementation as a shared library
  that can be linked to application programs.
Note that with the advent of receive packet steering primitives for TCP packets, user level implementa-
tions can easily be done today for TCP. However, there are other advantages of early demultiplexing.
• Prioritizing Packets: Early demultiplexing allows important packets to be prioritized and unnec-
  essary ones to be discarded quickly. For example, Chapter 6 shows that the problem of receiver
  livelock can be mitigated by early demultiplexing of received packets to place packets directly on
  a per-socket queue. This allows the system to discard messages for slow processes during over-
  load while allowing better-behaved processes to continue receiving messages. More generally, early
  demultiplexing is crucial in providing quality-of-service guarantees for traffic streams via service
  differentiation. If all traffic is demultiplexed into a common kernel queue, then important packets
  can get lost when the shared buffer fills up in periods of overload. Routers today do packet classi-
  fication for similar reasons (Chapters 12 and 14). Early demultiplexing allows explicit scheduling
  of the processing of data flows; scheduling and accounting can be combined to prevent anomalies
  such as priority inversion.
• Specializing Paths: Once the path for a packet is known, the code can be specialized to process the
  packet because the wider context is known. For example, rather than having each layer protocol
  check for packet lengths, this can be done just once in the spirit of P1, avoiding obvious waste.
  The philosophy of paths is taken to its logical conclusion in Mosberger and Peterson (1996), who
  describe an operating system in which paths are first-class objects.
• Fast Dispatching: This chapter and Chapter 6 have already described an instance of this idea using
  packet filters and user-level protocol implementations. Early demultiplexing avoids per-layer mul-
  tiplexing costs; more importantly, it avoids the control overhead that can sometimes be incurred in
  delayered multiplexing.

198      Chapter 8 Demultiplexing
