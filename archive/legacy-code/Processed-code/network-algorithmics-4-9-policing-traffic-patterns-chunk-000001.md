# network-algorithmics-4-9-policing-traffic-patterns (chunk 000001)

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
