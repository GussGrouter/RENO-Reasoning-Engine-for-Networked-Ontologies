# network-algorithmics-14-16-3-edge-aggregation-with-policing (chunk 000005)

The techniques described in this chapter (and the corresponding principles invoked) are summarized
in Table 15.1.
    In all four examples in this chapter the focus is not merely on performance but also on the use of
design and reasoning techniques from distributed algorithms to produce solutions that gain performance
without sacrificing reliability. The techniques used to gain reliability include periodic synchronization
of key invariants and centralizing asynchronous computation to avoid race conditions. Counterexamples
are also given to show how easily the desire to gain performance can lead, without care, to obscure
failure modes that are hard to debug.
    The sample of internal distributed algorithms presented in this chapter is necessarily incomplete.
An important omission is the use of failure detectors to detect and swap out failed boards, switching
fabrics, and power supplies.

Quick reference guide
   It is important for an implementor to learn how to make link flow control reliable, as described in Section 15.1.2. Im-
   plementors are increasingly turning to striping within networking devices. Solutions for link striping are described in
   Section 15.2. Solutions for striping across DRAMs while maintaining guarantees are described in Section 15.3.
