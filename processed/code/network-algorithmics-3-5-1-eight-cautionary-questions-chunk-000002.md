# network-algorithmics-3-5-1-eight-cautionary-questions (chunk 000002)

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

3.7 Exercises          71

optimization, which we will study in detail in Chapter 9, assumes that in the normal case the next packet
is from the same connection as the previous packet, P , and has sequence number one higher than P .
Will this assumption hold for servers that have thousands of simultaneous connections to clients? Will
it hold if packets get sent over parallel links in the network, resulting in packet reordering? Fortunately,
the code has worked well in practice for a number of years. Despite this, such questions alert us to
possible future dangers.
