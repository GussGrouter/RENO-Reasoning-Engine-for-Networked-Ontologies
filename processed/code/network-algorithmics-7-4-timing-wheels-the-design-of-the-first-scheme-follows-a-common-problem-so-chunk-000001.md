# network-algorithmics-7-4-timing-wheels-the-design-of-the-first-scheme-follows-a-common-problem-so (chunk 000001)

# Network Algorithmics — 7.4 Timing wheels The design of the first scheme follows a common problem-solving paradigm: (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 210
- Slice: from `7.4 Timing wheels The design of the first scheme follows a common problem-solving paradigm:` up to next detected section heading

---

7.4 Timing wheels
The design of the first scheme follows a common problem-solving paradigm:
First solve a simpler problem, and then use the insight to solve the more complex problem.
    The simpler problem we tackle first is as follows. Suppose timers are all set for some small interval,
say, MAXINTERVAL, and let the granularity of the timer be 1 unit. This suggests the use of P4, bucket-
sorting techniques, instead of the sorting techniques suggested by Schemes 2 and 3. However, bucket
sorting is really used for static sorting of a set of numbers. Here, new numbers keep being added and
deleted, and we still want to maintain order. (In technical algorithmic terms the timer data structure must
implement a priority queue that allows the operations of addition, deletion, and finding the smallest
element.) What is the bucket-sorting equivalent of a priority queue?

184      Chapter 7 Maintaining timers

FIGURE 7.2
Array of lists used by Scheme 4 for timer intervals up to MAXINTERVAL.

Given this motivation, it is not hard to have the following picture (shown in Fig. 7.2) float into the
reader’s mind. Imagine that current time is represented by a pointer to an element in a circular array
with dimensions [0, MAXINTERVAL − 1]. On every timer tick (for per-tick bookkeeping), we simply
increment the pointer by 1 mod the size of the array.
    To set a timer at j units past current time, we index (Fig. 7.2) into Element i + j mod
MAXINTERVAL and put the timer at the head of a list of timers that will expire at a time =
CurrentT ime + j units. Each tick, we increment the current timer pointer (modMAXINTERVAL) and
check the array element being pointed to. If the element is 0 (no list of timers waiting to expire), then
no more work is done on that timer tick. But if it is nonzero, then we do EXPIRYPROCESSING on all
timers that are stored in that list. Thus the latency for STARTTIMER is O(1); PERTICKBOOKKEEPING
is O(1) except when timers expire, but this is the best possible. If the timer lists are doubly linked and,
as before, we store a pointer to each timer record, then the latency of STOPTIMER is also O(1).
    We can describe this array somewhat more picturesquely as a timing wheel, where the wheel turns
one array element every timer unit. For a secretary, this is similar to a tickler file. For sorting experts,
this is similar to a bucket sort that trades off memory for processing. However, since the timers change
value every time instant, intervals are entered as offsets from the current time pointer. It is sufficient if
the current time pointer increases every time instant.
    A bucket sort sorts N elements in O(M) time using M buckets, since all buckets have to be exam-
ined. This is inefficient for large M > N . In timer algorithms, however, the crucial observation is that
some entity needs to do O(1) work per tick to update the current time; it costs only a few more instruc-
tions for the same entity to step through an empty bucket. This is a nice example of using Principles P4
(leveraging system components) and P2c (expense sharing).

7.5 Hashed wheels            185
