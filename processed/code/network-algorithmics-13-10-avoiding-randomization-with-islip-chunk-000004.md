# network-algorithmics-13-10-avoiding-randomization-with-islip (chunk 000004)

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
