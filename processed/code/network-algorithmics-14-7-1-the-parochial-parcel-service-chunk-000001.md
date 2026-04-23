# network-algorithmics-14-7-1-the-parochial-parcel-service (chunk 000001)

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
