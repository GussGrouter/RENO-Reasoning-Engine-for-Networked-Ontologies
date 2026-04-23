# Network Algorithmics — 13.10 Avoiding randomization with iSLIP (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 374
- Slice: from `13.10 Avoiding randomization with iSLIP` up to next detected section heading

---

13.10 Avoiding randomization with iSLIP
Parallel iterative matching was a seminal scheme because it introduced the idea that pretty-good
bipartite matchings can be computed at reasonable computation and hardware costs with clever par-
allelization. Once that was done, just as was the case when Roger Bannister first ran the mile in under
four minutes, others could make further improvements. But, PIM has two potential problems. First,
it uses randomization, and it may be hard to produce a reasonable source of random numbers at very
high speeds.2 Second, it requires a logarithmic number of iterations to attain maximal matches. Given
that each of a logarithmic number of iterations takes three phases and that the entire matching decision
must be made within a minimum packet arrival time, it would be better to have a matching scheme that
comes close to maximal matchings in just one or two iterations.
    iSLIP is a very popular and influential scheme that essentially “derandomizes” PIM and also
achieves very close to maximal matches after just one or two iterations. The basic idea is extremely
simple. When an input port or an output port in PIM experiences multiple requests, it chooses a “win-
ning” request uniformly at random, for the sake of fairness. Whereas Ethernet provides fairness with
randomness, token rings do so using a round-robin pointer implemented by a rotating token.


2 One can argue that schemes like RED require randomness at routers, anyway. However, a poor-quality source of random
numbers in an RED implementation will be less noticeable than poor-quality random numbers within a switch fabric.

348      Chapter 13 Switching



    Similarly, iSLIP provides fairness by choosing the next winner among multiple contenders in round-
robin fashion using a rotating pointer. While the round-robin pointers can be initially synchronized and
cause something akin to HOL blocking, they tend to break free and result in maximal matchings over
the long run, at least as measured in simulation. Thus the subtlety in iSLIP is not the use of round-
robin pointers but the apparent lack of long-term synchronization among N such pointers running
concurrently.
    More precisely, each output (respectively input) maintains a pointer g initially set to the first input
(respectively output) port. When an output has to choose between multiple input requests, it chooses
the lowest input number that is equal to or greater than g. Similarly, when an input port has to choose
between multiple output-port requests, it chooses the lowest output-port number that is equal to or
greater than a, where a is the pointer of the input port. If an output port is matched to an input port X,
then the output-port pointer is incremented to the first port number greater than X in circular order (i.e.,
g becomes X + 1, unless X was the last port, in which case g wraps around to the first port number).
    This simple device of a “rotating priority” assures that each resource (output port, input port) is
shared reasonably fairly across all contenders at the cost of 2N extra log2 N pointers, in addition to the
N 2 scheduling state needed on every iteration.
    Figs. 13.8 and 13.9 show the same scenario as in Fig. 13.7 (and Fig. 13.5), but using a two-iteration
iSLIP. Since each row is an iteration of a match, each match is shown using two rows. Thus the three
rows of Fig. 13.8 show the first 1.5 matches of the scenario. Similarly, Fig. 13.9 shows the remaining
1.5 matches.
    The upper left diagram of Fig. 13.8 is identical to Fig. 13.7, in that each input port sends requests
to each output port for which it has a cell destined. However, one difference is that each output port
has a so-called grant pointer g, which is initialized for all outputs to be A. Similarly, each input has a
so-called accept pointer called a, which is initialized for all inputs to 1.
    The determinism of iSLIP causes a divergence immediately in the Grant phase. Compare the upper
middle of Fig. 13.8 with the upper middle of Fig. 13.7. For example, when output 1 receives requests
from all three input ports, it grants to A because A is the smallest input greater than or equal to g1 = A.
By contrast, in Fig. 13.7 port 1 randomly chooses input port B. At this stage, the determinism of iSLIP
seems a real disadvantage because A has sent requests to both output ports 3 and 4. Because 3 and 4
also have grant pointers g3 = g4 = A, ports 3 and 4 grant to A as well, ignoring the claims of B and C.
As before, since C is the lone requester for port 4, C gets the grant from 4.
    When the popular A gets three grants back from ports 1, 2, and 3, A accepts 1. This is because port
