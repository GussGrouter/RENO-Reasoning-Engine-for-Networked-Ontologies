# network-algorithmics-7-9-obtaining-finer-granularity-timers (chunk 000002)

showed the cost of an interrupt on a 300- or 500-Mhz Pentium was around 4.5 microseconds. Worse,
as processors get faster, there is no indication that interrupt processing times will improve.
     Thus having a more frequent hardware interrupt will result in too much overhead. As the problem is
defined, considering the timer module as a black box leaves us no way out. However, systems thinking
provides a solution to our dilemma by considering Principle P4 again and leveraging off other system
components. Observe that the life of a CPU is chock full of other kinds of transition events that involve
state saving and restoring and changes in locality patterns. Such transition events include system calls
(e.g., a call to a device handler), exceptions (e.g., a page fault), and hardware interrupts (e.g., an interrupt
from the network adaptor).
     If we place a check for expired timers as part of the code for such transition events, the overhead for
state saving and locality changes is already part of the transition event and is not increased significantly
by the timer handler. This is good. Unfortunately, unlike the hardware clock interrupt, the frequency of
transition events is unpredictable. This is bad.
     However, experiments over a wide range of benchmarks in Aron and Druschel (1999) show that the
mean delay between transition events varies from 5 to 30 microseconds, depending on what the CPU is
running, that delays over 100 microseconds occur in only 6% of the cases, and that the maximum delay
never exceeded 1 millisecond.
     The data suggests an interesting use of P3, relaxing system requirements. Instead of providing a
“hard” timer facility that always provides microsecond timers, we provide a “soft” timer (Aron and
Druschel, 1999) facility that often provides 10 microseconds timers. We can also bound the error of the
soft timer facility by adding a hardware clock interrupt every 1 millisecond. Thus soft timers are useful
for applications that can benefit from an expected case (P11) of tens of microseconds and a worst case
of 1 millisecond.
     Fortunately, a large fraction of applications that use timers can benefit from such approximate
timers. Consider failure recovery, for example, fast retransmission. If most retransmissions are fast
except for the occasional retransmission that takes 1 millisecond, failure performance will improve.
Also, consider algorithms where the rate of production of some entity is being controlled. As long as
the algorithm correctness can tolerate variability or jitter in the rate, performance should improve in the
expected case. For example, Aron and Druschel (1999) show how a TCP connection can be rate con-
trolled to send packets roughly every 12 microseconds. The finer rate control decreases the burstiness
of the data, but deviations in the rate do not affect correctness.
     Finally, perhaps the right way to handle microsecond, or even nanosecond, timers is to add hardware
(P5). Such hardware could be in the form of a timer chip that completely handles all timers within the
chip using timing wheels or a d-heap. Thus the chip has an internal hardware clock, and the hardware
clock interrupt is fielded within the chip; the CPU is interrupted only when a timer expires. However,
if timers are frequently canceled, there can be considerable overhead for the CPU to cancel timers by
communicating with the chip.
