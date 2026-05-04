# network-algorithmics-7-4-timing-wheels-the-design-of-the-first-scheme-follows-a-common-problem-so (chunk 000002)

The system is already doing some work per tick to increment time. Thus what matters when figuring
out the cost of the algorithm is only the additional expense caused by the algorithm, not the cost taken
in isolation as is typically measured in algorithms classes. Note that this assumption would be false if
the system did not do some work on every clock tick and, instead, relied on a piece of hardware to keep
the time of day. What matters, unlike the sort, is not the total amount of work to sort N elements, but
the average (and worst-case) part of the work that needs to be done per timer tick.
    Still, memory is finite: It is difficult to justify 232 words of memory to implement 32-bit timers. So
how would you generalize this idea to larger timer values? If you haven’t seen it before, try to come up
with your own ideas before reading further.
    One naive solution is to implement timers within some range using this scheme and the allowed
memory. Timers greater than this value are implemented using, say, Scheme 2. Alternatively, this
scheme can be extended in two ways to allow larger values of the timer interval with modest amounts
of memory. The two techniques are motivated by two algorithmic techniques (P15): hashing and radix
sort.
