# network-algorithmics-6-9-exercises-1-packet-filters-and-upcalls-in-the-description-on-upcalls-fig (chunk 000005)

TCP implementation maintains its own timers for all outstanding packets and uses a single kernel timer
as a clock to run its own timers. TCP maintains its packet timers in the simplest fashion: Whenever its
single kernel timer expires, it ticks away at all its outstanding packet timers. For example, many TCP
implementations use two timers: a 200-millisecond timer and a 500-millisecond timer.
    The naive method works reasonably well if the granularity of timers is low and losses are rare.
However, it is desirable to improve the resolution of the retransmission timer to allow speedier recovery.
For example, the University of Arizona has a TCP implementation called TCP Vegas (Brakmo et al.,
1994) that performs better than the commonly used TCP Reno. One of the reasons TCP Reno has bad
performance when experiencing losses is the coarse granularity of the timeouts.
    Besides faster error recovery, fine-granularity timers also allow network protocols to more accu-
rately measure small intervals of time. For example, accurate estimates of round trip delay are important
for the TCP congestion-control algorithm (Jacobson, 1988) and the SRM (scalable reliable multicast)
framework (Floyd et al., 1995) that is implemented in the Web conferencing tool (McCanne, 1992).
    More recently, beyond accurate round trip delay measurements, recent congestion algorithms have
been using fine grained timers. Google’s BBR algorithm (Cardwell et al., 2017), for instance, uses fine
grained pacing to reduce packet drops in the network, especially for video.
    Finally, many multimedia applications routinely use timers, and the number of such applications is
increasing. An early example can be found in Siemens’ CHANNELS run-time system for multimedia
(Boecking et al., 1995), where each audio stream uses a timer with granularity that lies between 10
and 20 milliseconds. For multimedia and other real-time applications, it is important to have worst-case
bounds on the processing time to start and stop timers.
    Besides networking applications, process control and other real-time applications will benefit from
large numbers of fine-granularity timers. Also, the number of users on a system may grow large enough
to lead to a large number of outstanding timers. This is the reason cited for redesigning the timer facility
by the developers of the IBM VM/XA SP1 operating system (Davison, 1989).
    In the following sections we will describe a family of schemes for efficient timer implementations
based on a data structure called a timing wheel. We will also survey some of the systems that have
implemented timer packages based on the ideas in this chapter.
