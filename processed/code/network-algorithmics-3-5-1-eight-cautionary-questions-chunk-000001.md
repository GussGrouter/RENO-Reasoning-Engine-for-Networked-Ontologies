# network-algorithmics-3-5-1-eight-cautionary-questions (chunk 000001)

# Network Algorithmics — 3.5.1 Eight cautionary questions (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 96
- Slice: from `3.5.1 Eight cautionary questions` up to next detected section heading

---

3.5.1 Eight cautionary questions
In the spirit of the two case studies, here are eight cautionary questions that warn against the injudicious
use of the principles.

Q1: Is it worth improving performance?
If one were to sell the system as a product, is performance a major selling strength? People interested
in performance improvement would like to think so, but other aspects of a system, such as ease of use,
functionality, and robustness, may be more important. For example, a user of a network management
product cares more about features than performance. Thus, given limited resources and implementation
complexity, we may choose to defer optimizations until needed. Even if performance is important,
which performance metric (e.g., latency throughput, memory) is important?
    Other things being equal, simplicity is best. Simple systems are easier to understand, debug, and
maintain. On the other hand, the definition of simplicity changes with technology and time. Some
amount of complexity is worthwhile for large performance gains. For example, years ago image com-
pression algorithms such as MPEG were considered too complex to implement in software or hardware.
However, with increasing chip densities, many MPEG chips have come to market.

Q2: Is this really a bottleneck?
The 80–20 rule suggests that a large percentage of the performance improvements comes from op-
timizing a small fraction of the system. A simple way to start is to identify key bottlenecks for the
performance metrics we wish to optimize. One way to do so is to use profiling tools, as we did in Case
Study 2.

Q3: What impact does the change have on the rest of the system?
A simple change may speed up a portion of the system but may have complex and unforeseen effects
on the rest of the system. This is illustrated in Case Study 1. A change that improves performance but
has too many interactions should be reconsidered.

Q4: Does the initial analysis indicate significant improvement?
Before doing a complete implementation, a quick analysis can indicate how much gain is possible.
Standard complexity analysis is useful. However, when nanoseconds are at stake, constant factors are
important. For software and hardware, because memory accesses are a bottleneck, a reasonable first-
pass estimate is the number of memory accesses.
    For example, suppose analysis indicates that address lookup in a router is a bottleneck (e.g., because
there are fast switches to make data transfer not a bottleneck). Suppose the standard algorithm takes an

70       Chapter 3 Fifteen implementation principles

average of 15 memory accesses while a new algorithm indicates a worst case of 3 memory accesses.
This suggests a factor of 5 improvement, which makes it interesting to proceed further.

Q5: Is it worth adding custom hardware?
With the continued improvement in the price–performance of general-purpose processors, it is tempting
to implement algorithms in software and ride the price–performance curve. Thus if we are considering
a piece of custom hardware that takes a year to design, and the resulting price–performance improve-
ment is only a factor of 2, it may not be worth the effort. On the other hand, hardware design times
are shrinking with the advent of effective synthesis tools. Volume manufacturing can also result in ex-
tremely small costs (compared to general-purpose processors) for a custom-designed chip. Having an
edge for even a small period such as a year in a competitive market is attractive. This has led companies
to increasingly place networking functions in silicon.
