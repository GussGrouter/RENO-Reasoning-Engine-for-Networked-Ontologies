# Network Algorithmics — 16.1.1 Why counting is hard (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 479
- Slice: from `16.1.1 Why counting is hard` up to next detected section heading

---

16.1.1 Why counting is hard
Legacy routers provide only per-interface counters that can be read by the management protocol SNMP.
Such counters count only the aggregate of all counters going on an interface and make it difficult to
estimate traffic AS–AS matrices that are needed for traffic engineering. They can also be used only for
crude forms of accounting, as opposed to more sophisticated forms of accounting that count by traffic
type (e.g., real-time traffic may be charged higher) and destination (some destinations may be routed
through a more expensive upstream provider).
    Thus, vendors have introduced filter-based accounting, which enables customers to count traffic that
matches a rule specifying a predicate on packet header values. Similarly, Cisco provides NetFlow-based
accounting (Cisco netflow, 2001b), where sampled packets can be logged for later analysis, and 5-tuples
can be aggregated and counted on the router. Cisco also provides Express Forwarding commands, which
allow per-prefix counters (Cisco, 2001a).
    Per-interface counters can easily be implemented because there are only a few counters per inter-
face, which can be stored in chip registers. However, doing filter-based or per-prefix counters is more
challenging because of the following.
• Many counters: Given that even current routers support 500,000 prefixes and that future routers
  may have a million prefixes, a router potentially needs to support millions of real-time counters.
• Multiple counters per packet: A single packet may result in updating more than one counter, such
  as a flow counter and a per-prefix counter.
• High speeds: Line rates have been increasing from OC-192 (10 Gbps) to OC-768 (40 Gbps). Thus
  each counter matched by a packet must be read and written in the time taken to receive a packet at
  line speeds.
• Large widths: As line speeds get higher, even 32-bit counters overflow quickly. To prevent the
  overhead of frequent polling, most vendors now provide 64-bit counters.
    One million counters of 64 bits each require a total of 64 Mbits of memory, while two counters
of 64 bits each every 8 nanoseconds require 16 Gbps of memory bandwidth. The memory-bandwidth

1 Recall the comment by hardened battle veterans about the heroic Charge of the Light Brigade: “It is beautiful, but is it war?”

                               16.2 Reducing SRAM width using DRAM backing store                              453




FIGURE 16.1
Basic model for packet counting at high speeds using a large-width counter for each of a large number of flows.


needs require the use of SRAM, but the large amount of memory needed makes SRAM of this size
too expensive. Thus, maintaining counters or packet logs at wire speeds is as challenging as other
packet-processing tasks, such as classification and scheduling; it is the focus of much of this chapter.
    In summary, this section argues that: (i) packet counters and logs are important for network mon-
itoring and analysis; and (ii) naive implementations of packet counting and logs require potentially
infeasible amounts of fast memory. The remainder of this chapter describes the use of algorithmics to
reduce the amount of fast memory and processing needed to implement counters and logs.
