# Network Algorithmics — performance environment and measures (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Extraction: pdftotext -f 47 -l 49 -layout
- Slice: from `2.1.3 Performance environment and measures` up to (excluding) `Case Study 1`

---

## PDF page 47

2.1.3 Performance environment and measures
This section describes some important measures and performance assumptions. Consider a system
(such as a network or even a single router) where jobs (such as messages) arrive and, after completion,
leave. The two most important metrics in networks are throughput and latency. Throughput roughly
measures the number of jobs completed per second. Latency measures the time (typically the worst
case) to complete a job. System owners (e.g., ISPs, routers) seek to maximize throughput to maximize
revenues, while users of a system want end-to-end latencies lower than a few hundred milliseconds.
Latency also affects the speed of computation across the network, as, for example, in the performance
of a remote procedure call.
    The following performance-related observations about the Internet milieu are helpful when consid-
ering implementation trade-offs.
• Link Speeds: Backbone links are upgrading to 10 Gbps and 40 Gbps, and local links are upgrading
  to gigabit speeds. However, wireless and home links are currently orders of magnitude slower.
• TCP and Web Dominance: Web traffic accounts for over 70% of traffic in bytes or packets. Similarly,
  TCP accounts for 90% of traffic in a recent study (Braun, 1998).
• Small Transfers: Most Web documents accessed are small; for example, a SPEC (Carlton, 1996)
  study shows that 50% of accessed files are 50 kilobytes (KB) or less.
• Poor Latencies: Real round-trip delays exceed speed-of-light limitations; measurements in Crovella
  and Carter (1995) report a mean of 241 msec across the United States compared to speed-of-light
  delays of less than 30 msec. Increased latency can be caused by efforts to improve throughput, such
  as batch compression at modems and pipelining in routers.
• Poor Locality: Backbone traffic studies (Thompson et al., 1997) show 250,000 different source–
  destination pairs (sometimes called flows) passing through a router in a very short duration. More
  recent estimates show around a million concurrent flows. Aggregating groups of headers with the
  same destination address or other means does not reduce the number of header classes significantly.
  Thus locality, or the likelihood of computation invested in a packet being reused on a future packet,
  is small.
• Small Packets: Thompson et al. (1997) also show that roughly half the packets received by a router
  are minimum-size 40-byte TCP acknowledgments. To avoid losing important packets in a stream

---

## PDF page 48

2.1 Protocols             21



  of minimum-size packets, most router- and network-adaptor vendors aim for “wire-speed forward-
  ing”—this is the ability to process minimum-size (40-byte) packets at the speed of the input link.1
• Critical Measures: It is worth distinguishing between global performance measures, such as end-
  to-end delay and bandwidth, and local performance measures, such as router lookup speeds. While
  global performance measures are crucial to overall network performance, this book focuses only on
  local performance measures, which are a key piece of the puzzle. In particular, this book focuses on
  forwarding performance and resource (e.g., memory, logic) measures.
• Tools: Most network management tools, such as HP’s OpenView, deal with global measures. The
  tools needed for local measures are tools to measure performance within computers, such as profiling
  software. Examples include Rational’s Quantify (http://www.rational.com) for application soft-
  ware, Intel’s VTune (www.intel.com/software/products/vtune/), and even hardware oscilloscopes.
  Network monitors such as tcpdump (www.tcpdump.org) are also useful.
