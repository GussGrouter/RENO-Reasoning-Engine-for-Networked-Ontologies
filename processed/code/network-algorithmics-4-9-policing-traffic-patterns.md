# Network Algorithmics — 4.9 Policing traffic patterns (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 119
- Slice: from `4.9 Policing traffic patterns` up to next detected section heading

---

4.9 Policing traffic patterns
Some network protocols require that sources never send data faster than a certain rate. Instead of merely
specifying the average rate over long periods of time, the protocol may also specify the maximum
amount of traffic, B, in bits a source can send in any period of T seconds. This does limit the source to
an average rate of B/T bits per second. However, it also limits the “burstiness” of the users’ traffic to
at most one burst of size B every T units of time. For example, choosing a small value of the parameter
T limits the traffic burstiness considerably. Burstiness causes problems for networks because periods
of high traffic and packet loss are followed by idle periods.
    If every source meets its contract (i.e., sends no more than the specified amount in the specified
period), the network can often guarantee performance and ensure that no traffic is dropped and that all
traffic is delivered in timely fashion. Unfortunately, this is like saying that if everyone follows the rules
of the road, traffic will flow smoothly. Most people do follow the rules: some because they feel it is the
right thing to do, and many because they are aware of penalties that they have to pay when caught by
traffic police. Thus policing is an important part of an ordered society.

                                                                    4.9 Policing traffic patterns             93




FIGURE 4.16
The naive use of a single or multiple timers (to check whether a flow sends no more than B every T seconds) does
not catch all violations.


     For the same reason, many designers advocate that the network should periodically police traffic to
look for offenders that do not meet their contracts. Without policing, the offenders can get an unfair
share of network bandwidth.
     Assume that a traffic flow is identified by the source and destination addresses and the traffic type.
Thus each router needs to ensure that a particular traffic flow sends no more than B bits in any period
of T seconds. The simplest solution is for the router to use a single timer that ticks every T seconds
and to count the number of bits sent in each period using a counter per flow. At the end of each period,
if the counter exceeds B, the router has detected a violation.
     Unfortunately, the single timer can police only some periods. For example, assume without
loss of generality that the timer starts at time 0. Then the only periods checked are the periods
[0, T ], [T , 2T ], [2T , 3T ], . . .. This does not ensure that the source flow does not violate its contract
in a period like [T /2, 3T /2], which overlaps the periods that are policed. For example, on the left side
of Fig. 4.16, the flow sends a burst of size B just before the timer ticks at time T and sends a second
burst of size B just after the timer ticks at time T .
     One attempt to fix this problem is for the router to use multiple timers and counters. For example,
as shown on the right of Fig. 4.16, the router could use one timer that starts at 0 and a second timer that
starts at time T /2. Unfortunately, the flow can still violate its contract by sending no more than B in
each policed period but sending more than B in some overlapping period.
     For instance, in the right frame of Fig. 4.16 an offending flow sends a first burst of B at the end
of the first period and a second burst of B at the start of the third period, sending 2B within a period
slightly greater than T /2. Unfortunately, neither of the timers will detect the flow as being a violator.
This leads to the following problem.

Problem
Multiple timers are expensive and do not guarantee that the flow will not violate its traffic contract. It is
easy to see that with even a single timer, the flow can send no more than 2B in any period of T seconds.
One approach is simply to assume that a factor-of-2 violation is not worth the effort to police. However,
suppose that bandwidth is precious on a transcontinental link and that a factor-of-2 violation is serious.
How could a violating flow still be caught using only a single timer?

94        Chapter 4 Principles in action




FIGURE 4.17
Picking a random gap of T seconds between policing intervals allows the router to catch a violating flow with high
probability.



Hint: Consider exploiting a degree of freedom (P13) that has been assumed to be fixed in the naive
solution. Do the policing intervals have to start at fixed intervals? Also consider using P3a.

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
