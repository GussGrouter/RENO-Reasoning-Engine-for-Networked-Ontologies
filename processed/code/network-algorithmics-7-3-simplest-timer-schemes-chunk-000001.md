# network-algorithmics-7-3-simplest-timer-schemes (chunk 000001)

# Network Algorithmics — 7.3 Simplest timer schemes (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 209
- Slice: from `7.3 Simplest timer schemes` up to next detected section heading

---

7.3 Simplest timer schemes
The two simplest schemes for timer implementation are, in fact, commonly used. In the first scheme
STARTTIMER finds a memory location and sets that location to the specified timer interval. Every
T units, PERTICKBOOKKEEPING will decrement each outstanding timer; if any timer becomes zero,
EXPIRYPROCESSING is called.
    This scheme is extremely fast for all but PERTICKBOOKKEEPING. It also uses one record per out-
standing timer, the minimum space possible. It is appropriate if there are only a few outstanding timers,
if most timers are stopped within a few ticks of the clock, and if PERTICKBOOKKEEPING is done with
suitable performance by special-purpose hardware.
    Note that instead of doing a Decrement, we can store the absolute time at which timers expire
and do a Compare. This option is valid for all timer schemes we describe; the choice between them
will depend on the size of the time-of-day field, the cost of each instruction, and the hardware on the
machine implementing these algorithms. In this chapter we will use the Decrement option, except when
describing Scheme 2.
    In a second simple scheme, used in older versions of UNIX, PERTICKBOOKKEEPING latency is
reduced at the expense of STARTTIMER performance. Timers are stored in an ordered list. Unlike
Scheme 1, we will store the absolute time at which the timer expires, not the interval before expiry.
The timer that is due to expire at the earliest time is stored at the head of the list. Subsequent timers are
stored in increasing order, as shown in Fig. 7.1. In Fig. 7.1 the lowest timer is due to expire at absolute
time 10 hours, 23 minutes, and 12 seconds.
    Because the list is sorted, PERTICKBOOKKEEPING need only increment the current clock time and
compare it with the head of the list. If they are equal or if the time of day is greater, it deletes that list
element and calls EXPIRYPROCESSING. It continues to delete elements at the head of the list until the
expiry time of the head of the list is strictly less than the time of day. STARTTIMER searches the list to

7.4 Timing wheels           183
