# network-algorithmics-7-2-model-and-performance-measures (chunk 000001)

# Network Algorithmics — 7.2 Model and performance measures (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 208
- Slice: from `7.2 Model and performance measures` up to next detected section heading

---

7.2 Model and performance measures
A timer module (Varghese and Lauck, 1987) has four component routines:
STARTTIMER (Interval, RequestId, ExpiryAction): The client calls this routine to start a timer that
     will expire after “Interval” units of time. The client supplies a RequestId that is used to distin-
     guish this timer from other timers the client has outstanding. Finally, the client can specify what
     action must be taken on expiry, for instance, calling a client-specified routine or setting an event
     flag.
STOPTIMER (RequestId): This routine uses its knowledge of the client and RequestId to locate the
     timer and stop it.
PERTICKBOOKKEEPING: Let the granularity of the timer be T units. Then every T units, this routine
     checks whether any outstanding timers have expired; if so, it calls STOPTIMER, which in turn
     calls the next routine.

182      Chapter 7 Maintaining timers

FIGURE 7.1
Timer queue example used to illustrate Scheme 2.

EXPIRYPROCESSING: This routine does the ExpiryAction specified in the STARTTIMER call.
The first two routines are activated on client calls; the last two are invoked on timer ticks. The timer is
often an external hardware clock.
    Two performance measures can be used to choose between algorithms described in the rest of this
chapter. Both are parameterized by n, the average (or worst-case) number of outstanding timers. They
are the space (Space) required for the timer data structures and the latency (Latency), or the time be-
tween the invoking of a routine in the timer module and its completion. Assume that the caller of the
routine blocks until the routine completes. Both the average and worst-case latency are of interest.
