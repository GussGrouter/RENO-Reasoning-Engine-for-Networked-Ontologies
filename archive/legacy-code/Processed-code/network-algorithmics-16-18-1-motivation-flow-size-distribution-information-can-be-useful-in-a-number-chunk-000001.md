# network-algorithmics-16-18-1-motivation-flow-size-distribution-information-can-be-useful-in-a-number (chunk 000001)

# Network Algorithmics — 16.18.1 Motivation Flow-size distribution information can be useful in a number of applications in network measurement (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 510
- Slice: from `16.18.1 Motivation Flow-size distribution information can be useful in a number of applications in network measurement` up to next detected section heading

---

16.18.1 Motivation
Flow-size distribution information can be useful in a number of applications in network measurement
and monitoring. First, flow-size distribution information may allow Internet service providers to infer
the usage pattern of their networks, such as the approximate number of users with dial-up or broadband
access. Such information on usage patterns can be important for the purpose of pricing, billing, infras-
tructure engineering, and resource planning. In addition, network operators may also infer the type of
applications that are running over a network link without looking into the details of traffic, such as how
many customers are using streaming music, streaming video, and voice over IP. Over the years, more
and more network applications have become recognizable through flow-distribution information.
    Second, flow-size distribution information can help locally detect the existence of an event that
causes the transition of the global network dynamics from one mode to another. An example of such
mode transition is a sudden increase in the number of large flows (i.e., elephants) in a link. Possible
events that may cause this include link failure or route flapping. Merely looking at the total load of the
link may not detect such a transition since this link could be consistently heavily used anyway.

484      Chapter 16 Measuring network traffic

Third, flow-size distribution information may also help us detect various types of Internet security
attacks, such as DDoS and Internet worms. In the case of DDoS attacks, if the attackers are using
spoofed IP addresses, we will observe a significant increase in flows of size 1. In the case of Internet
worms, we may suddenly find a large number of flows of a particular size in Internet links around the
same time if the worm is a naive one that does not change in size. Also, the historical flow-distribution
information stored at various links may help us study its evolution over time.
