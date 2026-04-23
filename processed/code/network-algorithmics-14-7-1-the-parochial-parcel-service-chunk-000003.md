# network-algorithmics-14-7-1-the-parochial-parcel-service (chunk 000003)

Now, while bit-by-bit round-robin provides both bandwidth guarantees and delay bounds, our first
observation is that many applications can benefit from just bandwidth guarantees. Thus an interesting
question is whether there is a simpler algorithm that can merely provide bandwidth guarantees. We
are, of course, relaxing system requirements to pave the way for a more efficient implementation, as
suggested by P3.
    If we are only interested in bandwidth guarantees and would like a constant-time algorithm, a natural
point of departure is round-robin. So we ask ourselves: can we retain the efficiency of round-robin and
yet add a little state to correct for the unfairness of examples such as Fig. 14.9?
    A banking analogy motivates the solution. Each flow is given a quantum, which is like a periodic
salary that gets credited to the flow’s bank account on every round-robin cycle. As with most bank
accounts, a flow cannot spend (i.e., send packets of the corresponding size) more than is contained in its
account; the algorithm does not allow bank accounts to be overdrawn. However, perfectly naturally, the
balance remains in the account for possible spending in the next period. Thus any possible unfairness
in a round is compensated for in subsequent rounds, leading to long-term fairness.
    More precisely, for each flow i, the algorithm keeps a quantum size Qi and a deficit counter Di . The
larger the quantum size assigned to a flow, the larger the share of the bandwidth it receives. On each
round-robin scan, the algorithm will service as many packets as possible for flow i with a size of less
than Qi + Di . If packets remain in flow i’s queue, the algorithm stores the “deficit,” or remainder, in Di
for the next opportunity. It is easy to prove that the algorithm is fair in the long term for any combination
of packet sizes and that it takes only a few more instructions to implement than round-robin.
    Consider the example illustrated in Figs. 14.11 and 14.12. We assume that the quantum size of all
flows is 500 and that there are four flows. In Fig. 14.11 the round-robin pointer points to the queue of
F 1; the algorithm adds the quantum size to the deficit counter of F 1, which is now at 500. Thus F 1 has
sufficient funds to send the packet at the head of its queue of size 200 but not the second packet of size
750. Thus the remainder (300) is left in F 1’s deficit account, and the algorithm skips to F 2, leaving the
picture shown in Fig. 14.12.
    Thus in the second round the algorithm will send the packet at the head of F 2’s queue (leaving a
deficit of 0), the packet at the head of F 3’s queue (leaving a deficit of 400), and the packet at the head
of F 4’s queue (leaving a deficit of 320). It then returns to F 1’s queue. F 1’s deficit counter now goes up
to 800; this reflects a past account balance of 300 plus a fresh deposit of 500. The algorithm then sends

14.7 Providing bandwidth guarantees                        397

FIGURE 14.11
Deficit round-robin: at the start, all the deficit variables are initialized to zero. The round-robin pointer points to the
top of the active list. When the first queue is serviced, the quantum value of 500 is added to the deficit value. The
remainder after servicing the queue is left in the deficit variable.
