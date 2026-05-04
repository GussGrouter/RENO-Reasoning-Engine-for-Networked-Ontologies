# network-algorithmics-3-5-caveats (chunk 000002)

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
