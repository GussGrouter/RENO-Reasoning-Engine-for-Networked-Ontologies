# network-algorithmics-4-9-policing-traffic-patterns (chunk 000002)

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
