# Network Algorithmics — caveats (3.5) (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Extraction: pdftotext -f 90 -l 105 -layout
- Slice: from `3.5 Caveats` up to (excluding) `3.6 Summary`

---

3.5 Caveats            67




FIGURE 3.9
Retrieval of a Web page with images typically requires one request to get the page that specifies the needed images
and more requests to retrieve each specified image. Why not have the Web server download the images directly?

implementation principles (e.g., “use hints” and “optimize the expected case”). This book, by contrast,
assumes that much of the network design is already given, and so we focus on principles for efficient
protocol implementation. This book also adds several principles for efficient implementation not found
in Keshav (1991) or Lampson (1989).
    On the other hand, Bentley’s book on “efficient program design” (Bentley, 1982) is more about
optimizing small code segments than the large systems that are our focus; thus many of Bentley’s
principles (e.g., fuse loops, unroll loops, reorder tests) are meant to speed up critical loops rather than
speed up systems as a whole.



3.5 Caveats
                                  Performance problems cannot be solved only through the use of Zen meditation.
                                                —Paraphrased from Jeff Mogul, a computer scientist at HP Labs

The best of principles must be balanced with wisdom to understand the important metrics, with profiling
to determine bottlenecks, and with experimental measurements to confirm that the changes are really
improvements. We start with two case studies to illustrate the need for caution.

                            Case study 1: Reducing page download times
      Fig. 3.9 shows that in order for a Web client to retrieve a Web page containing images, it must
  typically send a GET request for the page. If the page specifies inline images, then the client must
  send separate requests to retrieve the images before it can display the page. A natural application
  of principle P1 is to ask why separate requests are needed. Why can’t the Web server automatically
  download the images when the page is requested instead of waiting for a separate request? This
  should reduce page download latency by at least half a round trip delay.

---

## PDF page 95

68     Chapter 3 Fifteen implementation principles



    To test our hypothesis, we modified the server software to do so and measured the resulting
 performance. To our surprise, we found only minimal latency improvement.
    Using a network analyzer based on tcpdump, we found two reasons why this seeming im-
 provement was a bad idea.
 • Interaction with TCP: Web transfer is orchestrated by TCP as described in Chapter 2. To
   avoid network congestion, TCP increases its rate slowly, starting with one packet per round-
   trip, then to two packets per round trip delay, increasing its rate when it gets acks. Since TCP
   had to wait for acks anyway to increase its rate, waiting for additional requests for images did
   not add latency.
 • Interaction with Client Caching: Many clients already cache common images, such as .gif
   files. It is a waste of bandwidth to have the Web server unilaterally download images that
   the client already has in its cache. Note that having the client request the images avoids this
   problem because the client will only request images it does not already have.
 A useful lesson from this case study is the difficulty of improving part of a system (e.g., image
 downloading) because of interactions with other parts of the system (e.g., TCP congestion control).


                  Case study 2: Speeding up signature-based intrusion detection
      As a second example, many network sites field an intrusion detection system, such as Snort
 (2001), that looks for suspicious strings in packet payloads that are characteristics of hacker at-
 tacks. An example is the string “perl.exe,” which may signify an attempt to execute perl and then
 to execute arbitrary commands on a Web server. For every potentially matching rule that contains
 a string, Snort searches for each such string separately using the Boyer–Moore algorithm (Cormen
 et al., 1990). The worst case happens to be a Web packet that matches 310 rules. Simple profiling
 using gprof reveals (Fisk and Varghese, 2001) that 30% of the overhead in Snort arises from string
 searching.
      An obvious application of P1 seemed to be the following: Instead of separate searches for each
 string, use an integrated search algorithm that searches for all possible strings in a single pass over
 the packet. We modified Boyer–Moore to a set Boyer–Moore algorithm that could search for all
 specified strings in one pass. Implemented in a library, the new algorithm performed better than
 the Snort algorithm by a factor of 50 for the full Snort database. Unfortunately, when we integrated
 it into Snort, we found almost no improvement on packet traces (Fisk and Varghese, 2001). We
 found two reasons for this.
 • Multiple string matching is not a bottleneck for the trace: For the given trace, very few
   packets matched multiple rules, each of which contained separate strings. When we used a trace
   containing only Web traffic (i.e., traffic with destination port 80), a substantial improvement
   was found.
 • Cache Effects: Integrated string searching requires a data structure, such as a trie, whose size
   grows with the number of strings being searched. The simplest way to do integrated set search-
   ing is to place the strings contained in all rules in a single trie. However, when the number

---

## PDF page 96

                                                                                   3.5 Caveats          69



      of strings went over 100, the trie did not fit in cache, and performance suffered. Thus the
      system had to be reimplemented to use collections of smaller sets that took into account the
      hardware (P4).
  A useful lesson from this case study is that purported improvements may not really target the
  bottleneck (which in the trace appears to be single-string matching) and can also interact with
  other parts of the system (the data cache).



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

Q7: Do prototypes confirm the initial promise?
Once we have successfully answered all the preceding questions, it is still a good idea to build a pro-
totype or simulation and actually test to see if the improvement is real. This is because we are dealing
with complex systems; the initial analysis rarely captures all effects encountered in practice. For ex-
ample, understanding that the Web-image-dumping idea does not improve latency (see Case Study 1)
might come only after a real implementation and tests with a network analyzer.
    A major problem is finding a standard set of benchmarks to compare the standard and new imple-
mentations. For example, in the general systems world, despite some disagreement, there are standard
benchmarks for floating-point performance (e.g., Whetstone) or database performance (e.g., debit–
credit). If one claims to reduce Web transfer latencies using differential encoding, what set of Web
pages provides a reasonable benchmark to prove this contention? If one claims to have an IP lookup
scheme with small storage, which benchmark databases can be used to support this assertion?

Q8: Will performance gains be lost if the environment changes?
Sadly, the job is not quite over even if a prototype implementation is built and a benchmark shows that
performance improvements are close to initial projections. The difficulty is that the improvement may
be specific to the particular platform used (which can change) and may take advantage of properties
of a certain benchmark (which may not reflect all environments in which the system will be used).
The improvements may still be worthwhile, but some form of sensitivity analysis is still useful for the
future.
    For example, Van Jacobson performed a major optimization of the BSD networking code that al-
lowed ordinary workstations to saturate 100-Mbps FDDI (Fiber Distributed Data Interface) rings. The

---

## PDF page 98

                                                                                 3.7 Exercises          71



optimization, which we will study in detail in Chapter 9, assumes that in the normal case the next packet
is from the same connection as the previous packet, P , and has sequence number one higher than P .
Will this assumption hold for servers that have thousands of simultaneous connections to clients? Will
it hold if packets get sent over parallel links in the network, resulting in packet reordering? Fortunately,
the code has worked well in practice for a number of years. Despite this, such questions alert us to
possible future dangers.
