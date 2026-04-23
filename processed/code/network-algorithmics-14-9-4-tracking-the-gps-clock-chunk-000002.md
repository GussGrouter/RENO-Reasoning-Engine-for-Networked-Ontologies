# network-algorithmics-14-9-4-tracking-the-gps-clock (chunk 000002)

However, precomputing all (expected) real finish times here is arguably a “self-inflicted wound.”
Rather, it appears that we need only to precompute the earliest one among them for tracking the GPS
clock (P2b). For instance, in the previous example, when p3,1 arrives at real time 23, we need only
to precompute V −1 (20) = 35, the real time corresponding to the earliest among the three GPS virtual
finish times just described (f1,1 = 20, f2,1 = 21, and f3,1 = 22). Then, it is not until this real time
t = 35 that the expected real finish time of the next packet (corresponding to f2,1 = 21) needs to be
precomputed as V −1 (21) = 38. Finally, it is not until t = 38 that the expected real finish time of the last
packet (corresponding to f3,1 = 22) needs to be precomputed as V −1 (22) = 40.
    Indeed, in an idealized systems implementation, the scheduler (process) can be put to sleep with
a timer (see Chapter 7) set to wake it up at the next earliest expected GPS real finish time. We illus-
trate such a timer-based implementation using the same instance. After some “cleanup” (defined next)
computations (to arrive at V −1 (20) = 35 among others) at t = 23, the scheduler goes to sleep, and a
timer is set to wake it up at t = 35 as calculated. Then, at t = 35, the scheduler that is awoken by the
timer performs the following processing: it changes the total weight of the backlogged flows from 4
to 3 (as F 1 is no longer backlogged after t = 35), computes the next real time to wake the scheduler
up (which is V −1 (21) = 38 as just calculated), and sets the next wake-up time to t = 38. We refer to
this scheduled operation of adjusting the total weight and scheduling the next wake-up time as cleanup,
since each such operation corresponds to the necessary maintenance associated with the departure of a
previously backlogged flow.
    Once the scheduler wakes up again at real time t = 38, the cleanup operation needs to change
the total weight of backlogged flows from 3 to 2 (as F2 becomes unbacklogged afterward) and sets
the wake-up timer to V −1 (22) = 40. This time, however, the scheduler does not wake up at real time
t = 40 as scheduled. Instead, at time t = 39, the scheduler gets a “rude awakening” from the arrival of
packet p3,2 . When this happens, the scheduler computes V (39) = 21 + (39 − 38)/2 = 21.5, the total
weight is adjusted to 3 (as F2 becomes backlogged again), and the next wake-up time is changed to
t = 39 + (22 − 21.5) ∗ 3 = 40.5 (from t = 40 previously). Note that there is a tiny gap between packets
p2,1 and p2,2 . This is because p2,1 finishes service under GPS at real time t = 38 and p2,2 won’t arrive
until real time t = 39.
    With this idealized timer-based implementation, the time complexity of each cleanup operation,
including that of computing the next (real) expected wakeup time (which could change due to “rude
awakening”) and adjusting the total weight of backlogged flows, is O(1), as shown in the previous
instance. In addition, we can maintain the GPS virtual finish times of the last packets of backlogged
flows in a balanced priority queue, such as a heap or a balanced binary tree, so that the next earliest
expected GPS virtual finish time can be obtained (by calling the ExtractMin() method) in O(log n)
time. For example, in the previous instance, at time 23+ , the priority queue contains three nodes keyed
by virtual finish times 20, 21, and 22, respectively. Therefore the total computational complexity of
tracking the GPS clock is O(log n) per packet in theory.
    However, for this O(1) cleanup algorithm to work in practice, its operation has to closely follow the
progress of (current) time in the following sense: when the current time is t, the cleanup operations for
all past events must be finished before t since otherwise we cannot compute V (·) in O(1) in the event
of a “rude awakening” (such as that at real time t = 39 in the previous example). However, it could
happen that a large number (say O(n)) of such events that require cleanups could happen within a tiny
time interval (see an example of that in Zhao and Xu (2004)). In this case we have to perform O(n)
cleanup operations, with a total time complexity of O(n), in a short time. Hence, the worse-case time
