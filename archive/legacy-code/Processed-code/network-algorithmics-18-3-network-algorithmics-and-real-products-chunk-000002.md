# network-algorithmics-18-3-network-algorithmics-and-real-products (chunk 000002)

• Fast copies: Flash-lite uses IO-Lite to avoid redundant copies.
• Process scheduling: Flash uses an event-driven server with helper processes to minimize scheduling
  and maximize concurrency.
• Fast select: Flash uses an optimized implementation of the select() call.
• Other optimizations: Flash caches response headers and file mappings.

System Example 2: Cisco 12000 GSR router
The Cisco GSR (Cisco Systems, 2001c) is a popular gigabit router and uses the following ideas from
router algorithmics.
• Fast IP lookups: The GSR uses a multibit tree to do IP lookups.
• Fast switching: The GSR uses the iSLIP algorithm for fast bipartite matching of VOQs.
• Fair queuing: The GSR implements a modified form of DRR called MDRR, where one queue
  is given priority (e.g., for voice-over-IP). It also implements a sophisticated form of RED called
  weighted RED and token buckets. All these algorithms are implemented in hardware.
