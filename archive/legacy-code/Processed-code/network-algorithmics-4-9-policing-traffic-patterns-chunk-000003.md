# network-algorithmics-4-9-policing-traffic-patterns (chunk 000003)

Solution
As suggested in the hints, the policing intervals need not be fixed. Thus there can be an arbitrary gap
between policing intervals. How should the gap be picked? Since a violating flow can pick its violating
period of T to start at any instant, a simple idea is to invoke P3a to yield the following idea (Fig. 4.17).
    The router uses a single timer of T units and a single counter, as before. A policing interval ends
with a timer tick; if the counter is greater than B, a violation is detected. Then a flag is set indicating
that the timer is now used only for inserting a random gap. Then the timer is restarted for a random
time interval between 0 and T . When the timer ticks, the flag is cleared and the counter is initialized,
and the timer is reset for a period of T to start policing again.

Exercises

• Suppose the counter is initialized and maintained during the gap period as well as during policing
  periods. Can the router make any valid inference during such a period, even if the gap period is less
  than T units?
• (Open Problem): Suppose the flow is adversarial. What is a good strategy for the flow to consistently
  violate the contract by as high a margin as possible and still elude the randomized detector described
  earlier? The flow strategy can be randomized as well. A good answer should be supported by a
  probabilistic analysis.