1 is the first output equal to greater than A’s accept pointer, aA , which was equal to 1. Similarly C
chooses 4. Having done so, A increments aA to 2, and C increments aC to 1 (1 greater than 4 in circular
order is 1). Only at this stage does output 1 increment its grant pointer, g1 , to B (1 greater than the last
successful grant) and port 4 similarly increments to A (1 greater than C in circular order).
    Note that, although ports 2 and 3 gave grants to A, they do not increment their grant pointers because
A spurned their grants. If they did, it would be possible to construct a scenario where output ports keep
incrementing their grant pointer beyond some input port I after unsuccessful grants, thereby continually
starving input port I . Note also that the match is only of size 2; thus unlike Fig. 13.7, this iSLIP scenario
can be improved by a second iteration, shown in the second row of Fig. 13.8. Notice that, at the end
of the first iteration, the matched inputs and outputs are not connected by solid lines (denoting data
transfer), as shown at the top right of Fig. 13.7. This data transfer will await the end of the final (in this
case second) iteration.

                                                    13.10 Avoiding randomization with iSLIP          349




FIGURE 13.8
One-and-a-half rounds of a sample iSLIP scenario.



    The second iteration (middle row of Fig. 13.8) starts with only inputs unmatched on previous itera-
tions (i.e., B) requesting and only to hitherto unmatched outputs. Thus B requests to 2 and 3 (and not
to 1, although B has a cell destined for 1 as well). Both 2 and 3 grant B, and B chooses 2 (the lowest
one that is greater than or equal to its accept pointer of 1). One might think that B should increment its
accept pointer to 3 (1 plus the last accepted, which was 2). However, to avoid starvation, iSLIP does
not increment pointers on iterations other than the first, for reasons that will be explained.
    Thus even after B is connected to 2, 2’s grant pointer remains at A, and B’s accept pointer remains
at 1. Since this is the final iteration, all matched pairs, including pairs, such as A, 1, matched in prior
iterations, are all connected and data transfer (solid lines) occurs.
    The third row provides some insight into how the initial synchronization of grant-and-accept point-
ers gets broken. Because only one output port has granted to A, that port (i.e., 1) gets to move on and
this time to provide priority to ports beyond A. Thus even if A had a second packet destined for 1
(which it does not in this example), 1 would still grant to B.
    The remaining rows in Figs. 13.8 and 13.9 should be examined carefully by the reader to check for
the updating rules for the grant-and-accept pointers and to check which packets are switched at each
round. The bottom line is that by, the end of the third row of Fig. 13.9, the only cell that remains to be
switched is the cell from B to 3. This can clearly be done in a fourth time slot.

350       Chapter 13 Switching




FIGURE 13.9
Last one-and-a-half rounds of the sample iSLIP scenario shown in Fig. 13.8.




FIGURE 13.10
How iSLIP avoids HOL blocking to increase throughput in the scenario of Fig. 13.6.



    Fig. 13.10 shows a summary of the final scheduling (abstracted from the internal mechanics) of the
iSLIP scenario and should be compared in terms of scheduling density with Fig. 13.6. While these are
just isolated examples, they do suggest that iSLIP (and similarly PIM) tends to waste fewer slots by
avoiding HOL blocking and computing pretty-good bipartite matchings. Note that both iSLIP and PIM
finish the same input backlog in four time slots, as opposed to six.
    Note also that, when we compare Fig. 13.8 with Fig. 13.7, iSLIP looks worse than PIM because
it requires two iterations per match for iSLIP to achieve the same match sizes as PIM does using one

                                                13.10 Avoiding randomization with iSLIP                 351



iteration per match. However, this is more illustrative of the startup penalty that iSLIP pays rather than a
long-term penalty. In practice, as soon as the iSLIP pointers desynchronize, iSLIP does very well with
just one iteration, and some commercial implementations use just one iteration: iSLIP is extremely
popular.
    One might summarize iSLIP as PIM with the randomization replaced by round-robin scheduling of
