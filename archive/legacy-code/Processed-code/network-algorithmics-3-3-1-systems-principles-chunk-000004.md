# network-algorithmics-3-3-1-systems-principles (chunk 000004)

both memory and speed may be improved. The Lulea IP-lookup algorithm described in Chapter 11
  uses this idea by using sparse arrays that can still be looked up efficiently using space-efficient
  bitmaps.
• P4c: Exploit Hardware Features. Compilers use strength reduction to optimize away multipli-
  cations in loops; for example, in a loop where addresses are 4 bytes and the index i increases
  by 1 each time, instead of computing 4 ∗ i, the compiler calculates the new array index as be-
  ing 4 higher than its previous value. This exploits the fact that multiplies are more expensive
  than additions on many modern processors. Similarly, it pays to manipulate data in multiples of
  the machine word size, as we will see in the fast IP-checksum algorithms described in Chap-
  ter 9.
    If this principle is carried too far, the modularity of the system will be in jeopardy. Two techniques
alleviate this problem. First, if we exploit other system features only to improve performance, then
changes to those system features can only affect performance and not correctness. Second, we use this
technique only for system components that profiling has shown to be a bottleneck.

P5: Add hardware to improve performance
When all else fails, goes the aphorism, use brute force. Adding new hardware,3 such as buying a faster
processor, can be simpler and more cost effective than using clever techniques. Besides the brute-force
approach of using faster infrastructure (e.g., faster processors, memory, buses, links), there are cleverer
hardware–software trade-offs. Since hardware is less flexible and has higher design costs, it pays to add
the minimum amount of hardware needed.
    Thus baking at the Greasy Spoon was sped up using microwave ovens. In computer systems, dra-
matic improvements each year in processor speeds and memory densities suggest doing key algorithms
in software and upgrading to faster processors for speed increases. But computer systems abound with
cleverer hardware–software trade-offs.
    For example, in a multiprocessor system, if a processor wishes to write data, it must inform any
“owners” of cached versions of the data. This interaction can be avoided if each processor has a piece
of hardware that watches the bus for write transactions by other processors and automatically inval-
idates the cached location when necessary. This simple hardware snoopy cache controller allows the
remainder of the cache-consistency algorithm to be efficiently performed in software.
    Decomposing functions between hardware and software is an art in itself. Hardware offers several
benefits. First, there is no time required to fetch instructions: Instructions are effectively hardcoded.
Second, common computational sequences (which would require several instructions in software) can
be done in a single hardware clock cycle. For example, finding the first bit set in, say, a 32-bit word
may take several instructions on a RISC machine but can be computed by a simple priority encoder, as
shown in the previous chapter.
    Third, hardware allows you to explicitly take advantage of parallelism inherent in the problem.
Finally, hardware manufactured in volume may be cheaper than a general-purpose processor. For ex-
ample, a Pentium may cost $100, while an ASIC in volume with similar speeds may cost $10.

3 By contrast, Principle P4 talks about exploiting existing system features, such as the existing hardware. Of course, the distinc-
tion between principles tends to blur and must be taken with a grain of salt.

---

## PDF page 89

62       Chapter 3 Fifteen implementation principles
