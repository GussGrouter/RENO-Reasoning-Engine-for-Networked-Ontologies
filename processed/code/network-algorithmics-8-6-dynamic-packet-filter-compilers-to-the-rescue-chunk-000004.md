# network-algorithmics-8-6-dynamic-packet-filter-compilers-to-the-rescue (chunk 000004)

Technology changes can invalidate design assumptions
      There are several examples of innovations in architecture and operating systems that were
  discarded after initial use and then returned to be used again. While this may seem like the whims
  of fashion (“collars are frilled again in 1995”) or reinventing the wheel (“there is nothing new
  under the sun”), it takes a careful understanding of current technology to know when to dust off
  an old idea, possibly even in a new guise.
      Take, for example, the core of the telephone network used to send voice calls via analog sig-
  nals. With the advent of fiber optics and the transistor, much of the core telephone network now
  transmits voice signals in digital formats using the T1 and SONET hierarchies. However, with the
  advent of wavelength-division multiplexing in optical fiber, there is at least some talk of returning
  to analog transmission.
      Thus the good system designer must constantly monitor available technology to check whether
  the system design assumptions have been invalidated. The idea of using dynamic compilation was
  mentioned by the CSPF designers in Mogul et al. (1987) but was not considered further. The CSPF
  designers assumed that tailoring code to specific sets of filters (by recompiling the classifier code
  whenever a filter was added) was too “complicated.”
      Dynamic compilation at the time of the CSPF design was probably slow and also not portable
  across systems; the gains at that time would have also been marginal because of other bottlenecks.
  However, by the time DPF was being designed, a number of systems, including VCODE (Engler,
  1996), had designed fairly fast and portable dynamic compilation infrastructure. The other clas-
  sifier implementations in DPF’s lineage had also eliminated other bottlenecks, which allowed the
  benefits of dynamic compilation to stand out more clearly.
