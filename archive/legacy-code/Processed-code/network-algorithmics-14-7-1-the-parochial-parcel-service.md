# Network Algorithmics — 14.7.1 The parochial parcel service (slice)

- Source: raw/code/pdf/Network.Algorithmics.pdf
- Full-text extraction: processed/code/network-algorithmics-full-layout.txt
- Slice start: PDF page 420
- Slice: from `14.7.1 The parochial parcel service` up to next detected section heading

---

14.7.1 The parochial parcel service
To illustrate the issues, let us consider the story of a hypothetical parcel service called the Parochial
Parcel Service, depicted in Fig. 14.7. Two customers, called Jones and Smith, use the parcel service to
send their parcels by truck to the next city.
   In the beginning all parcels were kept in a single queue at the loading dock, as seen in Fig. 14.8.
Unfortunately, it so happened that the loading dock was limited in size. It also happened that during
busy periods Jones would send all his parcels just a little before Smith sent his. The result was that,
when Smith’s parcels arrived during busy periods, they were refused; Smith was asked to retry some
other time.
   To solve this unfairness problem, the Parochial Parcel Service decided to use two queues before the
loading dock, one for Jones and one for Smith. When times were busy, some space was left for Smith’s
queue. The queues were serviced in round-robin order. Unfortunately, even this did not work too well

394       Chapter 14 Scheduling packets




FIGURE 14.7
A hypothetical parcel service.




FIGURE 14.8
A FIFO queue for loading parcels that is, unfortunately, hogged by Jones.


because the evil Jones (see Fig. 14.9) cleverly used packages that were consistently larger than those of
Smith. Since two large packages of Jones could contain seven of Smith’s packages, the net result was
that Jones could get 3.5 times the service of Smith during busy periods. Thus Smith was happier, but
he was still unhappy.
    Another idea that the Parochial Parcel Service briefly toyed with was actually to cut parcels into
slices, such as unit cubes, that take a standard time to service. Then, the company could service a
slice at a time for each customer. They called this slice-by-slice round-robin. When initial field trials
produced bitter customer complaints, the Parochial Parcel Service decided they couldn’t physically cut
packages up into slices. However, they realized they could calculate the time at which a package will

                                                     14.7 Providing bandwidth guarantees           395




FIGURE 14.9
Two queues and round-robin make Smith happier . . . but not completely happy.



leave in an imaginary slice-by-slice system. They could then service packages in the order they would
have left in the imaginary system. Such a system will indeed be fair for any combination of packet
(oops, package) sizes.
    Unfortunately, simulating the imaginary system is like performing a discrete event simulation in
real time. At the very least, this requires keeping the time stamps at which each head package of each
queue will depart and picking the earliest such timestamp to service next; thus the amount of time it
takes for this selection (using priority queues) is logarithmic in the number of queues. This must be
done whenever a package is sent.
    Worse, when a new queue becomes active, potentially all the time stamps have to change. This is
shown in Fig. 14.10. Jones has a package at the head of his queue that is due to depart at time 12; Smith
has a package due to depart at time 8. Now, imagine that Brown introduces a packet. Since Brown’s
package must be scanned once for every three slices scanned in the imaginary slice-by-slice system,
the speed of Smith and Jones has gone down from a speed of one in every two slices to one in every
three slices. This potentially means that the arrival of Brown can cause every time stamp to be updated,
an operation whose complexity is linear in the number of flows.


14.7.2 Deficit round-robin
What was all this stuff about a parcel service about? Clearly, parcels correspond to packets, the par-
cel office to a router, and loading docks to outbound links. More importantly, the seemingly facetious
slice-by-slice round-robin corresponds to a seminal idea, called bit-by-bit round-robin or the DKS (De-
mers, Keshav, and Shenker) scheme (Demers et al., 1989). Simulated bit-by-bit round-robin provides
provably fair bandwidth distribution and some remarkably tight delay bounds; unfortunately, it is hard
to implement at gigabit speeds. A considerable improvement to bit-by-bit round-robin is proposed in
the paper by Stiliadis and Varma (1996b), which shows how to reduce the linear overhead of the DKS
scheme to the purely logarithmic overhead of sorting. Sorting can be done at high speeds with hardware
multiway heaps; however, it is still more complex than deficit round-robin for bandwidth guarantees.

396       Chapter 14 Scheduling packets




FIGURE 14.10
Brown’s entry causes the time stamp of Jones and Smith to change. In general, when a new flow becomes active, the
overhead is linear in the number of flows.


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

the packet of size 750 and the packet of size 20. Assume that no more packets arrive to F 1’s queue than
are shown in Fig. 14.12. Thus since the F 1 queue is empty, the algorithm skips to F 2.
    Curiously, when skipping to F 2, the algorithm does not leave behind the deficit of 800 − 750 −
20 = 30 in F 1’s queue. Instead, it zeroes out F 1’s deficit counter. Thus the deficit counter is a somewhat
curious bank account that is zeroed unless the account holder can prove a “need” in terms of a nonempty
queue. Perhaps this is analogous to a welfare account.
