# network-algorithmics-9-4-1-efficient-reassembly (chunk 000003)

main trick is to fit the computation to the underlying machine architecture, using large word lengths,
lazy checks for carries, and even parallelism. The optimizations for TCP, UDP, and reassembly are all
based on optimizing simple expected cases (e.g., FIFO receipt, no errors) that cut through a welter of
corner cases that the protocol must check for but rarely occur. Table 9.1 presents a summary of the
techniques used in this chapter together with the major principles involved.
    Beyond the specific techniques, there are some general lessons to be gleaned. First, when consider-
ing the buffer-stealing algorithm, it is tempting to believe that finding the user with the largest buffer
allocation requires a heap, which requires logarithmic time. However, as with timing wheels in Chap-
ter 7, McKenney’s algorithm exploits the special case that buffer sizes only increase and decrease by 1.
    The general lesson is that for algorithmics, special cases matter. Theoreticians know this well; for
example, the general problem of finding a Hamiltonian cycle (Cormen et al., 1990) is hard for general
graphs but is trivial if the graph is a ring. In fact, the practitioner of algorithmics should look for
opportunities to change the system to permit special cases that permit efficient algorithms.
    Second, the dynamic threshold scheme shows how important it is to optimize one’s degrees of
freedom (P13), especially when considering dynamic instead of static values for parameters. This is a
very common evolutionary path in many protocols: for example, collision-avoidance protocols evolved
from using fixed backoff times to using dynamic backoff times in Ethernet; transport protocols evolved
from using fixed window sizes to using dynamic window sizes to adjust to congestion; finally, the
dynamic threshold scheme of this chapter shows the power of allowing dynamic buffer thresholds.
    Third, the discussion of techniques for buffer sharing shows why algorithmics, at least in terms of
abstracting common networking tasks and understanding a wide spectrum of solutions for these tasks,
can be useful. For example, when writing this chapter, it became clear that buffer sharing is also part of
many credit-based protocols, such as Ozveren et al. (1994) (see the protocol in Chapter 15), except that
in such settings a sender is allocating buffer space at a distant receiver. Isolating the abstract problem
is helpful because it shows, for instance, that the dynamic threshold scheme of Choudhury and Hahne
can provide finer grain buffer sharing than the technique of Ozveren et al. (1994).
    Finally, the last lesson from header prediction and fast reassembly is that attempts to design new
protocols for faster implementation can often be countered by simpler implementations. In particu-
lar, arguing that a protocol is “complex” is often irrelevant if the complexities can be finessed in the
expected case.
    As a second example, a transport protocol (Sabnani and Netravali, 1989) was designed to allow
efficient sequence number processing for protocols that used large windows and could handle out-of-
order delivery. The protocol embedded concepts such as chunks of contiguous sequence numbers into
the protocol for this purpose. Simple implementation tricks described in the patent (Thomas et al.,
1992) can achieve much the same effect, using large words to effectively represent chunks without
redesigning the protocol.
    Thus history teaches that attempts to redesign protocols for efficiency (as opposed to more func-
tionality) should be viewed with some skepticism.
