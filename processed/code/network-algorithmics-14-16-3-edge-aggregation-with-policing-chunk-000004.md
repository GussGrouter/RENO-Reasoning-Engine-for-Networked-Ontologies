# network-algorithmics-14-16-3-edge-aggregation-with-policing (chunk 000004)

Distributed systems are clearly evil things. They are subject to a lack of synchrony, a lack of assurance,
and a lack of trust. Thus in a distributed system, the time to receive messages can vary widely; messages
can be lost and servers can crash, and when a message does arrive, it could even contain a virus. In
Lamport’s well-known words a distributed system is “one in which the failure of a computer you didn’t
even know existed can render your own computer unusable.”
    Of course, the main reason to use a distributed system is that people are distributed. It would perhaps
be unreasonable to pack every computer on the Internet into an efficiency apartment in upper Manhat-
tan. But a router? Behind the gleaming metallic cage and the flashing lights, surely there lies an orderly
world of synchrony, assurance, and trust.
    On the contrary, this chapter argues that, as routers (recall routers include general interconnect
devices such as also switches and gateways) get faster, the delay between router components increases
in importance when compared to message-transmission times. The delay across links connecting router
components can also vary significantly. Finally, availability requirements make it infeasible to deal
with component failures by crashing the entire router. With the exception of trust, trust arguably exists
between router components, a router is a distributed system. Thus within a router, it makes sense to use
techniques developed to design reliable distributed systems.
    To support this thesis, this chapter considers four sample phenomena that commonly occur
within most high-performance interconnect devices, flow control, striping across links, striping across
DRAMs, and asynchronous data structure updates. In each case the desire for performance leads to
intuitively plausible schemes. However, the combination of failure and asynchrony can lead to subtle
interactions.
    Thus a second thesis of this chapter is that the use of distributed algorithms within routers requires
careful analysis to ensure reliable operation. While this is trite advice for protocol designers (who
ignore it anyway), it may be slightly more novel in the context of a router’s internal microcosm.
    The chapter is organized as follows. Section 15.1 motivates the need for flow control on long chip-
to-chip links and describes solutions that are simpler than, say, transmission control protocol’s (TCP)
window flow control. Section 15.2 motivates the need for internal striping across links and fabrics to
gain throughput and presents solutions that restore packet ordering after striping. Section 15.3 moti-
vates the need for further internal striping across DRAMs at high packet rates. Section 15.4 details the
difficulties of performing asynchronous updates on data structures that run concurrently with search
operations.
Network Algorithmics. https://doi.org/10.1016/B978-0-12-809927-8.00022-1
Copyright © 2022 Elsevier Inc. All rights reserved.
                                                                                                         429

430       Chapter 15 Routers as distributed systems

Table 15.1 Principles used in the various distributed systems techniques
               (for use within a router) discussed in this chapter.
               Number                        Principle                                       Used in
               P1     Avoid waste caused by partitioned buffers                       Internal flow control
               P13    Exploit degrees of freedom by decoupling logical from           Internal striping
                      physical reception
               P5c    Make fast buffers out of banks of DRAM with a DRAM              Distributed Memory
                      cache
               P3     Relax binary search requirements to allow duplicate             Binary search update
                      key values
