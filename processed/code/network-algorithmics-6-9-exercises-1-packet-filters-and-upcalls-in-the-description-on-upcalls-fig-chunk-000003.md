# network-algorithmics-6-9-exercises-1-packet-filters-and-upcalls-in-the-description-on-upcalls-fig (chunk 000003)

A timer module in a system is analogous to a secretary who keeps track of all the appointments of
a busy executive. The executive tells the secretary to schedule appointments and sometimes to cancel
appointments before they occur. It is the secretary’s job to interrupt the executive with a warning just
before the scheduled time of an appointment. Many secretaries actually do this using a so-called tickler
file, which is a moving window over the next N days. When the day’s appointments are done, the tickler
file is rolled to bypass the current day. We will find a strong analogy between a tickler file and a timing
wheel, the main data structure of this chapter.
     The chapter is organized as follows. Section 7.1 describes why timers are needed. Section 7.2
describes a model of a timer routine and the relevant parameters that are critical for performance.
Section 7.3 describes the simplest techniques for maintaining timers, some of which are still appropri-
ate in some cases. Section 7.4 introduces the main data structure, called timing wheels. This is followed
by two specific instantiations of timing wheels called hashed wheels (in Section 7.5) and hierarchical
timing wheels (in Section 7.6). The chapter ends with a technique called soft timers (Section 7.9) that re-
duces timer overhead by amortizing timer maintenance across other system calls. Table 7.1 summarizes
the principles applied in the various timer schemes.
     When compared to the first edition, probably the most notable change has been the hundreds of
thousands of fine granularity timers (Saeed et al., 2017) that are now routinely used in hosts in clouds
to provide bandwidth isolation for Virtual Machine traffic via traffic shaping, and for modern congestion
control algorithms like BBR (Cardwell et al., 2017) that do fine-graining pacing to reduce packet drops.
These new applications make a stronger case for the use of the main data structure in this chapter (timing
wheels), and the need for even more streamlined timer implementations in multicore machines.

Quick reference guide
    The most useful section for an implementor may be Section 7.5 on hashed timing wheels, versions of which have appeared
    in many operating systems, such as FreeBSD and in Google machines as part of the Carousel (Saeed et al., 2017) traffic
    shaping software. Linux used hierarchical timing wheels (Section 7.6) in early versions, as well as in a recent version that
    is more efficient but offers less precise timers (Corbet, 2015).

Network Algorithmics. https://doi.org/10.1016/B978-0-12-809927-8.00013-0
Copyright © 2022 Elsevier Inc. All rights reserved.
                                                                                                                                 179

180      Chapter 7 Maintaining timers

Table 7.1 Principles used by the timer schemes described
                      in this chapter.
                      Number             Principle               Timer technique
                      P14    Use array to store bounded timers Basic timing wheels
                      P2c, 4 Leverage off time-of-day update
                      P15    Using hashing or hierarchies      Hashed, hierarchical
                                                               timing wheels
                      P10    Pass handle to delete timer       Any timer scheme
                      P4     Leverage off system calls, etc.   Soft timers
                      P3     Relax need for accurate timers
                      P11    Optimize for fast timers