input and output pointers. However, this characterization misses two subtle aspects of iSLIP.
• Grant pointers are incremented only in the third phase, after a grant is accepted: Intuitively,
  if O grants to an input port I , there is no guarantee that I will accept. Thus if O were to increment
  its grant pointer beyond I , it can cause traffic from I to O to be persistently starved. What is even
  worse, McKeown et al. (1997) show that this simplistic round-robin scheme reduces the throughput
  to just 63% (for Bernoulli arrivals) because the pointers tend to synchronize and move in lockstep.
• All pointers are incremented only after the first iteration accept is granted: Once again, this
  rule prevents starvation, but the scenario is more subtle, which the exercises will ask you to figure
  out.
   Thus matches on iterations other than the first in iSLIP are considered a “bonus” that boosts through-
put without being counted against a port’s quota.


13.10.1 iSLIP implementation notes
The heart of the hardware implementation of iSLIP is an arbiter that chooses between N requests (en-
coded as a bitmap) to find the first one greater than, or equal to, a fixed pointer. This is what in Chapter 2
is called a programmable priority encoder; that chapter also described an efficient implementation that
is nearly as fast as a priority encoder. Switch scheduling can be done by one such grant arbiter for
every output port (to arbitrate requests) and one accept arbiter for every input port (to arbitrate between
grants). Priorities and multicast are retrofitted into the basic structure by adding a filter on the inputs
before it reaches the arbiter; for example, a priority filter zeroes out all requests except those at the
highest-priority level.
    Although, in principle, the unicast schedulers can be designed using a separate chip per port, the
state is sufficiently small to be handled by a single scheduler chip with control wires coming in from
and going out to each of the ports. Also, the multicast algorithm requires a shared multicast pointer per
priority level, which also implies a centralized scheduler. Centralization, however, implies a delay, or
latency, to send requests and decisions from the port line cards to and from the central scheduler.
    To tolerate this latency, the scheduler (Gupta and McKeown, 1999b) works on a pipeline of m cells
(eight in Tiny Tera) from each VOQ and n cells (five in Tiny Tera) from each multicast queue. This in
turn implies that each line card in the Tiny Tera must communicate 3 bits per unicast VOQ denoting the
size of the VOQ, up to a maximum of 8. With 32 outputs and four priority levels, each input port has to
send 384 bits of unicast information. Each line card also communicates the fanout (32 bits per fanout)
for each of five multicast packets in each of four priority levels, leading to 640 bits. The 32 × 1024 total
bits of input information is stored in on-chip SRAM. However, for higher speed, the information about
the heads of each queue (smaller state, for example, only 1 bit per unicast VOQ) is stored in faster but
less dense flip-flops.
    Now consider handling multiple iterations. Note that the request phase occurs only on the first
iteration and needs to be modified only on each iteration by masking off matched inputs. Thus K

352      Chapter 13 Switching



iterations appear to take at least 2K time steps because the grant-and-accept steps of each iteration take
one time step. At first glance, the architecture appears to specify that the grant phase of iteration k + 1
be started after the accept phase of iteration k. This is because one needs to know whether an input port
I has been accepted in iteration k so as to avoid doing a grant for such an input in iteration k + 1.
    What makes partial pipelining possible is a simple observation (Gupta and McKeown, 1999b): if
input I receives any grant in iteration k, then I must accept exactly one and so be unavailable in iteration
k + 1. Thus the implementation specification can be relaxed (P3) to allow the grant phase of iteration
k + 1 to start immediately after the grant phase of iteration k, thus overlapping with the accept phase
of iteration k. To do so, we simply use the OR of all the grants to input I (at the end of iteration k) to
mask out all of I ’s requests (in iteration k + 1).
    This reduces the overall completion time by nearly a factor of two time steps for k iterations, from
2k to k + 1. For example, the Tiny Tera iSLIP implementation (Gupta and McKeown, 1999b) does three
iterations of iSLIP in 51 nanoseconds (roughly OC-192 speeds) using a clock speed of 175 MHz; given
that each clock cycle is roughly 5.7 nanoseconds, iSLIP has roughly nine clock cycles to complete.
Since each grant and accept step takes two clock cycles, the pipelining is crucial for being able to
handle three iterations in nine clock cycles; the naive iteration technique would have taken at least 12
clock cycles.
