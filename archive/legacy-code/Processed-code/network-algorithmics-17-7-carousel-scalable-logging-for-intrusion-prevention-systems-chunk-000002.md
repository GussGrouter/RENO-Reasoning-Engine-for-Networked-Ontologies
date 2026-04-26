# network-algorithmics-17-7-carousel-scalable-logging-for-intrusion-prevention-systems (chunk 000002)

Consider an application scenario in which an enterprise network containing a large number of hosts
is monitored and protected by an intrusion prevention system (IPS). We assume that the IPS, which, by
sitting in a strategic position, can “see” all the packets transiting in the network. When a widespread
security event happens to this network, the IPS is tasked with logging, to its disk or SSD (solid state
drive), every distinct IP address involved in this event and a succinct event report associated with the
IP address.
     One such security event is the infection of many of its hosts by a worm. In this event for each IP
address (host) already infected by the worm, the IPS needs to record it along with a packet sent from the
host that serves as the evidence (event report). Here for simplicity, we assume that, upon examining the
header and the content of a packet, IPS can decide whether the packet is “infectious”; if so, its source
IP address needs to be logged. Our goal in this application scenario is to design a scalable solution for
the IPS to log all these IP addresses and their associated event reports.
     For ease of presentation, in the rest of this section we use this application scenario (of assessing the
scale of a worm attack) as the context for formulating our problem. Before we can get to the gist of this
problem, however, we need to make two additional assumptions. First, we assume that each infected
source (IP address) sends out a large number of packets (trying to infect others).
     With this assumption, the naive solution of logging the source (or destination) IP address of every
“infectious” packet does not work well, since it can log an infected source many times, which can lead
to poor throughput performance, as we will elaborate shortly. In other words, a good solution needs to
somehow filter out most of the duplicates and ideally log each infected source only once.
     Second, we assume that each infected source is persistent in the sense that it will send out “infec-
tious” packets for a relatively long period of time. This is really an “enabling” assumption in the sense
that without the assumption, it appears hard, if not impossible, to design an elegant solution to our
problem, as we will explain shortly. On the other hand, this assumption is also reasonable for this appli-
cation for the following reason. The very purpose for logging infected sourcess is to “neutralize” and if
possible remediate such sources. If an infected source has stopped sending packets, it no longer poses
a clear and present danger as far as the spreading of this particular (suspected) worm is concerned. In
this case, to log its IP address is less important than logging those persisent sources (worm spreaders).
     We now make our first attempt at formulating the problem using the data streaming language we
have introduced in Section 16.15. Consider a stream of data items, each of which is the source IP
address of an infectious packet, that arrive at the IPS at a very high rate. With high probability, each
such IP address appears many times (the first additional assumption above) and does so persistently (the
second additional assumption above) in the stream. Our problem is for the IPS to gather a near-complete
list of such IP addresses after performing one-pass processing of the data stream. This problem is
intuitively more difficult than the problem of counting the number of distinct elements (explained in
Section 16.16): here we need to write down the list of distinct elements.
     Like many other network algorithmics problems, this problem would be trivial if we did not have
stringent performance expectations for an ideal solution. In this case our expectations, to be stated next,
are reasonable with respect to the resource constraints of the system.
     Suppose the total number of such IP addresses is a large number N and the bandwidth of the disk
in the IPS is b. Suppose the IPS has certain resource constraints (which we will elaborate shortly)
that prevent various clever “smoothing” or “work amortization” tricks (e.g., via caching or buffering in
memory) from being used to speed up this logging task. Then intuitively an ideal solution can attain
no more than a maximum “throughput” of b, so it would need at least N/b amount of time to log the
