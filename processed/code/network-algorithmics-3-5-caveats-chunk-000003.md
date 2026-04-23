# network-algorithmics-3-5-caveats (chunk 000003)

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

---

## PDF page 97

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

Q6: Can protocol changes be avoided?
Through the years there have been several proposals denouncing particular protocols as being inef-
ficient and proposing alternative protocols designed for performance. For example, in the 1980s, the
transport protocol TCP was considered “slow” and a protocol called XTP (Chesson, 1989) was explic-
itly designed to be implemented in hardware. This stimulated research into making TCP fast, which
culminated in Van Jacobson’s fast implementation of TCP (Clark et al., 1989) in the standard BSD
(Berkeley software distribution) release. More recently, proposals for protocol changes (e.g., tag and
flow switching) to finesse the need for IP lookups have stimulated research into fast IP lookups.
